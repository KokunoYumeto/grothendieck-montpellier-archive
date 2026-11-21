# SF-E819: a local commutator obstruction to signed point modifications

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

**Status:** New complete proof awaiting independent whole-proof review. The first-order module argument, lifting of the hull map, and finite perfect-complex trace are written explicitly. No all-order quantization theorem, singular Hermitian--Einstein theorem, or formality assertion is used.

## 1. Statement and new scope

Let \(X\) be a complex abelian fourfold with genuine real multiplication of type \((2,2)\), compatible polarization \(\theta=\theta_++\theta_-\), and

\[
 v_q=(1-q\theta_+^2/2)(1-q\theta_-^2/2),\qquad q>0.
\]

Let \(E\) be a coherent sheaf, with locally free double dual \(H=E^{\vee\vee}\), such that the kernel \(T\) and cokernel \(Q\) of its canonical map to \(H\) have finite support:

\[
 0\longrightarrow T\longrightarrow E\longrightarrow H
       \longrightarrow Q\longrightarrow0.
 \tag{E819.1}
\]

Suppose that \(e^B\operatorname{ch}(E)=r v_q\), where \(r>0\) and \(B\) is a rational algebraic divisor. If \(E\) is weakly \(G\)-semiregular for any specified effective coherent finite translation/tensor action, then at every point \(p\)

\[
 \operatorname{length}Q_p=\operatorname{length}T_p.
 \tag{E819.2}
\]

In particular, a nonzero signed point defect at even one point prevents weak semiregularity. The theorem allows actual zero-dimensional torsion in \(E\), which SF-E817 excludes from its hypotheses. It does not settle modifications with equal lengths at every point, nor singular reflexive hulls or positive-dimensional defects.

The ordinary Hochschild trace/evaluation identity used here is the published Buchweitz--Flenner theorem: *The global decomposition theorem for Hochschild (co-)homology of singular spaces via the Atiyah--Chern character*, Advances in Mathematics217(2008),243--281, DOI10.1016/j.aim.2007.06.013, Theorem6.4.2. Exact author-copy locators are Proposition6.2.1, pp29--30; Proposition6.3.1 and Corollary6.3.2, pp30--31; Theorem6.4.2 and its proof through Proposition6.4.4, pp31--33, in arXiv:math/0606730. These identify semiregularity after Hochschild evaluation with contraction by the full Chern character. Only compatibility with the specified coherent finite action is taken from supplied DEG_L S-21: equation(S21.6), the paragraph following(S21.7), and the invariant-evaluation paragraph preceding(S21.8). Those are retained as supplied proved inputs. The obstruction tested is ordinary degree-two Ext; injectivity on the specified invariant Ext suffices because Hochschild evaluation takes values in those invariants. No Serre-adjunction identity is needed here.

## 2. A local first-order lemma

Let \(R=\mathbf C[[z_1,z_2,z_3,z_4]]\), let \(M\) be a finite \(R\)-module, and suppose there is an \(R\)-linear map

\[
 \phi:M\longrightarrow R^r
\]

with finite-length kernel \(T\) and cokernel \(Q\). Let \(\pi\) be a nonzero constant bivector in these coordinates. Put \(D=\mathbf C[\varepsilon]/(\varepsilon^2)\), and endow \(A=R\oplus\varepsilon R\) with the associative first-order product

\[
 f*g=fg+\frac{\varepsilon}{2}\pi(df,dg).
 \tag{E819.3}
\]

Associativity modulo \(\varepsilon^2\) follows from the Leibniz rule for the biderivation; no higher-order Poisson quantization is required. The elements \(z_i\) satisfy

\[
 [z_i,z_j]_* =\varepsilon\pi_{ij}.
 \tag{E819.4}
\]

**Local lemma.** If \(M\) has a \(D\)-flat first-order deformation to a finite left \(A\)-module, then \(\operatorname{length}Q=\operatorname{length}T\).

### 2.1. The map to the free hull lifts

Write \(K=\operatorname{im}\phi\). The two exact sequences are

\[
 0\to T\to M\to K\to0,
 \qquad 0\to K\to R^r\to Q\to0.
 \tag{E819.5}
\]

The four-variable Koszul complex and a finite-length filtration give
\(\operatorname{Ext}^j_R(T,R)=\operatorname{Ext}^j_R(Q,R)=0\) for \(j<4\). Applying \(\operatorname{Hom}_R(-,R^r)\) to (E819.5) consequently gives

\[
 \operatorname{Ext}^1_R(M,R^r)=0.
 \tag{E819.6}
\]

Let \(M_\varepsilon\) be a flat deformation as in the lemma, and give \(H_\varepsilon=A^r\) its free left-module structure. The map \(\phi\) lifts to an \(A\)-linear map

\[
 \phi_\varepsilon:M_\varepsilon\longrightarrow H_\varepsilon.
 \tag{E819.7}
\]

Here is a direct obstruction calculation. Choose a finite free resolution of \(M\) over the regular local ring \(R\). One can lift it to a free resolution of \(M_\varepsilon\) with the same finite ranks: lift generators successively; the kernels remain \(D\)-flat, because both the free source and its flat quotient are \(D\)-flat. Reduction modulo \(\varepsilon\) gives the chosen successive kernels. At the last step a kernel with zero reduction is zero by the nilpotent version of Nakayama's lemma. Apply \(\operatorname{Hom}_A(-,H_\varepsilon)\). The reduction map of these Hom complexes is surjective termwise, with kernel its \(\varepsilon\)-multiple, naturally the corresponding Hom complex over \(R\). The obstruction to lifting the degree-zero cocycle \(\phi\) lies in \(\operatorname{Ext}^1_R(M,R^r)\), which is zero by (E819.6). Correcting a lifted cocycle therefore gives (E819.7).

### 2.2. The defect cone is perfect over the dual numbers

Consider the two-term complex, in degrees \(-1,0\),

\[
 C_\varepsilon=[M_\varepsilon\xrightarrow{\phi_\varepsilon}H_\varepsilon].
 \tag{E819.8}
\]

It is a complex of left \(A\)-modules and a complex of flat \(D\)-modules. Its reduction is \(C_0=[M\to R^r]\), with cohomology \(T\) in degree \(-1\) and \(Q\) in degree zero. The short exact sequence of complexes

\[
 0\longrightarrow C_0\xrightarrow{\varepsilon} C_\varepsilon
      \longrightarrow C_0\longrightarrow0
\]

shows that every cohomology group of \(C_\varepsilon\) is finite-dimensional over \(\mathbf C\). As a complex over the Noetherian Artinian ring \(D\), it therefore has bounded finite cohomology and is pseudo-coherent. Its two flat terms give finite Tor amplitude. Thus it is a perfect \(D\)-complex. The exact general criterion is Stacks Project, Lemma15.76.2, tag `0658`; its proof truncates a finite free resolution using the finite Tor amplitude. In this Noetherian case the required bounded-above finite free resolution is obtained by choosing generators of cohomology and successive finite kernels.

Choose a bounded finite free \(D\)-complex \(P^\bullet\) representing \(C_\varepsilon\). Its Euler rank satisfies

\[
 \sum_j(-1)^j\operatorname{rk}_D P^j
  =\chi(C_0)=\operatorname{length}Q-\operatorname{length}T.
 \tag{E819.9}
\]

### 2.3. The commutator trace

Left multiplication by each \(z_i\) is a \(D\)-linear chain endomorphism of (E819.8), since \(\phi_\varepsilon\) is \(A\)-linear. Their commutator is \(\varepsilon\pi_{ij}\) times the identity. Transfer these endomorphisms to \(P^\bullet\) in the derived category. They can be represented by chain maps, and the commutator equality holds up to chain homotopy.

For a chain endomorphism \(f\) of a bounded finite free complex over a commutative ring, define its supertrace to be \(\sum_j(-1)^j\operatorname{Tr}(f^j)\). A degree-zero commutator has zero supertrace by cyclicity of ordinary matrix trace. A null-homotopic map has zero supertrace because the contributions of \(dh\) and \(hd\) cancel after shifting the index. Therefore (E819.4) gives

\[
 0=\varepsilon\pi_{ij}
       \bigl(\operatorname{length}Q-\operatorname{length}T\bigr)
       \quad\text{in }D.
 \tag{E819.10}
\]

At least one \(\pi_{ij}\) is nonzero. Since \(\varepsilon\ne0\) in \(D\), the integer in parentheses must be zero. This proves the local lemma. It is essential that the trace is taken on the finite perfect defect complex; no trace of an infinite-dimensional free \(R\)-module is used.

## 3. Vanishing of Hochschild evaluation gives the local deformation

We recall the elementary first-order identification to fix precisely what is used. For a \(\mathbf C\)-algebra \(R\), a square-zero multiplication deformation \(\mu+\varepsilon\mu_1\), and an \(R\)-module \(M\) with action \(\rho\), an action on \(M\oplus\varepsilon M\) has the form \(\rho+\varepsilon\rho_1\). The associativity equation is

\[
 \rho(a)\rho_1(b)-\rho_1(ab)+\rho_1(a)\rho(b)
       =\rho\bigl(\mu_1(a,b)\bigr).
 \tag{E819.11}
\]

The left side is the bar differential. The right side is the degree-two cocycle obtained by applying the Hochschild characteristic morphism to \(\mu_1\). The bar resolution \(R\otimes_{\mathbf C}R^{\otimes n}\otimes_{\mathbf C}M\) identifies this cohomology group with \(\operatorname{Ext}^2_R(M,M)\). Consequently the obstruction vanishes exactly when (E819.11) has a solution, giving a flat first-order module deformation. A normalized solution has \(\rho_1(1)=0\); this can equally be imposed by the normalized bar resolution. Nilpotent Nakayama shows that the resulting module is finite over the deformed algebra when \(M\) is finite.

For the completed local ring in §2 one can use a finite free resolution in place of the bar resolution. Lift its matrices to the product (E819.3). Their squared differential is \(\varepsilon\) times an endomorphism cocycle of degree two. Changing the lifted differential by \(\varepsilon h\) changes this cocycle by \(dh+hd\). Its class is exactly the characteristic class just described, as comparison with the bar resolution shows. Thus a zero class gives a finite free deformed complex. It is flat over \(D\), and reduction has cohomology only in degree zero. The elementary square-zero cohomology sequence then gives a flat degree-zero module and no other cohomology. This formulation keeps all maps continuous for formal power series; it does not assume that an arbitrary discontinuous action on power series is acceptable.

Restriction of the global characteristic morphism to a small affine neighborhood and then to its completed local ring is compatible with this description. In the HKR decomposition

\[
 HH^2(X)=H^2(\mathcal O_X)\oplus H^1(T_X)
                \oplus H^0(\bigwedge^2T_X),
 \tag{E819.12}
\]

the first two components restrict to zero on the affine/formal local scheme. A global class with bivector component \(\pi\) therefore restricts to the multiplication obstruction of (E819.3), up to a fixed nonzero normalization of the HKR map. That normalization does not affect either vanishing or the trace contradiction.

## 4. The balanced cap kernel supplies a nonzero bivector

For each real-multiplication plane, choose a nonzero invariant holomorphic bivector \(\pi_\pm\). Nondegeneracy of \(\theta_\pm\) defines a nonzero element \(\eta_\pm\in H^2(\mathcal O_X)\), supported on that plane, by

\[
 \pi_\pm\mathbin{\lrcorner}(\theta_\pm^2/2)=\eta_\pm.
\]

Wedge by \(\eta_\pm\) kills the degree-four term of its own two-dimensional plane. Hence on the factor \(1-q\theta_\pm^2/2\), contraction by \(\pi_\pm\) gives \(-q\eta_\pm\), while wedge by \(q\eta_\pm\) gives \(q\eta_\pm\). Their sum is zero. Acting on the other factor does not change this cancellation, so

\[
 \xi_\pm=\pi_\pm+q\eta_\pm
       \in\ker c^2_{v_q}.
 \tag{E819.13}
\]

For \(\operatorname{ch}(E)=r e^{-B}v_q\), conjugate this class by the usual divisor shear. The identity
\(e^{-B}\iota_v e^B=\iota_v+(\iota_vB)\wedge\)
shows directly that the shear adds mixed and wedge terms but leaves the projection to \(\bigwedge^2H^0(T_X)\) unchanged. We obtain a class \(\xi\in\ker c^2_{\operatorname{ch}(E)}\) whose holomorphic bivector component is the nonzero constant bivector \(\pi_+\). One could also take both plane components to obtain a nondegenerate bivector, but only nonzero is needed.

Suppose that \(\sigma^2_{E,G}\) were injective. Hochschild evaluation lands in invariant Ext by the stated S-21 compatibility. Buchweitz--Flenner Theorem6.4.2, together with Proposition6.2.1, gives the ordinary composition identity; restricting it to these invariant values gives \(\sigma^2_{E,G}\rho^2_{E,G}=c^2_{\operatorname{ch}(E)}\), with the consistent HKR convention just fixed. Therefore \(\rho^2_{E,G}(\xi)=0\). Its image in ordinary Ext is zero, and so is its restriction at every point. By §3, the completed local module of \(E\) admits the flat first-order deformation (E819.3).

Complete (E819.1) at any point. In characteristic zero the formal logarithm of the abelian formal group gives simultaneous formal coordinates in which all invariant vector fields, and hence both bivectors \(\pi_\pm\), are constant. Its hull is free, and its kernel and cokernel have the same lengths as before completion. The local lemma gives (E819.2). This proves SF-E819 for every specified effective coherent finite action, without any simplicity assumption.

## 4a. Reduced defects cannot survive even with equal lengths

There is a stronger conclusion when, at a point of the modification, both finite modules are killed by the maximal ideal. Suppose locally

\[
 Q\simeq k^m,\qquad T\simeq k^n,\qquad k=R/\mathfrak m.
 \tag{E819R.1}
\]

If either module is nonzero, a balanced weakly semiregular sheaf cannot have this local model. This is stronger than the signed-length conclusion when \(m=n>0\).

Choose a basis of the free hull so that its quotient to \(Q\) is the residue map on the first \(m\) coordinates. Then

\[
 K=\mathfrak m\otimes\mathbf C^m\oplus R^{r-m}.
 \tag{E819R.2}
\]

The extension of its free summand by \(T\) splits, since \(\operatorname{Ext}^1_R(R,T)=0\). For the remaining summand choose lifts \(e_i(v)\in M\), linear in \(v\in\mathbf C^m\), of \(z_i v\in K\). The Koszul presentation of \(\mathfrak m\) shows that the extension is encoded by matrices

\[
 B_{ij}:\mathbf C^m\longrightarrow\mathbf C^n,\qquad
 B_{ij}=-B_{ji},
\]

in the relations

\[
 z_i e_j(v)-z_j e_i(v)=B_{ij}v\in T,
 \qquad z_i T=0.
 \tag{E819R.3}
\]

Indeed the first Koszul syzygies generate all relations among the \(z_i\), and all next syzygies among (E819R.3) are automatically respected because \(\mathfrak m T=0\). Equivalently these six matrices are precisely the class in
\(\operatorname{Ext}^1_R(K,T)=\operatorname{Hom}(\mathbf C^m,\mathbf C^n)\otimes\bigwedge^2\mathbf C^4\).

Assume a flat first-order deformation for a nonzero constant bivector \(\pi\). Lift the map to the free hull as in §2.1. Lift each basis vector of \(T\) to \(M_\varepsilon\). Its image under \(\phi_\varepsilon\) reduces to zero, and hence has the form \(\varepsilon\) times a vector in the free hull. Reducing that vector at the origin and projecting to the first \(m\) coordinates defines a matrix

\[
 C:\mathbf C^n\longrightarrow\mathbf C^m.
\]

Lift the generators \(e_i(v)\) as well. Their images have the form \(z_i v+\varepsilon a_i(v)\). The lift of the left side of (E819R.3), minus the lifted right side, is \(\varepsilon\) times an element of \(M_\varepsilon\), because its reduction is zero. Apply \(\phi_\varepsilon\), project to the first \(m\) coordinates, and reduce the coefficient of \(\varepsilon\) at the origin. Terms \(z_i a_j-z_j a_i\) vanish there. The projected value of the correction term is zero because \(\phi(M)=K\) maps to zero in \(Q\). The commutator (E819.4) therefore gives the exact matrix equations

\[
 C B_{ij}=\pi_{ij} I_m\quad\text{for every }i,j.
 \tag{E819R.4}
\]

The local trace lemma has already forced \(m=n\). If \(m=0\), the modification is trivial. Otherwise some \(\pi_{ij}\ne0\), and (E819R.4) makes \(C\) invertible. Consequently

\[
 B_{ij}=\pi_{ij}C^{-1}\quad\text{for every }i,j.
 \tag{E819R.5}
\]

Thus the tensor of the six extension matrices lies in the one-dimensional bivector line \(\mathbf C\pi\), tensored with one fixed invertible matrix.

Balanced weak semiregularity requires local deformations for both independent bivectors \(\pi_+\) and \(\pi_-\) of §4. The same fixed extension matrices would satisfy (E819R.5) for each. This is impossible. Explicitly, choose a linear functional on \(\bigwedge^2\mathbf C^4\) that vanishes on \(\pi_+\) and not on \(\pi_-\). Applying it to (E819R.4) for the second deformation gives zero on the left and a nonzero scalar identity on the right. This proves the stronger reduced-defect obstruction.

This proof does not require the two first-order deformations to fit together into a deformation over a two-dimensional base: separate vanishing of the two obstruction classes already contradicts the fixed matrices. For nonreduced finite modules the simple matrix presentation (E819R.3) is unavailable; equal signed length there remains an open case in this argument.

## 5. An actual nonpure balanced family that this obstruction excludes

Use the explicit CM fourfold \(X=E_i^4\), genuine RM matrix \(U\), and integral divisor classes \(X_0,Y\) from SF-E815:

\[
 U=\operatorname{diag}(A,A),\quad
 A=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
 S=\operatorname{diag}(1,1,-1,-1),\quad
 X_0=\theta_S,\quad Y=\theta_{US}.
\]

Write \(X_0=x+y\), \(Y=\sqrt2(x-y)\), with
\(x^2=-\theta_+^2\), \(y^2=-\theta_-^2\), and
\(\int_Xx^2y^2=4\). The following degree-four isogeny makes a rational half-divisor into an actual integral divisor. Let

\[
 T_0=\begin{pmatrix}1&0\\1&1+i\end{pmatrix},\qquad
 T=\operatorname{diag}(T_0,T_0),\qquad f=[T]:X\to X.
\]

Then \(\deg f=4\), and direct matrix multiplication gives

\[
 T^*(US)T=\operatorname{diag}(2,-2,-2,2).
 \tag{E819.14}
\]

Thus \(f^*(Y/2)\) is the integral class
\(D_0=\theta_{\operatorname{diag}(1,-1,-1,1)}\).
Choose actual line bundles \(L_{\pm D_0}\) and set

\[
 Q_\pm=f_*L_{\pm D_0}.
\]

These are locally free rank-four sheaves, since \(f\) is finite étale. The finite étale Grothendieck--Riemann--Roch formula and \(\operatorname{td}(T_X)=1\) give the entire characters

\[
 \operatorname{ch}(Q_\pm)=4e^{\pm Y/2}.
 \tag{E819.15}
\]

Indeed \(f^*(\pm Y/2)=\pm D_0\), and \(f_*f^*\) multiplies rational cohomology by four. This invokes the already checked Fulton Corollary18.3.1(c), printed p.354, or equivalently the finite étale specialization of GRR; no Fourier--Mukai transform is needed for the construction.

Form the actual vector bundle

\[
 H=(L_{X_0}\oplus L_{-X_0})^{\oplus6}
            \oplus(Q_+\oplus Q_-)^{\oplus3}.
 \tag{E819.16}
\]

Its rank is thirty-six, its odd character components vanish, and its entire even character is

\[
 \begin{aligned}
 \operatorname{ch}_2(H)&=6X_0^2+3Y^2=12(x^2+y^2),\\
 \operatorname{ch}_4(H)&=\tfrac12 X_0^4+\tfrac1{16}Y^4
                         =\tfrac92 x^2y^2.
 \end{aligned}
 \tag{E819.17}
\]

Choose a point \(p\), and use the full fibre quotient
\(H\twoheadrightarrow k_p^{36}\). Let \(K\) be its kernel. The exact sequence and local freeness of \(H\) give

\[
 \operatorname{Ext}^1_X(K,k_p^{34})
     \simeq\operatorname{Ext}^2_X(k_p^{36},k_p^{34})
     \simeq\operatorname{Hom}(\mathbf C^{36},\mathbf C^{34})
                   \otimes\bigwedge^2T_pX.
 \tag{E819.18}
\]

The first isomorphism follows because \(\operatorname{Ext}^{>0}_X(H,k_p^{34})=0\). The second is the point Koszul complex. In particular this is a nonzero space of actual extension classes. For any nonzero class form the actual coherent extension

\[
 0\longrightarrow k_p^{34}\longrightarrow E\longrightarrow K
          \longrightarrow0.
 \tag{E819.19}
\]

The maximal torsion subsheaf of \(E\) is precisely the displayed point sheaf, because \(K\) is torsion-free. The double dual is \(H\), and the canonical map has kernel \(k_p^{34}\) and cokernel \(k_p^{36}\). Thus its signed local length is two. Since \([p]=x^2y^2/4\), its full character is

\[
 \begin{split}
 \operatorname{ch}(E)
  &=\operatorname{ch}(H)-2[p]
    =36+12(x^2+y^2)+4x^2y^2\\
  &=36(1-\theta_+^2/3)(1-\theta_-^2/3)
    =36v_{2/3}.
 \end{split}
 \tag{E819.20}
\]

Every such \(E\) is perfect on the smooth fourfold and ordinarily gluable because it is a coherent sheaf. This is an actual balanced construction with point torsion and point defect; neither is merely a virtual class. No indecomposability, simplicity, or finite action is asserted. For every finite coherent action that might exist, however, SF-E819 excludes weak semiregularity because \(36-34=2\ne0\).

## 6. Relation to the overlapping three-cohomology attempt

The signed primitive-divisor class that motivated the construction is

\[
 6(e^{X_0}+e^{-X_0})+3(e^Y+e^{-Y})-2
        =16v_{3/2}.
 \tag{E819.21}
\]

It has five distinct normalized divisor classes and a negative aggregate coefficient at the zero class. Thus the positive-weight hypothesis of SF-E815 does not apply. A three-cohomology model can put the four nonzero classes in degree zero, \(\mathcal O^{36}\) in degree \(-1\), and \(\mathcal O^{34}\) in degree \(-2\); the repeated zero class also defeats the globally disjoint-class hypothesis of SF-E816b. The Fourier--Mukai interpretation suggested this model, but equations (E819.14)--(E819.20) construct its nonpure coherent counterpart directly, so no claim about an undeclared inverse-equivalence deformation is needed for the theorem or its example.

Among nontrivial point modifications with locally free hull, the new local tests leave open only zero signed length at every point, with at least one nonreduced defect module at each point where the modification is nonzero. They do not assert that such modifications are semiregular. A locally free sheaf itself, with \(T=Q=0\), is not excluded by SF-E819; its earlier exclusions require the separate SF-E811--E813 hypotheses. The other outstanding possibilities include singular reflexive hulls, positive-dimensional torsion or defects, twisted objects outside this local ordinary-module argument, and derived complexes not equivalent to the coherent models just analyzed.
