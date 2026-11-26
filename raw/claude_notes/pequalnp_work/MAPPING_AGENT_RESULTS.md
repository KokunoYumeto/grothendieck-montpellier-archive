# Our mathematics on pequalnp.com's open lemmas: agent results (23 Nov 2026, from ~16:08 local)

By Claude Opus 5.5 at effort max (agent a3533d80e4df973c2, launched from session 672ae3a0; effort set at launch, recorded
in the agent's meta.json). Continues MAPPING_BY_READING_20261123.md (A1-A4, B, C, D there are not redone). Paper proofs
are mine and not yet checked by a second reader; numerical claims are reproducible from the scripts named (scratch
folder `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\672ae3a0-11a5-4e45-b4e2-c44a7908d05b\scratchpad\lvl\`;
copy what you keep). Running notes: `<local>/Documents\agent_notes\a3533d80e4df973c2_NOTES.md`.

Order (coordinator, 15:16 and ~16:50 UTC): L-gct-086 first (the desk handed it to KokunoYumeto), then the other live
links, then the rest. Notation: S_k(t) = sum of all k x k subpermanents; perm(J + t) = sum_k (n-k)! S_k(t); a level space
L has S_k = 0 on L for k = 1..n; DC = doubly centred matrices = V (x) V, V the sum-zero vectors (the standard
representation of S_n); p_k(t) = sum of k-th powers of the entries; LS(n) = max dim of a level space; kappa(n) = max dim
of a doubly centred level space (the core). Checked inputs used: L-gct-061 (p_2 = p_3 = 0 on W in C^M gives 3 dim W <= M),
L-gct-077, L-gct-080 (2n - 3), L-gct-092 (LS(n) <= kappa(n) + 2n), L-gct-158 (real level spaces <= p + q - 2).

## 1. L-gct-086 (level spaces are linear): what is proved, the obstruction to short proofs, and where it stops

Status: no proof and no counterexample. Five results below; the first two are proofs, the third is a family that
explains "a proof must use Taylor orders growing with n" exactly, the fourth reduces that family to a hypergraph copy
of the same problem, the fifth is the n = 4 chart and complex evidence.

### 1.1 The core, the real case, and the quadratic layer (translation of our O-011 Hessian)

- On DC: **S_2 = p_2/2 and S_3 = (2/3) p_3, for every n.** Proof: k! S_k = sum over distinct row k-tuples and distinct
  column k-tuples; Moebius inversion over the set-partition lattices of the row slots and the column slots gives
  k! S_k = sum_{pi, sigma} mu(pi) mu(sigma) N(pi, sigma), N(pi, sigma) = sum over row indices constant on the blocks of
  pi and column indices constant on the blocks of sigma of prod_l t(i_l, j_l). A pair with a singleton block yields a
  factor equal to an entry sum, a row sum or a column sum, which vanishes on DC. For k = 2, 3 only the one-block pair
  survives, with mu = -1 and mu = 2: 2 S_2 = p_2, 6 S_3 = 4 p_3. Invariant-theoretic reason: (V^(x)3)^(S_n) is
  one-dimensional ((1 + V)^(x)3 has 5 orbits on [n]^3), so the S_n x S_n-invariant cubic on V (x) V is unique.
  For k = 4: 24 S_4 = 36 p_4 - 18 sum_i (sum_j t_ij^2)^2 - 18 sum_j (sum_i t_ij^2)^2 + 3 p_2^2 + 6 tr((t t^T)^2).
  On all of {S_1 = 0} (row sums r, column sums c, row and column square sums r2, c2):
  S_3 = (2/3) p_3 - sum_i r2_i r_i - sum_j c2_j c_j + sum_ij t_ij r_i c_j + (sum r^3 + sum c^3)/3.
  (All checked numerically at n = 4, 5, 6: `checkS.py`.)
- **Real case.** On real DC, S_2 = |t|^2/2 > 0, so the real core is 0 and real level spaces have dimension <= 2n - 2
  (this is L-gct-158 seen through the O-011 eigenvalues: +1 on DC, -(n-1) on the 2(n-1)-dimensional row/column part).
  For a complex level space L, L meet conj(L) is the complexification of a real level space, so it has dimension
  <= 2n - 2: **the whole complex problem lives in the totally non-real part**, and the core K = L meet DC satisfies
  K meet conj(K) = 0.

### 1.2 First use of the cubic layer: LS(n) <= n^2/3 + 2n (proof)

For t in the core K = L meet DC, 1.1 gives p_2(t) = 2 S_2(t) = 0 and p_3(t) = (3/2) S_3(t) = 0, so K is a subspace of
C^(n^2) on which both power sums vanish. L-gct-061 gives 3 dim K <= n^2, and L-gct-092 gives
**LS(n) <= n^2/3 + 2n.** This improves the quadratic-layer bound floor((n^2 - 1)/2) (A3 of the mapping file) for
n >= 13, and up to the constant it is the most that orders <= 3 can give: see 1.3 (orders <= 3 leave a family of
dimension ~n^2/4).

### 1.3 Why every proof must use Taylor orders growing linearly with n: the root-of-unity block family F_q

Let q divide n, m = n/q, w a primitive q-th root of unity. Index rows as (I, a), I in [m], a in Z_q, and let
**F_q = { t : t((I,a), j) = w^a c_I(j) }**, c = (c_1, ..., c_m) an arbitrary m x n matrix: each block of q consecutive
rows consists of one free row vector multiplied by 1, w, ..., w^(q-1). dim F_q = n^2/q; F_q meet DC (rows of c summing
to zero) has dimension (n/q)(n - 1).

**Theorem.** S_k vanishes on F_q for every k with q not dividing k. Moreover S_q = (-1)^(q-1) q! sum_I e_q(c_I).
Proof: in the Moebius expansion of 1.1 the row index of a block beta of pi is a free pair (I_beta, a_beta), and
t((I,a), j) depends on a only through w^a, so N(pi, sigma) contains the factor prod_beta (sum_a w^(a |beta|)), which is
zero unless q divides every |beta|, hence unless q divides k. For k = q only pi = one block survives; it gives
mu = (-1)^(q-1) (q-1)! times q sum_i (sum over distinct column q-tuples) = (-1)^(q-1) q! sum_I e_q(c_I).
(Checked numerically: q = 2, 3, 4 at n = 6, 6, 8; S_(q+1) and S_(q+2) also vanish as predicted: `blockfam.py`.)

**Truncated version F_(q,r)** (q | r <= n, any n): put the block structure on the first r rows only and make the other
n - r rows zero; dim F_(q,r) = (r/q) n, and **S_k vanishes on F_(q,r) unless q | k and k <= r** (k > r: every k x k
submatrix has a zero row). Checked: (n,q,r) = (6,2,4), (6,3,3), (7,2,4), (7,3,6) leave exactly the orders {2,4}, {3},
{2,4}, {3,6} (`blockfam2.py`).

Consequences.
1. Any argument that uses only the Taylor orders k <= q - 1 cannot prove a bound below n^2/q (n^2/q - n/q inside DC).
   With orders <= 3 the truth for the core lies between (n/4)(n - 1) (F_4 meet DC) and n^2/3 (1.2).
2. **Theorem (how many orders a proof needs).** Let Omega be a set of orders such that "S_k = 0 on L for all k in Omega"
   implies dim L <= C n. Then for every q with (C'+1) q <= n, C' = floor(C), Omega contains one of q, 2q, ..., (C'+1) q
   (otherwise F_(q,(C'+1)q), of dimension (C'+1) n > C n, kills all of Omega). An order k serves at most C'+1 values of
   q (q = k/j, j <= C'+1), so **|Omega| >= floor(n/(C'+1))/(C'+1): a linear bound needs linearly many distinct Taylor
   orders**, and in particular orders up to about n/(C+1). This is the exact content of the desk's note "a proof must use
   Taylor orders growing with n".
2. The families are where the cube-root (q = 3) and circulant-type constructions live; they do not refute L-gct-086 by
   themselves: the next order S_q is a sum over blocks of e_q, and the remaining orders are governed by 1.4.

### 1.4 Self-similarity: on F_q the level problem is its own q-uniform hypergraph version

**Identity.** For t in F_q,
perm(J + t) = (q!)^m sum over ordered partitions (C_1, ..., C_m) of [n] into q-sets of
prod_I (1 + (-1)^(q-1) prod_{j in C_I} c_I(j)).
Proof: group permutations by the column set C_I that each row block receives; within a block the sum over bijections is
perm(J_q + lambda c_(I,C)^T) with lambda = (1, w, ..., w^(q-1)), and S_s(lambda c^T) = s! e_s(lambda) e_s(c) with
prod_a (1 + z w^a) = 1 - (-z)^q, so only s = 0 and s = q remain: q!(1 + (-1)^(q-1) prod_{j in C} c(j)).
(Checked numerically at (n, q) = (6, 3), (6, 2), (4, 2): `hyper.py`.) For q = 1 this is L-gct-086 itself.
- Level spaces inside F_q: if each c_I is supported on a fixed (q-1)-set, every product over a q-set vanishes and
  perm(J + t) = n!: **a level space of dimension n - n/q for every q dividing n** (linear, below 2n - 3; new as a family
  as far as I can see in their record). Larger level spaces inside F_q need cancellation in the hyperpermanent, i.e. the
  same problem one level up. An induction on q along this self-similar structure is the route I would try next; it is
  not carried out.

### 1.5 n = 4: a rational chart for the core and complex evidence (L-gct-182, L-gct-091, L-gct-185)

- Klein (Walsh) coordinates, rational, instead of the Q(i) Fourier chart of their L-gct-091 route:
  f1 = (1,1,-1,-1)/2, f2 = (1,-1,1,-1)/2, f3 = (1,-1,-1,1)/2, t = F X F^T with X in Mat_3; S_4 acts as the tetrahedral
  group, whose invariant cubic is abc. Exact (sympy, `q4.py`): **p_2(t) = tr(X X^T), p_3(t) = (3/2) perm_3(X),
  perm_4(t) = (tr X X^T)^2/32 + Q(X)/16**, Q = tr((X X^T)^2) + 6 sum X_ab^4 - 3 sum_a (sum_b X_ab^2)^2 - 3 sum_b
  (sum_a X_ab^2)^2. So L-gct-182 asks for a 4-dimensional maximal isotropic subspace of (Mat_3, tr X X^T) (the
  isotropic Grassmannian OG(4,9), dimension 10) killing perm_3 and Q: 20 cubic and 35 quartic coefficients, all over Q.
  The known 3-dimensional core is K = span(v e1^T, v' e2^T, v e3^T), v = (1, w^2, -w), v' = (1, w, -w^2), w = exp(2 pi
  i/3) (found by the search below and read off exactly): every column is a fixed isotropic vector times a scalar.
- Complex Levenberg-Marquardt searches with random complex starts (`dc4.py`, `plsearch.py`, `refine.py`):
  DC 4x4 dim 3: 31 hits in 960 restarts; **DC 4x4 dim 4 (L-gct-182): 0 in 2000** (best residual 1.39);
  4x4 dim 5: 3 in 104; **4x4 dim 6 (L-gct-185; would refute L-gct-091): 0 in 2600** (best relative residual 1.6e-4,
  re-minimized with fresh sample points: plateau 2e-4 with full-rank Jacobian, genuine local minima). Evidence, not
  proof (rigid solutions can have small basins); it supports kappa(4) = 3 and LS(4) = 5 over C. My 4 x 5 calibration
  (dim 6 exists) found nothing in a 300 s budget, so I report no 4 x 5 evidence. DC 5 x 5 (540 restarts each, 200 s
  budget): best relative residuals 8e-9 (dim 3, which exists: u (x) (1, z, ..., z^4), z^5 = 1, u in V with u_1 = 0),
  1e-6 (dim 4), 2e-5 (dim 5); re-minimizing with fresh points plateaus at 1e-8, 3e-6, 3e-5. The solver stalls even on
  the existing dim-3 family, so 5 x 5 is inconclusive; the two-orders-per-dimension gap is the only signal.
- A DC level family for every n, dimension n - 2: t = u (x) v with v = (1, z, ..., z^(n-1)) (z a primitive n-th root),
  u in V with u_1 = 0 (S_k(u (x) v) = k! e_k(u) e_k(v), e_k(v) = 0 for k < n, e_n(u) = 0). So kappa(n) >= n - 2;
  kappa(4) = 3 (evidence) is one above it.

### 1.6 Where it stops

What is missing is control of the core under all orders at once. Bounded orders cannot do it (1.3), the real structure
cannot see it (1.1), and the torus degenerations of BR_PENCIL do not apply directly: the only torus preserving the
problem moves J, and a torus-fixed limit of CJ + L is a coordinate space on which the multilinear perm cannot be a
nonzero power, so the limit falls into {perm = 0} and loses the level condition (the coordinate bound is n^2 - n).
The concrete next steps: (a) the q-induction along 1.4; (b) a Kneser-type lemma for the full family of singleton-free
invariants N(pi, sigma) of 1.1 (their T3, L-gct-163, is the p_4 case); (c) a certificate for kappa(4) = 3 in the
rational chart of 1.5 (OG(4,9) charts, Groebner over Q, Nullstellensatz cofactors for Lean).

## 2. L-gct-036 / L-gct-037 at their zero Sigma_m: exact second fundamental form; the real case proved (2m - 2)

Their point (GReduction.sig): Sigma_m = J - m E_00 (perm = m! - m (m-1)! = 0), the "J - 4E44" of the L-gct-036 attempts.
- Gradient: (m-1)! on row 0 and column 0, -(m-2)! on the block B (rows and columns >= 1). Hessian: H[(i,j),(k,l)] = 0 if
  i = k or j = l, (m-2)! if 0 is in {i,k} or {j,l}, else -2(m-3)!; hence **Q(t) = (m-3)! [2(m-2) S_2(t) - 2m S_2(t_B)]**.
- Under S_(m-1) x S_(m-1): (1) the doubly centred block (dim (m-2)^2): Q = -2(m-3)! |t|^2, negative definite; (2) two
  pieces with two copies of V'_0 each, t = alpha e_0 (x) w + beta 1' (x) w (row 0 = alpha w, every block row = beta w,
  sum w = 0) and its transpose: Q = 2(m-3)!(m-1)(m-2)|w|^2 beta(beta - alpha), one + and one - per copy; (3) the
  invariant piece meets T_y in dimension 3, contains y (the radical, the cone direction of L-gct-050/113) and carries one
  + and one -. **On T_y/Cy the signature is (+(2m-3), -(m-1)^2).** Checked for m = 3..10 (`sig_sigma.py`), exactly at
  m = 4 (`hess_sigma.py`: gradient (6,6,6,6,6,-2,...), rank 14 on T_y, signature (5,9,1)), piecewise at m = 5.
- **Theorem (real case of L-gct-037 at Sigma_m).** Every real linear subspace W containing Sigma_m on which perm_m
  vanishes has dim W <= 2m - 2 (W lies in T_y, W/Ry is isotropic for a form of signature (2m-3, (m-1)^2)); with
  L-gct-113 the same holds for real y + L. Exactly the conjectured value.
- Over C the quadratic layer gives 1 + floor((m^2-2)/2) (m = 4: 8 where L-gct-036 needs 6). The complex excess sits in
  the negative-definite doubly centred block, which by the L-gct-077 identity is the level-space core of perm_(m-1):
  **L-gct-036/037 at Sigma_m and L-gct-086 meet in the same core problem** (1.1-1.6), plus a frame of dimension O(m).

## 3. Off the live chain, complete: riffle rank of pairId_n is at least 2n (n >= 3); exactly 6 at n = 3

Improves L-gct-139 (2n - 1; A2 of the mapping file) by one over every field; with L-gct-140 (six terms)
**riffle(pairId_3) = 6**, the first exact value past n = 2 (Rossman, Question C.1).

Proof. Suppose sum_{l=1}^{2n-1} A_l(a) C_l(b,c) D_l(b,d) = [a=b][c=d] on [n]^4, n >= 3. Let A be the n x (2n-1) matrix
with columns A_l and M_l^b = C_l(b,.) D_l(b,.)^T (rank <= 1); the identity reads sum_l A_l(a) M_l^b = [a=b] I_n.
1. rank A = n: a functional phi killing all A_l gives phi_b I = sum_l phi(A_l) M_l^b = 0 for every b.
2. Fix b. The solutions are y (x) I + ker A (x) Mat_n (A y = e_b), dim ker A = n - 1, so V_b = span{M_l^b} has dim <= n
   and contains I = sum_l A_l(b) M_l^b. A basis of V_b among the M_l^b is at most n rank-one matrices spanning I, hence
   exactly n, u_k v_k^T with sum c_k u_k v_k^T = I; so V_b = U Diag U^(-1) and each M_l^b = lambda_l E_(f(l)) with
   E_k = U e_k e_k^T U^(-1). (This is A2's bound read as an equality case.)
3. Independence of the E_k: for each k, sum over G_k = {l : lambda_l != 0, f(l) = k} of lambda_l A_l = e_b. So
   W_b = A^(-1)(F e_b) (dim n) is spanned by n vectors chi_k with disjoint nonempty supports G_k and A chi_k = e_b, and
   K = ker A = {sum t_k chi_k : sum t_k = 0}.
4. On K the coordinate functional of l is 0 off the G_k and lambda_l tau_k on G_k (tau_k(sum t_j chi_j) = t_k); for n >= 3
   the tau_k are pairwise independent on {sum t = 0}. So the blocks G_k are the proportionality classes of the
   coordinate functionals on K, and each line F chi_k is the line of restrictions of K to G_k: both depend on K only.
   Hence W_b is the same for every b, so W_b meet W_b' = W_b; but W_b meet W_b' lies in A^(-1)(F e_b meet F e_b') = K,
   of dimension n - 1 < n. Contradiction. (At n = 2, tau_1 = -tau_2 and L-gct-095 gives three terms.)

## 4. The meta steps we hold (L-meta-632, 617, 655)

None of our GCT sources that I read (CUE_GCT isolation I-01..I-44 and purity P-01..P-13: ROABP identity testing,
character-sum and arithmetic samplers; GCT_KRON, GCT_OBS, GCT_PLETH: multiplicities, plethysm, border rank) contains a
statement about monotone AND/OR circuit size, vertex covers or rectifier networks; the open step of L_meta_647
(Nechiporuk-type count for rectangle-free relations) is not in them.

## 5. Sources read, and where they meet or do not meet the targets

- CUE_GCT G-21 (lines 8964-9045): the permanent-pencil image has dimension r m^2 - 2m + 2 (m >= 17, r >= 4), generic
  fibres = the row-column torus. A level space of dim q is a point of the fibre of (A_0..A_q) -> per(sum x_i A_i) over
  m! x_0^m with A_0 = J; that fibre contains L^(q+1) (dimension q(q+1)), so semicontinuity runs the wrong way: G-21 gives
  no bound on q. Recorded as read, no meet.
- CUE_GCT P-01..P-13 (lines 17657-18060): P-02 (AGHP quadratic-character points) and P-07 (Kronecker weights) are hitting
  sets for sparse polynomials at character or Kronecker points; the DIV hypotheses L-gct-103/104 need nonvanishing at
  the integers -1..-N, which these do not address. P-09/P-10 (weighted energy samplers need ~(delta+1)^n points; width-one
  products) is a barrier of the same kind as the dead L2-sampler routes recorded on L-clb-024/028, not a new route.
- GCT_KRON O-005..O-011 (lines 4269-4820), O-013, O-019, QA033 (lines 12273-12380): O-010/O-019 bound universal
  projection and jet-dominance arguments by parameter counts (L-gct-011 methodology, mapping section B). QA033's
  factorial transform perm(tJ + A) = T(matching polynomial of A) is the generating-function form of perm(J + sA) =
  sum (n-k)! S_k(A) s^k; its residue technique needs distinct roots, whereas a level space has all roots at 0.
- GCT_PLETH (section map; plethysm and canonical-map ranks), GCT_OBS (multiplicity gates at (8,9), (17,23); CP border
  rank 43/44 of the det_4/per_4 four-factor tensors) and the intakes GCT_SEPARATIONS (Paper II's finite multiplicity
  obstruction at (8,9)), GCT_FLIP, BORDER_RANK: all on L-gct-011 or tensor border rank (mapping section B); none on the
  level-space or zero-locus links.
