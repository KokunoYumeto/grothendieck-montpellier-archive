# A065 — independent review of the complete second-row-two rank law

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. The complete report `work/rectangular/second_row_two_canonical_rank_law.md`, SR.1–SR.17, was read and every proof checked. **PASS**, including the normalization scalar, transpose convention, all vanishing endpoints, and the full band decomposition. No new exhaustive calculation is claimed by this review.

## 1. The actual highest vectors

The polynomial \(F_{a,n,j}\) is symmetric in the \(a\) slots, has degree \(n\) in each slot, and has right highest weight \((an-2j,2^j)\). These statements follow directly from the initial minors and the factors of the first coordinates in SR.4. Its nonzero value is established by setting all first coordinates to one and including \(0,e_1,\ldots,e_j\) among the remaining slot vectors; it becomes a sum of squared real minors with a nonzero term. A064 proves that its highest-weight multiplicity is one, so it spans the specified highest line.

## 2. Exact polarization scalar

The report's normalized pairing sends \(\ell_1^a\cdots\ell_n^a\) under the grid regrouping map to \((\ell_1\cdots\ell_n)^a\) with scalar one. Thus the transposed map evaluates the polarized form at \(a\) copies of \(Q=\ell_1\cdots\ell_n\), exactly as in SR.5.

On the affine chart \(\ell_k=(1,v_k)\), put \(s=\sum_kv_k\), \(T=\sum_kv_kv_k^t\), and \(\mu=s/n\). The one-slot degree-two moment matrix is

\[
B=\begin{pmatrix}1&\mu^t\\ \mu&M\end{pmatrix},
\qquad M=\frac{ss^t-T}{n(n-1)}.
\]

I checked both distinct and repeated coordinate indices against the factorial pairing \((n-|\beta|)!\prod_i\beta_i!/n!\). The same matrix is obtained in both cases. Expanding the two determinants of one squared minor and applying the slot functionals gives \((j+1)!\det B\). Summing over its \(\binom a{j+1}\) slot sets therefore gives \((a)_{j+1}\det B\), with every outside factor contributing one.

The Schur complement is literally

\[
M-\mu\mu^t=-\frac{T-ss^t/n}{n(n-1)}.
\]

For the \(n\)-row matrix whose rows are \((1,v_k)\), Cauchy–Binet gives

\[
F_{n,a,j}(1,v_1;\ldots;1,v_n)
=n\det(T-ss^t/n).
\]

Combining these equalities gives the exact scalar, including its sign and both denominator exponents:

\[
h_{a,n}F_{a,n,j}
=\frac{(-1)^j(a)_{j+1}}{n^{j+1}(n-1)^j}\,F_{n,a,j}.
\]

The identity on the open first-coordinate chart extends to the full polynomial identity by multihomogeneity and density. At \(j<n\), choosing \(e_1,\ldots,e_j\) and zero remaining vectors gives centered determinant \((n-j)/n\ne0\). At \(j\ge n\), all corresponding minors vanish because the matrix has only \(n\) rows. This matches the row-length obstruction for the opposite plethysm and proves every scalar endpoint without division by a vanishing quantity; throughout this part \(n\ge2\).

The canonical map in the rank statement is the transpose grid map. Rational invariant perfect pairings identify each finite multiplicity block with the transpose block, so their ranks agree. The target multiplicity is one by A064. Hence the actual map has rank one exactly at \(j<n\), and rank zero at \(j\ge n\).

## 3. All other partitions in the band

For a tail \(\nu=(2^j,1^k)\) with \(k>0\), the stable balanced chart is valid because \(n\ge2\ge\lambda_2\). Skew Cauchy gives the literal Young-component embedding

\[
S_{(2^j,1^k)}\mathfrak h_a
\lhook\joinrel\longrightarrow
\Lambda^{j+k}\mathfrak h_a\otimes\Lambda^j\mathfrak h_a.
\]

The two exterior factors are distinct self-dual hook Specht modules by the explicit polytabloid map checked in A064. Their tensor product has zero invariant space. The injection consequently proves the full ones-tail vanishing, including \(j=0\) and maximal admissible exterior degrees.

The remaining nonzero tails are the pure two tails and the empty tail. The latter is the one-row component, on which the grid map takes the pure-power generator to itself. Partitions with more than \(a\) rows have zero target multiplicity by the iterated Pieri filtration. The displayed cokernel sum is therefore exactly the sum of the missing pure-two components \(n\le j\le a-1\), each once; characteristic-zero semisimplicity justifies the direct sum. Terms whose Schur functor vanishes in a chosen smaller vector-space rank are zero there, as asserted. The separate degree-one cases are the literal symmetric-power identity.

All constructions use normalized tensor permutations, multiplication, minors, and rational pairings. Their naturality with respect to the vector space proves the stated bundle transport by descent through frame changes. No assertion of exactness after an arbitrary pullback is required.
