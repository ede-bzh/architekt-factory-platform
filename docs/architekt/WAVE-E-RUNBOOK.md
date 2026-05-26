# Vague E — Runtime `architekt_platform`

**ADR** : [`docs/adr/001-rebrand-architekt.md`](../adr/001-rebrand-architekt.md) (niveau 3)  
**Statut repo** : livré (image Docker + `platform/runtime.py`)

## Layout runtime

| Contexte | Import Python | Chemin code |
|----------|---------------|-------------|
| Dev local | `platform` | `./platform/` |
| Image Docker prod | `architekt_platform` | `/app/architekt_platform/` |

| Paramètre | Valeur |
|-----------|--------|
| User Docker | `architekt` |
| OTEL défaut | `architekt-platform` |
| PG défaut compose | `architekt_platform` (surchargé par `.env` prod) |
| Clé API | `ARCHITEKT_API_KEY` |

## Détection runtime (code)

```python
from platform.runtime import runtime_package_name, container_code_dir, runtime_module

runtime_package_name()   # "platform" (dev) | "architekt_platform" (conteneur)
container_code_dir()     # Path | None
runtime_module("mcp_platform.server")
```

## Déploiement Azure (checklist)

1. Merger la release et tagger.
2. Vérifier `/opt/architekt/.env` : `PG_DB`, `DATABASE_URL`, `ARCHITEKT_API_KEY`, `OTEL_SERVICE_NAME=architekt-platform`.
3. Rebuild :
   ```bash
   cd /opt/architekt
   docker compose --env-file .env -f platform/deploy/docker-compose-vm.yml up -d --build --no-deps platform
   ```
4. Health : `curl -sf http://localhost/api/health` (nginx) ou port 8090 dans le conteneur.
5. Hotpatch CI : copie vers `/app/architekt_platform/` (voir `.github/workflows/deploy-azure.yml`).

## Rollback

Revenir au tag/image précédente ou restaurer le snapshot VM.
