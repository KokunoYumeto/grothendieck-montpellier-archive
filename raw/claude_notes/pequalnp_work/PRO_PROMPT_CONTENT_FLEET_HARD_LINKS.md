# Content for the Pro prompt on the fleet's hard links (for the main session's build)

Written by Claude Opus 5.5 at effort max (session 672ae3a0), 23 Nov 2026 ~21:3x UTC, at the main session's request.
This is the mathematics the prompt should carry for Parts A and B (statements, what is checked where, our results with
their check states, and the targets), so that the build can take it as the content of its spec. Part C's leads are in
the main session's distribution (field_experts/structural_maps_20261123/DISTRIBUTION_TO_PROMPTS.md, section B) and are
not repeated here. Nothing from the run goes to pequalnp.com: the prompt produces mathematics; we formalize later.

Check-state words below: CHECKED-FLEET (a Lean-checked node of the fleet, brilliant-hq/pequalnp-proofs), PAPER (complete
on paper, no second reader), NUMERICS, SKETCH. Fleet ids are L-<program>-<nnn>; our extension entries are X-*.

## Part A. Level spaces of the permanent at J (L-gct-086 and its small cases)

**Definitions.** For an n x n complex matrix t, perm(J + t) = sum_k (n-k)! S_k(t), where S_k is the sum of the permanents
of all k x k submatrices (CHECKED-FLEET L-gct-084). A level space is a complex linear space L with perm(J + t) = n! for all
t in L, equivalently S_k = 0 on L for all k >= 1; LS(n) is the largest dimension; rectangular p x q versions likewise
(sum over injections). Doubly centred (DC): row and column sums zero.

**Statements to attack.**
- L-gct-086 (open, the hard link): there is C with LS(n) <= C n for all n ("it may be false").
- L-gct-091 (open): LS(4) = 5.
- L-gct-179 (open, a search): is there a 7-dimensional level space of 4 x 5 matrices (sum over injections = 120)?
- LS(6) <= 10: the first case that, through CHECKED-FLEET L-gct-077, would give a new border determinantal bound
  (border size >= 26 for perm_7, above m^2/2 = 24.5); every smaller case gives nothing new (the Fable agent's reading of
  the fleet graph, Claude Fable 5.2 at effort high; PAPER for the arithmetic).

**Known on the fleet's board (CHECKED-FLEET).** 080 (a space of dimension 2n - 3), 092 (LS(n) <= kappa(n) + 2n, kappa the
DC core bound), 094 (LS(3) = 3), 214 (4 x 4 <= 6), 215 (4 x 5 <= 7), 216 (DC 4 x 4 <= 3), 217 (row-centred 4 x 4 = 5), 158
(real p x q level spaces <= p + q - 2), 105/106/134 (the DC layers below), 110 (direct sums on disjoint blocks are level),
077 (a level-space bound gives a border-dc bound), 074 (border dc(perm_m)/m^2 -> infinity, rate not explicit), 044 (the
method's ceiling (m - 1)^2 + 1), 087 (a non-real 7-dimensional space through Sigma_4 in the zero set of perm_4), 061 and
065 (Fermat-type and Kneser-for-codes bounds), 090/098/111/123 (product-type parts bounded by n - 1).

**Our results (with check states).**
1. DC layers: S_2 = p_2/2, S_3 = (2/3) p_3, 24 S_4 = 36 p_4 - 18(R_4 + C_4) + 6 tr((t t^T)^2) + 3 p_2^2, with
   R_4 = sum_i (sum_j t_ij^2)^2, C_4 = sum_j (sum_i t_ij^2)^2 (CHECKED-FLEET 105, 106, 134; our NUMERICS at n = 4..7 agree).
   The power-sum coefficients are (k-1)!/k. Cumulant reading: perm(J + t)/n! = E prod_i (1 + t_{i sigma(i)}) over uniform
   sigma; on DC matrices Var(sum_i t_{i sigma(i)}) = p_2/(n-1) and Cov(Y_1, Y_2) = p_3/(n-1) (Y_j = sum_i t_{i sigma(i)}^j),
   so orders 2 and 3 are pure power sums and order 4 is the first with connected non-power-sum terms (R_4, C_4, the trace
   term; 3 p_2^2 is the disconnected part). PAPER.
2. LS(n) <= floor(n^2/3) + 2n - 2 from layers 2 and 3 with 061 and 092 (agent, Claude Opus 5.5 at effort max; Codex's -2).
   PAPER. Through 077: 3N + 10m >= 2m^2 + 14, one more than CHECKED-FLEET 070 (X-gct-006, assembly not formalized).
3. Real case: real DC cores are 0; dim(L cap conj L) <= 2n - 2; the complex excess of a level space is totally non-real.
   PAPER (consistent with CHECKED-FLEET 158).
4. Taylor-order barrier (X-gct-001): for q | r <= n the family F_{q,r} (first r rows in r/q blocks, block I having rows
   omega^a c_I, a in Z_q) has dimension (r/q) n and S_k = 0 on it unless q | k <= r; so any set of orders whose vanishing
   forces dim <= C n has about n/(C+1) elements. PAPER (derived twice; Codex sharpened the count to (1/6 - o(1)) n for C = 2).
5. Self-similarity (X-gct-002): level spaces inside F_q are the level spaces of the q-uniform hyper-permanent of the
   (n/q) x n array (all hyper-matching sums vanish). PAPER.
6. Amplification (X-gct-003, Codex): R_{X (+) Y} = R_X R_Y, so LS is superadditive and lim LS(n)/n = sup LS(n)/n; one
   counterexample to a constant propagates. PAPER (Codex; not rechecked by Claude).
7. Prime powers (X-gct-004, Codex): dim L <= (n - 1)(r + 1) for the one-step defect r of a full row cycle, via the
   row-translation theorem (L-gct-211, Codex's proof, PAPER). Chebotarev's theorem on minors of the prime-order Fourier
   matrix is the engine (X-gct-009, SKETCH: extensions to orders pq and square-free orders exist in the literature).
8. A DC family u (x) (1, z, ..., z^(n-1)) gives kappa(n) >= n - 2. PAPER.
9. Finite free probability (Fable agent): level means the expected characteristic polynomial of a random generalized
   diagonal is lambda^n; no new bound yet. SKETCH.
10. The main session's structural leads for Part A (GCT.md 1.4, 4.1, 4.5; AG_HODGE_ANT.md B.2, B.7.1;
   MOONSHINE_LEECH_ALGEBRA.md A2, A5, B.9.1 in field_experts/structural_maps_20261123/): the connected Kneser route in
   cumulant form (compute c_5, c_6 on DC matrices, then a Kneser-type inequality with k growing linearly in n); the matrix
   zeta function of a level space; Proposition B.2 (one-symmetry level spaces have dim <= n^2/q < n, so extremal spaces are
   deformations of special points) with the torus-fixed points of Z_k in OG(k, N) at n = 4; the PSL2(7) slice as Klein's
   quartic with 24 level lines (NUMERICS; exact proof over Q(sqrt(-7)) next); frame shapes and rank-one level lines.

**Targets, in order.** LS(6) <= 10 (or a 6 x 6 level space of dimension 11, which would also be news); LS(4) = 5; the
4 x 5 dimension-7 question (179); a Kneser-type inequality using Theta(n) layers (the only kind the barrier allows);
the induction on q for the hyper-permanent; a defect bound for row cycles. A counterexample to 086 (superlinear growth)
is as valuable as a proof: by item 6 a single family of ratio above any C refutes it.

## Part B. Monotone and negation-limited circuits for edge functions of C4-free graphs (606, 608, 612, 650)

**Statements.** For a graph G, f_G(x) = OR over edges uv of (x_u AND x_v). L-meta-608: if G has girth >= 5, every
monotone fan-in-2 circuit for f_G has >= |E| + tau(G) - 1 gates. L-meta-606: |E| <= c (size + 1). L-meta-612: the joint
count (its shards: joint count; refutation on bipartite C4-free graphs, smallest first; one side of degree <= 3).
L-meta-650 (search): a circuit of at most 63 gates for the incidence graph of PG(2,3) (|E| = 52, tau = 13: 64 = 52 + 13 - 1).

**Known (CHECKED-FLEET).** 270 (line-ORs of a plane need exactly N q monotone gates), 529 (labelling invariant), 649
(line-degree <= 2 gives |I| <= 48|C| + 2N), 696, 697, 738 (transposition at line-degree 1), 739, 745 (the NOT-gate
recursion, with checked hypotheses 270 and 669), the forest theorems 104/105. For circuits, 606 on PG(2,q) incidence
graphs contains Jukna's open n^(3/2) problem (ECCC TR05-021, Problem 24); for formulas Jukna's TR04-005 Theorem 7.3
gives c = 2.

**Our results (check states).** One-level-AND circuits satisfy 608 on every C4-free graph (X-meta-002, PAPER); the
one-sided class: normal form, first-AND centres form a vertex cover, reads identity, and |E| + tau - 1 exactly at
line-degree 1 (PAPER, two derivations); the weight barrier (Theorem C, X-meta-001: on the affine-plane incidence graphs,
circuits of <= 28 w n gates reject every independent set of <= w vertices; PAPER, computation at q = 5, 7); light inputs
(Theorem D: weight <= 1 costs O(q^2); PAPER); with NOT gates the Singer-form line-ORs are one cyclic convolution, so about
N log^2 N gates suffice against exactly N q monotone (Theorem E, X-meta-102/103; PAPER; the negation-limited size bound is
cited from memory and must be checked); the L-meta-745 recursion on planes evaluates to 1, 0.5, 0.19, 0.07 of N q for
s = 0..3 NOT gates (computation); the AND count tau for leaf-deletable graphs (X-meta-003, PAPER); exact SAT: no
counterexample to 608 on connected girth-5 graphs with <= 7 vertices.

**Leads (main session's maps).** PG(2,3) in Singer form {0,1,3,9} mod 13 (symmetry group of order 78); its affine part
AG(2,3) is the tetracode configuration and the Pappus configuration is AG(2,3) minus one parallel class (Codex's public
proof); 64 = 44 + 16 + 4; the Leech-root ladder of girth-6 test graphs (targets 39, 59, 125); Golay code and PG(2,4)
hyperovals for 714/715; the inverse-semiring component lemma (B.9.6; the semiring reading of 608 itself is already in
prompt 93: do not duplicate).

**Targets, in order.** The exact count at line-degree 2 (the next rung; an exact constant there decides 582 and 650);
650 by the 44 + 16 + 4 split (an AG(2,3) circuit below 44 gates, or a proof that none exists, plus an additivity lemma for
the points at infinity); the cost of the Singer line-ORs as a function of the number of NOT gates between 1 and log2 N;
608 for two levels of AND gates.

## Structure, in my view
One prompt is right for research on hard links: it races nobody, since it produces mathematics rather than desk
submissions, and splitting it into desk-sized prompts would recreate the racing the user ruled out. If Parts A, B and C
are too far apart for one run's ledger, split by mathematics (A: level spaces; B and C: circuits, planes and the
arithmetic of SAT), not by desk step.
