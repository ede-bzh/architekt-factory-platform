# Architekt — GitHub Project setup

Ce document décrit la structure du **GitHub Project v2** que `scripts/github/setup-project.sh` provisionne (ou que vous pouvez créer manuellement).

## Project

- **Nom** : `Architekt Roadmap`
- **Type** : User/Organization Project v2
- **Visibilité** : Private (à passer Public quand la marque est posée)
- **Owner** : `ede-bzh` (à migrer vers l'org Architekt quand créée)

## Vues recommandées

### Vue 1 — Roadmap par phase (Board)
- Group by : `Milestone`
- Colonnes (Status) : Todo, In Progress, In Review, Done
- Filtre : tous les issues du repo

### Vue 2 — Backlog priorisé (Table)
- Tri : `priority` (must → should → could), `phase`
- Colonnes : Title, Phase, Area, Role, Priority, Status, Assignee

### Vue 3 — Kits stack (Board)
- Group by : `kit:*` label
- Filtre : `area:catalog OR label kit:*`
- Sert à voir l'état d'équipement du catalogue

### Vue 4 — ADR (Table)
- Filtre : `type:adr`
- Tri : numéro ADR
- Permet de tracker l'état des décisions

### Vue 5 — Décisions ouvertes (Table)
- Filtre : `status:needs-decision`
- Sert au CPO/CTO pour ne rien oublier

## Champs custom (à créer dans le Project)

| Champ | Type | Options |
|-------|------|---------|
| `Phase` | Single select | 0-Rebrand, 1-Catalog, 2-Practices, 3-Pilot, 4-OnDemand |
| `Priority` | Single select | Must, Should, Could |
| `Effort` | Single select | XS (< 1h), S (< 1j), M (< 3j), L (< 1w), XL (> 1w) |
| `Role` | Single select | CPO, CTO, Designer, Architect, SRE, Security, CS, GTM |
| `Risk` | Single select | None, Legal, Prod, Cost |

## Milestones

Créés par le setup script :

| # | Nom | Description | Due |
|---|-----|-------------|-----|
| 1 | Phase 0 — Rebrand | Tous les éléments de rebrand visibles + identifiants | +1 semaine |
| 2 | Phase 1 — Catalog & ADR | Catalogue technos + 6 ADR mergés | +2 semaines |
| 3 | Phase 2 — Doctrine & CI | 6 skills + CI verte | +3 semaines |
| 4 | Phase 3 — Pilot website | architekt.TBD live | +5 semaines |
| 5 | Phase 4 — On-demand | Toujours ouvert (continu) | (pas de date) |

## Convention de nommage des issues

- **Epic** : `[EPIC][P<phase>] <titre>` — couvre plusieurs features
- **Feature/Chore** : `[P<phase>] <area> — <titre court>`
- **ADR** : `[ADR-<num>] <titre>`
- **Bug** : `[BUG] <titre>`
- **Décision** : `[DECISION] <titre>` + label `status:needs-decision`

## Comment utiliser

1. Créer le Project manuellement (UI GitHub) ou via le script.
2. Ajouter le Project comme cible dans `.github/workflows/add-to-project.yml` (optionnel : auto-add nouveaux issues).
3. Liens : depuis chaque issue, `Projects` → `Architekt Roadmap`.

## Automatisations recommandées

- Issue créé → ajouté automatiquement au Project (workflow)
- Issue avec label `phase:0-rebrand` → champ `Phase` = `0-Rebrand`
- PR fermée linkée à issue → status = Done
