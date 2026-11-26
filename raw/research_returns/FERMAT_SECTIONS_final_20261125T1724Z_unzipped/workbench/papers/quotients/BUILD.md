# Building and checking the companion paper

This project is standalone. Its editable manuscript consists of `main.tex`,
the `.tex` chapters that it inputs, and `references.bib`. The chapters
include the complete transfer, arithmetic, local, group-theoretic, and
conditional arguments. No external source copy is needed to compile it.

Compile with a normal TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Reproducible arithmetic certificates

The readable program names used in the paper correspond to these files:

| Program | File |
| --- | --- |
| Quintic class-number certificate | `quintic_class_number_check.py` |
| Quintic residual-group certificate | `quintic_residual_group_check.py` |
| Quintic interval certificate | `check_quintic.py` |
| Quintic rational lower bound | `check_quintic_rational.py` |
| Septic principal-prime certificate | `septic_principal_prime_check.txt` |
| Septic class-number analytic certificate | `septic_class_number_check.py` |
| Septic auxiliary class-number certificate | `septic_auxiliary_class_number_check.py` |
| Septic central-value certificate | `check_septic.py` |
| Septic residual-field polynomial check | `septic_residual_field_check.py` |
| Exponent-eleven central-value certificate | `check_eleven.py` |
| Exponent-eleven rank-one derivative certificate | `eleven_rankone_certificate.py` |
| Exponent-eleven rank-one coefficient enumerator | `eleven_rankone_counts_source.txt` |
| Jacobi-sum coefficient enumerator | `jacobi_counts_source.txt` |
| Exponent-thirteen partial quotient checks | `check_thirteen_partial.py` |
| Exponent-thirteen central-value certificate | `check_thirteen.py` |
| Exponent-thirteen coefficient enumerator | `thirteen_counts_source.txt` |
| Exponent-seventeen arithmetic checks | `check_seventeen.py` |
| Nineteenth CM arithmetic checks | `nineteen_exact_check.txt` |
| Nineteenth central-derivative certificate | `nineteen_certificate.py` |
| Nineteenth canonical-model check | `nineteen_canonical_check.py` |
| Auxiliary level-twenty-seven Kummer certificate | `level27_kummer_certificate.py` |
| Exponent-thirty-one structural arithmetic checks | `check_thirtyone.py` |
| Exponent-thirty-seven structural arithmetic checks | `check_thirtyseven.py` |

The quintic interval certificate requires Python 3 and python-flint:

```sh
python check_quintic.py --limit 4096 --precision 192 --output quintic_certificate.json
```

Its JSON records the exact local factors and Dirichlet coefficients, the
positive theta enclosure determining the functional-equation sign, the
central value enclosure, and both infinite-tail bounds. The analytic
conductor and functional equation are named mathematical inputs in the
paper, not outputs of the numerical program.

An independent exact-rational quintic lower bound requires only Python's
standard library:

```sh
python check_quintic_rational.py
```

It certifies a leading term greater than 7/10 and an absolute remainder
less than 13/20, proving that the central value exceeds 1/20.

The exponent-eleven certificate requires Python 3, python-flint, and a C
compiler available as `cc`:

```sh
python check_eleven.py --limit 100000 --precision 96 --output eleven_certificate.json
```

The program compiles the original helper `jacobi_counts_source.txt` into a temporary
directory. It computes exact local factors from Jacobi sums and finite-field
counts, evaluates one rigorously enclosed contour integral, and bounds both
the vertical contour tail and the omitted Dirichlet terms. Its JSON retains
all local factors and nonzero coefficients used. The claimed central-value
interval is 1.78 < L(1) < 1.80. The conductor, functional equation, and
identification with the specified CM Jacobian are cited mathematical inputs.
No external mathematical source, database, or network access is needed by
any verification program.

The septic certificate requires Python 3, sympy, and python-flint:

```sh
python check_septic.py --limit 4096 --precision 112 --output septic_certificate.json
```

It proves 0.9763 < L(Jac(v^2+v=u^7),1) < 0.9765. Characteristic two
is handled by the Artin-Schreier trace in the exact finite-field count.
The same CM arithmetic theorem then gives finite rational group of
order seven and finite Tate-Shafarevich group.

## Scope of the mathematical proofs

The finite-derived, metabelian and maximal geometrically prosolvable
classification covers every odd exponent divisible by 3, 5, or any regular
prime greater than 5. The first remaining prime is 37. The regular-prime
proof combines proper cyclotomic torsors, the primary refinement of
McCallum's argument, a completed global unit and Saïdi's localization
theorem. Stoll's finite-descent criterion supplies the separate classical
Jacobian applications. Their quintic and exponent-eleven rank-zero and
finite-Sha inputs use Nekovář's published Hilbert-modular theorem after
certified nonvanishing. For every regular p>5, all n=p^r also have the full
geometric pro-p and stated derived/ordinary-central quotient classification.
No analogous statement for arbitrary p-multiples in the pro-p group is made.

The pro-3 chapter includes the explicit local reduction calculation,
cyclotomic Kummer restriction matrices, and source-surjectivity proof.
The one-place criterion retains its complete-cocycle ramification restriction
and integral unit-tangent hypothesis. The subsequent unrestricted chapter
proves Selmer cuspidality for the full group, every finite-derived quotient,
and every ordinary lower-central quotient at every exponent 3^r, 5·3^r, or 7·3^r, with r≥1. More
generally, it covers every quotient retaining abelianization with torsion-free
ordinary lower-central factors. It uses compact cancellation by the arithmetic
source, tangent-line cusp torsion, and central induction, without a rank or
Tate-Shafarevich hypothesis on the higher Jacobian. It explicitly
allows cusp parameters with infinite ramification support.
Two maps to the proper hyperelliptic quotient further show that every
pro-3 Selmer section at an odd exponent divisible by 3, 5, 7, or 11 is
locally cuspidal at 3. This local result already holds in every quotient
retaining geometric abelianization, but does not alone give global cuspidality.

The abstract-section chapter constructs sections of the actual full
geometric pro-3 group, at all exponents 3^r. One proof uses a free pair
exchanged by complex conjugation and infinite compact cohomology classes.
The other lifts prescribed boundary cocycles using cohomological dimension
one and gives zero compact cohomology class. Both constructions are
noncanonical and do not assert a continuous parametrization. All resulting
sections fail local geometry at 3 and are not Selmer counterexamples.

## Exponent-thirteen arithmetic and split-prime Selmer input

`python check_thirteen_partial.py` verifies exact small finite-field counts
for the genus-two cyclic quotient of the Klein quintic. Together with the
published rank-one input, these locate a rank-zero complementary Prym.
The companion proves rational Bloch–Kato vanishing and vanishing of the
Tate–Shafarevich Tate modules for almost all primes splitting completely in
K·Q(zeta_3), where K=Q(zeta_13)^{<3>}. The full proof is in
`thirteen_selmer.tex`: it uses the stated intermediate Euler-system machinery,
explicit CM inertia, and derived Selmer-complex base change. Together with
the split-prime descent criterion this includes exponent thirteen in the
finite-derived and prosolvable theorem. The rational-point input is explicitly
Wiles (1995), Theorem 0.5. Finiteness of the entire Tate–Shafarevich group is
not claimed; the pro-3 exponent range is unchanged.

## Exponent-thirteen analytic certificate

Run `python check_thirteen.py --limit 100000 --precision 144`. The program
uses `python-flint` and a C compiler, compiles its original helper
`thirteen_counts_source.txt` with `cc -x c` in a temporary directory, and
writes `thirteen_certificate.json`. It reconstructs exact Euler
coefficients and certifies `2.632 < L(P_13,1) < 2.636` using the universal
degree-eight Weil coefficient bound. The conductor, Hecke decomposition,
and functional equation are proved in `thirteen.tex`; the program does
not itself prove the split-prime Tate-module condition, which is established
in the separate mathematical argument `thirteen_selmer.tex`.

All theorem-like statements, including definitions and remarks, have
stable LaTeX labels. The complete split-prime descent argument is in
`split_primes.tex`; it requires no rank assumption after base change.

The current manuscript also contains the conditional two-prime mixed-exponent criterion. Its exact boundary range is r=1 or q≡2,4,5,7 mod9. Its compact integral3-Selmer localization hypothesis and additional higher-grade hypotheses remain explicit assumptions outside the unconditional 5·3^r and7·3^r families. The local metabelian point/cusp separation and the good-reduction quotient obstruction have complete proofs in the standalone source.

The mixed family 5·3^r is unconditional: the new arithmetic-source proof determines the quintic 3-torsion field of degree80 and discriminant3^76·5^94, and applies Odlyzko’s unconditional bounds to prove localization. It then verifies the compact and all graded gates without a rank or Sha computation for J15. The broader two-prime criterion remains conditional outside the verified families.

The exact residual-group certificate is self-contained Python:

```sh
python quintic_residual_group_check.py
```

It enumerates the semilinear similitudes over F81 and verifies the group presentation, inertia orders and reflex-norm images. Its output is quintic_residual_group_check.json. The arithmetic realization is proved separately in the manuscript.

## Quintic class-number certificate

`python quintic_class_number_check.py` reproduces the unconditional
Odlyzko explicit-formula certificate using python-flint/Arb. It writes
`quintic_class_number_check.json` beside the script. All acceptance
thresholds are exact rational numbers; the endpoint and infinite tail
are bounded explicitly in the paper and script.

## Septic residual-field polynomial check

`python septic_residual_field_check.py` uses SymPy exact arithmetic to
check the residual CM unit identities, the elliptic three-division
resultant and its recovering subresultant, and the integer root-discriminant
comparison. Its JSON is written beside the script. This checks the
explicit field specification; it does not compute its class group.

The auxiliary degree-48 septic class-number certificate is reproduced with `python septic_auxiliary_class_number_check.py`; remove or rename its prior JSON output before repeating. It proves class number one using exact rational acceptance bounds in the unconditional explicit formula.


## Unconditional septic three-class certificate

Run these commands from this directory, with PARI/GP and python-flint installed:

```sh
gp -q -f septic_principal_prime_check.txt
python septic_class_number_check.py septic_principal_norms.tsv --output septic_class_number_certificate.json
python septic_class_number_check.py septic_principal_norms.tsv --b 27/2 --precision 256 --output septic_class_number_comparison.json
```

The exact replay reconstructs and certifies the maximal order without loading a class-group object. It checks the defining field embeddings, all592 distinct prime ideals, residue degrees, and equality with the supplied principal ideals. The five line-aligned witness files are each smaller than4MB and are concatenated internally; their hashes are recorded in septic_principal_witnesses_manifest.json. The analytic program uses their resulting norm counts in the unconditional explicit formula. Together these certificates prove Cl(M)[3]=0 for the explicit degree56 field, and hence settle every7·3^r pro-3 family in the main theorem. No exact class-number claim forM or GRH assumption is used.

## Exponent-seventeen method obstruction

`python check_seventeen.py` prints the exact quotient-orbit, conductor-parameter,
and root-number checks retained in `seventeen_arithmetic_check.json`. The proof
in `seventeen_obstruction.tex` combines these with Gross–Rohrlich, McCallum,
Shu and Nekovář. Every simple factor has positive rational rank, and all three
central values vanish. This is an obstruction to the rank-zero target method;
it gives no new section classification or noncuspidal Selmer counterexample.


## Unconditional exponent-nineteen certificate

The chapters `nineteen_arithmetic.tex`, `nineteen_euler.tex`, and
`nineteen_certificate.tex` prove the rational threefold/sixfold decomposition,
all CM Euler factors and root-number conventions, and the certified simple
central zero. Together with McCallum–Tzermias's rational rank-one theorem and
Zhang's published analytic-rank-at-most-one theorem, they prove that the
rank-zero sixfold has finite Tate–Shafarevich group. This includes every odd
multiple of nineteen in the finite-derived and prosolvable classification.
It does not change the pro-3 exponent range.

Run these commands from this directory:

```sh
gp -q -f nineteen_exact_check.txt
python nineteen_canonical_check.py
python nineteen_certificate.py --precision 128 --output nineteen_certificate.json
```

The exact replay needs PARI/GP (verified with 2.17.4). It fixes the field
polynomial, cyclotomic embedding, and integral basis explicitly, so the saved
coordinate vectors do not depend on the integral basis selected by another
PARI version. It proves class number one by the Minkowski bound and three
explicit norm witnesses, then checks all 312 prime generators and their Euler
polynomials. It uses no `bnf` object, class-group computation, or GRH assumption.
The data are `nineteen_split_witnesses.txt`.

The canonical-model check needs Python 3 and SymPy. It verifies the invariant
differentials, canonical relation, and exact ranks. The plane quartic itself
is the published X15 of Kılıçer et al. (2018), credited in the manuscript.
The analytic certificate needs Python 3 and python-flint; it has no NumPy or
SciPy dependency. It reconstructs the integer coefficients, evaluates the
exact Gauss sum and enclosed Mellin integrals, and bounds both infinite tails.
Its complete output certifies 9.96 < L′(J,1) < 9.99. This packaging replay is a
targeted reproduction of the proved certificate, not a statement-only
independent reconstruction. The SHA-256 manifest is `nineteen_checks_manifest.json`.


## Compact Selmer localization at exponent eleven

The chapter `eleven_compact.tex` proves finite full Tate–Shafarevich group
and injective compact integral three-adic Selmer localization for the whole
Fermat Jacobian J11. Its rank is six. The proof uses the exact integral
[11] decomposition into A11^3 and six copies of the classical rank-one
factor B11=Jac(y^11=x(1-x)^2), a certified simple central zero for B11,
and Zhang's odd-degree Hilbert modular theorem. Each rank-one completed
Mordell–Weil factor injects by its nonzero local three-adic logarithm.

Run the derivative certificate with Python 3, python-flint, SymPy, and cc:

```sh
python eleven_rankone_certificate.py --limit 50000 --precision 128 --output eleven_rankone_certificate.json
```

The helper is compiled from `eleven_rankone_counts_source.txt` in a temporary
directory and removed afterward. The output retains all local factors and
573 nonzero coefficients, the enclosed contour, and both infinite-tail
bounds. It proves 3.114 < L′(B11,1) < 3.137. No rank routine, BSD assumption,
network connection, or external coefficient table is used.

Compact localization also holds at base exponents5 and7 by the existing
arithmetic-source proofs, as explained in `compact_base_cases.tex`. These
compact assertions do not expand the affine pro-3 classification: base5,
base7, base11 and higher11·3^r still have the precise limitations stated
in the manuscript. The new compact theorem has passed targeted mathematical,
source, exact point-count, and interval checks; its fresh statement-only
reconstruction is complete and whole-compared in the associated check record.


## Local exponent-seventeen and small-prime scope

`seventeen_local.tex` contains the complete local Brauer-support argument,
compact localization for every odd regular prime and all its prime-power Fermat Jacobians, and the
positive-rank split-prime sufficient criterion. Regularity at17 is proved by
Kummer’s criterion and seven displayed Bernoulli numbers; a class-number
software computation is not an input. The all-prime global cusp classification at every odd multiple of seventeen is now supplied separately by the regular-prime bridge.

`thirteen_small_prime_gate.tex` proves failure of MR(H.4) for the displayed
natural cubic-twisted three-adic lattices by residual Cartier self-duality.
It does not assert nonzero Selmer or Tate–Shafarevich group.

The general rank-one-factor lemma in `eleven_compact.tex` strengthens compact
localization for J11 to every coefficient prime, including primes dividing
the quotient-isogeny degree. Its proof handles the integral torsion kernel.

## Exponent-thirty-one arithmetic checks

Run `python check_thirtyone.py` (Python3 and SymPy). The exact output is retained in `thirtyone_arithmetic_check.json`. The program verifies the CM type and stabilizer, Bernoulli regularity, tame and higher-pairing congruences, the Gaussian-period multiplication matrix and bounded-prime list, and the relative class-number Bernoulli product. It computes no L-value, Mordell–Weil basis or Tate–Shafarevich group. The mathematical implications and remaining unproved rank/Selmer conditions are stated in `thirtyone_gate.tex`.

The joint-localization section proves an abstract continuous cohomology counterexample, an exact local-parameter relation condition, and a finite-ramification CM-character condition. These do not classify new affine Fermat exponents.

For every odd exponent n>=3, the Frey-three section criterion proves cuspidality from a global stable cyclic subgroup modulo9. A hypothetical noncuspidal prosolvable Selmer section has irreducible three-adic representation and density-one integrality. This is a sufficient criterion, not an enlargement of the classified exponent range.

## Compact section images and simultaneous Frey images

The base-five/seven full compact pro-three images are identified without an affine classification. For every odd exponent at least five, a hypothetical noncuspidal prosolvable Selmer section has individually and jointly open two-adic and three-adic Frey images. The proofs are in `compact_full_image.tex` and `frey_open_image.tex`. The stronger finite-field boundary theorem is in `finite_field_boundary.tex`: for every n>=3 in characteristic prime to 3n it gives the uniform cyclic blocks described in the introduction, and full boundary injectivity if 3 divides n. It does not give injectivity on the whole proper curve, exclude ordinary points from a full cusp fibre, or settle global affine boundary support. These proofs require no additional numerical calculation.

## Auxiliary level-twenty-seven calculation

Run `python level27_kummer_certificate.py` with Python 3 and SymPy.
The exact assertions verify the modular rational-function identity,
the fibre cubic and discriminants, the residue roots and finite-field
group operations at17 and71, and both finite group orders. The saved
output is `level27_kummer_certificate.json`. The accompanying full
finite-Chebotarev proof is in `auxiliary_level27.tex`. This certificate
concerns the auxiliary X0(27) Kummer condition, not a global Selmer
counterexample or the full compact Fermat point-map fibre.

## Regular-prime and irregular-prime arguments

`cyclotomic_first_case.tex` proves the proper finite torsor and cyclotomic character obstructions. `regular_prime_local_cusps.tex` isolates the compact local cusp at every regular p>5. `regular_prime_sections.tex` gives the full primary classification, and `allprime_regular_sections.tex` gives every odd-multiple finite-derived and prosolvable classification. These proofs do not require a new numerical certificate.

`irregular_finite_centres.tex` proves the fixed finite-set theorem and the higher-exponent bound. Its examples use exact published class-number inputs at37,59,67, with independently preserved arithmetic checks. `irregular_remaining_conditions.tex` states and proves the precise conditional prescribed-tower criterion. The existence condition and irregular global classification remain unresolved.

The finite regularity and earlier residue calculation at seventeen can still be replayed with `python regular_seventeen_certificate.py`; its output is `regular_seventeen_certificate.json`. The residue calculation is historical corroboration, not an additional hypothesis of the all-regular theorem.

The additional shared cyclotomic class-number check is run from the workbench root with Node.js and no external package:

```sh
node checks/cyclotomic_relative_classnumber_check.mjs
```

Its exact expected output is `checks/cyclotomic_relative_classnumber_expected.json`. The original ECMAScript module is retained as `.mjs` by both the importer and format validator. It checks the relative class numbers 37, 41241 and 853513 at the three irregular primes37,59,67, with small-prime controls. The real class-number input used in the theorem is a separate published result. The preserved replay receipt compares every output field with the earlier exact-integer certificate.

The source inventory is generated only after a matching fresh TeX build. The statement generator rejects missing new labels instead of assigning numbers from an earlier PDF. Same-model reconstruction status and historical losses are recorded in DEPOSIT.md and the workbench check ledger; no new independent worker is inferred from recovery.

## Exponent-thirty-seven structural certificate

Run from this paper directory with Python 3; no package beyond the standard library is required:

```sh
python check_thirtyseven.py
```

The saved expected output is `thirtyseven_arithmetic_check.json`. The exact integer/rational checks verify the CM type and stabilizer, descended primitive type, genus calculation, tame congruence, order-nine character restriction, branch-divisor eigenvalue and Bernoulli irregularity. The program prints JSON and does not modify the saved output. It computes no central L-value, exact Mordell–Weil rank or Tate–Shafarevich group. The two complete structural propositions and the precise published-theorem applicability barriers are in `thirtyseven_gate.tex`. The twelvefold's rank-zero and required Selmer input remain open.

## Current independent-check map

`records/quotient_main_independent_coverage.tsv` in the workbench records the exact current principal-statement scope. The former coverage qualifications for FQ.005 and FQ.009 are closed by the separate no-history exact reconstruction and whole comparison. The older finite-field Target26 covers only the a=5,7 theorem. The separate Target27 exact general-theorem proof froze at 16:46:56 UTC and passed root whole proof/source/exposure and 23-entry manifest comparison at 16:50:12 UTC. Both the 3-divisible clause and exact boundary-divisor order are covered. Its prior A/B and SGA1 exposure and initial-inventory timing remain disclosed. Historical status rows are retained. Source identities are generated separately after the complete source freeze; no identity is created by these instructions.

## Quintic finite-depth certificate

Run the standard-library Python program:

```sh
python check_quintic_finite_depth.py
```

It prints the exact JSON stored in `quintic_finite_depth_check.json`. It checks the residual tensor exponents through degree four, the counts of v^2+v=u^5 over F_11 and F_121, and the order-twenty companion matrix modulo three. The source proof is `quintic_finite_depth.tex`. The code does not calculate equality of fundamental-group sections; the complete group-cohomological and density argument is in that proof.

At rational primes q different from 3 and 5, split in Q(zeta5), with Frobenius of order twenty on the three-torsion of A=Jac(v^2+v=u^5), the full arithmetic cohomology set H1(G_Fq,N/gamma4 N) is a singleton for the proper Fermat quintic. Thus the whole proper point map is constant through nilpotency class three. This prime set has natural density 1/10 and contains q=11. The full proper pro-three theorem still separates different coordinate components; no full-group collision within one component is proved. Tensor-degree four already has a Frobenius eigenvalue one, so the stated low-depth exclusion stops there. This auxiliary limitation does not enlarge the affine classification or reduce a main mathematical gate.

`quintic_diagonal_limits.tex` gives the two additional full geometric proofs. They require no further computational dependency.

Two further geometric observations delimit diagonal-symmetry arguments for exponents5 and7. Over a finite field containing the relevant roots of unity, a nonidentity diagonal twist of Frobenius cannot have three-power order on the full Fermat residual homology; the three quotient maps force the diagonal weights to vanish. Separately, a geometric complement for the full diagonal group has centralizer contained in gamma2, with quotient modulo its intersection with gamma3 isomorphic to Z3^(g-1), of rank5 or14. The complement is not asserted to be Galois invariant. These statements do not decide the full same-component fibres or supply an affine boundary-support theorem.
