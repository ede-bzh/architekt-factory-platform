"""Rate limiting tests for /api/* mutation endpoints."""

from __future__ import annotations

import os
import sys

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.requests import Request

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from platform.security.rate_limit import (
    MUTATION_METHODS,
    RateLimitMiddleware,
    is_api_mutation,
)


def _make_request(method: str, path: str) -> Request:
    scope = {
        "type": "http",
        "method": method,
        "path": path,
        "headers": [],
        "client": ("127.0.0.1", 12345),
    }
    return Request(scope)


@pytest.fixture
def rl_app(monkeypatch):
    monkeypatch.delenv("PLATFORM_ENV", raising=False)
    app = FastAPI()
    app.add_middleware(RateLimitMiddleware, max_requests=5, window_seconds=60)

    @app.get("/api/health")
    def health():
        return {"ok": True}

    @app.post("/api/test-mutation")
    def mutate():
        return {"ok": True}

    @app.patch("/api/test-mutation")
    def patch_mutate():
        return {"patched": True}

    return app


class TestIsApiMutation:
    def test_mutation_methods(self):
        for method in MUTATION_METHODS:
            assert is_api_mutation(_make_request(method, "/api/foo"))

    def test_get_not_mutation(self):
        assert not is_api_mutation(_make_request("GET", "/api/foo"))

    def test_non_api_not_mutation(self):
        assert not is_api_mutation(_make_request("POST", "/projects/1"))


class TestRateLimitMiddleware:
    def test_get_unlimited(self, rl_app):
        client = TestClient(rl_app)
        for _ in range(20):
            assert client.get("/api/health").status_code == 200

    def test_post_rate_limited(self, rl_app):
        client = TestClient(rl_app)
        for _ in range(5):
            assert client.post("/api/test-mutation").status_code == 200
        blocked = client.post("/api/test-mutation")
        assert blocked.status_code == 429
        body = blocked.json()
        assert body["error"] == "rate_limit_exceeded"
        assert body["retry_after"] == 60

    def test_patch_rate_limited(self, rl_app):
        client = TestClient(rl_app)
        for _ in range(5):
            assert client.patch("/api/test-mutation").status_code == 200
        assert client.patch("/api/test-mutation").status_code == 429

    def test_per_token_buckets(self, rl_app):
        client = TestClient(rl_app)
        headers_a = {"Authorization": "Bearer token-a"}
        headers_b = {"Authorization": "Bearer token-b"}
        for _ in range(5):
            assert client.post("/api/test-mutation", headers=headers_a).status_code == 200
        assert client.post("/api/test-mutation", headers=headers_a).status_code == 429
        assert client.post("/api/test-mutation", headers=headers_b).status_code == 200

    def test_skipped_in_platform_env_test(self, monkeypatch):
        monkeypatch.setenv("PLATFORM_ENV", "test")
        app = FastAPI()
        app.add_middleware(RateLimitMiddleware, max_requests=1, window_seconds=60)

        @app.post("/api/x")
        def x():
            return {"ok": True}

        client = TestClient(app)
        assert client.post("/api/x").status_code == 200
        assert client.post("/api/x").status_code == 200

    def test_pg_hydration_after_restart(self, monkeypatch):
        monkeypatch.delenv("PLATFORM_ENV", raising=False)
        mw = RateLimitMiddleware(FastAPI(), max_requests=3, window_seconds=60)
        monkeypatch.setattr(mw, "_pg_hit_count", lambda key, cutoff: 3)

        app = FastAPI()

        @app.post("/api/x")
        def x():
            return {"ok": True}

        app.add_middleware(RateLimitMiddleware, max_requests=3, window_seconds=60)
        # Patch middleware instance created by add_middleware
        for m in app.user_middleware:
            if m.cls is RateLimitMiddleware:
                m.kwargs["max_requests"] = 3
        client = TestClient(app)
        # Fresh in-memory but PG says 3 hits -> 429 on first request
        monkeypatch.setattr(
            "platform.security.rate_limit.RateLimitMiddleware._pg_hit_count",
            lambda self, key, cutoff: 3,
        )
        resp = client.post("/api/x")
        assert resp.status_code == 429
