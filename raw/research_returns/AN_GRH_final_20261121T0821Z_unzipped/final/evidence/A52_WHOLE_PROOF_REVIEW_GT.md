# A52: independent whole-proof review

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Complete reading began 2026-11-21 07:57:45 UTC. Review recorded 2026-11-21T08:00:09.854031+00:00.

Source: work/row_audit/SMALL_INTEGRAL_ANNIHILATOR_CRITERION.tex.
SHA256: 17e09e5045d6f08d6b831607a5da392c1f7a3e4f4b60ecebf73122cfddddfe4b.

**PASS: complete manuscript, including the fixed-field lattice proposition and final scope paragraph.** This is a separate-reader proof check, not an independent construction or arithmetic computation.

## Integral criterion

Minimizing among integral annihilators with nonzero faithful evaluation removes every common coefficient prime other than p. The free disjoint original deck orbits make the degree of the principal function exactly the coefficient norm, with arbitrary signs allowed. A pth-power function would yield a smaller annihilator on taking its root. Thus the function and generated-field extension are separable.

The previously checked Poonen controlled-field result applies to the finitely many translates of a separable degree-d function. Its divisibility and genus bound imply e greater than one. I checked applicability here; I did not newly read that external proof in this audit.

The stabilizer comparison includes zero coefficients and does not assume global freeness on Z. Nonzero faithful evaluation makes both original orbit images injective. If those images coincided, the signed integral coefficient relation, iterated through the odd translating-element order, contradicts torsion-freeness of the integral group ring. This is valid in every characteristic.

A zero or pole fibre is then a singleton. Equivariance makes both complete original orbits totally ramified, so e divides every coefficient. Minimal content makes e a nontrivial p-power. A prime-order stabilizer anywhere on Z would force a divisor of n to divide e, hence the action is free everywhere. The unramified genus formula and g(Z) less than n give genus one for Z and its quotient. At all 2n totally ramified points the local separable derivative has different exponent at least e. Riemann--Hurwitz gives e at most g minus one. The local-different result is used with the same hypotheses as the previously checked criteria; no new primary-proof read is claimed.

Faithfulness on the generated field makes K the composite of that field with K^G. Degree comparison identifies the degree-e base map, and the entire etale fibre product has function field K and is connected. Etale base change preserves total ramification at P and Q. The obstruction is therefore excluded for 2 <= g <= p. No unspoken rationality assumption on the deck generator or operator is used.

## Fixed-field lattice

The exact multiplier order t times ell^(r-s) and fixed cyclotomic field identify the invariant ring with O_E tensor Z_p, including every unramified product component. Its elements act on the actual rational primitive p-primary group. The projection e_n delta is actual and rational because n e_n is a rational integral endomorphism and n is invertible on p-primary groups.

The annihilator has finite p-primary index W. Density of O_E in its p-adic tensor gives exactly that index for the integral lattice. The box containing (floor(W^(1/h))+1)^h points gives a nonzero difference in the ideal with the stated coefficient bound. A nonzero element of the field E has nonzero faithful evaluation. Substitution into the higher-level polynomial preserves the bound. Multiplication by 1 minus sigma^(ell^(r-1)) kills all proper conductors and the actual primitive projection; hence it kills the full collision class. The alternative exponent operator proves the minimum of the two displayed bounds.

The component formula W=p^(sum h_v e_v), M=p^(max e_v), zero-module convention, and transitive h=C_E=1 specialization all check. In that specialization the test is exactly the old prime-power exponent test.

## Scope of progress

No actual cover or point outside the full A45/A46/A47/A49 witness union is supplied or established by this review. Unequal formal component exponents may improve the lattice expression, but this is not a proved new geometric witness. There is no uniform estimate on W or eventual small annihilator theorem. Thus this is a new sufficient criterion with **no demonstrated strict shrink of the universal residual existence gate**, and no automatic review movement.

I reread A45 SD.1--SD.11 for the exact actual-module descent. No new external-source proof reading, code execution, or geometric construction is claimed. This verdict is tied to the exact hash above.
