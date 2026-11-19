# INTAKE_C: three Longue Marche runs on group actions and group schemes, every register row read, sorted and checked

Intake prompt, 19 November 2026. For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for your deliverables:
`INTAKE_C`. Written by Claude Opus 5.5 (Anthropic) at effort max.

## Why this run

Three research runs of GPT-6 Astra (ChatGPT Pro mode) came back between 12 and 17 November 2026 with 757 register
rows. Their subject is finite group actions on surfaces and on groups with loops, the involutions of the profinite
three-cusp group, and the group schemes M_{ρ,σ} over Z. Our intakes have read them only thinly: for every one of these
runs, the intakes of its newest return name fewer than a quarter of its rows (our intake ledger's count). A row an
intake did not name is not proved unread, and a row it named is not proved checked. This run takes in every row of the
three registers, each to its verdict, with our earlier intakes as background, and marks the rows they did not treat.

## The runs

| Run | Newest return we hold | Register rows (the run's statuses) | Its prompt asked | Rows named by intakes of this return (ledger) | Rows any document of ours names |
|---|---|---|---|---:|---:|
| LM1_GROUP_SCHEMES_rerun_20261112 | its return of 12 Nov 18:36 UTC | 84 (Proved 54, Refuted 16, Open 9, Known 5) | the group schemes M_{ρ,σ} over Z and the schematic envelopes of discrete groups (§§48-50); the rerun of 12 November | 0 | 84 |
| LM4_FINITE_GROUP_ACTIONS | its return of 14 Nov 04:06 UTC | 272 (Proved 241, Refuted 25, Known 3, Open 3) | finite groups acting on surfaces and on groups with loops (§§12-18, 23-25 bis, 31) | 21 | 71 |
| LM4_SUCCESSOR | checkpoint 40, 17 Nov 18:14 UTC; the run stopped its mathematics at its hour-40 review and marked itself INCOMPLETE | 401 (Proved 357, Refuted 19, Open 19, Known 6) | the involutions of the profinite three-cusp group, the icosahedral centralizer, and the open rows D.12, F.7, C.12 of LM4 | 84 | 116 |

In all: 757 rows. The fifth column counts the rows of the newest return that our intakes of that return name (our
intake ledger). The last counts the rows whose id appears in a passage about the run in any document of ours, notes
and reviews of earlier returns included (zip 3, `coverage/`): a script's count, which you confirm against the
documents. A document that read an earlier return of a run names the ids of that return; where the newest return
changed a statement, compare the two statements before you carry a verdict over.

What our records say about the earlier checks:
- LM1_GROUP_SCHEMES rerun: reviewed line by line by Claude Opus 5.5 at effort max on 12 Nov 2026, with its 17 programs
  rerun and 13 checks of its own (`LM1_RERUN_REVIEW_OPUS/REVIEW.md`). Our intake ledger does not scan that folder and
  counts the run as unread; the coverage table of this prompt includes the review.
- LM4_FINITE_GROUP_ACTIONS: D.32 and D.34 were refereed by Claude Opus 5.5 at effort max on the run's snapshot of 14
  Nov 01:56 UTC (the return you have is of 04:06 UTC). D.32, proved as claimed: a nontrivial element of finite order
  of the pure three-cusp group P, of GT̂₀ and of GT̂ is an involution with λ₂ = −1 (`REFEREE_A_LM4_D32.md`); D.34: its
  multiplier is −1 at every prime (`REFEREE_B_LM4_D34.md`).
- LM4_SUCCESSOR: the intake of its final checkpoint (`LM4_SUCCESSOR_FINAL_INTAKE_20261117.md`, Claude Fable 5.2 at
  effort high) checked the register counts, the status history and two computations, and read no proof of the 762-page
  paper. The run's 19 open rows were the same at its checkpoint 3 as at the end.

The documents that name the most rows of each register (document, rows named):
- LM1_GROUP_SCHEMES_rerun_20261112: `REVIEW.md` (84).
- LM4_FINITE_GROUP_ACTIONS: `INTAKE_20261114.md` (25), `PUSH_ITEMS_20261114.md` (23), `LATE_ROWS_LM7_LM4_20261113.md`
  (22), `INTAKE_20261113_EVENING.md` (21), `REFEREE_A_LM4_D32.md` (8), `EXPERT_IMPLICATIONS_E65_LM.md` (5).
- LM4_SUCCESSOR: `LM4_SUCCESSOR_FINAL_INTAKE_20261117.md` (84), `NOTES_20261115.md` (31), `GT_LINE_INTAKE_20261117.md`
  (30).

## What every row gets

For every row of every register (757 rows), in `ROWS.tsv` and in the run's section of `INTAKE.md`:

1. **The claim**, in one or two precise sentences of your own, with its hypotheses and its scope.
2. **Its status as the run gives it** (Proved, Refuted or False, Known, Open), and where the run proves it (file and
   label).
3. **Its proof in the return**: there or not there; complete, or incomplete with the missing part stated exactly. For
   a refuted row: whether the counterexample and the corrected statement are given and hold. For a known row: whether
   the source is cited with a locator. For an open row: the strongest proved reduction (its gate) and the step that
   stays open.
4. **The check**, for every new result: every proved row that is not a known result, every refutation, and every
   proved reduction of an open row. Re-derive each step of its proof from the statement and the results it cites,
   writing your derivation before you compare it with the run's text; rerun each computational step with a program of
   your own that does not reuse the run's, by a different method or library wherever one exists, or verify the
   certificate attached in zip 2; check each result it cites against its source. Record each check in
   `CHECK_EVENTS.tsv` with the type of what you did (paragraph "Check events" below). The outcome is one of: holds;
   holds after a repair you state and check (a missing case, a wrong constant, a corrected citation); gap at an exact
   step (what the step needs, and why the results it cites do not give it); false, with a counterexample.
5. **New, known, or already ours.**
   - New: not in the literature; say what you searched for and where.
   - Known: author, work, statement number and page, from the source you opened; write "to verify" in place of the
     locator when you could not open the source, and say why.
   - Already ours: the same result in one of our earlier registers, with its run and id and the intake or note of ours
     that recorded it (zip 3: `programme/PLACEMENT_LM_STATEMENTS_20261117.tsv` and the earlier intakes).
6. **Earlier treatment**: every earlier intake, note, review or referee report of ours that treated the row (the
   coverage table gives the candidates: open the document and confirm), with its verdict, and whether yours agrees;
   where it differs, the step where the two part. A row no earlier document treated is marked "not treated before".

Then three sections across the runs, in `INTAKE.md`:

7. **Our open items.** For each open item of our programme that these runs touch, what in these registers closes it,
   moves it to a strictly smaller gate, or refutes it, with the rows and your check of the decisive step. The open
   items are those of section 3.1 of `programme/COMPANION_OUTLINE_LM_20261117.md`, the questions of the prompts as
   sent (zip 4), and every open row of these registers.
8. **Contradictions.** Every pair of rows that cannot both hold, within this cluster, against another of our Longue
   Marche registers (the placement table), or against an earlier verdict of ours: which one holds, and the step where
   the other fails.
9. **Hunches.** What the rows suggest beyond themselves, each written in `PROMPT_IDEAS.md` as the question of a Pro
   prompt: the question, the rows it rests on, why it matters for the programme, and the first step to take.

## How to work

- For each run, read its prompt as sent first (zip 4: what it was asked), then its report, then its register row by
  row with the proofs in its TeX. Where the newest return is a checkpoint, take in what it holds: a row its report
  marks as unfinished keeps that state, with what is proved.
- Every status in these registers is the run's own claim. A run's own check-event files and audits are its
  self-checks: report them as the run's, and they do not replace your check.
- Rows that recur across runs (a successor run continues or re-proves an earlier row) each get their own line, linked
  to each other in the notes column.
- Our newer runs saved lean checkpoints, which hold only what changed since the checkpoint before. Where the newest
  return lacks a file of the run that an earlier checkpoint holds, the earlier file is attached, and its
  `MANIFEST.tsv` row names that checkpoint.
- Where a proof cites one of our earlier statements (as "LM6 E.12" or "EXIT_TOWER E.49"), look it up in the placement
  table, which gives its status and check record. In that table, LM1 is the LM1 rerun, LM4 is
  LM4_FINITE_GROUP_ACTIONS, LM7 is LM7_FERMAT_TOWER and LM8 is LM8_LIE_APPROXIMATIONS.
- The attachments hold no literature. Find the sources on the web (arXiv sources first, then the journals' open pages
  and the authors' pages) and open them before you cite them.
- The return zip holds no programs. Zip 2 holds the programs and certificates that register rows name as their
  evidence. For every other computation, write your own code.
- In our notes, home-folder paths read `C:\Users\<user>\...`; each zip's `MANIFEST.tsv` records that change where it
  was made. Nothing else in the attachments is changed.

## The order of the work

1. **The skeleton first.** One line of `ROWS.tsv` per row of every register, with the claim, the run's status and the
   earlier treatment filled in. It gives the counts of section 0 and is the measure of completeness.
2. **Run by run**, in the order LM1_GROUP_SCHEMES_rerun_20261112, LM4_FINITE_GROUP_ACTIONS, LM4_SUCCESSOR: for every
   row, its proof read and checked, its novelty settled, its verdict written. Write the files from the start and
   extend them as you go, so that an interruption loses little.
3. **The three sections across the runs** (7, 8, 9).
4. **The gaps.** When every row has its verdict, go back to each gap your checks found and work on it: close it with a
   repair you state and check, or show the step false with a counterexample. A gap that remains goes into its row's
   verdict with the exact missing step and every approach you tried, and its question goes into `PROMPT_IDEAS.md`.

Review the work every hour against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): for each run, the rows
with their verdict and the rows still to do; in step 4, every open gap with its status. In steps 1 to 3, movement
means rows reaching their verdict. In step 4, movement means only a gap closed or a step shown false. After two
consecutive reviews in step 4 without movement, stop the gap work, write the final package with every gap's state, and
deliver it.

## What the outcome must be

1. **Done** means:
   - `ROWS.tsv` has one line for every row of every register (757 lines), with every column filled;
   - every new result has been checked, and its check events are in `CHECK_EVENTS.tsv`;
   - `INTAKE.md` has section 0 and the sections per run and across the runs (below);
   - every hunch is in `PROMPT_IDEAS.md` as the question of a prompt.
2. **Not acceptable:**
   - a row without its verdict, or a sample of the rows in place of all of them;
   - "see the run's report" in place of a verdict;
   - a check recorded as a type it was not;
   - a row called new without what was searched, or known without a locator or "to verify";
   - a model named without its effort.
3. **Finished** only when the work is done in the sense of point 1. Keep working until then: do not stop because the
   remaining rows are many, because a run looks well checked already, or because much has been written. If the session
   itself ends first (the environment stops you, not your choice), the first line of `INTAKE.md` reads INCOMPLETE, and
   section 0 gives the state reached for every run (the rows with their verdict and the rows not yet reached), every
   approach tried on each open gap with where it failed, and the next step. A continuation run will resume from your
   newest checkpoint and this prompt. Never present such a return as complete.

---

THE MATERIAL YOU ARE GIVEN

Four zips. Each has a `MANIFEST.tsv` with every member's origin in our files, its SHA-256 and the reason it is
attached.
- `INTAKE_C_1_returns.zip`: the newest return of each run, one folder per run (`<RUN>_<return>/`): its register
  (`*_results.csv`), its report, its paper's TeX and sections, its notes TeX and records, its check-event files and
  its bibliography. Code, data, builds, page renders and earlier versions are left out. Where a run ended without a
  final and we saved its chat, the chat is in `_session_transcript/`.
- `INTAKE_C_2_evidence_code.zip`: the programs, outputs and certificates that register rows name as their evidence, in
  the same folders.
- `INTAKE_C_3_earlier_intakes.zip`:
  - `earlier/`: every intake, expert note, review, referee report and note of ours on these runs, at the paths of our
    files;
  - `WHO_WROTE_WHAT.tsv`: each document's author with model and effort, its date, and what it covers;
  - `coverage/<RUN>_rows_named_by_earlier_documents.tsv`: for every row, the documents that name it;
  - `programme/`: the companion outline (section 3.1: our open items) with the user's layers that supersede its
    structure, the placement of the 3,929 statements of 22 Longue Marche registers with their check records, our check
    ledger and our mathematics to-do of 17 November.
- `INTAKE_C_4_prompts_as_sent.zip`: the prompt each run was sent, with `PROVENANCE.tsv` (where each copy comes from
  and how we know it is the one sent).

WHAT TO DELIVER

One ZIP containing:
- `INTAKE.md`. Section 0: the scope (the runs, the return of each, the files you read), the row counts per run and per
  verdict, the rows no earlier document treated, and what the earlier verdicts and yours disagree on. Then one section
  per run, in the order above, and sections 7, 8 and 9.
- `ROWS.tsv`, one line per register row, with the columns `run`, `id`, `claim`, `status_in_run`, `where_proved`,
  `proof_in_return`, `proof_complete`, `check_types`, `check_outcome`, `novelty`, `locator_or_earlier_id`, `searched`,
  `earlier_treatment`, `agrees_with_earlier`, `bears_on_open_items`, `notes`.
- `CHECK_EVENTS.tsv` (paragraph below).
- `PROMPT_IDEAS.md`.
- `PROGRESS_LEDGER.md`.
- `code/`: every program you wrote or ran for a check, with its output.

Name every model with its effort: the runs and you as GPT-6 Astra (ChatGPT Pro mode); our intakes and notes as
`WHO_WROTE_WHAT.tsv` names their authors (for example Claude Fable 5.2 at effort high, Claude Opus 5.5 at effort max).
Work through every register; do not ask whether to go on.

IF THE EXECUTION ENVIRONMENT FAILS

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id,
date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate
/ used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's
id), outcome, where (the file and label of what you checked, and of your program for a computation). This covers the
statements of these runs and every earlier statement you check, use or refute here. Give each event the type of what
actually happened, neither more nor less: reading a proof without re-deriving its steps is not a check of it, and a
step you re-derived is a targeted proof check, not a re-proof of the whole. The statement id is the run and its id, as
`EXIT_TOWER:E.49`. Name yourself as "GPT-6 Astra (OpenAI), ChatGPT Pro mode, INTAKE_C". `CHECK_EVENTS.tsv` goes into
every checkpoint and into the final ZIP.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `INTAKE_C_checkpoint_<NN>.zip` with `NN` counting
up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint.
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter
or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before
you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable
written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a
new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it,
the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export
of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints
are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is
lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB
(536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be
larger, save it as several ZIPs of under 500 MB each, `INTAKE_C_checkpoint_<NN>_part<k>.zip`.
