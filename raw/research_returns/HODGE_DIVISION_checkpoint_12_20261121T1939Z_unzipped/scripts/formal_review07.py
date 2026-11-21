"""Seventh substantive review; guarded against premature execution or replay."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

R=Path(__file__).resolve().parents[1]
state_path=R/'RUN_STATE.json'; state=json.loads(state_path.read_text())
now=datetime.now(timezone.utc); start=datetime.fromisoformat(state['start_utc'])
due=start+timedelta(hours=9)
if now<due: raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed')!=6: raise SystemExit('Requires review06 exactly; no replay.')
previous=json.loads((R/'research/review06_snapshot.json').read_text())
rows=list(csv.DictReader((R/'QUESTIONS.tsv').open(),delimiter='\t'))
byid={r['id']:r for r in rows}
counted=['Q2bc','Q2bd','Q2be','Q2bf','Q2bg','Q2bh','Q5t','Q5v']
for rid in counted: assert byid[rid]['state']=='refuted'
opened=[r for r in rows if r['state'] in ('active','open','unchecked')]
assert {r['id'] for r in opened}=={'Q2i','Q5i'}
prior_open={r['id']:r for r in previous['open_rows']}
for row in opened:
    assert row['finding_ids_or_current_gate']!=prior_open[row['id']]['finding_ids_or_current_gate']
integrity=json.loads((R/'research/tex_integrity_review07.json').read_text())
assert integrity['input_files']==132 and integrity['status']=='PASS'
entry=f'\n## Formal movement review07 — {now.isoformat()}\n\n'
entry+=f'Seventh formal review, due {due.isoformat()}, compared substantively with review06 at {previous["date_utc"]}.\n\n'
entry+='''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main questions have strictly smaller proved gates.

For Q2i, D-A2-01--03 excludes all ordinary quasisimple PSL3(q)/PSU3(q), q>=3, with mixed factors and full compatible normalizers; L34-1--3 resolves the exceptional PSL3(4) extension coverage. PSL3(2) is expressly outside that result. D-HES-F and D-HES-01--06 now close the entire symplectic family of rank n>=4 over every even field, including mixed ranks/fields and outer, scalar and permutation actions. The successive finite, all-rank q2, and all-even stages are one expanding family exclusion, not several independent final gates. The former unverified semisimple citation has been replaced by a complete elementary parabolic proof. The q4 field involution has a direct descent and dual-weight argument.

D-C3-01--03 excludes every ordinary odd-characteristic rank-three symplectic core, allowing mixed fields and all compatible normalizers. It uses the complete similitude table with correct Clifford restriction; the q9 field endpoint is handled by projective semilinear symplectic descent. Its generic table premise is accurately identified as a dissertation and official data implementation, not a separately refereed journal table. No selfduality premise is needed. D-A7-01--03 closes all transitive A7-cover cores in the nonsplit problem, including double/triple/sixfold covers. Full spectra leave only standard outer reflections; actual split polarization handles the single standard factor, and the scalar-multiplier budget excludes standard tensors. This is strictly narrower than review06's residual A7-cover gate.

For Q5i, SF-E823 excludes all global tensor hull repairs of the unequal-degree unit surface module. SF-E824 then excludes every global form locally isomorphic to a positive number of copies of that unit module on the specified smooth ample complete intersection, including arbitrary nontensor gluing. The canonical first-overlap trace and determinant correction give the global obstruction. Rational B is handled by transporting ordinary obstruction vanishing, without asserting pullback of semiregularity. E824 strictly contains the tensor case; these are not counted as two independent final restrictions. Added free summands remain outside this completed exclusion.

SF-US and SF-UG give actual positive integral character examples and actual nontensor forms, respectively, but their construction alone is not counted as movement. SF-UGDC refutes a stronger proposed full-derived trace inference; it is a useful side counterexample, not a main-gate reduction. The newly written Heisenberg carrier lemma is checked locally, but its higher odd-symplectic consequence is not yet complete. The odd Sp4 calculations and the added-free-summand determinant draft are still under assembly or independent review and are not counted. Source searches, repeated arithmetic, register maintenance and packaging are not movement.

### Every open row at this review

| Row | State | Strongest proved reduction and remaining gate |
|---|---|---|
'''
for row in opened:
    entry+=f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
entry+='''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** complete checked polarization, published rank4 dominance and explicit integral detector and quadratic division constants. No new open gate.
- **Target2, class-number-one sixfolds with every determinant:** every split family, every Eisenstein determinant and Gaussian signed determinant class3 have effective numerical bounds. Other nonsplit determinants remain unresolved. Possible curve suppliers must satisfy the stronger core restrictions above, original-field descent, actual rank9 and integral effective cycle supply. Remaining exceptional profiles, small-field Lie families outside the completed exclusions, and ordinary alternating long-shape tensors remain under investigation. The balanced-RM eightfold seed is the non-curve alternative.
- **Target3, Eisenstein split eightfolds through G34:** complete published-input reconstruction, exact rank16, integral suppliers and transfer, and effective polarization/order constants. No unrefereed Severn theorem is a premise.
- **Target4, natural imprimitive sources:** exact signature criterion, all-family nondominance and sharp n5 maxima15/14 remain proved. The rank algorithm terminates for each specified Nielsen component; only documented finite examples have been executed.
- **Target5, actual perfect complexes for n3 or n4:** the n3 request is fulfilled by an actual checked perfect complex and coherent numerical variant. The genuine balanced-RM n4 seed remains open. All unit surface forms without free summands are now excluded. Added free summands, different local matrices or twists, other supports, unstable bundles, singular hulls, the remaining Artinian cases and broader derived configurations remain possible gates.

All counted findings have recorded whole-proof readings and the stated independent audits. Original character data are distinguished from new exact inequalities. Markman, Severn and032 retain conditional status. The included132-file TeX graph passes source checks; no successful TeX compilation is claimed.

Continue on the strictly smaller nonsplit-source and balanced-RM gates. No stopping rule is triggered. The next formal review is due2026-11-21T20:38:55+00:00.
'''
with (R/'LEDGER.md').open('a') as f: f.write(entry)
snapshot={'review':7,'date_utc':now.isoformat(),'compared_with_review':6,'movement':True,
          'counted_rows':counted,'open_rows':opened,'consecutive_no_movement':0}
(R/'research/review07_snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
state.update(last_review=now.isoformat(),formal_reviews_completed=7,
             consecutive_reviews_without_movement=0,next_review_utc=(start+timedelta(hours=10)).isoformat())
state_path.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({k:v for k,v in snapshot.items() if k!='open_rows'}))
