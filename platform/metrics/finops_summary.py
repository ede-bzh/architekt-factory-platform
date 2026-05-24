"""FinOps summary — margin vs revenue target for studio missions."""

from __future__ import annotations

import os
from typing import Any

from ..db.migrations import get_db


def _margin_target_pct() -> float:
    try:
        return float(os.environ.get("PLATFORM_FINOPS_MARGIN_TARGET_PCT", "50"))
    except ValueError:
        return 50.0


def _default_revenue_usd() -> float:
    try:
        return float(os.environ.get("PLATFORM_FINOPS_DEFAULT_REVENUE_USD", "5000"))
    except ValueError:
        return 5000.0


def mission_revenue_usd(mission_id: str) -> float:
    """Revenue estimate: mission config or env default."""
    if not mission_id:
        return _default_revenue_usd()
    db = get_db()
    try:
        row = db.execute(
            "SELECT config_json FROM missions WHERE id = ?", (mission_id,)
        ).fetchone()
        if raw_cfg:
            import json

            cfg = json.loads(row["config_json"]) if isinstance(row["config_json"], str) else {}
            raw = (cfg.get("constraints") or {}).get("revenue_usd")
            if raw is not None:
                return float(raw)
    except Exception:
        pass
    finally:
        db.close()
    return _default_revenue_usd()


def compute_margin(cost_usd: float, revenue_usd: float) -> dict[str, Any]:
    """Margin % = (revenue - cost) / revenue * 100."""
    revenue = max(revenue_usd, 0.01)
    margin_usd = revenue - cost_usd
    margin_pct = round((margin_usd / revenue) * 100, 2)
    target = _margin_target_pct()
    return {
        "revenue_usd": round(revenue, 2),
        "cost_usd": round(cost_usd, 6),
        "margin_usd": round(margin_usd, 2),
        "margin_pct": margin_pct,
        "target_margin_pct": target,
        "below_target": margin_pct < target,
    }


def global_summary() -> dict[str, Any]:
    """Platform-wide LLM cost and margin vs default revenue."""
    db = get_db()
    try:
        total_cost = float(
            db.execute(
                "SELECT COALESCE(SUM(cost_usd), 0) FROM llm_traces"
            ).fetchone()[0]
            or 0
        )
        total_calls = int(
            db.execute("SELECT COUNT(*) FROM llm_traces").fetchone()[0] or 0
        )
    finally:
        db.close()
    revenue = _default_revenue_usd()
    margin = compute_margin(total_cost, revenue)
    alerts = []
    if margin["below_target"]:
        alerts.append(
            {
                "level": "warning",
                "code": "margin_below_target",
                "message": (
                    f"Marge {margin['margin_pct']}% sous l'objectif "
                    f"{margin['target_margin_pct']}%"
                ),
            }
        )
    return {
        "total_calls": total_calls,
        "alerts": alerts,
        **margin,
    }


def missions_summary(limit: int = 20) -> list[dict[str, Any]]:
    """Per-mission cost + margin; flag missions below margin target."""
    db = get_db()
    target = _margin_target_pct()
    try:
        rows = db.execute(
            """
            SELECT mission_id,
                   COUNT(*) AS calls,
                   COALESCE(SUM(cost_usd), 0) AS cost_usd
            FROM llm_traces
            WHERE mission_id != ''
            GROUP BY mission_id
            ORDER BY cost_usd DESC
            LIMIT ?
        """,
            (limit,),
        ).fetchall()
        mission_ids = [r["mission_id"] for r in rows]
        names: dict[str, str] = {}
        if mission_ids:
            ph = ",".join("?" * len(mission_ids))
            for r in db.execute(
                f"SELECT id, name FROM missions WHERE id IN ({ph})", mission_ids
            ).fetchall():
                names[r["id"]] = r["name"]
        out = []
        for r in rows:
            mid = r["mission_id"]
            cost = float(r["cost_usd"] or 0)
            rev = mission_revenue_usd(mid)
            m = compute_margin(cost, rev)
            out.append(
                {
                    "mission_id": mid,
                    "mission_name": names.get(mid, mid),
                    "calls": r["calls"],
                    "cost_usd": cost,
                    "revenue_usd": m["revenue_usd"],
                    "margin_pct": m["margin_pct"],
                    "margin_usd": m["margin_usd"],
                    "below_target": m["below_target"],
                    "alert": m["below_target"],
                }
            )
        return out
    finally:
        db.close()


def margin_alerts() -> list[dict[str, Any]]:
    """All active margin alerts (global + per mission)."""
    alerts: list[dict[str, Any]] = []
    g = global_summary()
    alerts.extend(g.get("alerts", []))
    for m in missions_summary():
        if m.get("below_target"):
            alerts.append(
                {
                    "level": "warning",
                    "code": "mission_margin_low",
                    "mission_id": m["mission_id"],
                    "message": (
                        f"Mission {m['mission_name']}: marge {m['margin_pct']}% "
                        f"< objectif {_margin_target_pct()}%"
                    ),
                }
            )
    return alerts
