"""Eleventh scheduled substantive review, due after thirteen hours; no replay."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,json
R=Path(__file__).resolve().parents[1]
statepath=R/'RUN_STATE.json';state=json.loads(statepath.read_text())
now=datetime.now(timezone.utc);start=datetime.fromisoformat(state['start_utc']);due=start+timedelta(hours=13)
if now<due:raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed')!=10:raise SystemExit('Requires review10 exactly; no replay.')
previous=json.loads((R/'research/review10_snapshot.json').read_text())
rows=list(csv.DictReader((R/'QUESTIONS.tsv').open(),delimiter='\t'));byid={r['id']:r for r in rows}
base=['Q2cf','Q2cg','Q2ch','Q2ci','Q2cj','Q2ck','Q2cm','Q2cn','Q5an']
optional=['Q2cp','Q2cq','Q2cr','Q5ao']
for rid in base:assert byid[rid]['state']=='refuted',rid
counted=base+[rid for rid in optional if rid in byid and byid[rid]['state']=='refuted']
assert 'Q2cl' not in counted and 'Q2co' not in counted
opened=[r for r in rows if r['state'] in ('active','open','unchecked')]
assert {r['id'] for r in opened}=={'Q2i','Q5i'}
prior_open={r['id']:r for r in previous['open_rows']}
for row in opened:assert row['finding_ids_or_current_gate']!=prior_open[row['id']]['finding_ids_or_current_gate']
integrity=json.loads((R/'research/tex_integrity_review11.json').read_text())
assert integrity['status']=='PASS' and integrity['input_files']>=202
entry=f'\n## Formal movement review11 — {now.isoformat()}\n\n'
entry+=f'Eleventh formal review, due {due.isoformat()}, compared substantively with review10 at {previous["date_utc"]}.\n\n'
entry+='''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main questions have strictly smaller proved gates. Only accepted whole-proof results and actual new row dispositions are counted.

For Q2i, D-ATT04--06 first excludes every two-factor source for both ordinary two-box-tail alternating labels, in all degrees n>=15 over non-Eisenstein original fields. Its new permutation-index estimate retains a full positive constant, and the exact weighted swap plus actual degree2n quotient gives a strict moving-rank contradiction. D-ATT07--09 then excludes every larger transitive tensor count for these same labels. The exact short-word correction includes identity cycle products, and the factor-fixing estimate retains its full constant. Thus both two-box-tail labels disappear entirely from this main gate.

HD-AST07--09 excludes the exactly-two-standard-factor source in all n>=15 over every original imaginary quadratic field. The new tensor-index bound treats all target eigenvalues through Cauchy and both real-target cycle counts; its actual2n quotient proof needs no conductor hypothesis. HD-AST10--12 then excludes every larger transitive standard tensor count over non-Eisenstein original fields. The full pair constant and exact weighted-cycle error give the strict source contradiction. These results supersede the finite degree intervals of review10 rather than merely restating them.

HD-AT301--03 removes the next ordinary family, the two-row three-box-tail label(n-3,3), in every n>=15: the single factor over every original field, and every transitive tensor count over non-Eisenstein fields. Its new character-defect average gives a uniform all-eigenvalue index bound with a positive full constant. Summing over the actual natural quotient contradicts the source Euler budget. The label(97,3) atn100 passed the earlier necessary shape gates and is now removed, proving strictness independently of the standard and two-tail closures.

D-OL16--18 completes the ordinary odd-characteristic even-natural orthogonal case. The nonsquare-involution proof uses an actual invariant two-plane radical, all linear-weight sectors and all nonlinear Heisenberg multiplicities, giving7a/32. Together with the earlier odd-natural and even-field results, ordinary transitive orthogonal factors satisfy even d<=1134 and odd d<=1133.

D-OL19--21 removes the genuine-Spin descent boundary in odd characteristic and even natural dimension. Wonenburger's even-Clifford construction is combined with a separately proved odd bimodule, exact represented-kernel preservation by perfectness, unique odd-primary radical lifts, and full inverse-image Levi actions. A nonzero weight orbit gives the degree floor for every Spin module, without an ordinary-character degree theorem. Every compatible normalizer is covered. D-OL22--24 handles odd natural dimension: its fourth-order carrier includes both SO cosets, and higher two-powers are handled through the square in Omega. Both proofs force exactly twelve one-factor projective reflections, whose actual generation contradicts perfectness on a common nonzero perpendicular. Thus all odd-characteristic transitive represented Spin factors satisfy even d<=1134 and odd d<=1133, with mixed large-dimensional factors excluded as well.

For Q5i, SF-E840 improves the necessary rank-four condition for actual quadratic-jet companion pencils: every rank-four leading image is a principal four-space ell·V, with its line ell unique. The proof uses a multiplication lower bound and the equality case of the all-size matrix estimate. Its explicit nonsquare complete intersection survives the earlier rank-five and scalar-minor tests but has a nonprincipal rank-four image, proving strict new exclusion. All higher perturbations and positive multiplicities in the stated actual common-defect architecture remain covered. No semiregular object on the residual locus is constructed.

HD-ALT09/Q2cl is explicitly NOT counted as separate movement. It presents exact necessary integers29,59,89,149,269,629,989,2429 for the eight non-Eisenstein class-number-one fields, derived from the already accepted shape bounds and k>=3. Its endpoint sharpness concerns only those displayed necessary inequalities, not an actual source.

The proposed D-OL25--26 sharpening to dimensions751/752 FAILED its independent source audit and was never integrated. The second published LST exponent is sqrt(N)/6, not sqrt(N/6). Its exact integer arithmetic passed only a mis-transcribed analytic premise. The original and corrected/withdrawn candidates and failure records are retained. A separate early root inference that the gamma cutoff43 meant4^3 was also wrong: enlarged primary glyphs show decimal43; the later source inequality gamma<=1/7 appears numerically inconsistent, and the new work uses only the safe uniform bound19/20. These corrections do not alter the accepted first-line LST bound sqrt(N/7),N>=567 or its base Spin consequences. A new direct proof-parameter optimization, if completed, must have its own full proof and review; the failed candidate is not counted as movement.
'''
for rid in optional:
 if rid in counted:entry+='\nAdditional accepted strict reduction '+rid+': '+byid[rid]['finding_ids_or_current_gate']+'\n'
entry+='\n### Counted new rows\n\n'+', '.join(counted)+'. Derived-only and withdrawn claims, pending drafts, searches, finite supplements alone, status edits, and packaging are excluded.\n'
entry+='\n### Every open row at this review\n\n| Row | State | Strongest proved reduction and remaining gate |\n|---|---|---|\n'
for row in opened:entry+=f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
entry+='''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** polarization, published rank4 dominance, integral detector and effective division constants remain complete.
- **Target2, class-number-one sixfolds and every determinant:** all split families, all Eisenstein determinants and Gaussian determinant class3 have effective numerical bounds. The other nonsplit determinants remain open. Their finite-curve suppliers must satisfy the new smaller alternating/Spin gates, all previously proved classical and exceptional restrictions, actual original-field descent, exact rank9 and integral effective-cycle requirements. The remaining necessary representation profiles are not positive suppliers.
- **Target3, Eisenstein split eightfolds through G34:** the published-input reconstruction, rank16, cycle suppliers, transfer and effective constants remain complete. No unrefereed Severn dominance theorem is a new premise.
- **Target4, natural imprimitive sources:** the exact signature criterion, all-family nondominance and sharp n5 maxima15/14 remain proved. The terminating per-component Nielsen-rank procedure is not an executed unbounded classification table.
- **Target5, actual perfect complexes:** the n3 construction remains complete. A genuine balanced-RM n4 seed remains open. The rank-four quadratic residual now requires principal images; rank<=3, principal-image residual pencils, other Artin defect modules/higher initial degrees, unstable torsion-free cases, other positive-dimensional defects and broader overlapping derived constructions remain. Further local necessary identities count only if they prove a genuinely smaller remaining gate.

Each accepted new proof has a complete recorded author/root reading and a separate peer audit with honest shared-derivation provenance. Finite calculations supplement the universal arguments and do not certify unchecked analytic premises. Markman, Severn and032 remain conditional wherever invoked. Source integrity is not TeX compilation.

Continue on the strictly reduced main gates. The stopping rule is not triggered. The next formal review is due2026-11-22T00:38:55+00:00.
'''
entry+=f'\nThe included {integrity["input_files"]}-file TeX source graph passes all recorded source-integrity checks.\n'
with (R/'LEDGER.md').open('a') as f:f.write(entry)
snapshot={'review':11,'date_utc':now.isoformat(),'compared_with_review':10,'movement':True,
 'counted_rows':counted,'explicitly_not_counted':['Q2cl','withdrawn D-OL25--26/Q2co reserved only'],'open_rows':opened,'consecutive_no_movement':0}
(R/'research/review11_snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
state.update(last_review=now.isoformat(),formal_reviews_completed=11,consecutive_reviews_without_movement=0,
 next_review_utc=(start+timedelta(hours=14)).isoformat())
statepath.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({k:v for k,v in snapshot.items() if k!='open_rows'}))
