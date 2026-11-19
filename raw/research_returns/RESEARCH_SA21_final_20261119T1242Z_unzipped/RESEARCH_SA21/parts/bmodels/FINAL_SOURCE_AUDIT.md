# Final source-access and reading audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. Consolidated by /root/bmodels from the root's RESEARCH_SA21_references.bib and the per-agent reading, source and audit records. This inventory covers all **27 deduplicated bibliography entries**, plus the specifically requested Foulis–Holland theorem and the unverified Carmona search lead. It does not claim that the consolidating agent personally opened every source opened elsewhere in the team.

## Status conventions and limitations

**Primary text opened** means that the original mathematical text was available and the precise passages identified below were inspected. It does not mean that an entire book or every manuscript page was read. A publisher's original article reproduced in a mirror is distinguished from publisher-hosted access. **Metadata/contents only** means that bibliographic or table-of-contents information was opened, but the theorem text was not. **Not opened in full** means that retrieval failed or the source remained unavailable. Such a source supplies no uninspected theorem premise.

The bibliography records these distinctions individually. The actual proofs use the opened inputs listed below or give direct derivations; a failed download is not counted as an opened theorem. The downloaded arXiv source versions, the later journal bibliographic years, and the original manuscript's scan numbering are kept distinct. No priority claim is made.

## 1. Original manuscript and attached research material

### Grothendieck1986 — Grothendieck, A. (1986), Vers une géométrie des formes, cote 156

**Access:** supplied AI transcriptions, study files, correction tables and check-event registers were opened. The official Montpellier archive catalogue was opened. Original PDF images were inspected at the particular source-sensitive passages listed below. Reading a transcription is not reported as independent inspection of its ink.

**Original images inspected by the team:**

- **156-4/54–55:** equality-based complete join irreducibility and the following join-to-union assertion. The entire official 156-4 PDF was downloaded, 89 PDF pages and 37,603,160 bytes. These are PDF scan pages54–55, handwritten/printed pages53–54.
- **156-4/72–73:** unrestricted uniqueness in C6(a), its separately added stratum formula(b), and C7_0 extension. The high-resolution crop of scan72 was inspected independently by two agents.
- **156-6/12:** formula(1.20), whose two inequalities explicitly define bounded-join primality. The axioms agent rendered and inspected the original page during the final source-history audit.
- **156-6/34:** the shortened final At-star list's canonical-subfigure clause. Its relation to the longer membership clause on scan32 is kept explicit.
- **156-6/88:** the mixed-incidence variable eta ranges over all of F-prime in the ink. The literal condition and the exterior-variable replacement are treated separately.
- **156-8/4 and6:** the signed incidence, reversal and dimension-one clauses used for the maquette analysis. The unresolved source-only sign is not silently normalized; the mathematical readings are branched.
- **156-8/31:** the comparable-pair Mag4-prime clause. A preceding glyph is visible but its identification as a negation remains uncertain; both readings are analyzed and have finite certificates.
- **156-9/113:** the ten-element support example, including the set predicate and the overwritten diagram. The reconstruction is checked against the formula. A literal three-element-subset reading of the apparent superscript is separately shown not to give the announced lattice.

**Source conventions:** manuscript locators in the paper use PDF scan numbers, not handwritten page numbers. The records name exact attached transcription filenames and line ranges. Selected full PDFs and rendered images are retained outside the deliverable work tree, in SA21_sources. No claim is made to have re-inspected every original image of cote156.

### Final irreducibility/primality chronology — supersedes an earlier audit inference

This distinction materially changes which counterexamples apply.

| Source | Explicit definition | Final consequence |
|---|---|---|
| J156-4-07_transcription.tex:100, scan54 | X=Sup(F_i) implies some F_i=X | Equality-based complete join irreducibility. The six-element literal contrée counterexample applies; bounded-join primality/local distributivity is the exact missing representation hypothesis. |
| J156-6-02_transcription.tex:77–84, scan12, formula(1.20) | X≤Sup(F_i) implies some X≤F_i | Bounded-join primality is explicitly part of the actual156-6 convention. The deployment-union argument SA21-R6-12 is valid. M3 is not a model of the full actual156-6 system including(1.20). |
| J156-8-03_transcription.tex:106–112, scan20 | X=Sup(F_i) implies some F_i=X | The independent atlas list explicitly returns to equality-based irreducibility. Its literal M3 obstruction remains valid. This equality was independently checked in the supplied transcription; no unrecorded original-image inspection is claimed. |

The prior bmodels attempt to refute SA21-R6-12 by carrying the156-4 definition into156-6 was incorrect and is **withdrawn**. CORRECTIONS.tsv entries K10–K12 now uphold the original156-6 result and record the source distinction. Earlier CHECK_EVENTS rows retain an explicit superseded status and the correct final conclusion. New entries K29–K30 record the chronological definitions. The B.3 six-element156-4 result and its exact representation theorem are unchanged.

The manuscript's two meanings of open support are likewise distinguished: the scan87 polar-intersection definition, the scan90 refinement/boundary-disjointness definition, and the open-lieu representatives are compared in the proof of A16(d). Old whole-figure disjunction is not silently identified with modern internal disjunction.

## 2. Orthogonality, ordered sets and lattice theory

| Bibliography key and source | Access and exact passages inspected | What is used, and what is not inferred |
|---|---|---|
| **Jenca2022** — Jenča, G., Orthogonality spaces associated with posets; opened arXiv:2206.08113v1 (2022), journal record Order40(2023),575–588 | **Primary text opened:** full arXiv PDF and LaTeX source. Proposition2.3; Theorem3.3, p.5; proper quotients in §4, p.6; Lemma4.3, Corollaries4.4–4.5, p.8; Theorem4.10, p.10. DOI10.1007/s11083-022-09623-5. | Dacey's basis criterion and the finite bounded quotient-space theorem are used with their hypotheses retained. The split-poset comparison and the extension to finite conditional lattices are proved explicitly. Locators and the correction to Corollary4.5 refer to the opened2022 version, not an uninspected claim about every later version. |
| **PasekaVetterlein2022** — Paseka, J., & Vetterlein, T., Categories of orthogonality spaces, JPAA226(3),106859 | **Primary text opened:** full arXiv:2003.03313v2(2020) PDF and LaTeX source; journal metadata. Definition2.4, Lemmas2.5 and2.11, Proposition2.14, Example2.15, Definition3.1 and Theorem3.7. DOI10.1016/j.jpaa.2021.106859. | Normality, the Dacey basis criterion, their strict distinction, and the restrictions on normal homomorphisms are checked. The manuscript's closed-valued correspondences are proved to be complete-join morphisms directly; they are not equated with arbitrary orthogonality-preserving point functions. |
| **Sumner1974** — Sumner, D. P., Dacey graphs, J. Austral. Math. Soc.18(4),492–502 | **Primary text opened:** full original publisher PDF, especially the definition on p.492. DOI10.1017/S1446788700029232. | The source explicitly concerns finite graphs and the maximal-clique two-neighbourhood condition. This is the finite normality condition, not the stronger basis-spanning condition for every closed subset. |
| **Greechie1966** — Greechie, R. J., Orthomodular lattices, University of Florida dissertation | **Primary text opened:** original dissertation PDF. Proposition1.2.7 and Theorem1.2.8, printed p.14; Corollary1.2.9, pp.14–15. | This supplies an opened statement of the Foulis–Holland commuting-element theorem and its surrounding calculus. The paper proves the orthogonal-family formula directly from the orthomodular law, including its infinite-family application. |
| **Dacey1968** — Dacey, J. C., Jr., Orthomodular spaces, University of Massachusetts Amherst dissertation | **Full thesis not opened:** exact-title and repository searches did not retrieve it. Bibliographic identity was checked in opened primary papers. | The author's initials are J.C., not the prompt's J.R. The basis theorem is taken from the opened Jenča and Paseka–Vetterlein statements and is proved in the paper. No thesis page number or uninspected original proof is asserted. |
| **Kalmbach1983** — Kalmbach, G., Orthomodular lattices, LMS Monographs18 | **Metadata/preview only:** catalogue and preview metadata opened; full mathematical text not retrieved. | No theorem is invoked solely from this book. |
| **Beran1985** — Beran, L., Orthomodular lattices: Algebraic approach | **Metadata/contents only:** official publisher page and contents opened; full text requires subscription. DOI10.1007/978-94-009-5215-7. | No theorem is invoked solely from this book. |
| **Foulis1962** — Foulis, D. J., A note on orthomodular lattices, Portugaliae Mathematica21,65–72 | **Original full text not opened.** Theorem5, p.68, is the locator reported in the opened Greechie dissertation. | This reported locator is not presented as independent inspection of Foulis's original article. The Foulis–Holland input is available in opened Greechie and the needed orthogonal-family statement is proved directly. |
| **FoulisRandall1972** — Foulis, D. J., & Randall, C. H., Operational statistics.I.Basic concepts, J.Math.Phys.13,1667–1675 | **Original full text not opened:** publisher DOI retrieval was unavailable; metadata was cross-checked in opened primary papers. DOI10.1063/1.1665890. | Historical comparison only. The orthoset construction and morphism distinctions used here have direct proofs and the opened Paseka–Vetterlein comparison. |
| **Gallai1967** — Gallai, T., Transitiv orientierbare Graphen, Acta Math.Acad.Sci.Hungar.18,25–66 | **Metadata/references only:** official publisher page opened; full text unavailable without subscription. DOI10.1007/BF02020961. | No uninspected Gallai theorem is a premise of the order-graph classification. |
| **Corneil1981** — Corneil, D. G., Lerchs, H., & Stewart Burlingham, L., Complement reducible graphs, Discrete Appl.Math.3(3),163–174 | **Metadata only:** original publisher full-text endpoint returned403. DOI10.1016/0166-218X(81)90013-5. A search hit named cographs.pdf was inspected and identified as2009 lecture slides, not this article. | The recursive cograph argument is proved directly; the unrelated slides are not treated as the primary paper. |
| **Roman2002** — Román, L., Orthomodular lattices and quantales, arXiv:math/0211133 | **Primary source opened:** the LaTeX source supplied with the task. | Used as context for Sasaki-projection and quantale constructions under orthomodularity. The existence of an ortholattice is not used as a substitute for the orthomodular hypothesis. |

**Foulis–Holland source status:** the theorem is covered above even though it is a named theorem rather than a separate bibliography entry in the prompt. The original Foulis article was not opened and no separate original Holland article is recorded as opened. The inspected Greechie statement is the actual source-access basis; the application needed here has a direct proof.

### Sumner normality is not Dacey orthomodularity

The shared word Dacey names different conditions in these sources. Sumner's finite-graph condition tests a maximal clique covered by the union of two neighbourhoods. Paseka–Vetterlein's normality gives the corresponding Boolean behaviour of finite orthogonal families. Dacey's orthomodularity criterion instead requires **every maximal orthogonal subset of every orthoclosed set to generate that closed set**. The latter is the criterion used to characterize orthomodularity.

The distinction is proved, not inferred from terminology: the paper's eight-element interval orthoset is a comparability graph satisfying the Sumner condition while its twenty-element support lattice fails orthomodularity. The program verifies the finite example. For infinite orthosets, the paper explicitly separates the published finite-family normality convention from its own unrestricted family statement, and proves the latter where asserted.

### Qualification of the opened Jenča version

The opened2022 arXiv version's Corollary4.5, p.8, states a singleton double-polar formula without a boundedness condition. Two disjoint two-element chains refute that unrestricted assertion: the quotient space has two nonorthogonal elements, so either singleton closes to both, although its quotient-order ideal is a singleton. The paper proves the bounded replacement using the quotients from the global bottom or to the global top.

The use of Theorem4.10 retains **finite bounded lattice** hypotheses. The paper then proves the comparison for every split poset and derives the finite conditional-lattice classification by explicit trace-block arguments. It does not assume that orthomodularity passes to arbitrary induced subspaces. It does not extrapolate the finite conditional-lattice characterization to all infinite posets. The citation key Jenca2022 names the opened preprint; the bibliography separately records the2023 journal publication.

## 3. Event structures and the definable geometric model

| Bibliography key and source | Access and exact passages inspected | Derivation and scope |
|---|---|---|
| **Birkhoff1948** — Birkhoff, G., Lattice Theory, revised edition, AMS Colloquium Publications25 | **Primary text opened:** full scanned book downloaded. ChapterIX, §4, Lemma1 and Theorem5, printed p.139, visually inspected at PDF p.157. | Finite distributive representation and irreducible-to-prime implication. The paper proves the required principal-ideal version and the exact equivalence with bounded-join primality. |
| **NPW1981** — Nielsen, M., Plotkin, G., & Winskel, G., Petri nets,event structures and domains,partI, TCS13(1),85–108 | **Primary text opened:** author-hosted full PDF. Definition14, pp.99–100; Definitions17–18 and Theorems8–9, p.102, checked against images. DOI10.1016/0304-3975(81)90112-2. | Binary event causality/conflict and configuration domains. Finite causes are imposed explicitly for this application's finite deployments. Finite configurations are distinguished from their directed-complete ideal completion. |
| **Winskel1987** — Winskel, G., Event structures, LNCS255,325–392 | **Primary text opened:** author-hosted full PDF and official publisher metadata. Definition1.3.4 and Theorems1.3.5–1.3.7, pp.335–336; Definition3.4.6, p.378; Definition2.5.1 and Proposition2.5.2, p.355. DOI10.1007/3-540-17906-2_31. | The higher-consistency definition is separated from binary conflict. A three-event ternary-consistency certificate proves why C3 requires the binary subclass. Refinement is not silently identified with an event-structure morphism or recovered from the configuration poset alone. |
| **Coste1999** — Coste, M., An Introduction to o-minimal Geometry, author lecture notes | **Primary text opened:** full author-PDF text in the web reader, including the relevant statements and proofs. Fresh direct downloads intermittently timed out or returned503. §1.3, pp.9–10; Theorem3.4, pp.26–27; Proposition3.7 and Theorem3.9, p.28; Theorem3.22, pp.34–35; Theorem4.4, §4.3, p.42, proof pp.42–44. | These are the actual geometric inputs: arbitrary real closed fields, closed/bounded images, local closedness, definable connected components and paths, frontier dimension, and compatible triangulation. The proofs explain the compactification and relative-closure steps, then derive moderation and connectedness in the specified model. |
| **vandenDries1998** — van den Dries, L., Tame Topology and o-minimal Structures, LMS Lecture Note Series248 | **Metadata/contents only:** official chapter metadata and contents opened. Full linked PDF retrieval timed out or returned503. Chapter8, §2, Theorem2.9 locator was cross-checked in a Regensburg seminar bibliography, not inspected in the book itself. DOI10.1017/CBO9780511525919. | No theorem is accepted solely from the inaccessible page. Opened Coste Theorem4.4 supplies the triangulation input. |
| **Shiota1997** — Shiota, M., Geometry of Subanalytic and Semialgebraic Sets, Progress in Mathematics150 | **Metadata/contents only:** official publisher page and table of contents opened. ChapterII, §2 starts at p.116; ChapterIII, pp.270–304, concerns the Hauptvermutung. DOI10.1007/978-1-4612-2008-4. | No Hauptvermutung is invoked. Explicit extension and compatible definable triangulation suffice for the generalized-cell atelier, with their distinct roles proved. |
| **PillaySteinhorn1986** — Pillay, A., & Steinhorn, C., Definable sets in ordered structures.I, Trans.AMS295(2),565–592 | **Original full text not opened:** official AMS PDF returned403; bibliographic data confirmed in the author's publication list. DOI10.1090/S0002-9947-1986-0833697-X. | No theorem from this inaccessible paper is used as a proof premise. The requested source is explicitly recorded rather than silently omitted. |

The event-structure derivation is exact: equality-irreducible literal156-4 systems need the additional equivalent local-distributivity/prime condition; the whole representable subclass is then identified with binary-conflict prime event structures having finite causes. The geometric proof fixes a single ambient definable X, closed supports, finite frontier partitions and generalized cells. It does not assert that every informal meaning of cells or stratifications yields the same axiom table.

## 4. Maquettes, face posets and comparison maps

| Bibliography key and source | Access and exact passages inspected | Derivation and scope |
|---|---|---|
| **Bjorner1984** — Björner, A., Posets,Regular CW Complexes and Bruhat Order, European J.Combin.5(1),7–16 | **Primary text opened:** original publisher text reproduced in a public mirror. Definition2.1,p.8; §2.3,pp.8–9; Proposition3.1,p.11. The CORE PDF endpoint returned403. DOI10.1016/S0195-6698(84)80012-8. | The correct spherical lower-interval criterion and the local-Boolean/global-meet simplicial criterion are used at their stated scope. The paper gives the explicit reconstruction and orientation comparison; diamonds or connected links alone are not promoted to spheres. |
| **McCord1966** — McCord, M. C., Singular Homology Groups and Homotopy Groups of Finite Topological Spaces, Duke Math.J.33(3),465–474 | **Primary text opened:** original article PDF through an academic mirror. Theorem2,p.466; Theorem6,p.467; §5,pp.469–470. DOI10.1215/S0012-7094-66-03352-7. | The weak equivalence from an order complex to its Alexandrov poset is used with its explicit map and local preimage verification. It is not relabelled a homeomorphism or an unrestricted homotopy equivalence. |
| **Barmak2011** — Barmak, J. A., Algebraic Topology of Finite Topological Spaces and Applications, LNM2032 | **Primary text opened:** original book PDF through an academic mirror. Proposition1.2.4,p.5; Theorem1.4.6,p.12; Remark1.4.16,p.15; §7.1,pp.93–98. DOI10.1007/978-3-642-22003-6. | Finite-space/order connectedness and order-complex comparison are checked. The arbitrary-family connectedness argument is proved separately, including residual fibers; the finite proposition is not cited as an infinite theorem. |
| **Serre1977** — Serre, J.-P., Arbres,amalgames,SL2, Astérisque46 | **Primary text opened:** full original Numdam PDF, not only a publisher sample. ChapterI,§2.1,Definition1,p.22. | The graph convention with oriented edges and reversal is compared directly with the dimension-one axioms. The Numdam identifier contains1983, while the inspected volume/copyright gives1977; the bibliography uses1977. |
| **Hersh2014** — Hersh, P., CW Posets after the Poincaré Conjecture, arXiv:1411.1296v1 | **Primary text opened:** arXiv HTML. Definition1.1 and Theorems1.2 and2.2. The source archive was returned as an unsupported gzip by the web retriever. | Context only. No theorem in PartC depends on this source; it is not counted as a successfully downloaded LaTeX source. |

The lower-interval topology, local finiteness, sign conventions, and distinction between finite cycles and possible infinite paths are stated in the proofs. Source-defined polyhedral or predecessor conditions are not assumed to characterize simplices.

## 5. Prior attention, project attribution and search limits

| Bibliography key or lead | What was actually opened | Permitted conclusion |
|---|---|---|
| **Malgoire2002** — Malgoire, J., Vers une géométrie des formes(topologiques), présentation introductive à un manuscrit inédit(juin-juillet86)d'Alexandre Grothendieck; Montpellier seminar,3October2002 | **Complete official notice and abstract opened:** https://imag.umontpellier.fr/?idseance=509&page_id=526 | Establishes prior mathematical attention specifically to this manuscript. The notice alone does not establish a published article or a solution to the exact questions in this report. |
| **HuaProject** — Michel Hua's project, Grothendieck Project | **Landing page/repository description opened:** https://github.com/Commutator-IO/grothendieck-project . Individual modernized readings were not adopted as theorem proof sources. | The attached156-8 reading attributes the Serre-graph identification and signed-boundary observation to this project; that credit is retained explicitly. No passage or theorem from an unread individual project file is represented as checked. |
| Mateo Carmona2025 slides, search lead only | **Not counted as opened.** No surviving successful-open record was found in the root's source register. | No mathematical statement or historical conclusion relies on these slides. They are not an additional bibliography entry or verified evidence of a particular theorem. |

Searches included the exact manuscript title and combinations of Grothendieck/cote156 with orthomodularity, Dacey graphs, event structures, o-minimal cells, At14, At9Sigma, multistrates and connectedness, plus regular CW and prime-event comparisons. These searches are not a proof of absence of prior work. The official2002 seminar rules out any claim that this manuscript received no prior mathematical attention. No claim of novelty or priority is made.

## 6. Completeness of the requested-source status audit

Every original requested item has an explicit status above:

- Kalmbach, Beran and the Foulis–Holland theorem;
- Nielsen–Plotkin–Winskel and Winskel;
- McCord, Björner and Barmak;
- van den Dries, Shiota and Pillay–Steinhorn;
- Gallai and Corneil–Lerchs–Stewart Burlingham;
- Serre;
- Foulis–Randall and Dacey.

The additional opened inputs Birkhoff, Coste, Jenča, Paseka–Vetterlein and Greechie identify the actual statements used where requested full texts were unavailable or different formulations were necessary. Román's supplied source and Hersh's opened contextual text are labelled with their limited roles. Malgoire and Hua are recorded at the level actually inspected. The source-access limitations do not conceal an unproved mathematical premise: the needed replacements and transfer arguments are proved in the paper.

