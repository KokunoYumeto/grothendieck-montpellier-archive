# Characteristic-zero top ordinary quotient: finite-jet audit

**Research window:** 19 November 2026, after checkpoint 14 at 13:20 UTC.
**Owner:** GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06 /root/frobenius; inherited effort setting not separately exposed.
**Status:** method analysis and an auxiliary first-jet obstruction. No unrestricted top-Chow theorem or counterexample is claimed. No new main-gate movement is claimed for this window.

The unresolved target is the rational ordinary quotient
\[
B^{N-1}(X)_{\mathbf Q},\qquad
X=\operatorname{Spec}R-\{\mathfrak m\},\quad N\geq3,
\]
in characteristic zero. Ordinary algebraic equivalence here uses differences of fibres on an **actual fixed product** with a smooth proper parameter curve. A class on a nilpotent thickening, a compatible system of Grothendieck-group classes, and a class on a henselized product do not by themselves supply that relation.

## 1. Current-window assessment

We completed the final metadata and six-page visual verification of C.3be, including its already approved nonhenselian refinement, before checkpoint 14. Its theorem concerns residue field \(\overline{\mathbf F}_p\), not the remaining characteristic-zero gate. The parent's full revised audit is dated 13:06:39 UTC, the peer's full revised audit 13:06:03 UTC, and the owner inspected all six rendered pages by 13:10:30.283980 UTC. Those events are retained in the C3_surface_reduction_Fpbar files and do not constitute new movement after the 13:20 checkpoint.

In the present window we:

1. isolated the fixed-representative gap in a proposed finite-stabilization argument;
2. proved the constant-curve \(K_2\) differential obstruction below, with a precise primary dlog source and an explicit first jet;
3. checked two concrete ways to extend the special Fermat-cover argument and identified why they fail;
4. independently checked a specific open-complement assertion in Patel–Ravindra and retained its exact counterexample, without making a claim about their main torsion theorem.

None of these steps constructs a surviving top ordinary Chow class or proves that all such classes are ordinarily algebraically trivial. The next useful step must address the actual cycle-family or trace construction, rather than rename the same lifting condition.

## 2. Fixed objects versus Grothendieck-group stabilization

Let \(E\) be smooth projective, let \(L\) be an ample conormal bundle, and let \(P\) be a smooth projective parameter curve. For a **fixed** vector bundle \(F_0\) on \(E\times P\), relative Serre vanishing over \(P\), followed by the fact that \(P\) has cohomological dimension one for coherent sheaves, gives
\[
H^2(E\times P,\operatorname{End}(F_0)\otimes L^n)=0
\quad(n\gg0).
\]
Thus the usual obstruction to extending a specified bundle through further square-zero thickenings eventually vanishes. The bound depends on \(F_0\).

This does not prove that a class in \(K_0(E_n\times P)\), or a stable compatible sequence of such classes, is represented by bundles with a fixed restriction \(F_0\). Equality in \(K_0\) on a projective scheme does not imply stable isomorphism of vector bundles. Choosing new representatives at increasingly deep levels can change the obstruction bound. Consequently eventual constancy of the relevant groups does not, on its own, produce an existing compatible system of coherent sheaves to which formal GAGA applies.

The neighboring source Ballico–Gasparim–Köppe (2009) has precisely the narrower scope needed to keep this distinction visible. Its Section 3 assumes the exceptional locus is a **curve**; Theorem 3.2, Lemmas 3.3–3.4 and Theorem 3.5 concern filtrability and algebraicity there. Remark 4.2 uses the obstruction groups for a fixed bundle, and Theorem 4.3 is a formal principle for an already existing formal locally free sheaf. The parent's full primary reading is recorded separately. In this owner pass the publisher's indexed primary text was read, while direct author-PDF retrieval returned HTTP 503; no independent successful full-PDF opening is claimed.

Bloch–Esnault–Kerz (2014), Theorem 1.2 and Remark 1.3, author p. 2, likewise distinguish compatible \(K_0\)-classes with a prescribed Chern class from exact prescribed classes. Their Conjecture 1.4 and displayed map (1.3), on the same page, explicitly leave an algebraization problem. Appendix B's existing non-surjectivity example uses unbounded differential complexity. It is not automatically a counterexample in the ample-conormal setting, where coherent groups can vanish in high order. Conversely, that eventual vanishing is not the missing uniform-object argument.

## 3. Auxiliary constant-curve \(K_2\) obstruction

### 3.1 Statement and scope

Let \(P/\mathbf C\) be a smooth projective connected curve and
\[
R=(\mathbf C[t]_{(t)})^h .
\]
For every actual class \(\xi\in K_2(P_R)\), its relative-\(\mathbf C\) logarithmic differential is zero:
\[
d\log_{/\mathbf C}(\xi)=0
\quad\text{in }H^0(P_R,\Omega^2_{P_R/\mathbf C}).
\tag{KJ.1}
\]
This is an assertion for the algebraic henselization, whose finite data descend to pointed étale neighborhoods. We do not assert it for every class over \(\mathbf C[[t]]\).

If \(P=E_{\mathbf C}\) for the fixed elliptic curve
\[
E:\ y^2=x^3-x
\quad\text{over }\overline{\mathbf Q},
\]
there is a relative first-jet class on
\(E_{\mathbf C[\epsilon]/(\epsilon^2)}\) whose differential has nonzero
\(d\epsilon\wedge(dx/y)\) component. It therefore cannot be the first-jet restriction of an actual class in \(K_2(E_R)\). This gives a specific obstruction to a proposed \(K_2\)-family lifting argument. It does **not** identify a nonzero class in the top ordinary Chow quotient.

### 3.2 Descent and the vertical residues

Any specified \(\xi\) descends to \(P\times U\), where \(U\) is a smooth connected pointed étale neighborhood of \(0\) in \(\mathbf A^1_{\mathbf C}\). This is the finite-data limit property of algebraic \(K\)-theory; the base change \(P_R\) is the corresponding filtered limit. Compactify \(U\) to a smooth projective curve \(\overline U\), and put
\[
S=P\times\overline U,\qquad
D=S-(P\times U)=\coprod_j(P\times\{u_j\}).
\]
The boundary components are disjoint smooth vertical curves.

The unramified \(K_2\) section associated with \(\xi\) has a logarithmic differential in
\[
H^0(S,\Omega^2_{S/\mathbf C}(\log D)).
\]
At a boundary component \(D_j\), the residue is the logarithmic differential of its tame symbol. The Quillen localization boundary is a class in \(K_1(D_j)\); its determinant is a global unit of \(D_j\simeq P\), hence a constant in \(\mathbf C^*\). The relative-\(\mathbf C\) dlog of that determinant vanishes.

Equivalently, the Gersten differential of the tame symbol at every closed point of \(D_j\) vanishes: all the nonvertical divisorial residues are already zero on \(P\times U\), and no other vertical component meets \(D_j\). The tame symbol is a rational function on the proper curve \(P\) with zero divisor, hence constant. This equivalent argument also explains why no unaccounted horizontal residue can appear.

All logarithmic residues are therefore zero. The logarithmic residue exact sequence gives an actual holomorphic two-form
\[
\alpha\in H^0(S,\Omega^2_{S/\mathbf C})
\]
whose restriction is \(d\log(\xi)\).

### 3.3 Rational Betti compatibility and the proper Hodge argument

Asakura (2006), introduction, equation (1.1), p. 1, states for a smooth complex variety with a smooth normal-crossing compactification the inclusion
\[
d\log\Gamma(U,\mathcal K_2)\otimes\mathbf Q
\subset
H^0(\overline U,\Omega^2_{\overline U}(\log D))
\cap H_B^2(U,\mathbf Q(2)).
\tag{KJ.2}
\]
Only this inclusion is used; the conjectural equality mentioned immediately afterward is not used. The downloaded arXiv v4 header is 6 April 2006. The complete page was independently read in text and in its rendered image.

Apply (KJ.2) to \(P\times U\). The de Rham class of \(\alpha\) restricts to a rational Betti class with the \((2\pi i)^2\) normalization. This normalization is real. Thus
\[
[\alpha]-\overline{[\alpha]}
\in
\ker\!\left(H^2(S,\mathbf C)\longrightarrow
H^2(P\times U,\mathbf C)\right).
\]
The kernel is generated by the classes of the boundary divisors, by the cohomology-with-supports/Gysin sequence. It is therefore of Hodge type \((1,1)\). But \([\alpha]\) has type \((2,0)\) and its conjugate has type \((0,2)\). The direct Hodge decomposition forces both to vanish. Finally, on the **proper smooth** surface \(S\), the map from holomorphic two-forms to de Rham cohomology is injective. Hence \(\alpha=0\) as a differential form.

This last properness step is essential. We have not inferred that an exact differential form on the nonproper \(P\times U\) vanishes. In particular, a form resembling \(dt\wedge\omega\) can be exact on an open surface and remain nonzero. The proof instead extends the form to \(S\) before invoking Hodge theory.

The sheaf \(\Omega^2_{P_R/\mathbf C}\) is locally free, and restriction to the generic point is injective. The descended vanishing therefore proves (KJ.1).

### 3.4 The explicit missed first jet

For the elliptic curve \(E/\overline{\mathbf Q}\), the absolute differential
\(\omega=dx/y\) is defined over \(\overline{\mathbf Q}\), so it supplies a global section of \(\Omega^1_{E_{\mathbf C}/\mathbf Q}\) whose relative-\(\mathbf C\) image is nonzero. This choice avoids an unjustified claim that every geometric form on an arbitrary complex curve lifts to a global absolute form.

Bloch–Esnault–Kerz, Lemma 2.2 and Proposition 2.3, author pp. 3–4, give the exact infinitesimal symbol map
\[
a\,d\log b\longmapsto \{1+\epsilon a,b\},
\qquad
d\log\{1+\epsilon a,b\}
=d\epsilon\wedge a\,d\log b+
\epsilon\,da\wedge d\log b .
\tag{KJ.3}
\]
For \(n=2,r=2\), their exact sequence identifies the relative Milnor \(K_2\) sheaf with the absolute one-form sheaf. Its Quillen version is the standard rational tangent-\(K_2\) identification already used and independently checked in C.3ab: Goodwillie's Main Theorem, p. 348, together with the explicit degree-one cyclic calculation. Thomason–Trobaugh, Theorem 10.3, pp. 383–386, gives the descent spectral sequence. On the one-dimensional underlying curve the edge map
\[
K_2(E_\epsilon,E)_{\mathbf Q}
\longrightarrow
H^0(E,\mathcal K_2(E_\epsilon,E))_{\mathbf Q}
\]
is surjective, since there is no coherent/Zariski cohomology in degree two. Thus a relative class \(\beta\) with edge \(\omega\) exists.

By (KJ.3), the \(d\epsilon\)-component of \(d\log_{/\mathbf C}(\beta)\) is
\[
d\epsilon\wedge\omega\ne0.
\]
If \(\beta\) came from \(K_2(E_R)_{\mathbf Q}\), naturality of dlog would contradict (KJ.1). If an absolute class is used, subtract its pullback from the special fibre first; this makes it relative without changing the indicated component.

This argument also gives the more elementary sheaf-level conclusion without any appeal to the global Quillen edge map: the explicit relative Milnor-\(K_2\) section corresponding to \(\omega\) cannot be the first jet of an unramified section arising on the actual henselian product.

### 3.5 Independent check and limitation

The parent independently checked the localization determinant and the proper Hodge argument in this research window. Its refinement was to formulate the Hodge step directly as \(\alpha-\overline\alpha\) lying in the divisor-generated \((1,1)\) kernel, as done above. The parent subsequently independently opened the actual v4 primary text through its CiteSeer mirror and read introduction p. 1, equation (1.1). This is a targeted proof and exact-source check; it is not an audit of the unrelated later theorems in Asakura's paper.

The first-jet obstruction does not transfer automatically to a top coherent trace on an exceptional surface. A proper pushforward of a \(K_0\)-family on a resolution need not produce an actual \(K_2\)-class on the constant curve product to which (KJ.1) applies. C.3au in fact constructs nonzero trace directions from a special product cover. Any proposed counterexample must prove the additional transfer, including its support and boundary terms.

## 4. Two concrete cover constructions that do not provide the missing trace

### 4.1 Making the base of a pencil have large genus

Suppose a resolved pencil gives \(\pi:V'\to\mathbf P^1\). A nonzero piece of
\(H^2(V',L)\) can arise from
\[
H^1(\mathbf P^1,R^1\pi_*L).
\]
On a negative splitting summand \(\mathcal O(a)\), \(a\leq-2\), take any finite map \(g:B\to\mathbf P^1\). Then \(g^*\mathcal O(a)\) still has negative degree and no global sections. The hoped-for new \(H^1\)-classes of \(g^*\pi_*L\) arising from the high-genus base cup with \(H^1(B,\mathcal O_B)\) into \(H^2(B,-)=0\). They do not generate the negative-summand target.

Thus increasing the genus of the pencil base alone does not extend the C.3au spanning argument. This statement does not exclude arbitrary finite covers of \(V\), additional irregularity not inherited from the base, or a different correspondence.

### 4.2 An ample pullback in a product of three curves

Consider a smooth quintic \(V\subset\mathbf P^3\), a smooth product \(A\) of three projective curves, a finite map \(f:A\to\mathbf P^3\), and a smooth pullback \(T=f^{-1}(V)\). Put \(M=f^*\mathcal O(1)\), so \(T\in|M^5|\). The exact sequence
\[
0\longrightarrow M^{-4}\longrightarrow M
\longrightarrow M|_T\longrightarrow0
\]
and Serre duality/Kodaira vanishing give \(H^2(A,M^{-4})=0\). The resulting \(H^1(T,M|_T)\) is inherited from \(H^1(A,M)\). Cupping with inherited \(H^1(T,\mathcal O_T)\) therefore lands in the image of \(H^2(A,M)\).

The trace-dual test form in \(H^0(V,K_V\otimes\mathcal O_V(-1))\) pulls back, after the Jacobian factor, to a section in
\(H^0(T,K_T\otimes M^{-1}|_T)\) that lifts from
\(H^0(A,K_A\otimes M^4)\). Its connecting class is zero. By duality, it annihilates the inherited \(H^2(A,M)\) image. Hence this particular ample-cover construction does not supply the required nonzero trace.

This is a calculation conditional on the stated smooth finite-cover setup. It is not a theorem that every irregular cover or every surface correspondence has zero trace.

## 5. Normalized-surface pushforward remains a separate gate

The dimension-two prime-quotient reduction used in C.3be still represents every top curve by a finite pushforward from a normalized local surface. In characteristic zero, however, the corresponding local divisor classes can have proper, toric and additive parts. Their finite pushforward into a higher-dimensional germ has not been shown to be ordinarily algebraically trivial. Codimension alone supplies no such relation.

The earlier SNC energy identity already eliminates the simplest degree-unit edge term. A coefficient \(K_2(k)\) symbol has an actual proper-curve evaluation relation on the exceptional object, but that does not lift the relation to the fixed regular resolution. Likewise a nonzero dual-complex class may have a nonzero negative-\(K\) connecting image, so KST does not automatically lift it. Multiplying a local Picard torus by the exceptional normal divisor produces a boundary-supported class, which vanishes on the puncture and cannot supply a counterexample.

The first-jet calculation in Section 3 now gives an explicit reason not to assume that every proper-parameter nilpotent \(K_2\) class algebraizes. It still does not decide whether the particular \(K_0\)-classes and top coherent traces required for ordinary Chow equivalence can be algebraized by another construction.

## 6. Source acquisition and exact scope ledger

The reproducible script code/acquire_charzero_lifting_sources.py ran from
13:35:38.256435 to 13:35:48.524824 UTC, wall time **10.268465583998477 seconds**.
The output is output/charzero_lifting_sources.json.

| Source | Exact portions used/read in this owner pass | Access and limitation |
|---|---|---|
| Asakura, arXiv:math/0511190v4, 6 April 2006 | Introduction, equation (1.1), p. 1, including the following sentence distinguishing the conjectural equality | Complete PDF downloaded HTTP 200, 621489 bytes, SHA-256 9ba4e8d55d44036368a35bab7e8447398445cdebd0a939dba3668b9cff61cf61. Full p. 1 read as text and image. No audit of unrelated later theorems is claimed. |
| Bloch–Esnault–Kerz, Deformation of algebraic cycle classes in characteristic zero | Theorem 1.2, Remark 1.3, Conjecture 1.4 and (1.3), p. 2; Lemmas 2.1–2.2 and Proposition 2.3, pp. 3–4 | Complete author PDF downloaded HTTP 200, 534774 bytes, SHA-256 ada21939a4f347f5627db3cce1aff08b4fea89b8779239c33d0bccaaec752381. These portions reread. Appendix B was checked in the earlier C3ad/top-quotient audit; no new full Appendix B reread claimed here. |
| Ballico–Gasparim–Köppe (2009), Local moduli of holomorphic bundles | Publisher-indexed Section 3, Theorem 3.2, Lemmas 3.3–3.4, Theorem 3.5; fixed-bundle obstruction paragraph and formal-principle scope | Indexed primary text read; direct author PDF failed HTTP 503. Parent separately reports a full primary reading. The curve hypothesis is retained. |
| Quillen (1973), Higher algebraic K-theory I | Section 7, Proposition 3.2 and (3.3), p. 127, plus Gersten Theorem 5.11, pp. 133–134 | Exact primary statements already opened in the prior field-K2 family audit; reused, not claimed freshly downloaded here. |
| Goodwillie (1986); Thomason–Trobaugh (1990) | Main Theorem p. 348; Theorem 10.3 pp. 383–386 | Exact tangent/descent inputs reused from the independently checked C.3ab proof. |
| Patel–Ravindra, Purdue author version | Theorem 2.6 and Corollary 2.7, author p. 6; complete Lemma 3.2 and proof, author p. 7 | Complete author PDF downloaded HTTP 200, 357911 bytes, SHA-256 f10f2109386de4258593798eb9192fd3ae3c8edb68426e4e1b7d7a895b451ad1. Published p. 562 exact lemma was additionally read through indexed primary text; full published download failed. Separate review below. |

No priority claim is made. No unproved lifting assertion is promoted to a numbered result.

## 7. Subsequent local-cycle literature check

We reopened the primary Dao–Kurano paper, *Hochster's theta pairing and numerical equivalence*, at https://www.isc.meiji.ac.jp/~kurano/ronbun/kurano32.pdf, and reread its Remark 6.4, author pp. 20–21, and the precise scope of its local numerical groups and Corollary 8.2. The bars distinguishing numerical quotients can be lost in extracted text. The paper proves that actual algebraic equivalence implies numerical equivalence; it does not identify the two relations. Its numerical vanishing and finiteness therefore do not settle the ordinary quotient here.

Its reference [3], Celikbas–Walker, *Hochster's theta pairing and Algebraic equivalence*, Mathematische Annalen 353(2) (2012), 359–372, was subsequently opened in full through https://arxiv.org/pdf/1011.4886 (v1, 22 November 2010). We read Theorem 2.7 and its proof, author pp. 4–6, and Definition 3.2/Corollary 3.3, p. 7. These prove constancy of theta in actual flat families and factorization through their algebraic-equivalence quotient. They do not assert that all top cycles are ordinarily algebraically trivial. No new conclusion about the target quotient follows.

## 8. A field-specific Kodaira–Spencer lead, with the fixed-product gate retained

The following is a research lead, not a certified new result. For a smooth quintic surface \(V\subset\mathbf P^3\), put \(L=\mathcal O_V(1)\). Then \(K_V=L\),
\[
H^2(V,L)\simeq k,\qquad H^2(V,L^j)=0\quad(j\ge2).
\]
The remaining \(j=1\) absolute-differential obstruction is the cokernel of
\[
H^1(V,\Omega^1_{V/K}\otimes L)
\longrightarrow
\Omega^1_{K/\mathbf Q}\otimes H^2(V,L).
\]
By Serre duality the relevant map is dual to Kodaira–Spencer. This suggests testing a moduli slice with exactly 40 independent parameters, rather than the redundant 55-dimensional projective coefficient space.

An explicit slice near the Fermat point is
\[
F=\sum_{i=0}^3 x_i^5+\sum_m t_m x^m,
\]
where \(m\) ranges over degree-five monomials all of whose four exponents are at most 3. There are 40 such monomials. At the Fermat point they form the degree-five part of the Jacobian ring \(\mathbf Q[x_0,\ldots,x_3]/(x_0^4,\ldots,x_3^4)\). Thus the expected 40-dimensional Kodaira–Spencer map is an isomorphism at that point and generically. Over \(K=\overline{\mathbf Q(t_m)}\), this may verify the existing C.3ab cohomological hypothesis in a field-specific generic example. The complete tangent/deformation identification has not been assigned a new audit or numbered claim here.

It is essential not to infer the complex strict-henselian statement by the usual finite-type algebraic-equivalence base-change argument. A cycle on the complex strict henselization can descend to a finite pointed étale model whose coefficients vary with the parameter. A family on that varying étale neighborhood is not automatically a family on the **fixed** punctured henselian product. Both owner and parent identified this gate independently. It prevents a claimed extension to all complex generic quintic cones at this stage, and certainly prevents a universal top-quotient conclusion.
