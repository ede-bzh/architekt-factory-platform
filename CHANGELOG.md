# Changelog

All notable changes to Architekt Factory Platform are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [2.3.0] - 2026-05-25

### Added

- `platform/VERSION` as semver source of truth (`PLATFORM_VERSION` env override).
- `docs/architekt/RELEASE.md` release checklist and CI SBOM artifact notes.
- L2 architecture guard in `run_guard` (secrets in `code_write`, unsafe patterns).
- RL `recommend()` hook at pattern phase start when confidence ≥ 0.7.
- HITL deploy validation API (`/api/missions/{id}/hitl/*`).
- `MAX_ARCHITEKT_SKILLS` role-based skill injection caps (4–14).
- LLM trace prune job (`platform/ops/prune_llm_traces.py`).

### Changed

- CI: `bandit` and `pip-audit` are blocking (no `continue-on-error`).
- Deploy workflows require green `CI` job on `main`.
- `/api/health` exposes `version` and UTC `timestamp`.
- Unified API rate limiting via `RateLimitMiddleware` (mutations only).
- Monitoring live cache TTL 20s (aligned with UI polling).
- L1 adversarial guard fail-closed on LLM errors.

### Fixed

- Post-rebrand documentation sync (EN/FR, counters, Wave 5 backlog).

## [2.2.0] - 2026-05-24

### Added

- Architekt rebrand (UI, i18n EN/FR, branding tests in CI).
- `/api/health` enrichment and CSP hardening (no `unsafe-eval` outside workspace).
- `RateLimitMiddleware` export from `platform.security`.

[Merged via PR #10 — rebrand cleanup]
