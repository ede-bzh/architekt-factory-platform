"""Prometheus architekt_* metric aliases."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture(scope="module")
def client():
    os.environ["PLATFORM_ENV"] = "test"
    from fastapi.testclient import TestClient
    from platform.server import app

    with TestClient(app) as c:
        yield c


def test_prometheus_has_architekt_uptime(client):
    r = client.get("/api/metrics/prometheus")
    assert r.status_code == 200
    text = r.text
    assert "macaron_uptime_seconds" in text
    assert "architekt_uptime_seconds" in text
    assert "architekt_finops_margin_pct" in text
