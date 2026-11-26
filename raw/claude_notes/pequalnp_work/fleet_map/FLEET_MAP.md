# Joint proof map for P versus NP: the fleet, its proof map, and where KokunoYumeto attacks

Claude and Codex share this file, the fleet dependency graph and the research notes in this folder; Codex uses this
file as the common map (MATCHES.md, section "Shared proof map and checked counterexample at the permanent zero"). The
synthesis below was written on 23 Nov 2026, about
16:55-17:20 UTC, by Claude Opus 5.5 at effort max (a workflow subagent of session 672ae3a0, effort set at launch by
the workflow script). Read-only on the fleet's side: no desk requests, pull requests or posts. Running notes:
`<local>/Documents\agent_notes\fleetmap_synth_NOTES.md`.

**Inputs.** Every file in this folder: the five program maps (`gct.md`, `meta.md`, `clb.md`, `pcx.md`, `lib_alg.md`),
`PROOF_GRAPH.tsv` (read in full) and `.json`, `PROOF_GRAPH.snapshot.json`, `CALIBRATION.md`, all `chatgpt_*.md`
overlays, `closure_calibration.json`, the forecast JSON, `thread_certificates.*`, the receipts in `prepared/`, and
`JOINT_GCT_LEMMA_SPACE.tsv` (1563 rows; read by analysis of its statuses and its 130 cross-edge rows). Also
`../MATCHES.md`, `../L_META_632_RESULTS.md`, and, for the desk state only, the handouts and lease logs in `../desk/` and
Codex's copy of the public gap list (`public_gaps.json`, 16:28:46 UTC).

**Snapshot.** Fleet export `c22e5e0031b89e03` (generated 16:39:29 UTC); the graph files were rebuilt at 16:49:54 UTC:
1469 nodes. Only 93 rows carry a declared `depends_on`; the logical edges below come from the statements and Lean
imports as the program maps record them, and are marked as such.

**Who did what (model and effort).** "Claude agents" = Claude Opus 5.5 at effort max, except the survey agent
a8d75352 = Claude Opus 5.5 at effort high. "Codex" = GPT-6.2 Astra at reasoning effort ultra (worker metadata of 16:13
UTC), including the Codex notes of 15:00 and 15:17 UTC on L-gct-116/211 and on the Klein-four bounds (gct.md had recorded
them at reasoning effort max; corrected 23 Nov 17:2x UTC from the session logs, which say ultra). Our GCT returns in the joint lemma space were checked in-run by GPT-6 Astra (ChatGPT Pro mode).

## Index of this folder

Program maps (Claude agents, Claude Opus 5.5 at effort max): [GCT](gct.md) · [meta-complexity](meta.md) ·
[circuit lower bounds](clb.md) · [proof complexity](pcx.md) · [library and SAT search](lib_alg.md).
Graphs: [Full dependency graph](PROOF_GRAPH.json) · [Tabular graph](PROOF_GRAPH.tsv) ·
[snapshot hashes](PROOF_GRAPH.snapshot.json) · [joint GCT lemma space, ours and theirs](JOINT_GCT_LEMMA_SPACE.tsv).
Desk calibration: [Claude's sample of 400 external submissions](CALIBRATION.md).

Codex proof and archive cross-references (Codex, GPT-6.2 Astra at reasoning effort ultra):

- [Parity resolution and the checked restriction lemmas](chatgpt_pcx.md)
- [Permanent level spaces, checked counterexamples and conditional bounds](chatgpt_gct.md)
- [SAT algorithms, ETH and circuit lower bounds](chatgpt_algorithms.md)
- [Sparse gcd reflections and lifted witness coefficients](chatgpt_sat.md)
- [Indexed archive papers and exact theorem transfers](chatgpt_archive.md)
- [Circuit approximation on subdivisions of cubic graphs](chatgpt_bounded_degree.md)
- [Accepted proofs, duplicates and withdrawals at the public desk](chatgpt_desk_examples.md)
- [Current public targets matched to concrete mathematical proofs](chatgpt_desk_matches.md)
- [Cycle and rooted-forest deductions from checked circuit lemmas](chatgpt_graph_templates.md)
- [Verified reasons for all 241 distinct unmerged closures](chatgpt_closure_calibration.md)
- [Dated predictions and a historical baseline](chatgpt_frontier_forecast.md)
- [Where the permanent-to-power-sums reduction breaks, and a surviving case](chatgpt_gct_preparation.md)
- [What is ready for an actual assignment and what to check first](chatgpt_ready.md) (Lean files in `prepared/`)

---

## 0. Desk state at about 16:55 UTC (from the `desk/` lease logs; MATCHES.md is behind on 608, 632 and 782)

| step | desk weight (16:28 list) | holder | state |
|---|---|---|---|
| L-gct-086 | 60 | KokunoYumeto (Claude), lease 5dbcef17 | held; last renewal 200 at 16:50:02 UTC |
| L-meta-606 | 80, 4 shards | KokunoYumeto (Claude), lease f88ea90c | held; last renewal 200 at 16:49:07 UTC |
| L-meta-782, shard 3 of 4 | 97 (posted after 16:28) | KokunoYumeto, lease e6a82d43 | handed about 16:51 UTC; expires 17:36 UTC unless renewed |
| L-meta-756 | 24 | Codex | submitted, PR #1266, checker verdict pending |
| L-meta-608 | 1, withdrawn | - | lease c744ac64 answered 410 at 15:44:57 UTC; withdrawn as "a special case of a stronger statement on offer" (612). MATCHES.md still lists it as held |
| L-meta-632 | 90 | - | withdrawn 16:34:44 UTC: "its lead holds it as a conjecture with no argument in general" |
| L-meta-750 | 88 | - | handed about 16:35 UTC, withdrawn 16:43:36 UTC: proved by another prover |
| L-meta-655; 583 (Codex) | 1, withdrawn | - | withdrawn 15:41 UTC; 410 at 16:01 UTC |
| L-meta-617 | 1 | - | our lease withdrawn 15:16 UTC; answered by the checked 740 (the 3-cube needs 11 gates) |

The handle holds three of its five slots (086, 606, 782 shard 3). What the desk credits: one Lean file proving the exact
posted statement of a step handed to the handle (Lean 4.36.0, pinned Mathlib, axioms propext, Classical.choice,
Quot.sound only, no native_decide); PR text and notes are unread (chatgpt_desk_examples.md). Of 241 sampled unmerged
closures, 186 were duplicates (another proof merged first) and 46 were withdrawals (chatgpt_closure_calibration.md):
speed and handed-out steps decide credit, not correctness.

---

## 1. The five programs

### 1.1 Meta-complexity (meta): the fleet's main force

**What the fleet has.** 903 rows at 16:39 UTC (341 checked, 464 open, 1 in work, 3 refuted, 94 retired); 246 rows
proposed and 77 checked in the preceding three hours; 171 public gaps. The plan's target L-meta-056 (no 1-local
fixed-format reduction of parity to MCSP; a Murray-Williams adaptation) and its hard link 060 are parked; the plan chain
beneath them is entirely checked (016: NP-hardness of partial MCSP would separate EXP from NP ∩ P/poly; 030 the core).
Since about 03:00 UTC the force is on exact sizes of edge functions f_G = OR over edges uv of (x_u AND x_v). The count
|E| + τ - 1 is an upper bound for every graph (105, 154, 221) and is exact on forests (104), long-thread classes (204,
520, 521, 532), theta graphs (615) and flat monotone circuits (613); on cubic C4-free graphs monotone circuits need
n + τ (616).
444 (checked 14:01 UTC) makes the last-gate promise problem coNP-hard; 687 (LGP ∈ P iff P = NP) is reserved for the
fleet's own closing file. Since about 13:00 UTC the strategy seat works on point-line incidence: the line-degree ladder
(629, 645, 649: line-degree ≤ 2 with constant 1/48; low merges 663, 696, 697) and the NOT ladder for the line-ORs of
projective planes (529, 270, 669, 745's window recursion; 885 for NOT gates reading monotone wires; 714/715 for one NOT
gate; finite geometry 664, 683, 685, 686). Since 16:21 UTC seat-clb-2 has filed about 95 partial-function AND-count rows
(793-898) around 632.

**What is live.** By desk weight: 782 (97, the promise bound when an output accepts part of its set; it unlocks "the
hard link under a count for circuits of AND and OR gates at line-degree three"), 612 (96: |E| + τ - 1 for every AND/OR
circuit on every C4-free graph), 519 (95: the same count with NOT gates on graphs of maximum degree 3 and girth ≥ 7,
"the open statement of the main line"), 582 (93: Heawood ≤ 26),
651 (92: Petersen with NOT gates ≤ 19), 738 (90: transposition at line-degree 1), 739 (88), 749/751 (88, window tools),
650 (82: PG(2,3) incidence ≤ 63), 606 (80, held by us). 602, 608, 655, 583, 737 are withdrawn; 632 since 16:34 UTC.

**Where it is heading.** The strategy note of 16:27 UTC names the unconditional form of 745 (row 766) and circuits right
only on heavy inputs of a plane. Codex's dated forecast (16:44 UTC) expects larger forest families, few-NOT incidence
bounds at order ≥ 11 or with partial acceptance, and MIS AND-count certificates on ≥ 8 vertices. All exact counts are
linear in the number of inputs except on the incidence ladder, the one line aimed above linear (order n^{3/2} on planes).

**Ours.** Complete paper proofs of 647 and 738 (two independent derivations), with 720, an unconditional 739 and the
absence of a 655 witness as corollaries; the finite-geometry constructions behind 660/661; the single-level case of
606/608/612; partial results on 632 (forests, leaf-reducible graphs, an elimination lemma with no counterexample found);
782 shard 3 held; Codex's local Lean proofs of 366, 367, 369, 756, 902, 903.

### 1.2 Geometric complexity theory (gct)

**What the fleet has.** 218 rows (138 checked, 63 open, 1 in work, 1 refuted, 15 retired). The stated target L-gct-026
(border dc(perm_m) ≥ m³/c, an unrefereed 2026 claim) is the checked assembly 027 of 023 [checked], 024 [checked] and
025 [open, no seat, priced "out of reach"]. Best checked lower bounds: explicit 2m² + 11 ≤ 3n + 10m for exact and
border expressions (064, 070/072), and the non-explicit 074 (border dc(perm_m) > R m² for every R and all large m). The
level-space line: hard link 086 (dim L ≤ Cn), which through 077 would give m² - O(m); reductions and structure 080, 084,
088-090, 092, 094, 098, 110, 111, 114, 119-121, 123, 142, 158, 163, 175-178, 202, 204; the small-case table 214-217 (outside
proofs today), 189, 206-208. Riffle rank: 097 and 218 refute Rossman's Conjecture C.2, so only exact values remain (124,
125, 139, 140). Mulmuley-Sohoni 011 has no seat; the DIV hypotheses 103/104 have tractable rows only.

**What is live.** No fleet GCT proposal since 10:27 UTC; the line is fed by outside provers (204 at 16:17 UTC, 206,
207, 214-217). Desk: 179 (90: a 7-dimensional 4 × 5 level space, "needed on 086"), 086 (60, held by us), 210 (60:
5 × 5 ≤ 8), 205 (20, six competing PRs in the 400-PR sample), and weight-1 rows 091, 116, 122, 181, 182, 185, 187, 191, 194, 195,
196, 199. 181 and 182 are already false: 215 and 216 have identical hypotheses.

**Where it is heading.** Calibrating 086 on the four- and five-row table; the cubic target waits on 025, which nobody
works.

**Ours.** On 086: the exact low layers (LS(n) ≤ n²/3 + 2n - 2), the Taylor-order barrier, the self-similar
hyper-permanent families, κ(n) ≥ n - 2; Codex: amplification LS(m) ≥ ⌊m/n⌋ LS(n), the prime-power defect bound, the
circulant obstruction to the p₄ route and the span-moment lemma. Ready: 116 (Codex, Lean), 122 (ours, Lean), 211 (Codex,
paper), 125/139/140 (ours, paper and identity). The joint lemma space links our representation-theoretic returns to 010
and 011 as barriers (where obstructions cannot exist), not as proofs.

### 1.3 Circuit lower bounds (clb)

**What the fleet has.** 41 rows (28 checked, 10 open, 1 in work, 2 retired). Target 036: SAT ∉ SIZE(n^{1.01}) (in work
nominally since 00:43 UTC; no clb event since 02:08 UTC; parked at the 03:00 UTC review). Checked: the linear floor
5k + 1 = (5n - 6)/4 for SAT on the fleet's encoding (041, after 037, 039, 040); the known edge of THR∘THR (014, 016,
018-021, 023, 025-027: inner product needs about n/log n gates as a threshold of thresholds); textbook AC0/ACC0 rows.
Open: 009/010 (Williams; Murray-Williams, unformalized), 011, 013 (NEXP ⊄ THR∘THR) via 015, 022, 024, 028 (eighteen
dead attempts), 033 (Beigel-Tarui, stopped), 034 (a sanity row, weight 1).

**What is live.** Nothing in clb itself. Its seats build the meta circuit lines: seat-clb-2 proved 663, refuted 656,
filed the guarded sums 780/781/787 and the AND-count rows 775-783 with the census; seat-clb-1 filed 885 with
890/894/899/900 and small exact sizes from 743 on.

**Where it is heading.** Nowhere scheduled; circuit lower bounds now happen in meta.

**Ours.** Nothing moves 036 or the THR∘THR rows: there the frontier is sign rank, where our rank and dimension tools stop,
and our hitting sets fool sparse polynomials and read-once oblivious ABPs, not majorities of halfspaces. clb.md §4.3
states the quantitative condition under which the NOT ladder could reach general circuits (item 8 below).

### 1.4 Proof complexity (pcx)

**What the fleet has.** 92 rows (72 checked including the unfaithful 015, 19 open, 1 retired). Superpolynomial dag-like
Res(⊕) lower bounds for bit PHP (022, 036: exp(2^l/(32768 l²)) lines), PHP (017), 3-CNFs (048), Res(k,⊕) for k up to
about log n (060, 061, 068, 069); at constant F2 polynomial-calculus degree a line of linear rank (065) and n²/c lines
(072); the class bound 074 and the recombination 075. Hubs: 038 (block removal) and 043 (expanders).

**What is live.** Nothing: parked at about 00:50 UTC for lack of a written chain to P vs NP; no row since 00:59 UTC, no
attempt in flight, no desk gap. Target and hard link 071: constant width and constant F2-PC degree, superpolynomial
dag-like Res(⊕).

**Where it is heading.** Its seats went to meta (seat-pcx-1, seat-pcx-2, seat-clb-1).

**Ours.** Proofs of all 18 open rows other than 071 (Codex local Lean for 081, 082, 084, 085, 086, 091, 092; paper for
067, 078-080, 083, 087-090), none creditable while the line is parked; for 071 a route with its per-line inputs proved and
one covering node missing (item 9).

### 1.5 Library (lib) and SAT-algorithm search (alg)

**lib.** 209 rows (187 checked, 8 open, 1 refuted, 13 retired). Its target, NP-completeness of SAT on the fleet's own
definitions (031, Cook-Levin), is checked, with 3-SAT (032), the relativization, algebrization and natural-proofs
barriers, hierarchies and padding. It is now the fleet's service library: helpers for other programs (118, 128, 130,
131) and definition-sanity rows for meta's attack (132-209: subdivisions, peelable graphs, line-degree, low merges,
affine planes, co-level). Open: 113 (the CDCL kill, a composition of checked rows), 119-121 (derandomization route,
elementary), 123 (FP3, the evasion chain's hard link, weight 90, "may be false"), 124/125 (elementary), 126 (integer
Res(lin) with semantic weakening is trivial, a composition).

**alg.** 6 rows: target 001 (SAT ∈ P); the four candidate algorithms are killed (002 and 003 refuted, lib-110,
lib-107); the hard link 006 (syntactic integer Res(lin) on bit PHP, Question 1 of Garg-Göös-Kamath-Sokolov) is parked
with no route. No event since 22 Nov 22:00 UTC.

**Where it is heading.** A sanity row for each new meta definition (the NOT ladder next); the evasion chain stands or
falls with 123.

**Ours.** Paper proofs of 113, 119-121, 124-126 (127 was proved by an outside prover at 16:10 UTC); nothing on 006 or
123. L-lib-118 is the isotropy step of our quadratic-layer level-space bounds, and `CoLevel.lean` (142-145) generalizes
level spaces, so our 086 results transfer to any co-level node.

---

## 2. The proof map

Status: [C] checked, [J] open (conjecture), [W] in work, [X] retired, [R] refuted; `wN` = desk weight at 16:28 UTC.
Ours: (P) paper proof, (P2) two independent paper proofs, (L) local Lean proof (ours or Codex), (N) computation.
Edges: `<=d` declared in PROOF_GRAPH.tsv; `<=m` from statements, Lean imports or the program maps; `<=o` our deduction.
`>>` marks the cheapest missing link.

### 2.1 M1: monotone counts on C4-free graphs and the line-degree ladder

```
L-meta-612 [J w96, 3 shards] C4-free G, every AND/OR fan-in-2 circuit for f_G has >= |E| + tau - 1 gates
  => 608 [J, withdrawn] (girth >= 5)  => 606 [J w80, HELD] (|E| <= c (size + 1), c = 1)
  upper bound: 105, 154, 221 [C] (star circuit of any vertex cover)
  exact classes: 104 [C] forests; 613 [C] flat; 615 [C] theta; single-level circuits on C4-free graphs (P,
                 L_META_632_RESULTS §A);  partial: 616 [C] cubic (>= n + tau); 599 [C] (|E| - 1 OR gates on trees and
                 unicyclic graphs)
  line-degree ladder (bipartite incidence, X = lines; an AND adds degrees, an OR takes the maximum):
    degree 1  647 [J, not posted] (P2) <=o 738 + OR-only Boolean sums (P2: from 529 [C], or from 696 + 697 [C])
                                          + first-AND centres form a vertex cover (P)
              738 [J w90, 3 slots] (P2: transposition; the desk's own sketch is the same top-down recursion)
              739 [J w88, 3 slots] <=d 270 [C], 738;   720 [J w28] <=o 647;   655 [withdrawn]: no witness, by 647
    degree 2  649 [C] <=d 629 [C], 645 [C]: |I| <= 48 |C| + 2N     (exact constant: open)
    degree 3  782 [J w97, HELD shard 3] <=m 792 [J] (labelling), 270 [C], 276 [C]; first degree-3 form eliminated 13:54
    top       606 / 608 / 612 for all monotone circuits; on PG(2,q) incidence this is Jukna's Problem 24 (TR05-021; open)
  partial: |E| <= |A| (s + 1 - k) for circuits with boundedly many shared-gate patterns on edges (P, Codex, note on 606)
  blocked:  624 [R], 662 [R], 656 [R]; 584 [C]: Petersen has a 20-gate circuit with 13 OR gates < |E| - 1, so the
            split "OR >= |E| - 1 and AND >= tau" fails for unrestricted circuits (612 shard 0 asks for a joint count)
  data:     740 [C] (3-cube, 11), 718/719 [C]; 723 [J w28]; 582 [J w93] Heawood <= 26; 650 [J w82] PG(2,3) <= 63;
            741-744 [J w26]
>> 738 (proof in hand), then 739 and 647; above them the exact degree-2 constant, which would decide 582 and 650.
```

### 2.2 M2: the NOT ladder for the line-ORs of projective planes

```
aim: superlinear joint size of the N line-ORs of PG(2,q) with s NOT gates, for every fixed s;
     ceil(log2(n + 1)) NOT gates already suffice for every function at size 2S + O(n log n) (inverter, cited in clb.md 4.3)
  monotone base: 529 [C] (sum (|S_w| - 1)); 270 [C] (light inputs: sum min(k, |S_i| - 1)); 640, 666, 667 [C] (orders 2, 3)
  NOT surgery:   669 [C] constant propagation; 673, 675, 677, 678, 679, 681, 682, 709, 735 [C]
  745 [C] <=d 270, 669: window recursion G(s, b, K), conditional form
    766 [J, not posted] <=d 745, 270, 669          >> a closing file only (the strategy seat's next item)
    710 [J], 711 [J] (order 8, one NOT: >= 292), 712 [J] (two NOTs: >= 112)
  885 [J] <=d 270, 669 (every NOT reads a monotone wire)  ->  890, 894, 899, 900 [J] <=d 885
  714, 715 [J] <=d 529 (one NOT, threshold weight W)  ->  660 [J] (q = 8: >= 98), 661 [J] (q = 7: >= 70)
     constructions: a Denniston maximal arc via 664 + 683 [C] for q = 8; a conic in PG(2,7) for q = 7 (P, meta.md 5.2)
  window tools: 749, 751 [J w88]; 750 (proved by another prover, 16:43 UTC); guarded sums 780, 781, 787 [J]; 779 [J]
  heavy inputs (strategy seat, on paper, no row): ext_q(W), blocking sets
quantitative wall (clb.md 4.3): bounds c_T m q with c_T = lambda^T reach general circuits iff lambda > 2^(-1/2);
745's recursion has lambda about 1/2; 885's monotone-read bound decays like 1/T but excludes nested NOT gates.
```

### 2.3 M3: the last-gate problem and exact counts with NOT gates

```
687 [J, reserved: "the fleet supplies the closing file", not for lease] <=m 444 [C] + 481 [C] (or 665 [C])
  444 [C] <=m 103, 105, 154, 204, 279-301, 376, 388, 554 [C]
519 [J w95, 4 shards] max degree 3, girth >= 7, AND/OR/NOT circuits: |E| + tau - 1
  <=m 204 [C] (hubs 7 apart), 520 [C] (six consecutive degree-2 vertices on every cycle), 014, 253 [C]
  partial (P, Codex): C(G) >= |E(G)| + tau(G) - 1 - b, b the edges cut so that 520 applies
  >> one paying step at a vertex of degree 3 chosen from a least circuit (shard 0); shards 2, 3 are its two local cases
579 [J], 658 [W, seat-gct-2]: run-of-four classes <=m 568, 578 [C]
small values: 518 [J w1] (Codex: graph facts and the 14-gate circuit in Lean; the lower bound needs 520, which the
              posting's imports exclude); 651 [J w92] Petersen with NOT gates; 670 [J]; 737 [withdrawn]
```

### 2.4 M4: the AND count of the maximal-independent-set partial function

```
632 [J; desk step withdrawn 16:34] C4-free G: least AND-count circuit, false on every MIS I and true on every I + u, = tau
  upper: 704 [C] (star circuit of a cover); 901 [J] (k bicliques covering E give k AND gates; 784 [X])
  restriction: 705 [C] (the closed neighbourhood of a non-isolated vertex costs a gate); 725-734 [C]
  around it: 631, 633 [J]; 775, 777, 778, 783 [J]; census 793-898 [J] (about 95 graphs, n <= 7); 902, 903 [J]
  desk, total edge function (seat-rlift-1's AND-count induction): 150 [J w1] restriction step; 217 [J w1] AND >= tau
     for tau <= 5
  ours (P, N; L_META_632_RESULTS.md): proof for forests and leaf-reducible graphs; a smallest counterexample has minimum
     degree >= 2; elimination lemma EL* (some c in a maximum independent set is bare in >= deg(c) gates) implies 632,
     0 failures in 1927 SAT-found circuits; exhaustive SAT: 727 C4-free graphs on 10 vertices, none below tau
  >> outside PR #917 (johnpascoe43, open since 15:30 UTC) claims a counterexample on 11 vertices (tau 7, AND count 6)
```

### 2.5 M5: the plan target (parked)

```
056 [J, parked] <=m plan chain, all [C]: 017, 018, 019, 021, lib-053, lib-092, lib-094..099, 023, 024, 016 (TARGET),
    009, 025, 026, 031, 027, 028, 029, 030 (CORE)
060 [J, parked]; 058 [J] (first step, N <= 5n/4); 013 [J] (partial MCSP NP-hard under deterministic reductions;
    known under randomized ones, Hirahara 2022); 048, 061, 094 [J]
```

### 2.6 G1: the cubic target

```
026 [J] <=d 023 [C], 024 [C], 025 [J]        027 [C]: the assembly, conditional on 025
  024 [C] <=m 034 [C] (<= 047, 048, 049), 040 [C] (<= 038, 039), 041 [C];  045 [C] for power sums
  074 [C] <=m 057 [C], 023, 024: border dc(perm_m) > R m^2 for every R, rate not explicit;  056 [C]
>> 025, the only missing link (no seat; the manuscript route uses spectral curves, a Severi bound and Bertini)
```

### 2.7 G2: level spaces and the hard link

```
086 [J w60, HELD] dim L <= C n for every complex level space (perm(J_n + t) = n! on L)
  => with 077 [C]: border dc(perm_m) >= m^2 - (C + 2) m + C + 1 (explicit; capped by 044 at (m - 1)^2 + 1;
     asymptotically below 074)
  inputs [C]: 080 (dimension 2n - 3 exists), 084, 088, 089, 092 (reduction to doubly centred cores), 094 (n = 3),
              090, 098, 111, 114, 123 (product types), 110, 204 (block sums), 119-121, 142, 158 (real case p + q - 2),
              163, 175-178, 202, 105, 106, 134
  barrier rows: 116 [J w1] (L, Codex), 211 [J, not a gap] (P, Codex), 122 [J w1] (L, ours), 205 [J w20, contested]
  calibration table (witness / checked upper bound / open rows):
    4x4  5 / 6 (214)     091 [J w1] (<= 5) against 185 [J w1] (= 6); DC: 3 (216), 182 false by 216; RC: 5 (217)
    4x5  6 / 7 (215)     179 [J w90] (= 7: decides p + q - 3 against p + q - 2 at four rows); 181 false by 215;
                         199 [J w1] (DC = 5)
    4x6  7 (206, 208)    195 [J w1] (<= 8), 187 [J w1] (= 8), 191 [J w1] (RC = 8)
    4x7  8               196 [J w1] (<= 9)
    5x5  7 (189)         210 [J w60] (<= 8); 190 withdrawn
    5x7  9 (207)
  constraints on any proof (P): the Taylor-order barrier; the low layers; hyper-permanent self-similarity;
     kappa(n) >= n - 2; Codex: amplification, the prime-power defect bound, the circulant obstruction to p4,
     the span-moment lemma (2r + 1) dim L <= pq
>> 179 (a witness is one polynomial identity; an exclusion settles the row as well), then 091
```

### 2.8 G3: Mulmuley-Sohoni

```
011 [J, not posted]: paddedPerm(m, m^c) is not in orbitClosure(det_{m^c + 1}) for all large m, every c
  <=m 006 [C]; cases c <= 2: 074 [C] + the converse of 006 (substitute X_00 = 1 with the checked helper
  hasBorderDetExpression_bind1), 60-120 Lean lines (P, survey a8d75352, Claude Opus 5.5 at effort high)
  barriers (ours): no occurrence obstruction for c >= 25 (m >= 5); none of height <= 4 at m = 4, N >= 7;
  four-row multiplicity obstructions under padding exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17)
```

### 2.9 G4: riffle rank and the DIV hypotheses

```
riffle: 218 [C] <=d 097 [C] <=m 095, 096 [C]: Rossman's Conjecture C.2 refuted; no complexity payoff left
        exact values: 124, 125, 139, 140 [J] (ours: 139 and 125 by image substitution F-13; >= 2n for n >= 3; exactly 6
        at n = 3; Codex: >= ceil((19n - 14)/8) for n >= 14)
DIV:    103, 104 [J] <=m tractable rows 126 (a ring proof already sits in Outside/L_gct_126.lean), 127-130, 132, 137,
        138, 141, 144-149, 154, 155, 161, 164, 172-174 [J]; 150 [C] (gap lemma)
```

### 2.10 P1: proof complexity, the parked target 071

```
071 [J, parked] family: IP lift of an unsatisfiable F2-linear system on a boundary expander (inside 065/072)
  Route W: 072 [C] rounds -> n^2/c;  W*: cover the derivation by medium walks [open]
  Route M: M1 mu(A_L) <= 2^(-rank(L)/2) on lifted critical points (P, "L2");
           M2 a line carrying a boundary parity on a fibre has rank >= 2|dS| (P, "L1"; 091, 092 in Codex Lean);
           M3 COVER-mu: every refutation puts mass >= delta on lines of rank >= rho [open];  M1 + M3 => |pi| >= delta 2^(rho/2)
  Route R: 074 [C] + the rank-weighted kill (Codex); R* obstructed (restrictions map lifted refutations to base ones)
  Route S: 075 [C] + a fat-form selection S* [open]; 076, 077 [J] (fixed dictionary, not built by strategy)
  helper rows 067, 078-092 [J]: all proved on our side (Codex L: 081, 082, 084, 085, 086, 091, 092; P: the rest)
>> M3
```

### 2.11 C1: circuit lower bounds

```
036 [W nominal, parked] <=m 041 [C] ((5n - 6)/4), 039, 040 [C]: no route above linear
013 [J] <=m 015, 022, 024, 028 [J] (Williams' method; 18 dead attempts); known edge 014, 016, 018-021, 023, 025-027 [C]
009, 010 [J] (known theorems, unformalized); 011 [J]; 033 [J] (stopped); 034 [J w1] (sanity)
```

### 2.12 L1: library and SAT search

```
alg-001 [J] SAT in P: candidates killed by alg-002 [R], lib-110 [C], alg-003 [R], lib-107 [C]
  CDCL kill lib-113 [J] <=m lib-111, pcx-013, pcx-048 [C]  (P: a composition)
  hard link alg-004 [R] -> alg-005 [X] -> alg-006 [J, parked]; restricted: lib-102, lib-103 [C];
  lib-126 [J] <=m SemanticWeakening.short_refutation (P: a composition)
evasion: lib-122 [C] <=d lib-088 [C]; lib-123 [J w90] FP3 (the hard link; "may be false"); 124, 125 [J] (P)
derandomization: lib-119, 120, 121 [J] (P, elementary)
```

---

## 3. Ranked: the twelve live items where Claude and ChatGPT contribute most

Ordered by what our mathematics changes for the fleet, weighted by the desk's own priorities and by what we hold.

**1. L-meta-738 and L-meta-647, with 739 and 720 as corollaries.**
- *Desk.* 738 posted (weight 90, 3 parallel slots); 739 posted (88, 3 slots; three outside PRs open); 720 posted (28;
  outside PR #1083 open); 647 not posted. None held.
- *Why we move it.* We have complete paper proofs, derived twice independently by Claude Opus 5.5 agents at effort max
  (meta.md §5.1 and clb.md §5.1); Steps 1, 2, 4 and the assembly were re-derived for this map. Line-degree ≤ 1 over the
  lines X (inputs z_v) means no AND reads two X-dependent wires; the points are the inputs y_u. (i) No OR mixes an
  X-dependent and an X-free wire: such a gate is 1 at (z = 0, y = 1) and the value survives every later gate, where f_G
  is 0; so every X-dependent wire w computes OR_v (z_v AND α_{w,v}(y)), and α_{o,v} = OR_{u ∈ N(v)} y_u. (ii) Transposition (= 738): T_o = 1, T_w = OR over the
  readers g of w of T_g (merge) or m_g AND T_g (multiplying AND) gives a point-only circuit with at most P + K + M - |X| + 1
  gates, of which at most P_or + M - |X| + 1 are ORs, computing the Boolean sums OR_{N(v)} y; the desk's posted sketch is
  this recursion. (iii) For sums with pairwise intersections ≤ 1, OR gates alone number ≥ Σ(|S| - 1): the labelling
  invariant of the checked 529 merges classes only at OR gates (meta.md), or 696 + 697 applied to the incidence function
  OR_i (w_i AND D'_i) with fresh line inputs w_i (clb.md). Hence P_or + M ≥ |E| - 1. (iv) The first multiplying AND g on a path from z_v covers vu inside the biclique
  Src(g) × CN(Src(g)), so K ≥ bc(G) = τ without 4-cycles. Sum: |C| ≥ |E| + τ - 1, attained by 154.
  Corollaries: 720 (12 + 4 - 1 = 15, both orientations); 655 has no witness; 739 becomes unconditional (738 + 270); the
  exact line-degree-1 size of PG(2,q) incidence is N(q + 2) - 1, order n^{3/2}; and every circuit below the count on a
  bipartite C4-free graph (582, 650, 723, 583) has line-degree ≥ 2 on both sides.
- *Start from.* `fleet_map/meta.md` §5.1; `fleet_map/clb.md` §5.1; `L_meta_647_PARTIAL_PROOF.md`;
  `pequalnp-proofs/lean/PEqualNP/Outside/L_meta_529.lean` (main_inv, gate_cases); `Defs/LineDegree.lean`; the posted
  statement of 738 in Codex's `desk_match_evidence/public_gaps.json`; `fleet_map/lib_alg.md` §5.1 (a third, partial
  identity, useful as a cross-check).
- *First task.* A Lean proof of the exact posted 738 (HasLineDegree 1, ReflTransGen reachability, the top-down ctx
  recursion), then 647; a second reader for step (iii) against 529's Lean proof; a literature check (Nechiporuk,
  Mehlhorn, Pippenger on Boolean sums; Lenz-Wegener and Amano-Maruoka on single-level circuits; Jukna-Sergeev) before a
  Hexagon note. Asking the desk for 738 uses a slot: the user's decision.

**2. L-meta-782, shard 3 (held), with the labelling lemma L-meta-792.**
- *Desk.* Held: lease e6a82d43, weight 97, 10 parallel, shard 3 = "the assembly: disjointness across outputs and the
  sum"; expires 17:36 UTC unless renewed. 792 not on the 16:28 list.
- *Why we move it.* The assembly is our step (iii) disjointness verbatim. With A(g) = {p : g(e_p) = 1} (union at OR,
  intersection at AND: checked 276), call g private for output i when A(g) ⊆ S_i and |A(g)| ≥ 2. A gate private for
  i ≠ j would give |S_i ∩ S_j| ≥ 2, so the private sets are disjoint and Σ c_i ≤ Σ |Priv_i| ≤ |C| once each |Priv_i| ≥ c_i.
  The per-output count is shards 0-2: when the root label is false, the labelling lemma 792 (529's labelling invariant
  with the accepted set L_i in place of S_i) gives |L_i| - 1 private gates; when it is true, the promise gives k.
- *Start from.* `desk/next_12.json` (exact statement and shard spec); `Outside/L_meta_529.lean`; meta.md §5.1 step 3;
  clb.md §5.1 step 3; fleet rows 270, 276.
- *First task.* Now: the shard-3 Lean file (own namespace, imports PEqualNP.Defs), lease kept renewed; confirm how the
  desk merges shards before submitting.

**3. L-meta-612 (weight 96), L-meta-606 (held), L-meta-608: the general monotone count.**
- *Desk.* 606 held (f88ea90c; shards 0 and 1 are the checked 696 and 697; shard 2 "line-degree 3 for circuits whose
  output is an AND of two factors"; shard 3 refute). 612 posted with shards "joint count", "refute on bipartite C4-free
  graphs, smallest first", "one side of degree ≤ 3". 608 withdrawn in favour of 612.
- *Why we move it.* Item 1 settles the bipartite case at line-degree 1 exactly; our single-level proof (centres of star
  ANDs form a cover, lower ORs per centre by union-find) settles single-level circuits on C4-free graphs; Codex's
  cut-and-substitute bound |E| ≤ |A|(s + 1 - k) settles boundedly many shared-gate patterns; 649 gives degree 2 with
  constant 1/48. 584 forbids the separate OR/AND split, so a proof must charge jointly. The next rung is exact: at
  line-degree 2 an AND of two X-dependent wires multiplies coefficient functions α_{a,v} α_{b,v} and creates cross terms
  z_v z_{v'} that must be absorbed; extending the transposition recursion to these quadratic terms, with 645's honest
  factor in place of the centres, is the precise open step, and an exact constant there decides 582 and 650. For shard 1,
  item 1 confines any counterexample to circuits of line-degree ≥ 2 on both sides, a strong pruning of the exact SAT
  encodings we already run (no counterexample on girth ≥ 5 graphs with n ≤ 7).
- *Caveat.* On PG(2,q) incidence, 606 or 608 gives an explicit n^{3/2} monotone bound for f_G, which the literature lists
  as open (Jukna, ECCC TR05-021, Problem 24, read by our 632 agent). The full statements are long shots; the rungs are not.
- *Start from.* `L_META_632_RESULTS.md` (second part, §§A-D); `desk/CODEX_TO_CLAUDE_L_META_606.md`; meta.md §5.4; clb.md
  §5.3; `desk/l632/mono_total_sat.py`, `run608.py`; fleet rows 629, 645, 649, 584.
- *First task.* The shard-1 refutation search over bipartite C4-free graphs in increasing order with the line-degree
  constraint; in parallel, the degree-2 exact count on paper.

**4. L-meta-632 and its cluster (631, 633; desk rows 150, 217).**
- *Desk.* 632 withdrawn 16:34 UTC; 150 and 217 posted (weight 1, one slot each), both "needed by seat-rlift-1" for an
  AND-count induction on the total edge function.
- *Why we move it.* Our 632 agent (Claude Opus 5.5 at effort max, a58224616ed89704f) proved the bound for forests and
  leaf-reducible graphs with the exact restriction ρ_K (x_K = 1, x_{N(K)} = 0 maps a circuit for P(G) to one for
  P(G - N[K]) with ≥ |Γ(K)| fewer gates) and the cover inequality τ(G) ≤ τ(G - N[K]) + |N(K)|. Restriction alone stalls
  where deg(c) > 1 (C5 already); the elimination lemma EL* (some c in a maximum independent set is a bare vertex of
  ≥ deg(c) gates) closes the induction and held on every SAT-found circuit (n = 6-9). Its general form (some vertex c
  whose restriction removes ≥ τ(G) - τ(G - N[c]) AND gates) is the inductive step of seat-rlift-1's AND-count induction on
  the total function, of which 150 is the one-gate case; our evidence is in the partial-function model. 150 itself has a
  short proof: x_c = 1 propagates the constant 1 through OR gates and
  must leave that region through an AND gate, which becomes a copy, because f_G restricted to x_c = 1 is not constant;
  then x_{N(c)} = 0 gives f_{G - N[c]} (Lean tool: the checked 669).
- *First task.* Check outside PR #917 (johnpascoe43): it claims a counterexample on 11 vertices with τ = 7 and AND count 6;
  our evaluator decides it in minutes. If it stands, 632 and EL* fall at n = 11 and the fleet's census line needs to know;
  if not, prove EL*.
- *Start from.* `L_META_632_RESULTS.md`; `desk/l632/` (andcount_cegar.py, test_elim2.py, gen_c4free.py, res_n10.txt);
  meta.md §5.3; clb.md §5.4; chatgpt_frontier_forecast.md (F3).

**5. L-gct-086 (held).**
- *Desk.* Held (5dbcef17, weight 60, 10 parallel). Context: "a proof must use Taylor orders growing with n".
- *Why we move it.* Our results fix the shape of any proof. On doubly centred cores S₂ = p₂/2 and S₃ = (2/3)p₃, so 061
  gives LS(n) ≤ n²/3 + 2n - 2; real level spaces have dim ≤ 2n - 2 and the complex excess is totally non-real; the
  root-of-unity block families F_{q,r} (S_k = 0 unless q | k) force any sufficient set of Taylor orders to have Ω(n)
  elements reaching order ≥ n/(C + 1) (Codex: (1/6 - o(1))n for C = 2); inside F_q levelness is the vanishing of every
  hyper-matching sum of a q-uniform hyper-permanent; LS(m) ≥ ⌊m/n⌋ LS(n), so 086 may be proved along powers of 2; at
  prime powers dim L ≤ (n - 1)(r + 1) with r the one-step defect of a row cycle. Codex's circulant (1, i, -i, -1) is a
  level line with p₄ = 16, which kills the entrywise power-sum route, and his span-moment lemma gives (2r + 1) dim L ≤ pq
  when the row and column spans have vanishing power sums through order r. Routes: R1 induction on q in the
  hyper-permanent; R2' a span-moment inequality up to order Θ(n); R3 symmetry with bounded defect.
- *Payoff.* An explicit m² - O(m) through 077, asymptotically below the checked 074; a proof would be a new theorem.
- *Start from.* gct.md §5.1; chatgpt_gct.md; chatgpt_gct_preparation.md; `desk/CODEX_TO_CLAUDE_L_GCT_086.md`;
  `MAPPING_AGENT_RESULTS.md` §1; `desk/next_10.json`.

**6. L-gct-179 (weight 90) and the four- and five-row table (091, 185, 210, 195, 196, 187, 191, 199).**
- *Desk.* 179 posted ("needed by seat-barrier-1 and seat-lib-1 on L-gct-086": it decides whether the four-row target is
  p + q - 3 or p + q - 2); 210 (60); the others weight 1. None held.
- *Why we move it.* Codex's Lemma K equality analysis bounds the regular-Klein-row-invariant subclasses (DC: 3, 3, 5 at
  widths 4, 5, 6; RC: ≤ 3, 4, 6, 7 at widths 4-7), so witnesses for 199 and 191 must break that symmetry, and the same
  character decomposition is the natural first case split for 179; our
  rational Klein (Walsh) chart (p₂ = tr XXᵀ, p₃ = (3/2) perm₃ X at width 4) is the coordinate system for an exact
  certificate; our complex Levenberg-Marquardt pipeline (2600 restarts at 4 × 4, dimension 6: none) can search 4 × 5,
  dimension 7 under the symmetry-breaking constraint. A witness is one polynomial identity (kernel-checkable); 215's
  472 KB case analysis on ranks of row projections is the template for an exclusion. Either answer settles 179 and
  calibrates 091 and 210.
- *Start from.* gct.md §1.4 (table) and §5.2; `MAPPING_AGENT_RESULTS.md` §1.5; chatgpt_gct.md;
  `desk/L_gct_215_accepted.lean`; fleet rows 214-217, 178, 202.

**7. L-meta-519 (weight 95): the main line's open statement.**
- *Desk.* Posted, 4 shards: a paying step at a vertex of degree 3; refute; two adjacent degree-3 vertices; a thread with
  exactly two inner vertices between degree-3 vertices. Not held.
- *Why we move it.* Codex proved on paper C(G) ≥ |E(G)| + τ(G) - 1 - b: delete a vertex set whose b cut edges leave a
  graph meeting 520's hypothesis, each deletion saving a gate by 014 with 253's restriction, then apply 520; the missing
  step is precisely to recover the b. Codex's linear-time test for 520's hypothesis and the rooted-forest formula
  C(g OR f_T) = e + min{c + v, p + u - 2} (from 548/549) are the local bookkeeping the shards need; our restriction
  calculus from the 632 work (x_K = 1, x_{N(K)} = 0 maps f_G to f_{G - N[K]} exactly) supplies the cover accounting.
- *Start from.* chatgpt_graph_templates.md; `thread_certificates.py`/`.json`; `prepared/518/`; fleet rows 204, 520, 521,
  532, 014, 253, 254, 548, 549.

**8. The NOT ladder: the per-NOT loss factor and heavy inputs (660, 661, 714, 715, 766, 885 and its instances).**
- *Desk.* None of 660, 661, 714, 715, 766, 885, 890-900 posted at 16:28; window tools 749/751 posted (88, 3 slots).
- *Why we move it.* The one-NOT bound is min over W of max(T1(W), T2(W)), with T1(W) the least Σ_w(|S_w ∩ a| - 1)⁺ over
  (W - 1)-sets a and T2(W) = q · ext_q(W), ext_q(W) the most lines of PG(2,q) a W-set misses. A Denniston arc (664 + 683)
  gives 660's 98 at q = 8 and a conic in PG(2,7) gives 661's 70 (meta.md §5.2); the route is capped at order
  q^{5/2} = N^{5/4} by the variance bound. Heavy inputs reduce to ext_q(W) and its blocking-set dual (Bruen, Blokhuis,
  Rédei polynomials), finite-geometry work in our competence, open for odd q. The decisive question is quantitative
  (clb.md §4.3): ladder bounds c_T m q with c_T = λ^T give superlinear bounds for general circuits iff λ > 2^{-1/2};
  745 gives λ about 1/2. A theorem that window recursions of this kind cannot beat λ = 1/2 is the barrier the fleet's
  main line needs; anything above 2^{-1/2} would be a superlinear lower bound for general circuits computing an explicit
  multi-output function, the line-ORs of a plane.
- *Start from.* meta.md §4.1, §5.2; clb.md §4.3, §5.2; chatgpt_frontier_forecast.md (F2); fleet rows 745, 885, 714, 715,
  660, 661, 664, 683, 685, 686.

**9. L-pcx-071 (parked): close Route M.**
- *Desk.* Not posted; pcx parked since about 00:50 UTC.
- *Why we move it.* On the IP lift of an unsatisfiable F2-linear system over a boundary expander, our L2 gives
  μ(A_L) ≤ 2^{-rank(L)/2} on lifted critical points (Codex's sequential conditioning over blocks; the largest fibre
  probabilities of all 307 affine flats of F₂⁴ are ≤ 2^{-d/2}), and our L1 shows a line carrying a k-block gadget parity
  on a fibre has rank ≥ 2k (the polar form of a sum of IP gadgets is nondegenerate alternating; 092 gives
  rank(B|_W) ≥ 2 dim W - 4k; Dickson's normal form): Lemma K transported to characteristic 2. The single missing node is
  M3 (every refutation puts mass ≥ δ on lines of rank ≥ ρ), which gives |π| ≥ δ 2^{ρ/2}; L4 shows restrictions alone
  cannot supply it. A proof is a new theorem (only n² is in print, 072), publishable on Hexagon whatever the desk does.
- *Start from.* pcx.md §5.2-5.3; chatgpt_pcx.md; fleet Lean artifacts of 065, 072, 074, 075.

**10. L-gct-025: the only missing link of the GCT target 026.**
- *Desk.* Not posted; no seat.
- *Why we move it.* With 023 and 024 checked and 027 the checked assembly, 025 (perm_{11k} restricts affinely to a smooth
  form of degree ≥ k/3 in ≥ k²/100 variables) is the whole distance between the fleet and a cubic border lower bound.
  The fleet's own gadget reaches only (r - 1)d ≤ m²/4 explicitly and m² log m generically; the manuscript route needs
  spectral curves, a Severi bound and
  Bertini. The fleet already holds Bertini-lite (058, 060) and smooth sections from transversal subspaces (053); what is
  missing is control of the singular locus of an affine restriction in about k² variables, which is algebraic geometry
  of the kind our work covers. Our existing results do not reach it (gct.md §5.8): this is a reading-and-attack task.
- *Start from.* gct.md §1.3, §3 (row 025), §5.8, §5.9 item 4; the September 2026 cubic manuscript cited by
  arXiv:2610.40484 (ECCC TR26-287); fleet rows 024, 034, 040, 053, 057, 058, 060.

**11. Ready proofs waiting for an assignment (all weight 1 or not posted).**
- *Posted:* 366, 367, 369 (Codex Lean, checker ACCEPTED locally, `prepared/36x/`); 116 (Codex Lean, accepted locally,
  1080 constants); 122 (our Lean; PR #874 closed as stood down, the row is posted again); 518 (Codex: graph facts and the
  14-gate circuit in Lean; the lower bound needs 520, which the posting's imports exclude). *Not posted:* 902, 903 (Codex
  Lean, accepted locally); 211, 125, 139, 140 (paper and identity); pcx 067, 078-092; lib 113, 119-121, 124-126.
- *Why.* No research cost; each needs only an assignment and the upstream guard. The risk is the race (186 of 241
  sampled closures were duplicates).
- *Start from.* chatgpt_ready.md, chatgpt_desk_matches.md, `prepared/`; `desk/CODEX_TO_CLAUDE_L_GCT_211.md`;
  `pequalnp-proofs/lean/PEqualNP/Outside/L_gct_122.lean`.

**12. L-gct-011 (Mulmuley-Sohoni): the cases c ≤ 2 and the obstruction barriers.**
- *Desk.* Not posted: 011 quantifies over every c, so the board would have to split it.
- *Why we move it.* Orbit-closure membership of the padded permanent gives a border expression of size n + 1;
  substituting X_00 = 1 (checked helper hasBorderDetExpression_bind₁) with the checked 074 excludes c ≤ 2 for large m, in
  60-120 Lean lines (survey a8d75352, Claude Opus 5.5 at effort high). Our GCT returns tell any obstruction search where it
  cannot succeed (no occurrence obstruction for c ≥ 25, m ≥ 5; no multiplicity obstruction of height ≤ 4 at m = 4,
  N ≥ 7; four-row obstructions under padding only when n² ≤ 2m² - m + 1, m ≥ 17): a barrier note for the general case.
- *Start from.* gct.md §1.5, §5.7; `MAPPING_OUR_RESULTS_TO_PEQUALNP.md`; JOINT_GCT_LEMMA_SPACE.tsv rows
  PNP-SURVEY:converse-006, PNP-SURVEY:L011-c<=2, GCT_FLIP, CUE_GCT:R-14.

---

## 4. Not worth our slots now, and why

- 687 and 766: compositions of checked rows; 687 is reserved for the fleet's closing file, 766 is the strategy seat's
  next item.
- 205 (Lemma FK): a three-line argument with six competing PRs in the 400-PR sample.
- 720 and 739 as separate races: outside PRs are open; our proof covers both through 738 and 647 (item 1).
- 651, 670, 737 (Petersen with NOT gates): exclusions need a structured proof; SAT certificates do not pass the desk's
  kernel rules (no native_decide), and 737 is withdrawn.
- lib-123 (FP3, weight 90): no tool of ours; the known speedups (DTIME(t) ⊆ Σ₄TIME(t/log* t); DTISP(t, s) ⊆
  Σ₂TIME(√(ts))) do not give it, and it "fails relative to some oracles".
- alg-006, clb-013/015/022/024/028, clb-036: nothing of ours (integer Res(lin) lines are not affine flats; the THR∘THR
  frontier is sign rank; no superlinear general bound).
- 036/037: the payoff is an explicit constant below the checked 074; 087 rules out Σ₄; a different zero and the cubic and
  quartic layers are needed.
- 103/104 (DIV) and the riffle rows: no input from us for DIV; riffle has no complexity payoff left (ours ready anyway).

## 5. Corrections for the shared records

- MATCHES.md: 608 not held since 15:44:57 UTC (410; withdrawn for 612); 632 withdrawn 16:34:44 UTC; 782 shard 3 held since
  about 16:51 UTC; 750 handed and withdrawn (proved by another) 16:35-16:43 UTC.
- gct.md lists 204 as open: checked 16:17 UTC (outside prover gredia, PR #998); 206 and 207 are checked too.
- 181 is false by 215 and 182 by 216 (identical hypotheses); both still listed as gaps.
- 126 has a `ring` proof in `Outside/L_gct_126.lean` while listed open.
- `L_META_632_RESULTS.md` exists (written 16:40-16:46 UTC); four program maps say it did not.
- lib-127 checked (outside prover Osyden, via Hall's theorem); meta-784 retired in favour of 901; meta-740 checked (our
  617 search answered: no circuit below 11, consistent with our exclusion of 7-9 gates).

## 6. Check events of this synthesis

| statement | date | who | type | outcome |
|---|---|---|---|---|
| L-meta-647 and 738 (paper proofs in meta.md §5.1 and clb.md §5.1) | 2026-11-23 | Claude Opus 5.5 at effort max (this synthesis) | targeted proof check of steps (i), (ii), (iv) and the assembly; step (iii) carried as background (two derivations from checked 529 and from checked 696/697) | no fault found |
| L-meta-150 (x_c = 1 elimination argument, item 4) | 2026-11-23 | same | first proof here, on paper; not read by a second reader | open to check |
| L-meta-782 shard 3 (disjointness of private gates, item 2) | 2026-11-23 | same | used and rechecked (it is step (iii)'s disjointness) | no fault found |


## Codex proof and archive cross-references

- [Exact monotone circuit size for graphs with one cycle of length at least six](chatgpt_612_unicyclic.md)
- [How a gate in an optimal path circuit can be the only low merge for many vertices](chatgpt_612_literature.md)
- [Theta-graph factor searches and their limits](chatgpt_612_constructions.md)
- [Leaf elimination, uniquely restricted matchings and failure of a birth-gate assumption](chatgpt_612_orientations.md)
- [Why the adjacent-hub shard contains the general circuit question](chatgpt_519_reduction.md)
- [Adjacent marked cycle vertices in the full basis](chatgpt_519_adjacent.md)
- [Two adjacent hubs and the 12-vertex theta graph](chatgpt_519_core.md)
- [Jukna's pair representation versus full edge functions](chatgpt_pair_representation.md)
- [Counting hazardous line outputs using a shared monotone circuit](chatgpt_hazard_faces.md)
- [Primary proofs in the local archive and downloads](chatgpt_disk_literature.md)
- [Primary sources on arXiv and Hexagon](chatgpt_web_literature.md)
- [Literature connections indexed by fleet theorem](LITERATURE_GRAPH.md)

- [Comparison of public proofs with the 17-gate theta question](chatgpt_public_overlap.md)
- [One NOT can make every projective-plane line output hazardous](chatgpt_plane_hazard_construction.md)

## Structural reading across six fields · 23 November

[Private proof and source dossiers](<<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/outputs/STRUCTURAL_48H>). The cross-field conjectures and paper derivations are tracked separately from the fleet's accepted Lean declarations.

## Geometry connections from the six-field reading

[Full proofs and files](maps/codex_geometry/README.md) · [Typed geometry implications](maps/codex_geometry/edges.json). Geometry, modular arithmetic, graph covers, circuit minima and finite-group descent.

## Marked elliptic curves and the structural lemma roadmap

[Shared geometry and moonshine map](maps/codex_moonshine.md) · [Full geometry proof dossier](maps/codex_geometry/README.md).
