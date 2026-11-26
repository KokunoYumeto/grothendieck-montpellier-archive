# FLEET_HARD_LINKS (prompt 96), checkpoint 07 of 25 Nov 2026, 07:25 UTC: intake

Intake by Claude Opus 5.5 at effort max (agent a4ee2342403cca87e; pequalnp session 672ae3a0), 25 Nov 2026. Return:
`research_returns/FLEET_HARD_LINKS_checkpoint_07_20261125T0725Z_unzipped/`. Prompt:
`TO_SEND/PRO/1_Archive_research_by_topic/SENT/96_FLEET_HARD_LINKS/PROMPT.md`. Production model: GPT-6 Astra (ChatGPT Pro
mode); the run's records say "inherited effort not separately exposed". The run is still in progress (next review was due
08:04 UTC); this intake is of checkpoint 07. Read: the prompt (parts A level spaces, B monotone circuits of C4-free
graphs, C #SAT as a Hasse-Witt scalar); LEDGER.md in full (three formal reviews), README, QUESTIONS (statuses), CHECK_EVENTS
(tallies and the A-WEIGHTED rows); in full: `papers/A/weighted.tex` (the new unconditional bound) and the theorem and
corollary of `papers/B/threshold.tex`. Not opened: the other 45 TeX files of the three papers, the research reports, the
certificates and programs. Not opened by rule: the external-source extract named in section 7.

## Most interesting items, ranked by usefulness

1. **Part A, the hard link L-gct-086: a new unconditional bound 3 dim L <= n^2 + 2n - 1** (thm:weighted-bound,
   A-WEIGHTED-BOUND), so LS(5) <= 11, LS(6) <= 15, LS(7) <= 20. **I checked every step (section 8).** Through the checked
   L-gct-077 it gives border dc(perm_m) >= m^2 - 2m + 1 - floor((m^2 - 2)/3) (A-BORDER-WEIGHTED; 74 at m = 12), which beats
   the fleet's checked explicit bound L-gct-070, (2m^2 - 10m + 11)/3 (60 at m = 12), by about (4m - 6)/3 at every m.
2. **Part B: the one-NOT threshold theorem** (thm:one-not-threshold and cor:threshold-bound): conditional on the monotone
   bound sum (|S_i| - 1)_+ for families of sets meeting pairwise in at most one point, a circuit with at most one NOT has a
   threshold W with the two restricted sums bounded by |C|. Its titles match the open fleet nodes **L-meta-714 and 715**;
   I checked the proof (section 8). Candidates to settle both, after a comparison with their formal statements.
3. **Part B, L-meta-608 / 612 at four missing quadratic witnesses:** every gain-four profile is excluded (the optimal
   D6,e0 and D7,e0 profiles and D6,e1), at gain three the missing graphs P4 + K2 (D5 and D6) and K3 + K2 (D5,e0) are
   excluded, and a profile with exactly one deleted addition needs D >= 2^d - 1 (B-PURE-PRODUCT-CUT; at girth >= 5 the
   missing-edge graph must then be a matching). Gain two and the other gain-three branches remain.
4. **Part C:** an exact replica/orbit criterion separating Artin-Mazur height two from height >= 3 at every prime
   (C1-height); promised height-two decision is Mod_pP-complete at every p, height three complete at p = 2; exact
   height is #P-hard (nonadaptive oracle reductions) and in FPSPACE, with dense time 2^(O(d log p)) poly(s, d, log p)
   via the quasi-F-split matrix method (credited to Kawakami-Takamatsu-Yoshikawa and Batubara-Garzella-Pan, with
   Yobuko); fixed-prime unary-height decision is Mod_pP-complete. "Count-only" dependence is refuted: equal counts can
   give different height-two status.
5. Part A, symmetry classes and slices: at n = 6, level spaces invariant under a full 6-cycle, or with a nontrivial scalar
   symmetry, have dimension <= 10; the 9-dimensional hook is inclusion-maximal (A-HOOK-MAXIMAL); the Klein slice is
   exact (S_2, S_4; 24 flex lines; mixed planes <= 2; the pure flex lines do not extend) after a correction of the seed
   basis (E01 to E02). An 11-dimensional example at n = 6 must avoid all three classes.
6. Part C side results: the witness degree c_p equals c_0 outside finitely many primes for fixed integral orbit data
   (C3); the maximal affine families of odd theta characteristics in genus g have dimension g - 1, one per isotropic
   (g-1)-space, (2^g - 1) prod_{j=2..g} (2^j + 1) in number (C6, asked as input to L-pcx-071's route).

## 1. Useful or not

Yes, in all three parts, but no main question is settled: A1-uniform (L-gct-086), A1-six (LS(6) <= 10), B1-unrestricted
(L-meta-608) and the full complexity of the height (C1) are open with strictly smaller gates. The most usable item for
the fleet is the weighted bound (item 1), whose border consequence improves a checked explicit bound.

## 2. What it proved (statements, hypotheses, check status)

- A-WEIGHTED-BOUND (Paper A, thm:weighted-bound): n >= 3, L a complex level space: 3 dim L <= n^2 + 2n - 1. Proof: map A
  to (b_ij; alpha r_i; alpha c_j) with b = a - (r + c)/2, alpha = -(n-2)/(2n), weights 1 and -lambda, lambda =
  n^3/(n-2)^2; the weighted moments of degree 1, 2, 3 vanish (identities 2S_2 = sum b^2 - (n/4)(sum r^2 + sum c^2) and
  (3/2)S_3 = sum b^3 + ((n-2)/8)(sum r^3 + sum c^3)); the weighted Kneser lemma (lem:weighted-moment-stabilizer, after
  Mirandola-Zemor Thm 3.3, the fleet's L-gct-065) gives 3 dim V + dim H <= M when H cap V = 0; zero-weight blocks of the
  stabilizer exist only at n = 4 (16, 1) and n = 6 (27, 2) and are excluded by the marginal-sum constraint. Run checks:
  targeted proof checks (a_final_referee, a_weighted_referee) and a statement-first re-derivation, all GPT-6 Astra
  (ChatGPT Pro mode).
- A-BORDER-WEIGHTED: with L-gct-077, border dc(perm_m) >= m^2 - 2m + 1 - floor((m^2-2)/3); 74 at m = 12.
- A, other rows: six-cycle-invariant and scalar-symmetry bounds 10 at n = 6; hook maximality; Klein slice (A-KLEIN-EXACT,
  -24, -DIM2, -NOEXT); exact connected rook cumulants c_5, c_6 (A1-connected); the zeta formulation is only a
  reformulation (A1-zeta); general cyclic/abelian invariant bounds, n = 6: 10 + 5r (A5-cycle-defect); the root-of-unity
  block reduction is exact but the induction needs a dimension inequality (A5-hyperpermanent).
- B: thm:one-not-threshold and cor:threshold-bound (conditional on the monotone base bound, stated as a hypothesis); the
  four-missing-witness exclusions (B1-four-missing), the single-addition theorem (B-PURE-PRODUCT-CUT, D >= 2^d - 1), a
  size-preserving normalization of shared bilinear two-level architectures under a universal-row condition (B1-degree-two,
  B1-two-AND-levels), the bihomogeneous component lemma (B5), the PG(2,4) threshold functional 14 and the 168 hyperovals
  (B4), the Beals-Nishino-Tanaka negation bound and the near-linear endpoint at ceil(log2(q^2)) NOT gates (B3).
- C: C1-height (exact finite coefficient rule, infinity detected), C1-complexity (as in item 4), C2 model-dependent rank
  results, C3, C5 (exact DIV local identities with precise discs), C6.
Checks by others: none. All 453 check events are by workers of GPT-6 Astra (ChatGPT Pro mode): 244 targeted proof checks,
81 independent re-proofs (same model, from the statement), 61 computations or certificates, 59 used and rechecked, 6
refutations with refined statements. No other model and no human; my checks are in section 8.

## 3. New since the prompt's starting point

The prompt's baseline: our LS(n) <= floor(n^2/3) + 2n - 2, the barrier X-gct-001, the self-similarity X-gct-002; for B
the one-sided and at-most-three-missing theorems; for C the height-1 test (NK-6) and COUNTING_VARIETIES. New: the
weighted bound (A), its border consequence, the n = 6 symmetry-class bounds, hook maximality, the exact Klein slice;
the gain-four and partial gain-three exclusions, the single-addition theorem, the one-NOT threshold theorem (B); the
exact height-two criterion with its completeness results, FPSPACE membership, the unary-height classification (C).
Corrected: our torus-deformation route (AG_HODGE_ANT.md B.2) and the prompt's account of it (section 7).

## 4. Open: each main question's gate (from the 07:04 review)

- A1-uniform (L-gct-086): no uniform bound and no superlinear family. A1-six: 9 <= LS(6) <= 15; an 11-dimensional example
  must avoid full 6-cycle invariance, nontrivial scalar symmetry and hook containment. A2-four: 5 <= LS(4) <= 6.
  A2-four-by-five (L-gct-179): the 6-dimensional hook is inclusion-maximal; a 7-dimensional space is undecided.
- B1-unrestricted (L-meta-608): needs >= 4 missing quadratic witnesses and mixed variables on both sides; B1-four-missing:
  gain two (D,e) = (5,0) and gain three (5,0), (5,1), (6,0) remain, apart from the excluded missing graphs. B2 (affine
  AG(2,3) below 44, PG(2,3) at 63 = L-meta-650, infinity additivity): open; every SAT run timed out (UNKNOWN at 300 s).
- C1-complexity: the full function lies between nonadaptive #P-hardness and FPSPACE; binary-height and infinite-height
  decisions are open.

## 5. Relations

- A: the weighted bound strengthens our MAPPING_AGENT_RESULTS 1.2 (LS(n) <= n^2/3 + 2n, from L-gct-061) by replacing
  double centring with weighted marginal coordinates; the fleet's checked L-gct-070 corresponds to the older level bound
  (n^2/3 + 2n - 1 at n = m - 1), so the new bound improves it directly.
- B: continues prompt 93's paper 4 (thm:threemissing) and our X-meta-005/006; the threshold theorem is the base case of
  the fleet's checked NOT recursion L-meta-739/745.
- C: builds on NEG_NIGHT (p = 2) and COUNTING_VARIETIES (all p); the quasi-F-split algorithm is external and credited.

## 6. Candidates

- X-entry: the weighted bound with its border consequence (improves checked L-gct-070); checked here by hand.
- X-entries after a formal-statement comparison: L-meta-714 and 715 from thm:one-not-threshold and cor:threshold-bound.
- Hexagon: Paper A's weighted bound is a short self-contained note (a Kneser-type argument after Mirandola-Zemor), and
  Paper C's height-two criterion with its complexity is a candidate once a second model has read it.
- Lean: the weighted bound uses only L-gct-065 (checked), linear algebra and the gcd case analysis; it is a realistic
  formalization target that would improve a checked fleet node.

## 7. Problems, with the exact passages

- An external source was copied into an archive. LEDGER, 04:25 UTC: "The archive inadvertently included one external-
  source extraction, research/c_main_referee/lauder_wan_published_extract.txt. This violates the no-source-copy
  requirement". The copy is still on disk in this unzipped return at
  `_from_earlier_checkpoints/.../research/c_main_referee/lauder_wan_published_extract.txt` (97,656 bytes, from checkpoint
  03). I did not open it. It must not go to any repository; deleting or moving it is the user's call.
- Our deformation route was wrong. LEDGER, 02:10 UTC: "Two separate readers found the claimed torus-deformation
  implication unsupported: the specified symmetry group is finite." This concerns Proposition B.2 of our AG_HODGE_ANT.md
  and the prompt's sentence "by Proposition B.2 an extremal space is a deformation of a special point".
- A displayed basis was wrong and was corrected. LEDGER, 05:04 UTC: "The full expert A read corrected the displayed Klein
  basis from E01 to E02."
- Our Theorem E (Singer line-ORs with NOTs) cited the negation-limited bound from memory; the run's row B3-negation reads
  "Correct BNT bound and nearlinear endpoint proved at ceil(log2(q²)) NOTs". Compare it with X-meta-102/103 before those
  entries stand. I did not open `negation.tex`.
- No search result is evidence of nonexistence: "Unrestricted63gate pruned encoding UNKNOWN after300s; no witness or
  certified lower bound" (B2-PG23), and likewise B2-affine, B4-root39, B4-root59.
- Two B candidates are not accepted. LEDGER, 07:24 UTC: "Two separate B candidates, P4 disjoint K2 with excess one and P3
  disjoint2K2 with an optimal five-deletion frame, remain pending statement-only independent reproofs".
- Single-model checking throughout. README: "Separate workers in this workbench use the same model, GPT-6 Astra Pro, with
  inherited effort".

## 8. For the fleet

| Fleet node (live status, mirror of 25 Nov) | Result | Relation |
|---|---|---|
| L-gct-086, open (hard link) | thm:weighted-bound, 3 dim L <= n^2 + 2n - 1 | sharpens (quadratic; does not settle). |
| L-gct-070, checked: border dc(perm_m) >= (2m^2 - 10m + 11)/3 | thm:weighted-bound + checked L-gct-077 | **sharpens a checked node**: m^2 - 2m + 1 - floor((m^2-2)/3), better by about (4m-6)/3 at every m (74 vs 60 at m = 12). Checked by me (targeted proof check); same-model checks in the run. **Flag for an X-entry** (improvement of a checked node, not settlement of an open one). |
| L-gct-091, open (LS(4) = 5) | A2-four | no change: 5 <= LS(4) <= 6 (checked 214). |
| L-gct-179, open search (4 x 5, dimension 7) | A-HOOK-MAXIMAL (the 6-dimensional hook does not extend) | parallels; the search stays open. |
| L-gct-211, open (row-shift-invariant, prime n) | A5-cycle-defect (cyclic/abelian invariant bounds; n = 6: 10) | parallels (composite n). |
| L-gct-077, 092, 158, 214-217, 065, 061, checked | used as inputs | used. |
| L-meta-714, open (one NOT: threshold W) | thm:one-not-threshold | **settles, if the formal statements match**; the proof is correct as I read it. Conditional on the monotone base bound, as the fleet's title also is. Flag for an X-entry after the formal comparison. |
| L-meta-715, open (one NOT: min over W of a max of two sums) | cor:threshold-bound | same as 714. |
| L-meta-608 and 612, open | four-missing-witness exclusions, single-addition theorem | sharpen the gate (a counterexample needs >= 4 missing witnesses, gain <= 3, and avoids the excluded missing graphs); no settlement. |
| L-meta-606, 650, 972, 582, open | B2, B4 searches | no change (UNKNOWN). |
| L-meta-739 / 745, checked (NOT recursion) | B3 negation bound | parallels (endpoint at ceil(log2 q^2) NOTs). |
| L-meta-2585 / 2635, open (read-1 conversion) | B5 component lemma | parallels; no decision. |
| L-gct-011, open (Mulmuley-Sohoni) | C3 witness degree c_p = c_0 outside finitely many primes | parallels (specialization of separation degree; no separation). |
| L-gct-103 / 104 / 132 / 147, open (DIV and instances) | C5 exact local identities with discs | parallels. |
| L-pcx-071, open (parked) | C6 odd theta characteristics classification | parallels (an input the route asked for). |

Results that settle an open node and are checked: none settled outright. Two flags: **L-gct-070** is improved by a result
I checked (X-entry as an improvement of a checked node), and **L-meta-714 / 715** are candidates to settle once their
formal statements are compared with the run's theorem and corollary.

### Spot-checks, recorded in the TSV beside this file

- A-WEIGHTED-BOUND, targeted proof check: (i) Sigma b_ij^2 = Sigma a^2 + ((n-4)/4)(Sigma r^2 + Sigma c^2), hence
  2S_2 = Sigma b^2 - (n/4)(...), using 2S_2 = Sigma a^2 - Sigma r^2 - Sigma c^2 on S_1 = 0 (L-gct-159); (ii) (3/2)S_3 =
  A_3 - (3/2)C + (3/2)B + R_3/2, which is the S_3 formula I verified numerically at n = 4, 5, 6 on 23 Nov
  (MAPPING_AGENT_RESULTS 1.1), and Sigma b^3 = A_3 - (3/2)C + (3/2)B + ((6-n)/8)R_3 from Sigma a(r+c)^2 = R_3 + 2B and
  Sigma (r+c)^3 = nR_3; (iii) lambda alpha^2 = n/4 and -lambda alpha^3 = (n-2)/8; (iv) the weighted Kneser lemma:
  W = (C1 + V)^2 is w-orthogonal to V, H = St(W) is unital and lies in W, K = HU has K^2 = W and dim K >= dim H + dim V,
  and Mirandola-Zemor (fleet L-gct-065) gives dim W >= 2 dim K - dim H; (v) a zero-weight block needs a(n-2)^2 = b n^3
  with a <= n^2, possible only at n = 4 (16, 1) and n = 6 (27, 2), at most one block, and its indicator violates the
  marginal-sum constraint. PASS; no gap.
- A-BORDER-WEIGHTED, computation by hand: G = floor((m^2 - 2)/3) at n = m - 1; N >= m^2 - 2m + 1 - G = 74 at m = 12;
  L-gct-070 gives 179/3, i.e. 60, at m = 12.
- thm:one-not-threshold, targeted proof check: the input h of the single NOT is monotone; W = 1 + max{|a| : h(1_a) = 0};
  setting the inputs outside a to zero makes NOT h constant 1, and setting a W-set b to one makes NOT h constant 0
  (monotonicity of h on the down-set of 1_a and the up-set of 1_b); constant propagation leaves
  monotone circuits for the restricted disjunction families (intersections still at most one point), to which the base
  bound applies. PASS. The match with the formal statements of L-meta-714/715 is not checked.
