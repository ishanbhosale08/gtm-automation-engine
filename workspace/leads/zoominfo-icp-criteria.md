# ZoomInfo Search Criteria - ExampleCo ICP (ishan bhosale)

Run these searches in ZoomInfo to generate net-new prospect lists outside your Salesforce sequences.
Export each search as CSV, then run through the workable filter before loading into Outreach.

---

## How to Use

1. Open ZoomInfo > Search > People
2. Apply filters from the vertical section below
3. Add: **Company - Not in Salesforce** (suppression - prevents re-adding active customers)
4. Export up to 100 contacts, save to `workspace/leads/`
5. Paste the CSV path here and ask to run the workable filter

---

## Vertical 1: E-Commerce / Direct-to-Consumer (Highest Volume)

**Target personas:** VP Finance, Controller, CFO, VP Operations, VP E-Commerce

**Company filters:**
- Industry: Retail, Online Retail, E-Commerce
- Employee count: 50-500
- Revenue: $10M - $100M
- HQ Country: United States
- Technologies used: Shopify Plus, Magento, BigCommerce, WooCommerce, NetSuite, Brightpearl

**Person filters:**
- Title keywords (include ANY): Controller, CFO, VP Finance, Finance Director, VP Operations, RevOps Director, VP Ecommerce, Dir Commerce
- Title keywords (exclude): Junior, Coordinator, Analyst, Assistant, Intern, VP IT, CTO
- Seniority: VP, C-Suite, Director, Manager (Manager only for Finance/Ops)
- Location: United States

**Why Now signals to look for in ZoomInfo:**
- "Recently hired" CFO or Controller (new exec = new vendor review)
- Company funding in last 12 months (growth = new market complexity)
- Headcount growth 20%+ (scaling = workflow gaps)

**ZoomInfo saved search name:** `EXC-Ecommerce-ICP-v1`

---

## Vertical 2: SaaS / Software Companies

**Target personas:** VP Finance, Controller, CFO, Revenue Operations, VP Operations

**Company filters:**
- Industry: Computer Software, SaaS, Internet, B2B Software
- Employee count: 100-1000
- Revenue: $10M - $200M
- HQ Country: United States
- Technologies used: Salesforce, HubSpot, Zuora, Stripe, Recurly, Chargebee

**Person filters:**
- Title keywords (include ANY): Controller, CFO, VP Finance, Finance Director, RevOps Director, Head of Finance, VP Operations
- Title keywords (exclude): Junior, Coordinator, VP Engineering, CTO, VP Product
- Seniority: VP, C-Suite, Director

**Why Now signals:**
- Zuora/Recurly/Chargebee in tech stack = subscription billing + multi-entity complexity
- PE or VC-backed (multi-region ops scaling)
- IPO prep activity

**ZoomInfo saved search name:** `EXC-SaaS-ICP-v1`

---

## Vertical 3: Manufacturing & Distribution

**Target personas:** Controller, CFO, VP Finance, VP Operations, Operations Manager

**Company filters:**
- Industry: Manufacturing, Industrial Machinery, Wholesale Distribution, Building Materials
- Employee count: 100-2000
- Revenue: $25M - $500M
- HQ Country: United States
- Technologies used: SAP, Oracle ERP, Microsoft Dynamics, Epicor, Infor

**Person filters:**
- Title keywords (include ANY): Controller, CFO, VP Operations, Operations Manager, VP Finance, Finance Director, RevOps Director
- Title keywords (exclude): Plant Manager, VP Supply Chain, Logistics (unless multi-threading)
- Seniority: VP, C-Suite, Director, Manager

**Why Now signals:**
- Recently expanded to new regions (new warehouse, distribution center)
- M&A activity in last 18 months
- SAP or Dynamics implementation in progress (ERP change = workflow re-evaluation)

**ZoomInfo saved search name:** `EXC-Mfg-ICP-v1`

---

## Vertical 4: Professional Services / Systems Integrators

> **Note:** Check ROE before touching partner-adjacent firms - territory carve-outs may apply.

**Target personas:** Operations Manager, Compliance Manager, AP Manager, CFO

**Company filters:**
- Industry: Business Services, IT Services, Management Consulting
- Employee count: 50-500
- Revenue: $5M - $100M
- HQ Country: United States

**Person filters:**
- Title keywords (include ANY): Operations Manager, Compliance Manager, AP Manager, Controller, RevOps Director
- Seniority: Director, Manager

**ZoomInfo saved search name:** `EXC-ProfSvc-ICP-v1`

---

## Vertical 5: Multi-Location Operations (Multi-Region Ops module)

**Target personas:** VP Operations, RevOps Director, Dir of Business Systems, Controller

**Company filters:**
- Industry: Retail, Hospitality, Healthcare networks, Commercial services
- Employee count: 100-2000
- Revenue: $50M+
- HQ Country: United States

**Person filters:**
- Title keywords (include ANY): VP Operations, RevOps Director, Dir of Business Systems, Controller, CFO, Operations Manager
- Seniority: VP, Director, Manager

**ZoomInfo saved search name:** `EXC-MultiRegion-ICP-v1`

---

## Universal Suppression Filters (Apply to ALL Searches)

Add these to every ZoomInfo search to avoid touching contacts already in Salesforce or disqualified:

| Filter | Setting |
|--------|---------|
| CRM Suppression | "Suppress contacts in Salesforce" |
| Email Status | Valid (exclude Do Not Contact, Bad Email) |
| Direct Phone | Include if available |
| Last Updated | Within 12 months |
| Exclude Job Title | Intern, Junior, Coordinator, Assistant |
| Exclude Industry | Government (Govt entities rarely buy SaaS) |

---

## Export Settings

- **Format:** CSV
- **Fields to include:** First Name, Last Name, Title, Company, Email, Direct Phone, LinkedIn URL, Company HQ, Employee Count, Revenue, Technologies, Recent Funding
- **Max export per search:** 100 contacts (keeps list manageable for personalization)
- **File naming:** `YYYY-MM-DD-exampleco-[vertical]-zoominfo-export.csv`
  - Example: `2026-05-28-exampleco-ecommerce-zoominfo-export.csv`
- **Save to:** `workspace/leads/`

---

## After Export - What to Do

1. Drop CSV path here and ask: "Run workable filter on this ZoomInfo export"
2. The filter checks: active customer, open opp, DNC, email domain validity
3. WORKABLE contacts go into Outreach as a new sequence
4. FLAG contacts get manual review before touch
5. SKIP contacts are suppressed from the export in ZoomInfo (update suppression list)

---

## Weekly Cadence

| Day | Action |
|-----|--------|
| Monday | Run 1-2 ZoomInfo searches (25-50 contacts per vertical) |
| Monday | Run workable filter, load WORKABLE into Outreach |
| Wednesday | Check email replies in Outreach, update Salesforce |
| Friday | Review pipeline impact, adjust ICP criteria if needed |

Target: 50 new qualified contacts/week into sequences.

