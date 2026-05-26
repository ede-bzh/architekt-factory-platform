# 🧬 Darwin Teams — Evolutionary Agent Selection

Software Factory uses **evolutionary selection** to find the best agent teams and LLM models for each context — automatically, without configuration.

## Two Levels of Evolution

| Level | What competes? | Selection unit |
|-------|---------------|----------------|
| **Team Darwin** | Agent + Pattern combinations | `(agent_id, pattern_id, technology, phase_type)` |
| **LLM Darwin** | LLM models within the same team | `(agent_id, pattern_id, technology, phase_type, llm_model)` |

Both use **Thompson Sampling** with Beta distributions for probabilistic exploration vs. exploitation.

---

## Team Darwin (v2.1.0+)

### How it works

1. Patterns declare `agent_id: "skill:developer"` to opt-in to Darwin selection
2. For each mission, `TeamSelector.select_team()` samples from the Beta distribution:
   ```
   score ~ Beta(wins + 1, losses + 1)
   ```
3. The team with the highest sampled score is selected
4. After mission completion, wins/losses update the fitness table

### Fitness scores

- **Champion** (≥ 70, runs ≥ 10): elite team, preferred
- **Rising** (score trending up): gaining experience
- **Declining** (score trending down): losing effectiveness
- **Warmup** (runs < 5): random exploration phase
- **Retired** (soft): weight = 0.1, deprioritized but recoverable

### Cold start (similarity fallback)

If no data exists for the exact context:
```
angular_19 → angular_* → generic
```

### A/B Shadow Testing

Automatic parallel shadow runs when:
- Two teams have close fitness scores (delta < 10), OR
- Randomly at 10% of missions

A neutral evaluator picks the winner; losing team's fitness decreases.

### Dashboard

Visit `/teams` → **Leaderboard** tab:
- Fitness scores per team per context
- Champion/Rising/Declining/Retired badges
- Evolution chart (Chart.js)
- Selection history
- A/B test results

---

## LLM Darwin (v2.2.0+)

### How it works

Same team, but now the **LLM model** is also evolved:

1. Executor calls `LLMTeamSelector.select_model()` with agent + context
2. Candidate models come from the **routing config** (heavy + light for the agent's category)
3. Thompson Sampling picks the model: `Beta(wins+1, losses+1)` per model
4. After mission completion, `update_fitness()` records the outcome

### Priority chain in executor

```
1. Darwin LLM Thompson Sampling  (if AZURE_DEPLOY set + Azure AI key present)
2. DB routing config              (from Settings → LLM, stored in session_state)
3. Hardcoded defaults:
   - reasoning → gpt-5.2
   - code/tests → gpt-5.1-codex
   - default → gpt-5-mini
4. Local dev fallback             (agent.provider/model unchanged)
```

### Database tables

```sql
-- Per-model fitness per team × context
CREATE TABLE team_llm_fitness (
    agent_id TEXT,
    pattern_id TEXT,
    technology TEXT,
    phase_type TEXT,
    llm_model TEXT,
    llm_provider TEXT,
    runs INTEGER DEFAULT 0,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    fitness_score REAL DEFAULT 50.0,
    last_updated TEXT,
    UNIQUE(agent_id, pattern_id, technology, phase_type, llm_model)
);

-- A/B test records
CREATE TABLE team_llm_ab_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id TEXT,
    pattern_id TEXT,
    technology TEXT,
    phase_type TEXT,
    llm_a TEXT,
    llm_b TEXT,
    winner_llm TEXT,
    llm_a_score REAL,
    llm_b_score REAL,
    created_at TEXT
);
```

### APIs

```bash
# LLM model fitness leaderboard
GET /api/teams/llm-leaderboard?technology=generic&phase_type=generic

# A/B test history
GET /api/teams/llm-ab-tests?limit=20

# Routing config (read + write)
GET /api/llm/routing
POST /api/llm/routing   # flushes 60s executor cache
```

### Dashboard

Visit `/teams` → **LLM A/B** tab:
- Model fitness leaderboard (rank, agent, pattern, model, score, runs, wins)
- A/B test history with model A vs B and winner

---

## Configuration

### Opt-in to Team Darwin

In your pattern YAML:
```yaml
agents:
  - skill: developer     # Darwin picks the best developer
  - id: qa_engineer      # Explicit — Darwin NOT applied
```

### Configure LLM Routing

Visit **Settings → LLM** or via API:
```json
{
  "reasoning_heavy": {"provider": "azure-ai", "model": "gpt-5.2"},
  "production_heavy": {"provider": "azure-ai", "model": "gpt-5.1-codex"},
  "production_light": {"provider": "azure-openai", "model": "gpt-5-mini"},
  "tasks_light": {"provider": "azure-openai", "model": "gpt-5-mini"}
}
```

---

## Adaptive Intelligence — GA + RL (LIVE v2.3.0+)

Beyond Team/LLM Darwin (Thompson Sampling on teams and models), Architekt runs two additional **LIVE** adaptive layers documented in [`platform/CLAUDE.md`](../../platform/CLAUDE.md#adaptive-intelligence--thompson-sampling--ga--rl):

### Genetic Algorithm — workflow evolution (LIVE)

- **Engine**: `platform/agents/evolution.py` (`GAEngine`)
- **Scheduler**: `platform/agents/evolution_scheduler.py` — nightly at **02:00 UTC** (started from `platform/server.py` lifespan)
- **Cold start**: `platform/agents/simulator.py` seeds synthetic mission outcomes
- **API**: `GET /api/evolution/proposals`, `POST /api/evolution/proposals/{id}/approve|reject`, `POST /api/evolution/run/{wf_id}` (`platform/web/routes/evolution.py`)
- **UI**: `/workflows` → Evolution tab

### Reinforcement Learning — mid-mission adaptation (LIVE)

- **Policy**: `platform/agents/rl_policy.py` (Q-learning, ε-greedy)
- **Runtime hook**: `platform/agents/rl_hooks.py` → `apply_rl_pattern_override()` called from `platform/patterns/engine.py` at phase start when confidence > 0.7
- **Training**: nightly batch on `rl_experience` table (same scheduler cycle as GA)
- **Actions**: `keep | switch_parallel | switch_sequential | switch_hierarchical | add_agent | remove_agent`

---

## See Also

- [LLM Configuration](LLM-Configuration) — provider setup, environment variables
- [Patterns](Patterns) — how to opt-in to Darwin selection in patterns
- [API Reference](API-Reference) — full endpoint documentation
