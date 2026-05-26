"""Wave E — runtime package detection (ADR-001 niveau 3)."""

from __future__ import annotations

from pathlib import Path

import pytest

from platform.runtime import (
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


def test_container_package_detection(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    app = tmp_path / "app"
    pkg = app / RUNTIME_PACKAGE
    pkg.mkdir(parents=True)
    (pkg / "server.py").write_text("# stub\n", encoding="utf-8")
    monkeypatch.setattr("platform.runtime.APP_ROOT", app)
    assert runtime_package_name() == RUNTIME_PACKAGE
    assert container_code_dir() == pkg
    assert runtime_module("mcp_platform.server") == f"{RUNTIME_PACKAGE}.mcp_platform.server"
