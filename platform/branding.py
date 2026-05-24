"""Product branding and environment helpers for Architekt platform."""
from __future__ import annotations

import os

PRODUCT_NAME = "Architekt"
PRODUCT_SHORT = "Architekt"
PRODUCT_FULL_NAME = "Architekt Factory Platform"
THEME_STORAGE_KEY = "architekt_theme"
LEGACY_THEME_STORAGE_KEY = "macaron_theme"


def get_api_key() -> str:
    """Platform API key: ARCHITEKT_API_KEY with MACARON_API_KEY fallback."""
    return os.getenv("ARCHITEKT_API_KEY") or os.getenv("MACARON_API_KEY") or ""
