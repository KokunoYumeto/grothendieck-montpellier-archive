# Coverage and audit: cote 31

## Source reading

The reviewer manually read every one of the 118 index entries of MPL_31_002-051 against its actual passage. The full Pro transcription, the doubts file, and the complete K31-01, K31-02 and K31-03 transcriptions and short notes were read to find claims not flagged in the notes. Source reading preceded serialization of the judgments. The programs build structured files from manually authored records; they do not assign verdicts from headings, keywords or cues.

No second-pass folder exists for this topic. There were no scans in the supplied material. The transcription is therefore the textual source, and every proposed ink alternative remains undecided. Codex notes take no entries.tsv verdict rows. Their mathematical content is covered by claim, problem and reading records.

The full assigned source boundaries are: Pro raw lines1–1626 (scans2–51 with gaps present in the supplied file); K31-01 lines1–483 (scans52–69 as supplied); K31-02 lines1–616 (scans70–86 as supplied); K31-03 lines1–436 (scans87–102 as supplied). Gaps in scan numbering are not filled with invented text.

`read_log.tsv` records the numbered views used for most of the source reading. Its early writer had a variable-shadowing bug: the last field points to read_log.tsv rather than the excerpt. The correct excerpt is in outputs under the deterministic name `{mode}_{source}_{start:04}_{end:04}.txt`; the range and source fields are unaffected. This bug has been corrected in the program. The initial notes1–9, Pro lines1–239 and Codex short-note reading occurred before the helper was introduced; that reading is attested here, not assigned a fabricated timestamp. `primary_read_log.tsv` records later targeted primary-text reads. Other primary opens and searches are preserved in the raw web-response files.

## Completed stages

1. 118 entry verdicts: 95 kept,22 merged,1 corrected. They form96 items. Source comparison gives75 agrees,20 not-on-the-page (mostly identified earlier-run links or ideas),1 understates. A preserved note's contextual proposal is not promoted into Grothendieck's statement.
2. 126 claim records, with55 classA,10 classB,29 classC,28 classE and4 classF. No classD finding was made: an unidentified or partially matched exact assertion was not called undeveloped on the strength of a failed first search. All126 claims have exact query-id links and opened-reference comparisons, with limitations explicit.
3. 46 problems, MP-SA12-101–146. Every record separates the written question from a defensible modern formulation and gives exact referenced scope. No historical motive for abandoning a question is inferred without evidence.
4. 91 reading alarms. The supplied transcription is unchanged; mathematical necessity alone never decides the ink.
5. 76 link rows:42 published-work comparisons,12 internal folder/source links and22 earlier-context leads. The22 context leads are duplicated into their own `our_project_leads.tsv`. Only the supplied citation and named target description were inspected for unavailable earlier-run targets; those targets are explicitly not corroborated results or verified endpoints. The final merger should keep that distinction visible.
6. 12 ranked directions, each with origin ids, a stated outcome, known results and a first bounded step.

## Literature-search evidence

`search_manifest.json` records51 exact executed queries, their engines, claim mappings and comparison scope. `outputs/search_audit_01.json` through `_14.json` retain the request and response together. `claim_search_map.tsv` contains152 claim/query links. Search results returned jointly for a batch are recorded as batch results, not falsely attributed one-for-one to individual queries.

The searches used primary SGA/EGA texts, author-hosted books and papers, arXiv, Numdam and author bibliographies; zbMATH and MathOverflow discovery searches were also performed. Failed direct access is logged. Search-engine snippets are not substitutes for the opened exact theorem. The principal supplementary negative example is the MathOverflow question about module pullback: it was read and rejected as a match for inverse image of sheaves of abelian groups.

There are37 bibliography records.35 have an opened text or metadata page with the verification scope specified. BourbakiACVII and Giraud1971 remain `note={unverified}` because their original texts were not opened; indirect metadata and a backward citation are identified as such. Shatz1966 is a verified real reference with publisher metadata opened, but its theorem is used only through Milne's explicit discussion. No claim of full-text verification is made for it.

## Computations and check events

`programs/check_calculations.py` and `outputs/calculations.json` contain12 calculation/proof families. They distinguish exhaustive finite arithmetic, illustrative enumerations, symbolic all-n arguments and deductions using published existence theorems. A finite example does not certify a general theorem. `CHECK_EVENTS.tsv` marks actual textual/hypothesis comparisons, targeted checks, independent reconstructions, finite computations and refutations separately. In particular, automatically serializing those events does not convert the bibliography into proof certificates.

## File and preservation scope

The root reviewer is responsible for final schema normalization, global duplicate reconciliation, scheduled checkpoint ZIPs and the final ZIP. This child writes only reviews/31 and does not upload or checkpoint. Full third-party PDFs and extracted texts in external are local working copies and should be excluded from the final archive; exact primary excerpts, bibliography, search responses, code and outputs document what was read. The uploaded source files themselves need not be copied into a checkpoint.
