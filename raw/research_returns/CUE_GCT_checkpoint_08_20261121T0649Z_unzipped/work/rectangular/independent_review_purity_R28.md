# Independent whole-proof review of R-28

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run CUE_GCT-20261121-purity. Actual review completed 2026-11-21 05:35:25 UTC.

**PASS** after reading the entire fragment, SHA256 `36b154bb06c3b0e2ff685d50ba762089ba14c3e30f4ccdca776ecd85df02c8d5`.

The exact new-variable determinant dimension follows from independent cofactor blocks at a quaternary pencil and the explicit finite left-right stabilizer witness. Each new block has its own new-variable multidegree. The generic fiber bound is correct even when r exceeds n^2. The quaternary dimension/cofactor assertions are used as the cited R-17/R-23 inputs.

The padded image gains exactly r-1 dimensions: a nonempty irreducible open exists, and unique factorization recovers the nonlinear factor and the padding line from a generic product. The argument is projective before returning to affine-cone dimension, so no scalar dimension is counted twice.

I checked the complete common cyclic family and its two perfect matchings, including the determinant corner sign. The inverse image of the stable locus is a nonempty open by G-22. The displayed q*=P+epsilon z^m is Eisenstein as a polynomial in z: the leading coefficient is a unit, every other coefficient is divisible by x1, and the constant coefficient is not divisible by x1^2 because r>=3. Its infinitesimal stabilizer argument is exact: a single replacement in P cannot produce a pure monomial; the pure coefficients first force Bz=(c/m)z; each off-diagonal entry then has a distinct monomial P*x_i/x_j, so all vanish and the remaining diagonal entries are equal.

The three open sets meet in the irreducible parameter space. After fixing q, the stable padding lines form a nonempty open; avoiding fixed loci of the finite projective stabilizer makes the padded form projectively free. Unique factorization distinguishes the nonlinear factor and the line even when the padding exponent is one. A scalar symmetry of the enhanced tensor therefore comes from the center, whose exponent ns-e=r*nu_r is trivial.

Finally closed-orbit separation proves gcd one for the nonvanishing invariant degrees, and the cited numerical-semigroup argument gives occurrence in both cones at every integer stretch at least beta^2. The distinction between absence of an invariant-degree period and efficient coefficient extraction is correctly maintained.

I also read the full G-22 dependency during this review, as recorded in `work/root/independent_review_purity_G23.md`. G-21/R-17/R-23 and the established Mukai/semigroup inputs were accepted with their existing source/review records; no fresh complete source audit or numerical certificate rerun is claimed.
