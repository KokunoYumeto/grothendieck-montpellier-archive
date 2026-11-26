# Programs and exact computational certificates

This inventory covers the eleven Python source files currently in `workbench/programs`. The programs are original implementations accompanying the paper. Their outputs certify the displayed finite computations; the mathematical maps from those computations to arithmetic or geometric conclusions are proved and sourced in the paper and the check records.

## Environment and invocation

The recorded environment is Python **3.12.14**, SymPy **1.14.0**, and NumPy **2.3.5**. Seven programs use only the Python standard library. The three programs using SymPy are `check_cm_examples.py`, `check_cm_low_class_two.py`, and `verify_single_line.py`; `resonant_cut_probe.py` uses NumPy. Run Python without `-O`, because exact identities and expected values are checked by `assert` statements.

All commands below are written for the directory containing `workbench`; in this workspace that directory is `/workspace/scratch/2b04190c19aa`. The existing `checks` and `certificates` subdirectories must be present. The listed commands with `>` replace the named generated JSON file. Programs that write certificates themselves identify those paths below. No program requires network access.

The JSON files under `checks` are research records; those under `certificates` are the selected computational certificates packaged with the paper. Python cache files are not executable deliverables and are not inputs.

## Arithmetic data

### Bernoulli numerator factorizations and reflection exceptions

```bash
python3 workbench/programs/bernoulli_reflection.py > workbench/checks/bernoulli_reflection_certificate.json
```

**Dependencies:** standard library (`fractions`, `math`, `pathlib`, `json`). Inputs are `checks/bernoulli_reflection_factors.json` and `checks/bernoulli_reflection_lucas.json`.

The program recomputes every Bernoulli number through index 62 from its rational recurrence, compares the reduced numerator and denominator with the supplied factorization, and proves every listed factor prime using recursive Lucas certificates with the complete factorization of `q-1`. It checks all thirty even indices from 4 through 62 and extracts the prime factors at least `2^31`. The output gives fifteen exceptional primes attached to fourteen weights. The weights with no such exception are `1,...,15,21`.

This verifies the integer data used by reflection. It does not perform a class-group or Vandiver calculation at any of the fifteen large exceptional primes. The Herbrand, reflection, norm-control and published finite-range Vandiver inputs remain the separately stated mathematical inputs.

### The prime 37, its characters and its finite-precision root

```bash
python3 workbench/programs/p37_character.py > workbench/checks/p37_character.json
```

**Dependencies:** standard library only. No external data file is loaded.

The output recomputes the unique irregular index 32, verifies the finite Vandiver certificate with `q=149`, `z=16`, reduced exponents `r_c=c^4 mod37`, value `V=132` and fourth power 81, and checks the stated Iwasawa congruence. It then projects the finite Stickelberger element in the coordinate `kappa(gamma)=38`, giving the coefficients needed to locate the root modulo `37^3`.

The displayed coefficient precisions are **3, 2, 1 powers of 37**, respectively. The root and the transported eigenvalue are finite-precision values. The exact characteristic polynomial in the paper is defined using its actual 37-adic root; this program does not replace that root by a rational number. The main-conjecture and Kummer-duality identifications are separate cited steps.

### CM ray-field examples: first implementation

```bash
python3 workbench/programs/check_cm_examples.py > workbench/certificates/cm_examples.json
```

**Dependencies:** SymPy and the standard library. No external data file is loaded.

The program checks the cyclotomic discriminants, rational upper bounds for Minkowski's constant, residue orders, the norm-43 element in `Q(zeta_21)`, the quadratic period relation, and the ray-unit residues modulo 25 and 49. It also counts the points on the two displayed elliptic curves modulo 5 and 7. These are the exact arithmetic computations in the paper's elementary class-number and decomposition arguments. The ray-field equality and the deduction from those computations are supplied by the proof, not by an opaque class-group call.

### CM ray-field examples: independent implementation

```bash
python3 workbench/programs/cm_independent.py > workbench/checks/cm_independent_certificate.json
```

**Dependencies:** standard library only. No external data file is loaded.

This separately reconstructed implementation uses integral multiplication matrices and a Bareiss determinant, rather than SymPy resultants, for the norm-43 certificate. It emits the matrix and characteristic polynomial, the small prime-ideal candidates below the rational Minkowski bounds, the quadratic-period identity, and the same ray-unit tests. Its role and the accompanying proof are documented in the CM independent check records.

## Free Lie and derivation computations

### Pollack relation: sparse free-associative calculation

```bash
python3 workbench/programs/check_pollack_relation.py > workbench/certificates/pollack_relation.json
```

**Dependencies:** standard library only. No external data file is loaded.

The code constructs the derivations on the free associative algebra `Z<a,b>`, checks that they preserve `[a,b]`, and verifies both derivation values of

`[epsilon_4,epsilon_10] - 3[epsilon_6,epsilon_8] = 0`.

It also checks that the individual brackets are nonzero and prints their support sizes and a nonzero coefficient. This is an exact integral coefficient calculation. The passage to the arithmetic geometric action is proved separately in the paper.

### Pollack relation: independent coefficient calculation

```bash
python3 workbench/programs/pollack_independent.py > workbench/checks/pollack_independent_certificate.json
```

**Dependencies:** standard library only. No external data file is loaded.

This reconstructs the coefficient vectors on `[A_i,A_(13-i)]` by binomial sums. It checks the derivation value at `a`; the saved proof derives the value at `b` from preservation of `[a,b]` and the centralizer calculation in the free associative algebra. The output explicitly records that proof obligation rather than presenting an uncomputed second table.

### The low CM class-two bracket

```bash
python3 workbench/programs/check_cm_low_class_two.py > workbench/certificates/cm_low_class_two.json
```

**Dependencies:** SymPy, standard library, and the adjacent `check_pollack_relation.py` module, which it loads by its file path.

The program constructs Lyndon bases and the exact boundary-preserving derivation spaces in bidegrees `(2,2)` and `(3,3)`. It verifies their dimensions 1 and 2, computes the bracket with the degree `(2,2)` generator, and produces a nonzero two-by-two minor proving injectivity on the two-dimensional source. It outputs the actual bases and minor. The arithmetic realization of the relevant nonzero moments is a separate theorem in the paper.

### Six degree-seven Johnson brackets

```bash
python3 workbench/programs/check_johnson_detector.py
```

**Dependencies:** standard library only. No stored vector or matrix is loaded. The six finite lists of source triples and the expected comparison matrix are explicit in the source.

The program reconstructs six iterated brackets of degree-one Johnson derivations using sparse words in ten letters. It checks the boundary condition, weight, five detector contractions, and vanishing of the displayed auxiliary detector. It writes `certificates/johnson_detector.json` and prints intermediate row summaries. The determinant is **-203784**. The published representation multiplicities and the exact geometric maps are separate inputs, audited in the geometric recognition record.

### Single-line invariant tensors and polynomial identities

```bash
python3 workbench/programs/verify_single_line.py
```

**Dependencies:** SymPy and the standard library. No previous certificate is loaded.

The program reconstructs the twelve invariant tangent tensors from decorated tensor definitions, cyclic Lie constraints and contraction maps. It then checks all thirty-six entries of the stated polynomial identity and computes the relevant determinant. It writes both `certificates/single_line_input.json` and `certificates/single_line_polynomial.json`.

The prescribed comparison data are the displayed matrix `N0`, contraction indices and scalar polynomial `d0`; the input tensors and the two polynomial maps are reconstructed. The output checks those exact algebraic maps. The interpretation of their domains, images and covering maps uses the independent geometric proof and its primary sources. See `checks/single_line_reconstruction.md`.

## Finite probes with explicitly limited scope

### Mixed companion resonances

The three saved runs are reproduced by:

```bash
python3 workbench/programs/resonant_cut_probe.py --degree 5 --bound 1 --prime 1000003 --seed 25112026 --output workbench/checks/resonant_cut_d3n5_b1.json
python3 workbench/programs/resonant_cut_probe.py --degree 5 --bound 2 --prime 1000003 --seed 25112026 --output workbench/checks/resonant_cut_d3n5_b2.json
python3 workbench/programs/resonant_cut_probe.py --degree 6 --bound 1 --prime 1000003 --seed 25112026 --output workbench/checks/resonant_cut_d3n6_b1.json
```

**Dependencies:** NumPy and the standard library. No external data file is loaded. The specified prime keeps all intermediate products in the program's signed 64-bit elimination arithmetic within range; larger arbitrary primes are not a documented supported setting.

The model has `gamma w_k=w_(k+1)`, `gamma t=t+[w_0,w_1]` and `gamma d=d+[w_0,t]`. The program computes the exact finite source normal forms and the actual zero-`W` boundary vectors, then evaluates the rational coefficient maps at reproducible finite-field sample points on the total-product divisor.

| Degree | Index bound | Columns | Evaluated rank | Nullity |
|---:|---:|---:|---:|---:|
| 5 | 1 | 131 | 129 | 2 |
| 5 | 2 | 745 | 743 | 2 |
| 6 | 1 | 440 | 438 | 2 |

Each JSON file records the points, pivot columns, modular nullspace and source boundaries. The rank is exact for that finite evaluation matrix. Together with the two exact boundary identities, it finds no extra kernel in the stated finite source subspace. It does not prove saturation for all coefficient bounds or the bounded completed modules. The general proof is separate; see `checks/k_all_degree_companion_saturation.md`.

### CM Euler-space shear probes

Complete small runs:

```bash
python3 workbench/programs/check_cm_euler_J_finite.py --p 5 --level 1 --max-seconds 45 --output workbench/certificates/cm_euler_J_p5_n1.json
python3 workbench/programs/check_cm_euler_J_finite.py --p 7 --level 1 --max-seconds 45 --output workbench/certificates/cm_euler_J_p7_n1.json
python3 workbench/programs/check_cm_euler_J_finite.py --p 5 --level 1 --field minus19 --max-seconds 45 --output workbench/certificates/cm_euler_J_Kminus19_p5_n1.json
```

Budgeted larger run:

```bash
python3 workbench/programs/check_cm_euler_J_finite.py --p 5 --level 2 --max-seconds 40 --output workbench/certificates/cm_euler_J_p5_n2.json
```

**Dependencies:** standard library only. No external data file is loaded. `--field auto` is the default and selects `Q(i)` for `p=5` or `Q(sqrt(-3))` for `p=7`; `--field minus19` at `p=5` selects `Q(sqrt(-19))`. Other primes are not implemented.

The source is the **whole finite** `O_K^*`-invariant, zero-mass Euler-constraint space over `F_p` on `(Z/p^n)^2`. It is not assumed to equal the reduction of the actual arithmetic image. The target is compressed using antisymmetry and simultaneous unit coinvariants, whose invertible orders preserve the rank of the image under examination. The exact three shears are then evaluated on every processed exterior column.

| Field, prime, level | Euler-source dimension | Exterior dimension | Completed? | Recorded result |
|---|---:|---:|---|---|
| `Q(i)`, 5, 1 | 5 | 10 | Yes | rank 10, kernel 0 |
| `Q(sqrt(-3))`, 7, 1 | 7 | 21 | Yes | rank 21, kernel 0 |
| `Q(sqrt(-19))`, 5, 1 | 9 | 36 | Yes | rank 30, kernel 6 |
| `Q(i)`, 5, 2 | 103 | 5253 | **No** | 3744 columns processed, rank 3704 on those columns |

The last saved run has `complete=false`, `J_rank=null`, `J_kernel_dimension=null`, and `J_rank_lower_bound=3704`. It proves a full finite-space rank lower bound of 3704 and a kernel lower bound of `3744-3704=40`; it does not determine the full rank or kernel dimension. The number of processed columns and elapsed time vary by machine. The internal budget is checked between elimination columns, so it is not a hard wall-clock bound for preprocessing or a single long column.

The program records its SHA256 in the JSON. The first two level-one files were made before the later time-budget metadata was added and therefore have an older program hash and omit the `complete` field; both record full rank computations. The current invocation writes the newer metadata as well. An earlier unbounded level-two attempt was stopped without a returned result and contributes no certificate.

The file `certificates/cm_euler_axis_witnesses.json` contains two additional direct finite point-space witnesses, not the output of a separately packaged program. Their explicit supports and direct shear cancellations are documented in `checks/cm_actual_measure_image.md`. They are finite-characteristic, axis-supported witnesses. No statement about coherent inverse-limit lifts or membership in the actual arithmetic measure image follows from them.

## Reading the results

Successful exact checks terminate with exit code zero and their stated pass fields; an assertion failure terminates nonzero. Certificate data are not substitutes for the paper's source maps, primary arithmetic inputs or completed-module arguments. In particular:

- Finite 37-adic precision is displayed as precision, not an exact rational eigenvalue.
- Finite sampled rank tests retain their source bounds and finite-field scope.
- A budgeted partial elimination reports lower bounds and never a completed full rank.
- The finite CM Euler space is an enlarged constraint space; its rank does not decide the inverse-limit arithmetic shear kernel.
- The programs are exact computational checks, not a Lean-kernel verification of the paper or of the external K-theory archive.
