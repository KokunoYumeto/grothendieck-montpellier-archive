# Build

Engine: pdfLaTeX (TeX Live, standard packages).

From this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The main file uses local TeX inputs and an inline author-date bibliography.
No external source files, custom fonts, or unpublished style files are needed.
The final verification must be run from a fresh copy of this directory.
