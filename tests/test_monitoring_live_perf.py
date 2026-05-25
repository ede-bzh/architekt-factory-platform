"""Smoke test: monitoring_live latency with PLATFORM_ENV=test."""

from __future__ import annotations

import os
import time

import pytest

os.environ.setdefault("PLATFORM_ENV", "test")
os.environ.setdefault("PLATFORM_LLM_PROVIDER", "demo")

from fastapi.testclient import TestClient

from platform.server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_monitoring_live_p95_under_threshold(client):
    """Cached monitoring_live should stay under 2s p95 in test env."""
    latencies: list[float] = []
    for _ in range(5):
        t0 = time.perf_counter()
        r = client.get("/api/monitoring/live?sections=system")
        latencies.append(time.perf_counter() - t0)
        assert r.status_code == 200
    latencies.sort()
    p95 = latencies[int(len(latencies) * 0.95)]
    assert p95 < 2.0, f"p95 monitoring_live {p95:.3f}s exceeds 2s"
