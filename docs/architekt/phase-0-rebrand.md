# Phase 0 — Rebrand Architekt

> Durée cible : **1 semaine**
> Bloque : Phase 1, 2, 3
> Repo only, rien à déployer

## Objectif

Tout le repo et la documentation portent la marque **Architekt** (et **plus** Macaron / Software Factory).

## Pré-requis (à trancher avant ou pendant)

| # | Question | Qui | Statut |
|---|----------|-----|--------|
| Q1 | Domaine final ? (`.sg`, `.ai`, `.io`) | CPO | ouvert |
| Q2 | Couleur de marque ? (palette) | CPO + Designer | ouvert |
| Q3 | Licence ? (cf. ADR-006) | CTO + avocat | ouvert |

→ **Ne bloque pas** la phase 0 : on utilise `architekt.TBD` et la palette purple actuelle comme placeholders, on remplacera quand tranché.

## Périmètre — 3 niveaux

### Niveau 1 — Visible (P0-N1, doit être fait en Phase 0)

- [ ] `README.md` (EN) + variantes (FR, DE, ES, JA, KO, PT, ZH) → marque Architekt
- [ ] `README.laposte.md` : laisser tel quel (sync interne La Poste)
- [ ] `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CONTRIBUTING.md` → Architekt
- [ ] `.env.example` → commentaires Architekt
- [ ] `Makefile` : messages echo → Architekt
- [ ] UI : titres pages, logo placeholder
  - [ ] `platform/web/templates/base.html`
  - [ ] `platform/web/templates/login.html`
  - [ ] `platform/web/templates/onboarding.html`
- [ ] i18n : `platform/i18n/locales/*.json` (clés contenant `Macaron`)

### Niveau 2 — Identifiants (P0-N2, peut déborder Phase 1 si CI rouge)

- [ ] Variables env : `MACARON_API_KEY` → `ARCHITEKT_API_KEY` (+ alias rétro-compatible 6 mois)
- [ ] CLI : ajouter binaire `architekt` qui pointe sur `cli.sf:main`, garder `sf` en alias
- [ ] `pyproject.toml` : `name = "architekt-factory-platform"`, `authors` Architekt
- [ ] Doc : `docs/`, `dashboard/` → références Architekt

### Niveau 3 — Runtime / packaging (P0-N3, **PAS Phase 0**, fait Phase 3+)

- [ ] Package Python `macaron_platform` → `architekt_platform`
  - Bloquant prod Azure existante → reporté
- [ ] Image Docker `architekt-platform` (parallèle, sans casser l'existant)
- [ ] Helm chart renommé

## Plan jour par jour (5 jours ouvrés)

### Jour 1 — Décisions + ADR

- Écrire / merger `docs/adr/001-rebrand-architekt.md` (déjà fait ✅)
- Trancher (ou décider de reporter) Q1, Q2, Q3
- Issue GitHub `phase-0-rebrand` créée

### Jour 2 — README + docs racine

- Search & replace `Software Factory` → `Architekt Factory` dans tous les README
- Mise à jour CODE_OF_CONDUCT, SECURITY, CONTRIBUTING
- Commit unique `docs: rebrand README and root docs to Architekt`

### Jour 3 — UI templates

- `base.html`, `login.html`, `onboarding.html`, `home.html`
- Tokens CSS `--purple` → `--brand-primary` (valeur identique si pas tranché)
- Commit `feat(ui): rebrand templates and tokens to Architekt`

### Jour 4 — i18n + env vars

- 8 locales JSON
- `.env.example`, `Makefile`, scripts
- Alias `ARCHITEKT_API_KEY` + dépréciation soft de `MACARON_API_KEY`
- Commit `feat(config): introduce ARCHITEKT_* env vars (Macaron aliases kept)`

### Jour 5 — pyproject + CLI alias

- `pyproject.toml`, ajout entry-point `architekt = "cli.sf:main"`
- Doc CLI mise à jour
- Commit `chore: pyproject name and CLI alias to Architekt`
- PR finale Phase 0 → merge

## Search & replace exhaustif (à exécuter en Phase 0)

```bash
# Cibles à inspecter et remplacer manuellement (jamais en sed brut)
rg -l 'Software Factory' --type-not git
rg -l 'macaron-software' --type-not git
rg -l 'MACARON_' --type-not git
rg -l 'macaron_platform' --type-not git  # NIVEAU 3 SEULEMENT
```

## Gate de passage

- [ ] CI verte (pytest, lint)
- [ ] UI cohérente en local (`make dev` → marque Architekt visible)
- [ ] PR mergée vers `main`
- [ ] Sync La Poste vérifiée (le script ne casse pas)

## Risques + mitigations

| Risque | Mitigation |
|--------|-----------|
| Casser Azure prod existant | Niveau 3 reporté ; alias env vars |
| Sync La Poste casse | Test dry-run avant merge |
| Search/replace agressif casse code | Manuel + revue PR obligatoire |

## Suivi

- Milestone GitHub : **Phase 0 — Rebrand**
- Labels : `phase:0`, `area:rebrand`, `area:docs`, `area:ui`
- Issues : voir `docs/issues/P0-*.md`
