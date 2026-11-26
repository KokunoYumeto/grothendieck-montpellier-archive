# Writes INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv for the Derivateurs cluster (Claude Opus 5.5 at effort high, 24 Nov 2026).
import os
PILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WHO = 'Claude Opus 5.5 at effort high (intake pile 24 Nov 2026, Derivateurs cluster reader)'
D = '2026-11-24'
HDR = ('statement_id', 'date', 'who', 'type', 'outcome')
ev = {
'S2COUNT': [
 ('A.M1', 'targeted proof check', 'Every step of thm:Mr-wedge followed (sections/A_agent.tex): sphere map s_w on S^1*(S^0)^{*(n-1)}, each colour face matched to the bar face d_i (all relevant products equal e), orientation chain = z_w; simple connectivity; Whitehead. No fault found.'),
 ('A.M3', 'computation or formal certificate', 'Own program DERIVATEURS_checks/s2count_monoid_homology.py: normalized bar complex ranks over Q, F2, F3: r=0 H_2 only (degrees 1-5); r=1 rank 1 in degrees 2-5; r=2 ranks 1,2,4 in degrees 2-4; no 2- or 3-torsion. Agrees with H_n = Z^{r^{n-2}}.'),
 ('A.M5', 'targeted proof check', 'Cocycle identities alpha(mm\')=alpha(m\'), beta(mm\')=beta(m), Y_s(mm\')=0 and the Kronecker pairing f_w(z_v)=delta followed. No fault found.'),
 ('A.M6', 'targeted proof check', 'Gluing of the 2^n simplices checked face by face (faces 0 and 1 pair by the first bit, face i by bit i, face n by the last bit). No fault found.'),
 ('B:main', 'targeted proof check', '[BM,Y] = prod_{n>=2} pi_n(Y) for simply connected Y; Serre for infinitely many non-zero pi_n(S^3); Hopf fibration for S^2; finite-category sequential colimits give countable sets. Sound (Serre 1953 not opened).'),
 ('B:smallmonoids', 'targeted proof check', 'Rees-matrix case analysis followed; order 5 with |I|,|J|>=2 forces 1+(2x2). Supported by own census (residue_a5_monoid_census.py: 228 monoids of order 5, exactly one with non-zero rational H_1-H_3). Sweeney 2025 Thm 2.7 not opened.'),
 ('B:smallcategories', 'targeted proof check', 'Case analysis checked: two objects both ways (retract; at most six arrows argument), one-way c=1 (join; BC2*BC2 via Miller), c=2 (cofibre of B(S//L)->BL: BC2, S^1 v Sigma BC2, point, S^1), c=3 (S^1 v S^1), three objects (contractible). Sound modulo Miller 1984 Thm A (not opened).'),
 ('CD:wedgecriterion', 'targeted proof check', 'Pointed classes = prod pi_j, free classes = pi_1-orbits; distinct supports in distinct orbits. Sound.'),
 ('CD:alltargets', 'targeted proof check', '(i)=>(ii) via BM_1 = wedge of spheres and face posets of finite complexes; (ii)=>(i) via restriction to the (n_c+1)-skeleton; (ii)<=>(iii) by countable subcomplex enlargement. Sound.'),
],
'RESIDUE': [
 ('A.5', 'computation or formal certificate', 'Own program DERIVATEURS_checks/residue_a5_monoid_census.py: monoids of order 1-5 up to isomorphism 1, 2, 7, 35, 228 (labelled with identity fixed: 1, 2, 11, 156, 4122); of the 228 of order 5 exactly one (the rectangular-band monoid 1+(2x2)) has non-zero rational homology in degrees 1-3 (H_2 = Q). Agrees with the row; the 1-type assertion for the other 227 is checked only to the extent that their rational H_1-H_3 vanish.'),
],
'FREX': [
 ('A.13', 'targeted proof check', 'Every step followed (sections/A.tex A:equivalence-primes): blocks labelled j..j+m-1 mod m, rho(t alpha_j) = rotation of w by j, free Z/m action on ordered tuples of distinct classes, aug(t) in mR. Sound.'),
 ('A.23', 'targeted proof check', 'Second reading (first: Claude Opus 5.5 at effort max, 19 Nov): Zucker 2016 Thm 8.14 gives a precompact Ramsey expansion, invariant probability on the completion of G/H, Hamel functional R->Q with l(1)=1, signed averaging A.9. Sound modulo Zucker (not opened) and the run\'s Ramsey => exact step.'),
],
'REVLOC': [
 ('F.1', 'targeted proof check', 'Every step of the proof in sections/F12.tex followed: W-dagger strongly saturated (inverse image of isomorphisms under functors through Hot), aspherical objects contractible, absolute Loc (3) by Quillen A; witness: face posets of suspended polygons L8 -> L4 of degree 2 (|P| = 50, |Q| = 26 recounted: 10+24+16, 6+12+8; collages 77 and 53), B(int D) = mod-2 Moore space, so Tor H_2 fails; Loc (6\'a) fails on the same collage; Loc (8), (9) argued. Sound. The run\'s program FGH_literal_axioms.py not run.'),
 ('G.7', 'targeted proof check', 'Every step of sections/G7_compactness.tex followed: Tot(R^{q+1}K) Kan model of the 2-completed sphere with compact metrizable levels, Reedy fibrancy by the matching-map splitting, compactness lemma C_A = intersection of C_{L,A}, countable enlargement and nested-extension argument, rational acyclicity enlargement. Sound; Bousfield 2003 section 7.7 not opened.'),
],
'DER_LOCALIZERS': [
 ('B.4', 'computation or formal certificate', 'Own program DERIVATEURS_checks/derloc_b4_s3_extension.py: no psi: F(a,b) -> S3 with psi(a) = (23), psi(b[a,b]) = (12), for both commutator conventions; so the assignment does not factor through phi: a->a, b->b[a,b] (an H_1-isomorphism). Confirms the group step of the run\'s non-extension.'),
 ('A5.3', 'targeted proof check', 'Key homological step re-derived: the mapping torus T of a degree-2 self-map of S^2 has pi_1 = Z and H_*(T) = H_*(S^1), while its universal cover has H_2 = Z[t^{+-1}]/(2t-1) = Z[1/2]; so S^1 -> T is a Pi_1- and integral homology equivalence but not a weak equivalence, and a coproduct over N has infinitely many bad components. Agrees with the run; the 58-object certificate not recomputed.'),
],
'BISITE': [
 ('A.32', 'targeted proof check', 'Every step followed (sections/A.tex:434): W-dagger = pi_0-bijection and W_inf on connected categories satisfies literal Loc (1) (moderate saturation), (2), (3); u: E x BC_2 -> E over BC_2 not in W-dagger while u/c (two contractible components on each side) is; W-dagger fails Loc (1 bis). Sound.'),
 ('G.7', 'independent re-proof', 'For S = BC_2, k = F_2: p_* = homotopy fixed points; sum_n Sigma^n HF_2 = prod_n Sigma^n HF_2, so pi_0 p_*(sum) = prod_n H^n(BC_2;F_2) while sum_n pi_0 p_*(Sigma^n HF_2) = sum_n F_2; countable coproducts are not preserved. Agrees with the run.'),
 ('E.2', 'targeted proof check', '{1} -> [1] is right anodyne (the horn Lambda^1_1), hence a contravariant (presheaf) equivalence over [1]; its pullback along {0} -> [1] is the empty category -> e. Sound.'),
],
}
for run, rows in ev.items():
    path = os.path.join(PILE, 'INTAKE_%s_20261124_CHECK_EVENTS.tsv' % run)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write('\t'.join(HDR) + '\n')
        for sid, typ, out in rows:
            f.write('\t'.join([sid, D, WHO, typ, out.replace('\t', ' ')]) + '\n')
    print(path, len(rows))
