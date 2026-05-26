# Guide de déploiement

Comment exécuter la plateforme d'agents **Architekt** (Architekt Factory) en démo, production et développement local.

## Portes CI/CD de déploiement

Les déploiements démo et production ne partent **qu'après un workflow CI réussi** sur `main` :

| Workflow | Déclencheur | Condition |
|----------|-------------|-----------|
| `CI` | push/PR sur `main`, tags `v*` | ruff, bandit (High), pip-audit, secret-scan, pytest |
| `Deploy → OVH Demo` | `workflow_run` après CI | `conclusion == success` |
| `Deploy → Azure Prod` | `workflow_run` après CI ou `workflow_dispatch` | CI verte (sauf dispatch manuel) |

Les tags `v*` déclenchent aussi le job SBOM CI. Voir `docs/architekt/RELEASE.md`.

## Noms de package runtime (vague E)

Le dépôt utilise toujours le répertoire **`platform/`**. L'image Docker prod (`platform/deploy/Dockerfile`) installe le code sous **`architekt_platform`** (ADR-001 niveau 3).

| Contexte | Import Python | Chemin conteneur |
|----------|---------------|------------------|
| Dev local | `platform` | `platform/` à la racine du dépôt |
| **Docker cible** (post-rebuild) | `architekt_platform` | `/app/architekt_platform/` |
| Alias legacy (6 mois) | `architekt_platform` | Symlink → `architekt_platform` |
| Image non reconstruite | `architekt_platform` | `/app/architekt_platform/` (répertoire réel) |

Détection dans le code : `platform/runtime.py` (`runtime_package_name()`, `container_code_dir()`).

**Runbook opérationnel (rebuild, rollback, `.env` PG) :** [`docs/architekt/WAVE-E-RUNBOOK.md`](../architekt/WAVE-E-RUNBOOK.md).

> Les **noms d'infra Azure** restent legacy tant qu'une migration dédiée n'est pas faite : arborescence VM `/opt/architekt`, hôte PG `architekt-platform-pg...`, base `architekt_platform` si `PG_DB` est défini dans `.env`. Seul le **package Python dans le conteneur** est rebrandé.

## Comparaison des environnements

| | **Démo Architekt (OVH)** | **Production Azure** |
|---|--------------------------|----------------------|
| **Objectif** | Démo publique, sans clés LLM | Production client, Azure OpenAI |
| **Hôte** | VPS OVH (`<OVH_IP>`) | VM Azure (`<AZURE_VM_IP>`, francecentral) |
| **Utilisateur SSH** | `debian@<OVH_IP>` | `azureadmin@<AZURE_VM_IP>` |
| **URL** | `http://<OVH_IP>` | `http://<AZURE_VM_IP>` (+ auth basique nginx) |
| **LLM** | `PLATFORM_LLM_PROVIDER=demo` (mock) | Azure OpenAI `gpt-5-mini` |
| **Package Python** | `platform` (layout dépôt) | `architekt_platform` dans le conteneur (cible) |
| **Conteneur** | `software-factory-platform-1` | `deploy-platform-1` |
| **Code sur la VM** | `/opt/software-factory/` | `/opt/architekt/platform/` (chemin hôte inchangé) |
| **Fichier Compose** | `/opt/software-factory/platform/docker-compose.yml` | `/opt/architekt/platform/deploy/docker-compose-vm.yml` |
| **Base de données** | SQLite | PostgreSQL (`PG_DB` via `.env`, souvent `architekt_platform`) |
| **Tracing** | Optionnel | OTEL `architekt-platform` → Jaeger `:16686` |
| **Clé API (env)** | `ARCHITEKT_API_KEY` (recommandé) | `ARCHITEKT_API_KEY` ou legacy `ARCHITEKT_API_KEY` |

Les nouvelles intégrations ciblent la **démo OVH** et le module `platform`. Les chemins **hôte** Azure restent sous `/opt/architekt` jusqu'à migration infra.

---

## Démo Architekt (OVH)

| Propriété | Valeur |
|-----------|--------|
| VPS | OVH, Debian |
| Web | `http://<OVH_IP>` |
| LLM | Mode démo — pas de clé fournisseur |
| Image | `software-factory-platform:v2` |
| Données | SQLite sous `/opt/software-factory/data/` |

### Déploiement (CI ou manuel)

```bash
rsync -avz --delete /tmp/gh_push_ops/software-factory/ <OVH_IP>:/opt/software-factory/
ssh <OVH_IP> "cd /opt/software-factory && sudo docker compose up -d --build"
```

GitHub Actions : `.github/workflows/deploy-demo.yml` — secrets `OVH_SSH_KEY`, `OVH_IP`.

### LLM démo

```bash
PLATFORM_LLM_PROVIDER=demo
```

Aucune `ARCHITEKT_API_KEY` requise pour l'exploration en lecture seule ; définissez une clé si vous exposez des mutations publiquement.

---

## Développement local

| Propriété | Valeur |
|-----------|--------|
| Plateforme | `http://localhost:8099` |
| Dashboard | `http://localhost:8080` |
| Module | `platform` (exécution depuis la racine du dépôt) |
| DB | `data/platform.db` (SQLite) |
| LLM | MiniMax `MiniMax-M2.5` (ou surcharge via env) |

```bash
# Plateforme (JAMAIS --reload, TOUJOURS --ws none)
python3 -m uvicorn platform.server:app --host 0.0.0.0 --port 8099 --ws none --log-level warning

# Dashboard
python3 -m dashboard.server

# Tests
python3 -m pytest tests/ -v
```

Clé API optionnelle pour tester les mutations en local :

```bash
export ARCHITEKT_API_KEY="architekt_dev_$(openssl rand -hex 16)"
```

---

## Démarrage rapide Docker (poste local)

```bash
git clone https://github.com/ede-bzh/architekt-factory-platform.git
cd architekt-factory-platform
make setup
make run
# → http://localhost:8090
```

Le `Dockerfile` racine (poste local) utilise encore `platform` sur le port **8099**. L'image VM prod utilise `platform/deploy/Dockerfile` → `architekt_platform` sur le port **8090**.

Démo sans clés LLM :

```bash
PLATFORM_LLM_PROVIDER=demo make run
```

---

## Production Azure (VM `/opt/architekt`)

> **Arborescence hôte legacy** (`/opt/architekt`, hôte PG `architekt-platform-pg`). **Runtime conteneur** : vague E → import `architekt_platform` après rebuild d'image.

| Propriété | Valeur |
|-----------|--------|
| VM | D4as_v5 (4 CPU, 16 Go), francecentral |
| Web | `http://<AZURE_VM_IP>` (auth basique nginx) |
| LLM | Azure OpenAI / gpt-5-mini |
| Conteneur | `deploy-platform-1` |
| **Code conteneur (cible)** | `/app/architekt_platform/` |
| **Symlink / ancienne image** | `/app/architekt_platform/` |
| Compose sur la VM | `/opt/architekt/platform/deploy/docker-compose-vm.yml` |
| Contexte de build | `/opt/architekt` |
| Répertoire patches | `/opt/architekt/patches/` |
| DB | PostgreSQL Azure + adaptateur dual ; garder `PG_DB=architekt_platform` dans `.env` jusqu'au renommage DB |

### Rebuild complet (image vague E)

```bash
cd /opt/architekt
docker compose --env-file .env -f platform/deploy/docker-compose-vm.yml up -d --build --no-deps platform
```

Vérification dans le conteneur :

```bash
docker exec deploy-platform-1 python3 -c "from architekt_platform.runtime import runtime_package_name; print(runtime_package_name())"
# Attendu : architekt_platform
```

### Déploiement à chaud (CI ou manuel, sans rebuild)

GitHub Actions (`.github/workflows/deploy-azure.yml`) copie vers `architekt_platform` ou `architekt_platform` selon l'image en cours.

Rsync + redémarrage manuel :

```bash
rsync -avz platform/ azureadmin@<AZURE_VM_IP>:/home/azureadmin/architekt_update/platform/
ssh azureadmin@<AZURE_VM_IP> '
  CONTAINER=$(docker ps --format "{{.Names}}" | grep -E "platform" | head -1)
  PKG=$(docker exec $CONTAINER bash -c "[ -d /app/architekt_platform ] && echo architekt_platform || echo architekt_platform")
  docker cp ~/architekt_update/platform/. $CONTAINER:/app/$PKG/
  docker restart $CONTAINER
'
```

### Répertoire patches (optionnel)

```bash
ssh <AZURE_VM_IP> "sudo cp /home/azureadmin/platform/web/routes/*.py /opt/architekt/patches/"
```

GitLab CI : `.gitlab-ci.yml` — variables `AZURE_SSH_KEY`, `AZURE_VM_IP`, `AZURE_USER`.

### Note hotpatch

`docker cp` survit au redémarrage du conteneur mais est **perdu** sur `docker compose --build` — rsync vers la VM avant reconstruction.

---

## Helm (Kubernetes)

Chart : `deploy/helm/architekt/` (`architekt-platform`). Le chart `deploy/helm/architekt/` reste en référence jusqu'à suppression.

---

## Checklist des secrets

| Environnement | Secret | Emplacement |
|---------------|--------|-------------|
| Démo OVH | `OVH_SSH_KEY`, `OVH_IP` | GitHub Actions |
| Azure | `AZURE_SSH_KEY`, `AZURE_VM_IP` (ou `AZURE_IP`) | GitHub / GitLab CI/CD |
| Toute prod | `ARCHITEKT_API_KEY` | `.env` VM / secrets orchestrateur |
| LLM | Clés fournisseur dans `~/.config/factory/*.key` | Jamais `*_API_KEY=dummy` |

---

## Documentation associée

- [Référence API](API-Reference) — en-tête d'auth pour les hôtes déployés
- [Sécurité](Security) — nginx, CSP, portes HITL
- [Configuration LLM](LLM-Configuration) — fournisseur par environnement
- [Runbook vague E](../architekt/WAVE-E-RUNBOOK.md) — renommage conteneur, rollback, `.env` PG

[English](Deployment-Guide)
