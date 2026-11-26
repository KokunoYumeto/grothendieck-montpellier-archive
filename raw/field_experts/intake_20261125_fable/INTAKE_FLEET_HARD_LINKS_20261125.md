# FLEET_HARD_LINKS (prompt 96), checkpoint 07 of 25 Nov 2026, 07:25 UTC: intake note for the results graph

By Claude Opus 5.5 at effort max (agent a4ee2342403cca87e, session 672ae3a0), 25 Nov 2026. The run: GPT-6 Astra (ChatGPT
Pro mode); its records say "inherited effort not separately exposed"; at checkpoint 07 its ledger schedules a further
review at 08:04 UTC. Earlier intake of the same checkpoint, by this agent:
`field_experts/intake_20261121/intakes/FLEET_HARD_LINKS/INTAKE_FLEET_HARD_LINKS_20261125_cp07.md` (with its
CHECK_EVENTS file, now 8 rows). Return: `research_returns/FLEET_HARD_LINKS_checkpoint_07_20261125T0725Z_unzipped/
workbench/` (below "wb/"). Not opened, by rule: the external-source extract named in the earlier intake.

## What the return adds, by result (ids RUN:TAG from wb/STATEMENTS.tsv and wb/CROSSWALK.tsv)

Part A (level spaces of the permanent at J):
- FLEET_HARD_LINKS:A-WEIGHTED-BOUND (thm:weighted-bound, wb/papers/A/weighted.tex 51-163, with
  lem:weighted-moment-stabilizer 4-49): every complex level space of order n >= 3 has 3 dim L <= n^2 + 2n - 1; with
  fleet L-gct-077 the run states A-BORDER-WEIGHTED, border dc(perm_m) >= m^2 - 2m + 1 - floor((m^2-2)/3).
- FLEET_HARD_LINKS:A-CYC-02 (thm:rowcycle, wb/papers/A/symmetry.tex 4-68): 6 x 6 level spaces invariant under a full
  row (or column) six-cycle have dimension <= 10; A-ST-02e052d2f6896621 (cor:defect, 70-76): dim L <= 10 + 5r with
  r = dim L - dim(L cap TL); A-ST-1bf9a274fbadb87c (prop:twotransitive, 78-85): a two-transitive row symmetry gives n - 1.
- FLEET_HARD_LINKS:A-SYM6 (thm:scalar-six, symmetry.tex 92-117): a 6 x 6 level space on which some element of
  (S_6 x S_6) x <transpose> acts as a scalar omega != 1 has dimension <= 10.
- FLEET_HARD_LINKS:A-HOOK (thm:hook, symmetry.tex 119-143): a subspace containing the hook H_(p,q) on which S_1, S_2, S_3
  vanish equals the hook.
- Further A results not read by me: the Klein slice (A-KLEIN-EXACT, -24, -DIM2, -NOEXT; papers/A/klein.tex), the
  connected cumulants c_5, c_6 (A1-connected), the zeta formulation (zeta.tex), the hyper-permanent reduction
  (hyper.tex), the stabilizer and gate-failure sections.
Part B (monotone circuits of C4-free graphs):
- FLEET_HARD_LINKS:B-PURE-PRODUCT-CUT (thm:purecut, wb/papers/B/pure_cut.tex 4-28): one deleted addition forces
  D >= 2^d - 1 and, at girth >= 5, a matching of missing edges.
- FLEET_HARD_LINKS:B-ST-b6442e345004bda8 (thm:one-not-threshold, wb/papers/B/threshold.tex 8-24) and cor:threshold-bound;
  the run's crosswalk (wb/CROSSWALK.tsv:135) maps them to fleet L-meta-714 and 715.
- Not read by me: the gain-four exclusions (B_NEAR_OPTIMAL_D6_E1, two_cut.tex, three_cut.tex, two_visible.tex,
  one_cut.tex, with RUP certificates), the gain-three exclusions (lower_gain.tex, six_path.tex, B-D6-PATH-ROOT,
  B-D6-SINGLETON-UNION), degree_two.tex, negation.tex (the Beals-Nishino-Tanaka bound), light_inputs.tex, the
  PG(2,4) hyperoval computations, searches.tex.
Part C (#SAT modulo p and the Artin-Mazur height):
- Not read by me: height.tex (the exact replica/orbit height-two criterion), uniform.tex, unary.tex (C-UNARY-*),
  space.tex and quasi.tex (FPSPACE and the quasi-F-split matrix bound), height_three.tex, witness_degree.tex (C3),
  theta.tex (C6), class_groups.tex, div_discs.tex, deformation.tex, point_counts.tex, counting_height.tex.

## What I checked and found (submitted from staging/a4ee2342403cca87e/: checks.jsonl 6-9, checks2.jsonl, checks3.jsonl)

- A-WEIGHTED-BOUND: targeted proof check of every step: no gap found. A-WEIGHTED-IDENTITIES: the S_2 and S_3 marginal
  identities rederived; the S_3 expansion agrees with my own formula checked numerically at n = 4, 5, 6 on 23 Nov.
- A-BORDER-WEIGHTED: arithmetic by hand: 74 at m = 12, against 60 from fleet L-gct-070; the gain is about (4m-6)/3.
- A-CYC-02: targeted proof check: no gap found (the first assertion of lem:evenelementary read, not recomputed).
- cor:defect: no gap found. A-SYM6: my recomputation of the cube-root multiplicity table agrees (6, 4, 4, 6, 12, 10,
  12, 6, 8, 10, 12); the transposition table not recomputed.
- B-ST-b6442e345004bda8: targeted proof check of the theorem and corollary: no gap found; the formal statements of
  L-meta-714/715 were not compared.
- B-PURE-PRODUCT-CUT: the combinatorial steps (lines 16-28) checked, no gap found; the reduction of lines 12-14 rests on
  Paper B definitions I did not read.
The run's own 453 check events (all by workers of GPT-6 Astra (ChatGPT Pro mode)) are in wb/../CHECK_EVENTS.tsv.

## Relations (submitted: staging/a4ee2342403cca87e/relations.jsonl, lines 7-15)

- A-WEIGHTED-BOUND uses fleet L-gct-065 (Mirandola-Zemor Theorem 3.3; mirror RESULTS.tsv:113).
- A-BORDER-WEIGHTED sharpens fleet L-gct-070 (RESULTS.tsv:118), through fleet L-gct-077.
- A-CYC-02 is parallel to fleet L-gct-211 (prime n) and sharpens fleet L-gct-086 at n = 6 within the row-cycle class.
- A-HOOK sharpens fleet L-gct-179 (no 7-dimensional 4 x 5 level space contains the hook).
- B-ST-b6442e345004bda8 is parallel to fleet L-meta-714 and 715 (titles agree; formal comparison pending).
- B-PURE-PRODUCT-CUT sharpens fleet L-meta-612 and 608 (constraints on counterexamples).
Points submitted (points.jsonl lines 6-13): thm:weighted-bound, its lemma, thm:one-not-threshold, thm:rowcycle,
cor:defect, thm:scalar-six, thm:hook, thm:purecut, by file and lines.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Compare thm:one-not-threshold and cor:threshold-bound with the Lean statements of L-meta-714 and 715; if they match, enter X-entries | B-ST-b6442e345004bda8 | main |
| Enter an X-entry: the weighted bound and its border consequence improve the checked fleet L-gct-070 | A-WEIGHTED-BOUND, A-BORDER-WEIGHTED | main |
| Formalize thm:weighted-bound in Lean (inputs: fleet L-gct-065, linear algebra, the gcd case analysis) | A-WEIGHTED-BOUND | main (Lean pass) |
| Read and check Paper C's height-two criterion (height.tex) and its completeness results (uniform.tex, unary.tex) | C1-height, C-UNARY-* | a field expert of the counting line (Claude Opus 5.5) |
| Read and check the gain-four and gain-three exclusions with their RUP certificates | B_NEAR_OPTIMAL_D6_E1, B-D6-PATH-ROOT, B-D6-SINGLETON-UNION | a field expert of the circuit line |
| Read the Klein-slice section and the hook proof | A-KLEIN-*, A-HOOK | this agent or the level-space expert |
| Take in the final checkpoint of the run when it lands (it was still running at 07:25 UTC) | FLEET_HARD_LINKS | main |
| Decide what happens to the external-source extract in the unzipped checkpoint folder (named in the earlier intake, section 7) | `_from_earlier_checkpoints` of cp07 | the user |
