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

## Vague 6 — Fondations post-rebrand ✅

> Release **v2.3.0** (`main`, PR #11).

- `platform/VERSION` + `CHANGELOG.md` + `docs/architekt/RELEASE.md`
- CI : bandit + pip-audit bloquants ; deploy après CI verte
- Monitoring extrait (`platform/metrics/live.py`), cache 20s
- L2 + L1 fail-closed ; rate limit unifié ; HITL deploy API

## Vague 7 — Parallèle (PR #12 / #13)

- Doc ops (Darwin, DPA, HITL), mutation testing, dashboard legacy :8080, CSP

## Vague 8 — Documentation complète & rebrand doc (backlog)

> **Cadrage** — audit : `docs/architekt/REBRAND-DOC-AUDIT.md`  
> Tâches : `docs/architekt/PLATFORM-BACKLOG.md` § Wave 8.

- Wiki EN/FR, README, API/Security/Patterns — fin Macaron / La Poste côté utilisateur
- Complétion sections wiki minimales ; archivage Home hors EN/FR
- `CLAUDE.md` studio + gates tests doc

## Références

- Audit UI (vagues A–E) : `docs/AUDIT_REBRAND.md`
- Audit doc & complétude (Wave 8) : `docs/architekt/REBRAND-DOC-AUDIT.md`
- Backlog plateforme : `docs/architekt/PLATFORM-BACKLOG.md`
- Spécifications : `platform/SPECS.md`
- Issues : https://github.com/ede-bzh/architekt-factory-platform/issues
