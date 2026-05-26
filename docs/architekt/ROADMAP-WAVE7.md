# Roadmap Wave 7 — Scale & security (P2)

**Branch context:** `cursor/roadmap-parallel-wave2-7576` (parallel wave 2 doc + security polish).

**Tier:** P2 (Phase 4–6). **Gate:** 3 paying clients delivered (see `docs/architekt/PLATFORM-BACKLOG.md` § P2).

**Wave en cours (doc):** Wave 6 foundations — CI, releases, version API. Wave 7 picks P2 items previously listed under P3 or deferred from Wave 5.

---

## P2 deliverables (Wave 7)

| # | Item | Scope | Notes |
|---|------|-------|-------|
| 1 | **Multi-tenant** | DB row-level `tenant_id`, auth scope, per-tenant secrets | Was P3; gate = 10+ clients — track design in Wave 7, implement post-gate |
| 2 | **Stripe billing** | Subscriptions, usage metering (LLM tokens), webhook idempotency | SaaS Phase 7 optional; API keys + customer portal |
| 3 | **External pentest** | Third-party assessment + remediation sprint | L3 regulated workflows; report → backlog |
| 4 | **Docker `architekt_platform` rename** | Image, compose service, `/app/architekt_platform/` path | Align with ADR rebrand; alias `architekt_platform` 6 months |
| 5 | **Mutation testing 50 %** | mutmut on `platform/agents/`, `platform/security/`, `platform/llm/` | CI job optional; **full mutation 50 %** threshold on critical modules |

---

## Security polish (Wave 7 — this PR)

- [x] CSP documentation — `docs/architekt/CSP.md`
- [x] `PLATFORM_CSP_NONCE` env + optional per-request nonce in `security_headers` (HTMX-safe: keeps `unsafe-inline`)
- [ ] CSP phase 1: nonce on `base.html` scripts (follow-up PR)
- [ ] Remove `unsafe-inline` / `unsafe-eval` (multi-PR; see CSP.md roadmap)

---

## Dependencies

```
Wave 5 (P1) ──► Wave 6 (CI/releases) ──► Wave 7 (P2 + CSP doc)
                      │
                      ├── L2 LLM adversarial (in progress, other agents)
                      └── dashboard/ rebrand (in progress, other agents)
```

---

## Out of Wave 7 (unchanged)

- Site vitrine Astro (separate repo)
- E2E Playwright full 82 specs
- Backstage / Port IDP
- L3 regulated verticals (HIPAA, banking)

---

## Links

- Backlog master: `docs/architekt/PLATFORM-BACKLOG.md`
- CSP detail: `docs/architekt/CSP.md`
- Release process: `docs/architekt/RELEASE.md`
