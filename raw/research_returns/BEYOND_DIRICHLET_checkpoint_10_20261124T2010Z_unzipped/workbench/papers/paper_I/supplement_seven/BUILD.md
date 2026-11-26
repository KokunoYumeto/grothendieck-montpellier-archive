# Editable seven-adic supplement

This project contains the complete proof, every exact compact witness,
the interval specifications, and portable verification programs for the
seven-adic theorem stated in the main paper.

## Build

From this directory:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The standard packages used by main.tex are sufficient; no bibliography
processor or external source file is required.

## Reproduce the finite certificate

Use PARI/GP 2.19.1, Python 3, and python-flint 0.9.0.

    gp -q programs/seven_compact_verify.gp
    python analytic/certify.py
    python programs/seven_compact_arb.py

The GP command must be run from this directory. Both Python commands
resolve their inputs and outputs from their own locations.
The L-value command regenerates the analytic input before the regulator
command uses it. Its default precision and cutoffs are exactly those
specified in the proof. Existing successful evidence is included.

The verifier does not read a BNF binary, an asserted complete class group,
or an unverified regulator. The exact data contain only field polynomials,
units, automorphisms and residue characters. Full class numbers away from
seven are not needed.

The proof and programs are CC0 1.0 Universal. Cited publications retain
their rights. No human verification is claimed.
