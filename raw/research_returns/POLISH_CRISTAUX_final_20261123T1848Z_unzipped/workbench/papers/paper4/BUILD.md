# Build

This is a standalone LaTeX project. All mathematical text and the bibliography are in `main.tex`; it has no external inputs, figures, or generated data dependencies.

Use pdfLaTeX with standard TeX Live packages (`amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`, `lmodern`, `microtype`, `natbib`, `xcolor`, `xurl`, and `hyperref`). From this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Without latexmk, run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice. The output is `main.pdf`. The bibliography uses author–date citations and requires no BibTeX invocation.

The accompanying PDF was compiled from a fresh copy of this project, and every page was rendered and reviewed. Exact environment and review events are recorded in the workbench audit. The text is CC0 1.0.
