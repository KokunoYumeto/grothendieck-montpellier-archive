# Build

Engine: pdfLaTeX (TeX Live 2025 was used for the checked build).

The project is self-contained: `main.tex` contains the complete paper and inline bibliography. There are no external inputs, custom styles, figures, or bibliography programs.

From this directory, on a standard TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively use `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

Packages: fontenc, inputenc, lmodern, microtype, amsmath, amssymb, amsthm, mathtools, booktabs, array, geometry, hyperref, xurl. All are standard TeX Live packages.

Exact arithmetic certificate, Python 3 standard library only, from the deliverables root:

```sh
python3 programs/period_comparison_certificates.py
```

Expected final line: `ALL CERTIFICATES PASSED (exact arithmetic; no numerical transcendence inference).`

The certificate exhausts the 20, 42 and 110 smooth short Weierstrass coefficient pairs over F_5, F_7 and F_11 respectively. It verifies full local derivation matrices, the vertical term, and the Hasse coefficient by point counts. The written Cartier proof, rather than the finite computation, establishes the all-prime identity.

The expansion has a second independent exact-algebra and rational-bound certificate:

```sh
python3 programs/period_expansion_certificates.py
```

Expected final line: `ELLIPTIC EXPANSION CERTIFICATES PASSED`. It checks the explicit degree-two CM map, its scaling and exact differential, the value j=8000, and the rational estimates used in the E2-star Fourier proof. It does not check arithmetic transcendence. The written argument supplies the universal deductions and identifies the imported arithmetic theorem.

The checked expanded release has 84 pages and was built from a fresh directory in three pdfLaTeX passes. Every page was visually reviewed, with changed pages reviewed again after the last correction. Exact source/PDF hashes and the scoped check history are in the accompanying notes.

The local comparison expansion is mathematical text and introduces no new computational certificate. Its classification and comparison inputs are credited to the exact named primary theorems. The two-section identities and infinite Artin–Tate obstruction are proved in the paper. The current source crosswalk has 186 rows: 133 represented (one partly), one excluded, and 52 pending.

The real/adelic/orbit expansion likewise introduces no new computational certificate. It gives geometric and tensor proofs and uses exact named arithmetic inputs. The current 84-page build has no warnings. Page images1–5 and7–61 match the reviewed76-page edition; every changed or new page6 and62–84 was visually inspected after the seven-result number-field continuation. The separate fresh-worker main-theorem derivation and its exact named-input scope remain recorded in paper03_mathematical_gate_status_60page.md; the nine new rows and their different independence boundaries are in paper03_mathematical_gate_status_72page.md.

The elliptic-arithmetic expansion adds a third standard-library certificate:

```sh
python3 programs/period_elliptic_arithmetic_certificates.py
```

Expected final line: `ELLIPTIC ARITHMETIC CERTIFICATES PASSED`. It checks the exact Gauss–Manin numerator, torsion quartic identity, two mod-five counts, finite CM zeta denominator instances and horizontal equations/valuations. It proves no infinite-prime or transcendence claim by enumeration; the paper gives those arguments or imports exact named theorems.

The nine-result elliptic continuation uses written proofs and exact named primary inputs. Its supplementary exact calculations are checked by the additional program below. The refined analytic subgroup, quantitative density, ordinary inverse-Verschiebung, graph-rank and geometric-size inputs are identified in the paper. Two-jet and fixed-coordinate coefficient calculations are proved directly. The original statement-first attempt and the later dependency completions are recorded separately.

Additional late elliptic certificate, Python standard library only:

```sh
python3 programs/period_late_elliptic_certificates.py
```

Expected final line: `LATE ELLIPTIC CERTIFICATES PASSED (exact algebra and finite checks; no transcendence computation).` It checks generic matrix and product-jet coefficient identities, actual finite cyclic-subgroup sets and denominator sums, synthetic rational valuations, and the retained logarithmic example. General arithmetic conclusions remain in the written proofs.

The four-result comparison/Hodge continuation uses written geometric, linear-algebra and tensor arguments and exact named classical inputs. No new computational certificate is required for these proofs. Its precise source/freeze comparison and gate boundaries are in paper03_E_comparison_06.md and paper03_mathematical_gate_status_76page.md.

Number-field exact certificate, Python standard library only:

```sh
python3 programs/period_numberfield_certificates.py
```

The JSON output has `status: PASS`. It verifies the explicit CM j algebra, cubic trace/polarization matrices, discriminants and root intervals, quartic modular factorizations and permutation-matrix groups, and all cyclic-subgroup stabilizers among2454 invertible matrices over six stated moduli. The all-modulus lemma and arithmetic/categorical results are proved in the text or imported with exact primary locators. The07 comparison and84-page gate records preserve the original open CM-model input and its later replacement by the precise quasi-isogeny theorem.
