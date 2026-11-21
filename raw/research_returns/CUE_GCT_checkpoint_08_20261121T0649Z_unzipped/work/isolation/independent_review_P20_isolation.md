# Independent whole-proof review: P-20

Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I. Actual completed check recorded 2026-11-21T06:36:36.061094+00:00.
Exact file: `work/purity/P20_translation_block_pencils.tex`.
SHA256: `45e263ddf3de8b46b41159828f9fb853452e5c71cb16f4d94d6547e2be6ada18`.
Outcome: **PASS**. Full proof read and rederived; no numerical execution claimed.

## Scope

The first theorem requires a partition into consecutive blocks, degree one in each entire block, and formal common-translation invariance. It applies in every characteristic and arbitrary total block degree. The four-block corollary removes the translation hypothesis using the fully proved P-19. Neither ordinary unweighted SV evaluation nor arbitrary multiaffine blocks is asserted.

## Full checks

1. The coefficient of the common translation parameter separates into distinct block multidegrees. Because each entire block has degree one, the resulting vanishing derivative sum gives its full separate translation identity in every characteristic. Removing unused variables preserves formal generator membership and consecutive order.
2. At the cut after a block, coefficient rows from its earlier variables span the full rank because the last coefficient polynomial is their negative sum. At the cut immediately before the last variable, those same rows have rank r_b in one degree block; the nonzero last-variable term occupies a different degree block. Thus the intrinsic rank bound r_b+1<=3 is valid even though the H_i also contain preceding-block variables.
3. A smallest counterexample by number of blocks cannot have a rank-one block cut. The factorization uses disjoint variable sets, retains the homogeneous degree-one blocks, inherits width by complementary specialization, and inherits translation invariance by the highest homogeneous part. Prime ideal membership then gives a smaller counterexample. The block tensor factorization has independent prefix and suffix functions, so it makes every block coefficient-sum matrix zero.
4. A homogeneous linear 2x2 pencil of generic rank one has a polynomial rank-one factorization with one constant side. This forces one adjacent intrinsic block-cut rank to be one, contradicting minimality. Thus the pencils are generically invertible.
5. I checked the exact within-block rank identity: prefix-variable terms have rank equal to the stacked-row span of their coefficient matrices; suffix-variable terms have rank equal to the concatenated-column span. Independent preceding/following coefficient functions preserve these ranks. Complementary homogeneous degrees make them add.
6. The first prefix whose row span is two cannot be the last index, by the zero coefficient sum. It cannot be the first, because then all later columns lie in one line and their sum would make the first matrix singular. Earlier matrices share a row line, later matrices share a column line, and the pivot is their negative sum. The displayed factorization M=[U,b][a^T;V^T] and determinant product follow exactly, including characteristic two. Both linear determinants are nonzero because the original pencil is generically invertible.
7. The same one-pole center hits all these nonzero linear factors and both endpoint vectors simultaneously. Successive constant cut gauges normalize every invertible block constant. Rank-one endpoint updates are affine-linear in the entire endpoint block and have constant identity. No independent parameter is silently assigned to a block.
8. General multilinear pole extraction gives every first partial zero at this one-pole center under a hypothetical balanced two-pole identity. The nonzero row u0 annihilates the nonzero column v0 in dimension two, so that annihilator is exactly its line. Every u0 N_i lies on the line; all ordered coefficient products therefore vanish. This is a complete scalar contradiction, not merely preservation against constant boundary functionals.
9. For four blocks, the highest nonzero translation coefficient would inherit the witnessing coefficient-cut bounds by the leading-parameter limit. Its degree is at most three, so P-19/minimum-degree bounds exclude it. Translation invariance follows. The exact finite grids are I-40's denominator-safe selector product and amplitude simplex, giving 35(n+1)^2 at degree four with the stated working-field condition.

## Dependencies and verification limits

This check uses the already audited tensor-rank factorization, prime balanced ideals, general multilinear pole extraction, I-40 normalization/interpolation, and P-19, whose complete exact proof I independently read earlier in this run. No new external source or numerical experiment is claimed here. No mathematical repair was requested.
