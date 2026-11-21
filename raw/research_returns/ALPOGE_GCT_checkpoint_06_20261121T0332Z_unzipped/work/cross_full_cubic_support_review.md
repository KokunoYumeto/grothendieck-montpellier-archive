# Independent whole-proof review: P-F30

Reviewer: GPT-6 Astra Pro, inherited/undisclosed effort, `/root/bridges`.
Completed: 2026-11-21 01:33:59 UTC.
File read in full: `positivity_full_cubic_support.tex`.
Outcome: **PASS**. This is an actual independent reconstruction of the complete proof, not a review request or a finite-computation check.

## Reconstructed argument

The character of the support lattice sends the all-ones vector to the determinant of the diagonal stabilizer. For a rational support basis K, the solution of Kz=1 is unique, even when the support rank is less than n. Any nonzero maximal minor determines that solution by Cramer's rule. Its determinant is divisible by the common denominator of z, so its two-part bounds the determinant character's order. Full rank is never silently substituted for rational-span membership.

The graph columns split into full-rank components and components of rank one less than their vertex counts. Isolated vertices are included. A full component admits a tree-plus-one-column basis; the loop and cycle calculations give valuation at most v-1. A deficient component's tree cofactors are a common power of two times signed powers of minus two. Their maximal exponent is bounded by b=v-1-e. Equality forces a unique top-height vertex: the corresponding deleted-row minor is the product of v-1 factors all equal to two, so all heights decrease away from that root.

I checked the three normalized subset-sum bounds, including the potentially delicate three-vertex case containing the top vertex. A top entry of 1 is unique; every magnitude-1/2 entry is negative; all others have magnitude at most 1/4. Therefore the bounds 1, 5/4, 3/2 are valid for one, two, and three distinct vertices. No assumption of distinct numerical heights is needed.

Extending the graph basis by q independent triple columns and pairing them with the deficient-component cofactor vectors gives a rank-q compressed matrix. This follows because the pairing map has exactly the rational graph-column span as its kernel. Selecting a nonzero q-row minor then specifies an actual maximal minor of the original support matrix: retain all rows in selected deficient components and all full components; delete a height-zero row in each unselected deficient component.

The displayed determinant factorization (P-F30k) is valid with full components present. Rational column elimination in a full component or a square retained tree block does not affect other components, because its graph columns are supported only there. Expansion of the remaining tall tree blocks produces their signed cofactor pairings with the triple columns. This yields precisely the product of full-component determinants, all deficient-component common cofactor powers, and the compressed determinant. An integral unimodular change of basis is not being assumed.

After the specified row scaling, every compressed triple column has Euclidean norm at most sqrt(3). The partitions of its three distinct support vertices into selected components are 1+1+1, 2+1, or 3, giving squared norms at most 3, 41/16, and 9/4; omitted vertices only leave smaller cases. Hadamard's bound therefore applies to the exact selected original minor through the factorization.

For q<c, or for q=c with a full component, the resulting valuation is strictly less than n-f-c+q, which is at most n-1. Its integrality gives at most n-2. In the remaining q=c>0, f=0 case the original support matrix is square and every column sums to three. Its determinant is divisible by the odd number three. Since the factored tree determinants are powers of two, the compressed determinant retains that factor. Dividing its absolute-value estimate by three gives two-part strictly below 2^(n-1). All positive-q cases are thus strictly below the claimed extremal order.

For q=0, P-F27 applies to the graph subform because its span already contains the all-ones vector. Its equality case gives the chain and its eigenvalue list. That list permits no additional cubic monomials, so there are no hidden triple columns in the complete support. The chain relations force the lift itself to have order M once its determinant has order M. The coefficient normalization, smoothness, and attainment statements follow as stated.

Finally, a nonzero invariant evaluation produces a supported coefficient monomial of constant diagonal-torus weight. This expresses the all-ones vector as a nonnegative rational combination of support exponents. Thus the rational-span assumption does hold for every semistable cubic in every eigenbasis. I found no unproved strengthening of semistability, no exact-order assumption on the lift, and no omitted rank case.

## Scope

This proof closes the full mixed-support case. Its application to fixed quotient points still uses the separately proved finite-lift construction and the separately proved generic-smooth fixed-component pole lemma. The theorem does not equate an arbitrary lift order with the determinant order. No literature priority claim is part of this review.
