# DP50: independent complete nonunit-kernel and level-normalization review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Event **ABA-CE56**. Entire saved memo §§1–8 read and independently challenged during **03:01:27–03:04:26 UTC**, including the new source-normalization corollary in §7. No main-paper edits.

## Outcome and exact version

**PASS.** The proof supplies an infinite exact coefficient sequence, so its exponential-radius assertion does not rest on a single bad coefficient or on an unjustified transfer from logarithm radius. The precise source-normalization corollary is also correct. No mathematical correction was required.

- Entire memo SHA-256: `dec372362615adf1078ff8f2b2252a44933ffc370ccbd263bcb39f240b2328b5`.
- Complete statements and proofs, §§1–7, SHA-256: `ae634f2ed4c7047f056cec44187327f21c3169ffb4eb0c430fb16de98bc0c8cb`.
- Frozen complete memo: `late_proof_snapshots/DP50_complete_checked.md`.
- Metadata: `late_proof_snapshots/DP50_check_metadata.json`.
- Exact recovered source definition: `late_proof_snapshots/DP50_thExpr_source_66_70.lean`.

## 1. Boundary contraction and full dual cycle

The scalar excess `Δ=r_j−ρ` is strictly positive for `h≥3`, including the smallest case `j=h−1`; the stated geometric-sum numerator verifies this directly. Scalar logarithm terms beyond the identity therefore vanish after reduction at the new boundary weight.

For the dual, every first selected arrow has defect one, including the exceptional degree-`p²` arrow. A path through at least two selected arrows has geometric weighted increment strictly greater than the number of denominator powers. Thus the reduced logarithm is exactly `Id+M_η`, with all indicated arrow coefficients nonzero. Its inverse is the formal additive geometric series; arbitrary Frobenius powers of arrow units cause no problem.

The scaled input reduction retains exactly the first unit component `j`. Earlier components vanish because unramified nonunits have valuation at least one and `r_i−r_j<1`; later components vanish because `r_i<r_j`. Paths from `j` to `d` have exponents `p^(k_*−1)q^m`, one path for every `m`. The distinct exponents and nonzero unit products prove that none of these reduced coefficients cancels.

## 2. Full primitive-series minimum

I independently recomputed all baseline and cycle differences in NT15–NT18. In the first family, `p^i r_j+r_i=s+p^iΔ`, so its baseline lies strictly above `τ=s−1+Δ` by `(p^i−1)Δ`. Higher ghost and cycle indices add nonnegative quantities, strictly positive whenever the corresponding index is positive.

In the product family, the baseline difference is `(p^e−p)s−e+1`, zero exactly at `e=1`. The line-cycle increment is strictly positive because `r_j(q−1)>1`. The dual-cycle increment is strictly positive since its minimum numerator is `p+…+p^(h−1)>h−1`. Therefore only `+a_d^(−1)SY_d^p/p` realizes the minimum. This remains valid when `τ<0`; the proof does not reuse a lemma whose hypotheses require a nonnegative logarithm valuation.

## 3. Infinite exact coefficients survive exponentiation

After inverse substitution the complete reduced first level is an infinite series with nonzero coefficients in degrees `N_m=p^(k_*)q^m+1`. Formal reduction commutes with the substitution because all contracted maps and scaled inputs are integral and have zero constant term.

For `κ=p^aλ`, `a≥1`, the logarithm minimum becomes `L=a+τ>s`. Every exponential order at least two exceeds `L` by at least `(b−1)(L−s)>0`. Hence the entire first level of `exp(z)−1` is exactly the first level of `z`. This proves the equality at every `N_m`, not merely a lower bound.

The identity `τ−r_j(p^(k_*)+1)=−S_(k_*)` gives NT4. Its right side is an integer because `r_j(q−1)` is integral and `q^m−1` is divisible by `q−1`. The exact sequence tends to minus infinity at every smaller weight, whereas the boundary kernel is integral with constant one. This proves both threshold directions and the endpoint. Legendre's formula then gives the exact factorial liminf.

## 4. Invariant frames and prefactors

A normalized frame ratio equals one on both axes. Each nonconstant supported monomial therefore has positive scalar degree. Its original invariant weight is a positive multiple of `s`; increasing the scalar weight adds at least `Δ`. This gives the bound `ν(log J)≥s+Δ`. Multiplying by `κ` places the correction at least at `L+1`, so it cannot alter any coefficient in the exact first-level sequence. The stated exact valuations are consequently invariant under all the permitted frame changes, even for unit parameters outside `Z_p`.

For an arbitrary integral prefactor, its contracted restriction is integral at the boundary. This proves the universal coefficientwise lower bound. The pure kernel proves that the universal slope cannot be increased. The memo correctly declines to deduce the same individual radius for every nonzero prefactor: no multiplier obstruction covering that boundary has been proved here, and a prefactor could interact with the critical coefficients. Zero restrictions are correctly included only in the lower-bound assertion.

## 5. Numerical and fixed-prime claims

The height-three, `p=11` table agrees with `p^j/(q−1)`: the two pure-kernel slopes are `11/1330` and `121/1330`, compared with the unit-exponent values `1/1220` and `1/120`. Additional powers of `p` alter the exact coefficient constant but not the limiting slope.

Cross multiplication gives the positive numerator `(p−2)q+(p−1)p^j+1` for the improvement over the unit-exponent slope. The upper bound by `1/(p−1)`, and then the bound by one half of the logarithm of the odd radical, are correct. For a fixed integer exponent this affects only finitely many primes and contributes `O_κ(n)` to the stated sum. The text does not turn that observation into a theorem for a level varying with the construction.

The warning about a rational quadratic term is mathematically necessary: the new boundary may lie below `s/2`, so DP48's integral-quadratic observation from the unit-exponent case cannot simply be reused. If the quadratic is multiplied by a p-divisible `κ` and its original coefficient is integral, the asserted elementary integrality statement does hold.

## 6. Exact source normalization

I directly read the recovered `Formalism/LocalToGlobal/ProjectiveLattices/IsThRule.lean` lines35–86. Its `thExpr` definition at lines66–70 literally uses tensor exponent `M²` and the scalar inverse of `M^P.totalDegree`. The full source file SHA-256 is `d0570a0398b32df4c732c4b0d5051d27cda119195187e74377f4f0e40cfeb11e`; the exact definition block hash is `a1b6e87551d89c37c8011649688524eb2c0ec62a4b0c4ad965bd6989826ccda2`.

For a homogeneous ordinary-path degree `n`, division by `M^n` subtracts exactly `bn` from coefficient valuation. Thus the pure-kernel factorial slope becomes `p^j/(q−1)−b<0`, and the corresponding sharp universal lower bound follows for arbitrary integral prefactors. Since `p^j/(q−1)<s≤1/2`, its change relative to a unit-level pure kernel is strictly below `s−b≤−b/2`. All inequalities, including `b=1`, check.

This is the degree normalization actually present in the recovered definition. The proof carefully restricts the path comparison to homogeneous degree and does not assign every monomial of an arbitrary nonhomogeneous polynomial its total degree. Nor does it exclude compensating divisibility from a particular algebraic section or selected harmonic value.

## Scope

The actual arbitrary-unit display and primitive pairing are the independently checked DP46 inputs; no new deformation-classification premise is used. This event is a complete original-memo challenge and direct source-definition check, not a later integrated-block review, a Lean run, or an entire-paper proof audit. The theorem concerns the pure kernel, permitted invariant frames and a sharp universal bound with integral prefactors. It establishes no shorter-chain obstruction or exact value for the prescribed global theta section.
