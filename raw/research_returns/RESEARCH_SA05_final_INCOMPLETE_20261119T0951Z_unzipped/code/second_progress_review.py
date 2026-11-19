"""Execute the second scheduled review, without changing the first review."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0)
due = datetime(2026, 11, 19, 6, 50, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('Review02 is due at 06:50 UTC; it must not be executed prematurely.')
target = ROOT / 'progress/review_02.json'
if target.exists():
    raise SystemExit('Review02 already exists and will not be overwritten.')
previous = json.loads((ROOT / 'progress/review_01.json').read_text())
with (ROOT / 'ITEM_STATUS.tsv').open(newline='') as stream:
    items = list(csv.DictReader(stream, delimiter='\t'))
by_item = {row['item']: row for row in items}
open_rows = {
 'B.1': ('Under universal Tate and eigenvalue-one semisimplicity, Chow-cycle injectivity in codimension m on every smooth projective variety of dimension 2m−1, for m≥2. The first case is CH2 on a threefold, equivalently the stated H4(F0 P4,Qell(3)) invariant vanishing under those hypotheses.',
         'The rational blow-up construction gives split maps into codimension2m on rational (4m−1)-folds, but keeps an arbitrary original variety as centre. It is an encoding, not a strictly smaller gate. No universal Chow-phantom vanishing was proved.'),
 'B.3': ('Divisor Tate for smooth projective geometrically integral surfaces with H1(Y,O_Y)=0 and very ample canonical bundle over every finite extension of F_p. This is equivalent to the universal whole-prime-to-p Brauer and abelian-torsor finiteness assertions over every finite-type base, and to the previous single H3(F0 P3,Qell(2)) invariant gate.',
         'The separate singular/nonproper base-image obstruction is removed by unit cups, v-descent and integral finite-error descent. Prime-uniform Brauer and torsor results are proved with one finite group across all ell≠p. Yuan’s fixed-field reduction and the final high-degree-cut refinement give the proper intrinsic surface subclass. All fixed lower thresholds on K² and p_g, and an arbitrarily small interval about K²/c2=1, are included in this same argument. The remaining restricted Tate conjecture is not proved; the unrestricted characteristic-primary assertion remains refuted.'),
 'B.5': ('General prescribed pure-motive rational realization and the compatible arithmetic duality completion; already in degree1 on a number ring it includes the appropriate Sha-finiteness/Bloch–Kato realization condition.',
         'Finite and Artin–Tate cases remain proved. Dualizing finite torsion groups or defining a formal rational graded dual does not construct the required prescribed motivic realization. No smaller general gate was established in this review interval.'),
 'C.1(c)': ('Actual vanishing of the finite rational Chow tests in the unconditional all-power criterion. For general K3 surfaces the unresolved cycle is the transcendental exterior projector wedge^(23−rho)t2(X).',
             'The C+ premise has been removed: covariant polynomial superrepresentations, the schematic superorbit ideal and finite generation give the criterion without algebraic parity projectors. A total computable arity bound is proved with its exact coefficient hypotheses, but it does not decide the Chow vanishings. A complete Brauer-category countermodel rules out deduction of the determinant from BV/Frobenius identities alone; it is not a geometric K3 counterexample. Both October2026 K3 proof PDFs found in the current search are withdrawn.'),
 'C.4': ('The general sharp R0 weight endpoint in degree j≥3. The first normalized trait case is H3 of a semistable projective threefold over a mixed-characteristic local field; after the proved extreme strings, the remaining block is N:Gr4→Gr2(−1).',
         'The low-degree and extreme-weight reductions were already counted at review01. Restricted-family papers and equicharacteristic results do not prove this mixed-characteristic universal block. No further verified reduction is counted here.'),
 'C.6': ('Independence of the unramified flag for arbitrary pure motives, or a proved exact equivalence with a named conjecture. Arbitrary nonalgebraic projectors outside the established abelian-type case remain unresolved.',
         'New surface, low-degree and stated hyper-Kahler Chow summands follow from the already explicit purity criterion, but these special cases do not reduce the main universal gate. Strong compatibility after a ramified extension does not descend unramifiedness, and traces alone do not detect a nonzero monodromy operator.'),
 'Lead B1': ('The universal finite-field comparison retains the same odd-dimensional middle-plus-one Chow gate as B.1; general arithmetic comparison remains the explicitly formulated conjectural package.',
             'The arithmetic extension-degree formula and the counterexample to literal geometric-limit continuity are proved in their scopes. They do not establish the remaining universal rational-versus-numerical comparison.'),
 'Lead C1': ('The requested general all-powers K3 statement retains the same transcendental determinant vanishing as C.1(c).',
             'The modified-diagonal identification and low-power narrow-ring results remain proved. The BV formal countermodel and withdrawal audit clarify failed routes without settling the geometric cycle.')
}
movement = [
 'C.1(c): removed the C+ premise from the finite necessary-and-sufficient all-power criterion. The exact finite rational relations now work for arbitrary Weil coefficients, with a fully supplied covariant superrepresentation lifting proof. This removes a conjectural auxiliary gate; actual Chow vanishings remain open.',
 'B.3: removed the singular/nonproper base-image obstruction for relative Brauer groups. The finite-type h-cover, perfection/v degree-two injection, unit-cup kernel and finite-error unit descent give the same surface-Tate gate for every finite-type base.',
 'B.3: replaced the universal surface test class by the proper intrinsic subclass H1(Y,O_Y)=0 with very ample canonical bundle, using Yuan’s fixed-field theorem and a fully checked high-degree-cut refinement. All numerical lower thresholds and the ratio K²/c2 tending to1 are part of this one reduction. The remaining restricted Tate statement is unresolved.'
]
not_counted = [
 'The whole prime-to-p strengthening is a stronger theorem but retains the same Tate gate, so it is not an additional stopping-rule movement.',
 'The computable uniform arity bound does not decide the finite Chow identities and is not counted as an additional closure of C.1(c).',
 'The rational blow-up encoding, additional C.6 special cases, the BV formal countermodel, source withdrawal checks, typesetting, bibliography repair, packaging and verification are not qualifying mathematical movement. Changing the numerical thresholds in the canonical-surface cut is not future movement.',
 'The all-base abelian-scheme extension already counted just before review01 is not counted a second time.'
]
record = {
 'review': 2, 'scheduled_at': due.isoformat(), 'reviewed_at': now.isoformat(),
 'movement': True, 'consecutive_reviews_without_movement': 0,
 'comparison_review': previous['review'], 'movement_evidence': movement,
 'not_counted_as_movement': not_counted, 'all_item_rows': items,
 'open_mathematical_rows': {key: {'recorded_status': by_item[key]['status'],
                               'current_gate': gate, 'attempts_and_limits': attempt}
                            for key, (gate, attempt) in open_rows.items()},
 'main_A_status': 'Closed only in the corrected or explicitly conditional scopes. The separate current CM-Hodge preprint remains an external theorem input; it is not a proof of full Tate.',
 'main_D_status': 'Corrected determinations, counterexamples and the permitted exact comparison-class equivalence remain proved.',
 'B2_scope_note': 'The requested conjectural formulation and specializations are supplied; general arithmetic-completion existence is not asserted.',
 'editorial_rows': {key: by_item[key] for key in ['E.1', 'E.2']},
 'next_formal_review': '2026-11-19T07:50:00+00:00',
 'next_checkpoint': '2026-11-19T07:20:00+00:00',
 'stop_rule': 'Stop after two consecutive formal reviews without an open-row status change or a strictly smaller main gate. Do not count packaging, repeated encodings, isolated cases or unchanged conjectural gates.'
}
target.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
lines = [f'\n## Formal hourly review02 — {now:%Y-%m-%d %H:%M:%S} UTC\n',
         'Qualifying mathematical movement occurred after review01. Consecutive formal reviews without movement: **0**. The programme remains **INCOMPLETE**. The next review is due 07:50 UTC and the next checkpoint is due 07:20 UTC.\n',
         'All 44 item rows are snapshotted in `progress/review_02.json`. Every mathematically open item and Lead is listed below.\n',
         '| Open row | Current gate / smallest instance | Attempts and exact limit |',
         '|---|---|---|']
for item, (gate, attempt) in open_rows.items():
    lines.append('| ' + item + ' | ' + gate.replace('|', '\\|') + ' | ' + attempt.replace('|', '\\|') + ' |')
lines += ['\nMovement counted in this review:\n'] + ['- ' + item for item in movement]
lines += ['\nWork explicitly excluded from the movement count:\n'] + ['- ' + item for item in not_counted]
lines += ['\nNo original universal open assertion is declared solved merely because its exact remaining condition is now known. A and D retain their scoped statuses; the general B.2 existence problem is still conjectural. Work continues under the user’s stopping rule.\n']
ledger = ROOT / 'PROGRESS_LEDGER.md'
ledger.write_text(ledger.read_text() + '\n'.join(lines))
report = ROOT / 'RESEARCH_SA05_report.md'
report.write_text(report.read_text() + f'\n## Scheduled progress review02\n\nThe second formal review was completed at {now:%H:%M:%S} UTC. Three qualifying changes since review01 are documented: removal of C+ from the finite cycle criterion, removal of the arbitrary-base Brauer obstruction, and restriction of the surface-Tate test class to H1(O)=0 with very ample canonical bundle, together with all numerical cut refinements. The no-movement count is 0. All eight mathematically open rows remain explicit in `progress/review_02.json`; work continues. The prime-uniform upgrade and additional special cases are not separately counted as smaller conjectural gates.\n')
result = {'review': 2, 'reviewed_at': now.isoformat(), 'all_items': len(items),
          'open_mathematical_rows': len(open_rows), 'movement': True,
          'consecutive_without_movement': 0, 'seconds': round(time.monotonic() - started, 6)}
(ROOT / 'code/second_progress_review_output.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
