# PR #27 — suggested description (`cursor/wave-e-full-replace-7576`)

Copy everything between the HTML comment markers into the GitHub PR body (replace existing body or merge with your notes).

<!-- PR_BODY_START -->

## Résumé

**Vague E complète** : remplacement intégral de la marque et des identifiants legacy Macaron dans le dépôt — plus d’approche hybride (alias `MACARON_*`, symlink `macaron_platform`, métriques dupliquées, encarts « infra inchangée »).

**10 commits** · **181 fichiers** · **+1428 / −817** lignes vs `main`

Supersedes **PR #25** (`cursor/wave-e-rename-7576`, rename partiel + symlink 6 mois) and **PR #26** (`cursor/wave-e-wiki-deployment-7576`, wiki Deployment seul). Ne pas merger #25 / #26 — fermer en faveur de cette PR.

## Commits (ordre chronologique)

| SHA | Sujet |
|-----|--------|
| `6ee114cd` | **feat(wave-e):** rename container package to `architekt_platform` — `platform/runtime.py`, Dockerfile, compose, deploy-azure workflow, tests |
| `7a62910d` | **docs(wiki):** align Deployment guides EN/FR with Wave E runtime table + runbook links |
| `d2027d1d` | **feat(rebrand):** remplacement intégral Macaron → Architekt — supprime Helm `macaron/`, alias API/métriques, CLI `ARCHITEKT_*`, workspaces `~/.architekt` |
| `873cff22` | **chore(ci):** `scripts/ci/run-local-gate.sh`, `scripts/rebrand_macaron_to_architekt.py`, tests vague E en CI |
| `eb65a3e9` | **fix(security):** CSP par défaut sans `unsafe-eval` (gate CI) |
| `2be66c91` | **docs:** strip hybrid legacy wording (deployment, API wiki) |
| `e695995e` | **ci:** unit gate → `test_doc_no_macaron_user_facing.py` |
| `731a6f2c` | **feat(helm):** chart `deploy/helm/architekt/` complet (2.3.0, `architekt_platform`, OTEL, PG) |
| `42c342ad` | **docs(wiki):** single-truth `ARCHITEKT_API_KEY` in API FR + Security |
| `17c30119` | **docs:** align `platform/CLAUDE.md`, `PLATFORM-BACKLOG`, phase-0 rebrand |

## Changements principaux

| Domaine | Détail |
|---------|--------|
| **Runtime prod** | `/app/architekt_platform/`, user Docker `architekt`, `uvicorn architekt_platform.server:app` |
| **Dev local** | import `platform/` inchangé ; détection via `platform/runtime.py` |
| **Auth / env** | `ARCHITEKT_API_KEY` uniquement (plus `MACARON_API_KEY`) |
| **Prometheus** | préfixe `architekt_*` seul |
| **Helm** | `deploy/helm/architekt/` ; suppression `deploy/helm/macaron/` |
| **Docs** | ADR-001 niveau 3, [`WAVE-E-RUNBOOK.md`](docs/architekt/WAVE-E-RUNBOOK.md), wiki Deployment/API/Security, `docs/ROADMAP.md` vague E ✅ |
| **CI** | gates branding/doc + `test_wave_e_runtime` ; script gate locale |
| **CSP** | politique standard sans `unsafe-eval` (workspace projets conservent exception documentée) |

## Tests (recommandés avant merge)

```bash
python3 -m pytest tests/test_wave_e_runtime.py tests/test_api_key_alias.py \
  tests/test_prometheus_architekt.py tests/test_doc_no_macaron_user_facing.py \
  tests/test_architekt_branding.py tests/test_readme_en_fr.py -q
```

Ou gate locale : `bash scripts/ci/run-local-gate.sh`

## Déploiement prod (post-merge, hors PR)

Rebuild image + compose sur `/opt/architekt` — voir [`docs/architekt/WAVE-E-RUNBOOK.md`](docs/architekt/WAVE-E-RUNBOOK.md) :

- `.env` : `ARCHITEKT_API_KEY`, `PG_DB` / `DATABASE_URL`, `OTEL_SERVICE_NAME=architekt-platform`
- `docker compose -f platform/deploy/docker-compose-vm.yml up -d --build --no-deps platform`
- Health + hotpatch CI vers `/app/architekt_platform/`

## Liens

- ADR : [`docs/adr/001-rebrand-architekt.md`](docs/adr/001-rebrand-architekt.md)
- Roadmap : vague E marquée livrée dépôt dans [`docs/ROADMAP.md`](docs/ROADMAP.md)
- **Fermer sans merge** : PR #25, PR #26

<!-- PR_BODY_END -->

## Apply with GitHub CLI

```bash
gh pr edit 27 --body-file PR_UPDATE.md
# Or extract only the section between PR_BODY_START / PR_BODY_END
```
