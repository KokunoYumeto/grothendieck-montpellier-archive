# Surface-only follow-up to the first threefold pairing

Recorded during the 19 November 2026 checkpoint-08 interval by /root/part_c.
The target-only positivity proposition is already proved and integrated. The further implication investigated here remains unproved. This note records the exact obstruction rather than presenting the same primitive-radical criterion as new progress.

## The attempt using an ample surface and Tate surjectivity

Let V be a smooth projective threefold over the finite residue field, let j:T→V be a smooth ample surface of class mL, and let S be the double-intersection surface target. The maps on geometric ℓ-adic cohomology satisfy

$$
j_*j^*=mL:H^2(V)\longrightarrow H^4(V)(1).
$$

Hard Lefschetz therefore always gives a Galois-equivariant retraction

$$
r_\ell=m^{-1}L^{-1}j_*:H^2(T)\longrightarrow H^2(V).
$$

This does not require the algebraicity of L⁻¹. Thus the Galois map

$$
g_\ell=\rho\,r_\ell:H^2(T)\longrightarrow H^2(S)
$$

has the same image as the restriction map ρ.

The codimension-two Tate conjecture on T×S would realize gℓ as a class in the **Qℓ-span** of rational algebraic correspondences between T and S. This statement is weaker than the existence of one rational algebraic correspondence with precisely the required image, and that distinction blocks the attempted application of the positive-adjoint argument.

Indeed, the target-only proof uses a Q-algebra of correspondences and the real positivity of its rational adjoint trace. It proves nondegeneracy for images of rational algebraic projectors. It does not assert nondegeneracy for every Qℓ-linear projector in the scalar-extended algebra. The latter statement is false even as linear algebra: the already retained Q5 certificate gives the isotropic line Q5(1,i), where i²=−1, in the negative-definite rational plane. Therefore no new geometric counterexample is claimed, but the proposed scalar-extension shortcut is invalid.

## Why a rational linear-system argument still needs an input

Choose rational correspondences Γ₁,…,Γₘ whose Qℓ-span contains gℓ. One can ask for coefficients cᵢ solving

$$
\left(\sum_i c_i\Gamma_i\right)j^*=\rho.
$$

There is a Qℓ-solution from the construction of gℓ. To deduce a Q-solution by ordinary rational linear algebra, one needs the rational span of the algebraic classes Γᵢj* and ρ to extend faithfully to its Qℓ realization. That injectivity is not a consequence merely of the finite Qℓ dimension of the cohomology group. Mixed homological equals numerical equivalence supplies it through a nondegenerate rational intersection pairing; using that input returns to the mixed product hypothesis of the proved proposition.

Knowing that all these rational maps have coefficient-independent ranks does not formally supply this scalar-extension injectivity. A rational vector space can embed in a Qℓ space while acquiring new linear relations after scalar extension. In a correspondence algebra such invisible directions may occur in its homologically nonzero but numerically trivial radical. The positive and semisimple target algebra does not by itself eliminate a mixed radical map from an unrestricted source; the right-ideal proof explicitly uses mixed trace nondegeneracy at that step.

Thus the present argument does not deduce the required nondegeneracy from surface-product Tate surjectivity alone, from the known standard conjectures on individual surfaces, or from a supplied Galois-theoretic Hard-Lefschetz inverse. An algebraic inverse, a rational correspondence extension, or an appropriate mixed trace condition would repair the identified step, but none has been proved here for an arbitrary threefold component.

## A second tempting numerical-category shortcut

Over a finite field the Künneth projectors are algebraic, and numerical motives form a semisimple category. These facts do not permit us to replace the actual homological image of j* or ρ by its numerical image. A numerically trivial mixed correspondence can still be homologically nonzero in the absence of D. An idempotent onto the numerical image therefore need not have the same realized image as the original map. The target-only lemma deliberately includes the mixed trace hypothesis precisely to rule out that residual map.

Nor can one infer an algebraic inverse to L merely because the cohomological L is an isomorphism. The desired inverse is the Lefschetz standard conjecture in degree two; using it without an algebraic construction would circularly assume the extra condition that the surface-only attempt was intended to remove.

## Rational Frobenius data do not repair the descent step

We also tested whether the actual finite-field origin of the maps could be
replaced formally by rational Frobenius characteristic polynomials. The
retained exact certificate already has Frobenius \(F=2I_2\), preserves the
isotropic line \(R=\mathbf Q_5(1,i)\), and scales the rational form
\(-x^2-y^2\) by \(4\). The characteristic polynomials on the ambient space
and on \(R\) are respectively \((t-2)^2\) and \(t-2\); both have rational
coefficients and all their roots have the required weight-two absolute
value over \(\mathbf F_2\). Nevertheless \(R\) is not obtained by scalar
extension of a rational line and its restricted form is zero.

Thus even rational Frobenius data on the image itself do not formally turn
that image into a rational subspace when Frobenius has multiplicities. This
does not refute a statement about images of actual geometric restriction
maps: the certificate supplies no such geometry. It identifies why a
Frobenius-polynomial argument alone would not remove the mixed correspondence
or image-projector requirement. The existing exact code
\(\texttt{check\_c4\_isotropic\_ladic\_line.py}\) checks the form, the
\(\mathbf Q_5\) embedding, Frobenius stability, and similitude factor; the
two characteristic polynomials follow directly from the scalar action.

## Current-source check

A fresh primary-focused search used the queries “weight monodromy threefold 2026 proof conjecture” with a 90-day recency setting and “standard conjecture degree 2 threefold surfaces Lefschetz” with a one-year recency setting. The current primary weight–monodromy result returned was the already checked Ito–Zou hyper-Kähler theorem; the other explicit threefold result was Ito's 2003/2004 theorem under its stated Picard-number condition. Search-engine freshness labels on the latter were not mistaken for a new theorem. Neither supplies the unrestricted threefold pairing or an algebraic degree-two inverse for arbitrary threefold components.

This is a bounded account of these searches, not a claim that every possible source has been excluded. The existing exact Saito sections 4.1–4.3 remain the relevant source for the product-positivity and mixed-image-projector requirements.

A second search recorded at 08:33 UTC used the primary-focused phrases
“Hodge standard conjecture surfaces 2026”, “standard conjectures threefold
2026”, and “weight-monodromy surfaces positivity 2026”. We opened the
publisher record and the original arXiv version of Hu, Truong, and Xie,
*Tate's question, Standard conjecture D, semisimplicity and Dynamical degree
comparison conjecture* (published 2026; arXiv:2503.09432v1). Its Theorem 1.1
on author p. 5 explicitly assumes D on the middle cohomology of \(X\times X\).
The unconditional Theorem 1.5 on p. 7 concerns dynamical degrees of finite
correspondences and endomorphisms, including the absolute values of
eigenvalues for polarized endomorphisms. These statements do not supply
the arbitrary geometric restriction-image pairing needed here. We read
the abstract, introduction, and these theorem statements for scope; no
full-proof audit or use of these results as a theorem input is claimed.

Primary sources:
https://arxiv.org/pdf/2503.09432 and
https://actamath.cjoe.ac.cn/Jwk_sxxb_en/EN/10.1007/s10114-026-5249-8.
The retrieved primary references were turn865687446view0 and
turn684599316search1. The paper was already submitted in March 2025;
its October 2026 publication date does not make its conditional hypotheses
new unconditional results.

## The central-Frobenius check

There is a direct conditional observation, independently checked by Part D,
which does not repair the mixed-image problem. If D holds in codimension
\(\dim Z\) on \(Z\times Z\) over a finite field, it identifies
\(\operatorname{End}_{\mathrm{hom}}(hZ)\) with the finite-dimensional
semisimple rational algebra \(\operatorname{End}_{\mathrm{num}}(hZ)\)
of Jannsen's theorem. Frobenius is central over its finite field of
definition. The centre is a product of number fields, so the Frobenius
element has separable minimal polynomial, and the same polynomial
annihilates its cohomological action. That action is therefore semisimple.
If D is given over the algebraic closure, choose a finite field defining a
rational basis of the numerical endomorphism algebra; a power of
Frobenius is then central. Semisimplicity of that nonzero power implies
semisimplicity of Frobenius in characteristic zero. This argument uses the
opened full Jannsen Theorem 1, not an unverified implication from the new
dynamical paper.

This observation only explains what a self-product D hypothesis already
provides. It proves neither the mixed D required for the restriction map
nor positivity of its primitive image. The scalar Frobenius in the exact
\(\mathbf Q_5\) certificate is already semisimple. Thus adding that
property to the unsuccessful rational-polynomial argument does not remove
the stated obstruction.

