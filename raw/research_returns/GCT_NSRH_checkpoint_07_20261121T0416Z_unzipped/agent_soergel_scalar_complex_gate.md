# F59 continuation: changing the scalar coefficient complex

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited effort is not exposed. Date: 2026-11-21 UTC.

## 1. Question and exact category

The strongest F59 theorem excludes every bounded ordinary type-A Soergel lift of the actual generator class with the original cohomologically degree-zero scalar coefficient object. This note tests a strictly larger premise: replace that coefficient by an arbitrary bounded complex of finite graded scalar vector spaces with the same Euler class.

Let k have characteristic zero, let n be at least two, and let A be the standard degree-two polynomial realization for W=S_n times S_n. Fix the same simple reflection s in both factors and put tau=(s,s). Write delta=v+v^-1. Let X be a bounded complex of ordinary Soergel bimodules with

\[
 [X]=P_s=b_s\otimes b_s+(b_s-\delta)\otimes(b_s-\delta).
 \tag{SC1}
\]

Let C be a bounded complex of finite Z-graded k-vector spaces, with

\[
 \sum_{j,e}(-1)^j\dim_k H^j(C)_e\,v^e=\delta^2.
 \tag{SC2}
\]

The changed scalar coefficient object is C tensor_k A, with its ordinary central unit-bimodule action. Test an actual isomorphism

\[
 X\otimes_A^{\mathbf L}X\simeq C\otimes_k X.
 \tag{SC3}
\]

A homotopy quadratic in the ordinary bounded Soergel category implies (SC3), so a necessary condition for (SC3) is also necessary for that stronger lifting task. All conclusions below assume an actual isomorphism, not merely its Euler identity.

The word **scalar** is essential. A bounded complex of sums of unit bimodules whose differential contains nonconstant polynomials of A need not come from a complex of k-vector spaces. Such objects are not included in C. Neither are arbitrary central sheaf complexes, changes of the ambient K0 comparison, or unbounded completions.

## 2. Positive generic cohomology must be uniform on two graphs

### Proposition SC-A

Under (SC1)-(SC3), let Q be the ungraded fraction field of A. After generic graph localization, the cohomology of X is supported only on the identity and tau graphs. In every cohomological degree j their multiplicities are equal. More precisely, with

\[
 d(u)=\sum_j \dim_k H^j(C)\,u^j,
 \tag{SC4}
\]

the generic cohomology character is

\[
 F(u)=\frac{d(u)}2(e+\tau).
 \tag{SC5}
\]

In particular every coefficient of d(u) is even.

**Proof.** Ordinary generic Soergel localization is the semisimple category of finite sums of graph bimodules Q_g, with Q_g tensor_Q Q_h equal to Q_gh and no maps between distinct graphs. The original contexts used in F59 are Elias--Williamson, *Localized calculus for the Hecke category*, Section 1.1, equations (1.1)-(1.2), Section 1.2, Theorem 1.6 and Remark 1.7; the ordinary bimodule input is separately fixed in the F59 core.

We deliberately forget internal grading at this step. Write

\[
 F(u)=\sum_{g\in W}f_g(u)g,
 \qquad f_g(u)\in\mathbb N[u,u^{-1}],
 \tag{SC6}
\]

for the actual generic cohomological multiplicities. Kunneth over Q and (SC3) give the group-ring identity

\[
 F(u)^2=d(u)F(u).
 \tag{SC7}
\]

The class (SC1), with internal shifts forgotten, gives

\[
 F(-1)=2e+2\tau,\qquad d(-1)=4.
 \tag{SC8}
\]

Indeed b_s localizes to e+s, while b_s-delta localizes to s-e; their displayed two-factor sum is 2(e+tau).

Put a(u)=sum_g f_g(u). Augmentation of (SC7) gives a(u)^2=d(u)a(u). Since a is nonzero and Z[u,u^-1] is a domain, a=d. For every real u>0, the coefficients

\[
 \mu_u(g)=f_g(u)/d(u)
\]

form a nonnegative probability measure on the finite group W, and (SC7) says mu_u*mu_u=mu_u. Its support S is independent of u, because a nonzero Laurent polynomial with nonnegative coefficients is positive on the positive real axis.

For completeness, an idempotent probability measure on a finite group is uniform on a subgroup. Positivity gives S squared equals S. A nonempty finite subsemigroup of a group contains the identity and inverses, hence is a subgroup. Choose g_0 in S maximizing mu(g). Then

\[
 \mu(g_0)=\sum_{x\in S}\mu(x)\mu(x^{-1}g_0)
\]

is a weighted average of numbers at most mu(g_0), with every weight positive. Equality forces every mu(x^-1 g_0) to be this same maximum. These elements run through S, so the measure is uniform.

Thus f_g(u)=d(u)/|S| on S and zero elsewhere, for every real u>0. Laurent-polynomial identity then gives this equality identically. Evaluate at u=-1 and use (SC8): the coefficient of the identity is 2, so |S|=2, and the other element is tau. This proves (SC5) and coefficientwise evenness. No classification of arbitrary virtual measures is used. QED.

**Internal-grading warning.** This proposition does not assert that each full formal-degree multiplicity of C is even. Generic localization inverts homogeneous polynomials; in particular a degree-two unit identifies internal shifts differing by two. Forgetting internal grading is explicit in (SC6). It would be invalid to replace d(u) here by the entire two-variable graded polynomial and infer an immediate contradiction from the odd outer coefficients of delta squared.

## 3. A scalar repair must have nonflat cohomology

### Proposition SC-B

There is no X,C satisfying (SC1)-(SC3) for which every H^j(X) is graded flat as a left A-module. Equivalently in this finite graded setting, no such solution has all its cohomology graded left-projective or graded left-free. Consequently any scalar-complex repair must contain at least one nonflat cohomology bimodule.

**Proof.** Finite graded flat modules over this noetherian polynomial ring are finite graded projective, hence graded free. The last implication follows by lifting a homogeneous residue basis, splitting its graded free surjection, and applying graded Nakayama to the complementary kernel, as explicitly used in the strongest F59 proof.

By SC-A each H^j(X) has generic graph support only e and tau. Choose root coordinates x,y reversed independently by tau and fixed coordinates z. Let U,V be the matrices of right multiplication by x,y on a graded left-free cohomology module. Generically, the two possible graph actions give

\[
 yU=xV,\qquad U^2=x^2I.
 \tag{SC9}
\]

Left freeness extends these identities to A. Since x and y are coprime polynomial variables, entrywise divisibility gives U=xZ, V=yZ for a homogeneous degree-zero matrix Z over A, and Z squared is I. Right multiplication by every fixed coordinate equals its left scalar, first generically and then globally by torsion-freeness.

The bimodule idempotents (I+Z)/2 and (I-Z)/2 split the cohomology into the e and tau graph pieces. Their images are graded left-projective, therefore graded free. In particular they are also right-free. Thus there are finite Laurent polynomials with actual nonnegative multiplicities

\[
 a(v,u),b(v,u)\in\mathbb N[v,v^{-1},u,u^{-1}]
\]

such that the full, globally defined graded cohomology character is

\[
 H_X(v,u)=a(v,u)e+b(v,u)\tau.
 \tag{SC10}
\]

Here u records the actual cohomological degree and v the global internal shifts. The polynomial b is nonzero by (SC8). The full grading is legitimate now because it records actual globally free graph summands, not localized shifts.

Since all H^j(X) are right-free, the canonical cross-product Kunneth map

\[
 \bigoplus_{i+j=r}H^i(X)\otimes_A H^j(X)
 \longrightarrow H^r(X\otimes_A^{\mathbf L}X)
 \tag{SC11}
\]

is an isomorphism of graded bimodules. One direct verification is to split the bounded complex X as a complex of right A-modules into its projective cohomology and contractible pairs, and then tensor with the second complex. Those splittings are only right-module splittings; they are used to prove that the canonical cross-product map is bijective. The cross-product map itself is bimodule-linear, so the resulting isomorphism is a bimodule statement. No bimodule formality is inferred from the one-sided splitting.

Set

\[
 d(v,u)=\sum_{j,e}\dim_kH^j(C)_e\,v^e u^j.
\]

Scalar Kunneth and (SC3), followed by comparison of the actual graph multiplicities, yield

\[
 a^2+b^2=da,\qquad 2ab=db.
 \tag{SC12}
\]

Graph multiplicities can be compared separately: a map between the two distinct graph types would have its coefficient killed by 2x in the polynomial domain and is therefore zero. The coefficient ring Z[v,v^-1,u,u^-1] is an integral domain, and b is nonzero, so the second equation gives d=2a. Taking the cohomological Euler specialization u=-1 now gives

\[
 v^2+2+v^{-2}=2a(v,-1),
 \tag{SC13}
\]

which is impossible in the integral Laurent ring. The coefficients of v^2 and v^-2 on the left are odd. This proves the proposition. QED.

This proof restores the global grading only after the flatness hypothesis has supplied actual graph summands. It therefore does not contain the localization mistake excluded after SC-A.

## 4. Both previously explicit candidates still fail

### Corollary SC-C: the coupled Rouquier Euler lift

The actual coupled Rouquier object from the F59 core has derived image

\[
 X_{\mathrm R}\simeq A^{\oplus2}\oplus A_\tau(-2)\oplus A_\tau(2),
 \tag{SC14}
\]

concentrated in degree zero. It has the ambient Euler class (SC1), but no bounded scalar C satisfying (SC2) can make it satisfy (SC3).

Indeed the left-hand side of (SC3) is concentrated in degree zero. On the right, H^j(C) tensor_k X_R is nonzero whenever H^j(C) is nonzero. Thus C has cohomology only in degree zero. Its graded Euler class forces H^0(C) to be the original scalar object with character delta squared. The identity-graph character of X_R squared is

\[
 v^4+6+v^{-4},
\]

whereas that of delta squared times X_R is

\[
 2v^2+4+2v^{-2}.
\]

They differ. This is also an immediate application of SC-B, but the explicit computation shows that arbitrary scalar cohomological shifts cannot repair the original candidate.

### Corollary SC-D: the actual unit-cone direct-sum lift

Let C_s be the actual unit-dot cone from the F59 core, whose derived image is R_s(1) direct sum R(1)[1]. For

\[
 X_{\mathrm{dot}}=(B_s\boxtimes B_s)\oplus(C_s\boxtimes C_s),
\]

the ungraded generic cohomological character, with z denoting a shift [1] (cohomological degree -1), is

\[
 F(z)=(1+z^2)e+(1+z)(s_1+s_2)+2\tau.
 \tag{SC15}
\]

This cannot satisfy F squared=dF for any scalar Laurent polynomial d, even before imposing the Euler class (SC2). Evaluate on the three types of characters of the four-element group generated by s_1,s_2. The resulting nonzero polynomials are

\[
 z^2+2z+5,\qquad z^2-1,\qquad (z-1)^2.
 \tag{SC16}
\]

For each nonzero character value f, the equation f squared=df in the Laurent polynomial domain forces d=f. The three displayed polynomials differ, a contradiction. Equivalently, SC-A's positive-support argument already excludes the extra s_1,s_2 generic cohomology. This explicit Fourier calculation does not rely on retaining the lost internal grading.

## 5. What the finite-Frobenius argument still says

For the central finite Frobenius quotient B of the strongest F59 proof, put Z=X/IX termwise. The quotient construction and the equality IM=MI for its central homogeneous generators remain valid. It carries (SC3), if originally given as a homotopy quadratic, to

\[
 Z\otimes_B Z\simeq C\otimes_k Z.
\]

The fiber has nonzero cohomology because its Euler k-dimension is dim_k(B) times the nonzero Euler left rank four. Let r and a be the upper cohomological degrees of Z and C. The same local nonvanishing argument gives upper degree 2r for the square, while scalar Kunneth gives a+r on the right. Hence r=a. Exact graded Frobenius duality gives the corresponding equality of lower degrees.

Thus the old amplitude proof matches the extremes of Z to those of C; it no longer forces either to degree zero. The earlier minimal-complex argument cannot simply be repeated without its projective concentrated fiber. This is the precise point where an arbitrary mixed scalar coefficient changes the proof.

These statements do not construct a solution with nonflat cohomology. The remaining case is an actual bounded coupled Soergel complex with nonflat cohomology and an altered scalar complex, satisfying actual quadratic maps and any required higher-rank relations. No such construction or unconditional exclusion is proved here.

## 6. Separate Grothendieck translation

The added scalar C is a finite perfect complex of graded vector spaces in the framework of SGA 6, I, Definition 4.7, pp. 121-122, and Example 4.8, p. 122. Its Euler class belongs to the ordinary coefficient Grothendieck group, but the proof needs its actual cohomological multiplicities as nonnegative integers. The split-torus grading uses SGA 3, I, 4.7.2-3 and cote 90, scan 17. SGA 6, V, Sections 2-3, with cote 133, scan 18, is a vocabulary anchor for symmetric coefficient operations; it does not supply a lambda-ring structure on the noncommutative Hecke word algebra.

The distinction between generic localized graph multiplicities and globally graded free summands is an affine module-and-base-change distinction. EGA I, Theorem 1.3.7, p. 86, Corollary 1.3.8, p. 87, and Theorem 1.4.1, pp. 90-92, give the affine module/sheaf framework. The localization, Kunneth and flatness implications used here are proved explicitly or inherited from the exact already checked ordinary-Hecke source; no general cohomology-and-base-change theorem is being invoked without hypotheses.

The generic uniform-measure lemma is included with its elementary proof and is not claimed as a new general result about finite groups. The new application is the precise necessary cohomological support and the flat-cohomology obstruction for the actual nonstandard generator class under an altered scalar coefficient. Neither this finite Frobenius-algebra argument nor its dictionary asserts an arithmetic Frobenius, a Weil weight, a positivity polarization, or a canonical basis.

## 7. Author verification and requested fresh check

The positive group-algebra identity, subgroup/uniformity argument, specialization at cohomological Euler degree, global graph splitting, canonical Kunneth justification, integral parity contradiction, both candidate tests and finite-fiber amplitude scope have been independently reconstructed within this note. No computation or formal proof assistant is used. The exact ordinary Soergel/localization/source normalization was checked in the F59 core and its independent review; no new primary theorem is attributed to the archive.

Fresh whole-proof review is requested before integrating this continuation. The ordinary bounded theorem with the original degree-zero coefficient remains frozen; this note does not change its statement.
