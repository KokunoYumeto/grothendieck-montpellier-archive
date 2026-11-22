# RESEARCH_SA22 — final incomplete research record

**Status: INCOMPLETE.** The research phase stopped at the actual review
05 on 2026-11-19T21:39:16.282669+00:00, after the two
consecutive scheduled reviews without qualifying movement required by the
user's stopping rule. The exact remaining obligations, qualifications, actual
review records and assessment hashes are in `logs/final_status.json` and
`PROGRESS_LEDGER.md`. The status does not certify completion of those obligations.

## Reading the package

- `RESEARCH_SA22_paper.pdf` is the single delivered, actually visually approved
  paper PDF. `RESEARCH_SA22_paper.tex`, `sections/` and
  `RESEARCH_SA22_references.bib` contain its reproducible source.
- `RESEARCH_SA22_report.md` gives the outcomes, limits, source access scope and
  computation provenance; `RESEARCH_SA22_results.csv` is the canonical statement
  register.
- `CHECK_EVENTS.tsv` records mathematical checks with their actual scope.
  `SOURCE_ACCESS_EVENTS.tsv` preserves four relocated retrieval-only records;
  the full source-route history remains in the notes and logs.
- `PROGRESS_LEDGER.md`, `notes/` and `logs/` preserve the research, source,
  review, build and actual visual-inspection evidence.
- `code/` contains the research certificates and administrative programs. Their
  saved outputs distinguish actual executions, partial failures and unexecuted
  preparation. No computation should be inferred solely from program presence.

## Reproduction and source exclusions

From the extracted `RESEARCH_SA22` directory, use Python 3 and a standard TeX Live
installation providing LuaLaTeX and BibTeX to compile the paper:

```sh
python3 code/build_paper.py
```

Compilation creates build logs; it does not certify visual quality. Rendering
with `code/render_paper_qa.py` and `code/render_supplementary_qa.py` is followed by
actual viewing of the relevant pages. `code/record_visual_approval.py` records
only that completed inspection. Rendering utilities have their own dependencies
declared in their source. Mathematical programs likewise retain their exact
dependencies and saved execution scope.

Supplied scans, downloaded source PDFs and literature bodies are excluded from
the archive. Source URLs, access and reading limits, and available source hashes
remain in the bibliography, notes and logs. Earlier checkpoint member paths are
retained; earlier checkpoint ZIPs and historical paper PDFs are not nested in
this archive. The single paper-PDF path contains the current approved version.

## Archive verification

The timestamped internal `logs/final_archive_validation_*.json` records the
actual validation completed before ZIP creation; the associated
`notes/final_archive_inventory_*.json` hashes its payload, excluding the
inventory's own recursive self-hash. The postcreation receipt
`logs/final_archive_creation.json` is retained outside the archive with the
completed ZIP's hash, size, elapsed time and all-member verification outcome.
That receipt cannot be inside the ZIP whose final hash it records; no self-hash
or circular inclusion is claimed.
