"""Unit tests for LLM mission budget auto-pause."""

import json
import os
import sys
import uuid

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def budget_db(tmp_path, monkeypatch):
    """Isolated SQLite DB per test (avoids lock on shared platform.db)."""
    db_file = tmp_path / f"budget-{uuid.uuid4().hex}.db"
    monkeypatch.setattr("platform.config.DB_PATH", db_file)
    monkeypatch.setattr("platform.db.migrations.DB_PATH", db_file)

    from platform.db.migrations import get_db, init_db

    init_db(db_file)
    conn = get_db(db_file)
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS llm_traces (
            id TEXT PRIMARY KEY,
            provider TEXT,
            model TEXT,
            session_id TEXT,
            mission_id TEXT,
            cost_usd REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    conn.commit()
    conn.close()

    def _get_db():
        return get_db(db_file)

    monkeypatch.setattr("platform.llm.budget.get_db", _get_db)
    yield _get_db
    conn = get_db(db_file)
    conn.close()


def _insert_mission(conn, mission_id: str, config: dict | None = None):
    conn.execute(
        """
        INSERT INTO missions (id, project_id, name, status, config_json)
        VALUES (?, 'proj1', 'Test Mission', 'active', ?)
        """,
        (mission_id, json.dumps(config or {})),
    )


def _insert_trace(conn, session_id: str, mission_id: str, cost: float):
    conn.execute(
        """
        INSERT INTO llm_traces
        (id, provider, model, session_id, mission_id, cost_usd)
        VALUES (?, 'minimax', 'MiniMax-M2.5', ?, ?, ?)
        """,
        (uuid.uuid4().hex, session_id, mission_id, cost),
    )


class TestSessionCostUsd:
    def test_sums_traces_by_session(self, budget_db):
        from platform.llm.budget import session_cost_usd

        conn = budget_db()
        _insert_trace(conn, "sess-a", "m1", 0.25)
        _insert_trace(conn, "sess-a", "m1", 0.75)
        _insert_trace(conn, "sess-b", "m1", 1.0)
        conn.commit()
        conn.close()

        assert session_cost_usd("sess-a") == pytest.approx(1.0)
        assert session_cost_usd("sess-b") == pytest.approx(1.0)
        assert session_cost_usd("") == 0.0


class TestGetLlmBudgetUsd:
    def test_from_mission_constraints(self, budget_db, monkeypatch):
        from platform.llm.budget import get_llm_budget_usd

        monkeypatch.delenv("PLATFORM_LLM_MISSION_BUDGET_USD", raising=False)
        conn = budget_db()
        _insert_mission(conn, "m-budget", {"constraints": {"llm_budget_usd": 5.0}})
        conn.commit()
        conn.close()

        assert get_llm_budget_usd("m-budget") == pytest.approx(5.0)

    def test_env_fallback(self, budget_db, monkeypatch):
        from platform.llm.budget import get_llm_budget_usd

        monkeypatch.setenv("PLATFORM_LLM_MISSION_BUDGET_USD", "12.5")
        assert get_llm_budget_usd("unknown-mission") == pytest.approx(12.5)


class TestCheckAndPauseIfOverBudget:
    def test_pauses_run_at_100_percent(self, budget_db, monkeypatch):
        from platform.llm.budget import (
            check_and_pause_if_over_budget,
            mission_has_budget_exceeded,
        )

        monkeypatch.delenv("PLATFORM_LLM_MISSION_BUDGET_USD", raising=False)
        conn = budget_db()
        _insert_mission(conn, "m-pause", {"constraints": {"llm_budget_usd": 1.0}})
        conn.execute(
            """
            INSERT INTO mission_runs (id, workflow_id, session_id, status)
            VALUES ('run1', 'wf1', 'm-pause', 'running')
            """
        )
        _insert_trace(conn, "ceremony-1", "m-pause", 1.05)
        conn.commit()
        conn.close()

        assert check_and_pause_if_over_budget("ceremony-1", "m-pause") is True
        assert mission_has_budget_exceeded("m-pause") is True

        conn = budget_db()
        status = conn.execute(
            "SELECT status FROM mission_runs WHERE id = 'run1'"
        ).fetchone()[0]
        conn.close()
        assert status == "paused"

    def test_no_pause_under_budget(self, budget_db, monkeypatch):
        from platform.llm.budget import check_and_pause_if_over_budget

        monkeypatch.delenv("PLATFORM_LLM_MISSION_BUDGET_USD", raising=False)
        conn = budget_db()
        _insert_mission(conn, "m-ok", {"constraints": {"llm_budget_usd": 10.0}})
        _insert_trace(conn, "sess-ok", "m-ok", 0.5)
        conn.commit()
        conn.close()

        assert check_and_pause_if_over_budget("sess-ok", "m-ok") is False
