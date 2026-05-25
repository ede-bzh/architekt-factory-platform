"""Ensure La Poste–specific branding and sync tooling are removed from tracked sources."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SELF = Path(__file__).resolve()

_FORBIDDEN_PARTS = (
    "laposte",
    r"la\s+poste",
    "gitlab_laposte",
    "sync-to-laposte",
    r"plateforme\s+agents\s+la\s+poste",
    "innovation-laposte",
    "_laposte/",
    "readme.laposte",
)
FORBIDDEN = re.compile("|".join(_FORBIDDEN_PARTS), re.IGNORECASE)

SCAN_SUFFIXES = {
    ".py", ".md", ".yml", ".yaml", ".sh", ".env", ".example", ".html", ".j2",
    ".ts", ".js", ".json", ".txt", ".toml",
}

SKIP_DIRS = {"_FINARY", ".git", "__pycache__", "node_modules", ".venv", "venv"}

# Meta-docs that describe the migration may quote forbidden tokens intentionally.
ALLOWLIST_REL = frozenset({
    "docs/architekt/REBRAND-DOC-AUDIT.md",
    "docs/architekt/PLATFORM-BACKLOG.md",
    "docs/AUDIT_REBRAND.md",
    "docs/ROADMAP.md",
    "tests/test_doc_no_macaron_user_facing.py",
})


def _tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [ROOT / line for line in out.stdout.splitlines() if line.strip()]


def test_no_laposte_references_in_tracked_files():
    hits: list[str] = []
    for path in _tracked_files():
        if path.resolve() == _SELF:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in ALLOWLIST_REL:
            continue
        if path.suffix.lower() not in SCAN_SUFFIXES and path.name not in {
            ".env.example",
            ".gitlab-ci.yml",
        }:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if FORBIDDEN.search(line):
                hits.append(f"{path.relative_to(ROOT)}:{i}: {line.strip()[:120]}")
    assert not hits, "La Poste references still present:\n" + "\n".join(hits[:40])
