# Source-access coverage audit

This is a mechanical interval-union audit of **recorded source reads and source displays**. It is not a mathematical proof check, an independent certification of every historical statement, or a visual inspection of the manuscript scans. No source-access record is relabelled as a proof event.

## Scope and result

`work/page_map.json` has 398 blocks: **304 in-scope Pro blocks**, **42 in-scope Codex blocks**, and **52 cote100 blocks excluded from this task**. Every one of the 346 in-scope scan blocks is covered by the recorded evidence. The audit also checks complete in-scope file spans, including introductions, delimiters and shared apparatus, for eight transcriptions and twelve notes/doubts files.

The package8/9/4 transcription uses the explicitly documented initial read of lines1–335 in `work/cotes8_9_4/source_read_log.tsv:21`. This is distinguished from utility-generated later reads. The P56 transcription's first cote delimiter is covered by the explicit full-2033-line statement in `work/cotes5_6/research_log.md:7`; its scan blocks are already covered by the per-page ledger. Root's headerless `work/source_access_log.tsv` is parsed as a six-column access record, preserving its statement that a displayed extract is not a mathematical check.

## Honest prior gaps and current reads

Two apparatus spans lacked coverage in the earlier ledgers:

- P56 notes lines1–10: the introduction preceding the444 substantive notes.
- P894 doubts lines908–1047: the shared abbreviation and legibility appendix, which includes in-scope references and therefore cannot be dismissed as cote100-only material.

Both spans were actually opened and read during this audit. Their tool outputs are9928bd and3d00ec respectively. They are recorded in `source_coverage_current_reads.tsv` as **current scope-check reads**, never as invented earlier events. `prior_missing_spans` preserves both gaps in the TSV/JSON. There are no remaining in-scope coverage gaps after these current reads.

The shared appendix was also compared with the48 P894 reading alarms. It adds no independent high-impact mathematics-dependent alarm: the cited difficult passages are already registered; “plus gén.” at9/20, transcription613, is “plus généralement.” No reading row was appended from this apparatus check.

## Notes/doubts boundaries

The three wholly in-scope Pro notes files and their three doubts files are checked in full. The mixed P894 notes file is in scope through line598; every subsequent note is expressly cote100. Its doubts file is in scope at1–422 and again at908–1047 for shared apparatus; the cote100-only doubt rows423–907 are excluded. All four Codex notes files are checked in full. No Codex doubts files were supplied.

## Evidence and reproducibility

`source_coverage.tsv` has one row for each of346 scan blocks and20 file scopes. It records required spans, prior coverage, current coverage, any missing spans, documentary-only spans and evidence IDs. `source_coverage.json` resolves those IDs to exact ledger file/line references, preserves all52 excluded cote100 blocks and file exclusions, and records source/input hashes. `code/audit_source_coverage.py` reproduces the interval calculations without generating read events for missing historical coverage.
