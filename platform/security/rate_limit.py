"""PG-backed rate limiting for /api/* mutation endpoints."""

from __future__ import annotations

import hashlib
import logging
import os
import time
from collections import defaultdict

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)

MUTATION_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})


def is_api_mutation(request: Request) -> bool:
    """True when the request is a state-changing /api/* call."""
    return (
        request.url.path.startswith("/api/")
        and request.method.upper() in MUTATION_METHODS
    )


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limiter with PG persistence (survives restart) and in-memory fast path."""

    def __init__(self, app, max_requests: int | None = None, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests or int(os.environ.get("API_RATE_LIMIT", "60"))
        self.window = window_seconds
        self._hits: dict[str, list[float]] = defaultdict(list)
        self._pg_synced = False

    def _should_rate_limit(self, request: Request) -> bool:
        if os.environ.get("PLATFORM_ENV") == "test":
            return False
        return is_api_mutation(request)

    def _client_key(self, request: Request) -> str:
        client_ip = request.client.host if request.client else "unknown"
        token = request.headers.get("Authorization", "")[:20]
        if token:
            return f"{client_ip}:{hashlib.md5(token.encode()).hexdigest()[:8]}"
        return client_ip

    def _ensure_pg_table(self):
        """Create rate_limit_hits table if using PG."""
        if self._pg_synced:
            return
        try:
            from ..db.adapter import get_connection, is_postgresql

            if is_postgresql():
                db = get_connection()
                db.execute(
                    """CREATE TABLE IF NOT EXISTS rate_limit_hits (
                    id SERIAL PRIMARY KEY,
                    client_key TEXT NOT NULL,
                    ts DOUBLE PRECISION NOT NULL
                )"""
                )
                db.execute(
                    "CREATE INDEX IF NOT EXISTS idx_rl_key_ts "
                    "ON rate_limit_hits(client_key, ts)"
                )
                db.commit()
                db.close()
        except Exception:
            logger.debug("rate_limit_hits table setup skipped", exc_info=True)
        self._pg_synced = True

    def _pg_hit_count(self, client_key: str, cutoff: float) -> int:
        try:
            from ..db.adapter import get_connection, is_postgresql

            if not is_postgresql():
                return 0
            db = get_connection()
            row = db.execute(
                "SELECT COUNT(*) AS c FROM rate_limit_hits "
                "WHERE client_key = ? AND ts > ?",
                (client_key, cutoff),
            ).fetchone()
            db.close()
            if row is None:
                return 0
            return int(row["c"] if isinstance(row, dict) else row[0])
        except Exception:
            logger.debug("rate limit PG count failed", exc_info=True)
            return 0

    def _current_hits(self, client_key: str, cutoff: float, now: float) -> list[float]:
        hits = self._hits[client_key]
        self._hits[client_key] = [t for t in hits if t > cutoff]
        if not self._hits[client_key]:
            pg_count = self._pg_hit_count(client_key, cutoff)
            if pg_count:
                self._hits[client_key] = [now - 1] * pg_count
        return self._hits[client_key]

    async def dispatch(self, request: Request, call_next):
        if not self._should_rate_limit(request):
            return await call_next(request)

        self._ensure_pg_table()
        client_key = self._client_key(request)
        now = time.time()
        cutoff = now - self.window

        hits = self._current_hits(client_key, cutoff, now)
        if len(hits) >= self.max_requests:
            return JSONResponse(
                {"error": "rate_limit_exceeded", "retry_after": int(self.window)},
                status_code=429,
            )

        self._hits[client_key].append(now)

        try:
            from ..db.adapter import is_postgresql

            if is_postgresql():
                import asyncio

                loop = asyncio.get_running_loop()
                loop.call_soon(self._pg_persist, client_key, now, cutoff)
        except Exception:
            logger.debug("rate limit PG persist schedule failed", exc_info=True)

        return await call_next(request)

    def _pg_persist(self, client_key: str, ts: float, cutoff: float):
        """Persist hit to PG and cleanup old entries."""
        try:
            from ..db.adapter import get_connection

            db = get_connection()
            db.execute(
                "INSERT INTO rate_limit_hits (client_key, ts) VALUES (?, ?)",
                (client_key, ts),
            )
            db.execute("DELETE FROM rate_limit_hits WHERE ts < ?", (cutoff,))
            db.commit()
            db.close()
        except Exception:
            logger.debug("rate limit PG persist failed", exc_info=True)
