#!/usr/bin/env python3
"""Serialize accepted, manually read source quotations; make no mathematical verdicts."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
audit = json.loads((HERE / 'hyperplanes_quote_audit.json').read_text())
plan_path = HERE / 'hyperplanes_selected_quotes.json'
plan = json.loads(plan_path.read_text())
source = (ROOT / 'sources/texts/api/ega_v_cote25_combined.tex').read_text().splitlines()
by_number = {s['claim']: s for s in plan['selections']}
for record in audit['records']:
    number = int(record['claim_id'].rsplit('-', 1)[1])
    selections = record['selected_excerpts']
    for excerpt in selections:
        actual = '\n'.join(source[excerpt['first_line'] - 1:excerpt['last_line']])
        assert actual == excerpt['verbatim'], (number, excerpt['first_line'])
    by_number[number] = {
        'claim': number,
        'scans': sorted({scan for excerpt in selections for scan in excerpt['scans']}),
        'ranges': [[e['first_line'], e['last_line']] for e in selections],
        'reason': record['selection_reason'],
        'scope_note': record['scope_or_reading_note'],
        'audit_record': 'integration/hyperplanes_quote_audit.json#' + record['claim_id'],
        'accepted_by': 'SA23-20261119/root after individual review of the quoted selections and scope flags',
    }
plan['selections'] = sorted(by_number.values(), key=lambda r: r['claim'])
plan['final_audit_note'] = ('All 23 BT selections accepted after root review. The earlier three root '
    'selections remain. Source wording, including uncertainty and cancellation markup, is unchanged. '
    'Claims090 and105 receive separately authored scope corrections; question provenance is audited separately.')
plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_verbatim_segments': sum(len(r['selected_excerpts']) for r in audit['records']),
                  'accepted_claims': len(audit['records']), 'all_selected_claims': len(plan['selections'])}))
