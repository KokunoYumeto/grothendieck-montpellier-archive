# SA26 — Autour de *Pursuing Stacks*

## Part 2: cotes 106 and 107

**Consolidation and mathematical status as of 19 November 2026.** This dossier covers every entry of the supplied part-2 index and the complete supplied transcription. Its three main subjects are Grothendieck’s construction of localized Hom-sets by short fractions, his ordinary presheaf formalism of relative Hom, tensors and cotensors, and his question about filtered colimits in the ordinary homotopy category. These are the organizing subjects of the dossier. Comparisons with *Les Dérivateurs*, La Longue Marche and the earlier research returns are kept in a separate section and tables.

The central conclusions are these:

1. **The standard cofibration-category version of the cote 106 localization programme works.** The written argument ends with a section-independence problem. Under the explicit finite Brown-style axioms used below, acyclic cofibrations already generate the localization, both short-roof component constructions give the localized Hom-set, and the section ambiguity disappears. The manuscript’s abbreviated “C1–C3” is not identified by supplying those modern axioms.
2. **Much of cote 107’s first unit is valid ordinary presheaf theory, but several sweeping formulas are false.** Relative evaluation, copowers and the projection inverse-image formula survive careful typing. Separate continuity is not joint continuity; an unrestricted product-Hom formula fails on two-element sets. Cotensor closure and constant-coefficient assertions require precise hypotheses.
3. **The final unit separates a true stability statement from a false ordinary-colimit hope.** Every fundamental localizer on categories is stable under filtered colimits, by Cisinski’s exact theorem; its induced presheaf weak-equivalence class has the same stability. Ordinary sequential colimits in the usual homotopy category nevertheless need not exist. The degree-\(p\) circle sequence supplies a proof, and its telescope supplies nonzero maps invisible at every finite stage.
4. **The relative lifting problem has a real compatibility condition.** With cofibrant sources, fibrant targets and the stated cylinder or simplicial structure, the surviving existential criterion is correct when the projected homotopies agree or are homotopic relative to their endpoints. Two triangle homotopies chosen independently do not suffice.
5. **The private-project concordances do not add hundreds of manuscript claims.** The 255 STRATA/PATHS/BISITE/RESIDUE statements have no complete match in these leaves. Their inherited proof labels are preserved as provenance, never counted as results of this dossier.

The mathematical proofs and computation outputs are included. No source reading has been changed. No image of the manuscript was supplied, and every proposed reading remains a question for the ink.

## 1. Corpus, numbering and the boundary of this part

The input has six files: the index, Pro notes, Pro doubts, the transcription, its preamble, and `TOPIC.md`. There is one package, `MPL_106+107`, with 63 indexed `###` entries. The transcription has 2,774 physical lines and 41 `scanpage` blocks: 106/002–017 and 107/002–026. Its SHA-256 is

`516a428d7992190dbc5aa630f0c065214ccb54909e6633801e272ffeeb9237f9`.

That hash agrees with the frozen text identified by the later notes. The manifest records hashes of all six supplied files. The absent private inventories and previously reported 42-file audit were not reconstructed or treated as current checks.

**Locator convention.** A locator such as `107/021, L2472–2486` means cote 107, package scan 21, and one-based physical lines of `MPL_106+107_transcription.tex`. These are not invented manuscript line numbers. Original manuscript page labels in the public *Pursuing Stacks* and *Dérivateurs* editions are identified as such; they are not interchangeable with these scan numbers or with PDF page indices.

The complete `TOPIC.md` orientation is retained here. “Other part” means the source explicitly assigns it elsewhere; it does not mean the present run inspected those manuscripts.

| Cote | Catalogue subject, abbreviated | Catalogue pages | Coverage in this dossier |
|---|---|---:|---|
|103|Correspondence concerning Sinh’s thesis; 1974 material|17|Other part; orientation only|
|104|Champs (stacks) 1|16|Other part; orientation only|
|105|Champs (stacks) 2|52|Other part; orientation only|
|106|Champs (stacks) 3|16|All supplied scans 002–017|
|107|Closed models; catalogue asks whether later than PS|25|All supplied scans 002–026|
|108|Miscellaneous questions|5|Other part; orientation only|
|109|Tables, corrections and preparation for publication|37|Other part; orientation only|
|111|Tapis de Quillen; notes dated 10 September 1968|16|Other part; orientation only|
|112|Linéarisation|4|Other part; orientation only|
|113|Abelianization|12|Other part; orientation only|
|114|Asphéricité|5|Other part; orientation only|
|115|Functorial correspondences; duality of topoi|14|Other part; orientation only|
|116|Mapping-cone and related material|10|Other part; orientation only|
|117|Théories homotopiques|25|Other part; orientation only|
|118|Cohomology properties of maps in Cat|40|Other part; orientation only|

The official Montpellier catalogue was also opened [MontpellierCatalogue]. Its qualification concerning cote 107 is retained as a question. There is no basis here for assigning all these leaves to 1983, or for declaring them earlier or later than *Pursuing Stacks*.

The foot numbering runs 1–16 in 106 and 1–25 in 107. Additional unit numbers and letters coexist with it. Cote 107/002 calls its first formalism provisional; 107/018 starts a separate title for the filtered-colimit question. Machine `PAGE` numbers belong to the reused printouts. Dates of 24–25 August 1982 occur on stock in 106, and 4 June 1982 on stock in 107. They provide sheet-specific lower bounds for reuse, not a composition date for the whole packet. Mathematical diagrams on 106/013, 106/015, 107/022 and 107/024 were included in the audit even though those sheets also carry computer output. The printed programs were not mistaken for Grothendieck’s mathematical computations. [SA26-34]

## 2. Cote 106: from cofibrant replacement to short fractions

### 2.1 The opening theorem and its proof obligation

At 106/002, Grothendieck calls the equivalence induced by cofibrant replacement known:

\[
C_{\mathrm{cof}}[(W\cap C_{\mathrm{cof}})^{-1}]
\longrightarrow C[W^{-1}].
\]

He nevertheless tries to construct it directly. A weak replacement of each object and an enlarged-target lift of each arrow would define a quasi-inverse. The obstacle is independence of those choices. Given maps \(\varphi,\psi:x\to y\), with \(x,y\) cofibrant, and a weak equivalence \(\alpha:y\to z\) such that \(\alpha\varphi=\alpha\psi\), he needs their equality already in the localization of the cofibrant subcategory. The sentence conditioning the construction on this lemma is substantive. The trial diagrams on scan 003 do not turn it into a completed proof. [SA26-1, SA26-2; C-SA26-106-01–04; MP-SA26-01]

The calculation on scan 004 does prove naturality **once the functor exists**. If \(\alpha_y=\beta_f i_f\) and \(\beta_f\widetilde f=f\alpha_x\), then

\[
[\alpha_y][i_f]^{-1}[\widetilde f]
=[\beta_f][\widetilde f]=[f][\alpha_x].
\]

The source writes the check and closes it. It should neither be left in an undifferentiated list of open steps nor used to discharge the separate choice problem. Scan 006 reformulates the replacement theorem as a cancellation criterion. It does **not** explicitly retract the theorem, correcting the stronger implication of note #5’s combined withdrawal/reformulation label. [SA26-4; C-SA26-106-05; MP-SA26-06]

### 2.2 The sufficient modern assumptions used in this dossier

The reconstruction uses the CF1–CF4 precofibration axioms: a cofibrant initial object; composition-stable cofibrations and the specified isomorphisms; two-out-of-three for weak equivalences; pushouts of a cofibration A → B with A cofibrant along a map A → C with C cofibrant, preserving cofibrations and acyclic cofibrations; and factorization of a map with cofibrant source as a cofibration followed by a weak equivalence. After restricting to cofibrant objects, all objects under discussion are cofibrant. Finite coproducts then follow. No infinite-coproduct axiom, sequential-colimit axiom, functorial factorization or saturation is needed for the 106 proofs.

This package is called **H106** in the detailed proof file. It is a stated sufficient reconstruction. Brown’s original checked axioms use different lettering, so the letters on the manuscript are still a reading and bibliographic question. Brown’s 1973 factorization and weak-lifting results, together with the precise modern replacement theorem in Rădulescu-Banu, support this interpretation [Brown1973, I.2; RB2009, Definition 1.1.1 and Theorem 6.1.6]. They do not resolve the ink.

The missing cancellation lemma follows directly under these assumptions. Factor the fold \(x\amalg x\to x\) to obtain a cylinder. Its two endpoints are acyclic cofibrations. Weak lifting against \(\alpha\) gives, after an acyclic enlargement of \(y\), a homotopy between \(\varphi\) and \(\psi\). The endpoints become equal after localization because each is inverse to the cylinder contraction. Cancellation of the enlarged weak equivalence gives the required equality. The codomain \(z\) need not be cofibrant. The complete construction is in `parts/cote106/proof_checks.md`, §1.

### 2.3 The original roofs, their composition and the failed inverse argument

From scan 006, all objects are taken cofibrant. The first roof category has diagrams

\[
x\longrightarrow z\xleftarrow{\sim\,\mathrm{cof}}y.
\]

Pushout composes them. Associativity before taking components is through canonical isomorphisms; the induced composition on \(\pi_0\) is strictly associative. The morphisms used here are strict middle maps fixing the two endpoints, **not necessarily cofibrations**. Their weakness, where needed, follows from two-out-of-three. This convention matters to the localization proof. [C-SA26-106-06–08]

Grothendieck attempts to show that every weak equivalence becomes invertible. His particular zigzag passes through a denominator that need not be a cofibration. He notices this and tries to repair it by postcomposition. Scan 010 explicitly rejects that repair: postcomposing a nonmonomorphism cannot make it monic. The finite-set example in the audit checks every H106 axiom with all maps weak and injections cofibrations. The constant map from a two-element set to a singleton remains noninjective after every postcomposition. The general categorical cancellation argument, rather than the finite enumeration, proves the unrestricted assertion. [SA26-9; C-SA26-106-09–10]

The same page establishes surjectivity of the effect functor to the localization. Its equality \([w][i]^{-1}[g]=1\) is valid in the target localization. It does not by itself establish the inverse identities in the roof-component category. Scan 012 correctly isolates faithfulness as the remaining issue. [C-SA26-106-11–12; MP-SA26-02]

### 2.4 Why acyclic cofibrations already suffice

The author doubts that inverting \(W_0=W\cap\mathrm{cof}\) can invert all of \(W\). Under H106 it does. For \(w:x\to y\) weak, factor

\[
x\amalg y\xrightarrow{(a,b)}Q\xrightarrow{r}y,
\qquad ra=w,\quad rb=1_y,
\]

with the first map a cofibration and \(r\) weak. Both \(a\) and \(b\) are acyclic cofibrations. A functor inverting them sends \(r\) to \(F(b)^{-1}\), and hence sends \(w\) to \(F(b)^{-1}F(a)\). Thus it inverts every weak equivalence. This is a finite factorization argument; it does not presuppose the faithfulness being proved. [SA26-18; C-SA26-106-13; MP-SA26-03]

There is also a direct ordinary universal-property proof for the original roofs. If a denominator class \(D\) contains identities and is closed under composition and cobase change and the required pushouts exist, components of strict \(D\)-roofs localize \(D\). A \(D\)-inverting functor sends a roof \((a,s)\) to \(F(s)^{-1}F(a)\); strict roof maps and pushout composition preserve this value. The fold from \(z\amalg_y z\) supplies one of the inverse comparisons. Applying this to \(D=W\cap\mathrm{cof}\), then using the factorization above, proves the original roof theorem. No assertion about the nerve of the roof category follows merely from this ordinary argument.

### 2.5 The revised roofs and section independence

Scan 012 changes the convention: the **forward** map is now a cofibration and the backward map merely weak. Scan 014 deletes an ill-typed shortcut and instead factors an arrow, obtains a section of a weak map, and asks whether the result is independent of choices. Scan 016 constructs a common factorization and preserves sections through it, but ends with the independence of the section itself still to prove. The diagrams on scan 015 support the finite-coproduct closure used in this construction. [C-SA26-106-14–18; MP-SA26-04]

The detailed proof compares both restricted roof categories with unrestricted weak-denominator roofs by factoring the **joint map** \(x\amalg y\to z\). A strict map between two roofs induces a finite zigzag between their joint-map replacements. This proves the necessary bijections on connected components. It does not claim that any two roofs have one common strict refinement or that a \(\pi_0\) proof establishes a mapping-space equivalence. Two section roofs map to the same unrestricted roof and are therefore connected in the revised model. The section roof represents \([w]\); the section map represents \([w]^{-1}\). Keeping those two variances apart removes another possible source of confusion.

Modern strict short-roof results provide a stronger framework [Cisinski2010K, Proposition 3.23; Horel2016]. The modified forward-cofibration \(\pi_0\) comparison used here is explicitly proved in the dossier; it is not attributed verbatim to a theorem that uses homotopy fractions or a different roof convention.

Composition closure for the revised F1 roofs uses the excision consequence of the stated finite axioms [RB2009, Lemma 1.4.2]; it is included in the detailed check.

The couniversal-denominator proposal has a separate boundary. Couniversality supports pushout composition; it does not alone show that all weak equivalences are inverted. A broader recognition problem would require a specified relative category and additional assumptions. [MP-SA26-05; BataninBerger2017, §1]

## 3. Cote 107, first unit: ordinary relative Hom, powers and copowers

### 3.1 Preserve the author’s projection convention

Write \(P(A)=\mathrm{Set}^{A^{op}}\). The manuscript uses crossed subscripts:

\[
p_B:A\times B\longrightarrow A,\qquad p_A:A\times B\longrightarrow B.
\]

That convention is intentional and is retained. A presheaf on \(A\times B\) is a \(B^{op}\)-diagram of presheaves on \(A\), or symmetrically an \(A^{op}\)-diagram on \(B\). The right adjoint \(p_{B*}\) takes the pointwise limit over \(B^{op}\). Relative internal Hom followed by global sections recovers ordinary natural transformations. These statements concern ordinary presheaves, without a weak-equivalence class or derived functor. [C-SA26-107A-01; SGA4I, Exposé I, 1.4, 3.4–3.5, 5.1]

For \(M\in P(B)\), the displayed relative evaluation is

\[
(\Gamma_M X)(a)=\operatorname{Nat}(M,X(a,-)),\qquad
\Gamma_M X\cong p_{B*}[p_A^*M,X].
\]

At a representable \(M=h_b\), it gives \(X(-,b)\). The audit repeats the whole adjunction chain and flags uncertain subscripts by type, without changing them. A cancelled componentwise exponential formula is mathematically valid; its cancelled textual status must not be converted into a claim that the formula is false. If \(B\) has a final object \(b_0\), \(p_{B*}\) reduces to evaluation at \(b_0\). For \(B=\Delta\), this is degree zero. [C-SA26-107A-02–04]

### 3.2 Exactly which limits cotensors require

For an \(A\)-valued diagram \(X:B^{op}\to A\), the presheaf cotensor by \(M\) is represented at \(b\) whenever the appropriate limit in \(A\) exists:

\[
(yX)^{p_A^*M}(-,b)
\cong\lim_{\operatorname{el}(h_b\times M)^{op}}
y_A X(q(-)).
\]

Here \(q:\operatorname{el}(h_b\times M)^{op}\to B^{op}\) is the projection sending an element to its underlying object of \(B\). Consequently completeness of \(A\) suffices; more precisely, the required limit shapes involve **every \(h_b\times M\)**. The phrase on scan 008 about limits needed to present \(M\) is insufficient if interpreted as just one presentation of \(M\). A finite counterexample checks this distinction: take \(B=(x\to t\leftarrow y)\), \(A\) discrete on two objects, \(X\) constant at one of them, and \(M=h_x\). At \(b=y\), the weight \(h_y\times h_x\) is empty; the resulting terminal presheaf on \(A\) is not representable. All stated finite objects and values are enumerated in the code. This is an interpretation/hypothesis alarm, not evidence deciding the handwriting. [C-SA26-107A-05; MP-SA26-41]

For simplicial objects and simplicial sets with finitely many nondegenerate simplices, finite limits give the familiar finite cotensor construction. The precise finite scope is essential; it is not a claim about arbitrary simplicial sets with finite homotopy type. The exact modern finite-limit formulas are identified in the reference ledger.

A related small qualification affects the constant-presheaf test. A constant presheaf represented by an object of \(A\) must have singleton value, and that object is final. Thus, **when \(B\ne\varnothing\)**, \(p_A^*M\) is pointwise \(A\)-valued exactly when \(M\) is terminal and \(A\) has a final object. For empty \(B\), pointwise representability is vacuous. The unrestricted compound iff needs that exception, although it does not affect the intended simplicial case. [C-SA26-107A-06]

### 3.3 Copowers are not pointwise products of represented presheaves

The ambient exponential adjunction is valid. The additional assertion that its objects remain in \(A\) is another question. For a represented object \(a\) and a set \(S\), the presheaf \(h_a\times\Delta S\) is representable precisely when \(S\) is a singleton. Even \(S=\varnothing\) does not give a representable initial presheaf.

If the relevant coproducts exist **in \(A\)**, however, the author’s tensor can be defined by

\[
(X\otimes M)(b)=\coprod_{m\in M(b)}X(b).
\]

Its structure maps follow from the coproduct universal property. Under the corresponding cotensor existence assumptions, it gives the relative-Hom adjunction on scan 010. Yoneda preserves limits; it need not carry this \(A\)-coproduct to the pointwise coproduct in \(P(A)\). The notes are right to distinguish those objects. [C-SA26-107A-07–09; Kelly1982, §3.7]

### 3.4 Where the bivariate extension goes wrong

The genuine extension of \(X\in P(A\times B)\) to two arbitrary presheaves is

\[
\widetilde X(L,M)=\operatorname{Nat}(L\boxtimes M,X),
\qquad L\boxtimes M=p_B^*L\times p_A^*M.
\]

It preserves limits **separately** on the opposite presheaf variables. Density reconstructs it from the values at the original representables. This is the valid part of scan 014. The assertion identifying separate and joint continuity is false. For \(A=B=e\),

\[
F(L,M)=\mathrm{Set}(L\times M,2)
\]

has the separate property but sends the coproduct of \((1,0)\) and \((0,1)\) to a two-element set instead of a singleton product. The reverse implication also fails: a jointly represented Hom-pair need not preserve the terminal object in a fixed opposite variable. [C-SA26-107A-10–12]

The next proposed identification and its internal-Hom corollary fail just as concretely:

\[
\bigl|\mathrm{Set}(2\times2,2\times2)\bigr|=256,
\qquad
\bigl|\mathrm{Set}(2,2)\times\mathrm{Set}(2,2)\bigr|=16.
\]

The coordinate swap is a map of products that is not a product of two unary maps. The issue is the false identification of the already defined separately continuous extension with a represented Hom-pair. Genuine Yoneda in the larger category is still fully faithful. Correcting a variance sign or choosing the overwritten codomain does not remove the numerical contradiction. [C-SA26-107A-13–14]

The public *Dérivateurs* XVIII passage also records the same empty-object obstruction to a product-Hom proposal. This is a checked textual parallel, not a proof that every broader evaluation-representability question there is false. [DerXVIII, manuscript pp. 63–64]

### 3.5 Two valid repairs and a remaining unfinished formula

The projection formula

\[
p_B^*[L',L]\cong[p_B^*L',p_B^*L]
\]

is valid for all small \(A,B\), despite its appearance after a false general corollary. An independent evaluation proof establishes it. SGA4, Exposé IV, 10.1–10.3 and 10.5–10.6(2), gives exact published internal-Hom adjunctions and the criterion for the inverse-image comparison; this supplies a published source for the valid structure, not for the false external-product factorization [SGA4IV]. The extension with an arbitrary extra \(M\) is false. For a precise correction put

\[
D_M(b)=\pi_0\operatorname{el}(h_b\times M).
\]

The pointwise formula is

\[
[p_A^*M,p_B^*L](a,b)=L(a)^{D_M(b)}.
\]

For \(A\ne\varnothing\), the canonical map from a coefficient constant along \(B\) to its \(M\)-cotensor is an isomorphism for **every** coefficient exactly when every \(D_M(b)\) is a singleton. For \(B=\Delta\), the formula becomes the power by \(\pi_0M\). In particular nonempty connected \(M\) works, and arbitrary \(M\) does not. This is an explicit reconstruction, with its proof, rather than an emendation of the source. [C-SA26-107A-17–19]

The simplicial boundary sketch is also interpretable under precise hypotheses. For \(A\) with finite limits, evaluation on \(\Delta[n]\) gives \(X_n\), and evaluation on \(\partial\Delta[n]\) gives the matching object. One needs the face maps and compatibility relations, with separate degree-zero and degree-one conventions. The notation involving only \(X_{n-1}\) and \(X_{n-2}\) is a schematic presentation, not a fully specified two-object diagram. The relative matching map is formal; its being a fibration needs additional structure. The arrow from an internal Hom back to a coefficient object marked with question marks has, in general, no canonical evaluation without extra data such as a chosen point of the exponent. [C-SA26-107A-15–16]

Finally, scan 017 invokes the ordinary universal property of presheaf cocompletion. It is valid for small \(A\) and a cocomplete target. Passing to opposites requires the corresponding completeness assumptions; initial cocompleteness of one target does not license every later opposed display. The cancelled decorated-Hom box cannot be identified uniquely from the transcription. [C-SA26-107A-20–21; Kelly1982, Theorem 4.51]

## 4. Cote 107, second unit: what survives passage to Hot?

### 4.1 The order of the questions matters

Scan 019 asks whether filtered colimits exist in `Hot` and whether localization preserves them. The displayed Hom-set comparison makes the intended meaning an **ordinary categorical universal property**. A homotopy-colimit construction is a different statement.

The nerve preserves filtered colimits because a functor \([n]\to C\) uses only finitely many objects, generating arrows and equations. Both existence of representatives and equality of representatives can therefore be witnessed at one later stage. For countable filtered indexing, countability must include morphisms; the checked cofinal-poset construction and an enumeration give a cofinal sequence. A strict sequence can be replaced inductively by a cofibration sequence, with a levelwise weak comparison. These elementary reductions have their own hypotheses and proofs. [C-SA26-107B-01–03; SGA4I, I.8.1.6; Cisinski2006, proof of Proposition 5.2.1]

The source then distinguishes:

| Requirement | Exact role | Present result |
|---|---|---|
|(i) The replacement union represents an ordinary colimit in Hot|Existence of the displayed universal mapping property|False in general for ordinary weak homotopy types|
|(ii) The induced union map remains weak|Stability of weak equivalences under this colimit|True for every induced class of a fundamental localizer, with the stated axioms|
|Surjectivity into a fibrant target|Compatible stagewise homotopy classes have a global representative|True for a countable cofibration sequence in the stated model setting|
|Injectivity into a fibrant target|Stagewise homotopy determines global homotopy|False; the telescope example detects the defect|

Neither the positive result for (ii) nor surjectivity proves (i). [C-SA26-107B-04–08,12]

### 4.2 Filtered stability: the exact positive literature result

Cisinski2006, **Corollary 4.2.22, printed p. 188**, states filtered-colimit stability for **every fundamental localizer on Cat**. There is no accessibility hypothesis in that result. The definition used is weak saturation, terminal-object asphericity, and the relative slice form of Theorem A. Weak saturation here includes the split condition in §1.4.12; the dossier does not silently substitute a differently named axiom package.

For any small \(A\), the category-of-elements functor \(i_A:P(A)\to\mathrm{Cat}\) preserves small colimits [Cisinski2006, Corollary 3.2.13]. Applying it to a filtered natural transformation proves the same stability for \(W_A=i_A^{-1}W\). This last step is the dossier’s explicit formal deduction. It does not say that an arbitrary unspecified class named \(W\) is filtered-colimit stable, or that its localization has ordinary filtered colimits. [C-SA26-107B-05]

This also corrects a supplied contextual citation: note #51’s K3 associates Corollary 4.2.22 with a special/accessibility identification. That is not what the opened corollary says. The private identification itself was not independently verified. [SA26-51]

### 4.3 The telescope obstruction, including all hypotheses

Let \(T\) be the mapping telescope of degree-\(p\) maps of circles, with \(p\) prime, and let \(T_n\) be its finite subtelescopes. These form a sequence of CW cofibrations. Each \(T_n\) has the homotopy type of a circle, while

\[
H_1(T;\mathbb Z)=\mathbb Z[1/p],\qquad H_2(T;\mathbb Z)=0.
\]

The audit proves, rather than merely cites, the calculation

\[
\operatorname{Ext}^1(\mathbb Z[1/p],\mathbb Z)
\cong\operatorname{coker}\bigl((a_n)\mapsto(a_n-pa_{n+1})\bigr)
\cong\mathbb Z_p/\mathbb Z.
\]

The second isomorphism uses \((b_n)\mapsto\sum p^n b_n\). Telescoping shows the image of a coboundary is an ordinary integer; a direct divisibility formula proves the converse. The alternating sequence \(1,0,1,0,\ldots\) gives the noninteger \(-1/(p^2-1)\), proving nonvanishing. Finite matrix and congruence outputs check signs and sample cases; the infinite assertion is proved by the written argument.

The universal coefficient theorem now gives

\[
[T,K(\mathbb Z,2)]\cong H^2(T;\mathbb Z)
\cong\mathbb Z_p/\mathbb Z\ne0,
\qquad [T_n,K(\mathbb Z,2)]=0.
\]

Thus a map can be nullhomotopic on every stage and nonnullhomotopic globally. Here “phantom” means null on every finite subcomplex, not on each entire finite-dimensional skeleton: the telescope is two-dimensional and is not of finite type. The singular-complex version fits the manuscript literally: \(X_n=\operatorname{Sing}(T_n)\) are linked by monomorphisms and the singular target is Kan. Every singular simplex in the telescope has bounded height, so \(\operatorname{colim}\operatorname{Sing}(T_n)=\operatorname{Sing}(T)\). The source’s intended cofibration and fibrancy conditions are therefore satisfied. [C-SA26-107B-12; Milnor1962; Hatcher2002, Example 3F.9 and Theorems 3.2, 4.57]

The stronger nonexistence assertion needs another argument. If **any** ordinary colimit \(L\) of the degree-\(p\) circle sequence existed in unbased `Hot`, mapping into discrete sets would force \(L\) connected. Mapping naturally into \(K(M,1)\), for all abelian groups \(M\), would force \(H_1L\cong\mathbb Z[1/p]\) by Yoneda. There is no conjugation ambiguity for abelian targets. Mapping into \(K(\mathbb Z,2)\) would force \(H^2(L;\mathbb Z)=0\). The universal coefficient injection of the nonzero Ext group contradicts that. No finite-generation hypothesis is used. A checked primary publication of this exact stronger argument was not found; the supplied earlier notes proposed it, and this run independently proves it from the opened standard tools. It is not attributed to Grothendieck or claimed as new. [C-SA26-107B-04]

### 4.4 Surjectivity and the compatibility of homotopies

For a countable cofibration sequence of cofibrant objects and a fibrant target, mapping spaces form a tower of Kan fibrations in the simplicial setting. Compatible components can be represented by compatible vertices: choose one, lift a path at the next stage, and continue. This proves the manuscript’s surjectivity conclusion. The general \(\lim^1\) obstruction is a pointed orbit set; it is an abelian quotient only in appropriate examples such as the one above. [C-SA26-107B-07–08; Hovey1999; Hirschhorn2015]

For the more general square, write \(pg=g'i\), with a cofibration \(i:A\hookrightarrow B\) between cofibrant objects and a fibration \(p:E\to F\) between fibrant objects. A proposed \(\varphi:B\to E\) can be homotoped to a strict diagonal precisely when suitable triangle homotopies can be chosen compatibly. The mapping-space fibration

\[
\operatorname{Map}(B,E)\longrightarrow
\operatorname{Map}(A,E)\times_{\operatorname{Map}(A,F)}\operatorname{Map}(B,F)
\]

proves the existential criterion. Compatibility can be equality of projected paths, or homotopy between them **relative to both endpoints**, followed by a path-space lifting adjustment. This matches the surviving iff in the margin. An arbitrary model category requires compatible cylinders or framings; the audit supplies the appropriate construction without assigning extra labels to the manuscript. [C-SA26-107B-09–10]

Automatic compatibility is false. Take \(\partial I\hookrightarrow I\), the covering \(\mathbb R\to S^1\), endpoint lifts 0 and 1, a constant lower map and the proposed constant diagonal 0. Both triangle homotopies exist, but a strict diagonal would be a path from 0 to 1 contained in the discrete fibre \(\mathbb Z\). It cannot exist. Every cofibrancy and fibrancy hypothesis is checked. The example excludes **all** compatible choices for those fixed data, rather than merely one inconveniently chosen pair of homotopies.

The distinction between one and two fixed endpoints is equally concrete. The one-endpoint pushout-product is a trivial cofibration and supports the representative adjustment. The two-endpoint version need only be a cofibration. Already \(\partial\Delta^1\hookrightarrow\Delta^1\) changes components. Fibrancy of the target therefore does not solve every prescribed two-endpoint extension. The mathematical drawings on scans 022 and 024 belong to this argument. [C-SA26-107B-11; Quillen1967, consulted retypesetting Proposition 2.2.4]

### 4.5 The final retraction question is sharper than stagewise existence

The closing question asks about compatible components of retraction spaces. From a nonzero phantom map \(f:X_\infty\to Y\) and the zero map, form

\[
Z_n=Y\amalg_{X_n\times\partial\Delta^1}(X_n\times\Delta^1).
\]

Every stage retracts to \(Y\), because the two endpoint maps are homotopic there. The transitions are monomorphisms. A retraction at infinity would make \(f\) globally nullhomotopic, a contradiction. In fact, the inverse limit of the component sets of the retraction spaces is empty: compatible components in this countable fibration tower would strictify to a global retraction. Thus the positive reformulation and the negative existence example are both valid. [C-SA26-107B-13–14]

No checked source records an answer from Ronnie Brown or explains a later abandonment of these specific leaves. The dossier’s historical explanation stops with the obstacles the author actually writes down.

## 5. What the notes got right, and what changes here

The earlier notes correctly identified the unfinished faithfulness and section arguments in 106, the product-Hom failures in 107, and the decisive surjectivity/injectivity distinction in the final inquiry. Their telescope, no-alternative-colimit, relative-square and retraction arguments were read in full and independently re-proved. The revised dossier does not demote a sound argument merely because it originated in an earlier model run; it records exactly which proof has now been checked.

The substantive changes are concentrated and explicit:

| Source or passage | Correction or qualification |
|---|---|
|Note #5; 106/006|The theorem is reformulated as a criterion, not explicitly withdrawn.|
|106 roof claims|State H106, the strict-middle-map convention, and the precise \(\pi_0\) comparison; do not substitute a stronger nerve theorem without its hypotheses.|
|107/008 cotensor closure|The relevant weights are \(h_b\times M\) for every \(b\); one presentation of \(M\) alone can be insufficient.|
|107/008 representability iff|The compound pointwise assertion needs the empty-index exception.|
|107/014 bivariate formulas|Distinguish the false identification from genuine Yoneda; separate continuity cannot be replaced by joint continuity.|
|107/016 projection special case|It is true and gets an independent proof despite the false general corollary preceding it.|
|107/016 constant coefficients|Specify the singleton component weights; do not claim \(L^M=L\) for arbitrary \(M\).|
|Note #52 H11|The positive filtered-stability literature is more general than the earlier simplicial-only check.|
|Note #51 K3|The cited Cisinski corollary concerns filtered colimits, not the supplied accessibility identification.|
|Notes #47–63 project comparisons|Original public passages, private commentary, inherited statuses and this run’s deductions remain distinct.|

A counterexample to a transcribed formula does not decide whether Grothendieck made a mistake or the transcription misread the ink. Both possibilities remain visible in the reading table.

## 6. Literature fate and historical dating

Each mathematical claim has a searched fate and a claim-linked search record. Searches used the named database channels, exact formulations, author pages and backward references. Access failures, including direct zbMATH failures and oversized or unavailable PDFs, are recorded. Search snippets were not substituted for inaccessible theorem texts. MathOverflow was used for leads; mathematical authority comes from primary texts or the fully written proofs in this dossier.

| Reference | Date distinction and exact role |
|---|---|
|SGA4I|Seminar 1963–64; publication 1972. Ordinary Yoneda, density, Kan adjoints and cofinal indexing.|
|Milnor1962|Received 6 February 1961; published 1962. Receipt is not labelled first circulation. Earlier cohomological limit obstruction.|
|Quillen1967|Published 1967. Covering homotopy extension checked in a later retypesetting; original handwritten page alternatives remain undecided.|
|Brown1973|The paper identifies a May 1971 MIT thesis; its first public circulation was not verified. December 1973 volume, copyright 1974. Original axioms, factorization and weak lifting inspected; homotopy fractions distinguished from strict roof conventions.|
|Kelly1982|Original 1982; authorized electronic reprint 2005. Exact free-cocompletion and tensor/cotensor framework.|
|RB2009|arXiv first circulation 2006; version 4 consulted. Precise CF1–CF4 and fraction statements.|
|Cisinski2006|Published 2006; exact corollaries checked. Earlier circulation of those particular results not established here.|
|Cisinski2010K|Online 2009; journal 2010. Exact strict cocycle mapping-space proposition, in the dual convention.|
|Horel2016|arXiv 2015; publication 2016. Cofibrant short-roof framework.|
|Hirschhorn2015|Author manuscript 16 May 2015; arXiv 6 July 2015. Tower obstruction, including pointed-set qualifications.|
|Pursuing Stacks|Original 1983 material; opened electronic edition 2021. The separately verified SMF volume I appeared 2022. Locators here belong to the electronic primary edition.|
|Les Dérivateurs|Editor dates manuscript 1990–91. Public electronic chapter versions have later editorial dates; these are not dates of first composition.|

The A–F classes describe the relationship to the literature **for the exact stated scope**. They are not novelty certificates. In particular, B can include an explicit elementary consequence of established machinery when the literal manuscript formulation has no located verbatim theorem; the fate field says so. Class D on the false product formulas means the literal assertion has no valid development found and is closed negatively here, not that it remains a plausible open conjecture. Class F marks unidentified formulas. Class C on cotensor closure marks the missing hypothesis/interpretation boundary, not an unsolved theorem under the repaired assumptions.

The representability claim C-SA26-107A-06 has class E for its standard lemma and corrected criterion, while its unrestricted compound iff is marked “false as stated” because of the empty-index exception.

No exact later published theorem of Grothendieck was identified as settling one of these literal open steps. Public manuscript parallels are therefore not automatically placed in class A. EGA, the published-work bibliography, *Esquisse* and *Récoltes et Semailles* searches did not produce an adopted exact same-object link for these Brown, bivariate-presheaf or ordinary-Hot assertions. This is a bounded search result, not a claim that those works contain no related ideas.

## 7. Historical problems and what remains to do

The problem index includes steps that were open **on the pages**, including one immediately resolved there. It does not present all of them as open mathematics in 2026. The six problems in cote 106 are cancellation, original-roof faithfulness, inversion of acyclic cofibrations, revised-roof section independence, couniversal denominators, and the locally completed naturality check. The first four have affirmative answers under H106; the broader couniversal proposal needs a specified recognition problem before it becomes a new theorem task.

The five problems in 107’s first unit concern the cancelled componentwise assertion, cotensor representability, simplicial boundary evaluation, constant coefficients and opposed universal properties. Their ordinary precise forms are either standard, corrected by explicit counterexamples, or bounded by an undeciphered formula. The five final-unit problems concern colimits and injectivity, filtered stability, relative rectification, retractions, and strict representatives. Their standard model-theoretic formulations are settled in the directions explained above.

The strongest useful follow-up work is therefore a companion reconstruction with an ink check, exact axiom comparison and carefully delimited modern repairs. This dossier does not certify a new unsolved conjecture merely because a historical page ends with a question mark. `SA26_directions.md` ranks concrete next tasks, gives the item/claim/problem IDs for each, and distinguishes editorial payoff from a broader hypothesis problem. Those directions are not developed here.

## 8. Readings: mathematics raises the question; the ink decides

`SA26_readings.tsv` is the mathematical alarm list, rather than a reproduction of every uncertainty about a printed digit or decorative mark. Priority issues include the Brown axiom lettering; the typed numerator in roof composition; the direction of the weak map and its section in 106/014; the factor name in 106/016; projection and exponent subscripts in 107; the overwritten bivariate target and variance; the unfinished matching/evaluation formulas; barred versus unbarred diagonals; the Quillen reference; and neighboring-index signs in 107/025.

Every row gives the existing reading, an alternative or the exact question to inspect, the mathematical evidence, the consequence and confidence. “High” mathematical confidence means, for example, that a composition has the wrong source. It does not mean high confidence about an unseen handwritten letter. The transcription hash is preserved, and no alternative was silently substituted into the source.

## 9. Links and private-project concordances

The checked public parallels are precise and modest. *Dérivateurs* III separates actions and adjunctions from an additional external-Hom question; VI uses relative internal-Hom language; XVIII records an obstruction to a product-Hom proposal; XIII makes fibrant diagram data matter; XII has an actual open–closed gluing construction absent here. The PS parallels distinguish the present ordinary calculations from linearization and derived diagram operations. Their exact locators are in the link table and bibliography. [SA26-47]

For cote 106, additional public endpoints are checked directly: the Baues discussion in *Pursuing Stacks* §125 (ms530–533), the dual replacement equivalence in *Dérivateurs* VI, Théorème-Scholie2(I) (ms108–110), its distinct finer localizer in II (ms110–112), and the definition of couniversal weak equivalences in XII (ms109–111). These comparisons preserve the hypotheses and do not endorse the private commentary attached to the same references.

*Dérivateurs* VII provides a further checked comparison with arbitrary finite paths and ordinary localization (§7, ms59–82). Its additional homotopy-category comparison is a separate question: the attempted negative argument at ms112–113 is explicitly corrected in note 24 at ms114. The statement at ms123 compares different choices of \(C_\infty(t)\), not \(C_\infty\) with \(C\). The dossier therefore does not convert that discussion into a negative higher theorem about the short roofs here. [DerVII]

*Dérivateurs* VII provides a further checked comparison with arbitrary finite paths and ordinary localization (§7, ms59–82). Its additional homotopy-category comparison is a separate question: the attempted negative argument at ms112–113 is explicitly corrected in note 24 at ms114. The statement at ms123 compares different choices of \(C_\infty(t)\), not \(C_\infty\) with \(C\). The dossier therefore does not convert that discussion into a negative higher theorem about the short roofs here. [DerVII]

*Dérivateurs* VII provides a further checked comparison with arbitrary finite paths and ordinary localization (§7, ms59–82). Its additional homotopy-category comparison is a separate question: the attempted negative argument at ms112–113 is explicitly corrected in note24 at ms114. The statement at ms123 compares different choices of \(C_\infty(t)\), not \(C_\infty\) with \(C\). The dossier therefore does not convert that discussion into a negative higher theorem about the short roofs here. [DerVII]

For the final 107 inquiry, *Dérivateurs* V, ms43–49, supplies exact comparisons with invariant ind-objects, strictification and stagewise/global homotopy questions. XIII, ms73–74, concerns inverse towers with fibrant terms and fibration transitions; filtered stability is a separate assumption there. The finite-string nerve proof cited in note52 belongs to unavailable commentary and is not attributed to the opened V original. [DerV; DerXIII]

Within this packet, the changes of roof convention in 106 and the new title unit in 107 are observed argument boundaries. No invented cross-reference to an unseen TOPIC cote is supplied. Public total-asphericity and W(7) passages are verified as separate public comparison endpoints, without a first-occurrence claim. [SA26-61]

All note-specific project and run-name families are in `SA26_context_links.tsv`; their missing private target proofs are explicitly labelled. Three further tabular annexes retain the large statement concordances and earlier checking metadata:

| Annex | Content | What has been checked |
|---|---|---|
|`SA26_project_leads.tsv`|255 full STRATA/PATHS/BISITE/RESIDUE source rows and provenance|Each source row read; its bounded relation to the available manuscript assessed|
|`SA26_new_results_leads.tsv`|12 NEW_RESULTS statements plus 3 later notices|No full statement occurs in this packet; the K3 citation mismatch is corrected|
|`SA26_prior_checking_metadata.tsv`|12 quoted prover/checker histories|Preserved as supplied metadata, including limited and “not yet” checks|

For the 255 rows, the result is **212 absent full formulations, 37 thematic comparisons, 1 direct restricted form and 5 partial underived forms; zero complete matches**. The restricted path comparison is PATHS A.P1. The five underived forms are BISITE E.3, F.1, F.4, F.7, F.8. The inherited labels 146 Proved, 33 Known, 57 Refuted and 19 Open are the old returns’ labels, not classifications assigned by this run.

The private proof files, original CSV registers and AI companion commentary were not attached. Their target-side claims cannot be independently verified from a quotation in the notes. A supplementary title search for the named private files, followed by simpler alternate titles, returned no matches; this bounded lookup does not establish absence from unindexed material. Accordingly the main link table labels those rows **CONTEXT LEAD ONLY**, and `SA26_verified_textual_links.tsv` isolates the adopted public/internal textual comparisons. A retained lead is not represented as a verified two-endpoint theorem. This is the explicit evidence boundary of Stage 5; the unavailable private targets have not been fabricated or silently endorsed.

## 10. Verification, reproducibility and audit trail

Three parallel mathematical readings were reviewed by the root consolidator. The mathematical audit files are:

- `parts/cote106/proof_checks.md`: weak lifting, cancellation, localization algebra, the two roof presentations, common factorizations and section independence.
- `parts/cote107_objects/proof_audit.md`: all ordinary-Hom calculations, finite counterexamples, exact cotensor weights, matching objects and opposed universal properties.
- `parts/cote107_homotopy/narrative.md`: finite presentation, filtered stability, the infinite Ext proof, ordinary-colimit nonexistence, rectification and retractions.

Executable checks and outputs accompany each. They redo symbolic substitutions, finite presheaf and function-set calculations, boundary examples, telescope chain matrices and congruences. They are labelled according to their actual strength. A finite output is never presented as proving an infinite categorical existence or nonexistence theorem. The complete mathematical proofs provide those steps.

`SA26_self_flags.tsv` explicitly maps all 26 rows of the notes’ standing register to the claims, historical problems or title metadata that account for them. The separate R1–R11 and H01–H13 audits preserve the substructure of the two large mathematical notes.

`CHECK_EVENTS.tsv` records textual checks, targeted proof reviews, independent re-proofs, computations, refutations and background use under their actual types. Its model field identifies this run without inventing an unavailable reasoning-effort setting. Historical prover/effort claims remain in the separate provenance annex. `SA26_refinements.json` defines the corrected statements referenced by refutation events.

The scripts that parse the index and serialize tables do not create judgments from headings or keywords. They preserve already authored read verdicts and validate coverage, schemas, references and counts. All 63 source entries have exactly one verdict; every item has its sources; every mathematical claim has a searched fate; every historical problem has checked source support. Mechanical failures during table serialization are retained with their corrections in the audit output. Source attachments and downloaded third-party full texts are not copied into the deliverable.

## 11. Final counts

<!-- FINAL_COUNTS:START -->
| Measure | Count |
|---|---:|
| Indexed source entries, each with one verdict | 63 |
| Consolidated items | 43 |
| Mathematical claims, all with searched fates | 53 |
| Historical problems | 16 |
| Reading alarms after merging identical locations | 38 |
| Ranked directions | 7 |
| Check events | 258 |
| Bibliography records: verified / unverified leads | 40 / 4 |
| Adopted public/internal textual links | 43 |
| Context-only link rows, including repeated lead families | 317 |

### Entry verdicts

| Category | Count |
|---|---:|
| kept | 39 |
| merged | 19 |
| corrected | 5 |
| withdrawn | 0 |
| rests on a misreading | 0 |

### Item kinds

| Category | Count |
|---|---:|
| unproved claim | 5 |
| self-flagged step | 6 |
| unpursued implication | 3 |
| withdrawn in the same text | 3 |
| conjecture | 1 |
| idea of the earlier run | 9 |
| reading question | 12 |
| title, date or page count | 1 |
| other | 3 |

### Claims by literature class

| Category | Count |
|---|---:|
| A — own later published work | 0 |
| B — developed by others into established results | 8 |
| C — partly developed; exact scope gap specified | 1 |
| D — no valid development located; here closed negatively | 4 |
| E — known before these pages | 38 |
| F — not identifiable from the pages | 2 |

### Claims by status on the pages

| Category | Count |
|---|---:|
| proof sketched | 13 |
| stated without proof | 15 |
| open on the pages | 10 |
| proved there | 7 |
| corrected by himself later | 3 |
| false as stated | 5 |
<!-- FINAL_COUNTS:END -->

The counts concern this part only. Items remain mergeable with the other SA26 parts by their stable IDs. No claim IDs from a private contextual project are promoted to SA26 manuscript claims, and no absent TOPIC folder is represented as read.

## 12. Reading the deliverable

Start with this overview and the ranked directions. Use `SA26_entries.tsv` to trace any original note to its consolidated item. The items distinguish source wording from reconstruction; the claims distinguish status on the page from present mathematical status; the problems preserve the author’s questions; the readings preserve unresolved ink alternatives. The link tables and private-lead annexes separate genuine textual comparison from unavailable proof provenance. `SA26_references.bib` marks every cited work verified or unverified and states limited consultation where appropriate. The search ledger, checks, programs, outputs and progress log make the conclusions auditable without depending on this chat.
