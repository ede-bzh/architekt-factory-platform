# Spec : architekt-finops

> Skill cible : `skills/architekt-finops.md`
> ADR référents : ADR-011, ADR-016

## Objectif

Garantir que **chaque mission Architekt reste rentable** en gouvernant coûts LLM, infra, et heures humaines.

## Quand utiliser

- Création de mission (définition du budget)
- À chaque sprint review (tracking budget consommé)
- Sur alerte plateforme (70/90/100 %)
- En retro post-mission (apprentissage pricing)
- En revue trimestrielle marges agence

## Modèle FinOps mission

```
Budget mission = LLM tokens + Infra dédiée + Heures humaines
Revenue mission = SOW signé
Marge brute = (Revenue - Budget consommé) / Revenue
```

## Plafonds par offre (cf. ADR-016)

| Offre | LLM (SGD) | Heures | Infra/mois (SGD) | Marge cible |
|-------|-----------|--------|------------------|-------------|
| Audit | 50 | 30 h | 0 | 70 % |
| Launch | 100 | 40 h | 50 | 60 % |
| Internal Tool | 300 | 120 h | 150 | 55 % |
| MVP | 500 | 200 h | 200 | 50 % |
| AI Workflow | 1000 | 100 h | 300 | 55 % |

## Alertes & actions

| Consommation | Action |
|--------------|--------|
| 50 % | Note d'info au chef de projet |
| 70 % | Email + dashboard alerte |
| 90 % | Revue scope obligatoire avec sponsor client |
| 100 % | **Auto-pause mission** (sauf override CTO) |
| 120 % | Escalade CPO + comité go/no-go continuer |

## Coût horaire interne

- Fondateurs : **100 SGD/h** (taux interne pour calcul marge)
- Senior dev embauché : 80 SGD/h
- Junior dev embauché : 50 SGD/h
- Apprenti / freelance : selon contrat

## Visibilité

- **Dashboard FinOps par mission** dans la plateforme (Phase 5)
- **Rapport mensuel agrégé** : revenue total / coûts / marge moyenne / dépassements
- **Revue trimestrielle** : ajuster pricing offres si marge dérive

## Anti-patterns

- ❌ Lancer une mission sans budget LLM défini
- ❌ Ignorer une alerte 90 % (= dépassement quasi-certain)
- ❌ Imputer heures floues (toujours timestamp + activity)
- ❌ Sur-allouer une équipe "pour aller vite" (multiplie le coût horaire)
- ❌ Acheter infra "au cas où" (provisionner à la demande)

## Sources

- FinOps Foundation Framework
- ADR-011 (LLM cost governance)
- ADR-016 (Pricing model and margin targets)
