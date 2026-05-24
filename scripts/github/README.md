# scripts/github — outillage Architekt sur GitHub

Scripts pour peupler le repo GitHub avec **labels**, **milestones**, **issues** et un **Project v2** correspondant à la roadmap Architekt.

## Pré-requis

```bash
# gh CLI : https://cli.github.com
gh auth login                            # interactif
gh auth refresh -s project,read:project  # nécessaire pour Project v2

# jq + yq
brew install jq yq      # macOS
sudo apt install jq && sudo snap install yq    # Linux
```

## Utilisation

Depuis la racine du repo :

```bash
# Tout d'un coup (labels + milestones + issues)
bash scripts/github/setup-project.sh

# Étapes séparées
bash scripts/github/setup-project.sh labels
bash scripts/github/setup-project.sh milestones
bash scripts/github/setup-project.sh issues
bash scripts/github/setup-project.sh project    # optionnel (Project v2)
```

Le script est **idempotent** : relançable sans risque, il ne recrée pas ce qui existe déjà.

## Que crée-t-il ?

### Labels (cf. `.github/labels.yml`)
- `phase:0-rebrand` … `phase:4-on-demand`
- `area:*` (rebrand, ui, platform, agents, ci, deploy, security, website…)
- `kit:*` (astro, nextjs, nuxt, wordpress, shopify, fastapi, nestjs, spring…)
- `type:*` (epic, feature, chore, bug, question, research, adr)
- `role:*` (cpo, cto, designer, architect, sre, security, cs, gtm)
- `priority:*` (must, should, could)
- `status:*` (blocked, needs-decision, in-review)
- `risk:*` (legal, prod)

### Milestones
1. Phase 0 — Rebrand (+7 j)
2. Phase 1 — Catalog & ADR (+14 j)
3. Phase 2 — Doctrine & CI (+21 j)
4. Phase 3 — Pilot website (+35 j)
5. Phase 4 — On-demand (continu, sans deadline)

### Issues
- 5 epics (1 par phase)
- ~15 issues feature/chore
- 3 décisions ouvertes (domaine, couleur, licence)

### Project v2 (optionnel)
- Project `Architekt Roadmap` créé
- Vues à configurer manuellement selon `.github/PROJECT.md`

## Après exécution

1. Vérifier la liste des issues sur GitHub : `gh issue list`
2. Ouvrir le Project v2 et configurer les vues (Board par phase, Table backlog priorisé)
3. Ajouter les issues au Project (UI ou workflow auto-add)
4. Démarrer la **Phase 0 — Rebrand**

## Désinstaller / nettoyer

Pas de script automatique (volontaire — éviter destruction par accident).
Pour nettoyer manuellement :

```bash
# Supprimer un label
gh label delete <name> --yes

# Fermer toutes les issues phase:0
gh issue list --label phase:0-rebrand --json number -q '.[].number' | xargs -I {} gh issue close {}
```
