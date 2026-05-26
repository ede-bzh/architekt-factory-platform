"""Platform API key resolution — ARCHITEKT_API_KEY."""

from __future__ import annotations

import os


def get_platform_api_key() -> str:
    """Return the configured platform API key (ARCHITEKT_API_KEY)."""
    return os.environ.get("ARCHITEKT_API_KEY", "").strip()
