# Complete root review of amplified collision components

Reviewer: `/root`; model: GPT-6 Astra Pro; effort: not exposed; run: GCT_POS.
Date: 21 November 2026, completed 23:34 UTC.

**PASS.** Read the complete theorem and proof in `AMPLIFIED_COLLISION_COMPONENTS.tex` and the entire `verify_amplified_collision_component.py`. Independently replayed the script; the exact dimension58 certificate passed. K-020/K-021/K-025 are previously whole-proof-checked dependencies in this run.

At the free closed amplified tensor, the quotient and its finite-order fixed germ are smooth. Taking fixed vectors is exact in characteristic zero, so the differential from the full fixed vector space onto the fixed tangent quotient is surjective. A morphism between these smooth germs is consequently smooth there, with open image. The closure of the whole vector-space image is irreducible, lies in the fixed scheme, and contains an open part of its irreducible component; it is that component. This justifies the same-component assertion, including nonfree degenerations in the closure.

Writing k=8l+s gives the exact prefix character order D_(k-l)=2^s M. After the further power, the old prefix has primitive character M, while the new7l coordinates have scalar weights whose three-factor product is one. The direct sum of the critical prefix with the dimension3 odd block and the remaining one-dimensional blocks has all three marginal matrices equal to the identity. It is fixed by the dyadic element and by a commuting order3 element of primitive determinant character. Their product character has order3M. Thus its nonzero closed quotient point belongs both to the amplified component and to the higher colliding fixed locus.

The replay reconstructs the prefix support and positive margins, verifies the odd block symbolically, matches every collapsed cluster weight, checks every direct-sum support coordinate, and confirms the primitive character modulo3·2^57. It also independently recomputes all fixed-space counts697−339=358. It does not calculate a Hilbert residue.

This proves the collision exception is realized on the actual growing-dimensional family. It does not prove a three-adic denominator for that component, cancellation of the chain, or an actual pole at3M. Those distinctions are explicit in the statement and proof.
