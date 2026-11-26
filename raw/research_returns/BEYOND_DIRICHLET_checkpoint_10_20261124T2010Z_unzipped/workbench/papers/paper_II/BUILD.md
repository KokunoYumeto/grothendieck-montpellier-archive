# Paper II: build and verification

This directory contains a newly written research manuscript, not an unchanged copy of the supplied source material.

## Build

From this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The actual session build used the repaired local wrapper for both passes:

```sh
/workspace/scratch/d302445fe866/tmp/texbin/pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The wrapper points to the available pdfTeX binary with a generated format and font map. A normal TeX Live installation needs only the two standard commands above. Keep both `offcentral_obstructions.tex` and `functorial_identities.tex` beside `main.tex`; they supply the complete proofs in Appendices C and D and are required source files. The bibliography is embedded in `main.tex`; no BibTeX run or external bibliography file is needed. `latexmk -pdf main.tex` is an equivalent convenience command when installed.

## Exact field checks

```sh
gp -q -f field_checks.gp > field_checks.txt
```

The session's PARI/GP build is version 2.19.1, at `/workspace/scratch/d302445fe866/tmp/pari/pari-2.19.1/gp`. The checks use integer discriminants, exact finite-field factorizations, exact Sturm real-root counts, and PARI's Galois-group routine. The finite-field factorization witnesses also supply a short proof of the group assertion independently of the reported group label.

These algebraic computations alone do not certify a real-zero hypothesis. The analytic programs below certify discriminants 8249 and 60061; the autocorrelation certificate below additionally settles discriminant 30301, and the wild-prime calculation and triangular certificate settle discriminant 48976. The discriminant-1609 case is a published certified example of Calegari and Booker. Its Frobenius at 5 is a 5-cycle; Pilloni–Stroh now supplies the modularity input without Calegari's separate two-adic construction.

## Certified real nonvanishing

From the workbench root, the MPFR certificates run as follows:

```sh
python programs/s5_8249_mpfr_certificate.py > certificates/s5_8249_mpfr_certificate.json
python programs/s5_squarefree_mpfr_certificate.py --discriminant 60061 --output certificates/s5_60061_mpfr_certificate.json
```

The first program uses the Python standard library and the system MPFR shared library, loaded with `ctypes`. It requires GNU MPFR with correctly rounded directed operations; the recorded run used MPFR 4.2.2 and 160-bit endpoint precision. The second imports its endpoint and exact polynomial primitives from the first, so both files must remain in the same program directory. Field data and prime-power traces are recalculated from exact integer inputs.

The independently written Arb checks use Sympy 1.14.0 and python-flint 0.9.0:

```sh
python programs/s5_8249_arb_check.py --output certificates/s5_8249_arb_check.json
python programs/s5_arb_certificate.py --discriminant 60061 --output certificates/s5_60061_arb_certificate.json
```

In this session the additional Flint package is under `/workspace/scratch/d302445fe866/tmp/pydeps`; prefixing these commands with `PYTHONPATH=/workspace/scratch/d302445fe866/tmp/pydeps` exposes it. A regular installation of `python-flint==0.9.0` does not need that prefix. The Arb programs use 192-bit arithmetic and 2048 integral cells, independently factor the quintics modulo each relevant prime, and count traces on actual permutations of points and unordered pairs. The larger ramified prime 3533 for the second field is also factored even though it lies outside the prime-sum cutoff.

The mathematical argument and exact rational bounds are in Section 9. Both certificates use a test with nonnegative real part on the entire zero strip; they do not assume GRH, sample positivity on a finite grid, or rely on an unverified numerical zero list. The detailed author check is in `../../reviews/s5_8249_real_zero_proof.md`; the separate check is in `../../reviews/s5_8249_root_check.md` and the root check records.

### Third field: discriminant 30301

From the workbench root:

```sh
gp -q -f experiments/s5_real_zero/mpfr_30301_traces.gp > experiments/s5_real_zero/mpfr_30301_traces.csv
python programs/s5_30301_autocorrelation_mpfr.py --traces experiments/s5_real_zero/mpfr_30301_traces.csv --output certificates/s5_30301_autocorrelation_mpfr.json
```

The new program uses the existing directed-MPFR primitives but implements the positive autocorrelation test, nonsingular gamma integrand, and prime sum independently of the Arb certificate. It uses 160 bits and 16384 integration cells. The exact 32 integer weights and all autocorrelations are recalculated; the code asserts the displayed strict rational bounds. The fresh PARI stream contains 595877 prime-power traces and agrees byte for byte with the independently calculated FLINT stream. Its SHA256 is `099105b98cbfcff394f24fe472b91f28d434d8f9f2a980ef1a23ebcf1a6ba8eb`.

The separate root implementation is `programs/s5_30301_autocorrelation_arb.py`, with output `certificates/s5_30301_autocorrelation_arb.json`. It uses 192 bits and 32768 cells and independently factors all 595341 primes. Both implementations prove zero sum < 11 < 111/10 < real-zero threshold. No external real-zero-location theorem is needed.

### Fourth field: discriminant 48976

From the workbench root:

```sh
python programs/s5_48976_mpfr_certificate.py --output certificates/s5_48976_mpfr_certificate.json --traces experiments/s5_real_zero/euler_traces_48976_mpfr.csv
gp -q -f experiments/s5_real_zero/local_48976.gp > certificates/s5_48976_local_pari.txt
gp -q -f experiments/s5_real_zero/pari_48976_traces.gp > experiments/s5_real_zero/euler_traces_48976_pari.csv
python programs/s5_48976_arb_check.py > certificates/s5_48976_arb_check.out
```

The MPFR program imports both earlier primitive modules and uses 160 bits and 2048 cells. Its exact local input at two is proved in Corollary 9.5: the lower inertia groups are A4, V4, and 1; the conductor exponent is six; and the local denominator is 1+T. The complete conductor is 2^6·3061^3. A second proof uses the degree-ten pair field, whose full integral bases, discriminant, index and unconditional `nfcertify` output are retained. No class-group calculation or GRH assumption enters this step.

The separate Sympy/Arb program recalculates the quintic maximal order, enumerates transitive A4 subgroups, computes invariant dimensions and the wild Frobenius trace directly, and independently factors every relevant finite-field polynomial. At 192 bits and 4096 cells, it proves the same exact bounds as MPFR: S<61/10<224/25<2H(0), with gap >14/5. Its 465 trace rows agree with both our exact polynomial arithmetic and a fresh PARI calculation. The shared trace CSV SHA256 is `9f56ac56983838553c929a09270c0e6ec56756ced7fce7e27dce2db0148e8fb2`.

The full mathematical record is `../../reviews/s5_48976_local_and_real_zero.md`. The optional Liu zero-free bound in Section 10 is a separately named external theorem and is not needed for any finite certificate or the central-zero comparison theorem.

## Mathematical check boundary

The central-zero rigidity argument was reconstructed from the statement and published sources before the supplied `source/ours/` proofs were opened. The independent derivation is recorded in `../../reviews/s5_independent.md`. Subsequent source audit confirmed the Fourier interpretation and corrected the numbering of Calegari's published lemmas: the Landau lemma is 4.9, and equality at the remaining places is Lemma 4.10.

The manuscript proves equality of standard local L-factors at every place, including gamma factors, in the sense of Calegari's result. It does not replace that conclusion by an unsupported assertion that standard factors determine all ramified Weil–Deligne parameters.

Classical inputs are Calegari's automorphic construction and finite-exception lemma, Landau's theorem, Bochner's theorem, Cohen's idempotent theorem, the discrete-coset consequence proved by Kolountzakis, and order-one Hadamard factorization. This is same-model mathematical checking, not a claim of independent human peer review or formal verification.

## Off-central boundary results

The canonical-removal theorem and Appendix C prove canonical logarithmic positivity loss at arbitrary multiplicity and a sufficient rigidity criterion for a finite-progression description of the entire divisor. The appendix includes the complete proofs and three scoped countermodels. These results do not remove the general real-zero hypothesis or improve its remaining interval. The exact-prime construction imports only the stated Baker–Harman–Pintz short-interval estimate; the other new arguments use the named classical harmonic-analysis inputs.

The author's full proof record is `../../reviews/s5_offcentral_new_reductions.md`. The isolated targets are `../../reviews/s5_offcentral_statement_targets.md`. A fresh same-model agent reconstructed all six targets without opening the author proof or the manuscript; its complete record is `../../reviews/s5_offcentral_blind_reconstruction.md`. Its general-multiplicity proof uses Gaussian damping, a Følner-box limit, and Laplace-measure uniqueness instead of the manuscript's Haar-component argument. The separate reconstruction and the manuscript proof were subsequently compared. Source-use metadata and hashes are in `../../reviews/s5_offcentral_sources.json`; source PDFs remain outside the manuscript deliverable.

The optional Liu endpoint in Section 10 uses the stronger Theorems 1.2 and 8.29, with the degree-nine constant defined by that paper's equations (42) and (44). The exact isolation interval is checked by `../../programs/liu_boundary_exact.py`, with output in `../../certificates/liu_boundary_exact.json`. That finite algebraic check is separate from, and does not independently re-prove, the external analytic theorem.

## Published scope upgrade and common-zero theorem

The main arithmetic assumptions are now only an S5 Galois extension and complex conjugation of type (12)(34). Pilloni–Stroh Théorème 0.3 replaces Calegari's Lemma 3.2 modularity input. The complete downstream dependency audit is in `../../reviews/s5_scope_upgrade_reconstruction.md`, with its statement-only packet beside it. Root's primary-source targeted audit passed. A separate same-model agent reconstructed the entire scope package from the statement and primary sources before opening the author proof or manuscript; its proof is `../../reviews/s5_scope_upgrade_cubic_analytic_blind.md`. It explicitly grants the previously checked central-pole exclusion theorem, and does not claim to re-prove that prior theorem. Root and the author have read the complete reconstruction and found no discrepancy.

The main real-zero condition is absence of common off-central real zeros of B=zeta_H/zeta_F and C=zeta_J'/zeta_J. Belt Theorem 6.2 supplies odd-rank partial exterior-square entirety; every comparison pole of order r forces zeros of both functions of order at least r. All bad factors are explicitly removed, with nowhere-zero corrections in Re(s)>0. The author proof and root's separate statement-only reconstruction are in `../../reviews/s5_common_zero_proof.md` and `../../reviews/s5_common_zero_root_blind.md`; their exposure scopes are stated there. Both the root reconstruction and subsequent targeted reading passed.

The exact finite checks run from the workbench root:

```sh
python programs/s5_functorial_identities.py
python programs/s5_common_zero_finite.py
```

Their JSON outputs are in `../../certificates/`. Appendix D proves the representation identities and conditional transfer equivalences in full. These equivalences do not assert existence of the extra symmetric-square or Asai transfer. Source URLs, hashes and exact reading scopes are in `../../reviews/s5_functorial_sources.json`; the research outcome is in `../../reviews/s5_functorial_followup.md`.

## Visual verification

After compiling, render with:

```sh
pdftoppm -r 90 -png main.pdf rendered/page
```

The final check log records the actual compilation and rendered-page review. The numerical examples and bibliography must be checked against the final PDF, not only the TeX source.

Final compilation and visual-review details are in `CHECKS.md`. All four real-zero certificates and their separate Arb checks pass. `CHECKS.md` records the final PDF page count, compilation checks, and rendered-page review.


## Symmetric-square appendix and exact Rankin--Selberg citations (24 November 2026)

Appendix D now includes Proposition D.4 and Remark D.5: the full fifteen-point symmetric-square proof, signature and infinite factor, exceptional-prime table, all finite deletions and meromorphic orders, the conditional three-function consequence, and the decisive identity D=L(V)L(R)zeta_F. The latter proves that this criterion is subsumed by the existing Artin-factor variant; no new field or stronger criterion is claimed. Section 1 and the numerical certificates are unchanged.

The independent proof froze at 19:18:10 UTC before the authored symmetric-square note was read. The proof, exact integer checks, source/exposure receipt, and post-freeze targeted corrections are under `../../reviews/s5_symmetric_square_independent_1911_*`. The frozen proof SHA256 is `82c7427f0140855f272fae10e247cbf5d033f186635ab5e5654a2333e5dd51e5`. Takeda (2015), arXiv:1506.04791v1, Theorem 7.1 on pp.49--50 was personally inspected; its analytic proof remains an external input. The existing conditional-transfer argument now cites Jacquet--Shalika (1981 II), Proposition 3.3 p.795, Proposition 3.6 pp.802--804, Theorem 3.7 p.804, and Shahidi (1980), theorem p.462, all checked in the primary page images.

The amended source was built in the fresh isolated directory `../../reviews/s5_symmetric_square_mainII_stage_20261124_1922/`. Three successful sequential wrapper passes produced the current **43-page** PDF. The final log has no errors, unresolved references/citations, overfull boxes, LaTeX warnings, or natbib warnings. Pages **38--43 only** were freshly rendered and personally inspected for this amendment, covering all changed mathematical text and new references; this does not claim a new visual inspection of all 43 pages. The prior 41-page source/PDF, BUILD, deposit, checks and manifest are preserved read-only in `../../reviews/paper_II_before_symmetric_square_20261124_192143/`. Detailed machine receipt: `symmetric_square_build_receipt.json`.
