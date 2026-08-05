# Autonomous Outbound Loop Workspace

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

Persistent state for the `autonomous-outbound-loop` plugin. Initialize with:

```
/autonomous-outbound-loop:configure-loop --workspace workspace/autonomous-loop
```

## Files

| File | Purpose |
|------|---------|
| `loop-config.json` | Cadence, caps, RoE paths (from plugin template) |
| `loop-state.json` | Machine-readable ticks, accounts, pause flags |
| `WORKING.md` | Pipeline queues (scout → closer) |
| `PROGRESS.md` | Health and metrics |
| `MEMORY.md` | Long-term learnings |
| `memory/YYYY-MM-DD.md` | Daily operational log |

Templates: `*.template.json` and copies from `plugins/autonomous-outbound-loop/assets/`.

## Compliance

RoE gate is always on. See `plugins/autonomous-outbound-loop/assets/ROE-GATE.md` and `.cursor/rules/sales-outbound-agent.mdc`.

## Commands

- `run-loop` - execute tick or continuous mode
- `monitor-loop` - heartbeat status without sends
- `configure-loop` - bootstrap or update config

---

