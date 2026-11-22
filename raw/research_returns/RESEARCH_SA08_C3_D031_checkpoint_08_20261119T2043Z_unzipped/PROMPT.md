# RESEARCH_SA08_C3_D031: Grothendieck's uniqueness conjecture for admissible generalized de Rham theories over Z (cote 136, scans 117-121), and a check of Caradot-Lin, arXiv:2511.22614v4, Proposition 3.10

**What is to be settled, in two Parts:**
- **A.** His uniqueness conjecture for admissible generalized de Rham theories (cote 136, scans 117-121), over Z: the
  one open mathematical item of RESEARCH_SA08, its C.3. A is the main question.
- **B.** A check of RESEARCH_SA08's refutation of Proposition 3.10 of A. Caradot and Z. Lin, "Differential graded
  algebras with divided powers and homotopy Lie algebras", arXiv:2511.22614v4 (its statement D-031).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA08_C3_D031`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a34c04448e8299803, on 19 Nov 2026, from its
intakes of RESEARCH_SA08 and RESEARCH_SA09. The main session (Claude Opus 5.5 at effort max) decided on this prompt.

## What is attached

- **`RESEARCH_SA08_C3_D031_inputs.zip`: the parts of two research runs that the items need, and our intakes of them.**
  - `SA08/`: from the final of RESEARCH_SA08 (GPT-6 Astra, ChatGPT Pro mode, 19 Nov 2026, 10:27 UTC), the TeX
    sections in which every statement named below is proved (`SA08/sections/`); the rows of its results register
    and of its check events for those statements (`RESEARCH_SA08_results_C3_D031.csv`, `CHECK_EVENTS_C3_D031.tsv`);
    the last section of its report, on the gates and the approaches tried (`report_gates.md`); its bibliography; and
    the program and output of the D-031 counterexample (`code/D_lifting_counterexample.py`,
    `logs/D_lifting_counterexample.json`).
  - `SA09/`: from the final of RESEARCH_SA09 (GPT-6 Astra, ChatGPT Pro mode, 19 Nov 2026, 11:46 UTC), the sections
    A2 and A3 and the rows A2.1-A3.5 of its results register.
  - `intakes/`: our intakes of both finals, with their check events, by Claude Opus 5.5 at effort max (Anthropic).
  - `MANIFEST.tsv` gives the origin and SHA-256 of every file.
- **No literature is attached.** Fetch the sources listed under "Sources", preferring the arXiv LaTeX source.

## Where this comes from

RESEARCH_SA08 worked on cote 136 of the Grothendieck archive, his divided-power de Rham complex of 1975-76. It
settled every item but C.3 and stopped under its two-review rule; its report is headed INCOMPLETE. RESEARCH_SA09
worked on cote 137, where he builds the integral framework of the same programme: the walking complex, the universal
cosimplicial object and its Γ-operations. It settled all its items in 43 minutes. Our intakes checked parts of both;
what they checked, and what they did not, is in `intakes/`. Every statement of either run that you use is checked
by you where you use it (Rules of proof, 7). Cite them by statement id: C06, D-031, A3.2, and so on.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most
of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided
step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for all rings proved over
a field or over Q without saying so; a step that replaces a claim by a convenient special case without naming it; a
reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made and carry
doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA08_C3_D031_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The uniqueness conjecture over Z. A is the main question.**
- **A (RESEARCH_SA08's item C.3).** His uniqueness conjecture for admissible generalized de Rham theories (cote 136,
  scans 117-121: "connexe et simplement connexe ?", conjectures a) and b)), over Z. Prove it or refute it over Z,
  with the correct statement proved in its place.
  - **Settled by RESEARCH_SA08.** Strict common-source equalization, the strict form of b), fails over every nonzero
    ring (C07). The special universally flasque category has a contractible nerve (C06); so does the eventual
    admissible category over a Q-algebra under uniform hypotheses (C08). Common sources and terminal localization
    hold for explicit eventual-admissible theories over Z_(p)-algebras and over rings of positive characteristic (C09,
    C10), and for generalized admissible strict PD theories over every ring with finitely many noninvertible rational
    primes (C16, C17).
  - **The item.** Common sources and terminal localization over rings with infinitely many noninvertible primes,
    beginning with Z. Keep the two assertions apart.
  - **The gate, as that run left it.** C30 builds a common source over Z from p-local admissible repairs
    P_p → E_p → A_p, B_p whose first map is an isomorphism below a form degree d_p, with d_p → ∞. C32 builds terminal
    localization in the same way from local repairs of the pair target A ×_k B and of the homotopy equalizer H(f, g).
    C34 weakens the data to the finite form truncations of P with compatible target maps. None of these local
    completions is constructed, and neither their existence nor their necessity is proved.
  - **What was tried, and where it failed** (statement ids of that run):
    - ordinary tensor products: prime-power Tor in unbounded weights (C11);
    - independently marked free PD disks over Z: admissible only for the weight-one disk, and no map to A_N for
      N > 1 (D022, D023);
    - projection-preserving arithmetic gluing with unbounded first flasque weights (C12);
    - the standard tails as an initial family (C13);
    - free linear-disk replacements and free resolutions of the tails (C14, C15);
    - ordinary common-target pushouts: unbounded degree-one cohomology, even rationally (C19);
    - naive PD indecomposables, which are not invariant (C26), and a simple arity-homology pattern (D-032);
    - delayed p-local closures, which come without compatible target maps (C18);
    - the global partial model, which needs floor((d+1)/2)! inverted (C21);
    - automatic extension of a prescribed bar boundary: a counterexample over Z_(2) (C31);
    - adjoining rational halves of odd products (C35);
    - the finite-arity bar extensions (C24, C25, C27-C29, C36), which do not meet infinitely many eventual bounds at
      once;
    - a fixed finitely generated group of operations as the invariant: it cannot detect moving primes (C33);
    - the lifting proposition of Caradot and Lin as stated (D-031; see B).
  - **The new tools, proved by RESEARCH_SA09 on cote 137.** Cote 137 builds the universal cosimplicial object
    C^* = DP(C^•), its Σ-exact universal property and its Γ-operations. RESEARCH_SA09 proved:
    - A2.2: For every commutative ring, relative left-exact functors out of bounded nonnegative finite-free complexes are fully faithfully determined by their disk values; the essential image is the explicit finite-matrix kernel condition;
    - A3.1: Right-adjoint cochain tests R_n are bounded finite free split acyclic and denormalize the walking complex; test category closed under tensor and divided powers;
    - A3.2: Normalized cochains with the full natural Gamma action on the test functor determine and are determined by its tensor/unit/Gamma structure and the cosimplicial function ring Z^X.
    Determine whether they give the common source or the terminal object over Z, or an invariant that separates
    admissible theories.
  - **Where that run's state is:** `SA08/sections/` (the proofs of every statement named here),
    `SA08/RESEARCH_SA08_results_C3_D031.csv`, `SA08/CHECK_EVENTS_C3_D031.tsv` and `SA08/report_gates.md`.

**B. The check of D-031.**
- **B (a check carried over from RESEARCH_SA08).** That run refutes Proposition 3.10 of A. Caradot and Z. Lin,
  "Differential graded algebras with divided powers and homotopy Lie algebras", arXiv:2511.22614v4: its statement
  D-031, "unrestricted termwise-free chain-map lifting is false", proved in `SA08/sections/D_rejected_lifting_source.tex`,
  with the program `SA08/code/D_lifting_counterexample.py` and its output `SA08/logs/D_lifting_counterexample.json`.
  The counterexample is an explicit square-zero PD DGA projection from an identity disk to its lower-degree sphere,
  whose closed generator has no chain lift. The run states that their Theorem 3.15, which assumes an acyclic target
  resolution, is not refuted. Check this independently:
  - fetch the arXiv LaTeX source of v4 and quote, with section, page and equation numbers, the exact statement of
    Proposition 3.10, the definitions it uses (termwise freeness, Section 2.1) and the degree conventions;
  - verify every hypothesis of Proposition 3.10 on the counterexample, and the impossibility of the lift, by hand and
    by a program of your own;
  - determine which results of that paper use Proposition 3.10, Theorem 3.15 included, and whether the counterexample
    reaches them;
  - determine the hypothesis under which the lifting of Proposition 3.10 holds (an acyclic or cofibrant one, for
    instance), and prove that corrected statement.
  The item is done when the refutation is confirmed with these locators and the corrected statement is proved, or
  when the refutation is shown wrong at an exact step. Record the check under the statement id D-031 in
  CHECK_EVENTS.tsv.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- A. Caradot and Z. Lin, "Differential graded algebras with divided powers and homotopy Lie algebras",
  arXiv:2511.22614v4: Section 2.1, Proposition 3.10, Theorem 3.15, and every result that uses Proposition 3.10 (B).
- For A: the works that RESEARCH_SA08 cites in its sections, listed in `SA08/RESEARCH_SA08_references.bib` with that
  run's notes on which it opened; G. Horel, "Binomial rings and homotopy theory"; M. Mandell, "Cochains and homotopy
  type", Publ. Math. IHÉS 103 (2006); SGA 4, exposé V (flasque sheaves).

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the ring k and its torsion, the PD triple, the class of simplicial sets,
   gradings and completions, the weight convention). Do not replace it by a convenient special case. If you prove a
   special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it lives (graded modules over k{T}, simplicial
   modules, cosimplicial algebras, D(k)), and each extra property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "pass to the completion") comes with its comparison map and a proof
   that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism of graded algebras; isomorphism of k{T}-modules
   only; quasi-isomorphism; homotopy equivalence of simplicial modules; isomorphism in D(k) as against an isomorphism
   with products.
5. Check the edge cases in scope: characteristic 2 and 3 and torsion in k; k not flat over Z; infinite simplicial sets
   and cochains of unbounded weight against finite weights; graded against ungraded modules; weight 0 and the endpoint
   i = p; t = 0.
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
- `RESEARCH_SA08_C3_D031_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA08_C3_D031_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA08_C3_D031_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA08_C3_D031_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted,
  with the statement number); then what you read, what you computed (every program with its scope, counts and run time),
  and every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry ids such as S3-136-002-141-CE008 and CE-A12; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA08_C3_D031_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
