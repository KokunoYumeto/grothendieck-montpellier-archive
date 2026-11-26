# SA26 — Autour de *Pursuing stacks*, part 2

## Scope, evidence and principal findings

**Cotes 106 and 107; status assessed on 19 November 2026.** This dossier consolidates all 63 indexed entries in the supplied package `MPL_106+107`. Its primary mathematical source is the supplied diplomatic transcription, read against the entries themselves. It contains 16 scan blocks for cote 106 and 25 for cote 107. The other 13 cotes in `TOPIC.md` are accounted for in the scope table below, but their claims are not imported into this part. This is a completed audit of the supplied part, with explicit limits on what its evidence establishes.

The two folders contain three related lines of work. Cote 106 studies cofibrant replacement and short descriptions of morphisms in a localization. Cote 107 first develops ordinary presheaf operations, relative Hom, tensors and cotensors; it then asks whether ordinary filtered colimits exist in a homotopy category and investigates the required homotopy extension arguments. This order matters. The later project concordances in the notes are useful leads, but they do not define the questions these pages ask.

The main mathematical findings are these:

1. **The component-level roof questions in cote 106 have affirmative answers under explicitly stated finite cofibration-category axioms.** The manuscript does not itself finish all of these proofs, and its initial reference to “C1–C3 de Brown” does not identify an axiom list unambiguously. The two successive roof conventions must be distinguished. The common-refinement argument is independently checked here, and a particularly close literature match is Thomas’s strict calculus using a cofibration from the coproduct of the endpoints.
2. **Much of the presheaf formalism in cote 107 is correct, but several universal product formulas are false.** The notes correctly detect the false external-product Hom factorization and the false mixed exponential identity. The projection pullback nevertheless preserves exponentials. This audit also finds a missing hypothesis in the earlier notes’ account of when an ambient cotensor remains valued in the original category: the required weights involve every product of the testing representable with the weight, not just the weight alone.
3. **The ordinary sequential-colimit question has a negative answer for ordinary weak homotopy types.** The degree-p circle sequence has no ordinary categorical colimit in unbased `Hot`, even if one allows an object other than its usual telescope. For cofibration sequences, the manuscript’s surjectivity argument remains correct; its hoped-for injectivity fails through the familiar phantom-map obstruction. Preservation of weak equivalences by filtered colimits is a separate assertion and is true for simplicial weak homotopy equivalences.
4. **The relative homotopy criterion is correct when compatibility is made precise.** Two separately commuting triangles up to homotopy do not suffice. A compatible pair of homotopies, or a comparison of their projections relative to endpoints that permits adjustment, gives the required strict diagonal. The final retraction question also has a negative answer: every stage can retract while even the inverse limit of the sets of retraction components is empty.

These conclusions are supported by the source-by-source records in `SA26_items.json`, the 55-claim map in `SA26_claims.json`, the proofs in `evidence/independent_audit.md` and `agents/b/mathematical_audit.md`, the saved computations, and the literature audit. References below use the keys in `SA26_references.bib`; every verification label refers to an actually opened source, with theorem-level verification distinguished from metadata-only access.

### What the locators and status labels mean

`106/012` means cote 106, scan block 12, not manuscript page 12. All line numbers are one-based physical lines of the supplied `MPL_106+107_transcription.tex`; the hash and page boundaries are in `evidence/source_manifest.json` and `evidence/source_navigation.json`. Notes locators use their own physical lines. The scan blocks begin at 2 in each cote. There is no scan-1 offset to repair. Foot manuscript numbers, upper unit labels and the unrelated computer-listing pagination are different systems.

There are no scans, second-pass files or Codex notes in this attachment. The original TeX is therefore the current textual witness, not a checked image reading. No source reading has been altered. The reading table records mathematical and bibliographic reasons to inspect the ink later; a contradiction in a formula does not prove that the transcriber misread it. The absence of a second pass is expected under the task specification.

An entry verdict concerns what the earlier note says about the supplied text. An item can therefore **agree** with a note that correctly says a manuscript assertion is false. A claim’s `status_on_pages` and `present_status` answer different questions. A step labelled open on the pages may be settled today, and a local “cqfd” may complete only one calculation rather than the surrounding construction. The A–F classification records the relationship to the literature, not truth by itself. In particular, C is used for mixed or under-specified assertions with an established corrected part and a refuted bridge; it does not turn a refuted formula into a current conjecture. B does not assert a documented line of influence from these unpublished pages to later authors. E records standard antecedents or formal consequences, without inventing first-priority dates.

The catalogue’s broad dating and the dated reused computer paper do not establish dates of composition. The reverse-side print dates include 24–25 August 1982 in cote 106 and 4 June 1982 in cote 107. They date the reused paper. The official catalogue’s post-*Pursuing stacks* suggestion is itself qualified. The title/date/page-count audit keeps those facts apart; see `agents/c/scope.tsv` and the provenance records. [MontpellierCatalogue, entries 106–107 and notes 94–95.]

## 1. Cote 106 in manuscript order

### 1.1 Replacement, weak lifts and the cancellation bottleneck — scans 002–006

The opening aim is an equivalence between the localization of the cofibrant subcategory and the localization of the whole category. Grothendieck chooses cofibrant replacements, uses a weak-lifting construction to assign a localized arrow, and then isolates independence of that choice. The necessary cancellation statement says, in the page’s situation, that equality after a weak equivalence implies equality in the localization of the cofibrant subcategory. The source makes subsequent steps conditional on this lemma. It does not prove independence merely by naming the weak lift. These distinctions are items `SA26-1`–`SA26-6`, claims `CL-SA26-106-01`–`07`, and problem `MP-SA26-01`.

The naturality calculation at 106/004 is different: the page actually carries it out and ends that local calculation with “cqfd”. With the typed relations \(\alpha_y=\beta_f i_f\) and \(\beta_f\widetilde f=f\alpha_x\), the identity

\[
\alpha_y i_f^{-1}\widetilde f
=\beta_f\widetilde f
=f\alpha_x
\]

is correct in the localization. It assumes that the preceding construction of the comparison functor is available. It does not remove the earlier choice-independence hypothesis. This resolved local self-flag remains in the problem index as `MP-SA26-05`, so a future companion can show both the successful calculation and its logical boundary.

The earlier entry `MPL_106+107#5` described the later cancellation criterion under a withdrawal heading. Its content was substantially right, but the kind needed correction: the replacement theorem is reformulated conditionally, not retracted as false. Its verdict is **corrected**, with both passages retained.

The exact initial axiom citation is unresolved. Brown’s 1973 paper, Porter’s 1976 dual formulation and Baues’s book do not have interchangeable numbering. The opened Brown text uses axioms A–E; Porter’s C3 is a pushout axiom; Baues’s C3 is factorization and his later weak-lifting lemma is especially close to the source’s usage. This is a bibliographic and mathematical alarm, not permission to replace the handwritten name “Brown” by “Baues”. Brown here is also not automatically the Ronnie Brown named at the end of cote 107. [Brown1973; Porter1976, §2; Baues1989, I §1 and II (1.10).]

For a precise modern comparison this dossier uses the following hypothesis package, denoted **H** in the audit:

- There is an initial object \(0\), and it is cofibrant.
- Weak equivalences contain all isomorphisms and satisfy two-out-of-three. Cofibrations compose, and isomorphisms with cofibrant source are cofibrations.
- For a cofibration \(A\hookrightarrow B\) and a map \(A\to C\), with A, B and C cofibrant, the pushout exists; the induced map from C is a cofibration, and is acyclic if \(A\hookrightarrow B\) is acyclic.
- Every map with cofibrant source factors as a cofibration followed by a weak equivalence.

These are the finite CF1–CF4 hypotheses of the comparison used here. They do not assume functorial factorization, saturation, arbitrary coproducts or a sequential-colimit axiom. Roof constructions below take place in the cofibrant subcategory. The initial object’s cofibrancy is explicit: merely postulating an initial object does not provide the starting factorization of \(0\to X\). Under H, Rădulescu-Banu’s Theorem 6.1.6 supplies the replacement equivalence. Its exact hypotheses are matched; the manuscript’s unidentified shorthand is not silently declared equivalent to them. [RadulescuBanu2009, CF1–CF4 and Theorem 6.1.6.]

### 1.2 The first roof construction and its failed inverse argument — scans 006–012

After restricting to cofibrant objects, the manuscript describes morphisms by components of categories of cospans

\[
X\xrightarrow{a}Z\xleftarrow{s}Y.
\]

In the **first convention**, \(s\) is an acyclic cofibration and \(a\) is unrestricted. Pushouts compose these roofs. The ambiguity of a pushout choice disappears on connected components because canonical comparison isomorphisms give the same component. This ordinary categorical calculation is correct; it should not be conflated with a claim that the entire nerve has the homotopy type of a mapping space.

The attempted inverse comparison runs into a real local obstruction. A weak equivalence need not be a cofibration, so a proposed intermediate roof with that map as denominator need not be an object of the original roof category. The collapse \(\Delta[1]\to\Delta[0]\) in simplicial sets is a weak equivalence and is not a monomorphism. Postcomposing a nonmonomorphism cannot make it monic. Thus an argument that requires such a repair cannot be accepted. The manuscript’s successful localized inverse computation establishes fullness, but its next faithfulness question is still open on 106/012. [Claims `CL-SA26-106-09`–`14`; problem `MP-SA26-02`; saved formal and simplicial certificates.]

A direct universal-property proof resolves the component category under its actual denominator hypotheses. Let S contain identities, be closed under composition and pushout, and admit the needed pushouts. The category of components of strict S-denominator cospans is \(C[S^{-1}]\). Its canonical functor sends \(f\) to \((f,1)\); \((1,s)\) supplies the inverse of an S-map. For a functor F inverting S, the value of a roof is \(F(s)^{-1}F(a)\). An apex map \(u\) with \(us=s'\) has invertible image \(F(u)=F(s')F(s)^{-1}\), which proves invariance on roof components without assuming that u itself belongs to S. The fold map from the relevant pushout verifies the inverse relation. The complete proof is in the independent audit.

The page then doubts whether inverting only acyclic cofibrations already inverts all weak equivalences. Under H with all objects cofibrant, it does. For \(w:X\to Y\) weak, factor

\[
X\amalg Y\xrightarrow{j}Z\xrightarrow{r}Y,
\qquad rj_X=w,\quad rj_Y=1_Y,
\]

where j is a cofibration and r is weak. Both \(j_X\) and \(j_Y\) are acyclic cofibrations by two-out-of-three. Any F inverting them sends \(r\) to \(F(j_Y)^{-1}\), and hence sends w to an isomorphism. This proves the localization universal property, not just an assertion about how many arrows have representatives. Combining it with the preceding cospan argument settles the original roof category. [Claim `CL-SA26-106-15`; problem `MP-SA26-03`; Brown1973, factorization lemma; Baues1989, I (1.8).]

### 1.3 The revised roofs, common refinements and sections — scans 012–016

The manuscript changes the definition while reusing notation. The **revised convention** requires the forward map to be a cofibration and the backward map only to be a weak equivalence. An argument that passes between these conventions without saying so changes its hypotheses. In the revised convention, pushout composition also uses the gluing or excision property for weak equivalences along cofibrations between cofibrant objects. That property follows in the standard setting H; it is not a property of an arbitrary category equipped with a class W. [Claims `CL-SA26-106-16`–`21`; RadulescuBanu2009, Lemma 1.4.2.]

The useful common comparison is as follows. All maps of roofs in this table fix both endpoints and commute strictly.

| Name in this dossier | Forward leg | Backward leg | Additional condition |
|---|---|---|---|
| \(F_0(X,Y)\), first manuscript convention | arbitrary | acyclic cofibration | cofibrant apex |
| \(F_1(X,Y)\), revised convention | cofibration | weak equivalence | cofibrant apex |
| \(J(X,Y)\), comparison category | cofibration | acyclic cofibration | joint map \(X\amalg Y\to Z\) is a cofibration |
| \(R(X,Y)\), auxiliary category | arbitrary | weak equivalence | cofibrant apex |

Factoring the joint endpoint map replaces every roof by one in J. Given an apex map between two roofs, take joint replacements, push out their two apexes over \(X\amalg Y\), and factor the resulting comparison map. This produces a finite zigzag through J. Consequently the inclusions from J into each of \(F_0,F_1,R\) give bijections on components. Joint-cofibration roofs also compose by pushout, so the component bijections for \(F_0\) and \(F_1\) respect their prescribed composition. R is used only for each fixed pair of endpoints; arbitrary R-roofs need not admit a global pushout composition. This proves the component statement for the revised convention, without assuming the manuscript’s final unproved choice-independence statement as an input.

Thomas’s Theorem 3.128 gives an exact literature anchor: its Z-roofs impose precisely the joint-cofibration condition and equal localized maps admit strict common acyclic-cofibration refinements. This is more specific than Brown’s homotopy-commutative fractions or Rădulescu-Banu’s equality criterion with homotopies of numerators. [Thomas2012, Remark 3.124 and Theorem 3.128(a),(b), pp. 128–130; Brown1973, Proposition 2; RadulescuBanu2009, Theorems 6.4.4–6.4.5.]

The manuscript’s final question concerns independence of a section. If \(w:X\to Y\) is weak and \(i,i':Y\to X\) are sections, the two revised roofs \((1_X,i)\) and \((1_X,i')\) map in R to \((w,1_Y)\). The comparison through J transfers this connection back to the revised roof category. The value of these roofs is w; the localized sections themselves are \(w^{-1}\). The distinction avoids an easy direction error. This is an affirmative modern resolution of `MP-SA26-04` under H, while the page itself ends by saying that the remaining construction should be verifiable.

No higher equivalence of nerves follows merely from these component arguments. Cisinski’s Proposition 3.23 and the subsequent work discussed by Horel concern a stronger mapping-space model, with exact roof and factorization hypotheses to be respected. That comparison belongs in the literature map and in a separately scoped future task, not among questions explicitly asked by these pages. [CisinskiK2010, §3.3 and Proposition 3.23; Horel2016, Introduction and Theorem 7.5.]

## 2. Cote 107: presheaves, relative Hom and cotensors

### 2.1 The working notation and the valid core — scans 003–012

Grothendieck begins with a cancelled simplicial draft and restarts with two small categories A and B. The projections are deliberately cross-labelled:

\[
p_B:A\times B\to A,\qquad p_A:A\times B\to B.
\]

The subscript names the other factor. It is not an indexing error to correct globally. Write \(P(A)=\operatorname{Fun}(A^{op},\mathrm{Set})\). In modern notation, \(p_B^*\) is pullback and \(p_{B,*}\) its right adjoint; several plain-text records use `p_B*` for the latter, so the source/target should always be read with the formula.

The ordinary currying equivalences and relative-Hom constructions work. For example,

\[
\operatorname{Hom}_A(X,Y)
=p_{B,*}(Y^X),\qquad
\Gamma_M(X)(a)=\operatorname{Nat}_B(M,X(a,-))
\cong p_{B,*}\bigl(X^{p_A^*M}\bigr)(a).
\]

These are ordinary presheaf operations. Testing on representables and applying Yoneda supplies the calculation written on the pages. The cancelled draft does not make the typed identity false; the active treatment generalizes it. Likewise, applying global sections recovers ordinary Hom sets, and projection direct image of an A-valued B-diagram is evaluation at a terminal object of B when one exists. [Claims `CL-SA26-107-01`–`05`, `07`, `11`; problems `MP-SA26-30`–`31`; SGA4I, Propositions 1.4, 3.4 and 5.1; SGA4IV, 10.1–10.2.1.]

The source correctly distinguishes an A-valued tensor from an ambient presheaf product. If A admits the necessary copowers, define

\[
(X\otimes M)(b)=\coprod_{\sigma\in M(b)}X(b).
\]

This coproduct is taken in A. Its Yoneda image need not be the coproduct of the representable images in \(P(A)\). The natural comparison goes from the latter to the former. With the relevant tensors and cotensors present, the relative tensor–cotensor adjunction holds; its representability hypotheses must accompany it. [Claims `CL-SA26-107-09`–`10`; Kelly1982, §3.7.]

### 2.2 The closure hypothesis the earlier notes missed — scan 008

The statement that enough limits to present M by representables ensure that the entire cotensor \(X^M\) stays A-valued needs qualification. At a general b, the testing weight is \(h_b\times M\). A secure sufficient condition is the existence in A of the limits over \(\operatorname{el}(h_b\times M)^{op}\) that compute every component. Completeness of A suffices. A hypothesis concerning only one presentation of M does not.

The present audit checks a finite obstruction. Let A be the full small skeleton of finite sets of cardinalities \(2^n\), \(n\geq0\); A contains a terminal object and finite products. Let \(B=\Delta\), let \(M=\Delta[1]\), and let X be the nerve of the one-object monoid \(\{1,e\}\), \(e^2=e\). Every \(X_n\) has \(2^n\) elements, so X is A-valued. M itself is representable. Nevertheless the degree-1 value of the ambient cotensor, evaluated on the singleton, consists of commutative squares in this monoid. There is one factorization of 1 and three of e, giving \(1^2+3^2=10\) squares. No A-object has that cardinality. The saved program enumerates all ten, while the written proof checks why this cardinality test obstructs representability.

This is a new check in this audit, not a claim to a new counterexample in the literature. It refutes the weak literal reading of the sufficiency phrase, while leaving open whether the manuscript’s “types requis” and doubtful margin intended the stronger range of weights. The source is not emended. `MPL_106+107#46` is therefore **corrected**, with the original valid subclaims retained and this qualification isolated as item `SA26-122`, claim `CL-SA26-107-06`, problem `MP-SA26-32`. Ordinary density and weighted-limit theory supply the corrected framework; the source match is recorded precisely rather than supplied by analogy. [SGA4I, 3.4–3.5; Kelly1982, §§3.1, 3.7.]

There is a second, smaller boundary in the same entry. A constant presheaf \(\Delta S\) on A is representable exactly when S is a singleton and A has a terminal object. For the statement about all components of a B-diagram, the implication to existence of that terminal object requires \(B\ne\varnothing\). If B is empty the condition on the diagram is vacuous. The proof and counterexample are in claim `CL-SA26-107-08` and problem `MP-SA26-33`; no uncertain “iff” is changed in the transcription.

### 2.3 The false product formulas and the valid specialization — scans 014–016

Three constructions must be separated: an external product of presheaves, the separately continuous extension of a product presheaf, and a representable presheaf on the category \(P(A)\times P(B)\). The last has a genuine fully faithful Yoneda embedding. It does not justify identifying its values with Hom sets between ordinary external products. The overwritten codomain at 107/014 is retained in the reading apparatus.

| Assertion tested | Exact finite test | Verdict |
|---|---|---|
| Separate colimit-to-limit preservation equals joint preservation | \(F(L,M)=\mathrm{Set}(L\times M,2)\); the joint coproduct of \((1,0),(0,1)\) gives 2, while the product of the two values is 1 | False |
| Maps between external products are pairs of factor maps | \(A=B=1\), all four sets of size 2: \(4^4=256\) maps versus \(2^2\cdot2^2=16\) pairs | False; the coordinate swap is one missing map |
| The internal Hom of two external products factors externally | The same terminal-category example gives 256 versus 16 | False |
| Every mixed exponential \((p_B^*L)^{p_A^*M}\) equals \(p_B^*L\) | \(A=B=1\), \(L=M=2\): 4 versus 2 | False |
| Projection pullback preserves exponentials | Yoneda in the second variable gives \((p_B^*L)^{p_B^*L'}\cong p_B^*(L^{L'})\) | True, independently of the preceding false formula |

The finite tests have all the source’s smallness and presheaf hypotheses. There is also a failure of faithfulness of the unrestricted external-product functor when an empty factor erases a choice of map. These examples are reproducible in `code/independent_computations.py`. They establish mathematical falsity of the universal readings, not the exact location of an ink error. Claims `CL-SA26-107-12`–`15` distinguish the correct separate-density extension from the false bridge; claims `18`–`20` distinguish the valid projection identity, the false mixed assertion and the existence hypotheses of the constant-map arrow. [SGA4I, 1.4 and 3.4; SGA4IV, 10.2.1; Kelly1982, Theorem 4.51.]

The interleaf 107/015 contains useful boundary-cotensor scratchwork. With the necessary finite limits, boundary evaluation is the matching object \(M_nX=(\operatorname{cosk}_{n-1}X)_n\), and a map X→Y gives the relative matching map. The abbreviated limit in terms of \(X_{n-1},X_{n-2}\) needs its incidence maps and multiplicities. In particular \(M_0X\) is terminal and \(M_1X=X_0\times X_0\). A computation with the nerve of the group of order two gives eight triangle boundaries but only four filled 2-simplices. This distinguishes boundary data from fillings; all eight boundaries already satisfy their face-compatibility conditions. It does not recover the missing arrows. No Reedy fibrancy theorem is attributed to the page. [Claims `CL-SA26-107-16`–`17`; problem `MP-SA26-34`; RiehlVerity2014, Example 3.22 and Observation 3.23.]

Finally, 107/017 records the standard free-cocompletion property and trials involving opposites. For small A and a suitably cocomplete target M, restriction along Yoneda gives \(\operatorname{Cocont}(P(A),M)\simeq\operatorname{Fun}(A,M)\). Its formal dual has to keep both variance and completeness straight. The deleted box with an uncertain extra superscript does not determine a unique stronger theorem. It is class F, not a licence to supply a derived duality from another project. [Claims `CL-SA26-107-21`–`22`; problem `MP-SA26-36`; Kelly1982, Theorem 4.51.]

## 3. Cote 107: ordinary colimits, relative homotopies and retractions

### 3.1 Three distinct assertions — scans 019–021

The opening question is literally whether filtering direct limits exist in `Hot`. The subsequent displayed Hom bijection makes this an ordinary categorical universal property. Existence of a homotopy colimit of a coherent diagram is a different statement.

The source proposes replacing a countable system by one with monomorphism transitions and weakly equivalent terms. It then separates (i) whether the new union is an ordinary colimit in the homotopy category and (ii) whether the map between the two unions is weak. The model-category factorization constructs the replacement under appropriate hypotheses. For ordinary simplicial weak equivalences, (ii) is true for arbitrary filtered diagrams, without assuming monomorphisms in the lower sequence. Kerodon Proposition 3.2.8.3 is an exact source for this closure property. For an unspecified W, that closure theorem must still be supplied separately. [Claims `CL-SA26-107-24`–`25`; problem `MP-SA26-38`; Kerodon00XE; Quillen1967.]

The nerve’s preservation of filtered colimits is also correct. At simplicial degree n, a functor \([n]\to C\) is finite object, arrow and equation data. In a filtered colimit it appears at one stage; equality of two such functors is witnessed at a later common stage. This proves both directions of the levelwise comparison. It does not show that localization preserves these colimits. [Claim `CL-SA26-107-23`; item `SA26-118`; independent finite-data proof in `agents/b/mathematical_audit.md`.]

### 3.2 Surjectivity works; injectivity fails — scans 021–025

For cofibrant \(X_i\) with cofibration transitions and fibrant Y in a simplicial model category, the restriction maps \(\operatorname{Map}(X_{i+1},Y)\to\operatorname{Map}(X_i,Y)\) are Kan fibrations. A compatible sequence of homotopy classes can be represented by strictly compatible maps: choose a representative at the first stage and inductively lift paths to adjust each next representative. The maps then glue over the ordinary colimit. This proves the surjection

\[
[\operatorname{colim}_iX_i,Y]\twoheadrightarrow
\varprojlim_i[X_i,Y].
\]

It is the successful part of the manuscript’s argument. Compatible cylinders give the corresponding ordinary-model-category version. The statement does not supply uniqueness of the choices. [Claims `CL-SA26-107-28`–`29`, `32`; problem `MP-SA26-39`; Quillen1967, II §2 Proposition 4; Hirschhorn2015, Theorem 2.1.]

For failure of injectivity, fix a prime p and let T be the mapping telescope of degree-p circle maps. Each finite subtelescope \(T_i\) retracts onto its final circle, while

\[
H_1(T;\mathbb Z)=\mathbb Z[1/p],\qquad
H^2(T;\mathbb Z)
\cong\operatorname{Ext}^1(\mathbb Z[1/p],\mathbb Z)
\cong\mathbb Z_p/\mathbb Z\ne0.
\]

Taking \(Y=K(\mathbb Z,2)\), every finite-stage restriction is nullhomotopic, but some global maps are not. This realizes the manuscript’s precise monomorphism setting by \(X_i=\operatorname{Sing}(T_i)\) and a Kan target: compactness of a singular simplex bounds its telescope height, so the simplicial union is exactly \(\operatorname{Sing}(T)\). The earlier notes’ example survives an independent check of these hypotheses. [Items `SA26-115`–`116`; claims `CL-SA26-107-26`–`27`, `33`; Milnor1962, Lemma 2; Hatcher2002, Examples 3F.3, 3F.7 and 3F.9.]

The algebra was also redone. The free resolution has differential \(e_n\mapsto e_n-pe_{n+1}\). After applying Hom into \(\mathbb Z\), its cokernel is that of \(\delta(a)_n=a_n-pa_{n+1}\). The map \(b\mapsto\sum p^n b_n\pmod{\mathbb Z}\) identifies this cokernel with \(\mathbb Z_p/\mathbb Z\). Surjectivity follows from p-adic digits; if the sum is an ordinary integer m, the integers

\[
a_n=\frac{m-\sum_{k<n}p^kb_k}{p^n}
\]

give a preimage. The alternating digit sequence 1,0,1,0,… represents \(1/(1-p^2)\), not an ordinary integer. Saved computations verify the finite telescoping identity and residues; the written argument, not finite testing, proves the infinite assertion.

There is a stronger consequence, already proposed in the earlier notes and independently reproved here: **the degree-p circle sequence has no ordinary colimit object in unbased `Hot` at all**. If L were one, testing discrete targets would make L connected. Testing \(K(G,1)\) for all abelian groups G, naturally in G, would force \(H_1(L)=\mathbb Z[1/p]\) by Yoneda in abelian groups. Testing \(K(\mathbb Z,2)\) would force \(H^2(L;\mathbb Z)=0\). The universal coefficient injection from \(\operatorname{Ext}^1(H_1L,\mathbb Z)\) contradicts this. The argument uses unbased cohomology representability and no finite-generation assumption. It is not attributed verbatim to Milnor or Hatcher, and no historical priority is claimed. [Problem `MP-SA26-37`; Hatcher2002, Theorems 3.2 and 4.57 and the unbased qualification.]

### 3.3 The relative square and the last retraction question

For a strict square \(pg=g'i\), with i a cofibration between cofibrants and p a fibration between fibrants, a proposed \(\varphi:B\to E\) can be changed within its homotopy class to a strict diagonal exactly when the triangle homotopies can be chosen compatibly. In a simplicial model category, this is path lifting for

\[
\operatorname{Map}(B,E)\longrightarrow
\operatorname{Map}(A,E)
\times_{\operatorname{Map}(A,F)}
\operatorname{Map}(B,F).
\]

A comparison of the projected paths relative to endpoints permits adjustment to strict compatibility. Without endpoint control the argument does not apply. In a general model category one must use compatible cylinders or framings rather than assume a simplicial tensor. The manuscript’s surviving margin already says “iff”: necessity is not a later editor’s addition. [Item `SA26-117`; claims `CL-SA26-107-30`–`32`; problem `MP-SA26-40`; Quillen1967, II §2 Proposition 4, read also as Proposition 2.2.4 in QuillenRetypeset2022.]

The covering map \(\mathbb R\to S^1\) against \(\partial I\hookrightarrow I\), with endpoint lifts 0 and 1, constant base path at 1 and proposed diagonal \(\varphi\) constant at 0, checks the failure of automatic compatibility. Both triangles commute up to homotopy. A strict lift of the constant base map would lie in the discrete fibre \(\mathbb Z\), so cannot join 0 to 1. The one-endpoint extension used for surjectivity is an acyclic cofibration; the two-endpoint inclusion needed for injectivity is generally only a cofibration. Fibrancy therefore supplies the former lift, not the latter. [Problem `MP-SA26-41`; full counterexample and cylinder checks in the independent audit.]

The final “Ask Ronnie Brown!” question asks for compatible components of retractions, not just a retraction at each stage. From a nonzero phantom \(f:X_\infty\to Y\), with Y Kan, and the constant map c, form

\[
Z_i=Y\amalg_{X_i\times\partial\Delta[1]}
(X_i\times\Delta[1]),
\]

using endpoint maps \((f_i,c_i)\). All inclusions are monomorphisms and each \(Z_i\) retracts onto Y, because \(f_i\) is null. A retraction of the union would nullhomotope f. Moreover the retraction spaces form a tower of Kan fibrations, so a compatible sequence of components could be made into compatible actual retractions. It follows that even \(\varprojlim\pi_0\operatorname{Retr}(Z_i,Y)\) is empty. This checks the exact final question. It does not revise any differently quantified invariant-ind-object problem in a private project register. [Item `SA26-119`; claim `CL-SA26-107-34`; problem `MP-SA26-42`.]

## 4. Literature, chronology and the earlier notes

The searches were organized by exact statement families, followed backwards when broad titles were insufficient. The search logs record the queries, accessible sources, failed or limited access and which claim family each search served. The bibliography distinguishes opened theorem text from an opened catalogue or publisher record. A reference marked verified is real and opened; the accompanying audit says what was actually checked. No inaccessible book body is treated as though it had been read. In particular, the scoped relative lifting argument uses the read Quillen text rather than relying on the earlier notes’ Hovey citation.

Chronology is not collapsed into a single year. Milnor’s paper records receipt in February 1961 and publication in 1962. Brown’s paper records receipt and revision dates, and mentions earlier thesis work; that is not an established first-public-circulation date for every result. Quillen’s book was published in 1967; a modern retypesetting has different numbering and does not settle the original page numeral in the manuscript’s citation. SGA4’s seminar dates and 1972 publication are distinguished from the date of the consulted electronic reedition. Baues’s first publication in 1989 is distinguished from its 1988 copyright. Rădulescu-Banu’s arXiv versions, Thomas’s August 2012 dissertation and consulted March 2017 revision, Cisinski’s online and volume dates, and Horel’s arXiv and journal dates are recorded separately in the claim records. Where a first circulation was not established, the dossier says so.

The ordinary mathematics in the earlier notes is often more careful than its long project concordances might suggest. Their finite-set objections, distinction between projection and mixed exponentials, telescope example, stronger nonexistence proof, relative-square criterion and retraction construction all survive direct checking. Their separation of the two roof conventions is essential. The two entry-level corrections are limited and substantive: the kind of the conditional replacement reformulation (`#5`), and the hypotheses attached to the compound presheaf review (`#46`). Many entries are merged because they repeat a claim, a reading alarm or a completion report; a merged verdict is not a negative mathematical judgment.

The review also prevents several overextensions. A source arrow whose type is unclear is not repaired by mathematical plausibility. A computation of \(\pi_0\) is not a proof of a higher mapping-space equivalence. A known homotopy colimit does not supply an ordinary colimit in `Hot`. A correctly proved W∞ example does not settle every localizer W. The complete standard arguments are attributed to the present audit or the earlier notes as appropriate, not retroactively inserted into Grothendieck’s page.

## 5. Links and the limits of provenance evidence

`SA26_links.tsv` separates archive-folder links, published-work parallels and the earlier runs’ links to other projects. Public parallels were checked at both accessible passages. The full 2015 electronic edition of *Pursuing stacks* supplies the inspected late sections; they must not be cited as though all appeared in the SMF 2022 first volume. That volume contains §§1–91 and 95–98, whereas the main late parallels here include §§110, 115, 119, 125 and 136–139. In particular §125 begins at old manuscript p. 531; p. 530 belongs to §124. A later related passage does not by itself establish a published correction of the exact assertion in cote 106 or 107. [GrothendieckPS2015, §125, pp. 531–533; GrothendieckPS2022, Notice to the reader; MaltsiniotisPS.]

The public *Dérivateurs* originals permit specific comparisons: the ordinary-colimit and coherent-choice discussions, the later representability warning, and the four-object example whose proposed circle retraction is corrected to the homotopy type of a 2-sphere. These checks establish the passages and the mathematical relationship stated in the link rows. They do not verify a private companion’s commentary, a claimed finite-category census, a minimality theorem or a private result status. Nor do they establish a direction of influence without dated evidence. [GrothendieckDER_V, manuscript pp. 43–49; GrothendieckDER_XVIII, §4.2, manuscript pp. 61–64; GrothendieckDER_XII_App, §2.6, manuscript pp. 10–12, footnote 7.]

The supplied notes contain 255 individual STRATA/PATHS and BISITE/RESIDUE concordance rows, plus 12 numbered NEW_RESULTS entries and three Known-after-all notices, K1–K3. These are preserved in their own tables with note locations and run paths, alongside the selected status and provenance information. The private context packets, result CSVs, complete inventories, old run logs and hash lists were not attached. The audit verifies what the notes report and, where possible, the public mathematical endpoint; it does not certify an unavailable private result. The reported 42 SHA-256 values (41 page fragments and the combined text), 1,202-row inventory and historical visual/build reports are explicitly attributed to the K-completion tail. They are not misattributed to the earlier H-completion checklist and are not represented as checks performed in this run. [Items `SA26-207`, `SA26-210`; PrivateResultsState; PrivateDossierStatements; PrivateNewResults.]

A later public retrieval succeeded for the three specific Hua findings. Their actual source text and stable Git-blob identities are recorded in `agents/c/public_project_endpoints.tsv`. The displayed labels on 19 November 2026 are **candidate** for the 106 section criterion, **matched** for the 107 sequential-colimit finding, and **unsearched** for the relative-square finding. These labels are verified reports of that project, not mathematical statuses adopted by this dossier. The public 106 report names Baues, which does not decide the supplied Brown reading. The relative-square report questions autograph necessity, whereas the supplied transcription preserves an active “iff”. That disagreement is documented at the level of the two witnesses.

The displayed Lean sources were inspected for scope. The 106 file treats the revised roof convention and explicitly assumes all objects cofibrant for the relevant conclusion; its ambient class has stronger global assumptions before that restriction. The 107 file covers strict compatibility under the required relative-cylinder lifting hypothesis and explicitly excludes the endpoint-relative variant and a proof of general cylinder existence. **No Lean compiler or kernel execution was performed here**, and a report of an earlier review was not reproduced as a new check event. The link register therefore contains three checked public project reports alongside fifteen grouped private targets whose originals remain unavailable. [HuaFindings; HuaLean106; HuaLean107; `agents/c/evidence/public_project_scope.md`; `agents/a/lean106_scope_review.md`.]

This is the evidence boundary for Stage 5: all recoverable source endpoints and public targets have been checked, and every inaccessible private target is explicitly marked as an attributed lead. Treating those targets as verified would invent evidence. The separate tables preserve them so a later run with the actual project packets can verify the private claims independently without reopening the manuscript audit.

## 6. What is worth doing next

`SA26_directions.md` ranks bounded follow-up tasks by mathematical interest and what one run of a few hours could establish. The most useful immediate work is an ink-and-axiom audit of cote 106, a companion treatment of the cotensor hypothesis and its finite counterexample, and a precise account of the ordinary-colimit obstruction. A higher comparison of the revised roof categories is a separate, explicitly modern question; it is not added to Grothendieck’s problem index. Likewise, any investigation of positive injectivity hypotheses should start with a fixed class of targets and the exact \(\lim^1\) obstruction, rather than reopen the unrestricted assertion already refuted here. None of these directions is developed beyond its stated first step in the directions file.

## 7. Coverage and counts

<!-- COUNTS_START -->
| Measure | Count |
|---|---|
| Indexed entries | 63 |
| Consolidated items | 64 |
| Verdicts: kept / merged / corrected / withdrawn / rests on a misreading | 51 / 10 / 2 / 0 / 0 |
| Claims; all with recorded searched fate | 55 |
| Problems and self-flags, including resolved local checks | 20 |
| Reading-review rows; no ink decisions | 45 |
| Ranked directions | 8 |
| Link rows | 64 |
| Bibliography records: verified / unverified | 47 / 6 |
| Recorded check events | 394 |
| Supplied scan blocks: cote106 / cote107 | 16 / 25 |
| Whole-topic cotes: evaluated in this part / orientation only | 2 / 13 |

### Claims by literature class

| Class | Count |
|---|---|
| A | 0 |
| B | 14 |
| C | 6 |
| D | 0 |
| E | 34 |
| F | 1 |

### Claims by status on the pages

| Status | Count |
|---|---|
| proved there | 7 |
| proof sketched | 17 |
| stated without proof | 14 |
| corrected by himself later | 4 |
| false as stated | 4 |
| open on the pages | 9 |

These counts group the leading status categories. The JSON retains each qualification, including conditional proofs, same-page corrections and unfinished sufficiency arguments.

### Items by kind

| Kind | Count |
|---|---|
| conjecture | 1 |
| idea of the earlier run | 10 |
| other | 5 |
| reading question | 13 |
| self-flagged step | 10 |
| title, date or page count | 2 |
| unproved claim | 13 |
| unpursued implication | 5 |
| withdrawn in the same text | 5 |

### Text checks on consolidated items

| Text check | Count |
|---|---|
| agrees | 56 |
| not on the page | 4 |
| overstates | 1 |
| understates | 3 |

### All folders in TOPIC.md

| Cote | Catalogue title | Catalogue pages | This part |
|---|---|---|---|
| 103 | Courrier [Correspondance sur la thèse de Sinh][91] : copies d'article annoté (1974), lettres (1974). | 17 | Orientation only; out of this part |
| 104 | [Champs (stacks) 1][92] : copies de notes manuscrites (s.d.). | 16 | Orientation only; out of this part |
| 105 | [Champs (stacks) 2] : notes manuscrites (s.d.). | 52 | Orientation only; out of this part |
| 106 | [Champs (stacks) 3] : notes manuscrites (s.d.). | 16 | Evaluated; all supplied text read |
| 107 | Closed models [notes postérieures à PS ?] : notes manuscrites (s.d.). | 25 | Evaluated; all supplied text read |
| 108 | Divers, liste questions : notes manuscrites (s.d.). | 5 | Orientation only; out of this part |
| 109 | Tables [Corrections et préparation à l'édition][98] : notes manuscrites (s.d.), copies de notes manuscrites annotées (s.d.), copies de tapuscrit annoté (s.d.), copies de notes manuscrites (1983-1984). | 37 | Orientation only; out of this part |
| 111 | Tapis de Quillen [notes du 10/09/1968][99] : copies de tapuscrit annoté (1968). | 16 | Orientation only; out of this part |
| 112 | Linéarisation : notes manuscrites (s.d.). | 4 | Orientation only; out of this part |
| 113 | Abelianization : notes manuscrites (s.d.). | 12 | Orientation only; out of this part |
| 114 | Asphéricité[102] : notes manuscrites (s.d.). | 5 | Orientation only; out of this part |
| 115 | " Correspondances " fonctorielles. Dualité des topos : notes manuscrites (s.d.). | 14 | Orientation only; out of this part |
| 116 | Mapping-cône etc. : notes manuscrites (s.d.). | 10 | Orientation only; out of this part |
| 117 | Théories homotopiques : notes manuscrites (1983, s.d.). | 25 | Orientation only; out of this part |
| 118 | Cohomology properties of maps in (Cat) : notes manuscrites (s.d.). | 40 | Orientation only; out of this part |

One additional item, `SA26-125`, records an existence-hypothesis alarm found directly in the transcription; its empty `sources` list is intentional. Compound indexed entries can supply several items, while repeated entries can merge into one item, so the item count need not equal63. The reading count includes one explicit guard preserving the cross-labelled projection convention. The342 source doubt rows and270 contextual leads are documentary source counts, not extra claims or additional entry verdicts. ID gaps reserve the reader partitions and do not denote missing entries.

<!-- COUNTS_END -->

## 8. Reproducibility and check events

The archive contains the requested canonical JSON and TSV files, the complete bibliography, the integrated check-event table, UTC progress logs, authored evidence notes, the programs that generated the mechanical indexes and certificates, and their outputs. The attached source package and downloaded reference caches are excluded. A source hash and archive manifest permit exact identity checks without redistributing the inputs.

The entry decisions were made by reading entries and passages, not by matching headings or keywords. Scripts assemble those manually authored decisions, check referential integrity, count rows and execute the finite certificates. `CHECK_EVENTS.tsv` separates textual comparison, use of a checked reference result, targeted proof checks, independent proofs, finite computations and refutations. A source reading is never labelled an independent proof. The model’s effort setting was inherited but not separately exposed; the log does not invent a “max” setting. Mathematical confidence, textual uncertainty and the absence of a historical source are stated separately where they differ.

The infinite Ext calculation, the nonexistence of an ordinary colimit, the compatible-homotopy criterion and the roof universal property have written arguments. Their finite programs are supporting certificates with explicit limits, not substitutes for proofs. The source TeX remains byte-for-byte unchanged. All final record counts, cross-references, required fields and bibliography keys were checked by the saved integration validation.
