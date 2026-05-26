# Guide de déploiement

Comment exécuter la plateforme d'agents **Architekt** (Architekt Factory) en démo, production et développement local.

## Comparaison des environnements

| | **Démo Architekt (OVH)** | **Production Azure (legacy)** |
|---|--------------------------|-------------------------------|
| **Objectif** | Démo publique, sans clés LLM | Production client, Azure OpenAI |
| **Hôte** | VPS OVH (`<OVH_IP>`) | VM Azure (`<AZURE_VM_IP>`, francecentral) |
| **Utilisateur SSH** | `debian@<OVH_IP>` | `azureadmin@<AZURE_VM_IP>` (ou legacy `macaron@`) |
| **URL** | `http://<OVH_IP>` | `http://<AZURE_VM_IP>` (+ auth basique nginx) |
| **LLM** | `PLATFORM_LLM_PROVIDER=demo` (mock) | Azure OpenAI `gpt-5-mini` |
| **Package Python** | `platform` (layout dépôt) | `macaron_platform` (alias d'import dans le conteneur) |
| **Conteneur** | `software-factory-platform-1` | `deploy-platform-1` |
| **Code sur la VM** | `/opt/software-factory/` | `/opt/macaron/platform/` |
| **Fichier Compose** | `/opt/software-factory/platform/docker-compose.yml` | `/opt/macaron/platform/deploy/docker-compose-vm.yml` |
| **Base de données** | SQLite | PostgreSQL + adaptateur SQLite |
| **Tracing** | Optionnel | OTEL → Jaeger `:16686` |
| **Clé API (env)** | `ARCHITEKT_API_KEY` (recommandé) | `ARCHITEKT_API_KEY` ou legacy `MACARON_API_KEY` |

Les nouvelles intégrations doivent cibler les chemins **démo OVH** et le module `platform`. Les lignes Azure sont **legacy** jusqu'à la fin de la migration.

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

Démo sans clés LLM :

```bash
PLATFORM_LLM_PROVIDER=demo make run
```

---

## Production Azure (legacy)

> **Legacy uniquement.** Le conteneur importe `macaron_platform`, pas `platform`. N'utilisez pas ces chemins pour de nouveaux déploiements Architekt sauf si vous opérez cette stack.

| Propriété | Valeur |
|-----------|--------|
| VM | D4as_v5 (4 CPU, 16 Go), francecentral |
| Web | `http://<AZURE_VM_IP>` (auth basique nginx) |
| LLM | Azure OpenAI / gpt-5-mini |
| Conteneur | `deploy-platform-1` |
| **Code dans le conteneur** | `/app/macaron_platform/` |
| Compose sur la VM | `/opt/macaron/platform/deploy/docker-compose-vm.yml` |
| Contexte de build | `/opt/macaron` |
| Répertoire patches | `/opt/macaron/patches/` (appliqués au démarrage du conteneur) |
| DB | PostgreSQL Azure (`macaron-platform-pg...`) + adaptateur dual |

### Processus de déploiement legacy

```bash
# 1. rsync depuis l'artefact de build vers la VM
rsync -avz /tmp/gh_push_ops/software-factory/{platform,cli,skills,dashboard,mcp_lrm,projects}/ \
  <AZURE_VM_IP>:/home/macaron/

# 2. Hot-patch de fichiers (optionnel)
ssh <AZURE_VM_IP> "sudo cp /home/macaron/platform/web/routes/*.py /opt/macaron/patches/"

# 3. Redémarrage du conteneur legacy
ssh <AZURE_VM_IP> "sudo docker restart deploy-platform-1"
```

Reconstruction complète :

```bash
ssh <AZURE_VM_IP> "cd /opt/macaron && docker compose -f platform/deploy/docker-compose-vm.yml up -d --build"
```

GitLab CI : `.gitlab-ci.yml` — variables `AZURE_SSH_KEY`, `AZURE_VM_IP`, `AZURE_USER`.

### Note hotpatch legacy

`docker cp` vers `deploy-platform-1:/app/macaron_platform/` survit au redémarrage mais est **perdu** sur `docker compose --build` — rsync vers la VM avant reconstruction.

---

## Checklist des secrets

| Environnement | Secret | Emplacement |
|---------------|--------|-------------|
| Démo OVH | `OVH_SSH_KEY`, `OVH_IP` | GitHub Actions |
| Azure legacy | `AZURE_SSH_KEY`, `AZURE_VM_IP`, `AZURE_USER` | GitLab CI/CD |
| Toute prod | `ARCHITEKT_API_KEY` | `.env` VM / secrets orchestrateur |
| LLM | Clés fournisseur dans `~/.config/factory/*.key` | Jamais `*_API_KEY=dummy` |

---

## Documentation associée

- [Référence API](API-Reference) — en-tête d'auth pour les hôtes déployés
- [Sécurité](Security) — nginx, CSP, portes HITL
- [Configuration LLM](LLM-Configuration) — fournisseur par environnement

[English](Deployment-Guide)
