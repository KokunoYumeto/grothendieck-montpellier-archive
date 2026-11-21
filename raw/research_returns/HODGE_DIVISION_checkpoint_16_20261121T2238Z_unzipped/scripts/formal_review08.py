"""Eighth substantive review; a clock guard forbids early execution or replay."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

R=Path(__file__).resolve().parents[1]
sp=R/'RUN_STATE.json'; state=json.loads(sp.read_text())
now=datetime.now(timezone.utc); start=datetime.fromisoformat(state['start_utc'])
due=start+timedelta(hours=10)
if now<due: raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed')!=7: raise SystemExit('Requires review07 exactly; no replay.')
previous=json.loads((R/'research/review07_snapshot.json').read_text())
rows=list(csv.DictReader((R/'QUESTIONS.tsv').open(),delimiter='\t'))
byid={r['id']:r for r in rows}
counted=['Q5y','Q2bi','Q2bj','Q2bk','Q2bl','Q2bm','Q5z','Q5aa']
assert byid['Q5y']['state']=='proved'
for rid in counted[1:]: assert byid[rid]['state']=='refuted'
opened=[r for r in rows if r['state'] in ('active','open','unchecked')]
assert {r['id'] for r in opened}=={'Q2i','Q5i'}
prior_open={r['id']:r for r in previous['open_rows']}
for row in opened:
    assert row['finding_ids_or_current_gate']!=prior_open[row['id']]['finding_ids_or_current_gate']
integrity=json.loads((R/'research/tex_integrity_review08.json').read_text())
assert integrity['status']=='PASS' and integrity['input_files']==148
entry=f'\n## Formal movement review08 — {now.isoformat()}\n\n'
entry+=f'Eighth formal review, due {due.isoformat()}, compared substantively with review07 at {previous["date_utc"]}.\n\n'
entry+='''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main questions have strictly smaller proved gates.

For Q2i, the odd rank-two symplectic result excludes every ordinary Sp4(q) core for odd q>=5 under the stated transitive nonsplit-source hypotheses. The generic proof and finite exceptional endpoints are distinguished; four erroneous indexed identities in a cited table source were not used, and direct table values are retained. D-EXS excludes arbitrary mixtures of the four specific cores F4(2), F4(3), E6(2), and twisted E6(2), with full compatible normalizers. This is a finite family result, not an exclusion of all exceptional groups.

D-HOS03--06 excludes all ordinary symplectic factors of rank at least4 over odd fields q>=7, allowing arbitrary mixed factors and full compatible normalizers. Its complete elementary radical, carrier, and descent proofs are written. D-UNW and D-LNW give an explicit natural-dimension cutoff n<10^61 for the remaining transitive equal-degree linear and unitary cores: the high-level character estimate excludes the non-Weil case, and the already proved Weil exclusions handle the other case. This is an effective finite collection of possible groups, not an executed enumeration. D-OSM excludes the specifically listed small orthogonal cores and covers through full character spectra and compatible-normalizer bounds. No unlisted family is silently included.

For Q5i, SF-E825 supplies a necessary positive determinant-trace equation for all forms of the unit surface module with free summands, including arbitrary off-diagonal gluing. Flat adjusted determinants from the ambient variety are excluded. Positive adjusted determinants remain possible, so the result is a necessary gate, not a universal exclusion.

SF-E826 excludes the specified actual two-slope extension architecture using both actual long exact sequences and the normalized balanced middle-Ext cap18. Its explicit indecomposable example has invariant middle Ext at least192 and is not a seed. SF-E827 then removes the global opposite-cross-Ext3 vanishing requirement for two precise divisor settings. Nondegenerate cross-line differences leave6 diagonal classes per usable block; every nonzero difference in the rational four-divisor Gaussian algebra leaves4, including the degenerate cases. Selected negative blocks require their stated unit-block vanishing. These overlapping results are counted as successively stronger restrictions, not inflated as independent solutions.

The orthogonal degree/level/spin draft, the q5 symplectic refinement, the stronger87-percent alternating shape bound, and the equal-hull equivariance clarification have received substantial reviews but are not yet integrated into this snapshot and are not counted here. The newly written q3 and geometric-support/actual-entry refinements likewise remain pending. Source searches, successful arithmetic reruns, counterexamples outside the balanced character, and packaging are not movement.

### Every open row at this review

| Row | State | Strongest proved reduction and remaining gate |
|---|---|---|
'''
for row in opened:
    entry+=f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
entry+='''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** the checked polarization, published rank4 dominance, and explicit integral detector and quadratic division constants remain complete.
- **Target2, class-number-one sixfolds with every determinant:** all split families, all Eisenstein determinants, and Gaussian determinant class3 have effective bounds. Other nonsplit determinants remain unresolved. Any curve supplier must pass the smaller core gate, original-field descent, actual rank9, and integral effective-cycle requirements. Unresolved low-field families, the remaining ordinary alternating long-shape tensor cases, and exceptional inducing profiles still require work. A balanced-RM eightfold is the alternative route.
- **Target3, Eisenstein split eightfolds through G34:** the published-input reconstruction, exact rank16, integral suppliers, transfer, and effective polarization/order constants remain complete. No unrefereed Severn theorem has become a premise.
- **Target4, natural imprimitive sources:** the exact signature criterion, all-family nondominance, and sharp n5 maxima15/14 remain proved. The Nielsen-rank procedure terminates per specified component; no unexecuted unbounded calculation is claimed.
- **Target5, actual perfect complexes for n3 or n4:** the actual n3 complex and coherent numerical variant remain complete. A genuine balanced-RM n4 seed remains open. The added-free-summand determinant gate and the actual two-slope/diagonal class obstructions are now stronger. Nonsplit positive filtration factors, other local modules, different supports and divisor directions, the uncovered Artinian cases, and broader derived configurations remain possible.

The counted findings have whole-proof readings and the recorded independent mathematical or arithmetic audits. Exact calculations are kept separate from published source premises. Markman, Severn, and032 retain their conditional status. The included148-file TeX graph passes source-integrity checks; no successful TeX compilation is claimed.

Continue on both strictly smaller main gates. The stopping rule is not triggered. The next formal review is due2026-11-21T21:38:55+00:00.
'''
with (R/'LEDGER.md').open('a') as f:f.write(entry)
snapshot={'review':8,'date_utc':now.isoformat(),'compared_with_review':7,'movement':True,
          'counted_rows':counted,'open_rows':opened,'consecutive_no_movement':0}
(R/'research/review08_snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
state.update(last_review=now.isoformat(),formal_reviews_completed=8,
             consecutive_reviews_without_movement=0,next_review_utc=(start+timedelta(hours=11)).isoformat())
sp.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({k:v for k,v in snapshot.items() if k!='open_rows'}))
