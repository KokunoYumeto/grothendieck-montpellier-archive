"""Perform the second scheduled formal progress review, not before its due time."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 20, 4, 10, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('Formal review02 is not due yet.')
ledger = root / 'PROGRESS_LEDGER.md'
heading = '## Formal review 02: 2026-11-20 04:10 UTC'
if heading in ledger.read_text():
    raise SystemExit('Refusing to duplicate formal review02.')

entry = r'''

## Formal review 02: 2026-11-20 04:10 UTC

This is the second scheduled review, one hour after review01. We compare only changes since that review. The overall report remains INCOMPLETE. The requested A.2, D.1, D.2(ii), and residual L8 rows remain open. B.2's literal boundedness/cofinal-constancy pair is now decided, while the additional weak upper-cone replacement remains separately tracked below. A stronger alteration argument for that weak assertion is under actual-file audit and is not counted before verification.

| Open record / requested row | Current strongest checked gate | Movement since review01 | Next substantive test |
|---|---|---|---|
| A:unresolved / A.2, arithmetic and one-dimensional range | Every Noetherian curve still reduces exactly to simultaneous top-degree Milnor residues after one localization on every finite separable normalization; generic dimension one becomes simultaneous Pic/p divisibility. All semilocal curves are proved. Every Noetherian model of a characteristic-zero field with cd_p(K)=trdeg_Q(K)+2 is now covered, including every finitely generated characteristic-zero field in the finite-cd scope. The remaining finite-transcendence arithmetic fields have a strict cohomological-dimension drop. The canonical cyclotomic instance remains equivalent to the full number-field cyclotomic mu conjecture. | Yes. The maximal arithmetic-dimension class is a proved strict exclusion from the previous gate; it imposes neither finite type nor normality on the model. The Galois full-integral-closure restriction and exact class-persistence criterion clarify the construction route, without claiming a counterexample. | Seek a non-Galois tower combining eventual finite splitting and bounded ramification with persistent mod-p ideal classes; independently test a different nonarithmetic field construction. |
| A:unresolved / A.2, strictly local fraction fields and general models | Every Noetherian model of each strictly local surface field with a quasi-excellent principal quotient is covered, including nonnormal models of the Nagata–Gabber field. For a quasi-excellent strictly local fraction field in any dimension, every semilocal model and every model with a geometrically unibranch dense open is also covered. The normalization may be infinite and non-Noetherian. | Yes. Mori–Nagata containment, the Dedekind-overring residue argument, and EGA finite topological normalization give additional fully audited exclusions. The remaining general-model gate is outside these classes. | Test models without a geometrically unibranch dense open, and higher-dimensional nonexcellent local rings lacking the principal-quotient hypotheses. Do not replace an infinite normalization by a finite one. |
| B.2-U / additional weak upper-cone replacement | A stable upper cone is proved over every perfect field and after finite purely inseparable constants. Over the original arbitrary field it is now proved whenever a proper regular birational model exists, in particular in dimensions at most three by Cossart–Piltant. Only imperfect-field cases in dimension at least four without a supplied regular model remain under this formulation. | Yes. The regular-model proof uses successive bad-divisor restriction kernels and a proved bounded-exponent lemma, strictly strengthening the previous dimension-two result. The all-dimensional alteration extension is still under audit at this review. | Finish and independently check the full invariant Weil-Picard ambient, semilinear alteration-constant descent, generic divisor restriction, and dN torsion bound. |
| D:fixed-boundary-gate / D.1 | The same normal proper nonprojective positive-characteristic geometric cases remain outside the projective, characteristic-zero, regular normal-crossings, entire-boundary neighborhood, and previously stated positive cases. Every requested fixed-boundary tame quotient is now proved small; every open subgroup has finitely generated maximal pronilpotent quotient. | No new geometric gate reduction. Smallness and pronilpotent generation restrict the possible group but do not imply full finite generation, as the proved small alternating-product example demonstrates. | Obtain a uniform full generator bound or an actual geometric counterexample for the residual fixed-boundary quotient. Tameness at original divisors is not replaced by valuation tameness. |
| D:fixed-boundary-gate / D.2(ii) | The same singular proper nonprojective cases remain outside the boundary-neighborhood, finite regular-cover, finite-local-group, strongly F-regular, mutation-surface and finite-field surface results. For a finite omitted set, the unresolved case has at least two points and no common quasi-projective neighborhood; the explicit Schroer surface test uses transcendental constants. All proper codimension-two complements, even nonnormal ones, are now proved small. | No new geometric gate reduction. The strengthening from finite local groups to finite global images is being written as a sufficient criterion, but is not counted without a newly excluded residual instance. | Determine the global images of the punctured local groups in the explicit nonprojective surface test; or prove a new full-generation comparison. |
| L8, remaining component | Its arithmetic tame-homotopy, proper-descent, wild-local and direct-image components are settled. Its remaining finite-generation assertion is exactly the D.1/D.2(ii) gate. | No independent movement beyond its D dependencies in this hour. | Continue the same geometric D tests; this is not an additional independent theorem. |

**Requested row closed since review01:** B.2 has bounded h1 over every ground field, while the asserted constant domination-cofinal Picard diagram is false over an imperfect field by the complete threefold counterexample B.2q. The two branches preserve nonisogenous elliptic reduced identity components under every allowed domination. Thus the claimed equivalence fails in this precise cofinal interpretation. This is an actual status change, not an inference from the earlier nonfilteredness example. The weaker upper-cone assertion has remained explicit throughout and is not silently substituted for cofinality.

The other closed main questions retain their previously checked outcomes: A.1 and A.6 are refuted by excellent regular examples, A.5 by an excellent complete local mixed-characteristic example, B.1 is proved including infinitesimal group structure, and all PartC requests are decided in their exact marking conventions. The complete outcome table retains all57 requested rows and every lead.

**Review decision:** movement occurred in A.2 and B.2. The consecutive reviews-without-movement count remains **0**. The stopping condition is not met. Work continues. The next formal review is due **2026-11-20 05:10 UTC (06:10 CET)**; the next scheduled checkpoint is **04:40 UTC (05:40 CET)**. This formal review is not an additional checkpoint archive.
'''
ledger.write_text(ledger.read_text() + entry)

assembler = root / 'code/assemble.py'
s = assembler.read_text()
old = 'The first formal progress review was completed at03:10 UTC (04:10 CET): the residual gates strictly shrank, so the consecutive no-movement count is0. Work continues. The next formal review is due04:10 UTC (05:10 CET); the next scheduled checkpoint is03:55 UTC (04:55 CET). See PROGRESS_LEDGER.md for every open record and its exact gate.'
new = 'Formal review02 was completed at04:10 UTC (05:10 CET): A.2 gates strictly shrank and the stronger B.2 cofinal row was refuted; the consecutive no-movement count remains0. Work continues. The next formal review is due05:10 UTC (06:10 CET); the next scheduled checkpoint is04:40 UTC (05:40 CET). See PROGRESS_LEDGER.md for every open record and its exact gate.'
assert old in s
assembler.write_text(s.replace(old, new))
record = {
    'actual_utc': now.isoformat(), 'scheduled_utc': due.isoformat(),
    'review': 2, 'movement': True, 'consecutive_no_movement': 0,
    'open_requested_rows': ['A.2', 'D.1', 'D.2(ii)', 'L8 residual'],
    'additional_open_record': 'B.2-U',
    'closed_since_previous_review': ['B.2 strong cofinal Picard constancy (refuted)'],
    'next_review_utc': '2026-11-20T05:10:00+00:00',
    'next_checkpoint_utc': '2026-11-20T04:40:00+00:00'
}
(root / 'code/output/formal_review02.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
