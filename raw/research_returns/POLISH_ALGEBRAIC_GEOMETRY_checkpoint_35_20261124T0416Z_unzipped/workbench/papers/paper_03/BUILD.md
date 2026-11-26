# Build

Engine: pdfLaTeX, standard TeX Live packages. Bibliography is inline.

From a fresh copy of this directory:

```
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. Keep `main.tex`, `representability.tex`, and `descent.tex` together. There are no image dependencies, custom styles, network calls, or external bibliography files.
