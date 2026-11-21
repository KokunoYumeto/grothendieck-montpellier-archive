#!/usr/bin/env python3
"""Record the third actual review, with the complete dated row snapshot."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, hashlib, json

base=Path(__file__).resolve().parents[2]
hp=base/'work/review_history.json'
history=json.loads(hp.read_text())
assert len(history)==2, 'Refusing duplicate or skipped review'
due=datetime.fromisoformat(history[-1]['next_review_due_utc'])
now=datetime.now(timezone.utc)
assert now>=due, 'Third review is not yet due'
previous=json.loads((base/'work/review_02_snapshot.json').read_text())
qp=base/'deliverables/QUESTIONS.tsv'
with qp.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
old={x['id']:x for x in previous['all_rows']}
changed=[x['id'] for x in rows if x['id'] in old and x!=old[x['id']]]
new=[x['id'] for x in rows if x['id'] not in old]
assert 'RQ-27' in changed and 'G-Q20' in changed
gates=[
('Q1 Rectangular bridge','MOVEMENT: RQ26–30 and GQ20 change; R27 closes the previously undetermined four-variable dimension defect. G21–24 and R28 extend exact dimensions, strict-direction signs and the rectangular boundary comparison through m rows.','The exact strict-direction exponent is r m²−(r−2)n²−2m+r−1 for m≥17,4≤r≤m; it never vanishes. The eventual rectangular range is exactly m<n<r m/(r−1). Remaining: more rows, nonrectangular first-row equality faces, finite-degree and changing-direction comparisons, and polynomial-size extraction of general rectangular Kronecker/plethysm coefficients. R29 is still a candidate and is not counted.'),
('Q2 Haar integrals and orbit boundaries','The dimension and quotient arguments reduce specified orbit-boundary comparisons; no independent efficient positive-formula breakthrough is claimed.','Uniform polynomial-resource control of the actual Schur-isotypic Gram ranks and boundary ideals remains open. R21 is the fixed-ambient computation bound; R27/G23 decide specified eventual comparisons without providing the general positive count.'),
('Q3 Isolation and matrix invariants','I38 and I40 close additional mixed-rank and n≤9 balanced width-three subclasses. These are not independently counted as reducing the growing-width main gate.','I31 remains the arbitrary fixed-width construction. Polynomial dependence jointly on growing width, length and degree, or an equivalent explicit coefficient-matroid cone/joint-span construction, remains open. Shared-seed synchronization in I35 remains open; the unrestricted width-three two-pair problem remains open. I41 is a candidate, not a result at this review.'),
('Q4 Purity and arithmetic','P17 gives checked balanced-ideal restrictions and I40 closes its n9 residual; P13 transports the proved sampler budgets. No general-width movement is counted.','Explicit kernel avoidance with polynomial resources for growing-width tensor-train varieties remains the main gate. The purity-to-ROABP encoding and the efficient common arithmetic nonvanishing point are not constructed. Cubic balanced-ideal bounds at arbitrary length remain an active narrower target.'),
('Q5 Zero statistics','UNCHANGED under the task\'s stipulated theorem convention; the source-specific audit remains complete.','Unrestricted support/correlation, the general arithmetic moment recipe, and the specific automorphic hypotheses beyond Dirichlet/Hecke GRH remain additional statements. No further analytic theorem has been inferred.'),
('Q6 Grothendieck transport','New checked findings have explicit geometric dictionaries; exposition and packaging are not counted as movement.','Original cote133 scan images and an exact numbered primary locator for the draft\'s Masullo1.2 claim remain unavailable. Mathematical corrections to the supplied transcription are not an ink-level verification.')]
basis=('Existing RQ27 changes from exact zeros only at17/18 and the bound epsilon_m≤6(m−18) to exact zero for everym≥17, by the fully checked R27 uniform endpoint repair. Existing GQ20 consequently has an exact eventual sign in every strict four-row direction. R28/G21–24 then prove exact higher-row dimensions, all-integer strict-direction comparison and the rectangular equality-boundary comparison throughm rows. Restricted isolation/purity subclasses, new row creation, and packaging are not counted independently as growing-width main-gate movement.')
snap={'review_index':3,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),
 'run_id':'CUE_GCT_20261121_R1','who':'GPT-6 Astra Pro; root; effort not exposed',
 'baseline':'Actual review2 at '+previous['actual_utc'],'movement':True,
 'consecutive_reviews_without_movement':0,'movement_basis':basis,
 'questions_sha256':hashlib.sha256(qp.read_bytes()).hexdigest(),'question_count':len(rows),
 'all_rows':rows,'changed_existing_rows':changed,'new_rows_since_previous_review':new,
 'main_questions':gates,'next_review_due_utc':(due+timedelta(hours=1)).isoformat()}
(base/'work/review_03_snapshot.json').write_text(json.dumps(snap,indent=2,ensure_ascii=False)+'\n')
history.append({k:v for k,v in snap.items() if k not in ['all_rows','main_questions']})
hp.write_text(json.dumps(history,indent=2,ensure_ascii=False)+'\n')
def cell(x):return str(x).replace('|','\\|').replace('\n',' ')
with (base/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n\n## Third scheduled movement review — '+now.isoformat()+'\n\n')
 f.write('Due '+due.isoformat()+'. Actually performed at the timestamp above, after the complete row and main-gate review. **Movement: YES. Consecutive reviews without movement: 0.** The stopping condition has not been reached. Next review due '+snap['next_review_due_utc']+'.\n\n'+basis+'\n\n')
 f.write('| Main question | Status and movement | Strongest remaining gate |\n|---|---|---|\n')
 for row in gates:f.write('| '+' | '.join(map(cell,row))+' |\n')
 f.write('\n### Complete row-by-row status\n\nEvery current row is reproduced, including every open, partially resolved, source-gated and conditional row. Existing changed rows: '+', '.join(changed)+'.\n\n')
 f.write('| ID | Question | State | Finding or current gate |\n|---|---|---|---|\n')
 for row in rows:f.write('| '+' | '.join(cell(row[k]) for k in ['id','question','state','finding_or_current_gate'])+' |\n')
 f.write('\n### Next attacks selected\n\nComplete the independent proof checks of R29\'s prescribed-spectrum two-product construction, which may extend strict stable directions to2m−2 rows. Check the weight-two width-three connector proof I41, without promoting a finite-variable result to a growing-width sampler. Continue the arbitrary-length cubic balanced-ideal cut analysis. General efficient Gram extraction and coefficient-matroid synchronization remain the main unsolved targets.\n')
print(json.dumps({k:v for k,v in snap.items() if k not in ['all_rows','main_questions']},ensure_ascii=False))
