# Architekt — Catalogue technos

> Ce que l'agence sait faire, ce qu'elle n'a pas encore équipé, et qui s'en occupe.
> Règle d'or : **on n'équipe qu'à la commande**. Pas d'investissement spéculatif.

## Légende statut

- ✅ **Prêt** — agent existant, outils fonctionnels, déjà testé
- 🟡 **Partiel** — base présente, manque agent dédié ou pipeline build
- ⚠️ **À équiper** — ajouter sur 1er projet client de cette stack
- 🚫 **Hors scope** — explicitement non couvert (à ce stade)

## Tableau maître

| # | Famille | Stack | Statut | Agent référent | Build / runtime | Marché 2026 |
|---|---------|-------|--------|----------------|-----------------|-------------|
| 1 | Site contenu | **Astro 5** + Tailwind v4 + shadcn/ui | ⚠️ | `lead_frontend` | npm + Cloudflare Pages | Défaut sites contenu |
| 2 | Site + app léger | **Next.js 15** + Tailwind v4 + shadcn/ui | 🟡 | `lead_frontend` | npm + Vercel/Cloudflare | Standard agence |
| 3 | Site Vue | **Nuxt 3** + Vue 3 | ⚠️ | `lead_frontend` | npm | Si client Vue |
| 4 | WordPress classique | WP + ACF + Yoast | ⚠️ | nouveau `wp_dev` | PHP/MySQL/Kinsta | Sites marketing |
| 5 | E-commerce | Shopify (classic) ou Headless Shopify + Next | ⚠️ | nouveau `shopify_dev` | Shopify CLI | E-commerce |
| 6 | Back-end Python | **FastAPI** + PostgreSQL | ✅ | `lead_backend` | Docker, py_compile | Votre force |
| 7 | Back-end Node | **NestJS** + Prisma + PostgreSQL | ⚠️ | nouveau `nest_dev` | npm + Docker | Standard 2026 |
| 8 | Back-end Java | **Spring Boot + Spring Modulith** | ⚠️ | nouveau `spring_dev` | Maven/Gradle + JDK 21 Docker | Modular monolith Java |
| 9 | Mobile iOS | **SwiftUI** | ✅ | `mobile_ios_lead` | xcodebuild | — |
| 10 | Mobile Android | **Kotlin + Jetpack Compose** | ✅ | `mobile_android_lead` | Docker android-builder | — |
| 11 | CMS headless | **Payload CMS 3** ou Strapi | ⚠️ | `lead_backend` | Node + PostgreSQL | Montée 2026 |

## Hors scope explicite

- 🚫 React Native (préférer natif via 9/10 ou web responsive via 1/2)
- 🚫 Flutter (idem)
- 🚫 .NET / C# (pas demandé, ouvrir si client)
- 🚫 Ruby on Rails (idem)
- 🚫 Drupal / Joomla (préférer WordPress)
- 🚫 Magento (préférer Shopify)

## Patterns d'architecture par défaut

| Type de projet | Pattern |
|----------------|---------|
| Site vitrine | **JAMStack** (Astro + headless CMS) |
| App B2B | **Modular Monolith** (Next.js + NestJS/FastAPI) |
| Grande app | **Modular Monolith** au début → extraire 1 service si vrai besoin |
| E-commerce | **Headless** (Shopify backend + Next.js front) ou Shopify classic |
| Mobile | Natif + back-end FastAPI/NestJS partagé |

**Référence marché 2026** : modular monolith confirmé par Shopify, Amazon Prime Video (rollback de microservices vers monolith, -90% coût).

## Données

- **Base par défaut** : PostgreSQL (managé : Supabase, RDS, Azure Database).
- **Cache** : Redis ou Cloudflare KV selon le déploiement.
- **Search** : PostgreSQL FTS d'abord, Meilisearch si besoin.
- **Files / images** : S3-compatible (Cloudflare R2 préféré, ASEAN-friendly).

## Hébergement

| Type | Recommandation |
|------|----------------|
| Sites Astro/Next | Cloudflare Pages (edge global incluant Asie) |
| Vercel | Alternative pour Next.js si DX prioritaire |
| Backend Node/Python | Fly.io, Railway, ou conteneurs sur cloud client |
| WordPress | Kinsta (Asia-Pacific node) |
| Shopify | Shopify hosting (forcé) |
| Plateforme Architekt elle-même | VM Hetzner ARM (5 €/mois) ou Azure existant |

## Activation d'une nouvelle ligne

Quand un client signe sur une stack marquée ⚠️ :

1. Créer issue GitHub `kit:<stack>` avec template `chore.yml`.
2. Ajouter agent YAML dans `platform/skills/definitions/<role>.yaml`.
3. Ajouter image Docker si build spécifique (cf. `android-builder`).
4. Créer kit workflow dans `platform/workflows/definitions/<stack>-epic.yaml`.
5. Documenter dans `docs/catalog/<stack>.md` (commandes build, déploiement, gotchas).
6. Premier projet client = projet de validation du kit.

Budget temps : 1-3 jours par stack selon complexité.

## Suivi

Cette page liste l'état général. Les détails techniques (commandes build, Dockerfile, agent prompts) vont dans `docs/catalog/<stack>.md` au moment de l'activation.
