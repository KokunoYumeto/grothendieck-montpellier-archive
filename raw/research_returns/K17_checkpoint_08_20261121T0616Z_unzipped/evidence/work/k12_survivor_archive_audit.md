# Independent whole-proof and exact-certificate audit: the orientation survivor

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; reasoning effort not exposed.

**Verdict: PASS.** The explicit lattice proves the existence of a rank-ten projective degree-twelve Voronoi cell whose integral stabilizer preserves orientation. It disproves the strategy of removing every target cell by an orientation-reversing stabilizer. It proves neither a nonzero homology class nor nonzero K12.

Read the whole `work/k12_orientation_survivor.md`, the whole `work/k12_survivor_section.tex`, and every line of both the original exact certificate and the new standalone `work/k12_survivor_certificate.py`. Also read and reran the independent signed-column symmetry enumeration `work/k12_trimodular_extremal_check.py`. Reran both exact minimum certificates successfully. The standalone verifier uses hard-coded integers and only the Python standard library; it has no floating discovery or classification coverage dependency.

Reviewed hashes:

- Markdown: `fe926700481d5554cc4eecf6a7a560acdeb76a874abe49caecfee44a478dc047`.
- Standalone certificate: `e9e965761194558e02355c4c892235143a110c4da09d65922001c6b2e8e8893f`.
- TeX: `36cb756b94cc829736ba2db7d4f0a93e0f67c6f5706bbd878a76b55ee4baf0fc`.

## 1. Exact lattice, positivity and exhaustive minima

The matrix G and the twelve proposed minimum vectors in the final TeX agree entry by entry with the hard-coded standalone data. The certificate performs exact Fraction LDL decomposition, tests all nine pivots positive, and reconstructs every entry of Q=LDL^t. This proves positive definiteness, rather than relying on approximate eigenvalues. Every proposed vector has norm exactly one.

For z∈Z^9, the identity z^tQz=Σ_i D_i(z_i+Σ_(j>i)L_(j,i)z_j)^2 makes descending-coordinate enumeration exhaustive. All contributions are nonnegative. At each node, with rational shift a/b and remaining budget R, the only permitted integers satisfy (bz_i+a)^2≤(R/D_i)b². Because the left side is an integer square, computing M=isqrt(floor((R/D_i)b²)) is exact. The code's lower endpoint −floor((M+a)/b) is exactly ceil((−M−a)/b); its upper endpoint floor((M−a)/b) is also correct. Every integer in that interval is visited. Previously assigned later coordinates are the only ones used in the shift, so stale earlier coordinates cannot affect the recursion. At a leaf the full norm is recomputed and compared with the accumulated rational sum. The zero vector is omitted explicitly.

The independent rerun returns 326 visited nodes and exactly 24 nonzero vectors of norm at most one, equal to the twelve proposed pairs. Hence the minimum is one and that list is complete. Exact elimination on the upper-triangular entries of the twelve rank-one matrices gives rank twelve. Scaling Q to integral Gram matrix G preserves this minimum configuration; thus no integrality issue is hidden by normalization.

## 2. The integral relation identification

The first nine minimum columns are I9, so V maps Z^12 onto Z^9. Its integral kernel has the explicit basis B0=[−A^t | I3]. The code chooses a determinant-±1 three-column basis of the displayed relation configuration, inverts it exactly by cofactors, and moves it to the final three positions. This is an integral unimodular row change and a permutation, and the normalized matrix is precisely B0. The assertion B0 V^t=0 is checked coordinatewise. Therefore the quotient is the actual lattice Z^9, not a finite-index substitute.

The original relation columns, after changing signs of representatives as necessary, are exactly the three axis columns and the three finite fibers printed in the proof. Every 3×3 minor is checked, with maximum absolute value three and a unit minor. For V=[I9|A] and B0=[−A^t|I3], complementary maximal minors agree in absolute value, by the usual block-determinant expansion; the unimodular row change preserves these absolute values. Thus the maximum index among nine independent minimum columns is exactly three.

## 3. Full stabilizer classification and parity

A lattice automorphism preserving the perfect cone must permute its extremal rank-one rays. Every minimum vector is primitive (here this follows directly from its coordinates), so an integral invertible map can only send it to plus or minus another listed minimum vector. It therefore preserves the full integral kernel of V. Conversely a signed permutation preserving that kernel induces an integral automorphism of the quotient. This validates use of the entire relation lattice for the cell stabilizer, rather than only a subgroup of norm isometries.

An induced U∈GL3(Z) preserves contents of vectors. The unique content-three pair ±3e1 therefore forces Ue1=±e1. Multiplying by −I permits Ue1=e1. In the quotient by Ze1, the three signed primitive ray classes have multiplicities 3,2,4, so each is fixed separately. The images of e2 and e3 must be ± themselves modulo Ze1, and preservation of the ray e2+e3 forces the two signs to agree. Thus U has the triangular form printed in the proof.

For quotient sign +1, a finite interval invariant under translation has translation zero, giving x=y=0. For quotient sign −1, canonicalizing the sign sends the e2 fiber parameter t to −t−x. Its interval {−2,−1,0} forces x=2; the e3 interval {−1,0} forces y=1. Their sum three gives the required reversal of the four-element third interval. Hence the entire group is exactly {I,−I,J,−J}. No other quotient permutation is allowed because the multiplicities differ.

On pairs, −I is trivial. J reverses intervals of cardinalities 3,2,4, giving 1+1+2=4 transpositions and fixing all three axis pairs. Every symmetry therefore has even pair permutation. The standalone exhaustive enumeration corroborates this: the images of a fixed unimodular basis must be an ordered triple among the 24 signed columns with determinant ±1. The code enumerates every such triple, builds its unique integral U, and tests preservation of all signed columns. It returns exactly four matrices, all even. There is no untested finite symmetry subgroup assumption.

Since the twelve quadratic rays are independent, the determinant of the stabilizer on their span is exactly the sign of that permutation. The sum of the primitive ray generators is fixed, so removing the positive radial direction does not change the orientation sign on the projective cell.

## 4. Orthogonal extension and exact scope

For Q'=Q⊥[1], each vector with both components nonzero has norm at least two. Thus the new complete minimum set is the old 24 vectors together with ±e10. Their quadratic rays have rank thirteen: the old rays occupy the first 9×9 block, and the last ray has a nonzero final diagonal entry. The lattice is well rounded because these vectors span R10.

The relation matrix acquires one zero column. It is the only zero column, so every induced signed permutation fixes that last pair. On the other twelve columns it is one of the four already classified symmetries, all even. The sign of e10 itself does not change its quadratic ray. Every cell stabilizer therefore preserves orientation. Any full minimum basis must contain the last vector, and its remaining determinant is one of the old nine-vector determinants, so the maximal index remains three.

The resulting perfect cone has dimension thirteen and projective degree twelve. It meets the full-rank part of the Voronoi space, so it supplies an orbit generator in the relative chain group. Its orientation coinvariants are nonzero over Z[1/13!]. This is a chain-level statement only: neither the boundary nor the incoming image has been computed, and the proof makes no homology or K12 nonvanishing claim.

## 5. Provenance limits

The classification reference explains how the candidate was found. Its completeness is not used by this explicit existence proof. This audit does not re-audit that classification or claim to have enumerated the surrounding Voronoi complex. The auxiliary exclusion of the first discovered template was also checked by rerunning its exact six-term quadratic identity, but that exclusion is unnecessary for the survivor proposition.
