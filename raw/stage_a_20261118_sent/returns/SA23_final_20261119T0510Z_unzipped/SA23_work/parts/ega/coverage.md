# Core coverage: cotes22,23 and26

Owner ega; run SA23-20261119; status checked19 November2026. The core assignment is complete through Stages1–6. Cotes1 and21 are a separate succeeding assignment in `parts/analysis_curves`; this file does not claim them.

## Source coverage

All82 indexed notes of `MPL_22+23_002-016` were manually read with their actual transcription passages. The complete Pro transcription has1,777 physical lines; the complete doubts table was read as well. The complete Codex sources were read: K22-01(426 lines), K22-02(259), K23-01(560), K23-02(301), K23-03(535), K23-04(388), K23-05(654), K23-06(471), H26-01(352). Source-read outputs and line ranges are retained in `read_logs/`; reading is not counted as proof verification.

K22-01/02 and K23-06 overlap the Pro pages. K23-01–05 supply additional material through scan99; scan99 is in the actual file despite a catalogue synopsis ending at98. Scan markers42,43,48,69,72,86,95 do not occur in these supplied Codex files. This does not assert that archival sheets with those numbers do not exist. Cote26 has markers2–11. No scans or second-pass corrections were supplied; no transcription was edited.

## Deliverable counts

- Stage1:82 entry verdicts;69 indexed items SA23-101–169;21 additional Codex subjects SA23-1301–1321 (90 total subject records);69 kept,11 merged,2 corrected.
- Stage2:98 claims C-SA23-ega-001–098, including a separate unidentified handwritten R1 sketch. Classes A13,B26,C28,D0,E25,F6. Every claim has an explicit actual-search or direct-original-publication record.
- Stage3:37 authorial mathematical problems after the complete origin audit and the separately recovered Deligne request;34 editorial tasks preserve23 whole redirects and11 partial context splits.
- Stage4:48 mathematical reading alarms, none decided on the ink.
- Stage5:37 links:8 across archive places,22 to published work,7 quarantined earlier-project leads. The unavailable targets of the latter are expressly not certified.
- Stage6:7 ranked directions, each with numeric manual interest/progress ratings and exact subject/claim/problem IDs in directions.json. Additional subjects supply actual Codex provenance where no indexed note exists.
- Computation:19 finite certificates in `computation_outputs.json`, with code and scope; independent unrestricted arguments are in `proof_notes.md`.
- Bibliography:87 records. Verified means the link or primary file was opened, not that the whole work was re-proved. Unavailable originals are explicitly marked unverified.

The individual page-status wording is intentionally descriptive and preserves cancelled/rewritten layers; `validation_output.json` contains complete machine counts by page status and class.

## Reproducibility and evidence

The entry/item decisions, claim formulations, problem formulations and reading/link judgments were composed manually and only serialized by the build programs. `check_events.tsv` labels what actually happened: source concordance, hypothesis comparison, targeted proof checks, independent reconstruction, finite computation and bounded refutation. `search_log.jsonl` records actual queries, exact URLs, locators, matches, negative results and per-claim fate concordances. The original-publication image checks include EGAIII1p133; EGAIV1p204 and the relevant earlier sections; EGAIV4’s later errata; SGA6VII; SGA4II/III; and SGA2XI3.13.

Complete external PDFs, full extracted external texts, rendered external page images and raw search responses are internal working caches under `sources/external/ega/` or shared `external/` directories. They are excluded from checkpoints/finalZIP. Only the condensed literature evidence, programs, certificates and original analysis belong to the deliverable. Root handles checkpoints and the final aggregate.

## Bounded unresolved matters

A classC orF result is a completed, searched assessment, not a promise to do the missing work later in this run. The exact Lang proof gap, broad nonlocal Cohen existence, ambiguous finite-epimorphism descent, natural-functor category, initial geometry of the non-Cohen–Macaulay construction, some numbered proof simplifications and unidentified reused/handwritten fragments retain precisely stated limits. The next directions identify how to narrow them. The completed publication comparisons must not be confused with scan decisions or novelty claims.

## Final integration audit

The original twenty additional Codex subjects supply direction provenance; SA23-1321 separately records the recovered Deligne proof request; all82 indexed-entry verdicts are unchanged. The15 formerly empty-reference claims were reviewed in empty_reference_audit.json, with9 precise/limited reference additions and6 explicitly documented nonmatches or independent checks. C015’s present-run surjectivity sentence was corrected against Stacks10.89.2–3. All183 core/analysis claims have manually reviewed record_origin and verification_origin labels. The separate cross-owner review proposes3 indexed subject mergers and a conditional cocharacter-subsubject consolidation; no other owner’s registers were mutated.

## Approved problem-origin audit

The audit covers every original problem record:59 core and22 analysis/curves records. The initial records and directions are preserved under provenance/pre_origin_audit; the approved audit has exact literal cues. Whole reclassifications use original_id; partial editorial contexts use source_problem_id. Why-open and worth fields have been manually reviewed, and no missing historical reason is inferred. This part has 37 retained authorial problems, 34 editorial tasks, 7 Stage6 directions and 5 editorial directions outside Stage6. Run apply_problem_origin_audit.py last after a full rebuild.
