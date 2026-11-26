# Build instructions

The manuscript is standalone. It needs no external bibliography, figures, companion proofs, or third-party source copies.

From this directory, with a standard TeX Live or MiKTeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice. Required packages are Latin Modern, AMS mathematics, mathtools, geometry, microtype, natbib, xurl and hyperref. Check the final log for unresolved references and overfull boxes.

## Exact arithmetic supplement

Python3 and its standard library suffice. From the workbench directory:

```sh
python3 programs/paper16_boundary_checks.py
```

The program imports `paper16_factor_order_checks.py` from the same directory and writes the combined exact results. Its finite checks include direct group orders, exhaustive small-matrix elimination, incidence ranks, error-polynomial coefficients and degree inequalities. They corroborate the displayed symbolic proofs; they do not establish a geometric monodromy theorem by sampling.

New text and original code are dedicated under CC0 1.0. Sources cited in the bibliography are not included in this directory.
