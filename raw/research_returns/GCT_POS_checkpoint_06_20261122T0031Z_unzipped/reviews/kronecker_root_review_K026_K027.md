# Complete root review of K-026 and K-027

Reviewer: `/root`; model: GPT-6 Astra Pro; effort: not exposed; run: GCT_POS.
Date: 21 November 2026, completed 23:22 UTC.
Type: targeted check by reading both complete proofs and independently reconstructing their arguments.

**PASS, with the conditional scope retained.** Read every statement and proof in `branches/kronecker/CYCLIC_FIXED_COMPONENT_REDUCTION.tex` and `branches/kronecker/EXCEPTIONAL_LOCUS_REDUCTION.tex`. The inherited P-F23/P-F30/P-F60 proofs and their precise hypotheses were already read completely in this run and were rechecked at the new applications. The complete peer reviews of both findings were also read.

## K-026

The effective special-linear group is exactly the kernel of the determinant character on the quotient of GL_n cubed by the scalar kernel. At an effectively free nonzero closed orbit the full effective stabilizer injects into that character and is finite cyclic. Therefore its character-xi element is unique and has order M. Surjectivity of the M-power map on the central scalar torus supplies an honest order-M lift. Finite torsion conjugacy types, Chevalley constructibility on the stable effectively free locus, and irreducibility make one conjugacy type generic on each fixed component.

Cyclic stability makes the three spectra scalar translates of a common multiset. Division by three modulo the dyadic order gives a product-one scalar change to an identical matrix in all three factors. Its determinant has order M. Three-mode balancing folds to a nonnegative cubic-span expression for the all-ones vector, so the complete cubic support theorem applies, including arbitrary lift orders and deficient ranks. On the resulting tensor chain support the margin equations force every coefficient to occur and give independent incidence columns. The diagonal torus is consequently transitive on the nonzero coefficient choices. The component is the chain curve. Every other effectively free component has a cyclic orbit of size three and an S3 orbit of size three or six.

The moving tangent determinant is xi^(n^2), since the ambient tensor determinant has that value and each adjoint determinant is one. Conjugating the moving Euler product proves the displayed phase-line relation. It gives a common real line, not a common sign. Neither generic effective freeness nor three-adic integrality of other component densities follows from this argument.

## K-027

The moving homogeneous generators generate the fixed-scheme ideal: every monomial of total degree not divisible by M contains a moving generator. Their Koszul homology gives an integral graded coherent class supported on the fixed scheme, including its nilpotent structure. This avoids assuming that inverses of normal Euler classes already lie in an integral coherent Grothendieck group.

For a module whose support meets each higher colliding fixed locus only at the origin, the corresponding Koszul identity proves regularity at every root of order M times a positive power of three. Integral reduced cyclotomic denominators then imply integrality of every Laurent coefficient at the primitive-M root. All noncolliding factors are units at the chosen prime over three. Changing from t-xi to u=1-t^M preserves integrality: its linear coefficient is a unit, and the formal inverse is obtained recursively by division only by that unit.

The elementary coherent localization argument uses finitely many homogeneous generators, relations and morphisms. Clearing their denominators gives extensions; exactness errors are supported on the removed closed set. Extensions can be taken on a specified closed component. Thus the localization statement is about graded coherent G0, with support, and does not require a vector-bundle resolution on a singular quotient.

On the effectively free locus the quotient and its characteristic-zero finite-order fixed scheme are smooth. Distinct components do not meet there. After removing the explicitly defined exceptional set, K-026 leaves the chain and disjoint cyclic triples. Choosing extensions and their translates gives an integral chain class, triples with identical Hilbert series, and an exceptional class supported precisely as claimed. The three-adic unit moving-generator product may be divided after taking Hilbert series. The good triples have fully integral Laurent expansions and hence three-divisible principal parts. The chain has its actual simple coefficient, a three-adic unit; extensions differ only at the origin and cannot alter it.

It follows that exact cancellation requires an exceptional principal part whose simple coefficient is minus that unit modulo three, with every higher coefficient divisible by three. If the exceptional support is only the origin, this is impossible. The theorem does not establish that hypothesis in all dimensions, does not make the exceptional class canonical, and does not settle strict positivity or saturation indices.

No numerical replay is needed for these two general arguments. The earlier exact small-dimension and stabilizer certificates remain separately identified checks.
