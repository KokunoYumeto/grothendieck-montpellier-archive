# A29 independent whole-proof review

- Date: 2026-11-21.
- Reader: GPT-6 Astra Pro, `/root/effective_galois`; effort not exposed.
- Source: `work/gt_certificates/positive_rank_theta/A29_PRIME_POWER_CANONICAL.tex`.
- Reviewed final SHA256: `feb70cad020af94c8d471e4c97741eaf68e8d28a8381c09da164c38df46bb6b7`.
- Result: **PASS — entire statement, all six proof steps, residual-scope discussion, and actual-curve strictness corollary read; no mathematical gap found.** This is a mathematical reading, not formal verification.

## Statement and finite-group hypotheses

The hypothesis is a nonzero primary component of the fixed canonical class, not survival modulo the prime. A coordinate projection of the finite primary subgroup gives a surjective cyclic prime-power quotient detecting that component. The exponent is allowed to be larger than the order of the detected element. Even order of `p` modulo the odd prime forces even order modulo every chosen power, and the unique involution in the cyclic unit group is `-1`. No unsupported maximal order-growth or non-Wieferich assertion is used.

## Pointed cover and character calculation

The Lang map has constant kernel `J(k)`. Quotienting by the chosen subgroup and pulling back by the Abel map based at the prescribed point gives a split rational fibre and a constant deck group. The complete geometric-connectedness argument was read: a proper geometric monodromy subgroup gives an intermediate isogeny to which the Abel map lifts; the Jacobian universal property then gives an isogeny section, contradicting multiplicativity of degrees. Translation by the lift of the base point is necessary and is included.

The exact degree-two character polynomial follows from Riemann–Roch. In degree two all classes have one effective divisor except the canonical class, which has `q+1`; in larger degrees the effective-divisor count is uniform and the nontrivial character sum vanishes. The rational base point identifies every rational degree component with `J(k)`. The hyperelliptic involution gives the coefficient relation with the canonical class even without a rational Weierstrass point.

Reduction at a prime above the characteristic preserves the faithful character's order. Inversion is a power of residue Frobenius. If its value at one vanishes, the linear reduced polynomial forces the point sum to be `-1`; the inversion relation then forces the detected canonical class to have trivial faithful character value. This contradicts detection. This reasoning applies to each faithful character; it intentionally gives no conclusion for the imprimitive factors.

## Primitive factor and point-separation endgame

For the order-prime subgroup at the top of the cyclic prime-power tower, the characters not descending to the lower curve are exactly the faithful ones. The isogeny from the lower Jacobian times the connected norm kernel identifies the product of those character values with the integer rational order of that kernel. All factors are units at the characteristic, so the rational primary torsion of that kernel vanishes.

The collision implication is used only in the authorized direction: it supplies a rational lift with primary point difference. The equality `im(tau-1) = connected norm kernel` is proved using the deck sum and surjectivity of multiplication by the odd prime on the abelian variety. Applying `tau-1` to the point difference therefore gives zero. The resulting principal divisor has four distinct points, because the deck action is free and the two base points differ. Its simple poles give a separable map of degree two in characteristic two; in other characteristics degree two itself excludes inseparability. Uniqueness of the hyperelliptic pencil, followed by a fixed point of the odd-prime automorphism of the projective line, contradicts free deck action. The genus bound `n+1 >= 4` is adequate.

## Actual-curve strictness and limitations

The A09 class has exact order thirteen, so multiplying it by `-2` preserves that order. A finite extension rationalizes a point of its thirteen-division fibre. In that field the canonical class is thirteen-divisible; it is divisible by every other odd prime within its own subgroup of order thirteen. Its nonzero thirteen-primary component remains nonzero because inclusion of rational Jacobian points into points over a field extension is injective. Consequently every prime-level canonical detector vanishes, whereas a detecting cyclic thirteen-power quotient exists and has exponent at least two. The text correctly distinguishes strictness of the detection criteria from nonexistence of all prime-degree covers; A09's independent geometric witness remains possible.

The residual obstruction is also correctly stated: extending constants cannot change the finite order or primary support of the fixed canonical class, although it can change its divisibility in the ambient rational group. The argument makes no assertion about the cases of zero canonical class, purely characteristic-primary support, or odd support only at primes where the characteristic has odd multiplicative order.

## Recovered-source attribution read

The following source passages were read in full for the attribution, separately from the reconstructed proof:

- `recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex`, claim A.26 and its complete proof: the prime-degree canonical criterion already has the inversion-power hypothesis and the same Riemann–Roch symmetry.
- The same file, A.44 and its entire proof: the pointed-Weierstrass involution constraint concerns primitive Frobenius multipliers and is compatible with the residual case; it does not prove this new primary-detection statement.
- `recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`, B.13–B.14, complete statements and proofs: primitive cyclic prime-power packets and the rational top-step norm obstruction are explicitly present. Their finite-module strictness example does not claim Jacobian realization; A29's separate actual-curve argument does supply the claimed realization for its narrower detector comparison.

No source files were modified during this independent review.
