**The attached files.** Besides this file there is one ZIP, `SA10_Stratified_spaces_cotes_150-151_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA10_broad.zip` is the folder `RESEARCH_SA10_broad/`), so there is nothing more to unpack; every other file is at the top level under its own name.

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

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for every dimension
proved in low dimension without saying so; a step that replaces a claim by a convenient special case without naming
it; a reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made
and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA10_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

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

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the axioms assumed, the class of structures, finiteness and dimension
   hypotheses). Do not replace it by a convenient special case. If you prove a special case, name it as one and keep
   the general statement on your list.
2. Type every map and relation you introduce: source, target, the category or ordered set in which it lives, and each
   extra property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "refine to") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories or of topoi; homotopy
   equivalence; weak equivalence of a specified map; an isomorphism of lattices against an isomorphism of ordered sets.
5. Check the edge cases in scope: empty strata and empty figures; one stratum; disconnected strata; infinite and
   non-locally-finite families; dimension 0, 1 and 2; the non-faithful and the non-divisible cases.
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.

## What to deliver

One ZIP containing:
- `RESEARCH_SA10_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA10_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA10_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA10_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
  statement number); then what you read, what you computed (every program with its scope, counts and run time), and
  every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry ids such as SA21-R8-25; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA10_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
