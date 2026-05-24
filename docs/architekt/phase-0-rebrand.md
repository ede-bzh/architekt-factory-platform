# Phase 0 — Foundation & Rebrand

> Durée cible : **1 semaine**
> Bloque : Phase 1, 2, 3
> Repo only (rien à déployer), mais inclut **legal pack** et **positionnement**

## Objectif

Tout le repo + la documentation + le cadre légal portent la marque **Architekt** et le positionnement officiel.

> **Positionnement officiel** : *"AI-native digital product studio for APAC scale-ups and SMEs"*

## Pré-requis (à trancher avant ou pendant)

| # | Question | Qui | Statut |
|---|----------|-----|--------|
| Q1 | Domaine final ? (`.sg`, `.ai`, `.io`) | CPO | ouvert |
| Q2 | Couleur de marque ? (palette) | CPO + Designer | ouvert |
| Q3 | Licence ? (cf. ADR-006 révisé) | CTO + avocat | ouvert |
| Q4 | Entité légale Singapour ouverte ? | CPO | ouvert |

→ **Ne bloque pas** la phase 0 : on utilise `architekt.TBD` et placeholders.

## Périmètre — 3 niveaux + brand + legal

### Niveau 1 — Visible (P0-N1, doit être fait en Phase 0)

- [ ] `README.md` (EN) + variantes (FR, DE, ES, JA, KO, PT, ZH) → marque Architekt + nouveau positionnement
- [ ] `README.laposte.md` : laisser tel quel (sync interne La Poste)
- [ ] `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CONTRIBUTING.md` → Architekt
- [ ] `.env.example` → commentaires Architekt
- [ ] `Makefile` : messages echo → Architekt
- [ ] UI : titres pages, logo placeholder
  - [ ] `platform/web/templates/base.html`
  - [ ] `platform/web/templates/login.html`
  - [ ] `platform/web/templates/onboarding.html`
- [ ] i18n : `platform/i18n/locales/*.json`

### Niveau 2 — Identifiants (P0-N2)

- [ ] `MACARON_API_KEY` → `ARCHITEKT_API_KEY` (+ alias rétro-compatible 6 mois)
- [ ] CLI : binaire `architekt` (alias `sf` gardé)
- [ ] `pyproject.toml` : `name = "architekt-factory-platform"`

### Niveau 3 — Runtime / packaging (PAS Phase 0, reporté Phase 3+)

- [ ] Package Python `macaron_platform` → `architekt_platform` — reporté
- [ ] Image Docker `architekt-platform` — reporté
- [ ] Helm chart renommé — reporté

### Brand system minimal (nouveau Phase 0)

- [ ] **Logo placeholder** (text-based ou Figma simple) — Designer ou outil IA
- [ ] **Palette** OKLCH 4-6 couleurs (`docs/brand/palette.md`)
- [ ] **Typographie** : 1 sans-serif (corps), 1 mono (code) — recommandation Inter + JetBrains Mono
- [ ] **Tone of voice** (`docs/brand/voice.md`) : pro, technique, pas startup-hype
- [ ] **Templates commerciaux** (`docs/brand/templates/`) :
  - [ ] Pitch deck (Google Slides ou Pitch)
  - [ ] Proposal one-pager (par offre, cf. `docs/OFFERS.md`)
  - [ ] Case study template

### Legal pack (nouveau Phase 0)

- [ ] **NDA** (mutual, court, 1 page) — `docs/legal/architekt-nda-template.md`
- [ ] **MSA** (Master Service Agreement) — `docs/legal/architekt-msa-template.md`
- [ ] **SOW** (Statement of Work) — `docs/legal/architekt-sow-template.md`
- [ ] **DPA** (Data Processing Agreement, conforme PDPA SG) — `docs/legal/architekt-dpa-template.md`
- [ ] **IP assignment** clause — incluse dans MSA
- [ ] **Clause usage IA** (transparence, audit, opt-out) — incluse dans MSA + DPA
- [ ] **AUP** (Acceptable Use Policy) — pour clients utilisant la plateforme
- [ ] Revue par **avocat Singapour** (vivement recommandée avant 1er contrat)

### Landing page placeholder

- [ ] Carrd ou Astro 1-pager hébergé sur Cloudflare Pages
- [ ] Contenu : "Architekt — Coming soon. Studio agentique APAC. Contact: ___"
- [ ] Email contact (architekt.work@... ou GSuite SG)

## Plan jour par jour (5 jours ouvrés)

### Jour 1 — Décisions + ADR + entité

- Écrire / merger 5 ADR initiaux (001-006) — fait dans PR #1
- Trancher Q1 (domaine) et Q3 (licence) ou reporter explicitement
- Issue GitHub `[EPIC][P0]` créée (via setup-project.sh)
- **Entité légale SG** : si pas ouverte, démarrer process (ACRA — ~2 semaines)

### Jour 2 — README + docs + brand

- Search & replace `Software Factory` → `Architekt`
- Mise à jour CODE_OF_CONDUCT, SECURITY, CONTRIBUTING
- Brand : palette + typo + voice écrits
- Commit `docs: rebrand README + brand system`

### Jour 3 — UI templates + landing

- `base.html`, `login.html`, `onboarding.html`, `home.html`
- Tokens CSS `--purple` → `--brand-primary`
- Landing page Carrd ou Astro
- Commit `feat(ui): rebrand templates + landing`

### Jour 4 — Legal pack

- NDA + MSA + SOW + DPA templates (Markdown)
- IP + AI clauses
- Commit `docs(legal): NDA, MSA, SOW, DPA templates`
- Envoi à avocat SG pour revue (en parallèle)

### Jour 5 — env vars + pyproject + CLI

- `ARCHITEKT_API_KEY` alias
- `pyproject.toml` rename
- CLI alias `architekt`
- Commit final + PR merge

## Gate de passage

- [ ] Marque Architekt appliquée partout (Niveau 1 + 2)
- [ ] Anciens noms (Macaron / Software Factory) supprimés du visible
- [ ] Licence décidée (ADR-006 mergé)
- [ ] 7 templates commerciaux + legal prêts
- [ ] Politique IP/IA écrite (ADR-013)
- [ ] Landing page placeholder live
- [ ] CI verte
- [ ] Sync La Poste vérifiée (dry-run OK)

## Risques + mitigations

| Risque | Mitigation |
|--------|-----------|
| Casser Azure prod existant | Niveau 3 reporté ; alias env vars |
| Sync La Poste casse | Test dry-run avant merge |
| Search/replace agressif casse code | Revue PR obligatoire |
| Legal pack trop léger | Revue avocat SG dès J5 |
| Décisions ouvertes bloquent | Placeholders documentés, décisions documentées dans ADR |

## Suivi

- Milestone GitHub : **Phase 0 — Foundation & Rebrand**
- Labels : `phase:0-foundation`, `area:rebrand`, `area:docs`, `area:ui`, `area:legal`, `area:brand`
- Issues : créées via `scripts/github/setup-project.sh`
