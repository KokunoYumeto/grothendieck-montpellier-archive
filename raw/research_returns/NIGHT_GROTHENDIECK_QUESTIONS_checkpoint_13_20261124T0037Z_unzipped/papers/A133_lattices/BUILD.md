# Build

Engine: pdfLaTeX (TeX Live, standard packages).

From this folder, in a fresh copy of the project:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline. All local inputs are present in this folder. No downloaded source document is required. `main.pdf` is the compiled paper. The build check rejects any overfull box larger than 2 pt.
