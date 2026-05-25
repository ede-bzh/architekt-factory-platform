# Orchestration Patterns (15)

Patterns define how agents collaborate in a phase. Each workflow phase sets a `pattern_id` consumed by `PatternEngine` (`platform/patterns/engine.py`). Fifteen patterns ship: **12** stored in the DB (editable in UI) and **3** engine-only (`solo`, `loop`, `network`).

See also: [Security](Security) (adversarial L0–L2), [Workflows](Workflows) (36 templates).

## How patterns attach to missions

Mission control runs workflow phases in order. Example — **`product-lifecycle`** (canonical end-to-end epic):

| Phase ID | Pattern | Mission stage |
|----------|---------|----------------|
| `ideation` | `network` | Discovery debate (PM, UX, architect, métier) |
| `strategic-committee` | `human-in-the-loop` | GO / NOGO / PIVOT |
| `project-setup` | `sequential` | Constitution (backlog, sprints, ceremonies) |
| `architecture` | `aggregator` | Parallel analysis → architect synthesis |
| `dev-sprint` | `hierarchical` | Lead delegates TDD workers |
| `build-verify` | `sequential` | CI compile-from-scratch |
| `cicd` | `sequential` | Pipeline + DevSecOps |
| `qa-campaign` | `loop` | QA loop until approve |
| `qa-execution` | `parallel` | E2E + API + perf in parallel |
| `deploy-prod` | `human-in-the-loop` | **HITL deploy gate** (canary → human GO) |
| `tma-router` | `router` | Incident routing |
| `tma-fix` | `loop` | Corrective maintenance loop |

Gates between phases: `always`, `no_veto`, `all_approved` — see [Security](Security#human-in-the-loop-hitl-deploy-gate).

## Database-configured patterns (12)

### `solo-chat`

**Use case:** Single specialist, conversational (project chat, toolbox).

**Mission fit:** Ad-hoc sessions, not long SAFe epics.

**Protocol:** Solo execution; light adversarial on code writes.

---

### `sequential`

**Use case:** Pipeline — each agent output feeds the next (constitution, CI/CD, documentation).

**Mission fit:** `project-setup`, `cicd`, `build-verify`, backup/restore steps.

**Example chain:** Brain → Worker → Code critic.

---

### `parallel`

**Use case:** Fan-out work (multi-suite QA, chaos scenarios, license scans).

**Mission fit:** `qa-execution`, chaos-scheduled load + security probes.

**Gate:** Often `all_approved` — all branches must finish.

---

### `hierarchical`

**Use case:** Lead decomposes stories, workers report back, lead integrates.

**Mission fit:** `dev-sprint`, `cicd-pipeline` planning, mobile epics.

**Protocol:** `_DECOMPOSE_PROTOCOL` → `_EXEC_PROTOCOL` → `_QA_PROTOCOL`.

---

### `router`

**Use case:** Triage — one agent classifies input and routes to a specialist.

**Mission fit:** `tma-router`, `dsi-platform-tma` incident classification.

**Specialist slots:** Dev TMA, SRE, test automation, security.

---

### `aggregator`

**Use case:** Parallel specialists produce drafts; one architect consolidates.

**Mission fit:** `architecture` phase (lead dev, UX, security, DevOps → architect).

**Protocol:** Discussion + synthesis (research, not blind merge).

---

### `human-in-the-loop`

**Use case:** Agents work until a **checkpoint**; human submits GO/NOGO via UI or `POST /api/missions/{id}/validate`.

**Mission fit:** Strategic committee, **production deploy**, data-migration cutover, canary promotion.

**Gate:** Usually `all_approved` — mission pauses until validation.

---

### `debate`

**Use case:** Opposing agents argue; judge (brain) decides.

**Mission fit:** `debate-decide`, architecture option selection.

**Config:** `max_rounds` (default 5).

---

### `sf-tdd`

**Use case:** Full factory pipeline: plan → TDD implement → multi-critic → DevOps.

**Mission fit:** Feature-sprint workflows, hardened delivery paths.

**Chain:** Brain → TDD worker → code critic → security critic → arch critic → DevOps.

---

### `wave`

**Use case:** Dependency-ordered **waves** — parallel inside a wave, sequential across waves.

**Mission fit:** Large backlogs with explicit task DAG (infra waves, migration steps).

---

## Adversarial patterns

These embed **Team of Rivals** review (see [Security](Security#adversarial-validation-l0--l1--l2)).

### `adversarial-pair`

**Use case:** Writer and reviewer iterate until consensus or max iterations.

**Mission fit:** Documentation review, backup-restore validation, design-system sign-off.

**Mechanism:** Edge `conditional: veto` loops writer → critic (up to 5×).

**Layers:** Primarily L0 + L1; escalates to L2 on architecture flags.

---

### `adversarial-cascade`

**Use case:** Swiss-cheese defense — **L0 → L1 code → L1 security → L2 architecture** in sequence.

**Mission fit:** High-risk changes (security-hacking remediation, compliance deliverables).

**Agents (default):** worker → code-critic → security-critic → arch-critic.

**Rule:** No phase exit on absolute veto; incidents logged to `platform_incidents` for DORA.

---

## Engine-only patterns (3)

| Pattern | Use case | Mission fit |
|---------|----------|-------------|
| `solo` | Single agent, no bus traffic | Quick one-shot tools |
| `loop` | Repeat until approve or max iterations | QA campaign, UX review, TMA fix |
| `network` | Free-form multi-agent discussion | **Ideation**, DSI feature discovery |

`network` skips L1 adversarial on discussion outputs to avoid blocking brainstorming; L0 still blocks obvious slop/mock code.

## Pattern × protocol matrix

| Protocol | Patterns |
|----------|----------|
| **RESEARCH** (read/search only) | `network`, `human-in-the-loop`, `debate`, `aggregator` |
| **EXEC / QA / DECOMPOSE** | `hierarchical`, `sequential`, `parallel`, `loop`, `wave`, `sf-tdd` |
| **Adversarial** | `adversarial-pair`, `adversarial-cascade` (+ guards on all execution patterns) |

## Choosing a pattern

| Goal | Prefer |
|------|--------|
| Brainstorm requirements | `network` or `debate` |
| Need human sign-off | `human-in-the-loop` |
| Ship code with review | `hierarchical` + adversarial guard |
| Highest assurance | `adversarial-cascade` or `sf-tdd` |
| Route support tickets | `router` + `loop` |

Custom patterns can be created in the UI (non-builtin rows in `patterns` table); builtins are re-seeded on upgrade via `seed_builtins()`.

## Related docs

- [Workflows](Workflows) — which `pattern_id` each template uses
- [API Reference](API-Reference) — `validate` endpoint for HITL
- [Architecture](Architecture) — PatternEngine and MessageBus

## 🇫🇷 [Patterns (FR)](Patterns‐FR)
