# Architekt — Roadmap produit

Plateforme multi-agents SAFe pour le cycle de vie logiciel. UI **EN / FR** uniquement.

## Livré (base actuelle)

| Domaine | État |
|---------|------|
| Agents & patterns | 160+ agents, 12 patterns DB, 41 workflows builtin |
| SAFe | Portfolio, WSJF, PI, sprints, backlog |
| Qualité | Garde adversarial L0/L1, TDD workflows, auto-heal |
| i18n UI | Anglais + français (`platform/i18n`) |
| Identité | Rebrand UI Architekt, `ARCHITEKT_API_KEY`, thème `architekt_theme` |
| Observabilité | Métriques DORA, traces LLM, SSE live |

## Vague A — Identité & hygiène ✅

- Rebranding UI Architekt (templates, manifest, clés API)
- Suppression code mort (`dashboard/platform/`, `platform/orchestrator/`, doublons sécurité)
- Tests anti-branding Macaron dans l’UI

## Vague B — Documentation ✅ (cette branche)

- `docs/ROADMAP.md`, `platform/SPECS.md` §14.4 i18n
- Wiki EN/FR (`docs/wiki/`), captures README `docs/screenshots/{en,fr}` uniquement dans le dépôt
- `.env.example` aligné Architekt

## Vague C — Rationalisation ✅ (cette branche)

- Chiffres agents/workflows alignés dans README et wiki
- Wiki Home pages hors EN/FR retirées

## Vague D — Déploiements clients ✅

- Sync externe legacy supprimé (outil de sync miroir retiré du dépôt)
- GitLab CI squelette sans trigger Macaron legacy

## Vague E — Infra (planifié, hors scope auto)

- Renommage package Docker `macaron_platform` → nécessite runbook prod (RTO/RPO)

## Références
- Audit factuel (tests + vérifications) : `docs/AUDIT_REBRAND.md`

- Spécifications détaillées : `platform/SPECS.md`
- Backlog technique : issues GitHub `ede-bzh/architekt-factory-platform`


## Vague 6 — Fondations post-rebrand (en cours)

- `platform/VERSION` + `CHANGELOG.md` + `docs/architekt/RELEASE.md`
- CI : bandit + pip-audit bloquants ; deploy après CI verte
- Monitoring extrait (`platform/metrics/live.py`), cache 20s
- L2 + L1 fail-closed ; rate limit unifié ; HITL deploy API
