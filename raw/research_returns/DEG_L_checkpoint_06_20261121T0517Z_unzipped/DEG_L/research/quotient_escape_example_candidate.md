# Candidate B25a: an exact fourfold realization of the quotient escape

Status: separate candidate, pending independent whole-proof review. Date 2026-11-21. Author: /root/lvalue_bounds, GPT-6 Astra Pro; effort not exposed. Root proposed the fourfold refinement of the author's surface example. This example has a full rank-one CM field and a fixed integral quadratic action, but its CM type is imprimitive and its abelian varieties are not simple.

## Statement

Let
\[
 F=\mathbf Q(\zeta_3),\qquad K=\mathbf Q(i),\qquad
 E=\mathbf Q(\zeta_{24}),\qquad t=\zeta_{24},\quad \omega=\zeta_3.
\]
Use the CM type of $E$ induced from the fixed complex embedding of $F$ sending $\omega$ to $e^{2\pi i/3}$. Put $\mathcal O_m=\mathbf Z+m\mathcal O_F$ and identify the rational homology with the one-dimensional $E$-space using the $F$-basis
\[
 (e_1,e_2,e_3,e_4)=(1,i,t,it).
\]
Then
\[
 A_0=\mathbf C^4/\mathcal O_F^4,\qquad
 A_m=\mathbf C^4/\mathcal O_m^4\quad(m\ge1)
\]
are abelian fourfolds with product principal polarizations $L_0,L_m$, rational $E$ action with Rosati complex conjugation, and integral $\mathcal O_K$ action of signature $(2,2)$. Their source homology lattice is $I_0=\mathcal O_E$ and their target lattice is
\[
 \Lambda_m=\mathcal O_m e_1\oplus\mathcal O_m e_2
              \oplus\mathcal O_m e_3\oplus\mathcal O_m e_4.
\]
Its maximal-order core and hull, numerical core index, and relative $K$ determinant ideal are
\[
 \Lambda_m^-=m\mathcal O_E,\qquad \Lambda_m^+=\mathcal O_E,
 \qquad J_m=m^4,
 \qquad \mathfrak j_m=(m^2)\mathcal O_K.
\tag{B25a.1}
\]

Multiplication by $m$ gives an $E$-linear polarized isogeny
\[
 h_m:A_0\longrightarrow A_m,\qquad
 \deg h_m=m^4,
 \qquad h_m^*c_1(L_m)=m c_1(L_0).
\tag{B25a.2}
\]
Let $Z_0$ be the coordinate plane with coordinates 2 and 4 equal to zero, and let $Z_m=h_m(Z_0)_{\rm red}$. These are integral surfaces with nonzero $K$-Weil projection and
\[
 \deg_{L_0}Z_0=\deg_{L_m}Z_m=2,
 \qquad (h_m)_*Z_0=m^2 Z_m.
\tag{B25a.3}
\]
For the intermediate quotient of B25,
\[
 H_m=\ker h_m\cap\operatorname{Stab}(Z_0),\qquad
 G_m=\mathcal O_K H_m,
\]
one has
\[
 |H_m|=m^2,\qquad
 G_m=\ker h_m,\qquad |G_m|=m^4,
 \qquad B_m=A_0/G_m\simeq A_m.
\tag{B25a.4}
\]
Thus the residual isogeny is an isomorphism and the intermediate core index equals the entire target index. For $m>1$, $G_m$ is not $\mathcal O_E$-stable. The scalar multiplicity $m^2$ in (B25a.3) removes exactly the determinant-ideal content $(m^2)$ of the multiplicity-preserving pushforward. This supplies a geometric realization of the escape allowed by B25, without asserting any such escape on simple CM fourfolds.

## Proof

### 1. The maximal order and the induced CM coordinates

The cyclotomic integral-basis theorem gives $\mathcal O_E=\mathbf Z[t]$ and $\mathcal O_F=\mathbf Z[\omega]$. Here $i=t^6$, $\omega=t^8$, and
\[
 t^2=-i\omega.
\]
Consequently
\[
 \mathbf Z[t]=\mathcal O_F[i]+t\mathcal O_F[i].
\]
The two summands are independent over $F(i)$ since $[E:F(i)]=2$. The summands $\mathcal O_F+i\mathcal O_F$ are independent over $F$ since $[F(i):F]=2$. Hence
\[
 \mathcal O_E=\mathcal O_F\oplus i\mathcal O_F
               \oplus t\mathcal O_F\oplus it\mathcal O_F
\tag{B25a.5}
\]
with the displayed basis. The degree assertions follow either from the cyclotomic degrees $\varphi(24)=8$, $\varphi(12)=4$, and $\varphi(3)=2$, or from the distinct imaginary quadratic fields $F,K$ and the quadratic relation for $t$.

In the CM type induced from $F$, the natural representation of $E$ on $\mathbf C^4$ is the regular $F$-linear representation in this basis, after the fixed embedding of $F$ into $\mathbf C$. It has precisely the four embeddings of $E$ extending that embedding of $F$. Thus it is the stated CM type, and the rational homology is rank one over $E$.

Multiplication by $i$ has the integral matrix
\[
 J=\operatorname{diag}\left(
 \begin{pmatrix}0&-1\\1&0\end{pmatrix},
 \begin{pmatrix}0&-1\\1&0\end{pmatrix}\right).
\tag{B25a.6}
\]
Its analytic eigenvalues are $i,-i$, each twice. Multiplication by $t$ maps
\[
 e_1\mapsto e_3,\quad e_2\mapsto e_4,\quad
 e_3\mapsto-\omega e_2,\quad e_4\mapsto\omega e_1.
\tag{B25a.7}
\]
This matrix is monomial and unitary for the product Hermitian form because $|\omega|=1$. Therefore its Rosati adjoint is multiplication by $t^{-1}=\bar t$. Since $t$ generates $E$, the full rational $E$ action has Rosati involution equal to CM conjugation. The same assertion holds on every $A_m$: the product polarization metric changes by a common positive scalar in the four coordinates, so the adjoint matrices are unchanged. The matrix $J$ preserves $\mathcal O_m^4$ for every $m$, giving the fixed integral maximal quadratic-order action.

Each factor $\mathbf C/\mathcal O_m$ is an elliptic curve with its degree-one polarization; the product gives the asserted principally polarized fourfold. Every multiplication matrix for $E$ preserves a suitable integer multiple of the homology lattice, so its action remains rational and algebraic. No claim of integral $\mathcal O_E$ action on $A_m$ is made when $m>1$.

### 2. Core, hull, and determinant ideal

The largest $\mathcal O_F$-stable sublattice in $\mathcal O_m$ is $m\mathcal O_F$. Indeed write $x=a+mb\omega$ with $a,b\in\mathbf Z$. Since $\omega^2=-1-\omega$,
\[
 \omega x=-mb+(a-mb)\omega.
\]
The condition $\omega x\in\mathcal O_m$ forces $m\mid a$, and conversely every element of $m\mathcal O_F$ remains in $\mathcal O_m$ under $\mathcal O_F$. As $\mathcal O_E$ contains $\mathcal O_F$, the maximal-order core of $\Lambda_m$ is contained in $m\mathcal O_F^4=m\mathcal O_E$. The latter is itself an $\mathcal O_E$-ideal contained in $\Lambda_m$, so equality follows. The hull is $\mathcal O_E$ since $\Lambda_m\subset\mathcal O_E$ contains 1. Each coordinate contributes index $[\mathcal O_m:m\mathcal O_F]=m$, proving $J_m=m^4$.

For the relative determinant, use the $\mathcal O_K$-basis $(1,\omega,t,\omega t)$ of $\mathcal O_E$. It gives
\[
 \Lambda_m=\mathcal O_K\oplus m\omega\mathcal O_K
                    \oplus t\mathcal O_K\oplus m\omega t\mathcal O_K.
\]
Thus $\det_K\Lambda_m=(m^2)\det_K\mathcal O_E$ while $\det_K(m\mathcal O_E)=(m^4)\det_K\mathcal O_E$. Their quotient is $(m^2)\mathcal O_K$, as in (B25a.1), whose norm is $m^4$.

### 3. Isogeny, witness, and quotient

Multiplication by $m$ maps $\mathcal O_E$ into $\Lambda_m$. Its degree is $[\Lambda_m:m\mathcal O_E]=m^4$. On each elliptic factor the target fundamental area is $m$ times that of the source. A degree-one polarization has invariant two-form inversely proportional to this area, and multiplication by $m$ multiplies that two-form by $m^2$. Hence pullback multiplies the polarization by $m$, proving (B25a.2).

The restriction to the selected two coordinates is the product of two degree-$m$ elliptic isogenies. Its generic degree is $m^2$, and its image is exactly the corresponding coordinate plane in $A_m$. The product polarization on two elliptic factors has square 2, proving (B25a.3).

One of the two Weil lines, namely $\bigwedge^4 H^1(A_m,\mathbf C)_{J^*=i}$, contains
\[
 \eta=(dz_1+i\,dz_2)\wedge(dz_3+i\,dz_4)
       \wedge(d\bar z_1+i\,d\bar z_2)
       \wedge(d\bar z_3+i\,d\bar z_4).
\]
Its restriction to $Z_m$ is
$dz_1\wedge dz_3\wedge d\bar z_1\wedge d\bar z_3$, with nonzero integral. The self-adjoint Weil projector therefore detects a nonzero Weil component of $[Z_m]$. The same argument applies to $Z_0$.

The kernel in a single elliptic coordinate is
\[
 m^{-1}\mathcal O_m/\mathcal O_F
       =(m^{-1}\mathbf Z+\mathcal O_F)/\mathcal O_F\simeq\mathbf Z/m\mathbf Z.
\]
The stabilizer of the coordinate plane $Z_0$ is $Z_0$ itself. Its kernel intersection $H_m$ consists of the first and third kernel coordinates and has order $m^2$. Applying $J$ moves these to the second and fourth coordinates, so
\[
 H_m\cap iH_m=0,\qquad H_m+iH_m=\ker h_m.
\]
This proves (B25a.4) and the residual-isomorphism assertion. For $m>1$, the class of $m^{-1}e_3$ belongs to $G_m$, but multiplication by $t$ sends it to $-m^{-1}\omega e_2$. Its image under $h_m$ is $-\omega e_2$, which is not in $\Lambda_m$; hence it is not in $G_m$. Thus $G_m$ is not $\mathcal O_E$-stable.

Finally $\mathfrak j_m=(m^2)$ and $h_{m*}Z_0=m^2Z_m$ prove the exact cancellation of that scalar ideal content. The displayed bounded target witnesses are abelian subvarieties, and their stabilizers have positive dimension. The simple-source hypotheses of B20--B22a therefore do not apply. QED.

## Primary inputs

J.S. Milne, *Algebraic Number Theory*, version 3.08, Theorem 6.4(a)--(b), printed p.99, gives the degree and maximal order of a cyclotomic field. Its full displayed proof on p.99 and the complete supporting Lemma 6.5 proof on p.100 were read in this run; lower prerequisites are imported. Source: <https://www.jmilne.org/math/CourseNotes/ANT.pdf>. The identity (B25a.5) is proved explicitly above from that theorem and the powers of $t$.

J.S. Milne, *Abelian Varieties*, version 2.00, Chapter I, Theorems 2.8--2.9, printed p.14, and polarization definition printed p.15, supply the usual algebraicity of polarized complex tori and of their analytic homomorphisms. These exact statements and the complete brief proof sketch were read in this run; no full Riemann-criterion proof is claimed. Source: <https://www.jmilne.org/math/CourseNotes/AV.pdf>.
