# Standalone build

Engine: pdfLaTeX (TeX Live with standard packages). From a fresh copy of this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The third run stabilizes the table of contents and page references in a clean directory. The bibliography is inline. No external files, programs or downloads are required to build or read the proof. The resulting deliverable is `main.pdf`.

The current document has 55 pages. Its build has no unresolved references, LaTeX warnings or overfull boxes. One harmless underfull table box remains. See the separate review and build records at the deliverables root.

Current release: all 55 final pages were actually viewed after three successful configured clean passes. The runtime required an isolated map combining installed font maps with rsfs.map; the complete workaround and initial plain failure are recorded in ../../checks/continuation_paper01_build_candidate.py. No system configuration was changed. Exact scopes and hashes: ../../notes/continuation_paper01_candidate_final_release.json.
