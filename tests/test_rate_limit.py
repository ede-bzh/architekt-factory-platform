"""Tests for DB-backed API rate limiting."""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


@pytest.fixture
def rate_limit_db(tmp_path, monkeypatch):
    """Isolated SQLite DB with rate_limit_hits table."""
    db_path = tmp_path / "rate_limit_test.db"
    from platform.db.migrations import get_db, init_db

    init_db(db_path)
    monkeypatch.setattr(
        "platform.security.rate_limit.get_db",
        lambda db_path=db_path: get_db(db_path),
    )
    return db_path


class TestCheckRateLimit:
    def test_allows_requests_under_limit(self, rate_limit_db):
        from platform.security.rate_limit import check_rate_limit

        for _ in range(3):
            assert check_rate_limit("client-a", max_requests=5, window_seconds=60.0)

    def test_blocks_when_limit_exceeded(self, rate_limit_db):
        from platform.security.rate_limit import check_rate_limit

        for _ in range(2):
            assert check_rate_limit("client-b", max_requests=2, window_seconds=60.0)
        assert not check_rate_limit("client-b", max_requests=2, window_seconds=60.0)
