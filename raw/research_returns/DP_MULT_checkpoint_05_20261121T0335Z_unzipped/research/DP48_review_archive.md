# DP48: independent complete quadratic-gauge proof and fragment review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Events **ABA-CE48** (complete original proof) and **ABA-CE49** (complete intended integrated proof). Both were read in full during **02:44:11–02:44:58 UTC**. No main-paper edits.

## Outcome and exact versions

**PASS.** No mathematical correction was needed. The intended integrated proof retains all arguments of the complete memo. This review does not assert that the fragment was already present in the main paper; at closing it had zero exact occurrences there.

| Scope | SHA-256 |
|---|---|
| Entire memo, including application and scope | `7fdfe96fcd6b487ecfde5e409048aed373bd8224531f02ae5d9ca1fff42f91fc` |
| Complete statement and proof | `201a7760af7c476e1df9fc30de191a53396117ee6e1edcec871281b7d59b9e7c` |
| Entire intended integrated fragment | `28c545c5ea774e5d25fb1e6b895b1c57df0dbee2976bff482116681a87ccc827` |
| Complete integrated proposition and proof | `6562b7d89a1c33791ddeb2121086cad6ce49910291f206405d640364eecbd542` |

Frozen copies and `DP46_DP48_check_metadata.json` are in `late_proof_snapshots`.

## Complete proof challenge

The zero quadratic coefficient is exactly DP42. For a nonzero coefficient, unramifiedness supplies an integer valuation. If that valuation is nonnegative, the quadratic critical weight is at most `s/2`, strictly below `w_k`. Thus the quadratic exponential and its inverse are integral in an interval extending below the primitive threshold. Multiplying an unbounded primitive expression by that integral unit cannot make it bounded, since its integral inverse would reverse the operation. At and above the threshold both exponentials are integral units, and the finite norm equals that of the nonzero prefactor. Monotonicity correctly extends the near-threshold obstruction to every smaller nonnegative weight.

If the coefficient has valuation `−M≤−1`, then its quadratic threshold `(s+M)/2` is strictly greater than `s`, hence greater than `w_k`, because `p` is odd. Just below that threshold, the primitive kernel times the nonzero prefactor is already bounded. The quadratic exponent has valuation in `[0,s)` and initial form a nonzero scalar times `T²`; its derivative is nonzero in odd residue characteristic. The full DP41 fraction-field multiplier lemma, not merely a unit-prefactor statement, therefore proves unboundedness of the product. The endpoint is integral and monotonicity again supplies all smaller weights.

The finite-value assertion for a possibly vanishing-at-zero prefactor is valid because its restriction is required to be nonzero. At the endpoint, integrality gives the uniform coefficient bound. Any coefficient liminf greater than the asserted value would imply a finite Gauss norm at a rational smaller weight, contradicting the proved threshold. Legendre's formula gives both the factorial inequality and its exact liminf. In the nonintegral case the resulting slope `(s−M)/2` is strictly negative and therefore strictly worse than the original positive primitive-path slope.

## Canonical-gauge application and limits

The claimed application only uses the already traced source interface conditionally: a biadditive difference becomes bilinear in logarithmic coordinates, and then becomes `ct²` on a linear logarithmic path with the fixed linear diagonal endomorphism. This is an ordinary scalar restriction statement. It does not assert that arbitrary harmonic projections are unchanged, and it explicitly retains the source theorem's annihilation condition for selected-value invariance.

This event did not re-read all the recovered Lean source theorem proofs. The memo supplies the exact previously traced declaration/line locators and clearly states the remaining geometric identification. No theorem for arbitrary ramified quadratic coefficients, zero prefactor restrictions, or global theta cost has been inferred. The complete intended integrated proof retains these limits.


## Actual main integration closure

**ABA-CE53**, closed **2026-11-21T02:49:02Z**: the exact previously whole-reviewed DP48 fragment now occurs once in the main paper. Its SHA-256 is unchanged at `28c545c5ea774e5d25fb1e6b895b1c57df0dbee2976bff482116681a87ccc827`; complete proposition/proof hash remains `6562b7d89a1c33791ddeb2121086cad6ce49910291f206405d640364eecbd542`. This is a genuine integration/preservation check, not a redundant claim of a new independent whole-proof reading. It closes the earlier explicit intended-fragment limitation in ABA-CE49.
