# Architekt — 6 architectures de référence

> Patterns d'architecture standards Architekt. À choisir au début de chaque projet, à documenter en ADR projet.
> Référence : ADR-037.

## 1. Static-first

| | |
|--|--|
| **Usage** | Sites marketing, landing pages, documentation |
| **Composants** | Astro / Next static + CDN/edge hosting + headless CMS optionnel + analytics + form backend |
| **Sécurité** | Pas de server state par défaut, bot protection sur formulaires |
| **Sécu niveau** | L0 |
| **Hébergement** | Cloudflare Pages, Vercel |
| **Quand l'utiliser** | Tout contenu où l'interactivité est minimale |
| **Quand ne pas utiliser** | Auth utilisateur, DB temps réel, workflows complexes |

### Schéma simplifié

```
[Astro build] → [CDN edge] → [User browser]
                    ↓
              [Form backend Formspark]
                    ↓
              [Email / CRM client]
```

## 2. Modular monolith

| | |
|--|--|
| **Usage** | MVP, B2B apps, internal tools |
| **Composants** | Next.js frontend + backend modules + PostgreSQL + auth partagé + CI/CD |
| **Règles** | Module boundaries explicites, ADR par décision majeure, **éviter microservices avant pression scale** |
| **Sécu niveau** | L1-L2 |
| **Hébergement** | Fly.io / Hetzner / cloud client |
| **Quand l'utiliser** | Défaut pour apps client |
| **Quand ne pas utiliser** | Microservices avec besoin réel de scale différent par module |

### Schéma simplifié

```
[Next.js frontend]
       │
       ▼
[API Routes Next ou FastAPI/NestJS]
       │ modules internes stricts
       ├── auth
       ├── billing
       ├── users
       └── reports
       │
       ▼
[PostgreSQL] — chaque module = ses tables
```

Ref : ADR-002, Spring Modulith (Java), Shopify

## 3. API-first backend

| | |
|--|--|
| **Usage** | Portails, intégrations, futur mobile |
| **Composants** | FastAPI/NestJS + OpenAPI + PostgreSQL + background jobs + queue |
| **Règles** | Contrats API typés, intégrations idempotentes, versioning |
| **Sécu niveau** | L1-L2 |
| **Quand l'utiliser** | API consommée par plusieurs clients (web + mobile + tiers) |

### Schéma simplifié

```
[Web Next.js]   [Mobile native]   [Partner integration]
       │             │                      │
       └─────────────┴──────────────────────┘
                     │ HTTPS + Bearer / OAuth
                     ▼
              [FastAPI / NestJS]
                     │
              [OpenAPI contract]
                     │
              ┌──────┴──────┐
              ▼             ▼
        [PostgreSQL]   [Queue (RQ/BullMQ)]
                            │
                            ▼
                      [Background workers]
```

## 4. Headless commerce/content

| | |
|--|--|
| **Usage** | Contenu / e-commerce avec besoins omnichannel |
| **Composants** | Shopify / WordPress / Payload + frontend layer + CDN + webhook processing |
| **Règles** | **Ne pas faire du headless sans business case** explicite |
| **Sécu niveau** | L1-L2 |
| **Quand l'utiliser** | Multi-region, multi-channel, UX très personnalisée |
| **Quand ne pas utiliser** | Setup < 30 jours, équipe non-technique, < 500k revenue/an |

### Schéma simplifié

```
[Shopify/WordPress/Payload]  ← backoffice éditeur
        │
        │ API/webhooks
        ▼
[Next.js / Astro frontend]
        │
        ▼
[CDN edge]
        │
        ▼
[User browser]
```

## 5. AI workflow architecture

| | |
|--|--|
| **Usage** | Automation, processing documents, assistants internes |
| **Composants** | Ingestion + classification + retrieval (si besoin) + LLM execution + **human approval** + audit trail |
| **Règles** | **Aucune action irréversible autonome**, prompt/version logging, cost tracking |
| **Sécu niveau** | L1-L2 (selon données) |
| **Quand l'utiliser** | Workflows répétitifs avec input texte/document |

### Schéma simplifié

```
[Input: email/doc/form]
        │
        ▼
[Ingestion + parsing]
        │
        ▼
[Classification / routing]
        │
        ▼
[Retrieval (pgvector)] ← contexte client
        │
        ▼
[LLM execution]
        │
        ▼
[Human approval gate] ← L3/L4 actions
        │
        ▼
[Action exécutée + audit log]
```

Ref : ADR-010, ADR-019, ADR-036

## 6. Multi-region-ready architecture

| | |
|--|--|
| **Usage** | Clients internationaux, portails latency-sensitive, contraintes data residency |
| **Composants** | Regional hosting + CDN + region-aware storage + isolated environments |
| **Règles** | **Data residency décidée avant build**, pas de réplication globale sans review légale |
| **Sécu niveau** | L2-L3 |
| **Quand l'utiliser** | Clients EU + APAC + MENA + USA dans le même produit |
| **Quand ne pas utiliser** | Single-region suffit (over-engineering) |

### Schéma simplifié

```
                    [User SG]      [User UAE]     [User EU]      [User US]
                          │              │              │              │
                          ▼              ▼              ▼              ▼
                    [CDN edge global Cloudflare/Akamai]
                          │              │              │              │
                          ▼              ▼              ▼              ▼
                    [SG region]    [ME region]    [EU region]    [US region]
                          │              │              │              │
                    [PG SG]        [PG UAE]       [PG EU]        [PG US]
                          │              │              │              │
                          └──────────────┴──── pas de réplication ────┘
                                              cross-region par défaut
```

## Choix d'architecture par offre

| Offre | Architecture |
|-------|--------------|
| Launch | **Static-first** |
| MVP | **Modular monolith** |
| Internal Tool | **Modular monolith** |
| Portal | **API-first** + RBAC |
| AI Workflow | **AI workflow architecture** |
| Commerce | **Headless commerce** ou Shopify direct |
| Modernize | Cible **Modular monolith** depuis legacy |
| Audit | Advisory (rapport, pas d'implémentation) |
| Client international multi-région | **Multi-region-ready** + base + AI selon cas |

## Anti-patterns architecturaux

- ❌ Microservices avant 10 ingénieurs / pression scale réelle
- ❌ Headless juste "parce que c'est moderne"
- ❌ Multi-cloud sans business case
- ❌ AI workflow sans audit trail ni human approval
- ❌ Multi-region avec réplication globale sans review légale
- ❌ Réinventer auth (toujours utiliser Clerk/Auth0/SSO managed)

Voir `docs/RISKS.md` pour les risques associés.
