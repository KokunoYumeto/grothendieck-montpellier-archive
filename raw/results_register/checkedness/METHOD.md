# The checkedness ledger: method

Built 18 Nov 2026 by Claude Opus 5.5 at effort max (brief: `results_register/CHECKEDNESS_BRIEF.md`), with the script
`build_checkedness.py` in this folder. The script uses no model, no git command and no network; it reads files and
writes only into this folder. Rerun it to refresh everything:
`python -I -B <local>/Documents/results_register/checkedness/build_checkedness.py`.

Models named here: every research run is GPT-6 Astra (ChatGPT Pro mode), effort Pro (short: Astra 6 Pro). Every prompt
header says so ("For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode"), and every Astra event in the runs' check
files names it. The Claude documents are by Claude Fable 5.2 and Claude Opus 5.5 at the efforts recorded for their
authors in `field_experts/INTAKE_LEDGER_NOTES.tsv` and `check_ledger.jsonl` (from the agents' own transcripts), or in
the document's header. Where the registry records "at the session's default effort (none set at launch)", the ledger
carries that wording. The four sweep 1 agents are Claude Opus 5.5 at effort max.

## Files

| File | What it holds |
|---|---|
| `CHECKEDNESS_LEDGER.tsv` | One row per claim lineage (7,677 rows): canonical tag, member tags, status now and its history, counts by check type, by whom, first and last dates, strongest check, dependents, flags (main row, printed in S6_10, credit pending, in the register). |
| `CHECKEDNESS_EVENTS.tsv` | Every iteration and check behind the counts (24,354 rows): lineage, member, kind, who, actor (run or document), date, source file, and the line or outcome the event rests on. |
| `LEAST_CHECKED.md` | Per line: the strongest check each proved lineage has had, then the proved claims that others depend on, with the fewest real checks first. |
| `S6_CASE.md` | The 246 printed S6_10 rows with no line in CHECK_EVENTS.tsv and the 286 rows awaiting the credit comparison, row by row. |
| `checkedness_stats.json` | The numbers below. |

## 1. Claims and their history within a run

- **Snapshots.** Every results table of every return we hold: 159 tables of 49 runs. Sources:
  - the working copies that `field_experts/build_check_ledger.find_returns()` lists;
  - the `pro_returns` folders of the repositories in `github_backup_20261113/` (grothendieck-longue-marche,
    grothendieck-derivateurs, s6-complex-structure-workbench), which hold most checkpoints filed since 15 Nov;
  - `_from_earlier_checkpoints/` folders, `retained/checkpoint_NN/` (S6_02_PUSH), and zips in `answers/` that hold
    a main results table.

  Identical tables filed twice count once. Runs with more than one table: LM4_SUCCESSOR 22, S6_06_BLIND 17, EXIT_TOWER 12,
  S6_02_PUSH 10, S6_04_MAPS_MANIFOLDS 10, SECTIONS_OVER_Q 10, LM8_PUSH 9, S6_03_CDP 9, FERMAT_SUCCESSOR 5, DELTA_ON_GT 4,
  and two or three for nine more.
- **Nodes.** One per (run, statement id) in any snapshot (draft tag RUN:ID, as in REGISTER.tsv), plus one per label
  of the S6_09 and S6_10 inventories (`S6_09_PAPERS:<label>`, `S6_10_PAPERS:<label>`): 10,263 nodes.
- **History.** Each node's status in every snapshot. The ledger gives the changes (date, run, checkpoint, status) and
  `statuses_seen`; 245 lineages changed status (Known to Proved 70, Refuted to Proved 35, Open to Proved 30, Proved to
  Refuted 30, ...). `within_run_revisions` counts checkpoints at which a row's statement changed by more than a tenth of
  its words. A row absent from its run's newest table is marked dropped; two lineages consist only of dropped rows.
- **Three-hour reviews.** Their movement shows as status changes between snapshots. The review files themselves
  (progress_review_*h.json, movement_review_*.json, PROGRESS_LEDGER.md, hourly assessments) are read only for the ids they
  name (kind PROGRESS, 747 events); they are history, not checks.
- **Not in the register.** FINMON's checkpoint 20 has its results table only in the decoded copies
  (`github_backup_20261113/grothendieck-derivateurs/raw/pro_returns/FINMON_checkpoint_20/decoded/` and
  `derivateurs_companion_20261109/pro_prompts_max_20261112_work/FINMON/FINMON_checkpoint_20_decoded_20261117/`), so
  REGISTER.tsv (sweep 0) lacks its 695 statements. The ledger has them (603 lineages, line Derivateurs). It also has
  the rows that SECTION_GHOSTS (final) and S6_06_BLIND (checkpoint 35) added after the register was built.

## 2. Lineage: when two rows are one claim

Rows are merged into one lineage by these edges, in this order:
1. the S6 inventories' source columns (S6_10 `source_run`/`source_id` and `s6_09_label`, S6_09 `source_run`/`source_id`)
   and ANABELIAN_A1_SUCCESSOR's `A1_id` column (121 carried rows);
2. identical statement text (at least 60 characters after normalization) in two runs;
3. sweep 1's MERGES.tsv rows with relation `same` or `corrects` (560; the four sweep agents, Claude Opus 5.5 at effort max).

A lineage holds at most one row of each run: the inventories may hold several labels of one row, but two rows of one run
are never merged. 182 edges broke this rule and were kept as links, not merges. Without it, sweep 1's `same` pairs
chained distinct theorems into lineages of up to 92 rows (for example S6_03_CDP C.2.NC.1-5 and C.2.G.1 through the blind
run's P4 rows). The canonical tag is the lineage's earliest row (first seen), so it does not change when successors
come. The status now is that of the newest member still in its run's newest table.

Not merged, but recorded as iterations of the earlier claim:
- sweep 1's other relations (refines, weaker, stronger, refuted by, settled by);
- a later run's check column ("SECTIONS_OVER_Q A.44: confirmed", "EXIT_TOWER E.44: repaired");
- S6_06_BLIND's `stated_value_compared (run and id)` with its `agrees_with_stated_value`;
- prompt items: the R-items, tasks and leads of 47 prompts, of which 245 name rows of earlier runs ("R1 (LM4 D.32,
  D.34; refereed ...)"), with the successor's rows that cite the item in their answers, item or R-item columns;
- rows that name another run's id: in depends_on (a use) or elsewhere (a mention);
- probable restatements: statements in two runs sharing at least 60 % of their words (104 pairs). All of them already
  fell inside one lineage, so they add nothing.

## 3. Iterations and checks, typed by the rubric

Every event has a kind. The rubric types (memory `check-rubric.md`) and what feeds each:

| Kind | Rubric | Sources |
|---|---|---|
| T1 targeted proof check | 1 | the runs' CHECK_EVENTS (types "targeted proof check", "complete second proof reading", S6_10's code D, ...); the S6_09 writing checks carried in the S6_10 inventory (1,153); lines of Claude referee reports and reviews that give a verdict on the id; sweep 1 and intake CHECK_EVENTS |
| INTAKE_CHECK, EXPERT_CHECK | 1 (claimed) | a line of a Claude intake or expert note that says, first-hand, that the id was re-derived, recomputed, followed or holds |
| T2 independent re-proof | 2 | CHECK_EVENTS re-proof types; a later run's check column saying "confirmed"; a blind re-derivation that agrees. One event per run and lineage: twenty rows of the night run agreeing with one claim are one iteration |
| T3 computation or certificate | 3 | CHECK_EVENTS computation types, S6_10's code C, program replays |
| T3P computation inside its own proof | (3) | the row's where_proved or notes name code, a certificate or a program. A marker only; not counted as a real check |
| T4 checked in use | 4 | CHECK_EVENTS "used and rechecked"; a later run's row that uses the claim, or answers an R-item that names it, where the later prompt says inputs are "checked where you use them" (24 of the 47 prompts). Without that clause the use is exposure |
| exposure (USE, NAMED, PROMPT, T5) | 5 | later runs that used, named, restated or were given the claim as a prompt item without a check of their own; "carried as background" events |
| T6 discussion | 6 | Claude expert notes, debates, conferences, main-session notes |
| T7, REPAIR | 7 | refutations with the refined id; "refuted by" in sweep 1; "repaired" in a check column |
| INTAKE | (none) | an intake that names the id: a register-level reading, not a proof check |
| INRUN | (none) | an in-run review, audit or referee file of the return that names the id (1,569 files read); its scope is not parsed |
| REWORK | iteration | a later run holds a row of the lineage, re-wrote it in a paper inventory, took it up as a task, or stated a stronger, weaker or refined form |
| SRC | (source) | primary-source, literature and credit checks |
| EDIT, OTHER | (none) | editorial reconciliations, alias records, scope records |

**Counting rules.**
- A document counts once per lineage, however many members it names. Its event takes the strongest of its lines.
- A check event repeated in later checkpoints, or in both CHECK_EVENTS.tsv and the inventory's records, counts once.
  The dedupe key is the event's statement, type, checker, date and outcome text.
- Several events of one run on one claim count separately when they are different readers or scopes (a root reader and
  a second reader). The `runs_*` columns count distinct runs.
- Real checks = targeted proof checks + independent re-proofs + computations + runs that checked it in use + intake and
  expert lines that record a check. Register intakes, exposure, discussion, in-run file mentions and computations named
  only in the proof are not real checks.
- Strongest check, in this order: targeted proof check (by Claude, by a later run, or in its own run); the same claimed in
  an intake or expert line; independent re-proof; computation or certificate; checked in use; computation inside its own
  proof; named in an in-run review file; named in a referee report or review; survived exposure; discussion; read in an
  intake; none recorded.

## 4. Our documents

Of 131 documents, 130 are read in full by script: 38 intakes, 33 reviews, 5 referee reports, 40 expert notes, 6
main-session notes, 5 prompt-item files and 3 literature comparisons. The script listing
`LATE_ROWS_LM7_LM4_20261113.md` is not a reading and is skipped. The list is the union of `field_experts/check_ledger.jsonl`, `INTAKE_LEDGER.tsv`,
`INTAKE_LEDGER_NOTES.tsv`, the S6 reviews and intakes (`s6_pro_prompts_20261112_work/reviews/`, `intake/`,
`checkpoint_intake_20261115/`), `pro_intake_20261116/`, `pro_intake_20261117/` and `claude_math_notes/`. Ledgers,
registries, briefs and prompts are left out.

How an id in a document is attributed to a run:
- The nearest run name before it on the line counts ("LM4 D.32, D.34": both LM4). The aliases used in the prompts and
  reviews are known: LM6-, AP-, CK, TOTASPH, SQ, INV, FAM, PUSH, CDP, MAPS, ARI and others.
- Without a run name on the line, the run of the current heading counts, else the run the document is about (from the
  intake ledger, or the first run its title names).
- S6 labels (`inv:A1.0`, `cdp:st:C.2.G.1`, `night:P3K.69`) go through the S6_10 and S6_09 inventories.
- Bare numbers (Lemma 4.3) count only for Q03_DEPOSIT, in its own documents.
- An id counts only if that run has it in some snapshot.

What a document did to an id is read from the words that belong to it: from the id to the next id (at most 80
characters); for an id in a list, the words before the list; and, in reviews and referee reports, a verdict in the
section heading for the first id of the section.
- In reviews and referee reports, verdict words count: correct, holds, confirmed, proved as claimed, **proved**,
  checked, re-derived, recomputed, and "refuted", "false" or "gap" for a fault found.
- In intakes and expert notes only first-hand words count: re-derived, recomputed, by hand, own code, "I checked",
  "I followed", Holds.
- Negations ("unverified", "not checked", "undetermined", "checked in the X review", "according to") and conditionals
  ("if E.65 holds") make the mention a mention only.

The S6_10 inventory's check_record also lists our S6 documents per row (`s6_09_recorded_checks`, `ledger`). These
entries are merged with the scan, one per document and lineage.

## 5. What is heuristic

- Document attribution and verdicts (section 4). Samples of 8-12 events per kind were read after each change. The
  remaining error modes seen:
  - a verdict credited to an id that a table row names only as an input ("| F.16 ... H of E.3 | correct |");
  - a review's whole-document verdict not spread to the ids it read. The Q03 peer review (Claude Fable 5.2 at effort
    max) read the post in full, but its lemmas show only as "named in a referee report";
  - a plan line with "line by line" counted as a check.

  Every event carries its line in CHECKEDNESS_EVENTS.tsv, so each one can be verified.
- In-run review files are counted by the ids they name, not by what they checked.
- T4 relies on the prompt's clause: a later run whose prompt says inputs are checked where used is counted as having
  checked the claim when one of its rows uses it. That is what the prompt asked; whether each run did it is not read
  from its proofs.
- Text overlap, sweep 1's relations and the one-row-per-run rule decide lineage at the margins.
- Computations named in proofs (T3P) are found by words such as code, program, certificate, computed.

## 6. What could not be traced

- Checkpoints filed before 15 Nov were superseded and deleted (memory `returns-unpack-then-delete-zip`). Runs of
  10-14 Nov therefore have one table each, and their within-run history is the run's own files.
- 788 check-event rows did not resolve to a row of their run on the first pass. A second pass through prompt items
  and other runs' ids attached 172 events. The rest name literature (SGA1 III 7.3, Bousfield 1996 Theorem 3.3),
  internal labels (FREX "A:poset-weights", DER_LOCALIZERS "C.general_M"), checkpoints or sources, not statements.
- S6_03_CDP's `history/snapshots.json` (file versions inside the run) was not read; its nine filed checkpoints were.
- Code in the returns was not run; a certificate counts only where an event or the proof names it.
- S6_07_PAPER has no inventory, so its rewriting of S6 rows is not traced row by row.
- The night's Work returns whose who column names the wrong model (task note) are transcription returns, outside
  this ledger. In the research runs every Astra event is GPT-6 Astra (ChatGPT Pro mode).
- The environment is live: returns filed during the build are included (S6_06_BLIND checkpoint 35, SECTION_GHOSTS
  final), and later ones need a rerun.

## 7. What the ledger shows (build of 18 Nov 2026, 14:00 UTC)

| Line | Proved lineages | With no real check | With nothing recorded at all | Targeted check by Claude | By a later run | In its own run | Read in an intake | Reworked by a later run | Named in an in-run review |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Derivateurs (incl. FINMON) | 1,603 | 1,112 | 703 | 281 | 1 | 112 | 331 | 37 | 184 |
| Longue Marche / archive | 3,516 | 2,814 | 906 | 106 | 140 | 195 | 1,105 | 312 | 1,539 |
| S6 | 1,173 | 71 | 34 | 85 | 952 | 167 | 568 | 1,080 | 487 |

- **S6.** It has been worked over most. S6_09 and S6_10 (GPT-6 Astra (ChatGPT Pro mode)) re-wrote 1,080 of the
  1,173 proved lineages, and 952 of them carry a targeted check by one of those runs. S6_06_BLIND re-derived many
  blind. Claude's own targeted checks reach 85 lineages. Before the S6_10 intake (Claude Opus 5.5 at effort max) no
  Claude check had touched Paper IV's K-series or Paper V's night rows; that intake tested them for consistency and
  checked the rung-1 arithmetic, nothing more.
- **The S6_10 gap.** Of the 246 printed rows with no line in CHECK_EVENTS.tsv, 244 have S6_10 check events of their
  own in the inventory and `records/*.tsv`. The gap is in the CHECK_EVENTS file, not in the checking. Of the 286
  credit-pending rows, 283 have them. S6_CASE.md has the counts row by row.
- **Longue Marche and the archive.** Iteration is high: 1,792 proved lineages stand in more than one checkpoint, 312
  were reworked by a later run and 305 checked in use. Real checks are thin: 2,814 of 3,516 proved lineages have none
  recorded. Many are named in in-run review files (1,539) whose scope the ledger cannot read.
- **Derivateurs.** The eight first returns had row-by-row reviews by Claude Fable 5.2 (pro_reviews_20261110,
  pro_reviews_max_20261112), some unfinished (GALOIS: 22 of 74 rows). 281 proved lineages carry a targeted check by
  Claude. The later runs (INDLOCAL, REVLOC, FINMON, S2COUNT, DER_FOLLOWUP, FREX, DER_LOCALIZERS) have mostly their own
  checks and intakes, and FINMON's 695 rows were outside the register.
