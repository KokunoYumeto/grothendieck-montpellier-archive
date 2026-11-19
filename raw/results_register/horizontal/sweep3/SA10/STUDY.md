# SA10, Espaces stratifiés (cotes 150, 151, 152, 120): the study

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

**The brief:** the coordinator's message of 18 Nov, about 22:2x UTC (sweep 3). Read every transcribed page, work through the mathematics, re-derive the steps that carry it, close the dependencies, and write down the hunches, the research packages and the deliverables.

## What was read, and how

**Read in full tonight:** cote 151, scans 32-75 (package MPL_151_032-075).
- The source is the frozen Pro transcription, cleaned to `sweep3/_tools_a6d42bf6/c151b.txt`.
- The transcription of cotes 150-151 was corrected against the scans on 17 Nov by second-pass block agents (Claude Opus 5.5 at effort max): `grothendieck_archive_transcription_20261110/second_pass/out/`. I did not use those files in this reading. Where they bear on it, they agree: the strict "<" of 151/070 is read the same way there (enlarged ×5).
> [19 Nov 2026, sweep 3.5] Bears on line 11: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=167). See results_register/horizontal/sweep3_5/SUMMARY.md.
- One reading was checked on the scan image, 151/070.
> [19 Nov 2026, sweep 3.5] Bears on line 12: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=168). See results_register/horizontal/sweep3_5/SUMMARY.md.
- This is SA10-16 and SA10-17, the stratified topos of 1981: the end of §1, then §2-§3, then the beginning of his §4. On 151/070 the second pass reads the section number as 4, with a struck 2.
> [19 Nov 2026, sweep 3.5] Bears on line 13: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=169). See results_register/horizontal/sweep3_5/SUMMARY.md.

**Not read tonight, so the sweep-2 map (`sweep2/SA10/WHAT_IS_WHERE.md`) and the second pass of 17 Nov stand for them:**
- cote 150, scans 1-99 (SA10-6, 7, 10, 12, 13, 14);
- cote 151, scans 1-31 (SA10-15);
- cote 152 (SA10-18). By the split of 18 Nov, the plane trees are read by ae4ae3dc17acaa440 (SA20-7).
- cote 120 (SA10-19). By the same split, the tame axioms of 120-121 are mine; I did not reach them.

**Checks:** each re-derivation is one row of CHECK_EVENTS.tsv (SA10-C3-nn). Corrections are in CORRECTIONS.tsv (SA10-S3-Kn).

## 0. State after the readings (19 Nov 2026; extended as the readings of round 2 come in)

**Readers of round 2,** all Claude Opus 5.5 at effort max:
- the 17 Nov second-pass agents, resumed for the mathematical reading of their own blocks of cote 150;
- aff4deb18a6ec3192, for the comparison of the axiom systems of cotes 120, 121 and 156.

Their readings are in `readings/`, merged into the tables, and summarized at the end of this file.

1. **Cote 150, scans 1-16** (a00ca4596e2185740: 33 check events, 18 corrections).
   - Three statements are false without the hypothesis "T̊ open in X": 013 (8), "X* fermé" in 015 (11), and 015's c ⇒ b with Corollary 2. One counterexample refutes all three: a segment with a spur at a frontier point. With the hypothesis they hold.
   - The fidelity claim on 005 needs 4° or 3°. The counterexample is the one that refutes 151/57 (4) (SA10-S3-K1).
> [19 Nov 2026, sweep 3.5] Bears on line 33: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=319); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=425). See results_register/horizontal/sweep3_5/SUMMARY.md.
   - The correspondence of 004 is proved again, and M̄_{g,n} stratified by graph type is strict in that sense.
   - The deployed strata of 002/007 pass the (0,4) test that EXIT_TOWER A.11 fails.
   - **The pieces the gluing of 151/069 lacks:** 007's 𝒱_ijk and 002's corner square (§3).
> [19 Nov 2026, sweep 3.5] Bears on line 36: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=144); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=218); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=339). See results_register/horizontal/sweep3_5/SUMMARY.md.
   - 31 readings are still open. "strict|pur" on 016 needs a human eye.
2. **Cote 150, scans 17-30** (a81a7989e5a443c82: 34 check events, 13 corrections).
   - The Theorem of 150/023, re-proved for isomorphisms, is the one-stratum "déploiement". Its inverse cuts X open along Y and puts the collared boundary of its neighbourhood in place of Y: a real blow-up in the conical setting.
> [19 Nov 2026, sweep 3.5] Bears on line 39: INT-SA10-E31 (SA10 intake, confirmed; PROPAGATION.tsv n=485). See results_register/horizontal/sweep3_5/SUMMARY.md.
   - With the transversal collars of 027 and the cube corners of 029, his "précylindrique" stratifications are the face stratifications of manifolds with corners (H150b-1). The iterated deployment is the 1981-82 form of the Ayala-Francis-Tanaka unzipping. It is the inverse of the gluing theorem of 151/069, refuted as stated (§3).
> [19 Nov 2026, sweep 3.5] Bears on line 40: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=145); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=219); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=340). See results_register/horizontal/sweep3_5/SUMMARY.md.
   - The infimum claim of 029 holds only inside I_{ij}. Read globally it fails: the lens, a disc bounded by two arcs meeting at two corners, has two maximal common lower bounds.
   - The Proposition of 020 fails for merely compatible parts and holds for his "pure" parts.
   - Folio 9 against EXIT_TOWER: by A.1, M̄_{g,n} stratified by isomorphism classes fails his Boolean-interval condition; by A.3, the deployed version satisfies it. Our sweep-2 claim row SA10-C1 misstates A.1 (correction SA10-K150b-13).
3. **Cote 150, scans 31-43** (a1826390c189eb13e: 46 check events, 15 corrections).
   - **The reconstruction holds.** His formula (19) for gluing the space back from its strata and cut-open data, and the Théorème of 035 that they determine each other, are re-proved for isomorphisms, with the converse half of 026. The recursion of §8 is the full "déploiement".
   - **EXIT_TOWER refutes its own formalization, not his folios 15-16.** By 039 (2), his objects are the strata cut open along the lower ones. Under that convention M̄_{0,4} satisfies (1)-(2) and gives back S², so A.11 refutes the run's formalization. A.13 lies outside his hypotheses (028 c)). A.12 proves his margin condition on 039. Our record is corrected (SA10-K150c-15).
   - **The 17 Nov second pass is reversed on 033.** On the native scan, (20)ⓐ reads "Les Ẋ_β disjoints", as the first pass had it. Anything that took the second pass's "X_β" should go back.
   - **Two slips of his:** the reduction of (3) to "longueur 2" fails in his own count, where length 1 is right; and "p = long. d" on 043 should be p = card d.
   - His reconstruction of X from the flag presentation is postponed on 043 (package P150c-1).
4. **Cote 150, scans 44-57** (a7e8cd48a67cebfa2: 39 check events, 13 corrections).
   - **Square (32) on 049 is formal:** a pushout of orders gives a cartesian square of strict-flag spaces in any ordered space. Only the squares with a common final element carry geometry, through b) (33)-(34). His example square on 049 is degenerate as written; the concatenation square is meant.
   - **The restart of 056 repairs 045.** Its b) (Σ_{≤x} finite and totally ordered) is, for a deployment over I, (29) plus the disjointness of noncomparable faces.
   - **The 051 margin's claim is false in TOP.** It says (e) follows from c) and d). Counterexample: ΣH × ℝ ≅ S⁴ × ℝ, with H a homology 3-sphere (double suspension). It holds in the smooth and PL settings.
   - Five readings were decided on the scan.
   - Still open: the margins, "isotrivialité|équisingularité" on 051, and the converse of 054's equivalence.
5. **Cote 150, scans 58-71** (a3c1b6772b35008a9: 35 check events, 18 corrections).
   - **The Récapitulation (065-066) is incomplete.** As written, a)-c) do not give an order: twisting s_02 by a homeomorphism of Σ_0 keeps every condition and breaks transitivity. The missing axiom is s_ik = s_ij ∘ s_jk on Σ_ijk, that is (38)'s p₁p₂ = p₁s′, which is Mather's π-control. c) is ρ-control, and its b_ij^{-1} is a slip for s_jk^{-1}.
   - **His "probably a consequence" margins:**
     - 062 (transversality) holds under equisingularity in any setting;
     - 063 and 067 (manifold fibres and faces) fail in TOP (ΣH) and hold in PL and smoothly;
     - "mono" on 070-071 is redundant, which corrects the first pass's N07.
   - **§13, the topological category.** His "s fibrant" makes the nerve a Segal space whose mapping spaces are the links. For (S², p), Map(p, u) ≃ S¹ and the realization is S², while π₀ gives only a two-element poset: the loss of the "Remords" (147/180). For two strata the realization gives back X. This is the space-level form of §1 below (151/32-44).
> [19 Nov 2026, sweep 3.5] Bears on line 62: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=125); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=193); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=475). See results_register/horizontal/sweep3_5/SUMMARY.md.
6. **Cote 150, scans 72-84** (a04c1d305823567b3: 36 check events, 15 corrections).
   - **"Str_∞ p. 84" (151/59) is cote 147** ("Structure à l'infini des M_{g,ν}", 147/176-177). Its pieces (292)-(294) have their general form in §15 of cote 150, with a canonical comparison map V_J^L ↪ V_J ∩ V_L. H4 is refuted (SA10-K150f-14).
> [19 Nov 2026, sweep 3.5] Bears on line 64: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=207); SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=320); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=426). See results_register/horizontal/sweep3_5/SUMMARY.md.
   - **The margin (69) on 083 is re-proved under Mather's control condition and fails without domination.** It says V_J^L ↪ V_J ∩ V_L is a homotopy equivalence for J ≺ L. It answers his "Pourquoi … ?" of 077. With control, the retractions of 076 give the cartesian square (3) of 040.
   - **Refined:**
     - Σ_ij ⊂ Σ_j fails for independently chosen tubes;
     - (56) needs Z to be a union of strata;
     - row 2 of (70) is exact only when J ∩ L = ∅;
     - (49) has the slip X_(d) for X^(d);
     - the band lemma is re-proved, and his struck 3° follows from the other two.
   - Five readings stay open (072, 077, 079, 081).
7. **Cote 150, scans 85-99** (abca10fad1b368563: 44 check events, 16 corrections).
   - "Rare" in (Strat 5) means nowhere dense, as on 004. The dense faithful stratifications are exactly the locally finite partitions with the frontier condition.
   - **His "? à vérifier!" on (100) is justified.** Z = {0} ∪ {1/n} refutes both (100) and (104). Both hold when Z is a locally closed union of strata. (110) needs that hypothesis; (111) holds as it stands.
   - **(74) indexes the interior seams instead of the boundary.** The parenthetical of (75) is false, as his own margin says.
   - A compile fault in the second-pass file scan087.tex is reported to the main session (SA10-K150g-04).
8. **Cote 151, scans 1-17** (adc5b15ac68f0105c: 31 check events, 14 corrections).
   - **A layer of 1990-91.** 151/002 is the plan of "Structures stratifiées": its pages 1, 10, 16 and 23 are the sheets that begin §1-§4 (151/027, 045, 057, 070). But 151/003-025 is written on paper of 6 Dec 1990. It returns to what §1 needs, the homotopy type of a topos, and does not underlie it. The SA10-15 record is corrected (SA10-K151a-09, -10).
   - **His "forme équivalente" (Hyp) is false** (A = BC₂).
     - Hyp 1, 2 and 2′ hold exactly for forest-shaped diagrams.
     - The full (Hyp) needs equalizers and is then left exactness, so his last question has the answer no.
     - The symmetric nerve of a group satisfies Hyp 1, 2 and 2′ and realizes to BG, so these hypotheses give no descent.
   - **(**) on 017 is Hyp 2 for A = (finite sets)^op.** (*) is an incomplete presentation: it omits the two relations he boxed on 005, which are independent of the rest.
   - Packages P151a-1 (A-indexed hypercoverings) and P151a-2 (his presentation of the finite sets).
9. **Cote 151, scans 18-31** (a0370fd91592796de: 32 check events, 11 corrections).
   - **The provisional germ of 151/028 collapses.** He defines it as the topos limit of the open neighbourhoods of Y. For paracompact X that limit is Sh(Y), the punctured part is empty, and (5)-(10) say nothing. It works as a pro-object, as cote 150 §15 has it, or on étale and Zariski sites. This bears on §3 below: the stones must be read as pro-objects (SA10-K151b-05).
> [19 Nov 2026, sweep 3.5] Bears on line 87: SA10 intake 1. The main question (A.1): what glue l.52 (SA10 intake, reading; PROPAGATION.tsv n=336). See results_register/horizontal/sweep3_5/SUMMARY.md.
   - **(9) on 031 needs V* connected.** S¹ with a point refutes it under his "Y, X, X* connexes". The connected link assumed on 151/33 supplies the missing condition.
   - **"Z* is a manifold" (028) fails in plain topology** (Bing's dogbone space) and holds in PL and smoothly.
   - **Two arrows read wrong in both passes.** On the scans, the top arrows of the "cart" squares on 020 and 025 are the degeneracy X₂ ↪ X₃. (*) is cartesian for every system; (**) forces p*(X₃*) ⊂ X₂*. His "iso ???" is answered no by the nerve of ℤ/2. "i=1" on 025 is his slip for 2.
   - The letter conventions ζ|ξ and 𝔖|𝒢 (92 doubt marks) need a human look.
10. **The axiom systems of cotes 120, 121 and 156** (aff4deb18a6ec3192, `readings/axioms_120_121_156.md`: 16 check events).
   - Cote 120 (M1-M11) is the repaired copy of the cote-121 drafts:
     - M2 gives the intersections that 121/070 lacks;
     - M6-M7 prove the pushout that 121/073 leaves open;
     - M11 corrects 121/056;
     - 121/059 gives the exact form of 120/008's reconstruction.
   - The 1986 figure (156-4/2-3) is 121/052 condition by condition, with four additions.
   - "Contrée modérée" means common subdivisions. It fails in plain topology, holds o-minimally, and is Cor 2 of 121/016. It is not the Hauptvermutung (SA21 H2 refined).
   - Whether M1 follows from the others (120/008) is open.

## 1. The two-stratum case and the homotopy type (151/32-44, the end of §1)
> [19 Nov 2026, sweep 3.5] Bears on line 102: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=126); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=194); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=476). See results_register/horizontal/sweep3_5/SUMMARY.md.

**The setting:** a closed Y ⊂ X, with V_{Y,X} the tubular neighbourhood, taken as a germ, and V*_{Y,X} = V_{Y,X} ∖ Y.

**Homotopical normal local triviality (151/32, (11)):**
- V*_{Y,X} → V_{Y,X} ≃ Y should be a homotopy fibration whose fibre is the local link V*_{z,Z}.
- He proposes this as the *definition* of normal local triviality in a topos-theoretic setting, for example schemes with the étale topology.
- There the homotopy types should be profinite and localized away from the residue characteristics ("cf Artin-Mazur").

**The exact sequences (12)-(13) and the inertia-decomposition diagram (14), 151/33-34:**
- Suppose the link is connected and π₂(Y) → π₁(V*_{z,Z}) is zero.
- Then 1 → I = π₁(V*_{z,Z}) → D = π₁(V*_{Y,X}) → π₁(Y) → 1 is exact, and D maps to π₁(X*).
- (15): if Y and the link are K(π,1), so is V*_{Y,X}.
- I re-derived both from the long exact sequence (SA10-C3-04). The K(π,1) property of X* is not needed for (15).

**The category 𝓕 (151/35-36, (16)-(18 bis)).** 𝓕 is the category of sheaves locally constant on both strata. It is equivalent to the systems (E_{X*}, E_{Y,X}; φ) with φ: p*E_{Y,X} → i*E_{X*} on Π₁V*_{Y,X}. Equivalently, φ is a map of π₁(Y)-sets E_{Y,X} → E_{X*}^I.

**Two examples (151/36-40):**
- **X = ℂ, Y = {0}.** 𝓕 ≃ Ĉ, where C has objects a and b, Aut(a) = D ≅ ℤ, and one arrow a → b, so b is final. 𝓕 is therefore contractible, like ℂ. Checked (SA10-C3-05).
- **X = ℙ¹ ≃ S², Y = {∞}.** 𝓕 is again contractible, while S² is not. So X → 𝓕 is not a homotopy equivalence (24), although the pieces are K(π,1). Checked (SA10-C3-06).

**The resolution by gerbes (151/41-43):**
> [19 Nov 2026, sweep 3.5] Bears on line 123: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=127); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=195); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=477). See results_register/horizontal/sweep3_5/SUMMARY.md.
- A-gerbes glue along V*_{Y,X}.
- On a K(π,1), an A-gerbe is an extension of π by A.
- For S², the datum is an automorphism of the trivial extension of ℤ by A, so an element of Hom(ℤ, A) = A. That gives H²(S², A) ≅ A (25), "magnifique succès !". I re-derived it (SA10-C3-07).
- He concludes that there is a van Kampen theorem for colimits of topoi: "le type d'homotopie d'une Lim→ de Topos (Topos 'recollé') est la Lim→ des types d'homotopie". He judges it "relativement triviale, et justiciable sans doute de techniques bisimpliciales des plus standart".

**The programme (151/44).** The homotopy type of stratified spaces whose pieces are K(π,1) should be expressible by a finite inductive system of the fundamental groupoids of the pieces. His examples are the Teichmüller moduli spaces, their compactifications, and the tubular neighbourhoods of their canonical stratifications.

**What this is today:**
- 𝓕 is the 1-truncated exit-path category of the stratification.
- The gerbe computation is its 2-truncated level, the exit-path 2-category of constructible stacks (D. Treumann, "Exit paths and constructible stacks", Compositio Math. 145 (2009), 1504-1532).
- The full statement is the exit-path ∞-category (J. Lurie, *Higher Algebra*, Appendix A.6 and A.9; locators to be checked). This is SA10-8.

## 2. Global stratifications: the half-simplicial formalism without tubes (151/45-56, §2)
> [19 Nov 2026, sweep 3.5] Bears on line 136: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=170); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=235); SA10 intake 5. Corrections that bear on the trans l.149 (SA10 intake, refuted; PROPAGATION.tsv n=252); and 3 more. See results_register/horizontal/sweep3_5/SUMMARY.md.

**The setting (151/45-52):**
> [19 Nov 2026, sweep 3.5] Bears on line 138: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=171); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=236); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=454). See results_register/horizontal/sweep3_5/SUMMARY.md.
- a family (X_i)_{i∈I} of closed subsets, I ordered;
- (1′ a) locally finite; (1′ b) i ≤ j ⇒ X_i ⊂ X_j; (21 c) X = ⋃X_i; (21 d) X_i ∩ X_j = ⋃_{k≤i, k≤j} X_k.

**The constructions:**
- X_{Δ0} = ∐X_i → X is finite, that is proper with finite fibres, and a local immersion.
- X_{Δ1} = ∐_{i≤j} Γ_{ij}: a is an étale covering, constant on X_i with fibre I_{≥i}, and b is a local immersion.
- The X_{Δr} form the half-simplicial space of flags.

**His remarks:**
- I can be replaced by a category.
- I → P(X) need not be injective.
- One may keep only the non-degenerate flags.

**Proposition (151/52, (22)).** Under a)-d), lim→ X_{Δ*} → X is a homeomorphism. I re-derived it (SA10-C3-03):
> [19 Nov 2026, sweep 3.5] Bears on line 152: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=172); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=237); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=455). See results_register/horizontal/sweep3_5/SUMMARY.md.
- by (d), I_x is connected under ≤;
- by (c), the map is surjective;
- X_{Δ0} → X is closed and surjective, so it is a quotient map.

The Corollary of 151/52-53 ("sauf erreur", I finite with infs) was not checked.
> [19 Nov 2026, sweep 3.5] Bears on line 157: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=173); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=238); SA10 intake 5. Corrections that bear on the trans l.149 (SA10 intake, refuted; PROPAGATION.tsv n=253); and 1 more. See results_register/horizontal/sweep3_5/SUMMARY.md.

**Question (151/54, (24)).** Should (d) be strengthened to "Inf(i, j) exists and X_{i∧j} = X_i ∩ X_j"? He answers no. His example is the cone over a circle stratified by two arcs A, B and two points, with A ∩ B = {a} ∪ {b}: two connected strata with a disconnected intersection.
> [19 Nov 2026, sweep 3.5] Bears on line 159: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=174); INT-SA10-E20 (SA10 intake, confirmed; PROPAGATION.tsv n=466); SA10 intake 3. What the run settled, and what tha l.110 (SA10 intake, confirmed; PROPAGATION.tsv n=488). See results_register/horizontal/sweep3_5/SUMMARY.md.
- This is the condition he calls *polyédral* in 1986 (156-7/14: "deux éléments minorés ont un inf").
- In 1986 he again keeps the general, "spacious" case (156-7/11). See DEPENDS.

**Proposition (151/55).** The strata X_i* = X_i ∖ Ẋ_i partition X, and i(x), the least i with x ∈ X_i, is the unique i with x ∈ X_i*.
- His proof checks (SA10-C3-01).
- His margin says, "sauf erreur", that one may discard the i with X_i* = ∅. I proved that a)-d) survive (SA10-C3-02): X_k = ⋃_{l≤k, X_l*≠∅} X_l, because i(x) ≤ k for x ∈ X_k.

**(27)-(29):** Ẋ_{Δr} and X*_{Δr}. "Moralement", X*_{Δr} is the non-singular part. The X*_{Δr} do not form a half-simplicial space.

## 3. Introduction to tubes, and the gluing theorem (151/57-69, §3)
> [19 Nov 2026, sweep 3.5] Bears on line 169: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=146); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=220); SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=321); and 2 more. See results_register/horizontal/sweep3_5/SUMMARY.md.

**The definitions (151/57-58):**
> [19 Nov 2026, sweep 3.5] Bears on line 171: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=322); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=428). See results_register/horizontal/sweep3_5/SUMMARY.md.
- V̄_{ij} is the tubular neighbourhood of X_i in X_j;
- R_i = ⋃_{X_k⊅X_i} X_k and R_{ij} = R_i ∩ X_j (3, 3 bis);
- V_{ij} = V̄_{ij} ∖ R_{ij}, "un espace infinitésimal autour de" X_i*;
- V*_{ij} = V̄_{ij} ∖ Ẋ_j = V_{ij} ∩ X_j*;
- for i = j: V_{ii} = V*_{ii} = X_i*.

**(4), R_i ∩ X_i = Ẋ_i:**
- His proof of ⊂ is right.
- The inclusion ⊃, called "triviale", needs that no k < i has X_k = X_i. That holds when X_i* ≠ ∅.
- It fails otherwise. With I = {0 < 1} and X_0 = X_1 = X, we get R_1 = ∅ while Ẋ_1 = X (SA10-C3-08, SA10-S3-K1).
- He assumes X_i* ≠ ∅ only from 151/63, and at 151/71 he says he did not want to assume it. Given (4), (6)-(8) check (SA10-C3-09).
> [19 Nov 2026, sweep 3.5] Bears on line 182: INT-SA10-E10 (SA10 intake, refuted; PROPAGATION.tsv n=121); SA10 intake 2. Item by item l.72 (SA10 intake, refuted; PROPAGATION.tsv n=162); SA10 intake 5. Corrections that bear on the trans l.146 (SA10 intake, refuted; PROPAGATION.tsv n=248); and 1 more. See results_register/horizontal/sweep3_5/SUMMARY.md.

**The stones (151/58-61):**
> [19 Nov 2026, sweep 3.5] Bears on line 184: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=323); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=429). See results_register/horizontal/sweep3_5/SUMMARY.md.
- The "pierres" are X_i* → V_{ij} ← V*_{ij} → X_j*.
- On 151/59 he calls them "des côtes mal taillées". They are not enough for the pieces V^{d′}_{d,d″} ≃ Ñ | D* of "(Str_∞ p. 84)", the normal-crossings pieces. They are more than needed where j is a successor of i.
> [19 Nov 2026, sweep 3.5] Bears on line 186: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=324); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=430). See results_register/horizontal/sweep3_5/SUMMARY.md.
- Under standard equisingularity, V*_{ij} is a bundle over X_i* with fibre an open cylinder ℝ × C_{ij}, where C_{ij} is the link, compact when j is a successor of i, and V_{ij} is a bundle of cones over C_{ij}.
- The general stones are V^j_{i,k} = V̄_{ik} ∖ (R_{ik} ∪ S_{jk}) (10)-(11), with (12)-(13).
  - (12), R_{jk} ∪ S_{jk} = Ẋ_k, and (13) check (SA10-C3-10, 11).
  - His aside "(aussi R_{j,k} ∩ S_{j,k} = Ẋ_i)" is false in general. Take ℝ² with X_m the origin, X_l the x-axis, X_j = {(0,5)} and X_{l′} the y-axis, all below X_k = ℝ². Then R ∩ S is the origin, while Ẋ_j = ∅.
  - It holds, with Ẋ_j, when k is a successor of j (SA10-S3-K2).
- 151/61: he decides to work with the X_i* and the *elementary* stones V_{ij}, V*_{ij}, j a successor of i.

**The diagram Ĩ (151/62-68):**
- Among the elementary stones, under his "cas vraisemblables", the only inclusions are the three arrow types. His argument checks (SA10-C3-12).
- Ĩ has card I + 2ν vertices and 3ν arrows, ν being the number of elementary flags (checked).
- The examples are Δ_r (20), the V and Λ shapes (21)-(22), and the version with a dimension or codimension function (23)-(27).

**"Th. de recollement des tubes (1ère version)" (151/69).** "Considérons le diagramme de type Ĩ, formé par les X_i*, V*_{i,j}, V_{i,j} (i, j ∈ I, j un successeur de i) … Alors X s'identifie au topos Lim→ de ces topos." His margin adds that X should be sober.
> [19 Nov 2026, sweep 3.5] Bears on line 199: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=147); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=221); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=342). See results_register/horizontal/sweep3_5/SUMMARY.md.

**The theorem is false as stated, for any I with a chain of length 2** (SA10-C3-14, SA10-S3-K3).
- **The counterexample:** X = ℂ, X_0 = {0}, X_1 = ℝ, X_2 = ℂ. The successor pairs are (0,1) and (1,2).
- **Why it fails:**
  - The category of sheaves on the colimit topos is the 2-limit of the sheaf categories of the pieces.
  - That 2-limit contains the following object:
    - {*} on X_0*;
    - {*} on both rays of X_1*;
    - {1, 2} on both half-planes;
    - on V_{12}, the generization maps sending * ↦ 1 from the positive ray and * ↦ 2 from the negative ray, into the upper half-plane.
  - No sheaf on ℂ restricts to it. A section near 0 restricts to the upper half-plane with one value, and that value must be 1 and 2 at once.
- **Where the failure lies:** the successor-pair stones never see the germ of X_2 along X_0. That corner is the one his own remark on 151/59 points at.
> [19 Nov 2026, sweep 3.5] Bears on line 211: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=325); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=431). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **His own doubts on the page:** at 151/72 he calls the theorem's proof a local question on X, and retracts this in the margin: "un panneau dans lequel j'ai tendance à tomber, depuis le début de mes réflexions sur les croisements normaux". The sweep-2 notes record that the proof paragraph is cancelled on the page (SA10-C4).
> [19 Nov 2026, sweep 3.5] Bears on line 212: INT-SA10-E11 (SA10 intake, confirmed; PROPAGATION.tsv n=443). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **The refinement:** add the stones of every pair i < k, or the V^j_{i,k}, with their inclusions. Whether X is then the colimit is open (package P1).

## 4. The canonical topoi of a global stratification (151/70-75, his §4, the 2 struck)
> [19 Nov 2026, sweep 3.5] Bears on line 215: INT-SA10-E10 (SA10 intake, refuted; PROPAGATION.tsv n=122); SA10 intake 2. Item by item l.72 (SA10 intake, refuted; PROPAGATION.tsv n=163); SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=175); and 4 more. See results_register/horizontal/sweep3_5/SUMMARY.md.

**A) General inverse images (151/70-72):**
> [19 Nov 2026, sweep 3.5] Bears on line 217: INT-SA10-E10 (SA10 intake, refuted; PROPAGATION.tsv n=123); SA10 intake 2. Item by item l.72 (SA10 intake, refuted; PROPAGATION.tsv n=164); SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=176); and 3 more. See results_register/horizontal/sweep3_5/SUMMARY.md.
- The axioms (1) a)-d) are restated at 151/70.
> [19 Nov 2026, sweep 3.5] Bears on line 218: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=177). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - In d) the ink reads "⋃_{k<i,j}", with a plain <. That is his slip: for i = j it would give X_i = Ẋ_i. 151/52 and 151/57 have k ≤ i, j. The transcription reads the ink correctly (SA10-C3-15, SA10-S3-K4).
> [19 Nov 2026, sweep 3.5] Bears on line 219: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=178); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=239); SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=326); and 2 more. See results_register/horizontal/sweep3_5/SUMMARY.md.
- X′_i = X_i ×_X X′, and X′_{Δr} ≅ X_{Δr} ×_X X′.
- For X′ → X a proper local immersion or an open immersion, tubes commute with inverse images ((4)-(6)). His margin: "une propriété formelle importante des tubes qu'il faut vérifier … (p.ex. X compact — brrr!)".

**B) X_{I′} for a crible I′ (151/72-75):**
> [19 Nov 2026, sweep 3.5] Bears on line 223: INT-SA10-E11 (SA10 intake, confirmed; PROPAGATION.tsv n=446); INT-SA10-E12 (SA10 intake, confirmed; PROPAGATION.tsv n=450). See results_register/horizontal/sweep3_5/SUMMARY.md.
- X_{I′∩I″} = X_{I′} ∩ X_{I″} by (1 d). Checked (SA10-C3-13): k ≤ i ∈ I′ and k ≤ j ∈ I″ put k in both cribles.
- The empty strata can be discarded (74).
- On U_{I′,I″} = X_{I′} ∖ X_{I″} the induced stones need not be homotopy equivalent to the old ones: "il faut mieux ne pas trop s'avancer" (75).

**C) The V^{I‴}_{I′,I″} begins at 151/75.**
> [19 Nov 2026, sweep 3.5] Bears on line 228: INT-SA10-E12 (SA10 intake, confirmed; PROPAGATION.tsv n=451). See results_register/horizontal/sweep3_5/SUMMARY.md.

## 5. What the pages establish, what is wrong, what is open

**Proved on the page and re-derived:**
- the strata partition (151/55);
- the reconstruction of X from its half-simplicial flag space (151/52);
> [19 Nov 2026, sweep 3.5] Bears on line 234: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=179); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=240); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=458). See results_register/horizontal/sweep3_5/SUMMARY.md.
- the inertia-decomposition sequence and K(π,1) inheritance (151/33-34);
- 𝓕 for ℂ and for S² (151/38-40);
- H²(S², A) by gerbes (151/43);
> [19 Nov 2026, sweep 3.5] Bears on line 237: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=128). See results_register/horizontal/sweep3_5/SUMMARY.md.
- (6)-(8), (12)-(13), the inclusions among stones, and the crible formula.

**Wrong as written, and refined by me:**
- (4) needs X_i* ≠ ∅;
- the aside in (12);
- the gluing theorem of 151/69, refuted;
> [19 Nov 2026, sweep 3.5] Bears on line 243: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=148); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=222); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=343). See results_register/horizontal/sweep3_5/SUMMARY.md.
- the slip in (1 d) on 151/70.
> [19 Nov 2026, sweep 3.5] Bears on line 244: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=180). See results_register/horizontal/sweep3_5/SUMMARY.md.

**Open on the page:**
- the gluing theorem with the right stones;
- the formal property of tubes under inverse images (151/71);
> [19 Nov 2026, sweep 3.5] Bears on line 248: INT-SA10-E10 (SA10 intake, refuted; PROPAGATION.tsv n=124); SA10 intake 2. Item by item l.72 (SA10 intake, refuted; PROPAGATION.tsv n=165); SA10 intake 5. Corrections that bear on the trans l.146 (SA10 intake, refuted; PROPAGATION.tsv n=251); and 1 more. See results_register/horizontal/sweep3_5/SUMMARY.md.
- the comparison of constructible sheaves on X_{I′} and U_{I′,I″} (151/75);
> [19 Nov 2026, sweep 3.5] Bears on line 249: INT-SA10-E12 (SA10 intake, confirmed; PROPAGATION.tsv n=452). See results_register/horizontal/sweep3_5/SUMMARY.md.
- the van Kampen theorem for topos colimits (151/43), which he calls standard.
> [19 Nov 2026, sweep 3.5] Bears on line 250: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=129). See results_register/horizontal/sweep3_5/SUMMARY.md.

## 6. How it connects

- **To cote 150:**
  - "Str_∞ p. 84" (151/59) is cote 147, "Structure à l'infini des M_{g,ν}", p. 84 = scan 147/177, with the pieces (292)-(294) on 147/176. This was found in round 2 by a04c1d305823567b3 (SA10-K150f-14), and §15 of cote 150 is their general form. It was first guessed here to be cote 150, scans 44-84 (SA10-12), which is to be verified by his page numbers.
> [19 Nov 2026, sweep 3.5] Bears on line 255: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=208); SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=327); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=433). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - The research run EXIT_TOWER reads 150 folios 9 and 15-16. Its A.2 shows that the stratification of the moduli of stable curves has infima only for small (g, n). So his main example fails the strengthened condition of 151/54. That is a reason, from his own programme (151/44), to keep the general case.
> [19 Nov 2026, sweep 3.5] Bears on line 256: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=181); INT-SA10-E20 (SA10 intake, confirmed; PROPAGATION.tsv n=467); SA10 intake 3. What the run settled, and what tha l.110 (SA10 intake, confirmed; PROPAGATION.tsv n=489). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **To SA21 (cote 156):**
  - The axioms a)-d) of 151/45-52 are a frontier condition on closed strata, as are the figures of 156-4/2-3.
> [19 Nov 2026, sweep 3.5] Bears on line 258: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=182); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=241); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=459). See results_register/horizontal/sweep3_5/SUMMARY.md.
  - Question (24) of 151/54 is the polyhedral condition of 156-7/14.
> [19 Nov 2026, sweep 3.5] Bears on line 259: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=183); INT-SA10-E20 (SA10 intake, confirmed; PROPAGATION.tsv n=468); SA10 intake 3. What the run settled, and what tha l.110 (SA10 intake, confirmed; PROPAGATION.tsv n=490). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **To SA10-8 and Pursuing Stacks:** §1 is the 1981 form of the stratified homotopy hypothesis, with the gerbe level made explicit.
- **To La Longue Marche (1981):** 151/44 names the Teichmüller moduli spaces, their compactifications and their tubular neighbourhoods as the motivating case (H5).

## From the sub-agent readings

<!-- reading:150_017-030 -->
### From the reading of 150_017-030 (sub-agent; the full reading is readings/150_017-030.md)

**Cote 150, scans 17-30 (manuscript pages 3-9 and the §7 sheet), read in full, with the second pass of 17 Nov as
text.** On 012-016 the conical neighbourhood is the cone C(f) of f = 0·(−): Ṫ → Y, a mapping cylinder with its
[0,1]-action.

**The two compatibility notions and equisingularity (017-020).**
- Compatibility of a closed part with a collar is conical compatibility plus purity, T'∩Y = 0·Ṫ' (re-proved).
- Equisingularity is strengthened from separate local triviality to that of the whole family. A crossing pair of
  sections shows why.
- The alternative (14) and strict equisingularity after shrinking are re-proved.
- The Proposition of 020 is false for merely compatible parts; it holds for parts pure in the sense of the 018 margin.

**Germs and the découpage cônique (022-024).**
- The germ relation is an equivalence; his margin gives the step for transitivity.
- The Theorem of 023, an equivalence for isomorphisms between conical germs and data (X̃^*, Ẋ, ℰ, Y, f), is re-proved.
  Its inverse is the **deployment** of X along Y, the real blow-up in the conical setting: Y is replaced by the
  collared link Ṫ. This is the folder's second title.
- The closed-subset Corollary is re-proved; it keeps the extra base points in Y'.

**Collars against cones, and corners (024-029).**
- The product Condition of 025 is re-proved, with one precision: his b) is what stops the cone from rescaling the
  collar coordinate.
- Transversal families of collars, E_J ≃ B_J × I^J (027, canonical), are the compatible collars of a manifold with
  corners.
- Precylindrical stratifications (028) are its face stratifications: bordering faces, transversal collars, Boolean
  intervals. Their local structure is a cube corner (029), checked.
- The infimum claim of 029 holds inside I_{i,j}, where his proof works, and fails read in I. The lens (a disc bounded by
  two arcs meeting at two corners) is precylindrical, satisfies (14) and has no infimum of its two arcs.

**The step of the induction (030).**
- The intersection axiom (14) a) X_i ∩ X_j = ⋃_{α≤i,j} X_α, which he says on 031 he had forgotten, holds; its
  extension to finite intersections is re-proved.
- The germ form of the disjoint-neighbourhood statement needs compactness (a line and an exponentially close curve).

**Slips corrected:** "parties fermées de X" (X^*); Y_i for T̄_i; Ė_J for E_J; X_0 for Ẋ_0; the circular s_k; the
bordering arrows called "verticales"; "k ∈ j".

**Readings decided on the native scan:** Y_i; "globalement" struck; "des récurrences" (021: the boundary datum is
introduced "pour faire des récurrences"); the insertion arrow on 022; Ė_J.

**Open readings:** maximaux|minimaux (028), dans X|des X_i (030), the verb on 025, alors|et (019), 1°|a), σ|F (029).

**EXIT_TOWER (folio 9 = scan 028).**
- A.1 (Boolean intervals only for g = 0 and (1,1)) means that M̄_{g,n}, stratified by isomorphism classes, is not
  precylindrical.
- A.3 (Boolean factorizations of a fixed contraction, and the intersection axiom) means that its deployment is.
- Our register summary of A.1 misstates it (SA10-K150b-13).
<!-- /reading:150_017-030 -->

<!-- reading:axioms_120_121_156 -->
### From the reading of axioms_120_121_156 (sub-agent; the full reading is readings/axioms_120_121_156.md)

**The axiom systems of cotes 120, 121 and 156 against each other** (Claude Opus 5.5 at effort max, aff4deb18a6ec3192, for
a6d42bf6fe2b0d8a8, 19 Nov 2026; full working `readings/axioms_120_121_156.md`). Sources: the readings of cote 120
(ac69efa38b3a951d7), 121/49-73 (mine), 121/1-48 (a9e0641820ca2be57, in progress) and cote 156 (SA21); every correspondence
below was checked on the transcriptions of both sides (16 check events).

**Three kinds of system.** Coordinate families M_n ⊂ P(Rⁿ) (cote 120; 121/054-073); one space with a Boolean family of
subsets (121/004-017; the admissible partitions of 121/049-052); and the pointless figures, contrées and ateliers of 1986
(cote 156). The closed-strata axioms a)-d) of 151/45-52 (1981) link the second and third.
> [19 Nov 2026, sweep 3.5] Bears on line 326: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=184); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=242); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=460). See results_register/horizontal/sweep3_5/SUMMARY.md.

**120 against 121 (coordinate families).**
- 120's M1 + M4 is 121/070's C_* a)-d). 120 adds M2 (inverse images along diagonals) and derives intersections, the axiom
  whose absence leaves 121/070's intersection Proposition unprovable.
- M6 and M7 are 121/061's 6° (zero loci) and 5° (extension). The pushout theorem of 120/013-014 is 121/061-062, and it
  answers the question 121/073 leaves open ("à tirer au clair"). The separation clause of M6 comes, in both cotes, from the
  same products (121/067-068; 120/023-024).
- M11 (x − y, xy, inverses) is the correct form of 121/056's field claim, which fails under 1° and 2° alone.
- The reconstruction of 120/008 needs conservativity and an image axiom (ac69efa38b3a951d7). 121/059 Ⓐ-Ⓑ gives the exact
  form: images along maps mono on the set; all images (M1) correspond to Ⓑ, effective-epi images preserved by the functor.
- Compactness, neighbourhood bases, the sheaf of moderate maps, locally moderate spaces and M8 match 121/071-073.
- At each gap or question of 121/054-073 (intersections, the pushout, the field, the image axiom), 120 has the repaired
  statement. By content, 120 consolidates the 121 drafts; no page is dated.
- None of these systems excludes wild compact sets. Only the triangulation axiom of 121/065 gives finiteness in dimension one.

**One space (121/004-017).** The only system in 120-121 with complements and finitely many components (the ingredients of
o-minimality), on one space only. Its existence theorem (015-017) proves the coarsest admissible decomposition, starting from
the complement of the union of the boundaries: the first open stage that corrects 121/049. Cor 2 of 016 gives coarsest
common refinements. 121/014: finite stratifications are open maps onto finite T₀ spaces.

**Closed strata, 1981-1986.** 121/052 II is 151/45-52 a)-d) plus rarity of proper inclusions; 156-4/2-3's figure is 121/052
> [19 Nov 2026, sweep 3.5] Bears on line 347: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=185); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=243); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=461). See results_register/horizontal/sweep3_5/SUMMARY.md.
II clause by clause, plus non-emptiness (the proviso missing on 052), local compactness, connected manifold strata and a
dimension condition. 156-4/2 places its model explicitly in "un espace modéré … pour une théorie modérée donnée", the
moderate space of 120/020 and 121/072.

**156 against 120-121.**
- **"Contrée modérée" (156-4/70)** is the existence of common subdivisions. It fails in the topological model (a diameter and
  an arc crossing it infinitely often), holds in o-minimal models by the stratification theorem, and is Cor 2 of 121/016 in
  the Boolean setting. It is the common-refinement property of tame geometry, not the Hauptvermutung.
- **The Inf for ≪ (156-5/29)** is the same corollary; 156-4/70's "parfois un inf" fits, because the coarsest decomposition
  of 121 need not have manifold leaves.
- **Intersections (156-3/20)** exist only "en position relative modérée" in 1986; 120 derives them for all pairs and 121/070
  asserts them. So the coordinate systems exclude the non-mutually-tame pairs that 156-3 allows on non-total tronçons.
- **Faithful ateliers (156-9/4):** every atelier built from a 120-121 tame space is faithful, and in 121/004 its supports
  form a Boolean algebra.

**Hunches tested:** H7 confirmed; H2 refined (its identification with the Hauptvermutung refuted); H9-3 confirmed for spatial
models; H5-4's second clause corrected. **Dependencies:** the candidate SA21-13 row is replaced by read rows, with 12 more.
<!-- /reading:axioms_120_121_156 -->

<!-- reading:150_001-016 -->
### From the reading of 150_001-016 (sub-agent; the full reading is readings/150_001-016.md)

Cote 150 opens "Espaces stratifiés et voisinages coniques (ou : déploiement des espaces stratifiés)" (déc. 81): fourteen written pages (006, 011 blank) in three movements.

**1. The deployment (002, 007, 008).** A stratified space over a finite ordered set I is replaced by its deployed strata Σ_i (manifolds with boundary), tubes of raccord Σ_ij and junctions Σ_ijk: one space Σ_d for every flag d of I, contravariant in d. Initial segments give fibrations, cofinal segments bordant inclusions. Two cartesian squares govern the triple pieces: concatenation Σ_ijk = Σ_ij ×_{Σ_j} Σ_jk, and the corner Σ_ijk = Σ_ik ∩ Σ_jk in Σ_k. On 008 three strata become correspondences, and condition a) says exactly that Σ_0 ⨿ Σ_1 ⨿ Σ_2 is an ordered space over [2], the first form of the "Cat-objet" of 042. Slips: 002 l.41 (target Σ_k for Σ_i), 008 l.4, 35, 46.

**2. Stratifications as maps to an ordered set (003-005).** Esp(I), with the up-sets open (@809), is adjoint to the specialization preorder, and a stratification is φ: X → Esp(I). The stratifying partitions with I ordered are exactly the locally finite families of closed sets with 1° (increasing, covering), 2° X_i ∩ X_j = ⋃_{k≤i,j} X_k, 3° X_i^* ≠ ∅ and 4° X_j nowhere dense in X_i. All of it is re-proved here. False on 005: "3° bis with 1° and 2° gives fidelity" (I = {a<b}, X_a = X_b = X). It needs 4° or 3°; the same example refutes 151/57 (4) (SA10-S3-K1). For finite I the quotient condition reduces to a clean form c′), automatic under 4°. M̄_{g,n}, stratified by stable graph type, is strict: 2° is EXIT_TOWER A.3, 4° the irreducibility of closed strata.
> [19 Nov 2026, sweep 3.5] Bears on line 374: SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=328); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=434). See results_register/horizontal/sweep3_5/SUMMARY.md.

**3. Conical neighbourhoods (012-016).** The absolute conical neighbourhood is the mapping cylinder C(f) of f: Ṫ → Y, with the action of the monoid [0,1]; then thickenings, collars, conical subspaces. Three statements need a hypothesis he does not state, that T̊ be open in X (with T̄ closed):
- (8) of 013 for λ near 1;
- "X^* fermé" in (11) of 015;
- the Proposition's c ⇒ b, and Corollary 2 of 015.

One counterexample, a segment with a spur at a frontier point, refutes all three; with the hypothesis, radial reparametrization and the pasting lemma prove them. His repair is the germ definition (015 margin, 022).

**Connections.**
- 002 and 007 supply the corner stones that the successor-pair theorem of 151/69 lacks: 𝒱_ijk and the deployment over all flags (H1, P1).
> [19 Nov 2026, sweep 3.5] Bears on line 384: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=149); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=223); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=344). See results_register/horizontal/sweep3_5/SUMMARY.md.
- The deployed strata pass the (0,4) test that EXIT_TOWER A.11 fails for ordinary strata; 008 takes the whole fibre product, A.13's replacement.
- 004's 1°-2° are 151/45-52 a)-d); 2° is 156-4's frontier condition (SA21-13); Esp(I) is 156-8's Alexandrov topology.
> [19 Nov 2026, sweep 3.5] Bears on line 386: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=186); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=244); INT-SA10-E16 (SA10 intake, confirmed; PROPAGATION.tsv n=462). See results_register/horizontal/sweep3_5/SUMMARY.md.

**State.** 33 check events; 18 corrections (9 slips, 1 precision, 4 readings, 4 refuted and refined); 31 open readings. Ready for an edition with the marks kept, and for translation once the four reading corrections are in and strict|pur (016 l.27) is decided.
<!-- /reading:150_001-016 -->

<!-- reading:150_031-043 -->
### From the reading of 150_031-043 (sub-agent; the full reading is readings/150_031-043.md)

**Cote 150, scans 31-43 (manuscript pages 10-17), read in full, with the second pass of 17 Nov as text.**

**The forgotten axiom (031).**
- 031 ends the transversality begun on 029: the collar of X_{j'} in X_j pulls back to the collar of X_k ∩ X_{j'} in X_k.
- The intersection axiom (0), X_i ∩ X_j = ⋃_{k≤i,j} X_k, is added.
- His NB is re-proved: precylindrical stratifications are equisingular in the strongest sense, because one cube-corner
  chart trivializes the whole family along each stratum.

**The reconstruction and the Théorème (032-035).**
- The strict cone ∐T_β around the minimal strata gives the cut-open data (18).
- X is recovered by (19): X = X^* ∐_Ẋ C(p), and X_i = X_i^* ∪ ⋃_{β<i}(I·Ẋ_{iβ} ∪ X_β). Monotonicity and the
  intersection axiom are re-proved.
- The Théorème (17) ⟺ (18) holds for isomorphisms. It is the découpage of 023 with the Corollary of 024 and the Prop.
  of 026, whose converse is re-proved.
- The order of I records which minimal strata each X_i contains, so the defect of 020 does not return.

**The conical structure (035-038).**
- §8 defines it by recursion on card I: cut out the minimal strata, add their cone boundaries to the collared family,
  and recurse.
- The recursion is well founded and is the full deployment (H150b-1, now on the page).
- Remark 1 (existence) is conjectural; for Whitney stratifications it is the theory of control data.
- Remark 2 (independence of the filtration) is re-proved up to germs. Remark 3 is the stratification by the
  B_J = ∩_{α∈J} B_α over 𝒫(Λ)°.
- 038 announces local cylindrical stratifications, that is, manifolds with corners whose faces are not embedded. This is
  the case of M̄_{g,n}.

**The standard presentation (039-043).** Σ: Drap(I) → M, with:
- (1) last-vertex deletions fibrant;
- (2) other deletions boundary embeddings;
- (3) cartesian concatenation;
- the faces of each Σ_i precylindrical of type Dr(I,i)°.

Re-proved here:
- the Cor. of 039;
- the weakening of (3) in the top note, and the general cartesian square for amalgamated flags;
- the Segal reconstruction from the Σ_i and Σ_{ij};
- the internal category of 041-042, its order object, and the reduction of b) to n = 2.

Wrong as written:
- the reduction of (3) to "longueur 2" fails as he counts length (counterexample I = {h < i < j}); length 1 is right;
- "p = long. d'" on 043 is his slip for p = card d.

**EXIT_TOWER (SA10-C2).**
- His objects are the strata cut open to spaces with boundary. Under that convention M̄_{0,4} satisfies (1)-(2) and
  realizes to S².
- So A.11 refutes the run's raw-face formalization, not his statements.
- A.13 lies outside his hypotheses: graph types fail 028 c).
- A.12 proves the 039 margin condition for M̄_{g,n}.

**A reading reversed.** (20)ⓐ on 033 is "Les Ẋ_β disjoints", decided on the native scan. The second pass's "X_β" of 17
Nov and its notes-check consequence are withdrawn.
<!-- /reading:150_031-043 -->

<!-- reading:150_044-057 -->
### From the reading of 150_044-057 (sub-agent; the full reading is readings/150_044-057.md)

**Cote 150, scans 44-57 (sheets 18-24), read in full** in the second-pass text of 17 Nov. Seven readings were checked
again on the native scan. Claude Opus 5.5 at effort max, 19 Nov; full working in `readings/150_044-057.md`.

**The end of §10 (044 to 048 l.2).** The deployment of 002 is restated as one ordered space Σ_* over I:
- ⓐ the target maps Σ_ij → Σ_j are closed embeddings, so Σ_ii = Σ_i (26) and strict flags map to strict flags (27);
- ⓑ (28) Σ_ijk = Σ_ik ∩ Σ_jk, equivalently (29), the order below a point is induced from I;
- ⓒ disjointness when i, j have no common minorant;
- ⓓ transversality;
- e)-g): fibrations, manifolds with boundary, and the mixed condition. The boundary strata of every Σ_d are indexed by
  the nonempty flags of the ordinal sum of the gaps of d: Boolean intervals, so precylindrical (028).
- The flag consequences drawn from ⓒ in two margins of 045 are refuted by the diamond (N01, @836). They need
  disjointness for noncomparable indices.

**§11, "Digression : où on laisse tomber I" (048-057).**
- ⓐ: a topological ordered set Σ whose target map is a proper, locally bordant immersion, hence finite.
- (32) is formal. For a pushout (31) of ordered sets, the square of strict-flag spaces is cartesian in any ordered space.
  The squares that carry geometry share a final element and are not pushouts; condition b) (33)-(34) is their
  transversality. His example of a pushout is degenerate as written; the concatenation square is meant.
- (34) follows from b) by partial intersections of germs: "on voit … Car", read on the scan.
- b_2) means that the elements below a point form a finite chain. Γ is an augmented semi-simplicial space over Σ.
- (35) is off by one against Γ(d) = Σ^<(d+1).
- **The restart (056-057) separates three kinds of condition:** ⓐ topological, ⓑ set-theoretic (Σ_{≤x} finite and
  totally ordered), ⓒ geometric (transversal germs). Three facts follow from it:
  - Σ_1 is closed by properness;
  - the relative order is continuous automatically, a new re-proof;
  - for a deployment over I, ⓑ is equivalent to (29) plus the disjointness of noncomparable faces. That is the repair of
    045, eight sheets before 065.

**His self-flagged steps:**
- F01, "de = dim ??": right for faces; the manifold clause needs the smooth or PL setting.
- F02, the boundary formula: locally true from b), ⓓ and the corner model.
- F03, "ⓔ conséquence de c) et d)": refuted in Top, where ΣH × ℝ ≅ S⁴ × ℝ for a homology 3-sphere H; true smoothly and in
  PL. So #837 stands for Top.

**Slips:**
- 047, Σ_{d'} for Σ_d: the prime is in the ink;
- 049, the example;
- 055, the index of (35);
- 057, N(x) = card(Σ_{<x}), which the counts require.

**Connections:**
- 151/45-56 (the closed-strata twin);
> [19 Nov 2026, sweep 3.5] Bears on line 491: SA10 intake 2. Item by item l.74 (SA10 intake, refuted; PROPAGATION.tsv n=187); SA10 intake 3. What the run settled, and what tha l.109 (SA10 intake, refuted; PROPAGATION.tsv n=245); SA10 intake 5. Corrections that bear on the trans l.149 (SA10 intake, refuted; PROPAGATION.tsv n=254); and 3 more. See results_register/horizontal/sweep3_5/SUMMARY.md.
- EXIT_TOWER A.13: flags of points are pinned, so the squares are formal;
- Joyce's manifolds with corners: (35) is the order trivialising the 𝔖_d-action.

The open readings are margins and one name, "isotrivialité|équisingularité". 39 check events, 13 corrections.
<!-- /reading:150_044-057 -->

<!-- reading:150_072-084 -->
### From the reading of 150_072-084 (sub-agent; the full reading is readings/150_072-084.md)

**Cote 150, scans 72-84 (his sheets 31v-38), read in full on the second-pass text of 17 Nov; full reading
`readings/150_072-084.md`.**

**The Remarque (072).** The first "déploiement", Σ = ∐X_i with arrows ∐_{X_i⊂X_j} X_i, is 151's half-simplicial space
(s étale, b a closed immersion), re-proved; the second is the deployment of cote 150 (b bordant). The margin's "c) follows
from a), b)" needs manifold components and s locally trivial.

**§14, the deployed strata cut out by tubes (073-076).** Σ_i = X_i ∖ T̊_{<i}, Σ_{ij} = Ṫ_i ∩ Σ_j, and over flags
Σ_{i_0…i_n} = Ṫ_{i_0} ∩ … ∩ Ṫ_{i_{n−1}} ∩ Σ_{i_n}, made coherent by a dimension function and the filtration
X^{(d)} = X − ⋃_{α<d} T̊_α.
- Cofinal deletions are inclusions and the other deletions go through retractions: 039's standard presentation, built
  concretely.
- With Mather's control on the retractions, the cartesian square (3) of 040 is re-proved.
- Refined: Σ_{ij} ⊂ Σ_j needs T'_{ij} to be the trace of T_i (a smaller tube fails); (49) has the slip X_{(d)} for
  X^{(d)} and needs admissible tubes; closedness needs T̊ open (H150a-3).

**§15, pro-neighbourhoods (077-084).** V_i ≃ X_i^*; V_i ∩ V_j = ∅ for incomparable strata exactly under his "ouverts
normaux" (hereditary normality); X is the colimit of the V_i along the V_{ij} level by level, and of the V_d over
Drap(I)^op, so the corner pieces that refute 151/069 are present.
> [19 Nov 2026, sweep 3.5] Bears on line 519: SA10 intake 2. Item by item l.71 (SA10 intake, refuted; PROPAGATION.tsv n=150); SA10 intake 3. What the run settled, and what tha l.106 (SA10 intake, refuted; PROPAGATION.tsv n=224); SA10 intake 1. The main question (A.1): what glue l.62 (SA10 intake, reading; PROPAGATION.tsv n=345). See results_register/horizontal/sweep3_5/SUMMARY.md.
- Relative versions need Z a union of strata (counterexample Z = {0} ∪ {1/n}).
- Ideals and bands are the closed and locally closed subsets of Esp(I); V_J and the raccords V_J^L = V_J ∩ X_L^* reduce to
  J ≺ L.
- The band Lemma is re-proved, its struck 3° shown redundant.
- In X' = X^*_{I'}, X'_J is closed and X'_L open. The margin (69), V_J^L ↪ V_J ∩ V_L an equivalence for J ≺ L, is
  re-proved under control and fails without domination. With J = {i}, L = {j} it answers his question of 077.
- (70) row 2 is exact only for J ∩ L = ∅; (71)-(72) are a correct intersection-stable cover, and (73) its spectral
  sequence for I finite.

**H4 refuted.** "Str_∞ p. 84" (151/059) is "Structure à l'infini des M_{g,ν}" (cote 147), his p. 84 = scan 147/177, with
> [19 Nov 2026, sweep 3.5] Bears on line 529: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=209); SA10 intake 1. The main question (A.1): what glue l.35 (SA10 intake, reading; PROPAGATION.tsv n=329); INT-SA10-E03 (SA10 intake, confirmed; PROPAGATION.tsv n=435). See results_register/horizontal/sweep3_5/SUMMARY.md.
(292)-(294) on 147/176 (scans viewed). Cote 150 §15 is the general form of those normal-crossings pieces, and its
> [19 Nov 2026, sweep 3.5] Bears on line 530: SA10 intake 2. Item by item l.84 (SA10 intake, refuted; PROPAGATION.tsv n=210). See results_register/horizontal/sweep3_5/SUMMARY.md.
comparison map is canonical where (294)'s is not.

**Counts:** 36 check events (SA10-R150f-01 to 36), 15 corrections (SA10-K150f-01 to 15), 125 \unsure marks; five
consequential readings open.
<!-- /reading:150_072-084 -->

<!-- reading:150_058-071 -->
### From the reading of 150_058-071 (sub-agent; the full reading is readings/150_058-071.md)

**Cote 150, scans 58-71, read in full** in my second-pass text of 17 Nov (Claude Opus 5.5 at effort max, 19 Nov);
five places re-rendered from the PDF. Full working: `readings/150_058-071.md`.

**§11 ends (058-064): the order recovered.**
- The relative order of 056-057 gives only the cofinal faces b, b′, s′ (the décalage of the nerve). (36) adds the
  source s = p₁. (38) asks for p₂ with b p₂ = s b′ and p₁ p₂ = p₁ s′, the first square cartesian, p₁ transversal to b.
- **Re-proved:** p₂ is unique; ≺ is a strict order (060); the corrected face maps; the Scholie is equivalent to a
  separated ordered space with chains Σ_{<x}, b a proper immersion, transversal bordant germs, s transversal to b.
- **(40):** p and b′ are base changes; transversality is what makes b′ bordant. The upper "cart" holds only on the
  ordered half (K06).
- **His margins:**
  - 062 (transversality redundant) is true under equisingularity in any category, false without it;
  - 063 (the mixed case from 1° and 2°) is false in Top (ΣH × ℝ, as for 051), true in PL and smoothly.

**§12, the Récapitulation (065-067).**
- **c) is written b_ij^{-1}; s_jk^{-1} is meant (K01).** It is Mather's ρ-control.
- **(41) is not commutative "donc", and 066's claim that a)-c) give an order is false.**
  - Twisting s_02 by a homeomorphism of Σ_0 keeps every condition and breaks transitivity (K02).
  - The missing axiom, s_ik = s_ij∘s_jk on Σ_ijk, is (38)'s p₁p₂ = p₁s′, Mather's π-control. The functor on Drap(I) of
    039-043 had it by functoriality. With it, 066 holds.
- **Slips:** Σ_j ↪ Σ_ji (K03); the label b_ik (K04); the mixed case's map, meant s_ik: Σ_ik → Σ_i, whose target's j
  is struck on the native scan (K10), as on 002 l.41.
- **The 067 margin** (faces Σ_ij are manifolds with boundary) is false in Top, true in PL and smoothly.

**§13 (067-071): the topological category.**
- π₀(Σ_(0)) is a preorder. The Lemma, re-proved, works with s or b fibrant, so the switch is harmless (K11). φ̲: Σ̲ → I
  is universal.
- 069: δ is open and closed. Σ*_ii = ∅ by dimension needs pure dimension (K12): the block's first need for the
  "topologie modérée" of 073.
- 070: I is ordered under d). The "mono" hypothesis is redundant, against the first pass's N07 (K17).
- 071: b) is proved ("x et y" stands for x_i, x_j). With K02's axiom the Conséquence holds: equisingular deployments
  over I are the Scholie's ordered spaces with 1°), plus a strictly increasing map π₀(Σ) → I.
- **With s fibrant, the nerve of Σ̲ is a Segal space** whose mapping spaces are the homotopy fibres of (s,b). For
  (S², p), Map(p,u) ≃ S¹ and BΣ̲ ≅ S², while π₀ gives [1], the Remords' loss. For two strata, BΣ̲ ≅ X by 023.

**Counts:** 35 check events, 18 corrections, 77 doubt marks. Open readings: 067 l.18-21, 065 l.16, 066 l.27, 070 l.25.
<!-- /reading:150_058-071 -->

<!-- reading:150_085-099 -->
### From the reading of 150_085-099 (sub-agent; the full reading is readings/150_085-099.md)

Scans 085-099 of cote 150 are two pieces of his 1981-82 notes on stratified spaces, sheets 39-46 of his numbering.

**§16 (085-088) builds the deployed side of §15's pro-neighbourhoods.** For a band J:
- Σ_J is X_J^* minus the open tubes of the strata below J (70). It is closed in X, a homotopy model of X_J^* (73), and
  glued from the Σ_j along the Σ_ij (72).
- Its boundary is Σ̇_J (74).
- The tube of Σ_J in a larger band Σ_{I'} is (75)-(76).
- The band pieces Σ^♭_{J,L} = Ṫ ∩ Σ_L have their flag colimit (77)-(78) and the span Σ_J ← Σ^♭_{J,L} → Σ_L (79).

A margin proposes the "éclatés orientés", with Σ_i ⊃ X_i^*. The Remarque of 088 claims that Σ_{J,L} ↪ Σ_L is intrinsic up
to isotopy in tame topology.

**§17 (089-099) is a clean restart.**
- It puts the Alexandrov topology on I (closed = down-sets). Bands are its locally closed parts (= order-convex), with the
  domination J ≺ K.
- It states (Strat 1)-(Strat 5).
- It proves:
  - the open strata partition X;
  - the spectral sequence of the closed cover (89);
  - the criteria (95)-(96) for neighbourhoods of strata to meet.
- It sets out V_i, V_d, V^Z, V_J, V_{J,L}, V_J^L and V_{J_0…J_n} with their union and colimit formulas.

**The reading re-derived 44 steps (SA10-R150g-01 to -44).**
- "Rare" in (Strat 5) means nowhere dense, as on 004. The dense faithful stratifications are exactly the locally finite
  partitions with the frontier condition, I being the closure order (R150g-22 to -27).
- For a chain I, the bands under ≺ are the arrow poset Ar(I) (R150g-19).
- **His "? à vérifier!" on (100) is justified.** Z = {0} ∪ {1/n} in ℝ refutes it, and the same Z refutes (104).
  - Both hold for Z a locally closed union of strata, under control.
  - (110) needs that form; (111), with Z = X_L^*, holds (K150g-08, -11).
- (74)'s second and third lines index the interior seams, not the boundary (K150g-01).
- The parenthetical of (75) is false, as his own margin says (K150g-03).
- (96) ⟸ needs density (K150g-07).
- (103) holds for bands only (K150g-10).

**Corrections (K150g-01 to -16), 16 in all:**
- four refutations or confirmed self-doubts, each with its refined statement;
- three precisions of hypotheses;
- three readings decided by the mathematics;
- three slips;
- one notation proposal (♭ = the trace on the top open stratum);
- one immaterial reading;
- one typesetting error in the 17 Nov second-pass file. 087 l.5 reads "\qquadT", which does not compile; it must be fixed
  in the second-pass folder before any build.

**Open:**
- (100)/(110) in the control-free tame setting;
- the Remarque's isotopy invariance;
- five readings for the native scans:
  - 085 l.52;
  - the 086 margin's subscript;
  - the ♭ glyphs;
  - 085's head line;
  - 088's "le cas équisingulier".
<!-- /reading:150_085-099 -->

<!-- reading:151_001-017 -->
### From the reading of 151_001-017 (sub-agent; the full reading is readings/151_001-017.md)

**Cote 151, scans 1-17** (Claude Opus 5.5 at effort max; 31 check events, 14 corrections; full reading
`readings/151_001-017.md`).

**What the block is.**
- **002 is his plan of "Structures stratifiées".** Its start pages 1, 10, 16, 23 are the sheets where §1-§4 begin
  (151/027, 045, 057, 070), so it was written after sheet 23. The struck "Strat" is the heading of 057.
- **The rest is a later layer.** 003-009 are on the backs of copies of a letter dated 6 December 1990, and 009 and 018 on
  its letterhead. 018 continues both 015 and 017. So 151/003-025 dates from 1990-91, the time of *Les Dérivateurs*. It
  returns to what §1 needs, the homotopy type of a topos (151/032 "cf Artin-Mazur", the van Kampen of 151/043), and does
> [19 Nov 2026, sweep 3.5] Bears on line 647: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=130). See results_register/horizontal/sweep3_5/SUMMARY.md.
  not underlie it.

**003-009: π₀-systems of Čech nerves.**
- E₀, E₁, E₂ with 𝔖₂ and 𝔖₃ are the Čech nerve truncated at level 2 (Michel Hua's project).
- His relations hold in the model, except the boxed σ₃δ₁ = δ₁ of 003, which his own 005 and 007 correct to σ₁δ₁ = δ₁.
- The two "global" boxes of 005 are independent relations (models M1, M2): the 𝔖₃-invariance of δ₁δ₀, and
  p₀p₁₂σ₁ = p₀p₁₂.
- 009 is the edge-path presentation of π₁, with one relation per 𝔖₃-orbit (re-proved). Its claim that σ₁-fixed points
  are degenerate holds for tuple systems and Galois coverings, and fails for an 𝔖₃ covering of degree 3.
- E₂(α) is defined as π₀(F_α ×_F F_α).

**011-015: "Hyperrecouvrements".**
- A functor φ: A → 𝒳 from an arbitrary small A, motivated by "le yoga « Cechiste »" and its refinement "suggéré par
  Cartier".
- Re-proved: Hyp 1′ is tautological; the induction for Hyp 2; a)-c) ⟺ Hyp 1, 2, 2′; the left-exact case (Diaconescu)
  and its converse; b) ⇒ b′) and c) ⇒ c′), the latter by shortening zigzags.
- **His "forme équivalente" is false** (#g673; A = BC₂). What is true: Hyp 1, 2, 2′ ⟺ (Hyp) for finite diagrams indexed by
  finite forests. The full (Hyp) needs the parallel pair as well, and is then left exactness (two-cone argument; Shulman
  2012).
- So his closing question has the answer no, and "I = •" should be ∅.
- The gap matters: the symmetric nerve of a group satisfies Hyp 1, 2, 2′ and realizes to BG. These hypotheses do not
  give descent, and (Hyp) gives only flat systems.

**017: the finite sets 𝔼_n with δ_n, K_n and 𝔖_n.**
- The margin defines δ_nK_n as the projection p_{n+1}: idempotent, not the circular ρ_{n+1}.
- (**) is exactly Hyp 2 for A = (finite sets)^op, the product being given by the coproduct injections α, β. So 017 is
  the punctual case of 011-015.
- Its flat systems are the tuple systems S^n.
- (*) is not a complete presentation: it omits 005's two global relations (counter-model).
- The index of ρ clashes on the page.

**Connections:** H2, SA10-8, Les Dérivateurs, Artin-Mazur, SGA 4 V §7.
<!-- /reading:151_001-017 -->

<!-- reading:151_018-031 -->
### From the reading of 151_018-031 (sub-agent; the full reading is readings/151_018-031.md)

**Cote 151, scans 18-31, read in full** in my second-pass text of 17 Nov (Claude Opus 5.5 at effort max, 19 Nov);
native images checked on 020, 023, 025. Full working: `readings/151_018-031.md`.

**018** is a cancelled draft of the product step of "Hyperrecouvrements" (014-015): φ_! preserves products if it does
so on representables, by universal colimits (re-proved).

**019-025 (his pages ② to ⑦): the finite-set system of 017 in degree 3.**
- 019 lists five types of condition (I concatenation, II-V squares of δ's and K's), with consistent counts per degree.
- 020 writes out the degree-3 conditions, épi maps and two "cart" squares, and asks "iso ???" of X_2 → X_1 × X_1.
- **Decided on the native image:** the top arrows of the first square (020) and of (*) (025) are the degeneracy
  X_2 ↪ X_3, not maps X_3 → X_2, so the squares are the images of the E-squares beside them (E04 withdrawn).
- **With X_1 a point, re-proved:**
  - the five relations, pρd = c being the pointed form of pρd = δ_0p_1;
  - the lemma on the translates ρ^i d(ζ);
  - the orbit decomposition X'_3 = {e_3} ⊔ 𝔖_3 ∧_{1,σ_1} X_2^*;
  - the image Σ of (p, pρ), and the criterion |X_2| ≤ 2.
- **The two squares:**
  - (*) is cartesian for every system (an Eilenberg-Zilber-type identity), not only for card X_1 = 1.
  - (**) is a real axiom; it forces p^*(X_3^*) ⊂ X_2^*, so p^* is never onto (the single arrowhead).
- **Slips:**
  - ρσ_iρ^{-1} = σ_{i−1} under his composition, not σ_{i+1};
  - the second case on 025 reads "i=1" in the ink; 2 is meant.
- **What the system is:**
  - "iso ???" is answered in the negative by the nerve of ℤ/2, the page's own case.
  - A 3-sheeted cover with monodromy 𝔖_3 shows that |X_2| = 2 does not force X_3 = X'_3.
  - With 009's group relations, the system reads as the π₀ shadow of a Čech or hypercovering nerve.

**027-031: "Structures stratifiées" §1, pp. 1-3.**
- **The provisional germ collapses for paracompact X.** The topos limit of the open neighbourhoods is Sh(Y), and the
  punctured germ is empty. The pro-object (cote 150 §15) or a non-T₁ site (Zariski, étale) keeps the content.
- **His margin Y ≃ 𝒱** holds in shape, and as a homotopy equivalence for tame Y.
- **"Z^* a manifold" fails in Top** (Bing's dogbone) and holds in PL and smoothly, under the moderation he names.
- **The span (7)** glues X back for honest neighbourhoods.
- **Van Kampen:**
  - (8) holds without connectivity (Brown).
  - (9) needs 𝒱^* connected (X = S¹ with a point refutes it as stated); 151/33's connected link supplies it.
  - "extérieurement" and the path-class margin are right.
- **Into 032:** local triviality makes 𝒱^* → Y a fibration with fibre the link, which is (11) of 151/32.

**Counts:**
- 32 check events (SA10-R151b-01 to 32) and 11 corrections (SA10-K151b-01 to 11);
- doubt marks 192 → 191 after the fold-in.
<!-- /reading:151_018-031 -->
