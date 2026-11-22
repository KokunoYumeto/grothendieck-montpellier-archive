# Causal divisor separation and the actual trace witness

MA-JP-004 is proved in `causal_trace_separation.tex`, with equation tags MA-JP.40–.53 to avoid the earlier counterpath tags. Its abstract statement applies to any locally finite positive-integer divisor contained in a fixed vertical strip with multiplicity-weighted O(logT) count in unit-height intervals.

The exact assertion includes an essential exception: a divisor supported entirely at the two prescribed exponents is a linear combination of their exponential moment functionals, and therefore vanishes on their common kernel. Apart from that exception, the trace functional has a compact smooth positive-support witness with both moments zero and trace normalized to1. Positive support does not mean that the complex test takes nonnegative values.

The proof uses true compact tests t^(k−1)e^(−kappa t) psi(t/epsilon) chi(t/R), k>=4. Both their weighted L1 norms and their weighted second-derivative L1 norms remain bounded as epsilon goes to0 andR to infinity. The lower transition contributes O(epsilon^(k−j)) for j<=2; the upper transition is exponentially controlled. Two integrations by parts yield a uniform (1+gamma^2)^−1 bound, summable against the divisor count. This justifies the resolvent-power identity after removing both endpoint cutoffs.

The resulting sum of d_lambda/(kappa−lambda)^k is normally meromorphic on the whole plane. Every support point has a nonzero order-k principal part. Equality to two prescribed resolvent powers therefore forces the support into their two poles. Two translated small bumps give a nonsingular moment matrix, proving the exact annihilator statement without an unproved density assertion.

For the actual retained quotient, WP already constructs the convolution operator, its S1 ambient lift and its trace. The lemma is applied to that established trace, not used to define an operator through a zero sum. The actual fast-path construction of JP003 can therefore use a causal compact test. Hardy's classical result supplies nonemptiness for zeta only as explicitly stated; the primary locator and published-theorem scope are inherited from JP003 and are not presented as a newly reread full 1914 proof.

For the exact upper remainder in SB003/004, the lemma proves that vanishing on every causal test is equivalent to emptiness of that omitted divisor. The equivalence persists under both polar moment conditions because nontrivial completed zeros do not give the exponents±1/2. No zero outside the strip is asserted to exist, and no absence result is inferred.

Complete author proof QA passed. Root and peer independent readings were requested; their completion is recorded separately when received. No master or build file was edited.
