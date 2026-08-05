# Third-Party Notices

This repository combines original work by ishan bhosale with adapted open-source GTM agent tooling. Attribution is intentional and required.

## 1. GTM plugin marketplace (`plugins/`)

The plugin and skill marketplace under `plugins/` is **derived from and adapted from** an open-source GTM agents plugin marketplace licensed under the **Apache License 2.0**.

- **Upstream**: Open-source GTM agents plugin marketplace (Apache-2.0)
- **This repo**: Rebranded, genericized, and extended as **GTM Automation Engine**
- **Modifications**: Employer-specific content removed; autonomous outbound loop added; documentation and governance assets re-authored
- **Requirement**: Apache-2.0 requires preservation of copyright, license, and NOTICE attributions for derivative works. This file satisfies that obligation.

If you redistribute this project, include this NOTICES file and the `LICENSE` file with your distribution.

## 2. Autonomous agent-loop pattern (`plugins/autonomous-outbound-loop/`)

The scout → writer → rep → closer orchestration pattern, with heartbeat cadence and shared memory, was **inspired by** open-source GTM agent tooling released under the **MIT License**.

- **Relationship**: Conceptual inspiration and architectural pattern; **re-authored** for this repository (not a verbatim copy)
- **Original components here**: `ROE-GATE.md`, loop commands, agent prompts, workspace templates, and integration guidance written for GTM Automation Engine

## 3. Software dependencies

Runtime dependencies are minimal:

| Component | Dependency |
|-----------|------------|
| Python scripts (`scripts/`, `workspace/leads/`) | Python 3 standard library only (`csv`, `pathlib`, `re`, etc.) |
| Plugin runtime | Claude Code (Anthropic) with marketplace install |
| Optional integrations | Salesforce, Outreach, Glean, ZoomInfo (external services, not bundled) |

No `requirements.txt`, `pyproject.toml`, or root `package.json` is required for core operation.

## 4. LICENSE recommendation (Apache-2.0 vs MIT)

**Recommendation: keep Apache-2.0** as the project license.

| Factor | Apache-2.0 | MIT |
|--------|------------|-----|
| Substantial `plugins/` content derived from Apache-2.0 upstream | Compatible; satisfies upstream obligations | Does not satisfy Apache-2.0 attribution requirements for the derivative marketplace |
| Patent grant | Explicit | None |
| NOTICE file | Expected for derivatives | Not required |

The root `LICENSE` file is Apache-2.0 with **Copyright 2026 ishan bhosale**. Upstream Apache-2.0 attribution lives in this NOTICES file. If you prefer MIT for net-new code only, consult counsel: a single repo license cannot erase Apache-2.0 obligations on the adapted marketplace portion.

## 5. AI-assisted development

Portions of this repository were produced with AI-assisted development (Claude and related tooling). Human review, genericization, and attribution were applied before publication.

---

**Maintainer**: [ishan bhosale](https://github.com/tejaskembalkar-ship-it)  
**Project**: [gtm-automation-engine](https://github.com/tejaskembalkar-ship-it/gtm-automation-engine)

