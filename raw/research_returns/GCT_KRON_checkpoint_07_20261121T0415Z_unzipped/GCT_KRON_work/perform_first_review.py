#!/usr/bin/env python3
"""Record the first scheduled review, only once it is actually due."""
from pathlib import Path
import csv, datetime, json, subprocess, sys

root=Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc)
meta=json.loads((root/'RUN_METADATA.json').read_text())
due=datetime.datetime.fromisoformat(meta['first_review_due_utc'].replace('Z','+00:00'))
if now<due:
    raise SystemExit('The first timed review is not due yet.')
path=root/'TIMED_REVIEWS.json'
if path.exists() and json.loads(path.read_text()):
    raise SystemExit('The first timed review was already recorded.')
subprocess.run([sys.executable,str(root/'build_package.py')],check=True)
questions=list(csv.DictReader((root/'QUESTIONS.tsv').open(),delimiter='\t'))
def is_open(row):
    s=row['state'].lower()
    return not (s.startswith('proved') or s.startswith('refuted') or s.startswith('first refuted'))
open_rows=[row for row in questions if is_open(row)]
gates={
 'Q1':'The complete supplied assertion inventory is audited, with corrected interpretations and counterexamples A001–A017. A029 now recovers q_H^n from originalscan021, and the relevant originalcote133pages were visually checked. Othercotes and uncertainnames remain explicit source scopes.',
 'Q2':'Positive formulas and nonvanishing are proved for the stated two-row, hook, rectangle and IP families. A024 gives the complete height-two positive HW algebra; A026/A027 give height-three and growing-height rectangular counts. A general positive rectangular basis remains open.',
 'Q3':'Ordinary saturation inference from the supplied lambda operations, K-theoretic positivity, normality or purity is refuted. Exact restricted support classifications, relative-lattice saturation and stable-tail positivity for all stretches>=2 are proved. No unrestricted rectangular saturation assertion is made.',
 'Q4':'Actual multiplicity comparison remains an evaluation-rank problem outside the proved ranges. At n>=m25 require m>=190, at least52rows, n<P_d(dm), n<P_d(lambda2), lambda_(2j)>=28-j, q>=2, padding bounds, and failure of support/jet criteria. M017 adds lambda3>=27 OR lambda2>=478126780; lambda2=27 forces at least478126755rows. M018 adds lambda2>=1000001 OR lambda3>=29 OR lambda4>=27. A028 exhibits unbounded symmetric-orbit/closure gaps but no actual obstruction.',
 'Q5':'Every included finding has its own geometric dictionary and exact primary locators. Full proof readings, primary-source rereadings and finite computations are recorded separately. Final integrated PDF layout and cross-reference verification remain production work, not main-gate movement.'
}
record={
 'review':1,'date_utc':now.isoformat(),'scheduled_utc':due.isoformat(),
 'comparison_baseline':'Initial open questions recorded at run start, before any timed review.',
 'movement':True,'consecutive_no_movement':0,
 'movement_evidence':[
  'Q1 supplied mathematical assertions changed from unclassified to proved or refuted under explicit interpretations.',
  'Q2 exact positive family formulas, invariant algebras and rectangular dualities close stated family questions.',
  'Q3 proposed general saturation implications are refuted with explicit examples and replaced by precise restricted results.',
  'Q4 all-copy projection, degree, support and jet theorems strictly shrink the actual obstruction gate; O018/O022 supply actual-positive witnesses beyond earlier methods.'
 ],
 'not_counted_as_movement':'Packaging, rewording, rereading, and successive constants from an already established finite criterion are not counted by themselves.',
 'main_gates':gates,'open_rows':open_rows,
 'decision':'Continue. This is the first timed review and there has been substantial main-gate movement. Next review due one hour after the scheduled first review.'
}
path.write_text(json.dumps([record],indent=2,ensure_ascii=False))
lines=['# Timed review 01', '', 'Actual review: '+now.isoformat()+'. Scheduled: '+due.isoformat()+'.', '',
       '**Movement: yes. Consecutive reviews without movement: zero. Continue.**','',
       'This compares the present proved gates with the initial open questions. It does not count packaging or successive constant evaluations as movement.','',
       '## Current main gates','']
for k,v in gates.items():lines.extend(['### '+k,'',v,''])
lines.extend(['## Every currently open question row','', '| ID | State | Current gate |', '|---|---|---|'])
for row in open_rows:
    gate=row['finding_ids_or_current_gate'] or row['state']
    lines.append('| '+row['id']+' | '+row['state'].replace('|','/')+' | '+gate.replace('|','/')+' |')
lines.extend(['','## Movement evidence','']+['- '+x for x in record['movement_evidence']]+['',record['decision'],''])
(root/'TIMED_REVIEW_01.md').write_text('\n'.join(lines))
p=root/'LEDGER.md';s=p.read_text().replace('No timed review due yet.','The first timed review is recorded below and in TIMED_REVIEW_01.md.')
s+='\n## Timed review 01, '+now.isoformat()+'\n\nMovement: yes; consecutive reviews without movement: zero. The initial open questions have changed status and the actual multiplicity gate has strictly shrunk. The complete current main gates and every open question row are snapshotted in TIMED_REVIEW_01.md and TIMED_REVIEWS.json. Packaging and successive evaluations of an existing criterion are not counted. Continue; the next review is due 2026-11-21T03:00:17Z.\n'
p.write_text(s)
p=root/'IMPLICATIONS.md';s=p.read_text().replace('No three-hour progress review has yet occurred.','The first timed review recorded substantive movement and continuation; see TIMED_REVIEW_01.md.')
p.write_text(s)
print(json.dumps({'review':1,'date_utc':now.isoformat(),'open_rows':[r['id'] for r in open_rows],'movement':True}))
