# RESEARCH_SA10: Grothendieck's stratified spaces and stratified topos of 1981 (cotes 150-151): the gluing of tubes and the stratified homotopy hypothesis

**To be settled, in three Parts:**
- **A.** The correct form of his "Théorème de recollement des tubes" (151/069), which is false as he stated it. A.1 is the main question.
- **B.** His homotopy theory of stratified spaces at its first levels: the locally constant sheaves, the gerbes, and his principle that the homotopy type of a glued topos is the colimit of the homotopy types.
- **C.** The questions that the reading of cote 150 leaves open.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA10`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA10_study.zip`: our study of cotes 150-152 and 120.**
  - `study/STUDY.md`, with cote 151, scans 32-75, read in full.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the readings of cote 150 by blocks, and the comparison of the axiom systems of cotes 120, 121 and 156.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the topic's items SA10-1 to SA10-19.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA10_transcriptions.zip`: the transcriptions of cotes 150 and 151 (LaTeX), one file per scan.**
  - The first pass was by GPT-6 Astra (ChatGPT Pro mode). The second pass corrected it against the scans on 17 Nov 2026, by Claude Opus 5.5 at effort max, with change logs and notes checks.
  - The first pass's notes and doubt tables are included.
  - The scan number N is the PDF page of the cote; the archive's pencil page is N−1.
  - The transcriptions carry `\unsure{a|b}` marks. Where a step of yours depends on a doubtful reading, say so.
- Fetch the literature yourself. It is listed under "Sources" below.

## Where this comes from

**The pages.**
- **Cote 151 (1981): his stratified topos.**
  - §1, the two-stratum case Y ⊂ X with its tube V_{Y,X} and deleted tube V*_{Y,X}.
  - §2, global stratifications (X_i)_{i∈I} indexed by an ordered set, with their half-simplicial space of flags.
  - §3, the tubes V_{ij}, V*_{ij} and V^j_{i,k}, which he calls the "pierres", and the gluing theorem.
  - §4, the canonical topoi.
- **Cote 150:** stratifications, conical neighbourhoods and collars, and the reconstruction of a stratified space from its strata and gluing data, with flags and pro-neighbourhoods of strata.

**Our reading.**
- Sweep 3 read 151/32-75 in full (a6d42bf6). Sweep-3 readers read cote 150 by blocks; their readings are attached.
- One research run, EXIT_TOWER (GPT-6 Astra, ChatGPT Pro mode), studied cote 150, folios 9 and 15-16. Its statements A.1-A.3 and A.12 are proved, and A.11 and A.13 are refuted. They appear in the attached map under SA10-C1 and SA10-C2.

**A separate prompt, RESEARCH_SA20,** asks for his collars and tubular neighbourhoods of 119/148-153, his axioms of cotes 120-121 against o-minimality, and the gluing of 121/039-047. Those are not asked here.

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA10-C3-14, SA10-S3-K3).** His "Th. de recollement des tubes (1ère version)" (151/069) is false as stated.
  - **The statement:** X is the colimit, in the 2-category of topoi, of the diagram Ĩ of the X_i*, V_{ij} and V*_{ij}, for j a successor of i.
  - **The counterexample:** X = ℂ, with X_0 = {0}, X_1 = ℝ, X_2 = ℂ. The 2-limit of the sheaf categories of the stones contains an object that comes from no sheaf on ℂ. Its generization from the positive ray into the upper half-plane is * ↦ 1, and from the negative ray it is * ↦ 2.
  - **Where it fails:** the successor stones never see the germ of X_2 along X_0.
  - **His own remarks point at the gap:** on 151/059 the stones are "côtes mal taillées", not enough for the pieces V^{d′}_{d,d″} ≃ Ñ | D* of "Str_∞ p. 84". That is cote 147, "Structure à l'infini des M_{g,ν}", whose pieces (292)-(294) are on 147/176, and whose general form, with a canonical comparison map, is §15 of cote 150 (scans 72-84); in the margin of 151/072 he warns that restriction to opens does not commute with the "limit" topoi.
- **R2 (SA10-C3-01 to -03).** Under his axioms a)-d), lim→ X_{Δ*} → X is a homeomorphism (151/52, (22)).
  - **The axioms:** the X_i are closed and locally finite; i ≤ j ⇒ X_i ⊂ X_j; X = ⋃X_i; X_i ∩ X_j = ⋃_{k≤i,j} X_k.
  - The open strata X_i* = X_i ∖ Ẋ_i partition X (151/55).
- **R3 (SA10-C3-08, SA10-S3-K1).** (4) of 151/057, R_i ∩ X_i = Ẋ_i, needs X_i* ≠ ∅. Under that, (5)-(8) and (12)-(13) of 151/57-60 hold (SA10-C3-09 to -11), and the aside "(R_{j,k} ∩ S_{j,k} = Ẋ_i)" is false in general (SA10-S3-K2).
- **R4 (SA10-C3-04).** The inertia-decomposition sequence (14) of 151/34, 1 → π₁(V*_{z,Z}) → π₁(V*_{Y,X}) → π₁(Y) → 1, holds under his hypotheses: connected link, and π₂(Y) → π₁(link) zero. If Y and the link are K(π,1), so is V*_{Y,X} (15).
- **R5 (SA10-C3-05 to -07).** His two examples hold.
  - For X = ℂ ⊃ {0}, the category 𝓕 of sheaves locally constant on the strata is Ĉ, which is contractible.
  - For X = ℙ¹ ⊃ {∞}, 𝓕 is again contractible while X = S² is not. So X → 𝓕 is not a homotopy equivalence.
  - Gluing A-gerbes gives H²(S², A) ≅ A, his "magnifique succès !".
- **R7 (cote 150 readings, round 2: SA10-R150a to -R150f, SA10-K150a to -K150f).** These are the readings of cote 150 by blocks.
  - **The one-stratum "déploiement" (150/023)** is re-proved for isomorphisms: a real blow-up in the conical setting. His "précylindrique" stratifications are the face stratifications of manifolds with corners (150/027-029).
  - **The reconstruction (19) and the Théorème of 150/035** are re-proved for isomorphisms, together with the converse of 026.
  - **The Récapitulation of 150/065-066 lacks an axiom.** As written, its a)-c) do not define an order: twist s_02 by a homeomorphism of Σ_0. The missing axiom is s_ik = s_ij ∘ s_jk, which is Mather's π-control. Its c) is ρ-control.
  - **The margin (69) of 150/083** holds under Mather's control condition for J ≺ L and fails without domination. Its claim is that V_J^L ↪ V_J ∩ V_L is a homotopy equivalence.
  - **His "probably a consequence" margins are false in plain topology** (ΣH × ℝ ≅ S⁴ × ℝ, with H a homology 3-sphere) and hold in PL and smoothly: 150/051, (e) from c) and d); and 063 and 067. 062 holds under equisingularity.
  - **§13:** his "s fibrant" makes the nerve a Segal space whose mapping spaces are the links. For (S², p) the realization gives S², while π₀ gives a two-element poset.
  - **The refutations of EXIT_TOWER A.11 and A.13** concern that run's formalization, not his folios 15-16. By 150/039 his objects are strata cut open along the lower ones. Under that convention M̄_{0,4} satisfies his conditions and realizes to S² (SA10-K150c-15).
  - **"Str_∞ p. 84" (151/059) is cote 147,** "Structure à l'infini des M_{g,ν}" (147/176-177). §15 of cote 150 is the general form of its pieces (292)-(294), with a canonical comparison map.
- **R8 (cote 151, scans 1-31, round 2: SA10-R151a, -R151b, SA10-K151a, -K151b).**
  - **The provisional germ of 151/028 collapses.** Defined as the topos limit of the open neighbourhoods of Y, it is Sh(Y) for paracompact X, with empty punctured part. Tubes and deleted tubes must be taken as pro-objects (cote 150 §15) or on étale and Zariski sites.
  - **(9) of 151/031 needs a connected link,** which 151/033 assumes.
  - **151/003-025 is a layer written in 1990-91,** on paper dated 6 Dec 1990, around the homotopy type of a topos. His "forme équivalente" (Hyp) there is false. Hyp 1, 2 and 2′ hold exactly for forest-shaped diagrams, and the symmetric nerve of a group satisfies them and realizes to BG.
- **R6 (SA10-C3-15, SA10-S3-K4).** On 151/070 the axiom (1 d) is written with a strict "<". This is his slip, read the same way by the second pass; 151/052 and 151/057 have ≤.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** For conically stratified spaces (Thom-Mather, or conically smooth), X is the colimit of the stones of *all* pairs i < k with their inclusions. Equivalently, X is reached by iterated gluing along the deepest stratum, which is the "unzipping" of Ayala, Francis and Tanaka.
- **L2.** His "locale trivialité normale homotopique" (151/32, (11)) is Quinn's condition on homotopy links (homotopically stratified sets, 1988). Under it, his van Kampen principle for topos colimits (151/43) holds.
- **L3.** The two levels match the exit-path theory:
  - 𝓕 (151/35) is the category of representations of the exit-path category truncated at π₁ of the links;
  - the gerbe gluing (151/41-43) is Treumann's exit-path 2-category;
  - the full statement is the exit-path ∞-category.
- **L4.** The strengthened condition of 151/54, that strata with a common lower stratum have an infimum, fails for the stratification of M̄_{g,n} outside small (g, n) (EXIT_TOWER A.2). So his refusal of it (151/54) is forced by his own programme (151/44).

## What the outcome must be

{{OUTCOME}}

## Parts

**A. The gluing of tubes. The main question is A.1.**
- **A.1 (main).** Determine the correct form of the gluing theorem of 151/069.
  - **The setting:** a space X with a stratification (X_i)_{i∈I} satisfying a)-d) (R2), with tubular neighbourhoods. The tubes are taken as pro-objects of open sets (pro-topoi), not as topos limits, which collapse (R8).
  - **To determine:** which diagram of stones has X, that is Sh(X), as its colimit in the 2-category of topoi. The candidates are his V_{ij}, V*_{ij} and V^j_{i,k} (151/57-61) for all pairs or triples, with all their inclusions.
  - **Under which hypotheses:** Thom-Mather, conically smooth, or homotopically stratified.
  - **To prove:**
    - the theorem itself;
    - that the successor-pair version is false, verifying R1;
    - the minimality of the diagram, with a counterexample for each piece left out.
  - Compare it with the unzipping of Ayala-Francis-Tanaka and with the recollement of SGA 4, Exposé IV §9 (L1).
- **A.2.** His formal property of tubes (151/71): the formation of tubes commutes with inverse images along proper local immersions and open immersions.
  - Prove it under exact hypotheses, or refute it.
  - Settle his own retracted claim (151/72) that the proof of the gluing theorem is local on X.
- **A.3.** For cribles I″ ⊂ I′ of I (151/72-75), determine whether the stones of the induced stratification of U_{I′,I″} = X_{I′} ∖ X_{I″} are homotopy equivalent to the stones of X. Determine whether the constructible sheaves on X_{I′} and on U_{I′,I″} compare as he hopes.
- **A.4.** The Corollary of 151/52-53 ("sauf erreur"): for I finite with infima, X is the colimit of the X_i, X = X_{Δ0}/(X_{Δ1} ⇉), and the X_i → X are closed immersions. Prove it or refute it.
  - Determine the class of stratifications satisfying his strengthened condition (24) of 151/54.
  - Settle L4 against EXIT_TOWER A.2.

**B. The stratified homotopy hypothesis at its first levels.**
- **B.1.** For Y ⊂ X closed with tube V_{Y,X} and deleted tube V*_{Y,X}, determine the exact hypotheses under which 𝓕 is equivalent to the systems (E_{X*}, E_{Y,X}; φ) of (17)-(18 bis) (151/35-36), and prove the equivalence.
  - 𝓕 is the category of sheaves locally constant on X* and on Y.
  - He writes that this holds "indépendamment de toute hypothèse ... de locale trivialité normale". Decide whether that is true.
- **B.2.** State his van Kampen principle (151/43) precisely, for the gluings of A.1, with the shape of a topos. Prove it under L2's hypothesis, or refute it with the exact failure, and recover R5 from it.
  - **The principle:** "le type d'homotopie d'une Lim→ de Topos (Topos 'recollé') est la Lim→ des types d'homotopie".
- **B.3.** Settle L3.
  - Prove that, on a conically stratified space, the constructible stacks of groupoids are the 2-functors on the exit-path 2-category, in the form of his gerbe gluing (151/41-43).
  - Derive H²(S², A) = A from it.
  - State and prove the general truncation level by induction on the number of strata.
- **B.4.** The K(π,1) programme (151/33-34, 44): suppose the strata and the links of a stratified space are K(π,1). Determine what data beyond the diagram (8)/(10) of fundamental groupoids determine the homotopy type of X, and prove it. R5 shows that the 1-truncated diagram does not suffice.

- **B.5 (151/011-018, his layer of 1990-91).** Let φ: A → 𝒳 be a functor from a small category to a topos.
  - Determine the conditions on the comparison maps φ_!(lim F_i) → lim φ_!(F_i) under which the homotopy colimit of the U_α models the homotopy type of 𝒳 in the sense of Artin-Mazur. Prove they suffice, and that weaker ones do not.
  - Compare them with Verdier's hypercoverings (A = Δ^op) and with the symmetric case A = (finite sets)^op.
  - **Known on the page and in our reading:**
    - his Hyp 1, 2 and 2′ are equivalent to epi comparisons for forest-shaped finite diagrams;
    - the full (Hyp) is left exactness;
    - the symmetric nerve of a group satisfies Hyp 1, 2 and 2′ and realizes to BG.
- **B.6.** Decide whether (a)-(d) of 151/017, with the two global relations he boxed on 151/005, present the category of non-empty finite sets. Decide whether the low-degree list of 151/003-005 presents its truncation at three elements.

**C. Cote 150: the deployment, the presentation, and the control data.**
- **C.1.** For a stratified space with his conical structure (150, §8), build Σ: Drap(I) → Top with (1)-(3) and a)-c) of 150/039-043.
  - Prove that X is the colimit of the simultaneous mapping cones C_{Σ,d,d′} of 150/043 along their transition maps. He postpones this construction on 043.
  - Prove that Σ_• is a complete Segal space equivalent to the exit-path ∞-category.
  - Give the version over the incidence category of strata for M̄_{g,n}.
  - Relate the result to A.1.
- **C.2.** Prove that the Récapitulation of 150/065-066, completed by π-control (s_ik = s_ij ∘ s_jk on Σ_ijk), is equivalent to Thom-Mather control data in deployed form, at a level ε of the tubular functions. Verify the counterexample to the uncompleted form (R7).
- **C.3.** Determine when iterating the "découpage cônique" of 150/023, keeping the boundaries (150/021, 030), produces a precylindrical stratification (150/028 a)-c), (14)), that is, a manifold with corners.
  - Determine what indexes its faces: the poset of strata, its flags, or the category of strata and incidences.
  - For M̄_{g,n}, decide whether the real oriented blow-up of the boundary is precylindrical once indexed by fixed contractions.
- **C.4.** For Whitney, Thom-Mather or homotopically stratified spaces, prove:
  - (51), and (56)-(57) for unions of strata;
  - the margin (69) for J ≺ L;
  - the agreement V_d ≃ Σ_d;
  - the cover spectral sequence (73) of 150/073-084.

  Then identify V_J^L with the homotopy link, and derive 147/176's (294) canonically for normal crossings.
- **C.5.** Settle each of his "probably a consequence" margins (150/051, 062, 063, 067, 070-071) in each of TOP, PL and smooth, with a proof or a counterexample in each.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- D. Ayala, J. Francis, H. L. Tanaka, "Local structures on stratified spaces", Adv. Math. 307 (2017), arXiv:1409.0501.
- D. Treumann, "Exit paths and constructible stacks", Compositio Math. 145 (2009), arXiv:0708.0659.
- J. Lurie, *Higher Algebra*, Appendix A (A.5-A.9).
- C. Barwick, S. Glasman, P. Haine, "Exodromy", arXiv:1807.03281.
- P. Haine, "On the homotopy theory of stratified spaces", arXiv:1811.01119.
- J. Woolf, "The fundamental category of a stratified space", arXiv:0811.2580.
- F. Quinn, "Homotopically stratified sets", J. Amer. Math. Soc. 1 (1988).
- J. Mather, "Notes on topological stability" (1970; Bull. AMS 2012).
- M. Goresky and R. MacPherson, *Stratified Morse theory* (1988).
- SGA 4, Exposé IV §9 (recollement).

(arXiv numbers given from memory: check them.)

{{RULES}}

{{DELIVER}}
