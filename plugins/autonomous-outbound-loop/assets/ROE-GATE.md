# ROE Gate - ExampleCo Workable Contact Compliance

**Author:** ishan bhosale | **Copyright:** 2026 ishan bhosale

The autonomous outbound loop **must not** contact prospects until this gate passes. This document mirrors `.cursor/rules/sales-outbound-agent.mdc` and `sales-assistant/skills/01-contact-filter.md` for loop operators.

## Hard stops (Layer 1 - Salesforce)

Skip immediately if any are true:

1. Open opportunity on the account
2. Active customer or partner
3. DNC or email opt-out on contact or account
4. Outside operator ROE territory

## Sequence and activity (Layer 2 - Outreach + Salesforce)

Skip if:

5. Contact is in another rep's active sequence with last touch < 90 days
6. AE or CSM logged email, call, or meeting in last 90 days

## Recency (Layer 3)

Skip if:

7. Any logged activity on contact in last 12 months (unless explicit revival playbook applies)
8. Negative reply on record in last 12 months

## Data quality (Layer 4)

Skip or flag if:

9. Invalid business email or known bounce
10. Title does not map to ExampleCo buyer persona table
11. Borderline territory or ownership dispute → **FLAG FOR REVIEW**

## Required output per contact

```
CONTACT: [Name] | [Title] | [Company]
VERDICT: WORKABLE | SKIP | FLAG FOR REVIEW
REASON: [Exact rule]
NEXT ACTION: [Stage instruction or stop]
```

## Loop enforcement

| Stage | RoE requirement |
|-------|-----------------|
| Scout | Full filter before queue insert |
| Writer | Only WORKABLE rows; no override |
| Rep | Re-check if row > 24h stale |
| Closer | Confirm no new open opp before meeting booking |
| Mission Control | Sample audit + halt on violation |

## Systems of record

- **Salesforce**: account type, opps, activity, DNC
- **Outreach**: sequences, touches, sentiment
- **Glean**: internal history, ROE docs, references (search before Scout)

HubSpot is **not** used in this stack.

## Related skills

- `intent-signal-orchestration` → `suppression-logic`
- `sales-assistant` → `01-contact-filter.md`
- `sales-handoff-orchestration` → `routing-logic` (post-qualification only)

---

