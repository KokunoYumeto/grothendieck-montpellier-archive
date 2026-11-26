# Build

Engine: pdfLaTeX (TeX Live). From this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline. All local inputs are included. No external
figures, custom style files, shell escape, or copied third-party sources are
required. `main.pdf` is the compiled paper.
