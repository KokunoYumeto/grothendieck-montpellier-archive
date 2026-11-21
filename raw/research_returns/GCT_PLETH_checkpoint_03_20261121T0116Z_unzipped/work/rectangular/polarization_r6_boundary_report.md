# Six symmetric slots at the common-power-one boundary

Statement **R-015**. Completed and independently checked on 2026-11-21 UTC by GPT-6 Astra Pro, agent /root/rectangular_cases; inherited effort setting not exposed.

## Exact result

For every finite-dimensional complex vector space \(V\), the natural map

\[
 T_{6,1,5}:\operatorname{Sym}^6(\operatorname{Sym}^5V)
 \longrightarrow
 \operatorname{Sym}^6V\otimes\operatorname{Sym}^6(\operatorname{Sym}^4V),
 \qquad
 f\longmapsto[t_1\cdots t_6]\,
 f(v_1+t_1x,\ldots,v_6+t_6x)
\]

is injective. Here the parameters satisfy \(b=rL-1\) with \(r=6,L=1,b=5\).

By the exact coordinate-ring morphism R-013, the variety

\[
 Z_{1,5}(V)=\overline{\{\ell q:
        \ell\in V^*,\ q\in\operatorname{Sym}^4V^*\}}
       \subseteq\operatorname{Sym}^5V^*
\]

has no equations of degree at most six:

\[
 I_d(Z_{1,5}(V))=0\qquad(0\le d\le6).
\]

The pullback in degree six is precisely \(5^{-6}T_{6,1,5}\), not an unspecified nonzero scalar. This follows from R013.1. Vanishing in lower degrees follows by multiplying a nonzero lower-degree equation to degree six in the ambient polynomial domain, exactly as in R-013.

No general even-slot boundary classification or historical priority claim is made.

## Complete finite proof

### Reduction and source character

The source embeds in \((\operatorname{Sym}^5V)^{\otimes6}\). Iterated Pieri multiplication therefore gives only Schur functors with at most six rows. The natural tensor permutation and symmetrization formula for \(T_{6,1,5}\) acts by the same multiplicity-space matrices in all dimensions at least six. Checking \(\mathbb C^6\) consequently detects every possible kernel summand; smaller dimensions follow by naturality under an inclusion into \(\mathbb C^6\). This is the same Schur–Weyl argument proved in R-011, section 1, with six replacing four.

The exact source decomposition on \(\mathbb C^6\) has:

| Quantity | Value |
|---|---:|
| Distinct irreducible constituents | 893 |
| Sum of highest-weight multiplicities | 5,369 |
| Largest multiplicity | 32 |
| Number of monomial weights | 324,632 |
| Full representation dimension | 377,342,351,232 |

The last dimension equals \(\binom{257}{6}\), because \(\dim\operatorname{Sym}^5\mathbb C^6=\binom{10}{5}=252\).

The program character_r6_b5.cpp computes the complete character twice. One calculation multiplies the 252 factors

\[
 \prod_{\substack{\alpha\in\mathbb Z_{\ge0}^6\\|\alpha|=5}}
       (1-tx^\alpha)^{-1}
\]

through \(t\)-degree six. The other uses the exact Newton recurrence for \(h_j[h_5]\), \(j=1,\ldots,6\). It compares every monomial coefficient for every one of these six outer degrees. At degree six all 324,632 weights agree. The Weyl-alternant coefficient formula then extracts the multiplicity at every partition of 30 of length at most six. The sum of multiplicities times Weyl dimensions equals both the sum of all weight coefficients and \(\binom{257}{6}\). This proves the complete source multiplicity list used in the certificate.

### Integral source vectors

Let \(X\) be a \(6\times6\) variable matrix, with columns the six slots. For every nonempty subset \(I\subseteq\{1,\ldots,6\}\), let \(d_I(X)\) be the determinant using the first \(|I|\) rows and the columns \(I\) in increasing order. There are 63 such flag minors. A seed is

\[
 F_c(X)=\prod_I d_I(X)^{c_I}.
\]

The certificate records the 63 nonnegative integers \(c_I\). They satisfy

\[
 \sum_{I\ni j}c_I=5\quad(1\le j\le6),\qquad
 \lambda_k=\sum_{|I|\ge k}c_I\quad(1\le k\le6).
\]

Thus the seed has equal slot degrees five and highest weight \(\lambda\). The highest-weight property follows by applying a raising operator to each flag determinant: replacing a row by an earlier row repeats a row, giving zero.

The associated symmetric vector is its Reynolds sum

\[
 R_c(X)=\sum_{\sigma\in S_6}F_c(X_{\sigma(1)},\ldots,X_{\sigma(6)}),
\]

including the signs from sorting each determinant's columns. For compact integer storage, collect equal monomials in the 63 minors, divide their integer coefficients by their greatest common divisor, and choose the sign so that the first nonzero coefficient in lexicographic exponent order is positive. Each selected sum is nonzero. Its divisor is at most \(720\), since each coefficient is a signed sum of at most 720 terms; in particular it is a unit modulo \(1,000,003\).

Every source vector is therefore specified exactly by one 63-entry seed and this fixed normalization rule. The independent checker generates all 720 permutations anew, collects their signed contributions, and checks the seed's weight and all six slot degrees. Invariance follows directly by reindexing the complete group sum. No spanning assertion about the candidate seeds is required: the certificate supplies exactly the required number of independent images at each highest weight.

### Primary image evaluations by a squarefree logarithm

For a fixed point \(X,x\), every flag minor after the shift is exactly linear:

\[
 d_I(X+t x)=d_I(X)+\sum_{j\in I}a_{I,j}(X,x)t_j.
\]

Every term with two inserted columns vanishes because those columns are equal to \(x\). To find the coefficient \(t_1\cdots t_6\), work in the squarefree quotient ring

\[
 \mathbb F_P[t_1,\ldots,t_6]/(t_1^2,\ldots,t_6^2),
 \qquad P=1,000,003.
\]

The printed primary evaluation points have every \(d_I(X)\ne0\). Put \(C=\prod_Id_I(X)^{c_I}\). For a nonempty subset \(S\), define

\[
 \ell_S=(-1)^{|S|-1}(|S|-1)!
       \sum_I c_I\prod_{j\in S}\frac{a_{I,j}}{d_I(X)},
\]

where the summand is zero for \(S\not\subseteq I\). The formal logarithm of the product, after its constant factor \(C\) is removed, has coefficient \(\ell_S\) at \(t_S=\prod_{j\in S}t_j\). Indeed, the \(k\)-th term of \(\log(1+u)\) contributes \((-1)^{k-1}u^k/k\), and a product of \(k\) distinct variables has coefficient \(k!\) in \(u^k\). All relevant denominators are units because \(P>6\).

Exponentiating in this nilpotent ring gives the exact coefficient

\[
 [t_1\cdots t_6]F_c(X+t x)
 =C\sum_{\pi\text{ a set partition of }[6]}
          \prod_{S\in\pi}\ell_S.
\]

The primary evaluator computes this finite sum by the recurrence

\[
 H(\varnothing)=1,\qquad
 H(A)=\sum_{\substack{\varnothing\ne S\subseteq A\\\min A\in S}}
             \ell_SH(A\setminus S).
\]

The block containing the least element of \(A\) makes every set partition occur exactly once. It then adds the signed normalized Reynolds contributions.

### Independent verification and integer lifting

For every source constituent \(\lambda\) of multiplicity \(m_\lambda\), the certificate supplies \(m_\lambda\) selected normalized Reynolds vectors, \(m_\lambda\) evaluation rows, and the complete square matrix of their image values. Every one of the 893 determinants is nonzero modulo \(P\).

The independent program recheck_polarization_r6.cpp recomputes every selected entry without logarithms, inverses of minor constants, or set partitions. It expands the same linear minor factors by descending in-place Taylor recurrence, in reverse factor order:

\[
 c_A\leftarrow d_Ic_A+
          \sum_{j\in I\cap A}a_{I,j}c_{A\setminus\{j\}}.
\]

Descending subset index leaves each lower-index old coefficient intact. The independent program also evaluates all small flag determinants and every selected square determinant using power traces and Newton identities instead of the primary program's Gaussian elimination. For an \(m\times m\) matrix, these identities are

\[
 e_0=1,\qquad
 e_k=\frac1k\sum_{i=1}^k(-1)^{i-1}e_{k-i}\operatorname{tr}(A^i),
 \qquad\det A=e_m.
\]

Here \(m\le32<P\). The prime is separately checked by trial division, and the largest unreduced 64-bit sums are bounded by \(32P^2\).

All **65,481 selected entries** and all 893 determinants passed the independent check. Since the source vectors and coefficient-extraction map have integer coefficients, a nonzero determinant modulo \(P\) is a nonzero integer determinant. The selected images are therefore linearly independent over \(\mathbb Q\) and \(\mathbb C\).

Every source highest-weight multiplicity space is thus injective. Any nonzero equivariant kernel would contain a nonzero highest-weight vector. This proves the stated injectivity on \(\mathbb C^6\), and the dimension transfer already proved gives the result for all \(V\).

Two first-pass random seed lists were insufficient to exhibit their full ranks. Enlarged lists supplied full ranks four and seven in those blocks. The final selected certificate uses only complete square matrices; the two incomplete first-pass evaluations are not used in the proof.

## Reproducible compact artifacts

The complete certificate is POLARIZATION_R6_L1_B5_SELECTED.compact.gz. It contains every selected seed, point, square matrix and nonzero determinant, and occupies 329,843 compressed bytes. Its SHA256 is

~~~
6db560ac93c2f53850ddc547946b939556531a0e43aa0e52e18c2ae01e1326ca
~~~

The source character is POLARIZATION_R6_L1_B5_SOURCE.tsv; the complete rank summary is POLARIZATION_R6_L1_B5_ALL_RANKS.tsv; the independent receipt is POLARIZATION_R6_L1_B5_INDEPENDENT_RECHECK.txt.

To recheck, decompress the compact certificate, compile recheck_polarization_r6.cpp with C++17 and optimization, and give the decompressed file as its sole argument. The program character_r6_b5.cpp independently reproduces and compares both complete source-character calculations. The full candidate generator, original evaluator, and merge script are polarization_r6_seeds.py, check_polarization_r6.cpp, and merge_polarization_r6.py. The parallel intermediate directory is unnecessary for verifying the final certificate.

The next pair \(r=6,L=2,b=11\) has 13,019,909 monomial weights before Schur extraction and source dimension 9,679,525,138,407,392,632 on \(\mathbb C^6\). No rank certificate or theorem for that pair is asserted here.
