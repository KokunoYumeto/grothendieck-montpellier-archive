# Independent full-proof review of IF-02 and IF-04

Reviewer: GPT-6 Astra Pro; effort not exposed; SIGN_NEXT child `/root/critical_lefschetz`.
Date: 21 November 2026, completed 03:26:41 UTC.
Reviewed source: `SIGN_NEXT/work/integral_fock/contribution.tex`, whole-file SHA256 at the main read `6f8ec9e48ce8ffa45d35e126f5db1012beaf281cabb40a27445f2a6558950029`.

## Verdict and check depth

Both complete proofs pass independent reconstruction. I found no mathematical fault. This review did not rely on the author's finite-order computation for the general saturation theorem, and did not infer integral statements from rational irreducibility. I independently derived the coefficient-lattice argument, the highest-weight-line argument, the adjoint-isometry argument, the primitive root weight lattices, and all signs in the exterior embedding.

Two short expository clarifications were sent to the author and root:

1. The cyclic lattice is integrally weight-graded because every generating divided-root word applied to the initial vector is homogeneous for row weight. State this explicitly before taking a full dual-lattice intersection with one rational weight line.
2. The source's `rowDiv` allows equal row indices, while the text says root operators. Such a diagonal coefficient operator acts on a row-weight component by the integer binomial coefficient of that row weight, and therefore does not enlarge the integral cyclic lattice. This makes the claimed exact source identification explicit.

These are explanations of facts already implied by the definitions, not missing hypotheses. The author agreed to add both. The source locators were checked in the actual selected Lean files, but this report does not claim a new Lean formalization or kernel check.

Final revision check at03:39:44 UTC: both sentences are present and correct in `contribution.tex`, SHA256 `8009d0d9d266bb3d3f2a3bdc4fbba2eca0e34ab6df54091517d30418698a8114`. No outstanding condition remains for IF-02 or IF-04. The author's later changes to other IF sections are outside this report's original scope and are separately reviewed where stated.

## IF-02: independent reconstruction

### Replacing repeated blocks

For each choice of singleton pairs, the active empty/complete pairs form the standard tensor module U to the tensor power v. Every v from0 throughn occurs. Removing repeated identical blocks changes neither the image of any word nor the condition that its matrix entries be integral: the remaining block matrices are exactly one copy of each distinct block. Thus the replacement by the direct sum of U tensor v is legitimate for both image orders and their rational saturation.

### The coefficient lattice

The matrix entries of U tensor v are all products of v of a,b,c,d, independently chosen, so the coefficient lattice of the direct sum is exactly the degree-at-most-n image in Z[a,b,c,d]/(ad-bc-1). Reduction by ad=bc+1 never raises total degree. The normal monomials divide into a^r b^s c^t with r>=0 and b^s c^t d^u with u>=1.

The big-cell substitution sends the first type to a single Laurent monomial. For the second type its terms all have invariant `tau exponent - x exponent - y exponent = -u`, and its initial term has coefficient1. At fixed u, the remaining terms strictly increase s+t. The selected minor consisting of initial terms is consequently triangular with diagonal1. The nonnegative invariant in the first family separates it from every second-family row and gives an identity block. This proves both linear independence and a unimodular selected minor. Hence coefficient extraction restricts onto the full integral dual, rather than merely spanning it rationally. Terms outside the chosen degree-bounded initial-term rows cause no problem for this selected-minor argument.

The coproduct sends each entry to a sum of products of one entry in each tensor factor, so the degree-at-most-n submodule is a subcoalgebra. Its integral dual is therefore an algebra. The coefficient span gives faithfulness of its action. Counting normal monomials of degree exactlyv gives (v+1)^2, and summing gives the stated rank.

### Divided operators generate the full dual

In lower-unipotent/torus/upper-unipotent order, coefficient extraction in x^r y^s z^k after tau=1+z acts as F^(r) binom(H,k) E^(s). Every tau exponent lies in [-n,n]. On those consecutive integers, the shifted binomial polynomials binom(q+n,k) have an integer evaluation matrix with determinant1. Vandermonde changes them to binom(q,k) by an integer triangular matrix with diagonal1. Thus individual Laurent coefficients are integral combinations of these divided-root/toral coefficient operators.

I independently expanded the stated Gauss decomposition. Choosing lower degree s-j and upper degree r-j leaves the middle factor (1+uv)^(H-r-s+2j), which yields exactly the binomial in IF-02a. For r=s=k, the term j=k is binom(H,k), and every other term has smaller binomial degree after an integer shift. Negative shifts still have integral generalized binomial coefficients. Induction therefore puts every toral binomial into the divided-root algebra. This also works for k>n, when the root divided powers vanish: the same operator identity solves for the toral term using the earlier terms.

It follows that the divided-root image is the entire coefficient dual. Over Q, ordinary and divided root powers generate the same algebra. An element of the rational coefficient dual acts integrally exactly when it is integer on every matrix entry, hence exactly when it is integer on their spanning lattice. This is the claimed saturation equality for every n.

Finally H has exterior weight n-j in degreej, including the singleton blocks. An integral indicator of any one such weight is an integral combination of the binomial functions above. This proves the degree-projector claim. The rank comparison with the full endomorphism ring is strict for n>=1, giving infinite additive index there. The n=0 boundary case is harmless and is correctly excluded from that final strict comparison.

## IF-04: independent reconstruction

### One-dimensional top weight and the adjoint argument

For a column factor of height h, occupancy in the first k rows is at most min(k,h). The initial tensor saturates the sum of these bounds for every k. Because every summand in the sum satisfies its own upper bound, equality of the total forces equality in each column for every k. The only column subset satisfying those equalities is the initial subset of its height. Thus the entire ambient tensor has a unique basis vector of weightlambda, proving the asserted one-dimensional weight line without irreducibility or an integral splitting assumption.

The minor map is integral and row-equivariant: the coefficient expansion for a row substitution is the usual determinant expansion. On wedge tensors, opposite row operators are adjoint for the orthonormal basis. On polynomials, x_b partial_a and x_a partial_b are adjoint for the factorial monomial pairing, directly from alpha! normalization. Work in the finite homogeneous polynomial degree of p_lambda when taking the rational adjoint. Both sides of the minor map intertwine the two adjoint root operators, so pi* also intertwines them and A=pi*pi commutes with all roots and their Cartan commutators. Since all tensors have fixed total weight, the Cartan differences distinguish the weightlambda line. Therefore A t_lambda=c t_lambda. Pairing with t_lambda gives c=norm_Fock(p_lambda)>0.

Commutation with every root word makes A=c on the entire rational cyclic module. In particular the minor map has zero kernel there and scales the full pairing byc. Its integral image is exactly the row-word lattice, so the isomorphism is integral; there is no unproved claim that a rational irreducible summand is already an integral direct summand.

### Primitive simple-root strings and their duals

Only columns of heighti admit changing e_i to e_(i+1) in the initial tensor. Their number is d=lambda_i-lambda_(i+1). The divided s-th power sums the s-element subsets of these columns, each with coefficient1. Distinct subsets give orthonormal basis vectors. This immediately gives norm binom(d,s), and different values ofs have disjoint supports. A primitive integer vector of coefficient1 can be extracted in every support, so the whole string lattice is a primitive sublattice, not merely each line separately.

For the F formula, any fixed successor subset of size s+k has binom(s+k,k) predecessors of size s; for E, a fixed remaining subset of size s-k has binom(d-s+k,k) initial subsets. These are exactly the two coefficients displayed in IF-04a, with the stated zero convention beyond the string endpoints.

Over Q, straightening root words into negative, Cartan and positive order leaves only negative-root words on the highest-weight vector. A total weight loss s alpha_i can only use the root alpha_i, because every positive root has nonnegative simple-root coefficients. The entire rational weight space is therefore the single line Q q_s. Primitivity in the ambient tensor makes its integral intersection exactly Z q_s.

The integral cyclic lattice is the direct sum of its weight lattices: each row-divided word applied to t_lambda is a weight-homogeneous generator. Consequently a vector on Q q_s pairs integrally with the whole lattice precisely when it pairs integrally with Z q_s. Different weights are orthogonal, so the normalized dual intersection is exactly Z q_s/binom(d,s). This justifies the full dual-lattice conclusion, not merely a dual inside an isolated rational string.

### Particle-hole signs and the symplectic ambient space

Order the two root coordinates first inside every column. On their four basis states, the given permutation conjugates e_(i+1) wedge contraction_(e_i) to complete-pair creation, and the opposite operator to complete-pair removal. A direct four-state calculation gives coefficient+1 in both nonzero cases. Both original row operators have even parity, as do pair creation and pair removal, so preceding columns introduce no Koszul sign. Reordering an ordinary column basis to put an interior root first introduces the usual permutation sign; using the corresponding signed basis change preserves the claimed conjugation.

Each spectator's empty/occupied states are replaced by the two singleton states of a new symplectic pair. Both singleton states are annihilated by pair creation and removal. Thus the full symplectic L,D agree with the root operators on the embedded module, with exactly q+(r-2)q=(r-1)q pairs. The embedding maps an orthonormal integral basis to signed, distinct orthonormal exterior basis vectors, so it is isometric and primitive. Root orbit sums retain coefficients of absolute value1 and disjoint supports; a common column-order sign is irrelevant to primitivity and may be normalized. Hence q_s/binom(d,s) is not integral when the binomial exceeds1.

An independent exact script, `review_fock_particle_hole.py`, checks this construction starting from the ordinary coordinate order, including all interior simple roots. For r=2,3,4 and q=1,2,3 it checks 14,356 basis vectors and 28,712 signed intertwining identities, with distinct images. All pass. This finite check targets sign conventions; the general proof is the preceding four-state and parity argument.

## Exact source comparison

I read the local definitions of `rowDiv`, `hw`, and `weyl` in `lean_selected/Formalism/GradedWeylDivisibility/StatementA.lean`. The product of initial minors agrees with `hw`, and `weyl` is the integral span of all row-divided words. The extra equal-row operators allowed by its indexing only multiply homogeneous weights by integer binomial coefficients and do not change that lattice.

I also read `bDual`, `NablaEqDualWeyl`, and `WeylEqDualNabla` in `StatementE.lean`, and `DomWeight.detShift`, `DomWeight.natW`, `normFockQ`, and `FactDelDualNabla` in `LocalRingCardinality/DataCoeff.lean`. The Fock normalization and dual pairing in IF-04 match these definitions. A determinant twist shifts every row weight equally, so it does not change a simple-root gap or any of the stated root-string calculations. These were definition and normalization checks, not new proofs of the full formal source's downstream theorems.

## Limits

This report concerns IF-02 and IF-04 in full and the source definitions they use. It does not independently certify the IF-03 Smith table or the entire numerical/theta-lift application in IF-05 and later sections. The finite sign check is additional computational evidence, not a replacement for the all-rank proofs.
