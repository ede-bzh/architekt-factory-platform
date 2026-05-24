"""i18n — Platform UI internationalization (English and French only).

Usage in Jinja2 templates:  {{ _('key') }}  or  {{ _('key', name='World') }}
Usage in Python:            from platform.i18n import t; t('key', lang='en')
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

LOCALES_DIR = Path(__file__).parent / "locales"
DEFAULT_LANG = "en"
SUPPORTED_LANGS = ("en", "fr")

_catalog: dict[str, dict[str, str]] = {}


def normalize_lang(code: str | None) -> str:
    """Map a locale code to en/fr; unsupported codes fall back to English."""
    if not code:
        return DEFAULT_LANG
    base = code.strip().lower().split("-")[0].split("_")[0]
    return base if base in SUPPORTED_LANGS else DEFAULT_LANG


def _load_catalog() -> None:
    """Load EN/FR locale JSON files into memory."""
    global _catalog
    _catalog = {}
    for lang in SUPPORTED_LANGS:
        fpath = LOCALES_DIR / f"{lang}.json"
        if fpath.exists():
            with open(fpath, encoding="utf-8") as f:
                _catalog[lang] = json.load(f)
            log.info("i18n: loaded %d keys for '%s'", len(_catalog[lang]), lang)
        else:
            _catalog[lang] = {}
            log.warning("i18n: missing locale file %s", fpath)


def t(key: str, lang: str = DEFAULT_LANG, **kwargs: Any) -> str:
    """Translate a key. Falls back to English, then to the key itself."""
    if not _catalog:
        _load_catalog()
    lang = normalize_lang(lang)
    text = _catalog.get(lang, {}).get(key)
    if text is None and lang != DEFAULT_LANG:
        text = _catalog.get(DEFAULT_LANG, {}).get(key)
    if text is None:
        return key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text


def get_lang(request) -> str:
    """Detect language: sf_lang/lang cookie > Accept-Language > default en."""
    for key in ("sf_lang", "lang"):
        cookie_lang = request.cookies.get(key)
        if cookie_lang:
            base = cookie_lang.strip().lower().split("-")[0].split("_")[0]
            if base in SUPPORTED_LANGS:
                return base
    accept = request.headers.get("accept-language", "")
    for part in accept.split(","):
        code = part.strip().split(";")[0].strip()
        base = code.lower().split("-")[0].split("_")[0]
        if base in SUPPORTED_LANGS:
            return base
    return DEFAULT_LANG


def reload_catalog() -> None:
    """Force reload translations (e.g., after editing locale files)."""
    _load_catalog()


_load_catalog()
