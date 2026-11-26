# Reproducing the paper and its certificates

All commands below start in the **workbench root** (the directory containing this file). This index covers all 27 returned Python check/certificate programs. It was prepared from their command-line parsers, input/output code and saved receipts on 23 November 2026; the expensive computations were not rerun during final packaging.

Use a disposable copy of the workbench for a replay. Many programs intentionally replace their adjacent JSON certificate, and `check_weil_certificate.py` updates the arithmetic receipt in place. Preserve the delivered archive and its manifest. Regenerated elapsed times, numerical proposal vectors and JSON hashes need not be byte-identical; the stated assertions, rigorous enclosures and mathematical conclusions are the replay targets.

## Environment and paper build

The recorded runtime is Python 3.12.14, python-flint 0.9.0, SymPy 1.14.0, NumPy 2.3.5 and SciPy 1.17.0. The commands use `python3`; select a Python environment with those packages. For example, in a suitable environment:

```sh
python3 -m pip install python-flint==0.9.0 sympy==1.14.0 numpy==2.3.5 scipy==1.17.0
```

`flint` in the source is the **python-flint** package, which provides Arb/Acb ball arithmetic. SymPy supplies exact symbolic algebra. NumPy/SciPy propose finite eigenvectors in the local-probe computation; the program subsequently certifies the required quantities in Arb. The pure rational spectral check needs only the Python standard library. No GPU or network access is used by the computations themselves. The paper build needs pdfLaTeX/TeX Live and latexmk with standard packages:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd ..
```

Expected: a 169-page `paper/main.pdf`, with no overfull boxes or unresolved references. The delivered PDF is identified by SHA256 `1c6183b2a61aa8d4290ec8cbb05dddb78f3b0abeeb4dd13664188f095925cd7e`; a rebuild can differ in PDF metadata. `paper/BUILD.md` gives the clean-copy procedure. PyMuPDF 1.26.6 and Pillow 13.0.0 were used for the recorded visual workflow; they are not dependencies of the 27 certificate programs.

## Small exact and scalar checks

In this table, a JSON filename without a directory is written beside the named program. “PASS” means the program reaches its final printed success message after its assertions. These finite checks do not replace the analytic proofs or prove all-zero simplicity.

| Command from workbench root | Dependencies | Expected result and destination |
|---|---|---|
| `python3 checks/check_heat_trace_polynomials.py --max-degree 8` | SymPy | 66 partitions and 416 determinants pass; `checks/heat_trace_certificate.json`; prints the triple-plus-simple and two-double order profiles. |
| `python3 checks/check_phase_models.py` | SymPy | 28 single-center and 12 two-center exact discriminants/monodromies; rounding bound below 1/2; `checks/phase_models_certificate.json`. |
| `python3 checks/check_survival_constant.py` | python-flint | Printed JSON has `all_checks_passed: true`, survival constant in `(0.6725007,0.6725008)` and distinct constant in `(0.8362503,0.8362504)`; `certificates/survival_constant.json`. |
| `python3 checks/certify_gap_packet.py` | python-flint | PASS: 25 positive zeros through 90, specified gap and reciprocal-gap bounds, independent 80/120-digit evaluations; `certificates/indexed_gap_packet.json`. This program explicitly uses the certified indexed-zero routine. |
| `python3 drafts/finite_detection/check_detection_constants.py` | python-flint | PASS: `0 < F_0'(0) < 1/2` and explicit PF constant `2^-36`; `detection_constants_certificate.json`. |
| `python3 drafts/finite_detection/check_moment_gate.py` | SymPy | Five finite examples: exact residues, Schur complements and endpoint recovery agree; `moment_gate_certificate.json`. |
| `python3 drafts/finite_detection/check_kernel_surgery.py` | SymPy, python-flint | PASS exact derivative polynomials and rational monotonicity bounds; `kernel_surgery_certificate.json`. |
| `python3 drafts/finite_detection/check_zero_surgery.py` | python-flint | PASS nonzero derivatives at the first two positive zeros; `zero_surgery_certificate.json`. Uses the indexed-zero routine. |
| `python3 drafts/finite_detection/check_weil_normalization.py` | SymPy, python-flint | PASS direct hat convolution, exact `-log(4)` normalization and six independently evaluated constants; `weil_normalization_certificate.json`. |
| `python3 drafts/finite_detection/check_external_height_growth.py` | python-flint | JSON gives Toeplitz/window lower bound `1650000000000` and Jensen lower bound `4500000000000000000000000`; `external_height_growth_certificate.json`. The published height `3*10^12` is an input; this program verifies only the scalar transfer. |
| `python3 drafts/spectral_audit/check_spectral_identities.py` | Standard library | Prints `4/7`, `16/31`, variance `72/217`, coefficient `359/1736`, the 60,500-pair check, trace examples and `PASS: all exact checks`. Output is stdout; the saved transcript is `spectral_identities_certificate.txt`. |
| `python3 drafts/fresh_contour_check/check_residue_algebra.py` | SymPy | Prints `i difference: 0` and `j difference: 0`; asserts both polynomial identities. No output file. |
| `python3 drafts/moment_independent/check_formal_kernels.py` | SymPy | Zero division remainders, both target identities true, 62 coefficients; `formal_kernel_results.json`. Finite formal algebra only. |
| `python3 drafts/moment_independent/check_density_certificate.py` | SymPy | Reads the preceding `formal_kernel_results.json`; exact Bernstein/integration checks and `count_floor = 1/12960000000000`; `density_certificate_results.json`. Its recorded nonzero literal remainder documents a corrected identity, not a failed final certificate. |

The following four motion programs accept an output argument. These commands place the results beside the programs instead of using their default output in the current directory:

```sh
python3 drafts/motion_collisions/certify_hurwitz_motion.py --output drafts/motion_collisions/hurwitz_motion_certificate.json
python3 drafts/motion_collisions/certify_low_height.py --output drafts/motion_collisions/low_height_certificate.json
python3 drafts/motion_collisions/certify_square_mollifier.py --output drafts/motion_collisions/square_mollifier_recomputed.json
python3 drafts/motion_collisions/certify_cue_agreement.py --degree 110 --digits 180 --output drafts/motion_collisions/cue_agreement_recomputed.json
```

The Hurwitz, low-height and CUE programs use python-flint; the square-mollifier program uses SymPy. Expected outputs, respectively: the certified reversal at zero 1169 at 80 and 120 digits; `c1<1/128` and Euler-sector bound below `3/4`; a 62-monomial kernel with exact Bernstein/beta checks and certified sign fraction; and a rigorous CUE agreement enclosure strictly inside `(0.66654660183721072003, 0.66654660183721072008)`.

A separately written CUE implementation uses the centered Legendre basis:

```sh
python3 drafts/spectral_audit/recompute_cue_agreement.py
```

It uses python-flint, degree 110 and 180 decimal digits, writes to stdout, and should end with `PASS` after certifying

```text
0.6665466018372107200719020708703
  < A <
0.6665466018372107200719020748216.
```

The delivered transcript is `drafts/spectral_audit/cue_agreement_independent_certificate.txt`. Both CUE determinant evaluations can take materially longer than the scalar checks.

## Arithmetic matrix certificates and their dependent checks

The main arithmetic computation is expensive, especially level 6 (dimension 766). It does not take zero ordinates as inputs. To regenerate all six saved levels with the recorded precision and moment depth:

```sh
python3 drafts/finite_detection/check_weil_compressions.py --levels 1 2 3 4 5 6 --dps 120 --moments 10
```

Output: `drafts/finite_detection/weil_compression_certificate.json`, updated after each completed level. The script merges requested levels into an existing destination. Expected dimensions are `2,14,46,126,318,766`; saved strict rational certified heights are `14.134,20.704,26.782,39.913,62.413,97.632`. The program prints a PASS record with dimension, trace defect, best height and moment order for each level. A smaller first replay is `--levels 1 2 3`; use `--output PATH` to keep a separate arithmetic receipt, noting that dependent programs below read the canonical adjacent filename unless explicitly configured otherwise.

Three further returned programs read that arithmetic receipt:

| Command | Expected result and destination |
|---|---|
| `python3 drafts/finite_detection/check_weil_certificate.py` | Checks six displayed rational heights, congruence residuals and the scalar `pi/sqrt(D)` consequences. Updates `weil_compression_certificate.json` in place. It expressly does **not** recompute the arithmetic trace enclosures. |
| `python3 drafts/finite_detection/check_global_growth.py` | Reads level 6 and writes `global_growth_certificate.json`, certifying the arithmetic-only global constants and their comparisons. |
| `python3 drafts/finite_detection/check_separation_certificate.py` | Reads level 6; PASS `alpha6>7e-17`, spacing `>6e-10` through 90 and reciprocal spacing `>1.48e-13` through 45; writes `separation_certificate.json`. |

All three use python-flint. Their input is delivered. After a fresh matrix regeneration, run `check_weil_certificate.py` before generating new spectral-probe receipts, because the probe provenance includes the exact bytes of this arithmetic receipt.

## Local spectral probes, including the distinct-precision replay

The delivered receipt-only validation can be run **before changing any input receipts**:

```sh
python3 drafts/spectral_audit/check_local_probe_certificate.py
```

It reads four delivered probe receipts and the delivered arithmetic receipt. It checks exact program/input hashes, the displayed level-4 bounds, both rounding tests and distinct-precision overlaps. Expected: `PASS: all displayed N4 rational bounds, arithmetic-only provenance, both rounding tests, and distinct-precision pairing overlaps.` It writes no file. The program needs python-flint; it validates the saved certified arithmetic rather than rerunning the matrix integrations.

To regenerate the probe computations after the arithmetic stage, run the following in order. These require python-flint, NumPy and SciPy and can be expensive:

```sh
python3 drafts/spectral_audit/certify_local_probe.py --levels 3 4 --dps 120 --targets 1 --output drafts/spectral_audit/local_probe_certificate.json
python3 drafts/spectral_audit/certify_local_probe.py --levels 4 --dps 160 --targets 1 --output drafts/spectral_audit/local_probe_residual_replay.json
python3 drafts/spectral_audit/certify_local_probe_mass.py --levels 3 4 --dps 120 --residual-input drafts/spectral_audit/local_probe_certificate.json --output drafts/spectral_audit/local_probe_mass_certificate.json
python3 drafts/spectral_audit/certify_local_probe_mass.py --levels 4 --dps 160 --residual-input drafts/spectral_audit/local_probe_residual_replay.json --output drafts/spectral_audit/local_probe_mass_replay.json
python3 drafts/spectral_audit/check_local_probe_certificate.py
```

The residual generator imports `drafts/finite_detection/check_weil_compressions.py` by its path relative to `__file__` and reads the adjacent arithmetic receipt. The mass generator imports that residual module and uses the same arithmetic receipt. At level 4 the saved certificate has divided mass in `(0.9996487647,0.9996487649)`, logarithmic rounding error below `0.080978`, arithmetic reciprocal gap greater than `9/400`, and certified multiplicity one through height 20. Both precision runs must pass the final validator. Floating-point eigenvector proposals can vary across linear-algebra implementations; the outward-certified inequalities, rather than proposal bytes, are required to agree.

## Whole-edge heat contours

These programs use python-flint/Arb integration and can be expensive. They use no indexed zero list. The saved certificates integrate the count moment and combine it with the displayed sign-change brackets:

```sh
python3 checks/certify_heat_contour.py --height 20 --dps 100 --moments 1 --output certificates/heat_contour_height_20.json
python3 checks/certify_heat_contour.py --height 45 --dps 100 --moments 1 --output certificates/heat_contour_height_45.json
```

Expected: `PASS` and the output path, with whole-edge positive boundary bounds, a positive complex-time radius, counts 1 and 8 respectively, `no_indexed_zero_input: true`, and `all_enclosed_zeros_simple: true`. `--moments` is the number of integrated moments, starting at order zero; the delivered count receipts use 1. These saved runs do not claim a full 8-by-8 Hankel computation. The exact finite Hankel examples are covered by `check_heat_trace_polynomials.py`.

## Paths, inputs and scope

No executable in this 27-program inventory contains a hard-coded `/workspace`, `/home` or `/tmp` input/output target. File inputs are resolved relative to the program, and the four motion programs and several larger computations offer the output arguments shown above. Some historical docstrings say `python workbench/...`; that spelling assumes the parent directory. From the workbench root use the commands in this index, which omit that leading component. No source-code path edit is needed for these programs when the returned directory structure is retained.

The two dependency chains that must remain together are the formal-kernel JSON followed by its density check, and the arithmetic JSON/module followed by the spectral-probe generators and validator. Every required program and certificate in those chains is returned. The 27 programs require **no original attachment as a runtime input**. The original attachments remain necessary for historical source provenance; the named published theorems remain mathematical inputs with the scope recorded in the paper and check events. In particular, the external-height scalar script does not independently recertify the published height, and no script replays the admitted zero-location theorem's formal development.

Historical audit notes, source manifests, elapsed times and receipts can record the original execution paths or source hashes. Those are provenance data, not executable path requirements. `certificates/root_weil_replay.json` is a historical replay receipt; the arithmetic generator above is the returned executable for repeating its underlying computation. The final manifest and frozen audit files should be retained unchanged beside any separate replay copy.

This index documents how to repeat finite algebra, interval computations, input-hash validation and the paper build. It makes no claim of formal verification of the whole paper or a proof of the unresolved all-zero simplicity estimate.
