# Build instructions

The manuscript is a standalone LaTeX source. It needs no external bibliography, image, generated lemma file or third-party source copy.

## PDF

Use a standard TeX Live or MiKTeX installation with `latexmk`, Latin Modern, the AMS packages, `mathtools`, `geometry`, `microtype`, `natbib`, `xurl` and `hyperref`.

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively, run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice. Inspect the log for unresolved references or overfull boxes before distributing a changed edition.

## Exact calculation

Python 3 with its standard library is sufficient:

```sh
python primitive_monodromy_certificate.py
```

This writes `primitive_monodromy_certificate.json`. It checks seven sparse polynomial identities over F2, six cycle-index calculations and a generated S5 matrix group with nonzero orbit sizes five and ten. The output includes the program's SHA256, so a textual edit to the program changes that metadata field even if all mathematical results agree.

The calculation is corroboration of finite algebra. The infinite-family geometric and monodromy arguments are contained in the manuscript.

New text and code are dedicated under CC0 1.0. Third-party sources are cited by reference and are not required in this directory.
