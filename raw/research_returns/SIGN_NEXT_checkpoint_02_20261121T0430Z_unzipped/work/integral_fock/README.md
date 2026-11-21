# Integral Fock / actual exterior / theta-kernel contribution

Run: SIGN_NEXT, 21 November 2026. Author: `/root/integral_fock`, GPT-6 Astra Pro; effort not exposed. The parent agent owns the main paper, ledger, final package, and checkpoint persistence. No Library operation was performed by this child.

## What is proved

`contribution.tex` supplies IF-01–IF-07 and inputs the three further proof files. All are intended to be included from the root of SIGN_NEXT.

| Finding | Exact result |
|---|---|
| IF-01 | An integral, graded, isometric multiaffine Fock model of the actual symplectic exterior lattice. Row-transvection coefficient extraction is exactly the divided power; the coefficient normalization is proved. |
| IF-02 | The divided-root order is saturated in its rational image in the actual exterior endomorphism ring for every rank. Its rank is the sum of `(v+1)^2` for `0<=v<=n`. Its additive index in the whole endomorphism ring is infinite for `n>=1`. |
| IF-03 | Exact HNF/Smith certificates for ordinary/divided orders, with/without degree projectors, in the actual exterior lattice for `n=1,2,3,4`. These are different from the predecessor's specified string-lattice indices. |
| IF-04 | Every specified polynomial Weyl lattice is an explicit cyclic lattice in a tensor of exterior columns; the normalized Fock form is exactly the exterior form. The dual Weyl lattice is the dual of this lattice, not another copy of it. A fixed simple root has an integral particle-hole realization by an actual Lefschetz pair. |
| IF-05 | An explicitly auxiliary check on the step-10 `aPlus` factors, including all root indices and raw numerical divisibility contributions. It is not presented as the main column coefficient or as a full global period computation. |
| IF-06 | The full noncompact oscillator module is not a finite exterior Lefschetz module. This does not exclude finite compact pieces or finite theta jets. |
| IF-07 | A lift count alone cannot specify exact nonzero period valuations when the input can be scaled. With data fixed, the local root periods are exactly 2 or 1. No global period value is inferred. |
| IF-08 | The actual source `jetMap` and `KM.Gxz/applyAt0` kernels are explicitly transported to exterior-tensor coefficient matrices. The proof establishes lattice primitivity, the normalization constant, the transpose convention, determinant insertions, global class/stabilizer sums, and local frames. Every index of the same specified map is transported exactly. |
| IF-09 | Exact source `numEx` column weights, the `numBig` modification, actual kernel partitions, and determinant insertions `(91,2)` for the two lifts. The source's `ThE` kernel family gives a fully fixed primitive chain and period 1. It cannot be two positive ordinary or divided powers of one fixed Lefschetz operator under primitive or isometric integral embeddings. Neither numerical example is asserted to be a fully instantiated global automorphic chain; the `numBig` host-size obstruction is explicit. |
| IF-10 | An algebraic-correspondence realization of every specified algebraic coefficient matrix using powers of a CM elliptic curve. It retains the denominator-2 projector, the `-2i` dual-line factor, determinant characters, CM-character untwists and coefficient-field extension. It proves geometric coefficient transport, not a new automorphic motive or L-function identification. |
| IF-11 | An inhabited genuine `ColIn.Ok + JetsIn` two-step theta family, with exact actual weights and required jet degrees155/635, determinant insertions10/20, and second-root invariants. Source theorems establish the finite algebraic coefficient field with the same ordinary-derivative normalization. These particular parameters still fail full `SizeData₂`; no nonzero full global period is asserted. |

The full proofs are in the three TeX files. The computer output supports the finite arithmetic checks; it is not used in place of the all-rank proofs.

## Disposition of predecessor Q6g, U-04, U-05

The predecessor's coefficient-model gate has been removed. The finite theta jet is now a specified integral exterior-tensor operator, including all source normalizations and denominators. For a supplied algebraic theta-chain datum, its global finite matrix is the explicit class sum in IF-08k; its Smith invariants and terminal functional transport exactly. IF-10 also supplies a geometric correspondence realization after the stated CM-character normalization.

Several stronger readings are false or distinct. The generated Lefschetz order does not have finite index in the whole endomorphism lattice. Ordinary and divided orders have different indices. A Weyl lattice and its normalized dual have different root-map indices. The fixed `ThE` chain has primitive composite image, while two positive divided powers of one fixed `L` have composite divisible by a nonunit binomial coefficient. The full oscillator has a separate nilpotence obstruction. These refutations do not purport to prove nonexistence of every possible realization of one fixed global automorphic theta chain.

Exact values of a particular global period require that particular global map and vector. The formulas here transport them without change; they do not replace them by lift count or by an order saturation index. The actual `numBig` arithmetic theorem is only a numerical-facts witness and has host primes incompatible with the full global host axiom. A separate child traced the genuine finite-jet constructor used in IF-11 and proved the precise host/size obstructions in SF-Q6-01/02; the full global arithmetic specialization is a separate task tracked in the parent ledger. The fixed exponential family also has a positive common-root realization: its degree-zero arrows commute with one common Lefschetz action on primitive exterior sublattices, while they cannot themselves be positive powers of its raising operator.

## Reproduction

Executed environment: Python 3.12.14, SymPy 1.14.0. Run from any working directory:

```sh
python /workspace/scratch/3c0a202771c9/SIGN_NEXT/work/integral_fock/exterior_order_indices.py --n 1 2 3 4
python /workspace/scratch/3c0a202771c9/SIGN_NEXT/work/integral_fock/verify_exterior_orders.py
python /workspace/scratch/3c0a202771c9/SIGN_NEXT/work/integral_fock/step10_fock_test.py
python /workspace/scratch/3c0a202771c9/SIGN_NEXT/work/integral_fock/kernel_model_check.py
python /workspace/scratch/3c0a202771c9/SIGN_NEXT/work/integral_fock/cm_model_check.py
python /workspace/scratch/3c0a202771c9/SIGN_NEXT/work/integral_fock/inhabited_theta_weights.py
```

The first script uses right-word HNF closure, stopping only on equality of the full HNF lattice. The second checks signed exterior generators and independent local determinantal valuations at 2,3,5; it does **not** perform a second word closure. The parent supplied a separate left-word closure implementation for all sixteen orders in `work/root/verify_left_closure.py`; its result is `work/root/left_closure_verification.json`. Both algorithms use SymPy's HNF infrastructure.

The large actual highest-weight modules were specified by exact partitions and functorial matrices; their astronomical full matrices were not expanded. `kernel_model_check.py` expands four small complete models to check every normalization and executes the actual large-weight/determinant/jet arithmetic. `cm_model_check.py` checks the prime-2 eigenline normalization, primitive unit minors, and algebraic matrix-unit realization on nine actual cohomological exterior models of ranks at most three.

No new Lean compilation or formal kernel check was run. Source results are cited as supplied theorems; the source declarations and normalization interfaces were read and their use recorded. `cited_sources/` contains the exact fifty-four small Lean files cited here, with original paths; it is not a standalone Lean project with all imports. `source_locators.tsv` and `cited_sources_manifest.json` supply file hashes. The full extraction manifests remain alongside the computations.

## Check records

`check_events.tsv` records the author's full readings, actual executed computations, and cited-source checks. The independent IF-02/04/08/09/10/11 reports are in `work/critical_lefschetz/`; the parent also reread IF-01–IF-07 and supplied the independent left-closure computation. The parent merges these records into the package-wide `CHECK_EVENTS.tsv`.

No proof is labelled formally verified merely because it agrees with a Lean definition. The one initial failure in `kernel_model_check.py` was a SymPy domain coercion (integral values held in a QQ-domain matrix); converting the matrix to exact integers resolved it, and the full computation then passed. The proof and certificate scopes are distinguished in the event log.

## Grothendieck and preceding runs

Cote 16 scan 014, paragraph 7, is the actual symplectic exterior operator ring used in IF-01–IF-03. Scans 015–016 contain the matrix-unit/inverse-string normalization discussed in HODGE_SIGN SL-04 and SL-08; it is not substituted for ordinary contraction. Scan 017 makes the degree-projector data essential, and scan 018 names the Lefschetz correspondence ring. IF-10 constructs explicit geometric coefficient operators in a correspondence category; it does not assert that they all arise from powers of one Lefschetz element.

THETA3's Q6, as reported in its supplied intake, distinguishes a Fock determinant norm from the sign-only trace argument. The constants `c_lambda`, `2^d`, and `2i` here make that normalization distinction explicit. HECKE_DIV's supplied intake distinguishes rational projectors, integral denominators, and uniform division. Our matrices live over `Spec Z` and their base changes, but their integral cokernels are additional information not recorded by a rational character or by K-theory alone.

HODGE_SIGN SG-08–SG-11 and the cited sign-only theorem are not reproved or modified by this contribution. No new standard-conjecture, cycle-saturation, purity, or automorphic L-function claim is inferred from these coefficient models.
