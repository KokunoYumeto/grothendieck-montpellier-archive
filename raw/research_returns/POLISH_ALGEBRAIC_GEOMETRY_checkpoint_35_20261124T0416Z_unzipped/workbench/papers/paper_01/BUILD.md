# Build

Engine: pdfLaTeX, standard TeX Live packages.

From a fresh copy of this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline in `references.tex`; no BibTeX run or network access
is required. `main.pdf` is the resulting PDF. All local TeX inputs are included.

The current fourteen-page PDF was built three times from a fresh source copy.
There were no warnings, undefined references or overfull boxes. All final
pages were inspected; see `workbench/records/paper_1/FINAL_READS.md` for hashes
and the two full-reading records. A successful build is not mathematical
certification; check events state each proof's separate verification scope.
