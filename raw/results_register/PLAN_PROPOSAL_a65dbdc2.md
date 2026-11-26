# Plan proposal for the combined results index (agent a65dbdc241d1a129a, Claude Opus 5.5 at effort max)

Written 25 Nov 2026, before 15:45 UTC (date -u; an earlier label of ~16:4x was wrong), for the planning team: main 329fb1e6 (Claude Opus 5.5 at effort max), a0c4bb37f14505b26
(Claude Opus 5.5 at effort max; sweep 2, global interlinks) and me. It answers the main session's request of ~16:3x UTC
(the user, P9868: [the user's words, omitted]). I read the task file `task_notes/check_results_relations_register_20261125.md`
whole (P9839-P9868).

## 0. What I have built, and whether it fits

Built in `results_register/` (code only; no table has rows yet; nothing posted or pushed):

| File | What it does | Fits the plan? |
|---|---|---|
| `regkit.py` | Shared code: file names, column lists, the seven types with accepted spellings, verdicts, states, relation words, a lock file for concurrent writers, append-only writing, alias resolution | Yes. Needs the new columns (§1) and last-wins folding (§2). |
| `submit_check.py` | The one way to record a check. It validates object (by id or alias), scope, verdict (holds/gap/refuted), finding, who (model and effort required), type (one of seven), date and locator, then appends to CHECKS.tsv and prints CHK-nnnnnn. It can create a new object when given a canonical id and a title. | Yes. Add the fields `depth` and `agent_or_run` (§1). |
| `submit_relation.py` | The one way to record a link. It validates both ends, the relation word, the mechanism, who, the state and the locator, and checks that the cited CHECKS ids exist. A NON-LINK needs `--routes` and is always "open route". It appends to RELATIONS.tsv. | Yes. Add PUBLIC and NEEDS_PUBLIC. |
| `who_checked.py` (rewritten; the old one kept as `who_checked_legacy_before_register_20261125.py`) | Resolves any alias and lists, per object: the submitted checks with SCOPE and FINDING; the legacy events filed under any alias or under its run statements; the legacy events that only name it. It says "NOTHING IS RECORDED" when that is so. `--source` keeps the old search by file. | Yes. Add `--agent <id>` (§4). |
| `build_known_results.py` (first version) | KNOWN_RESULTS.md from the board and the legacy register: posted papers by statement, candidates, outside inputs (curated), with counts by type. Written but not run. | Partly. It becomes a generator from OBJECTS + CHECKS + RELATIONS (§6). |

Not yet written: `related.py`, `HOW_TO_SUBMIT.md`, the seed, the tests. Everything above is small and can change
before any row is written. That is why this is the time to fix the schema.

## 0b. Scope: everything the project ever did (the user, P9872)

"There is probably an enormous amount of mathematics that exists in our stuff that would be obvious if you organized it
well. Everything that has been done needs to be indexed ... literally everything we ever did."

So the index is not only the recent research runs and their checks. It holds every piece of mathematics we produced,
read, corrected or relied on, from the first course lessons of late September to today, together with the works that
carry it. Two additions to the object kinds of §1 make room for this:
- **WORK:** a deliverable. Examples:
  - an edition or transcription (EGA, SGA, FGA, the Montpellier archive cote by cote, Deligne, Noether, Weber,
    al-Khwārizmī, the Gelfand binders);
  - a translation, a reader, a course, a lesson, a paper or note, a GitHub repository, a workbench page, a deposit;
  - a prompt and its run.

  Its id is `WORK:<kind>:<name>`, for example `WORK:edition:SGA4-en` or `WORK:run:RESEARCH_SA12`.
  - Each statement object links to the works that contain it (`appears_in`).
  - Each work carries its own HEXAGON, NEW, PUBLIC and NEEDS_PUBLIC.
- **FINDING:** a correction or observation that is not a theorem of ours. Examples:
  - an erratum in an outside paper;
  - a misreading fixed in a transcription that changes the mathematics;
  - a course's finding (FINDINGS_LEDGER F-0091 and the like).

  Its id is `FINDING:<ledger>:<id>`. It is linked to the object it corrects (`refines`, `refuted and refined`).

**The existing inventories come first, so nothing is read from scratch:**
- `PROJECT_RECORD.md`;
- `knowledge/INDEX.md` and `knowledge/WORKSPACE_MAP.md`;
- the user's works inventory;
- `field_experts/INTAKE_LEDGER.md`: 215 research runs and 252 transcription units;
- the 18 Nov checkedness ledger: 7,677 claim lineages;
- the horizontal sweeps' OBJECTS, FLAGS and PLACEMENT tables: every archive topic SA01-SA32, item by item;
- the course hub and its findings ledgers, and the problem index of 5 Oct;
- the tag system and the implications logbook;
- the training-data graph scripts (prompts, returns, notes, checks, plans);
- the errata file `reports_20261120/errata/OUTSIDE_PAPERS_ERRATA.md`, the outreach register and the e-mail logs;
- the Hexagon board and the workbench pages;
- the October Pro batches and their API referee reports (`F:/user/Documents/claude_open_courses_20260926/plan/pro_checks_*`, `checks_*`);
- the RUNBOOK and USER_INPUTS, for links the user raised and we settled.

Layer 1 (§3) converts each of these inventories by script into WORK, RUN, ARCHIVE and FINDING objects with their
aliases. That is where the "obvious once organized" mathematics shows up:
- the same object under different names in a course, an archive sheet and a run becomes one object with many aliases;
- every such merge is a link nobody had written down.

The layer-2 areas of §3 gain three partitions for the older work:
- **11.** The Open Mathematics Courses: lessons, findings ledgers, the problem index and the October Pro batch answers with their API checks.
- **12.** Editions, transcriptions, translations and readers: EGA/SGA/FGA, the archive's cotes, Deligne, Noether, Weber and the others. Their mathematical corrections become FINDING objects, and their statements are linked to the research that uses them.
- **13.** GitHub, Hexagon, workbenches and deposits: the PUBLIC column, and what needs to be public.

## 1. The schema

All three tables are **append-only** TSV files, written only by the tools, under a lock. The current state of an object
or a relation is the fold over its rows (the last row of an id wins). Corrections are new rows that name what they
supersede. Nothing is ever edited in place, so concurrent agents cannot overwrite each other, and the history of every
judgement stays.

### OBJECTS.tsv: one id per thing we can check or link
| column | content |
|---|---|
| object_id | canonical id (§2) |
| kind | RESULT (ours, posted: by paper and number) / RUN (a run's statement) / INPUT (outside work) / CONJ (a named conjecture or theorem: CONJ:RH, CONJ:GRH_Dirichlet, CONJ:Hodge, CONJ:BSD, CONJ:VP_VNP, CONJ:Weil_RH ...) / ARCHIVE (Grothendieck's question at cote and scan) / TOPIC (a meeting point that is not a statement: j = 1728, the Bolza curve, umbral lambency 6, the Hecke characters of Q(√−3)) |
| title | short name |
| statement | the statement in one line, as printed (empty for TOPIC) |
| status | proved / refuted / open / conditional (on what: `conditional_on`) / known |
| conditional_on | object ids it rests on as hypotheses (Alpöge's theorem, Masullo's M, CT, ...) |
| aliases | every other name, " ; "-separated: run ids of every run that carried it, paper labels in every version, Hexagon ids, file names, board ids, the 18 Nov ledger's lineage tags |
| patterns | an optional regular expression for finding the object by name in free text (used by the lookups, never for counting) |
| HEXAGON | its Hexagon id (with version), or `not yet` |
| NEW | `new: <basis>` (the search that found nothing, with its locator) / `known: <citation>` / `unsettled: <what was searched>` or `unsettled: not yet searched` (the default: "new result?") |
| PUBLIC | where it is public, ";"-separated: `hexagon:2611.01043v1`, `github:<repo>/<path or WB id>`, `openmaths:<url>`, `arxiv:<id>` (outside work); or `nowhere` |
| NEEDS_PUBLIC | `yes: <why>` / `no: <why>` / `hold: <who decided, when>` (e.g. the user's hold on the conference, P9855) |
| locator | where the object is defined (file and line) |
| merged_into | set on a merge row: this id is an alias of that one (§2) |
| added_utc, added_by, origin | who added the row (model, effort, agent), when, and how (`submit`, `seed`, `legacy:<file>`, `pro:<run>`) |

### CHECKS.tsv: one row per check
| column | content |
|---|---|
| check_id | CHK-nnnnnn |
| object_id, alias_used | the object, and the name the submitter used |
| SCOPE | exactly what was checked. It opens with one word: PROOF (of the object itself), USE (our use of it in another object, which is not a check of its proof), STATEMENT (read at the statement), COMPUTATION, FORMAL, READING (a transcription reading). Then the sections, lines and steps. This removes the Hu ambiguity of 25 Nov. |
| depth | statement / proof-part / proof-full / formal-by-others / formal-rebuilt / computation |
| VERDICT | holds / gap / refuted (legacy rows whose source states none: `not stated`) |
| FINDING | what was found ("no fault" is a finding), with the gap or the counterexample |
| who | model and effort and agent or run, in one phrase (validated) |
| model_effort, agent_or_run | the same, split, for counting |
| type | one of the seven, exactly as named: targeted proof check / independent re-proof / computational or formal certificate / checked in use / survived exposure / discussed in an expert conference / refuted and refined |
| date, locator | when, and the record of the check (file and section) |
| supersedes | a CHK id this row corrects, if any |
| submitted_utc, submitted_by, origin | as above |

**A proposal for main to decide.** A statement read is not a check, but the user wants to know [the user's words, omitted] each outside
input was checked, and re-reading a statement is wasted work too. I propose that such readings go into CHECKS with type
`reading only (not a check)`, an eighth value that the counts never include. The alternative is a separate READINGS.tsv.

### RELATIONS.tsv: one row per settled link
| column | content |
|---|---|
| relation_id | REL-nnnnnn |
| subject, relation, object | object ids, with a relation word (implies, equivalent, enters, rests_on, reduces_to, refines, generalizes, specializes, same_object, instance_of, gates, uses, settles, computes, links, NON-LINK) |
| mechanism | the link as a statement, mathematical enough to check |
| established_by | model, effort, agent or run |
| checks | CHK ids that verify the link itself |
| locator | where it was established |
| state | established / checked / open route. A NON-LINK is always "open route" and carries `routes_tried`: every route, and why each fails. It is never a default. |
| HEXAGON, NEW, PUBLIC, NEEDS_PUBLIC | as for objects. A link can be new and unposted: fork 2's C4 is one. |
| supersedes, submitted_utc, submitted_by, origin | as above |

## 2. Canonical ids, and nothing entered twice

**Id forms.**
- **RESULT.** `RESULT:<hexagon id>` is the paper. `RESULT:<hexagon id>:<label>` is a numbered statement. Labels are normalized: Thm1.2, ThmA, Lem2.3, Prop4.17, CorC, Ex4.60, Rem7.2, Sec3, as numbered in the newest posted version. Earlier version labels go in as aliases (`v1:Thm 3`).
- **RUN.** `RUN:<run>:<id>`, with `<run>` as the legacy register spells it, without checkpoint suffixes (RUN:RESEARCH_SA12:D:wild-genus2-single-curve). One object per claim lineage, not per run. A statement that a successor run carried under the same or another id is one object, with every run's id as an alias.
- **INPUT.** `INPUT:<author>_<id or short title>`, for example INPUT:hu_2610.00216. Parts get sub-ids, such as INPUT:hu_2610.00216:Thm1.2-core and INPUT:hu_2610.00216:Cor9.6, so that "the core is unchecked" can be stated.
- **The rest.** CONJ:<name>, ARCHIVE:<cote>:<scan>, TOPIC:<slug>.

**Resolution.**
- A query resolves in this order:
  1. the exact id;
  2. an exact alias, after normalization (Unicode NFKC, case, whitespace, the dashes – and — to -, "Theorem"/"Thm." and the like in labels);
  3. a substring or pattern match, shown as candidates and never taken silently.
- The submit tools accept only an id, or an alias that resolves to exactly one object.

**Look up before creating.**
- To create an object, give its canonical id and a title. The tool first searches titles and aliases for near matches, and refuses while any exist; `--new-despite <id1,id2> --why ...` overrides that, recorded.
- `merge_objects.py OLD NEW --why` appends a merge row (`merged_into`). Resolution follows merge chains, so a duplicate found later costs one row and loses nothing.

**Seed from what is already merged.**
- The 18 Nov checkedness ledger (`results_register/checkedness/CHECKEDNESS_LEDGER.tsv`) already joins run statements into 7,677 claim lineages, with their member tags and dependencies. A script turns each lineage into one RUN object, with all its member tags as aliases.
- The board (HEXAGON_BOARD.tsv) gives the RESULT papers and the CAND rows. Its ids (H01, S12d, ...) become aliases.
- So the agents start from merged ids, not from 197,631 raw rows.

## 3. Sources, and a disjoint partition

The legacy register reads 241 source groups (1,664 files). The largest are:
- stage A returns, 36,667 rows;
- the 18 Nov ledger, 24,349;
- EGA_ES_FINISH, 15,830;
- the horizontal sweeps, 9,776;
- ALP_CONNES, 7,791;
- HODGE_DIVISION, 10,727;
- the S6 returns, 7,197;
- POLISH_CRISTAUX, 5,537;
- NEG_NIGHT, 4,900;
- ALP_MACHINE, 4,833;
- RESEARCH_SA15, 4,382;
- the French-school checks, 3,572;
- the intakes, 2,849.

**Split the work in two layers, so that no source is read twice and model tokens go only where judgement is needed.**

**Layer 1: scripts, no model (me, after main approves the schema).**
- **L1a.** Lineages to RUN objects (§2); the board to RESULT and CAND objects; the curated outside inputs to INPUT objects. Posted papers get their statements from their own CHECK_EVENTS ids and their TeX labels.
- **L1b.** Every legacy event whose type is one of the seven becomes a CHECKS row, about 140,000 rows:
  - the object comes from alias resolution; an unresolved id becomes a new RUN object;
  - SCOPE gets the event's statement id and its `where`;
  - FINDING gets its `result`;
  - VERDICT comes from the result's words, or `not stated`;
  - the origin is `legacy:<file>:<line>`.
  In-run reviews, intakes that only named a statement, and prompts stay legacy-only, but the lookups still show them.
- **L1c.** A manifest `PARTITION.tsv`: every source file or folder, the layer-1 rows it produced, the rows it could not map, and the one agent that owns it in layer 2. It is the record that nothing is skipped and nothing is done twice.

**Layer 2: Claude Opus 5.5 at effort max agents, one partition each (the task file's ten areas), each owning its rows of PARTITION.tsv.**
1. Archive research, sweep 3 (RESEARCH_SA05-SA23 and successors) and their intakes.
2. Longue Marche / anabelian / GT / sections / towers / Fermat.
3. Dérivateurs and homotopy (CATHOT, TOTAL_*, TOTEX2, FREX, FINMON, ...).
4. RH/GRH and Hodge, and the ALPOGE cluster.
5. Crystals, polish and AG runs, including EGA_ES_FINISH and the French-school checks.
6. Complexity / GCT / P vs NP. Fork 2 submits its own (REGISTER_SUBMISSIONS_PENDING.md); our GCT runs go here.
7. S6 (fork 1's records).
8. Posted papers, notes, workbenches, the conference papers and the board.
9. Maps, knowledge and discussions: MAP_*.md, INDEX.md, CONFERENCE files, knowledge/, claude_math_notes/, the RUNBOOK and USER_INPUTS.
10. The archive's Pro notes and the sweeps' readings (sweep1-3).

Each layer-2 agent does what scripts cannot:
- maps the unresolved ids of its partition to objects, merging duplicates;
- turns its md-only records into submitted checks with scope and finding: API referee reports, Pro in-run audits, intake prose without a TSV, conference reports;
- submits every link its sources state (RELATIONS);
- fills HEXAGON, NEW, PUBLIC and NEEDS_PUBLIC on its objects, NEW with the search it can cite;
- lists its "forgotten finds" (§7).

**Relations are the overlap risk.** The same link appears in a run, its intake and a map. The rule: the agent whose partition holds the earliest record of a link submits it, and the others add their CHK ids or a `same_object` row. a0c4bb37 (sweep 2, global interlinks) owns the cross-area links: areas 1-10 submit links inside their area, and links whose two ends lie in different areas go to a0c4bb37's queue (`RELATIONS_QUEUE_CROSS.tsv`). That is its expertise and keeps the global graph in one hand.

**Budget.**
- Layer 1 costs no model tokens.
- Layer 2 is ten agents at about 300-500k tokens each, so about 3-5M tokens. The largest partitions (5 and 4) may each need a second agent on a disjoint half of their files.

## 4. Asking every agent of the registry (P9867)

REGISTRY.md has 925 agent rows. The user: [the user's words, omitted]

**The protocol.** Sequential, logged, 10-20k tokens each.
1. **Order.** Field experts first, then intake agents, readers and referees, writers, then the rest. Within each group, the agents with the most files read go first (the registry's column).
2. **Before asking.** Run `who_checked.py --agent <id>`. It is a new option that lists every CHECKS and legacy row whose who names the agent. That list goes into the request, so the agent submits only what is missing and never resubmits.
3. **The request, one page, the same for all.**
   - Who asks, and why: the user's words P9867.
   - The list from step 2.
   - The commands: `who_checked.py` before each submission, `submit_check.py` per check, `submit_relation.py` per link it established.
   - The ceiling: stop at 15k tokens and report the counts.
   - The rule: nothing but this; no new checks, only records of past ones.
4. **The log.** `ASK_LOG.tsv` gets agent id, model and effort, date, tokens, checks submitted, links submitted, and "not reachable" for agents that cannot be resumed.
5. **Near-full agents** are asked too: they compact and go on (the standing rule), and the request tells them to reread their notes first.
6. **Cost.** 925 agents at 15k tokens is about 14M tokens. Asking only agents whose who appears in no source file, or whose files layer 1 could not map, cuts this to an estimated 300-400 agents, about 5-6M tokens. **Main and the user decide between [the user's words, omitted] and "filtered".** P9867 says all; the filter is my suggestion for cost.

## 5. The three Pro prompts (a512cf71)

The three ChatGPT Pro runs (GPT-6 Astra, ChatGPT Pro mode) get "the entire result bowl" and build the same index independently. To make their output usable:
- **Same schema.** Their deliverables are OBJECTS/CHECKS/RELATIONS TSVs in exactly the columns of §1. I will give a512cf71 the column file and the id rules, so their rows import mechanically, with origin `pro:<run>`.
- **Same ids.** Each prompt carries the seeded OBJECTS.tsv (ids and aliases) and must reuse ids before creating new ones, so their objects merge with ours.
- **Their role: a completeness check, not a second truth.** An object or link they find that we lack goes to a review queue, and an agent submits it after checking the source. A check they claim is recorded as their check, with their run as who. Where they disagree with a submitted verdict, a refuted-and-refined row is required before anything changes.
- **Timing.** They can run in parallel with layer 2. Their import comes after layer 2's first pass, so that the review queue shows only what our agents missed.

## 6. Acceptance tests

`results_register/test_register.py` runs these after every phase. It fails loudly and prints what is missing.

The task file's tests, as queries:
- **(a)** `related.py "RH" "moonshine"` returns every link, with locators:
  - MOONSHINE_AFTER_ALPOGE and its intake (the prime-ideal window criterion, Thm 1.2);
  - MAP_NUMBER_THEORY L10;
  - ALPOGE.md l.641-645 (which moonshine L-functions A covers: zeros on Re s = 3/4);
  - CHECKIN_20261125 l.24 and l.49-58 (the Hecke characters of Q(√−3) at the gate of four lines);
  - the moonshine maps of ad21742d;
  - aec1e030's PRETOT A.5 map;
  - the knowledge files.
- **(b)** `who_checked.py "Singer manuscript"` shows every check with its locator:
  - the Pro run Q02 (22-23 Oct, `pro_batch_20261022_open_questions/answers/Q02-solution.tex`);
  - the API referee report (Claude Opus 5.5 at effort max, 23 Oct, `F:/user/Documents/claude_open_courses_20260926/plan/pro_checks_20261023/Q02-check.md`: fixable gaps);
  - the two referee stages (Fable aee0b161, 36 + 23 events);
  - the independent check (a24b3bc6, 23);
  - the second reader (S89, 19);
  - the writer (16);
  - main's reads (6 events and RUNBOOK l.6995);
  - the finder (5).
  Its total must reach the 107 events the main session counted on T1, plus the Pro and API checks. The user counts four Pro and two or three API checks. Those not yet found are listed as missing, not hidden.
- **(c)** `related.py "Alpöge" "HODGE_EFFECTIVE"` finds the Heilbronn-Stark route (ALPOGE_ROUTES_20261125.md §0, a25c2acb).
- **(d)** `who_checked.py INPUT:hu_2610.00216:Thm1.2-core` prints NOTHING IS RECORDED. INPUT:hu_2610.00216:Cor9.6 shows afa2696b's chain check (`notes/INPUTS/CHECK_HU_20261125.md`).
- **(e)** `related.py "lambency" "S6"` returns fork 2's chain:
  - P205's ramification points are the Bolza curve's Weierstrass points (C4);
  - the binary octahedral group is the umbral group of lambency 6;
  - 2 × 3 = 6 with det = χ₋₃;
  - PG(2,3) is the plane of sl₂(F₃);
  - (2,3,6) maps onto the Singer group;
  - GL₂ × GL₃ → GL₆;
  - and the NON-LINK "Sp₄(F₂) = S₆ explains P205's level-2 match", with its failed route.
- **More, as the user said ([the user's words, omitted]).**
  - "where does j = 1728 show up" lists the areas that touch TOPIC:j1728.
  - Every posted paper resolves by its Hexagon id, board id and short name.
  - The tests do not drive the work. They check that the index is complete enough to answer such questions.

Integrity tests:
- every CHECKS and RELATIONS end exists;
- no alias belongs to two live objects (it is merged or flagged);
- every object has HEXAGON, NEW, PUBLIC and NEEDS_PUBLIC;
- every NON-LINK has routes;
- every check names model and effort;
- the counts in KNOWN_RESULTS.md equal a recount from CHECKS.

**KNOWN_RESULTS.md** is generated from the three tables:
- the posted results by paper and statement, with checks by type, verdicts, distinct checkers, depth, and what they rest on;
- the candidates;
- the outside inputs, with how far each is checked;
- the relation graph by area;
- the forgotten finds.

## 7. Reports and GitHub (P9864-P9866: they follow the work, never delay it)

- **Reports.** `results_register/reports/REPORT_<n>_<date>.md` after each phase, mostly generated:
  - the counts per table and per area;
  - the test results;
  - what is public where;
  - what needs to be public;
  - "forgotten finds".
  A forgotten find is an object with NEW = new or unsettled, PUBLIC = nowhere, and no row on the board or in any PROVENANCE: results in our notes that nothing tracked.
- **GitHub.** Main or the user chooses between a new KokunoYumeto repository for the index and the mathematics-workbenches hub. I suggest a new public repository, `results-index`. It holds:
  - the three TSVs after a privacy filter (local paths become repository-relative or descriptive locators; no keys, e-mail addresses, agent transcripts or personal text);
  - KNOWN_RESULTS.md and the reports.
- **Pushes.** One push per report, "do, then report". The filter script refuses to write while any `C:/Users`, `F:/` or `@` remains.
- **The PUBLIC column comes from a script.** It reads the board (Hexagon ids, WB pages) and the GitHub API listing of the KokunoYumeto repositories and the workbenches.

## 8. Order of work, and what I would do next

1. Main merges the proposals into PLAN.md. **The decisions main needs to take:**
   - the eighth CHECKS type for readings;
   - the cross-area owner (a0c4bb37);
   - "all" against "filtered" registry asks;
   - the GitHub repository.
2. I adapt the tools to the merged schema:
   - add the columns, last-wins folding, merges, `--agent`;
   - write `related.py`, `HOW_TO_SUBMIT.md` with the exact row formats, and `test_register.py`.
   About 1-2 hours of work, no new reading.
3. I write the layer-1 scripts (L1a-L1c) and run them. Then I report the counts and PARTITION.tsv to main **before** any agent backfill, as asked.
4. Main launches the layer-2 agents, one partition each, and a0c4bb37 for the cross-area links. The registry asks run sequentially beside them.
5. Then the Pro import, the generated KNOWN_RESULTS.md, the reports and the pushes.

**Seed material I have already gathered for the tests** (locators in my notes file, `agent_notes/a65dbdc241d1a129a_NOTES.md`):
- **The Singer record:** files and authors.
- **The Hu split:** the chain is checked; the core is not.
- **The Alpöge-Hodge route.**
- **Connes's Lemma 3:** CONNES_AFTER_RH intake l.5 and l.131-145.
- **The Ihara/Vandiver/K-theory links:** IHARA intake l.24-37.
- **GRH for Dirichlet L-functions and the twisted Tate motives:** ALPOGE.md l.345, BR-AT-01, confirmed by af2a18f6.
- **The moonshine sources.**
- **The lambency chain:** fork 2's pending file.
- **The HNAM chain:** zero-free half-plane (CT or Hu), then Koiran's Thm 9 replaced, then HN in AM.
