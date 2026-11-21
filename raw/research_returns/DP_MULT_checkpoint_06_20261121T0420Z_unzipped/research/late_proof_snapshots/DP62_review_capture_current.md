# DP62 — canonical norms and integral normalization of individual theta translates

Date: 2026-11-21 UTC. Author: `/root/formal_bound`, GPT-6 Astra Pro; reasoning effort not exposed. The parent reserved DP62. The new content is the explicit normalization, its integral descent at level primes, and the resulting exact bounds for the particular family in DP59. Classical theta-group and canonical-metric facts are cited with exact primary locators. No Lean execution or machine formalization is claimed.

## 1. Statement and fixed geometric data

Put \(E=\mathbf Q(\zeta_7)\) and \(S=\operatorname{Spec}\mathcal O_E[1/14]\). Use the good Jacobian scheme \(A/S\), its principal polarization, and its symmetric rigidified trace-one line \(L\) from DP49 and DP59. Fix once and for all a section

\[
0\ne s\in H^0(A,L)
\tag{TN1}
\]

which is primitive at the selected prime over 11. Such a section can be chosen over this ring: start with the primitive local section in DP59 and clear its finitely many global denominators by a scalar outside that prime, as in DP60. The scalar and resulting section are fixed independently of the level.

Let \(M\ge1\) be odd, set \(N=M^2\), and use the canonical rigidified multiplication isomorphism

\[
\Phi_M:[M]^*L\xrightarrow{\sim}L^N.
\tag{TN2}
\]

The actual Poincaré construction of \(L\) makes (TN2) and its normalized symmetry integral over \(S\), as proved in DP59 §3. Let \(F/E\) be a finite extension and let \(t\in A[N](F)\).

**DP62(a): no-root integral lift.** The symmetric theta lift \(U_t\) satisfying

\[
U_t^N=1,\qquad \iota(U_t)=U_t^{-1}
\tag{TN3}
\]

is unique, is defined over the field of definition of \(t\), and extends integrally over \(\mathcal O_F[1/14]\). This includes places dividing \(M\). No root extraction or further extension is needed to normalize the lift. Explicitly, for any local theta lift \(U\), put

\[
c=\iota(U)U,\qquad d=U^N,
\qquad
\boxed{U_t=\frac{c^{(N-1)/2}}{d}\,U.}
\tag{TN4}
\]

Here \(c,d\) are invertible scalars on the local base. The formula is independent of \(U\) and glues over its multiplicative-group torsor.

**DP62(b): good-prime integrality.** The individual translated section

\[
s_t=U_t\bigl(\Phi_M([M]^*s)\bigr)
\tag{TN5}
\]

belongs to \(H^0(A_{\mathcal O_F[1/14]},L^N)\). Thus it has no new prime denominators at any good-model prime, including primes dividing the level. This is an assertion about each individual allowed section, not only a linear combination.

**DP62(c): exact canonical norm.** At every complex embedding equip \(L\) with its canonical smooth Hermitian metric: its curvature is translation-invariant and its rigidification at zero has norm one. Equip \(L^N\) with the tensor-power metric. Then

\[
\boxed{\|s_t\|_{\sigma,\sup}=\|s\|_{\sigma|_E,\sup}}
\tag{TN6}
\]

for every embedding \(\sigma:F\hookrightarrow\mathbf C\). The right side is one of finitely many fixed positive constants. The same equality holds for \(L^r\)-norms, \(1\le r<\infty\), with probability Haar measure on the complex abelian variety.

In particular the individual sharp translates and sharp pairs obtained in DP59 have uniformly bounded canonical section sup norms, and are integral at every good-model prime. Their tensor levels remain \(M^2=O(n^2)\), with \(M=29^e=O(n)\); this theorem does not replace that level statement by a bound for the complete lifting construction.

**DP62(d): field degree.** For the permitted subgroup \(H=A[\alpha^2]\) of DP59, which is defined over \(E\) and has degree \(M^{2g}\), any fixed \(r\)-tuple \(t_1,\ldots,t_r\in H(\overline E)\) and all its canonical lifts and translated sections are defined over a field of degree at most

\[
[E(t_1,\ldots,t_r):E]\le M^{2gr}.
\tag{TN7}
\]

For \(g=3\), the ordinary and two-copy harmonic witnesses therefore require degrees at most \(M^6\) and \(M^{12}\), respectively. Their logarithms are \(O(\log M)\). There is no discriminant bound in this statement.

## 2. The relative theta group at every good prime

We use theta groups over schemes, rather than only their geometric points. For a symmetric rigidified relatively ample line \(\mathcal N\) on an abelian scheme, the theta group is the central extension

\[
1\longrightarrow\mathbf G_m\longrightarrow
\mathcal G(\mathcal N)\longrightarrow K(\mathcal N)
\longrightarrow1,
\tag{TN8}
\]

where \(K(\mathcal N)=\ker(\phi_{\mathcal N})\). Its fibre over a point is the torsor of translation isomorphisms of the line. The exact relative statement, including finite flat kernels rather than only étale ones, is stated in A. Polishchuk, *Analogue of Weil representation for abelian schemes*, §1, author preprint pp.4–5, immediately before Lemma 1.1. Proposition 1.2 and Corollary 1.3 there also give the known triviality of the underlying torsor in the odd symmetric case. We use (TN4) to make the normalization and its base-change behaviour explicit. Primary author preprint: https://arxiv.org/pdf/alg-geom/9712021 .

For \(\mathcal N=L^N\), the principal polarization gives

\[
\phi_{L^N}=N\phi_L,
\qquad K(L^N)=A[N]
\tag{TN9}
\]

as group schemes over \(S\). The kernel is finite locally free, even at residue characteristics dividing \(N\). Here is the precise use of known results: on every field fibre multiplication by \(N\) is finite locally free of degree \(N^{2g}\), by Stacks Project Lemma 39.9.8, Tag 0BFG. The source is smooth, hence flat and locally of finite presentation over \(S\), and the target is locally of finite type. The fibrewise flatness criterion, Lemma 37.16.4, Tag 039E, makes the relative multiplication map flat. It is proper with finite fibres, hence finite by Lemma 37.44.1, Tag 02LS. Over our noetherian base it is therefore finite locally free; its rank is \(N^{2g}\), read on fibres. Its kernel is the base change along zero. None of these statements assumes \(N\) invertible.

The normalized symmetry of \(L^N\) induces the automorphism \(\iota\) of (TN8). It is the identity on the central \(\mathbf G_m\) and covers \(t\mapsto-t\). Its square is the identity, since the symmetry is normalized at zero. These are precisely the symmetric Heisenberg-group conventions in Polishchuk §1. A torsor fibre admits lifts locally in the fppf topology; no global choice or étale triviality is being assumed.

## 3. The explicit normalization and its descent

Work over an arbitrary test scheme \(T\to S\) with \(t\in A[N](T)\), and take a lift \(U\) after a torsor-trivializing cover. Because \(Nt=0\), its \(N\)-th power lies over zero and is an invertible central scalar \(d\). Likewise \(c=\iota(U)U\) is central. In particular

\[
\iota(U)=cU^{-1},
\]

so \(\iota(U)\) and \(U\) commute. Applying \(\iota\) to \(U^N=d\) and using that it fixes scalars gives

\[
c^N=\iota(U)^N U^N=d^2.
\tag{TN10}
\]

Put \(a=c^{(N-1)/2}d^{-1}\). Since \(N\) is odd, this is an integral expression in units with integer exponents. From (TN10),

\[
a^2c=c^Nd^{-2}=1,
\qquad
a^Nd=
c^{N(N-1)/2}d^{1-N}
=(d^2)^{(N-1)/2}d^{1-N}=1.
\tag{TN11}
\]

Therefore \(U_t=aU\) satisfies (TN3).

Suppose a different local lift is \(U'=uU\), where \(u\) is an arbitrary invertible base scalar. Since \(\iota\) fixes the center,

\[
c'=u^2c,\qquad d'=u^Nd,
\qquad a'=u^{N-1-N}a=u^{-1}a.
\tag{TN12}
\]

Thus \(a'U'=aU\). The normalized local sections agree on every overlap and descend to the original base. The construction is functorial under arbitrary base change. If two normalized lifts differ by \(u\), their power and symmetry conditions imply \(u^N=u^2=1\); an integer Bézout identity for \(N\) and 2 gives \(u=1\). This argument also works over nonreduced rings: it does not replace group-scheme equations by a statement only about geometric points.

This proves (a) for any \(S\)-valued torsion point. In particular the underlying torsor is canonically trivialized in this normalization. The resulting map \(A[N]\to\mathcal G(L^N)\) is **not asserted to be a group homomorphism** on the whole kernel. On an isotropic subgroup, its normalized lifts commute and their products satisfy (TN3); uniqueness then makes that restriction a homomorphism. The possible nontrivial theta commutator is retained.

The source interface is exact: `ThetaPt.lean` lines44–51 defines `SymLift` by the prescribed point, the power identity, and compatibility with a symmetry. The normalized symmetry and (TN3) supply those clauses. Its `IsActOf` definition at lines83–84 is the associated action on sections. These source definitions were read directly; no Lean proof execution is claimed.

## 4. Algebraic points and global good-prime integrality

Let \(F/E\) contain a torsion point \(t\). Properness of the abelian scheme extends the point uniquely over each DVR \(\mathcal O_{F,v}\) with \(v\nmid14\). More precisely, Stacks Project Lemma29.43.5, Tag0BX7, extends the rational map to a neighborhood of each such point because the source is noetherian and its local ring is a valuation ring. The valuative criterion is Lemma29.43.1, Tag0BX5. These neighborhood extensions agree on overlaps by separatedness and the dense common generic fibre. They therefore glue to a section over \(S_F=\operatorname{Spec}\mathcal O_F[1/14]\). This supplies the usual valuative extension over the regular Dedekind base with its neighborhood-gluing justification.

The relation \(Nt=0\) extends as well, since the abelian scheme is separated. Thus \(t\) is an \(S_F\)-point of the finite flat kernel in (TN9), including at places dividing \(N\). Apply (TN4) to its theta torsor over \(S_F\). The local factors \(c,d\) are units, their inverses remain integral units, and the normalized lift glues. In particular a field of definition for the point is already a field of definition for the lift. There is no additional field needed for square roots or \(N\)-th roots.

The pullback of the fixed section \(s\) by the integral morphism \([M]\) is an integral section of \([M]^*L\). The isomorphism (TN2) is integral, and \(U_t\) is an integral translation isomorphism of \(L^N\). Applying these operations gives (TN5) integrally over \(S_F\). This proves (b).

In the DP59 setting \(M=29^e\), so the assertion specifically includes places over 29. It does not rely on the kernel being étale there. At the selected place over 11, the torsion is still finite étale; its field completions are unramified, as already used in DP59. The new normalization requires no further local extension. This preserves the integer valuation group needed for the exact individual-witness argument in DP59 §7.

No assertion of primitivity at every good prime is needed: the fixed base section can vanish modulo another prime. The conclusion is integrality everywhere on the good model and the already chosen primitivity at 11.

## 5. Canonical metrics and multiplication isometries

The exact known metric input is the existence and uniqueness of the smooth Hermitian metric on a rigidified ample complex line bundle over an abelian variety whose rigidification is an isometry and whose curvature is translation-invariant. The original primary statement is Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque129 (1985), Proposition II.2.1, printed p.48; the original page was recovered and visually read after the initial saved-proof review. It also gives the equivalent cubical-metric characterization. The same statement was directly read in R. de Jong and F. Shokrieh, *Faltings height and Néron–Tate height of a theta divisor*, Compositio Mathematica 158 (2022), §12.2. The metric theorem is used as a known result, not re-proved here.

Fix an embedding into \(\mathbf C\) and write \(\omega\) for this curvature form of \(L\). Translation invariance implies

\[
[M]^*\omega=M^2\omega=N\omega,
\tag{TN13}
\]

because the differential of multiplication by \(M\) multiplies tangent vectors by \(M\). Thus the pullback metric on \([M]^*L\) and the tensor metric on \(L^N\), compared by \(\Phi_M\), have the same curvature.

Their logarithmic norm ratio is a smooth real pluriharmonic function on the compact connected complex torus, hence is constant. The isomorphism is rigidified at zero, and both rigidifications have norm one, so that constant is zero. Consequently \(\Phi_M\) is an isometry. Pointwise,

\[
\|\Phi_M([M]^*s)(x)\|=\|s([M]x)\|.
\tag{TN14}
\]

Surjectivity of multiplication on the complex torus yields equality of the two sup norms. No numerical period normalization or coefficient choice for a theta function is involved.

## 6. Finite-order theta lifts are isometric

Let \(U\) be any theta lift over \(t\in A[N](\mathbf C)\) satisfying \(U^N=1\). The metric comparison between \(L^N\) and its translate under \(U\) again has zero curvature, since

\[
T_t^*(N\omega)=N\omega.
\]

Therefore its positive norm ratio is a constant \(r_U>0\), independent of the point of the abelian variety. Composing the lift \(N\) times multiplies these constant ratios, so its \(N\)-th power has ratio \(r_U^N\). But \(U^N\) is the identity, whose ratio is one. Hence \(r_U=1\).

This proves that every normalized \(U_t\) from §3 is isometric. Translation is a bijection, so it preserves the section sup norm. Combining with (TN14) proves (TN6). The source action can be expressed using either inverse convention for a line isomorphism; an isometry remains an isometry under inversion, so the conclusion is independent of that convention.

For finite \(r\), probability Haar measure is invariant under translation and its pushforward by the surjective compact-group endomorphism \([M]\) is again probability Haar measure. Integrating (TN14) and then applying the theta-translation isometry gives the asserted \(L^r\) equalities as well.

Every embedding \(F\hookrightarrow\mathbf C\) restricts to an embedding of the fixed field \(E\). The right side of (TN6) is therefore bounded by the maximum of the finitely many norms of the fixed \(s\), independently of \(M\), \(F\), or the particular torsion point.

## 7. Degrees of fields containing the actual witness tuples

For DP59, the endomorphism \(\alpha\) is defined over \(E\), so \(H=A[\alpha^2]\) is a finite \(E\)-group scheme stable under the absolute Galois group. Its degree is \(M^{2g}\), and over characteristic zero it is étale. A point \(t\in H(\overline E)\) therefore has a Galois orbit of size at most \(M^{2g}\), which is its separable residue-field degree. The product \(H^r\) has degree \(M^{2gr}\), yielding (TN7) for any tuple.

The lift construction is functorial and unique, so the lift and translated section descend to this same tuple field. This is a bound for the field needed by the actual ordinary or harmonic tuple, not for a field splitting all torsion simultaneously. If one instead chooses the full torsion field, the elementary injection

\[
\operatorname{Gal}(E(A[N])/E)
\hookrightarrow\operatorname{GL}_{2g}(\mathbf Z/N\mathbf Z)
\]

gives the cruder bound \([E(A[N]):E]\le N^{4g^2}=M^{8g^2}\). Both bounds are polynomial in \(M\), but neither estimates discriminants, regulators, or a geometry-dependent coefficient field in a separate construction.

## 8. Scope of the cost conclusion

DP59 already supplies sharp ordinary individual translates and sharp two-copy tuples at \(M=O(n)\). This theorem adds a fixed canonical sup-norm for each member and good-prime integrality over its actual number field, together with the degree bounds above. A two-copy product has the product of two fixed norm bounds; it does not carry the interpolation coefficients of an arbitrary section-space construction.

These are bounds for the canonical section norms. A local source coefficient function obtained by dividing by a frame or multiplying by a holomorphic exponential gauge may acquire a factor depending on \(M^2\). A fixed analytic chart and fixed gauge give the comparison discussed in DP60, but this theorem does not identify the complete source archimedean derivative norm or its factorial/Gamma normalization with the canonical sup norm. It also gives no bad-prime norm or discriminant estimate and does not construct the prescribed iterated theta image, mixed-type moduli object, or the full row-degree sequence.

Thus an uncontrolled canonical section norm or a new good-prime denominator is no longer an obstruction for these individual allowed witnesses. A net shortening of a full theta-lift chain still requires the specific remaining global comparisons; no inequality for the entire chain is inferred from (TN6) alone.

## 9. Exact source locators and review record

- Relative theta group and symmetry: A. Polishchuk, *Analogue of Weil representation for abelian schemes*, author preprint arXiv:alg-geom/9712021, §1, pp.4–5, definition before Lemma1.1, Proposition1.2 and Corollary1.3; https://arxiv.org/pdf/alg-geom/9712021 . The directly read source is the author preprint; publication details do not substitute for reading a different version.
- Multiplication on fibres: Stacks Project Lemma39.9.8, Tag0BFG, https://stacks.math.columbia.edu/tag/0BFG . Relative flatness: Lemma37.16.4, Tag039E, https://stacks.math.columbia.edu/tag/039E . Proper finite-fibre criterion: Lemma37.44.1, Tag02LS, https://stacks.math.columbia.edu/tag/02LS . All three exact statements were directly opened and read during this proof.
- Canonical complex metric: Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque129 (1985), PropositionII.2.1, printed p.48 (PDF page51), https://www.numdam.org/item/AST_1985__129__1_0.pdf . The original page was visually read; local PDF and page PNG are in `research/theta_norm_sources`. Also directly read: de Jong–Shokrieh, Compositio Mathematica158 (2022), §12.2, DOI10.1112/S0010437X21007661; https://www.cambridge.org/core/journals/compositio-mathematica/article/faltings-height-and-nerontate-height-of-a-theta-divisor/EEEA4CD22A6248EAC82F11C339C6F6F1 .
- Exact source interface: `research/external_lean/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/ThetaPt.lean`, `SymLift`44–51 and `IsActOf`83–84, directly read in numbered form. DP59 identifies the multiplication and permitted-root clauses.

Actual saved whole-proof reading events, source metadata and exact hashes are recorded separately. This memo makes no claim of numerical testing, Lean execution, TeX compilation or machine formalization.
