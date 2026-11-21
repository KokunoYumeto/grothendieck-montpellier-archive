# Independent complete proof review: I-36

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.

Completed and recorded: 2026-11-21T04:26:08Z.

Scope: complete I36_singular_width_three.tex, with the local-rank test construction in I21 section3 and the entire I30 endpoint/rank-stage argument reread as dependencies. Existing I29 support-four theorem is used as already independently checked. No new external source proof audit or finite numerical certification is claimed.

**PASS.** No mathematical repair is required. Explicitly stating 1<=r<=w is a harmless statement precision.

## Pairwise dominance and rank-one multiplication

The two-coordinate substitution matrix has determinant lambda_j(y)-lambda_i(y), which is nonzero because its value at a_i is minus one, including in characteristic two. Its inverse over E(y) proves injectivity for every bivariate polynomial, with arbitrary extensions independent of the fresh parameters. A coordinate alone is transcendental because its coefficient on t is one.

For a rank-one factor the chosen column times chosen row divided by the common pivot reproduces every entry by the two-by-two minor identities. Multiplication and denominator clearing give exactly the two univariate endpoint factors and adjacent bivariate scalar contractions. The identity includes the one-factor case. Nonzero original contraction forces all factors nonzero; pairwise dominance preserves every one under the same map, and a product of their images is nonzero in the parameter domain. Overlap of adjacent variable sets is harmless here because the assertion has already been reduced to scalar product closure.

## Maximal minors and simultaneous preservation

An rth compound has generic rank one when the original factor has rank exactly r, and is zero when its rank is smaller. Cauchy--Binet therefore reduces any nonzero r-minor of an interval to the preceding rank-one argument. This proves entry-by-entry preservation for every interval and minor. Finiteness and the domain property justify simultaneous preservation as a formal map; no separate numerical parameter selection is implicit. The compound dimension can be large, but the explicit map and its parameter count do not use it.

## Width-three completion

After constant invertible factors are absorbed, no remaining interval has generic rank three. Constant singular factors, if present separately, can likewise be absorbed or kept as constants without introducing a parameter. Padding a smaller-width representation with zero rows and columns is harmless. The compound argument preserves all nonzero two-minors even when longer intervals have rank one or zero.

The I21 minimal local rank-one tests have interiors all of whose nonempty subintervals have rank at least two. Here they therefore have rank exactly two, already preserved by the first centered pair. Original endpoint rows/columns are nonzero univariate polynomial vectors and remain nonzero at their transcendental coordinates. I30 absorbs them into generic and constant unit factors; every enlarged interval has matching generic and constant ranks in {2,3}. I29 then gives a nonzero coefficient of support at most four for the entire test. Four fresh pairs preserve the tests, and setting their amplitudes to zero retains the previous two-minors. I21's local induction consequently preserves the augmented scalar output. No rank-one preservation by the initial pair is asserted.

## Finite grid and scope

The common-center degree is at most D, each of five selector degrees at most (n-1)D, and total amplitude degree at most D. The tensor grid/Newton simplex size is exactly (D+1)((n-1)D+1)^5 binom(D+5,5). The stated field-size and extension-oracle qualifications cover all characteristics and n=1,D=0. The improvement applies to the singular-factor subclass, not arbitrary variable-dependent invertible factors and not the unresolved two-pair centered claim.
