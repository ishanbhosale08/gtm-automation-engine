---
name: monitor-loop
description: Reports heartbeat status, queue depth, RoE compliance samples, and loop pause state without executing outreach.
usage: /autonomous-outbound-loop:monitor-loop --workspace workspace/autonomous-loop --verbose
---

# Command: monitor-loop

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

## Inputs

- **workspace** – loop root. Default: `workspace/autonomous-loop`.
- **verbose** – include per-role last tick, handoff log, and compliance sample details.
- **since** – optional ISO timestamp to filter activity (default: last 24 hours).

## Workflow

1. **State read** – load `loop-state.json`, `WORKING.md`, `PROGRESS.md` without mutating queues.
2. **Heartbeat check** – compare `last_tick` per role to `heartbeat-cadence` expected intervals; mark stale if > 2× interval.
3. **Queue metrics** – count rows per stage; highlight bottlenecks (Writer > Rep > Scout imbalance).
4. **Compliance sample** – list last 10 `SKIP`/`FLAG` decisions with rule IDs from RoE gate.
5. **Operator status** – report `paused`, `halt_reason`, daily cap consumption, and next scheduled standup.

## Outputs

- Heartbeat dashboard (healthy / warning / halted).
- Stale handoff and blocked item list from `WORKING.md`.
- Optional Slack-ready summary when `verbose: true` (text only; operator posts manually).

## Agent and skill invocations

- `loop-mission-control`
- `heartbeat-cadence`, `shared-memory`

---

