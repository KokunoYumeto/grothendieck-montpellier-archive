# Build and reproduce

The standalone source comprises `main.tex` and the included proof file `supersingular_all_even.tex`; the bibliography is inline in `main.tex`. With a standard TeX Live installation, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The engine is pdfLaTeX. The source uses standard packages, T1 Latin Modern fonts, and author–date citations. Compilation requires no other manuscript, bibliography database, external figure, or downloaded source.

The exact arithmetic certificate uses the Python standard library only:

```sh
python rectangular_certificate.py --output rectangular_certificate.json
```

It reconstructs the Cartier operators, expands the parameter minors over the polynomial ring with two elements without division, and checks the stated local identities. The finite higher-degree matrices corroborate the uniform geometric proof; they do not prove an infinite family by sampling. The certificate and new text are CC0 1.0.

The additional thin-system program checks the explicit supersingular section in degrees including 8 and 10, and the mixed section at every nonzero parameter of the four-element field. It applies inverse Frobenius to vector coefficients at each iterate. Run:

```sh
python thin_cartier_certificate.py --output thin_cartier_certificate.json
```

These finite checks corroborate the uniform kernel and residue proofs; they do not establish uniformity by extrapolation.
