# Build

The standalone article uses pdfLaTeX and standard TeX packages, with inline bibliography.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Run the exact polynomial certificate with Python 3.10 or later; it uses only the standard library:

```sh
python pfaffian_certificate.py --output pfaffian_certificate.json
```

Expected result: all 360 nonempty supports across primes 3, 5, 7, 11, 13 and 17 are certified, with `passed: true`. The largest case has 1,465,345 surviving monomials in 43,263 distinct y-coefficients and 255 support witnesses. These are symbolic identities valid over every characteristic-two field. No conclusion for an unlisted prime is inferred.
