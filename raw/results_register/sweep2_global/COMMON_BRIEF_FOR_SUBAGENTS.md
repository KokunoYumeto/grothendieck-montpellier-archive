# Sweep 2 sub-agents: what every one of you needs (18 Nov 2026)

Written by the sweep-2 agent (Claude Opus 5.5 at effort max) for its five sub-agents, each Claude Opus 5.5 at effort max.
Read this file whole, then your own `BRIEF.md`.

## What this is

The user develops Grothendieck's mathematics from the Montpellier archive with AI models. Research runs (GPT-6 Astra,
ChatGPT Pro mode; each run returns a paper, notes and a results table) took up the questions his pages raise. Their
results are being organized into one tag space, in the manner of the Stacks Project and Kerodon:
`<local>/Documents\grothendieck_archive_montpellier\HANDBOOK_SKETCH_20261118.md` (read sections 2-5). Every
statement of every run is one row of a register, with a draft tag `RUN:ID`.

- Sweep 0 (a script, no model) built the register: `<local>/Documents\results_register\REGISTER.tsv`
  (7,032 rows, 48 runs). Columns: tag, run, line, id, status (normalized: Proved, Refuted, Known, Open, Unresolved, ...),
  status_raw, statement (one line), where_proved, depends_on, uses, lineage, his_places, check_events, check_types,
  check_docs, check_doc_kinds, same_statement, notes, ret (the run's newest return folder, relative to
  `<local>/Documents`), ret_kind, ret_num, stamp, results (the results table). **Never read REGISTER.tsv
  whole into your context**: filter it with a short Python script (`python -I -B`, `csv.field_size_limit(10**9)`,
  delimiter tab, encoding utf-8) and print only the rows you need.
- Sweep 1 (four Claude Opus 5.5 agents at effort max, one per scope, no sub-agents) placed the rows of their scopes
  and wrote merges, flag verdicts and corrections. Their folders:
  `<local>/Documents\results_register\sweep1_tower`, `...\sweep1_sections`, `...\sweep1_derivateurs`,
  `...\sweep1_s6`, each with SUMMARY.md, CORRECTIONS.md, MERGES.tsv, FLAG_VERDICTS.tsv, PLACEMENT.tsv,
  CHECK_EVENTS.tsv (and sweep1_tower/CROSS_RUN_EDGES.tsv, sweep1_derivateurs/XREF_EDGES.tsv). Their scopes:
  - tower: LM4_SUCCESSOR, LM8_PUSH, EXIT_TOWER, LM4_FINITE_GROUP_ACTIONS, DELTA_ON_GT, GT_TOWER_CHECK,
    LM8_LIE_APPROXIMATIONS, LM5_MULTI_GALOIS_TOPOI, LM1_GROUP_SCHEMES_rerun_20261112, LM2_LOOP_EQUATIONS,
    EXIT_ONE_TYPE, CYCLOTOMIC_KERNEL;
  - sections: FLAGGED_149, ANABELIAN_149_PUSH, ANABELIAN_SUCCESSOR, ANABELIAN_A1, ANABELIAN_A1_SUCCESSOR,
    LM6_POINTS_AS_SECTIONS, LM7_FERMAT_TOWER, LM7_PUSH, FERMAT_SUCCESSOR, SECTIONS_OVER_Q, SECTION_GHOSTS;
  - derivateurs: the 15 Dérivateurs runs plus TOTEX and PRETOT;
  - s6: the S6 runs and Q03_DEPOSIT.
  **No sweep-1 agent saw the links between scopes, or FINMON** (a Dérivateurs run of 695 rows that the register
  misses: its checkpoint-20 folder holds encoded files; the decoded table is
  `derivateurs_companion_20261109\pro_prompts_max_20261112_work\FINMON\FINMON_checkpoint_20_decoded_20261117\FINMON_results.csv`
  with `FINMON_report.md` beside it). That is sweep 2's work, and yours. Read the sweep-1 SUMMARY.md and CORRECTIONS.md
  of the scopes you touch before you start, and do not redo what they settled; build on it, and say where you disagree.
- Sweep 2 (me) closed the dependency graph by script. In `<local>/Documents\results_register\sweep2_global\`:
  - `GRAPH_EDGES.tsv`: from, to, kind (uses / names / restates / checks / refutes / corrects / strengthens / refines /
    answers prompt item / cites literature / cites his place / uses computation), field (where the reference was read),
    how (the rule that resolved it), in_sweep0, evidence (the words around it). "uses" comes from depends_on and
    where_proved; "names" and the relation kinds come from the words around a reference in the statement or notes,
    read by a keyword rule: **treat every relation kind from the notes as a hint to check, not a fact**. References
    through a prompt's rows ("R13", "Lead 3") are resolved through the run's prompt (`tools/prompt_rows.json`: each
    prompt row with the tags its leading parenthesis names).
  - `tools/crossrun_edges.tsv` (every cross-run edge with the statuses at both ends), `tools/crossscope_edges.tsv`
    (the 712 edges that cross the sweep-1 scopes), `tools/status_conflicts.tsv`, `tools/analysis_proved_on_unproved.tsv`,
    `tools/analysis_cycles.tsv`, `tools/cycles_detail.tsv`, `tools/cluster_pairs.tsv` (statement-similarity pairs
    across runs), `tools/places_parsed.tsv`.
  - The register is a snapshot of 13:06 UTC today. Two returns have moved on since: SECTION_GHOSTS has a final
    (`longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\`), and
    S6_06_BLIND has checkpoint 35 (its checkpoint 33 is in
    `s6_pro_prompts_20261112_work\returns\S6_06_BLIND_checkpoint_35_20261118T1208Z_unzipped\_from_earlier_checkpoints\`).

## Where the mathematics is

Each row's `ret` folder holds the return: the paper (`*_paper.tex`, often with `sections/*.tex`), the report
(`*_report.md`), the results table, notes, code, and sometimes CHECK_EVENTS.tsv. Read the TeX where the proof is
(`where_proved` names the file and the statement). Open the files you need by their names; to find a statement inside
a return, Grep with `path` set to that return folder. Prompts: `tools/prompt_rows.json` names each run's prompt file.

## Rules (the user's, and they bind you)

1. Read `<local>/Documents\AGENTS_MATHEMATICS.md` before you judge any proof. State the actual claim with its
   data; type the maps; justify each reduction; "up to" is a proof obligation; do not upgrade a comparison.
2. Work the mathematics through, critically, as mathematics, **without presuming it false** (AI mathematics is not
   presumed bad; mathematicians check too). An invalid proof is a gap, not a refutation; one verified counterexample
   refutes.
3. Cite known results by exact locator (EGA/SGA by their numbers, Stacks by tag, papers by statement and page); do not
   re-prove them.
4. Credit Michel Hua's project (github.com/Commutator-IO/grothendieck-project) wherever a finding is his.
5. Read-only everywhere outside your own folder. Write only in your folder
   `<local>/Documents\results_register\sweep2_global\sub_<name>\`.
6. No recursive search over big trees: never Grep or Glob `<local>/Documents` or a whole project folder; name
   the return folder you search. Never run any git command.
7. Name every model with its effort setting in what you write: the runs are "GPT-6 Astra (ChatGPT Pro mode)"; the
   intakes and experts named in the files carry their own (for example "Claude Fable 5.2 at effort max"); you are
   "Claude Opus 5.5 at effort max, sweep 2, sub-agent <name>".
8. Do not launch any agent.
9. Budget: about 200k tokens of context. At about 180k, stop reading, write your files, and finish. Write your files
   as you go (a first version early, then update), so that nothing is lost if you are cut off.

## What you write (in your folder)

- `FINDINGS.tsv`: id (yours, e.g. D01), kind (contradiction / proved-on-unproved / status conflict / two definitions /
  two names / restatement / correction / refinement / cycle / sound), tags (space-separated), finding (what is the case,
  stated as mathematics), fix (what the register, the rows or the handbook should say), confidence (high / medium /
  low), read (the exact files and statements you read), note.
- `CLUSTERS.tsv`: cluster (yours, e.g. DC01), member tags (space-separated), relation of each member to the canonical
  statement (same / stronger / weaker / refines / corrects / refuted by / equivalent / special case), canonical
  statement (as you would state it in the handbook, with its hypotheses), status of the cluster (with the strongest
  proved reduction if open), source.
- `CHECK_EVENTS.tsv`: statement tag, date (2026-11-18), who ("Claude Opus 5.5 at effort max, sweep 2, sub-agent
  <name>"), type (one of: targeted proof check / independent re-proof / computation or formal certificate / used and
  rechecked in this run / carried as background without fault found / refuted, with the refined statement's id),
  outcome. One line per statement you actually checked; say exactly what you checked, neither more nor less.
- `REPORT.md`: at most two pages: the links that matter and what each makes possible; the corrections, most important
  first; what you read; and a short account of your budget (about how many tokens, how many files, what you would do
  differently).

Your final message to me: at most ten lines, with your folder and the counts of each file.
