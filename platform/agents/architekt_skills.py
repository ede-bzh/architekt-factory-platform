"""Architekt doctrine skills — role/keyword injection into agent prompts."""

from __future__ import annotations

import re

from ..skills.library import get_skill_library

# ── Role sets ────────────────────────────────────────────────────

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

_ARCHI_ROLES = frozenset(
    {
        "enterprise_architect",
        "architecte",
        "solution_architect",
        "cloud_architect",
        "system_architect_art",
        "mobile_archi",
        "security-architect",
        "strat-cto",
        "brain",
    }
)

_TECH_ROLES = frozenset(
    {
        "dev",
        "dev_backend",
        "dev_frontend",
        "dev_fullstack",
        "lead_dev",
        "lead_backend",
        "lead_frontend",
        "dev_mobile",
        "dev_tma",
        "ml_engineer",
        "plat-dev-backend",
        "plat-dev-frontend",
        "plat-dev-agents",
        "plat-dev-patterns",
        "plat-tma-dev-back",
        "plat-tma-dev-front",
        "plat-tma-dev-agents",
        "plat-lead-dev",
        "plat-tma-lead",
    }
)

_UX_ROLES = frozenset(
    {
        "ux_designer",
        "mobile_ux",
        "solaris_ux_designer",
        "solaris_ui_developer",
        "dev_frontend",
        "lead_frontend",
        "rse-a11y",
        "accessibility_expert",
        "solaris_design_qa",
    }
)

_DATA_ROLES = frozenset(
    {
        "data_engineer",
        "data_analyst",
        "dba",
        "ml_engineer",
    }
)

_SECURITY_ROLES = frozenset(
    {
        "ciso",
        "securite",
        "devsecops",
        "pentester-lead",
        "exploit-dev",
        "security-architect",
        "secops-engineer",
        "security-dev-lead",
        "security-backend-dev",
        "security-frontend-dev",
        "qa-security",
        "security-researcher",
    }
)

_SRE_ROLES = frozenset(
    {
        "sre",
        "devops",
        "pipeline_engineer",
        "plat-dev-infra",
        "backup-ops",
        "monitoring-ops",
        "canary-deployer",
        "iac-engineer",
    }
)

_DELIVERY_ROLES = frozenset(
    {
        "chef_projet",
        "pmo",
        "chef_de_programme",
        "release_train_engineer",
        "scrum_master",
        "agile_coach",
        "responsable_tma",
        "strat-dirprog",
        "plat-tma-lead",
        "solution_train_engineer",
    }
)

_PRODUCT_ROLES = frozenset(
    {
        "product_manager",
        "product_owner",
        "metier",
        "business_owner",
        "epic_owner",
        "plat-product",
        "change_manager",
    }
)

_FINOPS_ROLES = frozenset(
    {
        "strat-cpo",
        "strat-dirprog",
        "strat-portfolio",
        "lean_portfolio_manager",
        "dsi",
        "pmo",
        "chef_projet",
    }
)

_AI_GOV_ROLES = frozenset(
    {
        "brain",
        "strat-cto",
        "rse-ethique-ia",
    }
)

_COMMERCIAL_ROLES = frozenset(
    {
        "business_owner",
        "metier",
        "strat-cpo",
        "solution_manager",
        "change_manager",
        "mkt-cmo",
    }
)

_QA_ROLES = frozenset(
    {
        "qa_lead",
        "test_automation",
        "qa-security",
        "testeur",
        "performance_engineer",
        "mobile_android_qa",
        "mobile_ios_qa",
        "plat-tma-qa",
        "solaris_design_qa",
    }
)

# ── Keyword triggers ─────────────────────────────────────────────

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

_ARCHI_KW = re.compile(
    r"\b(modular monolith|microservice|architecture pattern|c4 model|stack decision|"
    r"adr projet|system design)\b",
    re.I,
)

_TECH_KW = re.compile(
    r"\b(tdd|mutation test|12-?factor|test coverage|refactor|unit test|ci pipeline)\b",
    re.I,
)

_UX_KW = re.compile(
    r"\b(shadcn|design system|wcag|a11y|tailwind|radix|ui component|dark mode)\b",
    re.I,
)

_DATA_KW = re.compile(
    r"\b(postgres|postgresql|migration|schema design|rpo|rto|data retention|"
    r"database model|pgvector)\b",
    re.I,
)

_SECURITY_KW = re.compile(
    r"\b(asvs|sbom|sast|sca|pentest|owasp|secrets scan|supply chain|threat model)\b",
    re.I,
)

_SRE_KW = re.compile(
    r"\b(slo|runbook|deploy|hosting|backup|restore|otel|monitoring|infra|hetzner|"
    r"cloudflare pages|incident response)\b",
    re.I,
)

_DELIVERY_KW = re.compile(
    r"\b(discovery phase|hardening|handover|scope creep|definition of done|"
    r"mission phase|out-of-scope|sow)\b",
    re.I,
)

_PRODUCT_KW = re.compile(
    r"\b(jtbd|jobs.to.be.done|persona|user interview|hypothesis|problem statement|"
    r"user journey|discovery workshop)\b",
    re.I,
)

_FINOPS_KW = re.compile(
    r"\b(budget mission|marge|margin|llm cost|finops|pricing|cost overrun|"
    r"auto-pause|heures mission)\b",
    re.I,
)

_AI_GOV_KW = re.compile(
    r"\b(human approval|audit log|L3 action|L4 action|ai governance|"
    r"agent audit|opt-out ia)\b",
    re.I,
)

_COMMERCIAL_KW = re.compile(
    r"\b(lead qualif|devis|quote|bant|pipeline commercial|prospect|négociation|"
    r"commercial funnel)\b",
    re.I,
)

_QA_KW = re.compile(
    r"\b(quality report|hardening qa|lighthouse|playwright e2e|mutation score|"
    r"axe-core|pre-prod gate)\b",
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

_STRATEGIC_MANDATORY = ("architekt-compliance", "architekt-i18n")

_SKILL_RULES: list[tuple[str, frozenset[str], re.Pattern[str]]] = [
    ("architekt-compliance", _COMPLIANCE_ROLES, _COMPLIANCE_KW),
    ("architekt-i18n", _I18N_ROLES, _I18N_KW),
    ("architekt-archi", _ARCHI_ROLES, _ARCHI_KW),
    ("architekt-tech", _TECH_ROLES, _TECH_KW),
    ("architekt-ux", _UX_ROLES, _UX_KW),
    ("architekt-data", _DATA_ROLES, _DATA_KW),
    ("architekt-security", _SECURITY_ROLES, _SECURITY_KW),
    ("architekt-sre", _SRE_ROLES, _SRE_KW),
    ("architekt-delivery", _DELIVERY_ROLES, _DELIVERY_KW),
    ("architekt-product", _PRODUCT_ROLES, _PRODUCT_KW),
    ("architekt-finops", _FINOPS_ROLES, _FINOPS_KW),
    ("architekt-ai-governance", _AI_GOV_ROLES, _AI_GOV_KW),
    ("architekt-commercial", _COMMERCIAL_ROLES, _COMMERCIAL_KW),
    ("architekt-qa", _QA_ROLES, _QA_KW),
]

MAX_ARCHITEKT_SKILLS = 4
_MAX_SKILL_CHARS = 3500


def _cap_architekt_skills(selected: list[str], role_key: str) -> list[str]:
    """Compliance + i18n first for strategic orchestrators, then fill up to cap."""
    if role_key in _STRATEGIC_ORCHESTRATORS:
        mandatory = [sid for sid in _STRATEGIC_MANDATORY if sid in selected]
        for sid in _STRATEGIC_MANDATORY:
            if sid not in mandatory:
                mandatory.append(sid)
        rest = [sid for sid in selected if sid not in mandatory]
        ordered = mandatory + rest
    else:
        ordered = selected
    return ordered[:MAX_ARCHITEKT_SKILLS]


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
    """Choose Architekt doctrine skills for this agent turn."""
    ctx = mission_description or ""
    role_key = (agent_id or agent_role or "").lower()
    selected: list[str] = []

    for skill_id, roles, keywords in _SKILL_RULES:
        if role_key in roles or keywords.search(ctx):
            if skill_id not in selected:
                selected.append(skill_id)

    if role_key in _STRATEGIC_ORCHESTRATORS:
        for sid in _STRATEGIC_MANDATORY:
            if sid not in selected:
                selected.append(sid)

    return _cap_architekt_skills(selected, role_key)


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
