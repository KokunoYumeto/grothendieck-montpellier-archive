# Width seven: metric covariants, exact end-node coefficients, and the extension valuation

This report continues T-010–T-014. It supplies a complete positive formula for a three-parameter family inside the first remaining symmetric-power factor, together with further stable nonvanishing families. The constructions and proofs are unconditional. No global novelty claim is made.

All representations are over \(\mathbf C\). Put \(V=\mathbf C^7\), \(G=GL(V)\),
\[
R=\operatorname{Sym}(\Lambda^3V)=\mathbf C[\Lambda^3V^*],
\qquad S=\operatorname{Sym}(\Lambda^4V).
\]
The coordinate-ring action is \((gf)(\phi)=f(g^{-1}\phi)\). Thus \(R_d\) has positive central degree \(3d\). Highest weights are decreasing integral seven-tuples; a superscript on an entry means repetition.

For integers \(A\ge B\ge C\ge0\), \(d\ge0\), \(A+5B+C=4d\), define
\[
\mathcal P(A,B,C)=\left\{(k,\ell,j)\in\mathbf R_{\ge0}^3:
\begin{array}{rcl}
2k+4\ell+4j&=&A,\\
2k+2\ell+4j&=&B,\\
2\ell+4j&=&C.
\end{array}\right\}.
\]
The exact answer proved below is
\[
\boxed{[S_{(A,B^5,C)}V:S_d]
=\#(\mathcal P(A,B,C)\cap\mathbf Z^3).}
\tag{W7.1}
\]
This bounded polytope is empty or a point. Its unique possible point is
\[
k=(B-C)/2,\qquad \ell=(A-B)/2,\qquad j=(B+C-A)/4.
\tag{W7.2}
\]

## T-016. Cubic metric and polynomial quartic cometric

### Precisely located background

The following classical input is used.

1. A generic alternating three-form on \(V\) has stabilizer \(H=\mu_3\times G_2\subset GL(V)\), with \(G_2\subset SL(V)\) acting through its irreducible seven-dimensional representation. Its orbit \(O\) is open. The finite central factor is retained. An exact primary locator is Dave Anderson, *Chern class formulas for \(G_2\) Schubert loci*, Appendix A, Proposition A.1 and Corollary A.2, printed page 29: https://people.math.osu.edu/anderson.2804/papers/g2-chern.pdf

2. The complement of \(O\) is one irreducible hypersurface with degree-seven equation. The cubic metric below is nondegenerate exactly on \(O\), and has rank four on the dense codimension-one boundary orbit. Laurent Manivel, *Prehomogeneous spaces and projective geometry*, Example 4.3.3, printed pages 59–60, and Example 4.4.2, printed pages 61–62, give the orbit representatives, rank data, boundary diagram, and degree-seven invariant. Proposition 3.1.4, printed page 44, identifies fundamental relative invariants with irreducible hypersurface equations. The metric also appears in §5.1.2, printed page 68: https://manivel.perso.math.cnrs.fr/trento2012.pdf

Here “metric rank” always means the rank of the explicitly defined seven-by-seven matrix; the source's two rank labels need not be adopted. The classification and generic-stabilizer statements are cited background, not reproved as new results.

Choose a volume vector \(\tau\in\det V\), with dual volume form \(\Omega\). Define
\[
B_\phi(u,v)\Omega=(\iota_u\phi)\wedge(\iota_v\phi)\wedge\phi.
\tag{W7.3}
\]
The contracted forms have degree two, so this is symmetric in \(u,v\), and its coefficients are cubic in \(\phi\). Intrinsically its values lie in \(\operatorname{Sym}^2V^*\otimes\det V^*\). The actual coefficient morphism is
\[
F_B:\operatorname{Sym}^2V\otimes\det V\longrightarrow R_3,\qquad
F_B(uv\otimes\tau)(\phi)
=\langle(\iota_u\phi)\wedge(\iota_v\phi)\wedge\phi,\tau\rangle.
\tag{W7.4}
\]
Equivariance follows by pulling back the forms and moving \(g\) across the evaluation pairing. This fixes the determinant twist. For \(\phi=e^{123}+e^{145}+e^{167}\), evaluation at \(u=v=e_1\) gives \(6\Omega\), so the map is nonzero. Its source is irreducible, hence it is injective. In particular
\(b=F_B(e_1^2\otimes\tau)\ne0\) is a highest vector of weight \((3,1^6)\).

Let \(\Delta\) be an irreducible equation of the boundary. Its degree is seven and its character for the stated action is
\[
\Delta\in R_7,\qquad g\Delta=(\det g)^3\Delta.
\tag{W7.5}
\]
Indeed every character is a determinant power, and scalar matrices act on \(R_7\) by their twenty-first power.

Writing \(B=(B_{ij})\), its coefficient transformation is
\[
gB=(\det g)\,g^{\mathsf T}Bg.
\]
Thus \(\det B\) has degree twenty-one and character \(\det^9\). Its zero locus is exactly the boundary; unique factorization gives \(\det B=c_0\Delta^3\), \(c_0\ne0\). Rescale \(\Delta\) over \(\mathbf C\) so that \(c_0=1\).

Every entry of \(\operatorname{adj}B\) is divisible by \(\Delta^2\). To prove this, localize the polynomial ring \(R\) at the height-one prime \((\Delta)\), obtaining a discrete valuation ring. Modulo its maximal ideal the metric has rank four. Invertible row and column operations reduce its first four rows and columns to an invertible block; the entries of the remaining three-by-three Schur-complement block are divisible by \(\Delta\). Every six-by-six minor therefore has valuation at least two. Since the minors are polynomials and \(R\) is a unique factorization domain, this is divisibility by \(\Delta^2\) in \(R\).

Consequently
\[
C=\operatorname{adj}B/\Delta^2
\tag{W7.6}
\]
is a matrix of quartic polynomials and
\[
BC=CB=\Delta I_7.
\tag{W7.7}
\]
The adjugate transformation gives
\[
gC=(\det g)^2g^{-1}Cg^{-\mathsf T}.
\]
Its coefficient space is the image of the equivariant morphism
\[
F_C:\operatorname{Sym}^2V^*\otimes\det^2V\longrightarrow R_4.
\tag{W7.8}
\]
The matrix is invertible on \(O\), so this map is nonzero; its irreducible source makes it injective. Choose a nonzero highest vector \(c\) in its image. Its weight is \((2^6,0)\).

Neither \(b\) nor \(c\) is divisible by the irreducible \(\Delta\), since their degrees are three and four. Hence
\[
v_\Delta(b^kc^\ell\Delta^j)=j
\quad(k,\ell\ge0,\ j\in\mathbf Z).
\tag{W7.9}
\]
This is the exact extension test.

The symbolic receipt METRIC_PATH_CHECK.txt uses
\(\phi(t)=e^{123}+e^{145}+t e^{167}+e^{246}+e^{357}\).
It obtains metric ranks four at \(t=0\) and seven at \(t=1\), determinant \(-4374t^3\), and adjugate order at least two, attained by an entry. This finite check supplements the global divisibility proof.

## T-017. The required \(G_2\)-invariant spaces

Write \(\omega_1\) for the highest weight of the seven-dimensional \(G_2\)-module. Then
\[
\operatorname{Sym}^mV|_{G_2}
=\bigoplus_{r=0}^{\lfloor m/2\rfloor}V_{(m-2r)\omega_1}
\quad(m\ge0).
\tag{W7.10}
\]
Here is a proof of precisely this assertion. The nondegenerate invariant quadratic form gives the usual contraction
\(\operatorname{Sym}^mV\to\operatorname{Sym}^{m-2}V\), and the harmonic decomposition
\(\operatorname{Sym}^mV=H_m\oplus q\operatorname{Sym}^{m-2}V\) in characteristic zero. A highest vector \(v\) is isotropic because \(v^2\) has nonzero weight \(2\omega_1\), so \(v^m\in H_m\). It generates \(V_{m\omega_1}\). The Weyl formula for the six positive roots of \(G_2\) gives
\[
\dim V_{m\omega_1}
=\frac{(m+1)(m+2)(m+3)(m+4)(2m+5)}{120}
=\binom{m+6}{6}-\binom{m+4}{6}
=\dim H_m.
\]
Binomial terms with top below six are zero. Thus \(H_m=V_{m\omega_1}\), and induction proves (W7.10). Complete reducibility, harmonic decomposition, and the Weyl formula are the standard background theorems used here.

For \(a,b\ge0\), let \(L_{a,b}\) be the irreducible \(SL_7\)-module with highest weight \(a\omega_1+b\omega_6\), now using the \(SL_7\) fundamental weights. Then
\[
\boxed{\dim L_{a,b}^{G_2}
=\begin{cases}1,&a,b\text{ both even},\\0,&\text{otherwise}.\end{cases}}
\tag{W7.11}
\]
To prove it, use the exact determinant identity
\[
\operatorname{Sym}^aV\otimes\operatorname{Sym}^bV^*
=\operatorname{Sym}^aV\otimes S_{(b^6)}V\otimes\det^{-b}V.
\]
Pieri's horizontal-strip rule, applied to the six-row rectangle, gives
\[
\operatorname{Sym}^aV\otimes\operatorname{Sym}^bV^*
=\bigoplus_{i=0}^{\min(a,b)}L_{a-i,b-i}
\tag{W7.12}
\]
after restriction to \(SL_7\). This includes \(a=0\) or \(b=0\).
By (W7.10) and Schur's lemma the left side has \(G_2\)-invariant dimension
\[
H(a,b)=\#\{r:0\le r\le\min(a,b),\ r\equiv a\equiv b\pmod2\}.
\]
Set \(H(a,b)=0\) if either argument is negative. Subtracting (W7.12) at arguments \(a-1,b-1\) gives
\(\dim L_{a,b}^{G_2}=H(a,b)-H(a-1,b-1)\).
Different parities give two zero terms; both odd give equal terms; both even give difference one. The boundary cases follow from the zero convention. This proves (W7.11).

The independent rectangular-cases checker verified the Pieri calculation, the difference including all boundary cases, and the harmonic dimension argument.


## T-018. Exact polynomial sector and positive polytope formula

For \(a,b\ge0\) and \(s\in\mathbf Z\), set
\[
\gamma=(a+b+s,(b+s)^5,s).
\tag{W7.13}
\]
These are exactly the dominant integral seven-tuples with equal second through sixth entries. They label rational \(GL_7\)-representations. The central \(\mu_3\) acts by the character determined by
\(|\gamma|=a+6b+7s\).

Evaluation at the basepoint of \(O=G/H\) gives the actual isomorphism
\[
\operatorname{Hom}_G(S_\gamma V,\mathbf C[O])
\simeq((S_\gamma V)^*)^H.
\tag{W7.14}
\]
An \(H\)-invariant functional \(\ell\) corresponds explicitly to
\[
v\longmapsto f_{\ell,v},\qquad
f_{\ell,v}(gH)=\ell(g^{-1}v).
\]
Conversely evaluate an equivariant map at the identity coset. These operations are inverse. Regularity is the matrix-coefficient construction on \(G\) and its descent to the homogeneous space \(O=G/H\).

By (W7.11), this space has dimension one exactly when
\[
a=2k,\quad b=2\ell,\quad s=k+3j
\quad(k,\ell\ge0,\ j\in\mathbf Z),
\tag{W7.15}
\]
and otherwise it has dimension zero. The congruence on \(s\) is exactly the \(\mu_3\)-invariance condition; no determinant character has been dropped.

For (W7.15), the nonzero rational highest vector \(b^kc^\ell\Delta^j\) has the required weight and degree
\[
d=3k+4\ell+7j,
\tag{W7.16}
\]
\[
\gamma=(3k+2\ell+3j,(k+2\ell+3j)^5,k+3j).
\tag{W7.17}
\]
It is regular on \(O\) and spans its one-dimensional highest-vector space. It extends to \(R\) exactly when \(j\ge0\), by (W7.9). Indeed
\(\mathbf C[O]=R[\Delta^{-1}]\), and a fraction with only this possible denominator is polynomial exactly when its \(\Delta\)-valuation is nonnegative.

It follows that the subalgebra of \(R^U\) spanned by the highest weights with equal second through sixth entries is exactly
\[
\boxed{R_{\mathrm{ends}}=\mathbf C[b,c,\Delta].}
\tag{W7.18}
\]
The three generators are algebraically independent: their weights in (W7.17) determine the three exponents uniquely, so distinct monomials have distinct torus weights. Their nonzero products are independent. Thus (W7.18) identifies the algebra, its actual generators, and its positive monomial basis.

Now use the degreewise exterior-duality isomorphism
\[
\Lambda^4V\simeq\Lambda^3V^*\otimes\det V,
\qquad
S_d\simeq R_d^*\otimes\det^dV.
\tag{W7.19}
\]
A constituent of highest weight \(\gamma\) goes to highest weight
\[
\eta_i=d-\gamma_{8-i}\quad(1\le i\le7).
\tag{W7.20}
\]
This identifies multiplicities with their determinant shifts. Equations (W7.16)–(W7.17) give
\[
\eta=(2k+4\ell+4j,(2k+2\ell+4j)^5,2\ell+4j).
\tag{W7.21}
\]
Conversely \((A,B^5,C)\) determines precisely the parameters in (W7.2). If parity or the central congruence fails, (W7.14)–(W7.15) give zero; if an extension parameter is negative, the polynomial constituent is absent. If all three are nonnegative integers, (W7.17) is a polynomial constituent with multiplicity one, and (W7.19) supplies the target. This proves (W7.1), including all zero coefficients.

The slice \(\ell=0\) says
\[
[S_{(A^6,C)}V:S_d]
=\begin{cases}1,&A\text{ even},\\0,&A\text{ odd},\end{cases}
\qquad 6A+C=4d,\quad A\ge C\ge0.
\]
The degree condition forces \(C\equiv0\pmod4\) in the nonzero case. The slice \(k=0\) is also governed by the same explicit polytope, including the triangle condition \(A\le2B\).

### A precise obstruction to discarding the extension valuation

For \(k=3,\ell=2,j=-1\), (W7.17) gives
\[
d=10,\qquad \gamma=(10,4^5,0).
\]
The function \(b^3c^2/\Delta\) is regular on \(G/H\), has this polynomial dominant weight, and has a genuine simple pole on the boundary. Therefore
\[
\dim((S_{(10,4^5,0)}V)^*)^H=1,\qquad
[S_{(10,4^5,0)}V:R_{10}]=0.
\tag{W7.22}
\]
Every entry of \(\gamma\) lies between zero and ten and \(|\gamma|=30\), so it also satisfies the elementary torus weight-support bounds for \(R_{10}\). The failure of this transfer is proved by the localization morphism and its valuation.

Duality gives the corresponding zero
\([S_{(10,6^5,0)}V:S_{10}]=0\).
The possible polytope point is \((3,2,-1)\), displaying the failed inequality.

The exact verifier check_width7.py computes the character of \(R_d\) by Newton's recurrence and extracts Schur multiplicities by the Weyl alternant. Every end-node partition in degrees zero through ten—seventy-five partitions, including (W7.22)—agrees with (W7.18). END_NODE_CHECK.tsv is the complete receipt. This is a finite verification supplementary to the infinite proof.

## T-019. Stable positive families

T-010 realizes the stable coefficient \(c_\lambda=\langle s_\lambda,H[H-1-h_1]\rangle\), for width at most seven, as the multiplicity of \(S_{\lambda'}V\) in scalar degree \(|\lambda|\) of
\[
\mathcal M_7=
\operatorname{Sym}(\Lambda^2V)\otimes
\Lambda(\Lambda^3V)\otimes
\operatorname{Sym}(\Lambda^4V)\otimes
\Lambda(\Lambda^5V)\otimes
\operatorname{Sym}(\Lambda^6V)\otimes
\Lambda(\Lambda^7V).
\]
Taking constants in every factor other than \(\operatorname{Sym}(\Lambda^4V)\), (W7.21) yields
\[
\boxed{c_{(7^{\,2\ell+4j},\,6^{\,2k},\,1^{\,2\ell})}\ge1
\quad(k,\ell,j\ge0).}
\tag{W7.23}
\]
The empty partition has coefficient one. This is a stable multiplicity bound; (W7.1) computes exactly the contribution of the specified symmetric-power factor.

Differentiating \(\Delta\) produces the nonzero equivariant map
\[
\Lambda^3V^*\otimes\mathbf C\Delta\longrightarrow R_6.
\tag{W7.24}
\]
It is nonzero by Euler's identity \(7\Delta=\sum x_i\partial_i\Delta\); its irreducible source makes it injective. Its highest weight is \((3^4,2^3)\). Via (W7.19) it gives a nonzero highest vector \(g\in S_6\) of weight \((4^3,3^4)\). Hence
\[
c_{(7^3,3)}\ge1,\qquad
c_{(7^{\,4j+3h},3^h)}\ge1\quad(j,h\ge0).
\tag{W7.25}
\]
For the second assertion choose a determinant vector in \(S_7\), of weight \((4^7)\), supplied from \(\Delta\) by (W7.19), and multiply its \(j\)-th power by \(g^h\) inside the polynomial domain \(S\). Degreewise duality is used to produce individual constituents; all multiplication occurs in the stated target algebra.

A more flexible sufficient family is
\[
\boxed{\begin{split}
\lambda={}&(7^{\,2\ell+4j+3h+\epsilon_7},
6^{\,u_6},5^{\,\epsilon_5},4^{\,u_4},
3^{\,h+\epsilon_3},2^{\,u_2},1^{\,2\ell}),\\
&c_\lambda\ge1,
\end{split}}
\tag{W7.26}
\]
for \(\ell,j,h,u_2,u_4,u_6\ge0\) and
\(\epsilon_3,\epsilon_5,\epsilon_7\in\{0,1\}\).

For a complete proof, inside the single domain \(S\) multiply the cometric-derived highest vector of weight \((4,2^6)\) to power \(\ell\), the determinant vector to power \(j\), the differentiated vector \(g\) to power \(h\), and the pure highest vector \(e_1\wedge e_2\wedge e_3\wedge e_4\) to power \(u_4\). The result is nonzero and highest. In the symmetric factors for exterior degrees two and six, take pure highest vectors to powers \(u_2,u_6\). In each of the exterior-algebra factors of exterior degree three, five, and seven, take either its scalar or its degree-one highest vector according to \(\epsilon_i\). The tensor is nonzero, highest of weight \(\lambda'\), and has scalar degree \(|\lambda|\). This proves (W7.26). No power greater than one of a single vector is used in an exterior algebra.

Every stable conclusion transports to the finite coefficient
\(a_{n,m}^{\lambda[mn]}\) in T-010's exact range
\[
m\ge\lambda_1,\qquad
n\ge\left\lfloor\frac{|\lambda|+\lambda_1}{2}\right\rfloor,
\qquad mn-|\lambda|\ge\lambda_1.
\]
These bounds are Sarkar, arXiv:2610.07929v2, Theorem 6.4. This report supplies the stated constituents of his stable module.


## T-020. The remaining data: a finite-dimensional valuation filtration

For each dominant integral weight \(\gamma\), fix a highest vector \(v_\gamma\) of the rational irreducible \(L_\gamma\) and define
\[
E_\gamma=(L_\gamma^*)^H,\qquad
F_{\gamma,\ge q}=
\{\ell\in E_\gamma:
v_\Delta(gH\mapsto\ell(g^{-1}v_\gamma))\ge q\}.
\tag{W7.27}
\]
The zero function has infinite valuation. This is a vector-space filtration, since the valuation of a sum is at least the smaller summand valuation. The exact equality is
\[
[L_\gamma:R]=\dim F_{\gamma,\ge0}.
\tag{W7.28}
\]
The central character determines its degree whenever it occurs. Equation (W7.28) follows from (W7.14) and
\(R=\{f\in R[\Delta^{-1}]:v_\Delta(f)\ge0\}\). If the highest matrix coefficient is in \(R\), its entire irreducible span is in \(R\), because \(R\) is \(G\)-stable. Thus testing this coefficient proves the assertion for the full equivariant map, not only one function.

Multiplication by \(\Delta^t\) identifies the open-orbit highest spaces at \(\gamma\) and \(\gamma+(3t)^7\), and increases their valuations by \(t\). Thus the determinant-shift coefficients are precisely the dimensions of steps in this filtration. T-018 calculates the entire filtration for the end-node sector. Elsewhere, computing only the \(G_2\times\mu_3\)-invariant dimensions leaves the extension condition unevaluated. Example (W7.22) proves that replacing the filtered dimension by the full invariant dimension can change the coefficient.

There is a precise published limitation on copying the rank-six free-generator formula to all weights. Michel Brion, *Invariants d'un sous-groupe unipotent maximal d'un groupe semi-simple*, Annales de l'Institut Fourier 33(1) (1983), Theorem 3, printed pages 12–13, and case \((A_6,\omega_3)\) of §III.1, printed page 14, prove that the full algebra \(R^U\) is not polynomial:
https://www.numdam.org/item/10.5802/aif.902.pdf

The cited case gives a concrete contradiction. Its quotient dimension is at least \(35-21=14\). There is one generator in degree one, one additional generator in degree two, and further generators have degree at least three, using
\(\operatorname{Sym}^2(\Lambda^3V)=S_{(2^3)}V\oplus S_{(2,1^4)}V\).
Polynomiality would force the sum of generator degrees to be at least \(1+2+12\cdot3=39\). Brion's Corollary 2 to Theorem 2 bounds this sum by \(35\) in the polynomial case. This excludes that particular free-polynomial-algebra formula for all weights. It permits finite presentations, standard monomial bases, and positive polytope sums. Formula (W7.18) supplies a polynomial sector with its exact multiplicity interpretation.

A concrete next orbit-based computation is the filtration (W7.27) outside this sector. Rota and Stein's nine symbolic covariants, printed page 847 of *Symbolic method in invariant theory*, PNAS 83 (1986), 844–847, give explicit tensor-valued candidates:
https://pmc.ncbi.nlm.nih.gov/articles/PMC322966/
Their tensor operations require conversion to a presentation or valuation basis before serving as a basis of all \(R^U\). No assertion that these nine diagrams are nine algebraically independent generators of \(R^U\) is used.

## Verification status and artifacts

The complete arguments T-016–T-020 were reread with attention to coordinate-ring duals, the finite stabilizer, scalar degrees, both determinant twists, adjugate divisibility, all zero-boundary cases in (W7.11), and the use of degreewise duality versus multiplication in the target algebra. No gap was found in the stated conclusions.

The orbit classification and generic-stabilizer identification are cited established inputs. Their statements and relevant source sections were read; their classification proofs were not independently reproduced. The complete extension and coefficient arguments used here are supplied above. The finite checker uses exact integers and symbolic one-variable matrix calculations; it is not a proof-assistant certificate.

Accompanying files:

- check_width7.py: Newton/Weyl verification and cubic-metric path calculation.
- END_NODE_CHECK.tsv: all seventy-five end-node partitions through symmetric degree ten.
- METRIC_PATH_CHECK.txt: exact metric matrix, determinant, and adjugate orders.
- The parent CHECK_EVENTS.tsv records actual proof-reading and computation events.

One initial symbolic-check run included an unjustified expected normalization scalar for \(\det B\). The computed scalar was different; the check was corrected to test the claimed invariant statement, namely nonzero determinant order exactly three. All final tests passed. No plethysm coefficient prediction failed.



