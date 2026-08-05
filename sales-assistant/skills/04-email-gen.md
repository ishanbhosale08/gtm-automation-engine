# Skill: email-gen

**When to use**: Any time you need a cold email, bump, or LinkedIn first-touch for an ExampleCo prospect. Every email produced by this skill follows the 5-part formula. No exceptions.

---

## The 5-part ExampleCo formula

Every email has exactly these five parts. If a part is missing or generic, delete the email and start over.

### Part 1: Specific public-signal opener

One sentence naming a fact about the prospect's company that implies an operations or data automation problem. Must be verifiable (you have the URL or the Salesforce/ZoomInfo source). Must be recent (last 90 days is ideal, last 12 months acceptable).

**High-signal triggers for ExampleCo:**

| Trigger | Where to find it | Why it matters |
|---|---|---|
| New facility, warehouse, or office in a new region | Press release, company website, LinkedIn company post | Creates multi-system data sync and reporting gaps |
| Acquisition or merger | Press release, SEC filing, news | Inherited tool sprawl, duplicated workflows, integration debt |
| New market or entity registration | Business filings, registered agent notices | Ops teams may not have automation scoped for the new entity |
| Rapid headcount growth in new regions | LinkedIn Insights, job postings | Remote hubs increase reconciliation and handoff complexity |
| ERP migration or upgrade (NetSuite, Sage, SAP, Dynamics) | Job postings, partner news, careers page | Workflow automation is almost always a gap in ERP rollouts |
| Multi-entity nonprofit or association operating nationally | Website locations or chapters page | Document and approval workflows are often manual |
| E-commerce launch or platform change | Website, Shopify/BigCommerce partner news | Order-to-ledger sync breaks without automation |
| Quarter-end or audit season approaching | Calendar | Tie to reporting readiness and close cycles |
| Recent footprint expansion (warehouses, retail, data centers) | CBRE/JLL announcements, press releases | Operational reporting complexity increases |
| RevOps or Operations hiring surge | Job boards, LinkedIn | Signals active tooling evaluation |

### Part 2: "Poke the bear" diagnostic question

One binary question. Format is always:

> Do you already have a way to [desired outcome], or is your [team / people] still [painful manual process]?

**Proven ExampleCo diagnostic questions by module:**

Core Automation Platform:
- "Do you already have a way to reconcile data across [new region] and your core systems automatically, or is your team still exporting CSVs every week?"
- "Do you already have one platform that keeps ops and finance workflows in sync across all locations, or is someone still patching gaps in spreadsheets at month-end?"
- "Do your ERP and billing systems already push changes to new regions automatically, or does someone on the ops team still reconfigure integrations after each expansion?"

Document / Compliance Workflow module:
- "Do you already have a way to route and track approval documents across every team and vendor, or is your team still chasing status in email threads?"
- "Do you already have a central system where every workflow record is stored and auditable, or is someone on your ops team still managing that in spreadsheets?"

Multi-Region Ops:
- "Do you already have a way to standardize reporting when you open a new market, or is each region still running its own manual process?"
- "Do you already have a system that centralizes operational dashboards across all locations, or is your team juggling multiple tools and calendars?"

### Part 3: Named-account social proof

One sentence. Fictional or approved reference customer the prospect would recognize. Specific verb and specific outcome. No adjectives. No invented metrics.

**Reference accounts (fictional demo roster):**

| Segment | Examples to reference |
|---|---|
| Manufacturing / Distribution | Meridian Logistics, Summit Components |
| SaaS / high-growth | Contoso Software, Fabrikam Labs |
| E-commerce | Globex Retail |
| Enterprise | NorthwindSaaS |

Format: "[Company] uses ExampleCo to [specific outcome in 10 words or less]."

If you are not sure whether a company is an approved reference, do not use them. Ask your manager for the approved reference list.

### Part 4: Low-friction reciprocity CTA

The "buy lunch over Zoom" offer is the canonical ExampleCo CTA. Keep it. It works because it is specific (20 minutes), playful (lunch implies relaxed), and the reciprocity is real (they expense it).

Variations:
- "I'd love to buy you lunch over Zoom and show you exactly how to get [region] workflows live before [deadline]."
- "I'd love to buy you lunch over Zoom and show you how [reference company] centralized ops data in one place."
- "I'd love to buy you lunch over Zoom and walk you through exactly how [reference company] automated this in [X] days."

Always end with one word: "Interested?"

### Part 5: Opt-out + tight signature

Exact line, lowercase, always present:

> If you don't want any more emails, "no thanks" is appreciated.

Signature: First name, Last name / Title / Company / Address. Nothing else.

---

## The bump

Send 3 business days after the initial email if no reply. Keep it under 25 words. Human, not automated-sounding.

Canonical bump (copy verbatim):
> Hey [FirstName], just bumping this up. Still worth a 20-minute Zoom. I'll buy lunch. Open to it?

Second bump (send 7 business days after bump 1):
> Hey [FirstName], last nudge from me. If timing is off, totally fine, just reply "later" and I'll circle back next quarter. Otherwise I'll assume it's not a fit.

---

## QA checklist (run before every send)

Every email must pass all of these or it does not go out:

- [ ] Opener names a SPECIFIC recent fact, not a generic one
- [ ] The fact implies an ops or data automation problem ExampleCo actually solves
- [ ] Diagnostic question is binary ("do you already... or is your team still...")
- [ ] Social proof is an approved reference customer
- [ ] CTA offers something before asking (lunch + demo)
- [ ] Opt-out line is present, lowercase
- [ ] Body is under 120 words
- [ ] No em dashes anywhere
- [ ] No "I hope this email finds you well," "circling back," "touching base," "leverage," "synergy"
- [ ] No exclamation marks in the body
- [ ] Read it aloud: does it sound human or like a template?

---

## Output format

Every email produced by this skill returns exactly this structure:

```
SUBJECT: [Under 50 characters, references the specific trigger]

EMAIL:
[Body, under 120 words]

If you don't want any more emails, "no thanks" is appreciated.

[First Last]
[Title]
ExampleCo
[Your office address]

---
BUMP 1 (send day +3):
[Under 25 words]

BUMP 2 (send day +10):
[Under 25 words]

---
RESEARCH NOTES:
- Trigger used: [specific fact + source]
- Product angle: [which ExampleCo module and why it fits]
- Reference customer used: [company + why this prospect would care]
- QA: [all checks pass / list any that did not]
```

---

## Worked examples (fictional demos)

### Example 1: New region expansion (Core Automation Platform)

```
SUBJECT: Dublin hub

Hey Alex, with NorthwindSaaS opening your Dublin hub this quarter, do you already have a way to sync operational data across US and EU systems automatically, or is your team still reconciling exports manually each week?

Meridian Logistics and Summit Components use ExampleCo to stand up cross-region workflows in days. I'd love to buy you lunch over Zoom and show you exactly how to get Dublin live before Q2 close.

Interested?

If you don't want any more emails, "no thanks" is appreciated.

Morgan Rasmussen
Partnerships at ExampleCo
100 Market Street, Suite 400, San Francisco, CA 94105
```

### Example 2: ERP migration (Integration Hub)

```
SUBJECT: NetSuite cutover

Hey Randall, with Contoso Software mid-migration on NetSuite, the handoffs between billing, ops, and reporting usually get messy right after go-live.

Do you already have a way to keep workflows aligned while systems change underneath you, or is that still a manual fire drill every sprint?

Fabrikam Labs uses ExampleCo to keep integrations stable through ERP changes. I'd love to buy you lunch over Zoom and show you how it works.

Interested?

If you don't want any more emails, "no thanks" is appreciated.

Morgan Rasmussen
Partnerships at ExampleCo
100 Market Street, Suite 400, San Francisco, CA 94105
```

### Example 3: Multi-region nonprofit-style ops (Document Workflow module)

```
SUBJECT: approval workflows

Hey Jordan, Globex Health Co-op operates programs across six regions. Do you already have a way to route and track approval documents across every team and vendor, or is your team still chasing status in email threads?

Contoso Software uses ExampleCo to handle this on autopilot. I'd love to buy you lunch over Zoom and show you how to centralize Globex's workflow records in one place.

Interested?

If you don't want any more emails, "no thanks" is appreciated.

Morgan Rasmussen
Partnerships at ExampleCo
100 Market Street, Suite 400, San Francisco, CA 94105
```
