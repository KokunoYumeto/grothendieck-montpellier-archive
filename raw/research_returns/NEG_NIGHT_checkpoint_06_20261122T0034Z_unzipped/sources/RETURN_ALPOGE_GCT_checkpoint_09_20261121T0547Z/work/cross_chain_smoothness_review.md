# Independent whole-proof review: P-F24

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Actual proof and primary-source review completed 2026-11-21T00:56:52Z.
Draft: `work/positivity_chain_smoothness.tex`.

## Outcome: PASS, with one source pagination refinement

I read the entire proof and reconstructed the full automorphism and tangent computations. The theorem is valid for its stated range `n>=4`. It proves one smooth one-dimensional fixed component; it does not establish maximality among all fixed components or noncancellation of the global Hilbert-series pole.

### Full projective stabilizer

I recomputed half the Hessian and its tridiagonal entries. An unreduced tridiagonal block of length `l` has kernel dimension at most one; summing over blocks bounds the rank below by the number of nonzero off-diagonal coordinates. Thus rank at most two leaves at most two such coordinates. Each case in the draft is valid, including both potentially delicate boundary cases:

- For two adjacent nonzero coordinates at indices `1,2`, the length-three block has determinant `-x_2^3` when `n>=5`. At `n=4`, the additional `x_4` changes that determinant but supplies the disjoint nonzero singleton if `x_4!=0`, so the rank bound still excludes it.
- For the last nonzero off-diagonal coordinate, the separate singleton has rank one and the final two-by-two block has determinant `3b^2-a^2`; rank at most two gives precisely the two displayed points. With no off-diagonal coordinates one gets the third collinear point `[e_n]`.

The resulting four-point locus has a unique collinear triple, so every projective linear automorphism fixes `[e_1]`. Comparing powers of `x_1` forces the first two coordinate forms to be scalar multiples of `x_1,x_2`, and removes the possible additional term in the first coordinate. The induction is valid. In the base case, the coefficient of `y` is `v A^2+2u AB+3v B^2`; independence of `A,B` forces `u=v=0`, and the next comparisons force the remaining forms diagonal.

I recomputed the diagonal recursion, the projective group of order `2^(n-1)`, the exact-form group of order `3*2^(n-1)`, and its determinant exponent `S=(1-(-2)^n)/3`. Since `S` is odd and congruent to `n mod 3`, the determinant-one subgroup has order `gcd(n,3)` and is exactly the ineffective scalar subgroup. No unexamined nondiagnonal automorphisms remain.

### Quotient smoothness and fixed dimension

Smooth hypersurface stability gives a closed nonzero affine orbit. Killing the ineffective scalar kernel produces a reductive group with trivial stabilizer at the chain. Luna's slice theorem then gives a smooth quotient and the asserted tangent exact sequence. The diagonal matrix `A` normalizes the acting special linear group, fixes the chain form, and induces a generator of the grading `mu_M` action on the quotient: the exponent `3S/g` is odd, hence coprime to `M`.

The degree-three fixed monomials are exactly the chain monomials and the final cube. Distinct nonzero variable weights have distinct 2-adic valuations; in any zero sum of three weights the least valuation must occur twice, forcing the next chain weight. Three identical nonzero weights cannot sum to zero. Therefore the fixed cubic space has dimension `n`. The distinct eigenvalues on the underlying space give `n-1` fixed vectors in the adjoint special linear representation. Exactness of finite-group invariants yields fixed quotient tangent dimension one.

The formal averaging argument makes the fixed scheme smooth near the quotient point. The nonvanishing discriminant gives a one-dimensional grading orbit. Its irreducible closure must equal the unique one-dimensional fixed component through that smooth point. The proof correctly makes no statement about other components.

## Primary-source checks actually performed

- Huybrechts, *The geometry of cubic hypersurfaces*, Chapter 3, Exercise 1.4 p.149 and Corollary 1.6 pp.149–150. URL <https://www.math.uni-bonn.de/people/huybrech/Notes.pdf>. Direct author-URL attempts timed out, then I opened root's retrieved source and read the exact statements and proof at own refs `turn831468172view0` and `turn831468172view1`. Exercise 1.4 explicitly converts stability to properness of the affine orbit map, so the cited affine closed-orbit conclusion is supported.
- Luna, *Slices étales*, Section III.1, Théorème du slice étale p.97; Remarque 1° pp.97–98; the preceding equivariant smooth-local-coordinate lemma is p.96. URL <https://www.numdam.org/item/10.24033/msmf.110.pdf>. Own fresh refs `turn212759462view3` and `turn666731567view1`. The theorem and smooth-point refinement give exactly the quotient comparison needed. I sent root the pagination correction: use p.97 and pp.97–98, or encompassing pp.96–98, rather than pp.96–97 alone.
- Zheng, *On abelian automorphism groups of hypersurfaces*, arXiv:2004.09008v3, Section 3 definition of `G_F` p.4 and Lemma 3.2 p.5. URL <https://arxiv.org/pdf/2004.09008>. Own refs `turn831468172view2` and `turn666731567view2`. The group `G_F` is explicitly the diagonal subgroup, so the source is not overstated as an existing full-group theorem. The draft's Hessian proof supplies the needed full-group assertion.

No edits were made to root's theorem file. No historical-priority claim is made for the full-group argument.
