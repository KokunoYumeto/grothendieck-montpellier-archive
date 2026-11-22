# SF-E806: Integral balanced-RM obstruction

## SF-E806. An all-rank integral obstruction on a principal real-multiplication datum

Let \(A=E_i^4\) with its product principal polarization \(\theta\), and let

\[
 U=\operatorname{diag}\left(
 \begin{pmatrix}1&1\\1&-1\end{pmatrix},
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}\right).
 \tag{E806.1}
\]

This integral symmetric endomorphism satisfies \(U^2=2I\), so it gives a Rosati-invariant maximal-order action of \(F=\mathbf Q(\sqrt2)\), of multiplicity two at each real embedding on the tangent space. Write \(\theta_\pm\) for the two real eigencomponents of \(\theta\), and put

\[
 C=\frac{\theta_+^2+\theta_-^2}{2}.
\]

**The integral assertion.** For every positive integer \(r\) and every integral class \(\ell\in H^2(A,\mathbf Z)\),

\[
 \frac{\ell^2}{2r}-C\notin H^4(A,\mathbf Z).
 \tag{E806.2}
\]

This quantifies over all integral degree-two classes, not only algebraic classes or the RM divisor plane. The same assertion holds on any deformation preserving this integral polarized RM datum.

Consequently there is no positive-rank perfect object \(E\), with any rational divisor normalization \(B\), satisfying

\[
 e^B\operatorname{ch}(E)
 =r\left(1-\frac{\theta_+^2}{2r}\right)
     \left(1-\frac{\theta_-^2}{2r}\right).
 \tag{E806.3}
\]

In particular, the datum has no ordinary simple gluable fully semiregular object of the balanced RM character in any positive rank. Indeed S-22 gives \(4q^2r^2\in\{2,4\}\) for such an object. Since \(q\) is positive rational, the value two would make \((qr)^2=1/2\), impossible in \(\mathbf Q\). Thus \(q=1/r\), which is (E806.3). This last implication uses the supplied S-22; the integral assertion below is independent of semiregularity and simplicity.

### The integral four-form and its obstruction tensor

Choose an integral basis \(a_0,b_0,\ldots,a_3,b_3\) of \(H^1(A,\mathbf Z)\), with \(\theta=\sum_i a_i b_i\); juxtaposition means exterior product. Set

\[
 \theta_U=\sum_{i,j}U_{ij}a_i b_j,\qquad
 \theta_\pm=\frac{\theta\pm\theta_U/\sqrt2}{2},\qquad
 Q=4C=\theta^2+\frac{\theta_U^2}{2}.
 \tag{E806.4}
\]

The divided square \(x^{[2]}=x^2/2\) of an integral two-form is integral. Thus \(Q\) is integral. Make the unimodular integral change of basis

\[
 \begin{aligned}
 s_0&=a_0+a_1,&s_1&=b_0+b_1,&t_0&=a_1,&t_1&=b_1,\\
 s_2&=a_2+a_3,&s_3&=b_2+b_3,&t_2&=a_3,&t_3&=b_3 .
 \end{aligned}
\]

Let \(S=\langle s_0,\ldots,s_3\rangle\), \(T=\langle t_0,\ldots,t_3\rangle\), and

\[
 \omega=s_0s_1+s_2s_3,\quad
 \tau=t_0t_1+t_2t_3,\quad
 m=s_0t_1+t_0s_1+s_2t_3+t_2s_3.
\]

Direct substitution gives

\[
 \theta=\omega-m+2\tau,\qquad
 \theta_U=\omega-2\tau.
 \tag{E806.5}
\]

Consequently

\[
 Q\bmod2=\omega^{[2]}=s_0s_1s_2s_3,\qquad
 R:=\frac{Q_{(2,2)}}2\bmod2
    =m^{[2]}+\omega\otimes\tau .
 \tag{E806.6}
\]

The subscript denotes the \(S,T\) bidegree. The mixed two-form \(m\) is a tensor of rank four in \(S\otimes T\). Its divided square is the exterior-square tensor of the corresponding isomorphism, and therefore has rank six in

\[
 \bigwedge^2(S/2S)\otimes\bigwedge^2(T/2T).
\]

Adding \(\omega\otimes\tau\), a rank-one tensor, leaves \(\operatorname{rank}R\ge5\). This is the only numerical rank needed below. The exact certificate computes rank six. The first identity in (E806.6) also shows that \(Q\) is primitive at two.

### A two-adic divided-square lifting lemma

Let \(L=S\oplus T\) be a free \(\mathbf Z_2\)-module with both summands of rank four. Suppose \(Q\in\bigwedge^4L\) has reduction equal to a nonzero volume form of \(S/2S\), and suppose the tensor

\[
 R=\frac{Q_{(2,2)}}2\bmod2
 \in\bigwedge^2(S/2S)\otimes\bigwedge^2(T/2T)
\]

has rank at least two. Then, for no positive integer \(r\) and no \(\ell\in\bigwedge^2L\), is

\[
 \ell^{[2]}-\frac r4Q\in r\bigwedge^4L.
 \tag{E806.7}
\]

The reduction assumption makes \(Q_{(2,2)}\) divisible by two, so the definition of \(R\) is meaningful.

**Proof.** Integrality of the left side forces \(4\mid r\), because \(Q\) has a unit coefficient. Write \(r=2^e k\), with \(k\) odd and \(e\ge2\). The alleged congruence is

\[
 \ell^{[2]}\equiv 2^{e-2}kQ\pmod {2^e}.
 \tag{E806.8}
\]

Its left side has minimum coefficient valuation exactly \(e-2\). If \(\ell=2^a\ell'\) with \(\ell'\) primitive, then \(2a\le e-2\). Dividing by \(2^{2a}\) reduces to the same congruence for \(\ell'\) and exponent \(e'=e-2a\ge2\). It therefore suffices to consider primitive \(\ell\).

If \(e=2\), then \(\ell^{[2]}\bmod2\) is the nonzero decomposable volume form of \(S/2S\). An alternating two-form over a field of characteristic two whose divided square is a nonzero decomposable four-form has rank four and support equal to the support of that four-form. Here is a direct check. In a symplectic basis it is a sum of disjoint pairs. If it has at least two pairs, every vector in its support occurs nontrivially in a contraction of its divided square, so the support of the divided square equals its own support. The nonzero decomposable divided square has support dimension four. Thus

\[
 \ell=\ell_0+2D,\qquad
 \ell_0\in\bigwedge^2S,
\]

with \(\ell_0\bmod2\) nondegenerate. In bidegree \((2,2)\), modulo four, its divided square is

\[
 \ell^{[2]}_{(2,2)}
   \equiv 2\ell_0\otimes D_{(0,2)}\pmod4.
\]

After division by two and reduction modulo two, this has tensor rank at most one. The right side of (E806.8) has tensor rank \(\operatorname{rank}R\ge2\). This is a contradiction.

Now suppose \(e\ge3\). The alternating elementary-divisor algorithm over \(\mathbf Z_2\) puts \(\ell\) in the form of a sum of disjoint pairs with coefficients \(2^{a_1},\ldots,2^{a_j}\), absorbing units into basis vectors. This algorithm follows by choosing an entry of minimum valuation, clearing its row and column using divisibility by that entry, and continuing on the complementary summand. Since \(\ell\) is primitive, \(a_1=0\). The minimum coefficient valuation of \(\ell^{[2]}\) is \(a_1+a_2=e-2\), so \(a_2=e-2\) and every subsequent coefficient has at least that valuation. In the original \(S,T\) coordinates we may consequently write

\[
 \ell=\alpha+2^{e-2}\beta,
\]

where \(\alpha\) is primitive and decomposable and \(\beta\) is integral. Dividing (E806.8) by \(2^{e-2}\) gives

\[
 \alpha\beta+2^{e-2}\beta^{[2]}\equiv kQ\pmod4.
 \tag{E806.9}
\]

Let \(P\) be the two-dimensional support of \(\bar\alpha=\alpha\bmod2\). Reducing (E806.9) modulo two gives

\[
 \bar\alpha\,\bar\beta=\operatorname{vol}_{S/2S}.
 \tag{E806.10}
\]

Every vector in \(P\) wedges to zero with the left side, hence with the right side. The wedge-annihilator of this nonzero decomposable volume form is \(S/2S\), so \(P\subset S/2S\). Comparing the \((2,2)\) and \((3,1)\) components in (E806.10) now gives

\[
 \bar\beta_{(0,2)}=0,\qquad
 \bar\beta_{(1,1)}\in P\otimes(T/2T).
 \tag{E806.11}
\]

Indeed wedge multiplication by the nonzero \(\bar\alpha\in\bigwedge^2P\) is injective on \(\bigwedge^2(T/2T)\); on \(S/2S\) its kernel is exactly \(P\).

Write \(\alpha=a b\), with \(\bar a,\bar b\) a basis of \(P\). The \(T\)-components of \(a,b\) are divisible by two. Thus \(\alpha_{(0,2)}\) is divisible by four, \(\alpha_{(1,1)}\) is divisible by two, and

\[
 (\alpha_{(1,1)}/2)\bmod2\in P\otimes(T/2T).
\]

Consider the \((2,2)\) component of \(\alpha\beta\), divide by two, and reduce modulo two. Its three contributions are

\[
 \alpha_{(2,0)}\beta_{(0,2)},\quad
 \alpha_{(1,1)}\beta_{(1,1)},\quad
 \alpha_{(0,2)}\beta_{(2,0)}.
\]

The first, after division, has its \(S\)-factor in the line \(\mathbf F_2\bar\alpha\). The second has both of its \(S\)-factors in \(P\) by (E806.11), so its \(S\)-factor lies in the same line \(\bigwedge^2P\). The third vanishes after division and reduction.

If \(e\ge4\), the correction \(2^{e-2}\beta^{[2]}\) in (E806.9) vanishes modulo four. If \(e=3\), dividing its \((2,2)\) component by two gives

\[
 (\bar\beta^{[2]})_{(2,2)}
  =\bar\beta_{(2,0)}\bar\beta_{(0,2)}
     +(\bar\beta_{(1,1)})^{[2]}.
\]

The first term is zero by (E806.11); the second again has its \(S\)-factor in \(\bigwedge^2P\). In every case the \((2,2)\) component of the left side of (E806.9), divided by two modulo two, belongs to

\[
 \mathbf F_2\bar\alpha\otimes
       \bigwedge^2(T/2T),
\]

and has tensor rank at most one. The right side gives \(kR=R\), of rank at least two. This final contradiction proves the lemma. ∎

### Application to Chern characters

Apply the lemma to (E806.6), where \(\operatorname{rank}R=6\). This proves (E806.2). If an object satisfied (E806.3), its degree-two part would force \(B=-\ell/r\), where \(\ell=c_1(E)\). Comparing degree four then gives

\[
 \operatorname{ch}_2(E)=\frac{\ell^2}{2r}-C.
 \tag{E806.12}
\]

The left side is integral on a complex torus: the formula \(\operatorname{ch}_2(E)=\ell^2/2-c_2(E)\) holds for perfect K-classes, the second Chern class is integral, and the divided square of every integral two-form is integral in the exterior cohomology lattice. This contradicts (E806.2).

The obstruction is topological in the displayed integral RM datum. It therefore persists when the point is deformed to a simple or non-CM fourfold with the same datum. It is stronger than the minimal-divisor-space hypothesis in supplied S-32 for this datum, because every integral \(\ell\) was allowed. The following local argument extends the assertion to other integral data without imposing a hypothesis on the Néron--Severi space.

### SF-E806a. Maximal-order extension at two

Let \(F=\mathbf Q(\sqrt{\Delta})\), where \(\Delta>1\) is even and squarefree. Suppose a polarized abelian fourfold \((X,\theta)\) has Rosati-invariant RM by \(F\), with tangent multiplicities \((2,2)\), and suppose its integral homology at two is stable under the maximal local order

\[
 R=\mathbf Z_2[u],\qquad u^2=\Delta.
\]

Assume that \(D=\int_X\theta^4/24\) is odd. For every \(\ell\in H^2(X,\mathbf Z_2)\), every positive integer \(r\), and every \(z\in\mathbf Q_2\) of valuation zero,

\[
 \frac{\ell^2}{2r}-zC\notin H^4(X,\mathbf Z_2),\qquad
 C=\frac{\theta_+^2+\theta_-^2}{2}.
 \tag{E806.13}
\]

Thus no perfect object, with any rational divisor normalization, has balanced normalized character \(r v_q\) when \(rq\) is a two-adic unit. No assumption on \(\operatorname{NS}(X)_{\mathbf Q}\) is needed. In particular every simple gluable fully semiregular lift for an effective finite coherent target action \(G\) as in S-22 satisfies

\[
 2\mid D|G|.
 \tag{E806.14}
\]

**Proof of the local lattice normalization.** Let \(L=H_1(X,\mathbf Z_2)\) and let \(E\) be its alternating polarization pairing. Since \(D\) is odd, \(E\) is perfect over \(\mathbf Z_2\). The polynomial \(t^2-\Delta\) is Eisenstein at two. More explicitly, for \(a,b\in\mathbf Z_2\), the valuation of \(a+bu\) in \(F\otimes\mathbf Q_2\), normalized by \(v(u)=1\), is

\[
 v(a+bu)=\min\{2v_2(a),\,2v_2(b)+1\};
\]

the two possible valuations have different parity. This gives the discrete valuation ring \(R\), whose uniformizer is \(u\). The torsion-free finite \(R\)-module \(L\) is free of rank four, by the elementary basis algorithm over a discrete valuation ring.

Define an \(R\)-valued form

\[
 \Psi(x,y)=E(x,uy)+uE(x,y).
 \tag{E806.15}
\]

The Rosati-invariance identity \(E(ux,y)=E(x,uy)\) shows directly that \(\Psi\) is \(R\)-bilinear. It is alternating: \(E(x,ux)=E(ux,x)=-E(x,ux)\), hence \(E(x,ux)=0\), as the target has characteristic zero.

Put \(\kappa=1/(2u)\). For \(a+bu\in R\), one has

\[
 \operatorname{Tr}(\kappa(a+bu))=b,\qquad
 \operatorname{Tr}(\kappa u(a+bu))=a.
\]

The trace pairing \((v,w)\mapsto\operatorname{Tr}(\kappa vw)\) is therefore a perfect \(\mathbf Z_2\)-pairing on \(R\), and

\[
 E(x,y)=\operatorname{Tr}(\kappa\Psi(x,y)).
\]

It follows that \(\Psi:L\longrightarrow\operatorname{Hom}_R(L,R)\) is an isomorphism: composing with the displayed perfect trace identification is exactly the given perfect \(\mathbf Z_2\)-duality for \(E\). Choose a symplectic \(R\)-basis \(x_1,y_1,x_2,y_2\), with \(\Psi(x_i,y_j)=\delta_{ij}\). Such a basis follows by choosing a primitive vector \(x_1\), finding \(y_1\) with pairing one using perfectness, splitting off their span by the usual orthogonal projection, and repeating.

Let \(\alpha_i,\beta_i,\gamma_i,\delta_i\) be the \(\mathbf Z_2\)-dual basis to \(x_i,ux_i,y_i,uy_i\). Directly evaluating \(E\) and \(E(u\,\cdot,\cdot)\) gives

\[
 \theta=m:=\sum_{i=1}^2(\alpha_i\delta_i+\beta_i\gamma_i),
 \qquad
 \theta_u=\omega+\Delta\tau,
 \tag{E806.16}
\]

where

\[
 \omega=\alpha_1\gamma_1+\alpha_2\gamma_2,\qquad
 \tau=\beta_1\delta_1+\beta_2\delta_2.
\]

Take \(S=\langle\alpha_1,\gamma_1,\alpha_2,\gamma_2\rangle\) and \(T=\langle\beta_1,\delta_1,\beta_2,\delta_2\rangle\). The mixed tensor \(m\) is again nondegenerate. Write \(\Delta=2h\), with \(h\) odd. The eigencomponent formula gives

\[
 Q=4C=\theta^2+\frac{\theta_u^2}{\Delta}
   =2m^{[2]}+\frac1h\omega^{[2]}
          +2\omega\tau+4h\tau^{[2]}.
 \tag{E806.17}
\]

This is integral over \(\mathbf Z_2\), its reduction is \(\omega^{[2]}=\operatorname{vol}_{S/2S}\), and

\[
 (Q_{(2,2)}/2)\bmod2=m^{[2]}+\omega\otimes\tau
\]

has rank six by the same exterior calculation as before. Multiplication of \(Q\) by the unit \(z\) leaves these two mod-two properties unchanged. The divided-square lifting lemma applied to \(zQ\) proves (E806.13).

For the perfect-object assertion, degree-two normalization again forces \(B=-c_1(E)/r\), and the degree-four comparison gives \(\operatorname{ch}_2(E)=c_1(E)^2/(2r)-(rq)C\). This contradicts (E806.13) when \(rq\) is a unit.

Finally suppose \(D|G|\) were odd. S-22 gives

\[
 \frac{4D(rq)^2}{|G|}=k,\qquad k\in\{2,4\}.
\]

For \(k=2\), the valuation of the rational square \((rq)^2\) would be \(-1\), impossible. For \(k=4\), \(rq\) is a two-adic unit, contrary to the integral assertion. This proves (E806.14). ∎

The extension allows every integral degree-two class, including extra classes at CM points. It covers every maximal-at-two lattice for even squarefree \(\Delta\), and every odd-degree compatible polarization. It does not yet treat odd squarefree \(\Delta\equiv3\pmod4\) without the supplied minimal-divisor-space hypothesis, a nonmaximal order at two, or an even value of \(D|G|\). No eightfold supplier is constructed.

