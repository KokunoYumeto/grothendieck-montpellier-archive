# Our mathematics mapped onto pequalnp.com, by reading it (23 Nov 2026, from ~14:40 UTC)

By Claude Opus 5.5 at effort max (session 672ae3a0), reading the sources myself at the user's word ([the user's words, omitted]). This replaces the statement-
matching survey of a8d75352 (Claude Opus 5.5 at effort high), which read no proofs. Sources read so far: their 68 open
GCT lemmas with proof routes and the open lemmas of clb, pcx, lib and alg (`desk/open_gct_plain.txt`,
`desk/other_open.txt`); their checked L-gct-061, 065, 077, 080, 056, 074, 070, 010; their Lean definitions
(Defs/Gct.lean, Defs/RiffleRank.lean); in our returns: GCT_KRON (abstract, O-011 in full, section map), CUE_GCT
(abstract, section map, R-12, R-13, R-33), GCT_GINEQ (abstract, F-13 and F-14 in full, section map).

## A. Mappings carried to a proof or to a precise step

### A1. L-gct-122 "Lemma K" (p2 = p4 = 0 on W implies 3 dim W <= M): a complete proof

Translation (polarization, the apolarity step): for x, y, z, w in W, polarizing sum x_i^2 = 0 and sum x_i^4 = 0 gives
sum x_i y_i = 0 and sum x_i y_i z_i w_i = 0. So U := W * W (span of coordinatewise products) satisfies **U ⊥ 1** and
**U is totally isotropic** for the standard bilinear form. Let St = {x : x * U ⊆ U}, a unital subalgebra of C^M, hence
spanned by the indicators 1_{B_1}, ..., 1_{B_s} of a partition of the coordinates.
1. U ⊥ 1_{B_j}: <u, 1_B> = <u * 1_B, 1> = 0 since u * 1_B is in U.
2. U ∩ St = 0: the form is nondegenerate on St (diagonal with entries |B_j|) and U ⊥ St.
3. U + St ⊆ U^⊥, so dim U + s <= M - dim U: **2 dim U + s <= M**.
4. Kneser for codes (their checked L-gct-065, Mirandola-Zémor Thm 3.3) with S = T = W: **2 dim W <= dim U + s**.
5. Hence **4 dim W <= M + s**.
6. A block B with |B| <= 2: U restricted to B is isotropic and ⊥ 1_B in C^B, hence 0 (in C^2: (x, -x) with 2x^2 = 0).
   Then w * w vanishes on B for every w in W, so W vanishes on B; delete those coordinates (W, p2, p4 unchanged, M
   smaller) and conclude by strong induction on M.
7. Otherwise every block has at least 3 coordinates, s <= M/3, and 4 dim W <= 4M/3: **3 dim W <= M**. Sharp at blocks
   (1, w, w^2).
Lean route: the same skeleton as their checked L-gct-061 (p2, p3), with step 6 as the new piece.

### A2. L-gct-139 (riffle rank of [a=b][c=d] on [n]^4 is at least 2n - 1) is an instance of our GINEQ F-13

GCT_GINEQ F-13 ("image substitution"): flatten T with image U of dimension q; then any decomposition into atoms has
length >= q + min_{0 != u in U} (atom-length of u) - 1 (proved there for border rank by choosing q independent images,
taking the span of the atoms and a dimension count; the proof is verbatim for exact decompositions with any family of
atoms). For pairId flatten on a: the image is {phi ⊗ I_n : phi in F^n}, q = n; the atoms are the (b, c, d)-parts
C(b,c) D(b,d) of riffle-basic functions, each with every b-slice of rank <= 1; a nonzero phi ⊗ I has some b-slice
phi(b) I_n of rank n, so needs >= n atoms. F-13 gives **riffle rank >= n + n - 1 = 2n - 1**, their L-gct-139, and the
same frame gives their idea (pick n - 1 first factors independent modulo e_b, kill them). The certificate part of F-13
(an upper bound alpha_0 on the injective norm of the projector onto the image, F-14) is the tool to go beyond 2n - 1;
first target n = 3, where their bounds are 5 <= rank <= 6 (L-gct-139, L-gct-140).

### A3. The level-space problem (L-gct-086 and the small cases 091, 179-199, 210, 215, 143): the quadratic layer is our GCT_KRON O-011

perm(J + t) = sum_k (n-k)! S_k(t), S_k = sum of k x k subpermanents. O-011 (GCT_KRON, proof of (O-011.1)) computes at
J: perm = n!, gradient (n-1)! u (u all ones), Hessian (n-2)! B with **B = (J - I) ⊗ (J - I)**, eigenvalues (n-1)^2
on J, **-(n-1)** on the 2(n-1)-dimensional space of matrices with constant rows or constant columns and zero total
(1 ⊗ V + V ⊗ 1), **+1** on the (n-1)^2-dimensional doubly centred space V ⊗ V. So S_1(t) = <u, t> and
S_2(t) = (1/2) t^T B t = (1/2)(||t_0||^2 - (n-1)||t_r||^2 - (n-1)||t_c||^2) for t = t_r + t_c + t_0. Consequences:
- S_2 is nondegenerate on {S_1 = 0}: every level space is totally isotropic there, dim L <= floor((n^2 - 1)/2); this is
  the first step of their L-gct-091 route ("M_2 nondegenerate of Witt index 7 on {M_1 = 0}" at n = 4), for every n.
- Doubly centred level spaces (L-gct-182, 199): S_2 = (1/2) sum t_ij^2, so dim L <= floor((n-1)^2/2)
  (p x q: floor((p-1)(q-1)/2)).
- Rectangular p x q (L-gct-179, 181, 187, 195, 196, 215): Hessian ∝ (J_p - I_p) ⊗ (J_q - I_q), eigenvalues -(q-1) on
  V_p ⊗ 1, -(p-1) on 1 ⊗ V_q, +1 on V_p ⊗ V_q: nondegenerate on {S_1 = 0}, dim L <= floor((pq - 1)/2).
- The same eigenbasis is the coordinate system of their Fourier/mode-core analysis; the higher S_k restricted to the
  S_2-isotropic spaces carry the rest (their linear target needs them).
O-011 also gives, for the padded permanent F = X_11^s perm_m at J, the exact Hessian determinant
det H_F / det H_P = ((n-1)/(m-1))(1 - (m^2 - 3m + 1)(n - m)), nonzero except (m, n) = (3, 4), where an explicit other
point is given: the second-order input for Hessian-rank (Mignon-Ressayre type) arguments on the padded permanent of
L-gct-011 / L-gct-028.

### A4. Riffle rank beyond 2n - 1 (L-gct-124, 125, 139, 140; Rossman's Question C.1): BR_PENCIL's machinery is the route

BR_PENCIL (sections/pencils.tex, work/pencil/PENCIL_PROOFS.md) has, for flattening images of minor/permanent tensors:
the generalized border substitution BR(T) >= q - j + min_{W in Gr(j,U)} BR(P_W); P-01, the torus-weight degeneration
showing that the Grassmannian minimum is a coordinate minimum; P-07, further reduction to order ideals; P-08, the first-
prolongation (low-degree border-apolarity) necessary condition; exact values P-03, P-06, P-09. Translation to riffle
rank of pairId: the riffle atoms A(a) C(b,c) D(b,d) are preserved by the diagonal torus acting on b, so P-01's
degeneration applies to the border version of riffle rank, and the j-plane substitution reduces the lower bound to
small coordinate instances: riffle(pairId_n) >= n - j + R(j, n), R(j, n) the riffle length of
sum_{h<=j} e_h ⊗ e_h ⊗ I_n (a, b in [j], c, d in [n]). j = 1 is A2 (2n - 1). Deciding R(2, n) (between n + 1 and 2n
by F-13 and the trivial bound) is the next computation; R(2, n) >= 2n - 1 would give 3n - 3. P-08's prolongation test
is the certificate tool for n = 3 (5 or 6, L-gct-139/140).

## B. Our representation-theoretic results, translated onto their target L-gct-011 (Mulmuley-Sohoni)

L-gct-011: paddedPerm C m (m^c) is not in orbitClosure(detPoly C (m^c + 1)) for every c and large m (their Lean
objects). Their program reaches c <= 2 through border dc (L-gct-074 with L-gct-006); every route to c >= 3 through
representation theory must pass the following, which are ours:
- **Existence (where obstructions are):** CUE_GCT R-12: Phi_n:(Mat_n)^4 -> Sym^n(C^4)*, per(sum x_k A_k), is dominant
  for n = 4, 5, so m_lambda(per_n) = a_lambda(d[n]) for l(lambda) <= 4, and with D = 320112,
  m_lambda(per_4) - m_lambda(det_4) = 1 at lambda = (D + 4s, D, D, D): an infinite explicit family of multiplicity
  obstructions. R-13: Phi_n dominant iff 1 <= n <= 16; four-row multiplicity obstructions per_n vs det_n for every
  4 <= n <= 16. GCT_KRON: for the unpadded permanent a Hessian-bracket multiplicity-one obstruction at every n >= 3; an
  explicit highest-weight subalgebra with a strict multiplicity obstruction at every dilation. GCT_OBS / H13: occurrence
  obstructions per_n vs det_n without padding.
- **Exclusion (where obstructions cannot be):** GCT_KRON: at n >= m^25 a remaining actual obstruction needs at least 52
  rows with lambda_{2j} >= 28 - j (1 <= j <= 26) plus a joint later-row restriction; the grouped Foulkes-Howe
  refinement excludes every degree with n >= P_d(dm), P_d(dm) <= min{(d-1)^2, floor(d(d+m-1)/2)}; O-011: the family
  lambda_d = (d(n-2)+2, 2^{d-1}) carries no multiplicity obstruction; O-016 (degree-split exponent optimal), O-019
  (next jet order not dominant). CUE_GCT R-11: small-degree padding excludes all four-row obstructions. H14: four-row
  multiplicity obstructions under padding exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17), so that route stops near
  n = sqrt(2) m. H02, H02b, H23: GCT VI's PH2, SH(a), PH3 and GCT VIII's positivity hypotheses fail.
These are the representation-theoretic layer their GCT program has not built; in their language each is a statement
about which (m, n, lambda) can witness paddedPerm not in orbitClosure(detPoly).

## C. Their checked results that improve ours (update our texts)

L-gct-056 / L-gct-074 (checked in Lean; definitions read: standard border determinantal complexity, no sorry or axiom in
their Gct folder): border dc(perm_m) / m^2 -> infinity. L-gct-070: border dc(perm_m) >= (2m^2 - 10m + 11)/3. L-gct-010:
the separations behind our padded questions at (8, 9) and (17, 23) are already implied. Our texts must stop calling
m^2/2 the best border bound (it is the best refereed one).

## D. ChatGPT (from its rollouts, read 23 Nov ~14:50 UTC)

L-gct-211 proved on paper and extended to every prime-power order (the circulant coefficient from arXiv:1806.05905
feeds their checked L-gct-175), with an explicit order-6 family where the intermediate identity fails by 6 s^2 abcd;
fleet L-gct-056 rules out a single O(h^2) determinant for its paired-minor sum; their query-evasion lemma gives exact
query lower bounds for its period probes; no Lean, no submission yet.

## E. Still to read (in this order)

GCT_OBS and GCT_POS (statements), GCT_NSRH and ALPOGE_GCT (purity / flip: map to L-gct-011 and the positivity
hypotheses), GCT_PLETH (power sums: further Lemma K-type and Fermat-type statements), the remaining CUE_GCT parts
(G-21 differential rank and the isolation / hitting-set chapters against clb and the derandomization requests
L-lib-119 to 121), BR_PENCIL (apolarity for riffle rank and for the hard link L-gct-036/037), our Hexagon NEG row
(parity of #SAT as a Hasse-Witt scalar) against meta and alg.

### A5. The fourth-order level condition on doubly centred matrices (computed 23 Nov ~16:50 UTC, Claude Opus 5.5 at effort max)
Exact fit (relative error 1e-15, n = 5, 6, 7, independent of n), t doubly centred, G = t t^T:
  S_2 = p_2/2,  S_3 = (2/3) p_3,
  S_4 = (3/2) p_4 - (3/4) sum_i (sum_j t_ij^2)^2 - (3/4) sum_j (sum_i t_ij^2)^2 + (1/8) p_2^2 + (1/4) tr(G G).
The power-sum coefficients are (k-1)!/k (1/2, 2/3, 3/2): a cumulant-type expansion of log perm(J + t) in connected
S_n x S_n invariants is suggested; on a level space the lower invariants vanish order by order, which is the route to
reducing S_k to p_k and applying their iterated Fermat lemma (FermatIterated.lean). Next: fit S_5, S_6 the same way.
