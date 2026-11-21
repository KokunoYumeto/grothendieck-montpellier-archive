# Independent whole-proof review of R-26

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/isolation`; run CUE-GCT-20261121-I.

Result: **PASS**, after a complete reading and independent rederivation of `work/rectangular/r26_fragment.tex`, including its finite core certificate. This review establishes the stated uniform lower bound, not equality of the full normal rank at every size.

## Exact finite check actually executed

At 2026-11-21 04:44:07.195875 UTC I executed `check_R26_cores_independent.py`. It imports none of the author checker and uses neither the author's continuant recurrence nor elimination for determinants. It enumerates all matchings of each relevant path interval to reconstruct its continuant coefficient vector; every selected eight-by-eight determinant is evaluated by the full 8! Leibniz sum.

All 17 matrices, all 1,376 coefficient entries, all 17 selected nonzero residues, the prescribed edge rule, the actual boundary-core outer-product ratios, the paired-zero-edge counts, and the ordered manuscript row table passed. The exact report, method and reviewed hashes are in `R26_cores_independent_checks.json`.

This is an independent finite certificate for the cores. The extension to arbitrary sizes rests on the separate proof checks below.

## Whole-proof checks

1. **Endpoint derivatives.** I derived the complementary permanent by its forced upper or lower path and the two residual interval matchings. This gives both displayed first derivatives. For the quadratic rank-one coefficient, the two endpoint columns and the alternative other endpoint row give the stated two summands, including the factor two. The three endpoint formulas also agree with the direct two-row/two-column deletion.

2. **Character decomposition and normalization.** Each column has the displayed character modulo m. The eight ordinary-character columns have exactly the two integer weights r and r-m; their coefficient rows are disjoint. I checked all eight pairs directly from the endpoint formulas, including the factors delta_(r-1), delta_r^(-1), delta_j, delta_(j-1)^(-1) and K=E_j/D_r. Cancelling the common products gives precisely the reduced outer ratio in the text.

3. **Zero-edge limits.** Every chosen distinguished denominator edge is nonzero. In the paired-cut cores there is one zero edge on each outer side, with optional middle zeros absent from the reduced ratio. Replacing the zeros by scalar multiples of a common parameter realizes any prescribed nonzero limiting K. Repeated paired insertions preserve equal outer zero counts. A nonzero normalized limit minor therefore certifies a nonzero rational minor on the nonzero-edge locus; it does not assert literal rank at a disconnected zero-edge pencil. The boundary cores use the actual nonzero outer ratio, independently checked in the finite script.

4. **Paired insertion.** I tracked all sixteen interval endpoints in the pair matrix. For r,j at least six, insertion at edges 2 and m-4 places exactly one new isolated vertex in each positive interval and one in each negative interval. The extremal cases j=6 or r=6 remain valid: the shortened suffix starts at the left endpoint of the right cut, so it still includes the newly inserted vertex. All column pairs are multiplied by x in both components, the local denominator edges are merely reindexed, and the new cuts include 2 and (m+2)-4.

5. **Central insertion.** If j-r is at least four, insertion at r+1 lies inside every positive interval, including the shortest prefix and suffix, and outside every negative interval. The mapping is (p,q) to (xp,q). The reflected case gives (p,xq). The cut remains in the middle interval omitted from the reduced K ratio. This verifies iteration and the complete reduction from arbitrary ordinary characters to the 17 listed cores.

6. **Exceptional characters.** The single changed diagonal yields exactly the four displayed continuant identities. Consecutive unperturbed continuants are coprime by the recurrence and the absence of a factor h. The weighted-degree bounds make each possible polynomial syzygy coefficient zero; solving the resulting scalar coefficients gives the asserted four balanced forms in character zero and four pure weight-one forms in character one. I checked the recovery of all six zero-character forms, the two identities producing the additional weight-one forms, the three independent images modulo pure integer weight one, and the transposition/y-z symmetry for character minus one. These prove the lower bounds 6,7,7.

7. **A single pencil and a finite integer choice.** The independently nonzero minors lie in one irreducible Jacobi parameter space, so the finite open intersection is nonempty. Their product has parameter degree at most 8m^2-4m. The grid with 8m^2 positive integers in each coordinate is large enough and automatically keeps all diagonal and edge parameters nonzero. This proves existence without claiming an efficient selection algorithm.

8. **Homological consequence.** The previously reviewed exact bordered cancellation argument works with any number of independent normal columns. Thus the 8m-4 bound gives a loss of at most six relative to the torus upper-bound increment 8m+2. With the independently certified base epsilon_18=0, the stated bounds epsilon_m<=6(m-18), c_m>=4m^2-8m+110 and the strict padding comparison follow by direct arithmetic. No all-size zero-defect conclusion is inferred.

## Requested repairs and review scope

Only typography was requested: missing backslashes before `qquad` in the endpoint/one-basis displays and before `quad` in the zero-basis display. No mathematical repair was requested. No new external-source proof certification is claimed here. The dependency on the size-18 base case is the existing reviewed R-25 certificate.
