# gtm-automation-engine

> Agentic GTM automation platform: an autonomous outbound loop (scout → writer → rep → closer) with a governance/compliance gate, heartbeat + shared memory, and a plugin suite.

**What it does.** Runs the full outbound motion end-to-end so one operator covers what used to take a BDR team: finds accounts, qualifies contacts against Rules of Engagement, researches a live "Why Now" trigger, writes personalized outreach, multi-threads the account, and re-engages dormant pipeline — compliant by default.

**Architecture (4 cooperating repos).**
| Repo | Role |
|------|------|
| `gtm-automation-engine` | Sales brain + control center: qualification, list-building, the cold-email formula, multi-threading, re-engagement |
| [`Argus`](https://github.com/tejaskembalkar-ship-it/Argus) | Reliability + governance: compliance checks, security scanning, verification loops |
| [`Daedalus`](https://github.com/tejaskembalkar-ship-it/Daedalus) | Self-improving runtime: durable memory, skill creation, scheduled automations |
| [`Valkyrie`](https://github.com/tejaskembalkar-ship-it/Valkyrie) | Signal research: self-healing scrapers + MCP server for live buying signals |

**Stack.** Python · model-agnostic (Claude Sonnet/Haiku, OpenAI Codex) · MCP servers · runs in Claude Code / Cursor · Salesforce + ZoomInfo integrations · Git/GitHub with Husky pre-commit validation.

**Status.** Active development. Built and maintained by ishan bhosale.

Built with AI-assisted development; third-party components are credited in [NOTICES.md](NOTICES.md).

---

## What it does

GTM Automation Engine automates repetitive GTM work so teams can focus on strategy, relationships, and revenue:

- **Prospecting**: Lead qualification, list building, multi-threading, cold-email drafting
- **Orchestration**: Multi-step workflows across nurture, ABM, launches, analytics, and handoffs
- **Governance**: Rules-of-Engagement (workable-contact policy) gates before any outbound touch
- **Autonomous loop**: Scout → Writer → Rep → Closer cycle with heartbeat cadence and shared memory

---

## System design

| Layer | Role | Components in this repo |
|-------|------|-------------------------|
| **Control center** | Plugin marketplace + workflow orchestrators | `.claude-plugin/marketplace.json`, `plugins/*` (67 plugins, 200+ agents, 240+ skills) |
| **Governance layer** | Compliance gate before outreach | `plugins/autonomous-outbound-loop/assets/ROE-GATE.md`, `sales-assistant/skills/01-contact-filter.md`, `.cursor/rules/sales-outbound-agent.mdc` |
| **Runtime agent** | Always-on outbound loop | `plugins/autonomous-outbound-loop/` (scout, writer, rep, closer, mission control; heartbeat + memory) |
| **Research engine** | Enrichment and signal research | `plugins/data-enrichment-master/`, `plugins/intent-signal-orchestration/`, `plugins/data-signal-enrichment/` |
| **Sales brain** | Qualify-and-write playbook | `sales-assistant/` (contact filter, list builder, email formula, re-engage) |
| **Demo data** | Synthetic leads for workflow demos | `workspace/leads/sample_contacts.csv`, `parse_leads.py` |

See [ARCHITECTURE.md](ARCHITECTURE.md) for data flow, loop mechanics, and memory model.

---

## Stack

| Layer | Technology |
|-------|------------|
| Agent runtime | [Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| Plugin format | Claude marketplace (`.claude-plugin/marketplace.json`) |
| Orchestration | Markdown agents, commands, and Agent Skills (`SKILL.md`) |
| Demo scripts | Python 3 (stdlib only) |
| Optional CRM/SEP | Salesforce, Outreach, Glean, ZoomInfo |

---

## Quick start

### 1. Install the marketplace

In Claude Code:

```text
/plugin marketplace add tejaskembalkar-ship-it/gtm-automation-engine
```

Browse plugins:

```text
/plugin
```

### 2. Install the autonomous outbound loop

```text
/plugin install autonomous-outbound-loop
```

### 3. Configure and run one safe tick

```text
/autonomous-outbound-loop:configure-loop
/autonomous-outbound-loop:run-loop --mode tick
/autonomous-outbound-loop:monitor-loop
```

State persists under `workspace/autonomous-loop/`. Demo leads live in `workspace/leads/`.

### 4. Try the sales assistant skills

Ask Claude to apply skills from `sales-assistant/skills/`:

- Contact filter (workable vs skip)
- List builder (ZoomInfo-style criteria)
- 5-part cold email formula
- Multi-thread and re-engage playbooks

---

## Repository layout

```text
gtm-automation-engine/
├── .claude-plugin/marketplace.json   # Marketplace manifest (67 plugins)
├── plugins/                          # Plugin suite + autonomous-outbound-loop
├── sales-assistant/                  # Outbound qualification and copy skills
├── workspace/                        # Loop state + synthetic demo leads
├── docs/                             # Usage guides and use cases
├── scripts/                          # Validation and scaffolding utilities
├── ARCHITECTURE.md                   # Engineering design doc
├── NOTICES.md                        # Third-party attribution
└── LICENSE                           # Apache-2.0
```

---

## Documentation

| Doc | Description |
|-----|-------------|
| [GETTING_STARTED.md](GETTING_STARTED.md) | First-time setup |
| [QUICK_START.md](QUICK_START.md) | Fast path to first workflow |
| [docs/usage-guide.md](docs/usage-guide.md) | Commands and patterns |
| [docs/FAQ.md](docs/FAQ.md) | Common questions |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design |

---

## License

Apache License 2.0. Copyright 2026 ishan bhosale. See [LICENSE](LICENSE) and [NOTICES.md](NOTICES.md).

Impact figures in `pitch/gtm-platform-deck.html` are **illustrative / modeled, not actual results**.

