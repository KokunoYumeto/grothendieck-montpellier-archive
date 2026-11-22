**The attached files.** Besides this file there is one ZIP, `SA20_Esquisse_cotes_121-125_155_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA20_literature.zip` is the folder `RESEARCH_SA20_literature/`), so there is nothing more to unpack; every other file is at the top level under its own name.

**The same files in this Space.** Every file of `SA20_Esquisse_cotes_121-125_155_night.zip` may also be in this Space's files, flat, each named `P011__` followed by its file name; `P011__SPACE_INDEX.tsv` gives, for each such name, its path inside the ZIP. Where they are there, use them as you would the unpacked ZIP; where a Space file and the ZIP differ, the ZIP decides; where they are not there, unpack the ZIP.

# RESEARCH_SA20: Grothendieck's notes around the Esquisse d'un programme (cotes 119-123, 125, 152, 153, 155): collars and tame topology, a Tannakian duality over k′/k, the Milnor fibre, and the letter to Kostant

**What is to be settled, in five Parts:**
- **A.** Collars, cones and tame topology (119/148-153, cotes 120 and 121): his collar conjecture and the cascade of categories in the o-minimal setting, his axioms against o-minimality, the reconstruction of a tame theory from its category, and his canonical partitions. A.1 is the main question.
- **B.** Cote 155: tensor categories with a fibre functor to finite k′-modules as bialgebroids over k′. Cote 153: the "analysers" as plethories.
- **C.** Cote 122: the variation, its sign, and the vanishing of H^{n-1} of the Milnor fibre within his framework. Cote 125: his duality criterion for the cohomological dimension of a complement.
- **D.** Cote 123: the simultaneous resolution over a base, the letter to Kostant of 22 October 1969 and its dimension formula, and the Weyl-group computations his questions ask for.
- **E.** The finite geometry of 119/155-161 and the plane trees of cote 152.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA20`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent ae4ae3dc17acaa440, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA20_study.zip`: our study of the topic.**
  - `study/STUDY.md`. Its head gives the state of every section and the main findings; then one section per cote, in the order of the map.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the full readings of 119 (scans 144-161), of 152 and 120, of 121 (scans 1-48 and 49-73) with 153 and 155, and of 122 against the research runs with 125, each with its tables. The checking programs of the 119 reading (`119_144-161_276-281_checks_fin.py`, `_checks_pgl5.py`, with their output) are included.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the topic's items SA20-2 to SA20-19, SA20-W1 to W4.
  - `study/letter_to_kostant_123.md`: our report on the letter of 1969.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA20_transcriptions.zip`: the AI transcriptions (LaTeX) of the cotes.**
  - 119 (scans 144-161), 120, 121, 122, 152, 153 and 155 by GPT-6 Astra (ChatGPT Pro mode).
  - 123 and 125 by GPT-6 Astra at reasoning effort max in Codex web.
  - `\scanpage{N}` marks scan N of the cote's PDF; the archive's pencil page is N−1.
  - The transcriptions carry `\unsure{a|b}` marks. The readings decided some readings on the scan images, and their CORRECTIONS tables give them. Where a step of yours depends on a doubtful reading, say so.
  - Faces written by other people (typed or printed documents reused as paper) are left out; a comment line marks each one.
- **`RESEARCH_SA20_literature.zip`:** the LaTeX of SGA 7 II, exposés XIII-XV (our English edition, AI-translated, with its rights notice).
  - Fetch the other sources yourself. They are listed under "Sources" below.

- **`SA10_RESULTS_20261119.md` and `SA10_final_paper_tex.zip`:** the results of RESEARCH_SA10 (stratified spaces, cotes 150-151) that this prompt builds on, by statement id with status and checks, and the LaTeX of that run's paper with its results register. The section "Results of RESEARCH_SA10" below places this prompt on them.

## Where this comes from

**The pages.** These cotes of the Grothendieck archive at the University of Montpellier hold his notes around the Esquisse d'un programme (January 1984) and some earlier folders:
1. **119/144-161:** the Esquisse dossier: a note on the quotient of a foliation (March 1986); the "Additif Esquisse d'un Programme" on collars, cones, tubular neighbourhoods and filtrations (148-153); and the "Digressions combinatoires" (155-161).
2. **120 and 121:** axiom systems for a "topologie modérée", in several drafts (1980s).
3. **152:** plane trees and their rotations, written over a printout of 19 May 1982.
4. **153:** "analyseurs", the structure carried by the operations on rings, on printout of 19 April 1982.
5. **155:** a Tannakian-type duality over a finite extension k′/k, on documents of June-October 1984.
6. **122:** "Point singulier isolé de la fibre", after April 1968.
7. **123:** the simultaneous resolution of the adjoint quotient over a base, Kostant's principal elements, and the letter to Kostant of 22 October 1969.
8. **125:** local and projective duality.

**Our reading of them.** Sweep 3 of our horizontal reading (18-19 Nov 2026) read all of these pages in full: 122 and 123 by ae4ae3dc, the rest by readers. All are Claude Opus 5.5 at effort max.

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages. We know of no published study of most of these pages; check this.

## Results this prompt builds on (status on 19 Nov 2026)

Each result names its item and pages. Its check events and corrections are the rows of the attached tables with that item and those pages. Check each one where you use it (Rules of proof, 7).

- **R1 (119/148-149, SA20-3): the collar conjecture.**
  - II c), the contractibility of the automorphisms of a cone, is J. W. Alexander's trick. His "Alexandroff ?" is Alexander.
  - I c) is false as written. For B a closed manifold the group in question is the concordance (pseudo-isotopy) space of B, and its π₀ is nonzero for suitable closed manifolds of high dimension (Hatcher-Wagoner; Burghelea-Lashof-Rothenberg for the topological case; from memory). PL pseudo-isotopies are tame, so the obstruction carries over.
  - I b) falls with I c): his own struck line fibres the rigidified collars over the collars, with fibre a torsor under that group.
  - The fibrewise automorphisms (b, u) ↦ (b, h_b(u)) form a contractible group.
  - Readings decided on the images: "Ċ bordant dans X∖(C∖Ċ)" (148), "11 foncteurs" (150).
- **R2 (119/149-150, SA20-4).** In the cascade of categories (PB, PBC, PBCR, EP, EPC, EPCR), the 2-cells α and β are isomorphisms once a collar exists. The forgetful functors are equivalences exactly when the choice spaces of I and II are contractible. So PBCR → PBC → PB cannot all be equivalences when B has a non-contractible concordance space.
- **R3 (119/151-153).**
  - A tubular neighbourhood f⁻¹([0, ε]) is a strict cone for ε below the first bifurcation value of f on X∖Y (Hardt's triviality).
  - The homotopy class of φ: V̇ → Y is determined.
  - His correction "la moins fine" is necessary.
  - The margin "X∖Y régulier implique Y régulier" is false in general (the axes in ℝ²) and true under equisingularity.
- **R4 (cote 120, SA20-12).**
  - The graph calculus, finite limits, colimits and the amalgam criteria are re-derived.
  - The reconstruction M_* ⟷ (E, R, |·|) of 008/018 needs conservativity and an image axiom (the categorical form of M1).
  - 015 needs Card R₀ ≥ 2.
  - On 020, "compact" must be read "relatively compact".
  - On 024 the conclusion is for X∖Y, under M1-M4 and M11.
  - Generic triviality in his finite-diagram form (025) holds for inclusions and fails for parallel arrows; there is a counterexample with a rotation family.
- **R5 (121/001-048, SA20-13, -14).**
  - The existence of a coarsest admissible decomposition (015) holds as stated.
  - Prop D (028) fails for topological spaces (ℝ × cH).
  - The correspondence of Prop C fails in TOP, under either reading of "régulièrement immergée".
  - The fibre-manifold sentence of 036 holds in PL and fails in TOP.
  - The first sentence of Prop B follows from A in every context.
- **R6 (121/049-073, SA20-15).**
  - The gluing proof of 062 is complete.
  - The first stage on 049 is X − ∪ Fr(T_α).
  - The intersection claim of 070 does not follow from the stated axioms, so intersections must be an axiom.
  - Triangulability (065) is a new axiom: a Cantor set satisfies the rest.
  - 058 needs I = [−1, 1].
  - None of the axiom systems of 121 is o-minimal as written. O-minimality is cote 120's closure in all arities together with condition f) on the line, and axioms on compact sets alone see only the open core.
- **R7 (cote 155, SA20-17).**
  - The idealizer quotient J̃/J is Takeuchi's product A ×_{k′} A, so his condition (ii) makes the dual pro-ring A a ×_{k′}-bialgebra, a bialgebroid over k′.
  - The diagonal functor is exact for étale k′/k and not for inseparable k′/k.
  - End_A(U) ≅ A^o.
  - His question on 004 is answered by Deligne's theorem (1990) for rigid categories with End(1) = k.
- **R8 (cote 153, SA20-16).**
  - The binomial analyser is checked: integral product, composition and comultiplication in the binomial basis.
  - "OK si Ω est un module libre" (004) holds when k₀ is a domain.
  - The analysers are a one-sided form of the plethories of Tall-Wraith and Borger-Wieland.
- **R9 (cote 122, SA20-18, -19).**
  - Milnor's fibration as an open book: W = P ∪ Q with P = W − W₀ fibred over S¹ with fibre M, and Q = W₀ × D².
  - The Gysin sequence gives H^i(W − W₀) ≅ H^{i−1}(W₀) for i ≠ 0, 2n.
  - Local Lefschetz holds with the bounds n−2 (028) and n+1 (032), confirmed on the images.
  - H^i(M) = 0 for i > n: true, though his limit argument is a sketch.
  - The six-term sequence 0 → H^{n−1}(M) → H^{n−1}(W₀) → H^n(M)^∨ → H^n(M) → H^n(W₀) → H^{n−1}(M)^∨ → 0, whose middle arrow is u.
  - For W a sphere and n ≥ 3, H^i(M) = 0 for i ≠ 0, n−1, n.
  - The vanishing H^{n−1}(M) = 0 is not on the pages.
  - The sign he asks about on 022 is (−1)^n up to conventions.
  - No research-run row of ours is advanced by cote 122.
- **R10 (cote 125, SA20-W2).**
  - Every equivalence on 003 and 008 holds for X projective and Cohen-Macaulay, a hypothesis the page does not state.
  - His "?" on 006 holds.
  - The threshold is r−n−1 in today's convention.
- **R11 (cote 123, SA20-W1, W3, W4).**
  - Over a base S, ℬ^reg ≅ G′^reg is the largest open set over which the Steinberg resolution is an isomorphism.
  - For S normal and locally noetherian, Pic(ℬ) ≅ Pic(ℬ^reg) ≅ Pic(G′^reg).
  - His conclusion on 014 (no resolution of f analogous to that of f′ without touching G^reg) is explained by the finite Picard group of G^reg.
  - RigKos/G is finite étale of rank card(W)²/(h z φ(h)) (035, re-derived).
  - The map c ↦ c′ from Dynkin classes to parabolic classes is not injective for A₃.
  - The letter of 22 Oct 1969 states that if the orbit of x has dimension 2N − 2i, the Borel subgroups containing x form a variety of dimension i, so dim Z(x) = r + 2 dim B_x. Steinberg (Invent. Math. 36, 1976) and Spaltenstein proved it, and Douglass-Röhrle (arXiv:0802.0764) call it a conjectured formula of Grothendieck.
- **R12 (119/155-161, SA20-5).**
  - The "groupe trilitaire" of 156 is AGL₂(𝔽₃), of order 432.
  - For each of the three pairings of the four directions there is exactly one G_α ≅ S₆ in the symmetric group of the twelve lines. AΓL₁(𝔽₉) embeds in Aut(G_α) with index 10, and his "ordre 10" is that index.
  - The exact sequence III.5 does not split.
  - The torsor identities of 156-157 hold with ω(Q) the orientation of the square.
  - All of these were checked by exhaustive computation.
- **R13 (cote 152, SA20-7).**
  - A tree's edge pairing has genus 0 iff it is non-crossing (re-derived).
  - The rule of 004, read literally, rejects the nested pairing (1 4)(2 3). Contracting both edges of a pair repairs it.
  - The dictionary of 010 is the consistent one.
- **R14 (119/145-146, SA20-2).** His quotient of a foliation is the monodromy quotient, not the holonomy one. The third condition reads "et connexes" (image).

## Results of RESEARCH_SA10 that this prompt builds on (added 19 Nov 2026)

Added by Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8) from its intake of RESEARCH_SA10, the run of GPT-6 Astra (ChatGPT Pro mode) on the stratified spaces of cotes 150-151, final of 19 Nov 2026. `SA10_RESULTS_20261119.md` lists the results used here by statement id, each with its status and its checks; `SA10_final_paper_tex.zip` holds the paper with every proof. Cite them by statement id. Check each one you use as you use it, and record that check in CHECK_EVENTS.tsv.

RESEARCH_SA10 settled the questions on the stratified spaces of cotes 150-151 that overlap Part A here. They place Part A as follows; Parts B-E are untouched, and the items of Part A keep their wording.

**Settled: cite them, check them against his pages, and do what remains (A.6).**
- The recollement of 039 for sheaves of sets is B1.1, an unconditional closed-open recollement by triples (L, E, E → i⁻¹j_*L), with A3.2 (the left adjoint j_!, and when restriction to the open union is an equivalence). What remains of the first bullet of A.6 is the six-functor version in the derived setting and its match with his formulas on 039.
- For smooth Thom-Mather spaces, "control data ⟷ manifolds with fibred boundaries and compatible corners" is the resolution theorem C2.05, a known result (Albin 2016, Th. 6.3; Albin-Leichtnam-Mazzeo-Piazza, Props. 2.2-2.7; Albin-Brasselet-Piazza, Th. 2.10 and 2.13; Mather, §7). Cite it with these locators and do not re-prove it. The second bullet of A.6 is then: state his data of 041-047 exactly, prove that they are the data of that theorem or name the hypothesis they lack, and prove the reconstruction outside it: n strata in his own form, and the PL and topological versions.
- For the groupoid data of 043 in general: a full span of groupoids determines the two-stratum homotopy pushout when every piece is a K(π,1) (B4.1); the full flag diagram reconstructs X under pairwise asphericity (B4.2); forgetting the gluing coherence changes the space, Hopf S³ against S² × S¹ (B4.3); sets see π₀ of the exit mapping spaces and groupoid stacks see π₁ (B3.1, B3.2). What remains of the third bullet is dimension 2, worked out from these.

**Changed: restate these points before you work on the items they touch.**
- Pair pieces do not glue. For X = ℂ ⊃ ℝ ⊃ {0}, the diagram of all pair and triple tubes of 151/057-061 has neither Sh(X) as colimit (A1.3) nor the homotopy type of X as homotopy colimit (INT-SA10-K10: first Betti number 4 against 0). What glues is the tubes W_i of the strata in the whole space, chosen at once, with their actual pairwise and triple intersections (A1.2); A1.5 decides which pieces can be dropped. If 041-047 glue n strata along pair data, state the reconstruction theorem of A.6 with these overlaps.
- Control data include π-control as an axiom, since the bare intersection conditions do not imply it (C2.01, C2.02); the whole radial collar germ, since one radius level does not determine control (C2.03); and the regular source bundles, since the bare recapitulation is not Thom-Mather data (C2.04).
- Collars and manifoldness are hypotheses, not consequences. A homotopically stratified set need have no conical collar (C4.04, Quinn's shrinking hedgehog). Weak conical data do not give fibrancy (C1.01). A precylindrical stratification need not be a manifold with corners; C3.04 is the exact local criterion. In TOP neither manifold fibres nor manifold faces follow from the face conditions, while PL bundles and smooth submersions with those conditions give them (C5.03-C5.05; the matrix C5.08). State in which category each step of A.1, A.2 and A.6 is proved.
- A locally finite closed family is the colimit of its pieces (A4.1), but a finite diagram of closed embeddings over a meet-semilattice need not embed its members (A4.2); the cartesian-meet condition repairs it (A4.3), and closure of the strata under binary intersection is (24) of 151/054 with an empty-bottom qualification (A4.4). This bears on the intersection axiom of A.3(c) and on the reconstruction of A.4.
- Lower unions defined by supports do not commute with inverse images, and those defined by the order do (A2.2); the tubes of an open difference of cribles can change homotopy type (A3.1). This bears on "commuting with restriction to opens" in A.5 (049).

**Open:** A.1-A.5 and A.7, as they stand with the restatements above. RESEARCH_SA10 worked in TOP, PL and smooth, not in an o-minimal structure, and it did not treat concordance spaces, rigidified collars or the cascade of 119/149-150.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** In a fixed o-minimal structure, the space of strict rigidified collars of a bordant B is contractible, and the cascade holds with rigidified collars throughout: PB ≃ PBCR ≃ EPCR ≃ EP.
- **L2.** His two drafts each hold half of o-minimality. Cote 120 has the closure under projections in all arities, and cote 121 has finiteness on the line. Together, and only together, they give the compact definable sets of a structure with o-minimal open core.
- **L3.** The reconstruction of 120/008 holds with an image axiom ("E regular and |·| preserves images"), and M1 does not follow without it.
- **L4.** In D(Λ[π]) with π acting trivially on RΓ(W₀), T − 1 on RΓ(M) factors uniquely as u ∘ V with V: K → K^∨[−2n]. V is the variation, and this settles his sign question on 022.
- **L5.** H^{n−1}(M) = 0, for an isolated singular point with smooth total space, follows within his framework from the self-dual triangle, the six-term sequence and the (n−2)-connectedness of the link.
- **L6.** Cote 155 is an early formulation of non-neutral Tannakian duality through bialgebroids: Takeuchi's ×_{k′}-bialgebras, between Saavedra (1972) and Deligne (1990).
- **L7.** The presentation of the triality through AGL₂(𝔽₃) on 119/156 is not in the literature on the outer automorphism of S₆.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

**What counts as done,** per item of the Parts and per Lead:
- (a) a theorem with a complete proof; or
- (b) a refutation with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is finite), together with the strongest true statement proved in its place.

Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack the obstruction, starting from that instance.

"Known" counts only with the derivation of the statement used here from the cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is the whole answer.

**Not acceptable:**
- a survey;
- "open, see [reference]";
- a plan, an outline or a sample;
- a statement for every dimension proved in low dimension without saying so;
- a step that replaces a claim by a convenient special case without naming it;
- a reading of the manuscript taken on trust where the mathematics depends on it. The transcriptions are AI-made and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done.

If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA20_report.md` reads INCOMPLETE. Its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.

A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Collars, cones and tame topology. The main question is A.1.**
Work in a fixed o-minimal expansion of a real closed field, the semialgebraic case first. Take ∞-isotopic categories as simplicial categories of definable homeomorphisms.
- **A.1 (main). The collar conjecture of 119/148-149 and the cascade of 150.**
  - (a) Define "bordant" and prove or refute I a).
  - (b) Compute the definable concordance space of a closed definable manifold B, π₀ first, and compare it with the PL and TOP concordance spaces.
  - (c) Decide whether the space of strict rigidified collars is contractible, and so settle I b) and I c) as written, in the fibrewise form, and in the rigidified form (L1).
  - (d) Prove II b).
  - (e) Prove the cascade with the corrected collar notion: PB ≃ PBCR ≃ EPCR ≃ EP, with the 2-cells α and β, and the variants for multipairs and multipointed spaces. Determine which of his eleven functors are equivalences when B has a non-contractible concordance space.
- **A.2. Tubular neighbourhoods and filtrations (119/151-153).**
  - Prove the existence and essential uniqueness of Y-admissible rigidifications.
  - Decide whether the condition dim φ⁻¹(y) = codim_y(Y, X) − 1 can always be met, and whether it gives uniqueness.
  - Settle the equivalence for equisingular pairs (152).
  - Prove the existence of the canonical coarsest regular equidimensional filtration of a tame space (153), and determine its invariants.
- **A.3. His axioms against o-minimality** (cotes 120 and 121; L2).
  - (a) Characterize the one-space families of 121/004-024 (a)-f), with or without e_n) that arise as the definable subsets of a definable set in an o-minimal structure, with the extra data needed.
  - (b) Prove or refute that cote 120's M0-M11, completed by f) for M_1 (every moderate part of R is a finite union of points and intervals), characterize the compact definable sets of the structures with o-minimal open core.
  - (c) Settle the same question for the compact systems of 121/054-073, with intersections as an axiom and I = [−1, 1].
  - (d) Close the gap of 121/018: does a coarsest F-regular partition exist for regularity as smooth points of semialgebraic sets, with condition (S) for all closed saturated unions?
- **A.4. The reconstruction of cote 120** (L3).
  - Prove or refute 120/008 and the converse of 018: M_* ⟷ (E, R, |·|), with E finitely complete, |·| faithful, conservative, transportable and left exact, and every object embedding in some Rⁿ.
  - Decide whether M1 is a consequence or must be added.
  - Give a class closed under unique but not general existential quantification, or prove that none exists in this setting.
- **A.5. The canonical partitions (121/026-037 and 049-052).**
  - Prove Props A-D of 026-028 in the PL category.
  - Settle A, and the uniqueness bracket of B, in TOP.
  - Prove Conjecture 1 in the PL and the definable contexts: the intrinsic stratification is privileged and coarsest.
  - For Conjecture 2, take one proper definable map f: X → Y. Prove or refute that the largest open set over which f is non-singular and locally trivial is definable with rare complement, and that the recursion of 036-037 produces a coarsest privileged partition of f.
  - Prove the claim of 049: a coarsest strictly admissible partition adapted to a locally finite closed family, commuting with restriction to opens. Prove it in each named context with "strict" made precise, or determine the context where it fails.
- **A.6. Gluing (121/039-047).**
  - Write out the recollement of 039 with all six functors.
  - State and prove the reconstruction theorem behind 041-047 for n strata: a stratified space with control data ⟷ a system of manifolds with fibred boundaries and compatible corners.
  - Determine what the groupoid data of 043 determine in dimension 2 and in general.
- **A.7. The quotient topos of a foliation (119/145-146).**
  - State "Th", C ≃ C′, precisely: "multiplicité topologique" as an étendue or a topological stack, the morphisms of C′, and the conditions on R.
  - Prove it or refute it, with the monodromy quotient.
  - Decide whether Hom(ξ, η) is discrete.
  - Settle the version over a topos ("[ou topos ?]").

**B. Cote 155 and cote 153.**
- **B.1.** State and prove the equivalence of 155/002 (L6), identifying J̃/J with A ×_{k′} A.
  - An abelian k-linear ⊗-category with an exact faithful ⊗-functor to Modf(k′) corresponds to a commutative augmented k′-algebra U whose dual pro-ring A is a ×_{k′}-bialgebra.
  - Finish 006-010: the evaluation, the coevaluation, the antipode a: A → A^o and the triangle identities.
  - Derive the answer to his question on 004 from Deligne, "Catégories tannakiennes" (1990), with exact locators.
  - Determine what of 002 is in Takeuchi (1977), Hai (2008) and Schauenburg, and what is not.
- **B.2.** For the analysers of 153:
  - (a) Determine which analysers satisfying 1)-3) of 153/006 are plethories, and what structure must be added.
  - (b) Construct the divided-power analyser of 153/010 with its domain of action.
  - (c) For k₀ ⊂ K₀, decide when Ω = {F ∈ K₀[T] : F(k₀) ⊂ k₀} carries well-determined coaddition and comultiplication (004).
  - (d) Determine when Ω → App(Ω₀, Ω₀) is injective (008).

**C. Cote 122 and cote 125.**
- **C.1. Cote 122** (L4, L5).
  - (a) Prove the factorization T − 1 = u ∘ V in D(Λ[π]) and identify V with the variation map.
  - (b) Settle the sign of 122/022 ("ρ et ρ′ sont transposés (signe ?)") through the relation between u and the Seifert form.
  - (c) Give the étale version, with π the tame inertia and the twists placed so that u: K^∨(−n)[−2n] → K.
  - (d) Prove H^{n−1}(M) = 0 for an isolated singular point with smooth total space, from the triangle (a′), the six-term sequence of 032 and the (n−2)-connectedness of the link, naming each input used.
  - (e) Map each statement of 122/003-035 to Milnor (1968) and to SGA 7 I and XIII-XV, with exact locators.
- **C.2. Cote 125.**
  - (a) Write the chain of 125/003 as a theorem with its hypotheses (X projective Cohen-Macaulay of dimension r, Y closed, 0 < m < r), and prove every equivalence, including the injectivity clause and the reduction to O(−n).
  - (b) Determine, with exact locators, what of it is in SGA 2 XII-XIII, in Hartshorne (1968, 1971), in Ogus (1973) and in Speiser (1973): which direction, for which X, with or without injectivity.
  - (c) Complete the induction that the diagram of 006 sets up.

**D. Cote 123.**
- **D.1. The letter and the folder against the literature.**
  - Compare 123/004-014 and the letter of 22 Oct 1969 with Brieskorn (ICM 1970), Slodowy (LNM 815), Steinberg (LNM 366; Invent. Math. 36, 1976), Springer (Publ. IHÉS 30), Spaltenstein and Hesselink.
  - Determine which of the letter's questions were answered, by whom and where.
  - Prove the statements of cote 123 that are not in print: the form over a base S, the Picard sequences of 012-014, and the count of RigKos.
- **D.2. The computations his questions ask for,** type by type for all simple types:
  - (a) whether N_W(⟨c⟩) splits over ⟨c⟩ (123/002), and whether N ∩ N′ splits over μ_h × Z (029);
  - (b) the signs by which outer automorphisms act on 𝔤_ψ and on Kostant's line Δ (034, 035, 042), and whether 𝔤_ψ ≅ Δ canonically;
  - (c) which single vanishings in Σ x^α e_α (α ∈ Σ ∪ {−ψ}) give regular nilpotents (047);
  - (d) the map c ↦ c′ from Dynkin classes to parabolic classes: where it is injective, and which classes give a Borel (019-020).
  - Attach every program.

**E. Finite geometry and plane trees.**
- **E.1. The Digressions of 119/155-161 as a finished chapter.** Prove every statement of his two plans:
  - orientations and the contracted product;
  - squares;
  - the exceptional isomorphisms for 2 to 6 elements;
  - the duality S ↔ S* with its dictionary;
  - the square torsors;
  - the affine plane over 𝔽₃ and the triality;
  - the "trois perspectives" of the skew icosahedron;
  - the hexagram duality "par bihexagones";
  - the twist ε ∧ Q (Q* ≃ ε ∧ Q), with a definition that makes it true;
  - the "réalisations géométriques" his last line asks for.
  - Settle L7.
- **E.2. Cote 152.**
  - Determine what "type de mot" must mean for the equivalence of 152/003 to hold, under each reading ("isotypique", "isotopique"), and prove it.
  - Prove the repaired criterion of 004.
  - Determine how 152/010-013 relate to the classical theory of maps and unicellular gluings, and to the "cartes" of the Esquisse.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- **Tame topology and o-minimality:**
  - L. van den Dries, *Tame topology and o-minimal structures*, LMS LNS 248 (1998);
  - L. van den Dries and C. Miller, Duke Math. J. 84 (1996);
  - M. Coste, *An introduction to o-minimal geometry*;
  - M. Shiota, *Geometry of subanalytic and semialgebraic sets* (1997), and arXiv:1002.1508, 1310.5489;
  - R. Hardt, Amer. J. Math. 102 (1980);
  - A. Dolich, C. Miller and C. Steinhorn, Trans. AMS (2010);
  - C. Miller and P. Speissegger, Fund. Math. (1999).
- **Concordance and stratified spaces:**
  - A. Hatcher and J. Wagoner, Astérisque 6 (1973);
  - D. Burghelea, R. Lashof and M. Rothenberg, LNM 473 (1975);
  - D. Ayala, J. Francis and H. L. Tanaka, arXiv:1409.0501;
  - J. Lurie, *Higher Algebra*, Appendix A;
  - F. Quinn (1988); H. King, Topology Appl. 20 (1985);
  - A. Verona, LNM 1102 (1984);
  - D. Treumann, Compositio Math. 145 (2009);
  - R. MacPherson and K. Vilonen, Invent. Math. 84 (1986).
- **Foliations and topoi:** A. Kock and I. Moerdijk (1992, 1996); A. Joyal and M. Tierney, Mem. AMS 309 (1984); SGA 4 IV.
- **Tannakian duality, bialgebroids and plethories:**
  - P. Deligne, "Catégories tannakiennes" (Grothendieck Festschrift II, 1990);
  - P. Deligne and J. Milne (1982);
  - N. Saavedra Rivano, LNM 265 (1972);
  - M. Takeuchi, "Groups of algebras over A ⊗ Ā", J. Math. Soc. Japan 29 (1977);
  - P. H. Hai (2008); P. Schauenburg;
  - J. Borger and B. Wieland, "Plethystic algebra" (Adv. Math. 2005);
  - D. Tall and G. Wraith (1970);
  - N. Roby (1963, 1965).
- **Singularities and duality:**
  - J. Milnor, *Singular points of complex hypersurfaces* (1968);
  - SGA 7 I and XIII-XV (attached: XIII-XV);
  - K. Lamotke, Topology 14 (1975);
  - SGA 2 XII-XIII;
  - R. Hartshorne, LNM 156 (1970), Compositio Math. 23 (1971);
  - A. Ogus (1973); R. Speiser (1973).
- **Lie theory:**
  - E. Brieskorn (ICM 1970); P. Slodowy, LNM 815 (1980);
  - R. Steinberg, LNM 366 (1974) and Invent. Math. 36 (1976);
  - T. A. Springer, Publ. IHÉS 30 (1966);
  - N. Spaltenstein; W. Hesselink;
  - J. M. Douglass and G. Röhrle, arXiv:0802.0764;
  - B. Kostant, Amer. J. Math. 81 (1959) and 85 (1963).
- **Finite geometry and maps:**
  - B. Howard, J. Millson, A. Snowden and R. Vakil, arXiv:0710.5916;
  - P. Cameron's notes on S₆;
  - T. Walsh and A. Lehman (1972);
  - R. Stanley, *Enumerative Combinatorics 2*, ch. 6.

## Rules of proof (they bind every statement you deliver)

1. **State the actual claim with all its data:** the axioms assumed, the class of structures, the finiteness and
   dimension hypotheses. Do not replace it by a convenient special case. If you prove a special case, name it as one
   and keep the general statement on your list.
2. **Type every map and relation you introduce:** source, target, the category or ordered set in which it lives, and
   each extra property you use. Compositions must type-check.
3. **Every reduction** ("we may assume", "replace by", "refine to") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. **"Up to" names the ambiguity.** Keep apart:
   - equality;
   - isomorphism;
   - equivalence of categories or of topoi;
   - homotopy equivalence;
   - weak equivalence of a specified map;
   - an isomorphism of Hodge or Galois structures against an isomorphism of groups.
5. **Check the edge cases in scope:**
   - empty strata;
   - dimension 0, 1 and 2;
   - non-compact and non-locally-finite families;
   - characteristic 2 and 3 where the Lie-theoretic statements are made over a base;
   - the inseparable case for 155;
   - n = 1 and n = 2 for 122.
6. **Counterexamples.** A counterexample is given completely and, when finite, checked by a program whose code and output
   you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. **No authority.** Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. **What is not yet settled** stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. **Known results** are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never invent a reference;
   mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper (the arXiv e-print)
   where one exists.

## What to deliver

One ZIP containing:
- **`RESEARCH_SA20_paper.tex` and its PDF** (LuaLaTeX, compiles cleanly):
  - the mathematics in the order of the Parts, every statement numbered;
  - each statement labelled Proved; Proved under stated hypotheses (with whether they hold where the statement is
    used); Refuted (with the counterexample and the corrected statement); or Known (with citation);
  - each new statement with its complete proof;
  - checked and unchecked statements in separate parts;
  - English, first person plural;
  - where a statement is Grothendieck's, the cote and scan of his page.
- **`RESEARCH_SA20_results.csv`:** one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- **`RESEARCH_SA20_references.bib`:** each entry marked opened / not opened.
- **`RESEARCH_SA20_report.md`:**
  - first, the outcome table: one line per item of the Parts and per Lead, proved or refuted, with the statement
    number;
  - then what you read;
  - what you computed: every program with its scope, counts and run time;
  - every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- **`PROGRESS_LEDGER.md`:** the dated ledger of the progress reviews.
- **`CHECK_EVENTS.tsv`** (below) **and `code/`:** every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. The attached study's statements carry ids such as SA20-3 with their pages; keep them. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is.
- Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a
  display or a line of text.
- Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again.
- Then render pages to images and look at them: every page that had an overflow, and a sample spread over the
  document.
- Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA20_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
