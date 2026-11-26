# Original verification programs

These programs accompany the finite examples and algebraic checks in the paper. They use exact arithmetic and assertions. They do not formally verify the general theorems. A nonzero exit status or an assertion failure is a failed computation.

Use Python 3.10 or later. **FixedFieldReplay** and **FixedInvariantsReplay** also use SymPy, checked here with version **1.14.0**. The other programs use the Python standard library. Imports between programs resolve from their shared `programs/` directory.

## Names, commands, and certificates

Run the following commands from the workbench directory. Except where a command explicitly writes a file, the program prints its JSON certificate to standard output. WalshTransferChecks prints one exact case record per line followed by its success message; its saved JSON certificate collects those records and their scope.

| Name cited in the paper | Exact command | Saved certificate |
|---|---|---|
| CoreChecks | `python3 programs/core_checks.py --output certificates/core_results.json` | `certificates/core_results.json` |
| SparsePresentationChecks | `python3 programs/sparse_presentation_checks.py` | `certificates/sparse_presentation_results.json` |
| StructuredVerify | `python3 programs/structured_verify.py` | `certificates/structured_verification.json` |
| StructuredAlgorithms | `python3 programs/structured_algorithms.py` | `certificates/structured_algorithms.json` |
| FixedFieldReplay | `python3 programs/fixed_field_replay.py` | `certificates/fixed_field_results.json` |
| FixedInvariantsReplay | `python3 programs/fixed_invariants_replay.py` | `certificates/fixed_invariants_results.json` |
| DistributedPaddingChecks | `python3 programs/distributed_padding_checks.py` | `certificates/distributed_padding.json` |
| SparseLineGCDChecks | `python3 programs/sparse_line_gcd_checks.py` | `certificates/sparse_line_gcd_results.json` |
| SparseDigitDeflationChecks | `python3 programs/sparse_digit_deflation_checks.py` | `certificates/sparse_digit_deflation_results.json` |
| SaturationCIChecks | `python3 programs/saturation_ci_checks.py` | `certificates/saturation_ci_results.json` |
| SlicedColonChecks | `python3 programs/sliced_colon_checks.py` | `certificates/sliced_colon_results.json` (also written by the program) |
| WalshTransferChecks | `python3 programs/walsh_transfer_checks.py --verify` | `certificates/walsh_transfer_results.json` (structured record of the printed cases) |
| PrimeFieldPreprocessingChecks | `python3 programs/prime_field_preprocessing_checks.py` | `certificates/constant_field_preprocessing_check_results.json`, `certificates/constant_field_strengthened_check_results.json`, `certificates/linearized_block_check_results.json`, `certificates/affine_relation_check_results.json`, `certificates/zero_sum_check_results.json` (written by the programs) |
| CartierSupportChecks | `python3 programs/cartier_obstruction_check.py` | `certificates/cartier_obstruction_check_results.json` (also written by the program) |

To compare a stdout-only replay, redirect it to a temporary JSON file and compare the parsed JSON objects, since whitespace and key ordering are immaterial. Do not replace a saved certificate before inspecting any difference. The SymPy factorization routine may emit a modular-integer ordering deprecation warning on stderr; the polynomial computations remain exact.

## What the certificates establish

- **CoreChecks** checks Boolean coefficient identities, stabilization coefficients, explicit quartic point counts, and the complete positive-unit-clause example. The characteristic-three quartic counts are 13, 11, and 15; the unit-clause hypersurface has 9,953 projective points.
- **SparsePresentationChecks** checks bounded-equation counting, support projection, complete-intersection coefficient identities, and small examples of the presentation constructions. The ternary linear-constraint example has 10,065 projective points.
- **StructuredVerify** exhaustively checks the stated small OR-graph fields, tests twelve hidden-quadric recovery cases, verifies the squared-row-rank change from 1 to 4, and computes the short multipliers' exact valuations. Its largest valuation parameter is 300; that computation uses the explicit construction, not exhaustive enumeration of its Boolean cube.
- **StructuredAlgorithms** checks 120 grouped-gate examples, 60 rational moment windows, 72 reversible register programs and 2,304 direct word evaluations, along with trace/cap indicators and arrangement counts. The arrangement coefficient lists are `[-12,14,-6,1]` over F3 and `[-37,30,-9,1]` over F4; both count three ground-field points, and the latter counts 2,235 over the quadratic extension.
- **FixedFieldReplay** factors six unit-normalized examples. At p=2 the parameters are N=161 and K=L=33; at p=3 they are N=253 and K=L=55. The common-root degrees at S=0,1,2 are respectively 0,K,2K. It also checks the binary repeated-root identity and enumerates the two-variable cubic's 56, 324, and 3,500 points over F2, F3, and F5.
- **FixedInvariantsReplay** enumerates the two F4 curves with 5 and 7 points and checks the Adams-to-gamma generating-series calculation for v=1 through 9. At v=3 the gamma coefficients are `[1,-3,2]`, with filtration gcds `[1,1,2]`.
- **DistributedPaddingChecks** checks the near-minimal support construction and its coefficient identity, including its characteristic-two control cases. Its fixed random seed selects finite test instances.
- **SparseLineGCDChecks** checks exact recovery of a bounded-degree cofactor on affine lines, with large binary exponents on other rows and both zero and nonzero Frobenius scalars.
- **SparseDigitDeflationChecks** checks the rank-one Frobenius-digit factorization and scalar preservation on its finite test range. It does not assert that every sparse factorization has rank one.
- **SaturationCIChecks** independently forms the bounded-degree colon coefficient system for six examples in characteristics 2, 3, and 5, with nonreduced intermediate complete intersection `(w²,E)`. The recovered annihilator is the line generated by w.
- **SlicedColonChecks** evaluates high-degree rows in the full nonreduced fibre algebras. In the six cubic examples, two fibres reduce the candidate kernel dimensions from 2 to 1, whereas replacing the algebra by its radical leaves all four linear coefficients unconstrained. Three degree-profile examples distinguish regular combinations from every nonregular row pair. Three further quartic-surface examples use excess 2, twelve-dimensional fibre algebras, and a six-point Newton grid. Their successive kernel dimensions are `10,7,6,3,2,1`, ending at the line generated by w². The input exponents have 64, 93, and 113 bits. At p=3,5,7 the direct surface counts are 16,0,64 and the coherent scalars are 0,4,0.

- **WalshTransferChecks** implements the separately reconstructed triangular-transfer Walsh multiplier. It exhaustively checks the six local truth tables, checks integer residue-transfer populations for valuation parameters 1,2,3,4,5,10,20, and enumerates the full global Walsh polynomial for parameters 1 and 2. The proof for all parameters is separate from these finite checks.

Some entries in the certificates, including genus, p-rank, and cohomological dimensions, are evaluations of formulas proved in the paper. Their provenance is distinguished from direct point enumeration, polynomial factorization, and matrix rank calculations in the contribution records. None of the programs computes arbitrary motives, arbitrary curve cohomology, or the general asymptotic success probability.


**PrimeFieldPreprocessingChecks** runs five exact sparse-arithmetic programs. They cover 52 original-template recognition cases, three growing-dimensional Fermat instances, 32 strengthened cases including absent multipliers and the extremal single-carry boundary, and eight general linearized systems with up to nine unknown coefficients. Characteristics 2,3,5,7 and degrees with up to 211 binary digits occur. The general-system tests designate the Frobenius scale while recovering the coefficient vector; the exhaustive scale-enumeration argument is proved separately. The scripts write their full certificates and print shorter summaries.

**CartierSupportChecks** directly expands the finite iterates for r=1,2,3 in characteristic seven, checks supports 28^r, tests every nonzero prime-field linear combination of the three displayed rows, and verifies the Cartier eigenvalue6. Direct projective enumeration gives nine points on the cubic, hence scalar6. These finite cases support the separate all-r proof and do not prove scalar hardness.


The same PrimeFieldPreprocessingChecks command also runs **affine_relation_checks.py**, adapted only for portable certificate output and truthful replay provenance from the separately authored statement-only test program. It checks5,902 exhaustive known-representation cases over F2/F3 (including644 zero-normalized-inner cases),250 seeded cases over F2/F3/F5, an explicit lower-block cancellation, Q=2^80 and3^60, and rejection of degree-one input. Its elapsed time, completion clock and current source hash change on replay; compare mathematical case counts and success, retaining the original independently produced certificate in its proof record.


The same command also runs **zero_sum_checks.py**. It checks genuine support growth for four prescribed representations (including316-bit degrees), every displayed row in five strict-family cases,1,642 active digit matrices, and equality in the exponent gap over F2/F3/F5/F7. It verifies minimum-degree outputs in the strict family. The growth examples concern the displayed representations; the minimum-degree recognizer can find smaller ones. The original failed test, which incorrectly required the recognizer to return a nonminimal displayed representation, is preserved in contributions/core with its correction record. Geometry, scheme-theoretic saturation and asymptotic iteration are proved separately.


## Portable formal-group programs

The four CamelCase names below are proposed citation names for the accompanying programs. Source filenames are unchanged. This documentation reports root's existing portable replay and does not claim another execution.


Use the workbench baseline of Python 3.10 or later, with Python assertions enabled. All four programs use only the Python standard library; none requires SymPy, a project import, a theorem prover, or a network service. Do not use Python's optimized mode for these assertion-based checks. The workbench's SymPy dependency belongs to other programs.

The following direct commands are run from `deliverable/workbench/`. The scripts accept no documented command-line options. In particular, an `--output` argument is not implemented for any of these four scripts.

| Proposed name cited in the paper | Direct command from the workbench root | Output behavior | Saved certificate |
|---|---|---|---|
| **AllHeightSeedChecks** | `python3 programs/all_height_seed_checks.py` | Writes the certificate at the script's workbench location and prints one JSON summary to standard output. | `certificates/all_height_seed_results.json` |
| **InvariantDerivativeChecks** | `python3 programs/invariant_derivative_checks.py` | Prints the complete JSON certificate to standard output; does not write a certificate file itself. | `certificates/invariant_derivative_results.json` |
| **SecondHeightExampleChecks** | `python3 programs/second_height_example_checks.py` | Prints the complete JSON certificate to standard output; does not write a certificate file itself. | `certificates/second_height_example_results.json` |
| **ReplicaCountChecks** | `python3 programs/replica_count_checks.py` | Prints six JSON summary lines and writes the complete JSON certificate at the script's workbench location. | `certificates/replica_count_results.json` |

The seed and replica scripts locate their output directories through `Path(__file__).resolve().parents[1]`; their destinations do not follow a redirected standard-output stream. A direct invocation therefore replaces the corresponding certificate at that script location. For the two stdout-only scripts, a replay certificate can instead be captured in a temporary file before comparison.

#### A copy-first replay recipe

The following optional recipe is intended for a future replay. It has not been executed for this documentation task. Start in `deliverable/workbench/`; it copies only the four scripts into a disposable workbench layout so that the two self-writing scripts also preserve the saved certificates:

```sh
formal_replay_dir="$(mktemp -d)"
mkdir -p "$formal_replay_dir/programs" "$formal_replay_dir/certificates"
cp programs/all_height_seed_checks.py \
   programs/invariant_derivative_checks.py \
   programs/second_height_example_checks.py \
   programs/replica_count_checks.py \
   "$formal_replay_dir/programs/"

python3 "$formal_replay_dir/programs/all_height_seed_checks.py"
python3 "$formal_replay_dir/programs/invariant_derivative_checks.py" \
  > "$formal_replay_dir/certificates/invariant_derivative_results.json"
python3 "$formal_replay_dir/programs/second_height_example_checks.py" \
  > "$formal_replay_dir/certificates/second_height_example_results.json"
python3 "$formal_replay_dir/programs/replica_count_checks.py"
```

Run each command with assertions enabled and inspect its exit status. An assertion failure or other nonzero exit is a failed computation. A pre-existing certificate or a partially printed replica summary does not establish that a new run completed. Compare the newly produced JSON using the narrowly defined comparison rule in the recorded-comparison subsection below before replacing any saved certificate.

### Scope of the four formal checks

### AllHeightSeedChecks

**Arithmetic and method.** The program constructs the displayed finite seed data with arbitrary-precision Python integers, computes factorial multinomial coefficients, and obtains selected diagonal coefficients by enumerating all multinomial count vectors. Its imports are `datetime`, `math`, `pathlib`, and `json`; the clock is used only for the two timestamp fields. It performs no floating-point arithmetic.

**Structural cases.** There are **11** parameter pairs:

| Prime | Heights checked | Corresponding values of `N = p**h - 1` |
|---|---|---|
| 2 | 2, 3, 4, 5, 6 | 3, 7, 15, 31, 63 |
| 3 | 2, 3, 4 | 8, 26, 80 |
| 5 | 2, 3 | 24, 124 |
| 7 | 2 | 48 |

For each pair, the source asserts the prescribed multiplicity-vector length `(2*h - 1)*(p - 1)`, the sums of the multiplicities and reduced weights, zero greedy residuals, exact weighted representations of every integer from 0 through `N-1`, and the two endpoint bit vectors. It also asserts that the constructed monomials all have degree `N`, that every exponent in the non-pure monomials lies in `{0,1,2}`, that the monomials are distinct, and that every variable occurs. Finally, it checks integrality of the factorial quotient

\[
B_h=\frac{N!}{\prod_i\nu_i!}
\]

and asserts `v_p(B_h) = h - 1` for these 11 inputs.

**Direct seed coefficients.** There are **39** coefficient cases: powers `0..6` for `(p,h)=(2,2)`, `0..14` for `(2,3)`, and `0..16` for `(3,2)`. Each coefficient is calculated by complete enumeration of the count vectors at that power. The program asserts that a nonmultiple of `N` has no matching diagonal count vector and coefficient zero. At a multiple `a*N`, it asserts that the sole matching count vector is `a*nu` and that the coefficient is the corresponding factorial quotient. The tested values of `a` are 0, 1, and 2.

**Stabilizer cases.** There are **10** comparisons: `t=1..6` for the binary height-two seed with `Q=6`, and `t=1..4` for the explicit one-variable height-one seed with `Q=4`. The stabilized monomials are checked for common degree and distinctness. At each tested `t`, direct count-vector enumeration asserts equality of the seed and stabilized diagonal coefficients at power `t-1`, including both `t=Q` endpoints.

**Scope control.** One additional computation deliberately removes a required padding hypothesis. It asserts that the two diagonal coefficients are 6 and 12. The saved object calls this a `scope_counterexamples` entry, but it is a counterexample to the inadmissible extension of the statement, not to the theorem under its hypotheses.

The expected summary is `status="passed"`, 11 structural cases, 39 seed-coefficient cases, 10 stabilizer cases, one scope control, and `count_vectors_examined=90813`. The last number sums the stored enumeration counts for the 39 seed cases and 10 stabilized cases. It is not a count of every internal operation or of the additional seed-reference enumerations used in the stabilizer comparisons. The successful certificate also has an empty `failures` list.

These are finite algebraic checks. The program does not prove the all-height construction, check smoothness for arbitrary parameters, establish a complexity reduction, or replace the separately stated universal arguments.

### InvariantDerivativeChecks

**Arithmetic and method.** The program uses exact `fractions.Fraction` arithmetic, integer factorials, a truncated Hazewinkel logarithm recursion, and recursive formal-series inversion. It then composes the inverse series with the strict integral coordinate

\[
T=U+U^2+2U^3+U^7.
\]

Its imports are `fractions`, `math`, and `json`. All calculations below take place at finite truncation; there is no numerical approximation of a formal logarithm or derivative.

| `(p,h)` | Truncation `N` | Hazewinkel parameters supplied in the source | Constant terms checked | Equality witnesses |
|---|---:|---|---:|---:|
| `(2,2)` | 16 | `v1=2, v2=3, v3=5, v4=7` | 153 | 5 |
| `(2,3)` | 16 | `v1=2, v2=2, v3=1, v4=3` | 153 | 5 |
| `(3,2)` | 27 | `v1=3, v2=2, v3=6` | 406 | 4 |

For every `0 <= m <= n <= N`, the program calculates the exact rational value

\[
n![T^n]e(T)^m
\]

for its changed exponential series `e`. It asserts either that the value is zero or that its `p`-adic valuation is at least

\[
\max\!\left\{0,\ E_h(n),\ \left\lceil
\left(\frac1{p-1}-\frac1{p^h-1}\right)n-(h-1)
\right\rceil\right\},
\qquad
E_h(n)=\sum_{\substack{j\ge1\\h\nmid j}}\left\lfloor\frac n{p^j}\right\rfloor.
\]

This gives **712** constant-term cases in total, including zero terms and the boundary indices. Zero is represented internally by a valuation return value of `None`; it is accepted by the lower-bound assertion. There are additionally **14** equality-witness checks at `n=p**j`, `m=p**(j % h)`. The recorded witness valuations, in increasing `j`, are `0,1,2,5,10`; `0,1,3,6,13`; and `0,1,3,10` for the three rows respectively.

The Fermat-cubic comparison computes `b25 = 24!/(8!)^3 = 9465511770` and explicitly asserts `v_5(b25)=1` and `(b25/5) mod 5 = 4`. The fields `Fermat_cubic_b5=0`, `standard_Honda_height_2_leading_coefficient=1`, and `height=2` are literal explanatory metadata in this script; the program does not independently derive those fields or identify a formal-group isomorphism.

The expected JSON has `outcome="passed"`, three `formal_group_cases`, and the stated Fermat-cubic comparison. It demonstrates these finite constant-term inequalities and equality witnesses. The general divisibility statement for all series, every coefficient, arbitrary parameters, and the optimality claims require the separate proof.

### SecondHeightExampleChecks

**Arithmetic and method.** This program uses integer local-marginal enumeration with `collections.Counter`, `itertools.product`, and `math.comb`, and serializes with `json`. For each clause relation, it enumerates ordered `k`-tuples of satisfying local assignments, groups them by their one-count marginals, and combines the clause counts with the variable binomial weights. It inserts a tautological unary relation for an unused variable. It does not import a project module.

It treats **two fixed CNF presentations on three variables**, `phi0` and `phi1`, and computes the coefficient for `k=1` and `k=3` for each presentation: four coefficient evaluations. The source explicitly asserts that the complete lists of satisfying assignments coincide and that the two `k=3` coefficients are 20 and 1622. The common satisfying assignments are `(0,1,1)` and `(1,1,1)`.

| Presentation | `S` | `A1` (`k=1`) | `A2` (`k=3`, at `p=2`) | Recorded `(A2-A1**2)//2` | Nonzero `k=3` marginal contributions |
|---|---:|---:|---:|---:|---:|
| `phi0` | 2 | 2 | 20 | 8 | 4 |
| `phi1` | 2 | 2 | 1622 | 809 | 6 |

Thus the saved coefficients have different residues modulo 4, despite identical satisfying assignments. The complete certificate lists every nonzero marginal contribution. `S`, `A1`, and the displayed quotient are calculated and recorded; the code's explicit assertions are the assignment-list equality and the two `A2` values. In particular, the code does not separately enumerate the cyclic action or prove that the quotient counts its nonfixed orbits. The interpretation and the link to a height invariant belong to the manuscript arguments.

The JSON has no separate `passed` or `outcome` field. Successful termination together with the expected values is the relevant program outcome.

### ReplicaCountChecks

**Arithmetic and method.** This program uses exact integer dynamic programming for clause marginals, cached local tables, and integer binomial weights. Its imports are `collections`, `functools`, `itertools`, `math`, `pathlib`, `json`, and `random`. The pseudorandom generator selects a finite input corpus; it is not used for approximate arithmetic. Its explicit seed is **630925**, and the same generator is used in the source's fixed batch order.

For each formula the program enumerates its satisfying assignments to obtain `S`, asserts that the one-replica coefficient equals `S`, computes the `(p+1)`-replica coefficient `A`, and asserts `(A - S*S) % p == 0`. It then records `A mod p**2` and selected clauses witnessing the observed residues. Unused variables receive tautological unary relations.

| Prime `p` | Variables `n` | Formula inputs | Selection | Number of `S` values with more than one recorded residue modulo `p²` | Inputs with `S ≡ 0 (mod p)` and `A ≢ 0 (mod p²)` |
|---|---:|---:|---|---:|---:|
| 2 | 2 | 256 | All subsets of the eight unary/binary clauses in the source's universe | 1 | 0 |
| 2 | 3 | 300 | Seeded samples | 5 | 3 |
| 2 | 4 | 200 | Seeded samples | 8 | 13 |
| 3 | 3 | 200 | Seeded samples | 6 | 13 |
| 3 | 4 | 100 | Seeded samples | 10 | 15 |
| 5 | 3 | 100 | Seeded samples | 4 | 3 |

There are **1,156 formula inputs**, with two explicit assertions per input. Outside the exhaustive two-variable batch, each sampled formula contains between one and twelve distinct clauses chosen from the available clauses of width at most three. The counts in the final two columns are the values in the existing certificate, not assertions of corpus coverage beyond the selected samples. The complete output stores at most five examples from each batch under `zero_S_nonzero_second`; its `number_zero_S_nonzero_second` records the full number found. Despite that field's abbreviated name, its condition is divisibility of `S` by `p`, not literal equality `S=0`.

The six stdout lines are summaries rather than the saved certificate. The saved JSON contains `scope` and `results`, without a separate success-status field. The source establishes these finite coefficient checks and observations. It does not by itself prove the cyclic-orbit formula, a general height criterion, a hardness theorem, or an infinite-height classification.

### Recorded formal replay and exact comparison rule

The existing `workbench/certificates/formal_replay_manifest.json`, completed at `2026-11-25T04:03:02.254384+00:00`, describes a **single portable replay of the same original finite cases**. It records `parsed_mathematics_equal=true` for all four pairs below. This documentation reports that existing record; it does not create or claim a further replay.

| Portable program output | Original certificate named by the manifest | Fields excluded from the recorded parsed comparison |
|---|---|---|
| `workbench/certificates/invariant_derivative_results.json` | `contributions/formal_derivative_blind/FRESH_CHECKS.json` | None |
| `workbench/certificates/second_height_example_results.json` | `contributions/higher_counting_blind/finite_check_output.json` | None |
| `workbench/certificates/replica_count_results.json` | `contributions/formal_core/replica_count_probe_results.json` | None |
| `workbench/certificates/all_height_seed_results.json` | `contributions/all_height_seed_blind/EXACT_CHECK_RESULTS.json` | Only the top-level `started_utc` and `completed_utc` fields |

**Comparison rule:** parse both complete JSON objects; for the seed pair only, remove those two top-level timestamp fields from both objects; compare every remaining field and value. Do not ignore elapsed times, source hashes, status fields, case counts, parameter values, coefficients, witnesses, scope strings, or any other metadata. Do not drop or reorder list entries, sort witnesses, or coerce strings into numbers. JSON whitespace and object-key ordering are formatting and are not mathematical differences under parsed-object comparison.

The manifest records identical byte hashes for the derivative, two-presentation, and replica pairs. It records different byte hashes for the seed pair, whose parsed comparison excludes the two timestamps. The hashes below preserve the exact original and portable bytes rather than normalizing the saved files. A future replay should satisfy the same rule. A discrepancy in any nonexcluded field must be inspected; it is not covered by an additional implicit exception.

This guarantee concerns the stored finite outputs and this recorded replay. It gives no universal proof, broader input coverage, or separate certification of future interpreter versions. In particular, the seeded replica corpus is part of the recorded output and must not be silently replaced by another sample.

