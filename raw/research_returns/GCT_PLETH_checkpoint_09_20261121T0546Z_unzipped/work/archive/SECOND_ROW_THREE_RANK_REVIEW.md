# A066 — independent review of the complete second-row-three rank law

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. I read all of `work/rectangular/second_row_three_canonical_rank_law.md`, CT.1–CT.20 and its transport and endpoint arguments. **PASS.** I also reread T032, C.4–C.15, for the exact balanced chart and its polynomial-extension criterion. This is a whole-proof review, not a claim to have rerun the author's 40 scalar or 680 coefficient checks.

## 1. The invariant algebra and its finite-rank endpoints

The row-power-sum proof in CT.4 is valid with the exterior signs retained. After choosing the displayed order of occupied row types, the injective-row sum \(A(S_1,\ldots,S_l)\) is a scalar multiple of the signed orbit sum. Two identical odd types have an odd row transposition in the stabilizer and give zero average; other stabilizer factors are the indicated factorials. In the product of the \(p_{S_i}\), grouping by the equality partition of the row assignments gives the discrete term \(A\) once. Every other nonzero term has fewer occupied rows, with its exterior reordering sign determined by the literal products. This is an induction on \(l\), so it proves generation in every finite row count.

The projection \(E\to\mathfrak h_a\) induces a surjective exterior algebra map and has an equivariant section. It is therefore surjective on invariants. Singleton row sums become zero and the remaining generators are precisely the two-form and the three-form in CT.4. The degree-three generator is odd and its square is zero over \(\mathbf Q\). Thus the displayed graded algebra morphism is defined and onto.

The exterior contraction \(\Lambda^2T\simeq\det(T)\otimes T^*\) gives exactly the two multiplicity-free families
\[
S_{(p,p,0)}T,\qquad S_{(p+1,p+1,1)}T.
\]
Skew Cauchy then leaves only tails \((2^p)\) and \((3,2^p)\), with invariant multiplicity at most one. The two-column family has already been proved in A064. For the cubic family, length kills \(j\ge a-1\); at \(j=a-2\), the actual determinant-column isomorphism gives \((\det\mathfrak h_a)^2\otimes\mathfrak h_a\), whose invariant space is zero. This handles \(a=2\) as well.

## 2. The nonzero cubic highest vector and the chart

Translation invariance of CT.8 follows from centering. Adjugate congruence shows that its vector-valued form transforms by \((\det g)^2g\). Its first component has lower-coordinate weight \((3,2,\ldots,2)\) and is killed by every indicated raising operator.

For CT.9, centering the columns of \(R\) has determinant one and transforms \(R^tR\) to \(\operatorname{diag}(a,S)\). Differentiating the weighted Cauchy–Binet identity gives
\[
\sum_{I\ni i}\det(R_I)^2
=\det S+a\,z_i^t\operatorname{adj}(S)z_i.
\]
Multiplication by \((z_i)_1\), summation, and \(\sum_i z_i=0\) give \(a f_a\) on the left of the corresponding identity. Substituting the mean and multiplying by \(a\) produces exactly the two coefficients \(a-s-1\) and \(-(s+1)\) in CT.9, and the factor \(a^2f_a\). This proof is polynomial, including singular Gram matrices. The resulting expression has degree at most three in every slot.

For CT.10, \(v^tD^{-1}v=s+1\), so the displayed inverse and determinant follow by direct multiplication and the one-rank determinant identity. The adjugate values are \(s\) on \(e_1\), \(2(s+1)\) on each other basis vector, and \(2(s+1)\) on \(v\). Their weighted sum is \(2s-4(s+1)=-2(s+2)\), proving nonvanishing even at the minimal number \(a=s+2\) of slots.

The powers of \(u\), the outside first-coordinate factors, and the remaining linear factor in CT.13 give exactly \(u^nH_a(y_i/x_i)\). Each slot has degree \(n\). Under T032 C.11 the first centered column is multiplied by \(u\); the highest weight has first lower degree three, so this substitution multiplies \(H_a\) by \(u^3\). The chart's factor \(u^{n-3}\) gives precisely CT.12. This verifies the actual flag morphism and all stable \(n\ge3\) multiplicities.

At \(n=2\), T032 C.15 identifies the possible line with the extension of \(u^{-1}G_{a,3,s}\). In the specialization \(x_1=0,y_1=e_1\), all minors not containing row one have the outside factor \(x_1^2\). Among the remaining summands only the linear term indexed by row one survives, with positive coefficient \(a-s-1\). The remaining rows \(0,e_2,\ldots,e_s\) produce a nonzero minor, so the sum of squares is nonzero. Thus \(x_1\) does not divide \(G_{a,3,s}\), and the entire unique possible invariant line fails the exact extension condition. This proves the \(n=2\) exclusion by the explicit morphism.

## 3. The exact normalized scalar

The degree-\(d\) moment in CT.15 is the symmetric sum over ordered distinct indices divided by \((n)_d\). Its contraction with a coordinate monomial agrees with the multinomial pairing, including repeated coordinates. The translation covariance of this functional transfers the translation identity of \(H_a\), so the mean of all \(v_k\) may be removed by the literal common translation.

With zero mean, subtracting repeated indices gives
\[
C_2=-\frac{S_2}{n(n-1)},\qquad
C_3=\frac{2S_3}{n(n-1)(n-2)}.
\]
For the third identity each of the three exactly-two-equal patterns sums to \(-S_3\), while the all-equal pattern sums to \(S_3\); hence the distinct-index sum is \(2S_3\).

The outside linear terms in CT.9 have zero independent-slot evaluation. For one minor, replacing every row functional by \(L+tL(w_1\,\cdot)\) and differentiating the two-permutation determinant identity gives exactly
\[
(s+1)!\operatorname{tr}(\operatorname{adj}(B)B_1).
\]
Here \(B=\operatorname{diag}(1,C_2)\). Its adjugate is block diagonal as a polynomial identity, so only the lower block \(\operatorname{adj}(C_2)\) and the lower block \((C_3)_{1pq}\) of \(B_1\) contribute. The number of minor subsets times their inside coefficient is
\[
\binom a{s+1}(s+1)!(a-s-1)=\frac{a!}{(a-s-2)!}.
\]
Adjugation contributes degree \(s-1\) in the scalar multiplying \(S_2\); the third moment contributes one further factor \(n(n-1)(n-2)\). Finally \(H_n=n^2f_n\). These equalities give exactly
\[
h_{a,n}G_{a,n,s}
=
\frac{2(-1)^{s-1}a!}
{(a-s-2)!\,n^{s+2}(n-1)^s(n-2)}
G_{n,a,s}.
\]
No moment matrix was inverted in this deduction. The common-translation identity and multihomogeneity extend the affine calculation to the dense first-coordinate chart, and polynomiality extends it everywhere.

For \(n<s+1\), the target minor sum is empty. At \(n=s+1\), its inside coefficient and outside sum both vanish. For \(n\ge s+2\), the earlier centered configuration proves nonvanishing. The scalar is nonzero throughout its stated \(n\ge3\) domain. All endpoints therefore use actual polynomials and never substitute into the \(n-2\) denominator at \(n=2\).

## 4. The complete band and transport

Transposition of the normalized tensor regrouping preserves rank on every finite multiplicity block. With \(j=s-1\), the scalar proves rank one exactly for \(j\le n-3\). Combining this with A065 and the complete invariant-algebra exclusions proves CT.1–CT.3, including the direct-sum cokernel and all empty ranges.

The degree-one and outer-degree-two cases are separately identified by their actual maps. Rational tensor, Young, Reynolds, exterior, and coefficient maps commute with frame changes; their constant-rank kernels and images glue to the stated associated subbundles. The source locators in the concluding dictionary agree with the previously checked SGA6, SGA3, EGA, and A012 scopes. This review did not repeat those primary-source readings; it checked the maps asserted here against that established dictionary.

