# Independent review of Part A and additional primary-source ledger

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026, child agent `/root/frobenius`. This is an independent mathematical check within the same AI run, not human review. We have not modified the parent master or its `A_deuring.tex`.

## 1. Main findings

1. **A.5 has a counterexample under the general module-category definition of 15:16.** The complete proof is `A5_counterexample.tex`, paragraphs A.5c–d. It uses the actual reduction modulo 3 of the global maximal-order category, then scalar extension to \(\mathbb F_9\). Its determinant-rigidified autoequivalence category has noncommutative \(\pi_0\), so it cannot be a Picard category. The exact executable certificate is `code/verify_ramified_picard_counterexample.py`, with output in `output/verify_ramified_picard_counterexample.json`.

2. **A.2c, A.3a and A.4a have the correct distinction between a sign class and a sign automorphism.** Positivity chooses the class in \(H^1(\mathbb R,\mu_2)\); the chosen realization still has automorphism group \(H^0(\mathbb R,\mu_2)=\{\pm1\}\). No unique natural isomorphism exists.

3. **The global quotient in A.2b needs its positive transport stated explicitly.** The acting global category is \(\operatorname{Eq}(C)\), mapped into \(\operatorname{Eq}(C,T)\) by the canonical positive determinant normalization, exactly as written at 15:48. If one instead lets every possible determinant rigidification of a global equivalence act, the negative rigidification supplies an additional translation and changes the quotient.

4. **A.1d is an explicit geometric rule.** A terminating reconstruction makes it an explicit mathematical prescription. A program need not have been executed for every prime to prove this statement. An implementation limit should not be promoted to an undecided mathematical claim. The literal unrestricted finite-field version remains false by A.1a, independently of this assessment.

## 2. A.5: complete scope and determinant check

The transcription at 15:16 visibly brackets the Dedekind/maximal-order condition (a) and expressly separates it from the module-category conditions (b),(c). At 15:34 the proposed rigidified equivalences are invertible bimodules with a specified isomorphism of their reduced-norm line with the base ring. At 15:36 the base is an arbitrary commutative algebra and the Picard claim is marked “À vérifier!!”. We use those precise formulations.

For the global maximal order

\[
 O=\mathbb Z\langle1,i,(1+j)/2,(i+ij)/2\rangle
 \subset(-1,-3)_{\mathbb Q},
\]

put \(R=\mathbb F_3[\alpha]/(\alpha^2+1)\), \(B=O\otimes R\). Because 2 is invertible, its local generators give the algebra with basis \(e_0,e_1,x,y\), where \(x=e_0xe_1\), \(y=e_1ye_0\), and the radical has square zero. The reduced norm is the degree-two polynomial \(N(a,b,c,d)=ab\). It is not the determinant of the rank-four regular representation.

Every global rank-one projective right \(O\)-module becomes free at 3. Base change of its Hom modules is exact because the source is projective. Thus the base-changed category, not just a newly invented one-object category, is equivalent to the category of free rank-one right \(B\)-modules. Over the field \(R\) these are precisely the modules locally free of rank one over \(\operatorname{Spec}R\).

The reference object \(X=O\) has identity basis and positive norm generator 1, so \(T_R=\nu(X_R)\) is fixed without an extra scalar. Each norm-preserving automorphism \(\rho\) has a specific rigidification \(u_\rho=1\), rather than merely a transported norm line that happens to be abstractly trivial. The induced determinant map of a natural isomorphism represented by \(b\in B^*\) is \(N(b)\). Hence the precise rigidification condition is \(N(b)=1\). Tensor products of the chosen rigidifications remain 1.

Let \(t=1+\alpha\), of order eight. Let \(S\) exchange both vertices and both arrows, and let \(T_t\) fix the vertices and \(y\), while scaling \(x\) by \(t\). Both preserve \(N\). Their products obey

\[
 T_tS=\operatorname{Int}(d)ST_t,
 \qquad d=te_0+e_1,
 \qquad N(d)=t.
\]

Commuting with \(e_0\) kills both radical coordinates of a central element, and commuting with \(x\) makes its two diagonal coordinates equal. Thus \(Z(B)=R\) exactly. It follows that every intertwiner between the products is \(cd\), \(c\in R^*\), with norm \(c^2t\). This is never 1. Therefore these two rigidified classes do not commute.

The finite certificate enumerates all 6561 elements, all 5184 units, the entire centre, and all eight possible intertwiners. Their norms are exactly the four nonsquares. The first run completed in 0.168108 seconds using only the Python standard library. The proof does not rely on trusting the finite search.

**Qualification.** The algebra \(B\) is not Azumaya, and hence cannot satisfy condition (a) over a field. The counterexample therefore refutes the general formulation using (b),(c), as well as the claim that every ramified base change inherits the Picard structure. It does not refute the theorem for strict maximal-order or Azumaya categories. In those restricted domains the argument under condition (C) remains applicable. A statement that retains the universal quantifier must name which version of “Deuring category” it means.

## 3. A.2c: identification of the section torsor

The product decomposition is a decomposition into the two open-and-closed factors \(A''\) and \(\mathbb Z_p\). Away from \(p\), determinant-compatible Tate realizations give the comparison object between the determinant splitting gerbe and the square-root gerbe of the Tate line. At infinity the positive quaternionic realization gives its counterpart. At \(p\) the comparison gerbe is defined to be \(B\mu_2\), so its unit object is available. These are objects of the comparison gerbe, not a neutralization of the ramified quaternion Brauer gerbe at \(p\).

Given any base object in a banded abelian gerbe, twisting by a band torsor identifies its objects with torsors. Thus isomorphism classes of sections form a torsor under the stated \(H^1\). To make the identification with \(\mathcal T\) explicit, choose the crystalline parity-zero representative whose determinant rule is \(\xi_p\). Its remaining choices are precisely the unit squareclasses. Replacing it by the parity-one representative translates all local comparison data by \(f\); quotienting by \(\langle f\rangle\) therefore removes this choice. The unit section at \(p\) corresponds to \(\xi_p\), not to a coordinate-independent numerical unit.

The global equivalences used in this identification have the canonical **positive** determinant transport. We verified this against the actual map \(\operatorname{Eq}(C)\to\operatorname{Eq}(C,T)\) in the transcription at 15:48. It should be stated in A.2b to avoid adding an unwanted global negative rigidification.

## 4. A.3a and A.4a: sign and covariance

For \(V_E=\operatorname{Hom}(E_0,E)\otimes\mathbb R\), the right action and the form

\[
 \langle x,y\rangle=\beta(x^\vee y)
\]

obey \(\langle xa,yb\rangle=\bar a\langle x,y\rangle b\). A nonzero rational homomorphism identifies this form with a positive multiple of the reduced norm on \(\mathbb H\), so it is positive definite after extension to \(\mathbb R\). Postcomposition by \(f\) has adjoint \(f^\vee\) and multiplier \(\deg f\). The target must contain all quaternionic linear maps: the isometry-only category would omit nontrivial isogenies.

An intertwiner between two such functors exists by Morita equivalence and real Skolem–Noether. Naturality forces all intertwiners to differ by a central nonzero real scalar. Unit norm therefore leaves exactly two, differing by \(-1\). This is a \(\pi_1\) ambiguity. The separate \(\pi_0\) ambiguity consists of the two signs of a determinant trivialization; a quaternionic linear change of basis has positive norm, so positivity distinguishes the two classes. The current claims in A.3a and A.4a correctly keep these statements separate.

## 5. A.1d/e: explicitness and a more concrete intertwiner step

The previously found orientation issue has been repaired in the current parent draft: the action of **raw** \(a\), not \(\bar a\), on \(M/FM\) gives the tangent orientation when the covariant convention is \(D(a)=(a^\vee)^*\). The Hodge quotient is \(H^1(E,\mathcal O_E)=\operatorname{Lie}(E^\vee)\); pullback by \(a^\vee\) differentiates its dual \(a\). This verifies the sign without importing an incompatible convention for Dieudonné modules.

The formula using a marked curve, its crystalline cup-trace pairing, and an \(O,F\)-intertwiner is choice-independent by the scalar centralizer \(\mathbb Z_p^*\). The local classification plus oriented Deuring theorem supplies the required choices. The positive degree identity \(\deg(ta)=\deg(t)\operatorname{Nrd}(a)\) gives the norm transition functions. Primitivity of the degree ideal, using integral Tate/Dieudonné Hom comparisons at each prime, removes a hidden multiplicative unit in Morita compatibility.

The linear-algebra step can be made more explicit. First solve the \(O\)-linear equations over \(W\) for an integral invertible \(b_0:D(E)\to M\). Such a solution exists by the proved classification. The Hom lattice is free of rank one over \(W\), since its rational centralizer is scalar. There is a unit \(c\in W^*\) with

\[
 F_Mb_0=c\,b_0F_E.
\]

The valuation of \(c\) is zero because both determinants have valuation one. Set \(b=ab_0\), where

\[
 \sigma(a)/a=c^{-1}.
\]

The first equation modulo \(p\) is \(a^{p-1}=\bar c^{-1}\). Successive Witt digits are solved by Artin–Schreier equations. Every partial solution extends because the residue field is algebraically closed. This gives the intertwiner without an unspecified nonlinear search. Comparing the determinant with any fixed Tate determinant isomorphism gives a unit in \(\mathbb Z_p^*\); its class needs only reduction modulo \(p\) for odd \(p\), or modulo 8 at \(p=2\).

An effective input model for arbitrary Witt coefficients is needed to call this a uniform computer algorithm. The mathematical construction needs no computability hypothesis. The absence of an implemented all-prime crystalline evaluator is a disclosure about computation, not a gap in the choice-independent rule or the terminating geometric reconstruction. The prompt itself supplies no numerical input pair for which a value was left unevaluated. The literal claim on every finite-field pair is separately refuted by A.1a.

## 6. Additional opened primary sources

All sources below were opened and their relevant statements read on 19 November 2026. Exact source locators are given so the parent can add the appropriate citations without relying on our summaries.

| Source | Opened location and exact result | Relevance and limit |
|---|---|---|
| Honda (1968), *Isogeny classes of abelian varieties over finite fields*, *J. Math. Soc. Japan, 20*(1–2), 83–95, DOI 10.2969/jmsj/02010083 | [Full primary paper, mirrored PDF](https://scispace.com/pdf/isogeny-classes-of-abelian-varieties-over-finite-fields-2qwbdw79so.pdf), **Main Theorem, p. 83**; Propositions 1–4, p. 85; Theorem 1, p. 86; Theorem 2, p. 87. Publisher [metadata page](https://www.jstage.jst.go.jp/article/jmath1948/20/1-2/20_1-2_83/_article/-char/en) also opened. | The Main Theorem gives the bijection between simple finite-field isogeny classes and integral Weil numbers. The root construction in B.1 therefore uses the original theorem directly. Theorem 1 allows an extension field; it does not eliminate a fixed-field class obstruction. |
| Deligne (1973), SGA 4, III, Exposé XVIII | [French retypeset full volume](https://www.cmls.polytechnique.fr/perso/laszlo/sga4/SGA4-3/sga43.pdf), **Proposition 1.4.15**, original p. 529 (retypeset p. 339); **Corollary 1.4.17**, original p. 530 (retypeset p. 340). | Strictly commutative Picard stacks are represented by complexes in degrees \([-1,0]\). The point case gives noncanonical splitting, as proved below. No assertion that arbitrary base changes of a noncommutative order remain Picard follows. |
| Langlands and Rapoport (1987), *Shimuravarietäten und Gerben*, *J. Reine Angew. Math., 378*, 113–220, DOI 10.1515/crll.1987.378.113 | [Authors' IAS retypeset PDF](https://publications.ias.edu/sites/default/files/shimuravarietaeten-und-gerben_rpl_0.pdf), **Satz 4.4** (retypeset p. 46); the mod-\(p\) conjecture is **(5.e)–(5.g)** (retypeset p. 50). Assumptions explicitly read in §4, pp. 39–42. | Satz 4.4 compares the motivic and pseudomotivic gerbes with local maps under standard, Hodge and Tate hypotheses. It does not prove all of these hypotheses or determine an integral unit squareclass \(\xi_p\). The later point description is conjectural there. |
| Kisin (2017), *Mod p points on Shimura varieties of abelian type*, *J. Amer. Math. Soc., 30*(3), 819–914, DOI 10.1090/jams/867 | [Author's full PDF](https://people.math.harvard.edu/~kisin/dvifiles/lr.pdf), **Theorem (0.3)**, **Theorem (2.2.3)**, **Theorem (4.6.7)**. Journal metadata also [opened](https://geodesic.mathdoc.fr/articles/10.1090/jams/867/). | For \(p>2\), abelian type and hyperspecial level, the point description is proved with the stated \(I^{\mathrm{ad}}(\mathbb A_f)\)-conjugation ambiguity. Theorem (2.2.3) gives a CM lift inside an isogeny class. These are not integral all-prime determinant-normalization theorems. |

The three successfully downloaded PDFs and their text extractions are in `sources/`. Honda's complete paper was opened through the web retrieval service; its mirror refused the separate screenshot request, and we do not claim a local PDF copy. Attempts at Rochester and J-STAGE PDFs repeatedly timed out; Project Euclid returned a service notice. These failures do not affect the successful full-text opening of the mirrored primary paper. The Orgogozo SGA 4 site returned 502 errors; the Laszlo retypeset volume succeeded. Harvard DASH failed for Kisin; the author's Harvard PDF succeeded.

### The exact point-case consequence of SGA 4

Let \(\mathcal P\) be a strictly commutative Picard category. By Proposition 1.4.15 it corresponds to a two-term complex \(K\) of abelian groups, with \(H^{-1}(K)=\pi_1\mathcal P\) and \(H^0(K)=\pi_0\mathcal P\). Its truncation triangle has extension class in

\[
 \operatorname{Ext}^2_{\mathbb Z}(\pi_0\mathcal P,\pi_1\mathcal P)=0.
\]

The equality follows because every abelian group has a free presentation whose kernel, as a subgroup of a free abelian group, is free. The triangle therefore splits and \(K\simeq\pi_1\mathcal P[1]\oplus\pi_0\mathcal P\). This proves the split assertion used in R1. The splitting is not canonical in general, and no such conclusion follows if strict commutativity has not first been established. A.5c fails before this result could be applied.

## 7. Files and integration

- `A5_counterexample.tex`: ready-to-integrate A.5c–d, with full typed proof.
- `additional_references.bib`: new entries only, with opened markers and exact locators.
- `additional_results.csv`: A.5c–d and review/status rows.
- `CHECK_EVENTS.tsv`: appended checks, source openings, and computational certificate.
- `code/verify_ramified_picard_counterexample.py` and its JSON output: independently reproducible exhaustive finite verification.

The parent should replace A.5b's unresolved general module-category case by A.5c–d, retain the restricted condition-(C) theorem, explicitly state positive global transport in A.2b, and record A.1e's implementation scope separately from its proved mathematical specification.
