# Grothendieck's algebraic geometry: proof and literature workbench

This workbench records an audit of six bodies of proposed results connected to
Grothendieck's manuscripts. Five research papers are in `papers/`. Each paper
is an independent LaTeX project with a build command and a deposit sheet.
The proposed sixth paper is known from Milne's work and is preserved as an
editable comparison in `records/papers_5_6/known_gerbe_comparison/`, with the
decision in `records/papers_5_6/PAPER6_DISPOSITION.md`.

This is an active research record. A historical label “proved” is not a current
verification. The register separates source assertions, checks performed here,
literature status, and open gates. Read the release status and ledger before
using any mathematical claim.

## Records

- `REGISTER.tsv`: consolidated results, statements, proof locations and status.
- `CHECK_EVENTS.tsv`: what was checked, by whom, by which method, and with what
  outcome. Statement-only re-proofs are distinguished from proof reading.
- `records/`: detailed mathematical audits and literature search records.
- `programs/`: newly written computations and source-certificate runners.
- `papers/paper_XX/MANIFEST.sha256`: current standalone-project hashes; the enclosing immutable ZIP also has its complete manifest.

Only this project's work belongs in the repository. Published papers and source
editions are cited rather than copied. Paths beginning `source/` in audit records
refer to the user's input archive, not files redistributed in this workbench.

The repository destination for Papers 1–4 and 6 is
<https://github.com/KokunoYumeto/schemes-and-moduli-workbench>.
Paper 5 belongs to
<https://github.com/KokunoYumeto/algebraic-cycles-and-motives-workbench>.
The permanent records landing page is
<https://github.com/KokunoYumeto/mathematics-workbenches>.

This text and the new code and mathematics in this workbench are dedicated to
the public domain under CC0 1.0. No human verification is asserted.


## Rebuilding record tables and version manifests

From the parent deliverable directory, run `python workbench/programs/consolidate_records.py`, then `python workbench/programs/assemble_records.py`, then `python workbench/programs/write_version_manifests.py`. The assembly checks current PDF hashes against saved clean-build locators before writing each paper’s statement table. Permanent work numbers and tags remain for the owner to assign when filing; see FORMAT1_FILING.md. The manifest records a working version and does not assert that a remote deposit has occurred.

### General adjoint arithmetic

Run `python programs/check_general_adjoint_arithmetic.py`. Expected:JSON verdict `PASS`,43 assertions. This uses direct finite-field polynomial differentiation and integral exceptional Gram matrices. It checks the canonical derivative identity, saturation nonclosedness, the exceptional square identity and restriction degrees; it does not certify the geometric proof.

### Higher-conductor equality arithmetic

Run `python programs/check_higher_conductor_square.py`. Expected: `PASS`, 127864 arithmetic assertions. The program independently substitutes the Euler formula into the intersection pairing and checks exact rational boundary values. It does not certify the geometric normalization, fibration or positivity inputs.

### Odd strict reconstruction arithmetic

Run `python programs/check_odd_strict_reconstruction.py`. Expected: `PASS`,183 assertions. The checks use formal Chern roots, finite-field derivation matrices and exact Riemann–Roch/parity arithmetic. The complete independent geometric proof and primary-source comparison are separate records.

### Zheng preprint counterexample arithmetic

Run `python programs/check_zheng_v1_counterexample.py`. Expected: `PASS`,24 assertions; formal-series order of dx30, genus16, canonical coefficients(18,11), ample-difference coefficients(6,13), coherent Euler characteristic55. This independently uses the local equation z+t z^8=t^5, cyclic Euler weights and the intersection matrix. The correction concerns arXivv1Cor4.4 only; final journal wording is unknown. The full proof is in the corrections records.

### Conductor structure, descent, and the internal center

Commands in this subsection are run from the workbench directory. Run calculations in a writable working copy; the two structural/descent scripts below write their named JSON result files under `records/`. The archived comparison receipts preserve the original execution histories.

| Program name in the paper | Command | Expected result and scope |
|---|---|---|
| Conductor structure arithmetic verifier | `python programs/check_conductor_euler_structure.py` | `PASS`, 46,186 assertions; divisor intersections, degree-filtration Euler sums, local invariant algebra, and Chern identities. |
| Joint conductor polynomial verifier | `python programs/check_joint_conductor_polynomials.py` | `PASS`; exact rational coefficient identities, half-line coefficient sign certificates, and internal conductor-six numerator `[-800,100]`. |
| Conductor descent verifier | `python programs/check_conductor_descent_algebra.py` | `PASS`, 5,615 assertions; sparse differential kernels, truncated unit inverses, and quotient-degree identities. |
| Internal Cartier jet verifier | `python programs/check_internal_cartier_jets.py` | `PASS`, 128 quadratic units and 1,536 assertions; dual-number substitutions for local first jets. |
| Manuscript arithmetic verifier | `python programs/check_paper02_audit_arithmetic.py` | `PASS`, 12 rational identities checked by 14 coefficient witnesses, and the 10-prime conductor table reconstructed by enumerating genera. |

The local jet program proves only its stated finite algebraic checks. The proof for arbitrary formal units and the global Euler-extension argument are written in the paper. The arithmetic verifiers do not certify the geometric hypotheses.

The exact newcomer program can be rerun with `python records/paper02_100page_newcomer/arithmetic_verifier.py` (SymPy 1.14.0 in the recorded run); its twelve identities and table agree with the distinct coefficient method. The exact expert inline program, first saved after its original execution, is preserved honestly in `records/paper02_100page_expert_computation_addendum/exact_inline_sympy.py`; its nine zero residuals were reproduced by root. The respective receipts are `ROOT_PAPER02_100PAGE_ARITHMETIC.json` and `ROOT_PAPER02_EXPERT_POLYNOMIAL_RERUN.json`.

### Positive-excess arithmetic

From the workbench root run `python3 programs/check_positive_excess_bound.py`. Expected status: PASS; three sparse polynomial identities, four examples,696 exact rational recurrence cases and2436 steps. This verifies arithmetic only; the full geometry and exposure limits are in `records/ROOT_POSITIVE_EXCESS_COMPARISON.md`.

### Finite-cover filtration arithmetic

`python3 workbench/programs/check_positive_excess_filtration.py` (from the archive root) verifies two exact polynomial identities and240 explicit sums. Expected result: `PASS`; recorded outputs and byte-identical rerun are in `workbench/records/positive_excess_filtration_arithmetic/`. This checks arithmetic only.

Boundary arithmetic: `python3 programs/check_positive_excess_boundary.py` prints PASS with65 cusp,8064 polynomial,448 overlap,12800 degree and39 cyclic-order cases. These are arithmetic checks only; see the complete proof comparison and byte-identical rerun receipt.
