# Fujiwara: exact NDL/CiNii record cross-check

Completed 19 November 2026 at 17:52:39 UTC; GPT-6 Astra, OpenAI, agent `part_b_cycles`.

**Outcome: the candidate records are duplicates of earlier evidence, and their preserved public metadata supplies no distinct original copy. No network request was made.** The original Fujiwara1995 passage requirement remains unresolved; this check does not affect the mathematical theorem derived from other opened sources.

The parent supplied a new search occurrence of the NDL article record and the corresponding CiNii record. Before opening either, I searched the existing notes and cache inventory for their complete identifiers, then inspected the exact already preserved source blocks.

| Record | Prior exact evidence | Actual content inspected and conclusion |
|---|---|---|
| [NDL article record](https://ndlsearch.ndl.go.jp/books/R100000136-I1363107369908715904) | A567's earlier `turn961698034search5`; the exact record is also indexed in `checks/part_c_remaining_web_body_inventory.json:680–688`. | The preserved indexed record identifies Fujiwara, Duke University Press, 1995, volume80(1), and carries the digital-data label. Its DOI points to `10.1215/s0012-7094-95-08002-8`; its related-resource URI is exactly the already known Euclid Download URL. No separate NDL digitized-content link occurs in this inspected block. |
| [CiNii article record](https://cir.nii.ac.jp/crid/1363107369908715904) | Earlier indexed occurrence `turn961698034search8`; `notes/secondary_source_retrieval_20261119.md:58` records the actual opening as `turn274609710view1`. | The earlier direct opening produced a robot-verification page. It was not requested again. The preserved later search block contains only title/author metadata, not original mathematics. |

The NDL block's external related-resource link is `https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-95-08002-8`. The earlier failure of that route is already recorded in `notes/secondary_source_retrieval_20261119.md:55–58`. Neither it nor the DOI, challenged CiNii record, login page, or private viewer was followed during this check.

This is a bounded conclusion about the exact preserved record representation. It is **not** a claim that every NDL holding or every possible later interface has been searched. The digital-data label alone is not evidence of a freely accessible NDL-hosted copy. The present candidate offers no new advertised route in the evidence already available, so no repeated probe was necessary.

## Reproducible local inspection and timing

Executed once: `code/part_b_fujiwara_ndl_cached_links.py`. Compact output: `code/part_b_fujiwara_ndl_cached_links_output.json`.

- Start: `2026-11-19T17:52:39.944364+00:00`.
- Completion: `2026-11-19T17:52:39.945839+00:00`.
- Internal elapsed time: **0.001471550996939186 seconds**.
- Scope: one existing external-cache JSON read; two exact target records; two matched source blocks; zero new searches, network requests, downloads, or mathematical tests.
- Earlier source-retrieval timing is not recorded in this cache and has not been reconstructed or invented.

The raw source remains outside the deliverable project at `/workspace/scratch/9c53b536a97f/source_reading/recorded_web_prose_second_pass/part_a567_fujiwara_distinct_search_1633.json`, SHA256 `31f0ff5aa682f84287906d2c4601d192b5fa982eb4b7f3bdec882f990318165d`. The compact output preserves exact record URLs, prior reference IDs and individual source-block hashes without embedding the outside source bodies. Only this note, one event, and the local inspection script/output were added; no TeX, bibliography or aggregate file was changed.
