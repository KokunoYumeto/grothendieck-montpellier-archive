# Intake and integration of tonight's research returns: the brief (21 Nov 2026)

**Current intake assignment, 22 November.** Prompt 74 and all SAT_KRONECKER_FINITE_FIELDS returns belong to local Codex. Claude and its field experts should leave these files unopened. See [74_CODEX_INTAKE_OWNER.md](74_CODEX_INTAKE_OWNER.md).

You are launched by the main session (Claude Opus 5.5 at effort max) for the intake of one or two research runs of
20-21 Nov 2026. The runs are GPT-6 Astra (ChatGPT Pro mode). They were built on the two proofs of 20 Nov 2026, and on
P versus NP through geometric complexity theory and Grothendieck's programme. The user (21 Nov): [the user's words, omitted]; [the user's words, omitted]. The aim: the mathematics of each return
is known (what it proves, how, and whether it holds), and it is placed where it belongs in our work.

## The two proofs
- **Alpöge.** L. Alpöge, *Remark*, https://alpo.ge/remark.pdf: RH and GRH for Dirichlet L-functions, formalized in Lean
  (files at `Papors/Chatnotes/Zeta-Function-Foundation/literature/alpoge_rh_20261120/`). Cite it as a theorem.
- **Masullo.** A. M. Masullo, *The Music of the Primes*: a 940-page draft proposing GRH for the Hecke L-functions of
  every number field. It is unrefereed: every consequence of it is conditional. One run reports that its final numbered
  divisor theorem is unfinished.

## Your inputs
- **The return folder.** For each of your runs, the newest folder named `<TAG>_checkpoint_NN_..._unzipped` or
  `<TAG>_final_..._unzipped` in `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\`.
  A filer runs every 90 seconds, so a newer checkpoint may land while you work. Read the newest one present when you
  start, and name it in section 0.
- **What the return holds.** Each return should have:
  - its paper (`<TAG>.tex`, and a PDF if built);
  - `QUESTIONS.tsv`, `LEDGER.md`, `CHECK_EVENTS.tsv` and `IMPLICATIONS.md`.
  A checkpoint holds the work so far. Its run is still going, so say what is settled and what is still moving.
- **The prompt as sent:** `<local>/Documents\TO_SEND\PRO\1_Archive_research_by_topic\SENT\<NN>_<name>\PROMPT.md`.
  Its ZIP holds the attached sources; open only what a check needs.
- **Our related files:**
  - `reports_20261120\alpoge_rh\bridges\` (QUESTIONS.tsv, LEDGER.md, IMPLICATIONS.md);
  - `reports_20261120\alpoge_rh\bridges\FABLE_PROGRAM_SUGGESTIONS_20261120.md`;
  - `reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`;
  - the intakes of 20 Nov in `results_register\horizontal\sweep3\` and `field_experts\intake_20261120\intakes\`.

## What to do
1. **Read the main results first**, each with its proof in full, then the rest. The main results are the findings on
   the prompt's main question and the findings other findings depend on.
2. **Give each finding (by the run's statement id) the check it actually received**, in the terms of the check rubric:
   - a targeted proof check, confirmed;
   - a gap: where it is and what is missing;
   - refuted: with a counterexample or the false step;
   - or not read in full, with what you did read.

   Check a known result against its source by an exact locator.
3. **Say what is new**: against the literature, against the other runs of tonight, and against our own results, with
   citations.
4. **Check the scope of every use of the two proofs.** For each statement, say whether it uses:
   - GRH for Dirichlet L-functions (Alpöge, a theorem);
   - GRH for Hecke L-functions or Dedekind zeta functions of non-abelian fields (Masullo, conditional);
   - or more (Artin, GL_2, automorphic), which neither gives.

   Flag any statement that claims more than its input gives.
5. **Integration.** Say where each checked finding goes in our work, as exact edits or entries:
   - the open rows of our earlier runs it settles or changes (run and statement id);
   - the reading of Grothendieck's texts it changes (cote and scan);
   - the study or companion notes that need an edit (file, place, the edit);
   - the successor prompts it feeds: our prompts 30-36 in `TO_SEND\PRO\1_Archive_research_by_topic\`, and the
     successors of the runs.

   Make no edit outside your intake folder; list the edits. Check that each finding is also stated in the language of
   algebraic geometry and of Grothendieck's frameworks, as the prompts asked. Where the run did not do that, say so,
   and give the translation where it is short.
6. **Prompt updates:** what a successor prompt of the run needs, from what you found.

## What to deliver
In `<local>/Documents\field_experts\intake_20261121\intakes\<TAG>\`, for each run:
- `INTAKE_<TAG>_20261121.md`, holding:
  - section 0: the return folder read and your scope (findings read in full, findings read at the level of the
    statement);
  - the verdicts, finding by finding;
  - what is new;
  - the scope of the two proofs;
  - the integration;
  - the prompt updates;
  - **Hexagon readiness** (added 21 Nov at the user's word, P8640). For each finding that could become a post of ours,
    judge it against the five tests of `field_experts/HEXAGON_CANDIDATES.md`: complete, self-contained (its inputs are
    published or formalized), stable (nothing of ours running or planned will supersede it soon), checked, and of
    interest now. Say which tests it passes and which gate is left.
- `INTAKE_<TAG>_20261121_CHECK_EVENTS.tsv`, one row per check event with these columns:
  - statement id;
  - date;
  - who (model, effort, agent id);
  - type: targeted proof check, independent re-proof, computation or formal certificate, used and rechecked, carried
    as background without fault found, or refuted (with the refined statement's id);
  - outcome.

Write the intake document early and keep it current.

## Rules
- No sub-agents.
- When you name a model that did work, name its effort with it.
- Never run Grep or Glob over the whole of `<local>/Documents`; name the folder. No git commands.
- Write only in your intake folder and your work file.

## Final reply
Under 250 words:
- per run: the findings read in full and at statement level;
- the verdict counts;
- the main findings;
- what is integrated where;
- the paths of your intake documents.
