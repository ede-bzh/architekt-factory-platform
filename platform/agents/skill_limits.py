"""Role-based caps for Architekt skill injection."""

from __future__ import annotations

import os

_DEFAULT_MAX = int(os.environ.get("MAX_ARCHITEKT_SKILLS", "14"))

_ROLE_CAPS: dict[str, int] = {
    "dev": 14,
    "lead": 14,
    "backend": 14,
    "frontend": 12,
    "qa": 12,
    "test": 12,
    "security": 10,
    "architect": 10,
    "product": 8,
    "devops": 10,
    "default": 8,
}


def max_architekt_skills_for_role(agent_role: str) -> int:
    """Return max skills to inject for a role (env MAX_ARCHITEKT_SKILLS caps default)."""
    role = (agent_role or "").lower()
    cap = _DEFAULT_MAX
    for key, limit in _ROLE_CAPS.items():
        if key != "default" and key in role:
            cap = max(cap, min(limit, _DEFAULT_MAX))
    return min(cap, _DEFAULT_MAX)
