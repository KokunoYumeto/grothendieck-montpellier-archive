"""Record the independently audited cone and threefold gate reductions."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
record = root / 'code/output/integrate_D_cone_post_review03.json'
if record.exists():
    raise SystemExit('Refusing to duplicate this integration.')
now = datetime.now(timezone.utc).isoformat()
p = root / 'code/assemble.py'
s = p.read_text()
s = s.replace("('D.2(ii)','Incomplete in general; all lc and mixed Q-factorial/elliptic omitted surface points proved, as are stated local-purity cases; all-open pronilpotent generation holds','", "('D.2(ii)','Incomplete in general; all-genus Schroer surfaces, mixed lc/Q-factorial/elliptic surfaces, arbitrary finite-local-image boundaries, and klt threefold boundaries in characteristic greater than five proved','D:schroer-all-genera; D:graded-cone-tame; D:formal-torus-lift; D:finite-local-images-arbitrary; D:klt-threefold-boundary; ")
old = next(line for line in s.splitlines() if line.startswith("'D.1/D.2(ii) remain open in full."))
new = "'D.1/D.2(ii) remain open in full. The all-genus Schroer three-point surface test is now settled: every finite cover is tame at the two single-curve contractions, whose formal neighborhoods are exactly negative line bundles, and the resulting group is the fixed-boundary quotient of a projective partial contraction. The completed graded-cone theorem is proved by an affine lift group on all test algebras, Gabber local smallness, faithful flatness for arbitrary Hopf subalgebras, and a torus action centralizing the deck group. It proves both prime-to-characteristic ramification index and separable residue extension. The explicit fierce local family therefore cannot furnish a punctured cover of these cone germs. The previously proved mixed locally Q-factorial, single-elliptic and arbitrary log-canonical surface cases, including every Cartier index and rational exceptional trees without an lc hypothesis, remain. The arbitrary-boundary D.1 variant holds when every non-Q-factorial boundary singularity is isolated in the boundary and belongs to the stated elliptic or lc class. In every dimension, finite images of all omitted local fundamental groups suffice, without a uniform order bound and without a finite omitted set; the proof uses eventual etaleness of quasi-etale towers. This settles proper normal threefolds in characteristic p>5 with klt omitted locus and arbitrary retained singularities. Local purity also settles the stated regular and higher-dimensional complete-intersection boundary cases. A remaining surface counterexample must lie outside these classes and all projective-modification criteria; in particular the old higher-genus Schroer test is no longer an undecided instance. The next geometric gate is a non-Q-factorial, non-lc singularity with a non-linear formal exceptional neighborhood, or a more complicated exceptional configuration, with infinite exceptional wild image unavoidable on projective modifications. All requested groups are small and every open subgroup has finitely generated maximal pronilpotent quotient; these group conditions alone remain insufficient.',"
s = s.replace(old, new)
p.write_text(s)
entry = f'''

## Cone and threefold gates removed after review03: {now}

The new checked statements are D:finite-local-images-arbitrary, D:klt-threefold-boundary, D:Schroer-horizontal-tame, D:formal-torus-lift, D:graded-cone-tame, and D:schroer-all-genera. Root read the complete actual files, and each substantive proof received independent agent checks. The horizontal quotient is retained as a separate proved restriction; the stronger cone argument now closes the entire all-genus Schroer test.

The cone proof constructs a pro-affine lift group using every finite truncation and proves its kernel is the constant deck group on every test algebra, including nonreduced ones. Hartogs and idempotent lifting are used before invoking Hopf faithful flatness. The lifted connected torus centralizes the deck group. Finite weight algebraization yields prime-to-p radial index, and the commuting fixed fields prove separable residue extension. The final comparison uses a common genuine completed boundary DVR; it does not identify completion at the vertex with completion at the divisorial valuation.

For the global three-point surface, the blowup chart t=zu identifies the two exceptional formal neighborhoods with O_C(-c_1), for every positive genus. The projective partial contraction of A union R_2 has only these two divisorial boundary components. Every cover is tame there, so its projective fixed-boundary group equals the requested full fundamental group. This removes the explicit higher-genus test left open at formal review03.

The finite-local-image criterion now treats an arbitrary codimension-at-least-two boundary and assumes no uniform order bound. Its application to klt threefolds in characteristic p>5 is local near the omitted set; retained singularities are unrestricted. Root opened Carvajal-Rojas--Stabler2023 Theorem3.7 and the exact local-finiteness statements used, avoiding the overbroad optional claim about arbitrary prescribed big opens.

These are strict reductions of the remaining D.2(ii) gate since the05:10 review. The original D.1, D.2(ii), and residual L8 requests remain open. The report remains INCOMPLETE. The next scheduled formal review is06:10 UTC, and checkpoint07 is due05:25 UTC. No stopping review is performed by this integration entry.
'''
for name in ['PROGRESS_LEDGER.md', 'report_supplement.md']:
    with (root / name).open('a') as f:
        f.write(entry)
notes = root / 'parts/D/ROOT_POST_REVIEW03_NOTES.md'
notes.write_text(f'''# Root actual-file audits after review03

Recorded {now}.

Root read the complete `parts/D/D_klt_threefolds.tex`, `parts/B/D_Schroer_horizontal_reduction_B.tex`, `parts/C/D_graded_cone_tameness.tex`, and `parts/D/D_Schroer_all_genera.tex`. All six statements pass the full written-proof audit. The finite-local-image tower uses eventual local stabilization followed by the cited global theorem. The log product and blowup arcs prove the horizontal restriction. The completed-cone proof is checked on arbitrary test algebras, including the constant deck kernel and the fpqc finite-etale descent. Residue separability is obtained by the fixed-field identity, not inferred merely from the ramification index.

Primary sources actually read by root include: Hoshi2006 Proposition2.4, pp16--17, and PropositionA.10 with proof, pp57--58; published ILO XXI Theorem1.4, p529, with its unrestricted finite-group quantifier; Milne2012 VI Theorem11.1, pp82--85, including arbitrary Hopf algebras; Schroer1999 sections2.5 and3.1--3.2, author's pp4--5; and the published Carvajal-Rojas--Stabler2023 locators recorded in the bibliography. The source files and prior download records are retained. Independent actual-file cone audits by B and D, and the global corollary audit by B, agree.
''')
record.write_text(json.dumps({'utc': now, 'remaining_requested_rows': ['D.1 general', 'D.2(ii) general', 'L8 residual'], 'strict_gate_reductions_after_review03': ['all-genus Schroer test', 'arbitrary finite-local-image boundary', 'klt threefold boundary p>5'], 'checkpoint_due_utc': '2026-11-20T05:25:00+00:00'}, indent=2) + '\n')
print(record.read_text())
