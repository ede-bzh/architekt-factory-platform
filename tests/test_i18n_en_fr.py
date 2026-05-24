"""Regression tests: platform UI i18n limited to English and French."""
from __future__ import annotations

import pytest

from platform.i18n import (
    DEFAULT_LANG,
    SUPPORTED_LANGS,
    _catalog,
    get_lang,
    normalize_lang,
    reload_catalog,
)


class _FakeRequest:
    def __init__(self, cookies=None, accept_language=""):
        self.cookies = cookies or {}
        self.headers = {"accept-language": accept_language}


def test_supported_langs_are_en_fr_only():
    assert SUPPORTED_LANGS == ("en", "fr")
    assert DEFAULT_LANG == "en"


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("en", "en"),
        ("EN", "en"),
        ("fr-FR", "fr"),
        ("de", "en"),
        ("zh", "en"),
        ("", "en"),
        (None, "en"),
    ],
)
def test_normalize_lang(raw, expected):
    assert normalize_lang(raw) == expected


def test_get_lang_from_sf_lang_cookie():
    req = _FakeRequest(cookies={"sf_lang": "fr"})
    assert get_lang(req) == "fr"


def test_get_lang_legacy_lang_cookie():
    req = _FakeRequest(cookies={"lang": "fr"})
    assert get_lang(req) == "fr"


def test_get_lang_unsupported_cookie_falls_back_to_accept():
    req = _FakeRequest(cookies={"sf_lang": "zh"}, accept_language="fr-FR,fr;q=0.9")
    assert get_lang(req) == "fr"


def test_get_lang_accept_language():
    req = _FakeRequest(accept_language="de-DE,de;q=0.9,fr;q=0.8,en;q=0.5")
    assert get_lang(req) == "fr"


def test_catalog_only_en_fr():
    reload_catalog()
    assert set(_catalog.keys()) == {"en", "fr"}
    assert len(_catalog["en"]) > 30
    assert len(_catalog["fr"]) > 30


def test_api_i18n_unsupported_returns_en_catalog(client):
    en = client.get("/api/i18n/en.json").json()
    zh = client.get("/api/i18n/zh.json").json()
    assert zh == en


def test_set_lang_unsupported_normalizes_to_en(client):
    r = client.get("/api/set-lang/zh", follow_redirects=False)
    assert r.status_code == 303
    assert r.cookies.get("sf_lang") == "en"
