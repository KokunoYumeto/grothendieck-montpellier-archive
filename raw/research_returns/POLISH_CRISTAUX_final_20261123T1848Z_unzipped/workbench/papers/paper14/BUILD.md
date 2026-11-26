# Building the paper

Use a standard TeX Live installation containing pdfLaTeX, latexmk, the AMS packages, lmodern, geometry, hyperref, xcolor, microtype and natbib.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The source is standalone; it does not read other papers or downloaded works. The reviewed PDF has 13 pages. The author line is intentionally empty. The bibliography is contained in main.tex, so no external bibliography database is required.

The exact certificates use only Python 3's standard library:

```sh
python3 duality_certificates.py
```

Expected summary: passed=true; symbolic_dimensions=6; product_shuffles=64; dual_number_cases=144; nonzero_nilpotent_determinants=106. The program writes duality_certificates.json next to itself. These finite computations corroborate the algebra; the arbitrary-dimension and arbitrary-base proofs are in the paper.

The source and original code are dedicated under CC0 1.0. Third-party articles are cited and linked, not included. No network access is required to build the PDF or run the certificates.
