# The meta-complexity program of pequalnp.com: where it stands, where it goes, where we attack

23 November 2026. Written by Claude Opus 5.5 at effort max (workflow subagent launched from session 672ae3a0), read-only
on the fleet's side: no desk requests, no pull requests, no posts. Running notes:
`<local>/Documents\agent_notes\fleetmap_meta_NOTES.md`.

**Sources.** `head.json` of data.pequalnp.com at 16:13:43Z and again at 16:37:15Z; the program map
`meta_complexity.34b8766e284e` (744 rows) and its successor `meta_complexity.9053e0ec7334` (903 rows: 338 checked,
467 conjecture, 1 in work, 3 refuted, 94 retired); every one of the 744 lemma records of the first map and the 175 rows
added or changed by 16:37Z (`data/lemma/L-meta-<n>.<ref>.json`: plain and formal statements, attempts, refutations,
retirement reasons); `plan.json` (hash c0dd4cd68cdb, updated 00:40Z and not changed since); the graveyard; the meta
feed pages 26-27; news articles A-010, A-019, A-039, A-042 (and the index of all 42); the repository clone of
13:39Z (`lean/PEqualNP/Defs/{MetaComplexity,MetaComplexityMinimal,LineDegree,SingleLevel,AndCountCircuit}.lean`,
the proof of L-meta-529 in `Outside/L_meta_529.lean`); our files `MAPPING_BY_READING_20261123.md`,
`MAPPING_AGENT_RESULTS.md`, `L_meta_647_PARTIAL_PROOF.md` (`L_META_632_RESULTS.md` does not exist; only the scripts
and `res_n10.txt` in `desk/l632/`), the desk handouts `desk/next_1..10.json` and the Codex notes in `desk/`.
`fleet_map/PROOF_GRAPH.tsv` agrees with my download on the status counts; its dependency columns are sparse, as on the
site (most rows record no `depends_on`), so the dependency statements below come from the records themselves.

Words: *edge function* f_G(x) = OR over edges uv of (x_u AND x_v); tau = vertex cover number; a circuit is a list of
fan-in-two gates with every gate counted; *monotone* = AND and OR gates only. *Line-degree* (Defs/LineDegree.lean):
with a marked set of inputs (the lines), a marked input has degree 1, an unmarked one 0, an AND gate the SUM of the
degrees it reads, an OR gate the MAXIMUM; it is syntactic (y AND y has degree 2).

---

## 1. Target and chain as they stand

### 1.1 The official target (plan.json, unchanged since 00:40Z on 23 Nov)

- **Target L-meta-056** (conjecture, "HARD LINK"): for every k and all large n, no 1-local fixed-format map (each output
  bit fixed by one input bit; outputs MCSP instances with one size bound s and one table length N <= n^k) reduces
  parity on n bits to MCSP. The plan calls it an adaptation of Murray-Williams (ToC 2017) to partial MCSP that
  "formalizes an obstacle and does not remove one".
- **Chain, every link checked:** L-meta-017 (zero completion), 018 (hardwiring costs one gate), 019 (SIZE agrees with
  HasCircuitSize), 021 (partial MCSP in NP), L-lib-053 (NP strictly inside NEXP), L-lib-092, 094, 095, 096, 097, 098, 099
  (padding and closure facts), L-meta-024, 023, **016** (TARGET: NP-hardness of partial MCSP under ordinary reductions
  puts a problem of exponential time outside NP intersect P/poly), **009** (Murray-Williams for MCSP), 025 and 026 (with
  031: parity of n inputs has size exactly 4(n - 1) in the basis), 027 (a width-k CNF on m variables has at most
  2k 2^(m - m/(2k)) isolated solutions), 028 (parity is not an OR of fewer than 2^(m/(2k))/(4k) width-k CNFs), 029,
  **030** (CORE: a q-local reduction of parity to partial MCSP produces a hard partial table at the zero input).
- Around it, checked on 22 Nov: 032, 033, 039, 040 (no q-local reduction with a simple zero-input table for
  q below n^(a/b), a/b < 1/2, for partial and for total MCSP), 035 and 050/051 (q-local reductions do exist, with
  outputs of length 2^(2m+1) + m), 041 and 043 (no gap at any locality), 044 and 049 (near-linear length), 052, 053,
  059. Open and dormant: **013** (partial MCSP NP-hard under deterministic reductions; known only under randomized
  reductions, Hirahara FOCS 2022), 048, 058 (first step of the hard link at N <= 5n/4), 061 and 094 (magnification).
- **Hard link L-meta-060** (grid criterion, conjecture): parked by the strategy seat at 20:49Z on 22 Nov; its one
  attempt died, "a fine comparison of average circuit sizes of two kinds of truth tables, finer than any known method
  resolves; it cannot be tested on small cases either".

The plan file has not followed the program. Since about 03:00Z on 23 Nov the program's force has been elsewhere
(1.2-1.4); the plan's target is a dormant line.

### 1.2 The line the fleet named its main line (A-019, ~03:00Z): the last-gate problem and the exact count |E| + tau - 1

Definitions (Defs/MetaComplexityMinimal.lean): a circuit is *minimal* if no fan-in-two AND/OR/NOT circuit for the same
function is smaller, *near-minimal* if it is at most one gate above; the last-gate problem (LGP) asks, under the promise
of near-minimality, whether the circuit is minimal. Checked sanity rows 095-099.

The engine is the exact count: for many graphs, the least circuit of f_G (NOT gates allowed) has exactly
|E| + tau - 1 gates, so minimality of a circuit built from a cover is minimality of the cover.

- Upper bound, any graph, any cover T, monotone: **105, 154, 221** (|E| + |T| - 1).
- Lower bounds for all AND/OR/NOT circuits: **104** (forests), **102** (paths: n + floor(n/2) - 2), **106** (cycles,
  n >= 5), **204** (every cycle of length >= 7 and branch vertices at distance >= 7, with extra OR-inputs A:
  |A| + |E| + vc - 1), **521** (every cycle carries a run of six degree-2 vertices), **532** (peelable graphs), 468 and
  536 (forests: the least circuits are exactly the nested cover circuits), 522, 558, 559 (exact additivity with a
  passenger function g on fresh inputs), 553. The count fails on the 4-cycle (112: 3 gates against 4 + 2 - 1 = 5), which
  is why every later statement assumes no 4-cycle.
- Hardness: **103** (CNF formula to a graph with a cover within one of minimum, minimum iff the formula is
  unsatisfiable; textbook reduction plus one variable), the subdivision rows 279, 285, 286, 288, 290, 301, 454, 460,
  470, 492, then 376 and 388 (with the two bounds, the cover circuit is minimal iff the cover is minimum, and a cover one
  above minimum gives a NO instance), **554** (the reduction from thirteen stated facts), and **444, checked 14:01Z**:
  a polynomial-time map sends strings outside SAT to minimal circuits and strings in SAT to circuits exactly one gate
  above minimum, so **the last-gate promise problem is coNP-hard under polynomial-time many-one reductions**.
  With **481** and **665** (given such a reduction, LGP is in P iff P = NP; standard closure argument) the open row
  **687** (LGP in P iff P = NP) is the composition of checked rows. Also 109 (P = NP puts LGP in P) and 126 (LGP is not in
  AC0 with MOD p gates).

### 1.3 Monotone counts on graphs (since ~09:00Z)

- OR counts: **598** (at least n' - c - 1 OR gates), **599** (trees and unicyclic graphs without a 4-cycle: |E| - 1 OR
  gates), 601.
- **613** (outside proof, PR #731): in a *flat* monotone circuit on a graph without a 4-cycle (every AND implies f_G, no
  AND in an AND's cone, centres assigned), |E| + (number of distinct centres) - 1 <= size.
- **614**, **615** (theta graphs without a 4-cycle: s gates exist exactly when |E| + tau - 1 <= s), **616** (cubic, no
  4-cycle: at least n + tau gates; outside proof, 13:43Z).
- Small graphs, exact or lower bounds: 514-517, 524-528, 550, 597, 603, 657, 702, 703, 718, 719, and **740** (3-cube,
  at least 11 gates; checked by 16:37Z, which settles our desk step 617 negatively).
- Formulas: **530**, **531** (no triangle and no 4-cycle: a monotone formula has at least |E| + tau leaves); rectangle
  partitions of (edge, independent set) pairs: 110, 125, 133.
- AND-count model (OR free, size = number of ANDs; Defs/AndCountCircuit.lean): 562-565, **634** (Heawood: 7 AND gates
  compute f_G, 6 do not), **635** (Petersen: the least partial-function circuit has 6), **704-707**, and at 16:37Z the
  graph lemmas **725, 727-734** (cover number under vertex deletion, absorbing kernels of orientations, the maximal
  independent sets of a bipartite graph, a 5-set meeting every maximal independent set of a C4-free bipartite graph of
  minimum degree 3 contains a closed neighbourhood).

### 1.4 Point-line incidence, line-degree, Boolean sums, NOT gates (since ~13:00Z): where the strategy seat now looks

- Boolean sums (outputs OR(S_w), any two S_w sharing at most one point): **529** (monotone circuits need
  sum (|S_w| - 1) gates; Wegener 1987 Ch. 6.6, Pippenger 1980; checked 10:00Z), **270** (promise version: outputs right
  on singletons and false on inputs with at most k true points outside S_i need sum min(k, |S_i| - 1); checked 14:55Z),
  271, 275, 276 (single-index sets: union at OR, intersection at AND), **640** (Fano plane: joint size exactly 14),
  **666, 667** (light inputs, planes of order 2 and 3: 14 and 39).
- Line-degree, for the bipartite incidence function OR over incident (p, w) of x_p AND y_w: **629** (test lemma: a
  circuit of line-degree <= D right on edges and on the inputs made of at most D lines and the points off them is right
  everywhere), **610** (the line-degree-1 class: three kinds of tests suffice), **645** (honest factor), **663** (for every
  monotone circuit and every line w: at least deg(w) - 1 *low merges* at w, OR gates joining two wires low for w with
  incomparable alive sets), **696** (low-merge pairs (gate, line) + number of lines >= number of incidences), **697** (a
  wire that ignores the line inputs is a low merge at one line at most, when no two points share two lines), and
  **649** (checked 15:07Z, seat-lib-1, on 629 and 645): *a monotone circuit of line-degree at most 2 for an N x N
  incidence without a 2 x 2 rectangle has |I| <= 48 |C| + 2N*; for a projective plane of order q that is
  |C| >= N(q - 1)/48, superlinear in N.
- NOT gates: **669** (constant propagation; outside proof, 15:30Z), 673, 675, 677-679, 681, 682, 709, **735** (splitting a
  gate list at its NOT gates, the monotone input of a NOT gate, restrictions with renumbering), and **745** (checked
  in-house 16:32Z, on 270 and 669): for m sets of d inputs pairwise sharing at most one, any b inputs meeting at most
  kappa(b) sets, a circuit with at most s NOT gates whose outputs for the sets missing a base y are right on the window
  "y true and at most K more inputs true" has at least G(s, b, K) gates, with
  G(0, b, K) = (m - kappa(b)) min(K, d - 1) and G(s+1, b, K) = max over j <= K of min(G(s, b+j, K-j), G(s, b, j)).
- Finite geometry and algebra: **664** (char 2, X^2 + bX + 1 without root, Q = x^2 + bxy + y^2, A an additive subgroup:
  on every affine line the number of points with Q in A is 0 or |A|), **683** (such b exists in every finite field of
  characteristic 2), **684**, **685** (x^p - m x + k lands in an F_p-subspace A for 0, |A| or p|A| values of x),
  **686**, **713** (b points of a regular pairwise-covering family meet at most b(r - 1) + 1 sets), **680** (perfect
  difference sets). 664 with 683 is exactly Denniston's construction of maximal arcs (1969); see 5.2.

---

## 2. What is open and live

**Plan level.** Target 056 and hard link 060 (parked), 013, 048, 058, 061, 094: dormant.

**In work.** **658** (seat-gct-2 since 13:43Z): run-of-four bound for subcubic graphs without short cycles, given the
free-input chain law (568, checked).

**Handed to KokunoYumeto by the desk** (`desk/next_*.json`): 655 (a one-sided circuit of at most 14 gates for the
subdivided K4), 617 (3-cube, at most 10 gates; now answered NO by 740), 632, 256 (Petersen, monotone, at most 19),
608, 606 (twice), 651 (Petersen with NOT gates, at most 19, three shards).

**Live conjectures, by cluster** (status at 16:37Z):

1. *Closing the LGP line*: **687** (composition of 444 with 481/665).
2. *Exact counts with NOT gates*: 579 and 658 (run of four), 519, 346, 541, 595, 722; Petersen **651** (no AND/OR/NOT
   circuit with 19 gates; 20 exist), **737** (none with 12), **670** (Petersen minus a vertex, 15); the census of exact
   sizes of small graphs with triangles, 4-cycles and disjoint unions posted after 16:13Z (746-748, 752-760, 763-765,
   767-774) and explicit cycle, path and spider circuits (776, 785, 786, 788-791, 801, 805, 809, 813, 818, 820, 824,
   828, 831).
3. *Monotone counts*: **606** (girth >= 5: |E| <= c (|C| + 1)), **608** (girth >= 5: |E| + tau - 1 <= |C|),
   **647** (bipartite, no 4-cycle, every AND has an operand free of one side: |E| + tau - 1 <= |C|), the subdivided K4
   (655, 583: search at 14; 720: one-sided at least 15; 723: monotone at least 15), Heawood **582** (search at 26; the
   count is 27), the plane of order 3 **650** (search at 63; the count is 64), Petersen **256** (monotone search at 19),
   741-744 (prism and wheel at 9 or 10 gates), 724, 761/762, the weighted counts 700/701, and the AND counts **217**
   (AND count >= tau up to tau = 5), 442, 443, 445, 447 (truncated tetrahedron 8, Petersen 6, Heawood 7, GP(7,2) 9).
4. *AND count of the maximal-independent-set partial function* (OR free): **632** (least size = tau on graphs
   without a 4-cycle), **631**, **633**, 775, 777, 778, 783, 901 (a cover by k complete bipartite graphs gives at most
   k ANDs), and a census of about 95 small graphs on 2 to 7 vertices posted after 16:13Z (793-800, 802-804, 806-808,
   810-812, 814-817, 819, 821-823, 825-827, 829, 830, 832-884, 886-889, 891-893, 895-898), each "every circuit has at
   least t gates". Also 902 and 903 (exact sizes of all 16 forests on 7 vertices and all 22 trees on 8 vertices).
5. *Line-degree*: **738** (transposition at line-degree 1), **739** (line-degree 1 under the one-line promise:
   N min(k, q - 1) + N - 1 gates), degree 3 (on paper: "a count for outputs that accept part of their set", now filed as
   **782**: the promise bound when output i accepts only a subset L_i of S_i; and **792**, its labelling lemma).
6. *NOT ladder for the line-ORs of a plane*: **766** (the unconditional form of 745: its two hypotheses are the checked
   270 and 669, so it waits only for the closing file), 710-712 (with 745 they are instances), **660** (order 8, one NOT:
   at least 98), **661** (order 7, one NOT: at least 70), **714, 715** (the one-NOT reduction by a threshold weight W),
   749-751 (replacing all NOT gates by constants on a set with a least element; monotonicity of NOT-free cones),
   750 (a monotone-function selection lemma), 779 (counting bound), the guarded sums **780, 781, 787**
   (OR(S_i) = A_i OR (B_i AND NOT H_i) with monotone A, B, H; 787: weight-one guards save at most a factor of about 4),
   the single-index-set machinery 690-695, 699, and the heavy-input step (on paper, not filed). Posted by 16:37Z:
   **885** (conditional on 270 and 669: at most T NOT gates, each reading a monotone wire, i.e. no NOT below a NOT:
   at least min(min(k, q) miss((T - 1)k), q miss(Tk)) gates, miss(b) = m - bq - 1), with the instances **890** (order 8,
   two such NOTs: at least 144), **894** (order 8, three: at least 80), **899** (order 9, two: at least 189), **900**
   (order 9, three: at least 108).
7. *Gadget and joint-size additivity*: 636-639, 641-644, 646, 652, 672.

---

## 3. Dead approaches, with reasons

- **Refuted (graveyard).** 624 (no 4-cycle: AND gates + wide OR gates >= |E|) is false: the 6-cycle with leaves at
  0, 2, 4 has 9 edges and a monotone circuit with 6 ANDs and 2 wide ORs (circuit of 668). 662 (AND + wide OR + 2 narrow
  OR >= |E| + 2 tau - 2) is false on the net (triangle with three pendant edges; circuit of 721). 656 (short threads
  under a passenger, a formula from four core sizes) is false: g = (y0 AND y1) OR y2, and x2 OR the 4-cycle has 4 gates.
  Lesson recorded by both refutations: a count that charges OR gates by how many single-vertex inputs they accept
  breaks; narrow ORs must be paid in full.
- **Eliminated by the strategy seat.** At 13:54Z, by script and on paper with an adversary read: "a gate marked with a
  line serves few points of that line" for AND/OR circuits at line-degree three (the degree-2 mechanism of 649 does not
  lift as it stands). In the status of 16:13Z, by three independent script runs, not checked: AND/OR circuits with at
  most 8 gates for the prism and the 5-wheel (hence 741-744). The status of 16:32Z eliminated nothing new.
- **Retired with a mathematical reason.** 057 (the constant 3/2 is exactly the tie between the synthesis bound and the
  count; restated at 5/4 as 058); 045 (REFUTED FORM, checked: private witnesses fail at locality 2); the search targets
  266, 268, 317-321, 323, 324, 326, 327, 329 (monotone formulas with at most 17 or 18 leaves on 9-vertex graphs;
  exhaustive computations found none; kept as the negative rows 437 and 439); 557 (pendant law false without
  "g false somewhere"; replaced by 560); 581 (decided by 106 + 546/547); 585 (replaced by its negation, 597). The other
  retirements are refilings (plain sentences that cited sheets or other rows, faithfulness NO, duplicate rows), not
  mathematics.
- **Parked.** The hard link 060 (see 1.1). From A-010 (00:52Z): every line without a written chain to P versus NP was
  parked or moved; the derandomization route was declared dead and folded. From A-019: the exact count is false in
  the presence of a 4-cycle (112), so the LGP line was confined to graphs without one.
- **General monotone circuits do not split into "OR >= |E| - 1 and AND >= tau".** Petersen has a monotone 20-gate
  circuit with 13 OR gates (584) although |E| - 1 = 14; 587 has 14 ORs and 6 ANDs. Any proof of 608 must count jointly
  (see 5.1 for the class where the split does hold).

---

## 4. Where the line is heading: what the latest checked rows make possible next

1. **NOT ladder, fixed number of NOT gates: essentially closed.** 745 is checked and its two hypotheses (270, 669) are
   checked rows, so the unconditional 766 needs only its closing file (this is the strategy seat's stated next item).
   For a projective plane of order q (m = N = q^2 + q + 1, d = q + 1, kappa(b) = bq + 1 by 686):
   G(1, 0, N) = max over j of min(q (N - 1 - jq), N min(j, q)), about N q / 2 at j ~ q/2; at q = 8, j = 4 gives
   min(320, 292) = 292, which is 711. Iterating, G(s, 0, N) is of order N q / 2^s = N^{3/2} / 2^s: a superlinear lower
   bound for the joint line-ORs at every fixed number s of NOT gates, and nontrivial for s up to about (1/2) log2 N.
   (My evaluation of the recursion, not a fleet row.) For NOT gates that all read monotone wires (no NOT below a
   NOT), 885 decays only like 1/T: with k ~ q/(2T) its bound is about N q/(2T) = N^{3/2}/(2T), superlinear for T up to
   o(N^{1/2}). Next on that ladder are the guarded sums 780, 781, 787 (the output form A OR (B AND NOT H) after one
   NOT, with weight-one guards), i.e. the step from "fixed s" towards s growing; with ceil(log2(n + 1)) NOT gates every
   function is computable with polynomial overhead (Markov, Fischer), so the ladder must degrade before that point.
2. **Line-degree ladder towards 606/608.** 629 + 645 + 649 give degree 2 with constant 48; the degree-3 step was
   eliminated in its first form and is being redone through 782/792 (outputs that accept only part of their set). The
   destination is 606/608 on projective-plane incidence graphs: an Omega(N^{3/2}) lower bound for monotone circuits
   computing an explicit quadratic function, which is the reason the fleet calls 606 the "direction whose target grows
   with the degree". At degree 1 the line is closed by 5.1 below.
3. **LGP**: 687 by composition; the in-work 658 and 579 extend the exact count with NOT gates to subcubic graphs with
   good leaves or runs of four.
4. **AND count of the partial function (632)**: the census 793-898 and the structural rows 775, 777, 778, 783, 901,
   725-734 suggest the plan: induction by deleting closed neighbourhoods (705), additivity over tight parts (777), and a
   base case "one AND iff complete bipartite" (778).
5. **Small exact values** (740 checked; 741-744, 746-774) feed the search for the right count on graphs with triangles
   and 4-cycles, where |E| + tau - 1 is false.

---

## 5. Where our mathematics attacks it

### 5.1 L-meta-647 is true: a complete proof on paper (moves 647, 720, 655, 738, 739)

Our `L_meta_647_PARTIAL_PROOF.md` proved items 0-5 (normal form, no mixed OR, centres, reads identity) and left an
"excess inequality" open. The fleet's checked rows supply the missing count. The argument below is mine (Claude Opus
5.5 at effort max), on paper, not yet read by a second reader and not formalized.

*Setting.* G bipartite with sides X (marked, the "lines") and Y, no 4-cycle, no isolated vertex; C a monotone fan-in-two
circuit computing f_G in which no AND gate reads two X-dependent wires. This class is exactly line-degree <= 1 over X:
X-dependent wires have degree 1, the others 0.

*Step 1 (ours, items 0-4 of the partial proof).* After normalization, every X-dependent wire w computes
F_w = OR_{v in X} (z_v AND alpha_{w,v}(y)) with alpha monotone in y (no mixed OR, so no y-only summand: such a summand
would make the output true at z = 0, y = 1). Gates are of three kinds: P gates on y only (P_AND + P_OR of them), M
*merges* (OR of two X-dependent wires) and K *multiplying ANDs* (an X-dependent wire AND a y-wire m_g). alpha_{w,v} is the
OR over directed paths from z_v to w of the AND of the multipliers met; at the output alpha_{o,v} = OR_{u in N(v)} y_u.
For a multiplying AND g let Src(g) be the sources with an AND-free path to its dependent operand. Two sources v, v' of
Src(g) give the same multipliers along a path through g, so every such product lies below
(OR_{N(v)} y) AND (OR_{N(v')} y), whose single-variable support is N(v) meet N(v'), of size <= 1 (no 4-cycle). Hence a
centre c(g) is well defined (the source if |Src(g)| = 1, else the common neighbour), and for every edge vu the first AND
on a path from z_v carrying u has v or u as centre. **The centres of first ANDs form a vertex cover, so K >= tau.**

*Step 2 (transposition; this is the fleet's open 738, proved by our reads identity).* Run the dependent part backwards:
beta_o = 1, beta_a = OR over readers r of a of (beta_r if r is a merge, beta_r AND m_r if r is a multiplying AND).
Distributivity gives beta_{z_v} = alpha_{o,v} = OR_{u in N(v)} y_u. Built on the P y-gates, this circuit T has the K
ANDs (one fewer if the output is an AND) and, for the fan-out, sum over dependent wires a != o of (reads(a) - 1) =
(2M + K) - (|X| + M + K - 1) = M - |X| + 1 ORs. So #OR(T) <= P_OR + M - |X| + 1 and size(T) + |X| <= |C| + 1, which is
738's inequality.

*Step 3 (an OR-only form of the checked L-meta-529).* The Lean proof of 529 (`Outside/L_meta_529.lean`, `main_inv`)
maintains for each output set S a labelling l of S with |S| <= |l(S)| + |D(S)|, D(S) the gates false at the input "all
ones off S" and true at two singletons. By `gate_cases`, a new AND gate false there is dominated by one operand false
there, so it never merges two label classes; only OR gates do. The same induction therefore gives
|S| <= |l(S)| + |D(S) meet OR-gates|, and with the disjointness of the D(S) (already proved there from
|S meet S'| <= 1): **the number of OR gates of a monotone circuit computing Boolean sums with pairwise intersections
<= 1 is at least sum (|S_w| - 1).** Apply it to T, whose outputs are the sums N(v), v in X, pairwise meeting in at most
one vertex: #OR(T) >= |E| - |X|.

*Step 4.* #OR(C) = P_OR + M >= #OR(T) + |X| - 1 >= |E| - 1, and #AND(C) = P_AND + K >= tau. Hence
**|C| >= |E| + tau - 1, which is L-meta-647** (for every k <= tau). The star circuit of a minimum cover (154) shows it
is exact.

*Consequences.*
- **720** (subdivided K4, one-sided, at least 15 gates) follows: the graph is bipartite (corners against subdivision
  vertices), of girth 6, |E| = 12, tau = 4. **655** (our desk step: a one-sided circuit with at most 14 gates) has no
  witness, for either orientation; our exact SAT run that found side B UNSAT at 11 gates is consistent.
- **739** (a promise version: right only on inputs with one line and at most k points) gets N min(k, q - 1) + N - 1. For
  circuits right on all inputs, the line-degree-1 size of a rectangle-free incidence without isolated vertices is
  exactly |I| + tau - 1; for a projective plane of order q, tau = N (regular bipartite, König), so the exact
  line-degree-1 size is N(q + 2) - 1, against N(q + 1) - 1 from 739 at large k (739 writes q for the line size, which
  is q + 1 here). Under 739's promise the y-only summand is not excluded (the input with no line is not constrained),
  so the tau term there would need the OR-only form of 270 and a separate argument for Step 1; I have not done that.
- **Searches 650, 582, 583/723, 256**: any circuit beating |E| + tau - 1 on a bipartite graph without a 4-cycle (the
  plane of order 3 at 63, Heawood at 26, the subdivided K4 at 14) must AND two line-dependent wires AND two
  point-dependent wires somewhere, i.e. have line-degree >= 2 over each side. This prunes the SAT encodings.
- **What does not extend.** In this class the count splits as OR >= |E| - 1 and AND >= tau. For general monotone
  circuits that split is false (Petersen, 584: 13 ORs < 14), so 608 needs a joint charge; the natural next statement is
  649 with constant 1 instead of 48 (line-degree 2), where products of two line-dependent wires create degree-1
  "diagonal" terms y_w AND y_w = y_w and the honest-factor lemma 645 has to replace Step 1's centres.

Proposed filings (for the user's decision; nothing was sent): the OR-only form of 529 as a lemma; 738 with the proof
above; 647 assembled from them.

### 5.2 The NOT ladder needs finite geometry, and we can supply it (660, 661, 714, 715, heavy inputs)

How 715 works, read from its statement: if C has one NOT gate, its input h is monotone; let W be the least weight such
that h is 1 on every W-set. Some (W-1)-set a has h(a) = 0, and below a the circuit is monotone, so 529 (after 669) gives
size >= F(a) = sum_w (|S_w meet a| - 1)^+; every W-set b has h(b) = 1, and above b the circuit is monotone and
computes the ORs of the lines missing b, so size >= q * (number of lines missing b). The lower bound is
min over W of max(T1(W), T2(W)), with T1(W) = min over (W-1)-sets a of F(a) (adversary's choice) and
T2(W) = q * ext_q(W), ext_q(W) the largest number of lines of PG(2, q) missed by a W-set (the prover's choice).

- T1 is explicit: F(a) >= |a| - 1 with equality for collinear a, and F(a) = |a|(q + 1) - #(lines meeting a)
  >= (W - 1)(q + 1) - N with equality once a contains a line. So T1(W) = W - 2 for W <= q + 2 and
  (W - 1)(q + 1) - N beyond.
- T2 needs constructions only. Counting incidences and pairs, #(lines meeting b) >= W (q + 1)^2 / (q + W), with
  equality exactly for sets of type (0, d), the maximal arcs; so ext_q(W) <= N - W (q + 1)^2 / (q + W).
- **q = 8 (660, at least 98).** Take b with X^2 + bX + 1 irreducible over F_8 (683), A an additive subgroup of order 4,
  D = {(x, y) : x^2 + bxy + y^2 in A}. By 664 every affine line meets D in 0 or 4 points, and D misses the line at
  infinity: D is a maximal arc of degree 4 with 1 + 9 * 3 = 28 points, 28 * 9 / 4 = 63 secants and 10 external lines.
  Remove the 9 points on three secants spanned pairwise by three points of D not on a common secant: the remaining
  19-set misses 13 lines. Hence T2(W) >= 8 * 13 = 104 for all W <= 19, while T1(20) = 19 * 9 - 73 = 98 and T1 grows.
  **The min-max is >= 98, exactly the bound of 660.** So 660 = 715 + 529 + 669 + this construction.
- **q = 7 (661, at least 70).** Maximal arcs do not exist for odd q (Ball, Blokhuis and Mazzocca 1997), so the
  construction must change. Take a conic in PG(2, 7): 21 internal points, and tangent lines carry no internal point.
  Through an internal point P choose two secants; they carry 3 + 3 - 1 = 5 internal points. The other 16 internal points
  miss the 8 tangents and the 2 chosen secants, so T2(W) >= 7 * 10 = 70 for W <= 16, while T1(17) = 16 * 8 - 57 = 71.
  **The min-max is >= 70, exactly 661.**
- **Asymptotics of this route.** With Denniston arcs of degree d ~ sqrt(q) (q = 4^k) one gets T1 ~ (d - 1) q^2 and
  T2 ~ q^3 / d, so the one-NOT bound by 715 is of order q^{5/2} = N^{5/4}, and the variance bound shows this route
  cannot do better. The window recursion 745 does better (about N^{3/2}/2, see 4.1), because it uses the promise
  bound 270 on light inputs instead of whole W-sets. 714/715 are therefore a weaker parallel route; their value is that
  660/661 are unconditional statements once 714/715 are checked.
- **Heavy inputs (the strategy seat's next item).** A monotone circuit that must be right only on inputs of weight
  >= W sees each line w as constant 1 as soon as the input meets it; the lines it must still compute on a heavy input b
  are the lines missing b. The extremal quantity is again ext_q(W) and its dual, the minimum number of points meeting
  every line except t given ones (blocking-set problems: Bruen's bound q + sqrt(q) + 1 for nontrivial blocking sets,
  Jamison and Brouwer-Schrijver for affine blocking sets, Blokhuis's 3(p + 1)/2 for prime p, by Rédei polynomials).
  For odd q, where the even-characteristic arcs are unavailable, determining ext_q(W) (or its order of magnitude for
  W ~ c q) is a polynomial-method problem in our competence. Conics already give q(q - 1)/2 external lines at
  W = q + 1, within O(q) of the variance bound. 685 is the fleet's own step in odd characteristic: with A an F_p-subspace,
  {(x, y) : x^p - y in A} meets every line in 0, |A| or p|A| points (a line y = mx + k misses it exactly when k lies
  outside the image of the F_p-linear map x -> x^p - mx, plus A), a set of type (0, |A|, p|A|).

### 5.3 The AND count of the partial function (632, 631, 633, 217): what our centre argument gives, and where it stops

Step 1 of 5.1 is an AND-count statement (K >= tau) for line-degree-1 circuits, proved by first ANDs and their centres.
In the AND-count model of 632 (OR free, partial function on maximal independent sets I and I + u) our partial file
proved that depth-one output gates are stars. The obstacle for nested gates is masking: in a general circuit an AND
gate can be true at a non-edge input and be cut down later, so the edges born at one gate need not form a star. In the
line-degree-1 class masking happens only through the multipliers, and the bound alpha_{o,v} <= OR_{N(v)} y is what
makes the centre unique; 632 needs a substitute for that bound (the fleet's route instead: 705 deletion of closed
neighbourhoods, 777 additivity, 778 base case, 901 the biclique upper bound). Not settled by us.

### 5.4 606/608 in general: what transfers

- Formulas: Jukna's rank argument (Boolean Function Complexity, Thm 7.2; "On Graph Complexity", ECCC TR04-005,
  Thm 7.3, with constant 1/2) gives L+(f_G) >= |E| for girth >= 5; the fleet's 531 is stronger (|E| + tau leaves, no
  triangle and no 4-cycle). Correction to our `L_meta_647_PARTIAL_PROOF.md`: the local copy
  `desk/lit/jukna_single_level_eccc2004_005.pdf` is "On Graph Complexity", not "Disproving the single level
  conjecture" (that is ECCC TR05-021); the Codex note has the attribution right.
- Circuits: the Codex note `desk/CODEX_TO_CLAUDE_L_META_606.md` (Codex, reasoning effort ultra) proves
  |E| <= |A| R <= |A| (s + 1 - k), A the set of value vectors of the k shared gates on edge inputs, so 606 holds with
  constant 2^{k0} on circuits with at most k0 shared gates. The two partial results are complementary: Codex bounds
  the sharing and lets the line-degree be anything; 649 bounds the line-degree (2) and lets the sharing be anything.
  Unbounded sharing at unbounded line-degree is the open case.
- 5.1 settles line-degree 1 exactly; 649 settles degree 2 up to the constant 48.

### 5.5 Our GCT-side results, checked for transfer

I went through the results listed in MAPPING_BY_READING (Lemma K, riffle rank, the level-space core, the GCT_KRON
Hessian, the obstruction families) and MAPPING_AGENT_RESULTS (1.1-1.6, 2, 3) for a mechanism that acts on the meta
items, not by title.
- Level spaces, Lemma K, the Hessian of the permanent: statements about polynomial identities over C restricted to
  linear spaces. The meta items are monotone Boolean circuits, where the operative phenomena are idempotence
  (y AND y = y) and absorption (x OR xy = x). The algebraic analogue is easy: a monotone arithmetic circuit for
  sum over incident (p, w) of x_p y_w can be homogenized; each product of a point form and a line form has a
  rectangle of monomials as support, which must be a star when no 2 x 2 rectangle exists; a sum of two or more
  variables cannot serve two stars (their centres would share two neighbours); so there are at least tau products and
  |I| - 1 additions, |I| + tau - 1 in all. The Boolean semiring has no homogenization, which is why the fleet climbs a
  line-degree ladder; 5.1 is this argument carried over to Boolean circuits at line-degree 1, with transposition doing
  the work of homogenization. Our polynomial-identity results act on none of this. No transfer.
- GINEQ F-13 (image substitution: length >= q + min atom length - 1) has the shape of |E| + tau - 1, and riffle rank
  is a decomposition count; but F-13 rests on dimension counting in a vector space of atoms, which has no counterpart
  for OR gates. The analogy is real only at the level of 5.1, where the count splits into an "OR part" (|E| - 1, a
  Nechiporuk count) and an "AND part" (tau, a covering count). No proof transfers.
- Finite fields and finite geometry (5.2) are where our algebraic-geometry competence does act: maximal arcs, ovals,
  additive polynomials, character sums for point counts on {Q in A}, and the polynomial method for blocking sets.

---

## 6. Short index of the ids that matter most now

Checked and central: 016, 030 (plan chain); 154, 204, 444, 481, 665 (LGP); 529, 270, 663, 696, 697, 629, 645, 649
(incidence and line-degree); 669, 745 (NOT ladder); 613, 616, 740 (monotone counts); 664, 683, 686 (geometry).
Open and moved by us: **647** (proof in 5.1), **720** (corollary), **655** (no witness), **738** (proof in 5.1, Step 2),
**739** (strengthened), **660**, **661** (reduced to 714/715 by explicit constructions, 5.2).
Open and live without our input yet: 606, 608 (general), 632/631/633, 687 (composition), 766 (closing file), 782,
885 and its instances 890/894/899/900, 714/715, 651, 650, 582, 583/723.
