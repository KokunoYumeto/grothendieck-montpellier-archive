# Build

Engine: pdfLaTeX, TeX Live with standard packages. Run from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All local TeX inputs are included. No shell escape or external bibliography tool is required. The root `build.py` builds each paper in a clean temporary copy, returns its PDF, and records overfull boxes and unresolved references.
