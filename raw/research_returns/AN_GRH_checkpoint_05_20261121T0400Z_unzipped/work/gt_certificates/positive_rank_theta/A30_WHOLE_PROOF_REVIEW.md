# Independent whole-proof review: A30 genus-three pointing counterexample

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source: `work/effective_galois/A30_GENUS_THREE_POINTING_COUNTEREXAMPLE.tex`.
Final reviewed hash after equation-tag correction: `c2dc1b108ad00c3cfd8613787a0fb394a8d7c2819e9d70de8f342da19c923026`.

## Outcome

PASS. The entire proof and its final double-cover discussion were read, including the individual-character calculation. No mathematical gap was found. A collision between A30's original PC equation tags and A29's tags was reported; A30 now uses DC.1 through DC.13, and that narrow correction was checked. No final paper files were edited by this reviewer.

## Curve, quotient and rational fibres

The two poles of order three at t=0,1 give genus three and 2-rank one by the already reopened primary Pries–Zhu Lemma2.6. The two points at infinity are unramified and rational, so the chosen P is not Weierstrass, whereas W at t=0 is. The genus-three canonical class is twice the hyperelliptic degree-two class, hence4W.

The map x=1/(t^2+t), y=z to the elliptic curve y^2+y=x^3 is a separable double extension t^2+t=1/x. The latter function has exactly two simple poles, at Q=(0,0) and -Q=(0,1). The images f(P)=Q and f(W)=O are correct.

The nine rational points of E/F4 are checked directly: every nonzero x has x^3=1, and both0 and1 have absolute trace zero from F4 to F2. Each x therefore has two y-values. The tangent calculation is exact: with x=a+v, the tangent substitution has cubic intersection v^3=0 because a^4=a. Thus every nonzero rational point is killed by3, and E(F4) is C3 squared. The count yields numerator1+4T+4T^2 and reduction1.

For a quotient a:E(F4)->C3 with a(Q)=1, the translated Lang isogeny psi+Q has split fibre aboveQ and nontrivial translations1 and-1 at-Q andO. Its branch pullback along D/E therefore gives closed branch-point degrees1,1,1,3 onY. The degree2 and degree3 function-field extensions are geometrically linearly disjoint, so D' is geometrically connected. It is an etale cubic cover of D, with genus7 and split fibre aboveP. The defining rational character is b=a composed with f_*, and b(W-P)=a(-Q)=-1 proves both detection and surjectivity.

## Exact Euler-factor computation

For a double cover in characteristic two, the two unramified splitting types have identical reduced Euler factor (1-T^(2d))^-1. A ramified point of degree d changes that factor by multiplication by1-T^d. This proves the displayed formal-series identity. Since the constant field is even, passing to zeta numerators gives the denominator1-T, exactly as written.

Applying it to the two rational branch points onE gives H_D mod2=1-T. Applying it to the branch degrees1,1,1,3 on the isogenous elliptic curveY gives H_D' mod2=(1-T)^2(1-T^3). The norm/pullback isogeny for D'/D gives H_B mod2=(1-T)(1-T^3), which vanishes at1. Thus the actual relative class number is even. As a consistency check derived from the formulas, the reduced degrees give f_D=1, f_D'=5 and f_B=4; these agree with the double-cover branch counts and the dimensions. No numerical computation of a large Jacobian was claimed or needed.

The individual-character calculation also checks. On the elliptic base the nontrivial unramified character polynomial is1. After pullback to the double cover, the unramified Euler factors become the square-character polynomial evaluated atT^2, and the two branch corrections are1-T and1-zeta T. Thus the reduced degree-four character polynomial is precisely (1-T)(1-zeta T); the inverse character has zeta squared. Their product agrees with H_B above. The quadratic term is retained and cannot be discarded using the genus-two truncation.

## The proposed etale-double-cover transfer

The two ramification supports make the simple-pole and triple-pole Artin–Schreier classes independent. The diagonal subgroup meets neither inertia subgroup, so the associated double cover of the genus-two curve is etale. Its genus is three. The stated hyperelliptic involution is the translation of the triple-pole coordinate; it swaps the two lifts over the simple pole and fixes the two over the triple pole. Consequently only the first pair becomes non-Weierstrass. The final model is exactly the specialization f1=1/x, f3=x^3.

Both transfer limitations are valid. A geometric degree-two quotient is absent from the pro-prime-to-two fundamental group, so the original collision hypothesis does not give the required lifts. Also the branch-point difference downstairs has exact order2, and the norm of the upstairs difference is that class; every pulled-back odd character kills it. An upstairs detecting character is therefore not obtained by pulling back the desired character from downstairs. Independently, the explicit genus-three character calculation disproves the proposed genus-free symmetry rule.

This is a full mathematical reading, not a formal proof-assistant check. It does not assess unprovided higher-genus generalizations.

## Final scope clarification: narrow recheck

Final source SHA256: `cf643b8dbc2b236ff64cebcb5bd27ba5f7b18cb320b3c5aa91a8bb82b727371e`.
The first paragraph now states exactly which proposed extension fails: the claim that every detecting quotient has odd relative class number. It explicitly leaves open other quotients or higher powers for the same pointed genus-three curve. The entire changed paragraph was read; PASS. No mathematical proof changed. This reviewer has not independently rerun the author's subsequently added finite checker, so no such computation is credited here.
