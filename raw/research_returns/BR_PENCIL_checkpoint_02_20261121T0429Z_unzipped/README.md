# BR_PENCIL research package

Research run BR_PENCIL-20261121-R1, dated 21 November 2026.

The checked principal result is CP border rank at least **43** in
characteristic zero for each polynomial 4-by-4 determinant and permanent
coefficient tensor. The bound **42** holds over every algebraically closed
field in the explicit integral model. The exact
requested two-dimensional residual minimum is3 for each row family and6
for each polynomial family. The paper carefully distinguishes these
objects and the all-field integral/divided-power convention. R-11 also
proves the characteristic-zero bound binom(n,2)^2+7 for both polynomial
families at every n>=4. The current size-four improvement gates are
recorded explicitly; no global bound44 is asserted.

## Contents

- `BR_PENCIL.tex` and `sections/`: the complete paper source.
- `BR_PENCIL.pdf`: compiled reading copy when present.
- `QUESTIONS.tsv`: questions, resolutions and precise current gates.
- `CHECK_EVENTS.tsv`: whole-proof reads, independent checks, computations
  and source checks, distinguished by their actual type.
- `LEDGER.md`: dated state, attempted approaches, review and checkpoint rules.
- `IMPLICATIONS.md`: mathematical, GCT and Grothendieck-framework consequences.
- `checks/`: portable exact certificates and their verifiers.
- `work/` in a checkpoint/final ZIP: research notes, exploration code,
  raw finite-search results and independent audits, including unsuccessful
  approaches. Exploratory data are not promoted to proved theorems.

## Reproduce the principal exact certificates

From any directory run:

```sh
python /path/to/unpacked-package/checks/verify_all.py
```

Install NumPy and SymPy alongside Python. The verifiers check integer
Koszul minors, exhaustive configuration coverage, finite-difference
identities, rational arrangement strata and higher-prolongation
certificates using exact arithmetic. Check output and logs are saved beside the verifiers. Modular search
code in `work/` additionally uses NumPy and, in some exploratory generators,
SymPy/SciPy. A nonzero modular minor is used only with its justified field
scope; the all-field42 theorem uses the explicit integer/unit certificates.
No part of this package is a formal theorem-prover development.

## Build the paper

Use a standard TeX Live or MiKTeX installation with the packages named in
the preamble, and run `pdflatex BR_PENCIL.tex` twice. The research environment
had an incomplete default format search path; its local workaround in
`work/fields_literature/run_pdflatex.py` is an environment aid, not a portable
build dependency. The ordinary LaTeX source and compiled PDF are the
portable deliverables.

## Resume an interrupted run

Read `LEDGER.md`, `QUESTIONS.tsv`, then the latest research notes and check
events. The original attachment was unpacked once into `source/`; use the
original supplied archive and prompt for predecessor materials. Checkpoint
ZIPs do not contain earlier checkpoint ZIPs or duplicate the input archive.
Downloaded external reference caches are represented by URLs, versions,
locators, hashes and audit notes; they are not required to rerun certificates.

This is a continuing research state until a final package is explicitly
issued. The strongest checked bound must not be replaced by an exploratory
candidate or a partially verified stronger bound.
