#!/usr/bin/env python3
"""One-shot repo rebrand: Architekt → Architekt (wave E full replace)."""

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
}

SKIP_FILES = {
    "package-lock.json",
    "platform/tests/e2e/package-lock.json",
    "scripts/rebrand_macaron_to_architekt.py",
}

# Order matters: longer / more specific first
REPLACEMENTS: list[tuple[str, str]] = [
    ("ede-bzh/architekt-factory-platform", "ede-bzh/architekt-factory-platform"),
    ("architekt.ai", "architekt.ai"),
    ("architekt.ai", "architekt.ai"),
    ("sf.architekt.ai", "factory.architekt.ai"),
    ("RG-ARCHITEKT-vm-architekt", "RG-ARCHITEKT-vm-architekt"),
    ("architekt-platform-pg", "architekt-platform-pg"),
    ("architekt_platform", "architekt_platform"),
    ("architekt-platform", "architekt-platform"),
    ("ARCHITEKT_API_KEY", "ARCHITEKT_API_KEY"),
    ("/opt/architekt", "/opt/architekt"),
    ("architektbackups", "architektbackups"),
    ("RG-ARCHITEKT", "RG-ARCHITEKT"),
    ("vm-architekt", "vm-architekt"),
    ("architekt-app-", "architekt-app-"),
    ("architekt_update", "architekt_update"),
    ("architekt_pg", "architekt_pg"),
    ("~/.architekt", "~/.architekt"),
    ("agents@architekt.ai", "agents@architekt.ai"),
    ("Architekt Factory Platform", "Architekt Factory Platform"),
    ("Architekt PSY", "Architekt PSY"),
    ("Architekt Agents", "Architekt Agents"),
    ("Architekt Platform", "Architekt Platform"),
    ("ARCHITEKT FULL", "ARCHITEKT FULL"),
    ("ARCHITEKT HEALTH", "ARCHITEKT HEALTH"),
    ("architekt-sync", "architekt-sync"),
    ("architekt_cov_", "architekt_cov_"),
    ("architekt_arch_", "architekt_arch_"),
    ("architekt_gh_", "architekt_gh_"),
    ("architekt-canvas", "architekt-canvas"),
    ("architekt-prod", "architekt-prod"),
    ("architekt_uptime", "architekt_uptime"),
    ("architekt_http", "architekt_http"),
    ("architekt_mcp", "architekt_mcp"),
    ("architekt_process", "architekt_process"),
    ("architekt_llm", "architekt_llm"),
    ("architekt_*", "architekt_*"),
    ("VPS Architekt", "VPS Architekt"),
    ("DSI Architekt", "DSI Architekt"),
    ("Architekt", "Architekt"),
    ("Architekt Factory", "Architekt Factory"),
    ("[Architekt]", "[Architekt]"),
    ("in Architekt", "in Architekt"),
    ("from Architekt", "from Architekt"),
    ("Architekt ", "Architekt "),
    ("# ARCHITEKT", "# ARCHITEKT"),
    ("_ARCHITEKT_FACTORY", "_ARCHITEKT_FACTORY"),
    ("architekt2026", "architekt2026"),
    ("architekt:", "architekt:"),
    ("user architekt", "user architekt"),
    ("groupadd -r architekt", "groupadd -r architekt"),
    ("useradd -r -g architekt", "useradd -r -g architekt"),
    ("chown -R architekt:", "chown -R architekt:"),
    ("USER architekt", "USER architekt"),
    ("-u architekt:", "-u architekt:"),
    ("-U architekt", "-U architekt"),
    ("-d architekt_platform", "-d architekt_platform"),
    ("-g architekt", "-g architekt"),
    ("PG_USER:-architekt", "PG_USER:-architekt"),
    ("${PG_USER:-architekt}", "${PG_USER:-architekt}"),
    ("architekt_theme", "architekt_theme"),
    ("icon-architekt", "icon-architekt"),
    ("architekt-app", "architekt-app"),
    ("architekt@", "architekt@"),
    ("architekt/", "architekt/"),
    ("architekt\\", "architekt\\"),
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
