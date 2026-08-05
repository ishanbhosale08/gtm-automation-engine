---
name: run-loop
description: Starts or resumes the autonomous outbound loop for one tick or continuous mode with RoE gates enforced.
usage: /autonomous-outbound-loop:run-loop --mode tick|continuous --stage all|scout|writer|rep|closer --workspace workspace/autonomous-loop
---

# Command: run-loop

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

## Inputs

- **mode** – `tick` (single pass) or `continuous` (repeat until stop condition). Default: `tick`.
- **stage** – `all`, `scout`, `writer`, `rep`, `closer`, or `mission-control`. Default: `all`.
- **workspace** – path to loop state root. Default: `workspace/autonomous-loop`.
- **config** – optional path to `loop-config.json` (copy from `assets/loop-config.template.json`).
- **force** – `true` bypasses pause flag only; never bypasses RoE (always false for compliance).

### GTM Automation Engine Pattern and Plan Checklist

> Mirrors GTM Automation Engine orchestrator blueprint `plugins/orchestrator/README.md`.

- **Pattern selection**: Loop execution runs **pipeline** (RoE gate → scout → writer → rep → closer → telemetry). Parallel scout enrichment may use a **fan-out** segment with merge before Writer.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, stage, dependency graph, RoE checkpoint IDs, and success metrics (workable rate, meetings booked, suppression integrity).
- **Tool hooks**: Glean MCP (account history, ROE), Salesforce exports in `workspace/leads/`, ZoomInfo criteria in `workspace/leads/zoominfo-exampleco-icp-criteria.md`.
- **Guardrails**: Loop halts on any `SKIP` triggered by hard RoE rule; `FLAG FOR REVIEW` queues for human before Writer. Retry limit = 2 per stage error.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices` before continuous mode.

## Workflow

1. **Config load** – read `loop-config.json` and `loop-state.json`; abort if `paused: true` unless operator confirms.
2. **RoE gate (global)** – run workable-contact filter on inbound queue; drop or flag rows before stage work (`assets/ROE-GATE.md`).
3. **Stage dispatch** – invoke agents in order for `all`, or single stage; each agent updates `WORKING.md` and `loop-state.json`.
4. **Heartbeat** – Mission Control records tick in `PROGRESS.md`; emit `HEARTBEAT_OK` if queues healthy.
5. **Stop conditions** – exit continuous mode on daily cap, error budget, operator pause, or compliance halt.

## Outputs

- Updated `WORKING.md`, `loop-state.json`, and daily memory file.
- Tick summary (accounts processed, workable/skipped/flagged, handoffs).
- Plan JSON entry in `.claude/plans` when running orchestrated sessions.

## Agent and skill invocations

- `outbound-scout`, `outbound-writer`, `outbound-rep`, `outbound-closer`, `loop-mission-control`
- `heartbeat-cadence`, `shared-memory`, `loop-orchestration`
- `sales-assistant` contact filter (mandatory)

## GTM Automation Engine safeguards

- **Fallback agents**: Mission Control may run Writer QA or Rep logging if stage agent unavailable; no send without human approval in fallback mode.
- **Escalation triggers**: two consecutive RoE failures on same account, or suppression conflict, halts loop and pages operator.
- **Plan maintenance**: update plan JSON when stage mix or workspace path changes.

---

