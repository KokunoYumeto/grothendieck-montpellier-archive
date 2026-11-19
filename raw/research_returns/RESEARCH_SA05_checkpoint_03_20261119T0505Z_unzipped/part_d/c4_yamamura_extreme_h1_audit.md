# Audit of Yamamura 2026, Proposition 1.7

Read the complete argument on p. 10 of the primary preprint
`part_c/sources/Yamamura2026.txt`, arXiv:2608.01089v1. The proposition
asserts the extreme degree-one weight-spectral-sequence isomorphism

N^(d−1): E₂^(−d+1,2d−1) → E₂^(d−1,1)

for strictly semistable X of dimension d≥2. The paper reduces this
to a kernel-to-cokernel map on H¹ of the curve strata and cites
Rapoport–Zink, Satz 2.13. Part C is separately opening that original
source; this note does not claim to have read it.

## Independent check of the reduced assertion

Suppress the harmless common Tate twists. Put

U=⊕_C H¹(C,Q_l),
R=image[⊕_S H¹(S,Q_l) → U],

where C runs through the curve strata, S through the surface strata,
and the map is the alternating restriction map. The pairing on U is
the direct sum of the cup-product pairings on the curves. The
alternating Gysin map is its adjoint under Poincaré duality. Thus the
source and target of Yamamura's reduced map are R^perp and U/R.

The image R is a polarized nondegenerate subspace. Indeed the
restriction map on H¹(−,Q_l(1)) is the Tate-module realization of
the same signed restriction morphism

        ∏_S Pic⁰_red(S) → ∏_C Pic⁰(C).

Its image is an abelian subvariety B of the product of the curve
Jacobians. On rational Tate modules, the image of the morphism is
exactly V_l(B), since its kernel has a connected abelian part and a
finite group part. The product of the canonical principal
polarizations of the Jacobians restricts to a polarization on B.
The induced alternating pairing on V_l(B) is consequently
nondegenerate. The signs in the restriction morphism do not change
the positivity of the product polarization. This proves R∩R^perp=0.

It follows that R^perp→U/R is injective; source and target have the
same dimension, so it is an isomorphism. This is precisely the
asserted reduced map and verifies Proposition 1.7 independently of
the Rapoport–Zink reference once the displayed spectral-sequence
identifications have been made. Nonreduced Picard schemes in
characteristic p cause no problem, since Q_l Tate modules, l≠p,
only see Pic⁰_red.

## Consequence actually checked

Together with Proposition 1.5, the extreme H⁰-stratum argument,
this removes weights 2d and 2d−1 from ker N on H^d. Weak Lefschetz
and hard Lefschetz then give Proposition 1.8's bound

max(0,2i−2d) ≤ weights(H^i(Xbar,Q_l)^I) ≤ min(2i−2,2d−2)

for 2≤i≤2d−2. This is weaker than the expected upper bound i when
i≥3, and in middle degree three it still permits weight four.
The notation ker N as a literal direct sum of E₂ terms can be
read as a statement about its weight-graded pieces; no splitting
of the weight filtration is required for the bound.

## Subsequent original-source check and threefold equivalence

At approximately 05:03 UTC, independently opened the original author-hosted
Rapoport–Zink scan:
https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/UeberdielokaleZetafunktion.pdf.
Refs: `turn305760474view0` and the complete relevant text window
`turn359538442view0`, lines 666–749. Read Satz 2.10 and equation (2.11)
on pp. 40–41, Satz 2.12 on p. 41, and the whole Satz 2.13 proof on
pp. 41–43. The Picard-variety morphism and restriction of an ample
product polarization on p. 42 are exactly the argument above.
This subsequent check does not alter the earlier event's honest scope.

Read Part C's complete `c4_improved_lower_endpoint.tex`. Its
threefold equivalence is correct. For H³ of a projective strictly
semistable threefold, N³:Gr⁽W⁾₆→Gr⁽W⁾₀(−3) and
N²:Gr⁽W⁾₅→Gr⁽W⁾₁(−2) are already isomorphisms. Thus the only
possible weight above three in ker N is weight four. The generalized
Frobenius eigenspace decomposition makes the weight filtration strict
for N, so that this component is exactly
ker[N:Gr⁽W⁾₄→Gr⁽W⁾₂(−1)]. Poincaré duality pairs the two weight
spaces perfectly and gives equal dimensions. Vanishing of this kernel
is therefore equivalent to the remaining N-isomorphism, hence to
weight–monodromy for H³. This is an actual equivalence for the
specified threefold case, not merely a sufficient conjecture.

The same fragment's curve-selection argument and restriction/evaluation
injection also pass under the stated finite-type and excellence
hypotheses. The complete article title, checked on its first page, is
*Weights in étale cohomology over mixed-characteristic local fields
and applications to anabelian geometry*; the shortened wording with
“MLF’s” is the section heading, not the article title.
