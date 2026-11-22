# The complete-intersection plus points secant: an actual-object obstruction

Author/checker: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION `/root/sixfolds`. Date: 2026-11-21.

**Status.** Independently whole-proof reviewed by `/root` and `/root/imprimitive` on 2026-11-21: both GPT-6 Astra Pro, inherited effort not exposed; PASS for SF-E809--E810, including the Koszul and full trace ranks, invariant kernel and same-character Euler equality. The exact computation in `ci_secant_certificate.py` has actually run and passed. The sibling read every script line but did not rerun it, and no sibling computation is claimed. It checks the finite exterior algebra and the character/Euler identities; it does not substitute for any geometric or categorical argument below. Canonical deliverables are `ci_secant_obstruction_proofs.md` and `ci_secant_obstruction_section.tex`; this draft-path copy is retained so earlier review links remain usable.

These results concern a genuine rank-one ideal sheaf whose Chern character is a real quadratic two-exponential secant. This character is **not** the balanced real-multiplication product character of DEG_L S-22: their degree-two Hochschild contraction ranks are respectively 12 and 18. No genuine RM eightfold seed is asserted or presumed.

## SF-E809. Exact semiregularity kernel of the proposed ideal

Let \((B,\theta)\) be a principally polarized complex abelian fourfold. Let \(0<a<b\) be integers and suppose that divisors \(D_a\in|a\theta|\), \(D_b\in|b\theta|\) meet transversely in a smooth surface

\[
 S=D_a\cap D_b.
\]

Let \(Z\) be a reduced set of \(N>0\) points, disjoint from \(S\), and put \(F=I_{S\sqcup Z}\). The assertion is conditional only on this stated smoothness; for example, general divisors in \(|2\theta|,|4\theta|\) have the required property. Write

\[
 \sigma_F^j:\operatorname{Ext}^j(F,F)\longrightarrow HH_{-j}(B)
\]

for the full Atiyah--Chern trace. Then

\[
 \begin{aligned}
 \dim\operatorname{Ext}^1(F,F)
   &=a^4+b^4-(b-a)^4+10+4N,\\
 \dim\operatorname{Ext}^2(F,F)&=18+6N,\\
 \operatorname{rank}\sigma_F^2&=18,\\
 \dim\ker\sigma_F^2&=6N.
 \end{aligned}
 \tag{E809.1}
\]

More strongly, if a finite subgroup \(G\subset B\times\widehat B\) stabilizes \(F\), with any coherent equivariant structure, and if \(r\) is the number of its orbits on \(Z\), then

\[
 \dim\ker\left(\sigma_F^2|_{\operatorname{Ext}^2(F,F)^G}\right)=6r>0.
 \tag{E809.2}
\]

Consequently this ideal is not weakly \(G\)-semiregular for any such finite group. Its external product with its derived dual fails the same condition for every finite translation/tensor stabilizer on \(B\times B\), including correlated actions on the two factors. A Fourier--Mukai equivalence, line-bundle twist or shift cannot remove this invariant trace kernel.

### 1. The complete-intersection self-Ext groups

The two-term Koszul resolution of \(I_S\) is

\[
 0\longrightarrow\mathcal O_B(-(a+b)\theta)
 \longrightarrow\mathcal O_B(-a\theta)\oplus\mathcal O_B(-b\theta)
 \longrightarrow I_S\longrightarrow0.
 \tag{E809.3}
\]

Its sheaf endomorphism complex has terms

\[
 \begin{array}{c|c}
 \text{degree}&\text{term}\\ \hline
 -1&\mathcal O_B(-b\theta)\oplus\mathcal O_B(-a\theta)\\
 0&\mathcal O_B^{\oplus3}\oplus\mathcal O_B((b-a)\theta)
                          \oplus\mathcal O_B(-(b-a)\theta)\\
 1&\mathcal O_B(b\theta)\oplus\mathcal O_B(a\theta).
 \end{array}
 \tag{E809.4}
\]

For a positive integer \(m\), the cohomology of \(\mathcal O_B(m\theta)\) is concentrated in degree zero and has dimension \(m^4\); the negative line bundle has cohomology only in degree four. Also \(h^q(\mathcal O_B)=\binom4q\). These statements follow from Kodaira vanishing, Serre duality, and Riemann--Roch with trivial Todd class.

In the hypercohomology spectral sequence of (E809.4), the sole nonzero term of total degree two is the degree-two cohomology of the three trivial summands in degree zero. No higher differential enters or leaves this term, since the complex has only columns \(-1,0,1\). Thus

\[
 \operatorname{Ext}^2(I_S,I_S)\simeq H^2(\mathcal O_B)^{\oplus3},
 \qquad \dim\operatorname{Ext}^2(I_S,I_S)=18.
 \tag{E809.5}
\]

For total degree one there are the 12 dimensions in \(H^1(\mathcal O_B)^{\oplus3}\) and the cokernel on global sections of the map from degree zero to degree one. Its kernel has dimension one: every global endomorphism of a rank-one ideal with codimension-two support is scalar, since it is a regular function off that support and extends over the normal variety \(B\). The cokernel therefore has dimension

\[
 a^4+b^4-\bigl(3+(b-a)^4\bigr)+1.
\]

There are again no relevant higher differentials. Hence

\[
 \dim\operatorname{Ext}^1(I_S,I_S)
   =a^4+b^4-(b-a)^4+10.
 \tag{E809.6}
\]

### 2. The complete-intersection trace is injective in degree two

We prove this from the full trace/cap identity, not from a termwise diagonal trace in a chosen resolution. Put

\[
 W=H^0(B,T_B)\oplus H^1(B,\mathcal O_B),\qquad\dim W=8.
\]

Choose a holomorphic volume form. As in SF-E801, it identifies \(HH_{-j}(B)\) with \(\bigwedge^{4+j}W\) and makes Hochschild cap product exterior multiplication. Write \(E=H^1(B,\mathcal O_B)\), and choose bases \(e_1,\ldots,e_4\) of \(E\) and \(p_1,\ldots,p_4\) of \(H^0(B,T_B)\) so that contraction with \(\theta\) sends \(p_i\) to \(e_i\). Up to one fixed nonzero normalization, the character \(e^{t\theta}\) is the decomposable four-vector

\[
 v_t=\bigwedge_{i=1}^4(p_i-t e_i).
 \tag{E809.7}
\]

It is enough to compute the rank of multiplication by

\[
 v=v_{-a}+v_{-b}-v_{-(a+b)},
\]

because the Koszul resolution gives

\[
 \operatorname{ch}(I_S)=e^{-a\theta}+e^{-b\theta}-e^{-(a+b)\theta}.
 \tag{E809.8}
\]

There is a common 10-dimensional kernel in \(\bigwedge^2W\), namely

\[
 K=\left\langle e_i\wedge p_i,\;
 e_i\wedge p_j+e_j\wedge p_i\ (i<j)\right\rangle.
 \tag{E809.9}
\]

Indeed, on the quotient by the support of \(v_t\) we have \(p_i=t e_i\). A complementary 18-dimensional space has, for each \(i<j\), the three basis vectors

\[
 e_i\wedge e_j,\quad
 \frac{e_i\wedge p_j-e_j\wedge p_i}{2},\quad
 p_i\wedge p_j.
\]

Their images in that quotient are respectively \(1,t,t^2\) times \(e_i\wedge e_j\). Consequently the symmetric bilinear form

\[
 (z,w)\longmapsto z\wedge w\wedge v
\]

on this complement is the tensor product of the nondegenerate exterior pairing on \(\bigwedge^2E\) with

\[
 H=\sum_{(t,\lambda)=(-a,1),(-b,1),(-(a+b),-1)}
       \lambda\begin{pmatrix}1\\t\\t^2\end{pmatrix}
                    \begin{pmatrix}1&t&t^2\end{pmatrix}.
\]

The graph-to-quotient determinant in this calculation is one, independent of \(t\). The Vandermonde determinant gives

\[
 \det H=-a^2b^2(a-b)^2\ne0.
 \tag{E809.10}
\]

Thus multiplication by \(v\) from \(\bigwedge^2W\) to \(\bigwedge^6W\) has rank 18 and kernel exactly \(K\). Its image is

\[
 \mathcal T=K^\perp\subset\bigwedge^6W,
 \qquad\dim\mathcal T=18,
 \tag{E809.11}
\]

where orthogonality uses the perfect top exterior pairing. The six-dimensional subspace

\[
 H^4(B,\Omega_B^2)=\bigwedge^4E\otimes\bigwedge^2\langle p_1,\ldots,p_4\rangle
\]

lies in \(\mathcal T\): every element of \(K\) has an \(e_i\) factor, which wedges to zero with \(\bigwedge^4E\).

Let \(\rho^2\) denote Hochschild evaluation on the object. The Atiyah--Chern identity is

\[
 \sigma_{I_S}^2\rho_{I_S}^2
       =(-)\mathbin{\lrcorner}\operatorname{ch}(I_S).
 \tag{E809.12}
\]

The right-hand side has rank 18, and its middle Ext group has dimension 18 by (E809.5). Therefore \(\sigma_{I_S}^2\) is injective and its image is exactly \(\mathcal T\).

### 3. Disjoint support and the local point summands

For any rank-one ideal \(I_T\) with support of codimension at least two, the unit and trace split its derived endomorphism complex as

\[
 R\mathcal Hom(I_T,I_T)=\mathcal O_B\oplus\mathcal E_T,
 \tag{E809.13}
\]

because trace composed with the unit is multiplication by the rank, which is one. Moreover \(\mathcal Hom(I_T,I_T)=\mathcal O_B\), so all cohomology sheaves of \(\mathcal E_T\) have positive degree and are supported on \(T\).

A coherent derived object supported on a union of disjoint closed subsets splits into its objects supported on those subsets. For coherent sheaves this is the support decomposition, or equivalently the Chinese remainder decomposition on a sufficiently high infinitesimal neighborhood of the support. The decomposition extends through the bounded derived category, since there are no Hom or Ext groups between objects with disjoint supports. It does not require disjoint Zariski open neighborhoods. Applied to \(S\sqcup Z\), and using that the ideals coincide near their respective supports, this gives

\[
 \mathcal E_{S\sqcup Z}\simeq\mathcal E_S\oplus
                   \bigoplus_{z\in Z}\mathcal E_z.
 \tag{E809.14}
\]

At a smooth point of a fourfold, the truncated Koszul resolution of the maximal ideal gives the trace-free local self-Ext spaces

\[
 \mathcal H^j(\mathcal E_z)=\bigwedge^j T_zB,
 \quad j=1,2,3.
 \tag{E809.15}
\]

One can also obtain (E809.15) by applying Hom to \(0\to I_z\to\mathcal O_B\to\mathcal O_z\to0\) and the full Koszul resolution of \(\mathcal O_z\). The first three local tangent-space exterior powers have dimensions 4,6,4. The degree-four map \(\operatorname{Ext}^4(\mathcal O_z,\mathcal O_B)\to\operatorname{Ext}^4(\mathcal O_z,\mathcal O_z)\) is an isomorphism in the local Koszul comparison, so no fourth local self-Ext remains. Since these sheaves have zero-dimensional support, there is no higher sheaf cohomology. Thus (E809.14) proves the two self-Ext dimensions in (E809.1).

We now identify the trace images, a point needed for the invariant statement. The trace on the \(S\)-supported summand agrees with that for \(I_S\), by restriction and locality of the Atiyah class. More explicitly, any two extensions of the restricted trace differ by a morphism supported on \(Z\), and a source supported on \(S\) has no such morphism. On the shared \(H^2(\mathcal O_B)\) summand, the trace is multiplication by the Chern character. Replacing \(I_S\) by \(F\) subtracts \(N[\mathrm{pt}]\), whose product with \(H^2(\mathcal O_B)\) vanishes for dimensional reasons. Therefore the full 18-dimensional trace image \(\mathcal T\) of \(I_S\) persists unchanged inside the trace image of \(F\).

For a single point ideal, evaluation of a bivector in \(\bigwedge^2H^0(T_B)\) has trace equal to contraction with \(-[z]\), by (E809.12). This is an isomorphism onto \(H^4(\Omega_B^2)\). Its ordinary trace component in \(H^2(\mathcal O_B)\) is zero, so evaluation lies in the trace-free local summand. That summand has dimension six by (E809.15); its full trace is consequently an isomorphism onto \(H^4(\Omega_B^2)\), with no other trace components. Locality gives the same statement for each point in (E809.14).

All the point images are therefore already in \(\mathcal T\). The total trace has image exactly \(\mathcal T\), rank 18, and kernel dimension \(6N\), proving (E809.1).

### 4. Every finite translation/tensor stabilizer retains a kernel

The determinant of \(F\) is trivial and its rank is one. If

\[
 t_x^*F\otimes P\simeq F,\qquad P\in\widehat B,
\]

then determinants give \(P\simeq\mathcal O_B\). Thus every finite stabilizer in \(B\times\widehat B\) consists of translations. The translation preserves the subscheme \(S\sqcup Z\), hence preserves \(S\) and permutes \(Z\), since their dimensions differ.

Translations act trivially on Hodge cohomology. Since \(\sigma_{I_S}^2\) is injective and natural for translations preserving \(S\), they act trivially on \(\operatorname{Ext}^2(I_S,I_S)\). On the point summands they permute the points and identify their tangent spaces by the identity translation derivative. Scalar choices in an equivariant structure cancel in the conjugation action on self-Ext. The splitting above is natural for these actions.

It follows that the invariant point contribution has dimension \(6r\), while the invariant complete-intersection contribution still maps isomorphically to \(\mathcal T\). For each invariant point vector, its trace has a unique preimage in that complete-intersection contribution, and subtracting this preimage gives an invariant trace-kernel vector. Conversely these are all the kernel vectors, since the complete-intersection trace is injective. This proves (E809.2).

For \(F\boxtimes F^\vee\), the Kunneth summand

\[
 \operatorname{Ext}^2(F,F)\otimes\operatorname{Hom}(F^\vee,F^\vee)
\]

contains these nonzero vectors tensored with the identity, and their full trace is zero by the tensor-product trace formula. For completeness, a finite stabilizer of the product again has trivial flat-line component by its rank-one trivial determinant. Its two translation projections preserve \(F\) and \(F^\vee\), as follows by restricting a product isomorphism to a generic fiber away from the relevant supports. Such an isomorphism factors up to a scalar into isomorphisms on the two factors: both factors are simple and have no negative self-Ext, so the degree-zero Kunneth Hom space is their one-dimensional tensor product. Hence the invariant vector just constructed for the first projected group, tensored with the identity on the second factor, is invariant for the whole group, even when its two projections are correlated.

An equivalence identifies self-Ext, Hochschild homology, evaluation and trace; for abelian varieties it also conjugates the translation/tensor group. Thus Fourier--Mukai equivalences preserve the stated failure for actual finite stabilizers. Line-bundle twists and shifts are special cases. No assertion about an arbitrary new equivariant object after an unrelated isogeny is needed or made. This completes the proof of SF-E809.

## SF-E810. A numerical obstruction to every ordinary same-character repair

Let \(F\) be a simple gluable perfect complex on an abelian fourfold. Here gluable means \(\operatorname{Ext}^{j}(F,F)=0\) for \(j<0\). Suppose that, after the Fock identification above, its full Chern character is a nondegenerate two-pure secant

\[
 v=\lambda\operatorname{vol}_L+\mu\operatorname{vol}_M,
 \quad W=L\oplus M,\quad\dim L=\dim M=4,\quad\lambda\mu\ne0.
 \tag{E810.1}
\]

If \(\sigma_F^2\) is injective, then

\[
 \dim\operatorname{Ext}^2(F,F)=12,\qquad
 \operatorname{rank}\sigma_F^1=8,\qquad
 \dim\ker\sigma_F^1=\frac{-\chi(F,F)-2}{2}.
 \tag{E810.2}
\]

In particular, simultaneous injectivity of \(\sigma_F^1\) and \(\sigma_F^2\) forces

\[
 \chi(F,F)=-2.
 \tag{E810.3}
\]

The ordinary external product \(F\boxtimes F^\vee\) cannot be fully semiregular unless (E810.3) holds. These statements concern ordinary full semiregularity; for an arbitrary replacement object they do not exclude a new finite equivariant action whose invariant Ext groups are smaller.

### Proof of the character-level assertion

For a Calabi--Yau fourfold, the degree-two Hochschild evaluation \(\rho_F^2\) and full trace \(\sigma_F^2\) are adjoint under Serre duality and the perfect Hochschild pairing. This is the same evaluation/trace adjunction used in supplied DEG_L S-21 and in SF-E802. Injectivity of \(\sigma_F^2\) therefore makes \(\rho_F^2\) surjective. By the full trace/cap identity and SF-E801,

\[
 \dim\operatorname{Ext}^2(F,F)=\operatorname{rank}c_v^2=12,
 \qquad\ker\rho_F^2=\ker c_v^2=L\otimes M.
 \tag{E810.4}
\]

Write \(I=L\otimes M\). For \(\xi\in I\) and \(\alpha\in\operatorname{Ext}^1(F,F)\), compatibility of Hochschild action with trace gives

\[
 \xi\wedge\sigma_F^1(\alpha)
   =\sigma_F^3\bigl(\rho_F^2(\xi)\circ\alpha\bigr)=0.
 \tag{E810.5}
\]

The common annihilator of \(I\) in \(\bigwedge^5W\) is exactly

\[
 \mathcal A=
 \bigl(\bigwedge^4L\otimes M\bigr)
 \oplus\bigl(L\otimes\bigwedge^4M\bigr),\qquad\dim\mathcal A=8.
 \tag{E810.6}
\]

To see this, decompose a five-vector by bidegrees \((4,1),(3,2),(2,3),(1,4)\). The extreme components are killed by every mixed bivector. For either interior component, the collective maps \(\bigwedge^p L\to\operatorname{Hom}(L,\bigwedge^{p+1}L)\) and \(\bigwedge^{5-p}M\to\operatorname{Hom}(M,\bigwedge^{6-p}M)\), given by wedging with every possible additional vector, are injective, because their source exterior degrees are strictly below four. Their tensor product is injective as well. Thus a nonzero interior component is detected by some mixed bivector. Components of different bidegrees cannot cancel. This proves (E810.6).

Equation (E810.5) gives rank at most eight for \(\sigma_F^1\). On the other hand \(c_v^1:W\to\bigwedge^5W\), \(x\mapsto x\wedge v\), is injective: its two summands occupy the distinct bidegrees \((1,4)\), \((4,1)\) and both coefficients in (E810.1) are nonzero. Since \(c_v^1=\sigma_F^1\rho_F^1\), the trace has rank exactly eight.

Gluability and Serre duality give no self-Ext outside degrees zero through four. Simplicity gives \(e_0=e_4=1\); Serre duality gives \(e_3=e_1\); (E810.4) gives \(e_2=12\). Therefore

\[
 \chi(F,F)=14-2e_1,
 \qquad\dim\ker\sigma_F^1=e_1-8=\frac{-\chi(F,F)-2}{2}.
\]

This proves (E810.2)--(E810.3).

Finally, full semiregularity of \(F\boxtimes F^\vee\) forces injectivity of \(\sigma_F^2\), by its factor-Ext Kunneth summand. It also forces injectivity of \(\sigma_F^1\): if a nonzero \(\alpha\) is in the latter kernel, tensor it with any nonzero element of \(\operatorname{Ext}^1(F^\vee,F^\vee)\), which exists since \(e_1\ge8\). The tensor is a nonzero degree-two product-Ext vector whose trace vanishes. This proves the external-product assertion.

### Application to the tuned complete-intersection character

Put \(p=ab\) and \(s=a+b\). The character of \(I_S\) is

\[
 1-\frac{A}{2}\theta^2+\frac{B}{6}\theta^3
        +\frac{C_{\rm actual}}{24}\theta^4,
 \quad A=2p,\quad B=3ps,\quad
 C_{\rm actual}=-4p(a^2+b^2)-6p^2.
 \tag{E810.7}
\]

A normalized two-exponential moment sequence with rank one and first Chern class zero must have

\[
 C_{\rm required}=A^2-\frac{B^2}{A}.
\]

The difference is

\[
 C_{\rm actual}-C_{\rm required}=\frac{ab(a-b)^2}{2}=N.
 \tag{E810.8}
\]

This is an integer for every pair of integers \(a,b\): if \(ab\) is odd, then \(a-b\) is even. Thus no extra parity hypothesis on \(ab\) is necessary. Since \(\theta^4/24=[\mathrm{pt}]\), adding exactly these \(N\) disjoint points gives the required character.

Let \(u,v\) be the roots with

\[
 uv=A,\qquad u+v=-B/A=-3s/2.
\]

They are distinct, nonzero, and real, with squared difference

\[
 D=(u-v)^2=\frac{9a^2-14ab+9b^2}{4}
     =ab+\frac94(a-b)^2>0.
 \tag{E810.9}
\]

The weights \(\lambda=-v/(u-v)\), \(\mu=u/(u-v)\) are nonzero, sum to one and give first moment zero. The recurrence of their moment sequence gives exactly the coefficients in (E810.7) with \(C_{\rm required}\). Hence

\[
 \operatorname{ch}(I_{S\sqcup Z})=\lambda e^{u\theta}+\mu e^{v\theta}.
 \tag{E810.10}
\]

The two graph supports in the Fock space are transverse because \(u-v\ne0\) and \(\theta\) is nondegenerate. Thus (E810.1) applies, whether or not \(D\) is a rational square. For \((a,b)=(2,4)\), \(N=16\), \(D=17\), and this is an actual irrational real-quadratic secant.

Hirzebruch--Riemann--Roch, again with trivial Todd class, gives for every object with this same character

\[
 \begin{aligned}
 \chi(F,F)
 &=2C_{\rm required}+6A^2
   =8A^2-2B^2/A\\
 &=-4abD
   =-ab\bigl(4ab+9(a-b)^2\bigr).
 \end{aligned}
 \tag{E810.11}
\]

For unequal positive integers this is at most \(-34\), attained at \((a,b)=(1,2)\). Therefore **no simple gluable replacement with the same full Chern character can have both \(\sigma^1\) and \(\sigma^2\) injective**, and none can yield an ordinarily fully semiregular external product with its dual. The numerical examples are

\[
 \begin{array}{c|r|r|r|r|r}
 (a,b)&N&\chi(F,F)&\dim\operatorname{Ext}^1(I_{S\sqcup Z})&
 \dim\operatorname{Ext}^2(I_{S\sqcup Z})&\dim\ker\sigma^2\\ \hline
 (1,2)&1&-34&30&24&6\\
 (2,4)&16&-544&330&114&96.
 \end{array}
\]

The first row is conditional on the stated smooth complete intersection; the second exists for general divisors by basepoint freeness and Bertini. These numbers also satisfy \(\chi=2-2e_1+e_2\), an independent consistency check.

## Exact scope and remaining directions

SF-E809 rules out the actual complete-intersection-plus-reduced-points object, its ordinary external product and every finite translation/tensor invariant version of those objects. SF-E810 rules out all **simple gluable ordinary** same-character repairs of the external-product strategy. It does not rule out an arbitrary equivariant replacement with smaller invariant Ext spaces, a nonsimple indecomposable object, a different full character, or the balanced RM product character with an even local denominator/group factor. Those are distinct remaining gates.

## Primary inputs and proof provenance

1. Buchweitz--Flenner, *A semiregularity map for modules and applications to deformations*, Compositio Math. 137 (2003), 135--210, §4.1 and Proposition 4.2, pp.166--167, DOI `10.1023/A:1023999012081`: exponential Atiyah trace and contraction compatibility. Published PDF: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/semiregularity_map_for_modules_and_applications_to_deformations.pdf>.
2. Buchweitz--Flenner, *The global decomposition theorem for Hochschild (co-)homology of singular spaces via the Atiyah--Chern character*, Adv. Math. 217 (2008), 243--281, DOI `10.1016/j.aim.2007.06.013`; author-version Proposition 6.2.1 and Theorem 6.4.2, author pp.29,31: Hochschild factorization, evaluation/trace and module compatibility. The published work, not an unrefereed theorem, is being invoked; exact author-copy locators are distinguished from journal pagination. Author PDF: <https://arxiv.org/pdf/math/0606730>.
3. The Calabi--Yau evaluation/trace adjunction is the categorical duality already proved/used in supplied DEG_L S-21 and reviewed SF-E802. The new common-annihilator argument in degree five and the resulting Euler equality are proved here in full.
4. Orlov, *Derived categories of coherent sheaves on abelian varieties and equivalences between them*, Izv. Math. 66 (2002), Theorem 2.10 and Corollary 2.13 (author pp.9--12), supplies conjugation of the actual translation/tensor groups under derived equivalences; those statements and the corollary proof were read in the earlier SF-E803 audit. The failure of the product before any equivalence is proved here directly.
5. The exact Koszul, Vandermonde, support splitting, invariant-kernel and Euler arguments above are new deductions in this work. They invoke no Markman or other preprint assertion.
