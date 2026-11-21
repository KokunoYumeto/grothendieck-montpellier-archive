# Author proof reread and source audit: A29 prime-power canonical detection

Date: 2026-11-21.
Author/reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Complete source: `work/gt_certificates/positive_rank_theta/A29_PRIME_POWER_CANONICAL.tex`.
Final candidate SHA256: `feb70cad020af94c8d471e4c97741eaf68e8d28a8381c09da164c38df46bb6b7`.

## Result and check scope

PASS after an entire author reread of the six-step proof and a full check of the appended actual-curve strictness corollary. The original six-step version was independently whole-read and passed by root and row_audit; those independent reviewers maintain their own audit records. Row_audit subsequently passed the actual-curve appendix as a narrow delta check, and effective_galois independently whole-read and passed the final source hash above, including the appendix. Their own audit records retain those independent events. No proof assistant or numerical verification of the universal theorem is claimed.

The result holds for a genus-two curve over any finite field of characteristic p, a prescribed rational P, and an odd prime r different from p with even multiplicative order of p modulo r. It requires a nonzero r-primary component of kappa_P=[K-2P]. Its conclusion is a cyclic prime-power pointed cover whose top-step rational Prym has order prime to p, sufficient for the point-section separation conclusion. It does not assert geometric p-rank zero or that the whole new factor over the original base has rational order prime to p.

## Attribution and source scope

Recovered successor final A.26 already proves the prime canonical-class criterion in every characteristic; its entire statement and proof, together with A.25, were read. This source catch was immediately reported to root and row_audit, and A28 now explicitly presents the prime result as recovered/rechecked.

The complete recovered A1 B.1 and B.2 proofs were read: they supply the odd-deck collision endgame and the unramified character Euler-factor and relative class-number identities. The complete B.13 and B.14 claims/proofs were also read, including their distinction between prime quotients and primitive packets of higher cyclic powers. B.14's finite representation examples were read as source background; their code was not rerun or used to establish A29. The complete recovered successor A.44 statement/proof was read to distinguish its Weierstrass-point fixed-ring restriction from the nonzero canonical-class detector. None is attributed as a universal existence theorem.

The A12 Lang construction/connectedness proof and A11 prime-power deck endgame were reread. The retained A09 exact-order13 construction, its field of definition F16 and Weierstrass base point, and its rational-Jacobian-order-eight observation were reread for the two concrete scope statements.

## Mathematical checks

1. Finite abelian primary decomposition gives a surjection to some cyclic r^a factor that detects the nonzero primary class, even if that class belongs to rG. This is the actual weakening from the known prime detector.

2. Even order modulo r implies even order at every r^a; the cyclic unit group of an odd prime power has a unique element of order two. Therefore p raised to half its actual order is -1. No maximal order-lifting or non-Wieferich condition appears.

3. The Lang quotient is constant and etale and has a completely split fibre above the prescribed P. Its pullback is geometrically connected: a hypothetical nontrivial intermediate isogeny lifting the Abel map would admit a homomorphic section by the Jacobian universal property, contradicting multiplicativity of degree.

4. The genus-two L-polynomial is exactly 1+c1 T+q chi(b(kappa))T^2. In degree two the canonical line bundle has q+1 effective divisors while every other degree-two class has one. In higher degrees the character sum is zero by Riemann–Roch. The bijection R to its canonical complement gives c1(chi)=chi(b(kappa))c1(chi inverse). These calculations do not need a rational Weierstrass point.

5. Reduction modulo a prime over p preserves faithful odd-order characters. If a faithful L-value vanished, its reduced middle coefficient would be -1. Inversion is a p-power Frobenius conjugate, so the inverse coefficient is also -1. The Riemann–Roch identity then forces the faithful character to kill b(kappa), a contradiction.

6. In a cyclic r^a tower, characters nontrivial on its unique order-r deck subgroup are exactly the faithful characters. Cancelling the other Euler factors gives their product as #J_D(k)/#J_E(k)=#Prym(D/E)(k). The isogeny norm/pullback decomposition proves this is an integer; each factor is a p-unit, so its rational p-primary subgroup is zero.

7. For a collision class delta, (tau-1)delta lies in the top-step rational Prym and is p-primary, so it vanishes. The equality im(tau-1)=ker(Norm)^0 is proved directly using the divisibility of r-sum tau^i by tau-1 and surjectivity of multiplication by r. The resulting principal divisor has four distinct points and simple degree-two poles. It yields a separable hyperelliptic pencil. The free odd-prime deck element acts on that pencil and must fix a point of the curve over a fixed point on P1, a contradiction. This handles any genus-two base and needs no rank-one or non-bielliptic assumption.

## Actual-curve strictness append

A09 gives [R-W] of exact order13 over F16. Thus kappa_R=-2[R-W] has exact order13. A 13-division point exists over a finite extension, since multiplication by13 is finite etale and surjective. Over a field containing it, kappa_R lies in13J; it lies in rJ for every other odd prime by multiplication within its own order13 subgroup. Therefore every prime-level canonical detector fails there. The13-primary component is nevertheless nonzero, and ord_13(2)=12, so A29 yields a detecting13^a quotient with a>=2. The appendix explicitly does not claim that all actual prime-degree covers fail: the separate geometric13 witness remains available. No uncomputed field degree is asserted.

## Residual scope

In characteristic two with rational W, kappa_P=2[W-P], so only odd-primary components whose primes have even ord_r(2) are detected. Pure2-primary classes and classes supported on odd-order-doubling primes remain outside this construction. Their support does not change under constant extension, since the fixed class retains its exact order. In particular kappa=0 at a Weierstrass point. These are limits of the sufficient detector, not counterexamples to point separation or to actual cover existence. Odd etale covers change the genus, so the genus-two truncated L-polynomial cannot be silently reapplied on their total spaces.
