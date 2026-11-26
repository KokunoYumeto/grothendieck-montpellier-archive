# SA24 — Pursuing Stacks: the modelizing story

**Alexander Grothendieck, Montpellier archive. Consolidated dossier in English.**

**Assessment date: 19 November 2026.** Cotes 134-1 through 134-8 and 135 are accounted for below. Mathematical judgments concern the supplied transcriptions and the individually identified public comparison texts. They do not assert access to missing archive leaves or to scan images.

## 1. What this dossier establishes

The supplied material has three substantial mathematical strands: the weak-groupoid and coherence programme in the *Take off* material; the attempted linearization of homotopy types through additive intervals, resolving adjunctions and coefficient homology; and the Gr-category/Picard-category calculations, summaries and higher-stack questions in cote 135. Reading them in that order makes their connections visible without replacing Grothendieck’s questions with the terminology of later derivator projects.

The linearization leaves contain real proofs and a real remaining gap. In particular, the bicomplex argument on cote 134-8 scan 54 proves its stated resolving-functor lemma. The following degree-zero counit calculation also works. Neither argument supplies the acyclic-complex counit step explicitly left **“A prouver”** on scan 55. The dossier preserves these three different statuses instead of allowing a nearby “OK” to close the whole proposed theorem. [SA24-30, SA24-33, SA24-34; CL-SA24-042, CL-SA24-045, CL-SA24-048.]

Several broad assertions need narrower hypotheses. Global contractibility of an interval category of elements is weaker than the universal tensor condition used in the proposed linearization. An ordinary counit can be an isomorphism while the derived homology comparison fails. Object inversion in a symmetric monoidal category does not automatically invert its arrows. The claimed nonfaithfulness example involving suspension by S¹ conflicts with the precise symmetric monoidal stabilization theorem, although the conditional argument preceding the example is valid. Each of these conclusions is accompanied by a hypothesis audit or a precise theorem match, rather than a resemblance to later terminology. [CL-SA24-051; CL-SA24-083; CL-SA24-131; CL-SA24-137.]

The literature gives substantial positive results: modern test-category linearization under an explicit strong Whitehead hypothesis, the binomial-cochain comparison asked for in the typed schematization text, the classification of categorical groups and ordinary Picard groupoids, derived descriptions of appropriately strict Picard stacks, and determinant/K-theoretic interpretations of the first stable invariants. Their quantifiers are retained. A 2026 preprint claims the full Grothendieck homotopy hypothesis in a stated coherator convention; this dossier records that claim and the limited scope of its accompanying formalization, without calling the whole proof independently verified here. [Hubert2026, Theorems 5.14 and 6.15; Horel2024, Proposition 4.2; KubrakShuklinZakharov2026, Example 3.7; BaezLauda2004, Theorem 43; SGA4XVIII, §1.4; OpenAI2026HH, Theorem 1.1 and Corollaries 5.1–5.2.]

The complete entry, item, claim, problem, reading and link records are the accompanying machine-readable registers. This overview explains their principal decisions. Its citations use final claim/item/problem IDs and bibliography keys. Physical source line ranges live in the records, so a mathematical conclusion can be followed back to the exact supplied file.

## 2. Corpus, coverage and dating

### 2.1 Every catalogue folder is accounted for

| Cote | Catalogue subject and dates | Catalogue pages | Supplied material and treatment |
|---|---|---:|---|
| 134-1 | Breen, Deligne and Quillen correspondence, 1974–1976 and 1984 | 6 | Marked “other part” in TOPIC.md. No local transcription supplied; accounted for as a coverage boundary. |
| 134-2 | Chapter I, *Take off*, manuscript pp.1–65; typescript dated 19–22 February 1983, with 1975/undated letters and other material | 184 | Three Codex files, 33 supplied scans: 83–91, 93–115 and 128. All read. |
| 134-3 | Chapter II, *Reflections on homotopical algebra*, points 14–44, pp.1–88; 27 February–26 March 1983 | 93 | “Other part”; no local transcription supplied. |
| 134-4 | Chapter III, *Homotopy structures*, pp.89–187; 27 March–9 April 1983 | 100 | One supplied scan, 84: reused Récoltes et Semailles material. Read as provenance, not as a substitute for Chapter III. |
| 134-5 | Chapter IV, *Asphericity structures*, pp.188–319; 11 April–3 July 1983 | 132 | “Other part”; no local transcription supplied. |
| 134-6 | Chapter V, *Homology and cohomology: abelianization of homotopy types*, pp.320–442; 5 July–23 August 1983 | 124 | “Other part”; public comparisons are separately identified, not called an archive-page audit. |
| 134-7 | Chapter VI, *Schematization*, pp.443–554; 24 August–16 September 1983 | 112 | “Other part”; the public §119 comparison is checked explicitly. |
| 134-8 | Chapter VII, *Linearization of homotopy types*, pp.555–593; 22 October–12 November 1983, plus undated handwritten notes | 86 | Pro scans 43–59 and 61–87, plus Codex cover scan 41: 45 supplied scans. All read. The 509 indexed entries concern this Pro package. |
| 135 | Categories and Gr-categories; undated manuscripts and annotated copies | 58 | Four Codex files, 51 supplied scans. All mathematical prose and nonmathematical contents accounted for. |

Source: supplied `SA24_texts/TOPIC.md`, source manifest, and scan markers in the supplied transcriptions. Catalogue page counts total 895; the actual local transcription extent is **130 scans across four cotes**. The catalogue’s Pro/Codex/API columns describe a wider transcription project and are not an inventory of the attachments. For example, TOPIC.md reports 40 Codex pages for 134-2 while the three supplied files contain 33 scan markers, and reports zero Codex pages for cote 135 despite the 51 supplied scans. These are recorded discrepancies, not pages silently assumed to exist.

The source archive was extracted once. Its 24 files are identified by hashes in `evidence/source_manifest.json`; final validation checks that none was altered. There is no supplied second-pass folder for this topic, so the Pro notes and the supplied diplomatic transcriptions are the operative readings. Scan 60 of the Pro packet is absent. That absence is not filled by interpolation.

### 2.2 What “read” and “line” mean here

Each of the 509 stable note entries was read with its relevant transcribed passage. The readers also inspected the whole 44-scan Pro packet when an entry claimed that something was absent. Verdicts and semantic merges were authored after those readings. Scripts numbered passages, saved reading outputs, checked coverage, serialized the decisions and validated links; they did not infer verdicts from headings or keywords. The numbered reading log and the separate readers’ reports document this division of work.

Line numbers are **physical lines in the supplied UTF-8 transcription file**, not printed manuscript line numbers or OCR line numbers. A scan number is meaningful only with its cote and file. Some records give a complete scan-sized range because the argument spans a display and its surrounding qualifications. A bounded-absence locator covers the reviewed corpus and explicitly says that it is not a claim-bearing passage.

The Codex notes are leads, not additional rows in NOTES_INDEX. Their mathematical assertions were checked against the Codex transcriptions and entered directly into the claims and problem registers. Such claims have an empty `items` list with an explanatory `item_scope`; no fictitious indexed note was created to give them an item ID.

Nonmathematical reused material was not mistaken for evidence. Cote 135 scans 4 and 6 contain the song *Lonely Road*; scan 37 is a 1974 Hanoi calendar image transcribed into thousands of TikZ commands. Cote 134-2 scan 91 contains a printed Bourbaki programme; scan 98 is a closing salutation. Their presence helps describe the physical packet but does not date neighboring mathematical writing. The independent locator audit removed these pages from mathematical claim locators where an overly broad range had included them. [Calendar inspection output; root independent audit; core root locator review.]

### 2.3 Attribution and editions

Cote 135 includes two summaries of Hoàng Xuân Sính’s work. The French six-page summary is Grothendieck’s summary of her results; the English thirteen-page summary is Sính’s. The external primary collection and the supplied opening pages were compared. The classification is therefore not reassigned to Grothendieck as an original unpublished theorem. “1975” identifies the thesis context; it does not establish the date of every copied or annotated leaf. [Sinh1975; SinhSummaries; CL-SA24-128, CL-SA24-135.]

Three versions of *Pursuing Stacks* must also remain distinct. `PS2015` is the public transcription used for exact original-page comparisons. `GrothendieckPS2021`, arXiv 2111.01000, is the full extended/revised public transcription by Carmona and Buchholtz, first posted 1 November 2021 and revised 21 November. `PS2022` is the SMF printed Volume I, edited by Maltsiniotis, containing Chapters I–IV, §§1–91 and 95–98. It does not contain the Chapter VI–VII passages discussed here. Neither a matching typed passage nor the 2015/2021 transcription date proves that an undated handwritten leaf preceded a later authorial publication. This is one reason no class-A claim was assigned solely from such a parallel.

## 3. Take off: homotopy types, cells and coherence

### 3.1 The object of the programme

The initial question is how to represent homotopy types by weak higher groupoids. The finite version explicitly concerns n-truncated homotopy types; the later paragraphs state the untruncated infinity-groupoid localization programme. The modern terms “coherator” and the precise weak-equivalence convention clarify these passages, but the truncation restriction is already in the source. [134-2 scans 94, 97, 112; CL-SA24-004; MP-SA24-02.]

The negative comparison with strict infinity-groupoids is substantive. Under the usual strict globular convention, simply connected realizations have the homotopy type of products of Eilenberg–Mac Lane spaces. This does not describe all simply connected spaces and cannot be extended without qualification to arbitrary non-simply-connected realizations. Ara’s Theorem 5.4 supplies the exact modern statement, with its historical attribution. The manuscript’s need for genuinely weak coherence is thus supported by a precise obstruction. [CL-SA24-005; Ara2013Strict.]

The construction begins with globular sources, targets and prescribed compositions. Its standard n-globe has two cells in each dimension below n and one top cell. The allowed amalgamations attach disks along designated hemispherical subcells in a sequential order. This last condition is what makes the asserted contractibility plausible and provable; arbitrary disk gluings need not be contractible. The saved computation checks cell counts and Euler characteristics in finite dimensions, while the proof appendix supplies the general geometric argument. [CL-SA24-006, CL-SA24-009.]

Free successive adjunction of operations and fillers leads toward a globular theory. The source corrects an initial assertion about all fiber products: the structure must preserve the specified globular products, including the explicit postscript on scan 115. Modern definitions in Maltsiniotis and Ara use precisely designated globular sums, with an admissibility convention that must be stated. This is a real correspondence, not permission to restore the deleted all-limits assertion. [CL-SA24-007, CL-SA24-011; Maltsiniotis2010, §§1.4–1.6 and 2.3–2.9; Ara2013Homotopy, §§2–3.]

### 3.2 Three different faithfulness questions

The pages ask whether high-order operations are irreducible, whether a chosen topological realization is faithful, and whether the primitive part can be recovered from a free presentation. The tentative automorphism formula is withdrawn, and confidence in realization faithfulness is weakened. Bourke’s theorem proves faithfulness of cellular connecting functors in the formal theory. It does not prove that every chosen realization into topological disks is faithful, or that every relative endomorphism fixing a primitive subcategory is the identity. [CL-SA24-008, CL-SA24-010, CL-SA24-016; Bourke2020, Theorem 5.2; MP-SA24-03.]

The claimed invariance under choices of coherence also has levels. Equivalence of localized homotopy theories is weaker than an isomorphism of raw model categories and does not specify every coherent higher comparison suggested by the “seven mathematicians” discussion. Those levels remain distinct in CL-SA24-012. The separate binary/n-ary question lacks enough conventions to identify an exact higher theorem and remains class F, even though ordinary monoidal coherence supplies bounded analogues. [CL-SA24-013; MP-SA24-04.]

### 3.3 Fibrancy and the current homotopy-hypothesis claim

Moving from spaces to a model category requires care. The fundamental-groupoid construction in Ara’s Theorem 8.7 works under a stated setup including an ambient model category in which all objects are fibrant. Fibrancy is not automatically preserved by a pushout of contractible fibrant objects along cofibrations. The dossier checks a simplicial counterexample: take the nerves of the indiscrete groupoids on {0,1} and {0,2}, glued at {0}. Both are contractible Kan complexes and the inclusions are cofibrations, but the pushout has the two edges of a composable inner horn and lacks its third edge. The source’s own footnote already questions this point. [CL-SA24-014, CL-SA24-015; MP-SA24-05; `outputs/root_computations.json`.]

As of 19 November 2026, the literature record cannot stop at an older “still conjectural” label. Henry–Lanari’s 2023 paper proves the specified three-dimensional comparison and gives a conditional higher framework. The September 2026 OpenAI preprint states a full theorem for each coherator in its Ara–Henry convention. The associated Lean documentation covers elementary expansions, not the whole later semi-model-category/comparison argument. The dossier read the theorem statements, hypotheses and formalization scope; it did not compile the development or independently audit the full proof. The broad early programme is accordingly class C with an explicit current claimed solution and its scope, rather than either an unqualified established result or an assertion that no claimed solution exists. [CL-SA24-004, CL-SA24-012; HenryLanari2023; OpenAI2026HH; OpenAI2026Lean.]

The correspondence also mentions crossed modules, rational homotopy and fine/tame homotopy. Crossed-module and minimal-model background is kept distinct from the loosely specified fine-homotopy programme. The latter has a direct later conceptual parallel in the *Esquisse*, §§5–7, but these supplied leaves do not define a precise new equivalence theorem. Cox’s algebraic tubular-neighborhood papers are bibliographic leads; the letter explicitly says they had not yet been read. [CL-SA24-002, CL-SA24-003, CL-SA24-001; Sullivan1977; Cox1978I; Cox1978II; Esquisse1984; MP-SA24-01.]

## 4. Linearization: the handwritten argument and its exact gap

### 4.1 Additive intervals and all-degree vanishing

The first Pro leaves contain fraction/cylinder diagrams whose missing definitions prevent a unique general theorem. Scan 45 becomes explicit: an augmentation with a section splits an additive interval as the unit plus its augmentation kernel. Writing the second section through a map λ, the endpoint map is `(x,y) ↦ (x+y,λy)`. At `(x,−x)` its second component is `−λx`, whereas the transcription prints the positive sign. The kernel and monomorphism criterion survive this sign change, but the ink still has to decide the reading. [CL-SA24-017; CL-SA24-018; CL-SA24-019; SA24-7.]

The ensuing projective calculations concern a k-linear abelian monoidal setting, a coefficient functor κ and an adjoint φ. The proposed weak class is detected by derived φ. A crucial distinction is between positive acyclicity of a coefficient unit and the much stronger requirement that a contractor tensor have **zero derived φ in every degree, including degree zero**. The latter requirement is repeated in the source; omitting degree zero changes the argument. Under exactness of tensoring and enough projectives, it can be checked on suitable projective/free resolution terms. The proof uses an acyclic resolution and is given in the core appendix. [CL-SA24-022, CL-SA24-023, CL-SA24-024; scans 46 and 58.]

The elementary adjunction facts are valid with their stated direction and scope. An exact right adjoint makes the left adjoint preserve projectives; the converse uses enough projectives in the source category. For κ with source Mod_k, preservation of all small limits does give a left adjoint by the special adjoint functor theorem, since the module category has the relevant completeness, well-poweredness and cogenerator properties. A generic “missing solution set” objection would be wrong here. The later correction from products to limits must nevertheless be retained. [CL-SA24-027, CL-SA24-029; Mitchell1965, V §3, Corollary 3.2; scan 77.]

The formal small category of degrees and differentials on scan 52 presents nonnegative chain complexes once variance and the relation `d²=0` are supplied. Its opposite-category form reappears on scan 61. The uncertain completion marks on that later page are not identified by this elementary presentation, so the completion-specific claim remains separately class F. Neither notation identifies this handwritten Θ_k with Joyal’s category Θ. [CL-SA24-038; CL-SA24-056.]

### 4.2 What the bicomplex proof proves

For an exact functor Λ from an abelian category with enough projectives into nonnegative complexes, set φ=H₀Λ. If Λ(P) has no positive homology for projective P, applying Λ to a projective resolution gives a first-quadrant bicomplex. One augmentation compares its total complex to Λ(x); the other compares it to the complex computing Lφ(x). Exactness and first-quadrant convergence make both comparisons quasi-isomorphisms. This is the proof written on scan 54, not an inference from a heading. [CL-SA24-042; SA24-30.]

The mechanism is classical: the relevant resolving-functor result and two-augmentation argument already occur in Grothendieck’s 1957 Tohoku paper, §2.5, Propositions 2.5.1–2.5.2, with the derived-composite criterion in §2.4. The bounded bicomplex conventions were also checked in EGA III, chapter 0, §11.3. Their use here does not establish the manuscript’s whole monoidal equivalence. [Grothendieck1957; EGAIII1; CL-SA24-043.]

Projective objects of the abelian category of nonnegative complexes decompose into degree-zero projectives and projective disks. That is stronger than merely being degreewise projective. A nonnegative acyclic degreewise-projective complex is contractible by an induction starting in degree zero. These distinctions justify the formal projective test for the counit, with the exactness assumptions explicitly retained. They do not show that an arbitrary additive resolving functor respects a chosen chain homotopy. [CL-SA24-034, CL-SA24-037, CL-SA24-041, CL-SA24-047.]

### 4.3 The unproved acyclic counit and modern linearization

The degree-zero calculation identifies G(U[0]) with κ(U) by a chain of Hom adjunctions and Yoneda. A nearby flat-resolution argument gives a quasi-isomorphism, not generally a strict isomorphism. The remaining test asks whether FG sends every relevant acyclic projective complex to an acyclic complex. It is explicitly left to prove and is revisited without a completed argument. The dossier therefore records both the formal reduction and the missing implication; they are different claims. [CL-SA24-045, CL-SA24-046, CL-SA24-048; MP-SA24-07, MP-SA24-11.]

Hubert’s 2025 thesis gives an all-complex counit characterization in Proposition 4.2.5 and Corollary 4.2.6, pp.134–135; Remark 4.2.7 marks a related weaker-test issue. The 2026 preprint proves homotopical Dold–Kan/linearization results for test categories satisfying a strong Whitehead condition and establishes the required case of Joyal’s Θ. These are exact, valuable matches. They do not turn the handwritten theorem for an arbitrary k-linear abelian monoidal category into a proved general theorem. The thesis defense was 13 February 2025, its arXiv posting 13 May; the later paper was posted 10 February 2026. No journal publication of that later preprint was verified. [Hubert2025; Hubert2026, Theorems 5.14 and 6.15; CL-SA24-030, CL-SA24-040.]

### 4.4 Why global asphericity is insufficient

The source’s revised wording on scan 58 makes the distinction between an aspherical total category and a relative/universal condition consequential. A finite counterexample checks the weaker, global reading even with separated endpoints and a compatible multiplication. Let A be the span `0→2←1`. Use an ordered presheaf I with fibers `{a<b}`, `{c<d}`, `{u<w<v}`, whose restrictions send `(u,w,v)` to `(a,b,b)` and `(c,c,d)`. Minimum and maximum give distinct natural endpoints; maximum gives a natural multiplicative interval law. Its category of elements is a tree, hence contractible. [CL-SA24-051; core proof appendix §4.]

The augmentation kernel J of Z[I]→Z is pointwise free, and the endpoint difference is universally monic. Nevertheless, tensoring J with the free representable at 0 gives that representable again, with nonzero H₀. Thus contractibility of A/I does not give the required all-coefficient tensor acyclicity. The saved program checks the finite nerve, restrictions, multiplication and homology, while the appendix verifies the general categorical hypotheses. This is not a refutation of an intended stronger “over e” or universal reading; that possibility is exactly why the relevant deleted/uncertain words are on the scan-reading list. [MP-SA24-12; `outputs/core_computations.json`.]

## 5. Coefficients, totalization and binomial operations

### 5.1 Chain calculations are sensitive to scope

The scan-61 tensor-of-cycles formula is false for unrestricted complexes over a ring. Over Z, tensoring `[Z --2→ Z]` with `(Z/2)[0]` produces cycles not obtained by tensoring the original cycle module. Even degreewise freeness is insufficient over Z/4: the natural map `(2k)⊗(2k)→k` is zero while the intersection of the two kernels is nonzero. Neither example disproves a reading restricted to split/projective objects in the category of complexes. The preceding split-complex discussion was read, and the exact completion/scope remains an ink and formulation issue. [CL-SA24-053, CL-SA24-054, CL-SA24-055.]

The first-quadrant totalization question has a precise positive reconstruction in the full module categories. Encode complexes and bicomplexes by small preadditive categories; the finite diagonal-sum functor, with the usual total differential sign, realizes totalization as restriction. Left Kan extension supplies its left adjoint. Preservation of the manuscript’s smaller, uncertain completion is a separate issue. Infinite diagonals in an unbounded direct-sum totalization need not preserve products, so the same statement cannot simply be extended to the unbounded setting. The subsequent monoidal Eilenberg–Zilber compatibility is also separate, not proved by the existence of this adjoint. [CL-SA24-061, CL-SA24-062, CL-SA24-063, CL-SA24-064; MP-SA24-16, MP-SA24-20; EilenbergZilber1953.]

For derived sections, an exact coefficient functor must also commute with ordinary sections and carry the chosen injective resolutions to section-acyclic objects. The manuscript’s projective/Hom argument works on bounded-below derived categories with the explicit tensor/cotensor, completeness and flatness hypotheses recorded in the claims map. Exactness alone is insufficient: Q⊗− fails to commute with a countable product of copies of Z, since the sequence `(2^{-i})` has no common denominator. Likewise Hom_Z(Q,Q)=Q is not projective, so an arbitrary injective coefficient cannot be used to dualize injectives into projectives. [CL-SA24-065, CL-SA24-066, CL-SA24-067, CL-SA24-068; MP-SA24-22, MP-SA24-23.]

### 5.2 Ordinary and derived cofinality

The category-of-elements square and the exact presheaf slice equivalence are genuine links between the handwritten calculations and typed Chapter VII §135. For right presheaves, the homological comma category has the orientation A/b. The coefficient extension and cohomological dual need their own hypotheses and variance. The dossier matches these to the exact representable-testing and homology arguments rather than attaching “Theorem A” indiscriminately. [CL-SA24-021; CL-SA24-070, CL-SA24-071, CL-SA24-073, CL-SA24-074, CL-SA24-082; PS2015, VII §135, pp.563–564; Hubert2026, Proposition 4.6.]

One displayed implication fails on its literal ordinary-Kan reading. For `f:BZ→e`, ordinary coinvariants of a trivial coefficient group give `f!f*G≅G` for every G. Yet `H₁(BZ;Z)=Z`, while `H₁(e;Z)=0`. The free resolution over `Z[t,t^{-1}]` checks this directly. Passing from an ordinary counit to a derived homology comparison requires the missing derived/acyclic condition. A natural all-homology comparison does imply preservation and reflection of homology equivalences; preservation/reflection alone still does not give an equivalence of localized categories. [CL-SA24-083, CL-SA24-084, CL-SA24-085, CL-SA24-086; MP-SA24-19.]

The proposed reconstruction of an arbitrary presheaf as a pushed-forward projective unit also encounters a simple obstruction. In the additive presheaf setting restriction is exact, so its left adjoint preserves projectives. A projective unit can therefore only push forward to a projective F. The source’s subsequent narrowing to ordinary/representable objects is meaningful and retained. [CL-SA24-078, CL-SA24-079; MP-SA24-27, MP-SA24-17.]

### 5.3 The binomial calculation and its modern answer

Multiplication modulo t³ of the expressions `1+at+P(a)t²` forces

\[
P(a+b)-P(a)-P(b)=ab.
\]

For a polynomial law over k, comparison of the ab coefficient forces `2c₂=1`; conversely `t²/2` works when 2 is invertible. Over Q the solutions are `binom(t,2)+ct`. The integer-valued binomial polynomial must not be confused with a polynomial having integral coefficients. The symbolic expansion and finite negative/positive integer checks are saved, and the proof appendix gives the universal coefficient argument. The elementary identity is class E, with its SGA 6 antecedent; a public transcription of a parallel does not make it a later authorial discovery. [CL-SA24-080; SGA6, Exposé V, §§2.1(iii), 2.5(a), 2.6–2.7.]

The larger homotopical question is identifiable through typed Chapter VI §119, original pp.501–504. Horel’s Proposition 4.2 proves the canonical free-binomial cosimplicial comparison with integral cochains of K(Z,n), for n≥1. Kubrak–Shuklin–Zakharov’s derived binomial formulation gives the corresponding derived construction in Example 3.7. Their broader reconstruction results impose connectedness, nilpotence and finite type. The first arXiv versions were posted in November 2022 and August 2023 respectively; the journal publications are 2024 and May 2026. These exact results justify class B for the identified comparison, while not supplying every reconstruction claim on the sparse handwritten leaf. [CL-SA24-081; MP-SA24-18; Horel2024; KubrakShuklinZakharov2026; Ekedahl2002; Toen2020.]

### 5.4 The later interval and duality leaves

For a finite projective coefficient module, the unit/counit rank criterion quantifies over **every** coefficient and permits local rank zero as well as one. Existence of two adjoints does not by itself make every unit epic or every counit monic. A short exact unit-kernel sequence needs the epimorphism hypothesis. Reverse dual formulas need reflexivity or a suitable finite-projective condition; the fact that a dual happens to be finite projective is insufficient, as Z/2 with zero Z-dual demonstrates. [CL-SA24-091, CL-SA24-092, CL-SA24-093, CL-SA24-094, CL-SA24-096; MP-SA24-26, MP-SA24-14.]

The interval-transfer assertion on scan 81 is false under all its written hypotheses. The checked example begins with an ordinary multiplicative chain interval over Q and adds a summand Q[2], while retaining the augmentation, endpoints and comparison maps. The extra degree-two homology survives. Its repair requires an additional condition, such as universal tensor weakness of the comparison itself. Searches and backward references did not locate a development of the literal assertion; its class-D label records that bounded result, not an open conjecture or a novelty claim for the counterexample. [CL-SA24-097; MP-SA24-15; REF-LATE-1.]

On scan 84 the proposed β really does send both source endpoints to the first target endpoint. The displayed computation works; it does not achieve the desired two-endpoint compatibility. Scan 86 gives a valid Ext¹ obstruction criterion for extending a map along a specified short exact sequence, but the required exact sequence and λ-exactness application are unfinished. The early lift on scan 59 and these later attempts are merged into one problem with distinct unresolved substeps. [CL-SA24-098, CL-SA24-099; MP-SA24-13; REF-LATE-7.]

## 6. Gr-categories, Picard structures and higher extensions

### 6.1 Group, action and cocycle

Sính’s classification keeps three pieces of data: a group π₀, an abelian π₁ with its π₀-action, and an associator class in H³. The pentagon is the cocycle condition; changing skeletal choices changes the cocycle by a coboundary. Lifting prescribed maps between pinned categorical groups has an H³ obstruction and, when possible, an H² family of equivalence classes. The transformation level has its own cochain equations. These are not classifications by two abstract groups alone. [CL-SA24-104, CL-SA24-106, CL-SA24-128; Sinh1975; BaezLauda2004, Theorem 43 and Corollary 44.]

The kernel/bitorsor passage relates this class to the classical Mac Lane obstruction. For F-bitorsors the invariants are Out(F) and Z(F), with their natural action. The question whether every H³ class can be realized by an abstract kernel already has a classical positive answer: Mac Lane, IV §9, Theorem 9.2, gives a construction and refers back to Eilenberg–Mac Lane for the all-group form. The exclusion of C₂ from that particular book proof is not an exception to the theorem. The geometric 2-gerbe comparison remains separately stated. [CL-SA24-107, CL-SA24-108; MP-SA24-28; MacLaneHomology; Breen1994, §§6–7.]

The automorphism problem on cote 135 scans 19–20 also depends on the morphism level. In the ordinary monoidal self-equivalence groupoid of a split categorical group, the identity automorphisms form Z¹(G,M). Quotienting further by 0-cochains gives H¹ and an additional H⁰ level only after adjoining a different notion of higher modification. The explicit C₂-action on C₃ by inversion separates these groups: Z¹ has three elements while H¹ is trivial. [CL-SA24-113; MP-SA24-31; root proof appendix and computation.]

### 6.2 Ordinary Picard groupoids versus sheaf Picard stacks

With a monoidal structure fixed, two compatible symmetries differ by an antisymmetric biadditive form. Its diagonal is a homomorphism into 2-torsion; “antisymmetric” is not “alternating” in the presence of 2-torsion. For ordinary abelian groups every such diagonal is realized: choose an F₂-basis of M/2M and put the desired values on the diagonal. The source contains this proof, and the dossier independently reconstructs it. A global basis is not thereby available for arbitrary sheaves. [CL-SA24-101, CL-SA24-102.]

For ordinary Picard groupoids, the pinned invariants are M, N and σ:M→N[2]. The underlying ordinary Gr-category has trivial action and zero associator class, but `k=0` alone is not a sufficient condition for a general Gr-category to admit a Picard structure: abelian π₀ and trivial action are also needed. The split example with π₀=C₂ acting nontrivially on π₁=C₃ checks that omission. Identical maps on π₀ and π₁ do not identify functors either; an Ext¹ ambiguity remains, as the source itself soon acknowledges. [CL-SA24-103, CL-SA24-109, CL-SA24-110; MP-SA24-29.]

On a general topos, strictly commutative Picard stacks are described by two-term complexes, and the Ext² extension class need not vanish. SGA 4 XVIII §1.4 supplies the equivalence and the derived Hom, tensor and pushforward comparisons. The F-torsor stack is specifically BF=st(F[1]), with homotopy sheaves π₀=0 and π₁=F; it has no Ext²(π₀,π₁) class. Its ordinary global groupoid can split noncanonically without implying that every Picard stack with two nonzero homotopy sheaves splits. [CL-SA24-111, CL-SA24-122, CL-SA24-129; SGA4XVIII, §§1.4.15–1.4.21.]

The universal realization of arbitrary sheaf σ is the most delicate unresolved identification in this audit. The manuscript asserts a universal Ext-vanishing argument. Breen’s §7.9, equation (7.9.2), supplies an exact sequence ending

\[
\operatorname{Ext}^2(M,N)\longrightarrow H^5(K(M,3),N)
\longrightarrow\operatorname{Hom}(M/2M,N)
\longrightarrow\operatorname{Ext}^3(M,N).
\]

It records the punctual-topos collapse but does not itself prove that the last boundary vanishes universally. Conversely, a nonzero Ext³ group does not prove a nonzero value of that boundary. Backward checks of Breen’s 1969 and 1998 papers do not close this specific inference. The dossier therefore reports the exact obstruction and the limit of its searches. It does **not** claim that the question is currently open in the literature. [CL-SA24-112; MP-SA24-30; Breen1994; Breen1969; Breen1998.]

### 6.3 Higher stacks, envelopes and K-theory

The higher-stack leaves combine several different programmes: stackification and inverse images, detection of homotopy type by locally constant higher stacks, higher Picard envelopes, and base-change/Lefschetz hopes. Modern higher-topos theory gives precise versions with site, truncation and hyperdescent hypotheses. It does not identify a single theorem with every loosely stated higher “n-equivalence” on these pages. Hom-wise equivalence also needs essential surjectivity to imply an equivalence of categories; a one-object subcategory of a two-object discrete category checks the omission. [CL-SA24-115, CL-SA24-116, CL-SA24-117, CL-SA24-118, CL-SA24-119, CL-SA24-120; LurieHTT.]

The meaning of “strict” is equally important. Two-term complexes classify strictly commutative Picard 1-stacks; Tatar gives the appropriate length-three/Picard-2-stack result. Non-strict Picard 2-categories model stable 2-types, and strictness in a permutative/Gray convention is not the assertion that every self-symmetry is the identity. None of these references supplies an unrestricted theorem identifying every higher Picard stack with an ordinary complex on every site. [CL-SA24-121, CL-SA24-123; Tatar2011, Theorem 6.4; GJO2019, Theorem 6.1; GJOS2017, Theorem 3.14.]

Object inversion is distinguished from groupoidification. A one-object symmetric monoidal category with endomorphism monoid N already has an invertible object, but still has noninvertible arrows. The English summary’s use of the isomorphism core is consequently important. Applied to finitely generated projective modules with direct sum, the Picard envelope has the expected K₀/K₁ interpretation; changing to all finitely generated modules changes the split relations. Koszul self-symmetry of an odd line gives the sign −1, and the corresponding K-theoretic transposition describes the first stable η-operation. When this invariant is nonzero, it obstructs forgetting all commutativity data into a compatible two-term complex; it does not deny that abstract abelian groups can be placed in a complex. The sign can vanish, in particular in characteristic 2. [CL-SA24-126, CL-SA24-131, CL-SA24-132, CL-SA24-133; MuroTonks2007; MuroTonksWitte2015; Segal1974.]

The ring-category question also has a precise scope. Categorical rings are classified by third Mac Lane cohomology in the indicated convention. Braided Ann-categories have an abelian-cohomological classification; symmetric multiplication imposes the additional symmetry relation on β. A result about ordinary categorical rings does not automatically solve the doubly symmetric version proposed on the page. [CL-SA24-134; MP-SA24-39; JibladzePirashvili2007; QuangHanh2015.]

Finally, the stabilization page contains a valid conditional: nonfaithfulness of the comparison from ordinary suspension localization to monoidal fractions would obstruct a compatible ACU structure, by the two universal properties. Its asserted S¹ example is false in the stated symmetric-smash setting. Voevodsky’s Theorem 4.3 and Robalo’s Theorem 2.14 apply to ordinary categories: eventual triviality of the cyclic permutation on T³ gives the symmetric monoidal object localization. For S¹ that permutation on S³ has degree +1 and is homotopic to the identity. No finite-CW restriction is needed for the general categorical theorem, and no identification of all-space ordinary stabilization with the entire category of spectra is asserted. [CL-SA24-137; MP-SA24-41; Voevodsky1998, p.588; Robalo2015, pp.445–446; FreydStable1966, §2 pp.124–125 and §4 p.137.]

## 7. Earlier notes, readings and cross-project links

The earlier notes were valuable in identifying questioned counits, interval lifts, coefficient changes, binomial operations and relations to the typed *Pursuing Stacks* text. Their main weakness was that repeated private-context comparisons came to dominate the register. Of the final items, 287 are classified primarily as ideas of the earlier run. That is a provenance classification, not an assertion that 287 original Grothendieck claims were found or proved.

The consolidation corrects seven source-entry verdicts and records 130 merged entries. An especially clear correction is entry 30’s treatment of the scan-54 lemma as unproved: the passage contains the bicomplex proof. Other corrections preserve a mathematical scope or reading qualification instead of converting a damaged formula into a theorem. Five items concern withdrawals or corrections within the manuscript itself; their item kind is distinct from the verdict on whether an earlier note faithfully reported them.

The 82 reading alarms are deliberately undecided. They include the endpoint sign, mixed disk indices, a possible missing derived/weak-equivalence label, product-versus-limit wording, the Ext degree controlling existence versus ambiguity, the group action omitted from a skeletal tensor formula, cocycles versus coboundaries, a repeated π₀ where the 2-groupoid level requires π₂, and the S¹ stabilization example. Each row gives the current transcription, a mathematical alternative, its evidence, the dependence of the argument, and confidence. Two alarms on the same physical range were not merged when they concern different mathematical issues. No supplied transcription was changed.

The public links table contains checked archive-to-archive or published-work comparisons. The separate `SA24_project_leads.tsv` retains 392 attributed links to La Longue Marche, Les Dérivateurs, S6 and named research registers/runs. Their source note IDs and run labels survive. A private “Proved” or review label is not promoted to a verified result here: those private proof/context files were not supplied.

Some public DER endpoints were available and read. DER II, manuscript pp.36–36ter, contains a question, a retracted proposition and a renewed conjecture about total asphericity and filteredness. DER XII V §2.1, pp.75–78, supplies the strong W(7 bis) and cube discussion, absent from the local Pro packet. DER XII V §2.3, pp.88–91, uses an all-functor/category-of-elements total-asphericity definition that is not automatically the local tensor predicate. These comparisons establish precise leads and prevent a false identification; they do not verify private alleged counterexamples or later research-run conclusions. [SA24-1, SA24-2, SA24-84; DERII; DERXIIb.]

The same discipline governs published parallels. PS VI §121, pp.508–509, concerns a different adjunction, so its nonisomorphic counit is not imported as a counterexample to the handwritten resolving adjunction. PS VII §140, p.593, mentions abelianization scratchwork but does not identify or date every supplied leaf. The *Esquisse* gives a genuine thematic continuation of tame topology, with exact sections checked, not a proof that every informal hope on the letter was realized. [PS2015; Esquisse1984; links register.]

## 8. Check strength and reproducibility

The event ledger distinguishes source comparison, targeted proof checking, independent re-proof, finite computation, and background use. Reading a theorem statement was not counted as verifying its proof. Finite certificates test signs, boundary compositions, ranks and explicit counterexamples; they do not certify universally quantified classification theorems. The universal arguments that accompany them are written out in the proof appendices. Sính’s symbolic boundary check, for example, verifies d²=0 in the recorded formulas, while finite H² examples do not prove exactness of the whole resolution.

Every final item, claim and bibliographic reference has a direct check-event record. Every claim has at least one recorded search/retrieval mapping. The combined search log retains exact later query batches and distinguishes earlier retrieval batches for which the exact query text was not retained; it does not fabricate those queries. The searches include arXiv, zbMATH-indexed results, MathOverflow, Numdam, relevant EGA/SGA loci, author bibliographies and backward references. Blocked or failed primary accesses are stated, and metadata-only verification is not passed off as theorem reading.

All 86 bibliography records have an explicit verification note. “Verified” means that the identified URL/DOI was opened in the recorded scope, not that the entire work’s proof was verified. The three unverified historical leads are marked accordingly. First arXiv circulation, receipt/defense dates and journal dates are separated where known; when a first-circulation date was not established, no date is invented.

The archive preserves the authored programs, their outputs, source/reading manifests, the working-to-final ID map, independent audits and progress log. Original attachments and downloaded full public books/papers are excluded; their identities, URLs, verification scopes and retrieval outcomes remain. Computational reproduction uses the supplied attachment layout described in README.md and the reproduction guide. No fresh research direction in the ranked list has been developed as a separate project here; proofs and counterexamples in this dossier check claims already under review.

## 9. Final counts and interpretation

### Coverage and outputs

| Category | Count |
|---|---:|
| Indexed entries | 509 |
| Consolidated items | 373 |
| Claims | 137 |
| Problems | 41 |
| Reading alarms | 82 |
| Checked public/archive links | 53 |
| Separate project leads | 392 |
| Bibliographic records | 86 |
| Search/retrieval log rows | 194 |
| Check events | 800 |
| Ranked directions | 12 |

### Entry verdicts

| Category | Count |
|---|---:|
| kept | 372 |
| merged | 130 |
| corrected | 7 |
| withdrawn | 0 |
| rests on a misreading | 0 |

### Items by primary kind

| Category | Count |
|---|---:|
| conjecture | 0 |
| unproved claim | 28 |
| unpursued implication | 7 |
| idea of the earlier run | 287 |
| reading question | 8 |
| self-flagged step | 25 |
| withdrawn in the same text | 5 |
| title, date or page count | 9 |
| other | 4 |

### Claims by class

| Category | Count |
|---|---:|
| A — identified in his own later publication | 0 |
| B — developed by others into established results | 28 |
| C — partially developed / exact residual scope stated | 31 |
| D — no development identified after recorded searches | 1 |
| E — classical background / known beforehand | 60 |
| F — exact theorem not identifiable from the pages | 17 |

### Claims by primary page status

| Category | Count |
|---|---:|
| proved there | 6 |
| proof sketched | 32 |
| stated without proof | 50 |
| corrected by himself later | 4 |
| false as stated | 6 |
| open on the pages | 39 |

### Reference verification

| Category | Count |
|---|---:|
| verified | 83 |
| unverified | 3 |


The six primary page-status categories give one counting status per consolidated claim. `status_detail` and `variants` retain mixed cases, such as a proved conditional with an unqualified false corollary, or a source correction followed by a residual question. Thus “six false as stated” is not the count of every counterexample discussed in the dossier. Likewise class F means an exact theorem is not identifiable from the supplied formulation; class C identifies a bounded established part and a residual source or literature-identification issue, not necessarily a known open problem today.

There are no class-A entries because no reviewed exact claim was responsibly assigned to a demonstrably later authorial publication on the available chronology. The single class-D entry is the literal interval-transfer assertion, searched and refuted under its written hypotheses. Neither count is a blanket judgment about the historical influence of *Pursuing Stacks*.

The ranked tasks in `SA24_directions.md` turn the remaining bounded questions into separate research assignments. The most consequential are the exact missing counit implication, the universal interval condition, the ordinary/derived cofinality distinction, and the precise sheaf Picard realization assertion. Each direction names the item, claim and problem records from which it arises and states what a few hours could reasonably establish.
