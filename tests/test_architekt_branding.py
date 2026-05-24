"""UI must not expose legacy Macaron / Software Factory branding."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = re.compile(
    r"\b(Macaron|MACARON|Software Factory|macaron_world|macaron_theme|icon-macaron)\b"
    r"|macaron-app",
    re.IGNORECASE,
)
ALLOWLIST_SUBSTR = (
    "macaron_theme')",  # legacy localStorage fallback in JS
)


def _paths():
    templates = ROOT / "platform" / "web" / "templates"
    locales = ROOT / "platform" / "i18n" / "locales"
    static = [
        ROOT / "platform" / "web" / "static" / "manifest.json",
        ROOT / "platform" / "web" / "static" / "sw.js",
    ]
    files = list(templates.rglob("*.html")) + list(locales.glob("*.json")) + static
    return [p for p in files if p.is_file()]


@pytest.mark.parametrize("path", _paths(), ids=lambda p: p.relative_to(ROOT).as_posix())
def test_no_legacy_brand_in_user_facing_files(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        try:
            text = json.dumps(json.loads(text), ensure_ascii=False)
        except json.JSONDecodeError:
            pass
    for match in FORBIDDEN.finditer(text):
        snippet = match.group(0)
        start = max(0, match.start() - 40)
        context = text[start : match.end() + 40]
        if any(a in context for a in ALLOWLIST_SUBSTR):
            continue
        pytest.fail(
            f"{path.relative_to(ROOT)}: forbidden '{snippet}' near …{context}…"
        )
