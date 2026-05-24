# Phase 1 — Catalogue technos & ADR

> Durée cible : **1 semaine**
> Dépend de : Phase 0 (CI verte, rebrand merged)
> Sortie : `docs/CATALOG.md` (déjà créé) + 5 ADR mergés

## Objectif

Définir formellement ce que l'agence Architekt **sait faire** et avec **quelle architecture par défaut**, en s'appuyant sur les pratiques marché 2026.

## Livrables

### A. Catalogue technos (déjà rédigé)

- `docs/CATALOG.md` : 11 lignes (Astro, Next, Nuxt, WP, Shopify, FastAPI, NestJS, Spring Modulith, SwiftUI, Compose, Payload)
- Statut par ligne : ✅ / 🟡 / ⚠️
- Hors scope explicite

### B. ADR clés (5 documents)

| ID | Titre | Statut fichier |
|----|-------|----------------|
| 001 | Rebrand Architekt | ✅ écrit |
| 002 | Modular Monolith par défaut | ✅ écrit |
| 003 | Mutation testing | ✅ écrit |
| 004 | Design system shadcn+Radix+Tailwind v4 | ✅ écrit |
| 005 | Hébergement pilote (Hetzner + Cloudflare) | ✅ écrit |
| 006 | Licence (open-core) | ✅ écrit, **à valider avocat** |

### C. Templates kits par stack (squelette)

Pour chaque stack ⚠️ du catalogue, créer un squelette `docs/catalog/<stack>.md` :

```
docs/catalog/
  astro.md          # commandes build, exemple repo, Cloudflare deploy
  nextjs.md
  nuxt.md
  wordpress.md
  shopify.md
  nestjs.md
  spring-modulith.md
  payload.md
```

Squelette **vide au début**, rempli quand stack activée (cf. Phase 4).

## Pré-requis Phase 1

- Phase 0 mergée
- CI tests présente (sinon créer issue P1-XX en bloquant)

## Gate de passage

- [ ] `docs/CATALOG.md` mergé
- [ ] 5 ADR mergés (006 peut être "Proposé" en attente avocat)
- [ ] 8 squelettes `docs/catalog/*.md` créés (vides)
- [ ] Milestone Phase 1 fermé sur GitHub
