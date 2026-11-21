# Narrow algebra review of the fixed-field tower report

Date: 2026-11-21. Reader: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed.

**PASS, targeted proof check of the two complete algebra sections only.** Checked source:

`work/effective_galois/fixed_field_tower/PRIMARY_SCOPE_REPORT.md`

SHA256 `8a53fbea44b91ba892ca6620967b176479c7707ecea0c5be387065bc53c80127`.

The reading covers the full section “Complete algebra check: what semilinear descent does give” and the complete numerical/direct-sum algebra argument in “Why the nonabelian limit theorem does not fill the gap.” It does not audit or reread the six literature sources, their theorem proofs, or the bibliography claims.

For an odd tower prime ell, the order formula f_r=t ell^max(0,r−s) follows from the displayed valuation identity. The full product algebra O_r is finite etale of constant rank f_r over its invariants R_r. Freeness over the product of unramified DVRs gives the claimed additive f_r-fold copy, cardinality, p-rank, and exponent identities. These require no assumption that p is prime to f_r. The geometric dimension bound gives precisely the stated uniform bound on the number of rational p-primary generators, not an exponent bound.

The discrete G=Z_ell module A=direct_sum_r O_r/p^{e_r} is continuous: each element has finite support, so an open subgroup fixes it. For H_m=ell^m Z_ell, every summand with r≤m is fixed. For r>m, the image of Z^{ell^m} at every primitive ell^r root in characteristic p is a nontrivial ell-power root, since p differs from ell. Thus Z^{ell^m}−1 is a unit in the full O_r and its quotient modulo p^{e_r}; this proves that such a summand has no invariants. Therefore A^{H_m}=direct_sum_{r≤m} O_r/p^{e_r}, a finite group whose exponent is p^max_{r≤m} e_r. The e_r may grow arbitrarily. This verifies the stated abstract-module hypothesis comparison. It does not realize A by a geometric tower.

The separate numerical example p^{d ell^r}→1 ell-adically, with d=ord_ell(p), also checks by the elementary valuation identity. Neither this convergence nor finite invariant groups forces bounded p-exponents. No source modification is requested.
