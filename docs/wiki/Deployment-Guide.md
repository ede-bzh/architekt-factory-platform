# Deployment Guide

How to run the **Architekt** agent platform (Software Factory) across demo, production, and local environments.

## Environment comparison

| | **Architekt demo (OVH)** | **Legacy Azure production** |
|---|--------------------------|----------------------------|
| **Purpose** | Public demo, no LLM keys required | Customer production, Azure OpenAI |
| **Host** | OVH VPS (`<OVH_IP>`) | Azure VM (`<AZURE_VM_IP>`, francecentral) |
| **SSH user** | `debian@<OVH_IP>` | `azureadmin@<AZURE_VM_IP>` (or legacy `macaron@`) |
| **URL** | `http://<OVH_IP>` | `http://<AZURE_VM_IP>` (+ nginx basic auth) |
| **LLM** | `PLATFORM_LLM_PROVIDER=demo` (mock) | Azure OpenAI `gpt-5-mini` |
| **Python package** | `platform` (repo layout) | `macaron_platform` (import alias in container) |
| **Container** | `software-factory-platform-1` | `deploy-platform-1` |
| **Code on VM** | `/opt/software-factory/` | `/opt/macaron/platform/` |
| **Compose file** | `/opt/software-factory/platform/docker-compose.yml` | `/opt/macaron/platform/deploy/docker-compose-vm.yml` |
| **Database** | SQLite | PostgreSQL + SQLite adapter |
| **Tracing** | Optional | OTEL → Jaeger `:16686` |
| **API key env** | `ARCHITEKT_API_KEY` (preferred) | `ARCHITEKT_API_KEY` or legacy `MACARON_API_KEY` |

New integrations should target **OVH demo** paths and `platform` module names. Azure rows are **legacy** until migration completes.

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
git clone https://github.com/macaron-software/software-factory.git
cd software-factory
make setup
make run
# → http://localhost:8090
```

Demo without LLM keys:

```bash
PLATFORM_LLM_PROVIDER=demo make run
```

---

## Legacy Azure production

> **Legacy only.** Container imports `macaron_platform`, not `platform`. Do not use these paths for new Architekt deployments unless you operate this stack.

| Property | Value |
|----------|-------|
| VM | D4as_v5 (4 CPU, 16 GB), francecentral |
| Web | `http://<AZURE_VM_IP>` (nginx basic auth) |
| LLM | Azure OpenAI / gpt-5-mini |
| Container | `deploy-platform-1` |
| **In-container code** | `/app/macaron_platform/` |
| Compose on VM | `/opt/macaron/platform/deploy/docker-compose-vm.yml` |
| Build context | `/opt/macaron` |
| Patches dir | `/opt/macaron/patches/` (applied at container start) |
| DB | Azure PostgreSQL (`macaron-platform-pg...`) + dual adapter |

### Legacy deploy process

```bash
# 1. rsync from build artifact to VM
rsync -avz /tmp/gh_push_ops/software-factory/{platform,cli,skills,dashboard,mcp_lrm,projects}/ \
  <AZURE_VM_IP>:/home/macaron/

# 2. Hot-patch files (optional)
ssh <AZURE_VM_IP> "sudo cp /home/macaron/platform/web/routes/*.py /opt/macaron/patches/"

# 3. Restart legacy container
ssh <AZURE_VM_IP> "sudo docker restart deploy-platform-1"
```

Full rebuild:

```bash
ssh <AZURE_VM_IP> "cd /opt/macaron && docker compose -f platform/deploy/docker-compose-vm.yml up -d --build"
```

GitLab CI: `.gitlab-ci.yml` — variables `AZURE_SSH_KEY`, `AZURE_VM_IP`, `AZURE_USER`.

### Legacy hotpatch note

`docker cp` into `deploy-platform-1:/app/macaron_platform/` survives restart but is **lost** on `docker compose --build` — rsync to the VM before rebuild.

---

## Secrets checklist

| Environment | Secret | Where |
|-------------|--------|-------|
| OVH demo | `OVH_SSH_KEY`, `OVH_IP` | GitHub Actions |
| Azure legacy | `AZURE_SSH_KEY`, `AZURE_VM_IP`, `AZURE_USER` | GitLab CI/CD |
| All prod | `ARCHITEKT_API_KEY` | VM `.env` / orchestrator secrets |
| LLM | Provider keys in `~/.config/factory/*.key` | Never `*_API_KEY=dummy` |

---

## Related docs

- [API Reference](API-Reference) — auth header for deployed hosts
- [Security](Security) — nginx, CSP, HITL gates
- [LLM Configuration](LLM-Configuration) — provider per environment

## 🇫🇷 [Guide de déploiement (FR)](Deployment-Guide‐FR)
