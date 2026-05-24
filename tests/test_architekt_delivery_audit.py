"""Regression audit — waves 0–4 deliverables must exist and critical paths work."""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

ROOT = Path(__file__).resolve().parents[1]

WAVE_ARTIFACTS = [
    "platform/branding.py",
    "platform/auth/api_key.py",
    "cli/architekt.py",
    "platform/skills/architekt/architekt-product.md",
    "platform/metrics/finops_summary.py",
    "platform/metrics/quality_pdf.py",
    "platform/llm/budget.py",
    "platform/audit/ai_logs.py",
    "platform/reports/case_study.py",
    "scripts/ci/secret-scan.sh",
    ".github/workflows/ci.yml",
    ".github/workflows/e2e-smoke.yml",
]


@pytest.mark.parametrize("rel_path", WAVE_ARTIFACTS)
def test_wave_artifact_exists(rel_path: str):
    assert (ROOT / rel_path).is_file(), f"missing deliverable: {rel_path}"


def test_run_guard_success_path_no_name_error():
    from platform.agents.adversarial import run_guard

    async def _run():
        return await run_guard(
            "ok",
            agent_role="dev",
            pattern_type="sequential",
            enable_l1=False,
        )

    result = asyncio.run(_run())
    assert result.passed


def test_run_guard_rejects_secret_via_l2():
    from platform.agents.adversarial import run_guard

    tool_calls = [
        {
            "name": "code_write",
            "args": {
                "path": "config.py",
                "content": 'API_KEY = "sk-live-audit-secret-key-99999"',
            },
        }
    ]

    async def _run():
        return await run_guard(
            "saved",
            agent_role="dev_backend",
            tool_calls=tool_calls,
            pattern_type="sequential",
            enable_l1=False,
        )

    result = asyncio.run(_run())
    assert not result.passed
    assert any("L2" in i for i in result.issues)


def test_rate_limit_middleware_importable():
    from platform.security import RateLimitMiddleware

    assert RateLimitMiddleware is not None


def test_architekt_skills_cap():
    from platform.agents.architekt_skills import MAX_ARCHITEKT_SKILLS, select_architekt_skill_ids

    ids = select_architekt_skill_ids(
        agent_id="dev_backend",
        agent_role="dev",
        mission_description="build api",
    )
    assert len(ids) <= MAX_ARCHITEKT_SKILLS
