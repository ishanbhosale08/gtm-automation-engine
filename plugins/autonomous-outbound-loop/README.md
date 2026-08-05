# Autonomous Outbound Loop Plugin

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

Always-on orchestration pattern for outbound: Scout, Writer, Rep, Closer, supervised by Mission Control, with heartbeat cadence and shared memory between ticks.

## Quick start

1. configure-loop - copy config and workspace templates
2. run-loop --mode tick - single safe pass with RoE gate
3. monitor-loop - check queue health and compliance samples

## Layout

- agents: outbound-scout, writer, rep, closer, loop-mission-control
- commands: run-loop, configure-loop, monitor-loop
- skills: heartbeat-cadence, shared-memory, loop-orchestration
- assets: HEARTBEAT, ROE-GATE, config template, strategy playbooks

State persists under workspace/autonomous-loop/.

## Compliance

The loop does not bypass Rules of Engagement (workable-contact policy). Integrations: Salesforce, Outreach, Glean, ZoomInfo.


