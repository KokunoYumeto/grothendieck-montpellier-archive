# Reproducibility and execution record

Owner: `/root/cotes_156_8_9`, GPT-6 Astra Pro, inherited effort (no distinct effort value exposed to this child).

Authoritative task: `/workspace/scratch/4017236f14bf/upload/PROMPT(20261119-011407).md`.

The full reading sequence and actual UTC timestamps are in `operations.jsonl`. It begins 2026-11-19T01:15:40Z; every owned folder was read by 01:28:11Z. The first combined output was replaced by individual folder reads so that output truncation did not substitute for reading. Source hashes and exact line counts are in `source_manifest.json`; 24 full-read folders contain 190 scan markers. Source text files and notes themselves are user attachments and need not be copied into checkpoint ZIPs.

## Saved programs and their outputs

| Program | Purpose | Output |
|---|---|---|
|`read_corpus.py FOLDER`|Print the complete note and transcription with line numbers.|`read_outputs/FOLDER.txt`; call details in `operations.jsonl`.|
|`curate.py` plus every `curated_*.py`|Serialize manually authored claim, problem, reading, link and coverage decisions. No heading/keyword classifier is used.|`claims.json`, `problems.json`, `readings.tsv`, `links.tsv`, `coverage.tsv`, `claim_search_map.json`, `curate_output.txt`.|
|`computations.py`|Exact finite relation checks, graph counts, and explicit symbolic infinite examples.|`computations_output.txt`; interpretation and limits in `proof_audits.md`.|
|`locator_inventory.py`|Create scan-to-file map and list source-reference candidate lines for manual checking.|`scan_locator_map.json`, `crossref_inventory.txt`; console count24folders/190markers/77candidate lines.|
|`finalize_records.py`|Serialize manually recorded search/check events and validate only schemas, reference keys and locator bounds.|`search_log.tsv`, `check_events.tsv`, `source_manifest.json`, `audit_output.json`, `finalize_records_output.txt`.|

The mathematical computation command is `python computations.py > computations_output.txt` from this directory. The artifact build is `python locator_inventory.py`, then `python curate.py > curate_output.txt`, then `python finalize_records.py > finalize_records_output.txt`. Source and interpretation are both retained; an exhaustive finite model is not described as proof-assistant formalization, and sample enumeration is not described as a general theorem.

Web outputs are saved as `web_001.json` through `web_017.json`. Actual queries, exact opened URLs, unsuccessful fetches and their limits are recorded in `search_log.tsv`. The final supplementary file also stores its structured query input. Earlier query inputs are transcribed in the search log from the actual calls. Exact theorem locations and circulation/publication differences are in `references.bib` and the individual fate fields.

Shell `rg`, `sed`, `nl`, `cat` and directory listings were used for source navigation and repeated line checks. They did not generate mathematical verdicts. The cross-reference extraction is reproducible from its saved program. All mathematical code is saved; no unrecorded program supplies a claimed proof.

Milestones: full owned-corpus reading completed01:28:11UTC; claim assessments and references serialized by the01:41UTC progress report; schema/reference/locator validation passed before the01:47:17UTC clock read. Filesystem display times differ from the supplied clock tool; actual UTC timing comes from operations.jsonl and clock outputs rather than filesystem modification times. Root owns the45-minute checkpoint schedule and final archive.

## Explicit verification limits

- No scans were attached or consulted for the manuscript. Reading alarms are not ink verdicts.
- Direct zbMATH access failed; domain-restricted web searches are identified as such.
- A primary article mirrored as OCR was used for Björner after DOI/CORE access failed; its theorem text was opened, not inferred from a search snippet.
- SGA4 was initially checked in the modern transcription; the official editor PDF has now been opened and rendered, as recorded in supplemental_primary_checks.md. It is a2024 editorial reedition, not a facsimile of the1972 printing.
- All 87 claim records have a searched fate; class D denotes a documented search boundary, not demonstrated historical absence.
- Source definitions, counterexamples reconstructed in this run, authorial corrections and later published comparisons remain separately identified.

The final cross-cote supplement `curated_zzzz_support_check.py` links the IX14–18
reader's P4 certificate R-SA21-9E-005 to MP-SA21-8-12. The pointwise failure of
full faithfulness was independently checked against VIII86; the other reader's
finite computation was read, not rerun. `proof_audits.md` §N records the direct
argument and `finalize_records.py` records the targeted check event. The original
87claim total is unchanged; the problem now has an explicit finite answer.

## Final independent audit reconciliation

`correct_birkhoff_chapter.py` corrects the reference to Chapter IV in this part,
after direct comparison with the primary-book heading and polarity section.
`reconcile_late_ix.py` records the directly read IX95–97 corrected criterion and
updates MP-SA21-9-08 without changing its early source statement. Each program's
output is saved alongside it. `curate.py` and `finalize_records.py` were then run
sequentially, preserving all87 claims,23 problems,63 alarms,31 links and24
full-read folders. The two new, narrowly typed source/proof events are serialized
separately in `parts/final_audit/supplemental_check_events.tsv` for root to merge.
The complete final assembly inspection and its saved programs/outputs are in
`parts/final_audit`, not in the manuscript sources.
