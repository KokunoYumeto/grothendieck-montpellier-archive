# Separate post-CP29 outline: both stable quotients force opposite wild matrix entries

Written 2026-11-20 after B81 promotion and while B82 remains a separately audited candidate. Nothing in this note is a new promoted assertion. The current frozen CP29 sources are unchanged.

## Exact proposed hypotheses

Let p≥5, e=p(p−1), q=p², N=q−1, s=pN. Work over the common tame good field L/K of degree N, with algebraically closed residue and μp in K. Suppose an actual p³-torsion comparison has tame reducible residual representation, and both unequal-slope parameters are B_i=p²k_i with 1≤k_i≤p−2. The residual high lines are assumed exchanged by the actual comparison. The common finite determinant is nonsquare; normalize it to the primitive level-one character by a common finite tame height-one twist, which preserves the actual wild image and all L-valuations.

The equal-high alternative gives c1−B1=c2−B2 modulo N. Equality of finite determinants gives c1=c2 modulo p−1, so k1=k2 and then c1=c2 modulo N. Thus an unequal-character comparison in this sector must exchange the high lines.

## Both actual quotients

Each B_i>e, so the actual high quotient has parameter s−B_i=p(N−p k_i). A low quotient has parameter B_i/p=p k_i. Taking the quotient by either of the two common stable generic lines gives an actual p²-torsion isomorphism between these high and low quotients. The two new parameters divided by p are N−p k_i and k_j. Both are prime to p, and

N−p k_i ≥ 2p−1 > p−2 ≥ k_j.

If their residual action over L were tame, both first-level modules would be L-rational. Choosing a common vector outside both new high lines, the actual primitive p²-point coordinates have valuations b_i/p². Since both b_i are prime to p, the common point field has degree p² and supplies every first-level translation. A translation outside both high lines then has exact common lower break N b_i, forcing the unequal b_i to be equal. This is the direct point-field proof of the tame clause of B69; its proof does not use p∤e, but that extension must be explicitly written rather than citing the original prime-index theorem without qualification.

Hence each of the two actual quotient comparisons has nontrivial residual wild action.

## The actual lattice calculation

Put the two original common stable lines at Fp e1 and Fp e2. The original residual representation is L-rational, so every element of the full third-level wild image has matrix

ρ(g)=I+pA+p²B modulo p³.

For quotient by Fp e1, the actual Tate lattice is T'=T+Zp(e1/p). In its basis (e1/p,e2), the matrix is

[[ρ11, pρ12], [ρ21/p, ρ22]].

Its residual lower-unipotent coefficient is A21. For quotient by Fp e2 the analogous residual coefficient is A12. Thus the preceding two nontrivial quotient wild actions force both off-diagonal projections of the actual first congruence space W1 to be nonzero.

The residual tame matrix is diagonal, with eigenvalues α,β in Fp× and αβ equal to the normalized nonsquare determinant. Therefore α/β is nonsquare. If p≡1 mod4, neither 1 nor −1 is nonsquare, so the three conjugation weights 1,α/β,β/α are distinct. Exact tame projectors on the Fp-space W1 then give both E12 and E21 in W1.

The actual commutator identity modulo p³ gives [W1,W1]⊂W2, while pth powers give W1⊂W2. Thus W2 contains E12,E21 and diag(1,−1), three independent matrices. Consequently dim W1≥2 and dim W2≥3, and the actual wild image has order at least p⁵.

## Proposed consequence and limitations

If all details above pass a complete proof audit, then for p≡1 mod4 this removes the residual-tame both-divisible exchanged-line sector at wild orders ≤p⁴. Together with B81 and the still-separate B82, it would imply that every actual third-level different-character comparison at p=5,e=20 has wild image of order at least 3125, independent of residual type. It would not exclude any larger image, construct a counterexample, or settle the full index {2,3}.

For p≡3 mod4 the nonsquare ratio can equal −1. Then the two off-diagonal directions have the same tame weight, so nonzero projections alone do not supply both individual matrix units. That case is intentionally not covered. No computational result or source-read claim is attached to this outline.
