# Build and reproduce Paper I

This directory is a complete editable paper project. The main PDF contains the text, all exact witness tables, the oriented-action program, and the complete seven-primary appendix. The source includes the local proof and author–year bibliography files supplied inside supplement_seven; keep that folder when building. The programs do not read the attachment or number-field binary data.

## Build the PDF

Run from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

A standard TeX Live installation with Latin Modern, AMS, `microtype`, `natbib`, `hyperref`, `booktabs`, `longtable`, `listings`, and `needspace` is sufficient. BibTeX is not required. Three passes stabilize the first clean build, including author–year citation suffixes and page references. In the current workspace, the repaired engine used for the recorded build is `/workspace/scratch/d302445fe866/tmp/texbin/pdflatex`; the source itself contains no dependency on that location.

## Reproduce the finite arithmetic

PARI/GP 2.19.1 was used. The following programs are standalone and can be executed from any directory:

```sh
gp -q programs/base_logarithmic.gp
gp -q programs/genus_start.gp
gp -q programs/ray_start.gp
gp -q programs/cyclotomic_action.gp
gp -q programs/logarithmic_bound.gp
```

Expected endpoints are `BASE_CERTIFICATES_COMPLETE`, `GENUS_START_CHECK_COMPLETE`, `RAY_START_CERTIFICATE_COMPLETE`, `FRESH_ACTION_CERTIFICATE_COMPLETE`, and `COMPACT_CERTIFICATE_COMPLETE_BOUND_729`. A GP error is a failed execution even when the interpreter process returns zero. The evidence files contain successful complete executions; earlier unsuccessful implementation attempts are distinguished in the full workbench review records.

The base program proves the logarithmic groups C3 for the real cubic field and C9+C3 for its normal closure, after complete class/unit and maximal-order certification. The action program recomputes its degree-nine class and unit data, certifies completeness, constructs the logarithmic presentation, identifies the automorphism with cyclotomic value four, and checks every primitive quotient character at absolute input precisions 60 and 90. The upper-bound program uses only exact algebraic witnesses, a certified maximal order, and logarithms at precisions 40 and 70; it makes no assumption about complete degree-eighteen class or unit bases. The genus program is a finite cross-check through level ten of the all-level formula proved in the paper. The ray program fully certifies the cyclotomic fields at levels zero, one and two and computes their ray groups modulo 269, including the image of the unique prime above three. Their three-primary types are C9, C27² × C3 and C27⁸, and imposing splitting at three changes none of them.

## Reproduce the independent analytic and ordinary class checks

The exact finite theta-positivity certificate uses Python 3 alone:

```sh
python3 programs/cubic_theta_certificate.py
```

For rigorous interval calculations and the independent ordinary class proof, install the versions in `requirements.txt`, then run:

```sh
python3 programs/cubic_theta_certificate.py --central --output evidence/cubic_theta_certificate.json
python3 programs/ordinary_classes.py --output evidence/ordinary_classes.json
```

The recorded environment used Python 3.12, Sympy 1.14.0, and python-flint 0.9.0. In the current workspace only, the extra Flint package is under `/workspace/scratch/d302445fe866/tmp/pydeps`; prefixing the latter commands with `PYTHONPATH=/workspace/scratch/d302445fe866/tmp/pydeps` makes it available without changing the programs.

The ordinary-class program proves an exact ideal-relation index seven, rigorously encloses the Hecke value at one, and proves that the displayed unit is fundamental. The paper supplies the independent unit-index and S3 arguments giving Cl(E)=C7+C7. The completed-function positivity theorem concerns the real axis and does not assert a Riemann hypothesis.

## Inspect the output

The completed PDF must have no unresolved references and no overfull box exceeding 2 points. To render every page:

```sh
mkdir -p preview
pdftoppm -png -r 90 main.pdf preview/page
```

## Seven-primary companion supplement

The related seven-primary theorem in the introduction has its complete proof
printed as Appendix D in the main PDF and an editable extract in supplement_seven. That subproject contains the printed
exact witnesses, interval specifications, portable verification programs,
and successful evidence. Its own BUILD.md gives the PDF build and complete
finite-certificate reproduction commands. The supplement proves the exact
faithful module Z7[[T]]/(7,T), arbitrary continuous cyclotomic specializations,
integral weights, and finite wild characters. The three-primary argument
in this main paper does not use that result.

The main project is dedicated to CC0 1.0 Universal. Cited external publications retain their own rights. No human verification is claimed.

## One-prime ramification and universal norms

Appendix E is included from the local source `seven_universal_norms.tex`. Its full proof and finite matrices are printed in the main PDF. The source has no dependency on another manuscript. To reproduce the exact first-layer unit matrices from the already supplied compact unit data, run:

```sh
python3 supplement_seven/programs/seven_first_layer_local_units.py
```

The expected determinant residues are 28 and 7 modulo 49. The proof derives the universal-norm index at all levels, the linear characteristic factor, the natural index-seven embedding, and the precise moving-center valuation formula. A separate model implementation verified every matrix coordinate; its distinct scope is recorded in the full workbench review.
