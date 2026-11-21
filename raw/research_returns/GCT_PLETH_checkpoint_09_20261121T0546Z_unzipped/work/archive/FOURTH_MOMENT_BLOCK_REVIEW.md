# A069 — independent review of the fourth-moment canonical block

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. I read the complete R038 report `work/rectangular/fourth_moment_canonical_block.md`, FM.1–FM.17, including all endpoint and transport arguments. **PASS.** This is a whole-proof reading; the author's 160 expanded pairings and 46 binary-weight checks were not rerun.

## 1. Exact invariant and extension spaces

The equality-partition expansion of power sums spans the symmetric quartics. Restriction to \(p_1=0\), together with rational averaging, leaves the actual invariant span of \(P_a,K_a\). The two centered evaluations for \(a\ge4\) have determinant sixteen and prove independence. For \(a=2,3\), the displayed fourth Newton identity gives \(K_a=2P_a\), with a nonzero generator.

The two coefficients in FM.5 follow directly by setting all variables except \(w_i\) to zero:
\[
[w_i^4]P_a=\frac{(a-1)^4+(a-1)}{a^4}
=\frac{(a-1)(a^2-3a+3)}{a^3},\qquad
[w_i^4]K_a=\left(1-\frac1a\right)^2.
\]
Their unique cancelling combination is exactly \(J_a\). For a symmetric translation-invariant quartic, the coefficient of \(w_i^3\) in the total derivative is \(4A+(a-1)B\). Thus cancellation of the pure fourth powers also cancels every \(w_i^3w_l\). These are all monomials of per-variable degree greater than two. Hence \(J_a\) has precisely the polynomial extension asserted for both inner degrees two and three. At \(a=n=3\), the sole invariant \(P_3\) has a nonzero fourth-power coefficient and fails extension. This verifies all target dimensions and every small-degree endpoint by the actual chart.

## 2. Formal sample moments and the full matrix

The centered expansions FM.8 are exact. With first moment zero, the only surviving index patterns in FM.9 are the all-equal pattern and the indicated two-pair patterns. Their coefficients are \(a\) and \(a(a-1)\), with the factor three for the three pair partitions of four positions. Substitution yields all four rational coefficients \(C_4,C_{22},D_4,D_{22}\) exactly as displayed.

For a split form, the normalized symmetric pairing gives the ordered-distinct-index average. The fourth numerator is \(24e_4=3K_n-6P_n\); the second-moment square is \(K_n/[n^2(n-1)^2]\). The resulting matrix FM.13 therefore has the stated columns and rows, including the minus-six coefficient and every denominator.

The remaining determinant numerator factors as
\[
(a^2-3a+3)(a^2-2a+3)-3(a-1)(2a-3)
=a^2(a-2)(a-3).
\]
This gives the exact determinant
\[
-\frac{6(a-1)^2(a-2)(a-3)}
{a\,n^3(n-1)^3(n-2)(n-3)}.
\]
It is nonzero for \(a,n\ge4\). For the requested \(h_{n,a}\), the inverse is correctly \(M_{n,a}^{-1}\), applied to target coordinates and then expressed in the source basis with the indices reversed. Thus the report supplies actual preimages for both copies.

## 3. The inner-degree-two and three maps

The \(J_a\) combination cancels the \(\mu_4\) coefficient exactly. Its remaining coefficient is
\[
a(a-1)C_{22}-(a^2-3a+3)D_{22}
=-a(a-1)(a-2)(a-3).
\]
Because \(J_a\) has per-slot degree at most two, extending its first two moments arbitrarily to third and fourth moments does not change its value. This proves the literal identity
\[
h_{a,n}\widehat J_{a,n}
=-\frac{a(a-1)(a-2)(a-3)}
{n^2(n-1)^2}\widehat K_{n,a},
\qquad a\ge4,\ n=2,3.
\]
Its target polynomial and scalar are nonzero. Transposition preserves the finite multiplicity-block rank, giving the stated result with the parameters reversed as well. No vanishing factor \(n-2\) or \(n-3\) is used at these endpoints.

Translation and separate homogenization extend the chart computations to polynomial identities. Cauchy/Young functoriality identifies these same two-row multiplicity spaces in every vector-space dimension at least two. The associated-bundle construction therefore transports the same matrices, inverse matrices, and endpoint maps. This completes FM.1 and all claimed transport statements.

