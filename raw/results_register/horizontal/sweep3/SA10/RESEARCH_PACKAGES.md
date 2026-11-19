# SA10, Espaces stratifiés: research packages, in concept

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

These are concepts only. No prompt is written tonight.

## P1. The gluing theorem for tubes, corrected (H1, H2)

**The question:**
- For which stratified spaces is X the colimit, in topoi, of the diagram of its strata, its tubes and its deleted tubes?
- Which stones are needed: all pairs i < k, the V^j_{i,k} of 151/60, or an iterated gluing?
> [19 Nov 2026, sweep 3.5] Bears on line 11: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=334); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=440). See results_register/horizontal/sweep3_5/SUMMARY.md.
- Does his van Kampen principle (151/43) hold for that colimit? It says that the homotopy type of a glued topos is the colimit of the homotopy types.
> [19 Nov 2026, sweep 3.5] Bears on line 12: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=138). See results_register/horizontal/sweep3_5/SUMMARY.md.

**Why it matters:**
- It is the theorem the 1981 stratified topos is built for.
- As stated on 151/69 it is false (SA10-S3-K3), and the page gives no proof.
> [19 Nov 2026, sweep 3.5] Bears on line 16: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=155); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=229); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=350). See results_register/horizontal/sweep3_5/SUMMARY.md.

**What it rests on:** 151/32-75 (read in full; SA10-16, SA10-17); 151/1-31 (SA10-15); the normal-crossings pieces of "Str_∞ p. 84" (probably cote 150, SA10-12).

**Strongest known reduction:**
- The two-stratum case is formal for germ topoi: Sh(X) is the fibre product of Sh(X ∖ Y) and Sh(germ of X along Y) over Sh(deleted germ).
- The successor-pair diagram is refuted by ℂ ⊃ ℝ ⊃ {0}.
- The unzipping of Ayala-Francis-Tanaka is a known iterated framework.

**Material:**
- the MPL_151_032-075 and MPL_150_085-099+151_001-031 `.tex`, with the 151 scans;
- the cote-147 `.tex` for Str_∞ ("Structure à l'infini des M_{g,ν}", pp. 83-84 = scans 147/176-177), and cote 150 §15 (scans 72-84) for its general form;
> [19 Nov 2026, sweep 3.5] Bears on line 27: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=214). See results_register/horizontal/sweep3_5/SUMMARY.md.
- Treumann 2009; Lurie, *Higher Algebra*, App. A; Ayala-Francis-Tanaka 2017;
- SGA 4, Exposé IV §9 (recollement).

## P2. The stratified homotopy type of M̄_{g,n} from Teichmüller groupoids (H3, H5)

**The question:** carry out the programme of 151/44 for M̄_{g,n}, as an orbifold or stack:
- its homotopy type (or profinite homotopy type) from the Teichmüller groupoids of the strata;
- the inertia-decomposition data (151/34, (14)) at each boundary stratum;
- the gluing of P1.

The poset of strata lacks infima in general (EXIT_TOWER A.2). What replaces the half-simplicial formalism of 151/45-56?
> [19 Nov 2026, sweep 3.5] Bears on line 38: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=192); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=246); SA10 intake 5. Corrections that bear on the trans l.149 (SA10 intake, refuted; PROPAGATION.tsv n=255); and 3 more. See results_register/horizontal/sweep3_5/SUMMARY.md.

**Why it matters:**
- It joins the stratified-spaces material of the archive to La Longue Marche, on which the research runs stand.
- It is his own stated motivation.

**What it rests on:**
- 151/32-44 and 57-69;
> [19 Nov 2026, sweep 3.5] Bears on line 45: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=139); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=199); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=481). See results_register/horizontal/sweep3_5/SUMMARY.md.
- cote 150, folios 9 and 15-16 (EXIT_TOWER);
- La Longue Marche (the Teichmüller tower);
- the Esquisse §2-3.

**Strongest known reduction:**
- EXIT_TOWER A.1-A.3 and A.12 are proved; A.11 and A.13 are refuted.
- The strata of M̄_{g,n} are products of moduli spaces M_{g′,n′}, which are K(π,1) orbifolds.

**Material:** the EXIT_TOWER return; the 150-151 `.tex` with the scans; the Longue Marche edition; the literature on the Teichmüller tower and on the boundary of M̄_{g,n}, to be chosen by the main session.

## From the sub-agent readings

<!-- reading:150_017-030 -->
### From the reading of 150_017-030 (sub-agent; the full reading is readings/150_017-030.md)

**P150b-1. The deployment of a conically stratified space (companion to P1 of the SA10 study).**
- **The question:**
  - When does iterating the découpage cônique of 023, keeping the boundaries (021, 030), produce a precylindrical
    stratification (028 a)-c), (14))?
  - What indexes its faces: the poset of strata, its flags (039-043), or the category of strata and incidences?
  - For M̄_{g,n}: is the real oriented blow-up of the boundary a precylindrical stratification once indexed by fixed
    contractions?
- **Why it matters:**
  - it is the folder's programme, its second title;
  - it is the inverse of the gluing theorem of 151/69, which is refuted as stated (P1);
> [19 Nov 2026, sweep 3.5] Bears on line 70: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=156); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=230); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=351). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - it is the geometric input of the stratified homotopy type of 151/32-44.
> [19 Nov 2026, sweep 3.5] Bears on line 71: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=140); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=200); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=482). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **What it rests on:** 150/012-033 (second pass of 17 Nov; read here 017-030); 150/039-043; 151/32-75 (the SA10
  study); EXIT_TOWER A.1-A.3, A.12.
- **Strongest known reduction:**
  - the one-stratum case is the Theorem of 023, re-proved for isomorphisms;
  - corner structure follows from compatible collars and (14) (029, checked);
  - for M̄_{g,n} the fixed-contraction intervals are Boolean (A.3) and the deployed family is locally trivial (A.12);
  - the lens shows that global infima are not to be expected.
- **Material:**
  - the corrected `.tex` of MPL_150_001-043 with the scans;
  - the EXIT_TOWER return;
  - Douady 1961, Jänich 1968, Laures 2000, Ayala-Francis-Tanaka 2017, Quinn 1988, HTWW 2000 (locators to be checked);
  - for M̄_{g,n}, T. Kimura, J. Stasheff, A. Voronov, "On operad structures of moduli spaces and string theory",
    Comm. Math. Phys. 171 (1995), 1-25 (real blow-up along the boundary; locator to be checked).
<!-- /reading:150_017-030 -->

<!-- reading:axioms_120_121_156 -->
### From the reading of axioms_120_121_156 (sub-agent; the full reading is readings/axioms_120_121_156.md)

**P-AX1. One axiom system for tame geometry from cotes 120, 121 and 156.**
- **Question:** state the system that HAX-3 describes (Boolean families on all Rⁿ with M1-M4, M5, compactness and the
  component axiom f)), prove or refute that it is the definable sets of an o-minimal structure, and derive from it the
  canonical decompositions (121/015-017), the gluing (120/013-014), and the contrée axioms of 156-4 including "modérée".
- **Why:** the three cotes come at tame geometry from three sides; none has the whole. This is the precise form of SA20-10
  and of SA21's P2 (the o-minimal contrée).
- **Rests on:** this comparison; the readings of 120, 121/1-48, 121/49-73 and cote 156.
- **Strongest known reduction:** 120 derives intersections and gluing; 121/015-017 proves the canonical decompositions on
  one space; 121/065's triangulation gives finiteness in dimension one; 156-3 gives o-minimality on lines.
- **Material:** the three Pro packages, the 156 Codex returns, and van den Dries (1998), van den Dries-Miller (Duke Math. J.
  84, 1996), Shiota (1997), Pillay-Steinhorn (1986).
<!-- /reading:axioms_120_121_156 -->

<!-- reading:150_001-016 -->
### From the reading of 150_001-016 (sub-agent; the full reading is readings/150_001-016.md)

None new.
- P1 (the gluing theorem for tubes, corrected) and P150b-1 (the deployment of a conically stratified space) gain material:
  - 002, 007 and 008: the deployment over flags, 𝒱_ijk, and the three-strata correspondences with their slips corrected (SA10-K150a-01, SA10-K150a-09, SA10-K150a-12, SA10-K150a-13);
  - 012-016, for the conical-neighbourhood part, with the hypothesis "T̊ open in X" (SA10-K150a-14, SA10-K150a-16, SA10-K150a-17).
- P2 gains the strictness of the M̄_{g,n} stratification in the sense of 004 (SA10-R150a-12).
<!-- /reading:150_001-016 -->

<!-- reading:150_031-043 -->
### From the reading of 150_031-043 (sub-agent; the full reading is readings/150_031-043.md)

**P150c-1. From the deployment to the presentation and back** (companion to P1 and P150b-1).
- **Question:**
  - For a stratified space with his conical structure (§8), build Σ: Drap(I) → Top with (1)-(3) and a)-c).
  - Prove that X is the colimit of the simultaneous mapping cones C_{Σ,d,d'} of 043 along their transition maps, which
    he leaves unwritten.
  - Prove that Σ_• is a complete Segal space equivalent to the exit-path ∞-category.
  - Then give the version over the incidence category, for M̄_{g,n}.
- **Why it matters:**
  - it is SA10-C3, the folder's main construction, which he postpones on 043 ("On reviendra sur cette construction plus
    tard");
  - it is a point-set answer to P1 (gluing) that avoids the missing corner of 151/69.
> [19 Nov 2026, sweep 3.5] Bears on line 126: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=157); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=231); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=352). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **What it rests on:** 150/032-043 (this reading), 150/044-047 (§10), and EXIT_TOWER A.4, A.7 and A.11-A.13.
- **Strongest known reduction:**
  - the one-layer Théorème of 035 (checked);
  - the well-founded recursion of §8;
  - the Segal reconstruction and the order object (SA10-R150c-31 to 34);
  - the case M̄_{0,4} (SA10-R150c-23).
- **Material:**
  - the corrected .tex of 150/012-047, with the scans;
  - EXIT_TOWER `sections/A.tex`;
  - Lurie, *Higher Algebra*, App. A; Rezk 2001; Ayala-Francis-Tanaka 2017; Quinn 1988; Mather 1970/2012.
<!-- /reading:150_031-043 -->

<!-- reading:150_044-057 -->
### From the reading of 150_044-057 (sub-agent; the full reading is readings/150_044-057.md)

None new. Material for existing packages:
- **P150b-1** (the deployment of a conically stratified space):
  - the index-free axioms of 056-057 (ⓐ-ⓒ);
  - the formality of (32);
  - the equivalence of 056 ⓑ with the repaired ⓑ+ⓒ of 045 (R150d-07, R150d-17);
  - the index sets of the boundary strata (R150d-10 to R150d-12).
- **P1** (the gluing theorem for tubes): the squares that are formal (concatenation) and those that are not (common
  final element). The pieces the successor-pair theorem of 151/69 lacks are the second kind.
> [19 Nov 2026, sweep 3.5] Bears on line 149: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=158); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=232); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=353). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **P-AX1 or the tame line:** the redundancy question F03/F06/F07, with its Top counterexample (K150d-09).
<!-- /reading:150_044-057 -->

<!-- reading:150_072-084 -->
### From the reading of 150_072-084 (sub-agent; the full reading is readings/150_072-084.md)

**P150f-1. The pro-space model of a stratified space, and the Longue Marche's pieces made canonical.**
- *The question:* for Whitney (or Thom-Mather, or homotopically stratified) spaces, prove (51), (56)-(57) for unions of
  strata, the margin (69) for J ≺ L, the agreement V_d ≃ Σ_d, and (73). Identify V_J^L with the homotopy link, and derive
  147/176's (294) canonically for normal crossings.
> [19 Nov 2026, sweep 3.5] Bears on line 159: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=215). See results_register/horizontal/sweep3_5/SUMMARY.md.
- *Why it matters:*
  - it is the gluing theorem of P1 done with the right pieces (all flags), and it repairs 151/069;
> [19 Nov 2026, sweep 3.5] Bears on line 161: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=159); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=233); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=354). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - it supplies the canonical arrow that 147/176 lacks;
> [19 Nov 2026, sweep 3.5] Bears on line 162: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=216). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - it joins cote 150 to La Longue Marche's structure at infinity of M_{g,ν}.
- *What it rests on:* 150/073-084 (read in full here), 150/031-043 (standard presentation), 151/057-069, and
> [19 Nov 2026, sweep 3.5] Bears on line 164: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=160); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=234); SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=335); and 2 more. See results_register/horizontal/sweep3_5/SUMMARY.md.
  147/160-177.
- *Strongest reduction on the page:*
  - (53) holds level by level;
  - (69) reduces to (57) in X' and to X'_L being open;
  - (57) reduces to a control condition on the retractions (R150f-19);
  - (73) is the cover spectral sequence, for I finite.
- *Material:* the second-pass `.tex` of MPL_150_044-084 and MPL_151_032-075; the first-pass `.tex` of MPL_147_138-190;
  J. Mather, "Notes on topological stability" (control data); F. Quinn 1988; J. Lurie, *Higher Algebra*, App. A;
  D. Dugger and D. Isaksen, Math. Z. 246 (2004); SGA 4 IV §9. Locators to be checked.
<!-- /reading:150_072-084 -->

<!-- reading:150_058-071 -->
### From the reading of 150_058-071 (sub-agent; the full reading is readings/150_058-071.md)

None new. Material for existing packages:
- **P150c-1 and P150b-1** (deployment and presentation):
  - K02's axiom belongs in the deployment data;
  - the Conséquence of 071 is the index-free form, with "mono" automatic (K17);
  - the Segal reading of §13 (H150e-2), with the S² and two-stratum checks.
- **P1 and P150f-1** (gluing): the realization BΣ̲ ≅ X (two strata; S² with a point) is a candidate form of the gluing
  theorem.
- **P-AX1 and the tame line:** the split of H150e-3, with the counterexamples of K07, K08 and K09.
<!-- /reading:150_058-071 -->

<!-- reading:150_085-099 -->
### From the reading of 150_085-099 (sub-agent; the full reading is readings/150_085-099.md)

**P150g-1, joined to P150f-1 (one cluster, one prompt): the band form of the pro-space model, with the hypotheses that
make it true.**
- *The question:* in P150f-1's setting (Whitney, Thom-Mather or homotopically stratified spaces), prove for bands J ≺ L:
  - (100) and (104) for Z a locally closed union of strata, and (110) from them;
  - (111), V_J^L ≃ V_{J,L};
  - V_J ≃ Σ_J ((73) with (103)) and V_J^L ≃ Σ^♭_{J,L} (H150g-1);
  - (72); (78) with L = I'∖J; (74) in its corrected form (K150g-01);
  - the colimit formulas (101), (108) and (113) for the band presentation V_{J_0…J_n};
  - the Remarque of 088: Σ_{J,L} ↪ Σ_L is independent of the conical structure up to isotopy, in o-minimal (tame)
    topology.
- *Why it matters:*
  - it is P150f-1's gluing theorem along bands instead of strata, the form that a recollement (H150f-3) and the Longue
    Marche's pieces need;
  - it puts the self-flagged (100) on its true hypothesis.
- *Refuted forms, to be stated in the prompt so that no time goes into them:*
  - (100) and (104) for arbitrary locally closed Z (R150g-36, -40);
  - (103) for non-bands (R150g-39);
  - (96) ⟸ without density (R150g-34).
- *Strongest reduction on the page:*
  - (110) ⟸ (100), through the homotopy colimit of the open cover by the V_d (R150g-43);
  - (100) for a union of strata ⟸ control on the retractions (R150f-19);
  - (111) is (110) with Z = X_L^*;
  - (78) ⟸ the corner structure of the deployment (R150g-12).
- *Material:*
  - the second-pass `.tex` of MPL_150_085-099+151_001-031, scans 085-099, with K150g-04 fixed;
  - this reading's four files;
  - P150f-1's material;
  - for the Remarque: L. van den Dries, *Tame topology and o-minimal structures* (1998), triangulation and Hardt
    triviality (locators to be checked).
<!-- /reading:150_085-099 -->

<!-- reading:151_001-017 -->
### From the reading of 151_001-017 (sub-agent; the full reading is readings/151_001-017.md)

**P151a-1. A-indexed hypercoverings: the condition between covering and flatness.**
- **Question:**
  - for φ: A → 𝒳 with A small, which conditions on the comparison maps φ_!(lim F_i) → lim φ_!(F_i) make the homotopy
    colimit of the U_α model the homotopy type of 𝒳, in the sense of Artin-Mazur?
  - how do they compare with Verdier's coskeletal hypercoverings (A = Δ^op) and with the symmetric case A = (finite
    sets)^op?
- **Why it matters:** it is the definition his 1981 van Kampen principle (151/043, H2) and his 1990 layer both need, and
> [19 Nov 2026, sweep 3.5] Bears on line 232: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=141). See results_register/horizontal/sweep3_5/SUMMARY.md.
  it would turn SA10-8 into a descent statement.
- **It rests on:** 151/011-018; 151/032, 043; Verdier, SGA 4 V §7; Artin-Mazur, *Etale Homotopy* (LNM 100, 1969);
> [19 Nov 2026, sweep 3.5] Bears on line 234: SA10 intake 2. Item by item l.79 (SA10 intake, refuted; PROPAGATION.tsv n=202); SA10 intake 2. Item by item l.80 (SA10 intake, refuted; PROPAGATION.tsv n=204); SA10 intake 5. Corrections that bear on the trans l.153 (SA10 intake, refuted; PROPAGATION.tsv n=256). See results_register/horizontal/sweep3_5/SUMMARY.md.
  Dugger-Hollander-Isaksen, "Hypercovers and simplicial presheaves", Math. Proc. Cambridge Philos. Soc. 136 (2004), 9-51
  (locators to be checked); Shulman 2012.
- **Strongest known reduction:**
  - Hyp 1, 2, 2′ ⟺ epi comparisons for forest-shaped finite diagrams;
  - (Hyp) for all finite diagrams ⟺ φ flat ⟺ φ_! left exact;
  - the symmetric nerve of G separates the two (R151a-20 to 24).
- **Material:** the corrected transcription of 151/011-020 and this reading.
> [19 Nov 2026, sweep 3.5] Bears on line 241: SA10 intake 2. Item by item l.79 (SA10 intake, refuted; PROPAGATION.tsv n=203); SA10 intake 2. Item by item l.80 (SA10 intake, refuted; PROPAGATION.tsv n=205); SA10 intake 5. Corrections that bear on the trans l.153 (SA10 intake, refuted; PROPAGATION.tsv n=257). See results_register/horizontal/sweep3_5/SUMMARY.md.

**P151a-2. His presentation of the finite sets.**
- **Question:** do (a)-(d) of 017, with the two global relations of 005 in general form, present the category of
  nonempty finite sets? Does the low-degree list of 003-005 present its truncation at three elements?
- **Method:** by comparison with Grandis, Theory Appl. Categ. 8 (2001) (locator to be checked), or by a coset
  enumeration of the presented category for n ≤ 4.
- **Why it matters:** if they do not, his "systèmes satisfaisant (*)" are a larger class than the symmetric simplicial
  sets, and the punctual hypercoverings of 017 are defined on the wrong category.
- **It rests on:** 151/003-009, 017, 019-020.
> [19 Nov 2026, sweep 3.5] Bears on line 250: SA10 intake 2. Item by item l.80 (SA10 intake, refuted; PROPAGATION.tsv n=206); SA10 intake 5. Corrections that bear on the trans l.154 (SA10 intake, refuted; PROPAGATION.tsv n=258); SA10 intake 5. Corrections that bear on the trans l.155 (SA10 intake, refuted; PROPAGATION.tsv n=259); and 1 more. See results_register/horizontal/sweep3_5/SUMMARY.md.
- **Strongest known reduction:** (a)-(d) are incomplete (R151a-26, 27). The two missing relation types are exactly 005's
  boxes, which are independent of the rest (R151a-07).
- **Material:** this reading and its scripts (`check151a.py`, `check151a_models.py`, in the reader's scratchpad; to be
  re-run from the description in the check events).
<!-- /reading:151_001-017 -->

<!-- reading:151_018-031 -->
### From the reading of 151_018-031 (sub-agent; the full reading is readings/151_018-031.md)

**P151b-1, joined to P150f-1 (one cluster, one prompt): the punctured tubular germ as a topos.**
- **The question:** which object should 𝒱^*_{Y,X} be, so that (7) recovers X, (8)-(9) hold and (11) makes sense? The
  candidates are:
  - (a) the topos limit, which collapses for T₁ spaces X and is right for schemes with the étale topology;
  - (b) the pro-topos of punctured neighbourhoods;
  - (c) the oriented product Y ×← X^*.

  The package asks for the comparison maps between them where they are defined, and for the gluing, van Kampen and
  fibration statements for each.
- **Why it matters:** 151/32-44, the homotopy type of a stratified space from its pieces, rests on this object. With
> [19 Nov 2026, sweep 3.5] Bears on line 269: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=142); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=201); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=483). See results_register/horizontal/sweep3_5/SUMMARY.md.
  the topos limit, (5)-(10) are empty for Hausdorff X.
- **What it rests on:** SA10-R151b-25 and R151b-28 to R151b-32; STUDY §1; reading 150_072-084 (§15, the
  pro-neighbourhoods).
- **The strongest known reduction:**
  - For honest open neighbourhoods, and pro-systems of them, (7) and (8) are classical: open covers and Brown's
    groupoid van Kampen theorem.
  - The étale case is Artin gluing together with the description of i^*j_* by the henselized punctured neighbourhood.
- **Material:**
  - 151/027-044 and 150/077-084;
  - SGA 4 IV 9.5;
  - Illusie et al. 2014, exposé XI;
  - Quinn 1988.
<!-- /reading:151_018-031 -->
