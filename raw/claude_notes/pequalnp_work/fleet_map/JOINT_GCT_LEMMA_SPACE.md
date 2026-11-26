# One GCT lemma space: the pequalnp.com fleet's work and ours (23 Nov 2026)

Built by Claude Opus 5.5 at effort max (agent a4348514ce0275bbf, launched by session 672ae3a0 at the user's word, about
17:20 UTC). Reading only: no desk requests, no pull requests, no posts. The table is `JOINT_GCT_LEMMA_SPACE.tsv` in
this folder; this page says what is in it, cluster by cluster. Work file:
`<local>/Documents\agent_notes\a4348514ce0275bbf_NOTES.md` (the same text is in `joint_gct_space_NOTES.md`).

## What the table holds

**1,563 rows: 226 from the fleet ("swarm") and 1,337 of ours.**

- **The fleet's rows (226):**
  - all 218 GCT nodes;
  - L-lib-118, the library fact that L-gct-101 uses inline;
  - the seven meta nodes that our rows target: L-meta-583, 606, 608, 617, 632, 647 and 655.
- **No node of another programme depends on a GCT node.** No `depends_on` array points into GCT, and no GCT node
  points out of it. This holds in both the 16:28 and the 16:39 UTC proof graphs.
- **Our rows (1,337):**
  - The GCT runs. Every mathematical finding id of GCT_KRON (117), GCT_PLETH (189), GCT_OBS (140, checkpoint 15, which
    the intake read, merged with checkpoint 05), GCT_POS (85), GCT_GINEQ (23), GCT_NSRH (69), ALPOGE_GCT (108), CUE_GCT
    (137) and BR_PENCIL (42).
    - Source locators, literature checks and archive-inventory ids are left out.
    - GCT_PLETH's audit statements A-030 to A-102 review other ids. They appear as check events of the ids they
      review, not as rows.
  - Every theorem-like statement of the newest returns of GCT_FLIP (final, 152), GCT_SEPARATIONS (checkpoint 10, 89)
    and BORDER_RANK (checkpoint 14, 136). These were read inside the zips in `Downloads`; nothing was unpacked.
  - Today's pequalnp work:
    - `MAPPING_BY_READING_20261123.md` A1-A4;
    - `MAPPING_AGENT_RESULTS.md` sections 1-3;
    - the Lean proof of L-gct-122 on branch L-gct-122 of the clone;
    - the Codex results in the five `desk/CODEX_TO_CLAUDE_*` notes and in `chatgpt_gct.md`;
    - the a8d75352 survey's L-gct-011 item;
    - `L_meta_647_PARTIAL_PROOF.md`.
  - Hexagon board rows H02, H02b, H03, H13, H14, H20, H21, H23, GPK08 and GPK18; WB-0002 (three theorems); the GCT_OBS
    questions Q1a and Q1b; and CUE_GCT's sentence on the m^2/2 bound.

### The columns

The nine requested columns come first, in order: `id`, `side`, `statement`, `status`, `proof_link`, `depends_on`,
`used_by`, `topics`, `cross_edges`. Six more follow.

- **`source`.** For each field it names the origin:
  - the site, with the file: `data/lemma/<id>.<ref>.json`, the program map `data/map/program/gct.b583994396e7.json`,
    the feed pages `data/feed/program/gct/page-*.json`, `data/contributors.249cb61fb6e3.json` and
    `data/plan.c0dd4cd68cdb.json`;
  - or the repository: `lean/PEqualNP/...`;
  - or, on our side, the file and line.
- **The fleet's fields:**
  - Statements, status, `depends_on`, `used_by`, attempts, seats, deaths and corrections are from the site.
  - Proof links go to the repository (`https://github.com/brilliant-hq/pequalnp-proofs/tree/main/lean/PEqualNP/...`),
    plus the site artifact.
  - 215 lemma files are the desk cache, whose refs equal the current map refs. 204, 206 and 207 were fetched again,
    being newer.
  - Lean files of 176-178 and 215 are newer than our clone of 14:39; the accepted 215 is also in
    `desk/L_gct_215_accepted.lean`.
- **`title`.**
- **`formal_statement`:** the fleet's exact Lean statement. The `statement` column carries the plain text as posted,
  cut at 700 characters; ours is cut at 900, with the locator of the full text.
- **`history`:**
  - when the node was proposed, and by which seat;
  - its attempts, with every death reason;
  - when it was checked, and whether on an outside runner;
  - retirement or refutation, with the reason;
  - corrections.
- **`attribution`:**
  - the proposer seat and the result's contributor;
  - the outside GitHub author with the PR;
  - its role in the plan, and the news articles covering it.
- **`notes`.**

**Site snapshot.** `head.json` of 16:37:15 UTC, version `6f72ca7bb510d2d0`: 1,469 lemmas site-wide; GCT 138 checked,
63 open, 15 retired, 1 refuted, 1 in work. It agrees node for node with the proof graph rebuilt at 16:39 UTC. The files
are in `desk\site_20261123\`; 37 requests were made, at most two a second.

**Discussions.** The site publishes no hub-message or discussion file (none is listed in `head.json`). The public traces
of discussion are in the table:

- the attempts' death notes;
- retirements and corrections;
- the 504 GCT feed events;
- the seven news articles on GCT nodes: A-002, A-005, A-008, A-009, A-011, A-013 and A-031.

### Status vocabularies

- **Fleet:** checked (Lean), open (conjecture), dead (retired), refuted, in work, each with the time of the status.
- **Ours:**
  - proved, and checked by whom;
  - proved on paper, unchecked;
  - computed;
  - conjecture or open gate;
  - refuted.

**Who checked.**

- A run's own checks are by GPT-6 Astra (ChatGPT Pro mode) agents.
- Our intakes are by Claude Opus 5.5 at effort high or max, as each intake's check events record it.
- Codex's work today is GPT-6.2 Astra at reasoning effort ultra. That is what the turn context of all twelve Codex
  rollouts of 23 Nov records. `gct.md` says "effort max" for two of those sessions; their metadata says ultra.
- The three newest returns' own checks are by GPT-6 Astra (ChatGPT Pro mode). Codex intakes of 22 Nov (GPT-6.2 Astra
  at reasoning effort ultra) are noted where they apply.

### Edges

`cross_edges` holds the edges to the other side. Each edge is stored once and shown on both rows:

- on the subject row as `type:target [note]`;
- on the target row as `<-type:subject [note]`.

The types are `improves`, `uses`, `same_statement`, `parallel`, `refutes` and `open_target_of`. "candidate" marks an edge
that needs work; the work is stated in the edge.

Every edge was read from the statements, and those marked below also from the proofs. Field labels decided none of
them, and none was taken from memory. The list, with notes, is `joint_tools\edges.py`.

**121 edges:**

| type | edges |
|---|---|
| parallel | 49 |
| uses | 20 |
| improves | 14 |
| same_statement | 13 |
| open_target_of | 10 |
| refutes | 4 |
| candidate | 11 (6 parallel, 3 open_target_of, 1 improves, 1 same_statement) |

They join 56 fleet rows to 74 of ours. By the cluster of the fleet row:

| cluster | edges |
|---|---|
| border dc | 50 |
| level spaces | 38 |
| obstructions | 16 |
| riffle rank | 10 |
| meta (outside GCT) | 6 |
| sparse polynomials | 1 |

### Rows per cluster

The first number counts rows with the tag anywhere; the number in brackets counts rows with it as the main tag.

| cluster | fleet | ours |
|---|---|---|
| level spaces | 102 (102) | 25 (21) |
| border dc (with zero-locus spaces and Hessian rank) | 87 (84) | 28 (6) |
| riffle rank | 8 (8) | 4 (4) |
| border rank | 0 | 264 (257) |
| positivity and the GCT VI/VIII hypotheses | 0 | 366 (358) |
| Kronecker and plethysm coefficients | 0 | 321 (235) |
| obstructions | 2 (1) | 478 (311) |
| padding | 2 (0) | 147 (2) |
| sparse polynomials | 24 (24) | 83 (73) |
| other: archive (lambda-rings, cotes) | 0 | 72 (54) |
| other: counting and GRH | 0 | 18 (11) |
| other: meta (monotone circuits) | 7 | 5 |

How the tags were set:

- **Fleet rows:** by reading each statement.
- **Our run rows:** the main tag by the run and the id class, further tags by keywords. This is a reading aid, not a
  classification by proof.
- **Hand rows:** by reading.

## The clusters

### Level spaces

**What the fleet has.** 102 rows: 62 checked, 27 open, 13 retired.

- The base identities: 084, 088, 089, 099, 118.
- The reductions:
  - 077: a level-space bound gives a border-dc bound;
  - 092: LS(n) <= kappa(n) + 2n;
  - 098: Lemma I.
- The floor 080 (2n - 3) and the witnesses 189, 197, 198, 206, 207, 208.
- The doubly centred identities 105, 106 and 134, all three from outside authors.
- Exact small cases:
  - 094 (3 x 3, value 3); 109 (doubly centred 3 x 3, at most 1);
  - 156 and 157 (three rows);
  - 158 (real p x q: p + q - 2);
  - 214 (4 x 4, at most 6); 215 (4 x 5, at most 7; PR #806, 15:16 UTC);
  - 216 (doubly centred 4 x 4, at most 3); 217 (row-centred 4 x 4, at most 5).
- The product and core bounds: 090, 111, 123, 114, 175-177.
- Block sums: 110, and 204 (checked 16:22 UTC).

**What is open.**

- The hard link 086.
- 091: LS(4) = 5.
- 116, 122, 211 and 205.
- The searches and small cases 179, 181, 185, 187, 190, 191, 195, 196, 199 and 210.
- Build steps.

**What we have.**

- Lemma K: PNP-MBR:A1 with its Lean proof.
- The quadratic layer: PNP-MBR:A3.
- The layers S_2, S_3 and S_4 on doubly centred matrices, and the real case: PNP-MAR:1.1a-d.
- The cubic-layer bound LS(n) <= n^2/3 + 2n (1.2), sharpened by Codex to floor(n^2/3) + 2n - 2.
- The root-of-unity families and the Taylor-order barrier (1.3), with Codex's sharper count.
- Hypergraph self-similarity (1.4).
- The n = 4 rational chart and the numerical evidence (1.5).
- From Codex: the stability of Lemma K, the Klein-invariant maxima, amplification, the proof of L-gct-211, and the Lean
  proof of L-gct-116.

**Edges.**

- **same_statement:**
  - 1.1a = 105, 106; 1.1b = 134; 1.1d = 158 (square case);
  - A1 and our Lean proof = 122;
  - Codex = 211 and 116;
  - Codex's exact replay of 087.
- **improves:**
  - 216 makes our evidence that kappa(4) = 3 a theorem;
  - Codex's stability theorem improves 122.
- **uses:** 061, 065, 089, 092, 110, 175.
- **parallel:** 055, 080, 091, 116, 119, 152, 163, 204, 215 (the brief's edge 5, parallel to GCT_KRON O-011).
  - At 4 x 5 their checked 7 is below the 9 that the O-011 Hessian gives.
  - Their Lean proof of 215 is a case analysis on injection sums and row functionals; it does not decompose the
    Hessian.
- **refutes, within the Klein-invariant subclass only:** 182, 199, 191.
- **open_target_of 086:** five rows (A3, 1.2, 1.3b, the Taylor count, amplification).

**Open targets.**

- **086.** Three routes, set out in `gct.md` 5.1:
  - the q-induction on the hypergraph problem;
  - a Kneser inequality for all singleton-free invariants;
  - row symmetry with controlled defect.
- **The candidate +1 on L-gct-070** (below).
- **091**, by an exact certificate in the rational chart.
- **Proofs waiting only for a desk handout:** 122 (Lean), 116 (Lean), 211 (paper).

### Border determinantal complexity

This cluster includes the linear-space method through a zero and the Hessian-rank route.

**What the fleet has.** 87 rows: 75 checked, 8 open, 036 in work, 016 refuted, 2 retired.

- The textbook bounds formalized: 001-010 (Valiant, Grenet, Marcus-Minc, Mignon-Ressayre, Landsberg-Manivel-Ressayre).
- 015: MR + 1.
- 064, 070 and 072: 3n >= 2m^2 - 10m + 11, exact and border.
- 056, 057 and 074: border dc(perm_m)/m^2 tends to infinity.
- 024, 029 and 045: smooth forms and power sums, (r-1)(d-1)/11, a chain taken from an unrefereed 2026 manuscript.
- 035, 069 and 071: the subspace reductions.
- 044: the ceiling of the method.
- 087: a complex 7-dimensional space through Sigma_4.
- **Open:** the target 026 (a cubic bound, an unrefereed claim) and 025, 028, 036, 037, 078, 113, 115.

**What we have.**

- CUE_GCT's sentence calling m^2/2 "established", and the framing of H13 and H14.
- GCT_OBS S-002 and S-003: the LMR degree-12 example rebuilt for per_3 against det_3.
- GCT_KRON F-009 (Grenet), and M-007 with CUE_GCT G-08: explicit determinants of size S(m,r) for padded forms in few
  variables.
- The second fundamental form at Sigma_m and the real bound 2m - 2 (PNP-MAR:2a-c), with Codex's exceptional-row
  inertia.
- The survey's converse of 006, and with it 011 for c <= 2.

**Edges.**

- **The brief's edge 1.** 070, 056 and 074 improve the bound behind our "m^2/2 is the best border bound": CUE_GCT ctx,
  H13, H14.
- **010 improves S-002.** 010 gives 5 where S-002 gives 4.
- **The brief's edge 3.** S-003 uses 012, the Hessian rank of det_3 at a rank-two matrix.
- **GCT_KRON A-030:**
  - uses 013, the Mignon-Ressayre point;
  - parallel to 012, Muir's identity.
- **GCT_KRON F-009:**
  - uses 007;
  - its containment is 006 applied to 007.
- **Parallel:** M-007 and G-08 to 005 and 007.
- **The real bound at Sigma_m:**
  - uses 050 and 051;
  - parallel to 079 and to 037.
- **087 refutes the complex route at Sigma_4 (PNP-MAR:2c).**
- **QC-014 is parallel to 010 at (m, n) = (4, 7).** There 010 separates, but no multiplicity obstruction with at most
  four rows witnesses the separation.
- **Candidate: improves 070.** Codex's LS(n) <= floor(n^2/3) + 2n - 2 with 077 gives 3N + 10m >= 2m^2 + 14, one more
  than 070 in N for m >= 3. The arithmetic was rechecked here.
  - All its inputs (061, 092, 105, 106, 077) are checked in Lean. The assembly is not.
  - It is one unit, by the mechanism of 061 and 062; `gct.md` calls it "not a real gain". It is the cheapest formal
    improvement in the cluster.

### Riffle rank

**What the fleet has.** 8 rows.

- Checked: 095, 096, 097, 218. The upper bound is about n^1.585, and below c n^2/(log n)^d.
- Open: 124 (the PIR bridge), 125 (n = 2: not two terms), 139 (at least 2n - 1), 140 (n = 3: six terms).

**What we have.**

- PNP-MBR:A2: 2n - 1, as an instance of GCT_GINEQ F-13.
- PNP-MAR:3: at least 2n for n >= 3, and exactly 6 at n = 3.
- Codex: at least ceil((19n - 14)/8) for n >= 14, through disjoint recovering sets.
- PNP-MBR:A4: a route to 3n - 3 through BR_PENCIL's border substitution, torus degeneration and first prolongation.

**Edges.**

- **same_statement:** A2 = 139, and = 125 (its n = 2 case).
- **improves 139:** MAR:3 and Codex.
- **uses:** 140, giving the exact value 6; Codex's proof uses 065.
- **parallel:** GINEQ F-13 to 139; Codex's recoveries to 124, in the converse direction.
- **candidate:** A4 and BR_PENCIL P-01 to 139 and 140.

**Notes.**

- BR_PENCIL numbers its statements differently in its work files and in its sections. The first-prolongation test is P-08
  in `work/pencil/PENCIL_PROOFS.md`, while the sections give that number to another statement. The edge therefore sits on
  A4.
- Relayed from `gct.md`: 097 and 218 negate Rossman's Conjecture C.2. What remains here is exact values, without a
  complexity payoff.

### Border rank (tensors)

**The fleet has no row.** On their board "border" always means border determinantal complexity.

**What we have: 264 rows.**

- BR_PENCIL; GCT_OBS BR-001 to BR-057; GCT_GINEQ F-01 to F-24; H03.
- BORDER_RANK checkpoint 14:
  - thm:43 and thm:44 over every algebraically closed field;
  - thm:52: border rank at least 52 for the divided-power coefficient tensors of det_4 and per_4 in characteristic 0, 2
    and 3, past H03's 43;
  - thm:first-nine-intro: the first nine residual minima.

**Edges.** Only through riffle rank (F-13, A4). The substitution and apolarity machinery is the one link.

### Positivity and the GCT VI/VIII hypotheses

**The fleet has no row.** Their programme does not use the flip.

**What we have: 366 rows.**

- ALPOGE_GCT P-F1 to P-F75 and PLE-F5 to PLE-F8.
- GCT_POS N and PNEW.
- GCT_NSRH F01 to F69.
- GCT_FLIP's papers. Paper I's thm:main-collapse is WB-0002's three theorems (RH false; PH1 for the determinant false;
  no robust obstruction for m >= n^25).
- H02, H02b, H23, GPK08.

**Edges.** All are `parallel` to L-gct-011, each marked as a barrier to the flip route toward that separation: WB-0002
(three), GCT_FLIP main-collapse and padding-nonnormal, H02, H02b, H23.

### Kronecker and plethysm coefficients

**The fleet has no row.** L-gct-149's "Kronecker exponent" is the substitution x_j -> X^(2^j), not a coefficient.

**What we have: 321 rows.**

- GCT_PLETH G, T and R.
- GCT_KRON F.
- GCT_POS K and R-NEW.
- H20, H21, GPK08, GPK18.

**No edge.** Nothing on their board states a coefficient.

### Obstructions

**What the fleet has.**

- L-gct-011 (Mulmuley-Sohoni, open).
- The checked 006 (a determinantal expression puts the padded permanent in the orbit closure).
- No node mentions multiplicities, occurrence or plethysm.

**What we have: 478 rows.**

- GCT_KRON O, A and M.
- CUE_GCT R and G: four-row obstructions, the padding range.
- GCT_OBS S, QC and OBS: the padded questions at (8,9) and (17,23).
- GCT_SEPARATIONS Paper I and II: the full Hessian family; the named finite obstruction at (8,9) in degree 54 * 10^51.
- H13, H14.

**Edges.**

- **The brief's edge 2.** 010 with 006 (and its converse) settles the separations behind Q1a and Q1b. The obstruction
  questions stay open.
- **010 is parallel to our explicit obstructions,** whose separations are already implied: A-030, A-034, O-030,
  SEPARATIONS I.thm:full-family, R-12, R-13, H13, II.thm:finite-nonic, S-025, QC-019.
- **Barriers to 011:**
  - M-008, O-018 and F-021 (internal padding);
  - S-004 (same padding as theirs);
  - R-14 and H14 (four-row obstructions only for n^2 <= 2m^2 - m + 1);
  - GCT_FLIP thm:new-variable-no-occurrence: no occurrence obstruction in their exact padding for any c >= 25 (n >= 5).
- **open_target_of 011:** the survey's c <= 2, from 074 and the converse of 006.
  - The work it needs: split their node and write the converse of 006 in Lean, about 60-120 lines on their helper
    `hasBorderDetExpression_bind₁`.

### Padding

**The fleet:** 006 and 011.

**Our 147 tagged rows** come mainly from GCT_KRON, CUE_GCT, GCT_OBS, GCT_FLIP and WB-0002.

**A convention finding.** Their `paddedPerm` (`Defs/Gct.lean`) is x00^(n+1-m) perm_m with the permanent placed at
(i+1, j+1); `padIndex` avoids (0,0).

- **So the pad variable is not a permanent variable.** That is the "independent padding" of our GCT_OBS S-004, with
  support cap m^2 + 1. It is not GCT_KRON's internal padding, where X_11 is a permanent variable and the cap is m^2.
- **S-004 says which of KRON's row bounds survive the change.**
- **A correction is due.** The a8d75352 survey (`MAPPING_OUR_RESULTS_TO_PEQUALNP.md`, section 2) says their padding is
  internal and our m^2 cap applies. It should say independent, with cap m^2 + 1, and point to S-004.

**Edges.** S-004 and F-021 are parallel to 011; F-021's is a candidate, needing the transfer.

### Sparse polynomials

**What the fleet has: 24 rows, all open.**

- The algebraic route: the DIV hypotheses 103 and 104 for signed sums of powers of sparse integer polynomials divisible
  by (X+1)...(X+N).
- Its TRACTABLE ladder: weak Descartes, two cubes, the sparse-Wronskian steps, certified sign changes.
- 126 already has a one-line `ring` proof in the repository (`Outside/L_gct_126.lean`, in our clone). The map still
  lists it open.

**What we have.**

- CUE_GCT I-01 to I-45: isolation, Grassmannian compression, ROABP identity testing.
- CUE_GCT P-01 to P-20: hitting sets from purity, character and Kronecker points.
- ALPOGE_GCT C-PIT-01.

**One candidate edge.** CUE_GCT P-02 is parallel to 129: both are hitting-set statements for sparse polynomials, ours at
character points, theirs at -1..-N through Descartes. The work: decide whether a purity argument gives a DIV-type
divisibility bound. Our reading of P-01 to P-13 (`MAPPING_AGENT_RESULTS.md` 5, `gct.md` 5.8) found no root count on a
progression.

### Outside GCT (rows kept because our work targets them)

- **The meta nodes** 583, 606, 608, 617, 632, 647 and 655.
- **Our rows from `L_meta_647_PARTIAL_PROOF.md`:**
  - the normal form, the cover by first-AND centres and the reads identity (open_target_of 647 and 608);
  - the L-meta-655 SAT search;
  - the partial results on 632;
  - Jukna's formula case of 606 (same_statement, formulas only).
- **Codex's 606 for a bounded pattern count.**
- **Archive rows.** 72 of ours (lambda-rings, cote 133 and the others) carry no GCT statement. They stay, so that their
  ids resolve.

## Decided on their own board but not recorded there

- 181 (a 4 x 5 level space of dimension at least 8) is false by the checked 215.
- 182 (a doubly centred 4 x 4 level space of dimension 4) is false by the checked 216.
- 126 is proved in the repository.

These are noted on the rows; `gct.md` 2.3 says the same.

## Limits of this map

**Edges read in the proof** as well as in the statement:

- A1;
- MAR 1.1-3;
- the Codex notes;
- GCT_KRON A-030 (its known inputs), F-009, M-007, M-008, O-011 (through A3);
- GCT_OBS S-003, S-004, QC-014;
- CUE_GCT R-11 to R-14 and G-07, G-08;
- GCT_GINEQ F-13;
- the opening of the accepted proof of 215.

All other run statements were read at statement level only.

**What the table does not settle.**

- **Statuses of our run rows** come from the run's and the intakes' check events. Where a check event says only "used and
  rechecked", the status says so. Most BORDER_RANK statements carry the generic status "checks indexed in CHECK_EVENTS.tsv
  (BRR ids)".
- **Dependencies.** `depends_on` and `used_by` on our side are filled where the sources state them: the crosswalks of the
  newest papers ("consolidates earlier ids") and the hand rows. They are not a full dependency graph of our runs.
- **Statement text** of run rows was cut from the TeX by script at the defining heading or environment. Rows with no
  TeX definition quote their check events instead. There are 33 such rows, among them fifteen GCT_OBS BR rows of
  checkpoint 15.

**Files not opened:** SAT_WITNESS_EXTRACTION and the files of prompt 74.

**To rebuild:** `python -I -B <local>/pequalnp_work\fleet_map\joint_tools\build_joint.py`. The intermediate
files `ours_runs.json` and `zip_envs.json` sit beside it; `extract_ours.py` and `zip_envs.py` regenerate them.

## External claims, added 24 Nov 2026

The two claimed proofs of VP ≠ VNP are now in the table as eight rows with side `external`. No human has checked either.

- **Anthropic** (23 Nov):
  - EXT-ANTH:thm1.1, the main theorem;
  - thm1.4, approximate circuits;
  - rmkN.6, the determinantal consequence, which is not formalized;
  - thm2.2, the flat/contracting dichotomy, whose deciding case is open.
- **OpenAI** (24 Nov):
  - EXT-OAI:thm1.1;
  - cor1.2, the permanent, border dc and orbit closure;
  - thm1.3, the stretch theorem;
  - def2.1, strict shortening, which is open.

**17 new edges** bring the total to 138. Among them, cor1.2 and rmkN.6 improve L-gct-011, 026, 028 and 074, all claimed.
The full reading is in `VPVNP_INTEGRATION_20261124.md`, the per-node verdicts in `VPVNP_NODE_VERDICTS_20261124.tsv`, and
the Pro prompt on the open hinge in `vpvnp_integration/PROMPT.md`.

**Files.** The table now has 1,571 rows. The previous version is `JOINT_GCT_LEMMA_SPACE_before_vpvnp_20261124.tsv` / `.md`.
The rows come from `joint_tools/ext_claims.py`.
