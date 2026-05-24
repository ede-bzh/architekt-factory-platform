# ADR-001 : Rebrand de Software Factory / Macaron vers Architekt

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO
- **Contexte business** : création de la société **Architekt Pte. Ltd.** (Singapour), studio agentique pour livrer sites & plateformes en Asie.

## Contexte

Le code actuel porte deux marques mélangées :

- **Software Factory** (README, UI, docs publiques)
- **Macaron** (package Python `macaron_platform`, env vars `MACARON_API_KEY`, domaine `sf.macaron-software.com`)

Une troisième marque, **Architekt** (orthographe `A-R-C-H-I-T-E-K-T`), devient la marque officielle de la société exploitante.

## Décision

Rebrand complet en **trois niveaux** appliqués progressivement :

### Niveau 1 — Visible (Phase 0, immédiat)

- README + variantes langues → marque Architekt
- Titres pages UI (`base.html`, login, onboarding) → Architekt
- Emails / notifications → Architekt
- Domaine cible : `architekt.{TBD}` (`.sg`, `.ai`, `.io` à trancher après dispo)

### Niveau 2 — Identifiants (Phase 0/1, avec CI verte)

- Variables d'env : `MACARON_*` → `ARCHITEKT_*` (alias rétro-compatibles 6 mois)
- CLI : `sf` → `architekt` (alias `sf` gardé)
- `pyproject.toml` : `name = "architekt-factory-platform"`

### Niveau 3 — Runtime / packaging (Phase 3+, après pilote)

- Package Python `macaron_platform` → `architekt_platform`
- Image Docker `architekt-platform`
- Helm chart `architekt-platform`

## Justification du nom **Architekt**

- Orthographe distinctive (`K` au lieu de `C`) → marque déposable plus facilement
- Cohérent avec les **7 agents architecte** déjà présents dans la plateforme
- Aligné avec la dimension `architecture` (10%) du `QualityScanner`
- Évoque l'archi enterprise + delivery → positionnement premium

## Alternatives écartées

| Nom | Raison du rejet |
|-----|----------------|
| Architect Software Factory | Trop générique, SEO impossible |
| Macaron Architect | Conserve la dette de marque Macaron |
| Atelier Architekt | Trop francophone pour Singapour |

## Conséquences

### Positives
- Marque commerciale claire pour Architekt SG
- Distingue produit (Architekt Factory) de société (Architekt Pte. Ltd.)
- Cohérent avec la doctrine produit (architecture-first)

### Négatives / coûts
- ~70+ fichiers à toucher
- Sync La Poste (`sync-to-laposte.sh`) doit gérer 2 brandings
- Risque casser CI/CD si refactor mal séquencé → niveau 3 reporté à Phase 3+

### Risques
- Marque `Architekt` (orthographe DE) potentiellement confondue avec architectes du bâtiment → mitigé par tagline "AI-powered software studio"

## Plan d'action (résumé)

| Niveau | Phase | Bloquant |
|--------|-------|----------|
| 1 | Phase 0 | rien |
| 2 | Phase 1 | CI tests présente |
| 3 | Phase 3+ | pilote site Architekt en ligne |

## Suivi

- Issue tracker : milestone **Phase 0 — Rebrand**
- Revue : à la fin de Phase 1 (post-merge ADR-006 licence)

## Implémentation — alias API (2026-05-24)

- `platform/auth/api_key.py` : `get_platform_api_key()` lit `ARCHITEKT_API_KEY` puis `MACARON_API_KEY`.
- Middlewares `platform/security.py`, `platform/security/__init__.py`, `platform/auth/middleware.py` et health redaction utilisent ce helper.
- Fenêtre de migration documentée : **6 mois** — les deux noms restent valides ; préférer `ARCHITEKT_API_KEY` pour les nouveaux déploiements.
