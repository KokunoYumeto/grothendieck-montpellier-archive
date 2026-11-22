"""Consolidate actual root run records and the finite-certificate summaries."""
from pathlib import Path
import csv,json
root=Path(__file__).resolve().parents[1]
rows=[]
for path in sorted((root/'code/output').glob('*.run.json')):
    d=json.loads(path.read_text())
    rows.append({'record':str(path.relative_to(root)),'utc':d.get('utc',''),
                 'command':' '.join(d.get('args',[])),'seconds':d.get('seconds',''),
                 'returncode':d.get('returncode','')})
with (root/'PROGRAM_RUNS.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['record','utc','command','seconds','returncode'])
    w.writeheader();w.writerows(rows)
table=['## Programs and actual runs','',
       'All timings below are observed elapsed seconds. Finite checks certify only the displayed finite algebra, not the geometric theorems. Source downloads, build commands and extraction utilities are listed separately after the certificate table. Failed runs remain in the record.','',
       '| Program | Scope and counts | Calculation seconds |','|---|---|---:|']
certs=[
('parts/D/post18_research/code/check_residual_Frobenius_labels.py', '24,066 exact finite character-label translations and graded coefficient-slot/carry assertions; root independently reread and reran the program. The composite-order gerbe category, Frobenius functor, and unresolved formal atlas are not certified by this arithmetic', 'code/output/root_residual_Frobenius_labels_certificate.json', 'seconds'),
('parts/C/post16_research/code/check_RDP_Hom_framing.py', '536,909 exact monomial, colon-semigroup, endpoint-chart, multiplicity and internal-branch assertions; root independently reran the retained program. Duality, diagonalizable descent and the infinite geometric statements are proved separately; no Artinian-family classification is certified', 'parts/C/post16_research/output/RDP_Hom_framing_root.json', 'elapsed_seconds'),
('parts/D/code/check_elliptic_order_generators.py', '438,486 exact characteristic-three Jacobian, finite index-set, semisimple dimension and Frobenius-congruence assertions for r=2,4,...,256; torsion line bundles, geometric identifications and the sharp upper bound mu=3r are proved separately', 'parts/D/output/elliptic_order_generators_root.json', 'runtime_seconds'),
('parts/B/post14_research/code/check_superperfect_product.py', '112,276 exact permutation, tensor-support, counting and multiplicity assertions for the superperfect-cover product; Schur multipliers and GKKL computations remain cited literature inputs; source was outside checkpoint14 PDF and is assembled in checkpoint15', 'parts/B/post14_research/output/superperfect_product_root.json', 'runtime_seconds'),
('parts/D/code/check_Chow_surface_boundary.py', '1,705 exact integral-polynomial and F2/F3/F5 incidence assertions for the ample Chow-section boundary obstruction; checked research source was outside checkpoint14 PDF and is assembled in checkpoint15', 'parts/D/output/Chow_surface_boundary_root.json', 'runtime_seconds'),
('parts/C/code/check_RDP_branch_obstruction.py', '1,643 exact monomial, C3-action and valuation assertions for the rational-double-point branch-deletion obstruction; separate research source was outside checkpoint14 PDF and is assembled in checkpoint15', 'parts/C/output/RDP_branch_obstruction_root.json', 'elapsed_seconds'),
('parts/B/code/check_fixed_different_rational_chains.py', '2,340 exact assertions for20 degree-two characteristic-two covers: substitution, curve semigroup gaps, all resolution-chart transitions, different data and intersection determinants; properness and normality are proved separately', 'parts/B/output/fixed_different_rational_chains.json', 'runtime_seconds'),
('parts/B/code/check_alternating_quadratic_growth_reconstructed.py', '201,628 exact assertions: A5/A7/A9, elementary subgroup ranks, tensor dimension and composition bounds, and16 multiplicity inequalities; reconstructed program, distinct from the historical186,828-assertion JavaScript source', 'parts/B/output/alternating_quadratic_growth_reconstructed.json', 'runtime_seconds'),
('parts/D/code/check_psl2_bounded_ramification_v2.py', '31,222 exact assertions for q=4,8,16: fields, PSL2 generation, branch orbits, inertia, invariant polynomials, and product inequalities; separately reconstructed source, distinct from the historical306,144-assertion program', 'parts/D/output/psl2_bounded_ramification_v2_root.json', 'runtime_seconds'),
('parts/B/code/check_pure_root_tail.py','13 exact characteristic-two assertions for the pure degree-two source, cusp normalization, blowup chart, and changed Artin-Schreier equation with a simple pole; certifies the local failed tail-filling inference only','parts/B/output/pure_root_tail.json','runtime_seconds'),
('parts/B/code/check_finite_cone_genus2.py','16 exact characteristic-two assertions for the infinity chart, canonical and normal divisors, nilpotent Frobenius matrix, higher-obstruction degrees, and fixed cone degrees4 and8; formal algebraization and full inertia bounds are proved separately','parts/B/output/finite_cone_genus2.json','runtime_seconds'),
('parts/B/code/check_wild_genus2_source.py','22 exact characteristic-two identities for both source-resolution charts, their finite map, intersection points and Frobenius action; the pro-two conclusions are proved separately','parts/B/output/wild_genus2_source.json','elapsed_seconds'),
('parts/B/code/check_wild_genus2_curve.py','26 exact polynomial and chart assertions for the quadratic quasi-etale cover with a single genus-two exceptional curve; geometry and ramification are proved separately','parts/B/output/wild_genus2_curve.json','elapsed_seconds'),
('parts/D/code/check_uniform_h1_obstruction.py','2803802 exact assertions; alternating generators in degrees5–8, A5 deleted permutation module,14400 independent bar equations, and A5 squared outer tensor cohomology','parts/D/code/check_uniform_h1_obstruction_output.json','elapsed_seconds'),
('parts/C/code/check_fierce_different.py','1029677 exact assertions over q=2,3,4,5,8,9; finite-field affine actions, extension group generation, and rational Jacobian/different identities','parts/C/output/fierce_different_certificate.json','elapsed_seconds'),
('parts/C/code/check_quadratic_tower.py','111784 exact assertions; ranks1,2,3 regular-module quotient, transfer, inertia and Frobenius; Q(sqrt(-35)) norm/Minkowski seed','parts/C/output/quadratic_tower_certificate.json','elapsed_seconds'),
('parts/B/code/abelian_graph_certificate_B.py','19 exact checks; six geometric intersection points in F729; singular ideal, cusp normalization and valuation-semigroup identities','parts/B/code/output/abelian_graph_certificate_B.json','elapsed_seconds'),
('parts/B/code/elliptic_branch_certificate_B.py','11 exact checks; smooth elliptic cubics, tangent substitutions, full and reduced flex ideals, F3 point counts4 and6','parts/B/code/output/elliptic_branch_certificate_B.json','elapsed_seconds'),
('parts/C/code/check_threefold_local_geometry.py','11 exact polynomial checks; three A2 blowup charts and smoothness, coordinate changes, cusp multiplicity and36 quadratic-section basis monomials','parts/C/output/threefold_local_geometry.json','elapsed_seconds'),
('parts/D/code/check_small_group_obstruction.py','11 alternating-group coordinate-count cases, degrees5–15; fixed-index smallness is proved separately','parts/D/code/check_small_group_obstruction_output.json','elapsed_seconds'),
('parts/D/code/check_pronilpotent_obstruction.py','A5:3600 multiplication pairs,60 inverses,3600 commutator pairs,59 nontrivial normal closures and12 pigeonhole certificates','parts/D/code/check_pronilpotent_obstruction_output.json','elapsed_seconds'),
('code/verify_A_finite.py','19 exact checks; four prime cases and cohomology degrees 0–12; 1,024 Laurent forms; 11 independent negative-form classes','code/output/verify_A_finite.json','seconds'),
('parts/B/code/finite_certificates_B.py','Three alpha-group cases, 38 monomials; two finite-field elliptic cases, 70 nonzero projective triples','parts/B/code/output/finite_certificates_B.json','elapsed_seconds'),
('parts/B/code/imperfect_graph_certificate_B.py','24 symbolic identities across primes 2, 3 and 5; Frobenius graph, derivative and normalization checks','parts/B/code/output/imperfect_graph_certificate_B.json','elapsed_seconds'),
('parts/C/code/check_counterexamples.py','17 exact algebra/module checks; geometric assertions are proved separately','parts/C/output/check_counterexamples.json','elapsed_seconds'),
('parts/C/code/check_field_descent.py','All nine group vectors, four subgroup lines, 25 finite-field elements; quartic automorphism and isogeny identity','parts/C/output/check_field_descent.json','elapsed_seconds'),
('parts/C/code/check_pointing_and_detection.py','25 elements of F25; 12 proper subgroups of cyclic groups of orders 2–8','parts/C/output/check_pointing_and_detection.json','elapsed_seconds'),
('parts/D/code/check_d10_nonconstructible.py','Finite auxiliary fibre-product rings of 8–256 elements; C2 sign projectors over F3; tail and localization witnesses','parts/D/code/check_d10_nonconstructible_output.json','elapsed_seconds'),
('parts/D/code/check_prop5_chain.py','90,114 character values across 12 finite component families; 13 distinct level obstructions; two candidate two-sheet bijections per level','parts/D/code/check_prop5_chain_output.json','elapsed_seconds'),
('parts/D/code/check_exceptional_wild.py','Nine rational identities in characteristic two; nine P1(F2) product points; exceptional residue action and inseparable residue extension','parts/D/code/check_exceptional_wild_output.json','runtime_seconds'),
('parts/D/code/check_examples_extended.py','25 F25 elements and 24 inverses; C2 idempotents; nine affine F3 elliptic points tested; C2 common-refinement orbit obstruction','parts/D/code/check_examples_extended_output.json','runtime_seconds'),
('parts/D/code/check_examples.py','729 F9 triples, eight inverses, nine wreath quotients, five finite nominal-set cases, six wild-DVR identities','parts/D/code/check_examples_output.json','runtime_seconds')]
for program,scope,path,key in certs:
    p=root/path
    if p.exists():
        d=json.loads(p.read_text());table.append(f'| {program} | {scope} | {d[key]:.9f} |')
table.extend(['','### Recorded download, extraction, build and execution runs','',
              '| Run record | Command | Seconds | Exit |','|---|---|---:|---:|'])
for row in rows:
    command=row['command'].replace('|','\\|')
    table.append(f"| {row['record']} | {command} | {row['seconds']:.6f} | {row['returncode']} |")
table.extend(['','Agent-specific source-acquisition and preparation programs have their complete per-source results in parts/B/code/output, parts/C/output, and parts/D/code/*_output.json. Inline exploratory read commands are documented by retained source extracts and notes; they are not counted as finite certificates.',''])
(root/'PROGRAM_RUNS.md').write_text('\n'.join(table))
print(json.dumps({'root_run_records':len(rows),'certificate_programs':len(certs)}))
