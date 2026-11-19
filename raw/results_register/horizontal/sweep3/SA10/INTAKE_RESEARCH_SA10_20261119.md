# Intake of RESEARCH_SA10: the gluing of tubes and the stratified homotopy hypothesis (cotes 150-151)

- **The run.** GPT-6 Astra (ChatGPT Pro mode), on the prompt built in `pro_prompt_builds/RESEARCH_SA10` (uploaded as `PROMPT(20261119-040801).md`). It worked from 04:07 to 05:40 UTC on 19 Nov 2026, about 1 h 33 min. It saved checkpoints at 04:52 and 05:37 UTC.
- **The return** is filed at `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA10_final_20261119T0540Z_unzipped`. It contains:
  - a report of 16,564 words;
  - a paper of 74 pages: `RESEARCH_SA10_paper.tex`, with nine TeX files read through `\input` and 36,554 words of TeX;
  - a results register of 74 statements;
  - 302 check events, all by the run's own agents: 131 targeted proof checks, 95 used and rechecked, 48 independent re-proofs, 19 computations, 8 refuted and refined, 1 carried as background;
  - audits.

  The return has no ITEM_STATUS file. The status column of `RESEARCH_SA10_results.csv` and the report's outcome table serve as the item status.
- **Taken in by** Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8, which built the prompt), on 19 Nov 2026, finished at about 06:50 UTC. The intake ledger, rebuilt at 06:14 UTC, has no RESEARCH_SA10 row, so this is the first intake.
- **What I read.**
  - In full: the report's sections 1-7 and its readings tables, the results register, Part A of the paper (`sections_A.tex`), `unresolved.tex`, and the verdicts and main corrections of `C_source_corrections.md`.
  - In part:
    - `B_levels.tex`: B1.3, B2.3;
    - `B56.tex`: B5.2, B6.1, B6.3;
    - `C_sections.tex`: C1.01, C2.01, C2.04, C3.01, C3.03, C4.04, C5.02-C5.04, C5.07;
    - the first half of `C5_Hurewicz_C.tex`;
    - the counts in the run's check events.
  - Not read: the other proofs of B and C, the program audits, and the PDF. That was the limit of the intake's compute bound.
- **Files beside this one:**
  - `INTAKE_RESEARCH_SA10_20261119_CHECK_EVENTS.tsv`: 42 check events. It is not the topic table: `SA10/CHECK_EVENTS.tsv`, which `rebuild.py` rebuilds, is left as it was.
  - `INTAKE_RESEARCH_SA10_20261119_checks.py` and its `.out`: independent finite checks. They neither import nor run any program of the return.
  - `INTAKE_RESEARCH_SA10_20261119_hocolim.py`, with its `.out` and `_hocolim_test.py`.

## 1. The main question (A.1): what glues the tubes

**His theorem is false, and so is our repair of it.**
- The run confirms R1: the successor-stone diagram of 151/069 does not glue.
- It also refutes our Lead L1. Even the diagram of all his pair and triple stones, with all their inclusions, fails to glue. The run's example is the Whitney and conically smooth stratification ℂ ⊃ ℝ ⊃ {0}. With connected strata the example is {0} ⊂ ℝ² ⊂ ℝ⁴.
- In ℂ ⊃ ℝ ⊃ {0}, the triple stones of (10)-(11) on 151/060 are V₀₂* and V₀₂, so they add nothing.
- The cause is that the actual overlap V₀₂ ∩ V₁₂ is a germ of the punctured disk, where the rays meet the half-planes. It is not a stone. The stones that contain its pieces, V₀₁* (the rays) and V₀₂* (the half-disks), do not see the arrow from the rays to the half-planes. So two sheaves that disagree on that arrow agree on every named stone.
- Checks E03-E05:
  - a targeted check against the second-pass reading of 151/057-060;
  - an independent finite model, which found the run's 14 inclusions exactly, a compatible cocone, and no extension in either version.

**The correct theorem (A1.2) is proved.**
- Choose open neighbourhoods N_i ⊃ X_i simultaneously for all i.
- Put R_i^ord = ⋃{X_k : i ≰ k} and W_i = N_i ∖ R_i^ord.
- Since X_i ∖ R_i^ord = S_i, each W_i is an open neighbourhood of the open stratum S_i. Local finiteness and axiom d) make the W_i an open cover.
- Take the Čech diagram in degrees 0, 1 and 2 at each stage. Regard each degree as one synchronized pro-object. Its bicolimit in 2-Pro(Topos) is cSh(X).
- This holds for any locally finite index set, with no Thom-Mather, Whitney or link hypothesis.
- For a chain X₀ ⊂ … ⊂ X_n = X, W_i is his V_{i,n}. The correction therefore reads: take the tubes of the strata in the whole space, and glue them along their actual pairwise and triple intersections, not along his V_{ij}, V*_{ij} and V^j_{i,k}.
- Check E02.

**My assessment of A1.2.** It is open-cover descent for one well-chosen cover, and it is elementary once that cover is written down. The answer's real content is twofold:
- the choice of the pieces: the order-defined R, which is what survives base change (A2.2), and neighbourhoods chosen simultaneously;
- the two counterexamples, which rule out his stones and the all-pair repair.

**Around the main question:**
- A1.1: the topos limit of the neighbourhoods, his first reading of the tube on 151/028, collapses to Sh(Y), and the punctured limit is empty. So the tubes must be pro-objects. This confirms R8.
- A1.4: degrees 0-2 are the universal arities.
- A1.5: an exact criterion for dropping pieces from a given open gluing diagram. Every point's membership category must groupoidify to the terminal groupoid.
- At the homotopy level (B2.1), the shape of ∞-topoi preserves colimits, so the full Čech diagram of ∞-topoi glues the homotopy type. His van Kampen principle for ordinary topoi (151/043) is false (B2.2).
- Checks E01, E06, E07, E22.

**An addition from this intake: the stones also fail at the level of homotopy types.**
- I replaced each stone of the ℂ ⊃ ℝ ⊃ {0} example by its homotopy type. V₁₂ is a circle around 0 carrying the two rays and the two half-strips; the other stones are finite sets.
- The homotopy colimit over the stone inclusions then has rational Betti numbers 1, 4 for all pair and triple stones, and 1, 2 for the successor stones. ℂ is contractible.
- The same program gives 1, 0 on the actual Čech diagram of A1.2, which contains the punctured-disk overlap, and 1, 1 on pt ← two points → pt.
- So no homotopy-level reading of 151/069 with his stones holds either.
- This rests on the hand computation of the stones' homotopy types and on one computation (E42). No one else has checked it.

## 2. Item by item

All 74 statements have a heading in the compiled TeX, which I checked by script over the TeX files and their `\input`s. Every proof I read is complete in the TeX. In the table, "known" means the run cites the literature for the result, with its locator.

| Item | The run's status | Statements | Checked here |
|---|---|---|---|
| **A.1** (main) | 151/069 refuted (successor, and all pairs and triples); corrected theorem proved; minimality and an exact deletion criterion proved | A1.1-A1.5 | E01-E07, E42 |
| **A.2** | Exact cofinality criterion, satisfied by every closed map (proved). Open immersions fail (refuted); but on 151/071 he writes "mais pas" before them, so this refutes our reading, not his text. Support-defined R does not commute with inverse images; order-defined R does | A2.1-A2.3 | E08-E11 |
| **A.3** | Restriction to a closed crible keeps the stones (proved). Open differences change homotopy type: S¹ against two points (refuted). j^* with j_! on constructible sheaves (proved) | A3.1-A3.2 | E12-E13 |
| **A.4** | Reconstruction valid (R2). The strict "<" on 151/070 forces X = ∅. **The Corollary of 151/052-053 is refuted**: 7 indices, 19 points, a two-point colimit; the hypotheses (23a)-(23b) as transcribed all hold. Exact zigzag criterion and cartesian-meet repair (proved). (24) of 151/054 is equivalent to meet closure, with an empty-bottom qualification. Stable-graph classification proved | A4.1-A4.5 | E14-E20 |
| **B.1** | Closed-open recollement unconditional (proved). Tube systems classify constructible sheaves under the stated hypotheses (proved). An unconditional one-stage pro-tube formula fails (refuted: Hawaiian earring, stalk ℕ). Inertia sequence with its qualifications (proved). Exact criterion (proved) | B1.1-B1.5 | E21 (B1.3) |
| **B.2** | The ordinary-topos van Kampen principle fails (refuted: Set ← BC₂ → Set). Shape of ∞-topoi preserves colimits (known: Lurie HTT 7.1.6.15, BGH 4.2.1, Hoyois 5.1). Quinn's homotopy pushout (known: Quinn 2.1, 2.4, 3.1); unrestricted L2 refuted. R5 rechecked | B2.1-B2.4 | E22-E23 |
| **B.3** | n-truncated constructible sheaves are functors on h_{n+1}Exit (known: Lurie HA A.9.3, A.9.16, A.9.7, A.7.1, A.8.14; finite induction proved). Groupoid stacks and exit 2-functors (known: Treumann 7.13-7.14). H²(S², A) = A by gerbe gluing (proved) | B3.1-B3.3 | not checked |
| **B.4** | The premise of our B.4 refuted: * ← BZ → * already gives S², and 151/041 withdraws that fear itself. The full flag diagram reconstructs X under pairwise asphericity (proved). Coherence is needed: Hopf S³ against S²×S¹ (proved) | B4.1-B4.3 | E24 |
| **B.5** (151/011-018) | Forest comparisons are exactly Hyp 1, 2, 2′; full comparisons are epic iff flat (proved). Forest does not imply flat (refuted: C₂-orbits). Symmetric nerve (proved). Flat Fin_{≠∅}^op systems are E^S (proved). Verdier hypercovers do not lie between the two (refuted). Slice-shape and Artin-Mazur criteria (proved under hypotheses). Matching maps (known). Each matching degree necessary (proved). Component sets insufficient (refuted). Subdivision filling (known: Kerodon, DHI 3.2) | B5.1-B5.10 | E25-E26 |
| **B.6** | 151/017 with the boxes of 151/005 does not present Fin_{≠∅} (refuted; the missing relation is (B6.1.1)). Grandis's presentation translated (known: Grandis §3, Th. 4.2, §5). The final low-degree list of 151/005 presents F_{≤3}^op with last subscript 1 and fails with 3. σ₃e = e on 151/003 is false | B6.1-B6.3 | E27-E29 |
| **C.1** | Weak §8 data do not imply fibrancy (refuted). Under fibrancy: the complete Segal object, the simultaneous-cone construction with three transition families, and incidence groupoids (proved under hypotheses). The collage presents Exit(X) (proved under recursive conical-collar hypotheses) | C1.01-C1.04, C1.B1-C1.B3 | E31 (C1.01) |
| **C.2** | Bare a)-c) do not imply π-control (refuted). On 150/065 the hexagon (41) is asserted commutative with a "donc", and the gap is that inference. π-control repair (proved). One radius level does not determine control (proved). The bare recapitulation is not Thom-Mather data (refuted). Smooth resolution (known: Albin 2016 Th. 6.3, ALMP, ABP, Mather §7) | C2.01-C2.05 | E32-E33 |
| **C.3** | Precylindrical does not imply manifold (refuted: Cantor × [0,∞)). Boolean flag intervals (proved). The coarse moduli space is not a manifold (refuted: a genus-4 hyperelliptic curve; an orbifold with corners instead, Looijenga 8.11, 9.13, 9.16). Exact corner criterion (proved) | C3.01-C3.04 | E34-E35 |
| **C.4** | Germ comparisons (51), (56), (57), (69) for finite metric HSS (proved, Quinn Prop. 3.2). Relative holink (proved). Spectral sequence (73) (proved). HSS alone does not give conical collars (refuted: Quinn 1988 p. 452). Germ and face with variable-radius collars (proved). Normal-crossings comparison (294) of 147/173-177 (proved) | C4.01-C4.06 | E36 |
| **C.5** | Component order for path components (proved). Transversality not automatic in TOP, PL or smooth (refuted). Manifold fibres and faces not automatic in TOP (refuted, by Cannon). True for PL bundles and smooth submersions (proved). Raw fibrancy insufficient in PL and smooth (refuted). Connected components insufficient in TOP (refuted: pseudo-arc ray). Full matrix (C5.08) | C5.01-C5.08 | E37-E41 |
| **L1** | Refuted; replaced by A1.2 and A1.5 | A1.3 | E03-E05, E42 |
| **L2** | Refuted as stated. It needs Quinn's tameness and the holink fibration; the colimit form holds for ∞-topoi only | B2.1, B2.3 | E23 |
| **L3** | Proved after correction: sets see π₀ of exit mapping spaces, groupoid stacks see π₁, n-truncated targets see h_{n+1}Exit | B3.1-B3.2 | not checked |
| **L4** | Proved in the conditional reading. Infima exist exactly for g = 0 (n ≥ 3), g = 1 (1 ≤ n ≤ 3) and (g, n) = (2, 0). EXIT_TOWER A.2 is confirmed independently | A4.5 | E19-E20 |
| **R1-R8** | R1, R2, R5, R6 and R8 confirmed. R3 confirmed, and extended to inverse images (A2.2). R4 confirmed with the connected-fibre and connecting-map qualifications (B1.4). R7 and R8 were checked item by item (`C_inherited_audit.tsv`, `C_source_corrections.md`, `B5_scope_audit.md`). Several of our corrections are refined (section 5) | | E14, E25, E30, E32, E38, E40 |

**My checks: 42 events, every outcome "holds".** The partial ones:
- C5.06: the construction holds as far as I checked it. I did not check the Hurewicz-lifting estimate or the PL and smooth models.
- C5.07: I checked only its outline.

**Not checked by this intake:**
- the items marked "not checked" above;
- in B: B1.1, B1.2, B1.4, B1.5, B2.1, B2.4, B4.2, B4.3, B5.1, B5.3-B5.8, B5.10 and B6.2;
- in C: C1.02-C1.04, C1.B1-C1.B3, C2.02, C2.03, C2.05, C3.02, C3.04, C4.01-C4.03, C4.05, C4.06, C5.01, C5.05 and C5.08.

For these, the run's own events are the only checks.

## 3. What the run settled, and what that changes

**For the topic (SA10 STUDY, HUNCHES, PACKAGES):**
- **151/069.** The theorem should be stated in the form of A1.2, with both counterexamples: the successor one (ours) and the all-pair one (the run's). Our L1 and the all-pair repair proposed in the packages should be marked refuted, with the open-cover replacement. The stones also fail at the level of homotopy types (E42).
  - His own remark on 151/059, that the stones are "des côtes mal taillées", now has a precise content: the missing pieces are the actual overlaps of the tubes.
- **151/071.** Our STUDY bullet "for X′ → X a proper local immersion or an open immersion, tubes commute with inverse images" misreads him. He writes "mais pas" before the open immersion, and he is right (A2.2).
- **151/052-053.** His Corollary is false as stated. It holds under cartesian meets (A4.3), which a stratification by closed subsets of one space satisfies automatically.
- **151/054.** L4 and EXIT_TOWER A.2 are proved: conditional infima exist exactly for the small (g, n) listed above. The literal (24) needs an empty bottom.
- **151/028 and 151/035-043.**
  - The tubes are pro-objects.
  - Tube systems classify constructible sheaves only under the uniformity conditions of B1.5.
  - The van Kampen principle holds for ∞-topoi and fails for ordinary topoi.
  - The set level sees π₀ and the stack level sees π₁ (L3).
- **151/003-018, the layer of 1990-91.**
  - His forest conditions are weaker than flatness.
  - His global presentation of Fin_{≠∅} lacks the relation (B6.1.1).
  - The final low-degree list on 151/005 is complete with subscript 1.
- **Cote 150.**
  - π-control has to be an axiom; his "donc" on 150/065 is the gap.
  - The margins of 150/051, 062, 063, 067 and 070-071 are settled in each of TOP, PL and smooth (C5.08).
  - Coarse moduli spaces of curves are not manifolds with corners; the deployment gives orbifolds with corners, or manifolds on torsion-free level covers.

**For the companion:**
- The chapter on cote 151 can now state his gluing intuition in its correct form: tubes as pro-objects, glued along their actual overlaps, with the homotopy type glued at the level of ∞-topoi. It can say exactly where his stones fall short.
- For cote 150, the chapter can carry the C5.08 matrix in place of his "sans doute conséquence" margins.
- The run claims no novelty or priority. Its searches are in `notes/root_source_searches.md`.

## 4. What is left open, and whether a successor prompt is warranted

**No mathematical item is open.** I agree for every item I checked.

**Unresolved ink, each settled mathematically for every reading:**
- the final subscript on 151/005 (1 | 3);
- the overwritten index (i | j) and S | Σ in (10) on 151/060;
- the bound of the pseudo-partition on 151/060 (l < k | l ≤ k).

**Proofs checked only by the run's own agents.** They are long and constructive: C1.B1-C1.B3 (the collage presenting Exit), C4.05, C4.06, C5.05, the Hurewicz-lifting part of C5.06, B4.2, B5.6, B5.10, and the finite induction of B3.1.

**No research successor is warranted.** The questions are settled, and a successor would only derive them again; I would not spend a Pro slot on it. The long proofs above should be checked in use by whoever writes the companion chapters on cotes 150-151, or folded into a later prompt on the same cluster.

## 5. Corrections that bear on the transcription and the second passes (cotes 150-151)

**No second-pass page needs a change.** Each reading claim of the run that I checked agrees with the second pass:
- **151/071 l.4.** The second pass reads "mais \uline{\uuline{pas}}". It is correct; our STUDY and the prompt were wrong.
- **151/070.** The strict "<" is ink, and the second pass keeps it. It is his slip (R6).
- **151/060 (10).** The overwritten index j → i and S | Σ stay unsure. Nothing mathematical depends on them.
- **151/053 (23a)-(23b).** As transcribed, they are the hypotheses the counterexample satisfies.
- **150/065 l.39-40.** "On a donc … un diagramme commutatif hexagonal" is as transcribed.

**Ink claims of the run that a reader should check on the scans before any change:**
- **151/017.** The run reads the two lower bounds as n ≥ 2 and n ≥ 3; the second pass marks them doubtful. It also argues that the margin's p_{n+1} | ρ_{n+1} denotes the idempotent δ_nK_n: read as a permutation, the statement would be false. That is a mathematical argument for the reading p, to go into the page note.
- **151/003.** The boxed subscript 3 is confirmed as ink. The relation it gives is false (SA10-K151a-01), and the transcription rightly keeps the ink.
- **151/005.** The middle box has subscript 1, confirmed. The final subscript stays unresolved; it is now settled mathematically for both readings (1 true, 3 false), and the page note can say so.

## 6. Rows for the register

**Check events:** the 42 rows INT-SA10-E01 to E42, in `INTAKE_RESEARCH_SA10_20261119_CHECK_EVENTS.tsv`. Its columns are id, statement_id, date_utc, who, type, outcome and where; each row is added to the topic's CHECK_EVENTS through `cfg_SA10.py`.

**Corrections** (columns as in SA10/CORRECTIONS.tsv: id, item, where, kind, what, corrected, evidence, decided_by). For all ten rows, decided_by is "the RESEARCH_SA10 final, GPT-6 Astra (ChatGPT Pro mode); intake by Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8". That column is left out of the table:

| id | item | where | kind | what | corrected | evidence |
|---|---|---|---|---|---|---|
| INT-SA10-K01 | SA10-17 | 151/071 l.4; SA10 STUDY.md, "A) General inverse images"; prompt A.2 | our reading corrected | "for X′ → X a proper local immersion or an open immersion, tubes commute with inverse images" | he writes "imm. loc^le propre mais pas (ou une imm. ouverte !)": open immersions are excluded, and rightly (A2.2) | A2.2; INT-SA10-E09, E10 |
| INT-SA10-K02 | SA10-16 | 151/052-053, the Corollary ("sauf erreur") | his claim refuted, refined | for I finite with binary infima, under (23a)-(23b), the X_i → X are closed immersions | false: 7 indices, 19 points, a two-point colimit. True under cartesian meets X_{i∧j} ≅ X_i ×_{X_k} X_j (automatic for closed subsets of one space); exact criterion: no zigzag identifies two points of one member | A4.2, A4.3; INT-SA10-E15-E17 |
| INT-SA10-K03 | SA10-12 | 150/065 l.39-46 | qualification of SA10-K150e-02 | "π-control missing" | he asserts (41) commutative ("On a donc … un diagramme commutatif hexagonal"); the gap is the "donc": the left square does not follow from a)-c) and has to be an axiom | C2.01; INT-SA10-E32 |
| INT-SA10-K04 | SA10-12 | 150/051 margin; 150/063 l.39 margin | refinement of SA10-K150d-09 and SA10-K150e-07 | "false in Top; true in PL and smooth" | false in TOP (C5.03, C5.04); false in PL and smooth when "fibrant" means proper Hurewicz fibration (C5.06); true for regular PL bundles and smooth submersions with the face conditions (C5.05) | C5.03-C5.06, C5.08; INT-SA10-E38-E40 |
| INT-SA10-K05 | SA10-12 | 150/068-072 | refinement of SA10-K150e-11, -12, -17 and SA10-K150f-13 | the component-order conclusions | true for open path-connected components, or open proper sources (C5.01); false for arbitrary connected finite-dimensional TOP components (C5.07) | C5.01, C5.07; INT-SA10-E41 |
| INT-SA10-K06 | SA10-17 | 151/069; prompt L1 | our lead refuted | the stones of all pairs i < k (with the triple stones and all inclusions) glue X; equivalently AFT unzipping | false for ℂ ⊃ ℝ ⊃ {0} and for {0} ⊂ ℝ² ⊂ ℝ⁴; the gluing pieces are W_i = N_i ∖ R_i^ord with their actual intersections (A1.2); unzipping gives such a cover, not the all-pair list | A1.2, A1.3, A1.5; INT-SA10-E02-E05 |
| INT-SA10-K07 | SA10-16 | 151/032, 151/043; prompt L2 | our lead refined | his normal homotopy local triviality is Quinn's condition, and under it van Kampen holds for topos colimits | Quinn's HSS needs tameness as well as the holink fibration (the Hawaiian earring has the second without the first); the colimit principle holds for ∞-topoi (B2.1) and fails for ordinary topoi (B2.2) | B2.1-B2.3; INT-SA10-E22, E23 |
| INT-SA10-K08 | SA10-16 | prompt B.4; 151/041 | our premise refuted | R5 shows that the groupoid span (8)/(10) is insufficient | false: * ← BZ → * gives S²; 151/041 withdraws the fear; the failure belongs to the set-valued constructible topos | B4.1; INT-SA10-E24 |
| INT-SA10-K09 | SA10-15 | 151/017 with the boxes of 151/005 | his claim refuted, refined | the relations (a)-(d) present the category of nonempty finite sets | the relation (1 2)K₂(1 3)δ₂ = δ₁K₁ does not follow (two-state countermodel); a complete replacement is Grandis's presentation (B6.2); in degrees ≤ 3 the final list of 151/005 is complete with subscript 1 | B6.1-B6.3; INT-SA10-E27-E29 |
| INT-SA10-K10 | SA10-17 | 151/069 | his claim refuted at a second level (intake) | his stones glue the homotopy type | for ℂ ⊃ ℝ ⊃ {0} the homotopy colimit of the stones' homotopy types has b₁ = 4 (all pairs and triples) or 2 (successor) against 0 for ℂ | INT-SA10-E42 (a computation only; not yet checked by anyone else) |

**Depends rows** (columns item, relation, other, basis, where):
- SA10-17, *corrected by*, RESEARCH_SA10 A1.2-A1.5: "the RESEARCH_SA10 final; intake 19 Nov". Where: "the gluing of 151/069 is open-cover descent for W_i = N_i ∖ R_i^ord".
- SA10-16, *corrected by*, RESEARCH_SA10 A4.2-A4.5 and B1-B4: same basis. Where: "the Corollary of 151/052-053, (24) of 151/054, and 151/028-044".
- SA10-15, *settled by*, RESEARCH_SA10 B5-B6: same basis. Where: "the hypercover layer of 151/003-018".
- SA10-12, *settled by*, RESEARCH_SA10 C1-C5: same basis. Where: "the deployment, control data and margins of cote 150".

**Deliverables row for the return** (cote_part RESEARCH_SA10):
- **Scope:** a 74-page paper with 74 statements. 24 of them carry a refutation, each with a replacement: A1.3, A2.2, A3.1, A4.2, B1.3, B2.2, B2.3, B4.1, B5.2, B5.5, B5.9, B6.1, C1.01, C2.01, C2.04, C3.01, C3.03, C4.04, C5.02-C5.04, C5.06-C5.08. The rest are proved, proved under stated hypotheses, or known with locators.
- **Checks:** 302 check events by the run; 42 by this intake.
- **Next step:** check the long proofs listed in section 4 in use; fold sections 3 and 5 into SA10 STUDY, HUNCHES and PACKAGES at the next rebuild.
- **translate_to** fr, pl, ja, es, pt-BR. **Why:** this is the stratified-spaces and tame-topology material of cotes 150-151. The tame-topology entry of `knowledge/03_archive/translation_targets.md` names Polish (the Łojasiewicz school), Japanese, French, Spanish and Brazilian Portuguese, and French is also the language of the manuscripts.
