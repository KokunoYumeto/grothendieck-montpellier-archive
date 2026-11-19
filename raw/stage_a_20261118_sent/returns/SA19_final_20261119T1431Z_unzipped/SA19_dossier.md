# SA19 — Jacobiennes

## Scope, evidence and principal findings

**Literature cut-off: 19 November 2026.** This dossier consolidates every one of the 174 indexed entries against its supplied transcription passage, and reads all the other supplied transcription faces. It follows the archival sequence of cote 43, then cote 44, and finally identifies the substantial contextual material in cotes 16, 47 and 54. The machine-readable registers carry the exact entry, item, claim and problem identifiers, source locators, qualifications, computations and literature decisions. They are the detailed companion to this overview.

The central mathematical lines are local and generalized Jacobians; cohomological realizations and dualities; the passage between algebraic, formal, proalgebraic and finite group schemes; and the construction of abelian varieties from algebraically trivial cycles. The files also contain significant Lefschetz, Fourier-transform, flatness and reused-typescript material. Reading all of these as one Jacobian theorem would conceal both the actual questions and the different categories in which later results hold.

Five conclusions organize the dossier. First, many of the elementary local-cohomology, support-Ext, height-one group-scheme and affine-approximation constructions have exact counterparts in SGA, with hypotheses that matter. Second, modern geometric local and global duality gives substantial realizations of the proposed programme, but it does not validate an undefined Weil site or an unrestricted all-sheaf comparison. Third, the incidence/Picard construction is the closest verified historical model for the 1964 intermediate-Jacobian programme; universal regular representatives and algebraic Abel–Jacobi images are different objects. Fourth, several manuscript formulas or plausible literal readings fail under explicit counterexamples, and the dossier records their repairs as reconstructions rather than changing the text. Finally, the earlier notes' links to other projects supply comparison leads, not evidence that those projects' theorems occur in these sheets.

These conclusions depend on exact theorem matching, not merely titles. For example, the support-Ext assertion matches SGA2, Exposé VI, Théorème 2.3; the affine-group approximation matches SGA3, Exposé VIB, Proposition 11.13; the reused flatness sequence matches EGA IV₃, §11.4; and the finite-group/de Rham comparison has a precise formulation in Oda's Corollary 5.11. The historical Picard-family connection is strengthened by Kleiman's explicit attribution to an unrecorded 1964 observation of Grothendieck (Grothendieck & Dieudonné, 1966, §11.4; Grothendieck, 1968a, VI.2.3; Demazure & Grothendieck, 1970, VIB.11.13; Oda, 1969, Corollary 5.11; Kleiman, 1971, pp. 446–447). Bibliographic keys and opened URLs are in `SA19_references.bib`; the depth of access is recorded in `SA19_bibliography_audit.tsv`.

### What is and is not supplied

The outer ZIP already contains unpacked folders. It was unpacked once. Its immutable file hashes and the complete scan/line index are in `source_audit/`. The supplied files, rather than hypothetical Space copies, determine the source text.

| Archival component | Coverage in this dossier | Material limitation or distinction |
|---|---|---|
| Cote 43, K43-01 and K43-03 through K43-10 | Every supplied transcription face read; the eight short Codex notes read as leads | K43-02 is listed in `TOPIC.md` but is absent. Its indicated scans 17–31 cannot be reconstructed. K43-07 has no short notes file, but its transcription was read. |
| Cote 43, Pro range 94–142 | All 46 supplied faces and all 89 indexed entries read | Interspersed absent scan labels are recorded, not filled in. |
| Cote 44 in the mixed package | Every supplied face and indexed entry read | The catalogue says eight pages; the supplied text has nine scan markers. |
| Cotes 16, 47 and 54 in the same package | Every supplied face read; all 85 mixed-package entries across cotes 16, 44, 47 and 54 audited | The index's package-wide cote-44 label is not the actual cote of every entry. |
| Cote-16 second pass | All applicable change and checked-notes files read | Applies to cote 16, scans 1–53; it is not a second pass of cotes 43, 44, 47 or 54. |
| Archival images | None supplied | Mathematical alarms remain unresolved readings. No diplomatic transcription has been edited. |

The cote-43 catalogue count is 207, while supplied archival labels reach 208. That mismatch does not establish an authorial page count. Cote 16 supplies 54 scan markers, namely 1, 3–23 and 25–56. A detailed folder-by-folder inventory is in `SA19_folder_coverage.tsv`; it distinguishes unavailable files, gaps in scan labels, covers, dates, reused sheets and actually read faces. The absence of K43-02 is a source limitation of the package, not an omitted audit of an available file.

### How to read the registers

`SA19_entries.tsv` is an exhaustive partition of the supplied index. `SA19_items.json` consolidates repeated topics while retaining every source-entry ID and the original scope assessments. `SA19_claims.json` includes source assertions and eight explicitly labelled supplementary reconstruction records; those eight are excluded from the source-assertion subtotal. Canceled drafts, copied statements and anonymous reused material are identified rather than attributed automatically to Grothendieck. In particular, “recorded source assertion” does not independently authenticate handwriting or authorship.

`status_on_pages` records the canonical page status, and `status_detail` retains the fuller reading, including cancellations, partial proofs and uncertainty. A theorem can be established today while still “open on the pages.” Conversely, a correct reconstructed specialization is not a proof of the source's unrestricted sentence. `class` concerns the precise statement or expressly identified refinement: A, later own published work; B, established development by others; C, partial development; D, no exact development located within the recorded searches; E, attributed or otherwise established earlier background; F, insufficiently identifiable formulation. D is a bounded negative search finding, never a novelty certificate. A is a publication match, not proof that an undated sheet preceded the publication.

Line numbers refer to unchanged input `.tex` files, counted from one. Consolidated `cote` fields are lists and `scans` are qualified strings such as `43/125`; `occurrences` and `lines` preserve the individual source files and line ranges. This prevents a cross-package item from acquiring a fictitious single cote. Merged IDs remain resolvable through `SA19_aliases.tsv`. The top-level files are authoritative; workstream records preserve the fuller independent audit and may retain pre-consolidation IDs or counts.

## 1. Cote 43 in archival order

### 1.1. Class-field cohomology, ray classes and generalized Picard objects: scans 1–48

The opening sheets set out global arithmetic class-field theory through divisors, ray classes, idèles and norm maps. They explicitly name Artin–Takagi, Dirichlet and Minkowski. Their role in the dossier is therefore foundational background, not a collection of new conjectures. The later Artin map targets the abelianization, correcting the unrestricted nonabelian target of an earlier display. Unit factors outside a modulus, positivity at real places and the profinite completion of a local multiplicative group must be retained. The exact quotient behind the displayed `E₀` line also needs correction: an intersection and a quotient by one of its ambient groups are not interchangeable (CL-SA19-601–608; Milne, 2020, Chapters I and V).

The unfinished converse concerning finite-index subgroups of units has a contemporary exact input in Chevalley's power-congruence theorem. It is a closed mathematical verification, although the written sentence remains incomplete. The dossier does not infer its first circulation from a later exposition (MP-SA19-120; Chevalley, 1951, Theorem I).

The Picard object on scans 15–16 has a degree augmentation to the integers. It cannot silently mean only the connected Jacobian. Over a nonclosed base, relative Picard points and actual line bundles also differ by a descent/Brauer obstruction. These distinctions recur throughout the later local and curve tables. Koszul's contemporary exposition of Rosenlicht and Serre's class-field framework supply the historical setting, but the particular local-symbol and Lang-pairing diagrams on the sheets are not full proofs (CL-SA19-609; Koszul, 1954; Serre, 1959).

After the missing K43-02 range, scans 32–35 propose cohomology/Ext comparisons through a generalized Picard object and a degree-two Yoneda class. A section gives a proposed splitting, but its validity depends on the coefficient category and on the comparison itself. The strongest all-degree formulations are therefore kept conditional. The later formal-curve local Jacobian is a precise dimension-one comparison; it does not settle a higher-dimensional universal property for every commutative algebraic group (CL-SA19-610–611; MP-SA19-121; Contou-Carrère, 2013).

The Witt-series calculations on scans 37–38 are checked with their actual sign convention: Witt addition is multiplication of series, Verschiebung substitutes a power of the variable, and Frobenius/Verschiebung satisfy the appropriate multiplication-by-p relation. The Teichmüller plus convention is preserved rather than replaced by a familiar minus convention. Cartier's note gives the relevant later formulation, with its presentation date distinguished from publication (CL-SA19-612; Cartier, 1967).

The admissibility and limit questions on scans 40–43 expose a different issue. Lang-type vanishing for connected algebraic groups does not imply vanishing of all positive cohomology with constant integral coefficients. In continuous discrete cohomology,

\[
H^2(\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_q),\mathbf Z)
\cong \mathbf Q/\mathbf Z.
\]

For a finite Frobenius module, first cohomology gives coinvariants; rational points give invariants. Equal cardinalities do not produce a canonical identification. These exact distinctions explain the alarms without deciding whether an unclear symbol on the page names a more restricted category (CL-SA19-613–615; MP-SA19-123; `workstreams/codex43/proofs.md`, C3).

### 1.2. Flags, injectives, adèles and the path algebra: scans 45–69

This part builds rings along flags by iterated localization and completion, then relates them to Hom groups between indecomposable injectives. The order of operations matters. Even a smooth two-dimensional model distinguishes a power-series ring with Laurent coefficients from its iterated Laurent completion. The later correction from “local” to “semilocal” likewise preserves multiple branches rather than erasing them (CL-SA19-616; Braunling et al., 2016, Theorems 0.1–0.2).

A decisive continuity error occurs in the proposed passage

\[
\operatorname{Hom}(U_i,\varinjlim_j V_j)
\overset{?}{=}\varinjlim_j\operatorname{Hom}(U_i,V_j).
\]

Being finite over a localization is insufficient for the required finite presentation over the original ring. With \(R=k[[t]]\), \(K=k((t))\) and \(V_n=t^{-n}R/R\), each \(\operatorname{Hom}_R(K,V_n)\) is zero because \(V_n\) is killed by a power of \(t\), whereas the quotient map \(K\to K/R=\varinjlim V_n\) is nonzero. Every hypothesis used in the counterexample is checked. The repair is an actual finiteness/continuity hypothesis, not an ink decision (CL-SA19-618; RF-SA19-618; Matlis, 1958; EGA IV₃, 8.8.2–8.8.3).

The simplicial coefficient construction explicitly notices degeneracy difficulties. The path algebra has a real associativity calculation by triple concatenation, but its topology and restricted infinite sums need further specifications. The differential on the graded endomorphism algebra must have the form

\[
d(u)=\Theta u-(-1)^{|u|}u\Theta.
\]

The plus sign in one display disagrees with the following degree-zero formula. The incomplete expansion of a square is another separate alarm. The exact finite certificates check signs and multiplication; they are not evidence of convergence for all infinite series (CL-SA19-619–622).

Yekutieli's action of adèles on the residue complex is an exact later development to compare, and the higher-adèle operator algebras supply further structure. An action is weaker than an identification with all endomorphisms. The dossier therefore records those later theorems without declaring every topological comparison in the manuscript solved (Yekutieli, 2003, Theorem 0.1; Braunling et al., 2016, Theorems 0.1–0.2; MP-SA19-124–125).

### 1.3. Local Jacobians and changing cohomology theories: scans 71–98

Scans 71–76 begin explicitly in Zariski cohomology with locally trivial extensions. For a noetherian regular local ring of dimension \(d\), the supported cohomology of the structure sheaf is concentrated in degree \(d\); positive cohomology on the punctured spectrum shifts by one. Completion and split-unipotent dévissage have exact formulations. These are genuine local-cohomology results, subsequently developed in SGA2. They do not alone prove the proposed representability of an entire algebraic-group-valued functor by a local Jacobian pro-object (CL-SA19-623–626; Grothendieck, 1968a, Exposés II–V).

The change to “Weil cohomology” on scans 77–78 is mathematically substantive. No unrestricted fppf interpretation of positive-degree vanishing for the linear part is possible: the quaternion symbol over \(\mathbf C(x,y)\) has a nonzero residue and supplies a Brauer obstruction. This refutes the broad interpretation, while the unclear site prevents attributing that broad claim definitively to the intended text. The later radicial-purity question, the curve-Jacobian complex and the relation between fppf, fpqc, perfect and quasi-algebraic objects all remain category-sensitive (CL-SA19-627–634; MP-SA19-126, 128–131).

The Weil-site problem is merged across the successive stages at 77–78, 92–93 and 94–95. The definitions, coverings, coefficients and derived direct images still have to be matched. Serre's quasi-algebraic category deliberately kills purely inseparable information; it does not retain \(\alpha_p\) merely because the underlying point set seems harmless. Suzuki's precise rational, ind-rational and pro-étale settings provide exact modern comparison theorems, but their hypotheses cannot be transferred to arbitrary sheaves or to an unidentified earlier site (MP-SA19-01; Serre, 1960; Suzuki, 2022, Theorem 2.1.5; Suzuki, 2020a, Proposition 2.7.8 and Remark 2.7.9).

The Néron realization pages themselves withdraw a continuity assertion and raise injective/acyclicity questions. These are separate prerequisites for the spectral sequences, not consequences of drawing a double complex. A composite-functor spectral sequence is available once its acyclicity assumptions are met; the pages' broader realization claims require their own proof (SA19-26–30; CL-SA19-007–012; Grothendieck, 1957, Theorem 2.4.1).

### 1.4. Local and curve duality, supports and the Jacobian table: scans 100–142

The local Rosenlicht heading and the Ext comparison at scan 102 show the intended organization particularly clearly: local class-field objects should encode cohomology against algebraic group coefficients. The reciprocity core has exact proalgebraic and modern derived realizations. The all-degree, arbitrary-coefficient statement remains stronger than those verified results. The Witt quotient, perfecting operation and several compatibility squares are separately indexed, so that a theorem in one realization is not taken to prove an unnamed map in another (SA19-1, 30–35; CL-SA19-015–022; Serre, 1961, §4, Theorem 1; Suzuki, 2022, §§2.6–2.7).

The local tables distinguish ordinary local-field duality from geometrized cohomology over a residue field. Their complementary degrees differ. A component pairing also does not imply a canonical product splitting. The proposed higher internal-Ext vanishings require particular care: degree-one Barsotti–Weil duality does not justify concentrating every derived Hom in that degree. Ribeiro and Rosengarten establish specified internal Ext statements over arbitrary bases, while also exhibiting a nonvanishing higher degree. Oort–Oda's geometric algebraic Yoneda statement belongs to a different category (CL-SA19-037–052; Oort & Oda, 1968; Ribeiro & Rosengarten, 2026, Theorems A–C).

The coherent local-duality notes have especially exact publication matches. The regular-local formulation is SGA2, Exposé V, Théorème 2.1. The Ext-with-support formula at scan 125 recurs, with an actual proof and explicit coherence, at scans 161–162. These are one claim, CL-SA19-054, with separate occurrence statuses. Under the stated locally noetherian/coherent/quasi-coherent hypotheses, the sheaf formula is

\[
\underline{\operatorname{Ext}}^i_Y(F,G)
\cong\varinjlim_n\underline{\operatorname{Ext}}^i(F/\mathcal J^{n+1}F,G).
\]

The global version needs the corresponding noetherian finiteness. The proof uses injectivity of the torsion submodule of an injective. It is not the false unrestricted Hom–colimit argument above (SA19-36–38; Grothendieck, 1968a, VI.2.3; Stacks Project, tags 0BJD and 08XW).

For a complete curve, the Kummer sequences, trace, Jacobian self-duality and finite coefficient rows are substantial. Finite-flat global duality is established in a precisely declared setting by Artin–Milne and Suzuki. The text's full relative infinitesimal rows need an appropriate realization and the relevant higher-direct-image vanishing; perfect test-sites that kill infinitesimals do not automatically prove a big-fppf group-scheme identity. Likewise, geometric points of \(J[p]\) cannot replace the whole finite group scheme. The supersingular example makes that loss visible (CL-SA19-059–075; Artin & Milne, 1976, Corollary 4.9; Suzuki, 2020a, Theorem 3.1.3).

The local/global compatibility on scans 135–140 is a map-level question. Point-supported Ext, henselization/completion, extension by zero and the localization triangle have distinct hypotheses. The unshifted final box cannot simply replace the preceding formula with its connecting-degree shift. The dossier keeps the finite prime-to-characteristic restriction actually inserted on the page, and the canceled broader coefficient range remains canceled (SA19-44–48; CL-SA19-076–083; MP-SA19-28–32).

This Pro range does **not** supply a second Fourier-kernel proof, a uniform intermediate-cycle-Jacobian dimension bound or a height construction. Those negative findings were established by reading the whole range and the positive companion passages. They are retained inside the cross-package merged items, not silently turned into additional occurrences of a theorem.

The interspersed reused material also matters. Atiyah's Thom-complex/stable-homotopy material is a different author's text; the James-number and stable-range computations retain that attribution. EGA direct-image and multiplicity fragments are identified by exact published statements. In particular, EGA IV₃, 12.2.3(vi), explicitly records the unresolved multiplicity question under universal openness, full support and fibrewise \(S_1\) at the time. A simple nonflat module refutes an overbroad inequality-implies-flatness reading; it does not refute that different semicontinuity problem (CL-SA19-084–103; MP-SA19-33–39; Grothendieck & Dieudonné, 1966, pp. 182–183). Reused sheaf typescripts have mathematical matches with Cartan's results, without an unsupported authorship attribution.

### 1.5. Tate duality and retained finite models: scans 143–160

The English local/global duality sheets closely match Tate's 1962 congress report, published in 1963. Their finite-module pairing, local Euler characteristic, unramified annihilators and global exact sequence are verified against that primary report. The full p-primary collection involving \(\mu_p\), \(\alpha_p\) and \(\mathbf Z/p\) requires the flat site because of the infinitesimal groups \(\mu_p\) and \(\alpha_p\); \(\mathbf Z/p\) itself remains finite étale and is governed by Artin–Schreier theory. The quotient topologies differ. Tate's opening invertibility hypothesis alone does not cover the full infinitesimal range; the modern finite-flat theorem is recorded separately (CL-SA19-635–639; Tate, 1963, §§2–3; Suzuki, 2020b, Theorem 5.2.2.1).

The tentative abelian-variety extension at scan 146 does not prove finiteness of the Tate–Shafarevich group. No current claim of a general settlement is made. The problem index separates the existence of duality statements, conditional finite-group formulations and this unresolved finiteness condition (CL-SA19-640; MP-SA19-132).

The later integral and rational ℓ-adic diagrams distinguish a lattice, its rationalization and descent to finite models. A reversed arrow is checked against the tensor formula and the corrected following diagram. A continuous finite-dimensional ℓ-adic Galois representation has compact image and a stable integral lattice; compactness is essential. Serre's Lie-algebra invariance under finitely generated field extension does not imply invariance after every infinite extension. The source's retained model algebra can therefore differ from the actual monodromy algebra over the limit field (CL-SA19-641–646; Serre, 1968, Chapter I, §1.1; EGA IV₃, 8.8.2–8.8.3; MP-SA19-133–134).

### 1.6. Hom and Ext, primitive torsors and formal groups: scans 161–193

The tables are audited cell by cell in `workstreams/codex43/hom_ext_cells.tsv`, including blanks, canceled cells and an unlabeled matrix. Two hundred cells are recorded; a blank is not a zero and a canceled assertion is not restored. The Hom table is functorial and must be tested on nonreduced algebras. In particular,

\[
\underline{\operatorname{Hom}}(\mathbf G_a,\mathbf G_m)=D(\mathbf G_a)
\]

is a formal character object, although its geometric field points vanish. Height-one Hom groups are expressed through the restricted p-operation on Lie algebras. The finite, connected, étale, proper and affine arguments cover many cells, but they do not justify the unresolved mixed abelian-target comparisons (CL-SA19-648–654; SGA3, VIIA.7.2, VIIA.8.1 and VIIB.4.2).

The Ext heading explicitly says “geometric.” Over an algebraically closed field of characteristic p, labelled extensions of \(\alpha_p\) by itself are parameterized by two scalars. In the Dieudonné extension, F and V land in the subobject and vanish there, so \(FV=VF=0\), hence p kills the middle module; only then is the two-dimensional vector-space description justified. This gives \(k\oplus k\) as an additive group, with the scalar convention specified. It is not a classification of middle-group isomorphism types without labels (CL-SA19-652).

The three questioned unipotent cells have precise verified geometric answers. Hazewinkel–Oort's report gives \(\operatorname{Ext}^1(\mathbf G_a,\mathbf G_a)\) as the free left \(k[F]\)-module on the length-two Witt extension. The covariant Frobenius exact sequence proves \(\operatorname{Ext}^1(\mathbf G_a,\alpha_p)\cong k\). The contravariant sequence has a degree-two term: its degree-one computation gives only an injection into \(\operatorname{Ext}^1(\alpha_p,\mathbf G_a)\). The independently opened one-dimensionality statement in Fanelli–Schröer completes that equality. This correction to the run's initial deduction is preserved in the proof and check-event log (CL-SA19-680; Hazewinkel & Oort, 1972b, Lemma 2.1; Fanelli & Schröer, 2020, p. 8).

For an abelian variety A, the exact sequence for multiplication by p, together with \(\operatorname{Hom}(\mathbf G_a,A)=0\) and \(p\mathbf G_a=0\), gives the finite-kernel reduction

\[
\operatorname{Ext}^1_{\mathrm{alg}}(\mathbf G_a,A[p])
\cong\operatorname{Ext}^1_{\mathrm{alg}}(\mathbf G_a,A).
\]

It does not prove the different \(\alpha_p/A\) and \(\mu_p/A\) cells (CL-SA19-681). Those exact comparisons remain bounded unresolved findings after the recorded searches.

The primitive-torsor argument on scans 167–169 actually checks associativity and the unit under its rigidity hypotheses; its inverse reference to Serre's page 183 is not falsely reported as independently read in that edition. Étale extension invariance under radicial base change has an exact SGA1 counterpart. The seemingly remote Chevalley exposé cited for the Artin–Schreier calculation really does contain the needed primitive-polynomial argument (CL-SA19-655–657; SGA1, IX.4.10; Grothendieck, 1956–1958, Exposé 7, pp. 8–9).

The F/V classification sketches, formal/algebraic gluing and continuous Hopf duality retain their perfect-base, topology and covariance assumptions. Over a field, the affine-group approximation is established: SGA3 VIB.11.13 gives algebraic quotients and faithfully flat transition maps. Over a general ring, Barr's cofree-coalgebra existence and Kihara's projective-coring theorem over semihereditary rings are different statements. Neither licenses an arbitrary-ring finite-free subcoalgebra assertion (CL-SA19-658–663; Barr, 1974; Kihara, 2016).

The source correctly warns that an inverse limit may forget pro-information. Its further suggestion that artinian objects alone repair this is false in a general ambient category: the underlying-set functor on profinite sets forgets continuity. Finite presentation over a fixed base, by contrast, gives the relevant affine-scheme Hom–limit comparison. The presumed abelian ind-affine category on scan 193 remains insufficiently defined (CL-SA19-664–667; MP-SA19-147–148).

### 1.7. Length categories, Dieudonné modules and pairings: scans 195–208

The Ind construction from a small length category belongs to established abelian-category theory. The converse based only on finite socle-stage exhaustion is too weak. For \(R=k\oplus V\) with \(V^2=0\) and infinite-dimensional V, every module has Loewy length at most two, while R is not a union of finite-length submodules. Local noetherianity supplies a valid refinement; the initial Gabriel radical cannot be identified with the weaker filtration without it (CL-SA19-668–670; Gabriel, 1962; RF-SA19-669–670).

The formal-group module sketches then require a specified completed Dieudonné ring and essential-socle/artinian-injective assumptions that the source itself notices. Semilinear normal-form multiplication is checked exactly. An increasing union of Frobenius-nilpotent stages has elementwise nilpotence, not necessarily one exponent annihilating the whole union (CL-SA19-671–673; Oort & Oda, 1968, p. 82).

The final sheets return to Jacobian-type pairings through the Picard–Brauer obstruction, the Poincaré biextension and the tame symbol. The degree-one Tate pairing is meaningful without suppressing all higher Ext. A finite cover alone does not supply finite-group Tate cohomology. The tame symbol needs residue-field norms at nonrational points and its diagonal sign; the orthogonality claim needs strict local units, not arbitrary units. On \(\mathbf P^1\), pairing \(f=t\) with the idèle having component 2 at zero already distinguishes those readings. The final Albanese-kernel evaluation pairing leaves a choice-independence check unfinished, so its raw divisor evaluations are not declared invariant without the missing cancellation (CL-SA19-674–679; MP-SA19-150–152; Tate, 1963; Deligne, 1991, §1).

## 2. Cote 44: the 1964 cycle-Jacobian programme

The programme and the letter dated **Bures, 12 August 1964** seek abelian varieties attached to algebraically trivial cycles. Only the letter is explicitly dated; that date is not assigned to the separate programme leaves or reused sheets. Their requirements include the familiar endpoints, a uniform odd-Betti-number bound, complementary duality, cohomological realizations, positivity, height/intersection formulas and hyperplane restriction. The letter also admits that the intended “Albanese equivalence” is not well identified. This is a defining uncertainty, not an invitation to select whichever later Jacobian has the right dimension (SA19-225–231; MP-SA19-86–96).

The closest checked historical model is the **incidence/Picard quotient**. The actual construction forms divisor correspondences from cycle families. Saito's Proposition 3.4 proves the all-codimension Picard-homomorphism dimension bound, and Theorem 3.6 constructs the incidence representative. Kleiman's account explicitly credits the bounded Picard-family mechanism to an unrecorded 1964 observation of Grothendieck. This is stronger evidence than a merely similar modern theorem, while still not recovering the programme's unspecified integral kernel (Saito, 1979; Kleiman, 1971, pp. 446–447; CL-SA19-440–444).

Universal regular representatives and algebraic Abel–Jacobi images remain separate. Kahn's corrected codimension-two argument addresses the stronger regular-homomorphism problem. Achter, Casalaina-Martin and Vial provide exact functorial and realization results with their own prime and codimension restrictions. Ottem–Suzuki's counterexample to universality of an Abel–Jacobi map does not refute Saito's incidence construction. The 2026 sources checked here add torsor and motivic descriptions in specified settings; they do not establish universal existence in every codimension (Kahn, 2021; Achter et al., 2023, 2026; Ottem & Suzuki, 2020; Hernández & Pelaez, 2026).

The integral qualifications are decisive. Saito's complementary comparison is an isogeny, not automatically the canonical integral duality asked for on the sheet. An abstract finite-free \(\mathbf Z_\ell\)-subquotient already admits a noncanonical embedding by projectivity, so a substantive stronger Tate assertion must preserve extra geometry, naturality or equivariance. Those additional data are not determined by the bare phrase in the letter (CL-SA19-443–447; MP-SA19-89–91).

The middle incidence correspondence must pass four different tests: codimension, symmetry, descent and positivity. The first two are formal. Literal **integral descent through the full kernel** fails before positivity is considered. Take a complex elliptic curve E with \(\operatorname{End}(E)=\mathbf Z\), use twice the Poincaré correspondence, and obtain the symmetric homomorphism \(-4\). Quotient by its full kernel is \([4]\). Pullback through this quotient multiplies an integral homomorphism by 16, so the claimed descended class would require \(-1/4\). The product extension in the computations verifies the same obstruction in the stated higher middle-dimensional setting. Quotienting by a reduced connected radical or working rationally are explicit alternative formulations, not silent readings of “kernel” (CL-SA19-449–450, 459).

The factor-two Néron–Severi construction is valid: for a symmetric map f, graph pullback of Poincaré has associated map \(f+f^\vee=2f\). This does not prove ampleness. The primitive-decomposition qualification remains necessary, and the letter only refers to unspecified unproved assertions in its proposed reduction of Hodge positivity. It does not explicitly identify all of them as Lefschetz assertions. Peters's 2026 criterion is conditional; the Caibar–Clemens preprint was withdrawn in 2013 because of an error and cannot be cited as a settlement (CL-SA19-448, 461–463; Peters, 2026; Caibar & Clemens, withdrawn 2013).

The height formula likewise remains partly specified. The source proposes a geometric pencil relation between a Néron–Tate pairing and a signed intersection number. For divisors, a precise comparison uses a regular fibred model, vertical correction terms and an agreed normalization. Künnemann's higher-cycle theorem concerns abelian varieties over number fields, so it cannot be substituted for the unrestricted pencil statement. The finite-kernel phrase in the middle hyperplane clause is crossed out and remains withdrawn (CL-SA19-451–453; Ulmer, 2014, §4.3 and errata; Künnemann, 2001, Corollary 1.7).

The numerical-versus-\(\tau\) assertion has a clear conditional boundary. With \(\tau\) interpreted as torsion-algebraic equivalence, the divisor theorem is classical, whereas an unrestricted higher-cycle version is false. Clemens's non-torsion homologically trivial codimension-two classes supply the obstruction. This does not decide the ambiguous intended relation or authorize inserting “divisors” into the source (CL-SA19-454, 460; Grothendieck, 1962, FGA VI, §4; Clemens, 1983, Theorem 0.2).

Reused sheets in this cote are not suppressed. The completion draft needs its graded/noetherian setting. The root-system draft has a genuine integrality defect: finite reduced roots spanning the lattice and stable under integral reflections need not have integral coroots. The verified rescaled-root example isolates the missing primitivity hypothesis. The repaired assertion is this run's formulation, and neither its proof nor its authorship is assigned to the canceled draft (CL-SA19-455–457, 464–466; SGA3, XXI.1.1).

## 3. Contextual cotes 16, 47 and 54

### 3.1. Cote 16: Lefschetz structures, the standard conjectures and local Picard–Brauer duality

The largest contextual component develops intrinsic gradings, primitive strings, raising/lowering operators, a universal Lefschetz algebra and correspondence-theoretic consequences. Its letter **C** denotes inverse-Lefschetz algebraicity, conventionally called **B** in the later standard-conjecture notation. It must not be identified with the modern Künneth conjecture merely by the letter. Formal equivalences and product/hyperplane reductions are matched by their definitions and quantifiers, especially in Kleiman's Proposition 2.9, Lemma 3.15 and Theorem 2.13 (CL-SA19-201–215, 233–255; Kleiman, 1968).

The literal integral exterior model has two separate obstructions. Ordinary exterior multiplication satisfies \(\xi^n=n!\,\mathrm{vol}\), so the top integral map is not an isomorphism for \(n\ge2\). Ordinary symplectic contraction lowers a primitive string with coefficients \(j(n-i-j+1)\); this is not the unit-step operator prescribed by the draft's endpoint identities, even after rationalization. The earlier run's normalized integral matrix-algebra model is valid as a reconstructed object, but its identification with the literal exterior-contraction algebra is not established (SA19-101, 122–123; CL-SA19-208–210, 279).

Several operator alarms survive or are sharpened by the second pass: an overlong exponent range, the wrong endpoint projector, an unsupported global identity and the one-sided cutoff in the later induction. The last has an exact \(H^*(\mathbf P^2)\) certificate satisfying the intended inverse hypotheses. A two-sided block cutoff repairs the proof. Confirmed ink remains confirmed ink even when its mathematics is false (SA19-124; CL-SA19-212, 253–255, 280; MP-SA19-43).

The four-form Hodge-algebra construction is audited on its own terms. Associativity is an independent four-variable identity; nondegenerate pairings alone do not imply it. The scalar normalization also needs nonzero norm and a suitable square class. The earlier run's infinite-orbit and growing-span examples are rechecked under their explicitly fixed operator convention, while the source's smallest-dimension question remains separate from geometric realization as the cohomology of a smooth projective variety (CL-SA19-223–229; MP-SA19-46–48).

The local Picard–Brauer sheets have an exact source in *Le groupe de Brauer III*, §8. The published setting includes a complete normal noetherian two-dimensional local ring A, an algebraically closed residue field k, a chosen coefficient field k⊂A, and a proper birational regular resolution that is an isomorphism over the punctured spectrum. The exceptional intersection lattice gives a finite discriminant pairing. The claimed comparison with the cohomological pairing is a distinct step: Remark 8.5 explicitly acknowledges that the verification was not performed. Suzuki's Proposition 11.10 supplies a later exact analogue in mixed characteristic for p-primary component pairings, but its hypotheses do not directly close every equal-characteristic version of the old question (SA19-103–104, 109–111; CL-SA19-216–222; Grothendieck, 1968b, pp. 148–151; Suzuki, 2024, pp. 500–501).

The Coates letters currently read **4 January 1967** and **6 January 1966**. The latter date is confirmed by the supplied second-pass reading, even though editorial commentary proposes 1967. The dossier retains 1966 and labels the proposed harmonization as inference. The distinction between hard Lefschetz and algebraicity of its inverse is equally necessary. Katz–Messing's original paper documents Deligne's hard Lefschetz result in the 1973 lecture/submission period, before the full 1980 *Weil II* treatment; their Theorem 2 also proves specific finite-field characteristic-polynomial and Künneth assertions. Neither result proves the general inverse-correspondence conjecture. Jannsen's numerical semisimplicity theorem concerns a different quotient from the draft's homological independence hope (CL-SA19-240–252, 282–284; Katz & Messing, 1974; Deligne, 1980, Theorem 4.1.1; Jannsen, 1992, Theorem 1).

The reused editorial material is also fully audited. Matlis's module results and Hartshorne's sheaf-injective theorems match the mathematical statements, but exact typescript authorship remains distinct from a theorem match. The way-out-functor page, Karoubi announcement, Amitsur fragment, SGA3 correction and Bourbaki exposition plans keep their separate provenance and hypotheses. The finite-field algebra \(\mathbf F_2^3\) refutes unrestricted global monogenicity, and \(A\times A/(t)\) over \(A=k[t]\) refutes a finite-étale fibre criterion lacking flatness. Missing draft context remains an explicitly bounded source question (CL-SA19-230–232, 256–278; Matlis, 1958; Hartshorne, 1966, II.7.6, II.7.17–18; Stacks Project, tag 02GU).

### 3.2. Cote 47: Fourier transforms with the actual correction history

The opening convolution-to-tensor statement is proved on the next supplied page by base change, projection formula and Künneth, ending in “cqfd.” The earlier note's “unproved” description understates the text. Its general marginal extension still needs support, boundedness and monoidal-coherence hypotheses (SA19-201–202; CL-SA19-401–402).

The square of the relative transform evolves from identity to inversion and then to inversion with determinant line and shift:

\[
\Phi_{A^\vee}\Phi_A(F)
\simeq(-1_A)^*F\otimes\pi_A^*\det(\operatorname{Lie}A)[-g].
\]

The earlier K-theory formula does not visibly receive the line factor, and an old identity target survives inside the proof. Mukai's field theorem and Laumon's relative theorem establish the corrected result. The manuscript's actual comparison map still has an explicitly deferred zero-fibre compatibility. A Koszul rank calculation is necessary but does not by itself identify that map (SA19-203–205; CL-SA19-403–409; Mukai, 1981, Theorem 2.2; Laumon, 1996, Theorem 1.2.4 and Lemma 1.2.5).

In the checked ample-line-bundle case over a field, the exponential formula has a correct generating expression but a wrong extra rank factor in the expanded Chern coefficients. The elliptic-product example in the computations separates the two formulas exactly. A weaker final integral multiple survives; this does not settle the unrestricted relative exponential formula or an integral Fourier operation on the full unspecified Chow filtration. The relative reverse-product formula also retains determinant and both Todd factors. Moonen's precise Todd identity and the more restricted integral results are stated with their actual base, polarization and coefficient hypotheses (CL-SA19-413–421, 467; Moonen, 2026, Corollary 2.7(1); Beckmann & de Gaay Fortman, 2023, Theorem 3.8; Hasan et al., 2025).

### 3.3. Cote 54: de Rham duality, finite p-torsion and flatness drafts

The universal vector extension carries the Hodge sequence with an important variance convention: invariant differentials on the extension of A identify with \(H^1_{\mathrm{dR}}(A)\), while its tangent description involves the dual abelian variety. Coleman supplies a precise formulation. Exterior powers then give the specified Hodge-piece dualities, with the uncertain source differential subscript left as an ink question (CL-SA19-426–428; Coleman, 1998, Theorems 1.1 and 2.2).

The question whether the degree-one Hodge extension can be recovered from \(A[p]\) has a strong later answer over a perfect field. Oda identifies the finite Dieudonné module with de Rham cohomology and its Hodge subspace; this does not assert reconstruction of the entire algebraic group E(A) from A[p]. The group scheme, including F and V, matters; geometric p-torsion points are insufficient. Matching the manuscript's particular restricted p-operation still requires conventions rather than just an isomorphism of vector spaces. The June 1967 dissertation and 1969 publication are distinguished (SA19-218–222; CL-SA19-429–431; Oda, 1969, Corollary 5.11).

The reused flatness leaves have unusually exact matches with EGA IV₃. The original nilpotent criterion is Théorème 11.4.1; the universal ideal invoked as “4.1bis” corresponds to Corollaire 11.4.4; and the nonreduced generic-freeness corollary is 11.4.6. Proposition A matches the mechanism of Proposition 11.4.5, whose published base Y is irreducible; extending it to the source's merely nonempty Y uses this run's separately labelled approximation/component-open argument. The canceled nonnilpotent amendment fails for \(A=k[t]\), \(I=(t)\), \(A_1=k[t,t^{-1}]\), \(M=A/(t)\). The published nonnilpotent criterion, 11.4.7, adds an essential equivalence of adic topologies. The independent counterexample checks the written hypotheses and shows that noetherianity and separation alone do not restore flatness (SA19-223; CL-SA19-432–434, 458; Grothendieck & Dieudonné, 1966, pp. 143–147).

## 4. What the earlier notes got right and what changed

The earlier notes correctly identify many explicit questions, isolate several important scope warnings, and provide useful concrete models. Their strongest contribution is often to specify a missing comparison map rather than to proclaim a new theorem. The arithmetic-unit examples, normalized Lefschetz strings and selected four-form constructions are retained as earlier-run mathematics and independently checked.

The main corrections are of four kinds. **Textual updates** apply the actual cote-16 second pass, including the ambiguous reference 6.(5|15), the confirmed overlong exponent, the corrected projector index and the retained 1966 date. **Understatements** include calling the first Fourier identity unproved and overlooking the all-codimension incidence bound closest to the cycle programme. **Overstatements of mathematical force** include accepting a one-sided projector induction, integral full-kernel descent or an arbitrary internal-Ext conclusion from a geometric computation. **Attribution and scope errors** arise when anonymous reused sheets, earlier-run models or absent external project results are treated as claims on Grothendieck's pages.

The five cross-package item merges preserve those distinctions: Fourier comparison into SA19-203; cycle boundedness into SA19-226; height comparison into SA19-229; Cartier-annihilator comparison into SA19-220; and finite-group/Hodge reconstruction into SA19-222. General isogeny-kernel duality, its bidual sign and the separate semilinear conventions are not merged indiscriminately. One repeated support-Ext theorem is consolidated into CL-SA19-054, and the successive Weil-site questions into MP-SA19-01.

## 5. Open steps, readings, links and the present frontier

The problem index includes every identified explicit question, deferred verification, conjecture, hope and unfinished construction, including questions now settled, false interpretations and editorial/provenance problems. It is not a list of 125 currently open research conjectures. Each record gives the strongest source-supported formulation, a separately labelled plausible modern formulation, exact literature scope and a bounded assessment of what further work would be useful.

Several central tasks are now editorial rather than theorem-discovery tasks: reconstructing the source's Fourier comparison map, matching Oda's semilinear conventions, supplying the precise support-duality hypotheses, and aligning reused EGA/Hartshorne material. Other questions remain genuinely broad: standard-conjecture algebraicity, unspecified higher-dimensional local-Jacobian representability, universal regular cycle representatives in full generality, and the precise topological/formal categories proposed on the late sheets. Searches locating related theorems do not settle these formulations. Recent higher-local duality, for example, has a precise mixed-characteristic finite-étale theorem in Galet's 2026 revision; it does not supply the unrestricted representability asserted in the local-Jacobian sketch (Galet, 2026, Theorem A).

The reading register is an agenda for an image-equipped follow-up. It contains mathematical evidence, alternative readings, dependence weight and confidence. It never decides an absent image. Some alarms concern confirmed textual errors rather than uncertain ink; those are labelled accordingly. An implausible sign or index is evidence to inspect, not authority to rewrite the diplomatic source.

`SA19_links.tsv` contains checked archive and publication comparisons. The other-project leads are in their own `SA19_our_project_leads.tsv`, with exact note IDs and named run pointers. Those external target files were not supplied, so their theorem content and reported review status remain unverified. This is explicit source accounting, not a claim that both ends were checked. A separate named-pointer index preserves all detected run identifiers and citing entries. No unnamed Dérivateurs or S6 theorem is manufactured from the general project framing; an internal heading “S6” in the mixed notes is not the external project.

`SA19_directions.md` ranks concrete subsequent tasks by mathematical interest and plausible progress in a few hours. The dossier performs only the verification necessary to judge existing statements; it does not develop those new research programmes.

## 6. Verification, search limits and reproducibility

The four independent reading workstreams cover Pro cote 43, cote 16, cotes 44/47/54 and the nine supplied Codex folders. Substantive verdicts were made by reading entries and passages; scripts serialize those decisions, calculate exact examples and check integrity. Every source entry has one verdict. Every claim has a recorded literature search, with shared search families used only where the exact common mechanism is stated. Search routes include arXiv, Numdam, EGA/SGA, published papers, author bibliographies and backward references; zbMATH Open and MathOverflow were used as discovery routes, with blocked or unproductive access recorded rather than converted into negative evidence.

“Verified” in the bibliography means that the recorded URL was opened. It does not mean that every proof in a work was independently re-proved. The audit distinguishes full primary text, particular theorem/proof reading, abstract-only access, metadata-only verification and unavailable originals. The Oort book, the original Hodge article and some older chapters illustrate why these levels cannot be collapsed. Withdrawn papers remain withdrawn. First circulation, receipt, seminar, publication and reedition dates are separated whenever the opened source supports them; unknown dates remain unknown.

The exact calculations and proofs include integral exterior factorials, normalized string matrices, four-form identities, local discriminant congruences, module/flatness counterexamples, residue pairings, Witt Frobenius identities, finite Dieudonné extension relations, Fourier Chern coefficients, integral descent and root-system counterexamples. Formal proofs cover infinite counterexamples where finite testing would be insufficient. All authored programs and their saved outputs accompany the dossier. Downloaded third-party full texts and the original attachments are excluded from the ZIP; URLs, access evidence and hashes make the research route recoverable.

`CHECK_EVENTS.tsv` records what actually happened. A source-status comparison is not called an independent proof. A finite certificate is not called a proof of an infinite assertion. The actual internal effort setting is not exposed and no numeric setting is claimed. The C16 peer-review correction is retained as an event rather than erased from the record.

### Final counts

<!-- COUNTS_START -->
| Register | Final count |
|---|---:|
| Indexed entries, each assigned exactly once | 174 |
| Consolidated items | 147 |
| Claim records, including explicitly labelled reconstructions | 338 |
| Source-assertion records, including reused material | 330 |
| Supplementary reconstruction records | 8 |
| Problems, open steps and documentary questions | 125 |
| Reading alarms | 201 |
| Checked folder/publication links | 104 |
| Separate external-project lead groups | 23 |
| Separate unread-publication comparison leads | 1 |
| Ranked directions | 27 |
| Bibliography records | 129 |
| Check events | 910 |
| Supplied transcription faces read | 262 |

Entry verdicts: **131 kept**; **25 merged**; **4 withdrawn**; **14 corrected**.

| Class | Meaning | All claim records | Source-assertion records only |
|---|---|---:|---:|
| A | Later own published work | 40 | 40 |
| B | Established development by others | 106 | 101 |
| C | Partial development / exact formulation still qualified | 92 | 92 |
| D | No exact later development located in recorded searches | 14 | 13 |
| E | Earlier or explicitly attributed background | 66 | 64 |
| F | Not sufficiently identifiable | 20 | 20 |

| Page status | Count |
|---|---:|
| stated without proof | 131 |
| open on the pages | 66 |
| proof sketched | 80 |
| corrected by himself later | 11 |
| proved there | 20 |
| not a manuscript assertion | 8 |
| false as stated | 22 |

| Item kind | Count |
|---|---:|
| unpursued implication | 11 |
| idea of the earlier run | 29 |
| reading question | 32 |
| unproved claim | 28 |
| self-flagged step | 23 |
| withdrawn in the same text | 5 |
| title, date or page count | 5 |
| conjecture | 3 |
| other | 11 |

The counts measure adjudicated records, not independent theorems. Several table claims contain separately audited cells, and the problem index includes resolved and false questions. The eight supplementary records are CL-SA19-056, 279–281, 459–460, 465 and 467. Their origin is explicit; they are not attributed to the manuscript.

Bibliographic URL verification: 123 verified and 6 explicitly unverified. Access depth remains separately recorded. Raw workstream counts precede the five cross-package item merges, one repeated-claim merge and one repeated-problem merge.
<!-- COUNTS_END -->

### Principal reference guide

The bibliography contains every cited work and opened URL. The following APA-style guide identifies the principal theorem-bearing sources used in this overview; exact editions and access annotations are in the BibTeX and bibliography audit.

- Artin, M., & Milne, J. S. (1976). Duality in the flat cohomology of curves. *Inventiones Mathematicae, 35*, 111–129. Corollary 4.9.
- Cartier, P. (1967). Groupes formels associés aux anneaux de Witt généralisés. *Comptes rendus de l'Académie des sciences, Série A, 265*, A49–A52.
- Chevalley, C. (1951). Deux théorèmes d'arithmétique. *Journal of the Mathematical Society of Japan, 3*(1), 36–44. https://doi.org/10.2969/jmsj/00310036
- Deligne, P. (1980). La conjecture de Weil. II. *Publications Mathématiques de l'IHÉS, 52*, 137–252. Theorem 4.1.1.
- Gabriel, P. (1962). Des catégories abéliennes. *Bulletin de la Société Mathématique de France, 90*, 323–448. https://doi.org/10.24033/bsmf.1583
- Grothendieck, A., & Dieudonné, J. (1966). Éléments de géométrie algébrique IV: Étude locale des schémas et des morphismes de schémas, troisième partie. *Publications Mathématiques de l'IHÉS, 28*, 5–255. https://doi.org/10.1007/BF02684343
- Grothendieck, A. (1968b). Le groupe de Brauer. III: Exemples et compléments. In *Dix exposés sur la cohomologie des schémas* (pp. 88–188). North-Holland. Section 8.
- Grothendieck, A. (1968a). *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2).* North-Holland. Exposés IV–VI; corrected 2005 reedition distinguished in the audit.
- Hartshorne, R. (1966). *Residues and duality* (Lecture Notes in Mathematics, Vol. 20). Springer. Chapter II, §7.
- Jannsen, U. (1992). Motives, numerical equivalence, and semi-simplicity. *Inventiones Mathematicae, 107*, 447–452.
- Katz, N. M., & Messing, W. (1974). Some consequences of the Riemann hypothesis for varieties over finite fields. *Inventiones Mathematicae, 23*, 73–77.
- Kleiman, S. L. (1968). Algebraic cycles and the Weil conjectures. In *Dix exposés sur la cohomologie des schémas* (pp. 359–386). North-Holland.
- Kleiman, S. L. (1971). Finiteness theorems for algebraic cycles. In *Actes du Congrès International des Mathématiciens, Nice, 1970* (Vol. 1, pp. 445–449). Gauthier-Villars. Pages 446–447.
- Matlis, E. (1958). Injective modules over Noetherian rings. *Pacific Journal of Mathematics, 8*(3), 511–528. https://doi.org/10.2140/pjm.1958.8.511
- Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l'École Normale Supérieure* (4th series), *2*(1), 63–135. Corollary 5.11; the June 1967 dissertation is distinguished.
- Oort, F., & Oda, T. (1968). Higher extensions of abelian varieties. *Nagoya Mathematical Journal, 31*, 81–88. https://doi.org/10.1017/S0027763000012666
- Saito, H. (1979). Abelian varieties attached to cycles of intermediate dimension. *Nagoya Mathematical Journal, 75*, 95–119. Proposition 3.4 and Theorem 3.6.
- Serre, J.-P. (1960). Groupes proalgébriques. *Publications Mathématiques de l'IHÉS, 7*, 5–67. https://doi.org/10.1007/BF02699186
- Suzuki, T. (2024). Class field theory, Hasse principles and Picard–Brauer duality for two-dimensional local rings. *Algebraic Geometry, 11*(4), 460–505. https://doi.org/10.14231/AG-2024-015
- Tate, J. (1963). Duality theorems in Galois cohomology over number fields. In *Proceedings of the International Congress of Mathematicians, Stockholm, 1962* (pp. 288–295). Institut Mittag-Leffler.

The three Suzuki duality records retain preprint-based keys (`Suzuki2013`, `Suzuki2014`, `Suzuki2018`) while the overview cites publication years 2022, 2020b and 2020a respectively. Their exact titles, publication data and theorem locators are in the bibliography; this convention prevents conflating first circulation with publication.
