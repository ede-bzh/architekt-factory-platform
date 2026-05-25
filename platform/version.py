"""Single source of truth for platform semver (UI, OpenAPI, OTEL, /api/health)."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

_VERSION_FILE = Path(__file__).resolve().parent / "VERSION"


@lru_cache(maxsize=1)
def get_platform_version() -> str:
    """Read semver from platform/VERSION; override via PLATFORM_VERSION env."""
    override = os.environ.get("PLATFORM_VERSION", "").strip()
    if override:
        # Deploy may set tag:sha — use semver prefix when present
        if ":" in override:
            return override.split(":", 1)[0].strip() or override
        return override
    try:
        raw = _VERSION_FILE.read_text(encoding="utf-8").strip()
        if raw:
            return raw.split(":", 1)[0].strip()
    except OSError:
        pass
    return "2.3.0"
