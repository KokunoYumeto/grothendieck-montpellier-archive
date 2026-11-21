"""Third substantive hourly review, comparing the actual gates with review02."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

root = Path(__file__).resolve().parents[1]
state_path = root / 'RUN_STATE.json'
state = json.loads(state_path.read_text())
now = datetime.now(timezone.utc)
start = datetime.fromisoformat(state['start_utc'])
due = start + timedelta(hours=5)
if now < due:
    raise SystemExit(f'Not due until {due.isoformat()}')
if state.get('formal_reviews_completed') != 2:
    raise SystemExit('Requires exactly completed review02; no replay.')
rows = list(csv.DictReader((root / 'QUESTIONS.tsv').open(), delimiter='\t'))
open_rows = [r for r in rows if r['state'] in ('active', 'open', 'unchecked')]
text = f'\n## Formal movement review03 — {now.isoformat()}\n\n'
text += f'Third formal review, due {due.isoformat()}, compared substantively with review02 at 14:39:00 UTC.\n\n'
text += '''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main gates have strictly shrunk. On Q2i, D-EX and D-UP exclude two additional infinite scalar representation families; BI11--12 remove six fields and all real reflection closures from inducing dimension four; BI13 removes reflections from every inducing image for the six ramified-prime fields; BI14/14a supplies explicit linear and quadratic degree bounds for scalar-unramified models. BI15 rules out compatible symmetric larger-field twelve-branch sources. R5 and HD-E8IF1 reduce the five-dimensional and proper-field E8 possibilities to exact local profiles. None of the remaining profiles is asserted to give descent or dominance. On Q5i, SF-E811--813 excludes stable realizations and weakly semiregular semistable bundles with locally free stable factors. SF-E815 excludes the stated simple derived repairs with nonnegative aggregate projectively flat weights, and forces at least31 invariant endomorphisms in the particular seven-class model. These are proper reductions of the two gates recorded at review02. The actual two-pure E814 example, source-reading, check-register repairs and packaging are not counted as movement.\n\n### Every open row at this review\n\n| Row | State | Strongest proved reduction and remaining gate |\n|---|---|---|\n'''
for row in open_rows:
    text += f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|', ' / ')} |\n"
text += '''\n### Main-question gates\n\n- **Target1, Gaussian principal fourfolds:** complete checked numerical detector and quadratic division bounds, with the actual restricted polarization and exact rank4 published locator. No new gate.\n- **Target2, every class-number-one sixfold determinant:** all split data remain numerically proved using the explicitly supplied Perry input; every Eisenstein determinant and Gaussian signed determinant class3 is numerically proved. The class3 bound remains D3(Delta)=69984^12 M^114 Delta^18 B^(4L+21)S, with full conductor and lattice costs. Other nonsplit determinants remain open. A remaining curve source must satisfy the stricter representation, inducing-field, ramification, symmetry and local-profile gates above, or a genuine balanced-RM eightfold seed must escape the proved obstructions below. The new rank6/7 work and the new signed two-cohomology cone argument are still under preparation/check and are not counted here.\n- **Target3, Eisenstein split eightfolds through G34:** complete published-input reconstruction, actual rank16, integral cycle transfer and an explicit fixed-order/polarization bound. The unrefereed Severn theorem is not used as a premise.\n- **Target4, natural imprimitive sources:** exact signature criterion, all-family nondominance and sharp n5 maxima15/14 are proved. D-NR01--04 gives a terminating exact procedure for every specified Nielsen component, and finite tables at each fixed degree; only the specified small cubic matrix example and the separate explicit rank1 families have actually been executed. No unbounded table is claimed.\n- **Target5, actual non-curve object for n3 or n4:** the n3 request remains fulfilled by an actual checked perfect complex, with a numerical coherent variant. The remaining n4 balanced-RM seed is an alternative route to Q2i. In addition to the previous parity, CI and rational-block obstructions, stable locally free realizations and semistable locally free-factor repairs are now excluded. The stated simple derived models with positive aggregate weights are also excluded. Singular factors, objects outside the common primitive RM class space, signed larger class sets, sufficiently nonsimple objects and more general derived or twisted constructions remain open.\n\nAll conditional uses of Markman/032/Severn remain separated; supplied Perry and DEG_L categorical inputs retain their stated provenance. TeX has source-integrity verification, but no successful compilation is claimed. Every newly counted theorem has a whole-proof reading recorded; finite computations have only their actual certified scopes.\n\nContinue work on the reduced nonsplit source and balanced-RM gates. The next formal review is due2026-11-21T16:38:55+00:00. No stopping rule is triggered.\n'''
with (root / 'LEDGER.md').open('a') as file:
    file.write(text)
state.update(last_review=now.isoformat(), formal_reviews_completed=3,
             consecutive_reviews_without_movement=0,
             next_review_utc=(start + timedelta(hours=6)).isoformat())
state_path.write_text(json.dumps(state, indent=2) + '\n')
print(json.dumps({'review': 3, 'time_utc': now.isoformat(), 'movement': True,
                  'open_rows': [r['id'] for r in open_rows]}))
