# Architekt — Stack decision matrix

> Quelle stack pour quel type de projet. Source de vérité décisionnelle.
> Référence : ADR-038.

## Principe

> **1 type de projet = 1 stack par défaut.** Variation seulement si justifiée explicitement (justification documentée dans ADR projet).

## Matrice maître

| Type de projet | Stack par défaut | Hébergement | Trigger d'exception |
|----------------|------------------|-------------|---------------------|
| Marketing site | **Astro + Tailwind + shadcn/ui** (+ CMS optionnel) | Cloudflare Pages | App très interactive → Next.js |
| Interactive web app | **Next.js + PostgreSQL + FastAPI/NestJS** | Vercel/Cloudflare/AWS/Azure selon client | — |
| Internal tool | **Next.js + FastAPI + PostgreSQL** + Auth (Clerk/Auth0/Azure AD/Google Workspace) | Fly.io / Hetzner / cloud client | — |
| AI workflow | **Python + FastAPI + background workers + PostgreSQL** | Hetzner / cloud client | Vector DB **uniquement** si retrieval prouvé nécessaire |
| E-commerce | **Shopify first** | Shopify hosting | Headless seulement si perf/UX/multi-region le justifient |
| Enterprise Java client | **Spring Modulith** | Selon client | **Trigger** : client a estate Java OU exigence enterprise |
| Mobile | **Responsive web / PWA en premier** | Web hosting | Native SwiftUI/Kotlin **uniquement** après besoin validé client |
| CMS-heavy | **WordPress** (équipe éditoriale non-technique) OU **Payload/headless** (modèle de contenu dev-driven) | Kinsta APAC / cloud | Choix basé sur **besoins éditeurs** |

## Choix d'auth par contexte

| Contexte client | Auth recommandée |
|-----------------|------------------|
| Startup / scale-up | **Clerk** ou **Auth0** |
| Enterprise (Microsoft shop) | **Azure AD** / Entra ID |
| Workspace Google | **Google Workspace SSO** |
| B2B avec SSO requis | OIDC / SAML générique |
| App grand public | Email + magic link + OAuth providers |

## Choix de base de données

| Cas | Recommandation |
|-----|----------------|
| Défaut | **PostgreSQL** (Supabase / RDS / Azure DB / Neon) |
| Read-heavy + cache | + Redis (Upstash / Cloudflare) |
| Search | PostgreSQL FTS d'abord, Meilisearch si vraiment besoin |
| Time-series | TimescaleDB (extension PostgreSQL) |
| Graph | PostgreSQL + pg_graph extensions ; Neo4j si dédié |
| Vector (AI) | **pgvector** d'abord, Pinecone/Weaviate seulement si justifié |

## Choix de file d'attente / async

| Cas | Recommandation |
|-----|----------------|
| Jobs courts | **Python RQ** ou **BullMQ** (Node) |
| Jobs longs | Celery (Python) ou BullMQ |
| Event streaming | NATS ou Redis Streams ; Kafka seulement enterprise |
| Cron | GitHub Actions schedule, Cloudflare Workers cron, ou cron VM |

## Choix de monitoring

| Cas | Recommandation |
|-----|----------------|
| Logs | Console structuré (JSON) → **Better Stack** ou **Loki self-hosted** |
| APM | **Sentry** (errors) + **OpenTelemetry** (traces) |
| Uptime | Checkly / Better Stack synthetic |
| Metrics | Prometheus self-hosted ou Cloudflare Analytics |

## Choix CMS détaillé

| Cas | WordPress | Headless (Payload/Strapi) | Contentful (SaaS) |
|-----|-----------|---------------------------|---------------------|
| Éditeurs non-techniques | ✅ | ⚠️ | ✅ |
| Modèle contenu complexe | ⚠️ | ✅ | ✅ |
| Multi-langues natif | ⚠️ (plugin) | ✅ | ✅ |
| Coût | ~10-50 €/mois | 0 (self-hosted) | 200+ €/mois |
| Sécurité | ⚠️ (plugin attack surface) | ✅ | ✅ |
| Performance frontend | ⚠️ | ✅ (couplé Next/Astro) | ✅ |
| Souveraineté données | ✅ (self) | ✅ (self) | ❌ (US/EU) |

## Choix e-commerce

| Cas | Shopify | Headless Shopify | Médusa / Custom |
|-----|---------|-------------------|-----------------|
| Setup rapide < 30 j | ✅ | ⚠️ | ❌ |
| < 500k SGD revenue/an | ✅ | ❌ | ❌ |
| Multi-langues + multi-pays | ⚠️ | ✅ | ✅ |
| UX personnalisée extrême | ❌ | ✅ | ✅ |
| Coût | 30-300 USD/mois | + dev frontend | + dev complet |

## Stack par offre Architekt

| Offre | Stack par défaut |
|-------|------------------|
| Architekt Launch | Astro + Tailwind + shadcn + Cloudflare Pages |
| Architekt MVP | Next.js + FastAPI + PostgreSQL + Clerk + Cloudflare/Fly |
| Architekt Portal | Next.js + FastAPI + PostgreSQL + RBAC + S3 (R2) + Hetzner |
| Architekt Internal Tool | Next.js + FastAPI + PostgreSQL + Auth client SSO |
| Architekt AI Workflow | Python FastAPI + RQ + PostgreSQL + pgvector + LLM provider |
| Architekt Commerce | Shopify (classic) ou Shopify Hydrogen + Next + Sanity/Contentful |
| Architekt Modernize | Dépend client (audit puis modular monolith cible) |
| Architekt Audit | Architekt Platform (QualityScanner) + interviews |

## Règle d'or

> **Justifier une exception dans un ADR projet.**
> Si un client impose une stack hors matrice → soit on accepte (Tier C premium pricing), soit on décline.
