# Building the paper

Use a standard TeX Live installation with pdfLaTeX, latexmk, AMS packages, lmodern, geometry, microtype, natbib, xurl, xcolor and hyperref.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The source is standalone: the complete text, proofs and bibliography are in main.tex. It reads no other paper, downloaded article or network resource. The author line is intentionally empty. No program or finite numerical certificate is needed for the all-prime symbolic proofs.

The reviewed PDF has 13 pages. It was built in a fresh directory from the source alone, with zero overfull boxes and zero undefined references. Every page was read and viewed; the complete mathematical and exposition readings are recorded with their exact scopes in the workbench records.

Text and original source: CC0 1.0. Third-party articles are cited and linked, not included.
