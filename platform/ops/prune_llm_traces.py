"""Prune old LLM trace rows (retention policy)."""

from __future__ import annotations

import logging
import os
from datetime import datetime, timedelta, timezone

logger = logging.getLogger(__name__)

DEFAULT_RETENTION_DAYS = int(os.environ.get("LLM_TRACE_RETENTION_DAYS", "14"))


def prune_llm_traces(retention_days: int | None = None) -> int:
    """Delete llm_traces older than retention_days. Returns rows deleted."""
    days = retention_days if retention_days is not None else DEFAULT_RETENTION_DAYS
    days = max(1, min(days, 365))
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()

    try:
        from ..db.migrations import get_db

        db = get_db()
        cur = db.execute(
            "DELETE FROM llm_traces WHERE created_at < ?",
            (cutoff,),
        )
        deleted = cur.rowcount if cur.rowcount is not None else 0
        db.commit()
        db.close()
        if deleted:
            logger.info("Pruned %d llm_traces older than %s", deleted, cutoff)
        return deleted
    except Exception as exc:
        logger.warning("LLM trace prune skipped: %s", exc)
        return 0
