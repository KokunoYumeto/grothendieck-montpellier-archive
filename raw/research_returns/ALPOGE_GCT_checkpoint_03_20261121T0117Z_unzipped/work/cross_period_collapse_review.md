# Independent whole-proof review of P-F21

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-21 UTC.

## Outcome

The complete proof in `positivity_period_collapse.tex` passes independent review. The example has fixed Krull dimension three, a positive Hilbert presentation with all denominator weights one, zero positivity and saturation indices, and unbounded canonical parameter degrees. The proof correctly restricts this conclusion to general graded domains and does not identify the example with an ordinary plethysm algebra.

## Actual checks

1. I checked the three primitive cone rays and their linear independence. The real ray coordinates of every lattice point are unique and nonnegative. Subtracting their floors gives the unique integral point in the half-open parallelepiped. Thus the asserted finite free module decomposition, finite generation, dimension and parameter degrees follow. Finite freeness over the polynomial subring implies Cohen--Macaulayness: after localization, a flat local map from a regular ring has zero-dimensional fibers, so the local dimensions and depths agree. In particular the displayed parameter sequence is regular.
2. I recomputed every numerator multiplicity. For fixed `y`, the allowed `x` values split at `D-y-1`. There are `D-y` contributions of degree `y+1` and `y` of degree `y+2`. The case `D=2` has an empty intermediate sum and is included. Collecting coefficients gives `(1+(D-2)t)(1+t+...+t^(D-1))`; the resulting coefficient polynomial is correct in every nonnegative degree.
3. The three integer half-space inequalities cut out exactly the cone. Dividing each normal by its coefficient gcd gives a primitive integer linear form. Its half-space semigroup algebra is a polynomial algebra over a Laurent polynomial algebra after an integral basis change and is integrally closed. Intersecting these algebras recovers the cone algebra by monomial supports. An element integral over the cone algebra is integral over each larger half-space algebra and therefore belongs to the intersection. This proves normality with no unsupported semigroup-normality shortcut.
4. The rational-singularity conclusion follows from the exact toric resolution and higher-direct-image statements in Danilov, checked below. It is applied in characteristic zero.
5. The functional `(D-1)s-Dy` is nonnegative on each ray and vanishes only on the third ray. Hence the off-ray monomials span an ideal. Primitivity of `(0,D-1,D)` makes its quotient a polynomial ring whose generator has degree `D`.
6. A homogeneous parameter ideal has finite-dimensional graded quotient. Thus some power of that surviving monomial belongs to it, forcing at least one parameter to map nontrivially to the degree-`D` polynomial quotient. Every such positive degree is a multiple of `D`. The existing tuple `(1,1,D)` is indeed the lexicographically minimal nondecreasing tuple: either an earlier entry is larger than one, or its first two entries are one and its final entry is at least `D`. This establishes the source's canonical index exactly, rather than merely its minimum possible maximum.
7. The quotient has a primitive `D`th pole, whereas the ring series has reduced denominator `(1-t)^3`. The short exact sequence with the off-ray ideal puts that cyclotomic factor in the universal denominator. There is no claim that it occurs in the ring denominator.
8. The map to the published triangle is an integral affine bijection, with linear determinant minus one; on the `s`th dilation its translation is `(Ds,0)`. It sends the three vertices to the stated source triangle. The attribution is correct.

## Primary-source audit and one locator correction

- V. I. Danilov, *The geometry of toric varieties*, Russian Mathematical Surveys **33:2** (1978), 97--154, **Section 8.2 and Proposition 8.5.1**, printed pp. 124--125. The first provides a regular toric subdivision; the second states the structure-sheaf direct-image equality and vanishing of all higher direct images for a subdivision. Primary PDF: <https://www.math.purdue.edu/~arapura/danilov.pdf>. Own exact retrieval: `turn122557666view1`, lines 1087--1132. The printed heading on p. 124 explicitly identifies toric singularities as rational.
- McAllister--Woods, *The Minimum Period of the Ehrhart Quasi-polynomial of a Rational Polytope*, arXiv:math/0310255, **Theorem 2.2 and proof**, printed **pp. 3--5**. The theorem is on p. 3, the triangle and polynomial formula appear on p. 4, and the counting proof concludes on p. 5. Primary PDF: <https://arxiv.org/pdf/math/0310255>. Own retrieval: `turn185110272view0`, lines 155--256. I sent the author this pagination correction from the draft's pp. 3--4; it does not affect the mathematical proof or attribution.

This is an independent-agent targeted whole-proof check, with direct primary-source reads. It is not a formal certificate or a novelty assertion. No mathematical correction was required.
