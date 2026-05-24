# Architekt — Catalogue technos (tierisé A/B/C)

> Ce que l'agence sait faire, où, par qui, et **dans quelles conditions**.
> Règle d'or : **on n'équipe qu'à la commande**. Et on **tiers** pour éviter la dispersion.

## Légende tiers

- **Tier A — Core, maîtrisé** : projets vendables **immédiatement**. Équipe à jour, CI, agents prêts, runbook.
- **Tier B — Opportuniste** : équipable en **1-3 jours** sur signature client. Pas d'investissement avant.
- **Tier C — Sur contrat signé d'avance** : nécessite équipement lourd (image Docker, agent dédié, formation). Premium pricing.
- **Hors scope** : explicitement non couvert.

## Tier A — Core

Projets Architekt vendables sans délai d'équipement.

| Famille | Stack | Agent référent | Build | Statut plateforme |
|---------|-------|----------------|-------|------------------|
| Site contenu | **Astro 5** + Tailwind v4 + shadcn/ui | `lead_frontend` | npm | ⚠️ à équiper (1 j) |
| Site + app léger | **Next.js 15** + Tailwind v4 + shadcn/ui | `lead_frontend` | npm | 🟡 partiel |
| Back-end Python | **FastAPI** + PostgreSQL | `lead_backend` | Docker, py_compile | ✅ prêt |
| DB | **PostgreSQL** (Supabase ou managé) | `lead_backend` | psql, Alembic | ✅ prêt |
| UI | **Tailwind v4 + shadcn/ui** | `lead_frontend` | tw build | ⚠️ à équiper (1 j) |
| Hébergement static | **Cloudflare Pages** | `devops` | wrangler | ⚠️ à équiper (1 j) |
| CI | **GitHub Actions** | `devops` | yaml | ⚠️ à équiper (0,5 j) |

Tous les projets Tier A doivent être **livrables** au plus tard à la fin de Phase 2.

## Tier B — Opportuniste

Activables sur signature client. Pas d'investissement avant.

| Famille | Stack | Délai équipement | Marge spéciale |
|---------|-------|------------------|----------------|
| CMS classique | **WordPress** + ACF + Yoast | 2 j | Normale |
| E-commerce | **Shopify** (classic) ou Headless Shopify + Next | 2 j | Normale |
| CMS headless | **Payload CMS 3** | 1 j | Normale |
| Back-end Node | **NestJS** + Prisma + PostgreSQL | 1 j | Normale |
| Site Vue | **Nuxt 3** | 1 j | Normale |
| Cloud Azure (client Azure) | Azure App Service / AKS | 3 j | + 10 % |
| Cloud AWS (client AWS) | ECS / RDS / Lambda | 3 j | + 10 % |

## Tier C — Contrat signé d'avance

Ne **jamais** équiper sans contrat. Premium pricing obligatoire.

| Famille | Stack | Pourquoi Tier C | Premium |
|---------|-------|------------------|---------|
| Back-end Java | **Spring Boot + Spring Modulith** | Image JDK + agent dédié + courbe Java | + 25 % |
| Mobile iOS | **SwiftUI** | macOS + Xcode + signature Apple | + 30 % |
| Mobile Android | **Kotlin + Compose** | Image Docker SDK + tests émulateur | + 25 % |
| Multi-tenant SaaS | tenant isolation + billing | Complexité ops + sécurité | + 40 % |
| Kubernetes | EKS / AKS / GKE | Compétence ops dédiée | + 30 % |
| Modèles IA fine-tunés | LLM fine-tuning, RAG complexe | GPU + dataset + MLOps | + 40 % |
| Data Engineering | dbt + Snowflake / BigQuery | Domaine spécialisé | + 30 % |

## Hors scope explicite (refus poli)

- 🚫 **React Native / Flutter** — préférer natif (Tier C) ou web responsive
- 🚫 **.NET / C#** — pas demandé, ouvrir si gros contrat
- 🚫 **Ruby on Rails** — idem
- 🚫 **Drupal / Joomla** — préférer WordPress
- 🚫 **Magento** — préférer Shopify
- 🚫 **Wordpress legacy < 6.0** — refuser ou audit only
- 🚫 **Salesforce / SAP customization** — pas notre métier
- 🚫 **Blockchain dev** — pas notre métier
- 🚫 **Game dev** — pas notre métier

## Patterns d'architecture par défaut

| Type de projet | Pattern (ADR-002) |
|----------------|-------------------|
| Site vitrine | **JAMStack** (Astro + headless CMS) |
| App B2B | **Modular Monolith** (Next.js + NestJS/FastAPI) |
| Grande app | **Modular Monolith** au début → extraire 1 service si vrai besoin |
| E-commerce | **Headless** (Shopify backend + Next.js front) ou Shopify classic |
| Mobile | Natif + back-end FastAPI/NestJS partagé |
| AI workflow | Orchestrateur (Architekt Platform) + LLM API + DB + UI |

Référence marché 2026 : modular monolith confirmé par Shopify, Amazon Prime Video, Spring Modulith.

## Données

- **Base par défaut** : **PostgreSQL** (managé : Supabase, RDS, Azure Database, Neon).
- **Cache** : Redis ou Cloudflare KV selon le déploiement.
- **Search** : PostgreSQL FTS d'abord, Meilisearch si besoin.
- **Files / images** : S3-compatible (**Cloudflare R2** préféré, ASEAN-friendly, sans egress fee).
- **Backups** : snapshots quotidiens + PITR 7 jours (cf. ADR-018).

## Hébergement par cas

| Type de projet | Recommandation 1 | Recommandation 2 |
|----------------|------------------|------------------|
| Site Architekt (vitrine) | Cloudflare Pages | Vercel |
| Sites clients Astro/Next | Cloudflare Pages | Vercel |
| Backend Node/Python | Fly.io (ap-southeast) | Hetzner CAX |
| WordPress | Kinsta (Asia-Pacific node) | WP Engine |
| Shopify | Shopify hosting (forcé) | — |
| Plateforme Architekt | VM Hetzner CAX11 | Azure existant |
| Client AWS imposé | EKS Fargate ap-southeast-1 | ECS + RDS |
| Client Azure imposé | AKS Southeast Asia | App Service + Azure DB |

## Activation d'une nouvelle ligne (Tier B/C)

À reproduire à chaque trigger commercial :

1. **Issue GitHub** `kit:<stack>` (template `chore.yml`) + label tier
2. **Agent YAML** dans `platform/skills/definitions/<role>.yaml`
3. **Image Docker** si build spécifique (modèle `android-builder`)
4. **Workflow kit** dans `platform/workflows/definitions/<stack>-epic.yaml`
5. **Documentation catalog** `docs/catalog/<stack>.md` (commandes, gotchas)
6. **Premier projet client** = projet de **validation du kit**
7. **Retour d'expérience** dans `docs/case-studies/<client>.md`

Budget temps : selon tier (B : 1-3 j, C : 5-15 j).

## Évolution du catalogue

Le catalogue est **vivant**. Règles :

- **Promotion** Tier B → A : après 2 projets livrés avec succès + agent stable
- **Rétrogradation** A → B : si > 6 mois sans projet, dette technique non maintenue
- **Sortie** : si la stack ne se vend plus, on archive `docs/catalog/<stack>.md`

Revue trimestrielle : CTO + CPO ensemble.
