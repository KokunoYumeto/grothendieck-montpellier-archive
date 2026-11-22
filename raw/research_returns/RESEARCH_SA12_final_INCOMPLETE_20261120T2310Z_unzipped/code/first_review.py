"""Record the first scheduled progress review, only after its due time."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 20, 3, 10, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('The first formal review is not due yet.')
ledger = root / 'PROGRESS_LEDGER.md'
heading = '## Formal review 01: 2026-11-20 03:10 UTC'
if heading in ledger.read_text():
    raise SystemExit('Refusing to duplicate the first formal review.')

entry = r'''

## Formal review 01: 2026-11-20 03:10 UTC

This is the first scheduled three-hour review. We compare with the initialization and the dated working entries above. The complete report remains INCOMPLETE. There are three unresolved statement records, corresponding to the requested outcome rows A.2, B.2, D.1, D.2(ii), and the remaining part of L8. All of them are listed below; no open row has been silently closed by a special case.

| Open record / requested row | Status and strongest checked gate | Movement at this review | Next substantive test |
|---|---|---|---|
| A:unresolved / A.2, quasi-excellent case | Lower bound is general. Every noetherian curve reduces to simultaneous top-degree Milnor residue surjectivity after one localization on every finite separable normalization. In generic dimension one this is simultaneous Pic/p divisibility. The canonical cyclotomic ring for odd p is equivalent to the full number-field cyclotomic mu=0 conjecture; it is an instance, not a reduction of all A.2. | Yes. The curve criterion is now exact in every finite generic dimension; semilocal curves and arithmetic generic-dimension-two fields are proved, and multiple earlier counterexample routes are excluded. | Seek an actual persistent Pic/p obstruction in a noncyclotomic algebraic tower with generic dimension one, preserving mod-p classes under extension rather than merely increasing finite-stage class numbers. |
| A:unresolved / A.2, unrestricted noetherian case | Normalization removes the separate nonnormal curve obstruction. A.2 holds for local surfaces with a quasi-excellent principal quotient, in particular every regular strictly henselian equicharacteristic-zero local surface. The Nagata example is repaired on B[1/Ft]. Every normal noetherian model of a quasi-excellent strictly local fraction field, and every one-dimensional model of that field, is also covered. | Yes. These are proved exclusions from the residual gate, including the explicit formerly undecided Nagata post-shrink instance. | Test higher-dimensional or positive-characteristic nonexcellent models for which the principal-completion argument has no quasi-excellent quotient; retain the exact residue obstruction when the model is one-dimensional. |
| B.2-U / B.2, weak upper-cone stabilization | h1 boundedness is proved over every field. Full stabilization is proved over perfect fields; a stable upper cone exists after finite purely inseparable constants. Over the original arbitrary field the weak formulation is proved in dimensions at most two. In dimension at least three over an imperfect field, all models map to one fixed Weil-restricted Picard comparison; the kernels are uniformly bounded, leaving image realization. | Yes. The alteration-constant and kernel obstructions are removed, and the weak residual dimension is now at least three. | Bound or realize the images in that fixed comparison over the original field. A finite Frobenius-kernel chain is only an abstract warning, not a geometric counterexample. |
| B.2-U / B.2, stronger cofinal constant-diagram formulation | Kept distinct from the weak assertion. The allowed geometrically normal model category can fail filteredness, even for smooth rational models, but this alone does not refute constancy of its Picard diagram. | Yes relative to initialization: the indexing issue is now explicitly refuted, and the weaker assertion has separately proved ranges. No inference from nonfilteredness to Picard nonconstancy is made. | Supply an actual allowed-model comparison realizing incompatible Picard data, or a cofinal construction that is valid despite the failed graph normalization step. |
| D:fixed-boundary-gate / D.1 | Remaining normal proper nonprojective positive-characteristic compactifications have boundary with no quasi-projective open neighborhood and lie outside the regular normal-crossings/tame positive cases. All surfaces over the algebraic closure of a finite field are covered. Fixed boundary tameness is strictly weaker than valuation tameness; a projective modification can introduce wild exceptional divisors. | Yes. The entire-boundary neighborhood case is proved and removes the single-point test; finite-field surfaces are also excluded. | Attack the original fixed-boundary quotient on a compactification with no such neighborhood; do not replace it by the valuation-tame group. |
| D:fixed-boundary-gate / D.2(ii) | Remaining singular proper nonprojective positive-characteristic compactifications are outside the neighborhood, finite regular-cover, uniformly finite local-group, strongly F-regular and mutation-surface cases. A residual finite omitted set has at least two points and at least one infinite local group. A residual surface needs transcendental constants. | Yes. Several precisely proved cases strictly shrink the gate. | Determine the explicit three-point puncture of Schroer's Pic=0 surface from section3, whose removed horizontal curve prevents the earlier inertia-killing argument. |
| L8, residual component | Arithmetic tame homotopy, effective descent, the wild local comparison counterexample and the direct-image criterion are settled. Only the D.1/D.2(ii) finite-generation component remains. | Yes, through the checked D reductions above. | Continue the same fixed-boundary tests; this is a dependency row, not an additional independent unresolved theorem. |

Main questions already closed: A.1 and A.6 are refuted even by excellent regular affine examples without real residue fields; A.5 has a complete excellent mixed-characteristic counterexample and a proved replacement; B.1 is proved scheme-theoretically; all Part C classification and representability requests are decided in their stated marking conventions. D.7 now includes the literal-scope Proposition5 counterexample and its universal descent-completion replacement. D.10 has an exact criterion over arbitrary bases. The report's 57-row outcome table gives every requested item and lead with statement locators.

**Review decision:** movement occurred. The consecutive reviews-without-movement count is **0**. The user's stopping condition is not met. Work continues. The next formal review is due **2026-11-20 04:10 UTC (05:10 CET)**. The next checkpoint after checkpoint04 is due **03:55 UTC (04:55 CET)**; its schedule is independent of the formal reviews.
'''
ledger.write_text(ledger.read_text() + entry)

p = root / 'code/assemble.py'
s = p.read_text()
s = s.replace(
    'The first scheduled formal progress review is due around 03:10 UTC (04:10 CET). This checkpoint is not a stopping review. All open work remains active.',
    'The first formal progress review was completed at03:10 UTC (04:10 CET): the residual gates strictly shrank, so the consecutive no-movement count is0. Work continues. The next formal review is due04:10 UTC (05:10 CET); the next scheduled checkpoint is03:55 UTC (04:55 CET). See PROGRESS_LEDGER.md for every open record and its exact gate.'
)
p.write_text(s)

record = {
    'actual_utc': now.isoformat(), 'scheduled_utc': due.isoformat(),
    'review': 1, 'movement': True, 'consecutive_no_movement': 0,
    'open_statement_records': ['A:unresolved', 'B.2-U', 'D:fixed-boundary-gate'],
    'next_review_utc': '2026-11-20T04:10:00+00:00',
    'next_checkpoint_utc': '2026-11-20T03:55:00+00:00'
}
(root / 'code/output/formal_review01.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
