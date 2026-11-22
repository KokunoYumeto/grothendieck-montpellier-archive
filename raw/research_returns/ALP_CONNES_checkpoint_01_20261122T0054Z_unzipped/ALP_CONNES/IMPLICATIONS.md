# Implications of the findings

Working record, 22 November 2026. The theorem A is accepted as supplied. This document distinguishes consequences of A, unconditional constructions, source corrections, and the main gates that remain under active investigation. It does not claim cubic Kummer RH.

## 1. What changes in the rational trace programme

AC-T01–T02 establish the full rational character quantifier. A covers every continuous unitary character of the rational idele class group, after the stated norm normalization. The Weil form is positive in each primitive Dirichlet sector and hence on finite sums of sectors. The unconditional cohomological trace identity in Connes–Consani–Marcolli (2007), Theorem 6.1, Proposition 6.2 and Corollary 6.3 now has its required positivity. This is a direct closure of its analytic RH criterion.

The original Connes (1999) Sobolev realization requires a different conclusion. All nontrivial zeros now lie in its critical spectrum, but a fixed Sobolev parameter retains the source's truncated multiplicity. The local zero-jet representation is a Jordan block at a multiple zero. AC-T03 and AC-S02 therefore retain the exact simplicity and domain requirements for unitarizing that particular representation. AC-T04 and AC-S08 construct honest diagonal Hilbert realizations of the full zero divisor; these are explicitly different constructions and are not represented as a newly discovered geometric Hilbert–Pólya operator.

AC-T05–T06 provide every finite Dirichlet Weil window with its exact gamma symbol, finite prime-power operator, conductor and parity, and any zeta pole correction. They establish a closed form and a compact-resolvent self-adjoint operator. AC-T13 gives strict positivity at each fixed window. The all-width statements inherited from MAS_ARTIN, MA-FT-001–MA-FT-002, now hold in the rational/Dirichlet sectors by AC-T12, with their actual weights, identity-contact exclusion and joint cutoff limits retained.

The requested all-character original C99 cutoff formula is still a distinct comparison. The new cutoff bridge AC-T21–T24 makes its weighted Mellin Gram matrix, theta tails, principal angles and sufficient trace estimates explicit. Conductor dilation and parity do not eliminate the factor |L(1/2+it,chi)|² in the Gram matrix. Burnol's one-sided closure theorem gives a genuine global L² consequence of A; substituting its completed half-line ranges for the finite prolate images discards the zero trace. The remaining estimate is written in terms of actual finite Gram inverses and tail matrices, not left as an unspecified analogy.

## 2. Spectral convergence: what is proved and what still selects an eigenline

The original finite-window compact-resolvent results in the 2025 spectral-triple paper were already unconditional, and the 2021 paper already stated strict positivity under RH. This run does not relabel those statements as discoveries. AC-S03 adds the detailed closed-domain and all-index Galerkin form needed here.

AC-S05 gives the quantitative bound

    0 < a_r(lambda) <= C_r lambda^(4r+5) exp(-2*pi*lambda^2)

for each fixed index r and sufficiently large lambda. The theta kernel's normalization is corrected in AC-S04; all constants and sampling arguments use the corrected kernel. AC-S18 proves a stronger subspace statement: the projections below exp(-pi*lambda²), extended to whole-line L², converge strongly to the identity. For each derivative of the theta kernel it gives an explicit weighted L¹ error and consequently a uniform Fourier limit on every fixed horizontal strip. This is real convergence without an unproved simple-even-groundstate hypothesis.

That theorem also explains its limitation. The low-energy subspaces approximate every L² vector, so small energy alone cannot distinguish the desired bottom eigenfunction. AC-S19 proves nonclosability of the global compact-test Weil form in unweighted whole-line L², while each fixed-window form remains closed. The specific prolate/groundstate identification still requires a quantitative eigenline selection or separation theorem. No individual prolate eigenvalue is matched to a zeta zero merely by comparing counting asymptotics. The unresolved discrepancy between supplied prolate counting versions is isolated in `modules/spectral_prolate_unchecked.md` and is unused by the proved results.

For the local-factor moment problem, AC-S14 proves the actual finite-prime Jacobi/quadrature limit: an absolutely continuous measure of full support. The unscaled mass-one measures exhausted over all primes instead concentrate at zero, AC-S16. The proof can be made unconditional using the precise classical prime-number estimate; A is not needed for that stronger formulation. The formal Witt interpretation, AC-S15, remains a formal ring identity and does not assign an étale Frobenius or a motive. Subsequent local eigenbranch and scaled-limit findings retain their own statements and check events in the evolving spectral module.

## 3. Algebraic geometry, Grothendieck's frameworks, and the actual square

AC-G01 proves the exact Hermitian Hodge inequality on the test-function subspace with two vanishing moments. AC-G02 constructs its marked numerical intersection space, with a hyperbolic plane and negative spectral complement. It establishes uniqueness only for the specified minimal marked kernel. It does not construct the arithmetic square, a surface Riemann–Roch theorem, or the cohomology of a scheme. AC-G03 excludes a finite-dimensional single-Frobenius determinant model by its zero-counting growth. It does not exclude an infinite-dimensional or more general cohomological construction.

The scaling-site and Spec Z Riemann–Roch theorems retain their original dimension functions, right-continuous rounding and exceptional terms. Their exact source locators are in the paper. A supplies the analytic inequality sought by the square strategy; it does not prove the source's remaining geometric construction steps. The new Jacobian and absolute-geometry papers add genuine local and monoid structures but do not by themselves close that global comparison.

The Artin–Tate constructions are actual objects, not merely formal positive counts. AC-G04–G07 and AC-G12 give their complete zeta factors, including the prime 2, and distinguish a graded direct sum of pure constituents from a single pure object. A gives the corresponding translated global critical lines. Local weight purity was already unconditional. AC-G05 shows why taking inertia invariants at a ramified prime cannot be treated as a tensor functor. AC-G06 gives an exact positive-count counterexample to inferring existence of an actual representation from pointwise nonnegative traces.

The split-zero construction is made exact in AC-G08–G11. There is a difference between the additive zero and the supported ring zero; a sectionwise construction fails the sheaf condition and must be sheafified. The resulting clopen-support description and the separate semiring-spectrum construction are proved. The nonunital Boolean inclusion, failed additive power maps, and missing antipode are retained instead of silently importing ring identities.

The verified Grothendieck framework locators are SGA 1 V §4 and §7 (Galois categories and finite étale schemes), SGA 1 XI §6, Proposition 1, Definition 2, Corollary 3, Proposition 4 and Corollary 5 (Kummer torsors), SGA 4 II Theorem 4.1 (associated sheaf), and SGA 6 V 2.2(b), Lemma 2.2.1 (exterior powers and representation rings). They locate the categories and operations used here, not the new analytic results.

Montpellier cotes 2, 10, 11, 14, 16 and 19 are verified only at catalogue level in this run. Earlier attached documentation records cote 54 scans 003/005/007 and cote 4 scans 003/005/006; those are historical checks, not new scan inspections. Direct scans have not been obtained here. The requested scan-level transfer therefore remains a source gate wherever it is essential. Likewise the DELTA23 identification of Grothendieck's Delta with chi12 composed with u is not independently certified: only the intake assertions, not the definition and underlying proof, were located.

## 4. The follow-up geometric papers

The finite-prime circle construction has an exact Euler product, AC-G15: for an abelian extension it equals its Dedekind zeta function, with all ramified factors obtained from inertia and decomposition. A gives its critical-line zeros. AC-G16 proves square-root smoothed monodromy prime-power estimates and a prime-only estimate with the stated logarithmic loss. These are fixed-extension estimates; they supply no unproved uniform conductor control.

The supplied source versions require several precise corrections. AC-G13 retains the sign quotient in the archimedean Jacobian fiber. AC-G14 separates the idempotent locus from the whole rank-one-group monoid. AC-G17 handles the trivial-cover exception. AC-G18 distinguishes a compatible cyclotomic tower from its zeroth coordinate. AC-G19 proves that valuation profiles do not preserve ring addition as max-plus addition. AC-G20 keeps the abelianized nature of the stated global and local symmetry actions. AC-G21 corrects the proposed Ind-ring interpretation of Q/Z while preserving the valid inverse-limit product of frames and roots.

The Deninger comparison receives similarly scoped treatment in AC-T15–T20. Dropping finite-kernel restrictions changes the character space; a compact solenoid fiber cannot be substituted by one of its dense real-flow orbits. The corrected finite-cover and anti-equivariant-map statements remain available. These checks concern the exact attached versions and do not assert that every formulation in the wider programme has the same defect.

## 5. The cubic rung and the prior runs' open rows

AC-K01 corrects the rational Lambda-descent equivalence: it is a statement about finite étale algebras with cyclotomic field factors. A ramified field cannot itself carry the required integral Frobenius lifts, AC-K02. The relative ray-class construction supplies the necessary boundary algebra instead, AC-K03. At p=269 this is completely explicit: conductor (269), B=E×K, a maximal fibre-product order of index 72361, and every Frobenius lift, AC-K04.

The finite ray-class host removes an ambiguity in the arithmetic object. It does not prove ALP_MACHINE H04.4 or bound its individual twisted cohomology lengths. AC-K05 gives all norm-pullback Hecke sectors reached by A; AC-K06 preserves the obstruction to turning the actual cubic extension into a rational Dirichlet restriction by CM base change. AC-K07 and AC-B02 show precisely why a character-twisted partition function is not generally a positive Gibbs density. AC-K08 computes the surviving cubic factor in even tensor powers. AC-K09 proves unconditional strict Weil positivity for the cubic269 sector on 1<lambda<=4. This finite support range is not an unbounded arithmetic ramp window.

The CM ground-state bridge is concrete: AC-B03 builds the radical as an arithmetic observable, with its three Galois-conjugate ground-state values. AC-B04 gives the exact finite conductor correction for unit neutrality and separates it from infinite-order angular compensation. AC-B05 gives the exact norm/divisor-pair Fourier identity, its local solvability and its positivity limits. AC-B06 proves the common cyclotomic character table and the full factorization after adjoining the radical to Q(zeta12); the cubic and quadratic-twisted cubic factors remain.

The main inherited rows therefore stand as follows at this working checkpoint:

| Prior row | Change supplied here | Still required |
|---|---|---|
| ALP_MACHINE ALP-Q3 / H04.4 | Explicit primitive host and local lifts; one finite positivity interval; exact scope of attempted BC and neutrality bridges | Uniform twisted arithmetic lengths and growing-host costs sufficient for the sparse-ramp bound |
| ALP_MACHINE ALP-Q3-GLUE / H06–H07 | Correct integral boundary host is now explicit | No new bound is inferred from gluing dimensions alone |
| ALP_MACHINE ALP-Q3-SINGLE / H08 | One cubic character remains the precise analytic target | Its actual length bound, not merely equality of conjugate lengths |
| MAS_ARTIN MA-FT-001–002 | A closes the equivalence for every rational Dirichlet sector | Cubic delta-plus vanishing is still equivalent to the unproved cubic RH input |
| C99 all-character cutoff | Actual weighted Gram and tail comparison is explicit | The quantitative comparison of finite prolate images with the required cutoff trace |
| S25 / 2026 letter missing groundstate steps | All fixed low eigenvalues and whole low-energy subspaces have proved limits | Specific lowest-eigenline selection and comparison |
| Riemann–Roch square strategy | Exact analytic Hodge kernel and numerical construction | The global geometric square and its cohomology/intersection theorem |

These are live research gates. The dated ledger records subsequent changes and the scheduled movement reviews without counting packaging or a restated gate as movement.
