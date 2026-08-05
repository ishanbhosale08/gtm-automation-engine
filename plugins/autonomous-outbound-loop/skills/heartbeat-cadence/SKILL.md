---
name: heartbeat-cadence
description: Defines continuous run cadence, per-role tick offsets, stop conditions, and Mission Control heartbeat checks.
---

# Heartbeat Cadence Skill

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

## When to Use

- Starting continuous loop mode with `run-loop --mode continuous`.
- Tuning how often Scout, Writer, Rep, Closer, and Mission Control wake without overlapping writes.
- Diagnosing stale agents via `monitor-loop`.

## Cadence model

The loop uses a **15-minute base grid** (configurable in `loop-config.json`). Each role wakes on offset minutes to reduce file contention on `WORKING.md` and `loop-state.json`.

| Role | Default offsets (minute within hour) | Model tier | Primary action |
|------|--------------------------------------|------------|----------------|
| Mission Control | :00, :30 | haiku | Fleet health, compliance sample, PROGRESS update |
| Scout | :00, :15, :30, :45 | haiku | Research queue, RoE gate, scout handoffs |
| Writer | :02, :17, :32, :47 | sonnet | Draft copy from scout briefings |
| Rep | :04, :19, :34, :49 | sonnet | Send/log touches, reply triage |
| Closer | :06, :21, :36, :51 | sonnet | Qualify, meeting prep, AE handoff |

## On every wake

1. Read `workspace/autonomous-loop/WORKING.md` for queue state.
2. Read role strategy file under `plugins/autonomous-outbound-loop/assets/STRATEGY-<ROLE>.md` when present.
3. Read `workspace/autonomous-loop/memory/YYYY-MM-DD.md` for today's context.
4. Execute role checklist in `assets/HEARTBEAT.md`.
5. Update shared files; if no work, respond `HEARTBEAT_OK`.

## Stop conditions

- `loop-state.json` → `paused: true`
- Daily workable cap reached (`daily_cap.workable_contacts`)
- `halt_reason` set by RoE gate or suppression conflict
- Error budget exceeded (`error_budget.consecutive_failures`)
- Operator command: `run-loop` with explicit stop or session end

## Continuous run pattern

```
configure-loop  →  run-loop --mode continuous
       ↑                    |
       |              heartbeat ticks
       |                    v
 monitor-loop  ←  Mission Control standup (daily)
```

## Tips

- Keep heartbeat model on haiku; reserve sonnet for Writer, Rep, Closer creative work.
- Do not shorten Scout offset below 15 minutes when processing large ZoomInfo batches.
- Pair with `shared-memory` for atomic updates (last writer wins is not acceptable; use stage locks in `loop-state.json`).

---

