# Independent whole-proof review of K-012

Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro, effort not exposed. Date: 21 November 2026 UTC. Reviewed the complete theorem and proof in `branches/kronecker/ANTIPODAL_STABILIZER.tex`.

**Outcome: PASS.** No gap was found in the projective stabilizer or finite central extension argument. This review is mathematical, not proof-assistant certification. It assumes the theorem's stated centralizer and connected-stabilizer hypotheses. The finite arithmetic establishing those hypotheses for the K-010 list is being checked separately by root and is not certified by this review.

## Centralizer descent and the abelianization

If a lift of an element centralizing the image of g conjugates g to sg, then taking M-th powers gives s_i^M=1 and taking each factor's determinant gives s_i^n=1. The coprimality of odd n and M=2^m makes every scalar s_i equal to one. Thus the centralizer in H=L/S really has order M; it is not merely the image of a smaller centralizer without justification. The order of the image of g is M because its determinant-product character has that exact order.

Character column orthogonality then gives a total squared-character value M. The first M powers of χ are distinct linear characters, and each contributes one. There can be no further linear characters. Thus the abelianization has order M, is cyclic, and χ identifies it with μ_M. The argument does not assume that the kernel of χ is solvable.

## Finite central extension and Fourier separation

Normalizing the first two determinants gives a surjection from the displayed finite group to H with kernel Z=μ_n². It is an algebraic finite group because every fiber has n² points. The original g can be normalized by scalars in μ_M: taking n-th powers permutes μ_M. Its character still has order M, so the normalized element has exact order M, and scalar normalization preserves antipodal freeness of a spectrum.

Its centralizer in the finite extension is Z⟨g⟩, of order n²M. For odd u, g^u generates the same cyclic group. Since Z has odd order, g^u z has order M·ord(z) whenever z is nontrivial. These elements cannot be conjugate to g^u. Character orthogonality therefore gives the stated finite Fourier system on Z, and its inversion yields S_ω(u)=M for every central character. All normalizations and complex conjugations in that identity are consistent.

## Twists and the Parseval argument

A nontrivial self-twist by χ^j would make the g-spectrum invariant under a nontrivial two-power root of unity. Every such root generates a subgroup containing −1, so an antipodal-free spectrum excludes every such self-twist. The M distinct twists retain the same central character and have equal squared trace magnitude at each g^u with u odd. Their contribution to S_ω(u)=M gives the bound one on every such trace.

For h=M/2 the odd Fourier characters are orthogonal on exponent differences in the half-range 0,…,h−1. Thus the displayed Parseval identity has the factor 2/M, with no missing factor of two. The integer differences c_j have sum of squares at most one. Antipodal freeness gives dim V=Σ|c_j|, so each irreducible constituent is a line. Since the center acts through the same scalar on every line of one tensor factor, their character ratios descend to H and are powers of χ. The kernel of χ therefore acts projectively trivially on that factor.

## The connected pointwise stabilizer

The simultaneous intertwiner space E={(B,D):BM_i=M_iD} is a unital associative algebra: multiplication takes (B₁,D₁),(B₂,D₂) to (B₁B₂,D₁D₂). Its units are precisely the pairs with both matrices invertible, since the intertwining identities imply the corresponding identities for inverses. They form a nonempty Zariski-open subset of the affine vector space E, hence are connected. The map (B,D)↦(B,D^{-t}) is an algebraic group isomorphism to the subgroup fixing the first factor pointwise; indeed BM_i Cᵗ=M_i is equivalent to BM_i=M_i C^{-t}. No invertible slice is needed.

This connected subgroup is contained in L⁰=S and contains all scalar pairs (bI,b^{-1}I), so it equals that one-dimensional subgroup. Each element of ker χ can be represented with first factor scalar and normalized to first factor identity using S. It therefore lies in S, proving ker χ is trivial in H. Finally an SL_n³ stabilizer element has χ=1, hence lies in S. The remaining scalar subgroup is precisely the ineffective kernel, giving trivial effective stabilizer.

The repeated-spectrum application also has the correct qualitative mechanism: a two-dimensional linear operator preserving three distinct projective lines must be scalar. The existence of those lines and the listed rank/Smith computations remain separate finite-input checks.
