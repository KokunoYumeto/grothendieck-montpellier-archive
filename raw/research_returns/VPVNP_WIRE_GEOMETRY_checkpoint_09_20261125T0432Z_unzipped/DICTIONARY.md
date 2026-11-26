# Translation of the proved results into geometric language

This file describes mathematical connections proved here. It does not identify tensor prices with motives, lambda operations, or Grothendieck's conjectures. No archive cote is assigned where the attached material supplies none.

## Finite tensor identities and schemes of coefficients

A fixed cover template has finitely many local linear maps. Their entries are coordinates on an affine space over the prime ring, and equality of the resulting tensor with a prescribed wire tensor is a finite system of polynomial equations with integer coefficients. Invertibility conditions, when genuinely needed, are encoded by adjoining an inverse variable. Thus a template defines an affine scheme of finite type over Z.

The finite-certificate theorem says that failure of a finite metric to be a price is witnessed by a point on one such scheme, together with a strict real inequality involving its fixed combinatorial loads. The real inequality does not involve the map coefficients. This separates the algebraic existence problem from the geometric margin.

Over C, a nonempty coefficient scheme has a point over a number field. After clearing the finitely many denominators, the same point extends over the ring of integers with D inverted. Reduction at every prime not dividing D preserves the identity. The proof is in the finite-specialization and nonprice-specialization results. This is the same finite-witness mechanism as B7.1 of the attached ALPOGE_GCT bridges text; it does not import an unstated motive or weight theorem.

## Field extensions and amortized descent

For a finite extension L/k of degree d, expand local maps in a k-basis of L and apply a k-linear functional fixing1 to their coefficients. On n tensor copies the basis is still a basis of L, so at most d raised to the number of parties many k-restrictions are needed, independently of n. The extra logarithmic cost vanishes after division by n. A strict finite-certificate margin therefore descends. Arbitrary extensions are reduced to finite algebraic ones by the coefficient scheme and the Nullstellensatz.

This is a statement about finite-type equations and restriction of scalars at the level of explicit multilinear expressions. It is not a claim about descent of every individual linear map or every chosen algebraic point.

## Orbit closures and separating equations

The padded-permanent problem concerns two closed invariant cones in a finite-dimensional representation. Homogenization and dehomogenization are polynomial or linear maps between coefficient spaces, and hence continuous for the Zariski topology. The padding equivalence is a direct statement about their images and closures.

In characteristic zero, reductivity decomposes the homogeneous ideal of one cone into finite-dimensional irreducible representations. If the other cone is not contained in it, one such irreducible summand contains a separating equation; its highest weight line is a separating equation at an appropriate orbit translate. This does not compare the sets or multiplicities of irreducibles in the two coordinate rings. The paper gives a concrete torus example showing why those stronger conclusions do not follow formally.

The integral separating-equation argument rechecks the finite-witness reasoning of attached B7.1. Attached B7.3 supplies a bad-prime orbit example. Its conclusion is recorded only for orbit containment, not transferred without proof to prices.

## Representation rings, Schur functors, and moment polytopes

The explicit spectrum calculation uses Schur-Weyl projectors and entropy of marginal eigenvalues. These are representations and their tensor products; the nonzero-projector conditions are representation-theoretic positivity conditions. The square upper-functional counterexample is verified by exact rational projectors for S4, with coefficient minus1/48 and squared norm1/12.

The attached KRONECKER_FINDINGS text studies particular rectangular Kronecker coefficients. It provides motivation for exact positivity checks, not a theorem that the square metric belongs to a moment polytope. Our certificate is computed directly; no unverified earlier positivity claim is used to settle the price question.

Representation rings carry lambda operations through exterior powers, but the paper does not construct a lambda-ring homomorphism from the tensor semiring to prices. In particular, positivity in a representation ring does not by itself prove additivity, multiplicativity, or restriction monotonicity of a candidate spectral point.

## Norms, degeneration, and curvature

Local invertible maps do not change a spectral value. A limit of such maps may be a degeneration, under which the value can decrease. Norms invariant under a compact subgroup and the Kempf-Ness geometry of GL/U do not automatically produce functions invariant under the full linear group with the spectral axioms.

The attached bridges B5.1-B5.3 correctly distinguish bounded-operator norm statements from full orbit-closure statements. Their warning applies here: scalar changes can invalidate an unnormalized norm obstruction. The paper uses algebraic restrictions and exact rank inequalities rather than assuming a norm is already a spectral point.

The price-space embedding and flat-rectangle result concern metric nonpositive curvature. They show, conditionally on the cited preprint theorem, that a square price is equivalent to all finite planar Euclidean configurations being prices. They do not identify price spaces with symmetric spaces, Bruhat-Tits buildings, or any particular algebraic group.

## Motives, correspondences, and weights

No result of this paper constructs a motive, a correspondence, a realization functor, or a weight filtration for tensor prices. Entropy weights and highest weights have their usual representation-theoretic meanings; neither is a weight in the sense of a Weil cohomology theory. The attached sources do not establish such a bridge, so no archive cote or claimed application to a motivic programme is given.

## Cross-polytopes, flatness and a classical quadratic-form gate

The new dimensionwise equivalence is metric rigidity followed by algebraic duality. Pairwise Euclidean coordinate squares give complete orthogonal lines in the tangent cone; parallel-set splitting and Kirszbraun extension fill their convex hull. A compact extremal problem then turns absence of that metric into a strict homogeneous inequality. Cover duality realizes the inequality by finite local maps, so it again lands on a finite-type coefficient scheme. No identification of the CAT(0) tangent cone with a tangent scheme is intended.

For four terminals, the same argument identifies the remaining gate with the asymptotic partial-transpose rank of the identity matrix. Over C, polarization compares that rank within a factor2 with the minimum number of bilinear squares in a composition identity q(x)q(y)=q(f(x,y)). Thus the question is genuinely connected to the classical composition problem for quadratic forms, rather than only formally reminiscent of it. The known upper exponent is sqrt2; price membership is equivalent to its sharpness, under the price-space theorem.

A composition formula defines a morphism from a product of deleted projective quadrics to a deleted projective quadric: the norm identity ensures that nonisotropic inputs have a nonisotropic output. Dugger–Isaksen's Hopf-condition theorem uses the induced map on motivic cohomology; their separate2005 paper uses algebraic K-theory to obtain divisibility conditions. These are external cited theorems about the very coefficient formulas in the new gate. We have not re-proved their full cohomology calculations or obtained a new K-theoretic obstruction attaining exponent sqrt2. The connection creates neither a motive for a price nor a new weight filtration. No archive cote is assigned: this connection comes from newly retrieved primary sources, not from a demonstrated identification in the attached archive.

## Fourier contraction and the distinction between hypotheses

The exact Hilbert ratio on the additive group of binary matrices is a comparison of eigenvalues of two averaging correspondences on functions: average over rank-one increments and over invertible increments. Walsh characters diagonalize both operators. The top ratio is2(1-2^(-mu)) and is attained at rank-one dual characters. This is an elementary representation of a finite abelian group over the reals, with real squared distances; it does not concern the coefficient characteristic of the tensor identities. It explains why the Euclidean subclass alone cannot disprove the universal contracting hypothesis.

## Curves, sections, and the global reconstruction cost

The q-digit deformation replaces a rational normalizing factor by the algebraic function f=Y² on the smooth characteristic-two Fermat curve X^(q−1)+Y^(q−1)=1. Frobenius identifies its distinguished local branch with the inverse of an infinite digit product. The determinant is a section of O(D), where D is Θ times the full infinity hyperplane divisor. Its locally small tensor ranks at two places do not control its values globally without a reconstruction argument.

In algebraic-geometric language, the obstruction is the exact evaluation sequence for O(D−L0P0−L∞P∞). If its degree is at least2g, Riemann--Roch makes evaluation at the third point surjective, so a section can have all prescribed jets zero and still be nonzero there. If the degree is negative, there is no section, the jet map is injective and every evaluation factors through it. This proves the ambient budget NΘ+O(g), N=q−1. The same calculation supplies a valid finite tensor identity. It is not a rank lower bound on the determinant span. The finite8-label calculation makes that distinction explicit: the span has dimension45 and recovers with257 jets at each point, below the ambient385.

This is a genuine line-bundle/cohomology connection in the language of schemes; no specific archive cote or claim about motives, weights, or a new cohomology theory is made. The exact source is the Stacks Project Riemann--Roch lemma, tag0BS6, and the plane-curve genus lemma, tag0BYD.

## Subspace buildings and the contraction equality metric

The rank metric d(A,B)=sqrt(rank(A−B)) is obtained by sending a matrix to its graph subspace. The identity dim(graph A∩graph B)=μ−rank(A−B) converts matrix rank into the squared distance of subspace vertices in a CAT(0) orthoscheme complex. This is linear algebra on subspaces over F2, with the curvature theorem of Haettel--Kielak--Schwer as a cited input. It proves that curvature alone permits the extremal contraction metric. It does not realize that metric as a tensor price. The finite price test for contraction follows instead from the equality classification in the audited compactness argument. There is no demonstrated λ-ring, motivic, or archive connection beyond these stated facts.

## Determinantal divisors and the special fibre of the crossing kernel

The digit-kernel calculation is a statement about a matrix over the coordinate ring F2[X] of the affine line. The ideal generated by its middle minors is principal. Its generator is the explicit polynomial G in the paper. Localizing at each irreducible polynomial turns the calculation into a discrete-valuation problem: row and column operations preserve the determinantal ideal, and the smallest sums of invariant-factor valuations determine its order. These are determinantal/Fitting-ideal calculations, not an analogy with them.

At X=1 a strict gap separates the first M invariant factors from the second M. After division by G, the middle exterior power therefore has a rank-one special value: it is the outer product of the two Plücker coordinate vectors of the graph of the complement permutation. Balanced row and column slices turn this value into the required pair of crossing wires. The half-filled subset involution preserves energy exactly, so the same output survives the complete fixed-energy symbol classes. The proof is Proposition “A polynomial crossing after removing the common factor,” together with the middle-minor divisor proposition. This is an explicit degeneration in an exterior-power representation. The individual coefficient ranks are not determined by the divisor or by the generic fibre's change of basis.

Exterior powers are genuine lambda operations on vector bundles and representation rings. Here they are used at the level of a free module over F2[X]; no lambda-ring homomorphism from tensor prices is constructed. The vanishing orders at X=1 and at the other roots of1+X^(q-1) are local algebraic orders, not weights in a Weil cohomology theory. The attached archive does not identify this kernel with a motivic correspondence, so no archive cote is supplied.

## Invariant-support packing and the full local flip–cup algebra

The all-copy lower bound52^floor(k/2)*7^(k mod2) uses a finite-dimensional commutative invariant algebra with three idempotent blocks of dimensions1,9,6. Partial transpose is a specified involution on its coefficient space. Invariant linear forms give support sets that every feasible decomposition must meet; a nonnegative packing of these sets within the block-rank capacities gives a rank lower bound. Tensor products of the packing, not an unproved tensorization of minimum rank, give the all-copy conclusion. The argument remains valid in every characteristic except2, including characteristic3 where some coefficients vanish and supports only shrink.

This is finite-dimensional invariant theory and a combinatorial packing certificate. It does not require positivity of an operator or a semisimple decomposition in characteristic2. The exact two-copy minima and the separated flip/cup coding bound are more restricted statements in the same section. The latter uses the moment-matrix mechanism behind Rao's orthogonal-array bound, credited to Rao and Stinson. None of these fixed-algebra obstructions is a theorem about arbitrary partial-transpose decompositions.

## Hodge projectors, Fourier transforms, and the scope of coding positivity

The four-dimensional Hodge operator decomposes the local tensor square into blocks of dimensions1,3,3,9. Its partial-transpose action is the tensor square of a two-state transform that is sign-conjugate to the normalized quaternary MacWilliams transform. Consequently the full product Hodge algebra is exactly a coordinate-radial function space on an additive quaternary group, and matrix rank becomes weighted support size. The self equation becomes g+Fourier(g)=s for an explicit quadratic sign function. The asymmetric equation has two independent functions.

This is a proved correspondence between a representation algebra and a finite Fourier problem. The classical code and quantum-shadow transforms are cited from Calderbank–Rains–Shor–Sloane and Rains. Their positivity conditions apply to the source's code or positive-operator objects; arbitrary complex coefficient functions in this paper need not satisfy them. Thus the connection does not supply a positive cone, a weight filtration, or a motivic interpretation, and no positivity conclusion is imported without its hypotheses.

## Reynolds operators and an exact centralizer formulation of the main problem

Averaging over a compact orthogonal or spinor group is the characteristic-zero Reynolds operator. For tensor degree k, its conjugation matrices depend polynomially on a fixed number of group coordinates, with degree linear in k. The polynomial-space dimension is therefore polynomial in k. Expressing the Reynolds operator as a finite linear combination of that many conjugations bounds its effect on rank. Equivariance with partial transpose preserves the crossing equation.

This gives an exact asymptotic comparison between unrestricted partial-transpose cost and cost in full diagonal centralizers. Brauer's orthogonal centralizer theorem and dimension-two Schur–Weyl duality identify the resulting algebras, respectively, with a Brauer-algebra image and a Temperley–Lieb image. The spinor argument specifies the J-adjoint transpose and changes only the second summand when comparing with ordinary partial transpose. These are characteristic-zero representation-theoretic reductions; no modular Reynolds operator is assumed. Full centralizers contain large multiplicity spaces and interactions between copies, so the earlier bounds for products of small local algebras do not transfer to them.

The Temperley–Lieb operators can be written with noncrossing pairings, but this is a tensor-diagram statement, not a construction of algebraic cycles or motivic correspondences. The exact source identifications and the rank-overhead proof have separate locators and check records.

## Common centres and simultaneous full tensor values

The binary matrix rank metric has a common midpoint for every full-rank diameter in every CAT(0) realization. The proof uses rank-one idempotents: each produces a Euclidean rectangle, and these idempotents span the whole matrix space additively. The midpoint equality propagates through all translations. A normalized spectral realization can then be extended to that centre while preserving every old tensor value. The three-party edge classification fixes its functional on every full-rank diameter triple, simultaneously.

The matrix coordinates over F2 here are labels for a finite metric space; they are not a reduction of the coefficient field of the tensor spectrum. The conclusion is a compatibility condition on many overlapping tensor semirings. It does not identify a price-space building with a Bruhat–Tits building over the coefficient field and does not prove that the rank metric is a price.

## Scalar compounds and exact rank blocks in characteristic two

The scalar balanced compound has a direct decomposition by the two difference sets of a pair of occupied subsets. Within each block, its coefficients are matrices of binomial functions of intersection size. A single nonzero coefficient forces a whole collection of disjoint blocks. Reflection forces the complementary collection on the other cut. This proves a3/2 exponent obstruction, including arbitrary coefficients over characteristic-two extensions and arbitrary tensor powers of the full coefficient span.

The proof works directly with entries and disjoint matrix blocks. It does not import a characteristic-zero decomposition of the Johnson scheme into irreducibles. The tensor-power exponential rate is a finite symmetric probability calculation, not a weight argument from cohomology. Parameter-dependent exterior changes connecting the digit kernel to this scalar matrix do not preserve coefficient ranks, so the digit construction is expressly outside this obstruction.

## Geodesic motion of tensor values and radial homogeneity

The full normalized extension theorem supplies log-convexity of every tensor value when all its parties move by the same fraction along specified old geodesics. The proof uses two retractions, uniqueness of CAT(0) geodesics, and transport along zero-value-cost wires. Consequently, adjoining an already specified geodesic point does not change a unit tensor's exponent. This is a statement about the entire tensor semiring, stronger than a wire-distance inequality.

For the binary matrix rank metric, complementary-rank rectangles determine a common centre and the exact metric on every pair of radial segments. Compactness selects a point of largest normalized scale; Zorn selects a pointwise-minimal member of that fibre. A correlated threshold retraction then forces the value on each whole radial copy to be the original value raised to its radius. This does not determine tensors mixing radii and does not prove price membership.

In algebraic-geometric terms, these are compactness and multiplicative-evaluation statements on the tensor restriction semiring. They are not assertions that a moment-polytope functional or a norm on an algebraic group exists. The common scaling resembles homogeneity of a valuation, but no additive valuation on a coordinate ring is constructed. No identification with a scheme-theoretic, K-theoretic or motivic realization, and no Grothendieck archive cote, is supported by the sources here.

## Octonion output rigidity over Z[1/2]

For the fixed eight-output Cayley–Dickson multiplication table, the two linear maps R ↦ (Id±Γ)(VRVᵀ) are injective. The chosen coordinate relations reduce the kernel to one output functional, and eight product differences are ±2 times the basis vectors. Thus the proof works over every field in which2 is invertible. In scheme language the two kernel schemes over Spec Z[1/2] are zero sections; the unique pair solving the fixed-span crossing equation is R=S=I/2. The independent exact minors ±256 give the same localization. This is a concrete instance of spread-out reasoning with excluded prime2 for this scoped statement. It does not provide excluded primes for a square-nonprice certificate, which is still missing. No K-theoretic or motivic interpretation is asserted.

## Failure of equivariant Reynolds projection in characteristic two

On a positive tensor power of the standard SL2 module, let P select the first basis vector in the first factor. The determinant-one swap conjugates P to I−P. Every equivariant linear map into the centralizer therefore sends I to2π(P)=0. The invariant identity cannot be fixed by such a map.

This exhibits failure of an equivariant splitting for this conjugation representation over every characteristic-two field. It is the precise modular obstruction to the linear invariant projection used in the complex centralizer reduction. It does not exclude a different, nonlinear or nonequivariant rank reduction. The statement concerns invariant modules, rather than an obstruction in a Grothendieck group; no archive cote is justified by the attached materials.

## Ordered upper quantum expressions and power regularization

The exact two-wire witness is a Schur-functor calculation over C. At q² copies the local rectangle(q^q) is det^q, and its self-conjugate Specht module carries a one-dimensional sign pairing. Pairwise nonzero contractions of that pairing force every ordered crossing projector to survive. This gives the full ambient entropy value on a product of two wires, exceeding the product of the two individual values. Replacing q by q^m proves that both limsup and liminf tensor-power regularizations retain the gap. The centre can be a one-dimensional factor, giving q^sqrt(2) versus q for the centred-square expression.

In lambda-ring language, the exterior power of C^q tensor C^q and the rectangular Schur functor explain the one-dimensional general-linear-group factors. The actual obstruction is a finite-dimensional representation calculation followed by an exact all-dimensions formula. It is not a theorem about motives, Frobenius weights, or every spectral extension with the same individual-wire values. The complete proof is in the paper’s exact matching-wire proposition and its two power-regularization corollaries.

## The zero-order LOCC boundary and a simultaneous wire criterion

Normalized LOCC spectral points of scalar order alpha have a pointwise compact boundary as alpha tends to zero. Rescaling each fixed local linear map to a contraction introduces only a factor c^(2alpha), which tends to one; the limit is therefore invariant under algebraic restriction and has ordinary spectral normalization. A single product of the desired wires tests simultaneous attainment: the logarithmic deficit between its prescribed product value and its N-regularized upper-functional value is the sum of nonnegative individual deficits. The exact uniform criterion includes every tensor power and every GHZ catalyst, with the zero-th power supplying normalization on all natural units.

This is a passage from Hilbert-space monotones to algebraic restriction invariants. It does not identify the scalar parameter with a motivic weight or give an integral model of the analytic construction. Individual-wire values of the operator-mean family are exact at every positive parameter because all cut observables reduce to one commuting observable or the identity. Products of wires need not share this reduction. The small-parameter joint lower bound remains open, so no square price is claimed. Published Bugár–Vrana Proposition3.15, Theorem3.23 and Corollary5.5 provide the precisely stated regularization and established parameter-range inputs.

## Growth normalization and two diagonal wires

A positive-order LOCC upper functional has a well-defined growth exponent on natural-number/GHZ units. Power regularization followed by this exponent normalizes the abstract upper functional. In the square application, means supported on the three two-versus-two cuts are already exactly GHZ-normalized. Saturating just the two diagonal upper prices forces the four side prices by the CAT(0) quadrilateral inequality. The remaining sufficient estimate must be uniform under arbitrary GHZ factors; it is not established.

In algebraic language, this is normalization of subadditive/submultiplicative functions on a preordered tensor semiring, followed by a boundary passage to restriction-monotone semiring homomorphisms. It is not a construction of a lambda-ring operation, a motivic weight, or a correspondence. No archive cote asserts such a connection. Proofs: GHZ_GROWTH_NORMALIZATION_AUTHOR_PROOF.md, PAIR_CUT_GHZ_NORMALIZATION_AUTHOR_PROOF.md, TWO_DIAGONAL_SATURATION_AUTHOR_PROOF.md, and their independently frozen comparisons.

## A finite rank metric outside the cut cone

Sixteen binary3-by-3 matrices give a positive signed distance sum for the square root of rank, whereas every cut gives a nonpositive sum. This blocks nonnegative cut combinations for every matrix size at least three. The obstruction is to that convex cone only: no theorem identifies all spectral prices with that cone. The arithmetic uses only finite-field rank and an exact radical inequality; it does not provide a scheme-theoretic noncontainment or a motivic obstruction. Proof: INDEPENDENT_RANK_METRIC_16_L1_REPROOF.md and the rank-metric section.

## Projected pair-product algebras in characteristic two

For a complement-stable binary coordinate code S, projected multiplication operators in commuting pair nilpotents split into xor blocks. The diagonal equations force a rank cost whose fixed-code tensor-power rate is at least|S|^(3/2). The middle-weight code identifies the earlier balanced-compound coefficient space; the full cube gives a uniform barrier in the number of pairs. This is a rank theorem in a specified finite-dimensional algebra, valid after every characteristic-two field extension. It is not a bound on every Temperley–Lieb operator or every polynomial in the separate generators. The coefficient-space identification is checked after an exact fixed change of endpoint coordinates.

Within the larger square-zero multiplication algebra, requiring every monomial to have ordinary degree above the middle leaves no self-complementary solution in even pair number and exactly the Boolean majority pair polynomial in odd pair number. The proof decomposes by singly occupied sites and uses triangular Boolean interpolation. This is a statement about that high-degree subspace, not the unrestricted algebra.


## Non-tree prices, tangent limits, and the exponent gap

The price-space theorem realizes a finite price inside a complete CAT(0) space whose entire finite metric family consists of prices. If that space is not a real tree, first variation gives an angle strictly between zero and pi. A completed space of directions contains a short geodesic arc, so the tangent cone contains a Euclidean sector. Every finite planar configuration is a rescaled finite-subset limit. Thus any non-tree price is equivalent to a square price, and the normalized diagonal objective has only the values2 and2sqrt2. The geometric ingredient is classical and is credited to the Alexandrov-angle/tangent-cone literature, with Kleiner's broader dimension theorem identified precisely.

These tangent cones are metric tangent cones. They are not Zariski tangent schemes, normal cones of closed immersions, or associated graded rings of a local algebra. The argument gives no motive or realization functor for a price. Its relation to schemes enters only after spectral cover duality: on the tree branch, the universal four-point inequality gives finite covers by side-wire products with subexponential term counts. Their local coefficients satisfy finite polynomial equations over the prime ring, as in the coefficient-scheme construction above. Grouping terms by a cheaper adjacent cut proves a near-linear crossing exponent. Together with the square-price branch this yields the exact exponent alternatives1 andsqrt2, and the same alternatives for the complex Hurwitz formula count. It does not identify a single finite coefficient scheme whose nonemptiness decides the whole asymptotic branch.

The existing number-field specialization argument applies to an individual strict cover once it is found. The exponent dichotomy provides no explicit cover or denominator integer. The attached ALPOGE_GCT B7.1 connection remains the already checked finite-witness spreading argument; no additional archive identification is asserted.

## Combined Hamming weights as an integral direct-sum decomposition

The binary tensor module has an integral basis indexed by bit strings. Sorting pairs of strings by their combined weights on fixed coordinate blocks decomposes its tensor square into free direct summands W_h. The corresponding diagonal idempotent matrices have entries0 and1, so the projection E(X)=sum_h Q_h X Q_h is defined integrally and survives every base change. The complement-twisted partial transpose preserves the same entry mask. This gives an exact admissible subalgebra and rank overhead product_i(2k_i+1), with no division by a group order and no assertion of modular reductivity.

In K-theory notation the direct-sum identity is simply [U tensor U]=sum_h[W_h] for finite free modules. The ranks are coefficients of product_i(1+t_i)^(2k_i), and the endomorphism-algebra dimension follows from Vandermonde's identity. The decisive inequality is a rank inequality on compressed matrices; it does not follow merely from an equality in K0. The construction uses no lambda-ring morphism from spectra, motivic weight filtration, or unproved positivity principle. Its characteristic-two relevance comes from integral coordinate idempotents.


## Determinant covariants and a raw operator-mean witness

For a q-by-q-by-q-by-q tensor, the determinants of its two adjacent q-squared flattenings are polynomial relative invariants. Multiplication by a determinant power twists each polynomial GL representation by a rectangular highest weight. Their product therefore lies in simultaneous Schur sectors whose row lengths have a common lower bound. Entropy majorization and positivity of the geometric mean turn that algebraic support into the raw binary-mean estimate in the paper. Symmetrization bounds the coefficient-vector norm without numerical approximation.

This is a concrete connection between polynomial covariants, determinant characters and Schur-functor weights. Those are highest weights of linear-group representations, not motivic weights. The witness gives a strict raw matching surplus at q=2, but its entropy bound for grouped binary powers is n+1+o(1), and it contains no arbitrary-GHZ-factor estimate. It establishes no spectral point or motive. No further archive identification is asserted.

## The minimum four-cycle face and triangular graph ideals

Two relabeled four-cycle subrank inequalities force every normalized four-party wire metric with cyclic sides at most1/2 to have those sides exactly1/2 and diagonal sum at least1. Equality is precisely the alternating star(a,b,a,b). This is an exact numerical face of the normalized spectrum; it is not a new motivic or K-theoretic realization. Paired-cut operator means evaluate GHZ-catalyzed graph products supported on at mostthree parties exactly, giving the uniform four-party matching lower bound r q^(1+alpha). Its surplus vanishes at orderzero. Neither statement constructs a non-tree price.

In characteristictwo, the Artin algebra K[x_i,y_i]/(x_i²,y_i²) carries the heat involution L. Triangular coordinate changes x_i→x_i+F_i(y) identify the multiplication rank of u(y)product_i(x_i+F_i(y)) with the rank of multiplication byu in the y-algebra. For k>=4, two such common-coordinate principal ideals cannot contain a pair f,g with f+Lg=1. The proof uses the high-degree fixed-space calculation and a logarithmic derivative after complementation of squarefree x indices. This is a result about finite local algebras and ranks in characteristictwo, not an obstruction for arbitrary low-rank operators or a statement in a lambda-ring.

## Rectangular Specht commutants and determinant characters

Over C, the rectangular Schur module of shape(n^q) has the one-dimensional GL_q factor det^n. The corresponding Specht multiplicity module E carries a real invariant orthogonal form. Invariant four-party tensors identify with End_S_(qn)(E tensor E), and the two crossing cuts become ordinary and partially transposed matrix blocks. Products of the two flattening determinants, padded by a bounded power of the fourfold alternating contraction, give a vector supported on high-dimensional Specht blocks for both cuts. Its pairing with the crossing identity is nonzero. The hook formula therefore forces a rank-sum exponent at least h_(q²)/log2(q), which exceeds sqrt2 at heights2,3,4.

The determinant twists are polynomial representation characters; the rectangular partitions are highest weights. This is an exact Schur-functor and symmetric-group representation calculation, with classical Schur–Weyl and hook-formula inputs credited to their precise sources. It gives no motivic weight filtration, realization functor, or K-theoretic obstruction. In particular it does not identify this commutant with the exponent-equivalent full SL2 centralizer. The restriction to this family is essential, and the main square-price and uniform operator-mean gates remain open. No archive cote is justified by the attached work for this additional comparison.

## Canonical exterior powers and contraction blocks

In characteristic two, subset deletion and wedge multiplication on Lambda^p K^L give an exact crossing identity after all partial contractions are grouped into one opposite-cut operator. Sorting two subset bases by their symmetric difference and its orientation identifies the latter operator with direct sums of I plus Kneser disjointness matrices. Each nonzero common-subset block has a nonzero diagonal. Their multiplicities already force exponent at least log2(3) in binomial(L,p), including sequences with varying p. The proof does not use modular diagonalizability.

Exterior powers have their usual lambda-operation interpretation on finite free modules, but the conclusion is a rank statement about explicit maps and block decompositions; it is not deduced from a K0 identity. The canonical coefficients are essential. No motivic realization, weight argument, or additional archive cote is asserted, and arbitrary contraction coefficients and the unrestricted crossing problem remain open.
