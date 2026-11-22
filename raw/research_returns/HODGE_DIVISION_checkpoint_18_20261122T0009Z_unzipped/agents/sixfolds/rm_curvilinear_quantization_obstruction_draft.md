# SF-E820: common curvilinear point modules cannot repair the balanced character

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

**Status:** New complete proof, awaiting independent whole-proof review. This is a separate extension of SF-E819R to a specified nonreduced family. No conclusion for arbitrary Artinian defect modules is asserted.

## 1. Precise local and global statements

Let \(R=\mathbf C[[z_1,z_2,z_3,z_4]]\), and let \(\pi_+,\pi_-\) be constant bivectors that have rank two and complementary two-dimensional supports. In particular,

\[
 \pi_+\wedge\pi_+=\pi_-\wedge\pi_-=0,
 \qquad \pi_+\wedge\pi_-\ne0.
 \tag{E820.1}
\]

Let \(I\subset R\) be a curvilinear ideal of positive colength \(\ell\). This means that there are formal parameters \(u_1,u_2,u_3,u_4\) with

\[
 I=(u_1^\ell,u_2,u_3,u_4),\qquad
 A=R/I\simeq\mathbf C[t]/(t^\ell).
 \tag{E820.2}
\]

Suppose that a finite \(R\)-module \(M\) has a map to a free hull

\[
 0\longrightarrow T\longrightarrow M\xrightarrow{\phi}R^r
     \longrightarrow Q\longrightarrow0,
 \qquad T\simeq A^n,\quad Q\simeq A^m.
 \tag{E820.3}
\]

If \(m+n>0\), then \(M\) cannot admit flat first-order deformations for both multiplication classes \(\pi_+\) and \(\pi_-\).

Consequently, a balanced sheaf in the scope of SF-E819 cannot be weakly semiregular for any specified effective coherent finite translation/tensor action if it has a nontrivial local modification of type(E820.3) at even one point. The formal parameters in(E820.2) need not be simultaneous constant coordinates for the bivectors. Their brackets in the new parameters are retained in the proof.

## 2. The extension matrices over the Artinian quotient

The local trace lemma SF-E819 gives \(\ell m=\ell n\), hence \(m=n\), as soon as either nonzero bivector deformation exists. If one of \(m,n\) were zero while their sum were positive, this already gives a contradiction. We can therefore assume \(m=n>0\).

Choose a basis of the free hull so that its quotient to \(Q=A^m\) is reduction modulo \(I\) on the first \(m\) coordinates. Such a basis exists: lift the quotient matrix to \(R\); an invertible \(m\)-minor modulo the maximal ideal is a unit minor over \(R\), and elementary invertible changes reduce the surjection to the displayed projection. Its kernel is

\[
 K=I^{\oplus m}\oplus R^{r-m}.
 \tag{E820.4}
\]

The free summand contributes no \(\operatorname{Ext}^1(-,T)\), so it splits off from the extension by \(T\). Put

\[
 f_1=u_1^\ell,\quad f_2=u_2,\quad f_3=u_3,\quad f_4=u_4.
\]

This is a regular sequence. For each \(v\in\mathbf C^m\), choose a lift \(e_i(v)\in M\) of \(f_i v\in I^m\). The Koszul presentation gives matrices

\[
 B_{ij}\in\operatorname{Mat}_m(A),\qquad B_{ij}=-B_{ji},
\]

such that

\[
 f_i e_j(v)-f_j e_i(v)=B_{ij}v\in T.
 \tag{E820.5}
\]

These matrices encode the whole extension class. Indeed applying \(\operatorname{Hom}_R(-,T)\) to the Koszul resolution of \(A^m\) makes every differential zero, since \(I T=0\). Thus

\[
 \operatorname{Ext}^1_R(K,T)
  \simeq\operatorname{Ext}^2_R(A^m,A^m)
  \simeq\operatorname{Mat}_m(A)\otimes\bigwedge^2\mathbf C^4.
 \tag{E820.6}
\]

There is no condition that \(\mathfrak m T=0\); only \(I T=0\) is used here. This is the change from the reduced calculation.

## 3. Necessary equations for each bivector deformation

Assume a flat first-order deformation for one of the bivectors \(\pi\). Lift \(\phi\) to the free deformed hull by SF-E819, section2.1. For an element of \(T\), the image of a chosen lift is \(\varepsilon\) times a hull vector. Its class modulo \(K\) is independent of the lift, since changing that lift by \(\varepsilon M\) changes the vector by an element of \(K\). It defines an \(R\)-linear map

\[
 C:T\longrightarrow Q,
 \qquad C\in\operatorname{Mat}_m(A).
 \tag{E820.7}
\]

Linearity follows by applying the deformed hull map to a lifted product: its reduction on \(T\) is zero, so only the ordinary product remains in the coefficient of \(\varepsilon\).

Lift(E820.5), apply the lifted hull map, and reduce its \(\varepsilon\)-coefficient modulo \(I\) in the first \(m\) hull coordinates. Terms \(f_i a_j-f_j a_i\) vanish modulo \(I\). The correction to the lifted module relation maps into \(K\) and also vanishes. The first-order commutator is the Poisson bracket of the actual formal functions \(f_i,f_j\). Consequently

\[
 C B_{ij}=P(\pi)_{ij}I_m,
 \qquad P(\pi)_{ij}=\pi(df_i,df_j)\pmod I.
 \tag{E820.8}
\]

The constant-coordinate star product is evaluated on these possibly nonlinear functions. No unsupported claim that the brackets stay constant after straightening the curvilinear scheme is made.

## 4. A unit coefficient makes both bracket forms proportional

The cotangent vectors \(du_2(0),du_3(0),du_4(0)\) span a three-dimensional subspace \(W\) of the four-dimensional cotangent space. The restriction of at least one of \(\pi_+,\pi_-\), viewed as alternating bilinear forms on that cotangent space, is nonzero on \(W\).

For completeness, a rank-two alternating form on a four-dimensional space has a two-dimensional kernel. Any three-dimensional isotropic subspace contains that kernel: otherwise its image in the two-dimensional symplectic quotient would have dimension two. The kernels of \(\pi_+\) and \(\pi_-\) are complementary, by(E820.1). A three-dimensional subspace cannot contain both. Thus \(W\) cannot be isotropic for both forms.

After interchanging the two signs if necessary, some \(P(\pi_+)_{ij}\) with \(i,j\in\{2,3,4\}\) has a nonzero constant term. It is therefore a unit in the local Artinian ring \(A\). Equation(E820.8) makes \(C_+\) invertible: take determinants of the square matrices, or note that a product equal to a scalar unit matrix is invertible over a commutative local ring. It follows that

\[
 B_{ij}=P(\pi_+)_{ij}C_+^{-1}.
 \tag{E820.9}
\]

For the second deformation, substitute this into(E820.8). If
\(D=C_-C_+^{-1}\), then

\[
 D P(\pi_+)_{ij}=P(\pi_-)_{ij}I_m.
\]

The coefficient already chosen to be a unit shows that \(D=a I_m\) for some \(a\in A\). All the other equations now imply

\[
 P(\pi_-)=a P(\pi_+)
       \quad\text{in }\bigwedge^2 A^4.
 \tag{E820.10}
\]

## 5. The nonzero socle wedge contradicts proportionality

Let \(J=(\partial f_i/\partial z_j)\). The bracket matrix is
\(P(\pi)=J\pi J^{\mathsf t}\), reduced modulo \(I\). Exterior powers of this identity give

\[
 P(\pi_+)\wedge P(\pi_+)=0,
 \qquad
 P(\pi_+)\wedge P(\pi_-)
   =\det(J)(\pi_+\wedge\pi_-).
 \tag{E820.11}
\]

Here both sides are expressed in the ordered four-generator basis of the Koszul presentation. Since the \(u_i\) are formal parameters,

\[
 \det(J)=\ell u_1^{\ell-1}
      \det\left(\frac{\partial u_i}{\partial z_j}\right).
 \tag{E820.12}
\]

The second determinant is a unit. Its product with
\(\ell u_1^{\ell-1}\) is nonzero in \(A=\mathbf C[u_1]/(u_1^\ell)\), because the ground field has characteristic zero. By(E820.1), the mixed wedge in(E820.11) is therefore nonzero. But(E820.10) makes it \(a P(\pi_+)\wedge P(\pi_+)=0\). This contradiction proves the local statement.

The global consequence follows from the already reviewed SF-E819 argument: the two balanced cap-kernel classes have bivector components \(\pi_+,\pi_-\); invariant semiregularity would make both ordinary local characteristic obstructions vanish. The full published Buchweitz--Flenner source and the supplied finite-action compatibility remain exactly those recorded in SF-E819. No additional global deformation input is used.

## 6. Actual nonreduced balanced candidates covered by the theorem

On the explicit \(E_i^4\) with \(U,X_0,Y\) of SF-E815, put \(Z_\pm=X_0\pm Y\) and take the actual bundle

\[
 H=\mathcal O^{24}\oplus L_{X_0}^{\oplus2}
       \oplus L_{-X_0}^{\oplus2}
       \oplus L_{Z_+}\oplus L_{-Z_+}
       \oplus L_{Z_-}\oplus L_{-Z_-}.
 \tag{E820.13}
\]

Its complete character, calculated in SF-E815, is

\[
 \operatorname{ch}(H)
  =32-8(\theta_+^2+\theta_-^2)
        +2\theta_+^2\theta_-^2
  =32v_{1/2}.
 \tag{E820.14}
\]

Choose any embedded curvilinear scheme \(Z\) of length \(\ell\ge2\) at a point, and an integer \(1\le m\le32\). The restriction of \(H\) to the local Artinian scheme \(Z\) is free, so it has a quotient \(H\twoheadrightarrow Q=\mathcal O_Z^m\). Let \(K\) be the kernel and put \(T=\mathcal O_Z^m\). Local freeness of \(H\) and zero-dimensional support give

\[
 \operatorname{Ext}^1_X(K,T)
   \simeq\operatorname{Ext}^2_X(Q,T)
   \simeq\operatorname{Mat}_m(A)\otimes\bigwedge^2\mathbf C^4.
 \tag{E820.15}
\]

The last space has dimension \(6m^2\ell>0\), by the same Koszul calculation and the absence of higher cohomology for a point-supported sheaf. Every nonzero class gives an actual coherent extension

\[
 0\longrightarrow T\longrightarrow E\longrightarrow K
      \longrightarrow0.
 \tag{E820.16}
\]

Its maximal torsion is \(T\), its double dual is \(H\), and its hull-map cokernel is \(Q\). Its entire character is
\(\operatorname{ch}(E)=\operatorname{ch}(H)+\operatorname{ch}(T)-\operatorname{ch}(Q)=32v_{1/2}\).
Thus these are actual nonpure, ordinarily gluable, nonreduced balanced sheaves of zero signed local length. They are not excluded merely by the signed-length statement of SF-E819 or by its reduced corollary. SF-E820 excludes weak semiregularity for every specified coherent finite action that might exist. No simplicity, indecomposability, or such action is asserted.

The remaining local case includes defect modules not free over a common curvilinear Artinian quotient; even equal-length cyclic modules of embedding dimension at least two are not settled by this proof. Singular reflexive hulls, positive-dimensional modifications and unrelated derived objects retain their earlier open status.
