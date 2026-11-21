# Direct positive formulas on every proper fundamental face of outer degree four

## T-031. Statement and explicit formulas

Let \(\lambda=(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\vdash4n\), allowing trailing zero parts. Define the fixed binary-quartic count
\[
\begin{aligned}
F_4(N,K)=\sum_{\varepsilon=0}^1\#\{(a,b,c,d)\in\mathbf Z_{\ge0}^4:\quad
&N=a+2b+2c+3d+3\varepsilon,\\
&K=2b+4c+6d+3\varepsilon\}.
\end{aligned}
\tag{F.1}
\]
Set it equal to zero when \(N<0\), \(K<0\), or \(K>2N\). T-021–T-022 prove the exact algebra map and basis giving
\(F_4(N,K)=a_{4,N}^{(4N-K,K)}\) for valid indices. Each term in (F.1) is one bounded four-variable polytope.

For the lower face \(\lambda_3=\lambda_4=t\), put \(N=n-t\), \(K=\lambda_2-t\). Then
\[
\boxed{
a_{4,n}^{\lambda}=
\begin{cases}
F_4(N,K),&t\text{ even},\\
F_4(N-3,K-6),&t\text{ odd}.
\end{cases}}
\tag{F.2}
\]
The invalid-index convention includes every boundary case.

For the upper face \(\lambda_1=\lambda_2=H\), put \(N=H-n\), \(K=H-\lambda_3\). Then
\[
\boxed{
a_{4,n}^{\lambda}=
\begin{cases}
F_4(N,K),&H\text{ even},\\
F_4(N-3,K-6),&H\text{ odd}.
\end{cases}}
\tag{F.3}
\]

For the middle face \(\lambda_2=\lambda_3=\beta\), put
\[
R=\min(\lambda_1-\beta,\beta-\lambda_4)-6(\beta\bmod2).
\]
T-025 gives the single-polytope formula
\[
\boxed{a_{4,n}^{\lambda}
=\#\{(c_2,c_3,c_4)\in\mathbf Z_{\ge0}^3:
2c_2+3c_3+4c_4=R\}.}
\tag{F.4}
\]
Thus all proper faces of the three simple-root fundamental coordinates of \(A_4\), with every determinant shift retained, have direct bounded-polytope formulas. Indeed a proper face sets at least one of \(\lambda_1-\lambda_2\), \(\lambda_2-\lambda_3\), \(\lambda_3-\lambda_4\) equal to zero, exactly the three cases above. The formulas agree on their intersections because the proofs identify each with the same balanced Howe multiplicity. T-030 supplies another explicit presentation on the paired-row intersection.

## 1. Exact determinant shift

For any rank \(m\), a partition \(\eta\), and \(t\ge0\), the canonical highest-weight pairing identifies
\[
S_{\eta+(t^m)}E\simeq(\det E)^t\otimes S_\eta E.
\tag{F.5}
\]
One construction is to append \(t\) full-height columns to the column exterior-power realization of the Schur module. Those columns contribute \((\Lambda^mE)^{\otimes t}\); the Cartan product with the original Schur module is nonzero on its highest vector and has the displayed irreducible highest weight, giving the isomorphism. On the balanced weight \((n^m)\), this gives the exact \(S_m\)-module morphism
\[
(S_{\eta+(t^m)}E)_{(n^m)}
\simeq\operatorname{sgn}^{t}\otimes
(S_\eta E)_{((n-t)^m)},
\tag{F.6}
\]
because literal permutation matrices have determinant equal to their sign.

Apply this with \(m=4\), \(\eta=(\lambda_1-t,\lambda_2-t,0,0)\), and \(t=\lambda_3=\lambda_4\). Put \(A=\lambda_1-t\), \(B=\lambda_2-t\), \(N=n-t\). The equality \(A+B=4N\) and the partition inequalities imply \(N\ge0\) and \(0\le B\le2N\). By the refined balanced Howe identity T-003, (F.6) identifies the desired coefficient with the multiplicity of \(S_{(A,B)}\mathbf Q^2\) in
\[
\operatorname{Sym}^4(\operatorname{Sym}^N\mathbf Q^2)
\quad(t\text{ even}),\qquad
\Lambda^4(\operatorname{Sym}^N\mathbf Q^2)
\quad(t\text{ odd}).
\tag{F.7}
\]
The restriction to two variables is exact: the Schur coefficient for a partition of length at most two is unchanged by evaluating the character in two variables, while every partition of greater length vanishes there.

## 2. Binary alternants and the exact exterior-to-symmetric map

The following map works in every number \(m\) of binary slots, so we state and prove it in that form. Let \(F=\mathbf Q^2\), and write \(v_i=(a_i,b_i)\) for the variables in slot \(i\). Put
\[
[ij]=a_i b_j-a_j b_i,\qquad
\Delta_m=\prod_{1\le i<j\le m}[ij],\qquad
M=\binom m2.
\tag{F.8}
\]
The polynomial \(\Delta_m\) has degree \(m-1\) in every slot, transforms by the sign under slot permutations, and spans the \(GL(F)\)-character \((\det F)^M\).

Every alternating polynomial of equal degree \(N\) in all \(m\) slots is divisible by \(\Delta_m\). To see this, fix a pair \(i,j\). On the dense part of the bracket hypersurface where \(v_j=c v_i\), equal slot homogeneity gives
\[
f(\ldots,v_i,\ldots,c v_i,\ldots)
=c^N f(\ldots,v_i,\ldots,v_i,\ldots)=0,
\]
since interchanging the equal slots negates an alternating polynomial. The bracket \([ij]\) is an irreducible determinant polynomial, so it divides \(f\). Distinct brackets are nonassociate irreducibles in the polynomial unique factorization domain; therefore their product divides \(f\). Its quotient has equal slot degree \(N-m+1\), and is symmetric because numerator and denominator have the same permutation sign. Conversely multiplying any symmetric polynomial of that slot degree by \(\Delta_m\) produces an alternating polynomial of degree \(N\) in each slot. If \(N<m-1\), divisibility leaves a negative degree in each slot, so the alternating space is zero.

Multiplication by this explicit polynomial therefore gives the \(GL(F)\)-equivariant isomorphism
\[
\boxed{
\Lambda^m(\operatorname{Sym}^N F)
\simeq(\det F)^{\binom m2}\otimes
\operatorname{Sym}^m(\operatorname{Sym}^{N-m+1}F)
\quad(N\ge m-1),}
\tag{F.9}
\]
and the left side is zero for \(N<m-1\). The identification of alternating tensors with \(\Lambda^m\), and of symmetric tensors with \(\operatorname{Sym}^m\), is the characteristic-zero symmetrizer identification. The determinant factor in (F.9) records the actual \(GL_2\) action of \(\Delta_m\), rather than only its degree.

For \(m=4\), (F.9) shifts the inner degree by 3 and both output parts by 6. Thus the odd case of (F.7) has multiplicity
\[
[S_{(A-6,B-6)}F:\operatorname{Sym}^4(\operatorname{Sym}^{N-3}F)]
=F_4(N-3,B-6),
\tag{F.10}
\]
with value zero when \(N<3\) or \(B<6\). If these inequalities hold, \(A\ge B\) and \(A+B=4N\) automatically give a valid partition after the shift. Equations (F.7)–(F.10) prove (F.2), including its boundary conventions.

## 3. Exact complement duality and the upper face

For a rank-\(m\) space \(E\), a partition \(\lambda\) of length at most \(m\), and an integer \(H\ge\lambda_1\), define its rectangular complement
\[
\widehat\lambda=(H-\lambda_m,\ldots,H-\lambda_1).
\tag{F.11}
\]
There is a perfect equivariant pairing
\[
S_\lambda E\otimes S_{\widehat\lambda}E\longrightarrow(\det E)^H.
\tag{F.12}
\]
To construct it, place \(\lambda\) in an \(m\times H\) rectangle. Pair each column exterior power \(\Lambda^j E\) with the complementary \(\Lambda^{m-j}E\) by exterior multiplication into \(\det E\); reverse the order of the complementary columns to recover the partition (F.11). Applying the Schur/Cartan projections gives the equivariant pairing (F.12). It is nonzero: a highest column tensor and the complementary lowest column tensor wedge to a nonzero volume in every column. The two irreducible modules are contragredient after the displayed determinant twist, as their highest weights show, so Schur's lemma makes the induced pairing perfect. Equivalently,
\[
S_\lambda E\simeq(\det E)^H\otimes(S_{\widehat\lambda}E)^*.
\tag{F.13}
\]
On balanced weights this gives the exact module identity
\[
(S_\lambda E)_{(n^m)}
\simeq\operatorname{sgn}^{H}\otimes
\left((S_{\widehat\lambda}E)_{((H-n)^m)}\right)^*.
\tag{F.14}
\]
Since Specht modules are self-dual and tensoring by sign conjugates their partitions, T-003 yields the full coefficient equality
\[
p_{\mu,(n)}^\lambda
=p_{\mu^{[H]},(H-n)}^{\widehat\lambda},
\qquad
\mu^{[H]}=\begin{cases}\mu,&H\text{ even},\\\mu',&H\text{ odd}.\end{cases}
\tag{F.15}
\]
All quantities are polynomial representations: \(H\ge\lambda_1\ge n\), and \(|\widehat\lambda|=m(H-n)\). Thus the complement and the inner degree are nonnegative. Equation (F.14), not a dimension-only substitution, explains the sign and duality in (F.15).

For the upper face of rank four, take \(H=\lambda_1=\lambda_2\). Then
\[
\widehat\lambda=(H-\lambda_4,H-\lambda_3,0,0),
\qquad N=H-n,\quad K=H-\lambda_3.
\]
Its first two parts sum to \(4N\). Formula (F.15) turns the original symmetric outer coefficient into the symmetric binary coefficient when \(H\) is even and the alternating binary coefficient when \(H\) is odd. Apply (F.9) in the latter case. This proves (F.3) and all its edge cases.

## Provenance and scope

The binary-quartic presentation used in (F.1) is classical and is proved with the exact normalizer-algebra morphism in T-021–T-022; the primary Grace–Young locators and direct symbolic checks are recorded there. Formula (F.9) is the classical binary Vandermonde factorization, proved here to fix its slot grading, determinant power, and zero range. Equations (F.5) and (F.12) are the actual Schur-module maps carrying the formulas across determinant shifts and complementary partitions. The result completes all proper fundamental faces of the symmetric-outer \(A_4\) algebra. T-032–T-036 subsequently identify the full-face extension through an exact flag chart and four-point vanishing model, and T-037 completes the positive formula for every outer partition of four.

An independent exact cycle-index/Murnaghan–Nakayama calculation passed all 197 lower- and upper-face cases through inner degree 6. The receipt `work/rectangular/OUTER4_PAIRED_AND_PROPER_CHECK.tsv` also includes the 140 paired-row cases of T-030, for 337 total checks; reproduction code is `work/rectangular/verify_outer4_faces.py`. The independent proof reading checked the divisibility map, every zero-range convention, the complement pairing, and the literal determinant signs. T-032–T-034 subsequently give direct chamber formulas for every outer Schur label in \(\lambda_2\le n\) and \(\lambda_3\ge n\).
