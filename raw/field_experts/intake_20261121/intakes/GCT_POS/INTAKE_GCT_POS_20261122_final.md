# Intake of GCT_POS (prompt 52), the final return, by diff against checkpoint 03: items 1-7, 10, 11

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), 22 Nov 2026, for the main session (Claude Opus 5.5
at effort max). The run is GPT-6 Astra (ChatGPT Pro mode); its files give the effort as "not exposed". The return is
`research_returns\GCT_POS_final_20261122T0219Z_unzipped`. The earlier intake is
`INTAKE_GCT_POS_20261121_kronecker.md` ("the cp03 intake"). Items 8-9 (N-*) are a8d75352's and are only listed (§5).

## The result, with refuted and open kept apart

Let k_n(s) = g((s^n),(s^n),(s^n)) and M = 2^(n-1).

**Refuted: the existence clause of numerical PH3 for Kronecker coefficients**, GCT VI Hypothesis 3.3.4 with rank(x) of
§3.4, here n² + 5n. For every n ≥ 2 the series Σ k_n(s)t^s has a pole of some order M·3^r, r ≥ 0, so every form has a
denominator weight ≥ 2^(n-1) (K-023, R-NEW-004, K-024, PNEW-013). The check is the main session's (Claude Opus 5.5 at
effort max): a targeted proof check with computations, no gap found, at
`reports_20261122\gct_pos_ph3_check\CHECK.md`. I carry it and did not repeat it. The four files it hashed are
byte for byte those of the final (SHA-256 recomputed). Novelty was not searched.

**Open:**
- **the exact order M** (r = 0) for n ≥ 6. It holds for n = 2 and 3 (classical series) and n = 4, 5 (K-008, K-014);
- **PH2 for Kronecker coefficients:** a polynomial bound on p(k_n);
- **SH(a) for Kronecker coefficients:** a polynomial bound on s(k_n).

PNEW-016c is a dichotomy and decides neither PH2 nor SH(a). SH(b) is untouched by the refutation.

The run ends INCOMPLETE. It stopped at 02:01 UTC on 22 Nov, after two reviews without movement.

## 0. Method and scope

- **No code of the return was run for this intake.** My scripts are written from the statements and read data files
  only. They are in the scratchpad of session e0d20ada, a temporary folder that a reboot or cleanup can clear:
  `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\chk\gctpos`.
  - (durable copy, added 22 Nov by the main session: `reports_20261122\gct_pos_ph3_check\final_intake_scripts\`)
  - `check_final.py`: the new findings;
  - `k008_complete.py`: completeness of the mod-16 list, and its certificates;
  - `seg_compare.py`, `seg_more.py`: content against checkpoint 03;
  - `final_aux.py`: hashes, and the N-diff;
  - `final_verify.py`: the exact tests for K-022 and PNEW-016, the hashes again, and the search for the two proofs.
- **Read:** FINAL_STATUS.md (lines 1-98); for each finding, what its row says in §1.
- **The main session's events** are copied under its name, with two changes of form: ids in the run's hyphenated form,
  and its type "computation" written as "computation or formal certificate".
- **Not read:** the paper as a whole, the reviews, the dictionaries (item 11) and the source audit beyond the lines
  compared. Item 10 is the run's own "INCOMPLETE exhaustive audit"; I searched no literature.
- **No cote or scan was read**, so none is cited.

## 1. The 24 findings new since checkpoint 03 (items 1-7)

"Carried" means: statement read to the extent given, no fault seen, proof not checked. The last column gives the framework and the ids of
ours that the finding rests on or bears on.

| Id | Statement | What I read | Check | Verdict | In the project's terms |
|---|---|---|---|---|---|
| K-021 | At n = 2+7k the μ_{D_{k-l}} fixed scheme (D_j = 2·256^j) is smooth at x_k, of dimension 343l³+14l+1. For k ≥ 8 the μ_M fixed locus therefore grows cubically | statement; proof from line 29 to 104 | targeted proof check; computation from the printed gadget for every l < k ≤ 4: 1, 358, 2773, 9304 | **confirmed**, given K-020's full stabilizer | fixed points of μ_D on a GIT quotient, tangent space by Luna's slice; refutes the curve-only picture of P-F30/P-F31 for tensors |
| K-022 | A weighted cone over Gr(2,5) has two smooth μ_M-fixed curves with opposite residues, and no pole at order M | statement; proof lines 26-72 of 189 | computation for M = 8 to 64: two weights divisible by M, numerator zero to order exactly 2 (exact cyclotomic arithmetic), series regular; at M = 8 the series equals the standard-monomial count to degree 47 | **confirmed** for the cancellation; the ring properties read in part | fixed-point terms of Lefschetz-Riemann-Roch can cancel; a limit on using P-F23g alone |
| K-023 | The trace of the cyclic permutation of the factors on k_n is b_n, an SL_n-invariant count on W ⊕ S_(2,1)W; k_n ≡ b_n mod 3 | check file | main session's | **carried: checked by the main session** | Adams operation ψ³ on Schur functors (λ-ring of representations); links P-F60 to the cubic ring of P-F31 |
| R-NEW-004 | The hook-chain vector has zero Lie stabilizer | check file | main session's | **carried: checked by the main session** | stabilizer group scheme at a point of the quotient stack; input to K-024 |
| K-024 | b_n's series has a simple pole at order M, residue a unit at 3, none at M·3^r for r ≥ 1 | check file | main session's | **carried: checked by the main session** | Lefschetz-Riemann-Roch at the unique fixed curve; uses P-F23, P-F27, P-F30 |
| PNEW-013 | Congruent series mod 3 transfer the pole: k_n has one at some order M·3^r | check file; corollary lines 203-220 | main session's | **carried: checked by the main session**; its citation is an erratum (§4) | reduction mod 3 of a rational Hilbert series, a congruence in K₀; refutes 3.3.4 for GCT VI Problem 1.1.1 |
| R-DIAG-001 | xyz = w² with weights (3M,3M,3M,9M/2): a free cyclic action on the fixed locus, yet Laurent coefficients 1/6, 5/24, not 3-integral | lines 1-78 of 107 | targeted proof check; exact recomputation | **confirmed** | coherent classes on a fixed locus are not 3-integral by freeness alone; bears on K-027 |
| K-025 | n = 26: a critical tensor with a stabilizer of determinant order 3·2^25 | statement; lines 18-62 of 68 | targeted proof check; reduced matrices and order-3 element computed; the 2^25 summand rebuilt | **confirmed** | odd inertia on the quotient stack; shows why r = 0 does not follow from PNEW-013 |
| K-026 | A cyclically stable component with a free point is the chain | statement | none | carried | C₃ acting on fixed components; P-F60 |
| K-027 | Modulo 3 the principal part at order M is the chain's unit plus a class supported on exceptional components | statement | hand arithmetic on the n = 4 residues: total minus chain is divisible by 3 | carried; consistent at n = 4 | equivariant K₀ and Koszul classes on the fixed scheme; P-F23 |
| K-028 | Stabilizers of order prime to 3 leave the exceptional support | statement | none | carried | inertia stratification |
| K-029 | For k ≥ 8 the K-021 components contain nonzero μ_{3M}-fixed points | statement | none | carried | the collision strata exist |
| K-030 | Finite stabilizers leave the exceptional support | statement | none | carried | inertia stratification |
| K-031 | The chain is the only cyclically stable component; only collision closures can cancel the pole | statement | none | carried | the r = 0 gate as one virtual coherent class |
| K-032 | Normalization and graded pieces of the amplified components, n = 2+56l | first theorem's statement | none | carried | normalization of a fixed component |
| K-033 | n = 10: a four-dimensional component, normalized series of density 507281 | statement | computation: the printed series equals the printed polynomial to a = 39 | carried; the printed identity confirmed | Hilbert polynomial of a normalized fixed component |
| K-034 | That component's exception reduces to its conductor | statement | none | carried | conductor of the normalization |
| K-035 | No odd inertia on it at all, so it leaves the exception | statement | none | carried | inertia of the grading action |
| K-036 | A criterion excluding odd inertia on rank-two components | statement | none | carried | the same |
| K-037 | n = 18: an actual rank-three collision and a coherent counterclass that is not 3-integral | lines 1-44 of 301 | computation: Lemma K-037a (reduced matrices diag(ρ,1,1), order-3 element) at ρ = 0.5, 0.9 | carried; the lemma confirmed at those values | a coherent class on the collision stratum, not the class of K-031 |
| K-038 | The odd-root component at that point: stabilizer, dimension 3, local leading valuations | lines 1-40 of 244; FINAL_STATUS route 10 | none | carried | local fixed-point term at order 3D |
| PNEW-014 | A formal model with the same trace identity, reciprocity and ambient bound, in which k's analogue has small indices and b's exponential ones | statement to item 6 | none | carried | shows K₀ congruences alone cannot decide PH2 or SH(a) |
| PNEW-015 | The hook wave; a first dichotomy at 2^(n/32) | statements of a and c; proof of c in part | arithmetic 1/12 − 1/32 = 5/96 | carried | the wave of P-F56 on the trace series |
| PNEW-016 | (a) dim X^{μ_M} ≤ n³/5 for n ≥ 2000; (b) the constituent difference has degree ≤ n³/5 − 1; (c) for n ≥ 79004, p(k_n) > 2^(n/16) and s(k_n) ≥ 2^(n/16), or the coefficient mass is ≥ 2^((17/240)n⁴−6n³−4) | lines 18-22, 31-125, 141-169, 170-305 of 352 | targeted proof check of the lines read; constants recomputed exactly | **(a), (b) confirmed on the lines read; (c) confirmed given PNEW-015 and K-024. It decides neither alternative** | pole order ≤ dimension of fixed locus (Koszul); the P-F56/P-F57 route with its missing estimate named |

**Counts:** 5 confirmed here at the stated scope (K-021, K-022, K-025, R-DIAG-001, PNEW-016); 4 carried with the main
session's check; 15 carried at statement level; 0 refuted.

## 2. Earlier rows: what changed

### 2a. Verdicts and check bases that change

| Id | cp03 intake | Now | Check |
|---|---|---|---|
| Numerical PH3, Kronecker (Q1ph3, a row added by the run) | open asymptotically | **refuted** | main session's |
| K-018 | confirmed at n = 9, on the run's data | **confirmed at n = 9, 16, 23, 30**, rebuilt from the printed gadget. The formula for other n stays at statement level | computation: order of χ equals 2·256^k; margins, freeness, positivity |
| K-019 | carried | **fixed dimensions confirmed**: 1 at order 512, 4 at order 256. Discrete stabilizer carried | computation |
| K-020 | carried | **diagonal part confirmed for k ≤ 4; finite stabilizer for k ≤ 3** (full Lie rank mod 1000003). The discrete part and all k carried | computation |
| K-002, K-008 | confirmed on reruns of the run's verifiers; the list's generation unchecked | **confirmed with the gap in that check closed**: my own enumeration of all 307,307 and 291,704 normalized covered triples finds none outside the certified list, and all 87,720 certificates pass my own checker | computation |

No earlier finding is refuted or withdrawn.

### 2b. Content against checkpoint 03

The filer deleted the checkpoint-03 folder. Two content witnesses survive: the stored outputs of my own read commands,
compared as strings, and one manifest with SHA-256 (nonstandard branch only). No sizes were used.

| Rows | Compared | Result |
|---|---|---|
| K-009; the k₄ value table | whole file | same |
| K-001 to K-008 | lines 1-520 of 537 | same |
| R-NEW-003; R-NEW-002 | lines 1-90 of 115; lines 1-60 of 133 | same |
| K-014; K-018 | lines 1-60 of 132; lines 1-70 of 147 | same |
| PNEW-001, PNEW-005 | lines 1-40 and 329-420 of 429 | same |
| K-010's table | first 25 lines of the type table (the cp03 residue computation used all 77 rows) | same |
| K-012, K-013, K-016, K-019, K-020; PNEW-006, 008, 009, 010, 012 | the printed statement, 17 or 23 lines | same |
| K-017 | lines 9-24, line by line (the stored output was cut inside the statement) | each present |
| R-NEW-001 | first 5 lines; all 5,214 values checked in the final | same in those lines |
| K-011, K-015, PNEW-002, 003, 004, 007, 011 | nothing, or a title only | **cannot be said to be unchanged** |
| root LEDGER | first 81 lines | same; entries appended after |
| plethysm LEDGER; SOURCE_AUDIT | all 111 lines, cut at 900 bytes; lines 1-60 | changed (rows and entries added, some N rows reworded) |

Where a range is given, nothing is claimed outside it. "Same" holds only up to the stored width: lines were cut at 200 to 1,500 bytes in some stored outputs;
`seg_compare_result.txt` gives the width for each.

**QUESTIONS, first four columns, every row:**
- same: Q1a, Q1c, Q1n3, Q1n4, Q2 to Q8;
- added: Q1ph3;
- changed: Q1b (now "exact small dimensions and smaller exceptional support proved"; still open), Q9a to Q9e
  (a8d75352's), Q10 (now "INCOMPLETE exhaustive audit"), Q11 (dictionary provided; not read by me).

**Run events after checkpoint 03 on earlier rows of this part:** whole-proof checks of K-017 and K-019/K-020, and a
recheck of K-009. These are the run's events, not mine.

### 2c. Lines of the cp03 intake that this file replaces

Line numbers are those of `INTAKE_GCT_POS_20261121_kronecker.md` as it stands on 22 Nov.

| Lines | What they say | Replaced by |
|---|---|---|
| 49-50 | the run's two verifiers "only read files, so I ran them in place" | At that time I had read their first 30 and 20 lines and grepped for writes. I read both files on 22 Nov, after the run: standard library, read-only. The sentence claimed knowledge I did not yet have. |
| 65, 70 | K-002's generator not rerun; K-008 confirmed on the verifier | §2a. (The K-002 verifier does regenerate its coverage; the K-008 verifier does not.) |
| 77, 78, 79 | K-018, K-019, K-020 | §2a |
| 104-111 | counts | §1 for the new findings; §2a for the changes |
| 128-134, in part | poles known only at n = 4, 5 | the all-n pole, up to a power of 3. The facts at n = 4, 5 stand |
| 145-146, 186-187 | the witness "checked here exactly"; "two independent computations"; H02 waits for the final | §3. I recomputed the wave once, to 60 digits; the f₉(6) = 1 side rests on an exterior identity whose proof I did not read |
| 159-170 | PH3 for Kronecker open; attack through K-020's component | refuted; that attack is not needed for PH3. Its line 164 gave two-part orders only: K-025 gives odd factors too |
| 172-174 | PH2, SH(a): "No wave estimate yet" | still open, with an amplitude (PNEW-015) and a dichotomy (PNEW-016); §6 |
| 210-212 | H02 "Tests 1, 2 and 4 pass" | §3: for the additions, PNEW-002 to 004 and the exterior identity are unchecked |
| 213-217 | candidate "poles at n = 4, 5; wait for all n" | absorbed in H02b |
| 226-229, 235-240 | successor questions | §8 |

Lines 189-196 (H20, H21) and 230-234 stand. So do 218-221 (the K-018 candidate and its Kravtsov gate), with n = 9,
16, 23, 30 now checked where 219 says n = 9.

## 3. H02, H02b, H20, H21 (proposals; the register is not edited)

**H02 (plethysm: P-F31, P-F57).**
- The headline and the mathematics are unchanged.
- The gate "the run's final" is passed.
- PNEW-005 (threshold 79,000) and PNEW-006 (n = 9 witness) may be added only with their conditions: PNEW-002 to 004
  and the exterior identity have no intake proof check.
- Gates left: literature search with Hexagon, write-up, reading of every page.

**H02b changes most.** It was P-F60, the canonical clause for Kronecker at statement level. It becomes "numerical PH3
fails for Kronecker coefficients" (K-023, R-NEW-004, K-024, PNEW-013). The canonical clause follows, and P-F60 is no
longer needed for it.
1. **Complete:** the main session found no gap in the chain.
2. **Self-contained:** not yet. A post has to carry the proofs of P-F23, P-F27 and P-F30, which are ours and
   unpublished, and cite 3.3.4.
3. **Stable:** the run has ended, and settling r would strengthen the result without replacing it. No literature or
   Hexagon search has been done.
4. **Checked:** targeted proof check plus computations by the same checker. There is no independent re-proof and no
   second checker.
5. **Of interest:** high. It is GCT VI's hypothesis for the coefficients the flip names.

Gates: literature with Hexagon, self-contained write-up, reading of every page. The claim must stop at the existence
clause: not PH2, not SH(a), not exact order M.

**H20 (outer degree ≤ 5):** unchanged. R-NEW-001 is a checked finite table for degree six, not a formula; Q5 stays
open outside two-row output.

**H21 (varying outer degree):** unchanged in substance. Say "polynomial for each fixed b" for G-040, with PNEW-010's
obstruction to that construction. Q4 stays open.

## 4. Errata and faults

**Erratum to the run's text: the hypothesis cited for Kronecker.**
- `branches/plethysm/modular_pole_transfer.tex`, lines 207-208 (the corollary of PNEW-013), cites GCT VI Hypothesis
  1.6.7.
- `IMPLICATIONS.md`, line 5, does the same, "as fixed in the prompt".
- `QUESTIONS.tsv`, row Q1ph3 (line 4), gives 1.6.7 as the question's locator.
- `GCT_POS.tex`, lines 92-93, defines PH3 as 1.6.7 throughout.
- 1.6.7 is stated for plethysm constants. The Kronecker problem is named by **Hypothesis 3.3.4** (through 3.3.1,
  item 1 = Problem 1.1.1), with rank(x) of §3.4. Each place should cite 3.3.4; the parameter n² + 5n that the
  corollary uses is already the one of §3.4 (the run's SOURCE_AUDIT §10 says so too).
- The run does cite 3.3.4 for P-F14, and its 1.6.7 citations for the plethysm family are right.
- The cause is partly ours: the core of prompt 52, which I wrote, defined PH3 as 1.6.7 and then asked about Kronecker
  coefficients under that name; it named 3.3.1-3.3.4 only as "general-form versions".

**Faults in the dependent items:** none found in what I read. Most of K-026 to K-038 was read only as statements, so
this is no clearance of those proofs. Nothing I read affects the four results the main session checked.

**Faults of mine, found or corrected in this round:**
- the three requested corrections are made in GCT_PLETH part 4, ALPOGE_GCT part 4 and ALPOGE_GCT part 2, each with its
  check events and its old wording;
- ALPOGE_GCT part 2 also called P-F19 "Unchanged". By content, two scope passages had changed (proof the same).
  Corrected there;
- my last report said one imported module of GCT_PLETH's evaluator ran unscanned. It was 12 of 20. Corrected there;
- the verifier sentence of the cp03 intake (§2c, first row), and its "generator was not rerun" for K-002, which was
  inaccurate: that verifier regenerates the coverage;
- the cp03 intake's two claims about the n = 9 witness (§2c, lines 145-146 and 186-187);
- the core of prompt 52, which I wrote, also carried the false premise "maximal order 2^(n-1)" for tensors;
- still standing, outside the three files (all corrected 22 Nov 08:57 UTC by the main session e0d20ada, Claude Opus 5.5 at effort max):
  - ALPOGE_GCT part 3, line 132, says "identical sources" where only sizes were compared;
  - the events ALPOGE_GCT part 3 P-F31 and GCT_PLETH part 2 T-037 are typed "used and rechecked" although nothing
    was reread.

## 5. For a8d75352: N-items, not checked

By SHA-256 against the preserved checkpoint-03 manifest of `branches/nonstandard` (recorded 22:11 UTC, five minutes
before the snapshot): of 63 files listed, 51 are the same, 12 changed and none is absent. The full list is
`chk\gctpos\n_branch_diff.tsv`. Ids are the first named in each file.

- **New:** 79 files are not in that manifest (the TSV lists them). The proof files with new ids among them are:
  - N-017 `bar_fixed_first_block.tex`, N-018 `bar_fixed_second_block_failure.tex`;
  - N-019 `maximal_scaling_globalization.tex`, N-020 `sign_fibre_structure.tex`;
  - N-021 `dimension_degree_cutoff.tex`, N-022 `dimension_separate_scales.tex`;
  - N-023 `hecke_positive_comparison_obstruction.tex`, N-024 `dimension_scale_family_minimum.tex`.
- **Changed files:**
  - `nonstandard_results.tex` (the file of N-001 to N-008);
  - `integral_nonfreeness.tex` (N-009), `rational_gt_rank4.tex` (N-010), `edge_coefficients.tex` (N-011);
  - `viii_unbounded_scaling.tex` (N-012), `polynomial_order_rank4.tex` (N-015),
    `bar_fixed_finite_cutoff.tex` (N-016);
  - the two sign-specialization certificates (rank 3 and 4), the branch's CHECK_EVENTS, QUESTIONS and README.
- **Same:** `bar_fixed_descent.tex` (N-013), `viii_label_order.tex` (N-014), and the N-009 definition audit.
- QUESTIONS Q9a to Q9e all changed (§2b).

## 6. The open gates, and the next attack on each

1. **Exact order M (r = 0).** The obstacle is K-031's class: the moving Koszul class on collision closures, which has
   to cancel a unit mod 3. K-029 and K-037 show those closures exist, so freeness will not remove them, and
   R-DIAG-001 shows freeness would not give integrality. The next attack is to evaluate that class on one actual
   collision component (n = 18, with K-038's local data), or to decide the 3-adic valuation of the total residue from
   the trace identity of K-023 refined to the C₃-equivariant series.
2. **PH2 and SH(a).** The obstacle is one estimate, U_Δ^+(n;P) < 2^((17/240)n⁴−6n³−4) (PNEW-016c). The run's Fourier
   addendum shows that a subquartic bound would prove r = 0 as well, so it is at least as hard as gate 1. The next
   attack is a direct witness: an off-residue argument x where the constituent is negative, computed at n = 4 from
   R-NEW-003 once its numerator is expanded, then in a family.
3. **The K-018 orders.** The literature gate (Kravtsov; Franks-Reichenbach) stands. Later prompts must carry neither
   "maximal order 2^(n-1)" nor "odd lifts do not occur" (K-025).
4. **Q3, Q4, Q5.** Unchanged since checkpoint 03 in the columns compared: SH(b) in varying embeddings, uniform positive formulas, and outer
   degree six beyond two rows.

## 7. The scope of the two proofs, and what is new

- **Neither proof is used.**
  - I searched the return's 575 text files (tex, md, tsv, txt, py, json, bib, csv) for both names, "Riemann
    hypothesis", GRH and both titles, with the run id ALPOGE_GCT removed.
  - Outside the copy of the prompt there is one hit, SOURCE_AUDIT.md line 272: the run says that Alpöge's theorem is
    not an input to any new result and that Masullo's draft is not used.
  - The statements I read involve no L-function. PDFs and compressed files were not searched.
- **New against our own results:** the 24 rows of §1. The main one extends the refutation of numerical PH3 from
  plethysm (P-F19/P-F31) to Kronecker coefficients. P-F14 had refuted 3.3.4 only for torus subgroup restriction.
- **New against the literature: not known.** No search was made, Hexagon included.

## 8. Integration, and what a successor prompt needs

Nothing below is edited here.

- **Our earlier rows:** ALPOGE_GCT P-F60's gate (the Kronecker form of PH3) closes by K-023 to PNEW-013. The register
  changes are in §3.
- **Cotes, studies and companion notes:** none was read for this intake, so no edit is proposed.
- **A successor of prompt 52 needs:**
  - Hypothesis 3.3.4 and rank(x) of §3.4 wherever Kronecker coefficients are meant, and numerical PH3 given as refuted;
  - the main questions r = 0, then PH2 and SH(a), with the obstacles and attacks of §6;
  - neither false premise (maximal order 2^(n-1); no odd lifts), and PNEW-014 as the reason a K₀ congruence alone
    cannot decide PH2 or SH(a);
  - an exhaustive literature audit (Q10 is incomplete), with Kravtsov, Franks-Reichenbach and Hexagon.
- Prompts 30-36 were not reread, so I propose no edit to them.
