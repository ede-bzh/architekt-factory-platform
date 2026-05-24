"""DB-backed API rate limiting (SQLite + PostgreSQL via get_db)."""

from __future__ import annotations

import time

from ..db.migrations import get_db


def check_rate_limit(
    client_key: str,
    max_requests: int,
    window_seconds: float,
) -> bool:
    """Record a hit and return True if under limit, False if exceeded."""
    now = time.time()
    cutoff = now - window_seconds
    db = get_db()
    try:
        row = db.execute(
            "SELECT COUNT(*) FROM rate_limit_hits WHERE client_key = ? AND ts > ?",
            (client_key, cutoff),
        ).fetchone()
        count = row[0] if row else 0
        if count >= max_requests:
            return False
        db.execute(
            "INSERT INTO rate_limit_hits (client_key, ts) VALUES (?, ?)",
            (client_key, now),
        )
        db.execute("DELETE FROM rate_limit_hits WHERE ts < ?", (cutoff,))
        db.commit()
        return True
    finally:
        db.close()
