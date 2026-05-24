# ADR-038 : Stack decision matrix

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO

## Contexte

Sans matrice de décision stack, chaque projet relance le débat "Next.js vs Astro vs Nuxt", "Postgres vs Mongo", etc. Perte de temps et incohérence.

## Décision

**Matrice de décision stack officielle** (cf. `docs/STACK-MATRIX.md`).

### Règle d'or

> **1 type de projet = 1 stack par défaut.** Variation seulement avec justification documentée dans ADR projet.

### Matrice principale

| Type projet | Stack par défaut |
|-------------|------------------|
| Marketing site | Astro + Tailwind + shadcn/ui + Cloudflare Pages |
| Interactive web app | Next.js + PostgreSQL + FastAPI/NestJS |
| Internal tool | Next.js + FastAPI + PostgreSQL + Auth SSO |
| AI workflow | Python + FastAPI + workers + PostgreSQL + pgvector si justifié |
| E-commerce | Shopify first, headless si besoin |
| Enterprise Java | Spring Modulith (sur trigger) |
| Mobile | Responsive/PWA d'abord, native si validé |
| CMS-heavy | WordPress (éditeurs) ou Payload (dev-driven) |

### Auth

| Contexte | Provider |
|----------|----------|
| Startup / scale-up | Clerk ou Auth0 |
| Enterprise (Microsoft) | Azure AD / Entra ID |
| Workspace Google | Google Workspace SSO |
| B2B SSO requis | OIDC / SAML générique |

### DB

| Cas | Recommandation |
|-----|----------------|
| Défaut | PostgreSQL |
| Cache | + Redis |
| Search | PostgreSQL FTS, sinon Meilisearch |
| Vector AI | pgvector d'abord |

## Conséquences

### Positives
- Décisions rapides
- Maîtrise CTO réelle (pas 18 stacks)
- Pricing cohérent

### Négatives
- Risque "rigidité" si client demande exception
- Mitigation : Tier C pricing premium ou refus

## Sources
- `docs/STACK-MATRIX.md`
- `docs/CATALOG.md`
