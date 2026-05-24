"""Tests for ARCHITEKT_API_KEY / MACARON_API_KEY alias (ADR-001 niveau 2)."""

import importlib

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def _clear_api_key_env(monkeypatch):
    monkeypatch.delenv("ARCHITEKT_API_KEY", raising=False)
    monkeypatch.delenv("MACARON_API_KEY", raising=False)
    yield


def test_get_platform_api_key_prefers_architekt(monkeypatch):
    monkeypatch.setenv("MACARON_API_KEY", "legacy-secret")
    monkeypatch.setenv("ARCHITEKT_API_KEY", "architekt-secret")

    from platform.auth import api_key

    importlib.reload(api_key)
    assert api_key.get_platform_api_key() == "architekt-secret"


def test_get_platform_api_key_falls_back_to_macaron(monkeypatch):
    monkeypatch.setenv("MACARON_API_KEY", "legacy-only")

    from platform.auth import api_key

    importlib.reload(api_key)
    assert api_key.get_platform_api_key() == "legacy-only"


def test_auth_middleware_accepts_architekt_key(monkeypatch):
    secret = "test-architekt-key-7576"
    monkeypatch.setenv("ARCHITEKT_API_KEY", secret)
    monkeypatch.setenv("PLATFORM_ENV", "test")
    monkeypatch.setenv("PLATFORM_LLM_PROVIDER", "demo")

    from platform.auth import api_key

    importlib.reload(api_key)

    from platform.server import app

    client = TestClient(app)
    r = client.post(
        "/api/projects",
        json={"name": "api-key-test", "description": "x"},
        headers={"Authorization": f"Bearer {secret}"},
    )
    assert r.status_code != 401


def test_auth_middleware_accepts_macaron_key_when_architekt_unset(monkeypatch):
    secret = "test-macaron-key-7576"
    monkeypatch.setenv("MACARON_API_KEY", secret)
    monkeypatch.setenv("PLATFORM_ENV", "test")
    monkeypatch.setenv("PLATFORM_LLM_PROVIDER", "demo")

    from platform.auth import api_key

    importlib.reload(api_key)

    from platform.server import app

    client = TestClient(app)
    r = client.post(
        "/api/projects",
        json={"name": "api-key-legacy-test", "description": "x"},
        headers={"Authorization": f"Bearer {secret}"},
    )
    assert r.status_code != 401


def test_select_architekt_skills_for_brain():
    from platform.agents.architekt_skills import select_architekt_skill_ids

    ids = select_architekt_skill_ids("brain", "Strategic Orchestrator", None)
    assert "architekt-compliance" in ids
    assert "architekt-i18n" in ids


def test_architekt_skills_loaded_in_library():
    from platform.skills.library import get_skill_library

    lib = get_skill_library()
    lib.scan_all()
    assert lib.get("architekt-compliance") is not None
    assert lib.get("architekt-i18n") is not None
