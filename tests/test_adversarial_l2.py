"""L2 adversarial guard — architecture / security patterns."""
import asyncio
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from platform.agents.adversarial import check_l2, run_guard


def test_l2_rejects_hardcoded_secret_in_code_write():
    tool_calls = [
        {
            "name": "code_write",
            "args": {
                "path": "config.py",
                "content": 'API_KEY = "sk-live-super-secret-key-12345"',
            },
        }
    ]
    result = check_l2("Saved config.", agent_role="dev_backend", tool_calls=tool_calls)
    assert not result.passed
    assert result.level == "L2"
    assert any("L2_ARCH" in i for i in result.issues)


def test_l2_skips_without_code_write():
    result = check_l2("Analysis only.", agent_role="dev", tool_calls=[])
    assert result.passed
    assert result.level == "L2-skipped"


def test_l2_skips_non_dev_role():
    tool_calls = [
        {
            "name": "code_write",
            "args": {"path": "x.py", "content": "eval(user_input)"},
        }
    ]
    result = check_l2("Done.", agent_role="product_owner", tool_calls=tool_calls)
    assert result.passed
    assert result.level == "L2-skipped"

def test_run_guard_rejects_hardcoded_secret_via_l2():
    tool_calls = [
        {
            "name": "code_write",
            "args": {
                "path": "config.py",
                "content": 'API_KEY = "sk-live-super-secret-key-12345"',
            },
        }
    ]
    result = asyncio.run(
        run_guard(
            "Saved config.",
            agent_role="dev_backend",
            tool_calls=tool_calls,
            enable_l1=False,
        )
    )
    assert not result.passed
    assert result.level == "L2"
    assert any("L2_ARCH" in i for i in result.issues)
