# The intake ledger: how to rebuild it, and the rule

Set up 17 Nov 2026 by Claude Opus 5.5 at effort high, at the user's word of 17 Nov 2026: [the user's words, omitted] That evening an intake had been launched for runs that earlier intakes had already partly taken in.

## The rule

**Before you launch any intake or expert read, rebuild the ledger and read the row of every run concerned.** That covers
a Fable or Opus intake agent, a field expert's weigh-in, a Pro intake prompt (GPT-6 Astra, ChatGPT Pro mode) and a Pro
check prompt. The brief then names:
- what earlier intakes read (the file and the checkpoint);
- the checkpoint the new reader starts from;
- the rows that are still unread.

After the intake is written, rebuild the ledger again: the new file shows up in the run's row.

## Rebuild

    python -I -B <local>/Documents/field_experts/build_intake_ledger.py

`update_registry.py` also runs it, after the registry and the reading audit. It runs in about 10 seconds; the rebuild
of the registry takes longer. It reads files only. It uses no model and no network. Its git commands are path-limited
`git log` and `rev-list` calls in `github_backup_20261113/<repo>`, with no status call and no scan of a working tree.
Each run gives the same ledger from the same files; only the build time changes.

It writes four files:
- `INTAKE_LEDGER.md`: the ledger itself;
- `INTAKE_LEDGER.tsv`: one row per run or transcription unit;
- `INTAKE_LEDGER_NOTES.tsv`: one row per note file of ours;
- `intake_ledger_cache.json`: a cache of the return folders each agent's transcript touched. You may delete it; the
  next run rebuilds it.

## What is in the ledger

1. **Research runs whose newest material no intake has read**, newest first. Each comes with its route:
   - **Pro intake prompt**: the unread part is large (40 or more register rows), so the job is mostly reading and
     sorting;
   - **Fable expert**: the unread part is small, or the return is a paper without a register, so the job is judgement on
     what matters for the programme.

   Section **1b** lists the runs that were read up to the newest return, but whose intakes name fewer than a quarter of
   its register rows. This is where a duplicate intake is most likely. Read the newest intake's own scope paragraph
   first (for example section 0 of `GT_LINE_INTAKE_20261117.md`), then brief the new reader for the rest only.
2. **Pro intake-prompt candidates, in order.** 2b is the list for the rest of the runs in 1b.
3. **All research runs**, by programme. Each row gives:
   - every return received;
   - where it is filed (commit; whether it has been pushed, as of the last fetch);
   - every intake and expert note (file, date, agent with model and effort, the checkpoint it read);
   - the agents whose transcripts opened the return folders;
   - how many rows of the newest register its readers name;
   - the status and NEXT.
4. **Transcription runs**:
   - Pro packages: what has been done to each, by whom:
     - the first pass;
     - the three passes over Pro's notes (follow-ups, claims, gap) by a9ebc3d6 (Claude Opus 5.5 at effort max), with
       counts of research items, edition matters and "nothing further";
     - the Claude second-pass blocks, with their authors;
     - the method audit and the control verdicts that name it.
   - Codex-web units, by cote: the Pro second pass (SP prompts) and the control verdicts.
5. **Reader editions**, which need no intake.
6. **Our own notes and whether another model family has checked them.** This covers every intake, expert, consult,
   referee, debate and findings note, and `claude_math_notes/`. They are grouped by field, with the Pro check-prompt
   candidates: one prompt per field, "check every mathematical claim in these notes".

## Statuses

- *taken in up to the latest*: an intake, expert, referee or debate note has read the newest return.
- *partial: read up to cpNN*: an intake read an older checkpoint; the newer checkpoints are unread.
- *not taken in*: no intake has read any return of the run.
- *not needed*: a transcription with its second pass done, a control run, or a reader edition.

## How "read" is decided (heuristics; check the files when it matters)

- **What counts as a read:**
  - a document cites a return folder by its path;
  - it names a checkpoint ("checkpoint 17", "cp17", "final") right after the run's name, and that checkpoint exists and
    is older than the document;
  - or the document's author agent opened the folder in its tool calls (from its transcript).
- **What does not count as an intake:**
  - main-session notes (`claude_math_notes/`);
  - prompt-item files.

  They are listed in the row, with their tag.
- **"(by date)":** the document names no checkpoint. It is shown with the newest return older than itself, and it does
  not count as a read.
- **"Rows named":** the register ids of the newest return that appear in the readers' text. An intake may have read a
  row without naming its id. Registers whose ids are not of the form A.12 (FINMON: A1, A3(ii)) are marked *not
  countable*.
- **"Checked by another family"** needs one of two things:
  - a check prompt (CHECK, REFEREE, AUDIT or VERIFY in its name) whose text names the note;
  - or an entry in `CROSS_MODEL_CATCHES.md`.

  A research prompt that sends the note as background reads it and does not check it, even with a "check what you use"
  paragraph. The user, 17 Nov: Pro runs [the user's words, omitted]. Notes with
  generic names (REVIEW.md, FINDINGS.md) are matched only with their folder name.
- **Who wrote a file:**
  - first, `reading_audit.json` (the files each agent wrote) with `registry.json` (model and effort);
  - then an agent id or a "Claude ... at effort ..." line in the document's first 40 lines;
  - for files an agent wrote by script, the registry entry that names the file.

  A run launched without an effort setting is written "at the session's default effort (none set at launch)"; its
  registry row says more.
- **Run states** ("running (account 1)", "ended at checkpoint 17") are the user's words, kept in
  `reports_20261117/runs_queue_data_20261117.py` (STATE). Update them there.

## Superseded by this ledger

`INTAKE_TODO.md` (15 Nov) was kept by hand. It is no longer current. The ledger replaces it for the question "what has
been taken in". `CHECK_LEDGER.md` (`build_check_ledger.py`) still answers which statements each document checked; the
intake ledger reuses that script's `find_returns`.
