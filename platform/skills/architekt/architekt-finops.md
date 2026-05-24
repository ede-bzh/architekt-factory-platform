---
name: Architekt FinOps
description: FinOps mission Architekt — budget LLM/infra/heures, alertes, marge cible (ADR-011, ADR-016)
tags: [finops, architekt, budget, margin, llm-cost]
metadata:
  category: finops
  triggers: [budget, margin, llm-cost, pricing, mission-cost]
---

# Architekt FinOps

## Objectif

Garantir que **chaque mission Architekt reste rentable** en gouvernant coûts LLM, infra et heures humaines.

## Quand utiliser

- Création mission (définition budget)
- Sprint review (tracking consommé)
- Alerte plateforme 70/90/100%
- Retro post-mission / revue trimestrielle marges

## Modèle FinOps mission

```
Budget mission = LLM tokens + Infra dédiée + Heures humaines
Revenue mission = SOW signé
Marge brute = (Revenue - Budget consommé) / Revenue
```

## Plafonds par offre (ADR-016)

| Offre | LLM (SGD) | Heures | Infra/mois (SGD) | Marge cible |
|-------|-----------|--------|------------------|-------------|
| Audit | 50 | 30 h | 0 | 70% |
| Launch | 100 | 40 h | 50 | 60% |
| Internal Tool | 300 | 120 h | 150 | 55% |
| MVP | 500 | 200 h | 200 | 50% |
| AI Workflow | 1000 | 100 h | 300 | 55% |

## Alertes & actions

| Consommation | Action |
|--------------|--------|
| 50% | Note info chef de projet |
| 70% | Email + dashboard alerte |
| 90% | Revue scope obligatoire avec sponsor |
| 100% | **Auto-pause mission** (sauf override CTO) |
| 120% | Escalade CPO + comité go/no-go |

## Coût horaire interne

- Fondateurs : **100 SGD/h**
- Senior dev : 80 SGD/h
- Junior dev : 50 SGD/h
- Freelance : selon contrat

Heures toujours timestamp + activity (pas d'imputation floue).

## Visibilité

- Dashboard FinOps par mission (Phase 5 plateforme)
- Rapport mensuel : revenue / coûts / marge / dépassements
- Revue trimestrielle : ajuster pricing offres si dérive

## Anti-patterns

- ❌ Mission sans budget LLM défini
- ❌ Ignorer alerte 90%
- ❌ Sur-allouer équipe "pour aller vite"
- ❌ Infra sur-provisionnée "au cas où"
- ❌ Marge < 40% sur devis sans validation CPO+CTO

## Sources

- ADR-011 LLM cost governance
- ADR-016 Pricing and margin targets
- FinOps Foundation Framework
