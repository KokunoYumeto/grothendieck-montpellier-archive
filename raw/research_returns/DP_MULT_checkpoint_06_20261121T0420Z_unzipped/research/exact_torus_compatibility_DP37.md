# DP37: exact Cartier-dual compatibility of the displayed torus

Run DP_MULT_20261121. Author: `/root/archive_binomial`, GPT-6 Astra Pro, inherited model; runtime reasoning effort not exposed. Date: 2026-11-21 UTC. This is a complete proof of the exact embedding compatibility for DP32's already identified actual-dual model. The parent assigned the stable finding ID **DP37**. The averaging construction itself is left to the parent.

## 1. Statement

Let $p$ be any prime, $h\ge2$, $q=p^h$, $d=h-1$, and $\mathcal O=W(\mathbf F_q)$. Let $G_h$ be the Honda/Lubin--Tate line with logarithm

\[
L_0(T)=\sum_{n\ge0}\frac{T^{q^n}}{p^n},
\]

and identify its actual Cartier dual $H=G_h^D$ with the integral $d$-dimensional model constructed in DP32. Thus its logarithm is

\[
\mathcal L(\mathbf X)=\sum_{n\ge0}\frac{M^{\circ n}(\mathbf X)}{p^n},
\qquad M_1=X_d^{p^2},\quad M_i=X_{i-1}^p\ (i\ge2).
\]

For a primitive $(q-1)$-st root of unity $\zeta\in\mathcal O$, put

\[
A_\zeta(\mathbf X)
=(\zeta^pX_1,\zeta^{p^2}X_2,\ldots,\zeta^{p^d}X_d).
\]

Then $A_\zeta$ is an integral automorphism of $H$, and its Cartier dual on the Honda line is exactly

\[
\boxed{A_\zeta^D=[\zeta]_{G_h}.}
\tag{37.1}
\]

In particular the differential is $\zeta$, not another Frobenius conjugate. The equality holds for every $(q-1)$-st root by taking powers, and persists under integral base change. Thus the diagonal action

\[
([\zeta]_{G_h},A_\zeta^{-1})
\]

has precisely the additive-logarithm characters used in DP36:

\[
(x,y_1,\ldots,y_d)\longmapsto
(\zeta x,\zeta^{-p}y_1,\ldots,\zeta^{-p^d}y_d).
\tag{37.2}
\]

## 2. Complete proof

### 2.1. The displayed automorphism exists integrally

For an ordinary arrow, $p\cdot p^{i-1}=p^i$. For the exceptional arrow,

\[
p^2p^d=p^{h+1}\equiv p\pmod{q-1}.
\]

Therefore $M A_\zeta=A_\zeta M$, and the same relation holds for every iterate of $M$, for $\mathcal L$, and for its formal inverse. Consequently the integral formal law of DP32 satisfies

\[
F_H(A_\zeta\mathbf X,A_\zeta\mathbf Y)
=A_\zeta F_H(\mathbf X,\mathbf Y).
\]

The diagonal coefficients are units, and $A_\zeta^{q-1}=1$. This is an integral formal-group automorphism. It acts on the associated $p$-divisible group and hence has a Cartier-dual automorphism

\[
a=A_\zeta^D:G_h\longrightarrow G_h.
\]

The passage between the connected formal group and its $p$-divisible group is already supplied by DP32 and Tate's equivalence. Write $\lambda=da\in\mathcal O^\times$ for the scalar on the one-dimensional tangent space of the line.

### 2.2. A functorial Hodge--Tate sequence detects the missing character

Put $K_0=\operatorname{Frac}(\mathcal O)$ and let $C$ be the completed algebraic closure of $K_0$. Write $T_pG_h$ for the free $\mathbf Z_p$ Tate module of rank $h$, and $\mathbf Z_p(1)=T_p\mu_{p^\infty}$.

Use Tate, *p-Divisible Groups* (1967), **§4, Corollary 2 following Theorem 3, printed p. 180**. The proof on that page gives the natural exact sequence underlying its canonical Hodge--Tate decomposition:

\[
0\longrightarrow \operatorname{Lie}(G_h^D)_C
\longrightarrow \operatorname{Hom}_{\mathbf Z_p}(T_pG_h,C)
\longrightarrow \operatorname{Lie}(G_h)_C^*
 \otimes_C\operatorname{Hom}_{\mathbf Z_p}(\mathbf Z_p(1),C)
\longrightarrow0.
\tag{37.3}
\]

Its maps come from the Cartier pairing and its differential, as constructed on printed pp. 177--180. They are natural for endomorphisms. For the endomorphism $a$ of $G_h$, the action on the middle term is **precomposition** by $T_pa$; the action on the first term is $d(a^D)=dA_\zeta$; the action on the line's cotangent factor is pullback by $a$, hence the scalar $\lambda$. The cyclotomic factor is unchanged. These are adjoint/pullback actions: no inverse eigenvalue is introduced by writing the cotangent or Hom space.

For completeness, this naturality uses the equality of Cartier pairings

\[
\langle aP,Q\rangle=\langle P,a^DQ\rangle.
\]

Differentiating and passing to the Tate-module limit gives the asserted actions in (37.3). We only need the exact sequence and its characteristic-polynomial multiplicativity; no extra choice of Hodge--Tate splitting is required.

Let $P_a(Z)$ be the characteristic polynomial of $T_pa$ on the rank-$h$ $\mathbf Z_p$ module $T_pG_h$. It is monic of degree $h$ with coefficients in $\mathbf Z_p$. Precomposition on its $C$-linear dual has the transpose matrix, and therefore the same characteristic polynomial. Sequence (37.3) gives

\[
P_a(Z)
=(Z-\lambda)\prod_{i=1}^{h-1}(Z-\zeta^{p^i})
\quad\text{in }C[Z].
\tag{37.4}
\]

The element $\zeta^p$ has degree exactly $h$ over $\mathbf Q_p$. Indeed it is a primitive $(p^h-1)$-st root in the unramified degree-$h$ field, its Frobenius conjugates are $\zeta^{p^j}$, and no positive exponent $m<h$ satisfies $p^m\equiv1\pmod{p^h-1}$, since $0<p^m-1<p^h-1$. Its minimal polynomial is therefore

\[
Q(Z)=\prod_{j=0}^{h-1}(Z-\zeta^{p^j}),
\qquad\deg Q=h.
\tag{37.5}
\]

Because $\zeta^p$ is a root of $P_a$ and $P_a\in\mathbf Q_p[Z]$, $Q$ divides $P_a$. Both are monic of degree $h$, so $P_a=Q$. The $h$ displayed Frobenius conjugates are distinct. Comparing (37.4) and (37.5) proves

\[
\lambda=\zeta.
\tag{37.6}
\]

This determines the exact embedding; equality of Newton slopes alone would not determine it.

### 2.3. The differential determines the endomorphism

Over the characteristic-zero field $K_0$, conjugating a one-dimensional formal-group endomorphism by the normalized logarithm gives an additive formal power series. Such a series is linear: comparing the coefficient of $X^{n-1}Y$ in additivity kills every coefficient of degree $n\ge2$. Thus

\[
L_0(a(T))=\lambda L_0(T)=\zeta L_0(T).
\]

The Lubin--Tate endomorphism $[\zeta]$ has the same logarithm identity, so $a=[\zeta]$ over $K_0$ and hence over the integral coefficient ring. Equivalently, here $[\zeta](T)=\zeta T$, since $L_0(\zeta T)=\zeta L_0(T)$.

This establishes (37.1). Cartier duality and taking powers give the statement for the entire finite torus. Taking logarithms gives (37.2). The assertion was proved over $\mathcal O$; all series and maps are integral there, so it persists after the integral base extensions used in DP36. The argument includes $p=2$ and $h=2$.

## 3. Consequence for the identity biextension class

The statement just proved supplies the exact compatibility needed for the parent’s averaging argument. Under the usual functorial correspondence sending the canonical Poincaré biextension of $G_h\times H$ to the identity in

\[
\operatorname{Hom}(G_h,H^D)=\operatorname{End}(G_h),
\]

pullback by $(f,g)$ sends the classifying map $u$ to $g^D\circ u\circ f$. For $f=[\zeta]$ and $g=A_\zeta^{-1}$, (37.1) gives

\[
g^D\circ\operatorname{id}\circ f
=[\zeta^{-1}]\circ[\zeta]=\operatorname{id}.
\]

Thus this diagonal torus fixes the identity class, with the exact embedding and inverse sign required. This consequence does not itself construct a rational frame, logarithm representative or integral averaged coboundaries. Those constructions and any claim about a prescribed theta section remain separate. In particular, the present lemma imposes no geometric path or optimality assertion.

## 4. Exact source and verification scope

Primary source: J. Tate, *p-Divisible Groups*, in *Proceedings of a Conference on Local Fields*, Springer, 1967, pp. 158--183. The precise result used is **Corollary 2 immediately following Theorem 3, printed p. 180**, together with its displayed exact sequence on that page. Theorem 3 is on printed p. 179. This is not the different Corollary 2 on printed p. 181 following Theorem 4.

The supplied/local primary PDF is `research/Tate_PDivisible_1967.pdf`, retrieved earlier from `https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf`. I read the extracted primary text covering the construction and corollary, and directly viewed its original printed p. 180 in `late_proof_snapshots/tate_hodge_tate_cor2_p180.png` (PDF page 12). The visible formula uses the cotangent space of $G$ and the tangent space of $G^D$, exactly as in (37.3).

The classical Hodge--Tate theorem is cited rather than re-proved. The new short argument determines the exact torus embedding from its functorial characteristic-polynomial consequence. A subsequent whole-saved-proof reading and hash event records the completed check; no requested future independent review is counted as finished.
