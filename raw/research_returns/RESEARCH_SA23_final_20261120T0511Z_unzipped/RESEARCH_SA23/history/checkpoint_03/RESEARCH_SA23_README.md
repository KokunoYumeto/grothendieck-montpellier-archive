# RESEARCH_SA23

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 20 November 2026.
We claim no priority and attribute no work of this run to a human author.

## Reading the package

The current overall status appears on the first line of
`RESEARCH_SA23_report.md`. Its opening table has one row for every requested
item and Lead, with both the stable statement identifiers and the typeset
statement numbers.

- `RESEARCH_SA23_paper.pdf` is the current paper. Its first part contains
  checked statements and their proofs or exact derivations from opened
  sources. Its separate second part records uncertified assertions and
  remaining documentary questions.
- `RESEARCH_SA23_paper.tex`, `sections/`, and
  `RESEARCH_SA23_references.bib` are the complete typesetting sources.
- `RESEARCH_SA23_results.csv` has one row per numbered statement, with
  status, dependencies, proof location, manuscript pages, and notes.
- `CHECK_EVENTS.tsv` records the checks actually performed. Earlier study
  identifiers are preserved where their claims were checked or corrected.
- `CORRECTIONS.tsv` and the report anchor corrections to exact attached
  filenames and lines. A mistaken proof, a false statement, and an
  unsupported attribution are distinguished.
- `PROGRESS_LEDGER.md` records the requested progress states and reviews.
  A scheduled checkpoint is not a formal movement review.
- `code/`, `logs/`, `notes/`, and `verification/` preserve programs,
  outputs, source locators, failed retrieval attempts, audit notes, and PDF
  verification. Original attachments and reproducible full-source caches
  are identified but not copied into the working package.

## Reproducing the mathematical certificates

From the package directory, run the following with Python 3. The symbolic
geometry programs use SymPy. The other mathematical certificates use the
Python standard library unless their imports state otherwise.

```sh
python code/algebra_finite_checks.py
python code/category_counterexamples.py
python code/category_s3_obstruction.py
python code/geometry_finite_checks.py
python code/geometry_discriminant.py
python code/geometry_determinant_checks.py
python code/geometry_augmented_check.py
```

The matching saved outputs are in `logs/`. The report gives the exact
scope, counts, and measured runtime of each certificate. These finite or
symbolic checks support the specified claims; the proofs of statements
over infinite rings, categories, fields, and operator algebras are in the
paper.

Source-retrieval, OCR, rendering, and one-time editing scripts are retained
as records of the work. They are not a single pipeline to run indiscriminately:
some reproduce an earlier intermediate edit. The current merged sources,
registers, and paper are the entry points for continuing the research.

## Building the paper

With a standard TeX Live installation providing LuaLaTeX, BibTeX, Latin
Modern, and the packages named in the preamble, the ordinary build is:

```sh
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA23_paper.tex
bibtex RESEARCH_SA23_paper
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA23_paper.tex
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA23_paper.tex
```

`code/build_paper.py` records the same build cycle and its diagnostics in
the Linux environment used for this run. `code/setup_lualatex.py` records
the local repair of that environment; the downloaded TeX runtime is
reproducible and is omitted from the archive.

The actual delivery build log, overfull-box counts, and visual sample are
recorded in `logs/build_diagnostics.json` and
`verification/visual_QA.md`. An inspection of an older PDF is never
represented as an inspection of the current PDF.

## Continuing after an interruption

Use the newest saved checkpoint, its manifest and ledger, and the original
attachment. The manifest identifies prior checkpoints and omitted caches
by filename and hash. The supplied ZIP was extracted once in this run;
it is not nested into the deliverables. Read the open rows and their
current gates before repeating a source search or changing a proof.
