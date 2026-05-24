"""README documentation is Architekt-branded and limited to EN + FR."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_READMES = frozenset(
    {"README.md", "README.fr.md", "README_SECURITY_SCAN.md"}
)

FORBIDDEN = re.compile(
    r"\b(Software Factory|Macaron Software|macaron-software/software-factory)\b",
    re.IGNORECASE,
)
ALLOWLIST_SUBSTR = (
    "formerly *Software Factory*",
    "anciennement *Software Factory*",
    "sf.macaron-* (pre-rebrand)",
    "sf.macaron-* (pré-rebrand)",
)


def _tracked_readmes() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "README*.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line.strip() for line in out.stdout.splitlines() if line.strip()]


def test_only_en_fr_readme_files_tracked():
    tracked = set(_tracked_readmes())
    assert tracked == ALLOWED_READMES, (
        f"Expected README*.md = {sorted(ALLOWED_READMES)}, got {sorted(tracked)}"
    )


@pytest.mark.parametrize("name", ["README.md", "README.fr.md"])
def test_readme_architekt_branding(name: str):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    assert "# Architekt Factory Platform" in text
    assert "Architekt Factory Platform" in text
    for match in FORBIDDEN.finditer(text):
        start = max(0, match.start() - 60)
        context = text[start : match.end() + 60]
        if any(a in context for a in ALLOWLIST_SUBSTR):
            continue
        pytest.fail(f"{name}: forbidden legacy branding '{match.group(0)}' near …{context}…")


def test_readme_language_nav_en_fr_only():
    for name in ("README.md", "README.fr.md"):
        header = Path(name).read_text(encoding="utf-8").split("</p>", 1)[0]
        assert "README.fr.md" in header
        assert "README.md" in header
        for lang in ("README.de.md", "README.es.md", "README.zh-CN.md", "README.ja.md"):
            assert lang not in header, f"{name} still links to {lang}"
