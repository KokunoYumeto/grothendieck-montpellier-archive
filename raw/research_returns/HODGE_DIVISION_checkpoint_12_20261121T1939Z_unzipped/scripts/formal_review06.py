"""Sixth substantive review, guarded against premature execution or replay."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv
import json

R = Path(__file__).resolve().parents[1]
state_path = R / 'RUN_STATE.json'
state = json.loads(state_path.read_text())
now = datetime.now(timezone.utc)
start = datetime.fromisoformat(state['start_utc'])
due = start + timedelta(hours=8)
if now < due:
    raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed') != 5:
    raise SystemExit('Requires completed review05 exactly; no replay.')
rows = list(csv.DictReader((R / 'QUESTIONS.tsv').open(), delimiter='\t'))
byid = {r['id']: r for r in rows}
counted = ['Q2aw', 'Q2ax', 'Q2ay', 'Q2az', 'Q2ba', 'Q2bb', 'Q5q', 'Q5r', 'Q5s']
for name in counted:
    assert byid[name]['state'] == 'refuted', (name, byid[name]['state'])
opened = [r for r in rows if r['state'] in ('active', 'open', 'unchecked')]
assert {r['id'] for r in opened} == {'Q2i', 'Q5i'}
integrity = json.loads((R / 'research/tex_integrity_post_surface.json').read_text())
assert integrity['input_files'] == 114
for key in ('missing_inputs', 'undefined_citations', 'undefined_references',
            'duplicate_bibitems', 'duplicate_labels', 'environment_findings'):
    assert not integrity[key]

entry = f'\n## Formal movement review06 — {now.isoformat()}\n\n'
entry += f'Sixth formal review, due {due.isoformat()}, compared substantively with review05 at 17:39:04 UTC.\n\n'
entry += '''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main questions have strictly smaller proved gates.

For Q2i, D-BI-23 excludes all transitive linear-Weil cores SL_n(q), n>=3, including compatible outer normalizers. D-BI24 reduces all ordinary unitary-Weil cores to the single PSU4(2) degree5/6 endpoint; the existing non-Eisenstein nonsplit exclusion removes degree6 there. D-G2T-01--03 excludes all G2(q>=3) and triality 3D4(q>=2) cores, including mixed central products. D-ESC01--03 excludes the stated complete even-characteristic Sp4/Sp6 families, with the final Sp6(2) degree7 use retaining precisely the previous non-Eisenstein nonsplit scope. HD-ALT-04/05 forces every remaining large ordinary alternating factor to have a row or column exceeding 6n/7. The latter is a strict strengthening of the long-shape gate at review05, with (12,3) at n=15 an explicit new excluded shape. The intermediate 3n/4 threshold is not counted twice as an independent final restriction.

For Q5i, SF-E820 excludes all nontrivial modifications whose two defect modules are free over a common curvilinear Artinian quotient, at every length. SF-E821/E821a excludes actual local surface summands of ample class and the corresponding cones with any torsion-free quotient, including singular quotients. SF-E822 excludes genuinely coupled smooth integral surface repairs with equal ranks and equal ample degrees, hence all the specified same-character repairs. These coupled examples do not fall under the earlier local-summand argument, so this is a strict further reduction. Each construction supplies actual coherent sheaves or perfect complexes whose failure is proved; none is reported as a successful seed.

The all-representation A2/2A2 calculation, its PSL3(4) normalizer coverage, and the higher even symplectic work are still awaiting complete assembly or source verification at this review and are not counted. The unequal-slope positive Chern-character compensation and its explicit local nullhomotopies are test cases only; the proposed global tensor obstruction has not yet completed review and is not counted. Source substitutions, failed estimates, arithmetic reruns, register maintenance and packaging are not movement.

### Every open row at this review

| Row | State | Strongest proved reduction and remaining gate |
|---|---|---|
'''
for row in opened:
    entry += f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|', ' / ')} |\n"
entry += '''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** complete checked polarization, published rank4 dominance and explicit integral detector and quadratic division constants. No new open gate.
- **Target2, class-number-one sixfolds with every determinant:** all split families, all Eisenstein determinants and Gaussian signed determinant class3 have numerical bounds. Other nonsplit determinants remain unresolved. The possible curve suppliers now satisfy the strictly stronger core and alternating-shape restrictions above. Surviving exceptional profiles still require original-field descent, actual rank9 and effective algebraic cycle supply. The genuine balanced-RM eightfold seed is the non-curve alternative.
- **Target3, Eisenstein split eightfolds through G34:** complete published-input reconstruction, exact rank16, integral algebraic suppliers and transfer, and effective polarization/order constants. No unrefereed Severn theorem is a premise.
- **Target4, natural imprimitive sources:** exact signature criterion, all-family nondominance and sharp n5 maxima15/14 remain proved. The terminating rank procedure is proved for each specified Nielsen component; only the documented finite examples have been executed.
- **Target5, actual perfect complexes for n3 or n4:** the n3 request is fulfilled by the checked actual perfect complex and coherent numerical variant. The additional genuine balanced-RM n4 seed remains open. Unstable bundles, more general singular hulls, Artinian modules outside the proved point-defect cases, unequal-degree or singular surface modifications, and broader derived configurations remain under investigation.

All counted findings have recorded whole-proof readings and the specified independent checks. Complete character tables are distinguished from newly proved inequalities; the corrected Sp4 table and the dissertation status of the complete Sp6 table are explicit. Markman, Severn and032 retain their conditional statuses. The current114-file included TeX graph passes source-integrity checks; no successful TeX compilation is claimed.

Continue research on the smaller nonsplit-supplier and balanced-RM construction gates. No stopping rule is triggered. The next formal review is due2026-11-21T19:38:55+00:00.
'''
with (R / 'LEDGER.md').open('a') as stream:
    stream.write(entry)
snapshot = {
    'review': 6, 'date_utc': now.isoformat(), 'compared_with_review': 5,
    'movement': True, 'counted_rows': counted,
    'open_rows': opened, 'consecutive_no_movement': 0,
}
(R / 'research/review06_snapshot.json').write_text(json.dumps(snapshot, indent=2) + '\n')
state.update(last_review=now.isoformat(), formal_reviews_completed=6,
             consecutive_reviews_without_movement=0,
             next_review_utc=(start + timedelta(hours=9)).isoformat())
state_path.write_text(json.dumps(state, indent=2) + '\n')
print(json.dumps({k: v for k, v in snapshot.items() if k != 'open_rows'}))
