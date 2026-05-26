"""Product branding and environment helpers for Architekt platform."""
from __future__ import annotations

import os

PRODUCT_NAME = "Architekt"
PRODUCT_SHORT = "Architekt"
PRODUCT_FULL_NAME = "Architekt Factory Platform"
THEME_STORAGE_KEY = "architekt_theme"


def get_api_key() -> str:
    """Platform API key from ARCHITEKT_API_KEY."""
    return os.getenv("ARCHITEKT_API_KEY") or ""
