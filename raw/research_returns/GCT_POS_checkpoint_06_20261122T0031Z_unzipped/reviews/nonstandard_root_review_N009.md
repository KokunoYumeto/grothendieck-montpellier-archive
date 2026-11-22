# Independent whole-proof review: N-009

Date: 2026-11-21 UTC. Reviewer: /root. Model: GPT-6 Astra Pro.
Effort setting: not exposed. Run: GCT_POS.

I read the complete proof in `branches/nonstandard/integral_nonfreeness.tex`,
including the quotient argument, the finite coordinate model, closure, and
both cardinality lemmas. Outcome: **PASS for the explicitly specified full
P-generated order over Z[v,v^-1]**.

The original image calculation was independently reconstructed in
`branches/root/verify_mixed_jet.py`, importing none of the nonstandard
branch's code. This reconstruction uses the standard Hecke relation and
the expanded formula for P directly. It reads only the list of 128 actual
words and the reported parameters from the original certificate.

The independent cardinality algorithm uses globally minimal valuation
pivots over Z/1024, rather than the original Howell insertion algorithm.
Every pivot row is divisible coordinatewise by its pivot power of 2, so
the annihilator of that row is zero. Successive pivot projections prove
the product formula for the additive cardinality. All 384 products of
listed words by the three generators were verified to lie in their
R-span, proving that this span is the full image for arbitrary word
length. Multiplication by 2 and by eta was computed inside this image.

The independent results are log2|M| = 3690 and log2|(2,eta)M| = 3564.
Thus the residue quotient has dimension 126 over F2. The natural map
B/(2,v-1)B onto that quotient gives a lower bound of 126 on the number
of local generators. The generic rank is 114. A locally free module at
(2,v-1) would have a 114-dimensional residue quotient, a contradiction.
No flatness or injectivity of specialization is assumed. The proof
therefore excludes every basis of this order, in any positive, signed,
or factored cone, in every degree.

The result does not exclude a basis after extending scalars to
Q[v,v^-1], or a different integral lattice in the generic algebra.
It does not assert that the lower bound 126 is the exact minimal number
of generators of the original local order.

The exact source locator for generic dimension 114 was corrected from
the draft's section 11.7 to GCT IV, section 11.8, printed page 67.
The branch is separately auditing the definition of the integral order
and historical priority; this review does not certify novelty.

Computation receipt: `reviews/mixed_jet_p2_independent_verification.json`.

