## SF-E807. Maximal-order extension at two

Let \(F=\mathbf Q(\sqrt{\Delta})\), where \(\Delta>1\) is even and squarefree. Suppose a polarized abelian fourfold \((X,\theta)\) has Rosati-invariant RM by \(F\), with tangent multiplicities \((2,2)\), and suppose its integral homology at two is stable under the maximal local order

\[
 R=\mathbf Z_2[u],\qquad u^2=\Delta.
\]

Assume that \(D=\int_X\theta^4/24\) is odd. For every \(\ell\in H^2(X,\mathbf Z_2)\), every positive integer \(r\), and every \(z\in\mathbf Q_2\) of valuation zero,

\[
 \frac{\ell^2}{2r}-zC\notin H^4(X,\mathbf Z_2),\qquad
 C=\frac{\theta_+^2+\theta_-^2}{2}.
 \tag{E807.1}
\]

Thus no perfect object, with any rational divisor normalization, has balanced normalized character \(r v_q\) when \(rq\) is a two-adic unit. No assumption on \(\operatorname{NS}(X)_{\mathbf Q}\) is needed. In particular every simple gluable fully semiregular lift for an effective finite coherent target action \(G\) as in S-22 satisfies

\[
 2\mid D|G|.
 \tag{E807.2}
\]

**Proof of the local lattice normalization.** Let \(L=H_1(X,\mathbf Z_2)\) and let \(E\) be its alternating polarization pairing. Since \(D\) is odd, \(E\) is perfect over \(\mathbf Z_2\). The polynomial \(t^2-\Delta\) is Eisenstein at two. More explicitly, for \(a,b\in\mathbf Z_2\), the valuation of \(a+bu\) in \(F\otimes\mathbf Q_2\), normalized by \(v(u)=1\), is

\[
 v(a+bu)=\min\{2v_2(a),\,2v_2(b)+1\};
\]

the two possible valuations have different parity. This gives the discrete valuation ring \(R\), whose uniformizer is \(u\). The torsion-free finite \(R\)-module \(L\) is free of rank four, by the elementary basis algorithm over a discrete valuation ring.

Define an \(R\)-valued form

\[
 \Psi(x,y)=E(x,uy)+uE(x,y).
 \tag{E807.3}
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
 \tag{E807.4}
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
 \tag{E807.5}
\]

This is integral over \(\mathbf Z_2\), its reduction is \(\omega^{[2]}=\operatorname{vol}_{S/2S}\), and

\[
 (Q_{(2,2)}/2)\bmod2=m^{[2]}+\omega\otimes\tau
\]

has rank six by the same exterior calculation as before. Multiplication of \(Q\) by the unit \(z\) leaves these two mod-two properties unchanged. The divided-square lifting lemma applied to \(zQ\) proves (E807.1).

For the perfect-object assertion, degree-two normalization again forces \(B=-c_1(E)/r\), and the degree-four comparison gives \(\operatorname{ch}_2(E)=c_1(E)^2/(2r)-(rq)C\). This contradicts (E807.1) when \(rq\) is a unit.

Finally suppose \(D|G|\) were odd. S-22 gives

\[
 \frac{4D(rq)^2}{|G|}=k,\qquad k\in\{2,4\}.
\]

For \(k=2\), the valuation of the rational square \((rq)^2\) would be \(-1\), impossible. For \(k=4\), \(rq\) is a two-adic unit, contrary to the integral assertion. This proves (E807.2). ∎

The extension allows every integral degree-two class, including extra classes at CM points. It covers every maximal-at-two lattice for even squarefree \(\Delta\), and every odd-degree compatible polarization. SF-E808 below treats the odd squarefree radicands ramified at two. A nonmaximal order at two and an even value of \(D|G|\) remain outside the combined obstruction. No eightfold supplier is constructed.

