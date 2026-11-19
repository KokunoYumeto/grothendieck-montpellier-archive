# Reproducible commands and output inventory

Working directory: `/workspace/scratch/4017236f14bf`.

The initial source reader was run for J156-9-09 through J156-9-13 and each complete output was read sequentially, with additional short range reads to check the corrected clauses and outgoing links. The code is `code/read_sources.py`; each file in `outputs/J156-9-*_read.txt` retains every line and scan marker, followed by its entire note. Reproduce with:

```sh
python SA21_work/parts/cotes_9_09_13/code/read_sources.py J156-9-09 J156-9-10 J156-9-11 J156-9-12 J156-9-13
python SA21_work/parts/cotes_9_09_13/code/finite_checks.py
python SA21_work/parts/cotes_9_09_13/code/fetch_primary.py
python SA21_work/parts/cotes_9_09_13/code/author_claims.py
python SA21_work/parts/cotes_9_09_13/code/author_problems.py
python SA21_work/parts/cotes_9_09_13/code/author_tables.py
python SA21_work/parts/cotes_9_09_13/code/author_logs.py
python SA21_work/parts/cotes_9_09_13/code/validate.py
```

The finite program writes its assertions, full finite models and output to `outputs/finite_checks.json`. The download helper writes the URL, HTTP result and file hash for each fetched primary source. Primary PDFs were converted with `pdftotext -layout` to the corresponding basename `.txt`; these full texts and PDFs are research inputs, not deliverables. The source summaries and checked locators are in `source_checks.md` and `references.bib`.

Web research used the available web-search tool. Eight search outputs and seven opened-page output groups are saved; exact final requests are `outputs/exact_search_requests_7_8.json`. Earlier query families, rather than falsely reconstructed verbatim request strings, are recorded in `search_log.tsv`. Each claim has an explicit search-ID mapping. Source-title/metadata follow-up and exact theorem reading preceded all literature-fate judgments.

Additional read-only endpoint checks used `rg -n 'scanpage|Ces questions|Faute'` and `sed -n '1,180p'` on `sources/texts/codex/J156-9-14_transcription.tex`, plus `sed -n '164,206p'` and `sed -n '240,350p'` on `J156-9-08_transcription.tex`. These checked the earlier formula(*) and the later setting-aside of the span problem, without claiming full ownership coverage of either adjacent folder. Birkhoff's chapter locator was checked by `rg -n 'Galois|CHAPTER'` and `sed -n '3850,3875p'`, `sed -n '4320,4535p'` on the already extracted primary text in `parts/cotes_3_5/outputs/birkhoff1948.txt`.

One initial author-claims run emitted a harmless Python invalid-escape warning in a textual label; the label was changed to “minus” before the final regeneration. No assertion or computation failed. No Lean compilation was performed for this block. Proof reading, independent proofs and executable finite checks are separately typed in `check_events.tsv`.

Final bounded bibliography audit: `python SA21_work/parts/cotes_9_09_13/code/normalize_bib_notes.py` moved the six detailed verification notes into `annote` and set each `note` exactly to `verified`. Its saved output is `outputs/normalize_bib_notes_output.json`. `code/validate.py` was then rerun with explicit assertions for those six flags and retained detail fields. No mathematical computation was rerun or changed.
