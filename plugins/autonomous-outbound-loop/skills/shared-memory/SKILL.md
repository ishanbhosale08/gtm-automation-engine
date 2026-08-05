---
name: shared-memory
description: Persistent state and memory for accounts touched, statuses, next actions, and loop audit trail.
---

# Shared Memory Skill

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

## When to Use

- Bootstrapping a new loop workspace with `configure-loop`.
- Any agent handoff that must survive across ticks or sessions.
- Weekly synthesis of learnings into long-term memory.

## State files (canonical)

| File | Purpose |
|------|---------|
| `workspace/autonomous-loop/loop-state.json` | Machine-readable state: ticks, caps, pause, locks, account index |
| `workspace/autonomous-loop/WORKING.md` | Human-readable pipeline queues (scout → closer) |
| `workspace/autonomous-loop/PROGRESS.md` | Metrics, agent health, daily/weekly rollups |
| `workspace/autonomous-loop/MEMORY.md` | Long-term ICP refinements, approved copy patterns, lessons |
| `workspace/autonomous-loop/memory/YYYY-MM-DD.md` | Daily operational log |

Templates live beside active files as `*.template.*` copies from plugin assets.

## Account record schema (`loop-state.json` → `accounts[]`)

```json
{
  "account_id": "SF-001234",
  "company": "Example Corp",
  "roe_verdict": "WORKABLE",
  "roe_rule": "passed all layers",
  "stage": "writer",
  "contacts": [],
  "last_tick_role": "outbound-scout",
  "last_tick_at": "2026-06-03T14:15:00Z",
  "next_action": "draft email for Operations Manager persona",
  "handoffs": []
}
```

## Memory maintenance

- **Daily**: append tick outcomes to `memory/YYYY-MM-DD.md`.
- **Weekly (Sunday)**: promote durable patterns to `MEMORY.md`; archive daily files older than 30 days.
- **On SKIP**: log rule id and source system (Salesforce, Outreach, Glean) for audit.
- **On FLAG**: never auto-advance stage until operator sets `roe_verdict` to WORKABLE.

## Concurrency

- Mission Control holds the lock for `PROGRESS.md` updates.
- Stage agents update only their queue section in `WORKING.md` plus their rows in `loop-state.json`.
- Use `loop-state.json` → `stage_lock` to prevent double-writes during continuous mode.

## Integration pointers

- Import Salesforce orphan lists from `workspace/leads/`.
- Mirror suppression flags with `intent-signal-orchestration` `suppression-logic` skill taxonomy.
- Glean findings attach as `internal_notes[]` on account records (no outreach claims without source).

---

