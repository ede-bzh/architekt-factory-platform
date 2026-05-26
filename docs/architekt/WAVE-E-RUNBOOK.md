# Vague E — Renommage runtime `architekt_platform`

**ADR** : [`docs/adr/001-rebrand-architekt.md`](../adr/001-rebrand-architekt.md) (niveau 3)  
**Statut repo** : engagé (image Docker + helper `platform/runtime.py`)  
**Déploiement prod Azure** : à planifier (rebuild image + hotpatch compatible)

## Ce qui change dans le dépôt

| Avant | Après |
|-------|--------|
| `/app/macaron_platform/` (répertoire) | `/app/architekt_platform/` + symlink `macaron_platform` → 6 mois |
| `uvicorn macaron_platform.server:app` | `uvicorn architekt_platform.server:app` |
| User Docker `macaron` | User Docker `architekt` |
| OTEL `macaron-platform` (défaut) | OTEL `architekt-platform` |
| Compose PG défaut `macaron_platform` | Défaut `architekt_platform` (surchargé par `.env` prod) |

**Hors scope** (inchangé volontairement) :

- Arborescence VM `/opt/macaron`
- Hôte Azure PG `macaron-platform-pg.postgres.database.azure.com`
- Base prod `macaron_platform` tant que `PG_DB=macaron_platform` dans `.env`
- Compte blob `macaronbackups`, snapshots `vm-macaron-*`

## Détection runtime (code)

```python
from platform.runtime import runtime_package_name, container_code_dir, runtime_module

runtime_package_name()   # "platform" | "architekt_platform" | "macaron_platform"
container_code_dir()     # Path | None
runtime_module("mcp_platform.server")  # module dotted path
```

## Déploiement Azure (checklist)

1. **Merger** cette branche et tagger une release.
2. **Vérifier** `/opt/macaron/.env` sur la VM :
   - Conserver `PG_DB=macaron_platform`, `PG_USER=macaron`, `DATABASE_URL=...` tant que la DB Azure n’est pas migrée.
   - Optionnel : `OTEL_SERVICE_NAME=architekt-platform`
3. **Rebuild** (fenêtre maintenance ~15 min RTO code) :
   ```bash
   cd /opt/macaron
   docker compose --env-file .env -f platform/deploy/docker-compose-vm.yml up -d --build --no-deps platform
   ```
4. **Health** : `curl -sf http://localhost/api/health` (via nginx) ou depuis le conteneur port 8090.
5. **Hotpatch CI** (sans rebuild) : GitHub Actions détecte `architekt_platform` ou `macaron_platform` dans le conteneur.

## Rollback

- Revenir au tag/image précédente **ou**
- Hotpatch vers l’ancien layout si le conteneur n’a pas encore été reconstruit (`/app/macaron_platform` réel).

## Fin de vie alias (cible +6 mois)

- [ ] Retirer le symlink `macaron_platform` du Dockerfile
- [ ] Retirer la détection legacy dans `runtime.py` et le workflow deploy
- [ ] Mettre à jour la doc wiki Deployment (section legacy)
