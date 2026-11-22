"""Perform formal progress review03 at or after its scheduled time."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 20, 5, 10, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('Formal review03 is not due yet.')
heading = '## Formal review 03: 2026-11-20 05:10 UTC'
ledger = root / 'PROGRESS_LEDGER.md'
if heading in ledger.read_text():
    raise SystemExit('Refusing to duplicate formal review03.')
entry = r'''

## Formal review 03: 2026-11-20 05:10 UTC

This is the third scheduled review, compared with review02 at04:10 UTC. We count only requested status changes and strict reductions of a main residual gate. All Parts A, B and C are now decided. The only requested open rows are D.1, D.2(ii), and the dependent finite-generation component of L8. The report remains INCOMPLETE.

| Open record / requested row | Current strongest checked gate | Movement since review02 | Next substantive test |
|---|---|---|---|
| D:fixed-boundary-gate / D.1 | The remaining proper nonprojective positive-characteristic compactification lies outside all stated positive cases. For surfaces, the quotient is now finitely generated whenever every non-Q-factorial boundary singularity is isolated in the boundary and is either lc or has one smooth elliptic exceptional curve. All locally Q-factorial boundary singularities may be retained, even if non-lc, and all singularities outside the boundary may be arbitrary. The earlier whole-boundary-neighborhood and regular-SNC cases remain. Every remaining projective modification must have an exceptional boundary valuation with infinite wild image in the original group. | Yes. D:mixed-fixed-boundary strictly excludes arbitrary-boundary surface configurations not covered by the previous finite-point or SNC hypotheses. Its proof lists the unchanged original valuations and all newly extracted valuations, and produces the required surjection from a projective fixed-boundary quotient. The auxiliary smallness/pronilpotent results are not counted by themselves. | Attack a boundary passing through a non-Q-factorial nonisolated singular point, or prove a full uniform generator bound that controls the remaining exceptional wild images. Keep fixed-boundary tameness distinct from all-valuative tameness. |
| D:fixed-boundary-gate / D.2(ii) | Every proper normal surface with a finite omitted mixture of locally Q-factorial, single-smooth-elliptic, and arbitrary lc points is now proved, with unrestricted retained singularities. Rational SNC exceptional trees give bounded-exponent local class groups even without rational or lc singularities. No Cartier-index or Gorenstein restriction remains in the lc case. The same componentwise conclusion passes through finite normalization. In any dimension, purity also settles omitted regular local rings of dimension at least two and complete intersections of dimension at least three. A remaining finite-point surface example must omit at least one non-Q-factorial non-lc point outside the single-elliptic class, have no common quasi-projective neighborhood, and retain an infinite exceptional wild image on every projective modification. | Yes. The explicit elliptic three-point Pic=0 surface, all the mixed lc surface cases including characteristic-divisible index, non-lc rational-tree/Q-factorial points, and the higher-dimensional purity cases have complete independently audited proofs. These remove geometric instances from the previous gate. The original unrestricted row remains open. | Continue the genus-at-least-two Schroer three-point example via its fibration and compatible ramification; test whether the weighted different bound and global smallness imply stronger uniform control. A fierce local extension alone is not a global counterexample. |
| L8, remaining component | Its arithmetic tame-homotopy, proper-descent, wild-local and direct-image components remain settled. Its only open component is the D.1/D.2(ii) finite-generation gate above. | Yes, through the strict reductions of those D dependencies; no separate independent closure is claimed. | Continue the same geometric and ramification investigations. |

**Requested row closed since review02:** A.2 is refuted by the complete controlled quadratic tower. The resulting domain is excellent regular Dedekind, its fraction field has cd2=1, and every nonempty affine open has cd2=2 with infinite Pic/2. The proof checks finite character, bounded eventual ramification, persistence of ideal classes under every extension map, and vanishing of the Brauer group over every finite extension of the limiting field. The finite seed, transfer and regular-module computations have111784 exact assertions. The sharp curve statement and simultaneous-residue criterion are the proved replacements. A.1/A.6 also inherit the persistent strengthened refutation. There is no requested A gate left.

**Additional replacement closed since review02:** B.2-U, the weak stable-upper-cone formulation, is proved over every ground field and in every dimension by the full Galois-alteration argument. Semilinear constants, invariant abelian subvarieties, rational-torsor realization, bad-divisor kernels and the degree-times-exponent bound were checked in the written proof. The stronger constant domination-cofinal diagram remains refuted by the earlier imperfect-field threefold. No B gate remains open, and no equivalence between these distinct formulations is asserted.

**Quantitative limitation checked:** the local fierce Galois family has normalized different excess2/p^r tending to zero in a fixed characteristic. Its1,029,677 finite algebra/Jacobian assertions verify the displayed family, not a cover of a contracted surface. This refutes a proposed uniform positive lower bound and prevents that numerical shortcut. It does not itself count as a strict geometric reduction or decide either remaining requested row.

**Review decision:** movement occurred through the A.2 status change, the B.2-U replacement closure, and strict D geometric gate reductions. The consecutive reviews-without-movement count remains **0**. The stopping condition is not met. Work continues. The next formal review is due **2026-11-20 06:10 UTC**; checkpoint07 is due **05:25 UTC**. This review is not an additional checkpoint archive.
'''
ledger.write_text(ledger.read_text() + entry)
p = root / 'code/assemble.py'
s = p.read_text()
old = next(line for line in s.splitlines() if line.startswith("'Formal review02 was completed"))
new = "'Formal review03 was completed at05:10 UTC: A.2 and the additional B.2 weak replacement closed, and the residual D geometric gates strictly shrank. Only D.1, D.2(ii), and their dependent L8 component remain open. The consecutive no-movement count remains0. The next formal review is due06:10 UTC; checkpoint07 is due05:25 UTC. See PROGRESS_LEDGER.md for the exact gates and comparisons.',"
p.write_text(s.replace(old, new))
record = {
    'actual_utc': now.isoformat(), 'scheduled_utc': due.isoformat(),
    'review': 3, 'movement': True, 'consecutive_no_movement': 0,
    'open_requested_rows': ['D.1', 'D.2(ii)', 'L8 residual'],
    'closed_since_previous_review': ['A.2 (refuted)', 'B.2-U additional weak replacement (proved)'],
    'strict_gate_reductions': ['D.1 mixed arbitrary surface boundary', 'D.2(ii) all-lc/mixed surfaces and local purity'],
    'next_review_utc': '2026-11-20T06:10:00+00:00',
    'next_checkpoint_utc': '2026-11-20T05:25:00+00:00'
}
(root / 'code/output/formal_review03.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
