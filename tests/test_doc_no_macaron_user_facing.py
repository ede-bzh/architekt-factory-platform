"""User-facing doc surfaces must not expose Architekt / La Poste legacy branding."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

USER_FACING_DOCS = (
    ROOT / "docs/wiki/Home.md",
    ROOT / "docs/wiki/Home‐FR.md",
    ROOT / "README.md",
    ROOT / "README.fr.md",
)

_FORBIDDEN_PARTS = (
    r"architekt.ai",
    r"Macaron\s+Software\s+Factory",
    r"innovation-laposte",
    r"gitlab\.azure\.[^\s\)>]+laposte",
    r"gitlab[_-]?laposte",
    r"GitLab\s+La\s+Poste",
)
FORBIDDEN = re.compile("|".join(_FORBIDDEN_PARTS), re.IGNORECASE)


def _scan(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    hits: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if FORBIDDEN.search(line):
            hits.append(f"{path.relative_to(ROOT)}:{i}: {line.strip()[:120]}")
    return hits


@pytest.mark.parametrize(
    "path",
    USER_FACING_DOCS,
    ids=lambda p: p.relative_to(ROOT).as_posix(),
)
def test_no_macaron_or_laposte_in_user_facing_docs(path: Path):
    assert path.is_file(), f"missing user-facing doc: {path.relative_to(ROOT)}"
    hits = _scan(path)
    assert not hits, (
        "Legacy Architekt / La Poste branding in user-facing docs:\n"
        + "\n".join(hits[:40])
    )
