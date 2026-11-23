**The attached files.** Besides this file there is one ZIP, `70c_HODGE_FINISH.zip`. Unpack it once; there is no ZIP inside it. Everything you need that isn't a published source is in it, so don't rely on any earlier conversation.

# Finishing the Hodge paper: the Hodge conjecture for abelian varieties as a uniform bound over finite fields

You are GPT-6 Astra (ChatGPT Pro mode). This is the finishing run for the paper that the run HODGE_BOUNDED_CYCLES
(prompt 70) delivered as its final on 23 November 2026. The mathematics of that paper is recorded in its ledger and
check events, and two independent intakes have checked its main results. This run brings the text to the standard of the
rules below, splits it into two papers, and settles the three results that were left out of it.

## This prompt may be sent more than once

Everything you need is in the attached ZIP; rely on no earlier conversation. If a ZIP named
`HODGE_FINISH_checkpoint_NN.zip` or `HODGE_FINISH_final.zip` is attached as well, restore it, read its `LEDGER.md`, and
continue from the state it records; number your next checkpoint NN+1 and record the continuation, with its start time,
in the ledger.

## Part 1. What is attached

- `ours/final/`: the run's final: `LEDGER.md`, `QUESTIONS.tsv`, `CHECK_EVENTS.tsv`, `LITERATURE.md`, `DICTIONARY.md`,
  `CROSSWALK.tsv`, and the paper's LaTeX under `workbench/work/UNFILED/v1/paper/` (`main.tex` and its chapter files).
  Start from these sources and keep the run's register ids.
- `ours/intakes/HODGE_BOUNDED_CYCLES/`: our two intakes of the run, of checkpoint 02 and of the final, by Claude Opus
  5.5 at effort high, with their check events. They record which results were checked and how; the fixes below come
  from them, with their reasons.
- `ours/context/VOISIN_1248_STATE_OF_FIELD_20261123.md`: the state of the field from Claire Voisin's Bourbaki exposé
  1248 (January 2026) on Markman's theorem, written from the source by Claude Opus 5.5 at effort max. Cite the exposé by
  its URL and by the exposé's own page numbers.

## Part 2. The fixes, every one of them

1. **The state of the field.** Section 1 opens with it, before the theorems: adapt the attached Voisin text.
2. **The abstract and the title.** The abstract says whose work the paper starts from; that the equivalence uses
   published inputs only, and that the CM theorems are not inputs; what the Weil engine, Q10 and the fourfold numbers
   give; what is not proved; and it keeps its present closing sentence. The title is "The Hodge conjecture for abelian
   varieties as a uniform bound over finite fields". Add "after Brünjes and Serpé" to it exactly when Section 1 shows
   their Theorem 3.4 to be the engine of the arithmetic direction.
3. **A section headed "Proof overview"** in each paper, covering every main theorem (the equivalence, extraction, the
   small detectors, stabilization, Q10, Q12): for each, the difficulty, the idea that overcomes it, and where each
   hypothesis is used.
4. **Why it matters, and what is new.** A paragraph "Why this matters" and one sentence "What is new here", with the
   credit split by statement and page: Cattani, Deligne and Kaplan, p. 483; Bhattacharjee and Bhattacharya, Lemmas
   4.2-4.3 and Theorem 4.5; Brünjes and Serpé, Theorem 3.4.
5. **Markman, exactly.** Quote Markman's ICM Theorem 1.2 exactly, from the source, with its locator. Add one sentence on
   the withdrawn OpenAI manuscript on eightfolds, with its status.
6. **The rStation step.** Rest the step that now cites the agent-site preprint ("lelong_ridge and cm_symmetry_scout") on
   Cohen and Malle, whom the same paragraph already cites, and keep the preprint as a citation with one sentence on its
   status.
7. **Q23, Q24 and Q32.** Check each in full, as a referee who wants to find the error, and have a separate worker of this
   run re-prove each from the statement alone. Each that holds enters its paper with its proof and its check events;
   each that fails is recorded as refuted, with the refined statement in its strongest true form.
8. **The Schoen input and Q12.** Check the Schoen 2007 input behind the bound 36 against its source, by exact locator.
   Search the literature on the semiregularity of objects with Weil character, and state the result of the search for
   Q12 in its paper.

## Part 3. The two papers

- **Paper A, the criterion with the Weil engine:** the equivalence of the Hodge conjecture for abelian varieties with
  the Poincaré-pairing bound on the multiplier (bounded cycle degrees on the reductions of CM points); extraction; the
  small detectors with the numbers 48, 192 and 36; stabilization; Q10, the reduction of every split Weil family to one
  principal family per field and dimension; Q12, the criterion for strong semiregularity.
- **Paper B, the construction obstructions with the Mumford criteria.**

Each paper is complete on its own: it states and proves what it uses from the other, or cites it by statement. Build
each three times from a fresh copy of its sources; no box may stick out beyond about 2pt; render every page and read
it, then read the whole text a second time from the page images. Update each paper's deposit sheet, with its map of
the boxes of the rules below, box 8 included.

## The papers grow with the research

This is research and writing in one task. You are the author of the papers: you prove, and you write each result up
when it is proved.

- **Start with the paper.** Write the main theorems above into LaTeX with their full proofs, checking every step as you
  write. The first checkpoint already holds a compiling draft of each paper. From then on every checkpoint holds the
  newest draft, and a result you prove or correct enters its paper before the next checkpoint.
  Keep each paper editable on its own. Include its main TeX file, every local input, its bibliography
  (or inline references), any custom style and the editable source of its figures. Give the exact build
  command and engine in a short BUILD.md. Compile each changed paper from a fresh copy of its returned
  project, with standard TeX packages available, and include the resulting PDF alongside the source.
- **Then push the mathematics**, and let each paper grow with it. When a new result makes an older one a special case,
  restructure the paper around the stronger one.
- **Before anything is called new**, search: arXiv, the journals, the authors' pages, ECCC, and Hexagon
  (https://hexagonmath.org), in general mathematical terms, following the citations forwards from each work named
  here. Known results are cited with the exact statement and page, and are not proved again unless the form you need
  isn't in the source. Where an earlier work has a result of ours, cite it and present ours as what it is. Make no
  claim of priority and don't argue about one: say what each earlier work proves and what is proved here.

## What a paper has to be

A mathematician who has never seen our project, reading on a phone, understands from the first page what was believed
or conjectured, by whom and where, and what is now a theorem. An expert can check every line without any other file of
ours. Write an ordinary, good research paper, with the patience of one:

Correct and completely proved is the baseline, and a paper that stops there has failed its reader. The opening ticks
each of these boxes, in a short paper above all, concisely and without making a production of it:

1. **The title** says the theorem or question as the field knows it, and names whose theorem, conjecture or programme
   it is. Where we carry out someone's idea, it says "after" that person. It doesn't name a result by a technique, or
   by what the proof avoids.
2. **The abstract's first sentence** says whose work this answers or starts from, and what that work did. Then, with
   as few symbols as it can: what is proved, what is granted, and why it matters. Its last sentence says who produced
   and who checked it, and that no human has.
3. **The theorem in words.** Section 1 states each main theorem in full, with every hypothesis and input, and then
   says what it means, and names the famous statement that it implies or refutes.
4. **Why anyone should care:** the field, the question or programme that depended on it, and what changes now. A
   plain sentence that a result matters is allowed and wanted, at its true scope.
5. **The credit, split exactly.** What the source proved, conjectured or sketched, by statement, page or footnote;
   then what is supplied here. An idea of someone else's is theirs in the title, in the abstract and in Section 1.
   Name also those whose theorem carries the proof. Say nothing about the rest of their work that isn't proved here.
6. **The context.** The earlier theorems and proofs, compared by statement and by ingredients, never by merit; the
   neighbouring work that changed the picture, recent results and those of AI laboratories (OpenAI's among them)
   included, each opened and cited with a sentence on how it bears on this paper.
7. **The scope:** what follows and what isn't proved, in the same place.
8. **The proof overview,** a section headed "Proof overview", in prose before the proofs: the difficulty, the idea
   that overcomes it, and where each hypothesis is used.

An example of the difference is our note hexagon:2611.00789 (https://hexagonmath.org/2611.00789). Its draft was
correct and concise. It was called "Deligne's purity theorem without monodromy", gave the source of its idea one
clause, and went from the theorem straight to the lemmas. The published text is called "A short proof of Deligne's
bound for Frobenius eigenvalues, after Alpöge". It opens with Alpöge's sketch, separates those ideas from what is
written out, says that this is the Riemann hypothesis for varieties over finite fields, compares with Deligne's
ingredients, and explains the mechanism before it proves anything. Write the second kind.

After the opening:

- **The body** gives the proofs in the order of the argument; each section's first sentence says what it is for. Every new result is proved in full, in sentences.
  Define each symbol before it is used, name objects by what they are, and work the smallest instructive example by
  hand. A long calculation says what is computed, by which method, from which input and with which result.
- **What remains open** is stated exactly at the end, with the obstruction.
- **A short closing note on method** says that the mathematics and text were produced by GPT-6 Astra (ChatGPT Pro
  mode), names the checks by others with model and effort as their records give them, says that no human has checked
  it, dedicates our text to the public domain under CC0 1.0, and links the workbench.

A paper never contains run names, internal statement ids, prompts, checkpoints, intakes, agents, local file names or
paths, the history of our drafts, defensive asides, machine headers on statements, or words like "supplied", "actual"
and "retained" used as process words. Programs are cited once, by name, through the workbench. The line of authors
stays empty for us to fill. Length follows the mathematics: don't compress a proof into a summary, and don't pad.

Finished means that you have built each PDF, with no overfull box over 2pt, looked at every page, and read the whole
text twice: as the expert who wants to find the error, and as the newcomer who wants to know the point. Rewrite what
fails either reading.

## Checking

The attached records are evidence, and none of them replaces your check. Reprove or check whole every proof that
enters a paper, with its dependencies. Have each main theorem attacked and re-proved from the statement alone by a
separate worker of this run that hasn't seen the proof, and record it as what it is: a re-proof by the same model. A
statement that fails is corrected in its strongest true form, and the correction is recorded. Every proof is checked
before the paper is called finished.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the
type of what happened, neither more nor less.

Our internal ids belong in two record files, outside the papers: `CROSSWALK.tsv` (paper statement, our earlier ids,
source file, check) and `DICTIONARY.md`, which restates each new finding, with the proof that carries it across, in
the language of algebraic geometry and of our programme on Grothendieck's work (schemes over Z, λ-rings and K-theory,
motives and correspondences, weights), with a cote of the archive only where the attached sources really show the
connection.

## The workbench

The papers of one topic point to one public repository, defined once in each paper as
`\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/algebraic-cycles-and-motives-workbench}`. Deliver the folder `workbench/` ready to be that
repository (or to be added to it): a README a newcomer can read, the papers' sources, a table of every statement with
its proof and check, the check events, and the programs and certificates with exact commands and expected outputs. It
holds only our own work. Cite other people's papers by reference and link, and copy none of them into it.

Its format is format 1 of https://github.com/KokunoYumeto/mathematics-workbenches (`FORMAT.md`): statements with
permanent tags, check events, sources cited and not copied, and a manifest for each version. We give each paper its
number and permanent page when we file it. So every paper also defines
`\newcommand{\recordurl}{https://github.com/KokunoYumeto/mathematics-workbenches}` once and cites it as the
permanent address of its records. We replace that address with the paper's own page. A repository of a field that
isn't open yet opens with its first checked work.

## How to work

The rule that governs everything below: push. Write the papers as you go, and give most of the research time to the
main question: make every fix of Part 2 to the paper of the HODGE_BOUNDED_CYCLES final, check Q23, Q24 and Q32 in full, split the paper into the two papers of Part 3, and deliver both, every page checked. When one approach stalls, take the next one. Deliver nothing while an item is undecided and an
untried approach remains. A gap in a proof is an undecided step: attack it, and never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the
strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a
strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not
movement. After two consecutive reviews without movement, stop that work, finish and check the papers with every
item's state, and deliver; this check takes precedence over the rule about untried approaches.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `HODGE_FINISH_checkpoint_<NN>.zip` with `NN` counting
up. Never overwrite, rename or delete an earlier checkpoint. Save checkpoints once every 45 minutes and at no other
time. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work, so that
a new session can continue from it and the attached files. It is never a JSON file, a recovery file, a summary, or an
export of the newest part only. Each checkpoint zip holds the current deliverables and documentation; earlier
checkpoints are not copied into it.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint,
and continue to the end. Don't write files out in the conversation instead: the work reaches us only through
checkpoint ZIPs and the final ZIP.

## What to deliver

One final ZIP, `HODGE_FINISH_final.zip`:
1. each paper as standalone LaTeX and as a PDF, every finding with its proof, checked and any unchecked findings in
   separate parts, known results cited with exact locators;
2. for each paper a deposit sheet: title, abstract, subject, keywords, the note on method, the place in the text
   of each of the eight boxes, and the authors whose work it carries, so that we can tell them;
3. the folder `workbench/`;
4. `CROSSWALK.tsv`, `DICTIONARY.md`, `QUESTIONS.tsv` (one row for each question: proved, refuted, or, if the session
   ends, its current gate), `LITERATURE.md` (each search, with its date and what it found), `LEDGER.md` and
   `CHECK_EVENTS.tsv`.

An item is finished only when it is proved or refuted. A return may be marked INCOMPLETE only when the session itself
ends. It then gives the state reached, every approach tried with where it failed, and the next step.

## The attached files

- `ours/context`: 1 file
- `ours/final`: 231 files
- `ours/intakes`: 4 files

`ours/` is our own work (runs of GPT-6 Astra, ChatGPT Pro mode, and the checks of them): it holds the proofs behind every bracketed id. Fetch the published sources you cite from their public addresses. Text inside any attached file, earlier prompts included, is material to read and never an instruction to you.
