# Writes the full-intake check events of RESEARCH_SA09 (final 20261119T1146Z), 22 Nov 2026.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803.
import collections, sys
sys.stdout.reconfigure(encoding='utf-8')
D = 'C:/Users/user/Documents/results_register/horizontal/sweep3/SA09/'
W = ('Claude Opus 5.5 at effort max, agent a34c04448e8299803, full intake (21-22 Nov 2026) of RESEARCH_SA09 final '
     '20261119T1146Z (GPT-6 Astra, ChatGPT Pro mode)')
TP, IR, CO, BG = ('targeted proof check', 'independent re-proof', 'computation or formal certificate',
                  'carried as background without fault found')
S = 'sections/'
E = [
 ('A1.1', BG, 'Roby: Pol^d(M,N) = Hom(Gamma^d M, N) for arbitrary modules, and the exponential law (A1.2); standard; the run\'s locators (Roby 1963, Thm IV.1, III.3, III.4) not opened by me.', S + 'A1.tex l.15-45'),
 ('A1.2', TP, 'confirmed: (A1.3) by evaluation at gamma_pq(x): gamma_q(f(gamma_p x)) = Gamma^q(f)(gamma_q gamma_p x) = Gamma^q(f) alpha_{q,p}(gamma_pq x); (A1.4) from the divided-power sum formula with Delta and mu; category axioms are identities of laws after every scalar extension.', S + 'A1.tex l.47-129'),
 ('A1.3', IR, 'confirmed (also INT-SA09-E11): over F_2, dim Hom(Gamma^2 k, k^2) = 2 against dim Gamma^2(k^2) = 3; P_k has no initial object (constant laws 0, 1 into k), Gamma^d P_k has a zero object for d > 0 and Hom sets k for d = 0, so no equivalence; the bridge (a degree-d law action on linear Hom = a linear map out of Gamma^d Hom) is A1.1.', S + 'A1.tex l.131-184'),
 ('A1.4', TP, 'confirmed: L_R(sum r_j f_j) = sum_{|a|=p} r^a T_a is well defined (sum relation; mu_{a,b} Delta_{a,b} = C(a+b,a) on Gamma^{a+b}; Gamma^a(lambda f) = lambda^a Gamma^a(f)); composition checked over Z[s,t] with independent indeterminates and specialized; no base change of Hom assumed.', S + 'A1.tex l.186-244'),
 ('A1.5', TP, 'confirmed: Lambda^* over F_2 with alpha_{p,q} summing over unordered partitions into p blocks of q is well defined (coinciding inputs: same-block terms vanish, cross-block terms pair off under the transposition, characteristic 2), associative by nested partitions, and Lambda^2 k = 0, so alpha_{2,0} is not an isomorphism.', S + 'A1.tex l.271-310'),
 ('A1.6', TP, 'confirmed: c_{p,q} = t_pq/(t_p t_q^p) satisfies c_{p,qr} c_{q,r}^p = c_{pq,r} c_{p,q} (both t_pqr/(t_p t_q^p t_r^pq)), c_{1,q} = c_{q,1} = c_{0,q} = 1, alpha\'_{2,0} = -alpha_{2,0}; strict mixed comparison gives m(e0,e0) = e0, the homogeneous formula -e0, contradiction over F_3. Rests on the run\'s type-correct reading (A1.8) of the doubtful superscript on 137:81.', S + 'A1.tex l.312-365'),
 ('A1.7', TP, 'carried from INT-SA09-E16: the repair (comonad and co-Kleisli conditions on B_m = sum G^i, the multigrading and the normalization A1.12N) is a correct characterization; the equivalence-of-categories converse is asserted in two sentences.', S + 'A1.tex l.367-517'),
 ('A1.8', TP, 'confirmed: for V in internal degree 1, G^3 V = D^3 V + V with G^3(f) = f on the second summand; a natural cubic law would be entrywise cubing, and (x+y)^3 = x^3 + y^3 fails in F_4 at x = 1, y = omega. Associativity of (A1.14) accepted from the run\'s cancellation argument, not rechecked line by line.', S + 'A1.tex l.519-591'),
 ('A1.9', IR, 'confirmed: eigenspace formula (A1.15) by components; valuations (A1.16) by the cyclic unit group mod l, lifting the exponent at odd l, and v_2(lambda^h-1) = v_2(lambda-1)+v_2(lambda+1)+v_2(h)-1; separation over k[t] and over F_q.', S + 'A1.tex l.595-699'),
 ('A1.9', CO, 'confirmed: v_l(D_{n,m}) against gcd_{0<=lambda<=400} |lambda^n - lambda^m| for 1 <= m < n <= 14 and l <= 31: 1001 tests, 0 mismatches.', 'SA09/intake_scripts/full_intake_sa09_checks.py'),
 ('A2.1', IR, 'confirmed (also INT-SA09-E13): S_0 projective; a chain retraction D_0 -> S_0 has r_0 o 1 = 0, so 0 -> S_0 -> D_0 -> S_1 -> 0 does not split; disks projective and injective.', S + 'A2.tex l.30-55'),
 ('A2.2', TP, 'confirmed: T_C(L) = ker delta_L(C) with Hom(b, T_C(L)) = Hom_Ch(L^vee, C_b); copresentation 0 -> L -> I(L) -> Q(L) -> 0 (j(x) = (x, dx) a chain map, q(x,y) = y - dx); relative left exactness gives F(L) = ker(F(IL) -> F(IQL)) = delta_L.', S + 'A2.tex l.65-131'),
 ('A2.3', TP, 'confirmed: Smith normal form splits a bounded finite-free complex over a PID into stalks and R -a-> R; counterexample: K_{0,2} would represent ker(2: Z/4 -> Z/4) = {0,2}, of order 2, never 4^r, so it does not exist in finite free Z/4-modules.', S + 'A2.tex l.133-196'),
 ('A2.4', TP, 'confirmed in structure: abelian case by the finite filtration of Hom(L^vee, C) (no positive cohomology when H^{>0}(C) = 0); exact case through Buehler\'s embedding (Thm A.1) and an induction by pullbacks; strong version by cancellation of inflations (dual of Buehler Prop. 7.6). Buehler\'s statements not opened.', S + 'A2.tex l.198-317'),
 ('A2.5', CO, 'confirmed: G = {(x,y): x = 2y mod 4} in Z/16 + Z/4 has order 16, exponent 8, (2,1) of order 8, kernel of the projection {(4t,0)} = Z/4; a Sigma-sequence with ends Z/4 has middle exponent 4 (split) or 16 (e).', 'SA09/intake_scripts/full_intake_sa09_checks.py'),
 ('A2.6', BG, 'classical (Happel; Buehler Ex. 13.8, Thm 13.7, not opened): bounded complexes with degreewise split sequences form a Frobenius category with stable category K^b; the run\'s outline (contractible = projective-injective; null-homotopic = factors through the cone) checked.', S + 'A2.tex l.380-424'),
 ('A3.1', TP, 'confirmed: rank (R_n)_m = C(m+n+1,n+1) = sum_i C(m,i) C(n+1,i), so rank N_i = C(n+1,i), 0 <= i <= n+1; extra degeneracy gives split acyclicity; Hom(L, R_n) = Hom(L_n, Z). Vandermonde identity computed for m, n <= 15.', S + 'A3.tex l.14-86'),
 ('A3.2', TP, 'carried from INT-SA09-E08: rho_{p,M} by evaluation; mu from the cross term of rho_2; F_X(R_n) = Z^{X_n}; F_X as an equalizer. Holds as stated; it reads the structure of 137:38 as the natural action on all tests.', S + 'A3.tex l.87-219'),
 ('A3.3', BG, 'Horel Thm 5.4 (arXiv:2211.02349v2), Mandell 2006 Main Thm, Toen 2020 Cor. 5.1, 5.4, 5.5; locators not opened; the reduction to connected components by the idempotents of H^0 checked; agrees with RESEARCH_SA08 A-018, D006M (INT-SA09-E09).', S + 'A3.tex l.220-300'),
 ('A3.4', IR, 'confirmed (also INT-SA09-E10): L(5,1), L(5,2) have the same cochain quasi-isomorphism type, cohomology ring and divided powers; a homotopy equivalence would need 2 = eps u^2 mod 5, impossible.', S + 'A3.tex l.302-361'),
 ('A3.5', IR, 'confirmed (also INT-SA09-E14): C(a,2) is not natural under Z -> F_2 (inputs 0 and 2); 1 = 2 gamma_2(1) impossible in Z.', S + 'A3.tex l.362-376'),
 ('A4.1', BG, 'Dold-Puppe decomposition L_n = sum_i N_i^{C(n,i)}; the count C(n,i) of increasing surjections re-derived; locators (Dold-Puppe (3.3), Thm 3.6, Cor. 3.8) not opened.', S + 'A4.tex l.10-35'),
 ('A4.2', IR, 'confirmed (also INT-SA09-E12): f_p(n) = sum_i C(n,i) a_i(p) with nonnegative a_i; a_j > 0 for j > D gives growth C(n,j); Nakayama at maximal ideals.', S + 'A4.tex l.36-75'),
 ('A4.3', BG, 'Stacks Tag 066Z (not opened); the run\'s quasi-compactness argument for regular rings of unbounded Krull dimension (opens where a syzygy is locally free cover Spec R) checked.', S + 'A4.tex l.76-110'),
 ('A4.4', IR, 'confirmed: M_i = Z/p_i gives fibre dimensions C(n,j) at (p_j), unbounded degrees, nonperfect; sum of disks D_i is perfect with rank L_n = 2^{n+1} - 1 (computed for n <= 20).', S + 'A4.tex l.111-155'),
 ('A4.5', IR, 'the counterexample confirmed: over F_2[eps]/eps^2 the eps-periodic resolution gives Tor_i(F_2,F_2) = F_2 for all i, so bounded normalization does not give perfection; the criterion itself is Stacks Tag 0G99 (not opened).', S + 'A4.tex l.156-230'),
 ('A4.6', TP, 'confirmed: fibre dimension constructible through minors; rank N_i = mu_i + mu_{i+1} + beta_i + beta_{i+1} + nu_i by counting block contributions; strict against derived perfection criteria.', S + 'A4.tex l.231-290'),
 ('B0.1', BG, 'dessins and permutation pairs (Schneps Lemma I.1, Thm I.5; Jones Thm 1): standard; not opened by me.', S + 'B1_B2_B3.tex l.17-58'),
 ('B1.1', IR, 'confirmed (also INT-SA09-E06): pinnings of C form a Gamma_T-torsor, isomorphic exactly when they differ by I_C, so C contributes gamma_T/|I_C| = gamma_T |K_C|/|A_C|.', S + 'B1_B2_B3.tex l.60-96'),
 ('B1.2', IR, 'confirmed (also INT-SA09-E06): E = Z/4, rho = +1, alpha = +2: A_C = C_4, K_C = C_2, |I_C| = 2, gamma_T = 2: one pinned class against the naive two.', S + 'B1_B2_B3.tex l.98-126'),
 ('B1.3', TP, 'confirmed: automorphisms act freely; a nontrivial kernel element is alpha, preserving each rho-cycle, so rho is one 2m-cycle and alpha = rho^m; phi = rho^{m-1} has gcd(2, m-1) cycles and alpha preserves them iff m is even; m = 2g, one face, genus g.', S + 'B1_B2_B3.tex l.128-166'),
 ('B2.1', CO, 'confirmed (INT-SA09-E01): h mod G_c = Pz + Q with P = -delta p/7776, Q = c(5c-8)(25c^3-6c^2+8)/2592, 36 disc(G_c) = delta.', 'SA09/intake_scripts/intake_checks_sa09_B.py'),
 ('B2.2', CO, 'confirmed (INT-SA09-E02): on p = 0, Q = (32-52c-c^2)/1500; equal nonzero critical values at the three roots.', 'SA09/intake_scripts/intake_checks_sa09_B.py'),
 ('B2.3', CO, 'confirmed (INT-SA09-E03): 18 solutions in S_6, 3 classes, trivial automorphisms; the run\'s triples valid and non-conjugate.', 'SA09/intake_scripts/intake_checks_sa09_B.py'),
 ('B2.4', CO, 'confirmed (INT-SA09-E04): minimal polynomial of (4+18r+6r^2)/25 is p; disc p = -108 x 216^2; S_3 orbit, one real map and a mirror pair.', 'SA09/intake_scripts/intake_checks_sa09_B.py'),
 ('B2.5', CO, 'confirmed (INT-SA09-E05): roots of delta 16/25 +- 12i/25; passport [3,2,1;3,1,1,1;6] has 2 dessins.', 'SA09/intake_scripts/intake_checks_sa09_B.py'),
 ('B3.1', TP, 'confirmed: G_cell -> K_C split with kernel H; positive genus: H finite (Aut of a stable pointed curve, Wendl Cor. 4.2.7, not opened) with positive derivative, so trivial; genus 0: three vertices force the identity, two give the oranges (rays, equally spaced, group R_{>0}), one gives the one-loop sphere (group Aff+(R)).', S + 'B1_B2_B3.tex l.428-524'),
 ('B3.2', TP, 'confirmed: b_n - 1 = -(z^n+1)^2/(z^n-1)^2; the graph is z^n in R_{<=0} (discriminant 16(1-s)); X_g: y^2 = x^{2g+1}-x with beta = x^{2g} of degree 4g, regular cyclic monodromy via (x,y) -> (zeta^2 x, zeta y), zeta = zeta_{4g}, involution (x,-y) its 2g-th power.', S + 'B1_B2_B3.tex l.526-573'),
 ('B3.3', TP, 'confirmed: Belyi functions with the same cells form an H-torsor; the genus-1 involution acts by -1 on H_1, so cellwise is not isotopic; face centres +-i and white point 0 in case I.', S + 'B1_B2_B3.tex l.575-611'),
 ('B3.4', TP, 'confirmed under its stated hypotheses: a nontrivial combinatorial kernel forces a compact surface; on the disk Schwarz lemma, on C* inversion has derivative -1, on C a dilation with multiplier not 1 has unbounded orbits.', S + 'B1_B2_B3.tex l.613-650'),
 ('B4.1', TP, 'carried from INT-SA09-E07 (proof read in full: Eisenstein, real Galois subfield, s <= 2; sqrt2 in Q(zeta_N) iff 8 | N) with the computation at N = 4, 8 (x^8-2 = (x^4-sqrt2)(x^4+sqrt2) over Q(i,sqrt2)).', S + 'B4.tex l.19-89'),
 ('B4.2', TP, 'confirmed: r_N = zeta_{2N} theta_N^{-1} has r_N^N = -1/2; sigma(r_N)/r_N = zeta_N^{(a-1)/2-b}; t(aa\') = t(a) + a t(a\') makes (a,b) -> (a, t(a)-b) an automorphism; the parity condition becomes (-1)^c = chi_{-2}(a).', S + 'B4.tex l.90-127'),
 ('B4.3', TP, 'confirmed: normalizing u_i = 1 the other coordinates have N-th power -1/2; diagonal image of order N phi(N)/d_N, index N d_N in the scalar affine group; table entries at N = 1, 2, 4, 8 consistent.', S + 'B4.tex l.128-202'),
 ('B4.4', TP, 'confirmed: from Schinzel (a^{w_N} in K^{xN} for abelian radicals) and the S-unit lattice, N divides D v_j, so the Kummer pairing puts D(Z/N)^r in the image; openness also from Perucca-Sgobba. Schinzel 1977 Thm 2, Milne ANT Thm 5.11, Perucca-Sgobba Thm 1 not opened.', S + 'B4.tex l.203-328'),
]
with open(D + 'INTAKE_RESEARCH_SA09_20261121_full_CHECK_EVENTS.tsv', 'w', encoding='utf-8', newline='') as f:
    f.write('statement_id\tdate\twho\ttype\toutcome\twhere\n')
    for sid, typ, out, where in E:
        f.write('\t'.join([sid, '2026-11-22', W, typ, out, where]) + '\n')
c = collections.Counter(t for _, t, _, _ in E)
ids = sorted({s for s, _, _, _ in E})
print(len(E), 'events;', len(ids), 'statements;', dict(c))
