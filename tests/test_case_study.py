"""Mission case study markdown export."""
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


def test_case_study_endpoint_unknown_mission(client):
    r = client.get("/api/missions/unknown-mission-xyz/case-study.md")
    assert r.status_code == 200
    assert "introuvable" in r.text.lower() or "Case study" in r.text


def test_generate_case_study_markdown(monkeypatch, tmp_path):
    monkeypatch.setenv("PLATFORM_DATA_DIR", str(tmp_path))
    from platform.db.migrations import get_db, init_db
    from platform.reports.case_study import generate_case_study_markdown

    init_db()
    import uuid
    mid = f"cs-{uuid.uuid4().hex[:8]}"
    db = get_db()
    db.execute(
        "INSERT INTO missions (id, project_id, name, status, config_json) VALUES (?,?,?,?,?)",
        (mid, "proj-test", "Test Epic", "active", "{}"),
    )
    db.commit()
    db.close()
    md = generate_case_study_markdown(mid)
    assert "Test Epic" in md
    assert "FinOps" in md
