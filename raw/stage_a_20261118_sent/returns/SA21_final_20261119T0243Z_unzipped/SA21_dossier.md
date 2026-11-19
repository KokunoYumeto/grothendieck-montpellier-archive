# SA21 — Vers une géométrie des formes

## Consolidated dossier, 19 November 2026

This dossier consolidates the supplied transcriptions and notes for Montpellier cotes **156-1 through 156-9**. It follows the changing objects of the manuscript: forms and networks; ficelles and cuts; moderated boundaries; figures and subdivisions; ateliers, magasins and shadows; then disjoncteurs, spatios and correspondences. The result is a source-based account of a developing theory, with its successful arguments, withdrawn assertions, unresolved steps and distinct axiom versions kept visible.

All **122 indexed Pro entries** were read with their cited transcription passages and consolidated into **97 items**. All **82 supplied Codex folders**, their notes, the Pro transcription and its doubt table were read. The numerical inventory in TOPIC.md understates supplied coverage in VII, VIII and IX; the explicit folder list and the actual scan markers control the coverage record. There are **684 scan markers**, including two institutional covers, hence **682 manuscript markers** against 691 catalogue pages. The supplied texts omit **VII scans 2–9 and IX scan 129**. Reused typescript versos are included in the inventory and identified as such. These are limits of the supplied corpus, not supplied pages left unread. No handwritten scan was available, and no diplomatic reading has been changed. [SA21_coverage.tsv; audit/coverage_summary.json.]

The six stages are recorded in the principal tables and this overview. The table of readings remains a queue for a later examination of the ink, as the task requires. Unavailable destinations of cross-references remain explicitly unresolved. Their source passages were checked and their targets searched; the dossier does not describe an absent target as a completed two-ended verification.

### How to use the dossier

| File | Purpose |
|---|---|
| `SA21_entries.tsv` | One verdict for each of the 122 stable source-note IDs. |
| `SA21_items.json` | The 97 consolidated notes, with words, locations, reconstructions and source checks. |
| `SA21_claims.json` | Grouped assertions, constructions and computations across all nine cotes, with page status, checked scope and searched fate. |
| `SA21_problems.json` | Merged authorial questions, including questions answered later in the manuscript or by a checked counterexample. |
| `SA21_readings.tsv` | Mathematical reasons to inspect a sign, quantifier, index, word or marginal scope on the scans. |
| `SA21_links.tsv` | Folder and published-work links whose stated endpoints were inspected. |
| `SA21_project_leads.tsv` | The separately audited links to other research projects, with source IDs, exact recovered endpoints and missing targets. |
| `SA21_unresolved_links.tsv` | Manuscript/publication references whose precise destination or reading remains unresolved. |
| `SA21_directions.md` | Ranked, bounded next tasks, each traced to items, claims and problems. |
| `SA21_search_map.tsv`, `SA21_references.bib` | Executed searches by claim and the checked bibliographic records. |
| `CHECK_EVENTS.tsv` | The actual kind of check performed, without turning source reading into independent proof. |

Line numbers are one-based physical lines of the supplied transcription file. A Codex locator such as `J156-8-09:127` abbreviates `codex/J156-8-09_transcription.tex`, line 127. Some reader appendices use `J8-09` for the same file. Cote and scan are always retained, because manuscript pagination changes or repeats. The Pro file combines I and II, so its physical line numbers differ from the old notes' per-page convention. The source manifests supply hashes and scan-to-line maps. IDs in the principal tables are authoritative; `audit/problem_aliases.tsv` maps the original reader problem IDs to the global numbering.

## 1. The manuscript in its own sequence

The dates below are those of the supplied catalogue, rather than an assertion that every marginal correction was written on that date. Several later margins explicitly revise earlier pages.

| Cote | Catalogue date | Main movement | Supplied manuscript markers |
|---|---|---|---:|
| 156-1 | 5 June 1986 | Forms, segments, branches and network axioms | 26 |
| 156-2 | 6 June 1986 | Topological realizations, ficelles, rives and mailles | 18 |
| 156-3 | 8 June 1986 | Networks through cuts; ordinary topology gives way to moderation | 40 |
| 156-4 | 10 June 1986 | First Analysis situs: strata, figures, two orders and supports | 88 |
| 156-5 | 14 June 1986 | Set figures and a concrete algebra of refinement | 48 |
| 156-6 | 18–20 June 1986 | Second Analysis situs: shadows, restriction and subdivision | 93 |
| 156-7 | 23–26 June 1986 | Third version, loci and the move to primitive disjointness | 105 |
| 156-8 | 26 June–4 July 1986 | Fourth version, support representations and interval figures | 126 |
| 156-9 | 5–15 July 1986 | Spatial objects, ortholattices, correspondences and further corrections | 138 |

### I. Forms, segments and the local-to-global gap

The dimension-zero model is a set of lieux with an equivalence relation. The promised higher-dimensional recursion is not supplied at that point. In dimension one, a segment has a support and a two-element boundary. F1 gives a unique initial subsegment to a chosen point. F2 separates the two pieces at an internal point and imposes a side-containment condition. Its original nonempty-interior clause later becomes optional divisibility. F3 concerns branch germs; a marginal strengthening matters for filtering initial subsegments. F4 glues at a regular lieu, but the support of the composite may strictly contain the union. F5 demands two branches at a regular lieu. F6 is introduced only after an earlier argument fails, and its weak and strong forms differ. Deleted drafts cannot be added to this list as extra live axioms. [SA21-1–10, 17–36; C-SA21-1-001–032.]

Several precise results survive. F1 and the relevant F2 clauses imply injectivity of supports and uniqueness of endpoint pairs inside one ambient segment. Divisibility forces infinitely many lieux and subsegments. Once divisibility is removed, reduced networks may be ordinary simple graphs. A bounded segment can be described by a suitable partial order, unique up to reversal after choosing its endpoint. This is not a total-order theorem and does not solve global orientation. The matching later treatment is Hua2026 §76, with public formal statements inspected but no Lean compilation performed in this run. [audit/root_proofs.md, R-SA21-support, R-SA21-infinite and R-SA21-orders; Hua2026.]

Three countermodels separate nearby claims. A dense ordinal-sum diamond satisfies the ambient axioms, including strong F6, but a union of two successive intervals omits a branch needed by F4: arbitrary-subset inheritance is false. A rational fork is connected in the relevant incidence sense and locally filtered, while points in its two upper branches have no common upper bound; this confirms the author's withdrawal of local-to-global directedness. A chain with two incomparable maximal endpoints satisfies the weak interior version of F6 and fails the whole-support version. That last example diagnoses a missing containment step; it does not itself refute the separate equal-endpoint intersection lemma. [C-SA21-1-018, 027–029, 031; the three named countermodel proofs in audit/root_proofs.md.]

Global orientation remains a distinct native problem. Transport of the two-element endpoint and branch choices yields a useful holonomy formulation, but the network axioms have not been shown here to force trivial holonomy. The final equal-endpoint argument also stops unfinished. These obligations, regular-end prolongation and the filtering interpretation of F5 remain separately indexed. A theorem about one ambient segment cannot discharge all of them. [MP-SA21-007, 009, 010.]

### II. Ficelles, conical regularity and rives

The topological chapter uses a specific notion of regular immersion: after a closed subset is collapsed, the quotient point has a conical neighborhood with compact base. It is neither the algebraic-geometric regular immersion of EGA nor a product collar along the uncollapsed subset. The quotient-subspace embedding lemma has an elementary proof without extra normality assumptions. For a finite simplicial pair, a piecewise linear height function after subdivision constructs the required cone neighborhood. This establishes the finite-polyhedral assertion; an undefined universal tame category is not supplied by that proof. [C-SA21-2-001–005; R-SA21-quotient-embedding and R-SA21-cones.]

A ficelle has two disjoint closed nonopen end subsets, regularity at the contracted ends and connectedness of the punctured end-quotients. The literal definition allows disconnected ends and even a disconnected ambient space. Two disjoint intervals, with the left endpoints grouped into one end and the right endpoints into the other, satisfy every clause. Thus a later necessity of ambient connectedness fails under the unrestricted convention. Reduction to two point ends is valid, and a reduced ficelle is connected. Nontrivial connected finite polyhedra admit reduced structures; uniqueness of the unordered reduced end pair characterizes an arc in that category. The proofs and finite graph corroboration are saved separately. [C-SA21-2-006–011, 023–025; R-SA21-disconnected and R-SA21-polyhedra.]

The interval example has the same hypothesis sensitivity. On [0,1], the end sets {0,1} and {1/2} satisfy the literal ficelle definition but lie outside the asserted initial/final interval classification. Connectedness of both ends restores that classification. Enlarging an end can destroy the other punctured quotient's connectedness, as a checked tripod shows; the author retracts that assertion. A further counterexample found in this consolidation concerns contraction inside one side. Choose a cut in one arm of a tripod and collapse another whole arm, including the center and its end. The contracted subset is closed, connected, contractible and regularly immersed. Its image becomes an interior point of an interval, whose removal disconnects the quotient. Therefore the expanded side-contained contraction statement fails if that side includes the end. The older condition excluding both ends escapes this example. The U/X reading uncertainty remains for the ink. [C-SA21-2-017, 026–028; R-SA21-interval, R-SA21-tripod and R-SA21-side-contraction.]

Cuts retain geometric data. The cutting and gluing assertions use actual end spaces and gluing homeomorphisms; the n-cut construction gives n+1 pieces and n gluings. A categorical equivalence requires a morphism convention, which the reconstruction states explicitly. Mere disjointness is insufficient for compatibility: alternating two-point cuts of a circle are a concrete obstruction. Regularity at the cut is added after an earlier omission, and the two-cone lemma needs a neighborhood-cover hypothesis. The full proof obligations are therefore richer than a finite chain of cut indices. [C-SA21-2-012, 015, 018–033.]

The rive algebra is a filtered colimit of clopen algebras of punctured neighborhoods. In a compact conical model it records clopen subsets of the link. It may be infinite, as a Cantor link shows; connected links of different homotopy types can give the same two-element algebra. Three spaces must be distinguished: the global Stone spectrum, a relative Stone spectrum over the node, and the étalé space of algebra elements. The relative-spectrum interpretation is explicitly a reconstruction. The general neighborhood-section map is injective; the opened isomorphism theorem for a closed subset of a paracompact Hausdorff space is Schapira's Proposition 10.1.2(iii) for sheaves of k-modules, which applies to the F₂-algebra setting here. Hua2026 §77 treats a specified rive-to-boundary injection. Neither supplies all the regularity and gluing needed for a full spectral cut. [C-SA21-2-034–040; R-SA21-rives, R-SA21-sheaves; Schapira2023; Gillam2011.]

The maille assertions remain separate: regularity of the full cut, the partial cut with two copies of the node, its characterization as a ficelle, and final symmetry between two node-and-birive pairs. Boolean algebra alone does not prove these geometric statements. [C-SA21-2-042–046; MP-SA21-018–021.]

### III. Cuts, tronçons and the failure of ordinary topology

III makes cutting data primitive. Finite compatible sets, compatible complements and component relations lead to ordered tronçons. The successful reconstruction recovers the order up to reversal from betweenness and recovers betweenness from two-point cuts. The full converse characterization of arbitrary abstract cutting data remains separate. Bare symmetric compatibility does not suffice for the first complement-injectivity argument. [C-SA21-3-001–008; parts/cotes_3_5/proof_checks.md.]

The attempt to read this through ordinary topology then breaks. Twin rational points give a canonical tronçon topology that is neither T0 nor sober. A strict-coordinate order on R² produces the Euclidean topology without making the order total. These examples satisfy their stated order conditions; they are not objections to a stronger, specified ficelle model. The author's own closure argument also fails and is abandoned. The ensuing frontier, complement and component calculus is moderated. It keeps compatibility as part of the structure rather than assuming every pair of subsets behaves like ordinary closed subsets. This is an actual change of mathematical framework. [C-SA21-3-015 and neighboring claims; corresponding problem records.]

### IV–V. Figures, two orders and the set model

IV repeatedly changes its primitive objects: topological strata and residuals; multistrata, places and shadows; then figures with subfigure inclusion and subdivision/refinement. Each change addresses an obstruction. Arbitrary subfamilies need not preserve residuals, so subfigures must be lower families. Point shadows do not capture all intended cord data. Entrywise refinement need not extend to subdivision. An attempted boundary-replacement union is withdrawn because the larger elementary object may also need alteration. [C-SA21-4-001–043; parts/cotes_3_5/narrative.md.]

Two representation gaps deserve explicit separation. Complete join-irreducibility, in the equality-based sense used in IV, does not force joins to act like unions of strata: M3 is a checked counterexample. VI later strengthens the definition to complete join-primality. Separately, a set family with least neighborhoods need not distinguish its underlying points. Neither missing assumption may be imported silently into the earlier statement.

Virtual supports arise from double orthogonality. They form a complete ortholattice under the stated conditions, but need not be Boolean. The finite certificates include a seven-element multistratum system with eleven figures and six closed supports. All the relevant compatible-lower-family axioms are checked; identity subdivision handles the limited subdivision requirements at that stage. Later optional moderation axioms are outside the counterexample's scope. Hua2026 §79 gives the corresponding negative result; the dossier includes independently checked certificates and does not infer that the full later theory is refuted. [C-SA21-4-033–035.]

V supplies a concrete model: admissible families correspond to preorders on their supports, or Alexandrov topologies. The sorite adds a membership-coverage condition missing from an earlier formulation. Lower subfigures, refinement, compatibility, infima and a genuine subdivision-extension construction can then be checked directly. Yet two claims fail even here. On a two-point underlying set, the five elementary admissible figures have three comparison components. The proposed external-product construction also fails: it leaves an empty residual at its top. Another two-point example shows that keeping a closed stratum does not preserve its residual. These failures are distinct from the author's later withdrawal of a proposed least-extension characterization. [C-SA21-5-001–020.]

The final topology-extension theorem survives: if T is closed in (S,τ) and σ is finer than the induced topology on T, the least finer extension has closed sets A∪B, with A τ-closed and B σ-closed in T. It preserves the original closures of subsets of S∖T. Weaker intermediate criteria do not characterize it. The display with an intersection where this argument needs a union is a high-impact reading alarm, not an emendation made by this run. [C-SA21-5-021–029.]

### VI–VII. Shadows, local reconstruction and subdivision

The atelier now carries two orders. Elementary figures decompose larger figures; lieux are minimal nonzero objects for refinement. The large shadow records elementary refiners, while the small shadow records lieux. The least receiving stratum must compose, leading to At7. A local isomorphism on the subfigures of one fixed figure need not give global faithfulness. The affine and PL interval examples make that distinction concrete. [C-SA21-6-001–018.]

The strengthened VI join-prime definition validates the lower-set representation that failed under IV's weaker definition. A complete lattice map between downset lattices preserving all joins and all meets, including empty ones, is inverse image along a unique monotone map. An independent proof is supplied. This is a precise classical ingredient; it does not settle every proposed atelier morphism or every global reflection condition. A nonempty lower subfamily can fail the atelier compatibility axiom, requiring Sousat2. A pullback formula retaining every nonempty closed-stratum preimage can leave an empty open stratum. These claims have exact finite witnesses rather than informal warnings. [C-SA21-6-011, 013, 016, 043–044; parts/cotes_6_7/formalism_and_checks.md.]

Finite gluing and arbitrary directed local existence are distinct. At11, its binary compatibility part and At11bis are tracked separately. One initially suspected gap disappears under the actual stronger hypotheses: when all figures are of finite type and complete join-primality applies, the directed local-existence condition is vacuous because finitely many local generators occur at a common stage. The initial suspicion is explicitly withdrawn. The claim cannot be transferred to arbitrary refinement-increasing families, which VII treats separately. [C-SA21-6-022–031, 040.]

Subdivision is expressed through disjointness profiles. Under a support-witness hypothesis and locality, it becomes maximality among faces of a refinement, with maximality for the correct order. Extending a subdivision is an additional axiom; demanding an unchanged exterior or a single elementary filler is stronger still. Specific triangulation theorems establish related existence in semianalytic or definable categories, not all these abstract uniqueness or exterior-preservation clauses. [C-SA21-6-032–039; Lojasiewicz1964; Baro2010.]

VII tests polyhedral and locus reconstructions. Its weak proposed simplex criterion is false: a square has nine nonempty faces and satisfies the listed predecessor conditions, whereas a simplex on four vertices would have fifteen. Boolean principal intervals are a stronger standard condition. The ML reconstruction strengthens a lifting axiom during its proof. An attempted replacement of all structure by a disjointness graph is then expressly retracted: common-refiner and shadow-intersection properties had not been derived. Infinite figures require a chosen admitted family beyond finite elementary data. [C-SA21-7-002–016.]

The four-vertex path model is particularly useful. Its six virtual supports form O6, a non-Boolean ortholattice. The certificate checks the stated atelier and locus hypotheses; the relevant optional absorption axiom fails, so no theorem assuming that axiom is contradicted. The end of VII responds by making interior disjointness primitive and restarting the Mag system. The final system has two nested orders, least receiving faces and a symmetric irreflexive relation hereditary under open refinement, with distinct faces of a common stratum disjoint. VIII recapitulates this version. A canceled intermediate draft is not an alternative final axiom system. [C-SA21-7-038–052; LindenhoviusVetterlein2023, Example 3.3.]

### VIII. External supports and formal interval figures

VIII develops primitive strata, compatible lower-set figures, indexed set realizations and morphisms. L2 means that disjointness is detected by all pairs of lieux in the relevant shadows; it is not merely empty intersection of two sets unless different lieux are already disjoint. L1 does not imply L2 under the bare abstract axioms. A margin later makes face-bijection optional for certain maps; stronger conclusions still need that premise. Arbitrary monotone assignments of elementary objects need not extend to figure maps because their images may fail compatibility. [C-SA21-8-001–032 and the separately identified refinement records.]

Indexed families expose distinctions between a least containing index, partition into interiors, saturation and recovery of the index order. The two infinite constructions on VIII53–54 separate these conditions and were recomputed symbolically. A further warning concerns common-face disjointness: a later comparable-pair formulation is weaker. A five-stratum certificate satisfies the weaker condition and deployment injectivity while violating the stronger common-face clause. Where the source separately requires each deployment to be an actual spatial figure, that requirement may restore the omitted condition; its scope must be checked rather than guessed. [C-SA21-8-018R, 025–026.]

Natural geometric supports do not automatically give the announced faithful realization; the author retracts that assertion in a later margin. Faithful and fully faithful external supports must also be distinguished. The explicit P4 model attached to the later IX discussion separates them and answers the VIII88 question at its exact abstract scope. Boolean behavior inside a single compatible figure does not imply global Booleanity across incompatible figures. [C-SA21-8-033–039; R-SA21-9E-005.]

The interval model uses point strata P_a and proper-interval strata S_ab for a<b in a poset, with a separate face order and open refinement. A flag on n vertices has 2^(n−1) figures, according to the independently selectable adjacent intervals. Some support/shadow equalities require the explicit hypothesis H about extremal elements. On VIII103, the calculation of P_a's perpendicular omits S_ab; its double perpendicular is {P_a}. The separate whole-elementary-figure computation still gives full support and remains a valid counterexample to another asserted identity. The dossier preserves both conclusions. The least closed constructible support is still marked for verification on the page. [C-SA21-8-040–052, especially 045 and 045R.]

### IX. Spatios, corrected correspondences and the final obstacles

The beginning of IX adds formal half intervals and then reverses an initial convention at extremal points. A formal interval can survive even when its ordinary point interior is empty. Compactology is extra structure: the announced Borel–Lebesgue and subdivision-richness conditions are not fully formulated by naming them. At scans 38–41, **atelier** and **magasin exchange roles**: the atelier becomes the primitive stratum structure, while the magasin selects figures. Earlier terminology must be translated with this switch recorded. [C-SA21-9-001–021.]

A spatios is a complete ortholattice, not automatically a Boolean algebra. A disjoncteur is a set with symmetric orthogonality, allowing null elements under the stated self-orthogonality convention. Its support lattice is formed by double-perpendicular closed subsets. For spatial figures, face order is extra data rather than the support-lattice order. The representation at IX58–60 is sound under face closure and join-density: the set of generators whose support lies below a given lattice element recovers that element and its orthocomplement. The dossier gives a direct proof, independently of the subsequently failed unrestricted functoriality argument. [C-SA21-9-022–030; parts/cotes_8_9/proof_audits.md.]

The correction in IX66–104 is decisive. For a raw correspondence α:E→P(F), taking the closure of the union of its values always defines an isotone map on closed supports. It need not preserve joins, and join preservation alone need not recover the values on generators. IX95 inserts the missing equality

\[
 f_\alpha(\operatorname{cl}_E\{x\})=\operatorname{cl}_F(\alpha(x)),
\]

and IX97 explicitly acknowledges that it was added afterward. Together with arbitrary-join preservation, it is equivalent to closure commutation and existence of a pretranspose. The repaired normalized correspondences form the intended category. For a join-preserving f:L→M with right adjoint r, its orthogonal transpose is C_L r C_M. This gives the canonical category's involutive duality without asserting that every arbitrary point map has an adjoint. [C-SA21-9-031–066; parts/cotes_9_09_13/proof_checks.md, P1–P7.]

Two later hopes fail exactly. For the six-element complete ortholattice with four atoms in complementary pairs, its lattice of arbitrary-join-preserving endomorphisms has **234 elements, 40 atoms and 16 coatoms**. An order-reversing bijection would pair atoms with coatoms, so this lattice cannot be a spatios. On the associated four-point orthogonality space, using the coordinatewise OR relation as a reconstruction and leaving the transcription's cross-coordinate indices for scan review, product closure gives **114** closed relations, whereas closed rows and columns give **234**. A three-point diagonal has closed fibers but double-perpendicular closure equal to the whole product. Thus two proposed relation constructions differ. The saved enumeration is accompanied by proofs and matched against Ischi's precise tensor results. [Same appendix, P8–P9; Ischi2010, Theorems 3.4, 3.6 and 4.9.]

The universal factorization as a complement-preserving comorphism followed by a morphism whose transpose preserves complements also fails. A particular join map on that six-element lattice takes the top to a proper atom. Any complement-preserving join map from this lattice into a nontrivial complete ortholattice has zero kernel, forcing its orthogonal transpose to take top to top. Hence no proposed span can give the displayed join map, for any intermediate complete ortholattice; the trivial intermediate object gives the zero map. This is a symbolic obstruction over all intermediates, not a finite search mistaken for a universal proof. No exact external resolution of this particular span formulation was located, so its literature class remains a bounded D even though this run refutes it. [Same appendix, P10.]

The last pages make further distinctions. Boolean behavior of comparable elements expresses orthomodularity, not global Booleanity; finite non-Boolean examples separate the conditions. A lemma on IX121 needs the decomposition premise of the preceding lemma. The proposed transitivity of a refinement relation combined with joint Boolean commensurability fails in an explicit 18-element ortholattice. A faithful external support does not imply the stronger local support condition: private points and pair points realize the P4 relation faithfully while a compatible middle pair retains O6. Bare morphism axioms can also give a non-closed kernel. These certificates check the exact hypotheses and keep alternative morphism conventions separate. The last proposed support criterion depends on an uncertain named-axiom glyph; its counterexample is explicitly conditional on the reading and stated hypotheses. [parts/cotes_9_14_18, claims, proofs and finite_checks_output.json; R-SA21-9E-005.]

## 2. What became of the claims

The exact mathematics has a mixed history. Many order, polarity, topology and adjunction ingredients predate 1986. Several later sources give exact counterparts to particular assertions. The changing native atelier and magasin systems have far fewer exact published matches than their broad resemblance to stratification, topology or quantum logic might suggest. No A-class resolution in Grothendieck's own later published work was established in the recorded search.

| Source and checked locator | Result used and limit | Chronology kept distinct |
|---|---|---|
| [Birkhoff1948](https://math.chapman.edu/~jipsen/summerschool/Birkhoff%201948%20Lattice%20Theory%20Revised%20Edition.pdf), chapter IV §§5–7 | Polarity, Galois closure and completion; does not supply all atelier axioms. | Revised edition 1948, before these pages. |
| [Shmuely1974](https://msp.org/pjm/1974/54-2/pjm-v54-n2-p15-p.pdf), §§1,3,5–6 | Galois maps, closed-fiber relations and completeness of the ordered map collection on complete lattices. | June 1974 publication; receipt date is not asserted to be public circulation. |
| [CoeckeMoore2000](https://arxiv.org/pdf/quant-ph/0008021), §3 | Complete-ortholattice join maps and conjugate adjunction; the separate restrictive orthospace category is not identified with every disjoncteur. | First arXiv circulation 3 August 2000; book publication 2000. |
| [DomenachLeclerc2001](https://link.springer.com/article/10.1023/A:1010662327346), Theorems 4.1 and 5.1 | Biclosed relations for arbitrary closure spaces and Galois pairs; gives an exact correspondence after the stated dualization. | Author preprint dated November 2000; journal March 2001. |
| [Ischi2010](https://link.springer.com/article/10.1007/s00012-011-0108-5), Theorems 3.4,3.6,4.9 | Separates OR-product closure from the maximal closed-fiber product and excludes the requested orthocomplement in an allowed finite case. | Issue December 2010; online 20 January 2011; arXiv 8 September 2011. |
| [PasekaVetterlein2025](https://link.springer.com/article/10.1007/s10773-025-06031-4), arXiv v3, Lemma 2.3, Proposition 2.4 and Lemmas 3.4–3.7 | Exact density/support-reduction and join-dense representation cores; the raw-set categories differ in their treatment of null elements. | First arXiv 8 January 2025; journal 27 May 2025. |
| [Jenča2023](https://arxiv.org/pdf/2206.08113), §4, Lemma 4.1, Theorem 4.12 | Proper-interval orthogonality and flag core; the final equivalence assumes a bounded poset. It omits the extra point strata, half intervals and carrier data. | First arXiv 16 June 2022; journal 2023. |
| [Hua2026](https://hexagonmath.org/pdf/2611.00125v2), §§76–79 | Bounded one-dimensional order reconstruction, the specified rive injection, pair-cut reconstruction and a negative Boolean-support result. | Public November 2026 version; no independent historical influence or journal publication inferred. |

These are mathematical scope matches, not evidence that later authors knew or developed this manuscript. The public 2026 treatment is itself connected to the present archival transcription project; it is not independent evidence about doubtful ink. Its definitions and proof statements were compared with the supplied text. Public Lean files were inspected, not compiled.

The recent poset comparison also needs a version qualification. Jenča's *N-free Posets and Orthomodularity* appeared on 5 February 2026 and has a correction dated 11 August 2026. Its main formulation uses **incomparability**, whereas the late manuscript question uses strict comparability. The checked P4 example is used at its exact scope; no inaccessible corrected theorem is imported. [Jenca2026, Example 2.6; JencaCorrection2026.]

The topological comparisons in the earlier notes were also reopened. McCord's finite-space theorem concerns weak homotopy equivalence. Barmak–Minian compares simple homotopy under specified finite models. Clader's inverse-system construction distinguishes its limit from a further quotient; the 2016 erratum repairs the continuity argument and is included. Ayala–Francis–Rozenblyum's exit-path theorem retains conically smooth stratified homotopy information. These do not identify an unspecified category of network cuts with all compact spaces. [McCord1966; BarmakMinian2008; Clader2009 and Clader2016; AFR2019, Theorem 4.2.5.]

The opened EGA and SGA passages provide precise background, not a hidden completed geometry of forms. EGA I's ring spectrum is distinguished from a relative Stone construction. SGA4 II gives the sheaf equalizer pattern; IV gives specialization and localic/topos comparisons with their actual separation hypotheses. An erroneous T1-to-sobriety aside in the editorial SGA PDF was excluded rather than used. Esquisse §5 provides a real conceptual predecessor for retained attaching spaces and maps, and distinguishes isotopy classes from stronger information about isomorphism spaces. The relevant text circulated in 1984 and was published in 1997; it is not a later solution of the 1986 claims merely because its publication date is later. [EGAI1960; SGA4II; SGA4IV; Esquisse1984.]

### Meaning of the literature classes

**A** would require a matched result in his own later published work. **B** records an exact later established counterpart, including a negative answer where appropriate. **C** identifies the precise developed part and the remaining native hypotheses or construction. **E** records a pre-1986 ingredient, without claiming an earliest historical origin where none was checked. **F** is used when the page does not delimit an identifiable assertion, not simply when a search gives no hit.

**D is a bounded search outcome:** no exact publication was located by the recorded native-vocabulary, translated-mathematics and backward-reference searches. It does not mean that a result is original, remains open, or has never been treated. In particular, an elementary result independently proved here, a false statement refuted here, and a genuine remaining open step can all have D as their literature classification. Their present mathematical statuses are separately stated. Every claim is mapped to executed searches in `SA21_search_map.tsv`; the searches include the named arXiv, Numdam, MathOverflow and zbMATH channels, EGA/SGA and publication inventories. Access failures, including blocked zbMATH and some original older sources, are recorded rather than counted as opened results.

## 3. What the earlier notes got right, and what changes here

The Pro notes are useful precisely where they distinguish definitions from hopes, canceled drafts from live axioms, and geometrical data from the context packet's proposed pro-object interpretation. They correctly flag the unfinished orientation and maille steps, the weak/strong F6 issue, the disconnected-end convention, and the difference between a finite poset, a general category and enriched attaching data. Their explicit examples are labelled as earlier-run ideas and independently checked where used. The Codex notes are leads; they are not silently converted into additional Pro verdict rows.

The Stage1 verdict concerns whether a note reports its source accurately. It does not certify the mathematical truth of everything the note discusses. Consequently a note accurately reporting a false or withdrawn claim is retained, with that claim's actual status in Stage2. Repeated notes about one object or question are merged, while different strengthened versions remain distinguishable in their record.

Three source-entry corrections are explicit. Entry #110's Esquisse reference for the Isom comparison is §5, printed pp29–30, rather than §6. Entries #116 and #119 need the merged-file physical-line convention instead of the original per-page convention. The changes are locational, not alterations of the handwritten text. The other substantive corrections arise from fuller reading across the cotes and from mathematical checks: join-primality replaces the earlier inadequate irreducibility; the VIII singleton perpendicular calculation is corrected without discarding its separate whole-figure example; IX95/97 supplies the missing generator condition; and several universal support or morphism hopes fail in explicitly certified finite systems.

The dossier also corrects its own tentative alarms. Finite-type local directed existence in VI is valid under the actual strong hypotheses. The unusual null-element use of “antireflexive” agrees with the opened Birkhoff convention. A chapter-number error in the first Birkhoff source notes was corrected to chapter IV of the 1948 edition. These changes are recorded as check events; a suspicion is not retained merely because it once appeared in a reading note.

## 4. Problems, reading alarms and other-project links

The problem index contains authorial questions and deferred steps, including some now answered or refuted. It is not a list of claims that mathematics still regards as open. Repeated questions are merged across axiom versions, with the distinct formulations retained. Each record separates the strongest supported authorial formulation from a plausible present formulation. Where no source explains why a project was abandoned, the dossier says so; possible mathematical reasons are labelled as inference.

The most consequential remaining native tasks concern coherent network orientation, the final equal-endpoint argument, a fully specified topological realization and cutting category, regularity of spectral cuts and maille symmetry, a consolidated final two-order axiom system, exact local support hypotheses, and morphisms that preserve the required figure and support structures. Compactology, the full constructible-closure assertion and the proposed two-dimensional maquette equivalence remain separately delimited. A broad analogy with toposes or exit paths is insufficient to settle them.

Reading alarms are prioritized by mathematical dependence. High-impact cases include a missing nonempty or compatibility hypothesis, an open/closed or complement sign, a switched order, a free variable, a union/intersection error and the scope of a later margin. Alternatives are mathematical suggestions only. An incorrect formula can be a manuscript error, a transcription error or an insufficiently specified convention; no scan-free argument decides which. The output preserves the original reading in every case.

The other-project audit covers **all 125 Context paragraphs** and identifies **54 targets**. Two recovered neighboring context archives supply **20 located textual endpoints**: eleven full return rows, six selected excerpts, one exact run-summary entry, one complete earlier note and one reproduced manuscript passage. Two more targets are indirect ID mentions; thirty exact targets are absent; the two original package48 context-file versions were not recovered. A return row headed “Proved” is still a report from an earlier run, not a proof newly verified here. The separately recovered *Les Dérivateurs* XVI passage supports a thematic comparison with finite posets and simple homotopy, not an equivalence for SA21 cuts. [parts/project_links/narrative.md; SA21_project_leads.tsv.]

For note #118, seven exact rows or excerpts and the P3c-general run-summary endpoint were recovered; RESIDUE E.6 was not. Their old Open labels do not establish present worldwide status. Register section numbers count both second- and third-level headings, while stable source-note IDs count the specified third-level entries; this explains several apparent numbering discrepancies. Missing links remain in the explicit audit tables. They are neither erased nor listed as checked mathematical connections.

## 5. Research directions and what this consolidation does not develop

`SA21_directions.md` ranks separate next tasks by interest and realistic progress in a few hours. Each gives its source item, claim and problem IDs, the intended conclusion, known constraints and a concrete first step. The highest priorities are a stable formulation of the final spatial axioms, the exact missing hypotheses for local support complements, and the corrected correspondence/morphism calculus. Network orientation, equal-endpoint coherence, spectral-cut regularity, cutting categories, interval calculus, subdivision extension, infinite figures and the two-dimensional maquette question follow at their stated scope.

The completed finite examples in this dossier check or refute claims already on the pages. They are not an attempt to develop those new research directions. A future task should start from the corrected statement and specified axiom version, rather than treating the whole manuscript as one uniform system. The archive preserves enough proof and computation detail to reuse a certificate without inheriting a broader conclusion it does not establish.

## 6. Verification, reproducibility and accounting

The event ledger separates targeted proof checks, independent reproofs, finite computations, results used and rechecked, background carried without a new proof, and refutations with a refined-statement pointer. A text comparison is explicitly labelled as such. Reading a proof on a page is not described as independently proving it. A checked URL establishes access and bibliographic identity; the exact theorem checked and its scope are specified separately. Unopened original references are marked `unverified`, even where a later primary paper cites them.

Finite countermodels retain their complete input structures, axiom checks, numerical outputs and independent arguments. Symbolic arguments handle assertions beyond finite enumeration, including all-intermediate span obstruction and the infinite indexed-family examples. Public formal code was inspected only where stated; there is no claim of a Lean build. The root proof appendix also received a separate targeted review. The bundled programs perform mathematics or assemble already authored decisions; no note verdict was generated by heading or keyword matching.

The final archive excludes the user's original attachments, recovered context input archives, downloaded full publications and earlier checkpoint ZIPs. Source hashes, exact URLs, executed query metadata, curated passages and comparisons, programs and their outputs remain. See `README.md` for input restoration and reproduction. The checkpoint and final packaging manifests distinguish included work from excluded inputs.

### Final counts

The following counts are generated from the final principal tables. Claim records group linked assertions and include explicitly labelled definitions/constructions and current-run refinements. They are not a count of independently proved theorems. The status category gives a primary counting label; the full source history and hypotheses remain in each record. Separate R-SA21 proof/refinement anchors are outside those claim counts; `audit/proof_anchor_index.tsv` locates them, including the twelve structured refinements of the final IX block. They are not extra assertions attributed to the manuscript.

| Measure | Count |
|---|---|
| Indexed source entries | 122 |
| Consolidated items | 97 |
| Claim records | 446 |
| Manuscript claim/construction records | 437 |
| Separately labelled C-record refinements | 9 |
| Named R-proof/refinement anchors | 43 |
| Merged problem records | 124 |
| Reading alarms | 216 |
| Ranked research directions | 17 |
| Verified folder/publication links | 182 |
| Unresolved folder/publication links | 11 |
| Separate other-project targets | 54 |
| Bibliographic records | 64 |
| Check-event rows | 902 |

#### Source-entry verdicts

| Verdict | Entries |
|---|---|
| kept | 94 |
| merged | 25 |
| corrected | 3 |
| withdrawn | 0 |
| rests on a misreading | 0 |

#### Item kinds and source verdicts

| Consolidated item kind | Items | Kept entries | Merged entries | Corrected entries |
|---|---|---|---|---|
| conjecture | 1 | 1 | 0 | 0 |
| idea of the earlier run | 17 | 16 | 2 | 1 |
| other | 15 | 14 | 6 | 1 |
| reading question | 9 | 9 | 1 | 0 |
| self-flagged step | 6 | 6 | 1 | 0 |
| title, date or page count | 2 | 1 | 0 | 1 |
| unproved claim | 31 | 31 | 11 | 0 |
| unpursued implication | 9 | 9 | 1 | 0 |
| withdrawn in the same text | 7 | 7 | 3 | 0 |

#### Claims by literature class

| Class | Records |
|---|---|
| A | 0 |
| B | 14 |
| C | 29 |
| D | 308 |
| E | 89 |
| F | 6 |

#### Claims by primary source/check status

| Status | Records |
|---|---|
| proved there | 82 |
| proof sketched | 107 |
| stated without proof | 82 |
| corrected by himself later | 54 |
| false as stated | 17 |
| open on the pages | 55 |
| definition/construction | 40 |
| current-run refinement | 9 |

#### Claims by cote

| Cote | Records |
|---|---|
| 156-1 | 34 |
| 156-2 | 46 |
| 156-3 | 27 |
| 156-4 | 43 |
| 156-5 | 29 |
| 156-6 | 44 |
| 156-7 | 52 |
| 156-8 | 56 |
| 156-9 | 115 |

The class, source-status and item-verdict totals answer different questions. A class D record can have a complete independent proof or counterexample here; a retained note can accurately report a false assertion; and a question in the problem index can have been resolved later in the manuscript. The tables and check events preserve those distinctions.
