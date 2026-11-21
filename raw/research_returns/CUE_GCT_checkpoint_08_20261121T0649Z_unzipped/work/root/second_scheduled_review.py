#!/usr/bin/env python3
"""Record review2 at or after its actual hourly slot, with every question row."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv
import hashlib
import json

base=Path(__file__).resolve().parents[2]
history_path=base/'work/review_history.json'
history=json.loads(history_path.read_text())
assert len(history)==1, 'Refusing to duplicate or skip the second actual review'
due=datetime.fromisoformat(history[-1]['next_review_due_utc'])
now=datetime.now(timezone.utc)
if now<due:
    raise SystemExit('Review2 is not due until '+due.isoformat())
previous=json.loads((base/'work/review_01_snapshot.json').read_text())
questions_path=base/'deliverables/QUESTIONS.tsv'
with questions_path.open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
old={row['id']:row for row in previous['all_rows']}
changed=[row['id'] for row in rows if row['id'] in old and row!=old[row['id']]]
new=[row['id'] for row in rows if row['id'] not in old]
assert 'RQ-27' in changed
gates=[
('Q1 Rectangular bridge','MOVEMENT: existing open row RQ27 now has exact vanishing at17/18 and a uniform linear bound thereafter; RQ26 improves the dimension gate and eventual rectangular threshold.','R26 gives0≤epsilon_m≤6(m−18), m≥18, and n²≤2(m−1)²+53 is dimension-certified. Exact four-row rectangular range m<n<4m/3 holds for everym≥14. Uniform epsilon_m=0 for m≥19 needs six additional normal directions; general ambient/growing-parameter positive extraction and superlinear padding remain open.'),
('Q2 Haar integrals and orbit boundaries','NO independent main-gate movement counted. G19 identifies a specified rectangular discriminant copy and exact energies, but does not compare total multiplicities or survive positive padding.','Uniformly control Schur-isotypic Gram ranks and orbit-boundary ideals with polynomial resources. R21 fixed-ambient computation and G17/G18 direction comparisons remain the strongest general reductions in this run.'),
('Q3 Isolation and matrix invariants','Specified subclass improved: I36 gives five pairs for singular-factor width3; I37 gives two pairs for its affine subclass. These do not independently count as solving or reducing the growing-width main gate.','General unknown-order fixed-width construction I31 remains. The growing-width target still requires polynomial total sample size and construction cost. For the two-pair width3 subproblem, mixed variable-dependent rank2/rank3 affine transitions and nonlinear singular factors remain; I35 common-seed boundary synchronization remains open.'),
('Q4 Purity and arithmetic','NO independent main-gate movement counted. P13 inherits smaller arithmetic exponents in the newly proved subclasses; P16 refutes removal of the common center on its specified nodes.','A uniformly efficient kernel-avoiding arithmetic or purity family for growing width remains open. No new RH consequence or polynomial-in-width construction has been inferred.'),
('Q5 Zero statistics','UNCHANGED: the source-specific audit remains complete under the stipulated theorem convention.','Unrestricted correlation/support, the general moment recipe, and automorphic hypotheses beyond Dirichlet/Hecke GRH remain additional statements; no new analytic claim is made.'),
('Q6 Grothendieck transport','Updated dictionaries accompany every new checked result; packaging and exposition are not counted as movement.','Original cote133 images and the exact missing Masullo1.2 numbered primary locator remain unavailable. Mathematical transcription corrections are not visual ink verification.')]
snapshot={
    'review_index':2,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),
    'run_id':'CUE_GCT_20261121_R1','who':'GPT-6 Astra Pro; root; effort not exposed',
    'baseline':'Actual review1 at '+previous['actual_utc'],
    'movement':True,'consecutive_reviews_without_movement':0,
    'movement_basis':'RQ27 changes from an undetermined graded Tor defect, controlled asymptotically only by the earlier O(m^(3/2)) image bound, to exact zeros17/18 plus the uniform bound6(m−18); R26 narrows the main four-variable transition to constant width and proves the eventual rectangular range fromm14. New side rows and packaging are not counted independently.',
    'questions_sha256':hashlib.sha256(questions_path.read_bytes()).hexdigest(),
    'question_count':len(rows),'all_rows':rows,'changed_existing_rows':changed,
    'new_rows_since_previous_review':new,'main_questions':gates,
    'next_review_due_utc':(due+timedelta(hours=1)).isoformat()}
(base/'work/review_02_snapshot.json').write_text(json.dumps(snapshot,indent=2,ensure_ascii=False)+'\n')
history.append({k:v for k,v in snapshot.items() if k not in ['all_rows','main_questions']})
history_path.write_text(json.dumps(history,indent=2,ensure_ascii=False)+'\n')
def cell(s):
    return str(s).replace('|','\\|').replace('\n',' ')
with (base/'deliverables/LEDGER.md').open('a') as f:
    f.write('\n\n## Second scheduled movement review — '+now.isoformat()+'\n\n')
    f.write('The hourly review was due at '+due.isoformat()+' and actually performed at the timestamp above. The comparison baseline is review1. **Movement: YES. Consecutive reviews without movement: 0.** The stopping condition has not been reached. The next actual review is due at '+snapshot['next_review_due_utc']+'.\n\n')
    f.write(snapshot['movement_basis']+'\n\n')
    f.write('| Main question | Status and movement | Strongest remaining gate |\n|---|---|---|\n')
    for row in gates:
        f.write('| '+' | '.join(map(cell,row))+' |\n')
    f.write('\n### Complete row-by-row status at this review\n\n')
    f.write('Every row is reproduced. Newly treated subclasses are distinguished from changes to previously open main gates. Existing changed rows: '+', '.join(changed)+'.\n\n')
    f.write('| ID | Question | State | Finding or current gate |\n|---|---|---|---|\n')
    for row in rows:
        f.write('| '+' | '.join(cell(row[key]) for key in ['id','question','state','finding_or_current_gate'])+' |\n')
    f.write('\n### Next attacks selected\n\n')
    f.write('The permanent route now perturbs the four endpoint forms of the Jacobi pencil to recover its six missing normal directions. A candidate first-order map from the seven-dimensional kernel to the cokernel must retain exactly the one genuine scaling relation. The isolation route investigates passive-state propagation across variable-dependent invertible stretches in mixed rank2/rank3 words, using the pole-extracted derivative identities. Purity works on the matching rational-evaluation ideal. These are active targets, not asserted theorems.\n')
print(json.dumps({k:v for k,v in snapshot.items() if k not in ['all_rows','main_questions']},ensure_ascii=False))
