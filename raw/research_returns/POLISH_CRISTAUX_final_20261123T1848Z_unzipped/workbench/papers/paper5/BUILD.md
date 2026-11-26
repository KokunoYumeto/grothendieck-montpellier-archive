# Build

This is a standalone LaTeX project. The bibliography is inline in `main.tex`; no external inputs, images or custom styles are required.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Equivalent command when latexmk is unavailable: run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice.

Tested engine: pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev, Debian). Standard packages include amsmath, amssymb, amsthm, mathtools, geometry, microtype, lmodern, natbib, xurl and hyperref.

The finite certificate is run from the workbench root with:

```sh
python3 code/nodal_twist_identities.py
```

Its JSON output must equal `code/nodal_twist_identities.expected.json`. It checks finite polynomial identities by exact evaluation with degree bounds. It does not certify the infinite ring or any geometric assertion.
