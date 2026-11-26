# Building the paper

## Engine and dependencies

Use pdfLaTeX and latexmk from a standard TeX Live installation. The current build uses pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian) and latexmk 4.86. Required standard packages are Latin Modern, AMS mathematics and theorem packages, mathtools, geometry, microtype, booktabs, longtable, array, enumitem, natbib, hyperref, and url.

## Exact build command

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

For a forced rebuild after editing:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex
```

No bibliography processor, custom style file, shell escape, source outside this directory, or network access is required. The `refs_*.tex` files hold the bibliography, and `sections/` holds all body inputs. The title's author field is empty.

## Verification

The final project is to be copied to a fresh directory and rebuilt there. The log is checked for undefined references and citations and for overfull boxes greater than 2 pt. Every PDF page is rendered and visually inspected. Whole-text expert and newcomer readings are recorded separately from compilation in the event register. A checkpoint PDF is a compiling draft and is not a declaration that those final checks are complete.

Useful independent commands are:

```sh
pdfinfo main.pdf
pdftoppm -r 110 -png main.pdf page
```

Rendering outputs and TeX auxiliary files are temporary inspection material and are excluded from the delivered project.
