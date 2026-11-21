# An explicit toric presentation for the two-row sector of outer degree four

## Scope and prior result

This report gives a small presentation and a finite SAGBI basis for the subalgebra of G-009's \(A_4\) with output partitions of length at most two. It yields two fixed, four-variable polytopes for all coefficients \(a_{4,n}^{(4n-k,k)}\). The binary-quartic covariant algebra and this coefficient family are classical; the point here is the complete explicit normalizer-algebra morphism, the finite toric degeneration, and the directly verified lattice count. No discovery of the classical presentation or coefficient family is claimed.

Primary historical source: J. H. Grace and A. Young, *The Algebra of Invariants* (1903), §89, printed pp. 91–94, proves generation of the quartic covariants by five forms; §93, printed pp. 97–98, derives their syzygy. The source text was read in this run:
https://archive.org/download/algebraofinvaria00graciala/algebraofinvaria00graciala_djvu.txt
A scan is available at:
https://commons.wikimedia.org/wiki/File:The_algebra_of_invariants_(IA_algebraofinvaria00graciala).pdf
The coordinate normalization below is checked directly and does not require translating the historical symbolic normalization.

## T-021. Exact normalizer-algebra morphism

Let \(F=\mathbf Q^2\), with basis \(e_1,e_2\), and let
\[
P=\mathbf Q[a_1,b_1,\ldots,a_4,b_4]
=\operatorname{Sym}(\mathbf Q^4\otimes F).
\]
The determinant-one diagonal torus on the first factor fixes precisely the equal row-degree pieces
\[
B=\bigoplus_{n\ge0}P_{(n,n,n,n)}
=\bigoplus_{n\ge0}(\operatorname{Sym}^nF)^{\otimes4}.
\]
Literal row permutations act by \(S_4\). The upper unipotent group of \(GL(F)\) acts infinitesimally by
\[
D_{\rm rows}=\sum_{r=1}^4 a_r\frac{\partial}{\partial b_r}.
\]
The desired two-row part of the projected flag algebra is
\[
A_4^{\le2}=(B^{S_4})^{U_2}.
\tag{Q4.1}
\]
This is the actual subalgebra of \(A_4\) having right highest weights \((\lambda_1,\lambda_2,0,0)\). A polynomial of that right-torus weight uses only the first two columns. All positive-root operators involving later columns annihilate it; the remaining operator is \(D_{\rm rows}\). This proves the precise identification with the flag construction.

Put \(Q=\mathbf Q[x_0,x_1,x_2,x_3,x_4]=\operatorname{Sym}(\operatorname{Sym}^4F)\), where \(x_i=e_1^{4-i}e_2^i\). Define
\[
\Phi(x_i)=\binom4i^{-1}
\sum_{\substack{I\subseteq\{1,2,3,4\}\\|I|=i}}
\prod_{r\in I}b_r\prod_{r\notin I}a_r.
\tag{Q4.2}
\]
This is the pullback of the multiplication map on four linear forms, using the perfect symmetric-power pairing. It is a \(GL(F)\)-equivariant graded algebra morphism \(Q\to B^{S_4}\). In particular,
\[
D_{\rm rows}\Phi(x_i)=i\Phi(x_{i-1}),
\]
as is also verified directly: each monomial with \(i-1\) selected \(b\)'s is obtained \(5-i\) times before dividing by \(\binom4i\).

Every complex binary quartic factors into four linear forms. Therefore the multiplication map is surjective over \(\mathbf C\), so its pullback \(\Phi\) is injective, also over \(\mathbf Q\). In degree \(n\), its source and target both have dimension
\[
\dim\operatorname{Sym}^n(\operatorname{Sym}^4F)
=\binom{n+4}{4}
=\dim\operatorname{Sym}^4(\operatorname{Sym}^nF).
\]
Consequently \(\Phi\) is surjective degree by degree and is an algebra isomorphism. This is the explicit binary canonical Foulkes map \(h_{n,4}\) in each degree, and it is multiplicative across degrees.

Let
\[
D=\sum_{i=1}^4 i x_{i-1}\frac{\partial}{\partial x_i}.
\]
Since characteristic zero identifies invariance under the additive one-parameter group with the kernel of its locally nilpotent derivation, (Q4.1)–(Q4.2) give
\[
\boxed{A_4^{\le2}\simeq\ker(D:Q\to Q).}
\tag{Q4.3}
\]
This proves the morphism relating the binary-quartic calculation to the normalizer projection, including its multiplication.

## T-022. Complete presentation, positive basis, and SAGBI degeneration

In \(Q\), define
\[
\begin{aligned}
f&=x_0,\\
H&=x_0x_2-x_1^2,\\
T&=x_0^2x_3-3x_0x_1x_2+2x_1^3,\\
I&=x_0x_4-4x_1x_3+3x_2^2,\\
J&=x_0x_2x_4+2x_1x_2x_3-x_0x_3^2-x_1^2x_4-x_2^3.
\end{aligned}
\tag{Q4.4}
\]
Direct differentiation proves that each lies in \(\ker D\). Direct expansion gives
\[
T^2+4H^3-f^2HI+f^3J=0.
\tag{Q4.5}
\]
The exact presentation is
\[
\boxed{\ker D=\mathbf Q[f,H,I,J,T]/(T^2+4H^3-f^2HI+f^3J).}
\tag{Q4.6}
\]

Here is a full proof of generation and absence of further relations, formulated to identify the possible denominator obstruction explicitly. After inverting \(f=x_0\), translate by the group parameter \(-x_1/f\). The resulting coordinates have first coordinate \(f\), second coordinate zero, and the other three coordinates
\[
y_2=H/f,\qquad y_3=T/f^2,\qquad
y_4=(f^2I-3H^2)/f^3.
\]
The inverse translation recovers the original coordinates. Thus
\[
Q[f^{-1}]
=\mathbf Q[f^{\pm1},x_1/f,y_2,y_3,y_4],
\]
and \(D(x_1/f)=1\), while \(D\) annihilates the other four generators. Hence
\[
(\ker D)[f^{-1}]
=\mathbf Q[f^{\pm1},H,T,I].
\tag{Q4.7}
\]

Let \(C_0\) be the abstract right side of (Q4.6), and map it to \(Q\) by (Q4.4). Its defining equation is monic in \(T\), so it is free over the abstract polynomial ring \(\mathbf Q[f,H,I,J]\) with basis \(1,T\); in particular multiplication by \(f\) is injective. After inverting \(f\), the equation solves for \(J\), and (Q4.7) shows that the map becomes an isomorphism to the displayed polynomial subalgebra. Thus \(C_0\to Q\) is injective before localization as well.

Modulo \(f\), this map is
\[
\mathbf Q[H,T,I,J]/(T^2+4H^3)
\longrightarrow \mathbf Q[x_1,x_2,x_3,x_4],
\]
\[
H\mapsto-x_1^2,\quad T\mapsto2x_1^3,\quad
I\mapsto-4x_1x_3+3x_2^2,\quad
J\mapsto2x_1x_2x_3-x_1^2x_4-x_2^3.
\tag{Q4.8}
\]
This map is injective. The first two images give exactly the cusp algebra
\(\mathbf Q[x_1^2,x_1^3]\): reduction to \(H^aT^\epsilon\), \(\epsilon=0,1\), yields distinct powers of \(x_1\). Over \(\mathbf Q(x_1,x_2)\), the last two images are affine linear coordinates in \(x_3,x_4\), with nonzero triangular coefficients \(-4x_1\) and \(-x_1^2\). They are algebraically independent over \(\mathbf Q(x_1)\), and hence over the cusp algebra. This proves the asserted injectivity.

It follows that \(C_0\cap fQ=fC_0\). Every \(g\in\ker D\) belongs to \(C_0[f^{-1}]\) by (Q4.7). Choose a smallest \(r\ge0\) for which \(f^rg\in C_0\). If \(r>0\), then \(f^rg\in C_0\cap fQ=fC_0\), contradicting minimality. Thus \(r=0\), proving (Q4.6).

In particular the monomials
\[
f^aH^bI^cJ^dT^\epsilon,\qquad
a,b,c,d\ge0,\quad\epsilon\in\{0,1\},
\tag{Q4.9}
\]
form a basis.

Now put positive ambient weights \((1,2,1,2,2)\) on
\((x_0,x_1,x_2,x_3,x_4)\), and refine the weighted order by lexicographic order. The leading terms of \((f,H,T,I,J)\) are
\[
x_0,\quad -x_1^2,\quad 2x_1^3,\quad -4x_1x_3,\quad -x_1^2x_4.
\tag{Q4.10}
\]
The leading monomial of (Q4.9) is
\[
x_0^a x_1^{\,2b+c+2d+3\epsilon}x_3^cx_4^d.
\]
All these monomials are distinct: recover \(a,c,d\) from their coordinates, recover \(\epsilon\) by parity of the remaining \(x_1\) exponent, then recover \(b\). Therefore every nonzero element of \(C_0\) has leading monomial in the algebra generated by (Q4.10). Conversely the leading generator monomials belong to the initial algebra. This proves, without an unverified subduction assumption, that the five generators are a SAGBI basis and
\[
\boxed{\operatorname{in}(A_4^{\le2})
\simeq\mathbf Q[x_0,x_1^2,x_1^3,x_1x_3,x_1^2x_4].}
\tag{Q4.11}
\]
This is a toric algebra; normality is not asserted. Its only toric relation, with the coefficient normalization in (Q4.10), is \(T^2+4H^3=0\). The unique-exponent argument proves that there are no further relations. The ambient weight filtration, transported along (Q4.3), supplies the toric degeneration of the specified normalizer subalgebra.

The generator degrees \((n;\lambda_1,\lambda_2)\) are
\[
\begin{array}{c|ccccc}
 &f&H&I&J&T\\ \hline
n&1&2&2&3&3\\
\lambda&(4,0)&(6,2)&(4,4)&(6,6)&(9,3).
\end{array}
\]
Thus, for \(0\le k\le2n\),
\[
\boxed{
a_{4,n}^{(4n-k,k)}
=\sum_{\epsilon=0}^{1}
\#\left\{(a,b,c,d)\in\mathbf Z_{\ge0}^{4}:
\begin{array}{rcl}
a+2b+2c+3d&=&n-3\epsilon,\\
2b+4c+6d&=&k-3\epsilon
\end{array}\right\}.
}
\tag{Q4.12}
\]
These are two bounded rational polytopes of fixed dimension, specified by a constant matrix and the two input integers. The first equation bounds every coordinate. Unlike the general construction, no parameter-dependent Reynolds enumeration, Hilbert-basis calculation, or polynomial elimination is required to produce these polytopes. They recover a known coefficient family through the explicit normalizer algebra and its toric filtration.

## T-023. A precise obstruction for the ordinary lexicographic candidate

The same five generators do not form a SAGBI basis for ordinary lexicographic order \(x_0>x_1>x_2>x_3>x_4\). Their leading monomials are
\[
x_0,\quad x_0x_2,\quad x_0^2x_3,\quad x_0x_4,\quad x_0x_2x_4.
\]
But \(fJ-HI\) belongs to their algebra and has leading term \(-x_0^2x_3^2\). A nonnegative product of the listed leading monomials with zero \(x_2,x_4\) exponents can use only \(x_0\) and \(x_0^2x_3\). Obtaining \(x_3^2\) then forces \(x_0\) exponent at least four, rather than two. Thus the required leading monomial is absent. This proves the failure of that particular order; (Q4.10) gives an explicit order for which the same generators succeed.

## Exact checks and next sector

The script check_binary_quartic.py checks every derivation identity, the defining relation, the five weighted leading terms, and the lex obstruction by exact symbolic arithmetic. It also compares (Q4.12) with independent Gaussian-rectangle weight differences for all \(0\le n\le100\), \(0\le k\le2n\): 10,201 coefficients. Every value agrees. BINARY_QUARTIC_CHECK.tsv and SYMBOLIC_CHECK.txt provide the receipts. These are finite checks supplementary to the complete proof.

The full \(A_4\), and already its output-length-three subalgebra, contain additional highest weights and are not evaluated by (Q4.3). The displayed morphism is exact for the stated two-row sector. The next concrete task is an explicit presentation or filtration for the length-three sector, using the three-column flag variables rather than extending the binary map without a proved morphism.

