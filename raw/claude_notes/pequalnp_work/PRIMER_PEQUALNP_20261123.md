# Primer: our work with the pequalnp.com fleet (23 Nov 2026)

Written by Claude Opus 5.5 at effort max (session 672ae3a0) for the main session, at its request, 23 Nov 2026 ~19:3x UTC.
Recall, not review: statements and statuses as already recorded; locators are files in `<local>/pequalnp_work\`
unless said otherwise.

**The setting.** pequalnp.com is an open fleet of AI agents attacking P vs NP through Lean-checked lemmas (Lean 4.36.0,
repository brilliant-hq/pequalnp-proofs). A desk hands out steps (`/desk/next`); a step counts only as a Lean file proving
exactly the posted statement in a pull request, while the step is still posted. We work under the handle KokunoYumeto
(the user's authority: Claude and ChatGPT may post Lean proofs wherever accepted). Fleet ids are L-<program>-<nnn>
(programs gct, meta, clb, pcx, lib, alg). Alpöge's theorem (RH for every Dirichlet L-function, Lean) is cited as a theorem.

**What happened at the desk (the decisive fact).** Five sketched steps, five lost to faster outside pipelines on 23 Nov:
L-meta-750 (withdrawn 16:43 as proved by another), L-meta-756 (Codex's PR 1266: proved first by another), L-meta-782
(our clean build 17:22; another PR merged 17:17:57), L-meta-755 (handed 17:19:49, withdrawn 17:28:16; our file took 532 s
to elaborate), L-meta-738 (checked 16:51 before we began). Lemma K (L-gct-122) was closed unchecked as "stood down".
The user's ruling (~17:4x UTC): no racing; hold only hard links (`&hard=1`) and work them as research; everything else
goes to our mirror. We hold no step now.

## 1. Lemma K (L-gct-122)
- **Statement.** If W is a complex linear subspace of C^m on which the power sums p_2 = sum x_i^2 and p_4 = sum x_i^4
  vanish identically, then 3 dim W <= m.
- **Lemmas used.** The fleet's L-gct-065 (Kneser's theorem for codes: dim(S * T) >= dim S + dim T - dim St(S * T) for the
  span of coordinatewise products, after Mirandola-Zémor); polarization.
- **Proof in outline.** Polarize: W is isotropic for the dot product (from p_2) and sum u v z w = 0 for u, v, z, w in W
  (from p_4). So V = W * W is isotropic and orthogonal to the all-ones vector 1. If the stabilizer of V is the scalars,
  Kneser with S = T = W gives 2 dim W <= dim V + 1, and V + C1 inside V-perp gives 2 dim V + 1 <= m; together
  4 dim W <= m + 1, hence 3 dim W <= m. Otherwise split the coordinates along an idempotent of the stabilizer and induct
  on m (strong induction, `lemmaK_general`).
- **Files.** Lean: `pequalnp-proofs/lean/PEqualNP/Outside/L_gct_122.lean` (namespace LGct122K; builds; axioms propext,
  Classical.choice, Quot.sound), copy in `mirror/lean/L_gct_122.lean`, public in github.com/KokunoYumeto/pequalnp-mirror.
  Paper: `MAPPING_BY_READING_20261123.md` A1. PR brilliant-hq/pequalnp-proofs#874 closed unchecked 15:14 UTC (stood down).
  Codex's stability extension: `desk/CODEX_TO_CLAUDE_LEMMA_K.md` (after at most 7(m - 3 dim W) deletions the image is a
  direct sum of signed triple lines; 128 checks).
- **Good for.** The p_2/p_4 case of the Fermat/Kneser family the fleet uses for level spaces.

## 2. Level spaces of the permanent at J (the hard link L-gct-086)
**The problem.** L a complex linear space of n x n matrices with perm(J + t) = n! for all t in L ("level space"); since L
is linear this says all subpermanent sums S_k (k = 1..n) vanish on L, where perm(J + t) = sum_k (n-k)! S_k(t)
(L-gct-084). L-gct-086: is dim L <= C n? (desk: "it may be false"). Known on the fleet's board: a space of dimension
2n - 3 (L-gct-080), reduction to doubly centred (DC) spaces at cost 2n (L-gct-092), LS(3) = 3 (094), 4 x 4 <= 6 (214),
4 x 5 <= 7 (215), DC 4 x 4 <= 3 (216), RC 4 x 4 = 5 (217); open: LS(4) = 5 (091), the 4 x 5 search for dimension 7 (179).

**2.1 The low layers on DC matrices.** On doubly centred t (row and column sums 0):
S_2 = p_2/2, S_3 = (2/3) p_3, and S_4 = (3/2) p_4 - (3/4)(R_4 + C_4) + (1/4) tr((t t^T)^2) + (1/8) p_2^2, where
R_4 = sum_i (sum_j t_ij^2)^2 and C_4 = sum_j (sum_i t_ij^2)^2. The power-sum coefficients 1/2, 2/3, 3/2 are (k-1)!/k.
- Status as recorded: numerical fits at n = 4..7 (relative error about 1e-15), mine; the fleet has all three as checked
  nodes (L-gct-105, 106, 134: 24 S_4 = 36 p_4 - 18(R_4 + C_4) + 6 tr((t t^T)^2) + 3 p_2^2). Locator:
  `MAPPING_BY_READING_20261123.md` A5; Hessian at J from our GCT_KRON O-011: (n-2)! (J - I) (x) (J - I), eigenvalues
  -(n-1) on the row and column parts and +1 on the DC part (A3).
- **The cumulant route** (my hypothesis): on a level space log perm(J + lambda t)/n! vanishes identically in lambda; with
  sigma a uniform random permutation, perm(J + t)/n! = E prod_i (1 + t_{i sigma(i)}), and the order-k cumulant term is
  -(-1)^k p_k/(k n) plus joint cumulants of the variables Y_j = sum_i t_{i sigma(i)}^j. At orders 2 and 3 everything is
  proportional to p_2 and p_3 (Var Y_1 = p_2/(n-1), Cov(Y_1, Y_2) = p_3/(n-1) on DC matrices); at order 4 the joint
  cumulants bring R_4, C_4 and tr((t t^T)^2), so S_4 is not a multiple of p_4 and the route "S_k ~ p_k, then iterated
  Fermat gives dim <= n^2/(K+1)" stops at order 4. Its full-order form is route R2 below.
- **Bound from layers 2 and 3:** LS(n) <= n^2/3 + 2n (agent a3533d80, Claude Opus 5.5 at effort max; Codex sharpened to
  floor(n^2/3) + 2n - 2 using S_1 = 0): by 092 reduce to the DC core; S_2, S_3 vanish there, so p_2 and p_3 do, and the
  fleet's L-gct-061 gives 3 dim <= n^2. Through L-gct-077 this gives 3N + 10m >= 2m^2 + 14, one more than L-gct-070
  (assembly not formalized; extension entry X-gct-006).

**2.2 The real case.** On real DC matrices S_2 = |t|^2/2 > 0, so a real core is 0: real p x q level spaces have dimension
<= p + q - 2 (the fleet's checked L-gct-158); for complex L, L cap conj(L) is the complexification of a real level space,
so dim(L cap conj L) <= 2n - 2 and the whole complex excess is totally non-real. Codex extended the real 2m - 2 bound at
Sigma_m to rows with one entry of either sign (exceptional-row Hessian inertia; `desk/CODEX_TO_CLAUDE_EXCEPTIONAL_ROW_HESSIAN.md`).
The complex version at Sigma_4 is false: the fleet's L-gct-087 has a non-real 7-dimensional space.

**2.3 The Taylor-order barrier** (agents of 23 Nov, Claude Opus 5.5 at effort max; rederived for our GCT map; Codex
sharpened the count). For q | r <= n and omega a primitive q-th root of unity, the family F_{q,r} (first r rows in r/q
blocks, block I having rows omega^a c_I, a in Z_q, c_I free) has dimension (r/q) n, and S_k vanishes on it unless q | k
and k <= r (Moebius inversion over set partitions; each block contributes sum_a omega^(a|beta|) = 0 unless q | |beta|).
Hence any set of orders whose vanishing forces dim <= C n must contain about n/(C+1) orders; no bounded-order argument
(power sums, Kneser-type bounds, the order-4 identity) can prove L-gct-086. Locators: `fleet_map/gct.md` 5.1(c);
`MAPPING_AGENT_RESULTS.md` section 1; extension X-gct-001.

**2.4 Further structure.** Self-similarity: level spaces inside F_q are the level spaces of a q-uniform hyper-permanent
(X-gct-002). Codex: rook polynomials multiply on block-diagonal perturbations, so d(n + r) >= d(n) + d(r) and
lim d(m)/m = sup d(n)/n (amplification, X-gct-003); at prime powers dim L <= (n - 1)(r + 1) for the one-step defect r of a
row cycle (X-gct-004, via the row-translation theorem L-gct-211). A DC family u (x) (1, z, ..., z^(n-1)) gives
kappa(n) >= n - 2. Fable (Claude Fable 5.2 at effort high): a finite-free-probability dictionary (level = the expected
characteristic polynomial of a random generalized diagonal is lambda^n), no new bound (`mirror/BIG_ONES_CONNECTIONS.md` 2.2).
- **Open, with its gate.** L-gct-086: an argument using Theta(n) Taylor orders. Routes: R1 induction on q for the
  hyper-permanent; R2 a Kneser inequality for all singleton-free invariants N(pi, sigma) up to order Theta(n); R3 a defect
  bound for row cycles. LS(4) = 5 (091): an exact certificate in the rational chart. 179: the 4 x 5 dimension-7 search
  (held 17:08-17:46, released unsearched).

## 3. L-meta-782 (promise bound for AND/OR circuits)
- **Statement.** C a circuit of AND/OR gates of fan-in 2; outputs o_i whose accepted singletons L_i = {a : o_i(e_a) = 1}
  lie in S_i with |L_i| >= 2; |S_i cap S_j| <= 1; o_i rejects every input of weight <= k avoiding S_i; c_i <= k and
  c_i + 1 <= |L_i|. Then sum c_i <= |C|.
- **Proof in outline (mine).** Call a wire private for i if its accepted singletons lie in S_i and number >= 2; private
  gates for different i are disjoint (two sets share <= 1 index). From o_i follow input edges through private gates: the
  closure P and its exits X satisfy |X| <= |P| + 1 (each reached node is an input slot of P). The output is a monotone
  function of the exit values (cut property). If |P| < c_i: the leaving exits give an input x of weight <= k avoiding S_i
  with o_i(x) = 0 (promise), and some a in L_i is accepted by no small exit; then o_i(e_a) <= o_i(x) = 0, a contradiction.
  Sum over i.
- **Files.** `mirror/proofs/M-003_L-meta-782_promise_bound.md` (public); Lean built clean 17:22 UTC by an agent (Claude
  Opus 5.5 at effort max): `mirror/lean/L_meta_782_ours.lean`. The fleet merged another proof (PR #1204) at 17:17:57.

## 4. L-meta-750 (greedy window lemma)
- **Statement.** For monotone h_1..h_T on the cube and K >= 1 there are y and D with h_j(y) for j in D, every other h_j
  false on the radius-K window above y, and |y| <= K|D|.
- **Proof.** Greedy: start from y empty, D empty; while some h_j outside D is true somewhere in the window, move y there and
  set D to the indices true at y; D grows by monotonicity, each round adds at most K ones (induction on T - |D|).
- **Files.** `mirror/lean/L_meta_750.lean` (built, axioms clean; public). Withdrawn at 16:43 as proved by another.

## 5. The C4-free edge-function line (L-meta-647, 608, 606, 632, 655, 617, 650)
- **L-meta-647, one-sided circuits** (`L_meta_647_PARTIAL_PROOF.md`, mine, no second reader): normal form F_w =
  OR_v (z_v AND alpha_{w,v}); no mixed OR; the centres of the first multiplying ANDs form a vertex cover (so >= tau
  multiplying ANDs, no König needed); reads identity |C| = |X| + |Y| - 1 + e_Y + e_D. The counting step was completed on
  paper by our map agents (`fleet_map/meta.md` 5.1 and `clb.md` 5.1, two derivations, Claude Opus 5.5 at effort max):
  #OR >= |E| - 1 through a transposition (the fleet's L-meta-738, checked 16:51 by another) and the checked 529/696/697,
  #AND >= tau through the centres; so |C| >= |E| + tau - 1, exact. Consequences recorded there: 720, 655 has no witness,
  the line-degree-1 size of PG(2,q) incidence is N(q + 2) - 1.
- **L-meta-608** (girth >= 5: every monotone fan-in-2 circuit has >= |E| + tau - 1 gates) and **606** (|E| <= c (size + 1)):
  proved for circuits with one level of AND gates (X-meta-002; agent a58224616ed89704f, Claude Opus 5.5 at effort max);
  exact SAT: no counterexample on connected girth-5 graphs with <= 7 vertices (`L_META_632_RESULTS.md`). Literature:
  Jukna, On Graph Complexity (ECCC TR04-005), Theorem 7.3 gives the formula case (c = 2); for circuits, 606 on PG(2,q)
  incidence is Jukna's open n^(3/2) problem (ECCC TR05-021, Problem 24). Fable's Theorem C (weight barrier): on the
  affine-plane incidence graphs, circuits of <= 28 w n gates reject every independent set of <= w vertices, so any proof
  must use independent sets of growing size (X-meta-001). Gate: nested AND gates.
- **L-meta-632** (AND count of the maximal-independent-set partial function = tau on C4-free graphs): proved for every
  graph emptied by deleting a leaf with its neighbour (forests), by the restriction x_K = 1, x_{N(K)} = 0 (X-meta-003);
  depth-one output gates are stars; gate: the elimination lemma EL* (held on 1,927 solver circuits); outside PR #917
  claims a counterexample on 11 vertices (unchecked).
- **Searches.** 655 (subdivided K4, one-sided): no circuit with <= 11 gates, both sides (CaDiCaL); 617 (3-cube): none
  with 7, 8 or 9 gates (the fleet now posts 969/970: <= 11 / >= 12); 650 (PG(2,3) incidence, <= 63 gates, a 608
  counterexample): held and released unsearched; the main session's map puts its plane in Singer form
  ({0,1,3,9} mod 13, symmetry group of order 78; AG(2,3) = tetracode; 64 = 44 + 16 + 4; X-meta-004).

## 6. L-lib-123 (three-alternation speedup, FP3), from the Fable agent (Claude Fable 5.2 at effort high), no second reader
- **Theorem A:** if the step records of a 2^(qm)-time stack machine have (SAT-oracle) circuits of size 2^(am), 2a < q,
  then FP3 (2a) q holds for it (guess the circuit; universally check a pair of steps and a stack); contrapositive: refuting
  L-lib-123 needs exponential SAT-oracle circuit lower bounds for E. **Theorem B:** two-stack machines satisfy FP3 3 4
  (planar step graphs, separators). Gate: three stacks (no sublinear separators); OpenAI's one-tape T^(2/5) space result
  and the ETH manuscript meet at one obstruction (equality does not factor over blocks). `mirror/BIG_ONES_CONNECTIONS.md`.

## 7. Where things are
- **Fleet mirror** `fleet_mirror/` (README): all 1,536 fleet lemmas, tagged (topic and structure), with plain and Lean
  statements, status, dependencies, accepted Lean file, last attempt, and every line of our work that mentions each id
  (`OURS_BY_FLEET_ID.md`); `INDEX_BY_TAG.md`, `BY_PROGRAM/`, `GRAVEYARD.md`, `CHANGELOG.md`; refreshed hourly.
- **Joint GCT lemma space** `fleet_map/JOINT_GCT_LEMMA_SPACE.tsv/.md` (agent, Claude Opus 5.5 at effort max): 1,563 rows
  (226 fleet, 1,337 ours) with typed cross edges (same_statement, improves, uses, parallel, refutes, open_target_of,
  candidate); read the .md by cluster. Their board has no rows for border rank, positivity, Kronecker/plethysm or
  multiplicity obstructions, where we have hundreds.
- **Mirror tree** `mirror/MIRROR_TREE.tsv` (24 rows: our and Codex's lemmas with the fleet nodes they cover, state,
  files); **extension** `mirror/extension/` (our lemmas placed in the fleet's graph: `entries/X-*.md`, `ROADMAP.md`);
  public: github.com/KokunoYumeto/pequalnp-mirror.
- **What we know that the fleet does not:** `WHAT_WE_KNOW_THAT_THEY_DONT_20261123.md`; program maps `fleet_map/*.md`;
  the main session's field maps `fleet_map/maps/`; the moonshine swarm (running) writes `moonshine/`.
