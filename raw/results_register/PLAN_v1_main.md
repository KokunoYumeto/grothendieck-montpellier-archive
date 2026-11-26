# PLAN: the index of everything we ever did (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026 ~16:0x UTC)

Merged from PLAN_PROPOSAL_a65dbdc2_v2.md (Claude Opus 5.5 at effort max; the measured model of the material, the work
packages WP0-WP21) and PLAN_PROPOSAL_ae84c4aa.md (Claude Fable 5.2 at effort max; TOPIC nodes, APPEARANCES, the
secondary rule, waves, audits). The brief is PROJECT_BRIEF.md (the user's words P9839-P9874 verbatim); the task file is
task_notes/check_results_relations_register_20261125.md. Where the two proposals differ, the choice and its reason are
below. Nothing runs that is not in this plan.

## 1. The model of the material (measured: SURVEY_MATERIAL_20261125.tsv, SURVEY_SUMMARY_20261125.md)
410 places, at least 7.34M files and about 2,250 GB (13 places capped: lower bounds), classed A (our work: index),
B (copies), C (tools), D (to settle with the user). Structured records already exist: the old register (197,631 check
rows from 1,664 files), the 18 Nov ledger (7,677 joined claims), the sweeps' tables, the agent registry (925 agents), the
intake ledger (215 runs); 8,917 check-event files by name (most copies; four non-copies already found: H01, H09, H17,
ZH3). Agent transcripts (Claude 240 GB, Codex 160.6 GB) are NOT mined for checks: each agent submits its own (P9867); the
agents' final reports may be extracted by script as DRAFTS that the agent corrects (ae84c4aa).

## 2. The data model (append-only tables in results_register/; the last row for an id is current)
- OBJECTS: canonical id, kind (RESULT, RUN, INPUT, CONJ, ARCHIVE, WORK, FINDING, TOPIC), title, aliases, HEXAGON (id or
  not yet), NEW (new / known with citation / unsettled with what was searched), PUBLIC (where), NEEDS_PUBLIC, owner,
  privacy (ours / other people's / private), provenance of the row.
- CHECKS: object, date, who, model, effort, type (the seven, exactly as named), SCOPE beginning PROOF / USE / STATEMENT /
  COMPUTATION / FORMAL, VERDICT (holds / gap / refuted), FINDING, locator, provenance.
- READINGS (separate table, never counted as a check; decided: ae84c4aa's reason holds, a reading must not be countable
  as a check by any query): object, who, what was read, date, locator.
- RELATIONS: a, b, kind, mechanism (a statement), established_by, checks, locator, state; NON-LINK rows only with every
  route tried, open to attack.
- TOPIC nodes (decided: ae84c4aa): shared objects (j = 1728, Q(sqrt-3), PG(2,3), lambency, the Singer group, ...) each with
  one owner; statements are tied to the topics they are about; cross-area links come out of the topics, so no single agent
  has to read across areas.
- APPEARANCES (decided: ae84c4aa): every place an object occurs (locator, version), so one result found in five places is
  one object with five appearances.
- Rows taken from a summary (an index, map, intake or prompt) are SECONDARY until found at the source; a counter reports
  how many remain (ae84c4aa).

## 3. Work (a65dbdc2 v2's WP0-WP21, ordered by ae84c4aa's waves)
- WP0 survey completion: finish the capped folders that are ours; classify all 410 places; the check-event file
  comparison (8,917 against 1,664); the manifest giving every in-scope file exactly one owner. Drive, Zenodo, openmaths.org
  and ChatGPT-online only on the user's go (section 5).
- Layer 1, scripts (no model tokens): the tools (regkit, submit_check, submit_relation, submit_reading, who_checked,
  related, test_register) adapted to this model; the legacy tables converted with provenance; duplicate ids merged by
  script, confirmed by an agent.
- Layer 2, Claude Opus 5.5 at effort max agents, one per area, disjoint by the manifest, on this index only, no new
  mathematics and no rechecking during indexing; five waves ranked by use: (1) posted theorems, their inputs and the
  settled discussions (USER_INPUTS, RUNBOOK); (2) the candidates and the maps' links; (3) the runs' registers; (4) the
  notes, editions, courses and the Pro notes on the archive; (5) the rest.
- The registry agents: all 925, as the user said (P9867), in three tiers, each shown a script-made draft of what is
  already recorded under its id, ~15k tokens each, sequential and logged.
- The three Pro prompts (a512cf71) use the same schema and ids; their output imports mechanically and anything they
  find that we lack goes to a review queue.

## 4. Verification and done
The user's examples are completeness tests (RH and moonshine; lambency in a complex structure on S6; the fields where
j = 1728 appears; the Singer manuscript's full check record; Alpöge in the Hodge forcing criterion; Hu's unchecked core),
plus blind tests drawn by script, and a second agent re-tracing 2% of each area's rows to the source. Reports after each
phase in results_register/reports/, each with a "forgotten finds" section, published after a privacy filter (no local
paths, keys, e-mail addresses, other people's material or private rows).

## 5. For the user (decisions that are theirs)
1. The GitHub repository for the index and the reports: a new repository (private first, or public), or the workbenches
   hub.
2. The D-list folders and other projects (Junipero, PolyClank, D&D): outside this index?
3. The Papors/Chatnotes RH workbench and the ChatGPT research sessions: indexed now (both proposals say yes).
4. Go-aheads for the Drive and ChatGPT-online surveys.
5. Cost: about 15-27M Opus 5.5 max tokens in all, about half of it the 925 asks; six stretches of the main session.
