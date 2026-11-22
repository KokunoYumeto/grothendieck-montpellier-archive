# Pre-R_B abscissa and real-obstruction reduction

Date: 21 November 2026. Author/checker: GPT-6 Astra Pro, MAS_ARTIN /root/s5_audit. Effort is inherited and not externally exposed.

## Review status after checkpoint 05

MA-RB-002/003 is written in s5_abscissa_reduction.tex and passed the complete author post-writing reading. It was saved at checkpoint 05 as author-checked work outside Part I. Subsequently root and pf26_audit completed independent whole-proof readings, both passed, and root integrated the module. The current residual arithmetic question is the actual shared-zero exclusion on the interval stated below. Neither R_B nor that exclusion is proved. The source locator now explicitly uses article-PDF pagination, not journal page numbers; narrow weak convergence is distinguished from the proved vague convergence to zero.

## The sharper unconditional comparison reduction

Failure of the specified all-place Calegari comparison forces an infinite exceptional set and a positive-Euler abscissa gamma. The existing convergence at 1 and Landau argument give gamma<1. If gamma<=1/2, the Euler quotient is holomorphic and nonzero on Re s>1/2, its exact completed functional equation gives real-height support, and the already proved FQ006 theorem forces the entire genuine comparison datum to vanish. Therefore an actual failure has gamma in (1/2,1) and a real pole of order k>=1 there. No R_B, A or M premise is used in this reduction.

At that point put n=ord A, b=ord C, v1=ord L_(V eta), e=ord L_X. The exact comparison gives ord L_W=n+k and ord B=b+n+k. The previously proved tensor identities, now applied at gamma, and Takeda's full holomorphy range give v1+e>=k. Their finite local and gamma factors are units at every real point of (0,1), not only at the center.

The regular-character factorization then gives ord_gamma zeta_L>=b+5n+9k. The unconditional Hadamard estimate already proved inside RB001 yields

1−gamma >= (3 sqrt(k)−1)^2 / H_L >= 4/H_L,

where H_L=1+(1/2)log Delta_L. The optimizing parameter is checked to lie in (0,1] by first using that same inequality at t=1; no unsupported discriminant estimate is needed.

Consequently absence of a common real zero of B and L_(V eta)L_X in (1/2,1−4/H_L] suffices for comparison. This is a sharper condition on an actual comparison obstruction. It does not extend RB001's zero-free region to every B-zero: a B-zero may be absorbed by the automorphic numerator and C. Even exact comparison would give B=A C and would not itself prove R_B.

## Boundary positivity and its exact limitation

Let D be the positive Euler quotient, and define a_gamma(t)=−ord_(gamma+it)D. The positive finite measures

nu_epsilon = 4 epsilon sum_(p in Omega, j odd) log(p) p^(−j(gamma+epsilon)) delta_(j log p)

have Fourier transforms epsilon(−D'/D)(gamma+epsilon+it). Meromorphic local orders give the pointwise limit a_gamma(t). Passing finite positivity matrices to the limit proves that a_gamma is integer positive definite on R with its discrete topology, a_gamma(0)=k, and |a_gamma(t)|<=k. Its locally finite real support and membership in B(R_discrete) allow the already proved FQ002 coset classification.

This does not recover the original FQ closure. The actual center-1/2 positive prime measure is not tempered on this branch: polynomial mass growth would make its exponentially weighted integral converge for every sigma>1/2, forcing gamma<=1/2. Adding a finite-total-variation bad-prime/conductor correction cannot change that fact.

The measures nu_epsilon converge vaguely to zero on the ordinary real line while their total masses tend to k>0. They are not tight and have no narrow weak limit against bounded continuous tests. Their Fourier limit is discontinuous at zero, consistently with R_discrete positive definiteness. There is no exact ordinary pure-atomic Fourier identity for this boundary profile carrying the original prime support. The simple profile k 1_{0} satisfies all the forced boundary conditions and has continuous ordinary Fourier density as an atomic measure. This is a boundary-constraint test, not a genuine comparison L-datum or an arithmetic counterexample.

## Remaining precise gates

Checkpoint06 refinement: the independently checked MA-RB-007 retains both reflected real zeros, all complex gamma terms and the full known prime5 factor. Its attained variational bound J_(Delta,1) strictly improves the earlier endpoint whenever that branch remains feasible.

The subsequent single all-prime refinement MA-RB-008, in modules/s5_universal_euler.tex, RB.85–RB.96, has complete final author and independent PF passes. It uses coefficient120 for every unramified prime outside5 and6 for each ramified prime, determined by Delta. The completed zero divisor is nonempty by the fixed Hadamard identity, which proves the stronger denominator remains strictly positive. Its attained script-J_(Delta,1) is strictly smaller than J_(Delta,1).

The subsequent MA-RB-012 has complete author, root and PF whole-proof passes as of2026-11-22T00:15:53UTC. Its finite relative-zeta envelope fraktur-J_(L,1) is strictly smaller than script-J_(Delta,1), unconditionally. The current smallest proved shared-zero interval is (1/2,1/2+sqrt(fraktur-J_(L,1))] when that minimum is positive; a nonpositive value excludes the comparison-failure branch. The new minimum may occur at sigma=1. Finite Euler evaluations recover certified upper bounds. The earlier endpoints remain valid historical bounds. No assertion that the numerical exclusion criterion holds for every actual field is made. Root owns final integration and records its own review separately.

The actual real pole gives a nonreal Booker height −i(gamma−1/2), so real-height support is specifically false on the hypothetical nontrivial branch. The full prime measure's temperedness is specifically false there too. The discrete positive-definite boundary construction loses the ordinary frequency support through escape of mass.

Takeda supplies holomorphy, not real nonvanishing. A common-zero exclusion for B and L_(V eta)L_X on the residual interval is not known from the supplied inputs. Heilbronn's simple-zero theorem still does not apply to multiplicity at least nine. An explicit reflected formal order assignment with k=1 and v1=1 meets all listed order identities and attains regular multiplicity nine; it is not a field.

## Checks and sources actually used

The entire 498-line new module was read after writing and passed its author proof check. The source of the strengthened holomorphy range was freshly inspected in Takeda's primary PDF, Theorem 7.1 and its entire terminal proof, printed pp49–50. The theorem excludes only possible poles at 0 and1, so the application to gamma in (1/2,1) is valid. Its earlier integral/Eisenstein theory is retained as the same declared classical input, not newly re-proved.

The finite representation certificates and prior FQ proofs were not rerun. Their exact proved identities are used at the new point, with the local-unit argument extended by the explicit modulus inequality. The inherited Deligne/SGA1 motive locators and the exact Calegari comparison locators are stated in the TeX. No new archive inspection or general impossibility theorem is claimed.
