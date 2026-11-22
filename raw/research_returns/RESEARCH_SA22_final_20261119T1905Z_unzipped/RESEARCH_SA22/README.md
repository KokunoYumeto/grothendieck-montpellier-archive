# RESEARCH_SA22

**Status: INCOMPLETE.** Read `RESEARCH_SA22_report.md` first. Its opening table gives the outcome and exact scope for every requested task and lead. `PROGRESS_LEDGER.md` preserves the dated substantive reviews and the remaining requirements. This package is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority is claimed.

## Main files

| File or directory | Purpose |
|---|---|
| `RESEARCH_SA22_paper.pdf` | Typeset mathematical paper, with checked statements and remaining source requirements separated. |
| `RESEARCH_SA22_paper.tex`, `sections/` | Complete authored LuaLaTeX source. |
| `RESEARCH_SA22_results.csv` | One row per numbered statement, using stable statement IDs. The report maps those IDs to the current theorem numbers and pages. |
| `RESEARCH_SA22_references.bib` | Aggregate bibliography with actual opened/not-opened scope and exact source locators. |
| `RESEARCH_SA22_report.md` | Task outcomes, readings, program scopes/counts/runtimes, exact input corrections and typesetting records. |
| `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv` | Dated progress reviews and the actual kinds and outcomes of statement checks. |
| `code/`, `checks/`, `notes/`, `logs/` | Research programs, retained execution records, finite certificates, proof audits, source-access history and build records. |
| `qa/paper*.png` | Rendered pages of the authored paper used for visual inspection. |
| `CHECKPOINT_CONTENTS.txt` | Exact contents of the most recently created checkpoint. The final archive, when produced, has its own final manifest. |

The unchanged attached inputs are supplied separately by the user and are omitted from this archive. The report's correction tables refer to their original paths and line numbers. Raw downloaded literature and full non-user source extracts are reproducible reading caches: the package retains their URLs, hashes, exact reading locators, acquisition scripts and execution metadata. Source-cache manifests distinguish those originals from the authored mathematical work. Earlier checkpoint ZIPs are kept separately rather than nested inside this package.

In the results CSV, **Refuted** classifies the original manuscript claim. The statement field explicitly identifies the active caption and records the proved refutation and any corrected scope; it does not assert that the counterexample itself is false. Contributor and historical records retain their original descriptive titles, with this distinction documented in the polarity audit.

## Compile the paper

A normal LuaLaTeX installation needs the packages named in the preamble, including `fontspec`, `unicode-math`, `amsmath`, `amsthm`, `mathtools`, `longtable`, `booktabs`, `enumitem`, `microtype`, `xurl`, `hyperref` and `bookmark`, together with the Latin Modern Roman and Latin Modern Math fonts. BibTeX uses the standard `alpha` style. The aggregate bibliography and all included section files are already present.

From the unpacked `RESEARCH_SA22` directory, run:

```sh
mkdir -p logs
lualatex -interaction=nonstopmode -halt-on-error -output-directory=logs RESEARCH_SA22_paper.tex
BIBINPUTS="$(pwd):" bibtex logs/RESEARCH_SA22_paper
lualatex -interaction=nonstopmode -halt-on-error -output-directory=logs RESEARCH_SA22_paper.tex
lualatex -interaction=nonstopmode -halt-on-error -output-directory=logs RESEARCH_SA22_paper.tex
cp logs/RESEARCH_SA22_paper.pdf RESEARCH_SA22_paper.pdf
```

The historical build scripts also record the isolated TeX-cache settings used in the execution environment. The commands above use the reader's normal TeX installation. The cache itself is excluded from the archive. Build and visual-inspection records identify the exact PDF hash that was checked; a fresh compilation may have different PDF metadata even when its mathematical content is unchanged.

## Reproduce a mathematical check

Use the report's program inventory and the corresponding scope note to select a particular certificate. Each mathematical program states its finite objects or symbolic identities, and its saved output records the actual counts and result. Floating-point diagnostics, exact finite certificates, source retrievals, page rendering and record assembly have distinct roles in that inventory. A successful finite check establishes only its stated finite instance or identity.

Most exact algebra programs use Python and, where indicated in their imports, SymPy. Source-reading utilities may additionally require Poppler, OCR or image libraries. A source-access failure is recorded as such and is never treated as a mathematical counterexample or as proof that a source does not exist.

The original durations of a few early failed or administrative executions were not recorded. The report marks those values unknown and distinguishes any later timed rerun. No runtime has been reconstructed from file timestamps.
