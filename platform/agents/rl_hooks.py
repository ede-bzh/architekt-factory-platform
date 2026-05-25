"""Shared RL pattern-adaptation hooks for orchestrator and pattern engine."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)

_RL_ACTION_TO_PATTERN = {
    "switch_parallel": "parallel",
    "switch_sequential": "sequential",
    "switch_hierarchical": "hierarchical",
    "switch_debate": "debate",
}


def _mission_rl_metrics(epic_id: str) -> tuple[float, float]:
    """Return (rejection_rate, quality_score) from agent_scores for an epic."""
    rejection_rate = 0.0
    quality_score = 0.0
    try:
        from ..db.migrations import get_db

        db = get_db()
        row = db.execute(
            "SELECT rejected, iterations, quality_score FROM agent_scores"
            " WHERE epic_id=? ORDER BY iterations DESC LIMIT 1",
            (epic_id,),
        ).fetchone()
        db.close()
        if row and row["iterations"] > 0:
            rejection_rate = row["rejected"] / max(1, row["iterations"])
            quality_score = float(row["quality_score"] or 0.0)
    except Exception as e:
        logger.debug("RL metrics lookup skipped: %s", e)
    return rejection_rate, quality_score


def rl_recommend_for_phase(
    mission_id: str,
    phase_id: str,
    workflow_id: str,
    phase_idx: int,
    phase_count: int = 8,
    epic_id: str | None = None,
) -> tuple[dict[str, Any], str | None]:
    """
    Call RL policy for a mission phase.

    Returns (recommendation dict, new_pattern_type or None if keep / low confidence).
    """
    from .rl_policy import get_rl_policy

    rej, qual = _mission_rl_metrics(epic_id or mission_id)
    state = {
        "workflow_id": workflow_id or "",
        "phase_idx": phase_idx,
        "phase_count": phase_count,
        "rejection_pct": rej,
        "quality_score": qual,
    }
    rec = get_rl_policy().recommend(mission_id, phase_id, state)
    if not rec.get("fired") or rec.get("action") == "keep":
        return rec, None
    new_type = _RL_ACTION_TO_PATTERN.get(rec.get("action", ""))
    return rec, new_type


def apply_rl_pattern_override(
    current_pattern_type: str,
    mission_id: str,
    phase_id: str,
    workflow_id: str,
    phase_idx: int,
    phase_count: int = 8,
) -> str:
    """Return pattern type after optional RL override (logs when switching)."""
    rec, new_type = rl_recommend_for_phase(
        mission_id,
        phase_id,
        workflow_id,
        phase_idx,
        phase_count=phase_count,
    )
    if new_type and new_type != current_pattern_type:
        logger.warning(
            "RL hook: phase=%s pattern %s→%s (conf=%.2f action=%s)",
            phase_id,
            current_pattern_type,
            new_type,
            rec.get("confidence", 0),
            rec.get("action"),
        )
        return new_type
    return current_pattern_type
