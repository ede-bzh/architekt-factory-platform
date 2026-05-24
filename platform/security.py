"""Security middleware — authentication, RBAC, rate limiting."""

from __future__ import annotations

import hashlib
import logging
import os
import time
from collections import defaultdict

from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class AuthMiddleware(BaseHTTPMiddleware):
    """API key authentication for sensitive endpoints.

    Set MACARON_API_KEY env var to enable. If not set, auth is disabled (dev mode).
    Only protects API mutation endpoints and sensitive data — pages, static,
    health, docs, and SSE are always public.
    """

    EXCLUDED_PREFIXES = (
        "/health",
        "/static",
        "/docs",
        "/redoc",
        "/openapi.json",
        "/sse",
        "/favicon",
        "/api/health",
        "/api/i18n/",
    )
    # Public API reads (GET only) — always accessible
    PUBLIC_GET_PATHS = (
        "/api/projects",
        "/api/agents",
        "/api/missions",
        "/api/integrations",
        "/api/metrics",
        "/api/workflows",
        "/api/monitoring/live",
        "/api/notifications/status",
        "/api/analytics",
    )

    async def dispatch(self, request: Request, call_next):
        api_key = os.getenv("MACARON_API_KEY")
        if not api_key:
            if os.getenv("ENVIRONMENT", "dev") != "dev":
                logger.warning("AUTH DISABLED — set MACARON_API_KEY for production")
            return await call_next(request)

        path = request.url.path

        # Always allow excluded paths (static, docs, health, SSE)
        if any(path.startswith(p) for p in self.EXCLUDED_PREFIXES):
            return await call_next(request)

        # Allow all non-API paths (HTML pages)
        if not path.startswith("/api/"):
            return await call_next(request)

        # Allow public GET endpoints
        if request.method == "GET" and any(
            path.startswith(p) for p in self.PUBLIC_GET_PATHS
        ):
            # Mark as unauthenticated for info redaction
            request.state.authenticated = False
            return await call_next(request)

        # All other API calls require auth
        token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        if not token:
            token = request.query_params.get("token", "")

        if (
            not token
            or hashlib.sha256(token.encode()).hexdigest()
            != hashlib.sha256(api_key.encode()).hexdigest()
        ):
            raise HTTPException(status_code=401, detail="Invalid or missing API key")

        request.state.authenticated = True
        return await call_next(request)


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Deprecated: use ``platform.security.rate_limit.RateLimitMiddleware``."""

    def __init__(self, *args, **kwargs):
        from platform.security.rate_limit import RateLimitMiddleware as _RL

        self._impl = _RL(*args, **kwargs)

    async def dispatch(self, request, call_next):
        return await self._impl.dispatch(request, call_next)


def health_check():
    """Health check endpoint data."""
    return {
        "status": "healthy",
        "version": "0.1.0",
        "timestamp": time.time(),
    }
