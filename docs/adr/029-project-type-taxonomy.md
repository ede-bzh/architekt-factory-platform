# ADR-029 : Project type taxonomy

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO

## Contexte

Architekt va livrer plusieurs natures de projets. Sans taxonomie commune, l'équipe parle de "MVP" sans s'accorder, le pricing est instable, le catalogue stack incohérent.

## Décision

**10 types de projets officiels** (cf. `docs/PROJECTS.md`) :

| ID | Type |
|----|------|
| A | Corporate / marketing platform |
| B | Product MVP |
| C | Internal business tool |
| D | AI workflow automation |
| E | E-commerce / headless commerce |
| F | CMS / content platform |
| G | Client portal |
| H | Data / analytics dashboard |
| I | Modernization project |
| J | Security / quality audit |

Chaque projet client = **1 type principal** (max 2 secondaires).

## Conséquences

### Positives
- Vocabulaire commun équipe + client
- Stack par défaut prévisible (ADR-038)
- Pricing cohérent (`docs/OFFERS.md`)

### Négatives
- Risque "ne rentre dans aucune case" → ouvrir cas par cas avec CPO

## Sources
- Retour terrain agences digitales 2026
- `docs/PROJECTS.md`
