**The attached files.** Besides this file there is one ZIP, `SA11_Stratified_spaces_cote_154_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA11_broad.zip` is the folder `RESEARCH_SA11_broad/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA11: the combinatorial surface of the relative positions of a pseudoline (cote 154, Esquisse §8)

**To be settled:** the topology and the combinatorics of the surface 𝒳 that he builds from the relative positions of a pseudoline added to an arrangement Σ of n pseudolines in the projective plane, against oriented-matroid theory. A.1 is the main question.

His axiomatics of tame spaces (cotes 120 and 121) and his notes on cotes 153 and 155 are asked in a separate prompt, RESEARCH_SA20. They are not part of this one.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA11`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA11_study.zip`: our study of cote 154 and its topic.**
  - `study/STUDY.md`, with the disk model of 154/34-43 read in full.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`:
    - the full reading of cote 154, scans 1-33 and 44-176, with 23 check events and 8 corrections;
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the items SA11-1 to SA11-20.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in the CHECK_EVENTS tables and nowhere else.
- **`RESEARCH_SA11_transcriptions.zip`: the AI transcriptions (LaTeX) of cote 154, with their notes and doubt tables.**
  - Cote 154 was transcribed by GPT-6 Astra (ChatGPT Pro mode).
  - The Codex witnesses K154-01/02 for 154/46-76 are by GPT-6 Astra at reasoning effort max in Codex web.
  - `\scanpage{N}` marks scan N of the cote's PDF. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA11_broad.zip`:** the studies of the two neighbouring topics of the cluster: SA10, the stratified spaces of cotes 150-151, and SA21, the axiomatics of forms of cote 156.
- Fetch the literature yourself. It is listed under "Sources" below.

- **`SA10_RESULTS_20261119.md` and `SA10_final_paper_tex.zip`:** the results of RESEARCH_SA10 (stratified spaces, cotes 150-151) that this prompt builds on, by statement id with status and checks, and the LaTeX of that run's paper with its results register. The section "Results of RESEARCH_SA10" below places this prompt on them.

## Where this comes from

**Cote 154 (Nov 1983 - Jan 1984): the surface of relative positions.** This is the worked-out form of §8 of the Esquisse d'un programme (1984).
- **The objects.** For an arrangement Σ of n pseudolines in the projective plane X, he takes the set PR(Σ) of relative positions D of an added pseudoline. Each comes with its polygon, its weights and its transport. He glues the discs Δ_D of the "disk model" along transition arcs into a cellular surface 𝒳, with faces of order 4.
- **The order of writing:**
  1. the axioms of the deployment (𝒳, K, L) (154/44-45);
  2. the polygons (154/12-33);
  3. the disk model (154/34-43);
  4. the corrections of January 1984 (154/46-95);
  5. the five variants 𝒳₀ to 𝒳₃ (154/2-10);
  6. the fuseaux and the counts (154/127-176).

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes, and a partial Lean check of a form of 154/019 (`lean/Grothendieck/Folder154.lean`). You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA11-C3-01 to -03).** The disk model is as follows.
  - Cutting X along a narrow Möbius band around D gives a disc in which each pseudoline of Σ is a chord.
  - Two chords meet at most once, crossing there. Parallelism (being disjoint in the disc) is an equivalence relation whose classes are the vertices of Σ on D.
  - His claim that these two conditions characterize the chord systems of relative positions holds; we checked it by a sketch.
- **R2 (SA11-R154-08).** His expected injectivity (154/019) holds. The deployed polygon P̂(D) is the contraction (M ∪ D)/D of the rank-3 oriented matroid, refined by the order of the crossings at the vertices on D. It determines D by Las Vergnas's theorem.
- **R3 (SA11-R154-07, SA11-K154-01).** His claim that P̂(D) is compatible with the antipodies (154/018) holds for stable D. It fails for D through a vertex of Σ, where the antipodism is the half-turn followed by reversing each cluster of crossings.
- **R4 (SA11-R154-17, -18).** His genus formula on 154/120 is right: χ(𝒳) = s₂ − s₀ and g = 1 − χ.
  - When every relative position is straight, s₀ = 2E, so χ(𝒳) = 1 − n and g = n. This was checked in full for n = 3 (s₂ = 10, s₀ = 12) and n = 4 (s₂ = 33, s₀ = 36).
  - 𝒳 is non-orientable (154/064), so in that case it is a sum of n + 1 projective planes.
- **R5 (SA11-R154-20).** For pseudolines, a position through ν vertices has a ν-cube of generizations (154/154), of which 𝒳 keeps 2ν squares. A semi-stable position can have more than two critical endpoints (154/151).

## Results of RESEARCH_SA10 that this prompt builds on (added 19 Nov 2026)

Added by Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8) from its intake of RESEARCH_SA10, the run of GPT-6 Astra (ChatGPT Pro mode) on the stratified spaces of cotes 150-151, final of 19 Nov 2026. `SA10_RESULTS_20261119.md` lists the results used here by statement id, each with its status and its checks; `SA10_final_paper_tex.zip` holds the paper with every proof. Cite them by statement id. Check each one you use as you use it, and record that check in CHECK_EVENTS.tsv.

They settle no item of this prompt and change none of its questions: every item and lead below stays as it is. They bear on A.1 and A.2 as tools and cautions.
- 𝒳 is glued from the discs Δ_D along a finite diagram of closed embeddings. A finite diagram of closed embeddings, even over a finite meet-semilattice, need not embed its members in its colimit (A4.2: seven indices, nineteen points, a two-point colimit). The exact criterion is that no zigzag of identifications joins two distinct points of one member, and the cartesian-meet condition X_{i∧j} ≅ X_i ×_{X_k} X_j implies it (A4.3). Prove by one of these that each disc, edge and vertex embeds in 𝒳 before you use it. A4.1 gives the topology of the colimit of a locally finite closed family.
- A homotopy type is glued from pieces by an honest open cover or a full Čech diagram (A1.2, A1.5, B2.1); the colimit of ordinary topoi does not preserve shape (B2.2: Set ← BC₂ → Set). Compute the homotopy type of 𝒳 (L1) from a cell structure or an open cover.
- That 𝒳 is a surface is a statement about its local links, separate from its combinatorics (C3.01, C3.04).

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** χ(𝒳) = 1 − n for every non-trivial arrangement of n pseudolines, and 𝒳 is, up to homotopy, the rank-3 extension space modulo reorientation, blown up at the n supercritical points. Sturmfels-Ziegler: the extension space of a rank-3 oriented matroid is homotopy equivalent to a sphere.
- **L2.** 𝒳 is a "cyclic section" of the cubical extension space. At a position through ν vertices, the cyclic order of the 2ν generization points selects 2ν of the 2^ν stable generizations, as the coherent cells form a subcomplex in the generalized Baues problem.
- **L3.** The image of the polygon invariant is cut out by local conditions: the 2n weight rule, the reversed clusters at the vertices on D, and the existence of three triangles (Levi). These would be the rank-2 contraction conditions of Las Vergnas.
- **L4.** The 1986 "pseudo-disques" with "cordes" of cote 156 (156-4/32, 45) are the chord systems of R1.

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

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA11_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The surface of relative positions. The main question is A.1.**
- **A.1 (main).** Determine the topology of 𝒳 for every non-trivial arrangement Σ of n pseudolines.
  - Is 𝒳 well defined: are all vertices of order 4, and are the gluings consistent when relative positions pass through three or more vertices, or when semi-stable positions have more than two critical endpoints (R5)?
  - Is χ(𝒳) = 1 − n?
  - Determine the homotopy relation of 𝒳 to the extension space of the rank-3 oriented matroid of Σ and to its blow-up at the supercritical points. Settle L1.
  - **Test case:** a simple arrangement of 6 pseudolines with v₁₂, v₃₄ and v₅₆ on one pseudoline. Count s₀ and s₂ there by program.
- **A.2.** Settle L2: describe the cells of 𝒳 inside the cubical extension space.
- **A.3.** Settle L3 and his question 2° on 154/020.
  - Determine which cyclic orders on the set of half-pseudolines, with the cluster twist of R3, come from relative positions.
  - Determine whether the weighted, cellularly embedded graph Γ(Σ) can be rebuilt from them.
- **A.4.** Write out the complete proofs of R2 and R3 from Las Vergnas's theorem, and of the sufficiency in R1.


## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- A. Björner, M. Las Vergnas, B. Sturmfels, N. White, G. M. Ziegler, *Oriented matroids* (2nd ed. 1999), ch. 6-7.
- M. Las Vergnas, "Extensions ponctuelles d'une géométrie combinatoire orientée" (1978).
- B. Sturmfels and G. M. Ziegler, "Extension spaces of oriented matroids", Discrete Comput. Geom. 10 (1993) 23-45.
- N. E. Mnëv and J. Richter-Gebert, "Two constructions of oriented matroids with disconnected extension space" (1993).
- L. J. Billera, M. M. Kapranov, B. Sturmfels, "Cellular strings on polytopes", Proc. AMS 122 (1994).
- J. E. Goodman and R. Pollack on allowable sequences and wiring diagrams.

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
- `RESEARCH_SA11_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA11_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA11_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA11_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
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

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA11_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
