#!/usr/bin/env python3
"""Merge actual recorded late reviews; preserve historical rows and scopes."""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)

def add(statement, who, kind, scope, outcome, evidence, when):
    if any(evidence == row['evidence'] for row in rows):
        return
    event_id = f"DPC-{max(int(r['event_id'].split('-')[1]) for r in rows)+1:03d}"
    rows.append(dict(zip(fields, [event_id, statement, '2026-11-21 Europe/Berlin',
        when, who, 'GPT-6 Astra Pro', 'not exposed by runtime', 'DP_MULT_20261121',
        kind, scope, outcome, evidence])))

with (root/'research/archive_binomial_check_events.tsv').open(newline='') as f:
    for row in csv.DictReader(f, delimiter='\t'):
        number = int(row['event_id'].removeprefix('ABA-CE'))
        if number < 27 or number > 30:
            continue
        add(row['statement_id'], row['checker'], 'targeted proof check',
            row['scope'], row['outcome']+' LIMIT: '+row['limitations'],
            'research/archive_binomial_check_events.tsv:'+row['event_id'], row['utc_time'])

meta_path = root/'research/paper_review_actual_dual_metadata.json'
meta = json.loads(meta_path.read_text())
for check in meta['checks']:
    add(check['finding'], meta['agent'], 'targeted proof check',
        check['scope']+'; exact mathematical block SHA256='+check['math_block_sha256'],
        check['result']+'; manual proof reading, not Lean compilation.',
        'research/paper_review_actual_dual_metadata.json:'+check['event'],
        check.get('observed_utc', meta['observed_utc']))

meta = json.loads((root/'research/actual_dual_independent_review_metadata.json').read_text())
add('DP32;DP33', '/root/formal_bound', 'targeted proof check',
    'Read complete saved all-height and height-three proofs; challenged exact functional-equation inputs, finite-free lifting, F/V cancellation and LT identification, all inverse coefficients, all A1-A22 recurrence and sharpness steps. Exact snapshots are recorded in metadata.',
    'PASS; detailed whole-proof review ADIR1-4; no claimed audit of complete external classical theorem proofs and no global-cost inference.',
    'research/actual_dual_independent_review.md; research/actual_dual_independent_review_metadata.json',
    meta['date_time_utc'])

now = datetime.now(timezone.utc).isoformat()
add('DP34', '/root', 'targeted proof check',
    'Reread the complete integrated proof: preliminary nilpotence, each chain remainder including the endpoint, exceptional wrap, all affine base blocks and induction, primitive equivariance support, both telescoping sums and common sharp witness. This reread follows the earlier full draft read.',
    'PASS including p=2,h=2 and integer-ideal base change; the estimate concerns the displayed dual directions.',
    'research/root_late_check_notes.md:ROOT-DP34-INTEGRATED', now)
add('DP36', '/root', 'targeted proof check',
    'Reread the entire integrated statement and proof, including actual-model character conventions, duplicate-variable quantization, inverse substitution, boundary formal logarithm, unique binomial coefficient extraction, p-scaling, mixed factorial and the specified one-variable n! specialization.',
    'PASS as a sufficient implication under the explicit hypotheses; no claim of optimality, prescribed theta realization or no-shortening theorem.',
    'research/root_late_check_notes.md:ROOT-DP36-INTEGRATED', now)
add('ZINK-LEMMA111', '/root', 'used and rechecked in this run',
    'Read the precise Lemma111 statement and its preceding prorepresentable inverse-limit argument in published section4.2 p230; distinguished a formal torsor section from a bilinear splitting.',
    'PASS: an exact-functor torsor over the stated prorepresentable object has a section. This alone does not trivialize its biextension class.',
    'research/Zink_2002_Display.txt:Lemma111; published section4.2 p230', now)

with path.open('w', newline='') as f:
    writer=csv.DictWriter(f, fields, delimiter='\t')
    writer.writeheader(); writer.writerows(rows)
print(json.dumps({'events':len(rows), 'last_event':rows[-1]['event_id'], 'observed_utc':now}))
