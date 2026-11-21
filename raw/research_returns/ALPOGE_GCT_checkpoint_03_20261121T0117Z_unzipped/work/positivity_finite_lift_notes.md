# P-F26: finite lifts and the smooth fixed locus

Author/checker: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Theorem file: `work/positivity_finite_lift.tex`.

## What is now proved

For `M=2^(n-1)`, every nonzero `mu_M`-fixed quotient point of the canonical cubic invariant ray has a closed-orbit representative and an exact-form stabilizer matrix of finite two-power order whose determinant is primitive of order `M`. The order of the matrix itself is not claimed to equal `M` for singular representatives.

For every smooth representative, the matrix does have order `M`, its spectrum is the chain spectrum, and its cubic is linearly equivalent to the chain cubic. Thus the *entire* fixed scheme outside the discriminant boundary is the one smooth chain grading orbit. Every other irreducible fixed component lies in the discriminant boundary. This is stronger than merely checking smoothness at the previously known chain point.

## Complete proof structure and delicate points

The canonical grading has `GL_n` character `det^(3s/g)`, with `g=gcd(n,3)`. On cubic points the evaluation character is its inverse. Because `3/g` is odd, one can choose a primitive `M`th root `eta` with `eta^(-3/g)=zeta` and lift by an arbitrary matrix of determinant `eta`. This obtains primitive determinant directly; a scalar lift could unnecessarily introduce an odd factor. Closed-orbit uniqueness in the affine quotient then corrects that matrix by an `SL_n` element so that it fixes the representative exactly.

The semisimple part still fixes the cubic: on any semisimple eigenspace of eigenvalue different from one, the product with a commuting unipotent operator cannot have eigenvalue one. After diagonalization, project the finitely generated multiplicative group of eigenvalues to its finite two-primary torsion, killing a chosen free complement and odd torsion. The primitive determinant and every support-monomial relation are preserved. This produces the finite two-power lift without assuming that its entire stabilizer is finite.

If the cubic is smooth and a variable has a nontrivial two-power eigenvalue, the pure cube is forbidden. Its coordinate point is consequently on the hypersurface. Smoothness there forces a monomial `x_i^2*x_j`, whose second eigenvalue is the inverse square of the first. Starting from a maximal-order eigenvalue gives a sequence of orders `2^ell,...,2,1`, so there must be at least `ell+1` variables. Primitive determinant of order `2^(n-1)` forces equality. The distinct valuation spectrum allows only the chain monomials; smoothness forces all their coefficients nonzero; diagonal rescaling normalizes them all. The `GL_n` quotient action is the full grading action, since the odd determinant power map on `C*` is surjective.

P-F24 supplies local quotient smoothness and fixed-scheme smoothness along the chain orbit. The point classification therefore gives scheme-theoretic equality in the discriminant-open set, not merely equality of one orbit among possibly other smooth fixed points.

## Source audit and prior status

- Luna, *Slices étales*, Section I.1, printed p.84, gives uniqueness of a closed orbit in an affine reductive quotient fiber. URL <https://www.numdam.org/item/10.24033/msmf.110.pdf>. Direct source read in this run at `turn114409063view1`, lines95–100. P-F24 already verifies the later local slice theorem separately.
- Zheng, *On abelian automorphism groups of hypersurfaces*, arXiv:2004.09008v3, Theorem 4.8, printed pp.11–12, corroborates the known two-power order bound for smooth cubic hypersurfaces. Own exact retrieval `turn413119232view0` and `turn796664711view1`; URL <https://arxiv.org/pdf/2004.09008>. Its possible orders have two-part at most `2^(n-1)`. The projective and exact-form orders agree for two-power elements because the scalar exact-form kernel has order dividing three.
- Theorem 4.3 in the same source, p.8, states an abstract subgroup embedding into a diagonal group of a simple polynomial. It does not alone identify the original linear representation. I checked that scope explicitly at `turn796664711view1`. The theorem file uses a full elementary coordinate-point proof for the equality case and does not overstate that source.

No historical-priority claim is made for the order bound or chain realization. The purpose is to turn those ideas into a precisely verified statement about this actual canonical quotient and its fixed scheme.

## Remaining gate, with no overclaim

For a singular closed-orbit representative, exact-order lifting is equivalent to a section of the determinant extension over `mu_M`. A cyclic group of order `2M` mapping by squaring to one of order `M` shows that splitting is not automatic for abstract group extensions. That abstract example has **not** been realized here as a cubic stabilizer, so it is not a counterexample to exact lifting for singular cubic forms.

The outstanding weak-PH3 question is now concentrated on other fixed components and possible nonreduced structure in the discriminant boundary, their dimensions and generic singularities, and their contributions to the global Hilbert-series pole. The proof supplies neither uniqueness of the maximal-dimensional fixed component nor global noncancellation.

## Actual checks

At 2026-11-21T01:06:30Z I reread the complete theorem file and independently reconstructed all proof steps, including the character sign, finite-group projection, coordinate-point chain, equality classification, and the scheme-theoretic boundary conclusion. Root independently read the entire proof and reported PASS before this self-check was logged. `/root/plethysm` subsequently completed an independent whole-proof and fresh primary-source review and reported PASS; its actual event is recorded separately in `plethysm_checks.tsv`, including fresh Luna and Zheng retrievals. No requested-but-unperformed review is being counted.
