---
name: configure-loop
description: Initializes or updates autonomous loop cadence, workspace paths, caps, and Salesforce/Glean integration settings.
usage: /autonomous-outbound-loop:configure-loop --workspace workspace/autonomous-loop --heartbeat 15m --daily-cap 40
---

# Command: configure-loop

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

## Inputs

- **workspace** – loop root directory. Default: `workspace/autonomous-loop`.
- **heartbeat** – Mission Control interval (e.g. `15m`, `30m`). Role offsets defined in `heartbeat-cadence` skill.
- **daily-cap** – max net-new workable contacts entering Scout per day.
- **queue-caps** – max rows per stage (scout, writer, rep, closer) before throttle.
- **timezone** – operator timezone for standup and send windows (default from config template).
- **integrations** – `salesforce`, `outreach`, `glean`, `zoominfo` toggles (documentation only; keys via env).

## Workflow

1. **Template copy** – if missing, copy `plugins/autonomous-outbound-loop/assets/loop-config.template.json` to `workspace/autonomous-loop/loop-config.json`.
2. **State bootstrap** – copy `loop-state.template.json`, `WORKING.template.md`, `MEMORY.template.md`, `PROGRESS.template.md` to active filenames without `.template`.
3. **Cadence validation** – ensure role offsets do not collide; Mission Control runs on `:00` and `:30` by default.
4. **RoE wiring** – confirm `roe_gate.enforced: true` and paths to `sales-assistant/skills/01-contact-filter.md` and `.cursor/rules/sales-outbound-agent.mdc`.
5. **Dry-run tick** – optional `run-loop --mode tick --stage mission-control` to verify file permissions and JSON schema.

## Outputs

- `loop-config.json` and initialized workspace tree under `workspace/autonomous-loop/`.
- Configuration summary for operator review (cadence table, caps, integration flags).
- Changelog entry appended to `loop-state.json` `config_history`.

## Agent and skill invocations

- `loop-mission-control` for validation
- `heartbeat-cadence`, `shared-memory` skills

---

