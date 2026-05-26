"""L2-LLM adversarial guard — architecture / API semantic review (mocked LLM)."""
import asyncio
import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from platform.agents.adversarial import check_l2_llm, run_guard


def _api_tool_calls(body: str = "") -> list:
    default = """
from fastapi import APIRouter
router = APIRouter()

@router.post("/api/users")
async def create_user(payload: dict):
    return payload
"""
    return [
        {
            "name": "code_write",
            "args": {"path": "routes/api.py", "content": body or default},
        }
    ]


@pytest.mark.asyncio
async def test_l2_llm_demo_provider_skips(monkeypatch):
    monkeypatch.setenv("PLATFORM_LLM_PROVIDER", "demo")
    result = await check_l2_llm(
        "Implemented REST API.",
        task="Add user API",
        agent_role="dev_backend",
        agent_name="dev-1",
        tool_calls=_api_tool_calls(),
    )
    assert result.passed
    assert result.level == "L2-llm-skipped"


@pytest.mark.asyncio
async def test_l2_llm_fail_closed_on_exception(monkeypatch):
    monkeypatch.setenv("PLATFORM_LLM_PROVIDER", "minimax")

    def _boom():
        raise RuntimeError("llm down")

    with patch("platform.llm.client.get_llm_client", side_effect=_boom):
        result = await check_l2_llm(
            "Implemented REST API.",
            task="Add user API",
            agent_role="dev_backend",
            agent_name="dev-1",
            tool_calls=_api_tool_calls(),
        )
    assert not result.passed
    assert result.level == "L2-llm-fail-closed"
    assert any("reviewer unavailable" in i for i in result.issues)


@pytest.mark.asyncio
async def test_l2_llm_rejects_bad_verdict(monkeypatch):
    monkeypatch.setenv("PLATFORM_LLM_PROVIDER", "minimax")

    mock_client = MagicMock()
    mock_client.chat = AsyncMock(
        return_value=MagicMock(
            content='{"score": 8, "issues": ["RBAC: admin route has no auth"], "verdict": "REJECT"}'
        )
    )

    with patch("platform.llm.client.get_llm_client", return_value=mock_client):
        result = await check_l2_llm(
            "Implemented REST API.",
            task="Add user API",
            agent_role="dev_backend",
            agent_name="dev-1",
            tool_calls=_api_tool_calls(),
        )

    assert not result.passed
    assert result.level == "L2-LLM"
    assert any("RBAC" in i for i in result.issues)
    mock_client.chat.assert_awaited_once()


def test_run_guard_pipeline_l2_llm_before_l1_demo(monkeypatch):
    """Demo skips L2-LLM; deterministic L2 still runs before L1 in run_guard."""
    monkeypatch.setenv("PLATFORM_LLM_PROVIDER", "demo")
    tool_calls = _api_tool_calls('x = 1\n')
    result = asyncio.run(
        run_guard(
            "Saved routes.",
            task="API",
            agent_role="dev_backend",
            agent_name="dev-1",
            tool_calls=tool_calls,
            pattern_type="sequential",
            enable_l1=False,
        )
    )
    assert result.passed
    assert "L2-LLM" in result.level
