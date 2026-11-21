# Independent audit: removing maximal-index-one degree-twelve cells

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026. Effort not exposed. **PASS for the stated restricted orientation theorem**, including the new quadratic-independence lemma. This does not prove that all target cells have maximal index one, nor that the remaining K12 homology groups vanish.

I read the entire first version of `work/k12_orientation_attempt.md`, then independently reconstructed the updated §§3.1–3.2 after the simpliciality assumption was removed. The nontrivial-glue limitation remains essential.

## Quadratic independence

For a simple totally unimodular matrix V, every nonzero column remains nonzero modulo2. Two columns agreeing modulo2 have the same support; if they do not differ by one global sign, a two-row minor has determinant ±2. Thus the mod2 columns are distinct nonzero vectors.

Take a minimal nonempty binary cut C. Its complementary columns have rank at most N−1. If that rank were at most N−2, adding one column of C would still leave a proper subspace. A nonzero annihilator of this larger span has a nonempty proper cut inside C, because V has full row rank. This contradicts minimality. The complementary rank is therefore N−1.

Total unimodularity makes ranks over Q and F2 agree for every column subset. A basis of N−1 complementary columns and one column of C is unimodular. Its dual functional has values0 on the complement and ±1 on C, by the maximal-minor formula. Applying a proposed real quadratic relation to this functional gives the sum of its coefficients on C equal to zero.

Every binary cut decomposes into disjoint minimal nonempty cuts by repeated subtraction in the binary row space. Hence the coefficient sum vanishes on every cut. The distinct nonconstant characters b ↦ (−1)^(b·v_i) are orthogonal on F2^N; applying orthogonality to the resulting cut equations gives each coefficient zero. This proves quadratic independence with no general simpliciality assumption.

## Integral involution and its orientation

If every independent maximal subset of minimal vectors is a basis of the actual lattice, choosing one such basis writes V=[I A], and all minors of A are0,±1. The relation matrix B=[−A^t I] is also totally unimodular. Its row lattice is the actual integral kernel of Z^s → Lambda, not merely a rational relation space.

I freshly opened Heller's primary paper and read Theorem(4.2), including the projection lemma and the complete proof on pp.1358–1360. It bounds a rank-c signed Dantzig system by c(c+1) nonzero vectors, so there are at most c(c+1)/2 nonzero directions. The lattice interpretation in §6 p.1364 was also read. URL: https://msp.org/pjm/1957/7-3/pjm-v7-n3-p07-p.pdf ; retrievals `turn884950134view0`, `turn930356197view0`.

The stated inequality forces either two zero columns of B or two equal signed nonzero columns. After a harmless sign change, swapping those coordinates preserves its integral row lattice and descends to an integral involution of Lambda. It transposes exactly two quadratic rays. Their independence gives determinant−1 on their span. The radial direction is preserved positively, so the projectivized cell orientation also reverses.

The preceding independence lemma gives s=r=13 for any maximal-index-one degree12 cell. For N=9, c=4 and13>11; for N=10, c=3 and13>7. Both ranks are therefore covered. Inverting2 kills each such oriented-cell contribution.

## Scope

The example Lambda=Z^N+Z((e_1+...+e_5)/2), N≥6, has precisely the minimal pairs ±e_i because every nonintegral vector has squared norm at least5/4. Swapping e_1 and e_6 permutes these rays but changes the unique nonzero glue coset, so it is not a lattice automorphism. The example correctly blocks an unqualified extension of the argument to nonunimodular cells. Other symmetries may still reverse that particular cell; it is not represented as a counterexample to the desired full vanishing.
