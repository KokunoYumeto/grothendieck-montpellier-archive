# Build

The editable project is self-contained in `main.tex`; the bibliography is inline and there are no local inputs or figures.

Engine: pdfLaTeX (pdfTeX 1.40.27, TeX Live 2025 was used for this draft). From a fresh copy of this directory, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Required standard packages: fontenc, inputenc, lmodern, microtype, geometry, amsmath, amssymb, amsthm, mathtools, xcolor, hyperref, enumitem. No network access, bibliography processor, custom style, or shell escape is needed.

The current execution environment had an incomplete TeX file database and lacked a generated pdflatex format. An existing installed TeX Live tree was used to create a temporary format and font map outside the returned project. The fresh-copy build used the same command with a TEXMF override pointing to that temporary tree. No third-party TeX package or source material is included here.

Proof and literature status, the exact checks performed, and the PDF inspection record are in the workbench records. A successful build is not a claim that all research gates are closed.
