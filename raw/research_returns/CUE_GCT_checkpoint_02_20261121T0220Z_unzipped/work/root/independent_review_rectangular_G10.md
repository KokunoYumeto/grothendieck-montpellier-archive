# Independent agent proof review of G-10

Reviewer: `/root/rectangular_bridge`, GPT-6 Astra Pro, inherited effort
(not exposed), run CUE_GCT-20261121, 2026-11-21.

## Scope and conclusion

I read the complete statement and proof of G-10 in
`work/root/findings.tex`. The proof passes within its stated scope.
I also opened Chardin's original paper and visually inspected the
central theorem on printed p.306. This is a whole-proof review of
G-10 using its cited background theorem, not an independent reproof
of Chardin's entire paper, and not a formal verification.

## Image-degree bound

The projectivized coefficient map is given by degree-n forms. Its
dominant constructible image contains a dense open subset of the
reduced irreducible target. A general complementary linear section
can be chosen to consist of Δ reduced points in that open subset.
Each point has a nonempty fiber in the domain of definition.

For the common zero locus of the pulled-back hyperplanes, any
irreducible component meeting the domain of definition maps to a
single point of this finite target section. Therefore different
target points require different irreducible components. A component
contained in the base locus cannot account for any of those fibers.
Repeated componentwise projective Bézout bounds the sum of degrees
of all irreducible components by n^s: when an intermediate component
is already contained in the next hypersurface, its degree is retained
and is still at most n times its preceding degree; otherwise the
usual hypersurface intersection bound applies. Passing to maximal
components or removing duplicates can only decrease this upper sum.
Thus Δ≤n^s. This argument does not require a generically finite map
from the entire high-dimensional parameter space.

## Chardin's hypothesis and dimension convention

Primary URL inspected:
https://www.numdam.org/article/BSMF_1989__117_3_305_0.pdf .
The theorem is unnumbered on printed p.306 (PDF page index2).
Web open reference `turn887889610view0`; screenshot inspected
`turn659904946view0`.

The theorem states H_I(ν)≤binom(ν+D,D) deg(I) for every ν∈N,
under the homogeneous equidimensional geometrically reduced
hypothesis, with D the projective dimension convention used in
the paper. Its proof's normalization x_0,…,x_D confirms that
convention. For the homogeneous prime ideal over C in G-10,
equidimensionality and geometric reducedness hold, and D=s.
Thus the displayed upper bound Δ binom(d+s,s) has the correct
dimension index. It is valid in every degree, without a
Cohen–Macaulay assumption or a hidden regularity threshold.

## Lower Hilbert bound and threshold

Linear Noether normalization of a standard graded domain over C
provides dim(X) algebraically independent degree-one elements.
Taking r_n+1 of them is legitimate because the dimension gap
gives dim(X)≥r_n+1. Their polynomial subalgebra injects degree
by degree, giving binom(d+r_n,r_n). The ratio to the determinant
binomial upper bound is exactly (d+r_n)/r_n.

At d=r_n(B_n−1)+1 this ratio is B_n+1/r_n, and it increases
with d. The strict inequality therefore holds for every integer
d at or above the stated threshold.

## Multiplicity conclusion and dependencies

The strict GL4-module dimension inequality forces at least one
positive multiplicity difference. The previous highest-weight
support/ideal argument identifies these projected multiplicities
with the full orbit-closure multiplicities for length at most4.
G-05 eliminates lengths at most3, leaving exactly4.

The same proof applies to every R-14 dimension-certified padded
pair, including the new R-16 range. It gives an effective degree
and a finite exhaustive search, but no specified highest weight
and no polynomial complexity claim. Those limitations are stated
correctly in G-10.

No correction was required.
