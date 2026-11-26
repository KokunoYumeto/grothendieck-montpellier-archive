# Build and verification

Run from this directory with a standard TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The tested engine is pdfTeX1.40.26 (TeX Live2025/dev). The preamble lists all standard package dependencies; bibliography entries are embedded. Include every local TeX input and the figures directory where present. No source download is required to build.

The current fresh build has 33 pages, zero overfull boxes, and no undefined references or citations. All pages have been inspected. Expert and newcomer readings are documented in the review record; independent theorem checks remain separately typed. The original execution environment required regeneration of its absent pdflatex format and explicit TeX/font-map roots, an environment repair that is not a manuscript dependency.
