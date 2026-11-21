# Geometric cyclic towers and the remaining primitive-exponent supply question

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Result of the probe

No applicable bound on the rational characteristic-primary exponent of the new primitive factors was obtained. In particular, a bounded class-group result for a tower of constant fields cannot be used as such a bound for a growing geometric cyclic tower. This is a source-scope check and a reduction of the proposed approach, not a nonexistence theorem or a new closed row.

For a geometric cyclic cover of degree n=ell^a in A47, an exponent estimate

    M_n < (sqrt(n)+1)/2

would suffice in genus two and characteristic two. A uniform bound on M_n would therefore be useful. No such estimate follows from the results checked below.

## The fixed-field obstruction to an abelian Galois tower

Fix a finite field k, a curve C/k and P in C(k). Every constant, geometrically connected abelian etale P-split cover is a quotient of the Lang cover attached to the finite group J_C(k), by the Abel--Jacobi abelian-cover correspondence and the prescribed-point splitting. Hence the degrees of such covers divide |J_C(k)|. There is no unbounded tower of this kind over one fixed field. Equivalently, in unramified abelian class field theory the rational splitting condition removes the degree/constant-field direction and leaves the finite degree-zero class group.

An unbounded geometric cyclic ell-power system over fixed k must therefore use nonconstant deck action or otherwise leave this class of covers. Its individual covers can be geometrically cyclic without being Galois as function-field extensions over k. If an ell-adic Frobenius eigenline constructs such a system, constantization adds an arithmetic action on the geometric cyclic group; the normal closures are semidirect extensions. After removing a finite prime-to-ell part, the natural infinite group is generally Z_ell semidirect Z_ell, with nontrivial Frobenius action, rather than the abelian Z_ell required in the cited arithmetic theorem. This paragraph describes the proposed eigenline construction conditionally; it does not assert that every curve has such a rank-one quotient over its original field.

## Exact primary literature scope

Andrea Bandini and Ignazio Longhi, *The algebra Z_l[[Z_p^d]] and applications to Iwasawa theory*, arXiv2312.04666v3, 28 May2025:
https://arxiv.org/pdf/2312.04666

Theorem1.2 treats abelian Galois Z_p^d extensions of global fields. Its weighted formulas have unspecified nonnegative coefficients and supply no upper bound. Section7 assumes the field characteristic equals the tower prime p. Theorem7.12 identifies characteristic ideals with special-value ideals under splitting and primitive-root/non-Wieferich hypotheses; it does not assert those ideals are units. Corollary7.14 and the following boundedness statement concern the arithmetic, constant-field Z_p extension. Remark7.15 extends that constant-field result to any positive characteristic. The introduction explicitly leaves extension of the methods to nonabelian towers as a possible direction.

I directly read the above statements, the complete proof of Theorem7.12, the setup of Section7, Corollary7.14 and Remark7.15. Retrieval references: turn585225282view0, turn530038529view0, turn530038529view1, turn530038529view2. Earlier references retained in the session are turn620220067view0 and turn599051562view0--2. I did not verify the entire paper's proofs and do not claim that the search is exhaustive.

The notation in this source differs from the main problem: its p is the tower prime, while its l is the class-group prime. For the proposed application the latter would be the curve's characteristic. The source's constant-field specialization and its abelian Galois hypothesis must both be checked; neither can be silently transferred to a nonconstant-deck geometric tower.

## Remaining precise gate

One would still need a theorem controlling the characteristic-primary valuations, or exponents, of the actual primitive conductor factors in a suitable varying pointed geometric cover. An equality between a characteristic ideal and an L-value ideal merely rewrites that question unless a unit or quantitative valuation estimate is proved. Number-field GRH and positive Artin-prime density do not supply that estimate in the checked argument. The finite Fourier criterion of A49 gives a different exact sufficient test for a quotient already present over a chosen finite field; it does not provide the missing tower estimate.
