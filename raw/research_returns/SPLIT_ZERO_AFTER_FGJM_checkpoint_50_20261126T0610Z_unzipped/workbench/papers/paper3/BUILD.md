# Build Paper 3

The project is standalone: `main.tex` contains all mathematical text and its bibliography. There are no local style files or external figures.

## Standard build

Engine: pdfLaTeX, tested with pdfTeX 1.40.26 (TeX Live 2025/dev, LaTeX2e 2024-11-01). From a fresh copy of this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Packages: fontenc, inputenc, lmodern, microtype, amsmath, amssymb, amsthm, mathtools, booktabs, geometry, natbib, hyperref, url. All are standard TeX packages. Three passes settle cross-references; BibTeX is not needed.

`main.pdf` is built from the returned TeX source. The mathematical programs and certificates are in the workbench rather than required for typesetting. Computational commands are documented in the Paper3 records. The returned source has been compiled from a fresh copy with three passes. All pages have been visually inspected, and the mathematical and editorial reading passes are recorded in `checks/paper3_qa.md`. The exact scope of independent and targeted checks is recorded separately.
