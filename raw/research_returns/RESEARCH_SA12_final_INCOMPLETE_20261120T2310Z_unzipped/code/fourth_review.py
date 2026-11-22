"""Perform formal progress review04 at or after its scheduled time."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 20, 6, 10, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('Formal review04 is not due yet.')
heading = '## Formal review 04: 2026-11-20 06:10 UTC'
ledger = root / 'PROGRESS_LEDGER.md'
if heading in ledger.read_text():
    raise SystemExit('Refusing to duplicate formal review04.')
entry = r'''

## Formal review 04: 2026-11-20 06:10 UTC

This is the fourth scheduled review, compared with review03 at05:10 UTC. All requested Parts A, B and C remain decided. The only open requested rows are general D.1, general D.2(ii), and the dependent finite-generation component of L8. No requested row is newly declared closed in this interval. The report remains INCOMPLETE.

| Open record / requested row | Current strongest checked gate | Movement since review03 | Next substantive test |
|---|---|---|---|
| D:fixed-boundary-gate / D.1 | The remaining proper nonprojective positive-characteristic compactification lies outside the projective, common-boundary-neighborhood and regular-SNC cases, the mixed Q-factorial/lc/formally graded surface criteria, and the new curve-fibration criteria in every dimension. Every original boundary is covered when the geometric generic fibre of a morphism to a curve has projective normalization; every vertical boundary is covered without that hypothesis. More generally, finite generation of the geometric generic fixed-boundary group implies that of the whole quotient. In dimension two every boundary on every normal proper surface mapping nonconstantly to a proper curve is covered. The remaining surface therefore has no such morphism. Every applicable projective modification in a remaining counterexample must have an exceptional boundary valuation with infinite wild image. | Yes. The mixed formal-cone/weighted-graded boundary statements and all-dimensional generic-fibre theorems remove configurations beyond the review03 lc/elliptic hypotheses. The original theorem is still open. The old two-centre fibred mutation example is not counted again merely because it satisfies the new theorem. | Control the new horizontal exceptional wild inertia of a rational pencil on a projective modification, or obtain both uniform finite-module H1 and nonabelian crown-multiplicity bounds. A rational pencil does not itself satisfy the proved global-morphism hypothesis. |
| D:fixed-boundary-gate / D.2(ii) | In addition to the earlier projective, regular, local-purity and mixed lc/Q-factorial cases, every all-genus Schroer three-point example is proved. Formally positively graded surface germs are allowed in mixed omitted sets, using a Q-factorial partial extraction. Arbitrary codimension-two omitted loci with finite global local-group images are covered without uniform order bounds; this includes klt threefold omitted loci in characteristic greater than five with arbitrary retained singularities. Curve-fibration criteria now cover every finite-punctured proper normal surface with a map to a curve, arbitrary-dimensional vertical codimension-two boundaries, and arbitrary codimension-two boundaries when the geometric generic fibre has projective normalization. Finite normalization descent remains available. | Yes. The all-genus three-point test left open at review03 is now settled by the complete cone/tameness proof and a projective partial contraction. The arbitrary finite-local-image, klt-threefold, formally graded, and generic-fibre arguments give further strict reductions. No inference of full generation is made merely from pronilpotent generation or smallness. | Attack a proper normal nonprojective surface with no curve morphism, at least two omitted points lacking a common quasi-projective neighborhood, and a non-Q-factorial non-lc omitted germ outside the formal graded classes; or prove a uniform theorem that controls all finite nonabelian covers. The concrete fierce genus-two germ tests local ramification but is not a global finite-generation counterexample. |
| L8, remaining component | Its arithmetic tame-homotopy, descent, wild-local and direct-image components stay decided. Its sole open component is exactly the two finite-generation gates above. | Yes through the strict reductions of those dependencies; no independent closure of the residual L8 component is claimed. | Continue the same geometric and finite-group investigations. |

**Proof and scope changes since review03.** The torus-lift argument for completed graded cones has been checked on all test algebras, including nonreduced ones; finite weight algebraization and commuting fixed fields prove both prime-to-p radial index and separable residue extension. The weighted extension uses a finite regular cover even when the grading index is divisible by the characteristic, norm descent of divisor classes, and the actual common completed boundary DVR. The negative-curve cohomology criterion is a recognition theorem for the already covered formal-linear class and is not separately counted as movement.

The fibration proof initially treated vertical punctures, then all original surface boundaries, and finally arbitrary-dimensional geometric generic fibres. Its generic image is normal by the arithmetic exact sequence. One fixed base open is supplied by the retained relative smooth locus; it does not vary with the finite cover. The remaining full or wild inertia images have orders bounded by fixed component multiplicities. A finite-index subgroup avoiding those images is a quotient of a proper or tame curve group. Pure normalization preserves the original etale site and original divisorial tame condition. The source hypotheses and both the full-inertia and wild-inertia cases have complete written proofs and independent audits.

**Auxiliary findings, not counted as movement.** There is now an actual fierce quadratic punctured cover over a Gorenstein surface resolved by one genus-two curve of square -1. Its covering surface is resolved by one genus-two curve of square -2. The two strict-local maximal pro-two groups are C2 and1, but no bound on full nonabelian wild inertia follows. The two exact polynomial certificates have26 and22 assertions. The perfect alternating-product example satisfies a uniform linear H1 bound for every finite module while remaining non-finitely-generated. The exact replacement requires, in addition, a uniform polynomial bound on nonabelian crown multiplicities and gives c+2 generators. Its finite auxiliary certificate has2803802 assertions. These clarify failed approaches without deciding either general D request.

**Approaches still blocked.** Gabber local smallness bounds each finite target separately and supplies no uniform exponent for varying nonabelian chief factors. The examined uniform Lefschetz sources require rank/coefficient and curvewise conductor bounds that original fixed-boundary tameness does not provide. A small normalized-different excess can tend to zero, so that numerical shortcut remains unavailable. Rational pencils can introduce horizontal exceptional valuations with uncontrolled wild inertia. A proposed second iteration of the explicit wild quadratic cover fails, while replacing it by a nonabelian cover remains untested geometrically. The paper and detailed research notes retain these distinctions.

**Review decision:** the strongest main geometric gates have strictly shrunk. The consecutive reviews-without-movement count remains **0**. The stopping condition is not met; work continues. The next formal review is due **2026-11-20 07:10 UTC**. Scheduled checkpoint08 is due now, at **06:10 UTC**, and checkpoint09 is due **06:55 UTC**. This review is not an additional checkpoint archive.
'''
ledger.write_text(ledger.read_text() + entry)
p = root / 'code/assemble.py'
s = p.read_text()
old = next(line for line in s.splitlines() if line.startswith("'Formal review03 was completed"))
new = "'Formal review04 was completed at06:10 UTC. All A/B/C rows remain decided; only general D.1, D.2(ii), and residual L8 remain open. The main geometric gates strictly shrank through the all-genus cone example, mixed formally graded germs, arbitrary finite-local-image and klt-threefold criteria, and all-dimensional generic-fibre theorems. Auxiliary ramification and group-theoretic calculations are not counted by themselves. The consecutive no-movement count remains0. The next formal review is due07:10 UTC and checkpoint09 is due06:55 UTC. See PROGRESS_LEDGER.md for the exact comparisons.',"
p.write_text(s.replace(old, new))
record = {
    'actual_utc': now.isoformat(), 'scheduled_utc': due.isoformat(),
    'review': 4, 'movement': True, 'consecutive_no_movement': 0,
    'open_requested_rows': ['D.1', 'D.2(ii)', 'L8 residual'],
    'closed_requested_rows_since_previous_review': [],
    'strict_gate_reductions': ['all-genus Schroer three-point test',
        'mixed formal-cone and weighted-graded surface boundaries',
        'arbitrary finite-local-image and klt-threefold boundaries',
        'all original surface boundaries under a curve morphism',
        'all-dimensional generic-fibre and vertical-boundary criteria'],
    'auxiliary_not_counted': ['negative-curve recognition',
        'wild genus-two cover and exact pro-two groups',
        'uniform-H1 obstruction and crown criterion'],
    'next_review_utc': '2026-11-20T07:10:00+00:00',
    'next_checkpoint_utc': '2026-11-20T06:55:00+00:00'
}
(root / 'code/output/formal_review04.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
