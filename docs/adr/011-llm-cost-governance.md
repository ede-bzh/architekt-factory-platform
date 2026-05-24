# ADR-011 : LLM cost governance (FinOps)

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CFO (CPO), CAIO

## Contexte

Les missions agentiques peuvent consommer 5-10× le budget LLM prévu sans visibilité temps réel. Pour une agence avec marge 50 %, un dépassement LLM de 5k SGD sur un projet 20k SGD détruit la rentabilité.

## Décision

**FinOps obligatoire** pour toute mission Architekt :

### Budget par mission (mission manifest)

```yaml
budget:
  llm_tokens_sgd: 500        # plafond budget tokens en SGD
  infra_sgd_per_month: 200   # plafond infra dédiée
  human_hours_max: 200       # plafond heures imputées
```

### Alertes automatiques

- 70 % consommé → notification chef de projet
- 90 % consommé → notification + revue scope
- 100 % consommé → **auto-pause mission** (sauf override CTO)
- 120 % → escalade CPO + comité go/no-go continuer

### Tracking

- Tokens LLM par agent par mission (existant `llm_traces`)
- Coût alloué par mission (table `mission_costs`)
- Dashboard FinOps par projet client
- Rapport mensuel agrégé : coût LLM total / revenue / marge

### Seuils par offre (cf. `docs/OFFERS.md`)

| Offre | Budget LLM cible |
|-------|------------------|
| Architekt Audit | 50 SGD |
| Architekt Launch | 100 SGD |
| Architekt Internal Tool | 300 SGD |
| Architekt MVP | 500 SGD |
| Architekt AI Workflow | 1000 SGD |

## Conséquences

### Positives
- Marge protégée (R2 dans `docs/RISKS.md`)
- Décision continuer/scope cut/facturer avenant transparente
- Données pour pricing futur

### Négatives
- Ralentit certaines missions (acceptable)
- Investissement initial dashboard FinOps (Phase 5)

## Sources

- FinOps Foundation Framework
- Anthropic / OpenAI pricing 2026 (variabilité ×3 selon modèle)
- Retour terrain : missions agentiques non gouvernées = 3-10× budget
