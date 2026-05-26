"""Wiki EN pages that link to *‐FR must have a matching French file."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "docs" / "wiki"

FR_LINK = re.compile(r"\]\(([A-Za-z0-9-]+‐FR)\)")


def test_fr_wiki_targets_exist():
    missing: list[str] = []
    for path in sorted(WIKI.glob("*.md")):
        if path.name.endswith("‐FR.md") or path.name.startswith("_"):
            continue
        if path.name == "Home.md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in FR_LINK.findall(text):
            fr_path = WIKI / f"{target}.md"
            if not fr_path.is_file():
                missing.append(f"{path.name} → {target}.md")
    assert not missing, "Missing French wiki pages:\n" + "\n".join(missing)
