# The checkedness ledger: how often each claim has been worked over (brief, 18 Nov 2026)

Written by the main session (Claude Opus 5.5 Max) for one agent, Claude Opus 5.5 at effort max. Name every model with
its effort in what you write.

## Why, in the user's words (USER_INPUTS.md)
- P6820 (18 Nov 11:38 UTC): "when noting the degree to which a claim is checked, always check how often it's been
  reworked by different Astra instances and how many Fable intakes have taken place on that. Like a very targeted check
  isn't the same as continually working, but the Astra things, for example, do check the results. So that is a series
  of like multiple checks ... a degree to which the claims are checked ledger should probably be constructed ... there's
  probably a lot more checks than you think that have already happened. And actually constructing that will also show
  what hasn't been checked to any large degree as well."
- P6860 (18 Nov ~13:3x UTC), on an intake that found S6 rows with no line in CHECK_EVENTS.tsv: "That's valid, but also,
  are they not checked? How many times have they been iterated over? ... I do recommend putting an agent on ...
  probably max, to just like detective the fuck out of that for all of those claims".

The plan of 18 Nov is in `C:\Users\user\Documents\task_notes\checkedness_ledger.md`. The check rubric (seven types,
from the targeted proof check down to survived exposure, and refuted-refined) is in the memory file
`C:\Users\user\.claude\projects\C--Users-user-Documents\memory\check-rubric.md`. Read both first.

## The job
For every claim we hold (start from `C:\Users\user\Documents\results_register\REGISTER.tsv`: 7,032 statements of 48
runs, each from its run's newest results table), find every time it was worked over, by whom and how:
1. **Within its run, over time.** Every checkpoint of the run, not only the newest: its status at each checkpoint, and
   the reviews of the three-hour check that moved it. `field_experts/build_check_ledger.find_returns()` lists every
   return folder, earlier checkpoints included.
2. **Across runs.** Successor runs carry ids: LM4 to LM4_SUCCESSOR, ANABELIAN_A1 to ANABELIAN_A1_SUCCESSOR, S6_01 to
   S6_09 to S6_10, and the night run S6_06_BLIND. Later runs also restate claims, recheck them as inputs, or use them in
   proofs. Each is an iteration: say of which kind (reworked / used and rechecked / restated / carried unchanged).
3. **Recorded checks:**
   - every CHECK_EVENTS.tsv;
   - the check_record columns inside the inventories (S6_10's inventory holds 1,488 current events; its CHECK_EVENTS.tsv
     only 994);
   - `records/*.tsv` and `analysis/*/current_check_events.tsv` in the S6 returns;
   - the runs' own check ledgers (for example `checks/S6_CHECK_LEDGER.tsv`).
4. **Our reading of them:** intakes, expert notes, referee reports, conferences, my notes. Their files are listed in
   `field_experts/build_check_ledger.py` (CHECK_DIRS) and summarized per document and statement in
   `field_experts/check_ledger.jsonl`. Read the documents where the jsonl is too coarse to tell what was done to a
   claim.
5. **Computations and certificates,** where a return holds code that checks a claim.

Type each iteration by the rubric. Never count one document twice; and record what an event actually did, neither
overclaimed nor safety-coded (a register intake is not a check of the whole proof; a run that used a lemma in a later
proof and rechecked it there did check it in use).

## What to write, in `C:\Users\user\Documents\results_register\checkedness\`
- `build_checkedness.py`: your script, rerunnable, which produces the tables below from the files.
- `CHECKEDNESS_LEDGER.tsv`: one row per claim lineage. It holds:
  - the canonical tag and its member tags;
  - the status now and its history (date, run, status);
  - the counts by type: distinct runs that reworked it, runs that used and rechecked it, targeted checks,
    independent re-proofs, computations, intakes that read it, survived exposure;
  - by whom (model and effort);
  - the first and last dates;
  - the strongest check it has had.
- `LEAST_CHECKED.md`: the proved claims that matter most (main rows, rows others depend on) with the fewest real
  checks, by line, so that the next checks go where they are thin.
- `S6_CASE.md`: for the 246 printed S6_10 rows that have no line in CHECK_EVENTS.tsv, and for the 286 rows awaiting
  the credit comparison, how many times each has been iterated over, and by what.
- `METHOD.md`: how lineage and iterations were found, what is heuristic, and what could not be traced.

## Rules
- Read-only on everything outside your folder. Four sweep-1 agents are reading the same register now (folders
  `results_register/sweep1_*`); when their `MERGES.tsv` files exist, use them as one more source of lineage. Do not
  wait for them.
- No recursive search over big trees: walk the return folders the way find_returns does, to a bounded depth. Never run
  a broad git command.
- Do not stop for context below your bound. If your context starts with a summary, you were compacted: reread this
  brief and your own files, then go on. Your final message to the main session: five lines at most, with your folder.
