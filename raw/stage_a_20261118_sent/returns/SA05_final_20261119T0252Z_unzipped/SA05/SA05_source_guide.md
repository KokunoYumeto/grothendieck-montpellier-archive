# SA05 — source coordinates and reproducibility

This archive contains the completed dossier and its audit trail. The supplied attachments are deliberately not copied into it. Paths beginning `sources/` refer to the safely extracted originals beside the `SA05/` directory. All source bytes match the original data archives; hashes and the comparison result are in `SA05_source_manifest.json`.

## Reading the coordinates

A line number is a1-based physical file line. It is different from scan number, manuscript foliation and reused typescript pagination. A `\scanpage{N}` marker starts a physical scan section. A section ends just before the next marker, or at end of file. Repeated/reused material can have different scan labels in different witnesses.

| Short locator | Exact relative file |
|---|---|
| Pro early | `sources/texts/pro/MPL_12_002-050_transcription.tex` |
| Pro middle | `sources/texts/pro/MPL_12_051-098_transcription.tex` |
| Pro late | `sources/texts/pro/MPL_12_099-149_transcription.tex` |
| K11-01 through K11-04 | Same prefix plus `_transcription.tex` in `sources/texts/codex/` |
| K12-01 through K12-09 | Same prefix plus `_transcription.tex` in `sources/texts/codex/` |
| B12-01 and B12-02 | Same prefix plus `_transcription.tex` in `sources/texts/codex/` |

The final audit replaced inaccurate draft Codex offsets in the root records with explicit whole physical scan-section ranges, while retaining the more precise Pro spans. Claims and problems inherit these corrected item locators. `work/root/source_guide_aliases.json` contains the complete alias/section map; the before/after records are in `work/root/outputs/codex_locator_initial_*.json` and the latest audit TSVs. B12 sections never enter the K12 replacement lookup. For example, B12 scan066 and K12 scan072 remain two independently located witnesses of reused text, not one physical scan.

A missing K12 section is stated explicitly; it can still have a Pro or B12 witness. No source was altered to harmonize a sign, index, deleted word or page label. The earlier scope files and authoring programs remain audit provenance; the final canonical tables and the documented repair step control the delivered locators.

## Supplied transcription inventory

| Source file | Physical lines | Literal scan markers |
|---|---|---|
| codex/B12-01_transcription.tex | 180 | 22, 66, 68, 69, 70, 81, 83, 85, 97, 98, 100 |
| codex/B12-02_transcription.tex | 202 | 102, 117, 121, 123, 126, 128, 130, 132, 134, 136, 138 |
| codex/K11-01_transcription.tex | 550 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |
| codex/K11-02_transcription.tex | 340 | 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28 |
| codex/K11-03_transcription.tex | 513 | 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42 |
| codex/K11-04_transcription.tex | 644 | 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58 |
| codex/K12-01_transcription.tex | 384 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 |
| codex/K12-02_transcription.tex | 501 | 18, 19, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 |
| codex/K12-03_transcription.tex | 336 | 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 |
| codex/K12-04_transcription.tex | 296 | 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63 |
| codex/K12-05_transcription.tex | 431 | 64, 65, 67, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80 |
| codex/K12-06_transcription.tex | 253 | 82, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 |
| codex/K12-07_transcription.tex | 430 | 99, 101, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114 |
| codex/K12-08_transcription.tex | 412 | 115, 116, 118, 119, 120, 122, 125, 127, 129, 131, 133, 135 |
| codex/K12-09_transcription.tex | 269 | 137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149 |
| pro/MPL_11_002-042_transcription.tex | 1309 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42 |
| pro/MPL_11_043-058+56_transcription.tex | 1958 | 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39 |
| pro/MPL_12_002-050_transcription.tex | 1816 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 |
| pro/MPL_12_051-098_transcription.tex | 1071 | 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 |
| pro/MPL_12_099-149_transcription.tex | 1625 | 99, 101, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 118, 119, 120, 122, 125, 127, 129, 131, 133, 135, 137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149 |

## Which tables control interpretation

`SA05_entries.tsv` is the380-row entry ledger. `SA05_items.json`, `SA05_claims.json` and `SA05_problems.json` contain canonical IDs. `SA05_aliases.json` records redirects and partial source partitions. Merged records retain source-specific formulations and documentary changes. Historical reference aliases do not collapse different editions or different works.

`SA05_links.tsv` has the required three kinds. Only its folder/published-work rows are counted as checked two-ended links. Prior-project associations are also exported to `SA05_project_leads.tsv`. Absent archive targets and the unverified SGA4 backward reference are in separate lead files.

`SA05_reference_ledger.json` preserves all bibliography witnesses, edition/version limits and additional reopened passages. `SA05_searches.tsv` maps each claim to actual performed searches and their checked extent; inherited family URLs are provenance, not a claim that every result supports every assertion. `CHECK_EVENTS.tsv` distinguishes source comparison, proof checks, independent deductions, executed computations and refutations.

## Restore and reproduce

Place the five original attachments in `upload/` beside this unzipped `SA05/` directory. Run `python SA05/programs/bootstrap.py` if `sources/` needs reconstructing; it safely extracts the archives. The separate uploaded `PROMPT(4).md` supplies the later45-minute checkpoint rule. The older packaged prompt is retained only as supplied input.

The existing authoring files contain the manually made judgments. `python SA05/work/root/run_all.py` regenerates the root scope, repairs its Codex locators and executes its exact checks. Other scope run/build programs and their recorded outputs are retained. The refinement-supplement builder has a deliberate duplicate-ID guard and should not be blindly rerun after central incorporation.

For the final canonical build, run `programs/consolidate.py`, `programs/consolidate_references.py`, `programs/build_directions.py`, then `programs/build_documents.py` from the `SA05/` path as shown by the build report, followed by `programs/validate_final.py`. These programs use the existing approved joins and authored judgments; they do not search or reinterpret the manuscript automatically. The final archive includes all authored programs and their saved outputs.

Fetched full published texts are not redistributed. Raw web-result bodies under the search caches are replaced inside the ZIP by source-access audit records containing URLs, retrieval IDs and hashes. The authored query ledgers, checked theorem statements, own proofs, conclusions and limits are preserved. This replacement is a packaging operation only and does not change the completed literature judgments.
