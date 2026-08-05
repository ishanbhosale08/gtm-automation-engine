# Leads workspace

This directory holds **synthetic sample data only** for demonstrating the outbound workflow. No real contacts, employers, or CRM exports are stored here.

## Files

| File | Purpose |
|------|---------|
| `sample_contacts.csv` | ~10 fake contacts (ExampleCo, NorthwindSaaS, etc.) with name, title, company, email, and status |
| `parse_leads.py` | Loads `sample_contacts.csv` and prints a workable-queue summary |
| `filter_contacts.py` | Generic contact-filter helper (demo) |
| `prospecting-nodes.json` | Illustrative n8n node patches for ICP scoring workflows |
| `zoominfo-icp-criteria.md` | Generic ZoomInfo ICP search criteria template |

## Usage

```bash
python workspace/leads/parse_leads.py
```

Replace `sample_contacts.csv` with your own sanitized export before running against production systems. Never commit real lead data to this repository.
