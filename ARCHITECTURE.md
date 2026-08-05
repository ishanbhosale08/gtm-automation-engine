# Architecture

GTM Automation Engine is a Claude Code marketplace that combines a broad GTM plugin suite with a governed, always-on outbound agent loop. This document describes components, control/data flow, and the loop mechanics.

---

## High-level view

```text
┌─────────────────────────────────────────────────────────────────┐
│                     Claude Code (runtime)                        │
├─────────────────────────────────────────────────────────────────┤
│  Control center: marketplace.json + 67 plugins                   │
│    agents · commands · skills                                    │
├─────────────────────────────────────────────────────────────────┤
│  Governance: ROE gate + contact filter + cursor rules             │
├─────────────────────────────────────────────────────────────────┤
│  Autonomous loop: Scout → Writer → Rep → Closer                  │
│    heartbeat · shared memory · mission control                   │
├─────────────────────────────────────────────────────────────────┤
│  Workspace: workspace/autonomous-loop/ + workspace/leads/        │
└─────────────────────────────────────────────────────────────────┘
         │ optional                    │ optional
         ▼                             ▼
   Salesforce / Outreach          Glean / ZoomInfo
```

---

## Components

### 1. Plugin marketplace (control center)

**Location**: `.claude-plugin/marketplace.json`, `plugins/`

The marketplace registers 67 plugins across sales, marketing, orchestration, analytics, and industry verticals. Each plugin follows a consistent shape:

| Asset type | Purpose |
|------------|---------|
| `agents/*.md` | Role-specific system prompts (researcher, strategist, analyst) |
| `commands/*.md` | User-invoked workflows with inputs and guardrails |
| `skills/*/SKILL.md` | Reusable knowledge packages (frameworks, checklists, templates) |

Orchestration plugins (ABM, nurture, launch, analytics pipeline, etc.) compose multiple agents and skills into multi-step GTM programs. The marketplace is the **control center**: it defines what agents exist and how operators invoke them.

### 2. Governance layer

**Locations**:

- `plugins/autonomous-outbound-loop/assets/ROE-GATE.md`
- `sales-assistant/skills/01-contact-filter.md`
- `.cursor/rules/sales-outbound-agent.mdc`

Before any outbound action, contacts pass a **Rules of Engagement (workable-contact policy)** gate:

| Layer | Checks |
|-------|--------|
| CRM (Layer 1) | Open opp, active customer/partner, DNC, territory |
| Sequence (Layer 2) | Another rep's active sequence, recent AE/CSM activity |
| Recency (Layer 3) | Touches in last 12 months, negative replies |
| Data quality (Layer 4) | Valid email, persona fit, ownership disputes |

Output per contact: `WORKABLE`, `SKIP`, or `FLAG FOR REVIEW` with an explicit rule citation.

The governance layer is **fail-closed**: Writer, Rep, and Closer stages may not override a SKIP without human review.

### 3. Autonomous outbound loop (runtime agent)

**Location**: `plugins/autonomous-outbound-loop/`

| Agent | Responsibility |
|-------|----------------|
| **outbound-scout** | Discover and enrich targets; apply ROE gate; enqueue WORKABLE rows |
| **outbound-writer** | Draft trigger-based copy from scout context |
| **outbound-rep** | Prepare send-ready touches; re-validate stale rows |
| **outbound-closer** | Meeting booking and handoff prep |
| **loop-mission-control** | Cadence supervision, sampling, halt on violations |

| Command | Purpose |
|---------|---------|
| `configure-loop` | Copy config and workspace templates |
| `run-loop` | Execute tick, batch, or continuous mode |
| `monitor-loop` | Queue health and compliance sampling |

### 4. Research engine

**Locations**: `plugins/data-enrichment-master/`, `plugins/intent-signal-orchestration/`, `plugins/data-signal-enrichment/`

Provides enrichment waterfalls, signal scoring, suppression logic, and outbound play templates. Scout agents consume this layer to attach "Why Now" context before Writer runs.

### 5. Sales assistant (qualify + write)

**Location**: `sales-assistant/`

A focused skill library for SDR/AE workflows: contact filter, list builder, multi-thread map, 5-part email formula, re-engage. Complements the plugin suite with operator-grade outbound playbooks.

### 6. Workspace and demo data

| Path | Role |
|------|------|
| `workspace/autonomous-loop/` | Loop heartbeat, memory, queue state (templates in plugin assets) |
| `workspace/leads/sample_contacts.csv` | Synthetic demo contacts |
| `workspace/leads/parse_leads.py` | Stdlib script to load and summarize demo leads |

---

## Data and control flow (one loop tick)

```text
1. Heartbeat fires (schedule or manual /run-loop --mode tick)
2. Mission Control reads HEARTBEAT.md + MEMORY.md + loop-config.json
3. Scout:
   - Pull candidates (demo CSV or external enrichment)
   - Run ROE-GATE / contact-filter
   - Write WORKABLE rows to queue in shared memory
4. Writer:
   - Read WORKABLE queue only
   - Attach signal context; draft email/copy artifacts
5. Rep:
   - Re-check rows older than 24h
   - Stage send-ready payloads (human approval assumed)
6. Closer:
   - Confirm no new open opp before meeting actions
7. Mission Control:
   - Append tick summary to MEMORY.md
   - Sample audit; halt loop on ROE violation
```

Control flows **down** through agent stages; state flows **through** shared memory files under `workspace/autonomous-loop/`.

---

## Heartbeat and memory model

| File | Purpose |
|------|---------|
| `HEARTBEAT.md` | Cadence definition (tick interval, batch size, mode) |
| `MEMORY.template.md` | Seed for durable loop memory |
| `loop-config.template.json` | Operator settings (sources, limits, integrations) |
| `STRATEGY-SCOUT.md` / `STRATEGY-WRITER.md` | Stage-specific playbooks |

**Heartbeat**: A tick is an idempotent unit of work. Operators can run a single tick for safe testing or continuous mode for production-style cadence.

**Memory**: Append-only summaries per tick (queue depth, violations, learnings). Agents read memory at the start of each tick so later stages inherit scout decisions without re-querying external systems unnecessarily.

---

## Integration boundaries

| System | Used for | Not bundled |
|--------|----------|-------------|
| Salesforce | Account type, opps, activity, DNC | Credentials live in operator environment |
| Outreach | Sequences, touches | API keys external |
| Glean | Internal ROE docs, references | Enterprise MCP connector |
| ZoomInfo | List building criteria | Subscription external |

The repo ships **integration guidance** in agent prompts and skills, not live connectors.

---

## Extension points

1. **New plugins**: `scripts/scaffold_asset.py` + marketplace entry
2. **Custom ROE rules**: Edit `ROE-GATE.md` and `01-contact-filter.md` together
3. **Loop cadence**: `configure-loop` then edit `workspace/autonomous-loop/loop-config.json`
4. **Demo → production leads**: Replace `sample_contacts.csv`; point Scout at your sanitized export

---

## Security posture

- No credentials in the repository (see `SECURITY.md`)
- Demo leads are synthetic (`workspace/leads/README.md`)
- Governance gate runs before Writer/Rep stages
- Mission Control can halt the loop on compliance sample failures

---

## Related reading

- [README.md](README.md) — overview and install
- [NOTICES.md](NOTICES.md) — upstream attribution and license guidance
- `plugins/autonomous-outbound-loop/README.md` — loop operator quick start
