# Architekt — Roadmap produit & plateforme

> **Document maître.** Toute la planification Architekt (rebrand, technos, pratiques, pilote, scale) en une seule page.
> Mis à jour automatiquement par les agents quand une phase passe.

## Contexte

- **Architekt** = studio / agence digitale à créer à Singapour, ambition Asie (ASEAN).
- **Équipe** : 2 personnes (CPO + CTO).
- **Plateforme** = cet outil interne (anciennement *Software Factory*) qui orchestre des agents IA pour livrer des projets clients.
- **Repo** : `ede-bzh/architekt-factory-platform` (renommé le 2026-05-24 — ancien : `software-factory-macaron`).
- **État runtime aujourd'hui** : code sur GitHub uniquement, rien n'est déployé.

## Principes directeurs

1. **Studio d'abord, SaaS plus tard.** La plateforme reste un outil interne tant qu'on n'a pas 3 clients payants.
2. **Catalogue gouverné, pas catalogue spéculatif.** On n'équipe une nouvelle techno **que** quand un projet client la demande.
3. **Modular monolith par défaut** (consensus marché 2026 — Shopify, Amazon Prime Video, Spring Modulith).
4. **TDD + mutation testing** comme garde-fou qualité (Stryker JS/TS, mutmut Python, PIT Java).
5. **Design system standard** : shadcn/ui + Radix + Tailwind v4 (consensus marché 2026).
6. **Rien en prod sans CI verte + auth fail-closed.**

## Phases

| Phase | Nom | Durée cible | Livrable principal | Statut |
|-------|-----|-------------|-------------------|--------|
| **0** | Rebrand complet | 1 semaine | Repo + UI + docs en marque Architekt | À démarrer |
| **1** | Catalogue technos | 1 semaine | `docs/CATALOG.md` + 5 ADR | À démarrer |
| **2** | Doctrine bonnes pratiques | 1 semaine | 6 skills Architekt + CI qualité | À démarrer |
| **3** | Pilote site Architekt | 2 semaines | `architekt.TBD` en ligne | À démarrer |
| **4** | Équipement à la demande | continu | Kits stack ajoutés client par client | À démarrer |

Détails par phase : voir `docs/architekt/phase-{0..4}.md`.

## Vue d'ensemble

```
[ Phase 0 ]──[ Phase 1 ]──[ Phase 2 ]──[ Phase 3 ]──[ Phase 4 ]
  Rebrand   Catalogue    Doctrine     Pilote      On-demand
   1 sem      1 sem        1 sem       2 sem      continu
                                          │
                                          ▼
                              site architekt.TBD live
                              + 1 case study
                              + plateforme crédible
```

## Phase 0 — Rebrand complet (1 semaine)

**Objectif** : tout le repo, l'UI, les docs portent la marque **Architekt**.

| Niveau | Exemple |
|--------|---------|
| Visible | README, UI, login, emails → Architekt |
| Identifiants | `MACARON_API_KEY` → `ARCHITEKT_API_KEY`, package `macaron_platform` → `architekt_platform` |
| Marque | logo placeholder, palette CSS, domaine à choisir |

**Gate de passage** : commit `feat: rebrand to Architekt` mergé, CI verte, UI cohérente.

## Phase 1 — Catalogue technos (1 semaine)

**Objectif** : lister formellement ce qu'Architekt sait faire (et ne fait pas).

Sortie : `docs/CATALOG.md` avec **11 lignes** (Astro, Next.js 15, Nuxt 3, WordPress, Headless Shopify, FastAPI, NestJS, Spring Modulith, SwiftUI, Kotlin/Compose, Payload CMS).

Pour chaque ligne : statut (✅ prêt / ⚠️ à équiper), agent référent, exemple de projet, image Docker requise.

**Gate de passage** : catalogue mergé, 5 ADR clés écrits.

## Phase 2 — Doctrine bonnes pratiques (1 semaine)

**Objectif** : encoder les pratiques Architekt en **skills chargés automatiquement** par les agents.

| Fichier | Contenu |
|---------|---------|
| `skills/architekt-archi.md` | Modular monolith, ADR obligatoire, C4 |
| `skills/architekt-tech.md` | Twelve-Factor, TDD, mutation testing |
| `skills/architekt-ux.md` | shadcn/ui + Radix + Tailwind v4, WCAG 2.2 AA |
| `skills/architekt-data.md` | PostgreSQL, migrations versionnées, RPO/RTO |
| `skills/architekt-security.md` | SAST, OWASP, secrets en vault |
| `skills/architekt-sre.md` | SLO, error budget, runbook |

**Gate de passage** : 6 skills mergés, CI plateforme verte (pytest + lint + bandit).

## Phase 3 — Pilote site Architekt (2 semaines)

**Objectif** : `architekt.TBD` en ligne, fait par la plateforme.

**Stack** : Astro 5 + Tailwind v4 + shadcn/ui (recommandé) — alternative Next.js 15 si app interactive prévue rapidement.

**Hébergement** : Cloudflare Pages (edge Asie, quasi-gratuit).

**Pages** : Home / Offres / Méthode / Stacks / Équipe / Contact / Blog (EN + FR + ZH).

**Plateforme runtime** : VM Hetzner ARM ~5 €/mois OU local Mac OU Azure existant (à trancher).

**Gate de passage** : site accessible publiquement, rapport DORA + QualityScanner sur le projet pilote.

## Phase 4 — Équipement à la demande (continu)

| Trigger | Action |
|---------|--------|
| 1er client WordPress signé | Activer kit WordPress (1-2 j) |
| 1er client Shopify | Activer kit Shopify |
| 1er client Java | Activer kit Spring Modulith + image JDK |
| 3 clients actifs en parallèle | Augmenter concurrence missions (Semaphore > 1) |
| 5 clients | Ouvrir portail client read-only |

## Modèle Architekt

| Aspect | Choix |
|--------|-------|
| Société | Architekt Pte. Ltd. (Singapour) |
| Modèle | Studio / agence (pas SaaS au début) |
| Cible | Scale-ups + PME APAC, B2B |
| Cloud pilote | Azure existant ou Hetzner |
| Cloud cible | AWS ap-southeast-1 ou Azure SEA selon client |
| Licence | À trancher Phase 0 (AGPL vs commercial) |

## Décisions ouvertes (ADR à écrire)

| # | Décision | Statut |
|---|----------|--------|
| 001 | Rebrand Architekt + nommage | Phase 0 |
| 002 | Modular monolith par défaut | Phase 1 |
| 003 | Mutation testing (Stryker/mutmut/PIT) | Phase 1 |
| 004 | Design system (shadcn/ui + Radix + Tailwind v4) | Phase 1 |
| 005 | Hébergement pilote (Hetzner vs Azure vs Mac local) | Phase 3 |
| 006 | Licence du code plateforme | Phase 0 |
| 007 | Multi-tenant (quand et comment) | Phase 4+ |

## Indicateurs (à suivre dans GitHub Project)

| Indicateur | Cible Phase 3 | Cible Phase 4 |
|------------|--------------|---------------|
| CI verte sur `main` | 100% | 100% |
| Couverture mutation testing | ≥ 60% | ≥ 80% |
| Time-to-first-agent-message | < 5 min | < 2 min |
| Concurrence missions | 1 | ≥ 3 |
| Tenants isolés | non | oui |
| Rapport client exportable | oui | oui |
| SLO documentés par projet | oui | oui |

## Risques

| # | Risque | Mitigation |
|---|--------|-----------|
| R1 | Brûler 2 mois à équiper 11 stacks avant 1 client | Catalogue gouverné, à la demande |
| R2 | CI absente → impossible à vendre à un CTO client | Phase 2 obligatoire avant Phase 3 |
| R3 | Marque Macaron leak en prod | Phase 0 stricte, search/replace exhaustif |
| R4 | Coût LLM non maîtrisé en mission longue | Budget tokens/jour dans manifeste mission |
| R5 | Conflit licence AGPL vs revente projets clients | ADR 006 + avocat avant 1er contrat |

## Liens

- `docs/CATALOG.md` — catalogue technos
- `docs/architekt/phase-{0..4}.md` — guides détaillés
- `docs/adr/` — Architecture Decision Records
- `.github/labels.yml` — labels GitHub
- `scripts/github/setup-project.sh` — peuple GitHub Issues + Project + Milestones
