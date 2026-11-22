#!/usr/bin/env python3
"""Retain root's explicit eight-row supplement to the metadata audit."""
from pathlib import Path
import csv, datetime, json, time
root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
specs = [
    ('agents/cycles/partial_fourier_CHECK_EVENTS.tsv', 8, 'C.4ab', True),
    ('agents/cycles/partial_fourier_CHECK_EVENTS.tsv', 9, 'C.4ab', True),
] + [('notes/ROOT_POST_REVIEW2_CHECK_EVENTS.tsv', line, statement, False)
     for line, statement in zip(range(33,39), ['C.3ao','C.3al','C.3am','C.3an','C.3ap','C.3aq'])]
fields = ['path','line','statement_id','date','who_original','type_original',
          'recommended_action','recommended_category','rationale','outcome_original']
rows = []
for path,line,statement,receipt in specs:
    with (root/path).open(newline='') as f:
        original = list(csv.reader(f,delimiter='\t'))[line-1]
    sid,date,who,kind,outcome = original
    assert sid == statement
    if receipt:
        assert 'received' in kind
        action = 'retain in auxiliary administrative/access log'
        category = 'no mathematical canonical category assigned'
        reason = 'Receipt of a separately retained reviewer event; not an additional independent proof.'
    else:
        assert 'reconstruction' in kind and ('reread' in outcome or 'entire' in outcome)
        action = 'canonicalize actual renewed mathematical reread'
        category = 'targeted proof check'
        reason = 'Actual entire-proof reread explicitly recorded; preserve distinction from reconstruction alone and from new mathematical movement.'
    rows.append(dict(zip(fields,[path,line,sid,date,who,kind,action,category,reason,outcome])))
with (root/'notes/ROOT_EVENT_METADATA_OVERRIDES.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'rows':len(rows),'auxiliary_receipts':2,'actual_mathematical_rereads':6,
        'runtime_seconds':time.perf_counter()-start,
        'scope':'Exact root-reviewed metadata supplement only; original source logs unchanged.'}
(root/'logs/root_event_metadata_overrides.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
