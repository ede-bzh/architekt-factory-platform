"""Architekt doctrine skills — compliance & i18n injection into agent prompts."""

from __future__ import annotations

import re

from ..skills.library import get_skill_library

_COMPLIANCE_ROLES = frozenset(
    {
        "compliance_officer",
        "rse-dpo",
        "rse-juriste",
        "rse-manager",
        "ciso",
        "securite",
        "devsecops",
        "brain",
        "strat-cto",
        "strat-cpo",
        "strat-dirprog",
        "strat-portfolio",
        "enterprise_architect",
        "architecte",
        "solution_architect",
    }
)

_I18N_ROLES = frozenset(
    {
        "dev_frontend",
        "lead_frontend",
        "ux_designer",
        "rse-a11y",
        "accessibility_expert",
        "tech_writer",
        "solaris_ux_designer",
        "solaris_ui_developer",
        "product_manager",
        "metier",
    }
)

_COMPLIANCE_KW = re.compile(
    r"\b(gdpr|rgpd|pdpa|pdpl|ccpa|soc2|dpa|compliance|données personnelles|"
    r"personal data|sub-?processor|data residency|breach)\b",
    re.I,
)

_I18N_KW = re.compile(
    r"\b(i18n|l10n|rtl|locale|traduction|translation|multilingue|multi-?language|"
    r"arabic|arabe|icu|next-intl|globaliz)\b",
    re.I,
)

_STRATEGIC_ORCHESTRATORS = frozenset(
    {
        "brain",
        "strat-cto",
        "strat-cpo",
        "strat-dirprog",
        "strat-portfolio",
    }
)

_MAX_SKILL_CHARS = 3500


def _skill_excerpt(skill_id: str) -> str:
    lib = get_skill_library()
    lib.scan_all()
    skill = lib.get(skill_id)
    if not skill:
        return ""
    body = getattr(skill, "content", None) or ""
    if len(body) > _MAX_SKILL_CHARS:
        body = body[:_MAX_SKILL_CHARS] + "\n\n[... doctrine tronquée — skill complet en repo]"
    name = getattr(skill, "name", None) or skill_id
    return f"### {name}\n{body}"


def select_architekt_skill_ids(
    agent_id: str,
    agent_role: str,
    mission_description: str | None = None,
) -> list[str]:
    """Choose architekt-compliance / architekt-i18n for this agent turn."""
    ctx = mission_description or ""
    role_key = (agent_id or agent_role or "").lower()
    selected: list[str] = []

    if role_key in _COMPLIANCE_ROLES or _COMPLIANCE_KW.search(ctx):
        selected.append("architekt-compliance")

    if role_key in _I18N_ROLES or _I18N_KW.search(ctx):
        selected.append("architekt-i18n")

    if role_key in _STRATEGIC_ORCHESTRATORS:
        for sid in ("architekt-compliance", "architekt-i18n"):
            if sid not in selected:
                selected.append(sid)

    return selected


def inject_architekt_skills(
    agent_id: str,
    agent_role: str,
    mission_description: str | None = None,
) -> str:
    """Build prompt section for Architekt doctrine skills (may be empty)."""
    ids = select_architekt_skill_ids(agent_id, agent_role, mission_description)
    if not ids:
        return ""

    parts = ["\n## Architekt studio — doctrine (skills obligatoires)"]
    for sid in ids:
        excerpt = _skill_excerpt(sid)
        if excerpt:
            parts.append(excerpt)
    return "\n\n".join(parts) if len(parts) > 1 else ""
