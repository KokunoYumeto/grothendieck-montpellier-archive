# Building the Weil-class criterion

Engine: pdfLaTeX, with standard TeX Live packages.

From this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is included in `main.tex`. No external paper, shared local
input, custom style, or figure file is required. The PDF must be rebuilt after
every mathematical correction. Build and page-review records accompany the
version; an early draft is not a certification of its unreviewed statements.
