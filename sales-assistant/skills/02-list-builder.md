# Skill: list-builder

**When to use**: When you want to build a net-new prospecting list from ZoomInfo or a partner directory. Use this before the contact-filter skill to generate raw candidates, then filter them.

---

## Part A: ZoomInfo list build

### Step 1: Define your ICP filters

Tell the assistant your current focus. It will generate the exact ZoomInfo filter settings to use.

**Inputs to provide:**
- Product focus (Core Automation Platform, Document Workflow module, Multi-Region Ops, Integration Hub)
- Geography (state, region, or "my ROE territory")
- Company size range (employee count or revenue range)
- Industry vertical (optional but tightens results)
- Any specific trigger you want to target (new market expansion, recent funding, hiring surge, ERP migration)

### Step 2: ZoomInfo filter templates by product

#### Core Automation Platform targets

```
ZoomInfo Filters:
- Job Title (contains any): "Controller," "VP Finance," "CFO," "VP Operations," "Director of Operations," "RevOps Director," "Head of Finance," "Director of Accounting"
- Seniority: Director, VP, C-Suite
- Department: Finance, Operations, Revenue Operations
- Company Revenue: $10M - $500M (adjust per your segment)
- Company Size: 50 - 2,500 employees
- Industry: Retail, Manufacturing, Distribution, E-commerce, Technology, Professional Services
- Geography: [your territory states]
- Email Verified: Yes
- Exclude: Active customers (import suppression list from Salesforce export)
```

**High-signal intent filters to layer on (if your ZoomInfo tier includes them):**
- Intent topic: "workflow automation," "data integration," "RevOps tooling," "ERP implementation," "NetSuite," "Sage Intacct," "SAP"
- Recent job change: Filter for contacts who changed jobs in last 6 months (new decision-makers move fast in first 90 days)
- Company news: Recent funding round, recent acquisition, recent expansion to new region

#### Document / Compliance Workflow module targets

```
ZoomInfo Filters:
- Job Title (contains any): "Compliance Manager," "AP Manager," "Accounts Payable Manager," "Operations Manager," "Controller," "Director of Compliance"
- Seniority: Manager, Director, VP
- Department: Finance, Operations, Compliance
- Company Revenue: $5M - $200M
- Industry: Manufacturing, Distribution, Wholesale, Healthcare, Professional Services
- Geography: [your territory states]
- Email Verified: Yes
```

**Why mid-market ops teams fit:** They manage high document volume across vendors and regions. Manual approval chains and spreadsheet trackers are common. Globex Industries (multi-region, manual workflows) is a good fictional pattern.

#### Multi-Region Ops add-on targets

```
ZoomInfo Filters:
- Job Title (contains any): "VP Operations," "Director of Business Systems," "RevOps Director," "Controller," "CFO," "Dir of Finance"
- Seniority: Manager, Director, VP, C-Suite
- Department: Finance, Operations, Revenue Operations
- Company Revenue: $50M+ (multi-region automation makes economic sense at this size)
- Industry: Retail (large footprint), Manufacturing (multi-facility), SaaS (multi-entity billing), Healthcare
- Geography: [your territory states]
- Keyword (company): "multiple locations," "global operations," "distribution centers"
```

### Step 3: Suppression - CRITICAL

Before exporting from ZoomInfo, import a suppression list to exclude:
1. Export all active customer accounts from Salesforce (Account Type = Customer)
2. Export all active partner accounts (Account Type = Partner)
3. Export all DNC contacts (Do Not Contact = True)
4. Export all accounts with open opportunities

Upload these as suppression files in ZoomInfo before downloading your list. This prevents wasting credits on contacts you cannot work.

### Step 4: Export format

Request these fields from ZoomInfo:
- First Name, Last Name
- Title, Seniority, Department
- Direct Email (verified)
- Direct Phone (mobile preferred)
- Company Name, Company Website
- Company Revenue, Employee Count
- Industry, Sub-Industry
- LinkedIn URL (for research and LinkedIn outreach)
- State, City
- ZoomInfo Company ID (for deduplication)

---

## Part B: Partner directory scraping

### What this is for

ExampleCo's partner directory lists ERP consultants, systems integrators, and technology partners. These firms often have clients who need workflow automation but are not yet customers. Targeting the partner's clients through a co-sell motion is a high-conversion play.

### How to use it

1. Go to the ExampleCo Partner Directory (partners.example-saas.com or the internal partner portal)
2. Filter by partner type: ERP Reseller, SI Partner, RevOps consultancy
3. For each partner firm, search their website, LinkedIn, and G2 reviews for client industries and sizes
4. Look for client case studies and testimonials - these name companies that are partner-managed and likely need automation
5. Cross-reference with ZoomInfo to find the Finance or Operations contact at those companies

### Partner co-sell play email hook

When a prospect uses a firm that is a partner account, use this opener:

> "Hey [Name], [Partner Firm Name] is actually a partner account, so they can implement this for you in days rather than months if the fit is right. Do you already have a way to reconcile data across [X] systems automatically, or is [Partner Firm] still stitching spreadsheets together for you each month?"

---

## Output format

After building the raw list, the assistant outputs a preview table for your review before any outreach:

```
LIST BUILD PREVIEW
Product focus: [product]
Filters applied: [summary]
Raw count from ZoomInfo: [N]
After suppression: [N]
Ready for contact-filter: [N]

SAMPLE (first 5 contacts):
| # | Name | Title | Company | Revenue | State | Signal | Priority |
|---|------|-------|---------|---------|-------|--------|----------|
| 1 | ... | ... | ... | ... | ... | ... | High/Med/Low |
...

ACTION: Reply "filter all" to run all through contact-filter, or "filter top 20" to start with the highest-priority 20.
```

Priority scoring:
- **High**: Matches exact persona title + has intent signal + company in growth mode
- **Medium**: Matches persona title, no intent signal
- **Low**: Matches secondary persona title or has data quality question

---

## List hygiene rules

- Never add a contact to a sequence directly from ZoomInfo export. Always run through contact-filter first.
- Keep ZoomInfo lists in a dated Google Sheet or CSV. Name format: `YYYY-MM-DD_[Product]_[Territory]_raw.csv`
- After filtering, keep a separate sheet: `YYYY-MM-DD_[Product]_[Territory]_workable.csv`
- Log the export date. ZoomInfo data goes stale fast. Refresh any list older than 60 days before re-using.
