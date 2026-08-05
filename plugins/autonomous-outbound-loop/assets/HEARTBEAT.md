# HEARTBEAT.md - Autonomous Outbound Loop Checklist

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

Copy or reference this file from `plugins/autonomous-outbound-loop/assets/HEARTBEAT.md` when configuring a workspace.

---

## On Every Wake

1. Read `workspace/autonomous-loop/WORKING.md` for pipeline state.
2. Read role strategy file `assets/STRATEGY-<ROLE>.md` when operating that role.
3. Check `workspace/autonomous-loop/memory/YYYY-MM-DD.md` for today's context.
4. Confirm `loop-state.json` → `paused` is false (Mission Control may override only with operator ack).
5. Execute role checklist below; update shared files.
6. If nothing to do, reply `HEARTBEAT_OK`.

---

## RoE Gate (before Scout promotes any row)

- [ ] Glean search completed for company name
- [ ] Salesforce + Outreach checks per contact filter skill
- [ ] Verdict recorded: WORKABLE / SKIP / FLAG FOR REVIEW with rule id
- [ ] Suppression-logic skill cross-check for in-flight plays

---

## Mission Control (:00, :30)

**Fleet health**

- [ ] Check `loop-state.json` last_tick per role
- [ ] Identify stalled handoffs (> 2x cadence interval)
- [ ] Update `PROGRESS.md` metrics

**Pipeline review**

- [ ] Review queue caps; throttle Scout if Writer backlog
- [ ] Flag deals needing human attention
- [ ] Confirm handoffs flowing scout → writer → rep → closer

**Compliance (daily)**

- [ ] Sample 10% of WORKABLE rows for RoE revalidation
- [ ] Log suppression spikes to operator summary

---

## Scout (:00, :15, :30, :45)

- [ ] Process inbound list with RoE gate
- [ ] Enrich missing firmographics via data-enrichment plugins
- [ ] Capture Why Now signals for workable accounts
- [ ] Move dossiers to Writer queue in WORKING.md

---

## Writer (:02, :17, :32, :47)

- [ ] Draft from Scout queue only (WORKABLE rows)
- [ ] Apply 5-part formula and QA gates
- [ ] Mark copy complete for Rep queue

---

## Rep (:04, :19, :34, :49)

- [ ] Revalidate RoE if row age > 24h
- [ ] Log sends to Salesforce and Outreach
- [ ] Triage replies; route qualified to Closer
- [ ] Never send to SKIP or unresolved FLAG rows

---

## Closer (:06, :21, :36, :51)

- [ ] MEDDIC qualification on engaged threads
- [ ] Meeting prep and calendar proposal (human approves send)
- [ ] AE handoff packet when qualified
- [ ] Flag stalled 7+ day threads back to Rep

---

## Daily Standup (configurable, default 23:30)

Mission Control compiles:

- Completed today
- In progress by stage
- Blocked items
- RoE skip/flag counts
- Items needing ishan bhosale

---

## Memory Maintenance (weekly, Sunday)

- [ ] Review daily memory files
- [ ] Update MEMORY.md with ICP and copy learnings
- [ ] Archive daily files older than 30 days

---

