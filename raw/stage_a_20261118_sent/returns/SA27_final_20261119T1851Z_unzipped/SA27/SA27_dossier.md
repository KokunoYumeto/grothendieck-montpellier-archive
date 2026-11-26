# SA27 — Autour de Pursuing stacks, part 3

**Alexander Grothendieck, Montpellier archive; consolidation as of 19 November 2026.**

## 1. What this dossier establishes

These folders contain several connected investigations: weak equivalences and test categories; linearization and additive coefficients; kernels, duality and Isbell conjugacy; gluing of topoi; indexed homotopy theories; and the cohomological properties of functors between categories. They are not a single finished treatise. A list of questions in 108, an extended calculation in 113, an altered proposition in 114, a cancelled generalization in 115, and the numbered axioms of 117 have different evidential force. The dossier retains those differences.

The most consequential consolidation is a separation of assertions that earlier comparisons sometimes placed too close together. Product/diagonal total asphericity is not the later universal final-image condition. The Hom-lifting axiom Hot7 is not the reverse gluing principle later called W(7 bis). An ordinary categorical pushout is not automatically a homotopy pushout. A category localized at all its arrows is not thereby a homotopical localization for every theory of coherent diagrams. Formal opposition, ordinary Kan extension and derived duality each require their own hypotheses. These distinctions are made at the level of individual items and claims, not only in this overview.

The entry table contains exactly the 578 rows of the supplied index, each with a verdict reached by reading its note and the relevant transcription. Cross-package mergers preserve the original records in `work/` and give aliases in `work/item_aliases.json`. Where one indexed entry contains a large comparison register, it remains one source entry and one verdict; the constituent comparisons are preserved in supplemental tables. Splitting such a register into invented new index rows would obscure the requested coverage count.

This is a dossier of the supplied diplomatic text, not a new transcription. No scan was attached, no reading was changed, and all source hashes are checked again at delivery. Mathematical contradictions therefore generate either a counterexample to the transcribed assertion, an explicitly labelled reconstruction, or an entry in the scan-reading queue. They do not authorize an emendation of the ink.

## 2. Corpus, sequence and dates

The three packages contain 162, 98 and 318 indexed entries respectively. Their supplied TeX files contain 40, 34 and 38 scan blocks, for 112 in all. There are no second-pass or Codex note files in this attachment; the prompt expressly makes their absence permissible. The source inventory records every supplied file and its hash. `work/page_map.json` maps the scan blocks to the combined TeX files.

| Cote | Catalogue/topic description | Catalogue pages | Supplied scan blocks here | Scope |
|---|---|---:|---:|---|
|103|Correspondence on Sinh's thesis|17|0|Other part; orientation only|
|104|Champs1|16|0|Other part; orientation only|
|105|Champs2|52|0|Other part; orientation only|
|106|Champs3|16|0|Other part; orientation only|
|107|Closed models|25|0|Other part; orientation only|
|108|Divers, liste questions|5|5|Read here|
|109|Tables; corrections and preparation for publication|37|0|Other part; orientation only|
|111|Tapis de Quillen; notes of 10 September 1968|16|0|Other part; orientation only|
|112|Linéarisation|4|4|Read here|
|113|Abelianization|12|12|Read here|
|114|Asphéricité|5|5|Read here|
|115|“Correspondances” fonctorielles. Dualité des topos|14|14|Read here|
|116|Mapping-cône etc.|10|9|Read supplied text only|
|117|Théories homotopiques|25|25|Read here|
|118|Cohomology properties of maps in (Cat)|40|38|Read supplied text; TOPIC metadata corrected|

The final row needs an explicit qualification. `TOPIC.md` records zero Pro pages for 118, but the attachment actually supplies its transcription with 38 scan blocks. The actual file determines this run's textual scope. Scan identifiers 013 and 038 are absent from that supplied sequence; catalogue page counts, image identifiers and authorial pagination must not be treated as interchangeable. Similarly, 116 has nine supplied blocks against ten catalogue pages. These facts do not license reconstruction of an absent mathematical page. The seven other-part cotes above are covered as scope records, not assigned fictitious verdicts. [Supplied TOPIC; SA27-204, SA27-524; CatalogueMontpellier.]

The mathematical programme of 117 has positive dating evidence: a December 1983 title and a 24 November 1983 marginal date. Cote 118 is undated as a mathematical dossier. A reused notice dated 28 April 1983 and other printed or administrative material provide dates for those documents, not dates for every handwritten argument on them. The same caution applies to the reused 1973 letter material in 108 and the listings or printer sheets elsewhere. An archive order is evidence of organization, not a proof of chronological priority. [SA27-204, SA27-500, SA27-526; CatalogueMontpellier.]

**Locator convention.** Unless a record explicitly says otherwise, its line numbers are one-based lines of the supplied combined package TeX, not lines of the image or of an imaginary separate scan file. Cote and scan identify the image locus; the page map gives the containing line interval. External references distinguish printed page numbers, manuscript page numbers and electronic PDF pages where those differ. References to the final 418-page Cisinski PDF must not be silently transferred to an earlier 370-page author version.

## 3. His lines of work, in the supplied order

### 108 — Questions about models and weak equivalences

The opening list asks for axioms and constructions rather than announcing a completed foundation. Its objects are W, W_A, model structures, test categories and functors, contractors, integration, group objects, Hom objects and relative cohomology. Saturation is a live assertion, but the short 108 phrase does not identify which historical sense of saturation is intended. In 118 the localization-invertibility criterion is explicit; the consolidation records the connection without importing that stronger definition backwards. [SA27-1–SA27-7, SA27-9–SA27-13; SA27-2.]

The pullback test on 108/004 is particularly informative. The assertion that terminal-object inclusions suffice is false for W∞. The inclusion {1}→[1] passes every such test over [1], but the weak equivalence {0}→[1] pulls back to ∅→{1}. The immediately following question, which uses every vertex of every finite simplex, has an affirmative answer for W∞: a vertex and its image reduce every simplex operator by two-out-of-three, and Rezk's sharp-map criterion then applies after taking nerves. The two sentences must therefore receive different statuses. No extension of that argument to an arbitrary unspecified W is claimed. [SA27-14–SA27-15; SA27-C012–SA27-C013; Rezk1998, Theorem 4.1 and Remark 4.2(3); root mathematical checks §§6,8.]

Other agenda entries ask for homotopy and Dold–Puppe sequences, relative spectral sequences, relations between integration and colimits, and a way to compare diagram homotopy types with diagrams of homotopy types. Where no degree conventions, coefficient hypotheses or functor domains are supplied, a later theorem on a related subject is background rather than a solution of an identifiable formula. The problem register preserves these open-ended entries with that limit. [SA27-3, SA27-10–SA27-11, SA27-18, SA27-23–SA27-27.]

### 112 — Linéarisation

The next dossier works with abelian presheaves, integrated coefficient complexes, smoothness, negligible objects, localized categories and locally constant derived coefficients. The questions are about equivalences between those constructions, Ext comparisons, removing smoothness assumptions, replacing objects by complexes, and realizing truncations. The Δ case is marked positively, but that does not prove all subsequent A/B comparisons. A partially specified base or a doubtful marginal index remains part of the problem's data. [SA27-32–SA27-35, SA27-37–SA27-42, SA27-44.]

The modern context is derived homological algebra, but the translation must preserve boundedness and variance. A statement about a localized category of smooth abelian presheaves is not automatically the unbounded derived category of arbitrary diagrams, nor is a degreewise flat complex automatically suitable for a derived tensor product. Later resolution theory supplies precise strengthened hypotheses; it does not determine what an omitted manuscript subscript was. [Claims attached to SA27-34–SA27-35, SA27-37–SA27-42, SA27-44 and SA27-70; p108-Spaltenstein1988.]

### 113 — Abelianization and coefficient calculus

The positive core is ordinary enriched category theory: k-linear additive presheaves, representable copowers, Cauchy completion, tensor products of small additive categories, Hom–tensor adjunctions, and separately cocontinuous extensions. These are separated into individual claims, including the formal identities and the projectivity arguments. The comparison with earlier literature identifies universal-property results already available before these notes; their presence here is not treated as a claim of novelty. [SA27-45–SA27-59, SA27-63–SA27-69; p108-Kelly1982.]

Three qualifications matter. A recognition theorem for a module category needs an appropriate small family of small projective generators, not merely the phrase “enough projectives.” The completed tensor universal property must be distinguished from an algebraic external tensor functor: in the latter, E⊗E* reaches only finite-rank endomorphisms of an infinite-dimensional vector space E. Finally, unbounded quasi-isomorphism invariance requires suitable resolutions and a totalization convention. The explicit bi-infinite multiplication-by 2 complex over Z/4 is acyclic and degreewise free, but tensoring with Z/2 makes its differentials zero. That calculation diagnoses the unbounded claim; a finite truncation alone would not prove it. [SA27-50, SA27-59, SA27-70; SA27-C040, SA27-C049, SA27-C056; package proofs and computation outputs.]

### 114 — Asphéricité and the failed product criterion

The programme begins with morphisms of asphericity structures and contractors, slices, duality, test functors, finiteness and candidate indexing shapes. Its draft Proposition 4 then proposes an equivalence between total W∞-asphericity, total W-asphericity under Loc4, and a connectedness condition on products of representables. Loc4 is present and must be respected: the all-functors localizer would not be an admissible objection. [SA27-73–SA27-81, SA27-83–SA27-86.]

The ordinary cube category supplies the relevant obstruction with W=W0. It has a terminal zero-cube; products of representables are connected. But the product of two representable 1-cubes has, after removing degeneracies, four vertices, five edges and two squares. Its category-of-elements homotopy type has rational Betti numbers (1,1,1), so connectedness has not supplied asphericity. The exact finite nerve certificate and the reduction from the full category of elements are both recorded. This matches Cisinski's ordinary-cube discussion. The retained Pursuing Stacks Proposition 4 is a different assertion, so its number cannot be used to erase the failure of this draft. [SA27-C058; Cisinski2006, Remark 8.4.33; PS2021,§§95–96; root checks §7.]

The remaining page asks about restriction, dominance, generators, adjoints and preservation of asphericity. Reflection of the empty presheaf is weaker than faithful or conservative restriction, and asphericity alone does not imply those ordinary categorical properties. The cancelled adjoint argument stays cancelled. [SA27-90–SA27-97; SGA4 comparisons in the claims map.]

### 115 — Correspondences, conjugacy and the envelope

The kernel calculations lead to the wheel of equivalent ordinary presentations by currying and Yoneda extension. The audit distinguishes eleven distinct categories from thirteen drawn positions. Each transform has a variance; a repeated label or reversed Hom argument can change the assertion. The ordinary kernel adjunction, Isbell conjugacy, units, represented fixed points and coend pairing are positive content. General full faithfulness of the external product and an unrestricted exponential-independence assertion fail in elementary examples. [SA27-98–SA27-110, SA27-112–SA27-117, SA27-120.]

The pairing triples (P,Q,α), with one component of a morphism reversed, define an Isbell envelope. This is not the category formed by putting two strata side by side and adding a crossing-Hom bifunctor. The distinction is essential when comparing 115 with the gluing constructions in 116 and 118. Questions about reflexive objects, representability, weak equivalences, full faithfulness from an ambient category, and functoriality are not all settled by writing the conjugacy adjunction. The precise modern references are matched to those separate questions. [SA27-113–SA27-117, SA27-126, SA27-130, SA27-133–SA27-136, SA27-147.]

The final leaf returns to free cocompletion and coefficient opposition. Ordinary presheaves have the expected universal property for cocomplete targets. The analogous abelian formula needs an additive target and additive functors; with arbitrary Set-valued targets it is false. Opposing the value category and the source exchanges limits and colimits formally, but does not construct a geometric “opposite topos” or a derived duality theorem. [SA27-138–SA27-143.]

### 116 — Mapping-cone topoi and presheaf gluing

For a geometric morphism f:X0→X1, the triples(F0,F1,f*F1→F0) give the central gluing description. The closed stratum has the asserted all-coefficient cohomological comparison, and the retraction and support sequence explain the mapping-cone terminology. These are stronger coefficient statements than a comparison using only constant or locally constant sheaves. Their exact scope must therefore be retained. [SA27-205–SA27-213.]

For presheaf topoi, the condition that the gluing functor preserve all small limits is an exact earlier SGA4 match. The crossing bifunctor then reconstructs an ordinary category whose presheaves give the glued topos. The explicit collage is an earlier-run continuation after 116/008 and is written by Grothendieck in 118/017; those occurrences are consolidated in SA27-146, with their different provenance intact. [SA27-214; SA27-146; SGA4 IV9.5.10(b–c).]

### 117 — Théories homotopiques

Here the organizing object is A↦H(A), with restriction, natural transformations, evaluations, three levels of Hom, left and right Kan adjoints, Fubini, base change, fully faithful indexing and localization. The text is an early programme for an indexed homotopy theory. Its later relationship with derivators is substantial, but its actual axioms and hesitations must be read before importing a modern definition. [SA27-218–SA27-241, SA27-243–SA27-246.]

The infinite-product warning is genuine. Localization need not commute with arbitrary products: alternating fences with unbounded lengths give a uniform-zigzag obstruction. This is compatible with the finite statement and is not contradicted by a modern derivator satisfying its own coproduct axiom. Likewise, a relative functor induces maps on diagram localizations without necessarily preserving homotopy Kan operations. [SA27-225, SA27-229; SA27-C221 and package proofs.]

For the theory of category-valued diagrams localized objectwise at any modern fundamental localizer, the left Kan adjoints are established without an accessibility restriction. The exact proof transports Cisinski's general presheaf-localizer construction through the test category Δ and the equivalence of all localized diagram categories. Right Kan adjoints retain a separate accessibility-qualified positive result; the dossier does not infer their unrestricted existence by formal duality. [SA27-C233–SA27-C234; Cisinski2006, Proposition 3.1.26, Example 4.1.21 and Corollary 4.2.6; `work/p116/proof_checks.md`, P10.]

On the derived-sheaf page, the initial negative claim about a left adjoint is withdrawn immediately. That correction must not be suppressed. The replacement justification, however, wrongly treats ordinary left Kan extension as exact in general. Coinvariants for F2[C2] destroy injectivity in the displayed exact sequence; the code checks the original complex and the resulting homology. Derived left Kan extension repairs the existence assertion, not the underived exactness claim. [SA27-233–SA27-234, SA27-249; SA27-C235–SA27-C236, SA27-C247.]

Hot6 also needs a precise localization hypothesis. The face poset of the tetrahedron boundary has homotopy type S², while its ordinary all-arrow localization is equivalent to the terminal groupoid. Restriction of the spaces theory along that localization is not fully faithful: maps from a constant point to constant K(Z,2) detect H²(S²;Z). A reflective localization or a homotopical epimorphism supplies a different, valid hypothesis. Hot7, meanwhile, asks for surjectivity of a Hom comparison across two sieves or cosieves; it is not later strong reverse excision. [SA27-238, SA27-201; SA27-C241 and its separately labelled modern refinement.]

### 118 — Cohomological properties, gluing, products and limits

The first part compares fibrations, cofibrations, smooth and proper maps, universally weak maps, Serre maps and weaker Serre variants. The class diagrams contain positive assertions, crossed-out noninclusions and unanswered questions. Every identifiable clause is retained separately in the claims map. The initial-lift criterion must be distinguished from composition-stable Grothendieck opfibration data; SGA1 already makes that distinction. Some exact lattice relations remain unidentified because their class definitions or arrow directions are not secure. [SA27-418–SA27-425, SA27-451–SA27-464; SGA1Root VI Def6.1,§§7–10.]

The choice of localizer also changes the lattice. For W₀, which detects connected components, the chaotic two-object groupoid maps to BC₂ as a discrete bifibration. It is smooth and proper, yet it is not strong Serre: pulling back the W₀-map *→BC₂ gives a discrete two-point category mapping to a connected category. Thus smooth-plus-proper cannot imply strong Serre for arbitrary W. The usual W∞ conclusion is a separate positive theorem. Within the strong Serre class, fibre asphericity is equivalent to universal weakness for every fundamental localizer; equivalence with global W-membership is certified here under the additional hypothesis that the localizer is proper. This technical property of the localizer must not be confused with properness of the functor. [SA27-C433, SA27-C442–SA27-C445; modern audit SA27-C456; Cisinski2006, Proposition 6.2.3 and Corollaries 6.4.8, 6.4.16, 6.4.18; root checks §11; `work/p116/cross_review_118.md`.]

The cone displays have a related ambiguity. Under a standard collage-cylinder reconstruction, the projection has an adjoint section and a deformation retraction over its base, hence is universally weak and Serre. The negative annotation on 118/014 cannot be accepted for that reconstruction. But the source switches displayed directions, so the dossier treats this as a conditional diagnosis and scan question, not as an unqualified identification of C(f). [SA27-424, SA27-462; root checks §9.]

The gluing sequence distinguishes Grothendieck integration, cartesian squares with (op)fibration hypotheses, ordinary Cat pushouts and presheaf pushouts. The finite double-cone example refutes unrestricted forward pushout invariance: a contractible cosieve Y in a category X of homotopy type S² is collapsed to a point, and the pushout is [1]. A separate weak-attaching-immersion assertion requires a separate example; the dossier does not misuse the first example for both. Presheaf pushout invariance along a monomorphism is a different established theorem for a modern fundamental localizer and arbitrary small A. [SA27-404–SA27-405, SA27-411, SA27-415, SA27-427–SA27-429.]

The product sequence contains two further traps. For A=BG with G nontrivial, the weak maps of G-sets detected by action groupoids are precisely the bijections, hence are product stable, although BG is connected and nonaspherical. Connectedness therefore does not repair the converse. At A=∅, binary product comparisons can hold while the nullary comparison ∅→* fails. The distinction between binary and finite products is indispensable. Cisinski's October 2026 author correction confirms a missing assumption in the related implication of his Proposition 4.3.2. [SA27-407–SA27-408, SA27-439–SA27-442; Cisinski2026MO.]

The arbitrary-sum question has a positive modern answer for every fundamental localizer: the ordinary disjoint union represents the coproduct in Cat[W⁻¹]. The accessible case follows from the model structure and sum stability; a finite-witness argument reduces every set-indexed family of localized arrows and equalities to an accessible sublocalizer. This does not prove the distinct assertion that a specified fraction calculus provides one common weak target for an infinite family of roofs. Nor does it invalidate the infinite-product counterexample for arbitrary relative categories in 117. [SA27-C428–SA27-C429; `work/p118/proof_checks.md`, §11; root checks §12.]

Finally, the filtration theorem uses exhaustive sieve or cosieve filtrations preserving the stated nonempty infima. A filtration-preserving map yields only ψf≤φ for minimum-stage maps, not generally equality. Replacing the diagrams by their Grothendieck constructions repairs the proof while retaining the theorem's hypotheses. The aspherical-filtration corollary also retains nonemptiness of the index and its infimum conditions; connectedness alone is not a replacement. The saturation telescope then needs the fraction, factorization and filtered-union results it invokes. [SA27-406, SA27-416, SA27-443, SA27-2; root checks §3.]

## 4. What the earlier notes got right, and what changes

The earlier notes were often strongest when they kept a question as a question, recorded a cancellation, preserved the Loc4 clause, separated the ordinary envelope from a collage, or noticed the distinction between finite and infinite homotopies. Those judgments are retained. Their concrete finite-rank, tensor, coinvariant and pushout diagnostics have been checked at the level of their actual hypotheses, with executable computations where useful.

Several corrections are consequential. The accessibility attribution to Cisinski Corollary 4.2.22 is wrong: that corollary in the final 2006 edition proves filtered-colimit closure. The elementary final-object pullback criterion in 108 is false, even though the adjacent all-vertex criterion is true. The 115 source-to-item numbering shift discovered during cross-audit has been corrected against the original headings and passages. The metadata claim of zero Pro text for 118 is superseded by the actual supplied file. The 118 presheaf-pushout theorem must not be burdened with a local-test hypothesis needed for a later, different fraction-calculus argument. These changes are explicit in the records rather than concealed by rewritten summaries. [SA27-14–SA27-15, SA27-263, SA27-429, SA27-524; source and merge audit records.]

The links to La Longue Marche, Les Dérivateurs, STRATA, PATHS, BISITE, RESIDUE, S6 and the named research returns remain in a separate project table. Their finite-monoid classifications, path-space theorems, spectral non-detection results and claimed counterexamples are not certified by a page that merely contains a word such as “homotopy,” “proper” or “filtered.” Where a later public manuscript is available, its precise destination has been opened. Where only an earlier note's account of a private result is supplied, the endpoint is explicitly an unverified lead. There is no invented proof, run date or archive locator.

## 5. Present status and the limits of the literature match

Much of the ordinary category and coefficient calculus was already standard or became part of established theories of enriched categories, model categories, test categories, homotopy Kan extensions and derivators. That fact does not imply that every formulation on these leaves is correct. The claims map separately records a source status, a literature class, an exact present-status statement, reference locators and a search trail. A refuted original may have a well-established corrected version; the two are identified separately.

Three historical findings are especially useful. First, the strong W7 witness in Der XII§V.2.1 is much more precise than a general thematic comparison, and its asserted verification is not actually written there. Second, Der XII§V.2.3 expressly uses a totality notion different from Pursuing Stacks; the earlier Der II sequence includes a false proposition, its counterexample and a renewed conjecture. Third, 118 uses relative Theorem A in actual common-base arguments, but the mathematical leaves do not acquire a 1983 date from a reused notice. None of these establishes first occurrence across the entire archive. [SA27-150, SA27-151, SA27-203; DerII; DerXII5; DerXVI.]

The later weak-sieve example also needed mathematical checking rather than deference to print. Taken literally, its finite presentation has homotopy type S², not the stated fundamental group Z; the resulting pushout has type S³. It still gives a valid W∞ counterexample, but its printed wider range cannot be justified by the stated π1 argument. This qualification concerns the opened external edition, not an emendation of the supplied Montpellier text. [DerXIIApp; root checks §2 and finite certificate.]

Publication and circulation are kept distinct. Pursuing Stacks circulated in 1983; Volume I appeared in 2022 and covers §§1–91 and 95–98. It does not turn citations of §§107,136 or 137 into 2022 printed-volume references. The current editor bibliography lists Volume II as forthcoming. The electronically edited Derivateurs manuscripts are likewise not called later printed publications merely because a PDF is available. Rezk's sharp-map paper circulated on arXiv in 1998 and remains listed by its author among preprints; it is not confused with his different published paper on homotopy theories. [PSVolumeI2022; MaltsiniotisBibliography; GrothDerIndex; RezkBibliography.]

The searches used the relevant primary editions, author archives and bibliographies, arXiv, MathOverflow, Numdam and zbMATH discovery routes. Some direct zbMATH review links returned 403. That limitation is logged and is never converted into evidence that a result does not exist. A class D judgment means no exact development was found in the recorded bounded search; it is not a priority claim or a proof of present-day openness. Class F marks an assertion that cannot be identified from the text, not a hard problem that has merely resisted a search. A problem's “why open” field records a source explanation only where one was actually found.

## 6. Reading queue and computations

The scan-reading table is intentionally undecided. It includes variance and tuple order, suspect subscripts or superscripts, the distinction between “aspherical” and “coaspherical,” cancelled text and live margins, and a possible missing product sign. Some entries are high-stakes because a single arrow reverses an adjunction; others concern titles or pagination and do not change the mathematics. A mathematical repair is labelled as such. The next image-based run must decide the ink.

The computations are reproducible and bounded in scope. The root finite-category program closes generator relations under composition, checks associativity and identity laws, enumerates the nondegenerate nerve, verifies d²=0 and computes exact rational ranks. Its outputs certify the stated homology groups; separate geometric arguments identify the sphere types. Other programs check the F2[C2] complex, the tetrahedral face poset and finite algebraic diagnostics. Infinite-fence, finite-rank and unbounded-complex conclusions have analytic proofs; a finite enumeration is not presented as a proof of an infinite quantifier.

The arithmetic on the reused 118/004 sheet is kept documentary. Its first subtotal is correct; the displayed second subtotal differs by 500.00 from the sum under one transcribed reading, while the displayed grand total correctly adds the two displayed subtotals. The alternative reading is also calculated. This is neither a homotopy-theoretic claim nor a silent correction to the sheet. [SA27-526; `outputs/reused_sheet_arithmetic.json`.]

## 7. How to use the deliverables

Start with the entry table when tracing an earlier note; follow its canonical item to the claims and problems. Use the claims' `search_ids` to locate the exact search ledger, and the reference key plus locator to distinguish a theorem from background. The check-event table records textual use, targeted proof checks, independent proofs and computations with different event types. A textual comparison is never promoted to a proof check by the mere presence of a row.

The ranked directions are tasks cut from this consolidation. Each identifies its source items, claims and problems, what is already known, and a first concrete step suitable for a later run. The most useful next work starts with high-impact scan decisions and exact theorem formulations, then returns to the remaining coefficient and lattice questions. No proposed new research programme is developed in that file.

The validation program checks exact index coverage, source immutability, schemas, IDs, bibliography keys and check-event coverage. Those checks support the editorial audit; they do not prove mathematical truth or replace close reading. Original package records, detailed proof notes, search ledgers, programs and outputs are included so that a subsequent reader can reproduce both the decisions and the limited computations.

## 8. Counts and completion record

<!-- COUNTS_START -->
| Register | Count |
| --- | --- |
| Indexed source entries, each with one read verdict | 578 |
| Consolidated items | 462 |
| Supplied scan blocks / page-read records | 112 / 112 |
| Authorial claim records | 224 |
| Separate modern claim refinements | 2 |
| Authorial questions and unfinished steps | 94 |
| Separate historical/editorial questions | 16 |
| Separate modern audit questions | 15 |
| Undecided reading alarms | 148 |
| Ranked future tasks | 15 |
| Link records | 1080 |
| Bibliographic records | 69 |
| References marked verified / unverified | 68 / 1 |
| Recorded search families/actions | 96 |
| Detailed search-ledger rows | 178 |
| Check events | 972 |

### Entry verdicts

| Verdict | Source entries |
| --- | --- |
| kept | 450 |
| merged | 112 |
| corrected | 8 |
| withdrawn | 8 |
| rests on a misreading | 0 |

### Items and source verdicts by item kind

The kind is the read judgment attached to the canonical item. An item can own several source entries; consequently the item column totals differently from the verdict columns.

| Kind | Items | Source entries | Kept | Merged | Corrected | Withdrawn | Misreading |
| --- | --- | --- | --- | --- | --- | --- | --- |
| conjecture | 29 | 34 | 29 | 5 | 0 | 0 | 0 |
| unproved claim | 83 | 121 | 82 | 36 | 3 | 0 | 0 |
| unpursued implication | 5 | 5 | 5 | 0 | 0 | 0 | 0 |
| idea of the earlier run | 12 | 21 | 12 | 8 | 1 | 0 | 0 |
| reading question | 228 | 250 | 226 | 21 | 3 | 0 | 0 |
| self-flagged step | 60 | 86 | 59 | 26 | 1 | 0 | 0 |
| withdrawn in the same text | 13 | 14 | 5 | 1 | 0 | 8 | 0 |
| title, date or page count | 9 | 11 | 9 | 2 | 0 | 0 | 0 |
| other | 23 | 36 | 23 | 13 | 0 | 0 | 0 |

### Authorial claims by literature class

| Class | Meaning | Claims |
| --- | --- | --- |
| A | In his own later published work | 2 |
| B | Developed by others into established results | 34 |
| C | Partly developed or requiring the stated correction/scope qualification | 64 |
| D | No exact development found in the recorded bounded search | 8 |
| E | Known before the dated programme; undated-leaf limits retained | 76 |
| F | Not identifiable precisely from the supplied pages | 40 |

### Authorial claims by status on the pages

The six groups below were assigned by the package readers from their close readings. The full `status_on_pages` field retains mixed states, cancellations in place, conditional counterexamples and unfinished subclauses. A false-as-stated classification does not decide an uncertain reading of the ink. The two modern refinements are excluded from both claim tables.

| Page-status group | Claims |
| --- | --- |
| proved there | 0 |
| proof sketched | 33 |
| stated without proof | 83 |
| corrected by himself later | 12 |
| false as stated | 18 |
| open on the pages | 78 |

### Link categories

| Kind | Records |
| --- | --- |
| folder | 61 |
| published work | 28 |
| our projects | 991 |

All six stages have been completed for the supplied part. Every authorial claim has a mapped search record; every item, claim/refinement and cited result key has a check event. All 112 supplied scan blocks have read records, and all supplied-source hashes match the initial inventory. `outputs/validation.json` records the complete structural checks. Those checks certify coverage and consistency, not mathematical infallibility. The explicit unresolved readings, unidentified assertions, bounded literature gaps and unavailable private-project endpoints remain qualifications of the completed dossier.
<!-- COUNTS_END -->
