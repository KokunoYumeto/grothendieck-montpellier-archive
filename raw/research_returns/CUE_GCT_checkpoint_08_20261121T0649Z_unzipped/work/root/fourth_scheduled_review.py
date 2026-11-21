"""Record review four only after its actual due time, with all live rows."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,hashlib,json
B=Path(__file__).resolve().parents[2]
hp=B/'work/review_history.json';history=json.loads(hp.read_text())
assert len(history)==3,'Refusing duplicate or skipped review'
due=datetime.fromisoformat(history[-1]['next_review_due_utc'])
now=datetime.now(timezone.utc);assert now>=due,'Fourth review not yet due'
previous=json.loads((B/'work/review_03_snapshot.json').read_text())
qp=B/'deliverables/QUESTIONS.tsv'
with qp.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
old={x['id']:x for x in previous['all_rows']}
changed=[x['id'] for x in rows if x['id'] in old and x!=old[x['id']]]
new=[x['id'] for x in rows if x['id'] not in old]
assert 'G-Q26' in changed and 'G-Q27' in changed
gates=[
 ('Q1 Rectangular bridge','MOVEMENT: existing GQ26/GQ27 extend strict stable no-scaling and exact comparisons from r≤m to r≤2m. G26–28 close the nonrectangular boundary gate through2m, with a larger boundary-only range.','For m≥17 every fixed full-row direction throughm rows and every fixed nonrectangular direction through2m rows has an exact eventual sign. Boundary comparison holds for nonrectangles at m<r≤min(2n−2,m²). Remaining: rectangles beyondm rows, strict directions beyond2m, finite earlier degrees, changing directions, and efficient general coefficient extraction. R34 is a separately checked standalone construction awaiting manuscript integration; it is not counted in this review.'),
 ('Q2 Haar integrals and orbit boundaries','The new stable-quotient and generic-stabilizer arguments resolve additional exact orbit-boundary comparisons; this is the same movement counted underQ1.','Efficient positive/combinatorial realization of the general isotypic Gram ranks or quotient numerator remains open. No polynomial-time general plethysm/Kronecker coefficient algorithm follows from the explicit large thresholds.'),
 ('Q3 Isolation and matrix invariants','I41–I44 close successive actual-connector gates and the balanced theorem through12 variables/all characteristics and13 away from2. These do not independently count as polynomial-in-growing-width PIT movement.','I31 remains the arbitrary fixed-width construction. General jointly polynomial dependence on growing width, length and degree and the shared-seed coefficient-matroid bridge remain open. At width3, the next completed-manuscript gates are weight5 in characteristic2 and longer two-anchor connectors with at least3 positions of both internal types. New residue-Hessian work is standalone and not counted.'),
 ('Q4 Purity and arithmetic','P19 closes the previously open arbitrary-length cubic balanced-ideal gate in every characteristic; P18 is its checked support reduction.','Every remaining balanced width3 annihilator has homogeneous degrees4 throughn−4, with the stated I44 finite-variable exclusions. General-width kernel avoidance, the purity-to-ROABP construction and efficient arithmetic nonvanishing remain open. P20 is standalone and awaits the root full-proof reading; it is not counted.'),
 ('Q5 Zero statistics','UNCHANGED under the stipulated RH/Dirichlet-GRH theorem convention; no new analytic claim.','Full support/correlation, the arithmetic moment recipe and automorphic RH beyond the specified Dirichlet/Hecke hypotheses retain their source-specific gates. Masullo dependencies remain conditional.'),
 ('Q6 Grothendieck transport','All findings through R33/G28/I44/P19 in the compiled manuscript have geometric dictionaries and exact source locators. Exposition and packaging are not movement.','Original cote133 scans and an exact numbered primary locator for Masullo1.2 remain unavailable. The transcription conclusions concern mathematical necessity, not ink-level verification.')]
basis=('Existing GQ26/GQ27 advance from strict directions throughm rows to common stable no-scaling points and exact every-integer comparisons through2m rows, via R29/R30/G25. The main first-row boundary gate is then strictly reduced by G26–28: all fixed directions throughm rows and all nonrectangular directions through2m rows are classified eventually, with a larger on/below-face range. R33 supplies a genuine generic-stabilizer upper bound rather than assuming stability. P19 additionally closes the arbitrary-length cubic target that was open at review3. New row creation, later standalone candidates, packaging, and finite-variable isolation subclasses are not counted independently as solving the growing-width gate.')
snap={'review_index':4,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),
 'run_id':'CUE_GCT_20261121_R1','who':'GPT-6 Astra Pro; root; effort not exposed',
 'baseline':'Actual review3 at '+previous['actual_utc'],'movement':True,
 'consecutive_reviews_without_movement':0,'movement_basis':basis,
 'questions_sha256':hashlib.sha256(qp.read_bytes()).hexdigest(),'question_count':len(rows),
 'all_rows':rows,'changed_existing_rows':changed,'new_rows_since_previous_review':new,
 'main_questions':gates,'next_review_due_utc':(due+timedelta(hours=1)).isoformat()}
(B/'work/review_04_snapshot.json').write_text(json.dumps(snap,indent=2,ensure_ascii=False)+'\n')
history.append({k:v for k,v in snap.items() if k not in ['all_rows','main_questions']})
hp.write_text(json.dumps(history,indent=2,ensure_ascii=False)+'\n')
def cell(x):return str(x).replace('|','\\|').replace('\n',' ')
with (B/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n\n## Fourth scheduled movement review — '+now.isoformat()+'\n\n')
 f.write('Due '+due.isoformat()+'. Actually performed at the timestamp above after reviewing every live row and main gate. **Movement: YES. Consecutive reviews without movement: 0.** The stopping condition has not been reached. Next review due '+snap['next_review_due_utc']+'.\n\n'+basis+'\n\n')
 f.write('| Main question | Status and movement | Strongest remaining gate |\n|---|---|---|\n')
 for row in gates:f.write('| '+' | '.join(map(cell,row))+' |\n')
 f.write('\n### Complete row-by-row status\n\nEvery current row follows, including open, conditional and source-gated rows. Existing changed rows: '+', '.join(changed)+'.\n\n')
 f.write('| ID | Question | State | Finding or current gate |\n|---|---|---|---|\n')
 for row in rows:f.write('| '+' | '.join(cell(row[k]) for k in ['id','question','state','finding_or_current_gate'])+' |\n')
 f.write('\n### Next attacks selected\n\nIntegrate and transport the independently checked progression-free Weyl-pencil construction R34, then use its superlinear row range in the exact quotient comparison. Check the primary additive-combinatorial strengthening before using it. Complete the root reading of P20. Independently check the new actual-Hessian residue argument and longer chain connectors without promoting abstract quadratic identities to fixed polynomial counterexamples. Continue the separate rectangular scalar-period and general coefficient-synchronization gates.\n')
print(json.dumps({k:v for k,v in snap.items() if k not in ['all_rows','main_questions']},ensure_ascii=False))
