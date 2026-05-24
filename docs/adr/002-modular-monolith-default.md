# ADR-002 : Modular Monolith comme pattern d'architecture par défaut

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, Chief Solution Architect (agent), Chief Enterprise Architect (agent)

## Contexte

Architekt va livrer des projets clients sur des stacks variées (Next.js, NestJS, FastAPI, Spring, Nuxt…). Chaque projet doit avoir un pattern d'architecture **par défaut**, sauf justification contraire.

## Décision

**Modular monolith** comme pattern par défaut pour tous les projets clients.

```
1 projet client = 1 service déployable (modular monolith)
  ↳ modules internes stricts (packages, accès cross-module via API du module)
  ↳ chaque module possède ses tables (logique, pas physique)
  ↳ extraction en microservice UNIQUEMENT quand un module a un besoin réel
     de scale ou de déploiement indépendant
  ↳ serverless = outil ponctuel (events, jobs), pas architecture
```

## Justification (références marché 2026)

| Source | Conclusion |
|--------|-----------|
| Amazon Prime Video (2023) | Rollback microservices → monolith, -90% coût |
| Shopify (publications 2024-2026) | Modular monolith assumé en prod |
| Spring Modulith (Spring 2.x, 2026) | Standard de facto Java modular monolith |
| Calmops 2026 guide | "Most teams start with modular monolith, extract later" |

## Outillage par stack

| Stack | Outil modular monolith |
|-------|------------------------|
| Java | **Spring Modulith** (vérifie boundaries au build) |
| Python | Packages stricts + `pytest-architecture` |
| Node / TS | Monorepo Nx ou packages npm internes |
| Next.js | App Router + dossiers `features/` cloisonnés |

## Quand extraire un microservice ?

Critères cumulatifs (au moins 2 sur 3) :

1. Le module a une **cadence de déploiement** différente (release séparée).
2. Le module a un **profil de scale** différent (CPU/RAM/IO).
3. Le module a une **équipe propriétaire** distincte.

Sinon → rester dans le monolith.

## Conséquences

### Positives
- Démarrage rapide projet client (1 repo, 1 build, 1 deploy)
- Opérations simplifiées (logs, traces, debug)
- Extraction microservice = naturelle (le module est déjà isolé)

### Négatives
- Discipline nécessaire pour respecter les boundaries
- Outils de vérification à brancher dans CI (Spring Modulith verify, etc.)

### Risques
- Si discipline relâchée → "big ball of mud"
- Mitigation : `architekt-archi.md` skill rendu obligatoire dans les missions

## Application

- Tout nouveau projet client : pattern par défaut = modular monolith
- ADR projet client : doit justifier si autre pattern choisi
- Skill `architekt-archi.md` charge ce ADR dans le contexte des agents architecte
