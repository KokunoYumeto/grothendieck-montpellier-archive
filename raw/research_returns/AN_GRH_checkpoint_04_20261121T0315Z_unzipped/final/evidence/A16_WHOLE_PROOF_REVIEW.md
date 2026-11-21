# Independent whole-proof review of A16

**Result: PASS.** Reviewed the complete `final/proof_sources/composite_theta_example.tex`, including the prime-degree-five comparison. The reviewed file has SHA256 `b7ca247121441bf3e46229602ee6b12d8dc16c6d5766ce0e838f2d4bc8237845`. No changes were made under `final/`.

## Algebraic curve and theta characteristic

The reciprocal substitution gives the asserted Artin–Schreier equation with poles of orders three and one. The genus is two and the geometric 2-rank is one. At the unique point P above X=infinity, the valuations of X and Y are −2 and −5. The locally exact regular differential dX/X² has divisor 2P. It supplies the section of B¹ whose divisor is P on the one-fold Frobenius twist; therefore B¹=O(P^(1)), and the relevant theta support is C^(1)−P^(1). Retaining the twist is necessary because the coefficient z+1 is in F8, not F2.

## Principal-divisor certificate and exact order

The displayed vectors are the same polynomials used by the independent symbolic checker. I read the full checker, copied it into `work/gt_certificates/positive_rank_theta/A16_independent_review/`, and ran that copy. It passed the norm identity, the evaluations at R and its conjugate, the pole degrees, the field irreducibility, and the unit-group computation. This run writes only under `work/`; the original final certificate is unchanged.

Because X(R)=z² is nonzero, the two points over this coordinate are unramified and distinct. The norm identity has its only finite root at z², and the conjugate value is z≠0, so all fifteen finite zeros occur at R. The term X⁵Y is the unique highest-pole term, of order fifteen. Thus div(F)=15(R−P).

The possible proper orders are 1,3,5. Order one contradicts positive genus. Since 2P is canonical, Riemann–Roch gives l(3P)=l(2P)=2, so a function with unique pole of exact order three does not exist. A function with exact pole five can be scaled to Y+a₂X²+a₁X+a₀. Its norm has leading coefficient one and coefficient one at X. If its divisor is 5(R−P), its norm is (X+z²)⁵, whose X coefficient is z. This contradiction excludes order five. The class therefore has exact order fifteen.

## Cover, rational point, and geometric connectedness

For W¹⁵=F, all valuations are divisible by fifteen, so the normalization is etale in characteristic two. If F were a third or fifth power over the algebraic closure, respectively 5(R−P) or 3(R−P) would be principal. The exact-order proof excludes both possibilities, proving geometric connectedness.

With t=X²/Y, the leading term satisfies t¹⁵X⁵Y=(X⁵/Y²)⁷, whose residue is one, since the leading relation is Y²/X⁵=1. All other terms vanish after multiplication by t¹⁵. The local equation for tW consequently has the simple root one in the residue field, giving the claimed F8-rational point. F4096 contains F8 and all fifteenth roots of unity, so it supplies a constant cyclic deck group. The cover has genus 1+15=16.

## The full 2-rank computation

The primitive indices modulo fifteen have two doubling orbits, represented by ±1. The normalized theta class is literally M, since F_C^*(M^(1))=M² and 2·8=1 modulo fifteen. The theta point and its inverse give zero arrows on both primitive orbits, so the primitive factor has dimension eight and 2-rank zero.

The conductor-three factor has dimension two and is ordinary by A10, whose hypotheses hold because the base is nonordinary.

For conductor five, the norm-coefficient argument is valid for every geometric nonzero order-five theta point S−P: its X coordinate r must satisfy r⁴=1 and hence r=1. At X=1, the curve requires Y²+Y=z+1. The trace of z is zero (its minimal polynomial has no quadratic coefficient), while the trace of one from F8 is one. Thus this equation has no F8 solution. Every nonzero power M^(3i), i=1,2,3,4, is F8-rational. If one were on the Abel curve C−P, uniqueness in the Abel embedding would make the corresponding point of C rational as well, a contradiction. Twisting preserves this statement over F8. All four relevant character arrows are therefore nonzero maps of lines and are bijective. The conductor-five factor is ordinary of dimension four.

Consequently f_D=1+2+4+0=7. The whole new factor has rank six, although its primitive factor has rank zero. A15 applies to the latter alone on the rank-one base. This is exactly the extra geometric content of A15 and does not imply the absence of some different prime-power witness on the same curve.

## Prime-five comparison

For C5, direct expansion gives Norm(Y+X+1)=(X+1)⁵. The values at (1,0) and its conjugate are zero and one; the unique pole has order five. Nontriviality of R5−P5 gives exact order five. Its theta membership follows from the same locally exact differential. The reciprocal Artin–Schreier model has poles of orders three and one, so the curve again has genus two and 2-rank one. The divisor of X is 2(Q5−P5), because the unique point above X=0 is the branch point Q5. Thus P5 and Q5 have the same prime-to-two abelian Kummer class, while the separating degree-five cover detects their full point sections. The copied symbolic checker also passed this norm identity.

This is a mathematical and computational review, not machine-checked formal verification. I did not rerun or certify the full search over 784 models; the proof only requires the displayed certificate, and the final source labels the search as limited.
