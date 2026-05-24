# Local development — Architekt platform

Quick reference for running the platform locally without Docker or real LLM keys.

## Start the server (demo LLM)

From the repository root:

```bash
PLATFORM_LLM_PROVIDER=demo make dev
```

`make dev` runs uvicorn on **http://localhost:8090** with `PYTHONPATH` set to the repo root.

Equivalent without Make:

```bash
PLATFORM_LLM_PROVIDER=demo PYTHONPATH=. python3 -m uvicorn platform.server:app \
  --host 0.0.0.0 --port 8090 --ws none --log-level info
```

For day-to-day dev some teams use port **8099** instead:

```bash
PLATFORM_LLM_PROVIDER=demo PYTHONPATH=. python3 -m uvicorn platform.server:app \
  --host 0.0.0.0 --port 8099 --ws none --log-level warning
```

Do not pass `--reload` (conflicts with the stdlib `platform` module).

## API key (`ARCHITEKT_API_KEY`)

Mutating API routes require a bearer token when a platform API key is configured.

1. Copy the example env file if needed: `cp .env.example .env`
2. Set the preferred key (ADR-001 niveau 2):

```bash
export ARCHITEKT_API_KEY="your-local-secret"
```

`MACARON_API_KEY` is still accepted during the 6-month migration window; `ARCHITEKT_API_KEY` takes precedence when both are set.

Resolution lives in `platform/auth/api_key.py` (`get_platform_api_key()`).

Example authenticated request:

```bash
curl -X POST http://localhost:8090/api/projects \
  -H "Authorization: Bearer $ARCHITEKT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"local-test","description":"dev"}'
```

If no key is set, auth is disabled (convenient for local UI work; do not use in production).

## Run tests (CI gate)

Core unit tests match the GitHub Actions gate:

```bash
PLATFORM_LLM_PROVIDER=demo PLATFORM_ENV=test PYTHONPATH=. pytest \
  tests/test_demo.py \
  tests/test_events.py \
  tests/test_deterministic_tools.py \
  tests/test_adaptive_intelligence.py \
  tests/test_plugins.py \
  tests/test_llm_cache.py \
  tests/test_platform_api.py \
  tests/test_uruk_rtk.py \
  tests/test_workers.py \
  tests/test_b_features.py \
  tests/test_api_key_alias.py \
  -v
```

API key alias coverage only:

```bash
PLATFORM_LLM_PROVIDER=demo PLATFORM_ENV=test PYTHONPATH=. pytest tests/test_api_key_alias.py -v
```


## E2E smoke (Playwright)

# Local Development

## Platform server

```bash
# From repo root (parent of platform/ package)
pip install -r platform/requirements.txt
PLATFORM_LLM_PROVIDER=demo python3 -m uvicorn platform.server:app \
  --host 0.0.0.0 --port 8099 --ws none --log-level warning
```

Open http://localhost:8099 — use **Skip Demo** on `/login` if auth is enabled.

## E2E smoke tests (Playwright)

Minimal smoke (2 tests: login + `/api/health`):

```bash
cd platform/tests/e2e
npm ci
npx playwright install chromium
BASE_URL=http://localhost:8099 PLATFORM_LLM_PROVIDER=demo \
  npx playwright test smoke.spec.ts
```

Full E2E suite (82+ tests, longer runtime):

```bash
cd platform/tests/e2e
npm test
```

CI runs only `smoke.spec.ts` via `.github/workflows/e2e-smoke.yml` on push to `main`.

## Unit tests

```bash
pytest tests/test_platform_api.py -v
```
