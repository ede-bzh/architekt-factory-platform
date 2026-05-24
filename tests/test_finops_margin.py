"""FinOps margin summary tests."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_compute_margin_above_target():
    from platform.metrics.finops_summary import compute_margin

    m = compute_margin(cost_usd=100.0, revenue_usd=5000.0)
    assert m["margin_pct"] == 98.0
    assert m["below_target"] is False


def test_compute_margin_below_target(monkeypatch):
    monkeypatch.setenv("PLATFORM_FINOPS_MARGIN_TARGET_PCT", "50")
    from platform.metrics.finops_summary import compute_margin

    m = compute_margin(cost_usd=4000.0, revenue_usd=5000.0)
    assert m["margin_pct"] == 20.0
    assert m["below_target"] is True


def test_global_summary_has_margin_fields(monkeypatch, tmp_path):
    monkeypatch.setenv("PLATFORM_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    from platform.db.migrations import init_db
    from platform.metrics.finops_summary import global_summary

    init_db()
    g = global_summary()
    assert "margin_pct" in g
    assert "target_margin_pct" in g
    assert "alerts" in g
