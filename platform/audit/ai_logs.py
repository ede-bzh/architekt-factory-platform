"""Append-only AI audit log — one row per LLM trace."""

from __future__ import annotations

import json
import logging
import uuid
from typing import Any, Optional

from ..db.migrations import get_db

logger = logging.getLogger(__name__)


class AIAuditLogger:
    """SQLite-backed append-only audit log (INSERT only)."""

    def __init__(self):
        self._ensure_table()

    def _ensure_table(self):
        conn = get_db()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ai_audit_logs (
                id TEXT PRIMARY KEY,
                event_type TEXT NOT NULL DEFAULT 'llm_call',
                provider TEXT DEFAULT '',
                model TEXT DEFAULT '',
                agent_id TEXT DEFAULT '',
                session_id TEXT DEFAULT '',
                mission_id TEXT DEFAULT '',
                tokens_in INTEGER DEFAULT 0,
                tokens_out INTEGER DEFAULT 0,
                cost_usd REAL DEFAULT 0.0,
                status TEXT DEFAULT 'ok',
                payload_json TEXT DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_ai_audit_mission
            ON ai_audit_logs(mission_id, created_at)
        """)
        conn.commit()
        conn.close()

    def append(
        self,
        event_type: str = "llm_call",
        provider: str = "",
        model: str = "",
        agent_id: str = "",
        session_id: str = "",
        mission_id: str = "",
        tokens_in: int = 0,
        tokens_out: int = 0,
        cost_usd: float = 0.0,
        status: str = "ok",
        payload: Optional[dict[str, Any]] = None,
    ) -> str:
        """Append one audit record. Returns log id."""
        log_id = uuid.uuid4().hex[:16]
        conn = get_db()
        try:
            conn.execute(
                """
                INSERT INTO ai_audit_logs
                (id, event_type, provider, model, agent_id, session_id, mission_id,
                 tokens_in, tokens_out, cost_usd, status, payload_json)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
                (
                    log_id,
                    event_type,
                    provider,
                    model,
                    agent_id,
                    session_id,
                    mission_id,
                    tokens_in,
                    tokens_out,
                    cost_usd,
                    status,
                    json.dumps(payload or {}, ensure_ascii=False)[:4000],
                ),
            )
            conn.commit()
        except Exception as e:
            logger.warning("ai_audit_logs append failed: %s", e)
        finally:
            conn.close()
        return log_id

    def recent(self, limit: int = 50, mission_id: str = "") -> list[dict[str, Any]]:
        conn = get_db()
        try:
            if mission_id:
                rows = conn.execute(
                    """
                    SELECT * FROM ai_audit_logs
                    WHERE mission_id = ?
                    ORDER BY created_at DESC LIMIT ?
                """,
                    (mission_id, limit),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM ai_audit_logs ORDER BY created_at DESC LIMIT ?",
                    (limit,),
                ).fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()


_logger: Optional[AIAuditLogger] = None


def get_ai_logger() -> AIAuditLogger:
    global _logger
    if _logger is None:
        _logger = AIAuditLogger()
    return _logger


def append_ai_log(**kwargs) -> str:
    return get_ai_logger().append(**kwargs)
