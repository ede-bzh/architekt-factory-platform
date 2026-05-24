"""Tests for quality report PDF generation."""

import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


MOCK_SNAPSHOT = {
    "global_score": 72.5,
    "breakdown": {
        "global_score": 72.5,
        "dimensions": {
            "complexity": {"score": 80.0, "tool": "radon", "details": {}, "error": ""},
            "security": {"score": 65.0, "tool": "bandit", "details": {}, "error": ""},
            "coverage_ut": {"score": 55.0, "tool": "coverage.py", "details": {}, "error": ""},
        },
    },
    "timestamp": "2026-05-24T12:00:00",
}


def test_render_quality_pdf_starts_with_pdf_header():
    from platform.metrics.quality_pdf import render_quality_pdf

    pdf = render_quality_pdf(MOCK_SNAPSHOT)
    assert isinstance(pdf, bytes)
    assert pdf.startswith(b"%PDF")


@pytest.fixture(scope="module")
def client():
    os.environ["PLATFORM_ENV"] = "test"
    os.environ["PLATFORM_LLM_PROVIDER"] = "demo"
    from platform.server import app
    from fastapi.testclient import TestClient

    with TestClient(app) as c:
        yield c


def test_quality_report_pdf_endpoint(client):
    with patch(
        "platform.metrics.quality.QualityScanner.get_latest_snapshot",
        return_value=MOCK_SNAPSHOT,
    ):
        r = client.get("/api/quality/test-project/report.pdf")

    assert r.status_code == 200
    assert r.headers["content-type"] == "application/pdf"
    assert "quality-report.pdf" in r.headers.get("content-disposition", "")
    assert r.content.startswith(b"%PDF")
