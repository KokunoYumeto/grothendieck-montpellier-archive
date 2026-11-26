# SA03, part 3 — Géométrie et topologie combinatoire

## Consolidated dossier of cotes 91 and 93

**Evidence cutoff: 19 November 2026.** This dossier covers the 321 entries in the attached `NOTES_INDEX.tsv`, every supplied Pro and Codex transcription of cotes 91 and 93, and the additional questions and computations found in those transcriptions. It does not import claims from the other three parts of SA03. Bibliographical keys refer to `SA03_references.bib`; statement identifiers refer to the accompanying machine-readable tables. Exact source-file line ranges accompany each item and claim.

The two folders contain several distinct lines of work. Cote 91 moves from representability and flattening, through restriction of scalars and local Greenberg-type functors, to constructible applications, schematic sets, inverse systems and Greenberg–Néron questions. Cote 93 interleaves a Tate–Deligne elliptic formulary, orientation theory, an unidentified analysis fragment, projective differential geometry, crystalline Dieudonné theory, stratifications, Cartier operations and arithmetic differential equations. Their physical proximity is evidence of an archive arrangement, not evidence that every sheet belongs to one theorem or one research programme.

The strongest conclusions are correspondingly specific. Several representability and classification questions have precise published counterparts. Some displayed formulas fail elementary tests and receive explicit repairs as modern reconstructions. Some earlier notes ascribe more to a page than it says, especially when a question becomes a theorem, a conditional construction becomes an equivalence, or a link to another project becomes an asserted result. Other uncertainties are irreducibly textual: the Pro and Codex witnesses disagree about a deletion or a decisive word, and no scan image is supplied. The dossier resolves the mathematical implications of those alternatives without deciding the ink.

## 1. Corpus, witnesses and conventions

The archive supplied here has 59 files, including 26 transcriptions: four Pro files and 22 Codex files. They contain 454 scan markers representing 298 distinct cote/scan pairs. All supplied files remain byte-identical to the ZIP. The inventory and hashes are in `SOURCE_MANIFEST.tsv`; `TRANSCRIPTION_COVERAGE.tsv` and `SCAN_LOCATORS.tsv` give the actual coverage.

| Cote | Catalogue pages | Pro scan numbers supplied | Codex scan numbers supplied | Distinct scan numbers supplied |
|---|---:|---:|---:|---:|
| 91 | 142 | 114 | 129 | 129 |
| 93 | 235 | 42 | 169 | 169 |

The catalogue counts are not transcription counts. In particular, cote 91 includes a marker numbered 143. The old Pro/Codex columns of `TOPIC.md` do not enumerate the Codex files actually attached. `TOPIC_COVERAGE.tsv` audits all 30 cotes named there, distinguishes the two present cotes from the 28 assigned to other parts, and lists catalogue scan numbers without a supplied transcription. No absent page is reconstructed. There are no scan images and no second-pass files in this attachment; absence of a second pass is not a missing required input.

The 321 indexed notes belong to four packages: 108 entries in `MPL_91_019-058`, 70 in `MPL_91_059-098`, 60 in `MPL_91_099-143`, and 83 in `MPL_93_002-046`. Each has one verdict row based on reading its entry and its passage. Codex-only material creates additional items, claims and problems, but no fictitious verdict rows. Separate part tables and reading logs preserve the audit trail; the top-level files apply the reviewed cross-package merges. `ID_ALIASES.tsv` records every retired identifier and its canonical replacement.

“Line” means an actual line of an attached transcription file, not a manuscript line or an approximate locator inherited from an earlier doubts table. Short quotations preserve the witness. The modern statement records any added hypotheses, and the reconstruction field identifies the addition. A source correction, an alternative transcription and a modern mathematical correction are three different things. None changes the supplied text.

The six fate classes are used conservatively. A requires evidence of Grothendieck's own **later** publication, not merely an undated leaf resembling a published text. B requires an exact established development by others, with its scope stated. C records a precise remaining scope, identification or proof-comparison gap; it does not automatically mean an open problem in mathematics. D would require a documented unsuccessful search for development. E covers standard or reused published material without claiming personal priority from undated sheets. F means that the supplied fragment does not identify a sufficiently precise assertion. A theorem statement read in a paper is not recorded as a proof checked.

## 2. Cote 91 in its own order

### 2.1 Closed sections, flattening and the unramified part of Hom

The initial title sheets announce representability, relative products, Greenberg functors, flattening, quotients, Hom and Aut. Scans 5–18 develop closed-section and flattening criteria, a condition R on groups, image factorization through a monomorphism, formal principal homogeneous spaces, quotient kernels and coherent tangent modules. These are not merely introductory slogans: the Codex-only beginning supplies hypotheses needed by the later indexed notes. [SA03-53–60; CL-SA03-048–056.]

Murre's Bourbaki exposé gives close, explicit counterparts for closed sections and flattening, reporting Grothendieck's results. SGA 3 supplies the essential-freeness and transporter framework, but equality of every handwritten R variant with that published condition was not established. The formal-principal-action assertion also needs flatness: the identity between the action relation and the fibre relation alone does not make an fppf torsor. The refined statement and a concrete failure without flatness are separated. [A_Murre1966, §3A–B; A_SGA3VIII, §6; MP-SA03-26–29.]

Scans 19–32 ask when the formally unramified part of a restriction map between Hom functors is represented by an unramified separated scheme. The coherent tangent-module argument precedes the square-zero lifting discussion; this corrects the impression that the latter begins without a framework. The main conclusion has a modern reconstruction from algebraic-space Hom representability and the fact that a separated locally quasi-finite morphism of algebraic spaces is representable by schemes. Separatedness follows here from the separated target and the closed-section argument for the Hom diagonal. This uses proper, flat, finitely presented sources and a separated, locally finitely presented target. It does not certify every handwritten obstruction comparison. [CL-SA03-001–002; A_Olsson2006, Theorems 1.1 and 1.5; A_Stacks0418.]

Two errors in the module calculation are mathematically decisive. Compatible pairs satisfying a simultaneous relation are represented by the cokernel of the combined map, equivalently by the quotient by the image of its full kernel. Imposing only the two separate kernel relations misses mixed compatibility. Replacing the answer by a second, unrelated cokernel also fails even in a one-dimensional example. The dossier supplies the corrected universal presentation and counterexamples to the two displayed substitutes. These are repairs of the algebraic route, not refutations of the representability theorem. [SA03-8; CL-SA03-003–005; MP-SA03-03; `parts/a/proof_notes.md`.]

The stronger normally-flat finite-probe theorem and its quasi-affine and essential-ampleness conclusions need their own hypotheses. An unqualified separation conclusion is false without a separated target. Conversely, examples showing that one fixed jet order cannot detect all maps do not refute a theorem allowing the order to depend on a quasi-compact part of Hom. The dossier keeps these quantifiers apart. The proposed weakening of properness, connected-component finiteness, essential positivity and some spreading-out statements remain exact comparison tasks in the opened literature, rather than generic claims that Hom representability is unknown. [SA03-6, 10–17; MP-SA03-02, 04–09.]

The 11 September 1967 letter is read against its public correspondence transcription. A letter of 11 June 1963 already contains several of the same Hom corollaries; that establishes circulation by that date, not the date of every loose sheet. The non-schematic quadratic Hom example is tied to semilinear descent and an orbit admitting no affine neighbourhood. The general obstruction is identifiable; the particular proposed Nagata example is not fully recovered. [A_Letter1963; A_Letter1967; A_Raynaud1968; SA03-18; MP-SA03-10.]

### 2.2 Restriction of scalars, finite support and relative components

Scans 34–59 turn to the restriction functor itself. They examine descent formulas, affine representability, gluing, preserved properties, determinant line bundles, Grassmannian equations, dimension and finite étale objects. The construction of the open locus where an entire finite fibre lands in a target open is valid: it is the complement of the image of the closed complement under a finite projection. The relevant affine-neighbourhood condition concerns all points in the image of a finite fibre. It is not supplied merely by an arbitrary open cover. [SA03-23–36; A_BLR1990, §7.6; A_Stacks0BL0.]

Several property claims need restrictions that the earlier notes sometimes suppressed. Bare surjectivity is not preserved by restriction along an arbitrary finite locally free map: the surjective closed point of the dual numbers has no section after a nonempty base change from the residue field. Properness and projectivity behave differently in the finite étale and ramified finite-flat cases. The Grassmannian construction gives a closed module-stability condition followed by an open freeness condition; it does not prove that the final embedding is closed and projective. The determinant criterion is invertibility, not merely being nonzero in a general ring. [CL-SA03-028–032; SA03-31, 34–35, 38.]

The smooth-dimension formula is wrong as transcribed, and reversing its two sides does not repair the mixed-dimensional case. A correct pure relative-dimension statement multiplies dimension by the rank of the finite locally free source. For finite étale objects, the cardinality formula instead uses the number of geometric connected components of the source fibre. Dual numbers and the degeneration of μ₂ over the 2-adic integers distinguish length from component count explicitly. The bound obtained by determining an étale section from one point also requires separatedness. [SA03-41–46; CL-SA03-038–045; MP-SA03-20–23.]

The finite étale envelope at the end of the sequence is an internal-Hom and relative-component construction. It must commute with étale localization; an ordinary universal property on global morphisms is weaker. A general left-exact endofunctor of finite group-sets need not be internal Hom from a fixed group-set, and the dossier gives a finite categorical counterexample. Scan 59 continues this discussion, with finite and flat assumptions written into the converse. Its adjunction has left-adjoint variance; it must not be confused with the right adjoint studied next. [SA03-45, SA03-49–50; MP-SA03-25.]

### 2.3 Local functors and a partial right adjoint

Scans 61–80 develop a local covariant functor W and a representative of the functor T ↦ Hom(W(T), X). Locality means preservation of open immersions, unions and intersections. The affine ring-scheme construction, its augmentation and the same-underlying-space condition are separate assumptions. The adjective “special” has a marginal explanation; saying that it is wholly undefined would overstate the textual gap. [SA03-205–212.]

For affine targets, relations on powers of an affine ring-scheme generator give the representing algebra. Finitely many generators do not require finitely many relations: an arbitrary ideal can impose all relations. Global representability then requires open factorization, overlap compatibility and a covering condition. The triple-overlap step marked “Il faut vérifier” is followed immediately by its identity argument and is not left open indefinitely. The broad affine corollary is cancelled on scan 69 and returns in a qualified form after gluing. [CL-SA03-206–214; MP-SA03-31–35.]

Bertapelle–González-Avilés gives exact modern theorems for specified Artinian/Witt Greenberg constructions and for admissible finite locally free restriction. Those results do not establish every possible meaning of the manuscript's general “special” functor. The dossier distinguishes the 2013 first preprint, 2018 journal publication and checked 2022 revision. A later paper's broad title is not used to fill an omitted hypothesis. [B_BG, Definition 2.45, Theorem 2.47, Corollary 2.48, Proposition–Definition 7.10 and Proposition 11.3; B_Kan, §§3–4 and 8.]

### 2.4 Constructible applications, schematic sets and the infinite-partition obstruction

Scans 81–116 introduce atomic schemes, residue-field-compatible applications, constructible pieces, piecewise isomorphisms, affine models and the constructible topology. The reduced structure matters: field-valued points forget nilpotents. The local finite-piece category must also be distinguished from the category of ordinary scheme morphisms and from an absolutely flat realization. [SA03-233–253, 406–416.]

A genuine partition of a quasi-compact quasi-separated scheme into nonempty constructible subsets is finite: the pieces are open in its compact constructible topology and a finite subcover exhausts a disjoint partition. Thus a missing written word “finite” does not alone invalidate that definition. It does **not** yield one common finite partition for infinitely many maps. [CL-SA03-226; B_EGAIV1, §§1.8–1.9; B_StacksPatch; B_StacksRefine.]

Two ordinary scheme-theoretic consequences fail. The reduced ring B = k + xk[x,y] has a two-piece constructible model consisting of Spec k[x,x⁻¹,y] and a point, yet B is not noetherian. The inclusion A = k + x²k[x,y] ⊂ B gives a reduced affine piecewise isomorphism Spec B → Spec A that is not of finite type. The dossier checks reducedness, the two strata, quasi-compactness and the failure of finite generation. The first example separates noetherian topology from noetherian local algebra. [SA03-241–242; CL-SA03-230, 233; `parts/b/proof_checks.md`, P08.]

The second claim has a crucial witness conflict: Pro leaves it live, whereas Codex marks it deleted. It cannot be presented as an uncorrected error by Grothendieck. A similar conflict on scan 110 changes a positive constructible-image claim into an explicit warning that it is false. On scan 95, asking whether finite presentation follows and asking whether to define finite presentation are different questions. All alternatives remain in the reading register. [MP-SA03-36; SA03-411; SA03_readings.tsv.]

The inverse-limit question on scan 97 has a complete obstruction. Take T = A¹ over Q and Xₙ = Aⁿ with coordinate projections. For distinct rational points aₘ, let coordinate m be 1 at aₘ and 0 elsewhere. Every finite tuple is regular on a finite constructible partition, and the tuples are compatible. No one finite partition supports the whole tuple: the part containing the generic point contains an open subset, on which each coordinate, generically zero, would vanish identically; that open contains all but finitely many aₘ. The comparison's exact image consists of the families admitting a common finite partition. The finite computation is an illustration; this argument proves the infinite obstruction. [CL-SA03-237–238; MP-SA03-38.]

Olivier's absolutely flat envelope is a different, precisely identified construction: the universal absolutely flat ring has patch spectrum and the same residue fields, and the scheme construction has its own adjunction. EGA's announcement, Olivier's 1967–1968 talks and Liu–Sebag's later variety formulation are distinguished. Liu–Sebag assumes reduced separated finite-type varieties and does not prove the false arbitrary-scheme consequences. [B_EGAIV1, §1.9.16; B_Olivier6, Proposition 5; B_Olivier9, §II Proposition 2; B_LiuSebag, §2.2.2.]

### 2.5 Thick points, Laurent units, jets and reused printed leaves

The later programme compares “thickness” conditions in inverse systems and proposes Greenberg–Néron statements for rational maps. Properness and generic separability are genuine written hypotheses. A valuative extension of a point is not automatically a finite-level morphism of Greenberg schemes. Several terms—“simple” pieces, “finite index” and the bounded invariant—cannot be securely identified from these leaves. Greenberg, Sebag and the corrected modern Greenberg paper provide close theorems, but the dossiers record the quantifier differences instead of declaring the whole programme solved. [SA03-421–424; MP-SA03-67–71; C_Greenberg1966; C_Sebag; C_BG.]

The Laurent-unit functor is represented by a union of affine stages recording a series and its inverse. Its reduced valuation strata can be surjective on topological spaces without being surjective on points over nonreduced rings: 1 + εt⁻¹ over the dual numbers is the elementary test. A claimed strict stage difference cannot include equality of indices. The pro-Hom formula later in the folder has a precise quasi-compact **and quasi-separated** finite-presentation version; the broader quasi-compact-only wording is not silently certified. [SA03-425–428; CL-SA03-453; C_Stacks01ZC.]

Nilpotent coordinate evaluation, augmented jet algebras and truncated polynomial substitution are also different objects. Translation by ε need not preserve the ideal (t³) even when ε³ = 0. The exact expansions and invertibility tests are supplied. They prevent a coordinate formula valid on a nilpotent ideal from being promoted to an automorphism of every truncated algebra. [SA03-429–433; MP-SA03-74.]

The interleaved printed leaves carry Bourbaki material: Laurent-series linear algebra, characteristic-p associative identities, PBW and invariant tensors, exterior algebra, restricted enveloping algebras, formal groups and topological groups. These are not automatically personal unpublished theorems of the manuscript author. The exact published exercises expose a missing nonzero condition and a dual-basis prime; a two-dimensional solvable Lie-algebra representation refutes the printed tensor-submodule reciprocity without a splitting hypothesis. A noncommutative formal group with abelian Lie algebra and the symplectic and orthogonal coordinate calculations are checked in their stated characteristics. [B_BourbakiLie; B_BourbakiTopo; SA03-254–262, 434–441; part proof and computation files.]

## 3. Cote 93: the elliptic, orientation and crystalline sequences

### 3.1 The Tate–Deligne formulary and small characteristics

Scans 3–25 reuse a Tate–Deligne formulary with annotations. Its generalized genus-one families allow smooth, nodal and cuspidal fibres with a marked smooth section; the discriminant has not been inverted everywhere. The 1968 IHES version is an exact textual comparator and the 1975 publisher record verifies the later edition. Neither dates every annotation or authenticates a hand. Relative Riemann–Roch, duality and base change explain the initial ranks, with the cohomological convention for p! recorded explicitly. [SA03-602–605; D_Deligne1968; D_Deligne1975; D_StacksCoh; D_StacksDual.]

The integral invariant identity c₄³ − c₆² = 1728Δ, all coordinate transformations and the characteristic-2 and characteristic-3 normal forms are recomputed. One coefficient needs a derivative of F, not F itself; a characteristic-2 model needs its x² term; the shear composition depends on the shear parameter, not the translation parameter. In characteristics 2 and 3 the integral formula for Δ must be used before reduction. Stronger normal-form hypotheses do not follow from vanishing of an invariant on a nonreduced base. [SA03-610–613, 623–624.]

The Hasse-at-the-cusp question has the precise answer 1 in the canonical Tate differential trivialization. The Legendre polynomial identity is verified with its sign and coordinate convention. The weighted supersingular mass is an earlier-run deduction from the degree of the Hodge line and simple Hasse zeros, not a sentence written on the leaf. The uncertain small table still requires an ink decision. [SA03-606–609; D_Katz1973, §2.0; D_DR1973, VI §4.3–4.9.]

At j = 1728 the local vanishing coordinate is j − 1728. The small-prime formal-moduli question requires a strict-local coarse-quotient statement and a distinction between the whole automorphism group and effective inertia. The geometric group orders 12 and 24 differ from the suggested effective orders 6 and 12; the characteristic-2 group is checked explicitly as Q₈ ⋊ C₃. This is not a computation of the entire wild deformation action. The equal-characteristic divisibilities of v(j) by 6 or 12 are proved from the integral invariants, while mixed-characteristic good-reduction examples refute an unrestricted extension of them. [SA03-614–619; MP-SA03-93; D_DR1973, I §8.2 and III §1.2–1.3.]

Automorphisms must be treated as a sheaf: signs can be chosen independently on connected components. Equal j does not ensure that the relative Isom scheme has a section over the original base. The finite étale degree-two conclusion holds when the common P¹-valued j avoids 0 and 1728, including the multiplicative boundary at infinity. In characteristic 2 the ordinary isomorphism equation is Artin–Schreier. The characteristic-2 weight-one and characteristic-3 weight-two generators also obstruct a naive surjective reduction of the integral modular-form ring. [SA03-621–627.]

### 3.2 Orientation, the English fragment and the Schwarzian leaf

The orientation cluster consists of Marcus Wanderley's 1981 offprint and handwritten axioms. The offprint refers to a 1980 thesis whose body was not retrieved. Its cutoff N ≠ 4 must not be misread as excluding all higher-dimensional categories that include four-manifolds. Kirby's and Quinn's primary results supply relevant stability and annulus inputs; they do not, without an additional comparison, prove equivalence of the printed and handwritten axiom systems. The boundary sign and the identity principle for sections of a separated local system are independently checked. The latter gives uniqueness, not a global orientation. [SA03-629–635; MP-SA03-95; D_Kirby1969; D_Quinn1982.]

The English fragment runs in printed order scan 34 → scan 32. Its strong-convergence estimate is valid under the explicit uniform-boundedness, absorption and convex-hull hypotheses. The missing semigroup lemma and vector-measure compactness proposition remain missing. Huff's 1973 title is a verified bibliographical candidate; its theorem was not retrieved and is not substituted for the absent pages. [SA03-636–639; MP-SA03-96; D_Huff1973.]

Scan 36 uses G = −2S(f), where S is the Schwarzian derivative. Exact differentiation confirms that the final exponential formula has coefficient 1, superseding the intermediate coefficient 3. If f is the ratio of independent solutions of y″ + qy = 0, then S(f) = 2q and G = −4q(dz)². A Picard–Fuchs interpretation still needs a geometric family. The elementary exponential example has invertible, non-nilpotent p-curvature at every odd prime; it refutes an earlier-run shortcut, not a manuscript assertion. Katz's Gauss–Manin theorems retain their properness, base-change and Hodge-degeneration hypotheses. [SA03-640–647; D_Ovsienko2009; D_Dumas2009; D_Katz1970; D_Katz1972, Proposition 2.3.2 and Theorem 3.2.]

### 3.3 The Montréal programme: classification, deformation and comparison

Scans 37–48 closely match Chapter V of the Montréal Barsotti–Tate programme: a 1970 course published in 1974. The original French printed pages were inspected. Their agreement establishes a textual relationship, not the chronological priority of an undated copy; an announced theorem reprinted without a proof remains an announced theorem. The Pro ending is incomplete, but its continuation in Codex scan 47 is supplied and included. [SA03-649–682; D_GrothBT1974; D_BNF1974.]

Problem 1 separates full faithfulness from essential image. The unrestricted ordinary crystalline Dieudonné functor is not fully faithful over every base, as reported in opened primary literature through Berthelot–Messing counterexamples. Those counterexamples are not claimed to have been independently reconstructed here. Positive results for locally p-based or suitable complete-intersection bases must be distinguished from classifications using divided or prismatic crystals. Lau's preprint first circulated in 2018; its revised version and publication in 2026 explicitly compare the old problem and give exact hypotheses. [MP-SA03-98–99; D_deJong1995; D_deJongMessing1999; D_Lau2026, Theorem 1.9, Corollary 1.8 and Remark 1.12; D_Prismatic2023.]

The perfect-base finite-group question has a precise later classification in Lau's 2010 preprint, published in 2013, crediting Berthelot and Gabber. Finite Dieudonné modules, finite groups killed by p, and level-one truncated Barsotti–Tate groups must remain distinct. For BT₁, extra F/V-exactness conditions occur; αₚ is a finite group killed by p but is not BT₁. The manuscript's Λₙ-flat/free-Wₙ formulation is discussed in the finite category, without replacing it by a truncation slogan. [MP-SA03-101; D_Lau2013, Definition 6.1, Theorem 6.4 and Corollary 6.5.]

For finite-group deformation, following references backwards from the 2025 perfect-F-gauge classification reaches Faltings's 2002 Theorem 17. The public MPIM preprint gives a nilpotent-divided-power lifting theorem using filtered perfect complexes with strict O-action; the O = Zₚ comparison is stated separately. This substantially answers the historical deformation question, although the author's unnamed candidate remains unidentified. Madapusi–Mondal's 2025 theorem is labelled as a preprint classification, with its perfect-complex amplitude and weight restrictions retained. [MP-SA03-100, 103; D_BM1979; D_Faltings2002, Theorem 17; D_MadapusiMondal2025, Theorem A and Remark 8.1.5.]

The ordinary algebra underlying F/V identities is not enough to settle every crystalline assertion. Cancellation over a p-torsion-free ring gives exactness modulo p but does not give locally free images: xy = p supplies an exact complex with a nonfree reduced image at the node. Ordinary Frobenius pullback identifies distinct subbundles over the dual numbers, but that is not a counterexample to an assertion about crystalline pullback. The dossier therefore asks for the exact site and admissibility comparison, not a false refutation by a different category. [SA03-665–669; MP-SA03-104–105; D_Lau2026, §3.]

The Hodge-filtration deformation theorem requires nilpotent divided powers in its corrected form. Messing's full 1972 book supplies a direct comparison: IV 2.2 and 2.4 construct canonical universal-extension maps and verify their cocycle and base-change compatibility; V 1.6 gives the Barsotti–Tate filtration equivalence and V 1.10 the abelian version, with the printed local-liftability condition recorded. The broader infinitesimal alternative remains a separate comparison. Illusie's appendix gives the precise affine abelian-lifting result, its attribution to Grothendieck in 1962 and its relation to Serre–Tate theory. The rank g² calculation for Hodge-subspace lifts is checked, but does not prove effectivity. The arbitrary-base absolute-site formulation, all-nil characteristic-zero rigidity and crystalline multiplicative-cohomology identification remain distinct obligations. [MP-SA03-102, 106–110; D_Messing1972; D_Zink2002, Theorem 92 and following remark; D_Illusie1985, Appendix 1; D_FonsecaMatthes2024, §3.]

### 3.4 Filtered isocrystals, the mysterious functor and Euler characteristics

The continuation on scans 49–54 moves from crystals to isogenies, filtrations and generic-fibre comparisons. Rationalizing Hom does not automatically produce a stack on a non-quasi-compact base: locally bounded denominators need not have one global bound. Recovering a Hodge filtration over a perfect base and describing admissible filtrations over a general p-complete base are different tasks. The hoped-for Zariski openness of the admissible locus is too strong; the checked example exhibits an affine line of filtrations with infinitely many excluded rational points and nonempty complement. This negative answer concerns the stated Zariski topology, not the existence of a useful analytic admissibility locus. [SA03-1203–1207; CL-SA03-1207–1219.]

The “foncteur mystérieux” has an exact later field-valued realization in the filtered-Frobenius/Galois comparison. Its field hypotheses and the two-step Barsotti–Tate specialization remain explicit. A relative classification over every p-complete base does not follow from that theorem. The equal-characteristic generic full-faithfulness question also has a close de Jong theorem, with nondegenerate F-crystals over the specified DVRs and a separate Barsotti–Tate corollary. Removing Frobenius from the question about crystals is a further change of category. [CL-SA03-1212–1219 and their exact primary references.]

Scans 55–68 contain a separate Euler-characteristic programme. It distinguishes ordinary χ from compactly supported χ, derives cell, product and fibration formulas, and introduces recursively locally conical classes. The calculations for Euclidean spaces, balls, spheres and finite cell filtrations are checked. A compact core with end link S explains χ(X) − χ_c(X) = χ(S), under the stated finiteness and pair-cohomology assumptions. The finite-cover spectral-sequence argument proves the local-system rank–Euler formula for a finite open or excisive cover trivializing the system and having finite cohomology on its intersections. Arbitrary closed covers need an additional excision hypothesis. Fibration multiplicativity needs an appropriate finite-type setting and support convention. The recursively named classes are not silently identified with all triangulable spaces. [SA03-1212–1218; CL-SA03-1240–1255, CL-SA03-1314.]

The reused Banach-algebra exercises on scans 50 and 52 form another strand, with exact later Bourbaki concordances. Pseudo-resolvent expansions, Cohen factorization and weighted Liouville arguments are checked with their convergence assumptions. Some errors persist in the published exercise, while other printed formulas differ from the archive transcription. These include the point at which a resolvent norm is evaluated, the quantity approximated in a factorization lemma, a missing Fourier factor, an exponent shift and an outer-half-plane sign. The distinction matters: a published parallel can diagnose a formula, but still cannot decide what the archive ink says. Administrative report leaves and budget arithmetic receive provenance records rather than invented mathematical conjectures. [SA03-1209–1211, 1219; CL-SA03-1220–1239, 1256.]

### 3.5 Projective connections, quotient torsors and pointed curves

Scans 72–91 develop projective differential invariants and compare translation, multiplicative, affine and projective quotient structures. Their normalization is G₀ = −S/6, so the earlier scan-36 quantity is G = 12G₀. The explicit formulas, power examples, logarithmic ratios and Riccati/Miura expressions must be compared after that conversion. In particular, the t² example evaluates to 1/(4t²), not the transcribed 1/(2t). The connection attached to a horizontal nth-root frame has the corresponding negative logarithmic derivative; the source’s competing sign is preserved as a reading question. [SA03-1221–1222, SA03-640, SA03-1224–1237; SA03-640–641.]

The final part of this block interprets a Brauer–Severi curve through an Azumaya algebra, a form of PGL₂, a pointed rank-two extension, its adjoint Lie algebra, filtered connections and principal parts. A global rank-two vector bundle cannot be assumed in the nonsplit case; it is a local realization. The first infinitesimal neighbourhood requires the square of the diagonal ideal. Taking only the diagonal loses the rank-two jet information. Bracket factors, trace-zero versus scalar-quotient conventions, and the assumption that 2 is invertible are retained in the calculations. The representation list on scan 87 has an unresolved adjective: an ordinary rank-two representation of PGL₂ cannot be obtained by descending the tautological SL₂ representation when 2 is invertible, because its central involution acts nontrivially. A projective or twisted interpretation remains possible and is not decided without the image. [SA03-1239–1249; CL-SA03-1315–1316; C2_Milne2022, Proposition 20.31.]

An isolated loop-space/Postnikov question belongs to this interval but not to the differential calculation. It is indexed as a question with its precise delooping level. Results for double loop spaces do not settle a statement about arbitrary single loop spaces. [SA03-1238.]

The next supplied block starts at scan 135 after a gap in the archival sequence. Its algebraic extension is identifiable: scan 91 has L⊗ω ≃ P¹(ω) and cΩ = d¹, while scan 135 repeats that first-jet extension and universal operator, with residual freedom ω². This resolves the algebraic identification in MP-SA03-208; the canonical item is SA03-1248. The separate “canonical transcendental” construction invoked next is still not identified from the supplied pages. The standard regular-singular condition permits a double Schwarzian pole, whereas fixing its double-pole principal part leaves simple-pole differences. Those two meanings of regularity cannot be interchanged to refute the page. For a stable pointed smooth curve the cotangent description uses H⁰(K²(D)); the low-genus dimensions and automorphism contributions are recorded separately. [SA03-1248, SA03-802–805; CL-SA03-801, CL-SA03-1312; MP-SA03-208, MP-SA03-122–126; A2_PrincipalParts; C2_EGA_IV4, §16.7 and Proposition 16.8.4.]

### 3.6 Connections, stratifications, Picard–Fuchs sections and Gauss–Manin

Scans 142–167 build the machinery in a deliberate order: principal parts and connections, the de Rham complex, hypercohomology torsors, stratifications, formalization, Picard–Fuchs operators and a filtered construction of Gauss–Manin. A splitting of first principal parts gives the connection with the displayed sign. Integrability is the vanishing of its degree-zero curvature, and the extended differential squares to zero exactly in that case. Hypercohomology in degree one classifies a torsor with a compatible trivialization of its next pushout; the morphisms and the next differential are part of the statement. [SA03-806–810; CL-SA03-810–817.]

Grothendieck's published formalization and stratifying-cohomology discussion is an exact comparator, but the undated sheets do not prove that their text preceded the 1968 publication. In characteristic zero, the standard connection/stratification equivalence uses smoothness; the weaker sole condition that Ω¹ is flat is not substituted without a theorem. Similarly, horizontal sections of a quotient need not equal a quotient of horizontal sections. These are precise boundaries in the Picard–Fuchs and differential-operator construction, not generic doubts about the theory of connections. [SA03-811–816; CL-SA03-818–826; MP-SA03-129–134.]

The Gauss–Manin section explicitly follows Katz–Oda. Its base-form filtration has a graded description using the relative de Rham complex, and the first spectral-sequence differential gives the connection. The differential is linear over the base inverse-image sheaf, not over O_X; this matters when applying a derived projection formula. The page's coefficient-flatness alternatives and the flatness of base differential forms are recorded. The secondary class arising from the Leray filtration is a torsor with connection; it is not an arbitrary lift of an E∞ class into an unrelated group. The proposed “derived connection” still needs the proper differential-operator or stratification category. [SA03-818–822; CL-SA03-827–835; MP-SA03-135–139.]

### 3.7 Cartier and the arithmetic differential questions

The Cartier calculation on scans 169–178 begins over an F_p-algebra with the image of relative Frobenius and a local p-basis. That setting permits a direct de Rham cohomology calculation. A central displayed assertion is false if its target is the algebra of closed forms: the assignment dx ↦ x^(p−1)dx fails the required additivity before quotienting by exact forms. Already over F₂[x], d(x+1) = dx, while the proposed images differ by dx. The canonical map lands in de Rham cohomology; a p-basis can choose representatives, but that splitting is not canonical. [SA03-823–827; CL-SA03-836–848; MP-SA03-140–141.]

The relative-Frobenius and p-curvature formulas are then stated in their proper categories. A reduced base and an open finitely presented morphism do not force the Frobenius twist to be reduced. Smoothness supplies the needed local p-bases and finite local freeness. Cartier descent requires both integrability and zero p-curvature. For a line connection, the translated coefficient satisfies the Jacobson formula and the logarithmic criterion with a fixed sign convention. In higher rank, a bracket convention must distinguish ω∧ω from one half of the graded commutator when 2 is invertible. The top-degree Cartier map is the duality trace, not the ordinary algebra trace. [SA03-828–833; CL-SA03-849–857; MP-SA03-142–146.]

The continuation on scans 179–186 matches Cartier with residues, duality and the Picard Frobenius/Verschiebung operators, then studies the curve bundle Q = F_*O/Λ. The pairing C(f dg), alternating when p is odd, is checked in a p-basis; in characteristic 2 it is symmetric and generally not alternating. Its nonzero antidiagonal uses i+j = p, not p−1; an odd-prime determinant simplification also fails with the displayed normalization. The characteristic-2 square root and the odd-prime determinant-line construction are compared with exact published results rather than inferred from the faulty scalar. A proposed assertion about every imperfect characteristic-2 field is tested with its universal field quantifier intact. [SA03-1001–1017; corresponding claim and reading records; B2_Raynaud §4.1 p118.]

Scans 189–193 distinguish connections, stratifications and étale-local triviality. Cartier descent does not make every quasi-coherent module locally free: the Frobenius pullback of a torsion module supplies a simple test. Rank-one Kummer constructions require the inherited smoothness, characteristic and finite-monodromy hypotheses. The page's enlarged and relative fundamental-group proposals are not replaced wholesale by an ordinary profinite representation category. [SA03-1019–1027; CL-SA03-1019–1027.]

On scans 194–198, “integrable” or “level zero” is used for algebraic trivialization after a finite étale cover. It is stronger than merely flat. Finite analytic monodromy implies the desired algebraic conclusion only with a regular-singular or properness condition: the exponential connection on A¹ has trivial analytic monodromy but no algebraic horizontal trivialization. Spreading a finite étale trivialization proves the easy implication toward zero p-curvature after shrinking an arithmetic model. The converse is the Grothendieck–Katz p-curvature conjecture. Its general form remains open at the evidence cutoff. Rank-one and appropriate solvable cases are established (B2_Andre, Corollaries 4.3.5–4.3.6); B2_PatelShankarWhang Theorem 1.1 covers rank 2 generic curves, not every curve. Whole Gauss–Manin systems satisfy Katz’s theorem as restated in B2_LamLitt Theorem 1.1.1. B2_EsnaultGroechenig Theorem 3.1 treats privileged systems and §8 proves special boundary-distinguished subquotient cases; its introduction explicitly leaves arbitrary Gauss–Manin subquotients open. The 2026 papers do not establish the general conjecture. [SA03-1028–1039; CL-SA03-1028–1039; MP-SA03-163–166.]

Two adjacent specialization questions therefore have different answers. The section of the universal vector extension encodes a line bundle **with its connection**, and the canonical zero-p-curvature subgroup keeps that compatibility; the rank-one theorem applies. Requiring only that a projected point of an abelian scheme lift under Verschiebung in every closed fibre loses that data. For the latter question, take E: y² = x³ − 2x over Spec Z[1/10] and P = (2,2). The discriminant is 512, so this is an abelian scheme on that base. Doubling gives x(2P) = 9/4, and the torsion-integrality theorem proves that P is not torsion. At p = 3 the group has order 4. For every p ≥ 7, the Hasse interval lies strictly between 0 and 2p, and rational 2-torsion makes the group order even; it therefore cannot be divisible by p. Multiplication by p, and consequently Verschiebung on the rational points over F_p, is bijective. This proves the required lift at every closed point. It refutes the weaker question, not the universal-extension assertion or the rank-one p-curvature theorem. [SA03-1035, SA03-1040; CL-SA03-1035, CL-SA03-1040; `parts/b2/proof_checks.md`, P2_15.]

The next finite-field calculation also needs a multiplicity distinction. Fixed Cartier forms are counted by the kernel of the appropriate iterated operator minus 1, not by the algebraic multiplicity of eigenvalue 1. The smooth genus-two curve y² = x⁵ + x⁴ + x² + 1 over F₃ gives a nontrivial unipotent Cartier matrix: the eigenvalue has algebraic multiplicity 2 but the fixed subspace has dimension 1. The point-count and matrix checks supplement the exact argument. The identification with rational p-torsion in the Picard variety uses the curve and finite-field hypotheses. [SA03-1041–1045; CL-SA03-1041–1045.]

Scans 206–217 organize Picard functors with connection, integrable connection, zero p-curvature and nilpotent reductions. Čech logarithmic transition cocycles, the curvature obstruction, the Frobenius-twisted p-curvature map and formal completion are distinct stages. The additive p-curvature map is not O-linear, so its quotient cannot be called a vector bundle merely by applying a linear cokernel slogan. A low-degree spectral-sequence expression also has to use the appropriate filtration piece, not all of H² without qualification. The cancelled site drafts on scans 216 and 218 are compared with the published stratifying-site construction, including the absence of a final object and ind-representability by diagonal neighbourhoods; the broader cancelled category is not restored by guesswork. The final Gauss–Manin headings are retained as an agenda, with no invented missing theorem. [SA03-1046–1051, SA03-829–830, SA03-1054–1062, SA03-1064–1072; CL-SA03-1046–1068.]



## 4. What the earlier notes got right and what changed

The earlier notes were useful locators of explicit questions, missing proof steps, cancelled assertions and possible connections. Many were appropriately cautious about an incomplete source. The consolidation preserves their valid concerns while eliminating repeated entries and testing their claims against the supplied witnesses, comparing Pro and Codex where both are available.

The most consequential changes are these:

- **A question stays a question.** The scan-97 inverse-limit formulas, the Montréal image problem, marginal full-faithfulness hopes and uncertain definition requests are not promoted to proved theorems.
- **A supplied continuation is used.** Cote 91's initial Codex leaves provide the tangent-module setup, and cote 93's scan 47 completes the interrupted universal-extension paragraph. Conversely, absent preceding definitions are not invented.
- **Witness disagreement limits attribution.** A mathematical counterexample can refute a literal formula while leaving unresolved whether the author's live text asserted it or deleted it.
- **A counterexample has a stated target.** Fixed jets do not refute a variable-order quasi-affine restriction theorem; nonfaithful ordinary Frobenius does not refute crystalline descent; a pointwise arithmetic section test does not settle a compatibility condition on a universal extension.
- **Different finiteness notions stay separate.** Length, geometric component count, finite presentation, finite partitions, bounded Laurent order, and one common partition in an infinite system are not interchangeable.
- **Reused mathematics keeps its provenance.** Deligne's formulary, Wanderley's offprint and Bourbaki exercises are not reassigned to Grothendieck merely because the sheets are in his folder.
- **Earlier-project conclusions are not inherited.** La Longue Marche, Les Dérivateurs, S6, Hua registers and the named research runs remain attributed leads when their destination texts are unavailable.

These corrections do not imply a blanket negative assessment of the pages. Much of the material has exact modern formulations, and some of its questions already circulated in the correspondence decades before the later treatments. The dossier's purpose is to make those formulations, dates and proof obligations recoverable without turning a loose archive association into a mathematical equivalence.

## 5. Literature, checks, links and usable next tasks

The part search logs record actual queries, targeted portals, backward references, opened sources and failures. The consolidated `CLAIM_SEARCH_COVERAGE.tsv` connects every claim to its search audit. Searches include the requested zbMATH-scoped, arXiv, MathOverflow and Numdam routes, EGA/SGA and primary bibliographies. A search result or abstract is a lead; exact mathematical assertions rely on opened primary text or an explicitly supplied independent argument. Failure to retrieve a theorem is a verification limit, not proof that nobody developed it.

`CHECK_EVENTS.tsv` distinguishes textual and hypothesis checks, targeted proof checks, independent re-proofs, computations, background use and refutations. The programs and outputs are included, with original proof notes beside them. A finite experiment does not prove an infinite claim; a polynomial identity does not prove a representability theorem; reading a statement does not certify its proof. Reference verification is described in `REFERENCE_POLICY.md`.

`SA03_links.tsv` contains only links whose stated endpoints were checked. Direct references to unavailable archive folders, inaccessible historical theorem text and the unidentified old letter to Tate are in `SA03_link_leads.tsv`. The separate `SA03_project_leads.tsv` preserves the earlier notes' exact project/run names and originating note IDs. Its entries are source-attribution leads, not two-endpoint verified research links. This is the evidential boundary imposed by the supplied corpus, not an invitation to fill an unseen project from context.

The ranked directions in `SA03_directions.md` identify concrete subsequent tasks, their known starting points, what a few hours could establish and their item/claim/problem anchors. None is developed as a new research project here. The immediate priorities are source-sensitive and bounded: resolve high-weight readings on images, isolate exact categorical hypotheses, reconstruct the few decisive proof gaps, and only then transport a result to another programme.

## 6. Final census

<!-- CENSUS_START -->
These are counts of the final canonical tables. Local part files preserve their
original audit identifiers and are not additional canonical records.

| Record | Count |
|---|---:|
| Indexed entries, each with exactly one verdict | 321 |
| Canonical items, including additional Codex-only material | 380 |
| Canonical claim and explicit refinement records | 487 |
| Problem records, including resolved historical questions | 165 |
| Reading flags to decide on the scans | 264 |
| Ranked research directions | 36 |
| Two-endpoint-checked links | 122 |
| Separate unverified archive/publication leads | 5 |
| Separate earlier-project leads | 38 |
| Bibliography records | 195 |
| Check events | 1231 |

### Entry verdicts

| Category | Count |
|---|---:|
| kept | 211 |
| merged | 94 |
| corrected | 14 |
| withdrawn | 2 |
| rests on a misreading | 0 |

The verdicts sum to 321. A corrected entry can also contain a reading alarm;
the absence of a separate “rests on a misreading” verdict does not mean that no
misreading was diagnosed. Corrections and source-check reasons state the exact
issue without deciding uncertain ink.

### Item kinds

| Category | Count |
|---|---:|
| conjecture | 27 |
| unproved claim | 117 |
| unpursued implication | 17 |
| idea of the earlier run | 45 |
| reading question | 56 |
| self-flagged step | 65 |
| withdrawn in the same text | 17 |
| title, date or page count | 10 |
| other | 26 |

### Claims by literature class

| Class | Count |
|---|---:|
| A | 0 |
| B | 190 |
| C | 110 |
| D | 0 |
| E | 161 |
| F | 26 |

A and D are zero under the conservative policy in §1. Zero A is not a finding
that Grothendieck never published these results: a matching publication does
not by itself date an undated sheet. Zero D is not a finding that every question
was solved: exact scope gaps are specified in C and unidentifiable fragments
in F. E includes transparently attributed standard and reused printed material.
The complete fate and dated present-status text, rather than the letter alone,
states whether a literal assertion is established, refuted, unresolved, or
still awaiting an exact historical comparison.

### Claims by source-status group

| Category | Count |
|---|---:|
| proved there | 51 |
| proof sketched | 128 |
| stated without proof | 180 |
| corrected by himself later | 9 |
| false as stated / as transcribed | 46 |
| open on the pages | 73 |

The status grouping preserves the full qualified `status_on_pages` field in
`STATUS_GROUPS.tsv`. “False as stated / as transcribed” distinguishes a
mathematical failure of a literal witness from an authenticated error in the
author's live text. The open/unfinished group includes three cancelled drafts,
CL-SA03-1016, CL-SA03-1018 and CL-SA03-1066; their records explicitly identify
the withdrawal, and they are not presented as live conjectures. A modern
refinement can have its own claim ID, explicitly labelled as editorial, so
the 487 records are not a count of 487 independent propositions authored by
Grothendieck.

### Coverage and audit totals

All 487 canonical claims have a documented search route and an
actual part search log. There are 403 search-log records; these
include grouped searches, individual operations and documented access failures,
so they are not asserted to be 403 distinct mathematical results.
The bibliography has 191 opened-link records marked verified and
4 records marked unverified. Repeated works can have separate
inspector keys; 195 is a count of bibliography records, not distinct works.

The 16 reviewed aliases comprise 12 item merges, one claim merge and three
problem merges. Before those aliases the seven audit parts contain 392 items,
488 claim records and 168 problems. All 321 indexed entries retain their
original stable source IDs. The final integrity report checks the exact-once
mapping, source ranges, referenced IDs, actual search-log coverage, reference
flags, check events and direction anchors. The source-byte audit confirms that
all 59 supplied files remain unchanged. These mechanical checks supplement
the recorded readings and mathematical checks; they do not replace them.
<!-- CENSUS_END -->

