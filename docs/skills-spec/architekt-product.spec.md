# Spec : architekt-product

> Skill cible : `skills/architekt-product.md`

## Objectif

Encoder la **méthode discovery produit Architekt** pour que les agents PO/PM mènent la phase Discovery client avec rigueur (jobs-to-be-done, hypothèses, métriques).

## Quand utiliser

- Phase Discovery d'une mission (3-5 jours pour MVP/Internal Tool)
- Lors de découverte d'une nouvelle feature en cours de build
- En atelier idéation avec client
- Pour valider une hypothèse produit

## Outputs Discovery (livrables)

1. **Problem statement** (1 page)
2. **Jobs-To-Be-Done** (top 3 par persona)
3. **Hypothèses prioritaires** (avec critères validation)
4. **Personas** (2-3 max)
5. **User journey map** (parcours critique)
6. **Critères de succès** (métriques produit + business)
7. **Roadmap projet** (3 mois / 6 mois / 12 mois)
8. **Constraints** (techniques, légales, budget)

Format : Markdown dans `<projet>/docs/discovery/`.

## Méthode

### 1. Interview sponsor (1h)

- Quel problème ? Quels impacts ?
- Comment résolu aujourd'hui ?
- Qui sont les utilisateurs ?
- Quels critères de succès ?
- Quelles contraintes ?

### 2. Interviews utilisateurs (3-5 × 30 min)

- "Racontez-moi la dernière fois que vous avez fait X"
- Pas de questions hypothétiques
- Noter verbatim
- Identifier émotions, frictions, workarounds

### 3. Synthèse JTBD

Format Christensen :
```
When [situation],
I want to [motivation / job],
So I can [outcome].
```

### 4. Hypothèses prioritaires

```
Nous croyons que [persona] a besoin de [solution]
parce que [observation].
Nous saurons que c'est vrai quand [métrique mesurable].
```

→ Prioriser 3 hypothèses max pour MVP.

### 5. Métriques

| Type | Exemples |
|------|----------|
| Adoption | Nb utilisateurs actifs, % conversion |
| Engagement | Sessions/semaine, temps moyen |
| Rétention | DAU/MAU, churn |
| Business | Revenue, coût servi, marge |

## Anti-patterns

- ❌ Demander "qu'est-ce que vous voulez ?" (utilisateurs ne savent pas)
- ❌ Designer la solution avant le problème
- ❌ Faire une roadmap > 12 mois (incertitude trop grande)
- ❌ Inventer 10 personas (3 max)
- ❌ Pas de critères de succès mesurables
- ❌ Sauter la Discovery "pour aller vite"

## Sources

- Clayton Christensen — Jobs To Be Done
- Marty Cagan — Inspired
- Teresa Torres — Continuous Discovery Habits
- Steve Krug — Don't Make Me Think
