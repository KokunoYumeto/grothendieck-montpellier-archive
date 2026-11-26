# Build

Engine: pdfLaTeX (TeX Live), with standard AMS, Latin Modern, microtype, geometry, booktabs and hyperref packages.

From a fresh copy of this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The deliverable PDF is `main.pdf`. No external bibliography program or outside local input is required. All included TeX files are in this directory.
