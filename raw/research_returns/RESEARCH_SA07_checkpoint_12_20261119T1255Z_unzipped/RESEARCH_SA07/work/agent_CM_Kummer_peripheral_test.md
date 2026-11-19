# An arithmetic CM Kummer test for the boundary-extension block

19 November 2026. Work only. The quantified proper-homology premise in this test is the single explicit compactification E, together with the established CM comparison on the all-CM diagram. It is not the all-compactified-cover premise in E.2.22. The field/commutator proof below specifically tests survival after adjoining every CM abelian extension.

## KP1. A specified curve, rational non-torsion point, and Belyi map

Let E/Q be y²=x³−2, with O the origin and P=(3,5). It has good reduction at5 and7, with #E(F5)=6 and #E(F7)=7, by direct counting. For a good prime p, the prime-to-p rational torsion injects into reduction: in the formal parameter the series [n](z)=nz+terms of higher degree has valuation v_p(z) when n is a p-adic unit, so has no nonzero zero in the reduction kernel. Applying this at5 and7 excludes every primary torsion subgroup. Thus E(Q)_tors=0 and P is non-torsion.

The geometric endomorphism ring is Z[zeta3]; its Q-defined subring is Z, since actual complex conjugation interchanges zeta3 and its inverse. Put K=Q(sqrt−3). At5 the algebra K⊗Q5 is the unramified quadratic field Q25.

Define

\[
 b=\frac{2}{x^3},\qquad
 h(t)=\frac{27^{27}}{4\cdot25^{25}}t^2(1-t)^{25},
 \qquad\lambda=h\circ b:E\longrightarrow\mathbf P^1.
 \tag{KP.1}
\]

The map b has degree6 and branch values0,1,infinity: its inertia orders above these are6,2,3. The polynomial h has degree27, with derivative

\[
 h'(t)=\frac{27^{27}}{4\cdot25^{25}}t(1-t)^{24}(2-27t).
\]

The only finite critical values are0 and1, because h(0)=h(1)=0 and h(2/27)=1. Thus lambda is an explicit degree162 Belyi map. Its reduced branch-preimage divisor D contains O and P, since b(O)=0 and b(P)=2/27. Let U=E\D and U0=E\{O,P}. The filling map U→U0 induces an integral surjection H1(U,Z)→H1(U0,Z), with the corresponding actual completed and Galois-equivariant maps. Both compactify to E.

## KP2. The exact Kummer openness source

Opened original Lombardo--Tronto, *Explicit Kummer Theory for Elliptic Curves*, arXiv1909.05376v1,11September2019, https://arxiv.org/pdf/1909.05376. Theorem1.1 p2 assumes End_K(E)=Z for endomorphisms over the base field K. This was visually checked on the original page, so the barred geometric-field convention is not being confused with it. The preceding paragraph explicitly notes that this hypothesis always holds for an elliptic curve over Q. Thus it applies to the present E/Q despite geometric CM.

For the fixed non-torsion P, the theorem gives C such that

\[
 \frac{N^2}{[\mathbb Q(E[M],N^{-1}P):\mathbb Q(E[M])]}\mid C
 \qquad(N\mid M). \tag{KP.2}
\]

Its Section2.3, pp5--6, defines the exact Kummer and arboreal representations. Passing first to arbitrarily high M=5^m and then N=5^n proves that the translation kernel

\[
 \operatorname{Gal}\bigl(\mathbb Q(E[5^\infty],5^{-\infty}P)
                   /\mathbb Q(E[5^\infty])\bigr)
       \hookrightarrow T_5E
\]

has finite index. Indeed, at each N its finite image has index dividing C by (KP.2); the decreasing finite images stabilize and the resulting closed Z5-submodule has uniformly bounded index at every5^n quotient. This is openness in the actual Tate module, in its actual Betti-comparison coordinates.

After restriction to the finite CM field K the translation image remains open. The actual torsion image over K is open in (O_K⊗Z5)^× by CM reciprocity; the representation is the multiplication action on the rank-one O_K⊗Z5 Tate module. The CM main theorem used earlier in E.2.6/21 also places K(E[5^infty]) inside K^ab, hence inside F_CM.

Choose compatible5-division points of P along one real analytic path from O to P. Their coordinates are algebraic and real: they solve the division equations over Q and lie on the real group under this chosen division. Actual complex conjugation c therefore has translation component zero in the arboreal representation

\[
 r_5:\Gamma_{\mathbb Q}\longrightarrow T_5E\rtimes
                       \operatorname{Aut}(T_5E).
 \tag{KP.3}
\]

On V=T5E⊗Q5, its linear part C has C²=1, trace0 and determinant−1, and conjugates a CM scalar t to its field conjugate bar(t). The open torsion and translation statements above are sufficient for the argument below; no claimed adelic independence is used.

## KP3. Survival over the compositum of all CM abelian extensions

Let Q_CM and F_CM be exactly the fields of E.2.6/21. Actual complex conjugation is central on the Galois extension Q_CM/Q. Hence every commutator [c,g] lies in Gamma_QCM. Also F_CM/Q_CM is abelian: it is a compositum of the abelian extensions K'^ab Q_CM/Q_CM for CM fields K'. Therefore

\[
 \overline{[\Gamma_{\mathbb Q_{\rm CM}},
             \Gamma_{\mathbb Q_{\rm CM}}]}
       \subset\Gamma_{F_{\rm CM}}. \tag{KP.4}
\]

Let W be an open translation lattice in r5(Gamma_K). For each v∈W choose an actual preimage with arboreal image(v,1). Its commutator with c has image((C−1)v,1), so r5(Gamma_QCM) contains the lattice (C−1)W in the negative C-eigenspace. Gamma_QCM is normal in Gamma_Q. Conjugation by any actual element with CM scalar linear part t therefore puts t(C−1)W in the same image. The scalar image is open in the quadratic field's units, so it contains a t outside Q5. The two one-dimensional Q5-spaces (C−1)V and t(C−1)V are independent. Their integral lattices generate an open subgroup W' of V. It follows that

\[
 W'\subset r_5(\Gamma_{\mathbb Q_{\rm CM}})\cap V.
 \tag{KP.5}
\]

For an element with scalar linear part t, the commutator with c has linear part bar(t)/t. The open scalar image contains t with bar(t)/t≠1. Thus there is h∈Gamma_QCM with nontrivial norm-one scalar linear part q. Its possible translation component does not affect its conjugation action on pure translations. For v∈W',

\[
 r_5([h,v])=((q-1)v,1).
\]

Since Q25 is a field and q≠1, multiplication by q−1 is invertible over Q5. Therefore (q−1)W' is another open translation lattice. Compactness ensures all images of the closed Galois subgroups are closed, and (KP.4) gives

\[
 r_5(\Gamma_{F_{\rm CM}})\supset(q-1)W'. \tag{KP.6}
\]

At the same time every element of Gamma_FCM fixes E[5^infty], so the entire image of this subgroup consists of translations. Consequently its Kummer image is open in T5E. This proves directly that adjoining all CM torsion and all CM abelian extensions does not kill this Kummer image. It does not apply the fixed-number-field openness theorem naively after an infinite base extension; the actual commutators provide the required surviving image.

## KP4. Actual relative paths, finite coefficients and the dual integral lattice

Put D0={O,P}, U0=E\D0, and fix the actual complex embedding. The integral relative homology sequence is

\[
 0\longrightarrow\Lambda:=H_1(E(\mathbb C),\mathbb Z)
 \longrightarrow M_B:=H_1(E(\mathbb C),D_0,\mathbb Z)
 \xrightarrow{\partial}\mathbb Z(P-O)\longrightarrow0. \tag{KP.7}
\]

All groups are free. A real path p from O to P gives the lift [p] of P-O. For n=5^r, finite-coefficient comparison identifies the dual of M_B/n with H^1_et(Ebar,D0;Z/n)=H^1_c,et(U0bar,Z/n). This is the actual relative comparison: use the short exact sequence 0→j!Z/n→Z/n→i*Z/n→0 on E, and the natural comparison on E and D0. Thus no arbitrary isomorphism of extensions is chosen.

Here is the path description of the same finite module and its Galois action. A relative H^1 class is a finite Z/n-torsor on E together with trivializations at O and P, modulo simultaneous translation. Transport along an étale path from O to P, followed by comparison of the two trivializations, evaluates that class in Z/n. It gives a functional in Hom(H^1_et(Ebar,D0;Z/n),Z/n) that maps to 1 under the dual relative boundary map. The difference of two such functionals is evaluation on their abelianized loop in π1(Ebar,O)/n. This is the ordinary chain/torsor definition of the relative-homology class, and it is natural under Galois action because O and P are rational.

The multiplication cover [n]:E→E has deck group E[n]. It is the universal abelian exponent-n cover: analytically it corresponds to nΛ⊂Λ, and finite étale comparison carries that statement to Ebar. Lift p through [n] with initial point O. Its endpoint Q_r satisfies nQ_r=P and is the previously chosen real division point. Applying sigma to the transported endpoint therefore gives exactly

\[
  (\sigma[p]-[p])\bmod n
       =\sigma Q_r-Q_r\in E[n]=\Lambda/n\Lambda. \tag{KP.8}
\]

The convention in (KP.8) fixes the possible sign of the path-difference cocycle. Taking the compatible inverse limit identifies M_B⊗Z5, with its actual arithmetic action, with the Kummer extension 0→T5E→M5→Z5→0. In the basis consisting of an integral basis of Λ followed by [p], its matrix is

\[
 R_\sigma=\begin{pmatrix}\rho_{E,5}(\sigma)&\kappa_5(\sigma)\\0&1\end{pmatrix}. \tag{KP.9}
\]

For completeness, the dual map uses cohomology with compact support, not an inferred equality of two types of realizations. For every n the cup product and trace give the canonical perfect pairing

\[
 H^1_{c,\mathrm{et}}(\bar U_0,\mathbb Z/n)
   \times H^1_{\mathrm{et}}(\bar U_0,\mathbb Z/n(1))
       \longrightarrow\mathbb Z/n.
\]

This is Milne LEC v2.21, Theorem14.7 p93; its trace/localization maps are in Proposition14.5 p92, and the exact orientation comparison is Section24 p144/Theorem24.1 p144. The theorem and these maps were opened in the complete author PDF at https://www.jmilne.org/math/CourseNotes/LEC.pdf. Dualizing gives the actual Galois-equivariant perfect homology pairing

\[
 M_5\times H_{1,\mathrm{et}}(\bar U_0,\mathbb Z_5)
      \longrightarrow\mathbb Z_5(1),\qquad
 H_{1,\mathrm{et}}(\bar U_0,\mathbb Z_5)
       =\operatorname{Hom}(M_5,\mathbb Z_5(1)). \tag{KP.10}
\]

Under finite-coefficient Betti comparison it is the intersection pairing between relative and punctured integral cycles. It is unimodular over Z: it also follows directly by taking a compact oriented surface with two small disks removed and applying relative cellular duality. In particular an integral basis of M_B has an actual integral dual basis of H1(U0(C),Z). Passing to Z5 preserves the pairing. Therefore the punctured-homology matrix in these fixed bases is χ5(sigma)R_sigma^{-t}.

Every sigma∈Gamma_FCM has χ5(sigma)=1 and rho_E,5(sigma)=1. Thus the punctured-homology matrix is literally

\[
 \begin{pmatrix}I_2&0\\-\kappa_5(\sigma)^t&1\end{pmatrix}. \tag{KP.11}
\]

## KP5. An actual arithmetic one-cover obstruction

Choose any integral basis e1,e2 of Λ, and let m be the least nonnegative integer with 5^m(T5E) contained in the Kummer image of Gamma_FCM. It exists by KP3. Define a=Σ_{j≥1}5^{j!}∈Z5. Its digits are eventually neither all zero nor all four, so 5^m a is not an integer. By KP3 there is an actual sigma∈Gamma_FCM with kappa5(sigma)=5^m a e1. If a single fully specified element is desired, fix an enumeration of finite Galois subextensions of Qbar/Q and an order on each finite Galois group; inside the nonempty compact inverse image of this prescribed Kummer value, choose successively the first extendible finite Galois restriction. The compatible restrictions define one sigma. No computability assertion is made.

Equation(KP.11) now has a noninteger entry in an actual integral Betti basis. Hence sigma does not preserve H1(U0(C),Z) inside its 5-adic completion. On H1(E(C),Z) it acts as the identity after every finite completion: all torsion of the CM elliptic curve over K lies in K^ab⊂F_CM. The inclusion U→U0 induces an actual integral surjection on H1, commuting with the completed arithmetic action. Were sigma integral on H1(U(C),Z), its quotient action on H1(U0(C),Z) would be integral; this contradicts (KP.11). Thus the explicit finite étale Belyi cover U of P1−{0,1,infinity} supplies an actual arithmetic element that is nonintegral on its affine homology and is the identity on its proper homology.

All peripheral conditions here are the actual arithmetic ones. Since chi(sigma)=1, sigma sends every geometric inertia generator to a conjugate of the inertia generator at the sigma-conjugate boundary point. The divisor D and the Belyi map are Q-defined, so this is a peripheral-preserving action on the actual cover tower, not merely a quotient-extension automorphism. This proves the stated one-cover assertion. It does not establish proper integral action on every other compactified cover required by E.2.22; that quantified premise remains unproved for this sigma. It therefore does not close the proper-to-affine question with the all-cover premise, nor the main integral-motive gate.

## Audit status

KP1's elementary counts/Belyi derivative are to be retained as a finite certificate. KP2's exact theorem hypothesis was visually read in the primary PDF; its Kummer map is read at pp5--6. The elliptic agent independently passed KP2--3 and saved work/elliptic_audit_cm_kummer_survival.md, including an original p2 image. KP4's exact relative-path evaluation, finite-coefficient comparison, cup-product/trace duality and inverse-dual matrix have now been written explicitly; independent audit is requested. No production integration or main-gate movement is claimed.
