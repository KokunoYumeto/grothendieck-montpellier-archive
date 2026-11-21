# Independent review of P-F18 and P-F19

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-21 UTC.

## Review scope and outcome

I read the complete current versions of `positivity_dimension_bound.tex` and `positivity_cubic_counterexample.tex`, including their final scope paragraphs, and checked every proof step. Both pass. These are independent-agent **targeted whole-proof checks**, not formal verification certificates and not claims of historical novelty. The calculations below are the actual checks performed.

P-F18 supplies a finite envelope depending only on the inner dimension for ordinary general-linear plethysm. P-F19 proves that its optimal **canonical** modular-index envelope is not polynomially bounded. The canonical clause and the existence of an arbitrary positive rational Hilbert form must remain distinct. P-F19 does not by itself settle the weaker positive-form clause or PH2.

## P-F18: finite envelope

1. Subtracting the final part of the inner partition gives a determinant twist of a normalized partition with final part zero. The dimension and restriction to the special linear group are unchanged.
2. In the type-A Weyl dimension product, every factor is at least one and the factor attached to a simple root is `delta_i+1`; therefore every adjacent difference is at most `m-1`.
3. For any nonzero adjacent difference at position `i`, monotonicity in every difference compares the dimension with the fundamental weight at `i`. I independently telescoped the displayed product to `binomial(n,i)` and checked `binomial(n,i)>=n` for `1<=i<n`. Thus `n<=m` whenever `m>1`.
4. There are consequently only finitely many normalized pairs `(n,nu)` for fixed `m`. The count in the proof is an upper bound before imposing the dimension condition and is not used as a complexity bound.
5. Each such pair gives a fixed algebraic homomorphism `SL_n->SL_m`; it need not be injective. A basis change only conjugates it and induces isomorphic canonical ray algebras.
6. The central-balance equation is exactly `|pi|=|mu||lambda|`. If it fails, every positive-degree coefficient vanishes. If it holds, the general-linear and special-linear invariant subalgebras agree. The already checked P-F17 matrix-coefficient argument identifies the actual graded algebras, including determinant-only weights through their retained external grading. This justifies using the canonical index, not merely coefficient equality.
7. Taking a maximum of the finitely many fixed-homomorphism constants from P-F17 gives the asserted finite envelope uniformly over the determinant twist and both stretched weights.
8. For `m=1`, the representation is a determinant character, including `n=1`; the multiplicity sequence on positive integers is either constantly one or constantly zero. The specified canonical algebra and origin convention are correct.
9. The optimal envelopes exist because they are maxima of nonempty bounded subsets of the nonnegative integers. For `m>1`, the exact bounds `m^2<=h<=m^2+2m` yield both directions of each stated polynomial-growth equivalence. The positive form associated to a canonical h.s.o.p. is available by the Cohen--Macaulay input; no converse from an arbitrary positive form to a canonical h.s.o.p. is asserted.

The Weyl formula source was independently inspected earlier in this run: Borcherds--Haiman--Reshetikhin--Serganova--Johnson-Freyd, *Lectures in Lie Groups and Quantum Groups*, Part I, Theorem 6.1.1.30, printed pp. 102--103, and Example 6.1.1.31, printed p. 103, <https://math.berkeley.edu/~serganov/261/part1.pdf>. Own retrievals: `turn898211497view0` and `turn626532291view0`. This review reuses that checked source and rechecks the specialization algebraically; it does not claim a fresh scan inspection.

## P-F19: canonical cubic obstruction

### Canonical algebra and grading

The point space is `W*=Sym^3(V*)` while the coordinate ring is `Sym W`; no self-duality is assumed. The central subgroup of `SL_n` forces every nonzero ordinary invariant degree `D` to be divisible by `d0=n/gcd(n,3)`. At degree `d0*s`, general-linear action on the invariant subspace is precisely `det^(3s/g)`. Evaluation at compatible powers of a volume vector respects multiplication, so the canonical determinant multiplicity ring is the entire invariant ring with its grading divided by `d0`. It is not merely a numerical Hilbert-series match or an unexamined proper Veronese subring.

### Smooth chain and non-nullcone point

I checked the partial derivatives and the least-nonzero-coordinate argument. If the least nonzero coordinate is at `j<n`, the `j`th derivative forces the next coordinate to vanish, and the next derivative is then the nonzero square of that coordinate at `j`. If the least index is `n`, the last derivative is nonzero. This works also for `n=2`. Thus the discriminant is nonzero at the chain cubic. The proof uses only this nonvanishing, not a stronger stability assertion.

### Divisibility by the large power of two

I rederived both calculations in the written proof:

- In a surviving coefficient monomial, all variable exponents must be equal on the determinant-one torus. The recurrence `2a1=c`, `a_(i-1)+2ai=c`, `a_(n-1)+3an=c` has `c=3s/g` and `ai=c(2^i-(-1)^i)/(3*2^i)` for `i<n`. The factor `2^i-(-1)^i` is odd. Integrality for `i=n-1` therefore forces `2^(n-1)|c`, and the odd factor `3/g` can be removed. Nonzero evaluation guarantees a surviving monomial, so possible cancellation does not invalidate this necessity.
- For the diagonal stabilizer with successive exponents `1,-2,4,...`, each chain monomial is fixed and the final cubic is fixed for a root of order `3*2^(n-1)`. The sum of exponents is odd and congruent to `n` modulo three, so the determinant has order `3*2^(n-1)/g`. The semi-invariance character on coefficient polynomials then gives exactly the same divisibility of the stretch degree. I checked the inverse in the action on forms; its sign changes no order calculation.

### H.s.o.p. conclusion and its limit

For every homogeneous system of parameters the quotient is finite-dimensional and graded, so a power of the positive-degree discriminant lies in the parameter ideal. Evaluation at the chain cubic forces at least one parameter to be nonzero there. That parameter has positive degree divisible by `2^(n-1)`. This establishes the bound for **every** h.s.o.p., hence certainly for the lexicographically minimal one. The parameter `h=binomial(n+2,3)^2+n+1` is polynomial in `n`; the lower bound is exponential. This is enough to refute the specified canonical clause in ordinary plethysm with the single irreducible inner shape `(3)`.

The proof does not lower-bound poles of the scalar Hilbert series or the denominator weights of every positive presentation. Parameter nonvanishing at a point is additional algebraic information that can disappear from the Hilbert series. Accordingly the weaker positive-form clause and the positivity/saturation-index questions are explicitly left unresolved.

### Exact primary source audit

I freshly opened and read the primary papers, with the following exact results:

- McCrory--Shifrin--Varley, *Siegel modular forms generated by invariants of cubic hypersurfaces*, arXiv:alg-geom/9403005v3, **Section 3.1.2(i), printed p. 15**: the discriminant is an invariant of coefficient degree `n(k-1)^(n-1)` and vanishes exactly when the projective hypersurface is singular. URL: <https://arxiv.org/pdf/alg-geom/9403005>. Own exact retrieval: `turn839227287view2`, lines 1225--1237, PDF page 14. The preceding Proposition 3.1.1 and multiplicativity discussion also agree with the determinant-character normalization used here.
- Busé--Jouanolou, *A computational approach to the discriminant of homogeneous polynomials*, arXiv:1210.4697v1, **Definition 4.6 and Proposition 4.7(i), printed p. 40**: integral normalization by the resultant and homogeneous coefficient degree. URL: <https://arxiv.org/pdf/1210.4697>. Own exact retrieval: `turn839227287view0`, lines 3538--3556, PDF page 39.
- The same paper, **Proposition 4.13, printed pp. 42--43**: coordinate-change character `Disc(f circ phi)=det(phi)^(d(d-1)^(n-1))*Disc(f)`. Own exact retrieval: `turn839227287view1`, lines 3742--3756, PDF pages 41--42. Restriction to determinant one yields the required invariance.
- The same paper, **Example 4.12, printed p. 42**, explicitly contains the chain form, after reversing the variables and specializing its parameter to one, and attributes it to Demazure. Own exact retrieval: `turn839227287view1`, lines 3659--3666. The draft correctly acknowledges this and does not claim novelty for the forms or their stabilizers.

The canonical-ring locators in GCT VI were independently read during the P-F17 review: Section 4.1.1, printed p. 68, and Section 4.1.2, equation (4.5), printed p. 69, with the multiplication construction in equations (4.2)--(4.3), printed p. 67. P-F19 follows the detailed `T`-ring definition. Its scope discussion is consistent with the introductory `S`/detailed `T` notation discrepancy already recorded in P-F18.

## Related PLE-F8 clarification checked

I also read the added Cartan-evaluation paragraph in `positivity_actual_plethysm.tex`. The compatible highest vectors `v_s=x^(2s) tensor (x wedge y)^(5s)` have the required weights. The normalized highest-component injection sends `v_(s+t)` to `v_s tensor v_t`; composing intertwiners and ordinary symmetric multiplication evaluates to the product of their highest vectors. This proves the claimed graded-algebra compatibility with the canonical multiplication and passes review.

## Affine-slice warning sent to the team

An arbitrary central piecewise quasi-polynomial, even one globally quasi-polynomial on every ray, does not permit transfer of a large period on a fixed-target slice to a large simultaneous-stretch period. For example, for `M=2^a`, `F(x,y)=1+1_{y odd and M divides x}` has period at most two on every ray `(ku,kv)`, whereas `F(x,1)` has period `M`. The indicator is zero for even `k`; for odd `k`, divisibility by `M` depends only on `u`. This counterexample was supplied independently by `/root/complexity`; my prior example `1+sin(pi*x/2)sin(pi*y/2)` gives the same failure at period four. Neither example is asserted to be the Hilbert function of a domain branching algebra. Any successful transfer must use additional algebraic structure and cannot rely only on Fourier restrictions and quasi-polynomiality.
