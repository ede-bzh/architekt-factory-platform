"""Container/runtime package detection (ADR-001 wave E).

Repo layout uses ``platform/``; production Docker images install code as
``architekt_platform`` with a legacy symlink ``macaron_platform`` (6 months).
"""

from __future__ import annotations

import os
from pathlib import Path

RUNTIME_PACKAGE = "architekt_platform"
LEGACY_PACKAGE = "macaron_platform"
APP_ROOT = Path("/app")


def container_code_dir() -> Path | None:
    """Primary package directory inside Docker, or None in local dev."""
    primary = APP_ROOT / RUNTIME_PACKAGE
    if primary.is_dir():
        return primary
    legacy = APP_ROOT / LEGACY_PACKAGE
    if legacy.is_dir():
        return legacy.resolve() if legacy.is_symlink() else legacy
    return None


def runtime_package_name() -> str:
    """Import name: ``platform`` (dev) or container package (prod)."""
    code_dir = container_code_dir()
    if code_dir is None:
        return "platform"
    return code_dir.name


def runtime_module(subpath: str) -> str:
    """Dotted module path under the active runtime package."""
    return f"{runtime_package_name()}.{subpath}"


def container_package_paths() -> list[Path]:
    """All container package roots (canonical + legacy symlink)."""
    paths: list[Path] = []
    for name in (RUNTIME_PACKAGE, LEGACY_PACKAGE):
        p = APP_ROOT / name
        if p.is_dir():
            resolved = p.resolve()
            if resolved not in paths:
                paths.append(resolved)
    return paths


def default_otel_service_name() -> str:
    return os.environ.get("OTEL_SERVICE_NAME", "architekt-platform")


def default_pg_database() -> str:
    """Default PG database for greenfield compose; prod keeps PG_DB in .env."""
    return os.environ.get("PG_DB", "architekt_platform")
