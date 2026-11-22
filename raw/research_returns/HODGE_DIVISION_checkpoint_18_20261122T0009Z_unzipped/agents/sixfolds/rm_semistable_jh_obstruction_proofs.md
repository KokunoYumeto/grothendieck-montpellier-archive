# SF-E813: the balanced-RM obstruction for locally free Jordan--Hölder factors

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

**Status:** Whole-proof mathematical PASS reviews received from both /root and /root/imprimitive on 2026-11-21 (GPT-6 Astra Pro; inherited effort not exposed). Both reviewers reconstructed the complete argument and checked the exact invoked Mumford statements in the original book scan. SF-E811--E812 are also independently root/peer checked. No assertion about singular stable factors or degree-two derived gluings is made.

## Statement

Let \(X\) be a complex abelian fourfold with genuine Rosati-invariant real multiplication by a real quadratic field, of type \((2,2)\), and compatible polarization

\[
 \theta=\theta_1+\theta_2.
\]

Let \(E\) be a slope-semistable vector bundle admitting a filtration by holomorphic subbundles

\[
 0=E^0\subset E^1\subset\cdots\subset E^s=E
 \tag{E813.1}
\]

whose quotients \(Q_j=E^j/E^{j-1}\) are slope-stable **locally free** sheaves of the same \(\theta\)-slope as \(E\). Suppose that, for a rational algebraic divisor \(B\), rank \(N>0\), and \(q>0\),

\[
 e^B\operatorname{ch}(E)=N
    \left(1-\frac q2\theta_1^2\right)
    \left(1-\frac q2\theta_2^2\right).
 \tag{E813.2}
\]

For any effective finite translation/tensor subgroup \(G\subset X\times\widehat X\), with a specified coherent action and an equivariant structure on \(E\), the full trace on \(\operatorname{Ext}^2(E,E)^G\) is not injective. Thus no such bundle is weakly \(G\)-semiregular.

The filtration condition is essential to the scope: a semistable vector bundle on a higher-dimensional variety need not have locally free stable Jordan--Hölder factors. This theorem does not silently replace a torsion-free factor by its reflexive hull. It also does not assert that \(E\) itself is polystable.

## 1. All stable factors are projectively flat

Put

\[
 r_j=\operatorname{rk}Q_j,\qquad
 \alpha_j=c_1(Q_j)/r_j,\qquad
 \alpha=c_1(E)/N,\qquad \delta_j=\alpha_j-\alpha.
\]

Additivity of the Chern character in (E813.1) gives exactly the same variance identity as for an actual direct sum:

\[
 \Delta(E)=\sum_j\Delta(Q_j)
          -\frac12\sum_jr_j\delta_j^2.
 \tag{E813.3}
\]

Here \(\Delta(F)=c_1(F)^2/(2\operatorname{rk}F)-\operatorname{ch}_2(F)\). The normalized degree-four part of (E813.2) gives

\[
 \Delta(E)=\frac{Nq}{2}(\theta_1^2+\theta_2^2),
 \qquad \int_X\Delta(E)\theta_1\theta_2=0.
 \tag{E813.4}
\]

Each \(Q_j\) is an actual stable vector bundle, so SF-E811 applies and gives nonnegative mixed discriminant pairing. Equality of slopes makes the invariant representative of each \(\delta_j\) primitive for \(\theta\). The exact mixed quadratic identity (E811.4) gives

\[
 -\int_X\delta_j^2\theta_1\theta_2\ge0.
\]

Every term on the right of (E813.3), after this pairing, is therefore nonnegative, and their sum is zero. It follows that every term vanishes. SF-E811 shows that every \(Q_j\) is projectively flat and

\[
 \operatorname{ch}(Q_j)=r_je^{\alpha_j}.
 \tag{E813.5}
\]

The equality case of the elementary mixed quadratic identity also says that each invariant \(\delta_j\) is block diagonal for the two real-multiplication eigenspaces, and primitive on each complex two-plane separately. Hence every difference

\[
 \alpha_j-\alpha_k=\delta_j-\delta_k
 \tag{E813.6}
\]

has those same two properties.

## 2. Every nonzero difference has Hermitian signature \((2,2)\)

We prove the rationality point explicitly. Let \(\delta\in H^2(X,\mathbf Q)\cap H^{1,1}(X)\) be nonzero, block diagonal and primitive on each of the two complex eigenspaces. If one of its blocks vanished, \(\delta\) would be supported on just one eigenspace, say the one corresponding to the real embedding \(\sigma_i\). For \(u\in F\setminus\mathbf Q\) and rational homology vectors \(x,y\), this would imply

\[
 \delta(ux,y)=\sigma_i(u)\delta(x,y).
 \tag{E813.7}
\]

The left side is rational, because both \(u\) and \(\delta\) are rational. Nonzero rational \(\delta\) has some rational pair \((x,y)\) with \(\delta(x,y)\ne0\). Equation (E813.7) would make the irrational real number \(\sigma_i(u)\) rational, a contradiction. Thus both blocks are nonzero.

In a unitary basis for either complex two-plane, the Hermitian matrix of a real primitive \((1,1)\)-form is

\[
 A_i=\begin{pmatrix}a_i&b_i+\mathrm i c_i\\
                      b_i-\mathrm i c_i&-a_i\end{pmatrix},
 \qquad
 \det A_i=-a_i^2-b_i^2-c_i^2<0.
 \tag{E813.8}
\]

Its eigenvalues have opposite signs. The complete four-dimensional Hermitian form of \(\delta\) is the direct sum of these two nonzero blocks, hence is nondegenerate of signature \((2,2)\). In particular

\[
 \int_X\frac{\delta^4}{24}>0.
 \tag{E813.9}
\]

This conclusion applies to each unequal pair in (E813.6). No assumption that the divisor space of \(X\) is minimal has been used.

## 3. Unequal factor classes have no degree-one extensions

We first give an elementary finite-isogeny splitting argument for the projectively flat factors, so no classification of semihomogeneous bundles is being assumed.

Let \(Q\) have rank \(r\), with its projectively flat Hermitian--Einstein connection. Its scalar curvature is a harmonic invariant \((1,1)\)-form representing \(c_1(Q)/r\), up to the usual Chern--Weil scalar. Choose any positive integer \(m\) divisible by \(r\), and consider multiplication \(\pi=[m]:X\to X\). The line bundle

\[
 L_Q=(\det Q)^{m^2/r}
 \tag{E813.10}
\]

on the source has first Chern class \(m^2c_1(Q)/r\), the normalized first Chern class of \(\pi^*Q\). Give it a Hermitian metric with that invariant curvature; this follows from the usual \(\partial\bar\partial\)-lemma for line-bundle metrics, or directly from the invariant metric in the Appell--Humbert description. The difference of the two scalar curvature forms is a harmonic form with zero class, and is zero. Thus

\[
 \pi^*Q\otimes L_Q^{-1}
\]

is unitary flat. A unitary representation of the abelian fundamental group of a torus is a direct sum of one-dimensional unitary characters, by simultaneous diagonalization of commuting normal matrices. Therefore

\[
 \pi^*Q\simeq\bigoplus_{a=1}^r (L_Q\otimes P_a),
 \qquad P_a\in\operatorname{Pic}^0(X).
 \tag{E813.11}
\]

This is a genuine splitting of holomorphic bundles. Neither a projective action nor a root of a line bundle is substituted for it.

Apply this construction to two factors \(Q_j,Q_k\), taking \(m\) divisible by both ranks. If \(\alpha_j\ne\alpha_k\), every line-bundle summand of

\[
 (\pi^*Q_j)^\vee\otimes\pi^*Q_k
\]

has first Chern class \(m^2(\alpha_k-\alpha_j)\), whose Hermitian form is nondegenerate of signature \((2,2)\). Mumford's vanishing theorem and its complex index corollary then give cohomology only in degree two. The exact published locators are *Abelian varieties*, §16, Vanishing Theorem printed p.150, proof pp.150--153, and the unnumbered complex Hermitian-index corollary with proof pp.162--163. These statements are unchanged by a tensor factor in \(\operatorname{Pic}^0\), since that factor has zero curvature class.

Consequently

\[
 \operatorname{Ext}^{\ell}(\pi^*Q_j,\pi^*Q_k)=0
 \quad\text{for all }\ell\ne2.
 \tag{E813.12}
\]

The pullback map on these Ext groups is injective. Indeed, for a finite étale map the trace, divided by its degree, splits the unit inclusion \(\mathcal O_X\to\pi_*\mathcal O_X\). The projection formula makes \(H^{\ell}(X,Q_j^\vee\otimes Q_k)\) a direct summand of its pullback cohomology. It follows that

\[
 \operatorname{Ext}^{\ell}(Q_j,Q_k)=0
 \quad(\ell\ne2,\ \alpha_j\ne\alpha_k).
 \tag{E813.13}
\]

In particular both Hom and \(\operatorname{Ext}^1\) vanish across unequal normalized first Chern classes. Riemann--Roch also identifies the remaining dimension:

\[
 \dim\operatorname{Ext}^2(Q_j,Q_k)
   =r_jr_k\int_X\frac{(\alpha_k-\alpha_j)^4}{24}>0.
 \tag{E813.14}
\]

The nonzero degree-two extensions are not being declared harmless for derived constructions. They remain outside this coherent extension argument.

## 4. Iterated extensions split into actual slope-class summands

Let \(\mathcal C_\beta\) denote the class of bundles admitting a finite filtration by projectively flat stable factors of normalized first Chern class \(\beta\), among the factors in question and their translation/tensor images. The factor argument above works for all such images: they have the same normalized class and signature of any unequal difference.

For \(A\in\mathcal C_\beta\), \(B\in\mathcal C_\gamma\), with \(\beta\ne\gamma\), induction along their filtrations using the long exact Hom and Ext sequences gives

\[
 \operatorname{Hom}(A,B)=0,
 \qquad \operatorname{Ext}^1(A,B)=0.
 \tag{E813.15}
\]

Here is the precise induction for the extension assertion. For a short exact filtration step \(0\to B'\to B\to B''\to0\), the relevant sequence has \(\operatorname{Ext}^1(A,B')\) on the left of \(\operatorname{Ext}^1(A,B)\) and \(\operatorname{Ext}^1(A,B'')\) on its right. Vanishing of both outer terms forces the middle one to vanish, regardless of any subsequent \(\operatorname{Ext}^2\). Induction in the first argument uses the analogous contravariant long exact sequence. Hom is treated the same way. Thus no unproved assertion about an abelian category of all slope-semistable bundles is needed.

We now induct along (E813.1). Suppose its preceding term has already split by the distinct classes \(\beta\), and that the next quotient has class \(\gamma\). The extension class lies in the direct sum of the groups \(\operatorname{Ext}^1(Q, E_\beta)\). Equation (E813.15) makes all summands except \(\beta=\gamma\) zero. Therefore the new term is an extension entirely in the \(\gamma\)-block, direct-summed with all unchanged other blocks. This proves an actual decomposition

\[
 E=\bigoplus_\beta E_\beta,
 \qquad E_\beta\in\mathcal C_\beta,
 \qquad \operatorname{ch}(E_\beta)=r_\beta e^\beta,
 \quad r_\beta>0.
 \tag{E813.16}
\]

The decomposition is canonical in the sense needed here. Any morphism from an object in \(\mathcal C_\beta\) to \(E\) has zero projection to each \(E_\gamma\), \(\gamma\ne\beta\), by (E813.15). Thus it factors through \(E_\beta\). This characterization makes the summand independent of any splitting choices in the induction.

Translation and tensoring by a line bundle in \(\operatorname{Pic}^0\) preserve stability, the given slope, projective flatness and the normalized first Chern class. In particular they carry \(E_\beta\) into \(\mathcal C_\beta\). Every specified equivariant isomorphism \(t_x^*E\otimes P\simeq E\) therefore preserves each summand (E813.16), by the preceding Hom characterization and its inverse. The linearizations and their coherence restrict. Consequently (E813.16) is an actual decomposition in the given equivariant category on \(X\), not merely after an isogeny.

## 5. The invariant trace contradiction

If \(E\) were weakly \(G\)-semiregular, supplied DEG_L S-21 and invariant Calabi--Yau adjunction would make the trace image equal the degree-two cap image of the entire character. The trace of each actual equivariant summand in (E813.16) is contained in that image. Applying the same \(B\)-field shear to all characters, one obtains

\[
 \operatorname{im}c^2_{r_\beta e^{B+\beta}}
       \subset\operatorname{im}c^2_v,
 \qquad
 v=\left(1-\frac q2\theta_1^2\right)
   \left(1-\frac q2\theta_2^2\right).
 \tag{E813.17}
\]

SF-E801.5 and the full proof in SF-E812 identify the common annihilator of \(\ker c^2_v\) with the one-dimensional line spanned by \(v\). Perfect exterior pairing turns the image inclusion (E813.17) into the corresponding kernel inclusion. It follows that \(r_\beta e^{B+\beta}\) is proportional to \(v\). This is impossible: the cap rank of a nonzero pure exponential on a fourfold is six, while the balanced character has cap rank eighteen. This proves SF-E813.

## Exact input and scope

The only new published input beyond SF-E811--E812 is Mumford's line-bundle vanishing/index theorem. The primary book scan was retrieved from

<https://wstein.org/edu/Fall2003/252/references/mumford-abvar/Mumford-Abelian_Varieties.pdf>.

The printed pages 150--153 and 162--163 were visually checked; the intervening index proof pp.154--162 was also OCR-read, but this is not claimed as an independent audit of every step or of the book's earlier dependencies. The theorem is a published input. Sug Woo Shin, *Abelian varieties and Weil representations*, Algebra & Number Theory6(8)(2012),1719--1772, DOI10.2140/ant.2012.6.1719, Lemma2.4 printed p.1727, independently confirms the exact nondegenerate vanishing theorem and cites Mumford §16; that publisher PDF and lemma were opened. No preprint theorem is imported.

SF-E813 excludes finite equivariant semiregular repairs by nontrivial coherent extensions of the projectively flat stable factors just described, including the actual CM polystable examples. It leaves open semistable sheaves with singular stable factors, unstable bundles, twisted sheaves, and genuinely derived gluings using the nonzero degree-two Ext groups. The explicit surviving degree-two groups in (E813.14) explain why this proof does not assert a no-go result for all perfect complexes.
