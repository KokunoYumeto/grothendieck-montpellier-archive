"""Tenth substantive review, due after twelve hours; no early use or replay."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,json
R=Path(__file__).resolve().parents[1]
statepath=R/'RUN_STATE.json';state=json.loads(statepath.read_text())
now=datetime.now(timezone.utc);start=datetime.fromisoformat(state['start_utc'])
due=start+timedelta(hours=12)
if now<due:raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed')!=9:raise SystemExit('Requires review09 exactly; no replay.')
previous=json.loads((R/'research/review09_snapshot.json').read_text())
rows=list(csv.DictReader((R/'QUESTIONS.tsv').open(),delimiter='\t'));byid={r['id']:r for r in rows}
base=['Q2bv','Q2bw','Q2bx','Q2by','Q2bz','Q2ca','Q2cb','Q5aj','Q5ak','Q5al','Q5am']
optional=['Q2cc','Q2cd','Q2ce']
for rid in base:assert byid[rid]['state']=='refuted',rid
counted=base+[rid for rid in optional if rid in byid and byid[rid]['state']=='refuted']
assert 'Q5boundary1' not in counted
opened=[r for r in rows if r['state'] in ('active','open','unchecked')]
assert {r['id'] for r in opened}=={'Q2i','Q5i'}
prior_open={r['id']:r for r in previous['open_rows']}
for row in opened:assert row['finding_ids_or_current_gate']!=prior_open[row['id']]['finding_ids_or_current_gate']
integrity=json.loads((R/'research/tex_integrity_review10.json').read_text())
assert integrity['status']=='PASS' and integrity['input_files']>=186
entry=f'\n## Formal movement review10 — {now.isoformat()}\n\n'
entry+=f'Tenth formal review, due {due.isoformat()}, compared substantively with review09 at {previous["date_utc"]}.\n\n'
entry+='''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main questions have strictly smaller proved gates. The following changes are accepted whole-proof results, not merely candidate approaches.

For Q2i, D-HOS17--22 resolves the remaining higher characteristic-three ordinary symplectic source. The symmetric-form orbit estimate, primary-pair restriction and multiplicity-one torus centralizer cover the remaining odd primes. Together with the order-three and projective-involution cases, the resulting source ceilings contradict the factor degree floors. The earlier residual rank interval and restricted inertia types are superseded by full exclusion in the stated ordinary transitive higher-Sp3 scope. Mixed-family and small-rank limits remain explicit.

D-OL09--11 restricts every ordinary selfdual transitive orthogonal factor over q>=3 to natural dimension at most21, and every ordinary even-field transitive factor to natural dimension at most1134. D-OL12--15 further restricts ordinary odd-natural transitive factors over every odd field to natural dimension at most1133. The q>=5 proof uses the exact signed-radical action, allowing moving rank one, and full-O reality/Clifford theory for compatible normalizers. The q3 fixed-fraction quarter estimate is false, and its exact counterexample is retained. The successful q3 proof instead classifies every low-support operator: only actual negative reflections remain. The budget forces exactly twelve such one-factor inertia operators; actual generation then contradicts perfectness on their common nonzero perpendicular. This closes that source endpoint without changing or erasing the failed estimate. Odd-field even-natural ordinary modules and genuine spin modules retain their earlier bounds.

HD-ALT07 replaces the previous support minimum by the exact three-cycle tail fraction on all long shapes. Fomin--Lulov handles the only missing fixed-point-free involutions. The full scalar/outer/tensor and actual multiplier arguments give maxrow/column>((1+sqrt(3/5))/2)n. The explicit(88,12) label atn100 satisfies the stronger previous finite inequality and violates the new one, so the improvement is substantive even before taking a uniform decimal consequence.

For Q5i, SF-E836 proves the opposite-order companion-matrix identities for actual common complete-intersection point defects. Its commuting-triple/Jacobian-socle obstruction covers every such embedding-dimension-at-most-three algebra and coordinate power ideal. SF-E837 then excludes arbitrary formally mixed square thickenings in every positive multiplicity. Its all-size filtered matrix argument uses four distinct pair-monomial annihilators and the omitted-edge conditions; no deformation is base changed to a square quotient.

SF-E838 treats regular quadratic jets and all higher-order perturbations. The actual companion pencil and filtered image dimension force a necessary determinant-zero residual locus; an explicit nonsquare example and the24-dimensional open-family argument prove strict new scope. SF-E839 improves the necessary condition to rank at most four for every leading bracket pencil. Its36five-minors give at most216 polynomial coefficients of degree at most14 per Grassmannian chart. An explicit nonsquare rank-five example has identically zero E838 determinant and no commuting-triple presentation, so it proves another strict reduction. The residual equations are only necessary; no semiregular object or finite action on the residual locus is asserted.

The separate HD-CI-B1/Q5boundary1 integrable scalar-minor counterexample is not counted as movement: by itself it did not change either main gate. Later actual companion-matrix results exclude its source application without invalidating the counterexample. Source searches, finite supplements, status/notation edits, event classification and checkpoint packaging are also not movement.
'''
if 'Q2cc' in counted:
 entry+='''
HD-AST04--06 adds the actual scalar-conductor restriction for standard tensors. The rational tensor-wreath image has trivial scalar intersection, so the scalar coordinate is a character and the actual inducing field is contained in its cyclotomic field. The original quadratic discriminant forces at least two inertia phases of specified orders. Rational eigenspace multiplicities, and a separate fourth-root trace calculation, exclude standard tensors throughn19 for every non-Eisenstein field, throughn20 when8divides the discriminant, and throughn=5(p-1) for odd conductor primesp>=7. The class-number-one standard lower cutoffs are20,21,31,51,91,211,331,811 in the displayed field order. This is an actual-field inclusion argument; the original and inducing fields are not identified.
'''
if 'Q2cd' in counted:
 entry+='\nThe separately reviewed tail-two tensor restriction is also counted, with its exact current row: '+byid['Q2cd']['finding_ids_or_current_gate']+'\n'
if 'Q2ce' in counted:
 entry+='''
HD-ALT08 extends the conductor argument to every remaining long ordinary Specht label. Its exact necessary inequality is beta<=1/(5h)+3/(5e), withh4 for discriminant divisible by8 andh=p-1 for an odd discriminant primep>=5. The full universal finite-degree argument gives maxrow/column>(1+sqrt(1-4/(5h)))n/2. ForQ(sqrt(-2)) the fraction exceeds0.9472135954; the other six non-Gaussian/non-Eisenstein class-number-one fields have still stronger thresholds. The(94,6) label atn100 passes ALT07 but fails this inequality, independently of standard or tail-two tensor exclusions. The Gaussian shape gate remains its earlier one.
'''
entry+='\n### Counted new rows\n\n'+', '.join(counted)+'. Pending drafts with no integrated row are excluded.\n'
entry+='\n### Every open row at this review\n\n| Row | State | Strongest proved reduction and remaining gate |\n|---|---|---|\n'
for row in opened:entry+=f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
entry+='''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** the polarization, published rank4 dominance, explicit integral detector and quadratic division constants remain complete.
- **Target2, class-number-one sixfolds with every determinant:** all split families, all Eisenstein determinants and Gaussian determinant class3 have numerical effective bounds. Other nonsplit determinants remain open. The candidate suppliers must satisfy the strictly smaller group/shape gates above, the remaining exceptional inducing profiles, actual original-field descent, rank9 and effective integral-cycle requirements. A necessary representation profile is not a missing detector.
- **Target3, Eisenstein split eightfolds through G34:** the published-input reconstruction, exact rank16, integral cycle suppliers, transfer and effective polarization/order constants remain complete. No unrefereed Severn dominance theorem is used as a new premise.
- **Target4, natural imprimitive sources:** the exact signature criterion, all-family nondominance and sharpn5 maxima15/14 remain proved. The exact Nielsen-rank procedure terminates for a specified component; the unbounded table has not been executed.
- **Target5, actual perfect complexes:** the n3 construction and coherent numerical variant remain complete. The genuine balanced-RM n4 seed remains open. Every semistable torsion-free candidate is already excluded in the stated finite-action scope. The new common-Artin CI and quadratic-jet restrictions remove additional nonpure candidates. Unstable sheaves, other nonreduced defect modules, quadratic pencils of rank at most four, higher initial degrees, other positive-dimensional defects and broader overlapping derived constructions remain to be treated.

Every accepted new proof has a complete written-proof reading and its recorded independent mathematical/source audit. Finite supplements remain distinct from universal arguments. Milne's conductor source is identified as author course notes, with the invoked complete passages read; no fresh full reconstruction of upstream global class-field reciprocity or existence is claimed. Markman, Severn and032 remain conditional wherever used. Source integrity is not TeX compilation.

Continue on both reduced main gates. The stopping rule is not triggered. The next formal review is due2026-11-21T23:38:55+00:00.
'''
entry+=f'\nThe included {integrity["input_files"]}-file TeX source graph passes all recorded source-integrity checks.\n'
with (R/'LEDGER.md').open('a') as f:f.write(entry)
snapshot={'review':10,'date_utc':now.isoformat(),'compared_with_review':9,'movement':True,
          'counted_rows':counted,'explicitly_not_counted':['Q5boundary1'],'open_rows':opened,'consecutive_no_movement':0}
(R/'research/review10_snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
state.update(last_review=now.isoformat(),formal_reviews_completed=10,consecutive_reviews_without_movement=0,
             next_review_utc=(start+timedelta(hours=13)).isoformat())
statepath.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({k:v for k,v in snapshot.items() if k!='open_rows'}))
