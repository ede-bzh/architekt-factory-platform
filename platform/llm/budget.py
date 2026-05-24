"""LLM mission budget — auto-pause mission runs at 100% of configured budget."""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone

from ..db.migrations import get_db

logger = logging.getLogger(__name__)


class LLMBudgetExceededError(RuntimeError):
    """Raised when LLM calls are blocked because the mission budget was exceeded."""


def session_cost_usd(session_id: str) -> float:
    """Return total LLM cost (USD) for a ceremony session from llm_traces."""
    if not session_id:
        return 0.0
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT COALESCE(SUM(cost_usd), 0) FROM llm_traces WHERE session_id = ?",
            (session_id,),
        ).fetchone()
        return float(row[0] if row else 0.0)
    finally:
        conn.close()


def mission_cost_usd(mission_id: str) -> float:
    """Return total LLM cost (USD) aggregated by mission_id in llm_traces."""
    if not mission_id:
        return 0.0
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT COALESCE(SUM(cost_usd), 0) FROM llm_traces WHERE mission_id = ?",
            (mission_id,),
        ).fetchone()
        return float(row[0] if row else 0.0)
    finally:
        conn.close()


def get_llm_budget_usd(mission_id: str) -> float:
    """Mission budget from constraints.llm_budget_usd or PLATFORM_LLM_MISSION_BUDGET_USD."""
    budget = 0.0
    if mission_id:
        conn = get_db()
        try:
            row = conn.execute(
                "SELECT config_json FROM missions WHERE id = ?", (mission_id,)
            ).fetchone()
            if row and row["config_json"]:
                cfg = json.loads(row["config_json"] or "{}")
                raw = (cfg.get("constraints") or {}).get("llm_budget_usd")
                if raw is not None:
                    budget = float(raw)
        finally:
            conn.close()
    if budget <= 0:
        env_val = os.environ.get("PLATFORM_LLM_MISSION_BUDGET_USD", "").strip()
        if env_val:
            try:
                budget = float(env_val)
            except ValueError:
                pass
    return budget


def _resolve_mission_id(session_id: str, mission_id: str) -> str:
    if mission_id:
        return mission_id
    if not session_id:
        return ""
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT session_id FROM mission_runs WHERE id = ? OR session_id = ? LIMIT 1",
            (session_id, session_id),
        ).fetchone()
        if row and row["session_id"]:
            return row["session_id"]
    finally:
        conn.close()
    return session_id


def mission_has_budget_exceeded(mission_id: str) -> bool:
    """True if mission config marks llm_budget_exceeded."""
    if not mission_id:
        return False
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT config_json FROM missions WHERE id = ?", (mission_id,)
        ).fetchone()
        if not row:
            return False
        cfg = json.loads(row["config_json"] or "{}")
        return bool(cfg.get("llm_budget_exceeded"))
    finally:
        conn.close()


def is_llm_budget_blocked(session_id: str = "", mission_id: str = "") -> bool:
    """Pre-call guard: block LLM if mission budget was exceeded."""
    mid = _resolve_mission_id(session_id, mission_id)
    if not mid:
        return False
    if mission_has_budget_exceeded(mid):
        return True
    conn = get_db()
    try:
        row = conn.execute(
            """
            SELECT 1 FROM mission_runs mr
            JOIN missions m ON m.id = mr.session_id
            WHERE mr.session_id = ?
              AND mr.status = 'paused'
              AND m.config_json LIKE '%llm_budget_exceeded%'
            LIMIT 1
            """,
            (mid,),
        ).fetchone()
        return row is not None
    finally:
        conn.close()


def _pause_mission_for_budget(mission_id: str, cost: float, budget: float) -> None:
    """Pause running mission_runs and set llm_budget_exceeded on mission config."""
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT config_json FROM missions WHERE id = ?", (mission_id,)
        ).fetchone()
        if not row:
            return
        cfg = json.loads(row["config_json"] or "{}")
        cfg["llm_budget_exceeded"] = True
        cfg["llm_budget_spent_usd"] = round(cost, 4)
        cfg["llm_budget_limit_usd"] = round(budget, 4)
        cfg["llm_budget_paused_at"] = datetime.now(timezone.utc).isoformat()
        conn.execute(
            "UPDATE missions SET config_json = ? WHERE id = ?",
            (json.dumps(cfg, ensure_ascii=False), mission_id),
        )
        conn.execute(
            """
            UPDATE mission_runs SET status = 'paused', updated_at = datetime('now')
            WHERE session_id = ? AND status IN ('running', 'pending')
            """,
            (mission_id,),
        )
        conn.commit()
        logger.warning(
            "LLM budget exceeded for mission %s: $%.4f / $%.4f — auto-paused",
            mission_id,
            cost,
            budget,
        )
    finally:
        conn.close()


def check_and_pause_if_over_budget(session_id: str, mission_id: str) -> bool:
    """
    If session/mission LLM cost >= budget, pause mission runs and set flag.
    Returns True if budget was exceeded (and pause was applied).
    """
    mid = _resolve_mission_id(session_id, mission_id)
    if not mid:
        return False

    budget = get_llm_budget_usd(mid)
    if budget <= 0:
        return False

    if mission_has_budget_exceeded(mid):
        return True

    cost = mission_cost_usd(mid)
    if session_id and session_id != mid:
        cost = max(cost, session_cost_usd(session_id))
    elif session_id and not mission_id:
        cost = session_cost_usd(session_id)

    if cost < budget:
        return False

    _pause_mission_for_budget(mid, cost, budget)
    return True
