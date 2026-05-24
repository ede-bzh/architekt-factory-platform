"""Platform API key resolution — ARCHITEKT_API_KEY with MACARON_API_KEY fallback."""

from __future__ import annotations

import os


def get_platform_api_key() -> str:
    """Return the configured platform API key.

    Prefers ARCHITEKT_API_KEY (ADR-001 niveau 2). Falls back to MACARON_API_KEY
    for backward compatibility during the 6-month migration window.
    """
    return (os.environ.get("ARCHITEKT_API_KEY") or os.environ.get("MACARON_API_KEY") or "").strip()
