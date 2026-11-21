# A51: independent whole-proof review

Date: 2026-11-21.

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source: `work/row_audit/A51_NORM_COMPATIBILITY_AND_TOWERS.tex`.

SHA256: `ba76d8eba6a85ec3f81441dcf719d6565debcc38332507c3acedd1898d4a9fd2`.

**Verdict: PASS, independent reading of the entire seven-step manuscript.** This is a separate-reader proof check, not a new independent construction or a new arithmetic computation. I initially reported that this read was incomplete; it was completed only after the A51 Fox/rationality supplement had been written and sent.

I checked each claimed implication:

1. Norm and pullback on the actual rational p-primary groups give a direct-sum splitting because the refinement degree is prime to p. The exact order is the least common multiple of the old component's order and the norm-kernel component's order. No arbitrary kernel element is claimed to be a point difference.
2. Hilbert90 descends the geometric principal function. Its exact divisor order excludes a pth power over the perfect finite field. The norm has the specified divisor and hence differs from the power downstairs by a constant. The rational-function counterexample has simple zero and pole and is explicitly outside the pointed etale configuration.
3. Constant deck group and the two rational lifts give two disjoint rational fibres. The function's zero and pole fibres have one rational point each; counting its other rational fibres proves the stated lower bound on the particular point-difference order. The source correctly does not turn it into an upper bound or an arbitrary-large fixed-field cover assertion.
4. Coprime cyclic covers are geometrically linearly disjoint. Proper-quotient norm operators kill the integral faithful conductor projector. Pullback is injective on the relevant p-primary group by its norm composite, so the actual primitive subgroup is killed by those norms. This does not prescribe possible two-point divisors in that subgroup.
5. The Frobenius-stable rank-one quotient gives the conditional tower and its scalar multiplier. Weil weight excludes a root of unity. The binomial calculation yields the exact minimal field degree t times ell to the maximum of zero and r-s. The stable quotient is an assumption, not an asserted supply theorem.
6. The finite-etale conductor algebra and its Frobenius automorphism have a free geometric action of the exact order f_r. The cited A45 effective descent applies without dividing by f_r. Componentwise freeness over the invariant product of unramified discrete valuation rings gives the order, exponent, and p-torsion dimension identities. Combining the exact prime-power new-factor dimension with the p-rank bound gives the displayed uniform rational generator bound. The abstract modules of exponent p^e satisfy these algebraic hypotheses and are expressly not claimed to be geometric.
7. The discrete direct sum has a continuous Z_ell action. On a summand beyond level m, Z to the ell^m minus one is a unit at every primitive root in coefficient characteristic p, so it has no H_m invariants. The finite invariant groups and their arbitrary exponent growth follow exactly.

Known inputs were checked for their stated applicability, including the previously reviewed A45 descent. I did not newly reopen the external Hilbert90, divisor-norm, Milne, or Stacks source proofs during this particular whole-manuscript review. No independent code execution, geometric example, or universal-supply result is claimed. The final limitation paragraph is appropriately scoped.
