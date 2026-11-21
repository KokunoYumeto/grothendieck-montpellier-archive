# Independent complete proof review: DP41

Agent: `/root/step2_higher`. Model: **GPT-6 Astra Pro**. Effort: **not exposed**. Date: **2026-11-21 UTC**. This is a completed mathematical review, not a request for a future check. The main paper was not edited.

Reviewed memo: `primitive_exponential_radius_DP41.md`, SHA256 `b55c9ff12f798d0cde6f821cab8b97f1faa06945b2d53c74dc0824fe44a42fd0`. Exact read-only copy: `DP41_step2_review_snapshot.md`. I read the entire saved proof, challenged all its mathematical steps, and read the two subsequently clarified passages in full. **Result: PASS.** Exact time, block hashes and integrated-paper follow-up are in `dp41_step2_review_checks.json`.

## 1. Rational ghost computation and its stated domain

The divided-ghost identity is correct: Witt Frobenius shifts ordinary ghosts, so after division by p^n it sends u_n to p u_(n+1). The display operator therefore becomes AT on divided ghosts, and its resolvent is the stated finite geometric series on the nilpotent test inputs. Projecting the telescoping sum to T kills dQ because the zeroth T ghost of Q is zero. The resulting additive series has identity differential, so it is the normalized logarithm.

The first draft's sentence about finite ghost sequences was too broad if interpreted for arbitrary infinite Witt vectors: nilpotence of the coefficient ideal alone does not suffice. I raised this independently. The saved version now explicitly uses the finite-support nilpotent Witt functor and the particular Teichmüller and zeroth-ghost rational lifts. In this stated domain finite truncations have finite ghost sequences, and the actual resolvents are coefficientwise well-defined. This corrects the scope of the supporting sentence without changing a term in the formula. The root and archive agent are carrying out the separate primary-source inspection of Zink's ghost/exponential framework; this review does not invent an additional fresh visual source check.

For the line, a return to the T coordinate takes h steps and contributes p^(h−1) against h ghost denominators, giving exactly S^(q^m)/p^m. On the dual, the equations for C and the T′ components give precisely the previously constructed dual logarithm. The path from e_j* to e_0* takes h−j steps; each extra full cycle contributes one p in the numerator, giving the denominator p^((h−1)l+h−j). Thus the coordinate identification used later is an equality of normalized logarithms in these integral coordinates, not an inference from matching special fibres alone.

I also checked the signs in ER9 against the stated quotient convention. The V^−1 k term has negative divided ghosts; the negative hex logarithm changes that sign, while the inverse second pairing supplies −xC in the frame comparison. Taking the inverse comparison gives −Σ+xC. The path multiplier p^((h−1)l+j−1) gives the first denominator p^(n+l+1). The first ordinary-degree terms agree with sign-corrected DP38. Finite-degree support, torus invariance and uniqueness after excluding a bilinear invariant are preserved.

## 2. Full anisotropic initial form

I independently recomputed both term families. For the first family, its weight is

    p^n(s+p^j ρ(q^l−1)).

After subtracting t=as−1 its valuation is exactly ER12. With a≥p−1 and odd p, the n part is at least p^n−1−n, strictly positive for n>0; the l part is strictly positive for l>0. Hence precisely n=l=0 survives, for every j.

For L_0 C, writing k=h−j, its weight is

    ρ q^u+q^l(s p^k−qρ).

Subtracting the baseline weight s gives ER13. Multiplication by p−1 bounds its three summands by (p−1)u, (q−p)l and p^k−p. Subtracting the coefficient denominator gives exactly ER14. Every off-baseline case has a strictly positive contribution: p−2>0, q−p−(h−1)>0, and p^k−p−k+1>0 for k>1. Thus only u=l=0,k=1 survives.

Choosing all scales as powers of a common uniformizer makes the surviving scalars exactly the same μ, not merely of the same valuation: p^j r_0+r_j=s and r_0+p r_d=s. Therefore the full initial form is exactly

    Q=−Σ_(j=1)^d S^(p^j)Y_j+S Y_d^p.

Its monomials are distinct. In every residue characteristic p, ∂Q/∂Y_1=−S^p is nonzero, including d=1. No cancellation or perfectness assumption is needed for this derivative statement.

## 3. Nonintegrality and genuinely unbounded denominators

The first draft stated the lemma using only a non-pth-power initial form over an arbitrary complete discrete valuation field. I independently raised the imperfect-residue-field issue: that property alone need not survive multiplication by a nonzero scalar. The saved version now assumes a nonzero formal partial derivative; over a perfect residue field this is equivalent to the earlier wording. The actual Q satisfies the stronger hypothesis, so the application is unchanged.

For z with coefficient infimum t in [0,s), every higher exponential term in exp(pz) has valuation strictly greater than 1+t. This uses odd p and gives both the exact valuation and the same initial form as pz. If exp(z) were integral, its reduction would have pth power one and hence would be one. Write δ=ν(exp(z)−1)>0. When δ≥s all binomial terms have valuation at least 1+s, a contradiction. When δ<s the last binomial term is uniquely minimal at pδ; its initial form is a scalar multiple of a pth power and has every formal partial derivative zero. This contradicts the nonzero derivative of the initial form of pz.

The separate final step is essential and valid: if exp(z) merely had bounded coefficients, Gauss multiplicativity for bounded formal series over a discrete valuation ring would imply pν(exp(z))=ν(exp(pz))=0. It would therefore be integral. Thus the contradiction establishes coefficient infimum −∞, rather than only a single negative coefficient or failure of integrality. Gauss multiplicativity follows by dividing bounded series by their attained minimum valuations and reducing their product in the formal power-series domain.

At a=p the logarithm's minimum is exactly s; the factorial estimate makes the exponential integral, and its constant coefficient one forces norm zero. For larger a the same conclusion holds. Monotonicity supplies all a<p−1. The endpoint statements in ER1 are therefore correct.

## 4. Coordinate equivalence and the integral unit factor

For the line, the scaled logarithm coefficients have valuation a(q^m−1)/(q−1)−m≥0 for a≥1. For the dual, every elementary arrow satisfies p^e r_j−r_i=1. Iteration gives weight increment δ_m=1+p^(e_1)+…+p^(e_1+…+e_(m−1))≥m. Its contracted coefficient valuation is aδ_m−m≥0. Thus the scaled logarithms are integral formal maps with identity linear term; their inverses are integral by coefficientwise formal inversion. This is the precise scale range required, since the difficult interval [p−1,p) lies in [1,∞).

Substitution by an integral formal automorphism preserves the extended coefficient infimum. For bounded series, apply the substitution inequality in both directions. If an unbounded series became bounded, substitution by the integral inverse would make the original series bounded, a contradiction. No convergence of an analytic map on a boundary is being assumed. The formal maps have zero constant term, so each coefficient of a composition is a finite sum.

The contracted integral unit U and its inverse are integral in group coordinates, and remain so after the scaled inverse logarithm for a≥1. Multiplication therefore preserves both finite infima and the unbounded alternative. For a<1, monotonicity from a=1 completes the additive-coordinate claim. The prefactor really must have unit constant term for this argument; no assertion about a nonunit geometric theta germ is smuggled into it.

## 5. Exact strength and limitations

The conclusion rules out every full-series bound with a finite additive denominator error at weights a(r_0,…,r_d) for a<p. It proves that uniform anisotropic inflation p is sharp for this primitive class in the specified integral frame, and is stable under multiplication by integral unit prefactors. For arbitrary scalar exponents in the unramified coefficient ring, this sentence does not assert that every scalar power of an integral frame ratio is integral. It does not assert optimality among every possible unequal choice of weights.

No fixed-path or harmonic consequence follows merely by restriction. A path can annihilate or cancel the initial polynomial; at height two the identical-coordinate diagonal already cancels its two terms. A selected differential polynomial can ignore the offending coefficients. The present proof therefore does not improve the sufficient one-variable residual for an arbitrarily prescribed path, does not compute the selected connection estimate, and does not decide a lift count. The memo's explicit scope statements correctly retain those limits.

## 6. Corrected integrated DP38–DP39 preservation

I read the complete corrected integrated DP38 theorem, proof and following path paragraph, and the complete corrected integrated DP39 proposition, proof and following harmonic paragraph. DP38 now consistently has coefficients −1/p,+1/p, first form (−S^pY_1+SY_d^p)/p, mixed derivatives −(p−1)!,+(p−1)!, and the positive last-dual path coefficient ε^p/p. DP39(b) uses −1/p and evaluates exactly to −(p−1)!/2. Its row-degree, row-invariance, harmonic-cancellation and integral-function arguments are unchanged and remain valid. Both corrected blocks pass as complete mathematical statements, with the same local/global restrictions.

These are new preservation checks, **SPR-P-025** and **SPR-P-026**, and expressly supersede the exact-sign component of SPR-P-023 and SPR-P-024. They do not erase the historical snapshots or pretend the earlier positive-sign convention was the source convention. Current integrated snapshots and exact hashes are recorded separately in the JSON metadata.
