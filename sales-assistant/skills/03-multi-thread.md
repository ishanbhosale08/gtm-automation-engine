# Skill: multi-thread

**When to use**: Once you have one workable contact at an account, use this skill to find 2-4 additional stakeholders at the same account to enroll in a parallel or staggered sequence. Multi-threading increases meeting conversion rates significantly because if one contact ignores you, another one might respond.

---

## Why multi-threading works for ExampleCo

ExampleCo buying decisions touch multiple departments: Finance, Operations, IT/Engineering, and sometimes Legal. An Operations Manager might want it but the Controller approves the budget. The CTO or VP of Engineering has to approve the integration. If you only sequence one person, you are relying on a single point of failure.

The goal is not to spam an account. It is to reach 3-4 people who each have a legitimate reason to care, with messages that are relevant to their specific role.

---

## Step 1: Map the org

Ask the assistant: "Multi-thread [Company Name] - I have [current contact's name and title]."

The assistant will suggest which additional titles to find based on product:

### Core Automation Platform multi-thread map

| You have | Also find |
|---|---|
| Controller | CFO (budget holder) + Dir of IT/ERP (integration) + VP Operations (day-to-day user) |
| VP Operations | Controller (approver) + VP Finance (sponsor) + Dir of IT (integration owner) |
| CFO | Controller (champion) + RevOps Director (if exists) |
| VP Engineering / CTO | Controller or CFO (business sponsor) + VP Operations |

### Document / Compliance Workflow module multi-thread map

| You have | Also find |
|---|---|
| Compliance Manager | AP Manager (operational pain) + Controller (approver) + VP Finance (sponsor) |
| AP Manager | Compliance Manager (if separate) + Controller + Dir of Operations |
| Controller | Compliance Manager + CFO |

### Multi-Region Ops add-on multi-thread map

| You have | Also find |
|---|---|
| RevOps Director | CFO + VP Operations + Controller |
| VP Operations | RevOps Director + Controller |
| Controller | VP Operations + CFO |

---

## Step 2: Find the contacts

Use LinkedIn or ZoomInfo to find the additional contacts at the same account.

**LinkedIn search method:**
1. Go to LinkedIn, search the company name
2. Click "People" tab on the company page
3. Filter by keyword: the title you want
4. Cross-reference with ZoomInfo for direct email

**ZoomInfo method:**
1. Search company name in ZoomInfo
2. Go to "Contacts" tab for that company
3. Filter by department or title keyword
4. Verify email is valid before adding to sequence

---

## Step 3: Run each new contact through contact-filter

Every additional contact found must pass the workable filter before you sequence them. Do not skip this step even if the account looks clean - one of the contacts might be in another rep's sequence or have a DNC flag.

---

## Step 4: Sequence staggering

Do not enroll all contacts at the same account on the same day. Stagger by 3-5 business days to avoid setting off spam filters and to avoid an awkward situation where three people at the same company all get the same email on the same morning.

Recommended stagger:
- Day 1: Primary contact (the one you already had)
- Day 4: Second contact
- Day 8: Third contact
- Day 12: Fourth contact (if applicable)

---

## Step 5: Tailor the message to role

Each contact gets a version of the email that speaks to their specific pain. The core product story is the same but the diagnostic question and the angle change.

### Example: NorthwindSaaS expanding into the EU region

**VP Operations version:**
> "With NorthwindSaaS opening your Dublin hub this quarter, do you already have a way to sync operational data across US and EU systems automatically, or is your team still reconciling exports manually each week?"

**Controller version:**
> "With NorthwindSaaS live in Dublin, do you already have one platform that reconciles billing and ops data across regions, or is your team still stitching numbers together at month-end?"

**VP Engineering / IT version:**
> "With NorthwindSaaS expanding into the EU, do your ERP and billing systems already push changes to new regions automatically, or does someone on the ops team still reconfigure integrations after each expansion?"

Notice: same company trigger, same product, three different diagnostic questions aimed at three different pains.

---

## Output format

```
MULTI-THREAD PLAN: [Company Name]
Existing contact: [Name, Title] - [Sequence they are in or planned sequence]

ADDITIONAL CONTACTS TO FIND:
1. [Title to target] - Priority: High/Med - Reason: [Why this title matters for ExampleCo at this account]
2. [Title to target] - Priority: High/Med - Reason: ...
3. [Title to target] - Priority: Med - Reason: ...

FOUND (after ZoomInfo/LinkedIn search):
| Name | Title | Email | LinkedIn | Verified? | Contact-filter result |
|------|-------|-------|----------|-----------|----------------------|
| ... | ... | ... | ... | Yes/No | WORKABLE / SKIP / FLAG |

SEQUENCE STAGGER SCHEDULE:
- Day 1: [Name] - [Sequence name]
- Day 4: [Name] - [Sequence name, Role-variant]
- Day 8: [Name] - [Sequence name, Role-variant]

ROLE-VARIANT EMAILS:
[If requested, paste the role-specific email variants here using email-gen skill format]
```
