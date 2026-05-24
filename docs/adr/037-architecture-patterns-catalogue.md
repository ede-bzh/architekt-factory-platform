# ADR-037 : Architecture patterns catalogue

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, Solution Architect

## Contexte

Sans catalogue formel d'architectures Architekt, chaque projet réinvente le pattern. Risque incohérence et "big ball of mud".

## Décision

**6 architectures de référence officielles** (cf. `docs/ARCHITECTURES.md`) :

| # | Pattern | Use case |
|---|---------|----------|
| 1 | **Static-first** | Marketing, landing, docs |
| 2 | **Modular monolith** | MVP, B2B, internal tools |
| 3 | **API-first backend** | Portails, intégrations, mobile futur |
| 4 | **Headless commerce/content** | E-commerce, content omnichannel |
| 5 | **AI workflow** | Automation, document processing, assistants |
| 6 | **Multi-region-ready** | Clients internationaux, data residency |

Chaque projet client doit déclarer le pattern utilisé dans un ADR projet.

### Pattern par défaut par offre

| Offre | Pattern |
|-------|---------|
| Launch | Static-first |
| MVP | Modular monolith |
| Internal Tool | Modular monolith |
| Portal | API-first + RBAC |
| AI Workflow | AI workflow |
| Commerce | Headless (ou Shopify direct) |
| Modernize | Cible modular monolith |
| Client international multi-région | Multi-region-ready + pattern base |

## Conséquences

### Positives
- Vocabulaire commun (équipe + client)
- Skills agents alignés sur 6 patterns
- Reproductibilité

### Négatives
- Risque "tout marteau = clou"
- Mitigation : revue trimestrielle, ajout pattern si besoin réel

## Sources
- `docs/ARCHITECTURES.md`
- ADR-002 Modular Monolith (pattern dominant)
- Bertrand Meyer, Robert Martin (Clean Architecture)
- Sam Newman (Monolith to Microservices)
