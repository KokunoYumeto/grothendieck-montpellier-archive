# The actual four-slot boundary and its coordinate-ring morphism

Statements **R-012** and **R-013**. Completed and independently checked on 2026-11-20 UTC by GPT-6 Astra Pro, agent /root/rectangular_cases; inherited effort setting not exposed.

## R-012. The finite boundary map

For every finite-dimensional complex vector space \(V\), the natural map

\[
\begin{gathered}
T_{4,15}:\operatorname{Sym}^4(\operatorname{Sym}^{15}V)
 \longrightarrow
 \operatorname{Sym}^{16}V\otimes
 \operatorname{Sym}^4(\operatorname{Sym}^{11}V),
 \\
 f\longmapsto[t_1^4t_2^4t_3^4t_4^4]\,
 f(v_1+t_1x,\ldots,v_4+t_4x)
\end{gathered}
\]

is injective. This is the actual common-power boundary \(r=L=4,\ b=r^2-1=15\). Multiplication by \((4!)^4\) gives the undivided differential operator \(\prod_i(x\cdot\partial_{v_i})^4\), with the same kernel.

### Complete proof

The dimension reduction and flag-minor highest-weight construction are proved in full in R-011, sections 1–4 of polarization_boundary_report.md. They apply unchanged here: the source has only partitions of length at most four, the tensor permutation map has dimension-independent multiplicity matrices, and a nonzero equivariant kernel would contain a highest-weight vector. The following exhaustive finite certificate proves that every source multiplicity space maps injectively.

The exact source character has **1,713** distinct constituents, highest-weight multiplicity sum **14,018**, maximum multiplicity **35**, and full representation dimension on \(\mathbb C^4\)

\[
 \dim\operatorname{Sym}^4(\operatorname{Sym}^{15}\mathbb C^4)
 =\binom{819}{4}=18,609,648,876.
\]

For each constituent \(\lambda\) of multiplicity \(m_\lambda\), the certificate provides \(m_\lambda\) integral symmetric highest-weight polynomials, specified as signed sums of products of the fifteen flag minors. Their row weights and equal column degrees are verified directly. Invariance under the three adjacent slot transpositions is verified directly, including all determinant signs. The certificate then gives \(m_\lambda\) evaluation points and the full square evaluation matrix of their images under \(T_{4,15}\).

Every one of those 1,713 square matrices has a nonzero determinant modulo the prime \(1,000,003\). In particular, every determinant is a nonzero integer. Its columns are therefore linearly independent over \(\mathbb Q\), and hence over \(\mathbb C\). Thus the map is injective on every highest-weight multiplicity space. The highest-weight argument proves injectivity for \(\mathbb C^4\), and the dimension-independent tensor permutation argument proves it for all \(V\).

The certificate is exhaustive in the following independently verified sense.

1. The source multiplicities were first extracted from the exact Newton recurrence for \(h_4[h_{15}]\). A separate C++ program, verify_boundary_character.cpp, independently computes

   \[
   [t^4]\prod_{\substack{\alpha\in\mathbb Z_{\ge0}^4\\|\alpha|=15}}
   (1-tx^\alpha)^{-1}
   \]

   by multiplying the 816 individual geometric-series factors. It applies the Weyl alternant to every partition of 60 of length at most four, and obtains exactly the same positive multiplicities. Its Weyl-dimension sum and sum of all monomial weight coefficients both equal 18,609,648,876.

2. The original evaluator expands each shifted flag minor as its constant term plus its four possible linear terms, then uses forward coefficient propagation and modular Gaussian elimination.

3. A separately written evaluator, recheck_large_polarization.cpp, recomputes **all 203,840 entries** of the selected square matrices. It processes the flag-minor factors in reverse order, uses descending in-place coefficient recurrence instead of forward propagation, and independently computes every small determinant and selected matrix determinant by power traces and Newton identities. It also checks every selected polynomial's highest weight, four slot degrees, and exact invariance under the three generators of \(S_4\).

For clarity, the independent coefficient recurrence replaces a current coefficient array \(c_\alpha\), in descending index order, by

\[
 c_\alpha\ \leftarrow\
 d\,c_\alpha+\sum_{j=1}^4a_jc_{\alpha-e_j}
 \pmod {1,000,003}
\]

for each linear minor factor \(d+\sum_j a_jt_j\), retaining only \(0\le\alpha_j\le4\). Descending order guarantees that every referenced lower index still has its old value. Truncation cannot change the target coefficient because exponents are nonnegative. The determinant recheck uses

\[
 e_0=1,\qquad
 e_k=\frac1k\sum_{i=1}^k(-1)^{i-1}e_{k-i}\operatorname{tr}(A^i),
 \qquad\det A=e_m,
\]

for an \(m\times m\) matrix. Here \(m\le35<1,000,003\), so every division by \(k\) is valid. All products and unreduced sums fit signed 64-bit integers: the largest matrix-product sums have at most 35 terms, each smaller than \(1,000,003^2\).

The independent run made 4,517,197 Taylor evaluations, checked all 14,018 selected vectors, and passed every entry and determinant. The underlying finite-field modulus is checked by trial division. Consequently no probabilistic assertion enters the proof; the point generator merely supplied the printed points.

### Compact certificate

The file POLARIZATION_R4_L4_B15_SELECTED.compact.gz contains the complete selected source polynomials, points, matrices and determinants. Its uncompressed size is 11,569,652 bytes; compressed size is 2,761,977 bytes. Its SHA256 is

~~~
fa2bbbeb5e335d08cda726359ac2b1ffaf1fe1270bba56e3f29841b9957db107
~~~

The character table is POLARIZATION_R4_L4_B15.tsv. The rank summary is POLARIZATION_R4_L4_B15_ALL_RANKS.tsv. The independent receipt is POLARIZATION_R4_L4_B15_INDEPENDENT_RECHECK.txt. The complete full-candidate input and parallel batches are intermediate files; they are unnecessary for checking the selected certificate.

To recheck the selected certificate, decompress the gzip file, compile `recheck_large_polarization.cpp` with C++17 and optimization, and pass the resulting compact file as its sole argument. Compile `verify_boundary_character.cpp` and pass `POLARIZATION_R4_L4_B15.tsv` to recheck the source multiplicities independently. The compressed certificate contains only selected vectors, so the 124 MB full candidate input is not needed.

No priority claim is made for this finite rank computation. The supplied proof establishes this map and these parameters, without a classification for larger even numbers of slots.

## R-013. Exact morphism to the variety of padded forms

The coordinate-ring description is a known generalized Foulkes–Howe construction. A precise primary locator is Kadish–Landsberg, *Padded polynomials, their cousins, and geometric complexity theory*, **Theorem 1.7**, p. 3, with the full tensor construction and evaluation proof in **section 3, pp. 5–6**:

https://arxiv.org/pdf/1204.4693

The published article is *Communications in Algebra* 42 (2014), 2171–2180, DOI 10.1080/00927872.2012.758268. The statement and proof in the cited arXiv version were read in this run. The following proof fixes the exact scalar relating that coordinate-ring map to the coefficient-extraction operator used in our certificates.

Let \(r\ge1\), \(b\ge1\), and \(0\le L\le b\). Fix the normalized perfect pairing on symmetric powers by

\[
 \langle v^k,\ell_1\cdots\ell_k\rangle
 =\prod_{j=1}^k\ell_j(v).
\]

Define the polynomial morphism

\[
 \nu_{L,b}:V^*\times\operatorname{Sym}^{b-L}V^*
 \longrightarrow\operatorname{Sym}^bV^*,
 \qquad(\ell,q)\longmapsto\ell^Lq.
\]

Its pullback in coordinate degree \(r\) is

\[
 (\nu_{L,b}^*)_r:
 \operatorname{Sym}^r(\operatorname{Sym}^bV)
 \longrightarrow
 \operatorname{Sym}^{rL}V\otimes
 \operatorname{Sym}^r(\operatorname{Sym}^{b-L}V).
\]

Define \(T_{r,L,b}\) by extracting \(t_1^L\cdots t_r^L\) after substituting \(v_i+t_ix\) in the symmetric \(r\)-slot model. Then the exact equality is

\[
 \boxed{\displaystyle
 (\nu_{L,b}^*)_r=\binom bL^{-r}T_{r,L,b}.}
 \tag{R013.1}
\]

**Proof.** Products \(w_1^b\cdots w_r^b\) span \(\operatorname{Sym}^r(\operatorname{Sym}^bV)\), because pure powers span each symmetric power. As a coordinate polynomial, such a product sends \(P\) to \(\prod_i\langle w_i^b,P\rangle\). Its pullback along \(\nu_{L,b}\) is

\[
 \prod_i\ell(w_i)^L
 \prod_i\langle w_i^{b-L},q\rangle.
\]

This is represented in the displayed target by

\[
 (w_1^L\cdots w_r^L)\otimes
 (w_1^{b-L}\cdots w_r^{b-L}).
\]

The symmetric-slot representative of the original product is the average over all assignments of the \(w_i\) to the \(r\) slots. In each assigned row the binomial theorem gives the factor

\[
 [t_i^L]\langle w,v_i+t_ix\rangle^b
 =\binom bL\langle w,x\rangle^L
 \langle w,v_i\rangle^{b-L}.
\]

Multiplying the \(r\) factors and taking the same slot average therefore gives \(\binom bL^r\) times the tensor above. Equality on a spanning set proves (R013.1).

Let \(Z_{L,b}(V)\) be the Zariski closure of the image of \(\nu_{L,b}\). A homogeneous polynomial vanishes on that image precisely when its pullback is zero; vanishing on the image and its closure are equivalent by the definition of Zariski closure. Thus

\[
 \boxed{\displaystyle
 I_r(Z_{L,b}(V))
 =\ker(\nu_{L,b}^*)_r
 =\ker T_{r,L,b}.}
 \tag{R013.2}
\]

Moreover the maps \(\binom bL^{-r}T_{r,L,b}\), as \(r\) varies, are the graded pieces of the one algebra homomorphism \(\nu_{L,b}^*\). This identifies their multiplication exactly, including the normalization.

### Actual geometric corollaries

Combining R-011 and R-012 with (R013.2) gives, for every finite-dimensional complex \(V\),

\[
 I_4(Z_{1,3}(V))=
 I_4(Z_{2,7}(V))=
 I_4(Z_{4,15}(V))=0.
\]

The homogeneous ideals in all degrees \(0\le d\le4\) are zero as well. Indeed, a nonzero equation of smaller positive degree could be multiplied by a nonzero polynomial to degree four in the ambient polynomial coordinate ring, which is an integral domain; the product would contradict the displayed vanishing. Degree zero contains no equation because each image contains the origin. When the ambient vector space is zero-dimensional, the assertion follows directly from its coordinate ring.

These are explicit low-degree assertions for the varieties of forms \(\ell q\) of degree 3, \(\ell^2q\) of degree 7, and \(\ell^4q\) of degree 15. They give a geometric interpretation of the verified finite kernels, with the complete morphism and scalar proved above.
