---
name: Architekt Product
description: Discovery produit Architekt — JTBD, hypothèses, personas, métriques
tags: [product, architekt, discovery, jtbd, personas]
metadata:
  category: product
  triggers: [discovery, jtbd, persona, hypothesis, interview]
---

# Architekt Product

## Objectif

Encoder la **méthode discovery produit Architekt** pour que PO/PM mènent la phase Discovery avec rigueur (jobs-to-be-done, hypothèses, métriques).

## Quand utiliser

- Phase Discovery mission (3-5 j MVP/Internal Tool)
- Nouvelle feature en cours de build
- Atelier idéation client
- Validation hypothèse produit

## Livrables Discovery

Format Markdown dans `<projet>/docs/discovery/` :

1. **Problem statement** (1 page)
2. **Jobs-To-Be-Done** (top 3 par persona)
3. **Hypothèses prioritaires** + critères validation
4. **Personas** (2-3 max)
5. **User journey map** (parcours critique)
6. **Critères de succès** (métriques produit + business)
7. **Roadmap** 3 / 6 / 12 mois
8. **Constraints** (techniques, légales, budget)

## Méthode

### 1. Interview sponsor (1h)

Problème, impacts, solution actuelle, utilisateurs, critères succès, contraintes.

### 2. Interviews utilisateurs (3-5 × 30 min)

- "Racontez la dernière fois que vous avez fait X"
- Pas de questions hypothétiques — verbatim, émotions, workarounds

### 3. Synthèse JTBD (Christensen)

```
When [situation],
I want to [motivation / job],
So I can [outcome].
```

### 4. Hypothèses (max 3 pour MVP)

```
Nous croyons que [persona] a besoin de [solution]
parce que [observation].
Nous saurons que c'est vrai quand [métrique mesurable].
```

### 5. Métriques

| Type | Exemples |
|------|----------|
| Adoption | Utilisateurs actifs, % conversion |
| Engagement | Sessions/semaine, temps moyen |
| Rétention | DAU/MAU, churn |
| Business | Revenue, coût servi, marge |

## Anti-patterns

- ❌ "Qu'est-ce que vous voulez ?" (utilisateurs ne savent pas)
- ❌ Designer solution avant problème
- ❌ Roadmap > 12 mois
- ❌ 10 personas inventés
- ❌ Pas de critères succès mesurables
- ❌ Sauter Discovery "pour aller vite"

## Sources

- Clayton Christensen — Jobs To Be Done
- Marty Cagan — Inspired
- Teresa Torres — Continuous Discovery Habits
