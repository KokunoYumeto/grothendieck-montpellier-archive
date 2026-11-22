"""Record the fully audited post-checkpoint06 surface and local-purity reductions."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
record = root / 'code/output/integrate_D_lc_post06.json'
if record.exists():
    raise SystemExit('Already recorded; refusing to duplicate this integration.')
now = datetime.now(timezone.utc).isoformat()
p = root / 'code/assemble.py'
s = p.read_text()
s = s.replace(
    "('D.1','Incomplete: full finite generation remains; all fixed-boundary tame quotients are small and every open subgroup has finitely generated pronilpotent quotient; stated geometric cases proved','",
    "('D.1','Incomplete in general; mixed Q-factorial/lc/elliptic surface boundaries proved; all fixed-boundary quotients small with all-open pronilpotent generation','D:mixed-fixed-boundary; D:surface-mixed-boundary; D:lc-surface-boundary; D:finite-exceptional-wild; ")
s = s.replace(
    "('D.2(ii)','Incomplete: full finite generation remains; all proper codimension-two complements are small without normality, and all-open pronilpotent generation holds; stated geometric cases proved','",
    "('D.2(ii)','Incomplete in general; all lc and mixed Q-factorial/elliptic omitted surface points proved, as are stated local-purity cases; all-open pronilpotent generation holds','D:lc-surface-boundary; D:surface-mixed-boundary; D:rational-tree-Qfactorial; D:local-purity-boundary; D:finite-exceptional-wild; ")
old = next(line for line in s.splitlines() if line.startswith("'D.1/D.2(ii): smallness"))
new = "'D.1/D.2(ii) remain open in full. In dimension two, every mixture of locally Q-factorial omitted points, single smooth elliptic exceptional curves, and arbitrary log-canonical omitted points is now proved. No Gorenstein or Cartier-index restriction remains. A rational SNC exceptional tree gives a local class group of bounded exponent |det(M)|p^a, even without a rational or log-canonical singularity. A projective partial resolution leaves these Q-factorial points unchanged; the other boundary cores are elliptic or cyclic, and every pulled-back cover is tame there. The resulting projective fixed-boundary group surjects onto the original group. The arbitrary-boundary D.1 variant holds when every non-Q-factorial boundary singularity is isolated in the boundary and belongs to the elliptic or lc class. Retained singularities are unrestricted. In higher dimensions, local purity settles omitted regular local rings of dimension at least two and complete intersections of dimension at least three. A remaining finite-point surface counterexample must omit a non-Q-factorial, non-lc point outside the single-elliptic class, must have no common quasi-projective neighborhood of the omitted set, and must exhibit an infinite exceptional wild image on every projective modification. The explicit remaining Schroer test has initial curve genus at least two and transcendental constants. Its possible wild ramification necessarily has inseparable residue. The proved weighted different inequality restricts those extensions, but an explicit local Galois family has normalized excess 2/p^r tending to zero, so that numerical estimate alone does not rule them out. That local family is not claimed to be a cover of a contracted surface. All requested groups are small and every open subgroup has finitely generated maximal pronilpotent quotient; the alternating-product example proves these group restrictions alone insufficient.',"
s = s.replace(old, new)
p.write_text(s)

entry = f'''

## Log-canonical and mixed surface gates removed: {now}

The complete post-checkpoint06 arguments have received actual-file audits. The new checked labels are D:single-curve-residue-tameness, D:fierce-small-excess, D:finite-exceptional-wild, D:elliptic-surface-boundary, D:local-purity-boundary, the Gorenstein and prime-to-characteristic-index fallback statements, D:rational-tree-Qfactorial, D:lc-exceptional-configurations, D:lc-cusp-tame, D:lc-core-valuative-tame, D:Qfactorial-partial-resolution, D:surface-mixed-boundary, D:lc-surface-boundary, and D:mixed-fixed-boundary.

For D.2(ii), every mixture of locally Q-factorial, single-smooth-elliptic, and arbitrary log-canonical omitted surface points is now excluded from the residual gate, with arbitrary retained singularities. The rational-tree class is included without a rational-singularity or lc hypothesis. The lc proof uses real-valued discrepancy inequalities, a cycle identity retaining every extra edge, and an exact henselian comparison of the exceptional-curve fundamental groups. It does not invoke a separable index-one cover in characteristic-divisible index. The earlier prime-to-index argument remains a separately checked sufficient theorem, rather than a hidden hypothesis in the stronger result.

For D.1, the same projective partial-resolution argument covers an arbitrary closed boundary whenever each non-Q-factorial boundary singularity is isolated in the boundary and is single-elliptic or lc. Original divisorial valuations are unchanged; the new divisors lie only over the isolated points, where the local quasi-etale tameness proofs apply. This is a strict geometric exclusion beyond a finite omitted set. Local purity adds the stated regular and higher-dimensional complete-intersection cases to D.2(ii).

The remaining explicit Schroer test has genus at least two. A local family with inseparable residues and normalized different excess 2/p^r disproves a numerical lower-bound shortcut; it is not a global counterexample. Its finite algebra and Jacobian calculations passed1,029,677 exact assertions for q=2,3,4,5,8,9, with complete code and observed runtime. The general D.1/D.2(ii) requests and the dependent L8 component remain open, so the report stays INCOMPLETE. This is not a scheduled stopping review. Formal review03 remains due05:10 UTC; checkpoint07 remains due05:25 UTC.
'''
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write(entry)
with (root / 'report_supplement.md').open('a') as f:
    f.write(entry.replace('## Log-canonical and mixed surface gates removed:', '## Audited surface and purity additions:'))
with (root / 'parts/D/ROOT_POST06_AUDIT_NOTES.md').open('a') as f:
    f.write(f'''

## Root audits of the stronger lc and mixed-boundary arguments: {now}

Root read every line of `parts/B/D_all_lc_core_B.tex`, `parts/C/D_surface_mixed_boundary.tex`, and `parts/C/D_fixed_boundary_mixed.tex`. All seven numbered statements in these files pass the actual-file audit. The cycle identity includes internal multiplicity greater than two and all outside neighbors. The quasi-etale source is Q-Gorenstein and lc by the full different inequality; integrality of discrepancies is not used. A nonzero finite-index image in the target cycle's profinite fundamental group forces a cyclic source core. Galois transitivity then forces equality in every different bound, including residue separability.

The global argument retains Q-factorial omitted points and resolves the other singularities. Its projectivity proof explicitly checks both positive intersection with every curve and positive self-intersection. Root independently opened Fujino's author PDF Lemma2.2, printedpp6--7, including the characteristic-zero convention onp5; the short reproduced argument is characteristic-independent, and Tanaka2014 applies that fact in positive characteristic. The fixed-boundary extension lists all new divisors and proves that their centres are isolated points of the original boundary, where the covers are quasi-etale. The precise comparison is a surjective homomorphism from the projective fixed-boundary quotient to the originally requested quotient.

Editorial requests (status heading, Q-factorial wording, and explicit spreading from a local germ) were communicated before integration. No mathematical correction was needed. The original unrestricted D questions have not been marked solved.
''')
record.write_text(json.dumps({
    'utc': now,
    'remaining_requested_rows': ['D.1 general', 'D.2(ii) general', 'L8 residual'],
    'strict_surface_gate_reduction': True,
    'all_lc_indices_covered': True,
    'new_finite_certificate_assertions': 1029677,
    'checkpoint_due_utc': '2026-11-20T05:25:00+00:00'
}, indent=2) + '\n')
print(record.read_text())
