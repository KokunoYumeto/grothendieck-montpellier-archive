**The attached files.** Besides this file there is one ZIP, `SA21_Formes_cote_156_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA21_broad.zip` is the folder `RESEARCH_SA21_broad/`), so there is nothing more to unpack; every other file is at the top level under its own name.

**The same files in this Space.** Every file of `SA21_Formes_cote_156_night.zip` may also be in this Space's files, flat, each named `P006__` followed by its file name; `P006__SPACE_INDEX.tsv` gives, for each such name, its path inside the ZIP. Where they are there, use them as you would the unpacked ZIP; where a Space file and the ZIP differ, the ZIP decides; where they are not there, unpack the ZIP.

# RESEARCH_SA21: Grothendieck's axiomatics of forms of 1986 (cote 156): the supports and the orthomodular law, the axiom systems, and the maquettes

**To be settled, in three Parts:**
- **A.** The lattices of supports of his "ateliers" and "magasins": when they are orthomodular, when Boolean, and what his own theorems on them become. A.1 is the main question.
- **B.** His successive axiom systems for "contrées", ateliers and magasins: what implies what, what replaces his false axiom C4, the event-structure dictionary, and the o-minimal model.
- **C.** His oriented "maquettes" in every dimension, against regular cell complexes.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA21`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA21_study.zip`: our study of cote 156.**
  - `study/STUDY.md`. §0 gives the state after the readings, §2 the reading of 156-4 in full, §5 the later parts, and at the end the readers' summaries.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the full readings of 156-3, 156-5, 156-6, 156-7 (two readings), 156-8 and 156-9, each with its tables, and the checking programs `156-5_sorite_checks.py` and `156-8_checks.py`.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the topic's items SA21-1 to SA21-15.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA21_transcriptions.zip`: the AI transcriptions (LaTeX) of cote 156.**
  - 156-1 and 156-2 by GPT-6 Astra (ChatGPT Pro mode), with notes and doubts.
  - 156-3 to 156-9 by GPT-6 Astra at reasoning effort max in Codex web, one file per folder of 4 to 12 scans, with the doubts tables.
  - `\scanpage{N}` marks scan N of the cote's PDF; the archive's pencil page is N−1. The transcriptions carry `\unsure{a|b}` marks.
  - The readings above decided some readings on the scan images, and their CORRECTIONS tables give them. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA21_literature.zip`:** the LaTeX source of L. Román, "Orthomodular lattices and quantales" (arXiv math/0211133).
  - Fetch the other sources yourself. They are listed under "Sources" below.

## Where this comes from

**The pages.** Cote 156 of the Grothendieck archive at the University of Montpellier ("Vers une géométrie des formes") holds nine parts of handwritten notes, about 700 scans, from 8 June to 15 July 1986. In them Grothendieck axiomatizes "tame" geometric forms without points:
1. the contrées of 156-4, with figures, multistrates, lieux, refinement ≪, subdivision and the supports Σ;
2. the ateliers of 156-6 and 156-7;
3. the magasins of 156-8, with the relation |∘| ("intérieurement disjoints") as primitive;
4. in 156-9, after he swaps the two words on 9 July, the ateliers again, with the supports as ortholattices.

156-3 and 156-5 are the one-dimensional and the set-theoretic models.

**Our reading of them.** Sweep 3 of our horizontal reading (18-19 Nov 2026) read these parts:
- 156-4 in full, by a6d42bf6;
- 156-3, 156-5, 156-6, 156-7 and 156-8 in full, by readers (all Claude Opus 5.5 at effort max);
- 156-9 in full in two rounds, except the drawings of scan 112.

**Other work.** We know of no published study of these pages; check this. Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA21-R8-25).** In a faithful magasin, Σ_M is the algebra of regular open sets of the Alexandrov topology of (M, ≪°). It is a complete Boolean algebra, and Axiome supp 1 (156-8/88) holds.
- **R2 (156-9 reading; SA21-R9-10).** Under divisibility and Mag L2, the magasin is faithful exactly when Σ is Boolean with the lieux as distinct atoms. The plain form "Σ distributive ⇔ faithful" is false: two lieux that are not disjoint give Σ = {∅, M}.
- **R3 (SA21-R9-05 to -08).** His "spatios" (156-9/78-80) are complete ortholattices.
  - His Lemma 1 and Corollary 1 (156-9/109-111) and his "axiome des supports" (156-9/117) are the orthomodular law, for the spatial figures.
  - The law fails on the hexagon O₆, which arises from the fence a′ < a > b < b′; the smallest counterexample has 6 elements.
  - MO₂ is orthomodular but not Boolean.
- **R4.** The support lattice is not distributive in general: his own counterexample is the "ficelle à deux brins" (156-7/82-84).
  - His formal Lemma of 156-7/97-99 is the orthomodular law, and it is false: see the path A′–A–B–B′.
  - Σ ≅ P(L) when the disjointness of lieux is "≠".
- **R5 (SA21-K7b-15, SA21-R7b-21).** The Théorème of 156-7/94 is false under all its hypotheses: relative complements S_{A−B} = S_A ∧ C(S_B), and commutation with infima.
  - An eight-element atelier with a seven-lieu disjointness graph satisfies L1-L3, CL(spac), At D, At supp and At supp 1, and both conclusions fail.
  - The theorem holds where distinct lieux are disjoint.
- **R6 (SA21-K5-01).** 156-4's axiom C4 fails in the set-theoretic model Fig(L) of 156-5: the multistrates have 3 components on 2 points and 5 on 3. His claim on 156-5/13-15 that C4 "est automatique" is false.
- **R7 (156-6 reading).** At 13, "l'axiome du support", makes subdivision equal to maximal refinement. The induced refinement is an infimum for ≪; in 156-6 this is a theorem, where 156-4 had it as an axiom.
- **R8 (SA21-R8-01 to -08).** Mag 1-4 (156-8/8) imply the compatibility-disjunction axioms of 156-6 and 156-7 and the gluing of refinements.
  - The weakened Mag 4′ of 28 June is too weak (maquette countermodel).
  - The Proposition-Scholie of 156-8/16-17 lacks the transitivity of ≪°. There is a five-element countermodel, and the ≪°-form repairs it.
- **R9 (SA21-R8-32, -33).** Oriented maquettes:
  - in dimension ≤ 1 they are Serre's graphs;
  - in dimension 2 they are Serre graphs with 2-cells whose boundary is a vertex-disjoint union of directed cycles;
  - with "∂X connected" added, they are the 2-complexes whose cells are attached along closed edge paths through no vertex twice.
- **R10 (SA21-K7-03).** "Polyédral + At simp 1" (156-7/14-15) does not characterize simplices: the face poset of a square satisfies both.
- **R11 (156-3 reading).** On a totally ordered tronçon L, the tame parts Mod(L) are exactly the finite unions of points and open intervals, the definable sets of the o-minimal structure (L, <).
- **R12 (SA21-C3-05).** The finite contrées of 156-4/62 are the triples (M, ≤, R) with M_{≤x} finite and R reflexive, symmetric and closed downward. Their figures are the finite downward-closed R-cliques.
- **R14 (reader C, round 2: SA21-R9b-01 to -29, SA21-K9b-01 to -09).**
  - Axiome supp 1 holds in the magasin of an ordered set: he proves it for figures inside one flag (156-9/21-22), and it held for all 4,724 figures of the magasins of the connected orders with at most 5 elements.
  - His duality cosupp°Φ = Omb°Φ* (156-9/16) holds.
  - His Question of 156-9/3 holds for magasins of connected ordered sets and fails for local ateliers in general (a path of four lieux; twin lieux).
  - For the comparability disjoncteur of an ordered set, cograph ⇒ orthomodular is proved, and the converse fails: on 5 vertices, 60 non-cographs have orthomodular Σ, one with Σ = 2³.
  - His Lemme 1 of 156-9/72 is false, and his own Prop 4 repairs it.
- **R13 (156-8/90-127, 156-9/5-16).** The magasin of an ordered set L has points and intervals, with the positional order a < I_{a,b} < b.
  - |∘| is the comparability of that order, and the finite figures are the flags of the positional order.
  - It satisfies Mag 1-4 for every L. It is faithful exactly when L is total.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** The finite contrées of R12 are exactly the prime event structures with finite causes (Nielsen-Plotkin-Winskel), with figures as the finite configurations. Refinement, subdivision and Σ become notions of the domain of configurations.
- **L2 (replaces the cograph hunch, which R14 refutes as an equivalence).** For an ordered set, the support lattice of its comparability disjoncteur is orthomodular exactly when every induced fence N lies under a "repair", that is, when the comparability graph is a Dacey graph in Sumner's sense (D. P. Sumner, "Dacey graphs", J. Austral. Math. Soc. 18 (1974)).
- **L3.** In magasins with cords and strands, the failure of distributivity of Σ is measured exactly by the pairs of distinct lieux that are not disjoint.
- **L4.** Oriented maquettes in which every interval of length 2 is a signed diamond and the link of each cell is connected are the face posets of regular CW complexes with an orientation of each cell, after loops are excluded.
- **L5.** The o-minimal model:
  - in an o-minimal structure, the definable cells (or the definable stratifications with the frontier condition) form an atelier that is faithful, so Σ is Boolean by R1;
  - it is "modérée" in the sense of 156-4/70 (any two subdivisions have a common refinement), by the definable triangulation theorem.
- **L6.** Under Mag 1-4, every "facultatif" axiom of 156-6 and 156-7 except At L1, At supp and At 13 is a theorem.
- **L7.** His spatios and their "disjoncteurs" (156-9/61-108) are the orthogonality spaces of Foulis and Randall and of Dacey, and his correspondences of disjoncteurs are their morphisms.

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

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA21_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The supports and the orthomodular law. The main question is A.1.**
- **A.1 (main).** Determine exactly which ordered sets L have an orthomodular support lattice, and exactly which have a Boolean one. Prove both directions of each condition.
  - **For the comparability disjoncteur of L.** R14 gives cograph ⇒ orthomodular, and refutes the converse. Settle L2.
  - **For the magasin M(L) with its segments (R13).** Axiome supp 1 holds there (R14). Decide whether the whole Σ_M is orthomodular.
  - **His 10-element counterexample of 156-9/113** ("Card Σ = 10"). Reconstruct it and check it; the transcribed arrows do not form a lattice.
- **A.2.** Determine the class of magasins satisfying Mag 1-4, Mag L2 and divisibility whose support lattice is orthomodular.
  - Prove or refute, in that generality, that Axiome supp 1 (156-8/88) is equivalent to the orthomodular law for the spatial figures (156-9/117).
  - His margin "Oui !" on 156-8/89 says the axiom fails for some disjunctive magmas, without an example on the page. Give such a magma, or prove that none exists.
- **A.3.** His Question of 156-9/3 asks whether supp°x is an atom of Σ* = Σ ∖ {0} for every lieu x. It holds in faithful divisible magasins and in the magasins of connected ordered sets, and it fails for local ateliers in general (R14). Determine exactly the class of ateliers in which it holds.
- **A.4.** Determine exactly the class of ateliers in which the Théorème of 156-7/94 holds (R5). Settle L3.
- **A.5.** His question of 156-8/88: give a faithful support function that is not fully faithful, or prove that none exists.

**B. The axiom systems.**
- **B.1.** Write every axiom system of cote 156 side by side, with each implication between them proved and each non-implication shown by a model:
  - 156-4: Cont 1-5, C1-C8₀;
  - 156-6: At 1-At 14;
  - 156-7: At CD, At C, At D, At L1-L3, CL, At supp;
  - 156-8: Mag 1-4, Mag 1′-4′, Mog L1-L2, Mog div 3, At 1-At 5, At Fil;
  - 156-9: At 1-4 after the swap of names, At spat 1-3.

  Settle the open implications:
  - At 9_Σ + At 10 ⇒ At 12 (156-6);
  - the uniqueness in At 14 bis (156-6/88: "Je présume qu'on doit pouvoir prouver qu'un tel F′ est unique");
  - the converse of the Théorème-Scholie of 156-6/29-34;
  - L6.
- **B.2.** C4 is false in Fig(L) (R6). Determine the true connectedness statement that holds in Fig(L) and in the o-minimal model of B.4, and prove it.
- **B.3.** Prove or refute L1. If it holds, translate refinement, subdivision and Σ into the theory of event structures and domains. If it fails, determine the class of event structures that the finite contrées are.
- **B.4.** Settle L5.
  - For an o-minimal expansion of a real closed field and a definable set X, define the atelier of definable cells, or of definable stratifications with the frontier condition, of X.
  - Prove which of the axioms of B.1 it satisfies, that it is faithful, and that it is "modérée". Cite the triangulation and refinement theorems you use with exact locators.

**C. The maquettes.**
- **C.1.** Settle L4. Determine the axiom on oriented maquettes (Magor 1-6, ≪° = id, |∘| = ≠, 156-8/4-6) that gives connected cell boundaries. Prove that with it the oriented maquettes of every dimension are exactly the face posets of regular CW complexes with oriented cells, after loops are excluded. Where this is false, give the correct statement with its proof.
- **C.2.** Place within C.1 his "ateliers polyédraux" and "simpliciaux" (At pol 1 + At simp 1, 156-7/14-15) and the flags of 156-9/5-7. Determine the axiom on a maquette that characterizes simplicial complexes; R10 shows that his does not.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- G. Kalmbach, *Orthomodular lattices* (1983). L. Beran, *Orthomodular lattices: algebraic approach* (1985). The Foulis-Holland theorem.
- M. Nielsen, G. Plotkin, G. Winskel, "Petri nets, event structures and domains, part I", Theoret. Comput. Sci. 13 (1981). G. Winskel, "Event structures", LNCS 255 (1987).
- M. C. McCord, Duke Math. J. 33 (1966). A. Björner, "Posets, regular CW complexes and Bruhat order", European J. Combin. 5 (1984). J. A. Barmak, *Algebraic topology of finite topological spaces and applications*, LNM 2032 (2011).
- L. van den Dries, *Tame topology and o-minimal structures*, LMS Lecture Note Series 248 (1998). M. Shiota, *Geometry of subanalytic and semialgebraic sets* (1997). A. Pillay and C. Steinhorn, "Definable sets in ordered structures I", Trans. AMS 295 (1986).
- T. Gallai, "Transitiv orientierbare Graphen" (1967). D. G. Corneil, H. Lerchs, L. Stewart Burlingham, "Complement reducible graphs" (1981).
- J.-P. Serre, *Arbres, amalgames, SL₂*, Astérisque 46 (1977).
- D. J. Foulis and C. H. Randall, "Operational statistics I" (1972). J. R. Dacey, *Orthomodular spaces* (thesis, 1968).

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
- `RESEARCH_SA21_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA21_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA21_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA21_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
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

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA21_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
