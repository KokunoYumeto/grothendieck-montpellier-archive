# Completed source coverage — cotes 1 and 21

All ten assigned transcriptions and all ten corresponding context-free Codex note files were read. No manuscript scans or second-pass corrections are available. Codex notes create no Stage1 verdict rows; `entries.tsv` is deliberately header-only. The twenty additional subjects SA23-401–420 have no indexed-note source IDs; their source files are recorded separately in `additional_sources`.

| Source | Complete physical line coverage |
|---|---:|
| HC1-01 | 1–261 |
| K1-01 | 1–758 |
| K1-02 | 1–545 |
| K1-03 | 1–494 |
| K1-04 | 1–541 |
| K1-05 | 1–643 |
| K1-06 | 1–662 |
| K1-07 | 1–437 |
| K21-01 | 1–505 |
| K21-02 | 1–301 |

Total: **5,147 transcription lines**. Logged excerpts are in `read_logs`; the first oversized K21-01 output was reread in smaller chunks. Reading records are not proof-check events.

The claim map contains **85 claims**, the problem index **14 authorial mathematical problems plus15 editorial tasks**, and the computational file **27 finite certificates or explicitly labelled illustrations**. All claims have an exact searched literature fate, dated status, confidence, and references. Every problem points to its claim occurrences and opened sources. No unknown manuscript dates, missing leaves106/123/141, or catalogue descriptions have been supplied from inference. A catalogue allusion to a1953 letter is not evidence that that letter is present in these transcriptions.

Final validation reports zero errors. The package has148 checked links,20 verified references,195 check events and112 condensed search records. The final search log contains both exact targeted query records and a separate hypothesis-match record for every claim. Earlier search caches and whole external works are retained only under `sources/external/analysis_curves` and are excluded from the final ZIP. Bibliography verification means the URL was opened and the stated locator was read; it does not certify an entire external work. Failed access to zbMATH and the distinction between search leads and primary proofs are recorded.

`proof_notes.md` preserves the mathematical checks and all substantive repairs. `readings.tsv` records mathematical alarms without deciding the ink. `links.tsv` verifies both supplied-source and published-source ends. There are no other-project leads in these context-free Codex notes; the empty quarantined table is deliberate. Nine ranked directions have exact item, claim and problem IDs and separate interest/one-run-feasibility ratings.

Class A means an exact own-publication counterpart, sometimes for the repaired theorem; it does not imply that the undated manuscript preceded publication or that every published SGA exposé was written by Grothendieck. In particular SGA2 XIV retains Mme M. Raynaud’s printed authorship and its footnote credit to Grothendieck’s unpublished notes. Class C includes literal failures whose valid restricted counterparts are established, and underspecified residual programmes. No D classification is inferred from absent search hits.

The earlier core package in `parts/ega` is independent and complete. Do not rerun `build_registers.py` or `functional_claims.py` alone: they restore the initial adjudications and erase finalized literature fields. See `REBUILD.md` for the complete rebuild order.

## Approved problem-origin audit

The audit covers every original problem record:59 core and22 analysis/curves records. The initial records and directions are preserved under provenance/pre_origin_audit; the approved audit has exact literal cues. Whole reclassifications use original_id; partial editorial contexts use source_problem_id. Why-open and worth fields have been manually reviewed, and no missing historical reason is inferred. This part has 14 retained authorial problems, 15 editorial tasks, 8 Stage6 directions and 1 editorial directions outside Stage6. Run apply_problem_origin_audit.py last after a full rebuild.
