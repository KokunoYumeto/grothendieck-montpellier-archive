# SA29 part 2 — reviewer protocol

Read the user's complete prompt in `upload/PROMPT(20261119-185308).md`. Sources are already extracted once under `sources/`; do not unpack again. Only the 380 entries in this part's index receive verdicts. TOPIC.md's other-part folders are scope boundaries, not missing deliverables to invent. Current check date: 2026-11-19. Model: GPT-6 Astra Pro; reasoning effort is runtime-provided, not independently observable; do not invent an effort setting.

Every assigned entry must be read and compared with its actual transcription passage, and every transcription page in assigned packages read for unnoted claims/problems. `audit/entries_navigation.json` and `audit/pages_navigation.json` are navigation aids, never verdict engines. Use `python SA29_work/code/read_sources.py <relative-source-path> <start> <end>` for numbered reading with preserved request/output. You may write other programs, but preserve every program and its output under your review directory. Save progress incrementally. Do not write root deliverables or another reviewer's files.

Write manually reasoned package results under your reviewer directory:

* `items.json` — objects with `id,sources,kind,cote,scans,lines,his_words,statement,reconstruction,check,check_reason`.
* `entries.tsv` — `entry_id,item_id,verdict,reason`, exactly one row per assigned entry. Verdicts: kept / merged / corrected / withdrawn / rests on a misreading. Give a source-grounded individual reason; no keyword-generated judgments.
* `claims.json` — `id,items,cote,scans,lines,his_statement,statement,status_on_pages,computation,class,fate,fate_date,present_status,refs,confidence`.
* `problems.json` — `id,title,occurrences,as_he_states,plausible_today,state_of_art,why_open,worth,refs`.
* `readings.tsv` — `cote,scan,line,reading,alternative,evidence,weight,confidence`.
* `links.tsv` — `kind,from,to,what,evidence,note_ids` (kinds folder / published work / our projects). Both endpoints must be checked or explicitly label unavailable endpoint and do not describe as established.
* `references.bib`, `reference_checks.json` (key, opened URL, exact theorem/section/pages and supported result, tool ref when present).
* `CHECK_EVENTS.tsv` — `statement_id,date,who,type,outcome`. Allowed types exactly as user's prompt; text comparison is “used and rechecked in this run” with outcome saying textual comparison only; don't call this a proof. Bibliography metadata-only verification is distinguished from theorem checking.
* `search_log.tsv` — `claim_ids,source,query,opened_url,result,exact_match` documenting actual literature searches, including negative results and hypothesis mismatches. Search zbMATH, arXiv, MathOverflow, Numdam, EGA/SGA, relevant authors' works/bibliographies using grouped searches where suitable; every claim needs a searched fate. Use primary sources for conclusions. Record what you actually searched, not a planned list.
* `summary.md`, `directions.md`, and `progress.log`. Directions cite item, claim and problem IDs. Keep earlier-run ideas distinct from manuscript claims and from this run's reconstructions.

Second-pass changed readings are authoritative current readings where supplied. Do not modify input transcriptions. Record newly suspected ink issues without resolving them (no scans supplied). Bibliography notes are `note={verified}` only for URLs actually opened; otherwise `unverified`. Read sources, do not infer a theorem from its title. Check all hypotheses before a false-as-stated verdict. Redo finite calculations in saved programs with saved output; universal proof obligations need mathematics, not finite testing. Do not claim all-dimensional GT=Galois, profinite congruence, or anabelian reconstruction is settled without exact theorems.

Assigned ID ranges are disjoint. Root will reconcile duplicate objects across packages and renumber only if needed; preserve source entry IDs exactly. If a cross-package endpoint needs another reviewer's reading, message root with specific cote/scan/source. Do not wait for root to do your local reading or literature work.
