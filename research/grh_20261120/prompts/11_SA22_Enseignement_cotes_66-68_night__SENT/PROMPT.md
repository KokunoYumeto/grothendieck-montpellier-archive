**The attached files.** Besides this file there is one ZIP, `SA22_Enseignement_cotes_66-68_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA22_study.zip` is the folder `RESEARCH_SA22_study/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA22: Grothendieck's conformal surgery of 1984, his thesis problems of 1964, and the algebra of cote 68 (cotes 66, 67, 68)

**What is to be settled, in three Parts:**
- **A.** Cote 67: his programme of January-April 1984 for cutting, welding, capping and plumbing Riemann surfaces. A.1, whether the maps of section 6 onto moduli of stable curves are isomorphisms, is the main question.
- **B.** Cote 66: three of his 28 thesis problems of 1964, among them question 24 on numerical and homological equivalence for 2-cycles on fourfolds, and the fate of all 28.
- **C.** Cote 68: the corrected theory of exponentials and unipotent automorphisms, and the rearrangement inequalities for convolution on groups.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA22`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent ae4ae3dc17acaa440, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA22_study.zip`: our study of the topic.**
  - `study/STUDY.md`. Its head gives the state of the sections and what changed after the second wave of readings. §1 is cote 66, §2 and §3 cote 67, §4 cote 68.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the full reading of 67/003-046 and 084-101, and the readings of cote 68 decided on the images.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the topic's items SA22-0 to SA22-13.
  - `study/reports/`: our reports on characteristic 5 at 67/086, on the hexagonal ratio at 67/098, and on the date of cote 67.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA22_transcriptions.zip`: the AI transcriptions (LaTeX) of the cotes.**
  - 66 by GPT-6 Astra at reasoning effort max in Codex web.
  - 67 and 68 by GPT-6 Astra (ChatGPT Pro mode).
  - `\scanpage{N}` marks scan N of the cote's PDF; the archive's pencil page is N−1.
  - The transcriptions carry `\unsure{a|b}` marks. The readings decided some readings on the scan images, and their CORRECTIONS tables give them. Where a step of yours depends on a doubtful reading, say so.
  - Faces written by other people (a printed list on 67/008, a staff list on 68/018) are left out. A name and an address on two envelopes (67/012-013) are removed. A comment line marks each place.

There is no literature attachment: we hold no LaTeX source for the works this prompt needs. Fetch them yourself; they are listed under "Sources" below.

## Where this comes from

**The pages.** Three cotes of the Grothendieck archive at the University of Montpellier:
1. **66:** "Travaux de thèses", four sheets of 1964 with 28 numbered thesis problems, and margins of about 1968-71.
2. **67:** "Chirurgie des surfaces conformes", in two layers.
   - 1976-78: surgery sheets, the title sheet dated "(1976 ou 77 ?)", and envelopes, one metered at Nagoya University on 20.12.77.
   - December 1983 to April 1984:
     - the canonical metrics (024-046);
     - the anabelian sheets of 15.1.1984 (048-051);
     - the welding, capping and plumbing notes of 11-13.1.1984 (053-083);
     - "Moduli M0,4 et l'octaèdre" (084-089);
     - "Courbes elliptiques réelles" (091-101);
     - his letter to Lipman Bers of 15.4.1984 (016-021).
3. **68:**
   - positional games, in two drafts and a restart;
   - rearrangement inequalities for convolution on groups (015-022);
   - exponentials and unipotent automorphisms in characteristic 0 (036-046);
   - orientations and graded determinants (050-056).

**Our reading of them.** Sweep 3 of our horizontal reading (18-19 Nov 2026) read all of these pages in full: 66, 67/048-083 and 68 by ae4ae3dc, and 67/003-046 and 084-101 by a reader. Both are Claude Opus 5.5 at effort max.

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages. We know of no published study of cotes 67 and 68; check this.

## Results this prompt builds on (status on 19 Nov 2026)

Each result names its item and pages. Its check events and corrections are the rows of the attached tables with that item and those pages. Check each one where you use it (Rules of proof, 7).

- **R1 (67/054-061, 071-073, SA22-6).**
  - Théorème 1 is re-derived: a boundary chart forces the leading exponent n = 1.
  - Lemma 3 c) (removability of rectifiable curves) is right.
  - Théorème 4 and the Scholie of 073 need quasisymmetric gluing maps for existence; uniqueness holds for removable seams.
  - No regularity is needed to cut along a Jordan arc (Carathéodory).
  - Lemma 4, NB 1 is right.
- **R2 (67/061-070, capping).** His "Conjecture" of 068-069, that (D_i) ↦ (o(D_i)) is a bijection from admissible disc systems to systems of Euclidean discs, cannot hold as stated. By Koebe's quarter theorem the shadows are bounded (Michel Hua's project, re-derived), and the letter to Bers withdraws it (019). His worry about genus 0 is answered by the cusp coordinates of the complete hyperbolic metric.
- **R3 (67/074-082, SA22-7).**
  - Cutting along C and capping canonically gives the normalization of a Mumford-Deligne stable curve, with an element of T_{x₁} ⊗ T_{x₂} at each node.
  - His maps MDB_{g,ν} → M_stND_{g,ν} (real-analytic) and MD_{g,ν} → M_stN_{g,ν} (algebraic) have the right dimensions: real dimension 6g − 6 + 3ν for the bordered Teichmüller space.
  - Whether they are isomorphisms is open on the page; his key case is (0, 4).
- **R4 (67/084-089, SA22-8).**
  - The Proposition of 086, stated for characteristic ≠ 2, fails exactly in characteristic 5 among p ≤ 29. There the stabilizer of the six points {0, ∞, ±1, ±i} has order 120, with five Klein groups; at p = 5 these points are P¹(𝔽₅).
  - The Theorem of 089 holds in every characteristic ≠ 2, 5 included.
  - On 085 "face" means a pair of antipodal faces.
- **R5 (67/091-101, SA22-9).**
  - The hexagonal ratio on 098 is 3; he wrote √3.
  - His guess j = c·log a (097) is wrong, since j(a) = j(1/a).
  - The corollary of 091 needs Spec k connected.
  - The count on 100 needs his struck proviso: ℤ[(1+√−11)/2] gives three non-split classes.
  - The struck "sans [bord]" on 101 must stand.
- **R6 (67/016-021).** The "orange-slice" model of the letter to Bers is false as stated. The extremal-length argument is Michel Hua's project's; the numbers are in the Pro notes.
- **R7 (67/003-014, 024-046).**
  - The surgery sheets have slips: 3/2 for ½; "≥ 0 ?" fails when every face is a disc; "g(f) = 0 tjrs" needs K not inside a disc.
  - On the envelopes, |λ| ≠ 1 iff α ∉ [−2, 2].
  - The metric dossier reads in the order 027, 045, 028, 046, 029-044.
- **R8 (67/048-051, SA22-5).**
  - The anabelian sheets are from 15 January 1984: they are on printout paper of August 1982 and use the vocabulary of 1983.
  - The presentations of SL₂(ℤ) and GL₂(ℤ) on 050 are checked.
- **R9 (66, SA22-0).**
  - Subject 21 is the affine analogue of proper base change (Gabber 1994, Fujiwara 1995; from memory).
  - Subject 25's "pb du carré" has a negative answer by exterior products of cycles on E × E (from memory).
  - Subject 24, second question, "En dim 4, cycle de dim 2 équiv. num = équiv. hom ??": see L1.
- **R10 (68/002-034, 048, SA22-1).**
  - The second draft proves positional determinacy of reachability games in general, by a well-order device (026-030).
  - His "? Th 3" holds for finitely branching games and fails in general.
  - A largest winning strategy exists only without infinite compatible plays.
- **R11 (68/036-046, SA22-10).**
  - On 039, (**) holds only for finitely generated M; in general it holds with locally nilpotent endomorphisms.
  - On 041, c_ij = −1/(i+j+1)!.
  - On 044, E_{Θ+Θ′} = E_Θ ∘ E_{Θ′}, and "loc nilpotent" must mean nilpotent locally on X.
  - On 045, (i)-(iii) are equivalent; (iv), u = exp Θ with Θ nilpotent, is sufficient and not necessary: ℚ[x]/(x²) with u(x) = 2x. The corollaries listing (iv) as equivalent fail, and so does the NB "u induit l'identité sur gr_J(A)".
  - The last corollary of 046 fails: ℚ[ε]/(ε³), I = (ε), Θ = ε d/dε. His struck condition (iii′) on gr_I(A) repairs it.
- **R12 (68/015-022, SA22-2).**
  - The rearrangement and weak-majorization equivalences are re-derived.
  - The model case, symmetric intervals in a cyclic group, is closed under convolution with nonnegative coefficients.
  - In S₃ the symmetry of "prétassé" fails.
  - The words are decided on the images: "prétassé(s)" and "tassé(s)" (first transcribed "priorisés" and "bons").
- **R13 (68/050-056, SA22-11, -12).**
  - Orientation theories are unique up to unique isomorphism, with ε_n = sg ∘ det.
  - The Stokes signs are checked.
  - 056 gives Knudsen-Mumford's axioms for graded determinants.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** Over a field of characteristic 0, numerical and homological equivalence agree for 2-cycles on smooth projective fourfolds. Our sketch:
  - The Lefschetz components of an algebraic class α ∈ H⁴ are algebraic. Use L²α ∈ H⁸; the Lefschetz (1,1) theorem applied to L⁻²(Lα − L³c) ∈ H²; and then the primitive part.
  - The decomposition ℚL² ⊕ L·NS_prim ⊕ A_prim is orthogonal.
  - The form is definite on each piece: the Hodge index theorem on NS_prim, Hodge-Riemann on real primitive (2,2) classes.
  - So the form is non-degenerate on algebraic classes.
- **L2.** The maps of section 6 are isomorphisms. Plumbing (Kra's horocyclic coordinates; Earle-Marden; Wolpert; Hubbard-Koch's analytic construction of the Deligne-Mumford compactification) gives their inverses. The (0, 4) case is the gluing of two pants with lengths and a twist.
- **L3.** At each puncture of a hyperbolic surface, the cusp coordinate gives a canonical norm on the tangent line. The space of horocycle decorations (Penner) with this norm as section is the right form of his bundle TB → T.
- **L4.** As the boundary length grows, the capped disc tends to Koebe's slit domain. By Lavrentiev's inequality the admissible radii do not form a box. In an admissibly capped pair of pants, each disc depends on all three lengths.
- **L5.** Nothing after 67/073 depends on "rectifiable": from 074 on he glues smooth boundary circles.
- **L6.** The anabelian sheets ask for what became combinatorial anabelian geometry: Nakamura (1990); Ihara-Nakamura on Oda's problem (1997); Mochizuki's semi-graphs of anabelioids (2006); Hoshi-Mochizuki (2011).
- **L7.** The Theorem of 67/089 gives the moduli space M_{0,[4]} over ℤ[½, i].
- **L8.** The axioms of 68/017 (totally ordered families of finite sets, symmetric up to translation, with convolutions in the cones) give Condition K for the family they span, and cyclic groups and ℤ carry such systems.
- **L9.** The sheets 67/091-101 re-derive the classification of real elliptic curves (Alling).

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
- a statement for every genus proved in genus 0 without saying so;
- a step that replaces a claim by a convenient special case without naming it;
- a reading of the manuscript taken on trust where the mathematics depends on it. The transcriptions are AI-made and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done.

If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA22_report.md` reads INCOMPLETE. Its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.

A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Cote 67, conformal surgery. The main question is A.1.**
Take the definitions of his spaces from 67/053-083 and from §2.2 of the study. Where the pages leave a definition open, state the choice you make and prove that the results do not depend on it, or treat each choice.
- **A.1 (main). Section 6 (074-082): decide whether MDB_{g,ν} → M_stND_{g,ν} (real-analytic) and MD_{g,ν} → M_stN_{g,ν} (algebraic) are isomorphisms** (L2).
  - (a) Settle his key case (g, ν) = (0, 4) first: the gluing of two Thurston pants with lengths and a twist.
  - (b) Settle every (g, ν), through the map on fundamental groups and the tangent map, as his next steps on the page propose.
  - (c) Identify the inverse with the plumbing constructions of Kra, Earle-Marden, Wolpert and Hubbard-Koch. Derive each identification from the source after opening it.
- **A.2. The capping (061-070, 021)** (L3, L4).
  - (a) Decide the claim of 068 marked "?": in an admissibly capped pair of pants, does each disc depend only on its own boundary length?
  - (b) Determine the image of (D_i) ↦ (o(D_i)), and whether the map is injective. That is: is an admissible disc system determined by its radii, and what is the set of admissible radii?
  - (c) Determine the limit of the capped disc as the boundary length grows.
  - (d) Prove L3: the cusp norms, Penner's decorations, and the form of the bundle TB_{g,ν} → T_{g,ν}.
  - (e) Settle the collar question of the letter (021).
- **A.3. The welding statements.** Write Théorème 4, Lemma 4 B and the Scholie of 073 in their correct form (quasisymmetric gluing for existence, removable seams for uniqueness), and prove them. Settle L5.
- **A.4. The letter to Bers (016-021).**
  - Give the correct form of the orange-slice model with its proof, from the extremal-length argument.
  - Define the enlarged Teichmüller space in which boundary circles may collapse to marked points, with the intrinsic action of (ℝ⁺)^I, and prove its properties.
- **A.5. The octahedral M_{0,4} (084-089).**
  - Prove the Theorem of 089 in every characteristic ≠ 2.
  - Prove the Proposition of 086 in its correct form, characteristic ≠ 2, 5, with the characteristic-5 counterexample in full.
  - Settle L7.
- **A.6. The anabelian sheets (048-051)** (L6).
  - (a) For each of 049 a), b) and c) and the NB of 048, give the proved statement that answers it, with its derivation from the sources.
  - (b) Check the presentations of 050-051 (T⁺_{0,4}, T⁺!_{0,4} ≅ SL(2, ℤ)/±1, the Birman sequence) and his expectation of three kinds of presentation (pants, Lego, involutions) against the known presentations of the mapping class groups.
- **A.7. Real elliptic curves (091-101).** Prove the classification of 097-098 with the corrections of R5, the count on 100 with its proviso, and the topology and H¹(ℝ, E) of 101. Settle L9.

**B. Cote 66, the thesis problems of 1964.**
- **B.1. Question 24 (66/004), second question.**
  - (a) Prove L1 for Betti cohomology over ℂ, and for ℓ-adic cohomology over any field of characteristic 0.
  - (b) In positive characteristic, prove the agreement for 2-cycles on abelian fourfolds. Derive it from the Lefschetz standard conjecture for abelian varieties (Lieberman; Kleiman) and from the Hodge standard conjecture for abelian fourfolds (Ancona, 2021, from memory: open the paper and check what it proves). Determine the class of fourfolds that the same argument covers.
  - (c) Decide the first question of 24 on the same sheet, with the same standard of proof.
- **B.2. Question 25, the "pb du carré" (66/005).** State the question exactly from the sheet. Give the negative answer with a complete construction, an algebraically trivial cycle on a surface E × E whose square is not rationally trivial, with every step derived from Mumford (1968) and Bloch (*Lectures on algebraic cycles*). Then settle the second question of 25, beside it on the sheet, which his margin "faux, cf Mumford" marks.
- **B.3. The 28 subjects.** For each of the 28 subjects of 66/002-005 and each item of the "Pour mémoire" diagram, determine the work that settled it, with exact locators, or the strongest proved statement with its locator. Settle subject 21 with the derivation from Gabber (1994) and Fujiwara (1995).

**C. Cote 68.**
- **C.1. Exponentials and unipotent automorphisms (036-046).** Over a commutative ℚ-algebra A:
  - (a) Prove the bijection Θ ↦ exp Θ between the K-derivations Θ with Θ(I^k) ⊂ I^{k+1} for all k, and the K-automorphisms that induce the identity on gr_I(A), for a nilpotent ideal I. This is his struck condition (iii′).
  - (b) Determine exactly the differential automorphisms (J nilpotent) that are exponentials of nilpotent derivations, and describe the others.
  - (c) Extend the equivalence f ∘ exp(u) = exp(v) ∘ f ⟺ fu = vf of 040 to locally nilpotent u and v.
  - (d) Settle his question on 044: for K-functors in modules, determine when u ↦ ē_u and u ↦ e_u are bijective.
- **C.2. Rearrangement inequalities on groups (015-022)** (L8).
  - (a) Decide whether the axioms a)-d) of 017 imply Condition K (021) for the convolution-stable family they span.
  - (b) Determine which finite and discrete groups carry a system satisfying the axioms, and whether the 2-torsion extension G̃ → G is forced.
  - (c) Settle the symmetry question of 020 in general.
  - Attach a program for every finite check.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- **Teichmüller theory and plumbing:**
  - L. Bers, papers on Teichmüller spaces with boundary;
  - I. Kra, "Horocyclic coordinates for Riemann surfaces and moduli spaces I", J. AMS 3 (1990);
  - C. Earle and A. Marden, on plumbing coordinates;
  - S. Wolpert, on the hyperbolic metric near the boundary of moduli;
  - J. Hubbard and S. Koch, "An analytic construction of the Deligne-Mumford compactification of the moduli space of curves", J. Differential Geom. (2014);
  - R. Penner, "The decorated Teichmüller space of punctured surfaces", Comm. Math. Phys. 113 (1987);
  - O. Lehto and K. Virtanen, *Quasiconformal mappings in the plane*;
  - A. Pfluger (1960);
  - P. Koebe; M. Lavrentiev;
  - N. Alling and N. Greenleaf, LNM 219 (1971).
- **Anabelian geometry:**
  - H. Nakamura (1990);
  - Y. Ihara and H. Nakamura, J. reine angew. Math. 487 (1997);
  - S. Mochizuki, "Semi-graphs of anabelioids" (2006);
  - Y. Hoshi and S. Mochizuki, Hiroshima Math. J. 41 (2011);
  - J. Birman, *Braids, links, and mapping class groups*.
- **Algebraic cycles:**
  - D. Lieberman, Amer. J. Math. 90 (1968);
  - S. Kleiman, "Algebraic cycles and the Weil conjectures" (1968) and "The standard conjectures" (1994);
  - G. Ancona, on the standard conjectures for abelian fourfolds (2021);
  - D. Mumford, J. Math. Kyoto Univ. 9 (1968);
  - S. Bloch, *Lectures on algebraic cycles* (1980);
  - O. Gabber, Israel J. Math. 87 (1994);
  - K. Fujiwara, Duke Math. J. 80 (1995);
  - SGA 4, 4½, 5 and 6; M. Raynaud's thesis (1970).
- **Algebra and inequalities:**
  - EGA IV §16 on differential operators;
  - G. H. Hardy, J. E. Littlewood and G. Pólya, *Inequalities*, ch. X;
  - R. M. Gabriel, Proc. London Math. Soc. (1932);
  - F. Knudsen and D. Mumford, Math. Scand. 39 (1976).

## Rules of proof (they bind every statement you deliver)

1. **State the actual claim with all its data:** the genus and number of punctures, the base field and its
   characteristic, the finiteness hypotheses. Do not replace it by a convenient special case. If you prove a special
   case, name it as one and keep the general statement on your list.
2. **Type every map and relation you introduce:** source, target, the category, space or ring in which it lives, and
   each extra property you use. Compositions must type-check.
3. **Every reduction** ("we may assume", "replace by", "normalize") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. **"Up to" names the ambiguity.** Keep apart:
   - equality;
   - isomorphism;
   - real-analytic against algebraic isomorphism;
   - isomorphism of coarse moduli against isomorphism of stacks;
   - numerical, homological and rational equivalence.
5. **Check the edge cases in scope:**
   - (g, ν) = (0, 3), (0, 4), (1, 1);
   - cusps against boundary circles;
   - characteristic 2, 3 and 5 for the octahedron;
   - non-noetherian rings and modules not of finite type for C.1;
   - infinite groups for C.2.
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
- **`RESEARCH_SA22_paper.tex` and its PDF** (LuaLaTeX, compiles cleanly):
  - the mathematics in the order of the Parts, every statement numbered;
  - each statement labelled Proved; Proved under stated hypotheses (with whether they hold where the statement is
    used); Refuted (with the counterexample and the corrected statement); or Known (with citation);
  - each new statement with its complete proof;
  - checked and unchecked statements in separate parts;
  - English, first person plural;
  - where a statement is Grothendieck's, the cote and scan of his page.
- **`RESEARCH_SA22_results.csv`:** one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- **`RESEARCH_SA22_references.bib`:** each entry marked opened / not opened.
- **`RESEARCH_SA22_report.md`:**
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

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. The attached study's statements carry ids such as SA22-6 with their pages; keep them. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is.
- Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a
  display or a line of text.
- Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again.
- Then render pages to images and look at them: every page that had an overflow, and a sample spread over the
  document.
- Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA22_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
