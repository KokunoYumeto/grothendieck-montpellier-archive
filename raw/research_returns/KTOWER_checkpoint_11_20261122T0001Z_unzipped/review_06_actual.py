"""Record review06 only when root invokes it after actual review at the due time."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json

B=Path(__file__).resolve().parent
due=datetime.fromisoformat('2026-11-21T23:30:46+00:00')
now=datetime.now(timezone.utc)
assert now>=due, 'Review is not yet due'
p=B/'PROGRESS_REVIEWS.json'
data=json.loads(p.read_text())
assert len(data['reviews'])==5
previous=data['reviews'][-1]
old={r['id']:r for r in previous['all_question_rows']}
with (B/'QUESTIONS.tsv').open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
closed=[r['id'] for r in rows if r['id'] in old and old[r['id']]['state'].startswith('OPEN') and not r['state'].startswith('OPEN')]
assert closed==[],closed
opened=[r for r in rows if r['state'].startswith('OPEN')]
assert {r['id'] for r in opened}=={'KT-Q1B','KT-Q1C','KT-Q5','KT-Q7'}
streak=previous['consecutive_reviews_without_movement']+1
review={
    'number':6,'scheduled_utc':due.isoformat(),'observed_utc':now.isoformat(),
    'reviewer':'/root; GPT-6 Astra Pro; effort setting not exposed',
    'movement':False,
    'movement_basis':'No previously open row closes and no original main arithmetic or geometric gate has been proved strictly smaller since actual review05.',
    'closed_rows':closed,'strictly_smaller_conditional_gates':[],
    'excluded_from_movement':[
        'Order-five unit-norm/capitulation criterion without evaluation and abstract unbounded norm system',
        'p-divisible-weight exponent observation leaving the same possible order-p ideal-class component',
        'Saturated Rankin–Cohen operator limitation and class-pairing parity scope',
        'Multi-generator conormal inequality with unverified stronger congruence comparison',
        'BK normalization repair and displayed block-sign proof gap; source audit does not eliminate original strict Selmer classes',
        'Real-multiplication theta-preservation limitation without an all-odd-order cover conclusion',
        'Tame Frobenius ramification reformulation compatible with every surviving primitive order-five label',
        'Source retrieval, exact control reformulations still under review, layout and packaging'
    ],
    'consecutive_reviews_without_movement':streak,
    'main_all_weight_status':'OPEN: rational orders5 or >=7 remain. Order5 has at most one order-p ideal-class component and cyclic strict/K groups with exponent not known in general. Simultaneous source-compatible auxiliary units and nonessential stable rank3 exclusion remain unproved.',
    'all_question_rows':rows,'open_question_rows':opened,
    'decision':'Continue for the next review interval. This is the first consecutive no-movement review after review05. Stop research after review07 if it is also without movement, even if untried approaches remain.',
    'next_review_due_utc':'2026-11-22T00:30:46Z'
}
assert streak==1
data['reviews'].append(review)
p.write_text(json.dumps(data,indent=2)+'\n')
with (B/'LEDGER.md').open('a') as f:
    f.write('\n\n## Progress review06 — '+now.isoformat()+'\n\nMovement: NO. No old-open row changed status and no original main gate became strictly smaller after review05. Exact unit-norm and ramification reformulations, comparison/source corrections, operator and pairing limitations, and layout/packaging are not counted. Consecutive reviews without movement:1.\n\n| Open row | State | Strongest current gate |\n|---|---|---|\n')
    for r in opened:
        f.write('| '+' | '.join(r[k].replace('|','/') for k in ['id','state','current_gate_or_scope'])+' |\n')
    f.write('\nAll question rows are frozen in PROGRESS_REVIEWS.json. Next actual review:00:30:46UTC on22November2026. If that review also has no movement, the user’s stop rule takes precedence over untried approaches, and research stops for final packaging.\n')
cpath=B/'CHECKPOINTS.json';c=json.loads(cpath.read_text())
c['next_review_due_utc']='2026-11-22T00:30:46Z'
cpath.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps({'review':6,'observed_utc':now.isoformat(),'movement':False,'nonmovement_streak':streak,'next_review':review['next_review_due_utc']}))
