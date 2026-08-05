import re
import sys

def extract_contacts(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('  - createTime:')
    contacts = []

    for block in blocks[1:]:
        c = {}

        def get(pattern, default=''):
            m = re.search(pattern, block)
            return m.group(1).strip() if m else default

        c['name'] = get(r'title: (.+)')
        c['account'] = get(r'accountname\[1\]: (.+)')
        c['url'] = get(r'url: "(.+?)"')
        c['active_customer'] = get(r'activecustomer\[1\]: "(.+?)"')
        c['active_partner'] = get(r'activepartneraccount\[1\]: "(.+?)"')
        c['mkt_opt_out'] = get(r'allmarketingoptout\[1\]: "(.+?)"')
        c['in_engage_flow'] = get(r'currentlyinengageflow\[1\]: "(.+?)"')
        c['account_engaged_by'] = get(r'accountengagedby\[1\]: (.+)')
        c['business_structure'] = get(r'businessstructure\[1\]: (.+)')
        c['rating'] = get(r'rating\[1\]: (.+)')
        c['contact_status'] = get(r'contactstatus\[1\]: (.+)')
        c['nurture_reason'] = get(r'nurturereason\[1\]: (.+)')
        c['seq_user'] = get(r'currentsequenceusername\[1\]: (.+)')

        # From snippet - use simpler patterns
        snippet = get(r'snippets\[.+?\]: "(.+)"')

        def snip(key):
            m = re.search(r'"' + re.escape(key) + r'":"([^"]*)"', block)
            return m.group(1) if m else ''

        c['email'] = snip('Email')
        c['title_role'] = snip('Title')
        c['email_opt_out'] = snip('Email Opt Out')
        c['open_opps'] = snip('No. of Open Opportunities')
        c['actively_sequenced'] = snip('Actively Being Sequenced')
        c['last_activity'] = snip('Last Sales Development Activity')
        c['sequence_name'] = snip('Sequence Name')
        c['ltb_score'] = snip('MK Likelihood To Buy Score')
        c['engage_flow_owner'] = snip('Engage Flow Owner')
        c['engage_flow_name'] = snip('Engage Flow Name')
        c['account_record_type'] = snip('Account Record Type')

        if c['name'] and c['account']:
            contacts.append(c)

    return contacts


def run_filter(contacts):
    results = {'WORKABLE': [], 'SKIP': [], 'FLAG': []}

    for c in contacts:
        reasons = []
        verdict = 'WORKABLE'

        email = c['email'].lower()
        personal_domains = ['@gmail.', '@yahoo.', '@hotmail.', '@aol.', '@icloud.', '@outlook.com', '@live.com']
        is_personal = any(d in email for d in personal_domains)

        # Hard disqualifiers
        if c['active_customer'] == 'true':
            verdict = 'SKIP'
            reasons.append('Active customer')
        elif c['active_partner'] == 'true':
            verdict = 'SKIP'
            reasons.append('Active partner')
        elif c['email_opt_out'] == 'true':
            verdict = 'SKIP'
            reasons.append('Email opt-out = true')
        elif c['mkt_opt_out'] == 'true':
            verdict = 'SKIP'
            reasons.append('All marketing opt-out = true')
        elif c['open_opps'] and float(c['open_opps']) > 0:
            verdict = 'SKIP'
            reasons.append('Open opportunity ({})'.format(c['open_opps']))
        elif c['in_engage_flow'] == 'true' and c['engage_flow_owner'] and c['engage_flow_owner'] != 'ishan bhosale':
            verdict = 'SKIP'
            reasons.append('In active Engage Flow owned by {}'.format(c['engage_flow_owner']))
        elif is_personal or not email or '@' not in email:
            verdict = 'SKIP'
            reasons.append('Personal/invalid email: {}'.format(c['email']))
        else:
            # Soft checks - may flag
            flag_reasons = []

            if c['account_engaged_by'] and 'CAM' in c['account_engaged_by']:
                flag_reasons.append('CAM engaged account')

            if c['business_structure'] and 'ExampleCo for Accountants' in c['business_structure']:
                flag_reasons.append('A4A territory carve-out - verify ROE')

            # 12-month activity check
            if c['last_activity'] and c['last_activity'] >= '2025-05-28':
                flag_reasons.append('Activity within 12mo ({})'.format(c['last_activity']))

            # Account record type conflict
            if c['account_record_type'] == 'Customer Account Type' and c['active_customer'] != 'true':
                flag_reasons.append('Account Record Type=Customer but Active Customer=false - verify')

            if flag_reasons:
                verdict = 'FLAG'
                reasons = flag_reasons
            else:
                verdict = 'WORKABLE'
                reasons = ['No disqualifiers found - verify territory and DNC in Outreach']

        c['verdict'] = verdict
        c['reasons'] = reasons
        results[verdict].append(c)

    return results


contacts = extract_contacts(r'C:\Users\tejas.kembalkar\.cursor\projects\c-Users-tejas-kembalkar-gtm-automation-engine\agent-tools\d59525c1-cafa-4f63-91fe-d15856e7b661.txt')
print('Total contacts parsed: {}'.format(len(contacts)))

results = run_filter(contacts)

print()
print('=== WORKABLE ({}) ==='.format(len(results['WORKABLE'])))
for c in results['WORKABLE']:
    print('  {} | {} | {} | {} | LTB:{} | {}'.format(
        c['name'], c['account'], c['title_role'][:35], c['email'], c['ltb_score'], '; '.join(c['reasons'])))

print()
print('=== FLAG FOR REVIEW ({}) ==='.format(len(results['FLAG'])))
for c in results['FLAG']:
    ltb = c['ltb_score'] if c['ltb_score'] else '?'
    print('  {} | {} | {} | {} | LTB:{} | {}'.format(
        c['name'], c['account'], c['title_role'][:35], c['email'], ltb, '; '.join(c['reasons'])))

print()
print('=== SKIPPED ({}) ==='.format(len(results['SKIP'])))
for c in results['SKIP']:
    ltb = c['ltb_score'] if c['ltb_score'] else '?'
    print('  {} | {} | {} | LTB:{} | {}'.format(
        c['name'], c['account'], c['email'], ltb, '; '.join(c['reasons'])))

