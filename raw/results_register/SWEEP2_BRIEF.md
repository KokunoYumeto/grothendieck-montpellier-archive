# Sweep 2 over the whole register: how everything interlinks (brief, 18 Nov 2026)

Written by the main session (Claude Opus 5.5 Max) for one agent, Claude Opus 5.5 at effort max, with a large budget
and up to five sub-agents. Name every model with its effort in what you write.

## Why
The user, 18 Nov 2026 (USER_INPUTS.md P6848): "do a light sweep, see where everything goes, do another light sweep,
see how everything interlinks, see if there are obvious inconsistencies ... just Bayesian refinement." And (P6862-P6863):
launch one sweep agent with 900k of context and five sub-agents allowed, "and then compare the effectiveness. Just point
them apart a bit ... The logic being it's ... a lot to sweep, so it might be smart to give it some leeway." Four
sweep-1 agents (Opus 5.5 Max, 400k each, no sub-agents) are placing the rows of one line each in
`results_register/sweep1_*`. You take what no line agent sees: **the links between runs and lines, over the whole
register.**

## What you have
- `<local>/Documents\results_register\`: REGISTER.tsv (7,032 statements, 48 runs, draft tags RUN:ID),
  EDGES.tsv (13,793 edges), FLAGS.tsv, SUMMARY.md, build_register.py. Read `SWEEP1_BRIEF.md` there for the columns and
  the flags.
- The structure it feeds: `<local>/Documents\grothendieck_archive_montpellier\HANDBOOK_SKETCH_20261118.md`
  (sections 2-5).
- The programme map: `<local>/Documents\grothendieck_archive_transcription_20261110\notes_headlines\PROGRAMME_MAP.md`.
- The runs' returns, through each row's `ret` and `results` columns.

## What to do, across the whole register
1. **The dependency graph, closed.** Resolve every dependency the script could not:
   - the 225 that name no id of their own run, and every cross-run reference;
   - references to a paper's own labels, to the literature (by locator) and to his manuscripts (cote, scan).
   Write `GRAPH_EDGES.tsv` (from, to, kind: uses / restates / strengthens / refines / corrects / refutes / cites
   literature / cites his place, with a source) and `UNRESOLVED.tsv`.
2. **Clusters across runs and lines.** Find the same mathematics in several runs and lines, under one name or several:
   - a definition or an object with two names or two definitions;
   - a statement restated with changed hypotheses;
   - a result in one line that another line needs.
   Write `CLUSTERS.tsv` (cluster id, member tags, relation, the canonical statement as you would state it) and
   `CROSS_LINE.md` (the links between lines that matter, and what each makes possible).
3. **Global consistency.** Look for:
   - contradictions between runs or lines;
   - a proved row that rests, through the graph, on an open or refuted row used as if true;
   - cycles in the graph;
   - two statuses for one cluster.
   Read the proofs where it matters and work the mathematics through as mathematics. Write `CONSISTENCY.md`.
4. **His places.** Link every row that names a cote, scan or folio to that place. Write `HIS_PLACES.tsv` (tag, cote,
   scan, what he says there), so the companion can point from his page to our items.
5. **Corrections and refinements:** `CORRECTIONS.md`, each with the rows, the fix, how sure you are, what you read.
   Record your checks in `CHECK_EVENTS.tsv` (statement tag, date, who: Claude Opus 5.5 at effort max, sweep 2, type,
   outcome).
6. **`SUMMARY.md`.** It holds:
   - the counts;
   - the most important links and corrections;
   - a short account of how you used your sub-agents and your budget: tokens, what each sub-agent did, what it found,
     and what you would do differently. The user wants to compare this set-up with the 400k agents without sub-agents.

Write everything in `<local>/Documents\results_register\sweep2_global\`.

## Sub-agents
You may use up to five, if they help; you do not have to. Each is Claude Opus 5.5 at effort max, bounded to about 200k
of context, with a named part of the work (for example a set of runs whose references to resolve, or one cluster
family to check) and its own output file in your folder. Give each a full brief: they know only what you tell them.
None may launch further agents.

## Rules
- Read `<local>/Documents\AGENTS_MATHEMATICS.md` before you judge any proof.
- Work the mathematics through, critically, as mathematics, without presuming it false.
- Read-only outside your folder.
- Cite known results by locator; do not re-prove them.
- Credit Michel Hua's project wherever a finding is his.
- No recursive search over big trees; name the folders you open. Never run a broad git command.
- When the sweep-1 agents' `MERGES.tsv` and `PLACEMENT.tsv` appear in `results_register/sweep1_*`, use them; do not wait
  for them.
- Do not stop for context below your bound. If your context starts with a summary, you were compacted: reread this
  brief and your own files, then go on. Your final message to the main session: five lines at most, with your folder.
