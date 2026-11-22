# MA-RB-008: one universal all-prime Euler refinement

Date: 2026-11-21.
Author and author checker: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

The full proof is modules/s5_universal_euler.tex, MA-RB.85–96. The complete author post-writing reading of the final371-line discriminant-aware theorem has passed. pf26_audit independently read the entire final proof and passed it, with separate review events and detailed notes. Root proposed the discriminant strengthening, then independently read the complete final version and passed it at20:28:33 UTC; the theorem is integrated. Root owns packaging.

## Exact result

For the actual degree120 Galois normal closure, every residue degree f_p is at most6, including at ramified primes. A lift of the cyclic residue Frobenius belongs to a decomposition subgroup of S5; the residue degree divides that lift's element order. The possible S5 element orders are1,2,3,4,5,6.

Writing g_p for the number of primes over p gives the full local logarithmic derivative E_p(sigma)=g_p f_p log p/(p^(f_p sigma)−1). The decreasing function u/(x^u−1), together with g_p≥1 and f_p≤6, gives E_p(sigma)≥6 log p/(p^(6 sigma)−1) uniformly at every rational prime. At every unramified prime the stronger identity g_p f_p=120 improves the coefficient to120.

Subtract the discriminant-aware lower bound simultaneously for all p≠5 from the preceding denominator H_Delta: coefficient120 at p not dividing5Delta and6 at p dividingDelta. Its exact rational-zeta expression is −120(zeta'/zeta)(6sigma)−120log5/(5^(6sigma)−1)−114sum_(p|Delta)logp/(p^(6sigma)−1). Five is excluded because its exact Euler term was already retained by RB007 and5 does not divideDelta.

The resulting script-H denominator is strictly positive. The exact Hadamard identity expresses it as the zero sum plus nonnegative Euler remainders. The completed zero divisor is nonempty: otherwise the fixed logarithmic-derivative identity would equate zero with60log(sigma)+O_Delta(1) at infinity, since the Euler derivative tends to zero by dominated convergence and the previously proved gamma/Jensen estimate applies. Each completed zero contributes a strictly positive real part at sigma>1. The new denominator is also strictly smaller than H_Delta.

This is a pointwise comparison of full local logarithmic derivatives at real sigma>1, not coefficientwise positivity of the difference of their Dirichlet series and not a submotive assertion.

The resulting variational infimum script-J is finite, attained, and strictly less than the preceding J. The strict comparison evaluates the new function at the attained old minimizer; it does not infer strictness by merely comparing two infima. The actual comparison-failure branch would satisfy (gamma−1/2)^2≤script-J_(Delta,k)≤script-J_(Delta,1).

Thus script-J_(Delta,1)≤0 excludes that branch. If it is positive, the current shared-zero criterion is confined to (1/2,1/2+sqrt(script-J_(Delta,1))]. When the previous interval was nonempty, the new one is strictly shorter or the branch is excluded. This is a single universal Euler refinement, not separate progress claims for individual primes. No claim that the criterion excludes every discriminant, or that R_B is proved, is made.

## Finite-cover meaning

The local calculation is performed on the regular Artin representation Q[S5]. Inertia invariants have a basis of inertia orbits. The arithmetic residue Frobenius acts in g_p cycles, each of length f_p, so its local polynomial is (1−T^(f_p))^(g_p), even at ramified primes. This supplies the complete local Euler factor, rather than assigning a ramified Frobenius conjugacy class in S5. The argument uses finite-cover inertia invariants and makes no positive-cohomology claim about analytic zeros.

The categorical locators are inherited from the previously checked MA-S5 placement: SGA1, ExposéV, section7; Deligne1979, Definition6.1 and sections6.2–6.3, with equation0.5.3 for induction/restriction of scalars. They are not claimed as new sources for the analytic inequality.

## Checks actually performed

Read the initial325-line written module after writing; root independently passed that version. After root's proposed strengthening, read the entire final371-line module afresh. Recomputed the ramified residue-degree argument, both local bounds, the monotonicity derivative, coefficients120 and114 in the rational-zeta identity, the exclusion of prime5, the complete nonempty-divisor proof and dominated Euler limit, the paired-zero inequality, both endpoint expansions, attainment, and the strict old-minimum comparison. Checked the inertia-orbit determinant calculation with the specified left regular action and arithmetic Frobenius.

Freshly read the Calegari main hypotheses in S5ArtinWeb.tex lines123–136. Re-read the complete preceding RB007 text as used, including the exact identity RB.77 and the gamma/Jensen estimate. Checked the already established Artin-motive locators in s5.tex. No new full audit of SGA1 or Deligne is claimed.

Checked equation-tag uniqueness for RB.85–96. No numerical zero search, floating-point optimization, or new finite-representation certificate was needed.
