"""Record the audited post-checkpoint07 surface and group-theoretic results."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
record = root / 'code/output/integrate_D_fibration_post07.json'
if record.exists():
    raise SystemExit('Refusing to duplicate this integration.')
now = datetime.now(timezone.utc).isoformat()
p = root / 'code/assemble.py'
s = p.read_text()
for prefix, replacement in [
    ("('D.1',", "('D.1','Incomplete in general; mixed Q-factorial/lc/formally graded surface boundaries proved; all fixed-boundary quotients small with all-open pronilpotent generation','D:weighted-graded-boundary; D:formal-cone-fixed-boundary; D:negative-curve-tame; D:mixed-fixed-boundary; D:surface-mixed-boundary; D:lc-surface-boundary; D:finite-exceptional-wild; D:lc-elliptic-tame; D:fixed-boundary-small; D:cohomology-crown-criterion; D:uniform-H1-obstruction; D:fixed-boundary-positive; D:boundary-neighborhood; D:finite-field-surfaces; D:fixed-vs-valuation; D:fixed-boundary-gate'),"),
    ("('D.2(ii)',", "('D.2(ii)','Incomplete in general; every finite-punctured proper normal surface mapping to a curve, all-genus Schroer surfaces, mixed lc/Q-factorial/formally graded surface germs, arbitrary finite-local-image boundaries, and klt threefold boundaries in characteristic greater than five proved','D:surface-map-to-curve; D:vertical-fibration-multiplicity; D:vertical-fibration-models; D:weighted-graded-boundary; D:formal-cone-mixed-boundary; D:negative-curve-tame; D:schroer-all-genera; D:graded-cone-tame; D:formal-torus-lift; D:finite-local-images-arbitrary; D:klt-threefold-boundary; D:lc-surface-boundary; D:surface-mixed-boundary; D:rational-tree-Qfactorial; D:local-purity-boundary; D:finite-exceptional-wild; D:codim-two-small; D:fixed-boundary-positive; D:boundary-neighborhood; D:finite-regular-cover; D:finite-local-groups; D:finite-field-surfaces; D:fixed-boundary-gate'),")
]:
    old = next(line for line in s.splitlines() if line.startswith(prefix))
    s = s.replace(old, replacement)
old = next(line for line in s.splitlines() if line.startswith("'D.1/D.2(ii) remain open in full."))
new = "'D.1/D.2(ii) remain open in full. Every proper normal surface admitting a nonconstant morphism to a proper curve now has a finitely generated fundamental group after any finite puncture. Stein factorization and the p-rank-one criterion give a generically geometrically reduced connected family even in the quasielliptic case. In the proper homotopy sequence, a descended base cover has full inertia order dividing each retained fibre multiplicity. Those finite inertia images can be killed in one open subgroup, which is then a quotient of the fundamental group of a proper curve. A remaining finite-punctured surface must therefore admit no such morphism. The previously settled all-genus Schroer test remains, as do all mixed Q-factorial and arbitrary log-canonical omitted surface points. The formal-cone criterion now includes every normal positively graded completed surface germ, with arbitrary grading: a normalized blow-up produces one radial curve and only locally Q-factorial quotient charts, including characteristic-divisible weights. A single smooth exceptional curve also satisfies the criterion whenever its formal neighborhood is linear; the proved cohomological criterion includes self-intersection -d with d greater than max(0,4g-4). For arbitrary surface boundaries, the mixed theorem applies when the non-Q-factorial boundary singularities are isolated in the boundary and belong to these lc or formally graded classes. In every dimension, finite images of all omitted local fundamental groups suffice without a uniform order bound; this includes klt omitted loci on proper normal threefolds in characteristic greater than five, with arbitrary retained singularities. Local purity supplies the stated regular and higher-dimensional complete-intersection cases. The remaining geometric gate lies outside all these cases and has an infinite exceptional wild image on every applicable projective modification. An explicit characteristic-two Gorenstein surface with one genus-two exceptional curve of square -1 has a genuinely fierce quadratic quasi-etale cover, with index one, purely inseparable residue degree two, and different one. This disproves universal single-curve tameness, but does not refute finite generation. Finally, smallness, all-open pronilpotent generation, and even a uniform linear first-cohomology bound alone are insufficient group conditions. The proved exact group-theoretic replacement combines that cohomology bound with a uniform polynomial bound on nonabelian crown multiplicities. Neither uniform geometric bound is asserted in the remaining cases.',"
s = s.replace(old, new)
s = s.replace('The next formal review is due06:10 UTC; checkpoint07 is due05:25 UTC.', 'The next formal review and checkpoint08 are due06:10 UTC; checkpoint07 was saved at05:28 UTC.')
p.write_text(s)

entry = f'''

## Fibration and formal-neighborhood reductions after checkpoint07: {now}

The new checked labels are D:negative-curve-linearization, D:negative-curve-tame, D:formal-cone-mixed-boundary, D:formal-cone-fixed-boundary, D:weighted-graded-extraction, D:weighted-graded-boundary, D:wild-genus2-single-curve, D:uniform-H1-obstruction, D:cohomology-crown-criterion, D:vertical-fibration-exact, D:vertical-fibration-multiplicity, D:surface-map-to-curve, and D:vertical-fibration-models. Root read each complete actual proof file; substantive arguments also received independent agent audits.

The surface-map-to-curve theorem removes every finite-punctured normal proper surface with a nonconstant morphism to a proper curve. The proof retains arbitrary bad-fibre multiplicities and proves bounded full inertia rather than merely its wild part. The generic separability argument uses relative algebraic closedness and the base function field's p-rank one. Geometric reducedness, rather than smoothness, is the exact hypothesis of the original proper homotopy sequence, so quasielliptic fibrations are included. Birational surjection and finite normalization descent are written separately. This is a strict reduction of the D.2(ii) residual gate.

The weighted extraction extends the previously proved completed-cone case to every positive grading. Veronese extraction, the possibly characteristic-divisible toric regular cover, norm descent of local class groups, normalized-blow-up algebraization, and the common actual completed boundary DVR were all checked. The mixed global theorem accordingly adds these points to the allowable omitted classes. The sufficiently negative single-curve criterion is a proved recognition criterion for the already covered formal-linear class; it is not counted by itself as a new strict gate reduction.

The explicit fierce double cover has target equation b^2+(t^5+t^2 a^2)b+a^5=0 in characteristic two. Its weighted resolution has one smooth genus-two curve of square -1. The source and target are normal, the finite connected degree-two map is etale away from their origins, and the boundary DVR has e=1, purely inseparable residue degree2, and different1. The finite polynomial certificate passed26 exact assertions and received independent reruns. This refutes a local tameness shortcut, not either requested finite-generation assertion.

The uniform-H1 example is a small, non-finitely-generated product of alternating groups whose finite continuous modules all satisfy dim H1<=dim. The open-subgroup bound follows by continuous Shapiro. The separate exact profinite criterion adds polynomial nonabelian crown multiplicity and proves a c+2 generator bound. The finite auxiliary certificate has2803802 exact assertions. These are strategy clarifications and are not counted as geometric movement.

Only general D.1, general D.2(ii), and their residual L8 component remain requested open work. All Parts A, B and C remain decided. The report remains INCOMPLETE. The next scheduled formal review and checkpoint08 are both due06:10 UTC. This entry is not a stopping review or an additional checkpoint.
'''
for name in ['PROGRESS_LEDGER.md', 'report_supplement.md']:
    with (root / name).open('a') as f:
        f.write(entry)

with (root / 'parts/D/ROOT_POST_REVIEW03_NOTES.md').open('a') as f:
    f.write(f'''

## Post-checkpoint07 full-file and source audits: {now}

Root read all of `parts/B/D_negative_curve_linearization_B.tex`, `parts/D/D_formal_cone_global.tex`, `parts/C/D_weighted_graded_partial_resolution.tex`, `parts/B/D_wild_genus2_curve_B.tex`, `parts/D/D_uniform_cohomology_obstruction.tex`, and `parts/C/D_vertical_fibration.tex`. All13 displayed propositions/theorems/corollaries pass. The first-order normal-neighborhood argument excludes a spurious H1(O_C) obstruction; the weighted extraction allows inseparable regular covers and uses norms without a separability hypothesis. The wild example verifies both affine normality and the entire exceptional resolution, not just a generic polynomial identity. The crown proof includes the abelian case by explicit cocycle evaluations, so no unstated generator restriction is imported from a finite-group theorem.

Independently reopened primary sources include Stacks0EGH,03GV,02RS and all needed parts of0BG4 (54.11.1,54.11.3,54.11.6) for weighted extraction and completion; Stacks03H0,05DT,037P and0C0E for the fibration; original SGA1 TeX X1.1--1.4 pp261--263, X2.6 pp272--273 and XIII2.12 pp392--393; and Lucchini--Marion--Tracey2020 published pp10--13. LMT Proposition2.4, Lemma2.5 and equations(2.1)--(2.2) have exactly the required scope, including s>=d(L). Its classification-dependent finite-group inputs are identified in the manuscript. The independently downloaded LMT PDF has SHA256 b4e7f1907d222d95ef79db867cdb856b936bd515ab9e7d9e667ba4460bf061a5.

Independent actual-file passes were received from C/D for the negative-curve and weighted arguments, from C/D for the wild genus-two cover, from B for both uniform-H1/crown propositions, and from D for all four vertical-fibration statements. No priority claim is made.
''')
with (root / 'parts/D/ROOT_LITERATURE_SEARCH_0522.md').open('a') as f:
    f.write('''

Root subsequently read the full extracted author-linked Cutkosky--Srinivasan paper in three consecutive reads at05:24--05:25 UTC. Theorem1 on pp321--322 and Theorem3 on pp322--325 concern finite prime-to-p local groups and their resolution-tree presentation; Section3 supplies the characteristic-p Brieskorn tests. These do not supply a theorem of finite generation for the unrestricted local group. Some scanned formulas are OCR-corrupted; no further theorem is invoked on the strength of those formulas. This source search closes no requested row and is not counted as geometric movement.
''')

record.write_text(json.dumps({
    'utc': now,
    'new_audited_statements': 13,
    'certificate_programs_after_inventory_update': 20,
    'open_requested_rows': ['D.1 general', 'D.2(ii) general', 'L8 residual'],
    'strict_gate_reductions': ['finite-punctured normal proper surfaces mapping to a curve', 'mixed formally positively graded surface germs'],
    'next_review_utc': '2026-11-20T06:10:00+00:00',
    'next_checkpoint': 8
}, indent=2) + '\n')
print(record.read_text())
