# An integral one-cover homology lift with explicit cusp obstruction

19 November 2026. Root work note for the E.2.22 map. This is a concrete test of the general profinite lifting theorem. It supplies no comparison on the entire cover tower.

## The actual cover and its integral module

Let F=<x,y> be the topological fundamental group of P1(C) minus {0,1,infinity}, based at a rational point, with positively oriented loops about 0 and1. Let G be its profinite completion. Send x to the generator c of C5 and y to1. The resulting geometric cover is the restriction of z->z^5, with punctures 0,infinity and the five fifth roots of1.

Its discrete subgroup K has the Schreier basis

    t=x^5, y_i=x^i y x^(-i)  (0<=i<=4).

Thus its actual affine integral homology is L=Z t direct-sum Z[C5] y_0. The deck action fixes t and sends y_i to y_(i+1), with indices modulo5. Conjugating y_4 by x gives t y_0 t^-1, which is y_0 after abelianization; this proves the last cyclic step. The seven actual peripheral classes are t, the five y_i, and -t-sum_i y_i.

Let R be the kernel in G. The finite-index subgroup comparison gives R^ab=L tensor Zhat. The extension

    1 -> R^ab -> G/[R,R] -> C5 -> 1

has class beta represented by t under the explicit cyclic-cohomology map H2(C5,R^ab)=(R^ab)^C5/Norm(R^ab): the chosen lift x has fifth power t. Its class therefore lies in the t-summand modulo5.

## The integral automorphism and the exact lift

Put

    u(c)=-2+c+3c^2+c^3-2c^4,
    v(c)=1+c-2c^2+3c^3-2c^4.

Their product is1 modulo c^5-1, and each has augmentation1. Define gamma(t)=t and gamma(y_i)=u(c)y_i. The inverse uses v. Both maps are integral, commute with the actual C5 action, and fix beta because they fix its representative t.

Bleher--Chinburg--Lubotzky, arXiv:2004.08860v3 (10June2021), Theorem2.1 and its proof on pp4--5, supplies an actual automorphism alpha of G inducing gamma on R^ab and the identity on C5. The source proof first constructs the automorphism of the extension by the equality gamma(beta)=beta, then applies its Gaschuetz lifting Corollary2.4. This is the precise source map used here.

The inclusion of K into F induces the integral map t->5x and y_i->y on abelianization. Augmentation1 gives pushforward composed with gamma equal to pushforward. Consequently alpha acts identically on G^ab: it fixes y and5x, and multiplication by5 is injective on Zhat^2.

## The actual peripheral obstruction

The first y-cusp class has image

    gamma(y_0)=-2y_0+y_1+3y_2+y_3-2y_4.

This is not any of the seven displayed peripheral vectors or their negatives, as comparison of its six integral coordinates proves. More generally, it is not a profinite-unit multiple of a peripheral vector: a y-cusp vector has only one nonzero y-coordinate; a 0- or infinity-cusp vector has a nonzero t-coordinate. The displayed image has zero t-coordinate and five nonzero y-coordinates in Zhat.

An automorphism preserving the actual peripheral inertia conjugacy classes and preserving R induces, on R^ab, unit multiples of the corresponding primitive cusp classes. Conjugations act trivially on abelianization. The computed image therefore proves that every lift alpha supplied above fails that peripheral condition. In particular it cannot be the geometric fundamental-group action of an absolute Galois element, which carries each cusp inertia group to the corresponding conjugate inertia group. The proof uses the actual cusp vectors and induced maps.

The cover compactifies to P1, whose first homology is zero. This example addresses the affine homology and peripheral step. The separate A5-cover construction being pursued by triangle has nonzero proper first homology and tests descent through the filling quotient directly. Neither example constructs an automorphism satisfying E.2.22 on all covers.

## Exact finite verification

`work/code_root/check_bass_unit_lift.py` checks the integral unit and inverse, circulant determinant1, actual deck equivariance, the fixed beta representative and infinity class, the displayed base abelianization map, and the failure to permute peripheral classes up to sign. The preceding coordinate argument also excludes arbitrary profinite-unit multiples. The source lifting and geometric maps are proved in the text above, rather than inferred from the finite matrix calculation.

Primary source opened in full through the original arXiv PDF: https://arxiv.org/pdf/2004.08860, v3, Theorem2.1 pp4--5, Lemma2.5 and Corollary2.4. Root independently read the complete proof. No faithfulness or discreteness theorem for Aut(F) is needed for the peripheral obstruction.
