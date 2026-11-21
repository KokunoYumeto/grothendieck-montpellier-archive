# DP57. An explicit unramified CM repair and the actual adelic endpoint interface

Author: /root/step2_higher, GPT-6 Astra Pro. Reasoning effort is not exposed. Date: 2026-11-21 UTC.

This is a proved source application and an explicit geometric construction. It does not claim membership in the source's iterated theta image. The accepted source theorems are applied under their stated hypotheses; no Lean execution or RH audit is claimed. Source recovery and proof checks are recorded separately.

## 1. Statement and the exact source issue

Put \(E=\mathbf Q(\zeta _7)\), \(F=E^+\), and let \(J\) be the genus-three Jacobian of \(y^2=x^7-1\), with the CM type \(\Phi=\{1,2,3\}\) and the principal polarization established in DP22/DP49. Define
\[
 E'=E(i)=\mathbf Q(\zeta _{28}),\qquad F'=(E')^+=F(\sqrt7).
 \tag{AL1}
\]
The following assertions hold.

1. The original field \(E\), with its canonical conjugation, fails the exact IsCMUnram condition used by the source's CMData. The field \(E'\) satisfies it, and \(F',E'\) therefore give actual CMData directly. The extension \(E'/F'\) is finite étale at all finite places and also supplies the field-level toroidal Host.
2. The abelian variety \(A=J^2\), with its product principal polarization, has an integral \(\mathcal O_{E'}\)-action and CM type
\[
 \Phi'=\{a\in(\mathbf Z/28)^\times:a\bmod7\in\{1,2,3\}\}
       =\{1,3,9,15,17,23\}.
 \tag{AL2}
\]
At \(11\) the two \(E'\)-prime factors have heights \(6,6\), dimensions \(4,2\), and slopes \(2/3,1/3\). The underlying product \(J^2\) retains its height-three direct factors. Those product factors are not individual \(E'\)-stable factors.
3. For every positive Hermitian rank \(n\), there is a concrete endpoint level with \(T=1\), no \(T\)-decoration, and principal reduction level at one prime over \(29\), for which the source's DecoPtSurj and IsLevOf hypotheses hold. Its finite coefficient-value space is exactly the restriction of the source's actual adelic finite-weight space, through fi_iff_FiC. With the weak goodness proved in DP52 and the free-level argument in DP55, there are nonzero such endpoint forms and a partner with nonzero detecting period; the normalized construction can make that period \(1\).
4. This repair does not supply the source's old CMObj/HasType theta datum. The type \(\Phi'\) is induced from no imaginary quadratic subfield. Also \([F':\mathbf Q]=6\) fails the separate \(8\mid f\) hypothesis of the old host wrapper. Both wrapper restrictions are absent from the generic endpoint construction just asserted.

The precise source issue is not merely a generic demand for good reduction. Formalism/LocalRingCardinality/DataSpaces.lean:14–19 defines CMData with the field

\[
\begin{split}
\mathrm{IsCMUnram}(E):\quad&
E\text{ totally complex, conjugation compatible with every complex embedding},\\
&\forall P\subset\mathcal O_E\text{ maximal},\
\exists\theta\in\mathcal O_E:\theta-\bar\theta\notin P.
\end{split}
\tag{AL3}
\]

The literal declaration is Formalism/HermitianLattices/StatementMass.lean:44–48. This explicit residue-field condition is what the proof below verifies.

## 2. Original failure and the direct repair

The prime \(\mathfrak p=(1-\zeta _7)\) is the unique prime over \(7\) in \(\mathcal O_E=\mathbf Z[\zeta _7]\), with residue field \(\mathbf F_7\). Modulo \(\mathfrak p\), both \(\zeta _7\) and \(\zeta _7^{-1}\) equal \(1\). Consequently
\[
 \theta-\bar\theta\in\mathfrak p\qquad(\theta\in\mathcal O_E),
 \tag{AL4}
\]
which contradicts (AL3). This is a strict failure of the given CMData interface, rather than a claim that all adelic constructions over a ramified CM extension fail.

For \(E'\), two elements suffice. The norm calculation
\[
 N_{E/\mathbf Q}(\zeta _7-\zeta _7^{-1})
  =N(\zeta _7^{-1})N(\zeta _7-1)N(\zeta _7+1)
  =1\cdot7\cdot1=7
 \tag{AL5}
\]
shows that \(\zeta _7-\zeta _7^{-1}\) is a unit at every prime of \(E'\) not over \(7\). Indeed a prime containing this algebraic integer must contain its rational norm, by the integral characteristic polynomial. At a prime over \(7\), use \(i-\bar i=2i\), which is a unit there. Thus \(\theta=\zeta _7\) off \(7\), and \(\theta=i\) at \(7\), prove (AL3) at every finite prime, including those over \(2\).

The field \(E'\) is totally complex since it contains \(i\), and canonical conjugation commutes with its complex embeddings since it is cyclotomic. Its fixed field is totally real and has index two. To identify it explicitly, write
\[
 z=\zeta _7+\zeta _7^2+\zeta _7^4,\qquad
 z+\bar z=-1,\quad z\bar z=2,\quad
 \delta=1+2z,\quad \delta^2=-7.
\tag{AL6}
\]
Then \(i\delta\) is real with square \(7\). Since \([F:\mathbf Q]=3\), \(\sqrt7\notin F\), so \(F(\sqrt7)\) has degree six and is exactly the fixed field of \(E'\). These observations supply every field of CMData, without invoking the old host wrapper.

The same argument proves the stronger, literal ring-unramified condition in the toroidal Host. Let \(R=(\mathcal O_{F'})_v\) at a finite prime. Choose \(\theta=\zeta _7\) if \(v\nmid7\), and \(\theta=i\) if \(v\mid7\). Then \(\theta\ne\bar\theta\), so it generates \(E'\) over \(F'\). Its trace and norm belong to \(R\), and
\[
 \operatorname{disc}(1,\theta)=(\theta-\bar\theta)^2\in R^\times.
 \tag{AL6a}
\]
Indeed the chosen difference is a unit at every prime above \(v\). Thus \(R[\theta]\) is a finite étale quadratic \(R\)-algebra. It is normal since \(R\) is normal and finite étale algebras are smooth; its fraction field is \(E'\). Every element of the integral closure of \(R\) in \(E'\) is integral over \(R[\theta]\), hence belongs to it. Therefore \(R[\theta]\) is that integral closure. This proves that \(\mathcal O_{E'}\) is unramified over \(\mathcal O_{F'}\) everywhere. The standard normality fact is Stacks Project, Lemma 10.163.9, Tag 033C.

In the exact source ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean:14–26, take
\[
 d=7,\qquad rt=-\delta,\qquad w_0=-z,\qquad
 \bar{\phantom a}=\text{canonical conjugation},\qquad
 rt_0=\sigma_0(rt).
 \tag{AL6b}
\]
Then \(d\bmod16=7\), \(d\) is prime, \(rt^2=-7\), and \(2w_0=1+rt\). Equation (AL6a) supplies Host.unram. All field-level Host data are therefore constructed. This assertion deliberately stops before its Datum.dom condition.

For the standard cyclotomic facts used here, an exact primary textbook locator is J. S. Milne, Algebraic Number Theory, version 3.08 (2020), Proposition 6.2(b),(c), printed pp.96–98, and Theorem 6.4(a),(b), printed p.99. Theorem 6.4 gives \(\mathcal O_{\mathbf Q(\zeta _{28})}=\mathbf Z[\zeta _{28}]\). The proof of (AL5) itself is just \(\Phi_7(1)=7\), \(\Phi_7(-1)=1\).

## 3. Integral geometric realization, with principal polarization

Let \(\alpha\) denote the action of \(\zeta _7\) on \(J\), and let \(E\) act diagonally on \(A=J\times J\). Define
\[
 I=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\in\operatorname{End}(A).
 \tag{AL7}
\]
It commutes with the diagonal \(E\)-action and satisfies \(I^2=-1\). The polynomial \(X^2+1\) is irreducible over \(E\): \(E\) has the unique quadratic subfield \(\mathbf Q(\sqrt{-7})\), whereas \(i\notin\mathbf Q(\sqrt{-7})\). Hence the resulting unital homomorphism \(E(i)\to M_2(E)\subset\operatorname{End}^0(A)\) is injective.

The action is integral on the full ring of integers. With compatible roots \(\zeta _7=\zeta _{28}^4\), \(i=\zeta _{28}^7\), we have
\[
 \zeta _{28}=\zeta _7^2 i^{-1},\qquad
 \mathbf Z[\zeta _{28}]=\mathbf Z[\zeta _7,i].
 \tag{AL8}
\]
The right side acts through the integral automorphisms \(\alpha\) and \(I\), and Milne Theorem 6.4(b) identifies it with \(\mathcal O_{E'}\). No isogeny is needed.

For the product principal polarization, Rosati is transpose followed by the Rosati involution on \(\operatorname{End}^0(J)\). Thus
\[
 I^\dagger=I^{\mathsf T}=-I,\qquad a^\dagger=\bar a\quad(a\in E),
 \tag{AL9}
\]
so it acts as canonical conjugation on \(E'\). Equivalently, \(-\delta I\) realizes \(\sqrt7\), is self-adjoint, and squares to \(7\). This is an integral principally polarized realization. The alternative presentation \(\sqrt7\mapsto\left(\begin{smallmatrix}0&7\\1&0\end{smallmatrix}\right)\) with polarization \(\operatorname{diag}(1,7)\) is unnecessary; its degree \(7^6\) must not be reported as an unavoidable cost.

On the two-dimensional multiplicity space of every old tangent character, \(I\) has the two distinct eigenvalues \(i,-i\). Each old character in \(\Phi\) therefore contributes both extensions to \(E'\); the other old characters contribute none. This proves (AL2). Since \([E':\mathbf Q]=12=2\dim A\), it is a full CM action.

At \(11\), multiplication by \(11\) on \((\mathbf Z/28)^\times\) has the two orbits
\[
\begin{split}
 O_1&=(1,11,9,15,25,23),&
 \mathbf1_{\Phi'}|_{O_1}&=(1,0,1,1,0,1),\\
 O_2&=(3,5,27,17,19,13),&
 \mathbf1_{\Phi'}|_{O_2}&=(1,0,0,1,0,0).
\end{split}
\tag{AL10}
\]
Thus the CM factors have heights six and dimensions four and two. This also follows directly by taking two copies of the already established height-three factors of \(J\), so it introduces no new slope calculation theorem beyond DP22/DP49. The type patterns have period three, and the slopes are \(2/3,1/3\).

The distinction between the \(E'\)-factors and the old product factors is essential. Each \(E'\)-prime above \(11\) is unramified of degree six. After an unramified splitting extension, its action on a rational Dieudonné module decomposes the module into six eigenspaces, and Frobenius cyclically permutes them isomorphically. They have equal dimensions, so every nonzero factor stable under this local field has height divisible by six. In particular, the height-three product summands are not \(E'\)-stable scalar factors. Diagonalizing the \(E'\)-action on the tangent space does not supply such one-dimensional formal summands.

## 4. A concrete split prime and the exact surjectivity theorem

Choose \(\xi=\zeta _{28}\) and the prime
\[
 P=(29,\xi-2)\subset\mathcal O_{E'}.
 \tag{AL11}
\]
The residue class \(2\in\mathbf F_{29}^\times\) has order \(28\): \(2^{14}=-1\) and \(2^4=16\ne1\). Hence it is a primitive \(28\)-th root, and evaluation \(\xi\mapsto2\) gives \(\mathcal O_{E'}/P=\mathbf F_{29}\). All primitive roots are simple modulo \(29\), so \(29\) splits completely and the completion at \(P\) is \(\mathbf Q_{29}\). Conjugation sends \(\xi\) to \(\xi^{-1}\), whose value is \(15\), not \(2\); therefore \(P\ne\bar P\).

Take
\[
 S_T=\varnothing,\quad S_G=\{P\},\quad H_P=\{1\}
       \subset\mathrm{GL}_n(\mathbf F_{29}),
 \tag{AL12}
\]
with trivial level character. The literal IsSplitSet definition is
\[
 \forall Q,Q'\in S_T\cup S_G,\quad Q'\ne\bar Q.
 \tag{AL13}
\]
In source notation this uses IsConjPl, defined by membership after conjugating integral elements; (AL11) verifies its negation directly. Exact locators are Formalism/LocalToGlobal/Divisibility/DefGroupLemmas.lean:23–27. Thus IsSplitSet and Disjoint \(S_T,S_G\) both hold.

Three named source theorems now apply:

- Columns/InputsGenus.lean:17–19, unimodGenus_holds, supplies UnimodGenus \(hc,n\) for every CMData and \(n>0\). Its conclusion is that every unimodular lattice in the standard definite Hermitian space is the global lattice of a finite adelic unitary element; Columns/Inputs.lean:51–65 gives the exact local/global predicates.
- Divisibility/DefGroupLemmas.lean:1475–1481 proves reduction_surjective_bis : RedSurj. RedSurj, defined at :64–68, allows arbitrary prescribed invertible reduction matrices at an IsSplitSet for a definite unimodular lattice and a frame.
- Columns/AdelicLemmas.lean:1245, decoPtSurj_of, consumes precisely UnimodGenus, RedSurj, IsSplitSet \(S_T\cup S_G\), and disjointness. It supplies DecoPtSurj, the surjectivity of decoPt, defined at :737.

Applying these theorems to (AL12) proves the actual DecoPtSurj statement. This does not rely on the specialized ColDat wrapper or merely posit that the missing surjectivity ought to hold.

## 5. The actual endpoint level and IsLevOf

Use the generic constructor stepOf in Columns/RecLevelStep.lean:20–51 with
\[
 T=1,\qquad \pi=1,\qquad f=6,\qquad S_T=\varnothing,
 \qquad \Lambda_P.H=\{1\},\qquad\Lambda.\mathrm{chr}=1.
 \tag{AL14}
\]
Here BasePi \(\varnothing,1\) says divisibility by \(1\) is automatic and its conjugate is coprime to it. The equality \(\pi\bar\pi=T\) is \(1=1\); the condition \(P\in S_T\iff\pi\in P\) says \(1\) belongs to no prime. Cardinality hypotheses over \(S_T\) are vacuous, as are the conditions at primes dividing \(T=1\). The standard lattice is self-dual, so the required relative index is
\[
 1=T^{2f}.
 \tag{AL15}
\]
Every input is therefore supplied. Columns/TiedXp.lean:21–23 and :35–41 give exactly this construction as xp_basePi_one and tieLevP; their generic section has no X.Ok assumption. The appearance of the name Pr.vGs in that wrapper imposes no extra property: stepOf itself accepts an arbitrary finite \(S_G\), so (AL12) can be supplied directly.

The resulting StepLevel is compact and open and contains its own local compatibility proofs. More specifically, its definitions are
\[
 L.U=\mathrm{levU}(hc,n,\varnothing,\{P\},\Lambda.\mathrm{grp}),
 \qquad L.\chi=\mathrm{levTyp}(\sigma_0\circ\Lambda.\mathrm{chr}).
 \tag{AL16}
\]
These are literally stepOf fields U and chi at RecLevelStep.lean:46 and :50. They are the two fields demanded by IsLevOf, Columns/TiedValFi.lean:151–154. Thus IsLevOf is proved by the same two reflexivity proofs as tieLev_isLevOf at :265–266, without its specialized wrapper's X.Ok hypotheses.

At the selected split prime the finite level is principal reduction modulo \(29\); elsewhere it is the standard hyperspecial level prescribed by the generic constructor. Since the character is trivial, no character-extension choice is left unresolved.

## 6. Actual adelic finite-weight values and a nonzero period

Take the coefficient field \(K=E'\), the six embeddings in \(\Phi'\), and any dominant coefficient weights of the chosen positive Hermitian rank. Canonical conjugation commutes with these embeddings. Thus the weak conjugation compatibilities of DP52 hold. Its complete weak-goodness proof gives the required formGSD.Ok, without demanding X.Ok.quad.

Columns/TiedValFi.lean:239–255, fi_iff_FiC, now applies with three genuinely supplied inputs:
\[
 \mathrm{formGSD.Ok},\qquad \mathrm{DecoPtSurj},\qquad
 \mathrm{IsLevOf}.
 \tag{AL17}
\]
It identifies the finite coefficient-value space Fi with the restrictions of the actual adelic finite-weight space FiC at the selected adelic class representatives. The forward implication uses the explicit function adOf, defined at :179–181; adOf_mem at :185–201 proves its adelic transformation and weight conditions. The reverse implication uses the exact stabilizer invariance established at :209–237. Therefore this is an actual source interface identification, not just an abstract analogy between two finite-dimensional spaces.

The chosen level also supplies the nonvanishing input. As proved in DP55, a decorated positive-definite lattice has finite stabilizer. At \(P\), any stabilizer fixing its principal decoration lies in \(1+29M_n(\mathbf Z_{29})\), which has no nontrivial torsion. Hence all these stabilizers are trivial. There is a decorated standard lattice, and every dominant coefficient module has its nonzero extremal vector. A coefficient vector supported on this free class gives a nonzero finite value, hence a nonzero adelic form by (AL17). The perfect partner pairing and the actual source period formula from DP55 yield a partner with nonzero period; choosing its paired coefficient to be \(1\) yields period \(1\).

This argument is uniform in \(n>0\) and in the dominant weights, at the fresh principal level just constructed; it does not assert preservation of a prescribed earlier level. In particular, the generic endpoint level and its nonzero periods are not an additional obstruction to changing an admissible endpoint rank. It does not assert that a prescribed theta lift reaches the chosen nonzero vector.

## 7. The remaining exact type obstruction and cost scope

The old source HasType requires one constant tangent multiplicity on all embeddings with \(\tau(H.rt)=\rho\), and another constant multiplicity on the complementary embeddings. These are the two fibers of an imaginary quadratic field. Exact locators are Development/AbelianVarietyTheory/Definitions/CMLattices/IsDiffOf.lean:64–67; CMObj.typeP, typeM, typeB are :115–122. The corresponding uniform \(p,q\) trace identity is Datum.dom in TwoWeightEqOneAddRoot.lean:43–49. IsTen at IsDiffOf.lean:73–77 is also the specific Serre tensor compatibility with the source elliptic object, not a condition furnished by (AL17).

For \(\Phi'\), this imaginary-quadratic type condition fails. Its embeddings include the identity, \(3\), and \(15\) modulo \(28\). The element \(3\) has order six and
\[
 \langle3\rangle=\{1,3,9,27,25,19\},\qquad15\notin\langle3\rangle,
 \quad15^2=1.
 \tag{AL18}
\]
Thus \(3,15\) generate all twelve automorphisms of \(E'/\mathbf Q\). If every embedding in \(\Phi'\) restricted to one fixed embedding of a quadratic subfield \(K_0\), all their quotients with the identity would fix \(K_0\). Equation (AL18) would force \(K_0\subseteq\mathbf Q\), a contradiction. The same calculation says that the common restriction field Kq of this type is \(\mathbf Q\).

Consequently the construction in §§2–6 repairs the unramified CMData, decorated-lattice surjectivity, adelic level, and nonzero endpoint-period interfaces. It does not instantiate the source's old CMObj for this geometric \(A\). A mixed-type replacement of its actual theta-family and coefficient/path identities is still required before the local higher-height calculations can enter that family's global inequality.

The old AbelianUnramifiedExtensionConditions wrapper separately requires \(8\mid f\), at Columns/AbelianHostFieldConditions.lean:110–122. Here \(f=6\), so that wrapper is not supplied either. This does not affect the generic theorems used above: CMData has no such field, and all hypotheses of the endpoint constructors were explicitly supplied.

The construction doubles the geometric dimension from three to six, increases the CM field degree from six to twelve, and chooses a concrete principal level at \(29\). The product principal polarization has degree one. No uniform estimate for coefficient heights, denominator costs, mass factors, or the full global cost has been proved here. In particular, the surviving height-three product factors and the source's \(E'\)-eigenbasis must not be counted as free, interchangeable derivative directions. No claim about a smaller number of theta lifts follows from this endpoint construction alone.

## 8. Source provenance and check discipline

All Lean files cited above were read from the original author's split archive, with exact archive member and SHA-256 recorded in the incremental source manifest. Recovery is not a Lean compilation. Application of a named accepted theorem is kept separate from independent proof of the explicit field, type, matrix-action, prime, and level-input calculations.

External primary sources: J. S. Milne, Algebraic Number Theory, version 3.08, July 19, 2020, https://www.jmilne.org/math/CourseNotes/ANT.pdf, Proposition 6.2 and Theorem 6.4; the precise cited pages were opened on 2026-11-21. The cyclotomic integer-ring claim and prime-power residue claim are the only textbook facts needed from it. Its Lemma 6.5, printed p.100, also supplies an independent coprime-discriminant proof of \(\mathcal O_{E'}=\mathcal O_E[i]\), but the direct cyclotomic argument (AL8) already suffices. The local normality fact in (AL6a) is Stacks Project Tag 033C, https://stacks.math.columbia.edu/tag/033C.

The whole saved proof and the integrated-fragment preservation check have separate dated records. No future review or implementation success is asserted by this memo.
