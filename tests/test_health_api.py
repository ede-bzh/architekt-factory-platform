"""
Health API tests — /api/health liveness probe.
Run: pytest tests/test_health_api.py -v
"""
import os
import sys
from datetime import datetime

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    os.environ["PLATFORM_ENV"] = "test"
    from platform.server import app

    with TestClient(app) as c:
        yield c


class TestHealthApi:
    def test_health_returns_200(self, client):
        r = client.get("/api/health")
        assert r.status_code == 200

    def test_health_status_ok(self, client):
        data = client.get("/api/health").json()
        assert data["status"] == "ok"

    def test_health_has_version_and_timestamp(self, client):
        data = client.get("/api/health").json()
        assert "version" in data
        assert data["version"]
        assert "timestamp" in data
        ts = data["timestamp"]
        assert ts.endswith("Z")
        parsed = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        assert parsed.year >= 2024
