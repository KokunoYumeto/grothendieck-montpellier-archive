# ALP_MACHINE — active research package

This is an active-run checkpoint unless its archive is named `ALP_MACHINE_final.zip`. The main requested lift-count theorem, the arithmetic MainX pairing, and the Kummer Hecke RH theorem have not been established. Explicit partial theorems and their precise limits are in the paper sources and research reports.

## Contents and reproducibility

- `TASK_PROMPT.md` is the exact attached task.
- `ALP_MACHINE.tex` is the paper entry point. At the first checkpoint it is an interim reading guide; checked full proofs are in the included Markdown contributions. The final paper will integrate them with checked and unchecked parts separated.
- `QUESTIONS.tsv`, `LEDGER.md`, `CHECK_EVENTS.tsv`, and `IMPLICATIONS.md` record outcomes and open gates.
- `research/` and `agents/` contain full proofs, source audits, failed routes and exact locators.
- `scripts/` and `evidence/` contain reproducible computations. Every certificate states whether it is exact rational/symbolic computation or numerical evidence.
- `checks/` contains whole-proof reviews with dates, reviewer/model metadata and source-snapshot hashes.
- `research/alpoge_source/` contains recovered Lean text. The recovery manifests distinguish matches to supplied original-author hashes from pinned-mirror-only copies. No Lean compilation was performed in this run.

The supplied attachment was unpacked exactly once into `../sources/`. It remains the background source archive and is not copied into each new checkpoint. Public original PDFs are included when small, or represented by exact cited-page excerpts, URLs and original hashes when large. The 37 MB SGA 7 original is a reproducible external cache; its cited original pages and OCR used for navigation are included. OCR is not a substitute for the page scans.

No previous checkpoint ZIP is included in this archive. All substantive mathematical assertions retain their supplied or newly checked status; neither a computational check nor a source declaration inspection is called a formal proof build.
