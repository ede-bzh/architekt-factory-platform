# ADR-001 : Rebrand de Software Factory vers Architekt

- **Statut** : Accepté (niveaux 1–3 livrés — vague E 2026-05-24)
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO
- **Contexte business** : création de la société **Architekt Pte. Ltd.** (Singapour), studio agentique pour livrer sites & plateformes en Asie.

## Contexte

Le code portait deux marques mélangées :

- **Software Factory** (README, UI, docs publiques)
- Ancienne marque interne (package, clés API, domaines historiques)

**Architekt** (orthographe `A-R-C-H-I-T-E-K-T`) est la marque officielle unique dans le dépôt.

## Décision

Rebrand complet en **trois niveaux** :

### Niveau 1 — Visible

- README + variantes langues → marque Architekt
- Titres pages UI → Architekt
- Domaine cible : `sf.architekt.ai`

### Niveau 2 — Identifiants

- Variables d'env : `ARCHITEKT_*` (ex. `ARCHITEKT_API_KEY`, `ARCHITEKT_URL`, `ARCHITEKT_TOKEN`)
- CLI : `sf` (client) avec env `ARCHITEKT_URL` / `ARCHITEKT_TOKEN`
- `pyproject.toml` : `name = "architekt-factory-platform"`

### Niveau 3 — Runtime / packaging (vague E)

- Package Python conteneur : `architekt_platform` à `/app/architekt_platform/`
- Image Docker : user `architekt`, `uvicorn architekt_platform.server:app`
- Helm chart : `deploy/helm/architekt/`
- Métriques Prometheus : préfixe `architekt_*` uniquement

## Conséquences

- Dev local : import `platform` (répertoire source `platform/`)
- Prod Docker : import `architekt_platform` (même code, chemin image différent)
- Pas d'alias legacy (`MACARON_*`, symlink `macaron_platform`) dans le dépôt

## Suivi

- Runbook ops : [`docs/architekt/WAVE-E-RUNBOOK.md`](../architekt/WAVE-E-RUNBOOK.md)
- Gate doc : `tests/test_doc_no_macaron_user_facing.py`
