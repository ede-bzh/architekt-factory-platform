# Architekt — Roadmap produit

Plateforme multi-agents SAFe pour le cycle de vie logiciel. UI **EN / FR** uniquement.

## Livré (base actuelle)

| Domaine | État |
|---------|------|
| Agents & patterns | 150+ agents, 12 patterns DB, orchestration missions |
| SAFe | Portfolio, WSJF, PI, sprints, backlog |
| Qualité | Garde adversarial L0/L1, TDD workflows, auto-heal |
| i18n UI | Anglais + français (`platform/i18n`) |
| Observabilité | Métriques DORA, traces LLM, SSE live |

## Vague A — Identité & hygiène (en cours)

- Rebranding UI Architekt (templates, manifest, clés API `ARCHITEKT_API_KEY`)
- Suppression code mort (`dashboard/platform/`, `platform/orchestrator/`, doublons sécurité)
- Docs README EN/FR, `.env.example`, tests anti-branding Macaron dans l’UI

## Vague B — Documentation

- `docs/ROADMAP.md` (ce fichier), resync `platform/SPECS.md` §15
- Wiki plateforme EN/FR, captures `docs/screenshots/{en,fr}`

## Vague C — Rationalisation

- Aligner chiffres agents/workflows dans docs
- Réduire dépendances docs multilingues hors UI

## Vague D — Déploiements clients

- Sync La Poste isolé dans `tools/laposte-sync/`
- GitLab CI squelette sans trigger Macaron legacy

## Vague E — Infra (planifié, hors scope auto)

- Renommage package Docker `macaron_platform` → nécessite runbook prod (RTO/RPO)

## Références

- Spécifications détaillées : `platform/SPECS.md`
- Backlog technique : issues GitHub `ede-bzh/architekt-factory-platform`
