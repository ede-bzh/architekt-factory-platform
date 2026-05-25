# Architekt — Guide des releases

## Versioning

- Fichier canonique : `platform/VERSION` (semver `MAJOR.MINOR.PATCH`).
- Override runtime : variable d'environnement `PLATFORM_VERSION`.
- Surfaces exposées : OpenAPI (`app.version`), Jinja `app_version`, `/api/health`, OTEL `service.version`.

## Checklist pré-déploiement

1. CI verte sur `main` (pytest, ruff, bandit, pip-audit, secret-scan, tests rebrand).
2. Mettre à jour `CHANGELOG.md` (section Released + tag).
3. Vérifier `platform/VERSION` aligné avec le tag Git `v*`.
4. Télécharger l'artefact CI `sbom-platform` (CycloneDX) pour la release.
5. Smoke : `curl -s http://localhost:8099/api/health` → `status`, `version`, `timestamp`.
6. Déployer uniquement après CI (workflows `deploy-demo` / GitLab Azure avec `needs: ci`).

## Tags GitHub

Sur push de tag `v*` :

- Job `release` dans `.github/workflows/ci.yml` attache `sbom-platform.json` et résume pytest.

## Docker (vague E — hors release courante)

Le package runtime reste `macaron_platform` dans les images existantes. Le renommage `architekt_platform` est documenté dans `docs/adr/001-rebrand-architekt.md` et traité en vague E séparée.

## Rollback

1. Redéployer l'image ou le commit du tag précédent.
2. `PLATFORM_VERSION` peut pointer vers l'ancienne version pour les sondes sans rebuild immédiat.

## Compliance (DPA)

Modèles de Data Processing Agreement par région pour engagements clients : [`docs/compliance/dpa/`](../compliance/dpa/).

| Région | Fichier | Cadre |
|--------|---------|-------|
| Singapore | `dpa-singapore.md` | PDPA |
| UAE | `dpa-uae.md` | PDPL |
| EU | `dpa-eu.md` | GDPR (Art. 28) |
| US | `dpa-us.md` | SCC-oriented processor / CCPA-ready |

Faire relire par conseil juridique avant signature. Matrice régionale : [`docs/COMPLIANCE.md`](../COMPLIANCE.md).
