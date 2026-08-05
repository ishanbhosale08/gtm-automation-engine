---
name: loop-orchestration
description: Scout to writer to rep to closer handoffs, escalation paths, and Mission Control supervision for the outbound loop.
---

# Loop Orchestration Skill

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

## When to Use

- Designing or auditing the full autonomous outbound pipeline.
- Resolving stalled handoffs between roles.
- Extending the loop with additional human approval gates.

## Pipeline (default)

```
[Inbound list] → RoE Gate → Scout → Writer → Rep → Closer → AE Handoff
                      ↓           ↓        ↓       ↓
                   SKIP/FLAG   research   copy   send/qualify
```

### Stage contracts

| From | To | Entry criteria | Exit artifact |
|------|-----|----------------|---------------|
| RoE Gate | Scout | CSV/SF row submitted | WORKABLE verdict logged |
| Scout | Writer | Dossier + signals complete | Row in Writer queue |
| Writer | Rep | QA pass on copy | Approved email/LinkedIn blocks |
| Rep | Closer | Positive reply or meeting intent | MEDDIC snapshot |
| Closer | AE | Qualified opportunity | Handoff packet + SF task |

## Escalation ladder

1. **Stage owner** – agent retries once (error budget).
2. **Mission Control** – reassigns queue item, throttles intake, or pauses loop.
3. **Operator (ishan bhosale)** – resolves `FLAG FOR REVIEW`, RoE disputes, or send approval.
4. **RevOps** – only for systemic suppression or CRM mapping failures.

## RoE gate (non-optional)

Before Scout promotes a contact:

1. Glean search for company (internal history).
2. Run `sales-assistant/skills/01-contact-filter.md` layers 1–4.
3. Cross-check `intent-signal-orchestration` `suppression-logic` triggers.
4. Emit `WORKABLE`, `SKIP`, or `FLAG FOR REVIEW` with named rule.

No stage may override a `SKIP`. Writer and Rep must re-check if row age > 24h.

## Reuse existing GTM Automation Engine plugins

| Need | Use |
|------|-----|
| Prospecting lists | `sales-prospecting`, `data-enrichment-master` |
| Personalization | `copywriting/cold-email-personalization`, ExampleCo email-gen |
| Sequences | `email-sequence-orchestration` |
| Intent | `intent-signal-orchestration` |
| Handoff to AE | `sales-handoff-orchestration` |
| Internal search | Glean MCP |

## Mission Control supervision

- Runs on heartbeat grid; owns `PROGRESS.md` and compliance sampling.
- Daily standup compiles blocked items and human tasks.
- Can demote rows backward (e.g. Rep → Writer) when copy fails reply quality thresholds.

---

