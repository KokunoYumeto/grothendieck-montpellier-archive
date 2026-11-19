# Existing source-read coverage evidence

This audit identifies existing records only. It adds no source-read events and makes no retrospective claim that a truncated tool response was fully inspected.

## Pro package

| Source | Existing documented spans | Evidence |
|---|---|---|
| `sources/SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex` | 1–335; 336–564; 564–910; 910–1312 | `source_read_log.tsv` lines 21, 3–5. The first span is explicitly labelled an initial reading before the reader utility. Saved numbered outputs exist for the latter three spans. |
| `sources/SA15_notes/pro/MPL_8_079-081+9+4+100_notes.md` | 1–150; 150–542; 543–680 | `source_read_log.tsv` lines 2, 6–7; corresponding numbered output files. |
| `sources/SA15_notes/pro/MPL_8_079-081+9+4+100_doubts.md` | 1–105; 105–259; 260–399; 400–422 | `source_read_log.tsv` lines 8, 19, 22, 18. The 260–399 row explicitly records a manual reading and final-audit rereading; the other spans have numbered outputs. |
| `sources/SA15_texts/pro/MPL_7_061-072+8_001-078_transcription.tex` | 2755–2799 | `source_read_log.tsv` line 20 and its numbered output; this is the cote 8:78 continuation endpoint. |

`research_log.md` line 9 separately documents initial raw commands for Pro transcription 1–428 and notes 1–290. It also states that the combined output truncated and that affected spans were reread. **That command description is not additional complete-reading evidence beyond the explicit ledger and saved spans.** Lines 15–17 record completion of the 148 in-scope note entries, in-scope manuscript pages, doubts and Codex comparisons; the doubts-completeness claim needs the qualification below. Cote 100 is excluded; the two intentionally read out-of-scope manuscript endpoints, 1346–1392 and 2192–2216, are separately labelled in `source_read_log.tsv` lines 11–12.

### Shared doubts tail: prior-log gap

The tail of `sources/SA15_notes/pro/MPL_8_079-081+9+4+100_doubts.md` is **not all cote 100**. The global coverage auditor `/root/cotes6_7` identified lines **908–1047** as shared abbreviations and legibility/limits material that also references in-scope cote 8, 9 and 4 pages. My existing ledger contains no read span for that block. Therefore its recorded initial coverage cannot be inferred from the earlier general completion sentence. The auditor reports actually opening and reading 908–1047 in the current coverage audit (tool output `3d00ec`) and is documenting that current read separately, with the prior gap retained. This qualification records the other auditor's report; it is not a new or retrospective read event by `/root/cotes8_9_4`.

## Codex sources

| Source | Complete-file span(s) already recorded | `source_read_log.tsv` lines |
|---|---|---:|
| `sources/SA15_texts/codex/K8-01_transcription.tex` | 1–91 | 9 |
| `sources/SA15_texts/codex/K9-01_transcription.tex` | 1–135; 136–430 | 10, 13 |
| `sources/SA15_texts/codex/K9-02_transcription.tex` | 1–232; 232–455 | 14–15 |
| `sources/SA15_texts/codex/K4-01_transcription.tex` | 1–139; 140–272 | 16–17 |
| `sources/SA15_notes/codex/K4-01_notes.md` | 1–14 | 27 |
| `sources/SA15_notes/codex/K8-01_notes.md` | 1–9 | 28 |
| `sources/SA15_notes/codex/K9-01_notes.md` | 1–29 | 29 |
| `sources/SA15_notes/codex/K9-02_notes.md` | 1–26 | 30 |

The listed final endpoints equal the actual Codex file line counts. Each transcription span has its corresponding numbered `outputs/<stem>_<start>_<end>.txt`. The four short note reads were recorded without such output files; the ledger explicitly distinguishes their initial and final-audit readings. No additional omitted initial span was found in the package records.

The ledger's current line numbers above include its header. Its duplicate rows were removed by the already executed `code/final_polish_and_validate.py`, lines 279–284; `research_log.md` line 65 documents that cleanup. This audit has not rerun that serializer or edited the ledger.
