# Deployment Guide

How to run the **Architekt** agent platform across demo, production, and local environments.

## CI/CD deploy gates

Production and demo deploys run **only after a successful CI workflow** on `main`:

| Workflow | Trigger | Gate |
|----------|---------|------|
| `CI` | push/PR to `main`, tags `v*` | ruff, bandit (High), pip-audit, secret-scan, pytest |
| `Deploy → OVH Demo` | `workflow_run` after CI | `conclusion == success` |
| `Deploy → Azure Prod` | `workflow_run` after CI or manual dispatch | CI green (unless `workflow_dispatch`) |

Release tags `v*` also trigger the CI SBOM artifact job. See `docs/architekt/RELEASE.md`.

## Runtime package names (Wave E)

The **repo layout** always uses the directory `platform/`. Inside Docker images built from `platform/deploy/Dockerfile`, code is installed as **`architekt_platform`** (ADR-001 level 3).

| Context | Python import | Path in container |
|---------|---------------|-------------------|
| Local dev | `platform` | `platform/` at repo root |
| Docker (prod VM image) | `architekt_platform` | `/app/architekt_platform/` |

Detection in code: `platform/runtime.py` (`runtime_package_name()`, `container_code_dir()`).

**Operational runbook (rebuild, rollback, `.env` PG):** [`docs/architekt/WAVE-E-RUNBOOK.md`](../architekt/WAVE-E-RUNBOOK.md).

> **Ops note:** Some Azure control-plane resource IDs (e.g. managed PostgreSQL server hostname) may still use historical names in the portal; runtime on the VM uses `/opt/architekt`, user `architekt`, and `PG_DB=architekt_platform` in `.env`.

## Environment comparison

| | **Architekt demo (OVH)** | **Azure production** |
|---|--------------------------|----------------------|
| **Purpose** | Public demo, no LLM keys required | Customer production, Azure OpenAI |
| **Host** | OVH VPS (`<OVH_IP>`) | Azure VM (`<AZURE_VM_IP>`, francecentral) |
| **SSH user** | `debian@<OVH_IP>` | `architekt@<AZURE_VM_IP>` |
| **URL** | `http://<OVH_IP>` | `http://<AZURE_VM_IP>` (+ nginx basic auth) |
| **LLM** | `PLATFORM_LLM_PROVIDER=demo` (mock) | Azure OpenAI `gpt-5-mini` |
| **Python package** | `platform` (repo layout) | `architekt_platform` in container |
| **Container** | `software-factory-platform-1` | `deploy-platform-1` |
| **Code on VM** | `/opt/software-factory/` | `/opt/architekt/platform/` |
| **Compose file** | `/opt/software-factory/platform/docker-compose.yml` | `/opt/architekt/platform/deploy/docker-compose-vm.yml` |
| **Database** | SQLite | PostgreSQL (`PG_DB` from `.env`, often `architekt_platform`) |
| **Tracing** | Optional | OTEL `architekt-platform` → Jaeger `:16686` |
| **API key env** | `ARCHITEKT_API_KEY` | `ARCHITEKT_API_KEY` |

New integrations should target **OVH demo** paths and the `platform` module. Azure production uses `/opt/architekt` and `architekt_platform` in the container.

---

## Architekt demo (OVH)

| Property | Value |
|----------|-------|
| VPS | OVH, Debian |
| Web | `http://<OVH_IP>` |
| LLM | Demo mode — no provider API key |
| Image | `software-factory-platform:v2` |
| Data | SQLite under `/opt/software-factory/data/` |

### Deploy (CI or manual)

```bash
rsync -avz --delete /tmp/gh_push_ops/software-factory/ <OVH_IP>:/opt/software-factory/
ssh <OVH_IP> "cd /opt/software-factory && sudo docker compose up -d --build"
```

GitHub Actions: `.github/workflows/deploy-demo.yml` — secrets `OVH_SSH_KEY`, `OVH_IP`.

### Demo LLM

```bash
PLATFORM_LLM_PROVIDER=demo
```

No `ARCHITEKT_API_KEY` required for read-only exploration; set a key if you expose mutations publicly.

---

## Local development

| Property | Value |
|----------|-------|
| Platform | `http://localhost:8099` |
| Dashboard | `http://localhost:8080` |
| Module | `platform` (run from repo root) |
| DB | `data/platform.db` (SQLite) |
| LLM | MiniMax `MiniMax-M2.5` (or env override) |

```bash
# Platform (NEVER --reload, ALWAYS --ws none)
python3 -m uvicorn platform.server:app --host 0.0.0.0 --port 8099 --ws none --log-level warning

# Dashboard
python3 -m dashboard.server

# Tests
python3 -m pytest tests/ -v
```

Optional API key for local mutation testing:

```bash
export ARCHITEKT_API_KEY="architekt_dev_$(openssl rand -hex 16)"
```

---

## Docker quick start (laptop)

```bash
git clone https://github.com/ede-bzh/architekt-factory-platform.git
cd architekt-factory-platform
make setup    # install deps, init DB
make run      # start Docker containers
# → http://localhost:8090
```

Root `Dockerfile` (dev laptop) still uses `platform` on port **8099**. Production VM image uses `platform/deploy/Dockerfile` → `architekt_platform` on port **8090**.

Demo without LLM keys:

```bash
PLATFORM_LLM_PROVIDER=demo make run
```

---

## Azure production (VM `/opt/architekt`)

| Property | Value |
|----------|-------|
| VM | D4as_v5 (4 CPU, 16 GB), francecentral |
| SSH user | `architekt@<AZURE_VM_IP>` |
| Web | `http://<AZURE_VM_IP>` (nginx basic auth) |
| LLM | Azure OpenAI / gpt-5-mini |
| Container | `deploy-platform-1` |
| In-container code | `/app/architekt_platform/` |
| Compose on VM | `/opt/architekt/platform/deploy/docker-compose-vm.yml` |
| Build context | `/opt/architekt` |
| Patches dir | `/opt/architekt/patches/` (applied at container start) |
| DB | Azure PostgreSQL + dual adapter; `PG_DB=architekt_platform` in `.env` |

### Full rebuild (Wave E image)

```bash
cd /opt/architekt
docker compose --env-file .env -f platform/deploy/docker-compose-vm.yml up -d --build --no-deps platform
```

Verify inside the container:

```bash
docker exec deploy-platform-1 python3 -c "from architekt_platform.runtime import runtime_package_name; print(runtime_package_name())"
# Expected: architekt_platform
```

### Hot deploy (CI or manual, no rebuild)

GitHub Actions (`.github/workflows/deploy-azure.yml`) copies into `/app/architekt_platform/`.

Manual rsync + restart:

```bash
rsync -avz platform/ architekt@<AZURE_VM_IP>:/home/architekt/architekt_update/platform/
ssh architekt@<AZURE_VM_IP> '
  CONTAINER=$(docker ps --format "{{.Names}}" | grep -E "platform" | head -1)
  docker cp ~/architekt_update/platform/. $CONTAINER:/app/architekt_platform/
  docker restart $CONTAINER
'
```

### Patch directory (optional)

```bash
ssh <AZURE_VM_IP> "sudo cp /home/azureadmin/platform/web/routes/*.py /opt/architekt/patches/"
```

GitLab CI: `.gitlab-ci.yml` — variables `AZURE_SSH_KEY`, `AZURE_VM_IP`, `AZURE_USER`.

### Hotpatch note

`docker cp` survives container restart but is **lost** on `docker compose --build` — rsync to the VM before rebuild.

---

## Helm (Kubernetes)

Chart: `deploy/helm/architekt/` (`architekt-platform`).

---

## Secrets checklist

| Environment | Secret | Where |
|-------------|--------|-------|
| OVH demo | `OVH_SSH_KEY`, `OVH_IP` | GitHub Actions |
| Azure | `AZURE_SSH_KEY`, `AZURE_VM_IP` (or `AZURE_IP`) | GitHub / GitLab CI/CD |
| All prod | `ARCHITEKT_API_KEY` | VM `.env` / orchestrator secrets |
| LLM | Provider keys in `~/.config/factory/*.key` | Never `*_API_KEY=dummy` |

---

## Related docs

- [API Reference](API-Reference) — auth header for deployed hosts
- [Security](Security) — nginx, CSP, HITL gates
- [LLM Configuration](LLM-Configuration) — provider per environment
- [Wave E runbook](../architekt/WAVE-E-RUNBOOK.md) — container rename, rollback, PG `.env`

## 🇫🇷 [Guide de déploiement (FR)](Deployment-Guide‐FR)
