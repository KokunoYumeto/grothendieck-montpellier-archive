"""Ninth substantive review; guarded against early execution and replay."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,json
R=Path(__file__).resolve().parents[1]
sp=R/'RUN_STATE.json';state=json.loads(sp.read_text())
now=datetime.now(timezone.utc);start=datetime.fromisoformat(state['start_utc'])
due=start+timedelta(hours=11)
if now<due:raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed')!=8:raise SystemExit('Requires review08 exactly; no replay.')
previous=json.loads((R/'research/review08_snapshot.json').read_text())
rows=list(csv.DictReader((R/'QUESTIONS.tsv').open(),delimiter='\t'));byid={r['id']:r for r in rows}
counted=['Q2bn','Q2bo','Q2bp','Q2br','Q2bq','Q2bs','Q2bt','Q2bu','Q5ab','Q5ac','Q5ad','Q5ae','Q5af','Q5ag','Q5ah','Q5ai']
for rid in counted:assert byid[rid]['state']=='refuted',rid
opened=[r for r in rows if r['state'] in ('active','open','unchecked')]
assert {r['id'] for r in opened}=={'Q2i','Q5i'}
prior_open={r['id']:r for r in previous['open_rows']}
for row in opened:assert row['finding_ids_or_current_gate']!=prior_open[row['id']]['finding_ids_or_current_gate']
integrity=json.loads((R/'research/tex_integrity_review09.json').read_text())
assert integrity['status']=='PASS' and integrity['input_files']>=171
entry=f'\n## Formal movement review09 — {now.isoformat()}\n\n'
entry+=f'Ninth formal review, due {due.isoformat()}, compared substantively with review08 at {previous["date_utc"]}.\n\n'
entry+='''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main questions have strictly smaller proved gates.

For Q2i, D-HOS07--12 excludes the higher q5 symplectic factors and the selfdual higher q3 factors, in their explicitly stated mixed-factor and normalizer scopes. D-HOS13--16 closes the unbounded rank of the nonselfdual q3 case. The elementary order-three support estimate is 2/9; the complete remaining prime-order reduction and published LST restricted-mu2-support estimate give the explicit residual interval 4<=n<=283. The coarse n<10^30 result and its sharper refinement are not counted as two solutions to the main question. The incompatible diagonal outer class, tensor cycles, actual intermediate-cover branch budget and original-field interfaces are all retained.

D-OL01--08 first gives an effective degree/level reduction, then proves full-O extension and selfduality in the required low-level range, and finally proves a full compatible-normalizer support bound7/64 for every O-extendible ordinary character over the nine remaining small fields at natural dimension at least22. The actual nontrivial form multiplier forces total degree at most64, below the factor-degree floor. Thus the former unbounded orthogonal natural-dimension gate is closed, with all transitive orthogonal factors restricted to d<=4*10^30-3. These are finite simple-factor parameter ranges; no enumeration of all tensor multiplicities, scalar extensions or actual sources is claimed. HD-ALT06a/b separately tightens the ordinary alternating shape gate from row/column>6n/7 to row/column>87n/100, with the exact quantitative tail inequality and all small endpoints checked. Long-shape alternating tensors still remain.

For Q5i, SF-E828 removes the equal-hull-Chern-class exception in the precise two-slope architecture. SF-E829--831 replace coarse opposite-Ext assumptions with geometric surface supports, then actual extension-entry spans, and then separate support spaces at each selected vertex. The resulting diagonal-Ext lower bounds and necessary incidence budget are actual obstruction statements, not assertions that arbitrary incidence data are realizable. SF-E832/R and E833 exclude the actual single-center square-zero star architecture for both uniform signs and then arbitrary mixed signs, using the intrinsic defect determinant, compound-form equation and full cubic character. Multicenter and different-unit architectures remain outside.

SF-E834 fills the stable-reflexive mixed-curvature gap. Translation averaging gives the precise divisor-pair Chern-Weil identities; equality, Bianchi and clean compact slices give bounded tracefree curvature across the entire curve/point singular set. Smooth determinant normalization and the published Biswas theorem give an actual bundle extension, after which the checked E811 theorem supplies projective flatness. SF-E835 uses this result on the stable-factor reflexive hulls of every semistable torsion-free balanced sheaf. Actual effective support cycles remove surfaces and curves, and local-cohomology vanishing lifts actual extension classes across the remaining finite set. The actual hull then satisfies E818. Consequently singular hulls and singular stable factors no longer provide a semistable escape: all such semistable torsion-free balanced sheaves are excluded from weak equivariant semiregularity.

Current further orthogonal strengthening, the q3 projective-involution refinement, and the arbitrary-Artin local obstruction research are not integrated results at the time this review script was prepared. Any later draft is excluded from the movement just counted unless it receives a separate subsequent integration and review. Source searches, corrected event classifications, notation-only TeX improvements, successful reruns and checkpoint packaging are not movement.

### Every open row at this review

| Row | State | Strongest proved reduction and remaining gate |
|---|---|---|
'''
for row in opened:entry+=f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
entry+='''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** the polarization, published rank4 dominance, explicit integral detector and quadratic division constants remain complete.
- **Target2, class-number-one sixfolds with every determinant:** all split families, all Eisenstein determinants and Gaussian determinant class3 have effective bounds. The other nonsplit determinants remain unresolved. The possible suppliers must satisfy the strictly smaller finite symplectic/orthogonal parameter ranges, the longer alternating-shape condition, the remaining exceptional inducing profiles, original-field descent, actual rank9 and effective integral-cycle requirements. These necessary restrictions do not construct a missing supplier.
- **Target3, Eisenstein split eightfolds through G34:** the published-input reconstruction, exact rank16, integral cycle suppliers, transfer and effective polarization/order constants remain complete. No unrefereed Severn theorem has become a premise.
- **Target4, natural imprimitive sources:** the exact signature criterion, all-family nondominance and sharp n5 maxima15/14 remain proved. The exact Nielsen-rank procedure terminates per specified component; the unbounded table has not been executed.
- **Target5, actual perfect complexes:** the n3 construction and coherent numerical variant remain complete. The genuine balanced-RM n4 seed remains open. Every semistable torsion-free candidate is now excluded in the stated finite-action scope, and all signed single-center stars in the specified architecture are excluded. Unstable sheaves, nonpure Artin modifications outside the checked cases, other positive-dimensional defects and local units, and broader overlapping derived constructions still require work.

Every counted new proof has a whole-proof reading and the recorded independent mathematical/source audit. The numerical supplements are kept separate from universal arguments and published inputs. The original Harris--Tonegawa full proof was not obtained; the exact published Biswas theorem and complete proof were read, with that upstream scope explicit. Markman, Severn and032 retain their conditional status. No TeX compilation is claimed.

Continue on both strictly smaller main gates. The stopping rule is not triggered. The next formal review is due2026-11-21T22:38:55+00:00.
'''
entry+=f'\nThe included {integrity["input_files"]}-file TeX source graph passes all recorded source-integrity checks.\n'
with (R/'LEDGER.md').open('a') as f:f.write(entry)
snapshot={'review':9,'date_utc':now.isoformat(),'compared_with_review':8,'movement':True,'counted_rows':counted,'open_rows':opened,'consecutive_no_movement':0}
(R/'research/review09_snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
state.update(last_review=now.isoformat(),formal_reviews_completed=9,consecutive_reviews_without_movement=0,next_review_utc=(start+timedelta(hours=12)).isoformat())
sp.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({k:v for k,v in snapshot.items() if k!='open_rows'}))
