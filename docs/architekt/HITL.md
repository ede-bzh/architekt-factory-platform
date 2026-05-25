# Human-in-the-Loop (HITL) API

Mission checkpoint gates and GA proposal review endpoints. Source: `platform/web/routes/missions/hitl.py` and `platform/web/routes/evolution.py`.

## Mission checkpoint validation

Used when a phase gate is `checkpoint` or pattern is `human-in-the-loop`. The orchestrator pauses until a human submits GO/NOGO/PIVOT.

| Method | Path | Body | Response |
|--------|------|------|----------|
| POST | `/api/missions/{mission_id}/validate` | `{ "decision": "GO" \| "NOGO" \| "PIVOT" }` | `{ "decision", "phase" }` |

- **Auth**: Bearer token required for mutations (`MACARON_API_KEY`).
- **404**: Unknown `mission_id`.
- **Side effects**: Updates current phase status (`done` on GO, `failed` otherwise), posts `DECISION: …` to mission session + A2A bus.

### Example

```bash
curl -X POST "$BASE/api/missions/run-abc123/validate" \
  -H "Authorization: Bearer $MACARON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"decision":"GO"}'
```

## GA evolution proposals (HITL approve/reject)

Workflow template proposals from the genetic algorithm require human approval before applying.

| Method | Path | Body | Response |
|--------|------|------|----------|
| POST | `/api/evolution/proposals/{proposal_id}/approve` | — | `{ "ok", "proposal_id", "status": "approved" }` |
| POST | `/api/evolution/proposals/{proposal_id}/reject` | — | `{ "ok", "proposal_id", "status": "rejected" }` |

UI: `/workflows` → **Évolution** tab, or `/proof` (redirects to `/workflows#evolution`).

## Related GET endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/evolution/proposals` | List pending/approved/rejected proposals |
| GET | `/api/evolution/runs` | GA run history |
| GET | `/api/warmup/status` | Adaptive intelligence warmup state |

## E2E gating

Playwright specs skip when `PLAYWRIGHT_E2E=0` or `BASE_URL=""`. Data-dependent skips use `test.skip(condition, reason)` — see `platform/tests/e2e/helpers.ts`.
