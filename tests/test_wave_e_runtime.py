"""Wave E — runtime package detection (ADR-001 niveau 3)."""

from __future__ import annotations

from pathlib import Path

import pytest

from platform.runtime import (
    LEGACY_PACKAGE,
    RUNTIME_PACKAGE,
    container_code_dir,
    default_otel_service_name,
    runtime_module,
    runtime_package_name,
)


def test_local_dev_uses_platform_package():
    assert runtime_package_name() == "platform"
    assert container_code_dir() is None
    assert runtime_module("server") == "platform.server"


def test_default_otel_service_name():
    assert default_otel_service_name() == "architekt-platform"


@pytest.mark.parametrize(
    "layout,expected_pkg",
    [
        (RUNTIME_PACKAGE, RUNTIME_PACKAGE),
        (LEGACY_PACKAGE, LEGACY_PACKAGE),
    ],
)
def test_container_package_detection(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, layout: str, expected_pkg: str
):
    app = tmp_path / "app"
    pkg = app / layout
    pkg.mkdir(parents=True)
    (pkg / "server.py").write_text("# stub\n", encoding="utf-8")
    monkeypatch.setattr("platform.runtime.APP_ROOT", app)
    assert runtime_package_name() == expected_pkg
    assert container_code_dir() == pkg
    assert runtime_module("mcp_platform.server") == f"{expected_pkg}.mcp_platform.server"


def test_architekt_preferred_over_legacy_symlink(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    app = tmp_path / "app"
    primary = app / RUNTIME_PACKAGE
    primary.mkdir(parents=True)
    legacy = app / LEGACY_PACKAGE
    legacy.symlink_to(RUNTIME_PACKAGE, target_is_directory=True)
    monkeypatch.setattr("platform.runtime.APP_ROOT", app)
    assert runtime_package_name() == RUNTIME_PACKAGE
    assert container_code_dir() == primary
