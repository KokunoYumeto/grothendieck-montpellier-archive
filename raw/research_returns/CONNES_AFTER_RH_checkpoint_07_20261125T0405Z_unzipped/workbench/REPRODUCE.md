# Reproduction

## Manuscript

From `paper/`: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
The engine is pdfLaTeX, TeX Live 2025 in the producing environment. Standard packages only; there is no private style dependency. Before final delivery, build in a fresh directory and inspect all rendered pages. Checkpoint PDFs may precede the final visual and two-reader passes.

## Calculations

From the workbench root run `python3 checks/check_harmonic_packets.py` and `python3 checks/check_extensions.py`.
The harmonic calculation uses NumPy and SciPy and is explicitly a floating-point illustration. The independent mathematical proofs are in the paper.
The extension checks use exact arithmetic for 4,000 Euler coefficients and elementary matrix witnesses. They do not certify any Riemann hypothesis, a zero height, or a half-plane theorem.

## Provenance

External Lean verification reports were read as primary-source reports. No Lean kernel run was performed in this task. Publication PDFs, attached papers, and extracted source text are excluded from the archive. Source locators and available byte hashes are in the source registers.

## Source register and visual inspection

From the workbench root, `python3 checks/build_source_register.py` rebuilds the normalized SOURCES.tsv from original retrieval receipts; its output states the number of source records. The command prints the current number of records. Sources are linked and hashed where exact bytes were downloaded, never copied.

`python3 checks/render_paper_qa.py paper/main.pdf /absolute/qa-output` renders every page and six-page contact sheets. It records rendering hashes, not an inspection claim. Actual inspection is recorded separately in research/visual_qa_checkpoint04.json and research/visual_qa_checkpoint05.json; later revisions require their own pass.

For a guarded standalone rebuild from the workbench root, use `python3 checks/build_fresh.py paper /absolute/new-build-directory /absolute/new-build-record.json`. The directory must not exist. It copies editable sources, runs latexmk, checks references/overfull boxes, records source hashes, and copies a passing PDF back. Visual inspection remains a separate manual step. The latest full-page record is research/visual_qa_checkpoint07.json, matched to the passing build_checkpoint07d.json and its 101-page PDF. The earlier build07c failed on a20.59273pt overfull box; the short wording repair and clean rebuild07d are preserved rather than hiding that failure.
