# Motivic monodromy equivalence and the missing pure realization

Research state recorded 19 November 2026 during the checkpoint-07 freeze. This is a proved analytic-category encoding and an exact limitation of the attempted converse. It is not a converse theorem for C6 and is not counted as movement on its universal gate.

## 1. What the Binda--Gallauer--Vezzani theorem supplies

Use the exact version arXiv:2306.05099v2, dated 31 October 2024. Theorem 1.3 identifies rigid analytic motives over C_p with algebraic motives over the residue field equipped with a nilpotent monodromy map. Its more useful arithmetic form is Corollary 4.14, page 32: for a complete rank-one nonarchimedean field K with perfect residue field k, a choice of pseudo-uniformizer gives an equivalence

$$
\operatorname{RigDA}_{\mathrm{gr}}(K)\simeq\operatorname{DA}_N(k).
$$

The right side contains pairs (T,N:T→T(−1)). Lemma 2.13, page 9, and Proposition 4.13, page 31, give the required compactness statements; a pair with compact underlying motive and square-zero N is compact. I read the complete internal proofs of Lemmas 2.13 and 2.17, Lemma 2.31 and Proposition 2.32, Propositions 4.10 and 4.13, Corollary 4.14, and Proposition 4.25. The proofs refer to their foundational inputs; this is not a claim to have independently re-proved all of those inputs.

Corollary 4.33, page 36, extends any monoidal realization of the residue-field motive to the monodromy category. Its underlying realization and monodromy are exactly the realization of T and of N. The identification with the usual unipotent inertia logarithm is stated in Remark 4.61, pages 42--43, with a proof sketch and a reference to Ayoub's Theorem 11.17. That original theorem was also opened: its statement is on printed page 110 and its concluding proof on pages 115--116. The latter proves the exponential compatibility with tame inertia; not every preparatory lemma and diagram in its 145-page article has been independently audited here.

## 2. Square-zero encoding of an arbitrary algebraic cycle

Let X/k be smooth projective over a finite field and let α∈CH^r(X)_Q. In algebraic motives write C_X for the cohomological motive, whose geometric realization is RΓ(X_bar,Q_l). The cycle determines a morphism

$$
a:\mathbf1\longrightarrow B:=C_X(r)[2r].
$$

Put T=1⊕B(1). Then T(−1)=1(−1)⊕B. Define N:T→T(−1) by the single nonzero block a from the first source summand to the second target summand. The composite N(−1)N is zero: N vanishes on the second summand. There is no cohomological shift in this square-zero construction beyond the [2r] already in B.

Both 1 and B are compact, so (T,N) is compact. Take K=W(k)[1/p] and pseudo-uniformizer p. Corollary 4.14 supplies a compact unipotent rigid motive R_α over this finite unramified extension of Q_p with the prescribed pair. Passing to C_p is optional, not required for the construction.

After geometric l-adic realization, the sole possibly nonzero cohomology block of N is

$$
H^0(a):\mathbb Q_l\longrightarrow H^{2r}(X_{\bar k},\mathbb Q_l(r)),
\qquad1\longmapsto\operatorname{cl}_l(\alpha).
$$

Thus N vanishes on every cohomology group of R_α if and only if the l-adic cycle class of α is zero. This statement uses the geometric realization; no arithmetic Ext group is substituted for the cycle class. If α is initially over Fbar_p, X and its finite cycle data descend to some finite k, so the same construction applies.

Consequently, an independence-of-l assertion for vanishing of monodromy on **all compact unipotent rigid motives** would imply independence of homological equivalence over Fbar_p. Using the usual inertia-logarithm identification, the same conclusion follows from the corresponding enlarged unramifiedness assertion. Van Dobben de Bruyn's published equivalence then converts this to his rank formulation. This enlarged assertion has not been renamed as the original C6 conjecture.

For a general algebraic map a:A→B, the identical construction T=A⊕B(1) satisfies rank(H^iN)=rank(H^ia). The cycle specialization above is enough for the converse implication to homological-equivalence independence, and avoids assuming an algebraic degree projector in characteristic zero.

## 3. What the equivalence does not supply

The constructed R_α is an object in a stable category obtained using cones and retracts. The cited theorem does not provide a smooth projective variety over a number field, a rational algebraic or motivated projector on its cohomology, or a simultaneous realization-compatible identification of such a pure motive with the constructed object.

Proposition 4.25, page 34, must not be read as such a statement. It identifies a heart of a bounded weight structure on the analytic category with the image under ξ of residue-field Chow motives. Under the monodromy equivalence these heart objects have zero N. This analytic heart is not the category of all pure motives on the generic fibre: the H1 motive of a Tate elliptic curve is pure on the generic fibre and has nonzero local monodromy. BGV Proposition 4.21 and Remark 4.23 explicitly discuss that Kummer/Tate-curve object.

Likewise, Ayoub--Gallauer--Vezzani Proposition 2.2.13, author page 37, constructs a monoidal analytification functor and its functoriality. Theorem 3.7.21, author pages 121--122, identifies rigid motives at a geometric point with modules in formal/special-fibre motives. I read those statements and their complete local proofs. Neither asserts that every compact analytic object is the analytification of a pure Chow or motivated object over a number field.

Even algebraization as a mixed algebraic motive over a p-adic field would leave two issues: passage to the pure category actually quantified in C6, and number-field realization preserving the relevant monodromy flag for all coefficient primes. Closure under cones or extensions cannot silently remove the first issue. Unramifiedness is not stable under arbitrary extensions of unramified representations: a nontrivial tame unipotent extension of two unramified graded pieces has nonzero N. Its graded pieces therefore do not detect its ramification.

The precise missing step in this route is a pure number-field realization, or a proved reduction to a finite family of such realizations, which preserves the vanishing of the prescribed square-zero monodromy for every l. We have not obtained that step, and no assertion of its impossibility is made.

## 4. Bounded current-source follow-up

The search checked primary current versions rather than relying on an obsolete title or a search abstract.

* Park, *Log motivic nearby cycles*, arXiv:2405.14083v1: Theorems 1.1--1.6, pages 2--3; Theorem 6.10, pages 21--22; Remark 7.2, page 24. The latter explicitly distinguishes the positive-residue-characteristic comparison and describes stable-category equivalences. These statements do not furnish a pure number-field algebraization. Only the exact relevant statements and nearby proof text were read, not a full independent proof audit of the paper.
* Gabber--Zavyalov, *Algebraization Techniques and Rigid-Analytic Artin--Grothendieck Vanishing*, published 2026: author Theorems 1.2--1.4 and Corollary 1.5, pages 2--3. These concern rig-smooth formal algebras and partial algebraization of affinoids. They do not give a pure projector presentation of the compact object above. The primary statements and introductory scope were read, not their complete proof sections.
* The withdrawn earlier Cisinski comparison strategy is separately recorded in `cisinski_current_version_scope.md`; it supplies no replacement algebraization theorem.

No pure-number-field essential-surjectivity theorem was found in this bounded follow-up. This is a report of the consulted results, not a claim that every possible publication has been excluded.

## Primary URLs and exact opening scope

- Binda--Gallauer--Vezzani: https://arxiv.org/pdf/2306.05099v2; published DOI 10.4171/jems/1634. Exact key pages were located in the extracted primary PDF: Lemmas 2.13/2.17 page 9, Proposition 2.32 page 13, Proposition 4.13 page 31, Corollary 4.14 page 32, Proposition 4.25 page 34, Corollary 4.33 page 36, Remark 4.61 pages 42--43. The source and hash are archived by `code/fetch_bgv_sources.py`.
- Ayoub--Gallauer--Vezzani: https://user.math.uzh.ch/ayoub/PDF-Files/AGV.pdf; Proposition 2.2.13 page 37 and Theorem 3.7.21 pages 121--122, including their local proofs; introduction's categorical-versus-analytic explanation pages 2--4. The foundational 192-page proof is not claimed independently checked.
- Ayoub: https://smf.emath.fr/download/pdf/44402; *La réalisation étale et les opérations de Grothendieck*, Ann. Sci. ENS 47 (2014), 1--145; Theorem 11.17 page 110, concluding proof pages 115--116.
- Park: https://arxiv.org/pdf/2405.14083; current primary author listing https://www2.math.uni-wuppertal.de/~park/publications.html.
- Gabber--Zavyalov: https://bogdanzavyalov.com/refs/papers/artin-grothendieck-vanishing.pdf; published metadata https://smf.emath.fr/node/3693440, Ann. Sci. ENS 59(2), 387--436 (2026), DOI 10.24033/asens.002641.

Bibliography and numbered-main integration are deferred until the checkpoint freeze ends. This note and source records preserve the proof and remaining limitation immediately.
