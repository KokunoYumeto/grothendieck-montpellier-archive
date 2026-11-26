# SA12 — Séminaire de Géométrie Algébrique: consolidated dossier

**Alexander Grothendieck papers, Montpellier archive; part 1, cotes 29, 31 and 33.**
**Assessment date: 19 November 2026.**

## 1. Result, scope and how to use the dossier

This dossier consolidates all 342 entries of the supplied `NOTES_INDEX.tsv`, the corresponding Pro notes and doubts, and the supplied Pro and Codex transcriptions. Each indexed entry has one passage-based verdict. The claim and problem maps also include the supplied leaves outside the Pro index. The record tables distinguish the diplomatic text, the later literature, earlier-run suggestions and this review’s reconstructions. They do not modify any transcription.

The principal result is a substantially more discriminating account of what these folders contain. Much of the material has precise descendants in SGA 1, SGA 2, SGA 3, SGA 4 and SGA 7. Several apparently surviving questions are closed by later work, including the characteristic 2 Lefschetz-pencil question and the cancelled EGA implication. Several broad formulations fail, with explicit examples checking the written hypotheses. Other questions remain exact identification problems because the leaves omit a definition or refer to an absent preliminary text. These outcomes must not all be called “open.” The mathematical and historical conclusions below refer to the numbered claim records and the verified bibliography; the complete arguments and source-access limits are retained in the package reviews.

### Supplied corpus

| Cote | Indexed Pro entries | Supplied transcription files | Distinct supplied scan labels | Main sequence |
|---|---:|---:|---:|---|
|29|133 in two packages|21|213|Tame covering data and realizations; finiteness and birational invariants; formal inertia; finite and infinite torsor fundamental objects; descent and Galois categories.|
|31|118|4|93|Flat/Galois cohomology; multiplicative-type groups; local cohomology; transfer and ramification; cohomological dimension; purity and base change.|
|33|91|1|48|Étale-cohomology programme, supports and purity, compact supports, fundamental classes, trace and duality; reused algebra and root-system sheets.|
|**Total**|**342**|**26**|**354**|All supplied loci are accounted for in `SA12_source_coverage.tsv`.|

“Scan label” means a locus identified by `\scanpage{N}` in a supplied transcription. No original scan image was supplied or inspected. Pro and Codex are independent text witnesses; neither is promoted to an ink correction. The attachment contains no second-pass changes for these packages, which is an expected source condition. Missing labels inside the numerical ranges are not silently reconstructed: cote 29 lacks 7, 190 and 208; cote 31 lacks 34, 40, 41, 46, 53, 64, 73 and 89. Cote 33 supplies 2–49. The catalogue’s larger page counts and the other cotes listed in `TOPIC.md` describe the wider topic; this part’s instructed scope is the supplied material of 29, 31 and 33. [Source inventory; `SA12_source_coverage.tsv`.]

The second cote 29 Pro package has **four indexed `###` umbrella entries**, containing 56 internal `####` notes. All 56 internal notes were read and evaluated, but only the four actual index rows receive verdicts. `reviews/29b/internal_note_map.tsv` preserves this relationship. Creating 56 synthetic index rows would have broken the supplied index.

The authoritative consolidated files are at the archive root. `SA12_id_map.tsv` resolves every package-local identifier to its canonical identifier; the original review records remain in `reviews/`. Semantic merges were decided by comparing the actual subject and hypotheses, not by matching headings. The consolidation preserves a later corrected version, a counterexample to an early version, or a genuinely new clause within a shared source bundle. In particular, the Bertini sheet is partially redistributed among its repeated claims while its additional local-property assertion remains separate. The audit of these decisions is `outputs/semantic_merge_audit.json`.

## 2. Cote 29 in its documentary and mathematical order

### 2.1 Tame data, realization and the distinction between an abstract cover and a scheme

The early leaves start with tame ramification data, relative group actions and realization functors. The relevant objects are not merely finite covers of one fixed scheme: the text compares categories built from a group acting on a scheme, chosen fibres, Kummer data, and the ways these categories change when one refines the data. The letters and editorial comments must be attributed correctly. In particular, the opening Murre letters are Murre’s words about the manuscript; their presence in Grothendieck’s papers does not turn every sentence into an authorial theorem of Grothendieck. The early source review records the speaker and the scope of each assertion. [Early29 source review and claim records.]

Two general distinctions govern these pages. A fibre over one chosen point may miss an entire component of a realization, even when the base scheme is connected. Also, uniqueness of extra structure on a realized cover depends on the admissibility of the Kummer data. Conditions imposed for a separate stronger theorem cannot be imported into every preceding definition without saying so. The supplied early pages and the late categorical continuation were therefore checked together with the actual realization hypotheses. The early review contains the explicit component and repeated-divisor tests, with their qualifications; the independent peer check records why the relevant source definitions do or do not exclude each example. [Early29 claim map; `reviews/29a/peer_early29_checks.md`.]

Finiteness of quotient realization also needs a hypothesis on the base. For the characteristic-zero nonnoetherian ring $A=\mathbf Z\ltimes V$, where $V=\bigoplus_{n\geq1}\mathbf F_2$ is a square-zero ideal of 2-torsion, the sign action of $C_2$ on $B=A[\varepsilon]/(\varepsilon^2)$ is faithful, but $B^{C_2}=A\oplus V\varepsilon$ is not a finite $A$-module. Thus a finite group quotient of a finite scheme need not remain finite over an arbitrary base. A locally noetherian base or invertibility of the group order gives the sufficient repairs recorded separately. [CL-SA12-965–966; `reviews/29early/calculations.md`.]

The late leaves return to this distinction in more abstract language. A category of local data can satisfy useful exactness and descent properties without all of its descended objects being representable by schemes. The opened Stacks doubled-line descent example gives a precise obstruction: local scheme data can descend to a nonschematic algebraic space, even with trivial local structural groups. Thus an unconditional scheme-realization claim needs an effectiveness/representability hypothesis or an enlarged target category. Conversely, the finite-frame construction has a positive argument under G0–G3 and a conservative FinSet-valued functor preserving finite limits and finite coproducts. Its degree and descent assumptions remain explicit; an extra quotient axiom is not added when effective descent already supplies the needed quotient. [Late29 proofs and claims; Stacks03FN.]

The cancelled equivalence between a faithfulness condition and an additional realization condition is tested separately. Essential surjectivity also cannot be deduced from an empty notion of subordination: the covering condition on the dominating object matters. For the proposed G0–G5 characterization, the slice interpretation of the rank condition and its literal unsliced interpretation have different consequences. The countable-set diagnostic is therefore explicitly conditional. It is not reported as a blanket refutation of every possible reading of the axioms. [Late29 categorical claim and problem records.]

### 2.2 Finiteness of coverings and the generic-fibre argument

The relative-finiteness cover at scan 47 introduces a generic-fibre descent argument. The initial lemma at 48 is materially sensitive to the adjective transcribed as a reduced/bireduced condition. Katz–Lang’s exact smooth, surjective, finite-type version over a normal connected locally noetherian base has a proof by normalization and descent, with connected geometric generic fibre. A proper homotopy theorem does not automatically settle a possibly nonproper, weaker-fibre version. That distinction remains explicit in CL-SA12-001–002 and MP-SA12-01. [KatzLang1981, Preliminaries Lemma2; Stacks0BUM.]

The degree-zero finiteness question has a strong later answer. Déglise’s account of Gabber proves constructibility of direct image of a constructible finite-set étale sheaf for finite-type morphisms over a noetherian base, without the manuscript’s universal-Japanese restriction. Its degree-one and punctured-local results have different hypotheses. The review independently proves finiteness of Hom between constructible finite-set sheaves by a common finite stratification and conservative geometric stalks. It does not infer the adjacent nonabelian finite-fibre gluing assertion from finite Hom alone. [CL-SA12-003–005; DegliseGabber2007, Theorems1.1–1.4.]

The reductions on scans 54–58 retain their quantification over normal integral subschemes, finite étale base changes and subgroups of products of finite groups. Finiteness of maps to each fixed finite group is weaker than uniform topological finite generation of a profinite group. The checked product of elementary abelian groups at distinct primes, with unbounded ranks, separates these notions. Likewise, Artin–Schreier classes show why removing prime-to-characteristic restrictions changes affine finiteness and product statements: classes of increasing degree on A¹ and the mixed class xy on A² supply the actual obstructions. These tests reject proposed strengthenings, not the correctly restricted tame theorems. [CL-SA12-006–017; `reviews/29a/independent_checks.md` §§2–3; ESS2021.]

The reading “finite generation” versus “finite presentation” at 64 is not cosmetic. Modern finite-presentation results for suitable smooth compactifications and for connected proper schemes have precise hypotheses. They do not identify every quotient defined using divisorial wild inertia on an arbitrary singular compactification. The corresponding problem is kept at the exact boundary of those results. [MP-SA12-06; ESS2021; LSS2023.]

The early uniformity and prime-to-characteristic finite-presentation questions have a particularly precise later comparison in Orgogozo's 2003 article. The recovered appended erratum corrects eight lines of the proof of Theorem 2.2; it neither retracts nor adds hypotheses to the cited Corollary 4.4 or Theorem 4.11. Their proof dependencies use the corrected theorem. The added tame field-invariance corollary retains a good-compactification hypothesis. The full appendix was read by both package reviewers and the root reviewer. Its separate first-circulation date is not established by the 2007 HAL metadata; the complete appendix is present in the recovered 2011 archived copy. [CL-SA12-949,952,957,958; Orgogozo2003; OrgogozoErratumHAL; `reviews/33/auxiliary_orgogozo/ERRATUM_SCOPE.md`.]

### 2.3 Generic and special sections

The early Bertini formulation at 67 says only that X is irreducible over an arbitrary field. This is inadequate for geometric generic irreducibility: P² over C, regarded over R, is integral but splits after extending scalars to an algebraic closure. The later scan 113 explicitly supplies geometric irreducibility. These are now one claim with two versions, CL-SA12-021, rather than two unrelated notes or a silent correction of the first transcription.

For the general morphism version, Poonen–Slavov Theorem 1.8, Lemma 7.1 and the proof in §7 provide the exact modern comparison. If the image has dimension at least 2, the bad hyperplanes form a proper locus; successive **generic** sections give the stated codimension range. Properness and normality are not needed for that assertion. Theorem 1.5 of the same paper has an equidimensional-fibre hypothesis and must not be substituted while dropping that hypothesis. The paper first circulated on 23 January 2020, appeared online on 4 August 2020, and was printed in 2022. Its backward reference to Jouanolou was followed as a reference, but the book itself was not opened. [CL-SA12-021; PoonenSlavov2020/SA12_PoonenSlavov2020.]

The fundamental-group argument needs the inverse image of the section in **every connected finite étale cover** to remain connected. A global normal or suitable geometric-unibranch hypothesis makes the geometric-irreducibility argument applicable to those covers. The later Corollary 3 on scan 113 weakens this to a small image for the local bad locus. That version is false, even when X is proper. Separately, the target π₁(X) must be distinguished from π₁(X_K) over the geometric generic parameter field: full base-field invariance uses properness, while the prime-to-characteristic comparison has broader scope. SGA 1 X 1.8, X 1.10 and X 2.10–2.11 supply the exact published comparisons. [CL-SA12-023.]

The counterexample is explicit. Over C, blow up a point q of P² and identify two distinct points on the exceptional curve. The resulting proper geometrically integral surface X still maps to P² and is an isomorphism away from q. All its bad points map to q, so the source's small-image condition holds for sections of codimension one. Every line avoiding q pulls back to P¹. Nevertheless, cross-gluing two copies of the normalization produces a connected finite étale double cover of X whose restriction to that P¹ is disconnected. The opened pushout and finite-étale descent theorems establish that this is an algebraic cover, not merely a topological picture. The obstruction is precisely that a connected cover of this non-unibranch integral X can be reducible. The full construction checks every written hypothesis. [CL-SA12-023,055; `reviews/29a/bertini_pinching_counterexample.md`; Stacks 0ECH and 0EK3.]

Proper connectedness itself survives. For proper geometrically irreducible X and 1≤s≤dim f(X)−1, every inverse linear section of codimension s is geometrically connected. The higher-codimension reconstruction uses the universal Grassmannian incidence family and Stein connectedness over the normal parameter space; it does not assume that arbitrary special intermediate sections are irreducible. Thus Corollary 4 is retained, while its attached Corollary 5 on π₁ fails under the written local-only conditions. The local unibranch/normal/smooth assertion on the same sheet remains a separate, qualified literature match, CL-SA12-241; the counterexample does not refute that assertion. [CL-SA12-024; MP-SA12-08,73; SGA1 X2.10–2.11.]

The tame Lefschetz request at scan 82 and explicit Theorem 6 at 114–115 are consolidated as CL-SA12-055/MP-SA12-20 with their different hypotheses retained. The same pinched surface refutes the later theorem: take the boundary D empty, so tameness is vacuous; X and the map are smooth/isomorphic near the chosen section, satisfying even a strong local reading of the source. The proof sketch uses the false Corollary 3. By contrast, SGA 7 XVIII 6.1 gives a valid published surjectivity argument in its own setting. Esnault–Kindler's regular proper/SNC theorem distinguishes Lef surjectivity from the stronger Leff isomorphism statement; its normal-variety extension also needs the ample-complete-intersection condition in the 2016 erratum. The false literal draft is not an open conjecture, and it is not certified by a related published theorem. [SA12_SGA7XVIII; EK2016; EKerr2016; the saved counterexample.]

The characteristic 2 vanishing-cycle question at 115–116 is **closed**, not a proposed new research task. Deligne’s Weil II gives the more restricted sufficiently general-pencil comparison. Orgogozo’s §11, using a 2005 Gabber letter, proves the required monodromy conclusion for Lefschetz pencils without the additional dual-transversality condition, with finite invertible coefficients. Vanishing cycles are conjugate up to sign and the monodromy image agrees with the universal hyperplane system in the specified setting. This does not assert surjectivity of the ordinary fundamental group of a line complement onto that of the whole parameter complement in characteristic p. First arXiv circulation was 22 July 2005; publication was 2006. [CL-SA12-245; MP-SA12-75; SA12_Orgogozo2006; SA12_Illusie2006; SA12_Deligne1980.]

### 2.4 Birational fundamental groups and nonreduced Picard objects

The pages on models require one fixed source for their inverse-limit argument. Fixing the regular locus of a proper normal projective model, then using properness, purity and connected-cover surjectivity, supplies compatible maps to the other model groups. Compactness gives the map to the inverse limit. Unrelated genus bounds on changing models would not do this. A regular proper model gives stationarity; uniform finite generation by itself does not. [CL-SA12-026–029; SGA1; Stacks0BMB/0BX7.]

The shortcut identifying the regular-locus fundamental group of any normal proper model with the birational group is false. The checked quotient of P¹×P¹ by simultaneous sign inversion has four A₁ singularities and a nontrivial étale double cover of its regular locus. Its rational function field has a simply connected regular proper model; the associated quadratic extension also ramifies at a valuation with a centre on every proper model. Thus that regular-locus cover cannot become étale on a proper modification. The codimension-two pullback step has an independent elementary defect: blowing up a surface point turns the omitted point into a divisor. Neither example is represented as a refutation of a correctly stated surrounding finiteness theorem. [CL-SA12-020,030; `reviews/29a/independent_checks.md` §§3–4.]

The Picard pages concern scheme-level Pic^τ, including infinitesimal structure. Reduced birational Picard invariance, equality of tangent dimensions and a genus bound for the classical Picard variety do not settle that stronger statement. The finite group schemes α_p ⊂ α_(p²) have the same geometric-point and tangent-space tests but different lengths; the sequence α_(p^m) has unbounded length despite those coarse bounds. These are counterexamples to proposed abstract criteria, not fabricated geometric counterexamples to the full Picard theorem. All Frobenius iterates matter: agreement at ker F alone does not give agreement at every ker F^ν. [CL-SA12-033–052; MP-SA12-12–17; Kleiman2005; KLOS.]

KLOS provides an exact route to bounding the reduced Picard dimension by restriction to a suitable complete-intersection curve. It does not establish stabilization of all nonreduced Pic^τ on unrestricted normal models. Three conservative class D records retain the recorded searches for model stationarity, the codimension-two kernel question and nonreduced Picard stabilization. The label reports that no exact development was identified in those searches; it is not a novelty claim or a proof that the mathematics remains open. [CL-SA12-029,031,046.]

### 2.5 Formal inertia, Chern classes and the two explicit obstructions

Murre’s 30 April 1969 letter explains a concrete bottleneck: a missing generalized-Kummer algebra lemma led the preliminary argument to use ordinary Kummer lifting and impose pairwise disjoint boundary components. Other draft-numbered doubts refer to realization, normality, canonicity or an absent Giraud letter. Those numbers and dependencies are preserved; unspecified categories are not filled in from a familiar modern theorem. The Grothendieck–Murre 1971 contents provide an exact chapter-level match, including the comparison of two H² classes, but access to contents does not certify the unavailable theorem text. [CL-SA12-053–062,095–102; MP-SA12-18–39; GM1971.]

In the formal setup, U lies in the special divisor after removing the induced remaining boundary. It is not the complement of that special divisor in the underlying formal space. Inertia has a cyclotomic action. The finite tame extension F₄((u))/F₂((t)), t=u³, has group C₃⋊C₂ with inversion, so arithmetic centrality cannot be assumed. A fixed finite H¹ class dies on its torsor, and a fixed class vanishing in a filtered colimit dies at some stage. Neither fact gives one stage for all coefficient levels or permits unrestricted interchange with profinite inverse-limit coefficients. [CL-SA12-081–089,204,210; SA12_SGA7I; Milne2008.]

The finite Čech comparison between an inertia extension class and a Kummer Chern class is independently checked, with signs and action fixed. The whole formal realization and the pro-limit identification remain separate. The inserted sum of omitted divisor classes on scan 94 is necessary for Picard localization. The finite-Ab prorepresentability input is also precise: vanishing H¹ makes H² left exact; SGA 4 I 8.3.3 is the relevant small-category result, and Bourbaki Exposé 195 A §3 supplies strictness under the stated Artinian conditions. SGA 4 I 8.13.3 is a different accessibility theorem and cannot be applied to FinAb by name alone. [CL-SA12-086,090,094,210,265; MP-SA12-26–29; SA12_Bourbaki195; SA12_SGA4I.]

Two stronger assertions fail in the actual formal setting. First, the later curve leaf calls the inertia extension trivial after π₂ vanishes. For an elliptic curve E/C, L=O_E(0), and n>1, multiplication by n and M=L^n give a finite map of line-bundle total spaces, branched along the zero sections. Complete those total spaces along the zero sections and then delete those sections. The resulting connected tame cover has degree n³ and a noncommutative theta deck group. Mumford's nondegenerate theta pairing is the exact published input. A split extension with this abelian geometric base and trivial cyclotomic action could not have that nonabelian finite quotient. [CL-SA12-203; MP-SA12-51; `reviews/29a/formal_elliptic_nonsplitting.md`; Mumford1966; MoonenTheta.]

Second, unique n-divisibility of the Picard kernel is false without controlling global units. Let X₀=E×G_m/C, choose nonzero a∈H¹(E,O), and glue a first-order thickening by z_j=z_i(1+εa_ij). Its units sequence identifies the Picard kernel with H¹(X₀,O)/Za; the class a/n modulo Za is nonzero n-torsion. The formal transition exp(ta_ij) gives the corresponding regular formal example. The opened unrestricted assertion in Stacks 0C6S has the same omitted global-unit quotient and is flagged as unreliable for this use. Both researchers checked the example; no external source was edited and no priority claim is made. [CL-SA12-091; `reviews/29a/independent_checks.md` §8.]

A correct finite-level refinement keeps the power isomorphism: objects are pairs (M, M^n≅L), with fixed L and invertible n. Nil-invariance and unique roots of principal units then give the relevant root-pair groupoid comparison. In the counterexample, the special-fibre power isomorphism is the nontrivial unit z, so its underlying trivial line bundle does not make the root pair trivial. This explains why the example does not contradict étale nil-invariance. Infinite formal effectiveness and algebraization remain additional hypotheses. [CL-SA12-092–093; MP-SA12-30; Stacks04DY/03PK; Lipman1974§2.4.]

### 2.6 Finite and infinite fundamental objects, and reused material

The finite-group-scheme pages separate a geometric fundamental object from arithmetic descent, discuss minimal pointed torsors, anticipate homotopy and product statements, and propose the abelian-variety system lim A[n]. Over a perfect field, the finite connected–étale semidirect splitting is exact; it is not the same decomposition as the later commutative multiplicative–unipotent splitting in cote 31. Modern Nori-type results give meaningful descendants, but their base field, reducedness, properness and separability assumptions remain attached to each exact claim. The strong family-variation hope and variable-base minimality statements are not certified by the existence of a fundamental group scheme in another category. [CL-SA12-213–224,248; the cited Nori and later references in those records.]

The equalizer issue is concrete: finite-flat group schemes are not closed under every equalizer over an arbitrary base. The cusp example checks failure of the unrestricted variable-base minimality-to-injectivity implication. It does not refute a restricted category of constant finite groups in which the required closure hypotheses hold. The source’s later choice of an admissible category is therefore retained. [CL-SA12-223–224; MP-SA12-60,67; `reviews/29b/independent_checks.md`.]

The subsequent infinite-covering notes define pointed torsor functors on discrete groups, strict prorepresentability, topology classes, simplicial-component presentations and effectiveness subfunctors. Several constructions are established under specified descent and finiteness conditions; their unrestricted variants are not identified merely by citing a finite Galois category. The written Set-functor criterion has an explicit counterexample: continuous maps from an inverse limit of infinite discrete spaces need not depend on a finite stage. Uniform continuity or compact finite systems supply different correct regimes. The accompanying categorical programme and its questions remain separate from that false criterion. [CL-SA12-249–273; MP-SA12-76–89.]

Reused sheets are evaluated on their own terms. The diagonalizable character exactness proof continues across the package boundary and is one canonical claim, CL-SA12-080. Quotient descent, n-torsion and graded affine actions remain distinct statements. The Raynaud construction has an exact SGA 7 IX counterpart; global cancellation of a working sheet does not withdraw the theorem. The EGA 17.4.10 draft number does not name the same printed assertion: final 17.4.1(d), 17.4.9 and 17.5.1 provide the correct comparison. The English Plücker/rational-structure proofs, Chinese-remainder and monic-factor arguments, Nullstellensatz and uniform-completion sheet have separate checks. The anonymous local abelian-variety pairing fragment remains an attribution problem; an inaccessible exact source is not replaced by a confident guessed theorem. [CL-SA12-063–080,225–235,239,250–251,274–275; MP-SA12-90; SA12_EGAIV4.]

## 3. Cote 31: cohomology, rigidity and the boundaries of comparison

### 3.1 Flat coefficients and multiplicative-type groups

The opening pages distinguish a dimension defined using all relevant sheaves from one using finite commutative group schemes on a finite-flat covering site. The inclusion gives an inequality; equality with a modern big-fppf invariant is not proved or silently assumed. Milne’s account of Shatz explains why the all-sheaf quantifier matters. The Shatz metadata was checked, while the original full text was unavailable; that access boundary stays explicit. [CL-SA12-401–407; MP-SA12-101–102; MilneADT; Shatz1966.]

The scans 47–51 programme uses finite-coefficient dévissage, filtered continuous cohomology, perfect-field group structure, Kummer and Artin–Schreier sequences, and Tsen. These are different ingredients with different hypotheses. The degree-one torsion comparison fails: a nonzero quadratic character over C(t) becomes a coboundary in the multiplicative group of a separable closure. The comparison becomes an isomorphism from degree 2 onward with a specific degree 1 kernel; the manuscript later narrows its range. For elementary abelian groups Γ=(F_ℓ)^r, the regular-representation determinant has the unique exception Γ=C₂, and the inverse-determinant repair changes the representation’s dimension. [CL-SA12-461–472,524; MP-SA12-119–126; saved calculations.]

The multiplicative-type rigidity, character-scheme, Hom/Isom and isotriviality sheets closely match SGA 3 IX and X. Finite presentation, flatness, connectedness, unibranchness, clopen pieces and the exact topology all matter. The cancelled subgroup formulation has a printed analogue, so its deletion alone does not prove it false. The countable finite-clopen converse has a qualification in the edited SGA 3 X discussion. A fibrewise schematic-density lemma and the density of a cofinal torsion family are distinct from the individual n-torsion integrality statement in cote 29. [CL-SA12-408–417,503,505; MP-SA12-103,146; SGA3 IX2–5, X5.1–5.16.]

### 3.2 Local cohomology and finite-group actions

The old cofinite-module convention is Hom-finiteness, not the later condition involving all Ext groups. The explicit shift example has finite annihilator and an infinitely generated quotient under that old convention. Calling it a counterexample to the modern statement would misidentify the definition. Formal full faithfulness, algebraization and algebraization by a locally free sheaf are likewise distinct. The exact SGA 2 XII boundary degrees, the EGA III 2 erratum and the proper hypothesis in Murre’s Picard application prevent overextending the nonproper programme. [CL-SA12-418–442; MP-SA12-104,108–111; SGA2; Murre1964; EGAIII2 erratum24.]

The finite-group pages contain valid trace and transfer arguments beside stronger false claims. For the stable-corestriction assertion, G=C₄ acts faithfully on B=Z⁶ by (12)(3456), H has order 2, and M=Z² uses the first factors. A relative trace-one element exists. The stable part of Tate H⁰(H,M) is the diagonal in F₂², but corestriction is zero there, while Tate H⁰(G,M)=F₂. Full corestriction is still onto. This checks the stated faithfulness and relative-trace hypotheses and separates relative projectivity from the extra bijection. [CL-SA12-448,452–453; MP-SA12-112; Broue2007§6.8; saved exact example.]

The residual H¹ claim fails for the faithful C₂ action ε↦ε+ε² on F₂[ε]/(ε³): the unit group is C₄ with inversion, so H¹ is C₂, whereas the residue unit group is trivial. There is one maximal ideal, so the semilocal transitivity conditions hold. The GL_n proposal already fails at n=1. A tame Artin refinement, proved by filtering principal units and averaging, is explicitly this review’s sufficient replacement, not the author’s missing statement. A separate norm assertion needs local-field scope: in C((u))/C((t)), u²=t, all units are norms although the extension is ramified. [CL-SA12-456–460,523; MP-SA12-114–118.]

### 3.3 Cohomological dimension, purity and base change

The local-cohomological-dimension sequence is not one theorem with optional adjectives. The strict inequality fails at a finite field; transcendence formulas need the coefficient prime separated from the characteristic; a spectral-sequence total degree is a sum, not a difference. The finite-transcendence-degree real-embedding assertion also fails for a non-Archimedean real closure of Q(t). [CL-SA12-423–426,483.]

SGA 4 gives many exact later statements. Gabber’s quasi-excellent affine/local results and non-quasi-excellent counterexamples show why excellence cannot simply be deleted. The rejected pointwise affine bound is tested with an example that actually satisfies coefficient invertibility: combine the opened existence theorem ILO XVIII-B 3.2.5 with XVIII-B 4.1.2 and SGA 4 X 2.4. This is a checked deduction from a published construction, not an independently produced explicit ring. In mixed characteristic, Gabber–Orgogozo 6.1 uses Kato’s p-dimension and affine opens in Spec(A[1/p]); it does not settle every affine-open assertion on the manuscript leaf. Undefined δ, N and φ notation remains an identification limit. [CL-SA12-479–502; MP-SA12-129–137; ILO2014; GabberOrgogozo2008.]

The closed-restriction counterexamples are marked reconstructions. Products of injective skyscraper sheaves give ambient all-functions sheaves; restriction to closed curves or surfaces can produce the stated failure of acyclicity. The separate compressed flasqueness assertion on an irreducible curve remains a distinct question rather than a consequence silently inserted into the proof. [CL-SA12-474–476,525–526; MP-SA12-127–128.]

The purity, tame-curve and smooth-base-change pages have close SGA 1/SGA 4 matches. There is also an exact controlled modern nonabelian development: Haine–Holzschuh–Wolf prove prosmooth base change for specified Σ-torsion étale sheaves of spaces on qcqs schemes. This gives a substantive fate for the H² programme while preserving the missing band/gerbe or homotopy-coefficient convention in the source. Their backward citation to Giraud was verified as a citation; the original book was not opened. [CL-SA12-509–515; MP-SA12-139–142; HaineHolzschuhWolf2024, Theorem0.1, Definition1.9, Corollary2.30.]

For wild ramification, Achinger’s constant-Swan curve-family theorem gives an exact partial continuation. Its example proves failure of base change without the condition; that is not automatically a proof that a chosen direct-image sheaf is non-locally-constant. The broader higher-dimensional normal-crossings programme remains separately scoped. [CL-SA12-516–518; MP-SA12-143–145; Achinger2017, Corollary2.3.]

## 4. Cote 33: the cohomology programme and the reused sheets

### 4.1 From sites to supports, trace and duality

The handwritten sequence uses L-functions as motivation for developing torsion duality, Künneth and Lefschetz, then ℓ-adic coefficients and applications. It does not state a specific L-function rationality theorem in its opening sentence. The progression is through sites and geometric points, ordinary images, proper and smooth base change, comparison, dimension, supports and purity, constructibility, compact supports, classes, traces, derived categories and duality. The title-only global-duality leaf is recorded as a title, not an unstated theorem. [CL-SA12-601 and the cote33 source-coverage map; MP-SA12-151.]

Several exact scope corrections matter. The nonproper algebraic–analytic comparison cannot range over every torsion sheaf without a constructibility condition. On A¹_C the sum of skyscrapers at the integer points has algebraic global sections ⊕Λ but analytic global sections ∏Λ, because the analytic support is locally finite while the algebraic base is quasi-compact. SGA 4 XVI 4.1 retains the disjunction of properness or constructibility. For a proper smooth morphism and finite locally constant coefficients of order invertible on the base, higher images are finite locally constant; they need not be free over Z/n. A rank-one Z/4 local system on a complex elliptic curve with sign monodromy has H⁰={0, 2}, which is not a free Z/4 module. [CL-SA12-607–613; SGA4 XVI4.1,2.1–2.2.]

The fundamental-class programme is coherent but not complete at every stage on the page. The divisor class comes from Kummer; products for regular sequences require independence from presentation. Base change needs the appropriate Tor-independent regime, and products without excess need transversal hypotheses. The support spectral-sequence edge calculation is checked exactly. Passing a supported class to compact supports requires the support to be proper over the base. Trace is fixed by base change, transitivity, the identity and the P¹ Kummer normalization. Its isomorphism condition uses **geometric** connectedness: Spec C → Spec R already separates ordinary connectedness from geometric connectedness in relative dimension 0. [CL-SA12-616–645; MP-SA12-156–165; SGA4 XVIII; Riou XVI2.3,2.5.13,3.1.1–3.1.4.]

The modern absolute-purity result is recorded in its regular, invertible-torsion setting; normal-crossing divisor formulas are not collapsed into one-stratum purity. Nonproper constructibility is matched with the quasi-excellent theorem in ILO XIII 1.1.1. The sources themselves explain the historical dependence on resolution-of-singularities methods for these purity/finiteness developments. Other omissions receive no invented psychological or editorial explanation. [CL-SA12-619–625; MP-SA12-158–161; ILO2014; Riou; SGA4 XVI3.10 and XIX introduction.]

### 4.2 All-degree duality and a false partial-range extension

For Λ=Z/n, the duality discussion is not restricted to free cohomology stalks: Λ is injective over itself. The short Baer-criterion calculation is independently checked, and SGA 4 XVIII 3.2.6 uses exactly this fact. If all cohomology sheaves of Rf!F are finite locally constant, internal duality therefore yields the asserted all-degree local constancy in the proper dual range. [CL-SA12-650–651; Stacks05NU; SGA4 XVIII3.2.6.]

The partial-range sentence at 48 is false. Over C, let f:G_m×A¹→A¹ be (u,v)↦u and write f=jp, with j:G_m→A¹ open. For Λ=F_ℓ, the map is smooth, separated, finite type, pure relative dimension 1 and compactifiable. One has Rf!Λ=j!Λ(−1)[−2], so R⁰f! and R¹f! vanish and are locally constant. But R¹f_*Λ(1) is the nonzero skyscraper at 0. Thus the proposed implication from compact-support degrees i≤1 to ordinary degrees j≥1 fails. The all-degree hypothesis is absent precisely because R²f! is not locally constant. A disjoint-union variant makes f surjective if desired. The saved geometric proof, not a numerical simulation of a topos, establishes the counterexample. [CL-SA12-678; `reviews/33/review.md` §2.4; Riou XVI3.1.3.]

### 4.3 Root systems, English sheaves and the resolved EGA question

The reused root-system pages have their own attribution problem. Their organization fits the Bourbaki Lie IV–VI family, whose publication metadata was opened, but the exact numbered draft is not identified. The exact program reconstructs the supplied coordinates and checks root counts 72, 126, 240, Cartan determinants 3, 2, 1, highest-root heights 11, 17, 29, weights, reflections and Weyl-order arithmetic. It does not claim to enumerate the entire E₈ Weyl group. [CL-SA12-652–665; exact calculation outputs; Coxeter1934; Bourbaki bibliography.]

Beyond the known E₆ factor 12+1 error, the proposed quotient generator μ=(ε₈−ε₇−ε₆)/3 is not a weight in the supplied convention: its simple-coroot pairing includes 1/2, and 3μ has nonintegral simple-root coordinates. The candidate 2(ε₈−ε₇−ε₆)/3 is consistent with the supplied first fundamental weight and order 3 quotient. This suggests an ink check, not an automatic replacement. Ordered Cartan integers require both orientations, and independent irreducible components can be rescaled; one ordered entry or one global minimum-length normalization cannot justify the stronger length claims. [CL-SA12-659–663; readings table.]

The English product-of-stalks construction is a sheaf, but its claimed Hom equality is too strong. On the Sierpinski space over F₂, the constructed rank-one example has 8 sheaf endomorphisms versus 4 diagonal stalkwise endomorphisms. An explicit off-diagonal map checks the failure. The genuine adjunction has the original sheaf as source. A Gray mimeograph is a bibliographic lead; missing Chapter I assumptions are not invented to rescue the literal assertion. [CL-SA12-670–674; Kleisli–Wu1964; Gray1965 access note.]

The cancelled EGA leaf at 47 is now identified exactly. Final EGA IV 4 Theorem 19.5.5 proves the missing implication b⇒c **without separatedness**, and a footnote explicitly credits P. Deligne. Here b is bijectivity of the polynomial map to the associated graded for the enlarged filtration; c is quasi-regularity for the original associated graded. The additional separatedness hypothesis on the relevant graded subquotients gives equivalence with regularity; it is not required for the displayed implication. Remark 19.5.6(iii) matches the stated failure of the converse even for one element. The following 19.6 matches the filtered exact-sequence fragment. The primary text and proof structure were read and the printed pages visually checked; this is not labelled an independent re-proof of the full induction. Publication was 1967, and no earlier circulation date is inferred. [CL-SA12-675–677; MP-SA12-172; SA12_EGAIV4, printed206–210.]

## 5. What changed relative to the earlier notes

The earlier notes were often strongest where they retained a doubt: nonreduced Picard structure, local-versus-global realization, finite-versus-profinite coefficients, support properness, the ordered-Cartan issue and the English Hom failure. Their context-driven project comparisons were useful as leads but did not supply proofs of the SGA objects. The consolidation preserves those leads separately.

The main changes are substantive rather than cosmetic:

- Repeated source objects now have canonical records, with exact versions and aliases. Subject similarity alone did not merge finite connected–étale splitting with commutative multiplicative–unipotent splitting, schematic torsion density with n-torsion finiteness, or finite-coefficient prorepresentability with a homotopy identification.
- Later source wording resolves some earlier doubts: geometric irreducibility at 29/113, the actual splitting assertion at 29/96, and the refined category hypotheses in the finite-torsor construction.
- Exact later publications close questions that should not survive in a new-task queue: the characteristic 2 vanishing-cycle case and the cancelled EGA b⇒c implication.
- Independent checks strengthen several objections into counterexamples satisfying the relevant hypotheses: formal elliptic nonsplitting, the global-unit Picard obstruction, stable corestriction, residual H¹, partial-range duality, and the additional E₆ generator error.
- Some earlier corrections were too strong. Cancellation of reused paper is not withdrawal of every theorem on it; locally constant finite Λ-modules need not be free; self-injectivity of Z/n permits the full duality statement without that extra freeness assumption.
- Numbering, speaker and source category are now explicit. Draft EGA numbers can differ from print; Murre’s correspondence is attributed to Murre; title leaves and borrowed typescripts do not become unstated authorial theorems.

Each entry’s actual verdict and reason is in `SA12_entries.tsv`. Original package verdicts remain in the audit even when a cross-package merge changes the final target.

## 6. Present status, evidence levels and research priorities

Classes A–F describe the **identified literature fate**, not a truth-value scale. A records an exact descendant in the author’s published work, B an established development by others, C a precise partial match, D a documented negative search for the exact development, E an earlier standard result, and F an unidentifiable formulation. A false literal reading can have an established corrected descendant. A class F record can be mathematically refuted yet remain bibliographically unidentified. A class C residual can be a missing definition or exact-source match rather than an unresolved theorem of 2026.

Every claim has a saved mapping to executed literature searches. Searches used the requested source families, including zbMATH-facing searches, arXiv, MathOverflow, Numdam, EGA/SGA and author bibliographies; backwards references were followed where direct title searches were insufficient. A broad-topic hit is not evidence of settlement. Bibliography `note={verified}` means the listed URL or DOI was actually opened; `annote`, access registers and check events distinguish official metadata, a theorem statement, an inspected argument and an independent proof. Unverified references remain explicitly marked. [Search maps in each review; `outputs/claim_search_coverage.json`; `SA12_references.bib`.]

The problem index includes questions that were open **on the pages**, later solved problems, false hopes and editorial/source-identification tasks. Its `why_open` field gives an explanation only when a source supports it. The direction list is this review’s prospective task queue. It ranks mathematical/historical interest separately from the concrete progress feasible in a few hours. It does not develop new projects here. The strongest immediate opportunities are controlled formulations: relative finite-torsor representability, finite-flat minimality categories, the Picard root-pair correction, exact mixed-characteristic dimension hypotheses, local-constancy/ramification comparisons, and the remaining categorical effectiveness conditions. Historical and critical-edition tasks have their own achievable endpoints.

### Links and the earlier projects

Each internal or published link states its endpoints, the relationship, and the actual inspection level. Where an exact published text was inaccessible, its row is a metadata or source-location lead and does not certify that theorem or its proof. A correspondence between a draft and a published theorem is distinguished from a shared proof ingredient or a broader thematic resemblance. External projects named in the earlier context—La Longue Marche, Les Dérivateurs, S6 and named research runs—were not supplied as independently inspectable mathematical endpoints. Their exact source-note references are preserved in `SA12_project_leads.tsv` and the `our projects` partition of `SA12_links.tsv`, explicitly quarantined as leads. Their reported theorems or statuses are not imported into this dossier. This is an evidence boundary, not an assertion that an absent external proof was checked.

### Reading alarms and verification

`SA12_readings.tsv` lists mathematical reasons to revisit the ink: signs, exponents, target groups, coefficient ranges, quantifiers, cancellations and words that reverse a premise or conclusion. Confidence concerns the mathematical diagnosis and candidate alternative, not visual certainty. No reading is decided and no source file is changed. The root-lattice outputs, finite-group calculations and other computations are paired with general arguments; a finite check is not called a certificate for an entire geometric theorem. `CHECK_EVENTS.tsv` identifies what was actually done for each statement, including refined statements when a literal assertion was refuted.

## 7. Counts and completion audit

<!-- COUNTS_BEGIN -->
The final register contains **342 indexed entry verdicts, 421 items, 482 canonical claim records, 194 problems, 319 reading alarms and 22 ranked directions**. All 354 supplied scan labels are mapped. The 492 original review claim records all have executed-search mappings; 10 explicit claim aliases produce the canonical total. There are also 10 item aliases and 4 problem aliases. The surviving IDs are unchanged.

### Entry verdicts

| Verdict on the earlier note | Entries |
|---|---|
| kept | 240 |
| merged | 91 |
| corrected | 11 |
| withdrawn | 0 |
| rests on a misreading | 0 |
| Total | 342 |

These verdicts concern the earlier notes and their relation to the supplied text. They are not truth values for the manuscript mathematics. A kept note may accurately report an unproved or false assertion; cancellation and reading uncertainty are separately recorded in the item and claim fields.

### Item kinds

| Kind | Items |
|---|---|
| conjecture | 17 |
| unproved claim | 115 |
| unpursued implication | 16 |
| idea of the earlier run | 37 |
| reading question | 59 |
| self-flagged step | 62 |
| withdrawn in the same text | 32 |
| title, date or page count | 38 |
| other | 45 |
| Total | 421 |

The item total exceeds the indexed-entry total because the complete Codex witnesses add source objects, including documentary leaves and unindexed claims. Those additions have no invented NOTES_INDEX verdict rows.

### Claim classes

| Class | Meaning used in this dossier | Records |
|---|---|---|
| A | Exact own-work published lineage, with any source variants qualified | 197 |
| B | Developed by others into an established result | 51 |
| C | Partial or restricted development; precise residual or false broader version stated | 124 |
| D | No exact development identified in the recorded searches | 3 |
| E | Earlier standard result or definition | 74 |
| F | Exact assertion or fate not identifiable from the supplied material | 33 |
| Total |  | 482 |

Classes are literature-fate labels, not truth values, and C, D or F is not a claim of present mathematical openness or novelty. The records include explicitly attributed correspondence, definitions, diagnostic examples and modern refinements; the total is not a count of independent theorems written by Grothendieck.

### Status on the supplied pages

| Accounting category | Records | Scope |
|---|---|---|
| Proof supplied or marked proved on the pages | 24 | Reports the existing proof-status label, including explicitly limited components; it is not a fresh proof certification. |
| Proof or calculation sketched | 152 | An argument or calculation is sketched; omitted hypotheses, continuations and flagged steps remain visible in the exact label. |
| Stated or used without a supplied proof | 117 | An assertion, input, formula or conditional deduction is recorded without a complete supplied proof; no truth verdict follows. |
| Open or self-flagged on the pages | 97 | A historical question, verification request or explicitly unfinished task. This does not mean open in 2026; later fate is a separate field. |
| Authorially corrected or withdrawn wording | 25 | The manual label explicitly records authorial revision or withdrawal. This is not a count of false theorems; physical cancellation alone is not promoted to mathematical withdrawal. |
| False assertion, version, reading, or step recorded | 55 | At least the specified assertion, interpretation, formula or proof step is negatively qualified. The count does not label every component or historical version of a claim false. |
| Other documentary status or modern reconstruction | 12 | Definitions, documentary descriptions, ambiguous draft status and explicitly nonauthorial reconstructions are kept separate from source proof claims. |
| Total | 482 | Exclusive accounting categories; original status wording is preserved. |

This rollup summarizes 261 exact status labels. In particular, the negative category counts **records containing a false assertion, version, reading or step**; it does not count independent counterexamples or declare every component of a bundled record false. The proved category describes the recorded page status with its qualifications, not a new certification of complete proofs. `outputs/status_rollup_claims.tsv` gives every assignment, `outputs/status_rollup_exact.tsv` gives exact-label counts, and `outputs/status_rollup_methodology.md` explains the accounting rules.

### Remaining audit counts

| Register | Count |
|---|---|
| Problem and deferred-step records | 194 |
| Reading alarms awaiting original scans | 319 |
| Link records | 445 |
| Of which separately quarantined external-project leads | 220 |
| Ranked future directions | 22 |
| Bibliography records | 219 |
| Bibliography records marked verified (at their stated access level) | 204 |
| Bibliography records explicitly unverified | 15 |
| Check-event rows | 1506 |
| Additional explicit REF correction records | 21 |

A bibliography record is a key with a stated access scope; multiple keys may address different inspected passages of the same work. A check-event count is a count of recorded actions and scopes, not independent mathematical results. Both rankings in the direction list are complete permutations of 1–22. Every direction names its source items, claims and problems.

All counts are derived from the consolidated tables after manual semantic decisions. `outputs/global_counts.json`, the status-rollup files and the final validation report preserve the exact accounting.
<!-- COUNTS_END -->

The 342-entry bijection, identifier resolution, bibliography keys, search-map coverage and supplied-locus coverage are checked by the assembly/validation programs. Detailed status strings are retained in `outputs/global_counts.json`; any compact status table above is an accounting summary, not an erasure of qualifications. The archive contains the manually authored reviews, proof notes, search/access registers, programs and saved outputs. External full books, retrieved source-page images, the supplied attachments and earlier checkpoint ZIPs are excluded. Raw web-return files are distributed as exact request/URL/retrieval metadata with hashes rather than copies of external source prose. This preserves the audit without redistributing the reference works.

## 8. File guide

| File | Use |
|---|---|
|`SA12_entries.tsv`|One verdict for each of the 342 supplied index rows.|
|`SA12_items.json`|Canonical note/source objects, quotations, locators and reconstruction boundaries.|
|`SA12_claims.json`|Every recorded claim family, computations, dated fate and reference keys.|
|`SA12_problems.json`|Authorial questions and open steps, with later status and exact hypotheses.|
|`SA12_readings.tsv`|Mathematical alarms to check against the original scans.|
|`SA12_links.tsv` and `SA12_project_leads.tsv`|Checked local/published relationships and separately marked contextual leads.|
|`SA12_directions.md`|Ranked future tasks, each tied to item, claim and problem identifiers.|
|`SA12_references.bib`|Opened links/DOIs and precise verification/access annotations.|
|`SA12_id_map.tsv` and `outputs/semantic_merge_audit.json`|Canonical aliases, partial moves and explicit nonmerges.|
|`SA12_source_coverage.tsv`|All 354 distinct supplied transcription loci and their records.|
|`CHECK_EVENTS.tsv`, `progress.log`, `reviews/`, `programs/`, `outputs/`|Evidence of reading, searching, proof checking, calculation, consolidation and validation.|

Bracketed work names and reference keys in this overview are expanded in the bibliography and the cited claim records; claim and problem identifiers provide the exact source-line and hypothesis detail. Some works retain more than one package-specific key for distinct inspected sections. The bibliography-key collision for EGA IV 4 is consolidated into one record with both verified comparisons.
