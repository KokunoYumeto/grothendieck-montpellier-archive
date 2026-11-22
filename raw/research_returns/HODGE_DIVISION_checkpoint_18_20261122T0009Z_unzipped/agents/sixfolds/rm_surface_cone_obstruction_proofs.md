# SF-E821: local coisotropy excludes ample surface summands in balanced cones

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

**Status:** Independently whole-reviewed by /root and /root/imprimitive on 21 November 2026; mathematical reviews PASS, with fresh peer primary-source checks and independent full exterior verification for E821. Reviewers: GPT-6 Astra Pro, inherited effort not exposed. Reviewed draft SHA-256: `770138f789de62ebf83087d3f3e5322243727e854e8d458a63003cb19835d749`. This is a local support criterion, followed by a specific excluded family. No claim is made for arbitrary extensions whose surface part is not a local direct summand.

## 1. The support criterion

Let \(X\) be a complex abelian fourfold with genuine real multiplication of type \((2,2)\), holomorphic tangent decomposition \(V=V_+\oplus V_-\), and compatible polarization \(\theta=\theta_++\theta_-\). Put

\[
 v_q=(1-q\theta_+^2/2)(1-q\theta_-^2/2),\qquad q>0.
\]

Let \(E\) be a perfect complex with
\(e^B\operatorname{ch}(E)=r v_q\), where \(r>0\) and \(B\) is an algebraic rational divisor. Suppose that, near a general smooth point of a reduced irreducible surface \(S\subset X\), the complex \(E\) has a direct summand \(i_*F[a]\). Here \(i:S\hookrightarrow X\), \(F\) is a nonzero locally free sheaf on that smooth part of \(S\), and \(a\) is any integer. Other local summands may be arbitrary perfect complexes.

If \(E\) is weakly semiregular for a specified effective coherent finite translation/tensor action, then the conormal plane of \(S\) is isotropic for both bivectors
\(\pi_+\in\bigwedge^2V_+\) and
\(\pi_-\in\bigwedge^2V_-\). Equivalently, at a general smooth point,

\[
 T_pS=\ell_+(p)\oplus\ell_-(p),
 \qquad \ell_\pm(p)\subset V_\pm
 \text{ are complex lines}.
 \tag{E821.1}
\]

Consequently

\[
 \int_S\theta_+^2=\int_S\theta_-^2=0.
 \tag{E821.2}
\]

In particular, such a local summand is impossible on an effective surface cycle of class \(k^2\theta^2\), for \(k>0\). More generally it is impossible whenever either pairing in(E821.2) is positive.

This statement does not exclude every surface. In particular, a real-multiplication abelian surface with tangent type \((1,1)\) has exactly the mixed tangent plane(E821.1). Such surfaces actually occur in the explicit \(E_i^4\) example below: either coordinate twofold corresponding to one \(2\times2\) block of \(U\) has one tangent eigenline in each RM plane. The criterion imposes no contradiction on that support class by itself.

## 2. Proof by the two local first-order multiplication obstructions

The full cap-kernel calculation in SF-E819, section4, supplies classes whose holomorphic bivector components are the two independent \(\pi_+,\pi_-\). Divisor shear leaves those leading components unchanged. Published Buchweitz--Flenner Theorem6.4.2 and Proposition6.2.1 identify evaluation followed by semiregularity with contraction by the full Chern character. The precise finite-action compatibility is the same supplied DEG_L S-21 input as in SF-E819. Hence injective invariant semiregularity implies that both ordinary characteristic classes of \(E\) vanish.

Restrict to an affine neighborhood of the point. The \(H^2(\mathcal O_X)\) and \(H^1(T_X)\) terms of the chosen Hochschild classes restrict to zero. The remaining local classes are the first-order multiplication deformations defined by \(\pi_+,\pi_-\). Naturality of the characteristic morphism with inclusions and projections shows that a zero characteristic endomorphism on a direct sum has zero characteristic endomorphism on each direct summand. Shifts do not change vanishing. Thus each local coherent sheaf \(i_*F\) has zero first-order characteristic obstruction for both bivectors.

The explicit bar/resolution calculation in SF-E819, section3, now gives a flat first-order module deformation of \(i_*F\) for each multiplication class. Let \(I_S\) be its annihilator on the neighborhood; it equals the reduced ideal of \(S\), because \(F\) is locally free and nonzero on \(S\). If \(f,g\in I_S\), their actions on a flat first-order deformation reduce to zero. Each therefore carries the module into its \(\varepsilon\)-multiple. Their two composites are zero, since \(\varepsilon^2=0\). The deformed algebra commutator, however, acts as

\[
 [f,g]_* =\varepsilon\pi(df,dg).
\]

Flatness over the dual numbers identifies the \(\varepsilon\)-multiple with the original module. We conclude that \(\pi(df,dg)\) annihilates \(i_*F\), and hence

\[
 \{I_S,I_S\}_{\pi_+}\subset I_S,
 \qquad \{I_S,I_S\}_{\pi_-}\subset I_S.
 \tag{E821.3}
\]

This is the precise first-order coisotropy condition used here. No all-order quantization or general involutivity theorem is imported.

Let \(N_p^*S\subset V_+^*\oplus V_-^*\) be the two-dimensional conormal space. Condition(E821.3) says that its projection to either two-dimensional summand is isotropic for that summand's nondegenerate alternating form, and thus has dimension at most one. Both projections must have dimension one: otherwise the two-dimensional conormal space would project with dimension two to the other summand. Therefore

\[
 N_p^*S=\ell_+^*(p)\oplus\ell_-^*(p)
\]

for lines in the two cotangent planes. Taking annihilators proves(E821.1). The form \(\theta_+\) has rank one on this surface tangent plane, and so does \(\theta_-\). Their squares restrict to zero. Since the same holds on a dense open subset of the smooth locus, it holds throughout that locus by continuity. The pairing of a smooth form with the fundamental surface cycle is its integral over that regular locus; lower-dimensional singular subsets do not contribute to that cycle integral. This proves(E821.2), including for a surface cycle whose irreducible components satisfy the local hypothesis.

Finally, \(\theta_+^3=\theta_-^3=0\), while
\(\int_X\theta_+^2\theta_-^2>0\). Thus

\[
 \int_X k^2\theta^2\theta_+^2
   =k^2\int_X\theta_+^2\theta_-^2>0,
\]

and likewise with the two signs interchanged. This contradicts(E821.2) for a surface cycle of class \(k^2\theta^2\). The proof does not use gluability or simplicity; it only uses the asserted local summand and weak semiregularity.

## 3. Why the proposed two-cohomology surface cones have this local summand

Let \(A\) be a vector bundle and let

\[
 B=B_0\oplus C_1\oplus\cdots\oplus C_s,
 \qquad C_j=i_{j*}F_j,
 \tag{E821.4}
\]

where \(B_0\) is coherent and each \(F_j\) is a line bundle, or more generally a nonzero vector bundle, on the smooth part of a reduced surface \(S_j\). For any actual class \(a\in\operatorname{Ext}^2_X(A,B)\), form the actual distinguished triangle

\[
 B[1]\longrightarrow E_a\longrightarrow A
        \xrightarrow{a}B[2].
 \tag{E821.5}
\]

On an affine neighborhood \(U\) where \(A\) is locally free,
\(\operatorname{Ext}^2_U(A|_U,B|_U)=H^2(U,A^\vee\otimes B)=0\).
Thus(E821.5) splits there as \(A|_U\oplus B|_U[1]\).
Near a general smooth point of a component of any \(S_j\), the corresponding \(i_{j*}F_j[1]\) is consequently a genuine local direct summand. This is a local splitting of the actual triangle; the sheaves \(C_j\) are not being inferred as global summands of an arbitrary extension.

If the full character of \(E_a\) is balanced and any one of these surface cycles has a positive pairing in(E821.2), SF-E821 excludes weak semiregularity for every specified coherent finite action that might exist. This applies to every extension class \(a\), including classes with nonzero components in the surface Ext groups.

## 4. A signed class outside the primitive-factor hypotheses

Use \(X=E_i^4\) with its standard product principal polarization \(\theta\), and

\[
 U=\operatorname{diag}\left(
 \begin{pmatrix}1&1\\1&-1\end{pmatrix},
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}\right).
\]

The RM eigenpolarizations satisfy
\(\theta=\theta_++\theta_-\) and
\(\theta_U=\sqrt2(\theta_+-\theta_-)\).
For an integer \(k\ge1\), put

\[
 D=k\theta,
 \qquad N=k\theta_U.
\]

Direct expansion, using \(\theta_+^3=\theta_-^3=0\), gives the entire character identity

\[
 \begin{split}
 &18+e^N+e^{-N}
       -e^{D+N}-e^{-D-N}-e^{D-N}-e^{-D+N}\\
 &\qquad=16-4k^2(\theta_+^2+\theta_-^2)
                 +k^4\theta_+^2\theta_-^2
       =16v_{k^2/2}.
 \end{split}
 \tag{E821.6}
\]

The odd terms vanish in the displayed pairs. The degree-two calculation is
\(N^2-(D+N)^2-(D-N)^2=-2D^2-N^2\).
The degree-four term is
\((N^4-(D+N)^4-(D-N)^4)/12=k^4\theta_+^2\theta_-^2\).
Since \(\int_X\theta_+^2\theta_-^2=4\), its self-Euler characteristic is \(256k^4\).

These divisor classes are not primitive on each RM plane. The signed expression is therefore not covered merely by the primitive-factor hypotheses of SF-E815 or SF-E816.

## 5. Actual surface sheaves and actual gluable complexes

We give an explicit existence construction, rather than leaving(E821.6) as a virtual class. Write the four elliptic coordinates as \(x_1,\ldots,x_4\). Choose on each elliptic factor a point \(a_i\) of exact order \(L=2k+1\). Put

\[
 A_i=\{0,a_i,\ldots,(k-1)a_i\},
 \qquad
 B_i=\{ka_i,\ldots,(2k-1)a_i\}.
\]

Let \(D_0\) be the sum of the coordinate divisors \(x_i=a\) for \(a\in A_i\), and let \(D_1\) be the analogous sum for \(b\in B_i\). Each has class \(D=k\theta\), and they have no common irreducible divisor. Their complete intersection \(S=D_0\cap D_1\) is a reduced surface. Indeed, locally their equations are products of disjoint subsets of regular coordinate parameters; the resulting ideal is the intersection of the prime ideals generated by one parameter from each subset. Its irreducible components are the smooth coordinate twofolds

\[
 x_i=a\in A_i,\qquad x_j=b\in B_j,\qquad i\ne j.
\]

Their fundamental cycle has class \([S]=k^2\theta^2\).

Choose the standard line bundles with classes \(D\) and \(\pm N\), using the product polarization and Poincare bundles for the displayed integral Hermitian matrices. Choose a prime \(p>L\), and a degree-zero line bundle \(P\) whose restriction to every elliptic factor is a nonzero point of exact order \(p\). Define

\[
 C_\pm=(L_{\pm N}\otimes L_D\otimes P)|_S,
 \qquad
 B=L_N\oplus L_{-N}\oplus i_*C_+\oplus i_*C_-.
 \tag{E821.7}
\]

The notation \(C_\pm\) in(E821.7) denotes line bundles on \(S\); the last two terms of \(B\) are their pushforwards.

We claim \(H^0(S,C_+)=H^0(S,C_-)=0\). For the plus sign, the Hermitian matrix of \(L_N\otimes L_D\) in either two-coordinate block is

\[
 k\begin{pmatrix}2&1\\1&0\end{pmatrix}.
\]

On a component whose two free coordinates belong to that same block, this is nondegenerate of index one, so it has no sections, even after any degree-zero twist. This is exactly the already checked Mumford index theorem, *Abelian Varieties*, section16, printed pp150--153 and162--163. On a component with one free coordinate from each block, the restriction is an external product of line bundles of degrees \(2k\) or zero. If either degree is zero, its flat part is an \(L\)-torsion class plus the specified nonzero \(p\)-torsion class. It is nontrivial because \(p\) and \(L\) are coprime, so that component has no sections.

Only components with free coordinates \(x_1,x_3\) can remain. The restriction of a global section to such a component must vanish along all the divisors \(x_1\in A_1\cup B_1\) and \(x_3\in A_3\cup B_3\): each is an intersection with a component just shown to have no sections. Subtracting those \(2k\) points on each factor leaves an external product of degree-zero line bundles. Again its flat part on either factor is an \(L\)-torsion class plus a nonzero \(p\)-torsion class, so it has no sections. The restriction to every irreducible component is zero. A section of a line bundle on a reduced scheme injects into its restrictions at the generic points of the irreducible components, so the section is zero.

For the minus sign the block matrix is
\(k\left(\begin{smallmatrix}0&-1\\-1&2\end{smallmatrix}\right)\).
The identical argument interchanges odd and even coordinate indices; the possible positive components now have free coordinates \(x_2,x_4\). This proves the claim.

The bundles \(L_{\pm N}\) themselves have index two and \(h^2=4k^4\), so

\[
 H^0(X,B)=0,
 \qquad H^2(X,B)\supset H^2(X,L_N\oplus L_{-N})
                  \simeq\mathbf C^{8k^4}.
 \tag{E821.8}
\]

Choose any nonzero class
\(a\in\operatorname{Ext}^2_X(\mathcal O_X^{18},B)
=H^2(X,B)\otimes(\mathbf C^{18})^*\), and form(E821.5) with \(A=\mathcal O_X^{18}\). This is an actual perfect complex, since every coherent sheaf on the smooth fourfold is perfect. It has cohomology \(B\) in degree \(-1\) and \(\mathcal O^{18}\) in degree zero.

It is ordinarily gluable. The exact two-cohomology identity proved in SF-E816a gives
\(\operatorname{Ext}^{-1}(E_a,E_a)=\operatorname{Hom}(\mathcal O^{18},B)=0\).
For degrees at most \(-2\), the standard t-structure gives vanishing directly from these two cohomological degrees. This argument imposes no unproved formality or degeneration assertion.

Finally, the Koszul resolution of the actual complete intersection gives

\[
 \operatorname{ch}(i_*C_\pm)
   =e^{\pm N}(e^D-2+e^{-D}).
 \tag{E821.9}
\]

Flat twists do not change this character. Combining(E821.7) and(E821.9), the class of the actual triangle is exactly(E821.6). Thus these are actual ordinarily gluable, rank16 balanced perfect complexes, with \(q=k^2/2\). No simplicity or finite action is asserted. The local support criterion proves that none can be weakly semiregular for any specified coherent finite action, because \(S\) has class \(k^2\theta^2\).

## 6. Remaining scope

The local support criterion applies whenever the indicated surface object is an actual local direct summand, whether or not a global splitting exists. It does not identify the cohomology pieces of an arbitrary perfect complex as direct summands. In particular, gluing through a non-locally-free quotient, through local positive-degree Ext groups, or through a complex with a genuinely coupled local differential is outside this proof. Surface support of mixed RM tangent type is not excluded merely by its existence. These are concrete remaining ways a surface construction might evade the obstruction.
