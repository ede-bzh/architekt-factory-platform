"""Container/runtime package detection (ADR-001 wave E).

Repo layout uses ``platform/``; production Docker images install code as
``architekt_platform`` at ``/app/architekt_platform/``.
"""

from __future__ import annotations

import os
from pathlib import Path

RUNTIME_PACKAGE = "architekt_platform"
APP_ROOT = Path("/app")


def container_code_dir() -> Path | None:
    """Package directory inside Docker, or None in local dev."""
    primary = APP_ROOT / RUNTIME_PACKAGE
    return primary if primary.is_dir() else None


def runtime_package_name() -> str:
    """Import name: ``platform`` (dev) or ``architekt_platform`` (container)."""
    code_dir = container_code_dir()
    return RUNTIME_PACKAGE if code_dir is not None else "platform"


def runtime_module(subpath: str) -> str:
    """Dotted module path under the active runtime package."""
    return f"{runtime_package_name()}.{subpath}"


def default_otel_service_name() -> str:
    return os.environ.get("OTEL_SERVICE_NAME", "architekt-platform")


def default_pg_database() -> str:
    return os.environ.get("PG_DB", "architekt_platform")
