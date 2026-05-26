#!/usr/bin/env python3
"""One-shot repo rebrand: Architekt → Architekt (wave E).

Safe to re-run on already-rebranded trees (idempotent). Skips tests/ that
intentionally mention legacy names for CI gates.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".mutmut-cache",
    "__pycache__",
    ".pytest_cache",
    "platform/tests/e2e/node_modules",
    "_FINARY",
}

SKIP_FILES = {
    "package-lock.json",
    "platform/tests/e2e/package-lock.json",
    "scripts/rebrand_architekt_to_architekt.py",
}

SKIP_PATH_PREFIXES = (
    "tests/test_",  # gate tests reference forbidden legacy strings by design
)

SKIP_PATHS = {
    "docs/adr/001-rebrand-architekt.md",
    "docs/architekt/REBRAND-DOC-AUDIT.md",
}

REPLACEMENTS: list[tuple[str, str]] = [
    ("architekt.ai", "architekt.ai"),
    ("sf.architekt.ai", "sf.architekt.ai"),
    ("architekt_platform", "architekt_platform"),
    ("architekt-platform", "architekt-platform"),
    ("ARCHITEKT_API_KEY", "ARCHITEKT_API_KEY"),
    ("ARCHITEKT_URL", "ARCHITEKT_URL"),
    ("ARCHITEKT_TOKEN", "ARCHITEKT_TOKEN"),
    ("architekt_world", "architekt_world"),
    ("architekt_theme", "architekt_theme"),
    ("icon-architekt", "icon-architekt"),
    ("architekt-app", "architekt-app"),
    ("architekt_view_", "architekt_view_"),
    ("/opt/architekt", "/opt/architekt"),
    ("RG-ARCHITEKT-vm-architekt", "RG-ARCHITEKT-vm-architekt"),
    ("architektbackups", "architektbackups"),
    ("Architekt Factory Platform", "Architekt Factory Platform"),
    ("Architekt Agent Platform", "Architekt Agent Platform"),
    ("Architekt Software", "Architekt Software"),
    ("Architekt", "Architekt"),
    ("ARCHITEKT", "ARCHITEKT"),
    ("architekt_", "architekt_"),
    ("user architekt", "user architekt"),
    ("User=architekt", "User=architekt"),
    ("-d /app architekt", "-d /app architekt"),
    ("usermod -aG docker architekt", "usermod -aG docker architekt"),
    ("~/.architekt", "~/.architekt"),
    ("architekt", "architekt"),
]

TEXT_EXTENSIONS = {
    ".py",
    ".md",
    ".yml",
    ".yaml",
    ".sh",
    ".html",
    ".js",
    ".ts",
    ".json",
    ".toml",
    ".tpl",
    ".txt",
    ".env",
    ".example",
    "Dockerfile",
    "Makefile",
}


def should_process(path: Path) -> bool:
    if path.name in SKIP_FILES:
        return False
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP_PATHS or rel.startswith(SKIP_PATH_PREFIXES):
        return False
    for part in path.parts:
        if part in SKIP_DIRS:
            return False
    if path.name == "Dockerfile" or path.suffix in TEXT_EXTENSIONS:
        return True
    return False


def main() -> int:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or not should_process(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        original = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(path.relative_to(ROOT))
    print(f"\nUpdated {changed} files", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
