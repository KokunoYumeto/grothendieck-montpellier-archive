# RESEARCH_SA20 final package — INCOMPLETE

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We claim no priority.

We return this package after scheduled reviews14 and15 both recorded no qualifying movement, triggering the requested stopping rule. The final review was recorded at 2026-11-20T04:04:05.434948+00:00. Of the70 original rows,67 have determinations and three remain open: A.1(b), A.5 proper-map maximal locus and recursion, and C.2(b) literature directions/hypotheses.

## Read first

`RESEARCH_SA20_report.md` begins with INCOMPLETE and the full70-row outcome table. `RESEARCH_SA20_outcomes.csv` contains the same original-row mapping. `RESEARCH_SA20_results.csv` records267 numbered statements; `CHECK_EVENTS.tsv` records712 check events, including audits and failed routes. These are not counts of independent proofs. The dated `PROGRESS_LEDGER.md` preserves earlier research states and the final stopping review.

The430-page `RESEARCH_SA20_paper.pdf` contains the numbered proofs and exact remaining gates. Its LuaLaTeX source and every included TeX dependency are present, with `RESEARCH_SA20_references.bib`. The PDF passed compilation and explicit visual inspection of every changed or overflow page and a spread. `logs/pdf_qa.json` gives the exact page list, warning counts and hashes.

## Reproduce

We provide the mathematical verification programs in `code/` and `agents/*/code/`, with actual outputs in `logs/` and `agents/*/logs/`. Finite certificates support their stated finite claims; they do not replace the all-arity or topological proofs. Run `python3 code/assemble_records.py` to assemble the current CSV, TSV and BibTeX records, then `python3 code/update_report.py` for the report and outcome CSV. The recorded build uses LuaLaTeX, BibTeX and two further LuaLaTeX passes. Any changed build requires its own warning and visual review.

Downloaded original sources, manuscript scans, the supplied source archive, and previous checkpoint ZIPs are omitted. Their bibliographic URLs and inspection locators are retained. All authored research notes, code, logs, checks and deliverables are preserved subject to the documented exclusion of reproducible compiler auxiliary files. Pending or unnumbered method notes remain outside the checked statement inventory; inclusion does not promote them to proved original-row conclusions.

`notes/final_status.json` records the final status, and `notes/final_file_manifest.json` lists the included files and SHA256 hashes. The archive integrity record and delivery receipt are created after the immutable archive, so they are provided separately.
