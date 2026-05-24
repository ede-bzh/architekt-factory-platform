"""AI audit log append-only tests."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_append_and_recent(monkeypatch, tmp_path):
    monkeypatch.setenv("PLATFORM_DATA_DIR", str(tmp_path))
    from platform.db.migrations import init_db
    from platform.audit.ai_logs import get_ai_logger

    init_db()
    logger = get_ai_logger()
    log_id = logger.append(
        provider="demo",
        model="demo",
        mission_id="m-test",
        tokens_in=10,
        tokens_out=20,
        cost_usd=0.01,
    )
    assert len(log_id) >= 8
    rows = logger.recent(limit=5, mission_id="m-test")
    assert any(r["id"] == log_id for r in rows)


def test_trace_call_writes_audit(monkeypatch, tmp_path):
    monkeypatch.setenv("PLATFORM_DATA_DIR", str(tmp_path))
    from platform.db.migrations import init_db
    from platform.llm.observability import get_tracer

    init_db()
    tid = get_tracer().trace_call(
        provider="demo",
        model="demo",
        tokens_in=5,
        tokens_out=5,
        mission_id="m-trace",
    )
    from platform.audit.ai_logs import get_ai_logger

    rows = get_ai_logger().recent(mission_id="m-trace")
    assert any(r.get("payload_json", "").find(tid) >= 0 or r["mission_id"] == "m-trace" for r in rows)
