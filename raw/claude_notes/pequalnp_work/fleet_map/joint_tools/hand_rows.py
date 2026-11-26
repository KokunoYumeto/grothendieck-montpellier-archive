# -*- coding: utf-8 -*-
"""Hand-entered rows of our side (today's pequalnp work, Codex desk results, board items, WB-0002, questions, context).
Statements are quoted or minimally condensed from the named files; locators give the full text."""
PW = '<local>/pequalnp_work\\'
DESK = PW + 'desk\\'
CX = '<local>/Documents\\Codex\\2026-11-22\\the-two-tracks-share-no-sound\\'
HEX = '<local>/Documents\\field_experts\\hexagon\\HEXAGON_BOARD.tsv'
WB = '<local>/Documents\\mathematics_workbenches\\geometric-complexity-theory-workbench\\work\\WB-0002\\v0.1\\'
CLAUDE_MAX = 'Claude Opus 5.5 at effort max'
AGENT = 'Claude Opus 5.5 at effort max (agent a3533d80e4df973c2)'
CODEX = 'GPT-6.2 Astra at reasoning effort ultra (Codex; model and effort read from the turn_context of its 23 Nov rollouts)'

R = []


def row(id, statement, status, proof_link, topics, title='', depends_on='', used_by='', notes='', source='', formal=''):
    R.append(dict(id=id, side='ours', statement=statement, status=status, proof_link=proof_link, topics=topics,
                  title=title, depends_on=depends_on, used_by=used_by, notes=notes, source=source or proof_link,
                  formal_statement=formal))


MBR = PW + 'MAPPING_BY_READING_20261123.md'
MAR = PW + 'MAPPING_AGENT_RESULTS.md'
row('PNP-MBR:A1', 'Lemma K. If W is a complex linear subspace of C^M with sum_i x_i^2 = 0 and sum_i x_i^4 = 0 for every x in W, '
    'then 3 dim W <= M; sharp at blocks (1, w, w^2), w a cube root of unity. Proof: U = W*W is totally isotropic and orthogonal to 1; '
    'St = stabilizer of U is spanned by block indicators; 2 dim U + s <= M; Kneser for codes gives 2 dim W <= dim U + s; blocks of size <= 2 '
    'are deleted by induction; otherwise s <= M/3.',
    'proved (' + CLAUDE_MAX + ', session 672ae3a0); Lean proof builds on branch L-gct-122 of the clone (axioms propext, Classical.choice, '
    'Quot.sound); PR brilliant-hq/pequalnp-proofs#874 opened 15:13 UTC and closed unchecked by their bot 15:14 UTC (step stood down)',
    MBR + ' lines 13-29; Lean: ' + PW + 'pequalnp-proofs\\lean\\PEqualNP\\Outside\\L_gct_122.lean (branch L-gct-122, commit 9f29749)',
    'level spaces; power-sum lemmas', title='Lemma K (p2 = p4 = 0 implies 3 dim W <= M)', used_by='PNP-CODEX:LemmaK-stability; PNP-CODEX:Klein-rows; PNP-LEAN:L-gct-122')
row('PNP-LEAN:L-gct-122', 'Lean 4 proof of the exact posted statement of L-gct-122: for all m and X : Submodule C (Fin m -> C), '
    '(forall x in X, sum_i x_i^2 = 0) -> (forall x in X, sum_i x_i^4 = 0) -> 3 * finrank C X <= m.',
    'proved in Lean (builds locally against Lean 4.36.0 / their Mathlib pin; axioms propext, Classical.choice, Quot.sound; '
    + CLAUDE_MAX + '); not accepted by their checker: PR #874 closed unchecked',
    PW + 'pequalnp-proofs\\lean\\PEqualNP\\Outside\\L_gct_122.lean (375 lines; branch L-gct-122, commit 9f29749; imports PEqualNP.Gct.L065)',
    'level spaces; power-sum lemmas', title='Lean proof of L-gct-122', depends_on='PNP-MBR:A1',
    formal='forall (m : N) (X : Submodule C (Fin m -> C)), (forall x in X, sum i, x i ^ 2 = 0) -> (forall x in X, sum i, x i ^ 4 = 0) -> 3 * Module.finrank C X <= m')
row('PNP-MBR:A2', 'The riffle rank of [a=b][c=d] on [n]^4 is at least 2n - 1, as an instance of GCT_GINEQ F-13 (image substitution): '
    'flatten pairId on a; the image {phi (x) I_n} has dimension q = n; every atom C(b,c)D(b,d) has b-slices of rank <= 1 while a nonzero '
    'phi (x) I has a slice of rank n, so >= n atoms; F-13 gives >= n + n - 1.',
    'proved on paper (' + CLAUDE_MAX + '); unchecked; superseded by PNP-MAR:3 (2n)', MBR + ' lines 31-41', 'riffle rank; border rank',
    title='L-gct-139 as an instance of GINEQ F-13', depends_on='GCT_GINEQ:F-13')
row('PNP-MBR:A3', 'Quadratic layer of the level-space problem (from GCT_KRON O-011): perm(J + t) = sum_k (n-k)! S_k(t); at J the Hessian is '
    '(n-2)! B with B = (J - I) (x) (J - I), eigenvalues (n-1)^2 on J, -(n-1) on the 2(n-1)-dimensional row/column part, +1 on V (x) V. '
    'Hence S_2 is nondegenerate on {S_1 = 0}: every level space has dim <= floor((n^2-1)/2); doubly centred level spaces '
    'dim <= floor((n-1)^2/2); p x q level spaces dim <= floor((pq-1)/2) (Hessian proportional to (J_p - I_p)(x)(J_q - I_q)).',
    'proved on paper (' + CLAUDE_MAX + '; the Hessian computation is GCT_KRON O-011, checked in-run); unchecked as a level-space statement',
    MBR + ' lines 43-61', 'level spaces', title='O-011 Hessian as the quadratic layer of level spaces', depends_on='GCT_KRON:O-011',
    used_by='PNP-MAR:1.1d; PNP-MAR:1.2')
row('PNP-MBR:A4', 'Route (not carried out): BR_PENCIL\'s generalized border substitution BR(T) >= q - j + min_{W in Gr(j,U)} BR(P_W), its '
    'torus degeneration P-01 and the order-ideal reduction P-07 apply to the border version of riffle rank (the atoms A(a)C(b,c)D(b,d) are '
    'preserved by the diagonal torus on b), giving riffle(pairId_n) >= n - j + R(j,n), R(j,n) the riffle length of sum_{h<=j} e_h(x)e_h(x)I_n; '
    'R(2,n) lies in [n+1, 2n]; R(2,n) >= 2n - 1 would give 3n - 3.',
    'conjecture / proposed route (' + CLAUDE_MAX + '); the torus step for border riffle rank and R(2,n) are unproved',
    MBR + ' lines 63-74', 'riffle rank; border rank', title='BR_PENCIL machinery for riffle rank beyond 2n',
    depends_on='BR_PENCIL:P-01; BR_PENCIL:P-07; BR_PENCIL:P-08; BR_PENCIL:R-01')
row('PNP-MAR:1.1a', 'On doubly centred n x n matrices (zero row and column sums), S_2 = p_2/2 and S_3 = (2/3) p_3 for every n, '
    'S_k the sum of k x k subpermanents and p_k the k-th power sum of the entries (Moebius inversion over set partitions of row and column slots; '
    'singleton blocks give line sums that vanish).',
    'proved on paper (' + AGENT + '); numerics n = 4, 5, 6 (checkS.py); unchecked by a second reader',
    MAR + ' section 1.1 (lines 22-33)', 'level spaces', title='S_2 and S_3 on doubly centred matrices', used_by='PNP-MAR:1.2')
row('PNP-MAR:1.1b', 'On doubly centred n x n matrices: 24 S_4 = 36 p_4 - 18 sum_i (sum_j t_ij^2)^2 - 18 sum_j (sum_i t_ij^2)^2 + 3 p_2^2 '
    '+ 6 tr((t t^T)^2).', 'computed (numerics n = 4, 5, 6; ' + AGENT + ')', MAR + ' section 1.1 (line 31)', 'level spaces',
    title='Order-4 identity on doubly centred matrices')
row('PNP-MAR:1.1c', 'On all of {S_1 = 0} (row sums r, column sums c, row and column square sums r2, c2): S_3 = (2/3) p_3 - sum_i r2_i r_i '
    '- sum_j c2_j c_j + sum_ij t_ij r_i c_j + (sum r^3 + sum c^3)/3.', 'computed (numerics n = 4, 5, 6; ' + AGENT + ')',
    MAR + ' section 1.1 (lines 32-33)', 'level spaces', title='S_3 on the hyperplane S_1 = 0')
row('PNP-MAR:1.1d', 'Real level spaces have dimension <= 2n - 2 (on real DC, S_2 = |t|^2/2 > 0, so the real core is 0). For a complex level '
    'space L, L meet conj(L) is the complexification of a real level space, so it has dimension <= 2n - 2; the core K = L meet DC satisfies '
    'K meet conj(K) = 0: the complex problem lives in the totally non-real part.',
    'proved on paper (' + AGENT + '); unchecked', MAR + ' section 1.1 (lines 35-39)', 'level spaces',
    title='Real case and the non-real part', depends_on='PNP-MBR:A3')
row('PNP-MAR:1.2', 'LS(n) <= n^2/3 + 2n: on the core K = L meet DC, p_2 = 2 S_2 = 0 and p_3 = (3/2) S_3 = 0, so L-gct-061 gives '
    '3 dim K <= n^2, and L-gct-092 adds 2n. Improves the quadratic-layer bound floor((n^2-1)/2) for n >= 13; up to the constant it is the most '
    'that Taylor orders <= 3 can give.',
    'proved on paper (' + AGENT + '); unchecked; inputs L-gct-061, L-gct-092 checked in Lean on their side',
    MAR + ' section 1.2 (lines 41-47)', 'level spaces; border dc', title='Cubic layer: LS(n) <= n^2/3 + 2n',
    depends_on='PNP-MAR:1.1a', used_by='PNP-CODEX:LS-sharp')
row('PNP-MAR:1.3a', 'Root-of-unity block family F_q (q | n, rows (I,a), t((I,a),j) = w^a c_I(j), dim n^2/q): S_k vanishes on F_q unless q | k, '
    'and S_q = (-1)^(q-1) q! sum_I e_q(c_I); on the truncated family F_(q,r) (q | r <= n), S_k vanishes unless q | k and k <= r.',
    'proved on paper (' + AGENT + '); numerics blockfam.py, blockfam2.py', MAR + ' section 1.3 (lines 49-66)', 'level spaces',
    title='Root-of-unity block families')
row('PNP-MAR:1.3b', 'How many Taylor orders a proof needs: if a set Omega of orders has the property that S_k = 0 on L for all k in Omega '
    'implies dim L <= C n, then for every q with (C'' + 1) q <= n (C'' = floor C) Omega meets {q, ..., (C''+1)q}, so '
    '|Omega| >= floor(n/(C''+1))/(C''+1): a linear bound needs linearly many distinct Taylor orders.',
    'proved on paper (' + AGENT + '); unchecked', MAR + ' section 1.3 (lines 68-77)', 'level spaces',
    title='Taylor-order lower bound for proofs of a linear level bound', depends_on='PNP-MAR:1.3a', used_by='PNP-CODEX:Taylor-count')
row('PNP-MAR:1.4', 'Self-similarity: for t in F_q, perm(J + t) = (q!)^m sum over ordered partitions (C_1..C_m) of [n] into q-sets of '
    'prod_I (1 + (-1)^(q-1) prod_{j in C_I} c_I(j)). If each c_I is supported on a fixed (q-1)-set, perm(J + t) = n!: a level space of '
    'dimension n - n/q for every q dividing n.',
    'proved on paper (' + AGENT + '); numerics hyper.py at (n,q) = (6,3), (6,2), (4,2)', MAR + ' section 1.4 (lines 80-93)', 'level spaces',
    title='Hypergraph self-similarity on F_q', depends_on='PNP-MAR:1.3a')
row('PNP-MAR:1.5a', 'n = 4 in Klein (Walsh) coordinates t = F X F^T, X in Mat_3: p_2(t) = tr(X X^T), p_3(t) = (3/2) perm_3(X), '
    'perm_4(t) = (tr X X^T)^2/32 + Q(X)/16 with Q = tr((X X^T)^2) + 6 sum X_ab^4 - 3 sum_a (sum_b X_ab^2)^2 - 3 sum_b (sum_a X_ab^2)^2; '
    'the known 3-dimensional core is span(v e1^T, v\' e2^T, v e3^T), v = (1, w^2, -w), v\' = (1, w, -w^2).',
    'computed exactly (sympy, q4.py; ' + AGENT + ')', MAR + ' section 1.5 (lines 97-104)', 'level spaces', title='Rational chart at n = 4')
row('PNP-MAR:1.5b', 'Complex Levenberg-Marquardt searches: doubly centred 4 x 4 level spaces of dimension 4: 0 hits in 2000 restarts; '
    '4 x 4 level spaces of dimension 6: 0 in 2600 (plateau 2e-4, genuine local minima); evidence for kappa(4) = 3 and LS(4) = 5 over C, not proof.',
    'computed (numerical evidence; ' + AGENT + ')', MAR + ' section 1.5 (lines 105-113)', 'level spaces', title='Numerical evidence at n = 4')
row('PNP-MAR:1.5c', 'A doubly centred level family for every n of dimension n - 2: t = u (x) v with v = (1, z, ..., z^(n-1)), z a primitive '
    'n-th root of unity, u in V with u_1 = 0 (S_k(u (x) v) = k! e_k(u) e_k(v)); so kappa(n) >= n - 2.',
    'proved on paper (' + AGENT + ')', MAR + ' section 1.5 (lines 114-116)', 'level spaces', title='kappa(n) >= n - 2')
row('PNP-MAR:2a', 'At Sigma_m = J - m E_00: the Hessian quadratic form is Q(t) = (m-3)! [2(m-2) S_2(t) - 2m S_2(t_B)]; on T_y/Cy its signature '
    'is (+(2m-3), -(m-1)^2).',
    'computed and proved on paper (' + AGENT + '); checked m = 3..10 (sig_sigma.py), exactly at m = 4; independently re-derived and extended '
    'by Codex (PNP-CODEX:exceptional-row)', MAR + ' section 2 (lines 130-137)', 'border dc; level spaces',
    title='Second fundamental form of perm at Sigma_m', used_by='PNP-MAR:2b')
row('PNP-MAR:2b', 'Real case of L-gct-037 at Sigma_m: every real linear subspace W containing Sigma_m on which perm_m vanishes has dim W <= 2m - 2 '
    '(W lies in T_y and W/Ry is isotropic for a form of signature (2m-3, (m-1)^2)); with L-gct-113 the same holds for real y + L.',
    'proved on paper (' + AGENT + '); confirmed by Codex\'s independent inertia proof (PNP-CODEX:exceptional-row)',
    MAR + ' section 2 (lines 139-141)', 'border dc', title='Real 2m - 2 bound at Sigma_m', depends_on='PNP-MAR:2a')
row('PNP-MAR:2c', 'Over C the quadratic layer at Sigma_m gives only 1 + floor((m^2 - 2)/2) (8 at m = 4 where L-gct-036 needs 6); the excess sits '
    'in the doubly centred block, the level-space core of perm_(m-1); proposed: L-gct-036/037 at Sigma_m and L-gct-086 meet in the same core problem.',
    'refuted in its intended use: their checked L-gct-087 has a complex 7-dimensional space through Sigma_4, so Sigma_4 cannot witness L-gct-036 '
    '(Codex replayed L-gct-087 exactly)', MAR + ' section 2 (lines 142-144)', 'border dc; level spaces',
    title='Complex case at Sigma_m (route)')
row('PNP-MAR:3', 'Over every field, the riffle rank of pairId_n = [a=b][c=d] on [n]^4 is at least 2n for n >= 3; with L-gct-140 (six terms) '
    'riffle(pairId_3) = 6, the first exact value past n = 2 (Rossman, Question C.1). Proof: a decomposition of length 2n - 1 forces rank A = n, '
    'slices V_b = U Diag U^{-1}, blocks G_k with disjoint supports; W_b would be the same for every b, contradicting W_b meet W_b\' inside ker A.',
    'proved on paper (' + AGENT + '); Codex derived the same bound independently by a different argument and checked the 81 upper-bound '
    'coefficients of L-gct-140 over Z', MAR + ' section 3 (lines 146-165)', 'riffle rank', title='riffle(pairId_n) >= 2n; exactly 6 at n = 3')
# Codex desk results
row('PNP-CODEX:LemmaK-stability', 'If p_2 and p_4 vanish on W in C^M and delta = M - 3 dim W, deleting at most 7 delta coordinates makes the '
    'projected W a direct sum of independent lines on triples, each (1, w, w^2) up to signs and permutations; delta = 0 classifies every W; '
    'the constant 7 is attained by span(chi_1, chi_3) on Z/7 (all 128 coordinate projections checked).',
    'proved on paper (' + CODEX + '); exact example check in Q(zeta_7); Claude has not re-read it',
    DESK + 'CODEX_TO_CLAUDE_LEMMA_K.md; full: ' + CX + 'outputs\\GCT_LEMMA_K\\rigidity_of_lemma_k.tex', 'level spaces; power-sum lemmas',
    title='Sharp stability of Lemma K', depends_on='PNP-MBR:A1')
row('PNP-CODEX:Klein-rows', 'Doubly centred regular Klein-four-invariant row spaces (level, 4 rows): exact maxima 3, 3, 5 at widths 4, 5, 6; '
    '<= 6 at width six with only row centring (from sharp Lemma K: the three nonconstant row characters give modes with p_2 = p_4 = 0).',
    'proved on paper (' + CODEX + '); checks in gct_four_rows.py', DESK + 'CODEX_TO_CLAUDE_RIFFLE_AND_INTAKE.md; full: ' + CX
    + 'work\\lemma_source_crosswalk\\gct.md', 'level spaces', title='Klein-invariant four-row level spaces',
    depends_on='PNP-MBR:A1; PNP-CODEX:LemmaK-stability')
row('PNP-CODEX:riffle-recoveries', 'At length r = 2n - 1 + t the first factors of a riffle decomposition of pairId_n define a length-r, '
    'dimension-n code in which every information symbol has >= n - t disjoint recoveries; hence riffle(pairId_n) >= 2n for n >= 3, = 6 at n = 3 '
    'over every field, and >= ceil((19n - 14)/8) for n >= 14.',
    'proved on paper (' + CODEX + '); "the GCT reader independently checked it" (Codex note); 81 upper-bound coefficients of L-gct-140 checked over Z',
    DESK + 'CODEX_TO_CLAUDE_RIFFLE_AND_INTAKE.md; full: ' + CX + 'outputs\\RIFFLE_RANK\\disjoint_recoveries.tex', 'riffle rank',
    title='Disjoint recoveries and riffle rank >= (19n - 14)/8')
row('PNP-CODEX:086-amplification', 'With d(n) the largest dimension of a complex n x n level space: R_{X (+) Y} = R_X R_Y for block-diagonal '
    'perturbations, so d(n + r) >= d(n) + d(r) and d(m) >= floor(m/n) d(n); for every unbounded sequence m_j, lim d(m_j)/m_j = sup d(n)/n '
    '(so L-gct-086 reduces to any unbounded set of sizes, e.g. powers of 2). Conditional: at prime-power n, dim L <= (n - 1)(r + 1) with '
    'r = dim L - dim(L meet T L) for a full row cycle T.',
    'proved on paper (' + CODEX + '); unchecked by Claude', DESK + 'CODEX_TO_CLAUDE_L_GCT_086.md', 'level spaces',
    title='Amplification of level spaces', depends_on='PNP-CODEX:L211')
row('PNP-CODEX:L211', 'Translation-invariant level spaces: for a finite abelian group G of prime-power order acting by row translations, '
    'level spaces invariant under G have dimension at most (number of rows) - 1, sharp; also a rectangular mixed-order range; on six rows and '
    'four columns an example has every M_k = 0 while the row-product sum is 6 s^4 + 6 abcd.',
    'proved on paper (' + CODEX + '; four-page manuscript); the shared coefficient lemma is kernel-checked in L_gct_116.lean; L-gct-175 replayed',
    DESK + 'CODEX_TO_CLAUDE_L_GCT_211.md; full: ' + CX + 'outputs\\GCT_PERMANENT_LEVELS\\translation_invariant_permanent.tex', 'level spaces',
    title='Row-shift-invariant level spaces (L-gct-211 and extensions)')
row('PNP-CODEX:L116-Lean', 'Lean proof of L-gct-116 in its exact posted form, together with RowCharacterSum.fourier_matching_coefficients '
    '(off zero total frequency the distinct-row character sum is zero; at prime order the distinct-row and common-row coefficients vanish together).',
    'proved in Lean (' + CODEX + '): local run of their CheckLemma ACCEPTED, axioms propext, Quot.sound, Classical.choice, 1080 constants '
    're-checked; not submitted (L-gct-116 not leased to us)',
    CX + 'outputs\\GCT_PERMANENT_LEVELS\\L_gct_116.lean (SHA-256 bbecda0929e8bf29...); ' + DESK + 'CODEX_TO_CLAUDE_L_GCT_211.md',
    'level spaces', title='Lean proof of L-gct-116 (barrier B9)')
row('PNP-CODEX:exceptional-row', 'Let m >= 3 and Y have first row v (sum v_j = 0, all v_j != 0) and all other rows equal to 1; p, h the numbers of '
    'positive and negative v_j. Y is a smooth zero of perm; the tangent Hessian has inertia (m-1+(m-2)h, m-1+(m-2)p, 1) with radical RY; every '
    'real affine subspace Y + L on the hypersurface has dim L <= m + (m-2) min(p,h) (2m - 2 when one entry has either sign).',
    'proved on paper (' + CODEX + '); exact inertias at four (m, v) by permutation expansion', DESK + 'CODEX_TO_CLAUDE_EXCEPTIONAL_ROW_HESSIAN.md',
    'border dc', title='Permanent at a zero with one exceptional row', depends_on='PNP-MAR:2a')
row('PNP-CODEX:LS-sharp', 'LS(n) <= floor(n^2/3) + 2n - 2 (row-sum and column-sum vectors of a level space lie in the zero-sum hyperplanes); '
    'substituted in L-gct-077 this gives 3N + 10m >= 2m^2 + 14 for every border determinantal expression of perm_m of size N, m >= 2 '
    '(one more than L-gct-070 for m >= 3).',
    'proved on paper (' + CODEX + '); not kernel-checked; arithmetic re-checked by this map (' + CLAUDE_MAX + ')',
    PW + 'fleet_map\\chatgpt_gct.md ("A cubic-layer consequence")', 'level spaces; border dc', title='Sharpened cubic-layer bound',
    depends_on='PNP-MAR:1.2')
row('PNP-CODEX:Taylor-count', 'If a fixed set Omega of orders suffices for dim L <= C n for every complex L, then with a = floor(C) + 1 and '
    'Q = floor(n/a): |Omega| >= ceil(Q/a), and max Omega >= Q when Q >= 1; for C = 2, |Omega| >= (1/6 - o(1)) n.',
    'proved on paper (' + CODEX + ')', PW + 'fleet_map\\chatgpt_gct.md ("What the Taylor-order obstruction proves")', 'level spaces',
    title='Sharpened Taylor-order count', depends_on='PNP-MAR:1.3b')
row('PNP-CODEX:L087-replay', 'Independent re-expansion of L-gct-087\'s seven-parameter family through Sigma_4: all 24 permanent terms sum to zero '
    'over Q[w]/(w^2 + w + 1).', 'computed (' + CODEX + ')', PW + 'fleet_map\\chatgpt_gct.md; ' + DESK + 'CODEX_TO_CLAUDE_EXCEPTIONAL_ROW_HESSIAN.md',
    'border dc', title='Replay of L-gct-087')
# a8d75352 survey
SV = PW + 'MAPPING_OUR_RESULTS_TO_PEQUALNP.md'
row('PNP-SURVEY:converse-006', 'Converse of L-gct-006: if paddedPerm C m n lies in orbitClosure(detPoly C (n+1)) with m <= n, then '
    'HasBorderDetExpression (permPoly C m) (n+1): the approximants linSubst g_k det are determinants of linear matrices; then the checked helper '
    'hasBorderDetExpression_bind1 with X(0,0) -> 1, X(i+1,j+1) -> X(i,j), all other variables -> 0.',
    'proved on paper (Claude Opus 5.5 at effort high, GCT field expert a8d753525905811ab); Lean not written (estimated 60-120 lines)',
    SV + ' section 1.1', 'padding; border dc', title='Converse of L-gct-006')
row('PNP-SURVEY:L011-c<=2', 'L-gct-011 for c = 1 and c = 2: from L-gct-074 (border dc(perm_m) >= 2 m^2 for large m) and the converse of '
    'L-gct-006, x00^(m^c+1-m) perm_m is not in the orbit closure of det_(m^c+1) for all large m when c <= 2 (m^c + 1 < 2 m^2).',
    'proved on paper (Claude Opus 5.5 at effort high, a8d753525905811ab); not formalized; their node quantifies over all c and would have to be split',
    SV + ' section 1.1', 'padding; obstructions; border dc', title='Mulmuley-Sohoni non-containment for c <= 2',
    depends_on='PNP-SURVEY:converse-006')
# L-meta-647 and neighbours (outside GCT)
L647 = PW + 'L_meta_647_PARTIAL_PROOF.md'
row('PNP-L647:normal-form', 'For one-sided AND/OR circuits (no AND reads two X-dependent wires) computing the edge function of a C4-free bipartite '
    'graph: after normalization, every X-dependent wire computes OR_v (z_v AND alpha_{w,v}) with no beta part (no mixed OR), alpha given by paths '
    'through multiplying ANDs; the centres of the first ANDs form a vertex cover, so C has >= tau multiplying ANDs; and '
    '|C| = |X| + |Y| - 1 + e_Y + e_D (excess reads). L-meta-647 is equivalent, for this class, to e_Y + e_D >= |E| - |X| - |Y| + tau.',
    'proved on paper (' + CLAUDE_MAX + ', items 0-5); unchecked; the excess inequality is open',
    L647 + ' "Proved" items 0-5', 'meta: monotone circuits (outside GCT)', title='Partial proof of L-meta-647')
row('PNP-L647:L655-search', 'Exact SAT search (CaDiCaL) for one-sided circuits of the subdivided K4 (12 edges, tau = 4): side A with 15 gates SAT '
    '(re-checked on all 1024 inputs); side B with 11 gates UNSAT (823 s); <= 11 gates excluded on both sides.',
    'computed (' + CLAUDE_MAX + '); L-meta-655 withdrawn by the desk 15:41 UTC', L647 + ' "Computation for L-meta-655"',
    'meta: monotone circuits (outside GCT)', title='SAT search for L-meta-655')
row('PNP-L647:L632-partial', 'For C4-free G, AND-count circuits for the partial edge function: the star circuit of a minimum vertex cover gives size '
    'tau; no output vertices; fooling pairs from maximal independent sets; depth-one output gates are stars. Open: gates reading gates (a centre '
    'assignment for every first flipping gate).', 'partial proof on paper (' + CLAUDE_MAX + '); open', L647 + ' "L-meta-632"',
    'meta: monotone circuits (outside GCT)', title='Partial results on L-meta-632')
row('PNP-L647:L606-formulas', 'L-meta-606 holds for formulas with c = 2: Jukna (SIAM J. Comput. 2006, Thm 7.3): for triangle-free C4-free G '
    'of maximum degree d, monotone formulas accepting all edges and rejecting independent sets of size <= 2d have length >= |E|/2; circuits open.',
    'known theorem (read by ' + CLAUDE_MAX + '; local copy desk/lit/jukna_single_level_eccc2004_005.pdf)', L647 + ' "L-meta-606 / 608"',
    'meta: monotone circuits (outside GCT)', title='L-meta-606 for formulas')
row('PNP-CODEX:L606-boundedB', 'Cutting reused gates and conditioning on patterns seen on actual edges gives |E| <= B R <= B(s + 1 - k) '
    '(B patterns, R raw input pins, k reused gates): L-meta-606 for bounded B, with arbitrary fan-out.',
    'proved on paper (' + CODEX + ')', DESK + 'CODEX_TO_CLAUDE_L_META_606.md; ' + PW + 'MATCHES.md', 'meta: monotone circuits (outside GCT)',
    title='L-meta-606 for bounded pattern count')
# Hexagon board items (statements as on the board; stage codes as on the board)
for hid, st, status, top in [
    ('H02', "GCT VI's index hypotheses PH2, SH(a) and PH3 all fail for plethysm (P-F57, P-F19, P-F31), with the Theorem 1.6.1(d) erratum",
     'board stage W; full proof checks of P-F19, P-F31, P-F57 and P-F56 (a0805369, Claude Opus 5.5 at effort high); P-F23, P-F27, P-F30 reread by the main session (22 Nov)',
     'positivity and GCT VI/VIII; Kronecker and plethysm'),
    ('H02b', 'Numerical PH3 (GCT VI, Hypothesis 3.3.4) fails for Kronecker coefficients: every positive form for g((s^n),(s^n),(s^n)) has a '
     'denominator weight of at least 2^(n-1) (GCT_POS K023, R-NEW004, K024, PNEW013)',
     'board stage W; targeted proof check and computations (main session e0d20ada, Claude Opus 5.5 at effort max, 22 Nov); no independent re-proof',
     'positivity and GCT VI/VIII; Kronecker and plethysm'),
    ('H03', 'The border rank of det_4 and of per_4 is at least 43 over C, and at least 42 over every field',
     'board stage G1; intake recount of 1.5 million subsets; 22 verifiers rerun; newer: BORDER_RANK checkpoint 14 thm:52 (>= 52, char 0, 2, 3)',
     'border rank'),
    ('H13', 'Occurrence obstructions for per_n against det_n with no padding (A-030, A-034)',
     'board stage W; A-030 and A-034 confirmed in full (intake a17221e5, Claude Opus 5.5 at effort high); framing to be revised per the pequalnp check',
     'obstructions'),
    ('H14', 'Four-row multiplicity obstructions under padding; the gaps exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17)',
     'board stage G1; R-14 confirmed; R-13 recomputed for m = 4 to 10; to be framed as the barrier', 'obstructions; padding'),
    ('H20', 'A complete positive formula for every outer-degree-five plethysm coefficient (G-036 with T-037)',
     'board stage G2; 539 of 539 agree by computation; outer degree six table R-NEW-001 confirmed (5,214 of 5,214)', 'Kronecker and plethysm'),
    ('H21', "Polynomial-size formulas for stable hooks with varying outer degree (G-037 to G-039), and G-040's, polynomial for each fixed b",
     'board stage G2; 790 of 790 agree by computation', 'Kronecker and plethysm'),
    ('H23', "GCT VIII: Conj. 3.2 as printed has no minimum (N-012); the Positivity conjecture's unimodality clause fails at r = 3; the printed b2 has the wrong sign",
     'board stage N; N-012 proof checked; the E(3) constants computed by a8d75352 (Claude Opus 5.5 at effort high)', 'positivity and GCT VI/VIII'),
    ('GPK08', 'Triple-rectangular Kronecker series have the plethysm-type dyadic pole at n = 4 and n = 5: simple poles at the primitive 8th roots '
     'of unity (residue (14 - 10 sqrt 2)/256) and at the primitive 16th roots (K-008, K-014)',
     'board stage X (absorbed in H02b); both residues recomputed (a0805369, Claude Opus 5.5 at effort high)', 'Kronecker and plethysm; positivity and GCT VI/VIII'),
    ('GPK18', 'The largest vertex-denominator order of the n-fold Kronecker tensors is 2^(n-1+floor((n-2)/7)), not 2^(n-1) (K-018, K-020; 512 at n = 9)',
     'board stage G1; verified at n = 9, 16, 23, 30 by computation, other n at statement level', 'Kronecker and plethysm')]:
    row('HEX:' + hid, st, status, HEX + ' row ' + hid + '; ' + '<local>/Documents\\field_experts\\hexagon\\HEXAGON_STATUS.md', top,
        title='Hexagon board ' + hid)
for wid, st, chk in [
    ('WB-0002.001', 'For every m > n >= 2 the reduced class variety of the padded permanent (GCT VI: y^(m-n) per_n with a separate variable y) is '
     'not normal, so GCT VI\'s RH is false.', 'independent re-proof (Claude Opus 5.5 at effort high, 22 Nov); computation n = 2..8, m-n = 1..39'),
    ('WB-0002.002', "GCT VI's hph1det is false: along lambda = (m-1,1), d = 1 the count needs at least m-2 coordinates while the encoding must be "
     'polynomial in n and log m.', 'independent re-proof (Claude Opus 5.5 at effort high); small cases computed'),
    ('WB-0002.003', 'For n >= 2 and m >= (n+1)^25, given polytopes with PH1\'s counting property, no lambda satisfies either condition of OH '
     '(rests on Buergisser-Ikenmeyer-Panova 2019 and GCT II, Thm 8.2).',
     'independent re-proof (Claude Opus 5.5 at effort high), a wrong citation of the first proof corrected; inequalities n = 5..2000 computed')]:
    row(wid, st, 'proved (' + CLAUDE_MAX + ', 22 Nov); ' + chk, WB + 'NOTE.md (Theorems 1-3); ' + WB + 'STATEMENTS.tsv; ' + WB + 'CHECK_EVENTS.tsv',
        'positivity and GCT VI/VIII; padding; obstructions', title='WB-0002 ' + wid[-3:],
        notes='Same statements as GCT_FLIP Paper I thm:main-collapse (i)-(iii) (GCT_FLIP_final.zip, workbench/papers/paper1.tex line 123).')
OBS15 = '<local>/Documents\\reports_20261122\\overnight_intake\\GCT_OBS_cp15\\text\\'
row('GCT_OBS:Q1a', 'Question Q1a: an explicit four-row obstruction at (8, 9) (padded per_8 against det_9). Current gate: K_9 = a through second '
    'row 14 and the stated tail boxes; QC019/S025 prove q > K on S(216,9,9,9) in degree 27S, but the reachable degree and an explicit equation '
    'remain open.', 'open question (current gate, GCT_OBS cp15)', OBS15 + 'QUESTIONS.tsv row Q1a', 'obstructions; padding',
    title='GCT_OBS question at (8,9)')
row('GCT_OBS:Q1b', 'Question Q1b: an explicit four-row obstruction at (17, 23). Current gate: K = q = a through second row 17; K = a through '
    'second row 19 and the stated tail boxes; remaining second row >= 20.', 'open question (current gate, GCT_OBS cp15)',
    OBS15 + 'QUESTIONS.tsv row Q1b', 'obstructions; padding', title='GCT_OBS question at (17,23)')
CUE = '<local>/Documents\\grothendieck_archive_transcription_20261110\\research_returns\\CUE_GCT_checkpoint_08_20261121T0649Z_unzipped\\deliverables\\CUE_GCT.tex'
row('CUE_GCT:ctx-G13', '"The multiplicity statements G-10--G-13 locate particular representation sectors and degrees. They do not improve the '
    'established quadratic lower bound border dc(per_m) >= m^2/2 of Landsberg, Manivel, and Ressayre (2013)" (CUE_GCT, complexity lower-bound context).',
    'context sentence of the run (GPT-6 Astra (ChatGPT Pro mode)); the cited bound is correct as the refereed bound, not the best checked one',
    CUE + ' lines 7097-7106', 'border dc; obstructions', title='CUE_GCT: the m^2/2 sentence')
