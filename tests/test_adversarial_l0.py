"""L0 adversarial guard — ZERO SKIP pattern rejection."""
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from platform.agents.adversarial import GuardResult, check_l0


def _reject(content: str, **kwargs) -> GuardResult:
    result = check_l0(content, agent_role="dev", **kwargs)
    assert not result.passed, f"Expected rejection, got pass: {result.issues}"
    assert result.level == "L0"
    assert result.score >= 5
    return result


def _approve(content: str, **kwargs) -> GuardResult:
    result = check_l0(content, agent_role="dev", **kwargs)
    assert result.passed, f"Expected approval, got reject: {result.issues}"
    return result


class TestAdversarialL0ZeroSkip:
    def test_rejects_test_skip_in_output(self):
        result = _reject('Added coverage with test.skip("pending") for now.')
        assert any("test.skip" in i for i in result.issues)

    def test_rejects_ts_ignore_in_output(self):
        result = _reject("// @ts-ignore legacy API mismatch")
        assert any("ts-ignore" in i.lower() for i in result.issues)

    def test_rejects_except_pass_in_output(self):
        result = _reject("try:\n    risky()\nexcept:\n    pass")
        assert any("except: pass" in i for i in result.issues)

    def test_rejects_test_skip_in_code_write(self):
        tool_calls = [
            {
                "name": "code_write",
                "args": {
                    "path": "src/foo.test.ts",
                    "content": 'it("works", () => { test.skip(); });',
                },
            }
        ]
        result = _reject("Wrote tests.", tool_calls=tool_calls)
        assert any("ZERO_SKIP" in i for i in result.issues)

    def test_rejects_ts_ignore_in_code_write(self):
        tool_calls = [
            {
                "name": "code_write",
                "args": {
                    "path": "src/utils.ts",
                    "content": "// @ts-ignore\nconst x = legacy();",
                },
            }
        ]
        result = _reject("Patched utils.", tool_calls=tool_calls)
        assert any("ZERO_SKIP" in i for i in result.issues)

    def test_rejects_except_pass_in_code_write(self):
        tool_calls = [
            {
                "name": "code_write",
                "args": {
                    "path": "src/handler.py",
                    "content": "def run():\n    try:\n        go()\n    except:\n        pass\n",
                },
            }
        ]
        result = _reject("Added handler.", tool_calls=tool_calls)
        assert any("ZERO_SKIP" in i for i in result.issues)

    def test_approves_clean_output_with_tool_evidence(self):
        tool_calls = [
            {
                "name": "code_write",
                "args": {
                    "path": "src/utils.ts",
                    "content": "export function add(a: number, b: number) { return a + b; }\n",
                },
            }
        ]
        _approve(
            "Implemented add() with full test coverage and no skip directives.",
            tool_calls=tool_calls,
        )
