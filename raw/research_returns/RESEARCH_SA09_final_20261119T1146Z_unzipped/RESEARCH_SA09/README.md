# RESEARCH_SA09

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026.
This package studies Grothendieck's cotes 137 and 138 using the attached AI
transcriptions. It makes no claim to have inspected original scan images that
were not attached, and claims no priority.

## Start here

- `RESEARCH_SA09_report.md`: task and lead outcomes first; sources, computations,
  exact corrections, and verification record.
- `RESEARCH_SA09_paper.pdf`: the integrated 41-page paper, with 43 numbered
  statements and their proofs or checked source derivations.
- `RESEARCH_SA09_paper.tex`, `sections/`, `RESEARCH_SA09_references.bib` and
  `RESEARCH_SA09_paper.bbl`: complete typesetting source.
- `RESEARCH_SA09_results.csv`: one record per numbered statement.
- `CHECK_EVENTS.tsv`: actual proof, source, and computational check events.
- `PROGRESS_LEDGER.md`: initial gates and final review.
- `code/`, `logs/`, `notes/`: exact certificates, saved outputs, source-access
  records and independent proof reviews.
- `qa/`: rendered final pages, contact sheets, and visual-review report.
- `ARCHIVE_MANIFEST.json`: file sizes and SHA-256 checksums of archive payloads.

## Reproduce the mathematical certificates

With Python 3 and SymPy installed, run from this directory:

```sh
python code/final_verify.py
```

This executes all four mathematical certificate programs and saves their
complete stdout. Their finite ranges are explicit. General theorems are proved
in the paper, not inferred from bounded testing. The verification programs do
not download literature or need the original attachments.

To assemble the CSV, bibliography and check-event fragments:

```sh
python code/root_review_records.py
python code/assemble.py
```

These two programs assemble historical metadata; running them is not itself
a new proof check. The per-part registry writers are retained as documentation
of the work, not required for reproduction of the final assembled files.

## Reproduce the PDF

On a complete TeX Live installation, the ordinary commands suffice:

```sh
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA09_paper.tex
bibtex RESEARCH_SA09_paper
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA09_paper.tex
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA09_paper.tex
```

The build uses LuaLaTeX, Latin Modern fonts, and standard AMS/hyperref packages.
The execution environment lacked a prebuilt format and some Lua font support;
`notes/TEX_REPRODUCTION.md` and `code/tex_runtime_install.py` document the local
repair. After recreating that runtime, `python code/build_paper.py` produces
the captured multi-pass build and its statistics.

For rendered-page review, install Poppler, Pillow and pypdf, then run:

```sh
python code/render_qa.py --render
```

This regenerates labelled contact sheets. It does not perform or certify the
visual inspection; the actual inspection is recorded in `qa/QA_REPORT.md`.

## Source and archive scope

The original attachments are not duplicated. Fetched third-party article and
book text, source-page images, and TeX runtime caches are not redistributed.
The source-fetch scripts, request outcomes, exact locators, and source hashes
are retained. Source-reading JSON outputs retain their metadata and locators;
verbatim source-text fields are omitted in the exported copies, as recorded in
the manifest. Mathematical certificate outputs are retained in full.

Only the integrated paper PDF is delivered. A temporary section harness was
used during development, but its PDF is excluded. No checkpoint ZIP is nested
inside this package. The archive-building script is included and verifies CRCs,
required files, PDF count, result/event schemas, and the 500 MB size ceiling.
