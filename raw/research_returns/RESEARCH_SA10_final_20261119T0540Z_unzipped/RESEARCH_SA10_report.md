| Item | Outcome | Statements | Exact conclusion |
|---|---|---|---|
| A.1 | Refuted; corrected gluing theorem proved | A1.1–A1.5 | Successor stones and even all manuscript pair/triple stones fail. Synchronized actual open intersections give the pro-topos bicolimit. Arity minimality and the exact honest-open deletion criterion are proved. |
| A.2 | Refuted as posed; exact criterion proved | A2.1–A2.3 | Neighborhood pullback is governed by cofinality; closed continuous maps suffice. Open immersions fail. Honest open-cover descent is local, while recomputed germ formation need not commute with open restriction. |
| A.3 | Refuted; precise comparison proved | A3.1–A3.2 | Closed-crible restriction preserves retained stones; deleting a crible can change their homotopy type. Constructible restriction has fully faithful extension by empty and is an equivalence exactly when the removed part is empty. |
| A.4 | Corollary refuted; reconstruction, repair and classification proved | A4.1–A4.5 | The given closed-stratum reconstruction is valid. Arbitrary finite meet diagrams need the exact no-identification condition; cartesian intersections suffice. The stable-graph conditional-meet cases are completely classified. |
| B.1 | Unrestricted formula refuted; exact equivalence criterion proved | B1.1–B1.5 | Closed–open recollement is unconditional. Uniform pro-tube systems require precisely the stated local-system extension and morphism conditions; compact conical bundles satisfy them, infinite-stalk germs need not. |
| B.2 | Ordinary-topos principle refuted; higher replacement proved | B2.1–B2.4 | Shape preserves colimits of infinity-topoi. Actual full open-cover diagrams satisfy higher descent. The ordinary bicategorical principle fails, and the two-stratum geometric homotopy pushout is proved with tameness. |
| B.3 | Proved with explicit hypotheses and truncations | B3.1–B3.3 | Constructible groupoid stacks are functors from the exit 2-category under the written exodromy hypotheses; all finite truncation levels and finite-stratum induction are given. The banded-gerbe gauge calculation gives H²(S²,A)=A. |
| B.4 | Claimed obstruction refuted; full assembly data determined | B4.1–B4.3 | A full coherent groupoid span of aspherical pieces already determines its pushout. General assembly uses the coherent spatial flag diagram, with an exact groupoid reduction when pairwise incidence links are 1-types. |
| B.5 | Proposed weaker conditions refuted; exact typed criteria proved | B5.1–B5.10 | Full ordinary Hyp is flatness. Forest tests fail. Verdier and symmetric comparisons, every matching degree, exact arbitrary-index local filling, and original Artin–Mazur comparison are settled with hypercompletion explicit. |
| B.6 | Global presentation refuted; complete replacement and low-degree answer proved | B6.1–B6.3 | The global relation list remains incomplete after both boxes. A complete translated presentation is given. The corrected three-object list presents all 56 maps; both readings of the doubtful final subscript are settled. |
| C.1 | Weak implication refuted; construction and corrected Exit theorem proved | C1.01–C1.04; C1.B1–C1.B3, including C1.B2a | Three transition families give the full simultaneous-cone colimit. Fibrancy gives a complete Segal object in spaces; recursive controlled bundles give the geometric Exit equivalence. Moduli incidence uses all chain-isomorphism groupoids and atlas descent. |
| C.2 | Bare equivalence refuted; exact controlled replacement derived | C2.01–C2.05 | Bare intersection axioms miss projection control unless the displayed commutative diagram is included. One level does not supply radial control. Full compatible radial collar germs and iterated fibrations give the precise smooth resolution equivalence. |
| C.3 | Manifold identification refuted; exact resolution criterion proved | C3.01–C3.04 | Literal finite recursive §8 data retain transverse collars and yield precylindricity. The exact additional manifold condition is regular manifold open faces. Flags index face chains; incidence categories retain branches and automorphisms. Coarse moduli remain singular in an explicit genus-four interior example. |
| C.4 | Germ, holink and spectral statements proved at exact scope; HSS-to-cone claim refuted | C4.01–C4.06 | Finite metric Quinn HSS give the stated pro-homotopy comparisons. Controlled proper collars give V_d≃Σ_d. The spectral sequence is actual sheaf descent. Normal crossings yield the canonical homotopy class of (294). |
| C.5 | Every listed TOP/PL/smooth reading proved or refuted | C5.01–C5.08 | The full margin matrix distinguishes raw Hurewicz fibrancy from regular bundles/submersions and full face-product triviality. Compact TOP and PL/smooth Hurewicz counterexamples, the component counterexample, and corrected category theorems are supplied. |
| L1 | Refuted; corrected theorem proved | A1.2–A1.5 | All raw pair/triple stones still lose an actual overlap, even with connected Whitney/conically smooth strata. Unzipping retains the additional incidence data. |
| L2 | Refuted as stated; corrected theorem proved | B2.1–B2.3 | Holink fibrancy alone omits tameness; ordinary-topos bicolimits do not obey the proposed shape principle. The precise higher and tame geometric statements are proved. |
| L3 | Proved after hypotheses and level correction | B3.1–B3.3 | Sets see π₀ of exit mapping spaces; groupoid stacks see π₁; general n-truncated targets use h_(n+1)Exit. Gerbes form the specified banded subproblem. |
| L4 | Proved with exact classification | A4.4–A4.5 | Conditional meets hold precisely for g=0,n≥3; g=1,1≤n≤3; and (g,n)=(2,0). A literal all-pairs meet statement also needs the empty-bottom convention. |

# RESEARCH_SA10 final research report

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**, 19 November 2026. Effort is not separately exposed by the execution interface. No priority is claimed, and none of this run's writing or calculations is attributed to a human author. All nineteen requested items and leads are settled by the statements above; there is no open mathematical gate in the delivered paper. The retained paleographic uncertainty on 151/005 is explicitly answered under both readings.

The paper contains 74 numbered statements. Its proofs, exact hypotheses and corrections govern the claims. The program certificates cover only their stated finite scopes; this package is not a machine-checked formalization. Earlier working notes are retained as process evidence, and may describe gates that the final paper subsequently closes.

## 1. Main conclusion: what glues the tubes

The ordinary inverse limit of the neighborhood topoi is the wrong object for retaining a tube. For a closed subset of a regular Hausdorff space, that limit is the subspace topos, and the punctured part is empty (A1.1). We retain neighborhoods as pro-objects and give the exact category in which the gluing statement lives.

For the manuscript axioms a–d, let R_i^ord be the union of X_k over indices with i not≤k. Choose, simultaneously for all i, an open neighborhood N_i of X_i and put W_i=N_i minus R_i^ord. Local finiteness makes R_i^ord closed, and the least-index argument makes the W_i an open cover. At a fixed neighborhood stage, ordinary descent gives Sh(X) from the disjoint unions of the W_i, their pairwise intersections and their triple intersections, including the descent maps. Synchronize the neighborhood choices before forming the pro-objects. The finite bicategorical descent limit then commutes with the filtered change of stage. This proves the constant pro-topos cSh(X) is the bicolimit in 2-Pro(Topos) (A1.2). The proof works for infinite locally finite index families because every degree is one synchronized coproduct; it never moves an infinite product across a filtered colimit.

The failure of the manuscript diagram is stronger than the successor failure. For 0⊂R⊂C, compatible sheaves on every named pair/triple stone can choose different maps from a ray into the upper half-plane on two stones. The named pieces do not contain the actual overlap on which those maps must agree. The finite certificate checks all fourteen nonidentity inclusions among nine distinct stones. A connected-stratum version uses 0⊂R²⊂R⁴. Thus Thom–Mather, Whitney and conically smooth hypotheses do not repair this particular diagram (A1.3).

The minimality statement has two precise forms. Universally, the vertex, pair and triple slots of the subset-indexed ordinary descent diagram are each necessary in some example; higher arities are unnecessary for this ordinary bicategorical question (A1.4). For a specified honest open diagram on a T1 space, one can decide exactly whether deletion preserves descent: the groupoidification of every point's membership category must be terminal (A1.5). It would be false to demand that every redundant named stone be indispensable in every cover. Soul objects may be redundant, and repeated simplicial indices are not separate universal necessities.

The higher homotopy statement uses the full Čech diagram and infinity-topoi (B2.1). Truncating to degree two retains precisely the ordinary sheaf gluing information and does not establish higher shape descent. SGA4 IV9.5.4 instead describes the two-stratum noninvertible specialization arrow; AFT unzipping retains actual collar and incidence overlaps. Neither theorem identifies the failed manuscript all-pair diagram with the corrected one.

## 2. Further conclusions and their boundaries

**Base change and cribles.** Closed continuous maps satisfy the exact neighborhood-cofinality criterion, which in particular proves the usual proper locally compact Hausdorff case. Open immersion does not suffice: removing the tube's center leaves a nontrivial deleted germ on the pullback side and an empty-center neighborhood system on the other. The original scan 151/071 actually inserts “mais pas”; the positive open-immersion assertion in the attached study and task is a reading error. Support-containment definitions of R must also be replaced by the order-defined form when strata become empty or coincide. Closed-crible restriction is valid; deleted-crible restriction can change a circle-shaped tube into two components. The exact constructible-sheaf comparison is given in A3.2.

**Finite meets and moduli.** The reconstruction of an already given locally finite closed stratification is valid. The separate finite-diagram corollary is false without a condition preventing zigzags from identifying distinct points of one member; the finite counterexample has seven indices, nineteen input points and a two-point colimit. The complete stable-graph classification is proved by a genus-zero split argument, explicit infinite negative families, and exhaustive proofs for the four positive small genera. A second enumeration uses direct bounded multigraphs rather than inverse contractions and agrees in all positive cases. The classification concerns conditional meets of graph types; orbifold incidence data require the actual contraction category and automorphisms.

**Sheaves, stacks, and shape.** Closed–open recollement is unconditional, but a morphism of local systems on a pro-tube must be represented at one neighborhood stage. The Hawaiian-earring counterexample makes the uniformity obstruction explicit for infinite stalks. For higher objects, the paper states the exact exodromy hypotheses and proves the finite-stratum truncation induction. The sphere gerbe calculation includes the quotient by changing neutralizations. The full groupoid span *←BZ→* already recovers S², so the prompt's inference that R5 disproves groupoid-span reconstruction is false; the failure belongs to the set-valued functor topos. The Hopf example and a finite tetrahedral calculation isolate the coherence that must be retained in general flag assembly.

**The later hypercover layer.** Full ordinary comparison epimorphisms are exactly left exactness. Forest tests alone permit a nontrivial group nerve. Ordinary flat simplicial objects and Verdier hypercovers are incomparable; symmetric flatness implies hypercover strictly. The naive symmetric affine coend can differ from the homotopy colimit, so the phrase “realizes to BG” must specify the realization. B5.10 gives the arbitrary-index subdivision-filling scheme for local weak equivalence after hypercompletion. B5.6 separately gives the exact pro-space mapping tests and the original Artin–Mazur tests, with π₀ applied after the mapping-space limit and q applied after the pro-space construction. Each matching degree is independently necessary. The global finite-set relations are incomplete, while the corrected three-object presentation is complete by normal forms, not merely by checking that its relations hold in finite sets.

**Cote 150.** The literal recursive §8 input retains old and new transverse collars at every cut. Its finite deployment is precylindrical. That word alone does not imply manifold open faces; the exact corner criterion and the TOP cancellation obstruction are stated separately. The simultaneous-cone diagram needs initial-prefix transitions in addition to the other two transition families. Fibrant source maps make its strict nerve a complete Segal object in spaces, after appropriate presentation replacement; equivalence with the geometric Exit category requires the proved recursive controlled-bundle hypotheses. Raw degreewise orbit sets cannot be used for moduli: the complete isomorphism groupoid of chains is retained at every degree. The coarse genus-four counterexample lies in the interior, so boundary blow-up cannot repair it.

**Control data and the margins.** A single ε level cannot determine radial control. The full equivalence uses compatible radial collar germs, horizontal pullback faces, vertical fibre faces, and proper iterated bundles. The margin (69) and union statements are proved for the finite metric HSS setting actually adopted on the pages. The agreement with resolved faces uses genuine variable-radius control tubes; fixed rectangles are not cofinal. The spectral sequence is derived from an actual open cover with sheaf coefficients, not from an invalid assumption that arbitrary sheaf cohomology is homotopy invariant. The normal-crossings comparison is canonical as a homotopy class after normal-derivative normalization.

Every TOP/PL/smooth margin is entered in C5.08's matrix. Raw Hurewicz fibrancy does not imply manifold fibres even for PL or smooth total spaces and maps; the complete compact construction uses a contractible manifold, a controlled collapse, Ferry's theorem and explicit PL/smooth height models. Regular PL bundles and smooth sources with the full face conditions satisfy the positive conclusions. The smooth proof derives submersion on every vertical corner face before integrating horizontal lifts. Arbitrary connected TOP components admit a compact pseudoarc-ray counterexample; the manifold/category and finite-dimensional locally finite PL versions have full positive proofs with their target-embedding hypotheses stated.

## 3. Root manuscript readings and exact corrections

Paths in the next table are relative to the unpacked attachment root `sources/`, except `upload/PROMPT(20261119-040801).md`. Line numbers refer to the supplied files, not regenerated copies. The detailed B and C correction records below supply the remaining corrections and inherited statement IDs.

| Attached location | Check or correction | Final result |
|---|---|---|
| `RESEARCH_SA10_study/study/STUDY.md`, lines153–156 | Closed-flag reconstruction was re-proved; the unverified arbitrary finite-meet corollary is false. | A4.1–A4.3; complete finite counterexample. |
| Same file, lines158–160; `study/HUNCHES.md`, lines34–39; prompt line89 | Conditional lower-bounded meets must be separated from literal all-pairs meets and the empty-bottom convention. The stated stable-graph classification is independently proved. | A4.4–A4.5; L4. |
| Same file, lines173–181; prompt line60 | Support-defined R_i loses its claimed identity when strata are empty. The order-defined deletion restores the identity and stable pullback. | A2.2; SA10-C3-08 and SA10-S3-K1. |
| Same file, lines188–191; `MPL_151_032-075_151_scan060.tex`, lines8–17,25–30 in the second-pass directory below | The R∩S aside is false; both overwritten i/j readings and the explanatory cutoff are handled explicitly. The S/Σ glyph changes no definition. | A1.3 and A2.2; SA10-S3-K2. |
| `RESEARCH_SA10_study/study/STUDY.md`, lines199–215; `study/HUNCHES.md`, lines10–19; prompt line83 | The successor counterexample is confirmed. The proposed all-pair/triple refinement and its asserted equivalence with unzipping are false. | A1.2–A1.5; L1. |
| Same study file, lines218–219; prompt line79; second-pass `MPL_151_032-075_151_scan070.tex`, line13 | The strict inequality is genuine ink. Taken literally with local finiteness it forces X empty, not merely a defect in one proof. | A4.1; SA10-C3-15 and SA10-S3-K4. |
| Same study file, line221; prompt A.2 at line125; second-pass `MPL_151_032-075_151_scan071.tex`, line4 | The original scan explicitly inserts “mais pas” before the open-immersion alternative. The supplied second-pass transcription is correct here; the study and task misstate it. | A2.1–A2.3. |
| Same second-pass 151/071 file, lines7–8 | The asserted inverse-image formula for support-defined R is false when pulled-back strata coincide; the S union and order-defined R have the required fixed-index behavior. | A2.2. |
| `RESEARCH_SA10_study/study/STUDY.md`, lines224–228,248–250 | Closed-crible restriction and deletion are different operations. The explicit circle-versus-two-points tube example settles the caution, and the sheaf restriction has its exact adjunction. | A3.1–A3.2; SA10-C3-13. |
| Same study file, lines87,713–714; prompt line76 | The neighborhood-topos collapse is proved with regular Hausdorff hypotheses; “paracompact” is not silently used without a separation convention. | A1.1; SA10-R151b-25 and SA10-K151b-05. |
| `RESEARCH_SA10_study/study/readings/151_018-031.md`, lines217–232 | The regularity qualification in the detailed reading is retained. The pro-object and ordinary inverse-limit constructions are kept distinct. | A1.1–A1.2. |

The second-pass directory abbreviated above is `RESEARCH_SA10_transcriptions/transcriptions/second_pass_17Nov/MPL_151_032-075/`. No mathematical assertion depends on preferring one unresolved 151/060 ink reading: A1.3 treats the alternatives. Original scans151/057,060,070,071 were visually opened; cote150/043 was independently opened by multiple agents. The full C corrections distinguish the genuine /043 counting inconsistency from corrected or still doubtful transcription glyphs.

For completeness, the abbreviated B.5–B.6 transcription locators in the contribution record below expand to these exact attached files, all under `RESEARCH_SA10_transcriptions/transcriptions/second_pass_17Nov/MPL_150_085-099+151_001-031/`:

| File | Supplied lines | Disposition |
|---|---|---|
| `MPL_150_085-099+151_001-031_151_scan003.tex` | 55 | The sigma-three relation is false; original ink confirms the three. B6.3. |
| `MPL_150_085-099+151_001-031_151_scan005.tex` | 23,26–30 | The middle sigma-one is confirmed; the two global boxes do not complete the all-degree presentation. The final1/3 subscript remains uncertain, and both mathematical readings are settled. B6.1–B6.3. |
| `MPL_150_085-099+151_001-031_151_scan015.tex` | 24–33 | A one-object limit comparison is an identity and cannot supply the inhabitedness condition; the empty diagram is required. The mathematical correction is independent of a new ink claim. B5.1. |
| `MPL_150_085-099+151_001-031_151_scan017.tex` | 22–30,37–42 | Both typed relation families and the doubtful lower bounds are treated; original bounds2,3 were visually confirmed. The countermodel is checked under either supplied bound choice. B6.1–B6.2. |

## 4. Research and source practice

The requested primary literature was fetched or opened with exact locators. Full source-status details follow in the source audit and `.bib` file. Download failures are not recoded as successful local downloads: Higher Algebra and Stratified Morse Theory were opened online even though local retrieval returned403. The original Mazur1961 paper was not opened and is not an unchecked premise; the actual construction uses the opened Zeeman1964 p347 and the explicit intervening proof, with Milnor and Ferry at their cited theorems. An abstract or search snippet is not counted as full text.

No argument was taken from Michel Hua's project. The supplied study and prior-run summaries were checked where used. The actual EXIT_TOWER paper was not included among the supplied files, so its stable-graph conclusion is independently derived, with the attachment's exact attribution preserved only as provenance.

Before any possible priority claim, searches covered tube-recollement counterexamples, neighborhood pro-topos base change, pointwise open-diagram descent, stable-graph common refinements, infinite-stalk local systems, ordinary-to-higher shape failures, coherent K(π,1) assembly, finite-set presentations, arbitrary-index hypercovers, symmetric realization, controlled Hurewicz maps and stratified resolutions. Exact query records and failed proof routes are retained in `notes/root_source_searches.md`, the B contribution reports, the C audit, and `C5_Hurewicz_review.md`. We make no priority claim, including for arguments for which these searches found no exact prior formulation.

## 5. Proof revisions made during checking

The independent checks changed the mathematics in concrete places. The initial simultaneous-cone draft omitted the initial-prefix face family; a two-point-chain certificate exposed the extra isolated point, and C1.03 now includes all three families. The initial fixed-rectangle cofinality argument failed for a tube r₁<r₀²; C4.05 now uses actual variable-radius control tubes and a natural projection. The first normal-crossings comparison needed identity normal derivative and a positive scaling map; both are now proved. An arbitrary radial perturbation could leave the positive-radius domain; C2.03 now uses a specified bounded negative function with positive derivative. The smooth C5.05 argument now derives vertical-face submersions before the corner Ehresmann step. The PL category extension explicitly requires PL target embeddings.

The Hurewicz construction also records a discarded route: direct use of a simplicial mapping-cylinder theorem did not justify a height-preserving identification of the ordinary quotient. The final proof supplies that identification explicitly and proves full Hurewicz lifting with Ferry's strong-regularity estimates. These are resolved corrections, not hidden open gates. Audit artifacts retain what was checked and why the replacement was needed.

## 6. Registers and event semantics

`RESEARCH_SA10_results.csv` has exactly one row for each of the 74 numbered statements. `CHECK_EVENTS.tsv` includes events for this run and the inherited IDs actually used or refuted. The aggregate uses exactly the requested event vocabulary. `CHECK_EVENT_NORMALIZATION.tsv` records purely terminological changes from the individual agents' labels; the original labels remain in the aggregate outcomes and the original event files are preserved. No normalization turns a source check or a bounded computation into an independent general proof.

The independent register audit checks actual recursive TeX inputs, statement headings, CSV uniqueness, exact-ID event coverage and bibliography-key/access-status consistency. Its scope is clerical integrity; it does not replace the substantive proof audits. The final PDF QA record below is tied to a SHA256 digest of the published PDF.

## 7. Timing and continuation record

Work began at approximately05:07 Europe/Berlin (04:07UTC). Checkpoint01 was saved at05:52:40 Europe/Berlin (04:52:40UTC), after the first45-minute interval. Subsequent checkpoint and completion timestamps are recorded in `PROGRESS_LEDGER.md`. The first formal three-hour progress review is due at08:07 Europe/Berlin; completion before then does not fabricate a formal review or invoke the two-no-movement stop rule. Running gate updates and publication checks are labelled as such. The final package retains all deliverable/documentation paths from checkpoints, current versions of their contents, and their manifests; it contains no earlier checkpoint ZIP and no supplied attachment or full research-input literature.

Checkpoint02 was created at06:37:02 Europe/Berlin (05:37:02UTC) and saved during that scheduled interval. It is25,554,624bytes. Its302 manifest hashes and ZIP CRC all pass. It contains two duplicate helper-script entries whose bytes are identical; the final packaging path includes each file only once. The checkpoint is preserved unchanged. The final archive has a separate complete file-hash manifest and a strict no-duplicate-name check.


---

## Requested primary sources and access status

# Requested-literature opening-status matrix

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/hypercovers_finite_sets. No priority claimed.

Snapshot: 2026-11-19T05:38:55.754859+00:00. This matrix covers all ten mathematical works named in the user's Sources list. It consolidates actual openings recorded in the bibliography, source-status files and logs. It does not treat a search result, a failed download or an abstract as a full-text opening, and it does not claim that the catalog generator reopened these sources.

All ten requested works have a recorded full primary-text opening. Local download failures for Higher Algebra and Stratified Morse Theory coexist with successful online full-text openings. LaTeX-source availability is stated separately and is not inferred from the existence of a PDF.

| Requested work | Status/version | Exact locators | Use and current paper citation |
|---|---|---|---|
| Ayala–Francis–Tanaka, Local structures on stratified spaces | OPENED;arXiv v6;Adv.Math.307(2017)903–1028 | Cor.1.2.10;Lemmas6.1.4,6.1.7;Th6.1.9;Cor.7.3.7;Th7.3.8;Props7.3.10,8.2.3,8.2.5 | Unzipping, conically smooth local models, cone/collar and exit comparisons;citation:yes |
| Treumann, Exit paths and constructible stacks | OPENED;arXiv v1;Compos.Math.145(2009)1504–1532 | Definition3.1;Theorems7.13,7.14 | Constructible groupoid stacks and exit-path2-functors;citation:yes |
| Lurie, Higher Algebra, Appendix A | OPENED;18September2017 | TheoremsA.4.19,A.7.1,A.9.3;Cor.A.9.4;RemarkA.9.7;Prop.A.9.16;A.8.4,A.8.11,A.8.14;finite induction pp1463–1465 | Constructible sheaves, exit categories, truncation and recollement induction;citation:yes |
| Barwick–Glasman–Haine, Exodromy | OPENED;arXiv v7,23August2020;opened PDF datedAugust2020 | Definition2.1.8;Lemma2.7.3;Theorem2.7.4;Definition4.2.1;Example4.2.3 | Shapes, stratified homotopy and exodromy framework;citation:yes |
| Haine, On the homotopy theory of stratified spaces | OPENED;v6;paper dated27March2023 | Definition1.1.1p7;Definition1.1.4 and Theorem1.1.7p8;Theorem3.2.4p27;Comparison3.4.2p30 | Theorem1.1.7 identifies flag decollages with conservative infinity-categories after C1.B2;citation:yes |
| Woolf, The fundamental category of a stratified space | OPENED;arXiv v3,including2013 correction;J.Homotopy Relat.Struct.4(2009)359–387 | Lemma3.5;Theorem4.3,p15 ofv3 | Opened comparison/background for endpoint fibrations and constructible sheaf classification;citation:no;opened contextual source with exact locator in this matrix/bibliography |
| Quinn, Homotopically stratified sets | OPENED;JAMS1(1988)441–499 | Definition2.1pp451–452;Lemma2.4 and corollarypp454–455;Definition3.1 and Proposition3.2p469 | Tame holinks, mapping-cylinder comparison, stratified-fibration and normal-germ results;citation:yes |
| Mather, Notes on topological stability | OPENED;July1970 notes;the requested2012 publication is not substituted silently | Section7,p15,control equations | Projection/radius control and comparison with Thom–Mather data;citation:yes |
| Goresky–MacPherson, Stratified Morse Theory | OPENED;Springer1988 | PartI Section1.4pp40–41;Section1.5pp41–42;Section1.6pp42–43 | Normal slices/links,conical local triviality,first isotopy lemma and stratified maps;citation:no;opened contextual source with exact locator in this matrix/bibliography |
| SGA4, Expose IV section9 | OPENED;Tome1,LNM269(1972);opened revised2015 primary PDF | ExposeIV Sections9.3–9.6,especially9.5.1–9.5.7 and Theorem9.5.4;PDFpp240–246 | Closed–open recollement and the gluing comparison;citation:yes |

## Individual evidence and retrieval qualifications

### Ayala–Francis–Tanaka, Local structures on stratified spaces

Primary URL: <https://arxiv.org/abs/1409.0501>. Bibliography keys: `AFT;AFTLocal;C_AFT`.

- Opening evidence: `references_A.bib;B_references.bib;C_source_manifest.tsv;notes/root_source_searches.md`.
- LaTeX-source status: Opened: literature_C/AFT/AFT1-2016.tex;source archive fetched by C agent.
- Qualification: Root web source-fetch attempt failed; C-agent TeX retrieval succeeded. Earlier85-page author version also opened; cited numbering uses v6. Root additionally opened AFT1-2016.tex lines5533–5565 for Proposition8.2.5 on regular neighborhoods of closed constructible embeddings;both8.2.3 and8.2.5 checked.

### Treumann, Exit paths and constructible stacks

Primary URL: <https://arxiv.org/pdf/0708.0659>. Bibliography keys: `Treumann2009`.

- Opening evidence: `B_references.bib;code_B/download_sources.out;literature_B/treumann.tex`.
- LaTeX-source status: Opened and saved as literature_B/treumann.tex.
- Qualification: ArXiv identifier and DOI verified on the primary abstract page; no failed download used as an opening.

### Lurie, Higher Algebra, Appendix A

Primary URL: <https://www.math.ias.edu/~lurie/papers/HA.pdf>. Bibliography keys: `LurieHA`.

- Opening evidence: `B_references.bib;code_B/download_sources.out;CHECK_EVENTS_B.tsv`.
- LaTeX-source status: No LaTeX source opening recorded.
- Qualification: Full PDF actually opened online. Local direct download returned403; local-file failure does not negate the online opening.

### Barwick–Glasman–Haine, Exodromy

Primary URL: <https://arxiv.org/abs/1807.03281>. Bibliography keys: `BGHExodromy`.

- Opening evidence: `B_references.bib;CHECK_EVENTS_B.tsv`.
- LaTeX-source status: No LaTeX source opening recorded.
- Qualification: Full primary paper opened through https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/barwick-glasman-haine.pdf;version verified on arXiv.

### Haine, On the homotopy theory of stratified spaces

Primary URL: <https://arxiv.org/pdf/1811.01119>. Bibliography keys: `B56Haine2023`.

- Opening evidence: `references_B56.bib;B5_scope_audit.md;CHECK_EVENTS_B56.tsv;C1_collage_B.tex`.
- LaTeX-source status: No LaTeX source opening recorded;full PDF downloaded/text extracted.
- Qualification: Not a premise of B5;does not replace the separate geometric Exit comparison. Independently opened by B1–B4 agent.

### Woolf, The fundamental category of a stratified space

Primary URL: <https://arxiv.org/pdf/0811.2580>. Bibliography keys: `Woolf2009`.

- Opening evidence: `B_references.bib;CHECK_EVENTS_B.tsv`.
- LaTeX-source status: No LaTeX source opening recorded.
- Qualification: Introduction's obsolete Theorem4.6 reference is not used;body numbering is4.3. Paper citation status is reported separately below.

### Quinn, Homotopically stratified sets

Primary URL: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/quinn5.pdf>. Bibliography keys: `Quinn1988`.

- Opening evidence: `B_references.bib;code_B/download_sources.out;literature_B/quinn.txt`.
- LaTeX-source status: No LaTeX source opening recorded;full scanned PDF downloaded/text extracted.
- Qualification: Quinn's cylinder topology is distinguished from ordinary quotient topology;additional fibration hypotheses are stated.

### Mather, Notes on topological stability

Primary URL: <https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf>. Bibliography keys: `C_Mather`.

- Opening evidence: `C_references.bib;C_source_manifest.tsv;literature_C/Mather.pdf/.txt`.
- LaTeX-source status: No LaTeX source opening recorded;primary notes PDF opened.
- Qualification: Opening claim is for the1970 notes at the cited locator, not a separately opened2012 typesetting.

### Goresky–MacPherson, Stratified Morse Theory

Primary URL: <https://www.math.ias.edu/~goresky/pdf/SMT.pdf>. Bibliography keys: `GoreskyMacPherson1988`.

- Opening evidence: `references_supplement.bib;notes/supplement_source_audit.md;code/fetch_supplement_sources.out`.
- LaTeX-source status: No LaTeX source opening recorded;full author-hosted PDF opened online.
- Qualification: Local download403;full text was actually read through web retrieval. Source warns normal-slice maps need not be topologically constant along a stratum.

### SGA4, Expose IV section9

Primary URL: <https://www.cmls.polytechnique.fr/perso/orgogozo/SGA4/tomes/tome1.pdf>. Bibliography keys: `SGA4`.

- Opening evidence: `references_A.bib;logs/fetch_primary_A.out;notes/root_source_searches.md`.
- LaTeX-source status: No LaTeX source opening recorded;full primary PDF fetched.
- Qualification: Search result/English transcription was a locator only;the primary text was opened and used.

## Additional source-status caveat

Mazur's original1961 Annals paper, DOI10.2307/1970288, is **not opened in full**. It is not one of the ten requested works. The C5 proof uses the actually opened Zeeman1964p347 construction/nontrivial-boundary statement, Milnor's h-cobordism theorem, Ferry's strong-regularity theorem, and Rolfsen's explicitly limited auxiliary group presentation. See `C5_Hurewicz_review.md` and `references_C5_Hurewicz.bib`. A reproduced abstract and inaccessible JSTOR PDF are not called a primary full-text opening.

Original cote147,150,151 scan readings and their remaining ink ambiguities are recorded separately in `C_source_manifest.tsv`, `notes/root_source_searches.md`, and `ink_B56/INK_REVIEW.md`; the present matrix does not upgrade transcription readings to independent ink readings.


---

## Every program: scope, counts and observed runtime

# Complete saved-program audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/hypercovers_finite_sets. No priority claimed.

Snapshot: **2026-11-19T05:38:55.754859+00:00**. **32 programs**, including this catalog generator; **10 mathematical certificate programs**. No inventoried program was rerun to produce this catalog.

Every count and duration below comes from an existing observed output, except the catalog generator's own current-run measurement. Historical outputs are not silently promoted to measurements of later edited files. A script runtime, a tool wall time, and an uninstrumented run are explicitly distinguished.

Machine-readable records: `PROGRAM_AUDIT.tsv`. Exact file inventory and SHA256s: `PROGRAM_AUDIT_FILES.tsv`. Requested-source matrix: `REQUESTED_SOURCE_STATUS.md` and `.tsv`. Paths are relative to the working deliverable directory; `../primary` and `../texmf` are external research/runtime inputs.

## Coverage and missing evidence

- Missing saved output: none.
- No printed script elapsed time: code/check_tex_runtime.lua; code/fetch_supplement_sources.py; code_C/build_C_sections.py; code_C/build_C_source_audit.py.
- Newly auto-discovered programs: none.
- `fetch_supplement_sources.py` failed with HTTP403 before its elapsed-time print; the saved traceback is an observed output, not a successful download.
- `check_tex_runtime.lua` is uninstrumented. `build_C_sections.py` is uninstrumented; its separately recovered tool wall time is labelled as such in the saved output.
- Preserve all four original code directories, the `stable_graph_data` JSONs, and the source/build logs. Final packaging additionally mirrors agent code under `code/programs/` and copies the source-fetch log into `code/`; these aliases are excluded from source discovery and inventory counts to avoid double counting. Each program's primary observed stdout/JSON is retained under the final code subtree; supplementary build logs and generated documents keep their recorded locations. Full fetched copyrighted sources and third-party TeX runtime packages remain excluded. This catalog does not relocate execution paths or assert that embedded working paths are portable.

## Mathematical certificates

### `code/check_A_finite.py`

Finite A1 gluing and Cech-arity counterexamples; A4 finite-meet colimits; R3/R6 support identities.

- **Inputs:** Embedded finite posets, sheaf maps, assignments and meet diagrams; no external input file.
- **Observed output:** `code/check_A_finite.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 9 distinct all-pair objects;14 nonidentity inclusions;32 successor assignments,0 extensions;7-index examples12→1 and19→2 points;three Cech-arity witnesses;9 failed strict-bound comparisons.
- **Timing:** observed printed timing — seconds=0.000640s.

### `code/stable_graph_meets.py`

Exhaustive stable-graph generation by inverse single-edge contractions; canonicalization and common-refinement tests.

- **Inputs:** Embedded (g,n) cases (0,3),(0,4),(0,5),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(3,0); genera, labelled legs, loops and multiple edges.
- **Observed output:** `code/stable_graph_meets.out`.
- **Generated artifacts:** code/stable_graph_data/g0_n3.json;code/stable_graph_data/g0_n4.json;code/stable_graph_data/g0_n5.json;code/stable_graph_data/g1_n1.json;code/stable_graph_data/g1_n2.json;code/stable_graph_data/g1_n3.json;code/stable_graph_data/g1_n4.json;code/stable_graph_data/g2_n0.json;code/stable_graph_data/g2_n1.json;code/stable_graph_data/g3_n0.json.
- **Observed scope/counts:** 10 cases;graph counts1,4,26,2,5,23,163,7,16,42;pair counts0,6,325,1,10,253,13203,21,120,861;meet failures only (1,4):21,(2,1):2,(3,0):25. Full graph/contraction/failure lists saved.
- **Timing:** observed printed timing — elapsed_seconds=1.847699604695663e-05s; elapsed_seconds=0.00013880499318474904s; elapsed_seconds=0.001682411995716393s; elapsed_seconds=3.1104995287023485e-05s; elapsed_seconds=0.0001572719993419014s; elapsed_seconds=0.013842715001374017s; elapsed_seconds=0.15386597600445384s; elapsed_seconds=0.00021443599689519033s; elapsed_seconds=0.000957172000198625s; elapsed_seconds=0.044610784003452864s.

### `code_B/check_B_finite.py`

Integral normalized C2 bar differential and tetrahedral sphere cocycle/coherence witnesses.

- **Inputs:** Embedded C2 and tetrahedral boundary;SymPy exact integer linear algebra.
- **Observed output:** `code_B/check_B_finite.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 8 associativity triples and2 inverses;bar differentials through degree4;H1(BC2;Z)=Z/2;tetrahedron4 vertices6 edges4 faces;rank(d2)=3;integral cocycle pairing−1.
- **Timing:** observed printed timing — elapsed_seconds=0.091153s.

### `code_B56/check_B56.py`

Finite-set presentations, global relation countermodel, forest/orbit conditions, symmetric group nerve and hypercover nonimplications.

- **Inputs:** Embedded finite sets/functions,C2 actions and exact rational simplex functions;no external data.
- **Observed output:** `code_B56/check_B56.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 14 corrected low-degree relations;56 finite maps;412 global countermodel instances;4 C2 cospans/8 squares;mod2 H1 dimension1;16 symmetric products;1528 cospans/6871 target pairs;126 monotone maps;30 rational amalgams.
- **Timing:** observed printed timing — runtime_seconds=0.044837s.

### `code_B56/check_B6_translation.py`

Check every coface/codegeneracy cycle-word substitution into the manuscript's delta,K,permutation generators.

- **Inputs:** Embedded finite-set maps for every n1–12 and every allowed index i.
- **Observed output:** `code_B56/check_B6_translation.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 90 coface words+78 codegeneracy words=168 checks;zero failures;last generators recovered literally.
- **Timing:** observed printed timing — seconds=0.000609891s.

### `code_B56/check_C5_boundary_group.py`

Check a nontrivial finite quotient of the opened Mazur-boundary group presentation.

- **Inputs:** Embedded presentation <x,y|y^5=x^7,y^4=x^2 y x^2>;fixed7-cycle;all5-cycles on7 points.
- **Observed output:** `code_B56/check_C5_boundary_group.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 504 five-cycles checked;14 solutions;chosen x,y generate A7 of order2520;both defining relations explicitly evaluated.
- **Timing:** observed printed timing — seconds=0.006783651s.
- **Qualification:** Certifies the recorded group's nontriviality; does not replace the geometric verification of a handle presentation.

### `code_B56/check_matching_independence.py`

GF2 cocycle matching-map ranks for the independently indispensable hypercover degrees.

- **Inputs:** Embedded cocycle models K(F2,n),n1–4,simplex degree k0–7.
- **Observed output:** `code_B56/check_matching_independence.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 32 comparisons;for each n exactly degree k=n+1 fails, image codimension1. Full row data in stdout.
- **Timing:** observed printed timing — runtime_seconds=0.016021s.

### `code_B56/check_stable_graphs_independent.py`

Independent direct bounded-multigraph enumeration of the positive stable-graph cases, distinct from the root inverse-contraction algorithm.

- **Inputs:** Embedded (g,n)=(1,1),(1,2),(1,3),(2,0);all bounded genera/legs/edge multiplicities.
- **Observed output:** `code_B56/check_stable_graphs_independent.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** Candidate counts2,22,717,18;graph counts2,5,23,7;pair counts1,10,253,21;compatible pairs1,8,107,18;zero failures.
- **Timing:** observed printed timing — runtime_seconds=4.4e-05s; runtime_seconds=0.000146s; runtime_seconds=0.00284s; runtime_seconds=0.000157s.

### `code_C/check_cone_transitions.py`

Cellular quotient certificate for the missing selected-prefix transitions and the corrected simultaneous-cone construction.

- **Inputs:** Embedded constant one-point chain diagrams with0–6 vertices;union-find of cells under transition families.
- **Observed output:** `code_C/check_cone_transitions.output.json`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** Two-vertex old diagram:2 components,3 vertices,1 edge;corrected:1 component,2 vertices,1 edge. All7 chain sizes0–6 checked;at6 vertices364 blocks,2366 raw cells,2276 transitions,quotient cell counts6,15,20,15,6,1.
- **Timing:** observed printed timing — elapsed_seconds=0.024328412s.

### `code_C/check_cote150.py`

Projection-control twist counterexample;Boolean flag intervals;exact genus4 branch-set automorphisms;quotient local homology.

- **Inputs:** Embedded6-point twist;all naturally labelled posets through5 elements;ten rational/infinite branch points;SymPy and Fraction exact arithmetic.
- **Observed output:** `code_C/check_cote150.output.json`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 6 twist vertices/6 strict arrows/2 transitivity failures;poset counts1,1,2,7,40,357;4135 flags/10603 intervals;720 Mobius candidates,only identity;genus4 tangent invariant/anti-invariant dimensions7/2;local torsion Z/2 in degree16.
- **Timing:** observed printed timing — runtime_seconds=0.129894s; runtime_seconds=0.724255s; runtime_seconds=3.3e-05s; total_runtime_seconds=0.854292s; runtime_seconds=4e-05s.

## Retrieval, typesetting, metadata, packaging and audit programs

### `code/build_paper.py`

LuaLaTeX/BibTeX build, task-local TeX support/cache setup, build-history preservation and overflow/citation checks.

- **Inputs:** RESEARCH_SA10_paper.tex and recursive inputs;RESEARCH_SA10_references.bib;existing aux;task-local texmf;system TeX fonts/maps.
- **Observed output:** `code/build_paper.out;logs/build_summary.json`.
- **Generated artifacts:** RESEARCH_SA10_paper.pdf;RESEARCH_SA10_paper.log;RESEARCH_SA10_paper.aux;RESEARCH_SA10_paper.bbl;pdftex.map;logs/build_*.out;logs/build_summary.json;logs/build_history/**.
- **Observed scope/counts:** Overfull boxes: [1.4243, 0.20518] | Overfull boxes exceeding 2pt: 0 | Runtime: 23.495529 seconds | "overfull_pt": [ | "overfull_exceeding_2pt": 0, | "runtime_seconds": 23.495528904997627, | "missing_characters": 0, | "undefined_citations": 0
- **Timing:** observed printed timing — Runtime=23.495529s; runtime_seconds=23.495528904997627s.
- **Qualification:** Build outputs are snapshots and may change with the final build. Preserve all existing history logs; this catalog does not run a build or authorize PDF delivery.

### `code/check_tex_runtime.lua`

Inspect task-local TeX cache directory permissions and compare lfs writable-file result with an actual temporary-file write.

- **Inputs:** Task-local tex_cache directory and LuaFileSystem module.
- **Observed output:** `code/check_tex_runtime.out`.
- **Generated artifacts:** Temporary runtime_test.tmp is removed by the program..
- **Observed scope/counts:** Observed isdir=true, writable-file predicate=nil, actual write=true.
- **Timing:** not instrumented.
- **Qualification:** No script timing instrumentation. This is environment diagnosis, not a mathematical check.

### `code/fetch_primary_A.py`

Download/identify cote151, SGA4 tome1 and Schmitt notes; record bytes, SHA256 and per-file duration.

- **Inputs:** URLs embedded in script: Montpellier151.pdf;CMLS SGA4 tome1.pdf;Bonn Schmitt Script.pdf.
- **Observed output:** `code/fetch_primary_A.out;logs/fetch_primary_A.out`.
- **Generated artifacts:** ../primary/151.pdf;../primary/SGA4_tome1.pdf;../primary/Schmitt_ModCurves.pdf.
- **Observed scope/counts:** 3 completed files:27695508,1512797,6518673 bytes;each SHA256 saved.
- **Timing:** observed printed timing — seconds=632.8592769669995s; seconds=23.43754161099787s; seconds=6.256165902996145s.
- **Qualification:** Original stdout is logs/fetch_primary_A.out; the package preflight also preserves it as code/fetch_primary_A.out. Identical copied logs are not counted as separate runs. Fetched full primary PDFs are research inputs excluded from the deliverable.

### `code/fetch_supplement_sources.py`

Attempt a local download and text extraction of Goresky–MacPherson Stratified Morse Theory.

- **Inputs:** https://www.math.ias.edu/~goresky/pdf/SMT.pdf
- **Observed output:** `code/fetch_supplement_sources.out`.
- **Generated artifacts:** Intended ../primary/Goresky_MacPherson_SMT.pdf/.txt;not produced by the failed observed run..
- **Observed scope/counts:** One attempted request;HTTP403 before timing output.
- **Timing:** instrumented, but no elapsed time in the observed output.
- **Qualification:** Failure log is preserved. The full text was separately opened online; download failure is not an unopened-source claim. Timing instrumentation exists but was not reached.

### `code/fetch_tex_support.py`

Fetch three CTAN LuaLaTeX support archives and extract task-local runtime files; generate lualibs entry point when needed.

- **Inputs:** CTAN luaotfload.zip;lualibs.zip;lua-uni-algos.zip;local LuaTeX executable.
- **Observed output:** `code/fetch_tex_support.out`.
- **Generated artifacts:** ../texmf/tex/luatex/luaotfload/*;../texmf/tex/luatex/lualibs/*;../texmf/tex/luatex/lua-uni-algos/*.
- **Observed scope/counts:** 3 archives:1993888,282788,95510 bytes;103,35,11 extracted runtime files (149 total).
- **Timing:** observed printed timing — Runtime=23.239087s.
- **Qualification:** Third-party runtime packages are not mathematical code authored in this run; retain the fetch program and observed log.

### `code/finalize_qa.py`

Seal the PDF verification record after matching the final PDF hash, successful build metrics and three independent visual-inspection records.

- **Inputs:** RESEARCH_SA10_paper.pdf;qa/render_manifest.json;logs/build_summary.json;PDF_VISUAL_ROOT.md;PDF_VISUAL_B.md;PDF_VISUAL_C.md;logs/build_history/20261119T052014525518Z/build_pass2.out.
- **Observed output:** `code/finalize_qa.out`.
- **Generated artifacts:** qa/final_qa.json;PDF_QA_REPORT.md;logs/PDF_QA_APPROVED.txt.
- **Observed scope/counts:** Runtime 0.004582853 seconds.
- **Timing:** observed printed timing — Runtime=0.004582853s.
- **Qualification:** Checks recorded image inspections rather than treating a successful render as visual approval. Before/after overflow counts and the exact PDF hash are retained in its artifacts.

### `code/finalize_report.py`

Assemble the outcome-first final report from the root conclusions, source/program catalogs, detailed proof/correction records and publication/register audits.

- **Inputs:** REPORT_ROOT.md;REQUESTED_SOURCE_STATUS.md;PROGRAM_AUDIT.md;agent_B_levels.md;agent_B56.md;C_source_corrections.md;C5_Hurewicz_review.md;C5_audit_B.md;PDF_QA_REPORT.md;FINAL_register_audit_B56.md;RESEARCH_SA10_results.csv;CHECK_EVENTS.tsv.
- **Observed output:** `code/finalize_report.out`.
- **Generated artifacts:** RESEARCH_SA10_report.md.
- **Observed scope/counts:** Assembled final report: 10 sections/source records; 129858 characters; 74 results; 302 events. | Runtime 0.006510858 seconds.
- **Timing:** observed printed timing — Runtime=0.006510858s.
- **Qualification:** Observed character/section/result/event counts refer to the saved run. A later assembly may include a refreshed version of this catalog.

### `code/finalize_root_records.py`

Record the root's late source/proof checks and annotate exact A-result dependencies.

- **Inputs:** Embedded actual check descriptions;RESULTS_A.csv.
- **Observed output:** `code/finalize_root_records.out`.
- **Generated artifacts:** CHECK_EVENTS_ROOT_FINAL.tsv;RESULTS_A.csv.
- **Observed scope/counts:** Recorded 72 actual root check events; annotated 15 A result dependencies. | Runtime 0.001156276 seconds. | Recorded 73 actual root check events; annotated 15 A result dependencies. | Runtime 0.001005915 seconds.
- **Timing:** observed printed timing — Runtime=0.001156276s; Runtime=0.001005915s.

### `code/integrate.py`

Aggregate result CSVs, check events and bibliography fragments; reject duplicate result IDs or bibliography keys; normalize recorded event labels when configured.

- **Inputs:** RESULTS_A.csv;RESULTS_B.csv;results_B56.csv;RESULTS_C.csv;RESULTS_C1_B.csv;CHECK_EVENTS_*.tsv;references_A.bib;B_references.bib;references_B56.bib;C_references.bib;references_C5_Hurewicz.bib;references_supplement.bib.
- **Observed output:** `code/integrate.out`.
- **Generated artifacts:** RESEARCH_SA10_results.csv;CHECK_EVENTS.tsv;RESEARCH_SA10_references.bib;CHECK_EVENT_NORMALIZATION.tsv when produced..
- **Observed scope/counts:** Assembled 74 result rows, 302 check events, 40 bibliography records. | Runtime: 0.007535 seconds
- **Timing:** observed printed timing — Runtime=0.007535s.

### `code/make_checkpoint.py`

Create a new numbered full-work checkpoint with SHA256 manifest, excluding supplied/fetched sources and earlier ZIPs; refuse overwrite or ≥500MB.

- **Inputs:** CLI checkpoint number;current work tree;PDF_QA_APPROVED marker;library_helpers/*.py.
- **Observed output:** `code/make_checkpoint_01.out;code/make_checkpoint_02.out`.
- **Generated artifacts:** CHECKPOINT_<NN>_FILES.tsv;../RESEARCH_SA10_checkpoint_<NN>.zip.
- **Observed scope/counts:** 89 working files; 296541 compressed bytes; runtime 0.192699 seconds | 303 working files; 25554624 compressed bytes; runtime 1.211560 seconds
- **Timing:** observed printed timing — runtime=0.192699s; runtime=1.211560s.
- **Qualification:** Checkpoint ZIPs remain separate; never place earlier checkpoint ZIPs inside the final ZIP.

### `code/make_final_package.py`

Verify the approved PDF hash,74 unique result rows and preserved checkpoint paths;prepare delivery-only code mirrors and helper records. Optional --build writes the final ZIP,hash manifest and CRC check while refusing overwrite or size≥500MB.

- **Inputs:** qa/final_qa.json;RESEARCH_SA10_paper.pdf;RESEARCH_SA10_report.md;RESEARCH_SA10_results.csv;CHECKPOINT_*_FILES.tsv;authored work tree;../library_helpers/*.py.
- **Observed output:** `code/make_final_package.out`.
- **Generated artifacts:** code/programs/{code_B,code_B56,code_C}/**;code/fetch_primary_A.out;support/library_helpers/*.py;DELIVERY_EXCLUSIONS.tsv;with --build only:DELIVERY_MANIFEST.tsv and ../RESEARCH_SA10_final.zip..
- **Observed scope/counts:** Preflight PASS: 299 selected current files; 74 results; QA digest matches; no missing checkpoint-manifest path. | Excluded 264 research-input/runtime files. No supplied attachment or previous ZIP is selected. | Preparation runtime 0.054080653 seconds.
- **Timing:** observed printed timing — runtime=0.054080653s.
- **Qualification:** The observed output currently records a default/preflight run only. It is not evidence that --build ran or that a final ZIP/CRC check has already succeeded. Delivery mirrors are excluded from program-source discovery because they duplicate the originals.

### `code/render_pdf_qa.py`

Render every PDF page with Poppler, create indexed contact sheets and locate theorem/citation keywords;record the exact PDF hash.

- **Inputs:** RESEARCH_SA10_paper.pdf;Poppler pdftoppm;PyMuPDF;Pillow.
- **Observed output:** `code/render_pdf_qa.out`.
- **Generated artifacts:** qa/pages/page-*.png;qa/contact/contact-*.png;qa/render_manifest.json.
- **Observed scope/counts:** "sha256": "1786ba59ec32382ec60392f23bd95ef926d14872f851478dbeb0771e12a79301", | "runtime_seconds": 23.081229158997303, | "note": "Rendering and text location only. Human-style image inspection must be recorded separately."
- **Timing:** observed printed timing — runtime_seconds=23.081229158997303s.
- **Qualification:** Observed current render has74 pages at110dpi and7 contact sheets. Rendering and keyword location do not themselves constitute visual approval; the output explicitly records visual_approval=false pending separate image inspection.

### `code/update_working_report.py`

Assemble the working report and update the dated progress ledger from explicit item/lead states and agent summaries.

- **Inputs:** Embedded19 item/lead states;agent_B_levels.md;agent_B56.md;PROGRESS_LEDGER.md.
- **Observed output:** `code/update_working_report.out`.
- **Generated artifacts:** RESEARCH_SA10_report.md;PROGRESS_LEDGER.md.
- **Observed scope/counts:** Updated 19 item/lead states. Runtime 0.001724 seconds.
- **Timing:** observed printed timing — Runtime=0.001724s.
- **Qualification:** Historical working-report generator. Its recorded run is not evidence that the current final report still has that wording.

### `code/verify_archive.py`

Verify an existing ZIP's CRC, every current manifest hash, duplicate-name byte identity and absence of nested ZIPs;final-delivery manifests additionally forbid duplicate names.

- **Inputs:** CLI archive pathname and --output pathname;embedded CHECKPOINT_<NN>_FILES.tsv or DELIVERY_MANIFEST.tsv.
- **Observed output:** `code/verify_archive.out`.
- **Generated artifacts:** JSON integrity report at the supplied --output pathname;observed stdout..
- **Observed scope/counts:** "bytes": 25554624, | "duplicate_bytes_identical": { | "runtime_seconds": 0.29703593300655484
- **Timing:** observed printed timing — runtime_seconds=0.29703593300655484s.
- **Qualification:** The observed saved run verifies checkpoint02:305 entries,302 manifest hashes,no mismatch or nested ZIP;two duplicated helper filenames have identical bytes. It is not an observed verification of the not-yet-built final archive.

### `code_B/download_sources.py`

Fetch Treumann source/PDF, Quinn PDF and Higher Algebra; preserve failures; decompress Treumann TeX.

- **Inputs:** Four URLs embedded in script;existing literature_B files.
- **Observed output:** `code_B/download_sources.out`.
- **Generated artifacts:** literature_B/treumann_source;literature_B/treumann.pdf;literature_B/treumann.tex;literature_B/quinn.pdf;intended literature_B/HA.pdf..
- **Observed scope/counts:** Treumann source34221 bytes and PDF451815 bytes already present;Quinn1370605 bytes downloaded;HA local request403;Treumann TeX decompressed.
- **Timing:** observed printed timing — elapsed_seconds=11.378s.
- **Qualification:** Higher Algebra was independently opened online. Fetched complete copyrighted source files are excluded from the package.

### `code_B/write_B_records.py`

Write B1–B4 result rows and their recorded check events.

- **Inputs:** Embedded statement/check descriptions.
- **Observed output:** `code_B/write_B_records.out`.
- **Generated artifacts:** RESULTS_B.csv;CHECK_EVENTS_B.tsv.
- **Observed scope/counts:** Observed output15 statement rows,29 check-event rows;later independent additions may increase the current event file.
- **Timing:** observed printed timing — elapsed_seconds=0.000767s.

### `code_B56/audit_final_register.py`

Recursively inspect actual manuscript inputs;match numbered statement headings to the requested five CSVs and exact-ID check events;verify citation keys/access labels.

- **Inputs:** RESEARCH_SA10_paper.tex and recursive TeX inputs;five result CSVs;source/aggregate CHECK_EVENTS;RESEARCH_SA10_references.bib.
- **Observed output:** `code_B56/audit_final_register.out;code_B56/audit_final_register_052044.out;code_B56/audit_final_register_053221.out;code_B56/audit_final_register_053641.out`.
- **Generated artifacts:** FINAL_register_audit_B56.md;FINAL_register_audit_B56.json.
- **Observed scope/counts:** "scope": "Actual recursive TeX inputs; only numbered statement headings, not equation tags or older drafts.", | "missing_includes": [], | "numbered_statements": 74, | "register_counts": { | "missing_result_rows": [], | "duplicate_statement_headings": {}, | "missing_exact_source_check_events": [], | "missing_exact_aggregate_check_events": [], | "inherited_C_ids_missing_exact_aggregate_event": [], | "missing_bibliography_keys": [], | "cited_bibliography_keys_missing_access_status": [], | "scope": "Actual recursive TeX inputs; only numbered statement headings, not equation tags or older drafts.", | "missing_includes": [], | "numbered_statements": 74, | "register_counts": { | "missing_result_rows": [],
- **Timing:** observed printed timing — seconds=0.012551097s; seconds=0.010835391s; seconds=0.017263091s; seconds=0.01214952s.
- **Qualification:** Does not execute mathematical tests or reopen every source. Records SHA256 snapshots; counts in stdout identify the audited version.

### `code_B56/build_program_audit.py`

Inventory all saved programs in four code directories;read their observed outputs;catalog requested-source opening evidence without executing inventoried programs.

- **Inputs:** code/**;code_B/**;code_B56/**;code_C/**;logs;reference/status notes;current TeX citations.
- **Observed output:** `code_B56/build_program_audit.out`.
- **Generated artifacts:** PROGRAM_AUDIT.md;PROGRAM_AUDIT.tsv;PROGRAM_AUDIT_FILES.tsv;REQUESTED_SOURCE_STATUS.md;REQUESTED_SOURCE_STATUS.tsv.
- **Observed scope/counts:** 32 programs cataloged;10 requested works;no inventoried program rerun.
- **Timing:** observed printed timing;before final report serialization — runtime_seconds=0.018680949s.
- **Qualification:** The current run's measured interval covers inventory/source analysis and ends immediately before final report serialization. No inventoried program is rerun.

### `code_B56/finalize_B56_records.py`

Update the B56 integration note,13 result rows and final scope/source/audit check events.

- **Inputs:** agent_B56.md;results_B56.csv;CHECK_EVENTS_B56.tsv;embedded exact audit descriptions.
- **Observed output:** `code_B56/finalize_B56_records.out`.
- **Generated artifacts:** agent_B56.md;results_B56.csv;CHECK_EVENTS_B56.tsv.
- **Observed scope/counts:** Two retained runs:13 result rows in both;check events54 then56;new event IDs retained in the output.
- **Timing:** observed printed timing — seconds=0.001580352s; seconds=0.001191058s.

### `code_B56/sync_B56_mirrors.py`

Normalize B56 section levels and mirror the directly maintained authoritative TeX into secondary TeX/Markdown.

- **Inputs:** B56.tex;Pandoc.
- **Observed output:** `code_B56/sync_B56_mirrors.out`.
- **Generated artifacts:** B56.tex;agent_B56.tex;agent_B56_proofs.md.
- **Observed scope/counts:** Two parallel B5/B6 sections;TeX mirror byte-identical;observed Markdown42518 bytes.
- **Timing:** observed printed timing — seconds=0.176059078s.

### `code_C/build_C_sections.py`

Convert the C-agent's complete source into the paper contribution and result rows while retaining separately audited TeX inputs.

- **Inputs:** agent_C.md;Pandoc;embedded statement/locator/dependency mappings.
- **Observed output:** `code_C/build_C_sections.out`.
- **Generated artifacts:** C_paper_source.md;C_sections.tex;RESULTS_C.csv.
- **Observed scope/counts:** Latest recovered stdout:27 statements;95724 TeX bytes;remaining non-ASCII character ö. Earlier generation:93716 bytes.
- **Timing:** not instrumented.
- **Tool wall time, not script runtime:** 0.476677675, 0.441562165s.
- **Qualification:** No script timing instrumentation. Recovered tool wall times are0.476677675s for the latest generation and0.441562165s for the earlier one; original outputs preserved without rerunning.

### `code_C/build_C_source_audit.py`

Record the exact inherited cote150 statement IDs actually checked, their supplied file/line locators and current proof dispositions;append corresponding check events.

- **Inputs:** ../sources/RESEARCH_SA10_study/study/readings/150_*_CHECK_EVENTS.tsv;150_*_CORRECTIONS.tsv;CHECK_EVENTS_C.tsv;embedded actual audit descriptions.
- **Observed output:** `code_C/build_C_source_audit.out`.
- **Generated artifacts:** C_inherited_audit.tsv;C_source_corrections.md;CHECK_EVENTS_C.tsv.
- **Observed scope/counts:** 56 inherited source-ID records;98 total C check-event rows.
- **Timing:** not instrumented.
- **Qualification:** Metadata-only program;does not modify TeX or perform a new mathematical computation. Script runtime not instrumented.

## Stable-graph case-by-case recorded measurements

These rows are parsed from the saved outputs, not recomputed.

| Program | (g,n) | Graphs | Pairs | Compatible | Failures | Recorded seconds |
|---|---|---:|---:|---:|---:|---:|
| code/stable_graph_meets.out | (0,3) | 1 | 0 | 0 | 0 | 1.847699604695663e-05 |
| code/stable_graph_meets.out | (0,4) | 4 | 6 | 3 | 0 | 0.00013880499318474904 |
| code/stable_graph_meets.out | (0,5) | 26 | 325 | 70 | 0 | 0.001682411995716393 |
| code/stable_graph_meets.out | (1,1) | 2 | 1 | 1 | 0 | 3.1104995287023485e-05 |
| code/stable_graph_meets.out | (1,2) | 5 | 10 | 8 | 0 | 0.0001572719993419014 |
| code/stable_graph_meets.out | (1,3) | 23 | 253 | 107 | 0 | 0.013842715001374017 |
| code/stable_graph_meets.out | (1,4) | 163 | 13203 | 2050 | 21 | 0.15386597600445384 |
| code/stable_graph_meets.out | (2,0) | 7 | 21 | 18 | 0 | 0.00021443599689519033 |
| code/stable_graph_meets.out | (2,1) | 16 | 120 | 90 | 2 | 0.000957172000198625 |
| code/stable_graph_meets.out | (3,0) | 42 | 861 | 603 | 25 | 0.044610784003452864 |
| code_B56/check_stable_graphs_independent.out | (1,1) | 2 | 1 | 1 | 0 | 4.4e-05 |
| code_B56/check_stable_graphs_independent.out | (1,2) | 5 | 10 | 8 | 0 | 0.000146 |
| code_B56/check_stable_graphs_independent.out | (1,3) | 23 | 253 | 107 | 0 | 0.00284 |
| code_B56/check_stable_graphs_independent.out | (2,0) | 7 | 21 | 18 | 0 | 0.000157 |


---

## Detailed B.1–B.4 proof and correction record

# B.1–B.4: proof report and integration notes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/homotopy_levels`, 2026-11-19. Effort is not separately exposed. No priority is claimed.

## Outcome table

| Item | Outcome | Statements |
|---|---|---|
| B.1 | The unrestricted uniform pro-tube assertion is false. The exact necessary-and-sufficient pro-tube criterion is proved, and compact conical tube hypotheses are verified sufficient. | B1.1–B1.5 |
| B.2 | The ordinary-topos bicategorical principle is false. The correct infinity-topos shape theorem is known and derived explicitly; the actual A.1 cover diagrams satisfy higher descent stage by stage. Quinn's geometric hypothesis is separated from the formal theorem. | B2.1–B2.4 |
| B.3 | The exit-path equivalences hold under the stated paracompact, local singular-shape, conical and ACC hypotheses. Every truncation level is proved with a finite-stratum induction; groupoid stacks and the complete gerbe calculation follow. Unrestricted conical bases are refuted by the one-stratum Cantor example. | B3.1–B3.3 |
| B.4 | The prompt's inference from R5 is false: a full groupoid span of aspherical pieces suffices in the two-stratum case. The full flag assembly formula is proved, including the exact coherent groupoid reduction for aspherical pairwise incidence links. | B4.1–B4.3 |
| L2 | False as stated. A holink fibration omits Quinn tameness; arbitrary ordinary-topos bicategorical colimits do not preserve shape. Correct replacements are stated and proved/derived. | B2.1–B2.3 |
| L3 | Correct after the exact hypotheses and truncation convention are supplied. A link's fundamental group and the fundamental group of an exit mapping space are different levels of data. Gerbes are a subproblem of general constructible stacks. | B3.1–B3.3 |

## Deliverables

- `B_levels.tex`: 15 numbered statements, typed constructions, proofs, counterexamples, edge cases and exact citations.
- `RESULTS_B.csv`: one row per numbered statement.
- `CHECK_EVENTS_B.tsv`: 29 check events, including earlier study IDs SA10-C3-04 through SA10-C3-07 and SA10-8.
- `B_references.bib`: ten opened primary references, with exact theorem locators and version qualifications.
- `code_B/check_B_finite.py` and output: finite checks described below.
- `code_B/download_sources.py` and output: source retrieval record.
- `code_B/write_B_records.py` and output: reproducible generation of the metadata files.

## Primary manuscript readings

Read directly the second-pass transcriptions of 151/027–044 and 151/057–061 on 2026-11-19. The mathematical conclusions on 151/035–043 do not depend on the doubt marks about typography, the category's name, or punctuation. In particular (18)'s direction, the invariants map, the sphere diagram and the explicit retraction of the feared groupoid-span failure on 151/041 are unambiguous in the supplied text.

The manuscript itself initially calls the tube a topos limit on 151/028. The task requires the repaired pro-object interpretation. The counterexample in B1.3 concerns this required pro-interpretation with actual local-system germs and morphisms represented at one stage. It is not a claim that a collapsed ordinary topos limit retains the punctured-neighbourhood information.

## Corrections and qualifications, with attached locations

All paths below are relative to the unpacked `sources/` directory, except the prompt.

1. `RESEARCH_SA10_study/study/STUDY.md:117`: the unrestricted equivalence of ordinary tube systems with constructible sheaves needs B1.5's extension and uniform morphism conditions. B1.3 gives a compact metric counterexample with infinite stalks. The inertia formulation also requires the surjectivity and connecting-map qualifications in B1.4.
2. The same file, lines 112–115: independently confirmed by the homotopy exact sequence in B1.4. This rechecks SA10-C3-04.
3. The same file, lines 120–121: independently confirmed in B2.4 (SA10-C3-05 and SA10-C3-06). Its category C is used contravariantly as a presheaf index; our covariant exit category is its opposite. Thus 'final' there and 'initial' here are consistent, not a mathematical contradiction.
4. The same file, line 125: for the constant abelian band, extensions must be central. A gerbe and a group extension are equivalent descriptions after basepoint/neutralization choices, not canonically identical objects.
5. The same file, line 126: independently confirmed in B3.3, including why changing either neutralization does not identify distinct elements of A (SA10-C3-07).
6. The same file, line 127: the unqualified colimit assertion is false in the ordinary 2-category of topoi, by B2.2. B2.1 states the correct infinity-topos theorem.
7. The same file, line 132: F is a category of representations of the homotopy exit category, not the exit category itself. B3.1 gives the exact equivalence. Lines 133–134 become correct under the stated hypotheses and finite truncation conventions (SA10-8).
8. `upload/PROMPT(20261119-040801).md:143`: its last sentence is false. R5 does not show that the groupoid span (8)/(10) is insufficient when all pieces are K(pi,1). B4.1 reconstructs the sphere as the homotopy pushout `* <- BZ -> *`. In `RESEARCH_SA10_transcriptions/transcriptions/second_pass_17Nov/MPL_151_032-075/MPL_151_032-075_151_scan041.tex:3-11`, Grothendieck explicitly withdraws that fear and distinguishes the failure of F.
9. The prompt, line 84 (L2): Quinn's Definition 3.1 has both tameness and a holink source-fibration condition. Fibration alone is not his entire condition; the Hawaiian-earring common point witnesses that distinction. Also, the formal shape theorem applies to infinity-topos colimits, not all ordinary bicategorical colimits.
10. The prompt, lines 85–88 (L3): set-valued sheaves retain pi_0 of exit mapping spaces, while groupoid stacks retain their pi_1. The pi_1 of a whole incidence link can still enter the set-valued description through its maps to stratum fundamental groups. These two uses of 'pi_1 of links' should not be conflated.
11. `RESEARCH_SA10_transcriptions/transcriptions/second_pass_17Nov/MPL_151_032-075/MPL_151_032-075_151_scan032.tex:16,19`: the running text has the normal fibre `V*_{z,Z}`, while display (11) has `V*_{z,X}`. We have not claimed a paleographic correction without the scan. Mathematically the local normal-model reading is the one that types correctly. The two readings differ in positive stratum dimension: for a line in the plane the normal link is S0, whereas the ambient point link is S1. The proof uses the normal-model reading, and the ambient-point reading is false in this example.
12. A source locator correction discovered during this run: Woolf's corrected arXiv v3 introduction still refers to Theorem 4.6 for constructible sheaves, but the actual body statement is Theorem 4.3, PDF p.15. The bibliography records the body locator. Miller's arXiv v1 holink theorem is 4.9, which differs from journal numbering quoted by Woolf.

## Primary sources opened and used

The complete URLs and opened annotations are in `B_references.bib`.

- Lurie, *Higher Algebra*, 18 September 2017: Theorem A.9.3, Corollary A.9.4, Remark A.9.7, Proposition A.9.16; Theorem A.7.1; recollement A.8.4/A.8.11/A.8.14; the finite-rank induction on printed pp.1463–1465. PDF opened online. Both local PDF download attempts returned HTTP403, which is recorded; this does not affect the opened web source.
- Lurie, *Higher Topos Theory*: shape §7.1.6, especially Remark7.1.6.15 and Example7.1.6.9.
- Treumann, arXiv:0708.0659: PDF and LaTeX source opened; Definition3.1, Theorems7.13 and7.14, introductory examples.
- Quinn, *Homotopically stratified sets*: Definition2.1, Lemma2.4 and its corollary, Definition3.1, Proposition3.2. PDF downloaded and text extracted. His mapping-cylinder topology is not the ordinary quotient topology. The final B2.3 proof therefore derives the ordinary homotopy-pushout statement independently, from actual numerable open covers and the fixed-tame pro-neighborhood/holink comparisons proved explicitly in C4.02. Quinn's controlled strict relative theorem remains cited with its own convention.
- Barwick–Glasman–Haine, *Exodromy*, arXiv1807.03281v7: Definition2.1.8, Lemma2.7.3, Theorem2.7.4, Definition4.2.1, Example4.2.3.
- Hoyois, *Higher Galois theory*: Proposition5.1, with hypercompletion explicitly retained.
- Miller, *Popaths and Holinks*, arXiv0909.1201v1, Theorem4.9.
- Woolf, arXiv0811.2580v3, Lemma3.5 and Theorem4.3: opened as background verification of the holink and set-level classification; not substituted for the full infinity-exodromy theorem.
- Ayala–Francis–Tanaka, arXiv1409.0501v6, Lemmas6.1.4 and6.1.7 and Theorem6.1.9. The primary abstract pages verified arXiv identifiers and versions.

## Computations and actual scope

`check_B_finite.py` ran in 0.091153 seconds. It verified C2 group operations, all eight associativity triples, and both inverses. The normalized bar complex through degree4 has differentials 0,2,0,2, giving H1(BC2;Z)=Z/2. It also checked the tetrahedral sphere with four vertices, six edges and four faces: the second boundary matrix has rank3, its fundamental cycle is (-1,1,-1,1), and the cochain (1,0,0,0) pairs to -1. Thus the Hopf-bundle coherence class is not a coboundary. These checks certify the finite algebra used in B2.2 and B4.3; they do not purport to certify the general theorems.

`download_sources.py` ran in 11.378 seconds. It obtained and unpacked the Treumann LaTeX source and downloaded the Quinn PDF; the HA403 failures were logged.

`write_B_records.py` ran in 0.000767 seconds and produced 15 result rows and29 check-event rows. Its purpose is metadata generation, not proof checking.

## Literature search and priority

No priority is claimed for any argument. Exact primary theorem locators were searched and opened rather than relying on the attached reading. Further searches used the queries 'locally constant sheaves germ neighborhood closed subset infinite stalk extension Hawaiian earring recollement', 'shape bicategorical pushout topoi classifying topos suspension group', and 'stratified space aspherical links fundamental groupoids homotopy colimit coherence'. No primary source for the two exact counterexamples B1.3 and B2.2 was located in those searches; their complete direct proofs are supplied. Searches for 'infinity category collage mapping cylinder pushout left fibration correspondence' and 'infinity category collage lax colimit correspondence Grothendieck construction universal property' are part of the additional C.1 proof assistance, not a priority claim.

## Integration caution

Do not apply B2.1 directly to an ordinary 2-Pro(Topos) colimit from A.1. Apply it to the honest full open-cover descent diagram at each synchronized neighbourhood stage. Do not exchange an infinite homotopy colimit with a pro-limit. The ordinary-topos counterexample is exactly why the distinction matters.

B4.2 distinguishes two meanings of 'links': all pairwise incidence links versus only each stratum's entire normal link. The latter does not imply pairwise asphericity; the three-stratum closed4-ball is an explicit witness. The full spatial flag diagram still reconstructs X; it reduces to groupoids exactly under the stated one-type condition.

No PDF has been independently published by this agent. The root owns integration, LuaLaTeX compilation, rendering and final storage.

## Additional C.1 assistance

`C1_collage_B.tex` gives four explicit lemmas/theorems for the full coherent Exit comparison: directed collage, the crossing-arrow left fibration, coherent inward transport of retained outer faces, and recursive cone-collar induction. It has been sent to the C agent for independent review and integration. `CHECK_EVENTS_C1_B.tsv` records these checks. The hypotheses deliberately include recursive compatible conical collars and proper stratified locally trivial source bundles; mere fibrancy is not asserted to imply them.

We visually inspected the primary cote150 PDF page43, rendered at2200px as `literature_B/cote150_scan043.png`. The main text really reads `p=long.d-prime`, whereas the margin says `d` is the set of maxima of `d1,...,dp`. Thus the mismatch is in the supplied manuscript scan, not an invented correction to an AI reading. For an arbitrary selected subflag the corrected count is `p=|d|`. The projection-chain index is `p+1`, resolving the supplied `p+1|p-1` doubt; the boxed equation below visually reads29.

Added an opened primary research citation for the classical gerbe classification used in B3.3: Ashwin Deopurkar, *Torsors and gerbes*, arXiv2305.15412v1, Theorem2.7 and Remark3.1. This supplies the precise H²/banded-gerbe and neutral-gerbe/torsor identifications; the sphere gluing and gauge quotient are proved directly.


## Final independent C audits

- `C4_path_proof_B.tex` supplies the full C4.02 proof with all relative paths allowed when bands overlap. The explicit path-shortening equivalence and endpoint-preserving radial-replacement homotopy are continuous in families and coherent under shrinking. The strict-holink version is false when the bands coincide.
- `C4_collar_proof_B.tex` repairs C4.05: fixed rectangles are not cofinal (for instance a tube may impose r1 < r0²). Actual control tubes with radius functions on their stratum bases are cofinal by proper closed-subtube maps. Their intersections are triangular varying-radius regions, each homeomorphic to the open resolved face times a cube. One natural projection proves the pro-equivalence. The proof derives the triangular coordinates from the full horizontal/vertical collar axioms of C2.05.
- `C4_remaining_audit_B.tex` makes C4.03 exact sheaf descent: in the interval hull, L is open, so choose all L-stratum neighborhoods inside it; their union is exactly X_L. It also records the local flabby/direct-image argument and normal-crossings identity-normal-derivative and positive-scaling precision for C4.06.
- `CHECK_EVENTS_C4_B.tsv` contains six independent audit events, one for each C4.01–C4.06.
- `C1_incidence_audit_B.tex` checks C1.04 completion using full chain-isomorphism groupoids, not only object replacement. It proves atlas independence by local sections, split augmented Čech diagrams and open-cover exit excision, and specifies globally pulled-back orbifold collar data.
- Haine, arXiv1811.01119v6 (27 March2023), Definition1.1.4 and Theorem1.1.7, printedp8, were opened independently. Their complete-Segal proof identifies flag décollages with conservative infinity-categories; this corroborates the C1.B2 category model but does not replace the geometric comparison. Bibliographic key B56Haine2023 is supplied by the B5–6 agent.


---

## Detailed B.5–B.6 proof and correction record

# B.5--B.6 completed contribution and integration notes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority claimed. The complete proofs are in `agent_B56_proofs.md` and their LaTeX conversion `B56.tex` (also `agent_B56.tex`). Metadata: `results_B56.csv`, `references_B56.bib`, `CHECK_EVENTS_B56.tsv`. Do not include fetched full copyrighted literature in the deliverable ZIP; retain bibliographic locators, our proofs, code and outputs.

## Outcomes

B.5 is settled in the precise typed sense given by B5.1--B5.10. Full ordinary comparison epimorphisms are exactly flatness and suffice for homotopy descent even before hypercompletion. The forest collection fails, with checked C2 examples. Exact necessary-and-sufficient local descent is the explicit subdivision-filling scheme B5.10.1 on the simplicial replacement, after hypercompletion. The pro-space comparison has the exact mapping-space tests B5.6.2; the original Artin--Mazur comparison is precisely q of the hypercomplete shape, with exact pi0 tests B5.6.3--4. Verdier comparisons and the symmetric case are explicit; every matching degree is independently indispensable. The supposed strictly-between relationship is false. Slice shapes and component sets must be kept separate, as must original Artin--Mazur Pro(Ho Spaces) and infinity-categorical pro-spaces.

B.6 is settled. The global relation list remains incomplete after both global invariances; a countermodel already appears on arities 1,2,3. A complete replacement follows from opened Grandis Theorem 4.2 by explicit inverse substitutions. The corrected final low-degree list of 151/005 is complete, with hom-cardinality matrix [[1,1,1],[2,4,8],[3,9,27]]. The two sigma3 alternatives in 151/003 and 005 are false. Original scans003,005and017 have now been independently inspected; the boxed003 sigma3, middle005 sigma1, and017 lowerbounds2,3 are clear. The last005 subscript remains visually unresolved; both readings are retained. See ink_B56/INK_REVIEW.md.

## Pivotal corrections to prior study

| Source locator | Finding | Corrected statement |
|---|---|---|
| `study/readings/151_001-017_INTEGRATION.md`, lines 61--68 and 78--83; `151_001-017.md`, lines 303--309 | Hypercovers need not satisfy Hyp2prime, even with symmetric indexing; flat simplicial systems need not be hypercovers | B5.5, B5.7, B5.10 |
| User R8 / `151_001-017.md`, group-nerve paragraph around lines 303--309 | “Realizes to BG” depends on realization | Homotopy colimit and ordinary simplicial realization are BG; finite-group naive symmetric coend is contractible, B5.3 |
| 151/017, boxed four relation families, plus 151/005 global boxes | Still not a complete global presentation | B6.1 countermodel; B6.2 complete replacement |
| 151/005 line 30, unsure subscript 1 or 3 | Only subscript1 is true; original ink remains visually unresolved | B6.3 proves corrected list complete and disproves subscript3 |
| 151/003 line55 vs 151/005 line23 | sigma3 e=e false; sigma1 e=e true | B6.3 independently confirms SA10-K151a-01 mathematically |
| 151/015 line29, single dot as Hyp1 diagram | One-object comparison is an identity | Empty diagram required, B5.1; no new ink claim |

## Computations

- `code_B56/check_B56.py` / `.out`: 14 corrected low-degree relations; all 56 finite maps on arities1--3; 412 typed global countermodel relation instances; four C2 cospans/eight completing squares; H1(BC2;F2) dimension1; 16 symmetric products, 1,528 cospans, 6,871 compatible target pairs; 126 monotone maps; 30 exact-rational symmetric singular-hypercover amalgams. Final recorded run: 0.044837 seconds.
- `code_B56/check_matching_independence.py` / `.out`: 32 GF2 matching comparisons, n=1--4 and k=0--7; unique failed degree k=n+1. Runtime 0.016021 seconds.
- `code_B56/check_stable_graphs_independent.py` / `.out`: independent check of root A4.5, using direct bounded multigraph enumeration instead of inverse contractions. Positive cases graph counts 2,5,23,7 and pair counts1,10,253,21; no failures. Times 0.000044, 0.000146, 0.002840, 0.000157 seconds.

All infinite-family assertions have proofs independently of finite bounds. The normal-form proof, not target verification alone, proves low-degree completeness.

## Primary literature opened

Full URLs, exact theorem locators and access status are in `references_B56.bib`. Grandis 2001, DHI 2004 (arXiv v2 and LaTeX source), HTT, Barnea--Schlank v9, Barnea--Harpaz--Horel 2017 Theorem6.0.4 pp625--626, Curtis 1971, Stacks 019G, and Kerodon 00ZA/00ZH/00ZK are opened and used. The requested Haine1811.01119v6 is fully opened; Definition1.1.4 and Theorem1.1.7 p8 are cited in C1_collage_B.tex for the flag-Segal framework, not used as a premise in B5. Dugger--Isaksen topological hypercovers and Stacks 01GZ were opened for context. Shulman 2012 search metadata was found, but full-text links failed; it is not used as a premise. Searches covered finite-set presentations, flat and covering-flat functors, arbitrary-index hypercovers, local weak equivalences, Artin--Mazur derived realization, symmetric realization, and Ex-infinity. We assert no priority.

## Independent review of parent Part A

A1.2 synchronized pro-Cech proof checked: the truncated simplex category has finitely many objects and morphisms, so the filtered-bicolimit/finite-bilimit interchange is legitimate, while infinite I stays inside each synchronized coproduct. A1.3 plane examples and the connected R2-in-R4 repair checked; identity comparisons on the strata prevent exchanging 0 and1 to repair the mismatch. A4.5 uniform negative families and genus-zero argument checked, and positive finite cases independently enumerated as above. These reviews have own CHECK_EVENTS rows.

## Further completed review

C5_Hurewicz_review.tex/.md and references_C5_Hurewicz.bib close the proper PL/smooth Hurewicz fibre-manifold gate, with independently audited complete constructions and an auxiliary A7 finite quotient certificate. B6.2 now includes explicit cycle words for every Grandis coface/codegeneracy, the full translated relation scheme, and a surjective-generator/composite-isomorphism argument that excludes missing defining equations. check_B6_translation.py/.out checks168 generator words through n12 in0.000609891seconds.


## Final B.5 scope audit

`B5_scope_audit.md` records exact request coverage and all implication directions. The primary BHH theorem explicitly identifies the hypercompleted shape; no inference from local weak equivalence to full nonhypercomplete shape remains. Full flatness still gives the stronger pre-hypercompletion assertion. Symmetric full Hyp implies hypercover strictly; ordinary flatness and hypercover are incomparable. The Artin--Mazur criterion applies pi0 after the limit of mapping spaces and applies q after the pro-space colimit.

`B56.tex` is the directly maintained authoritative proof, with separate B.5 and B.6 section headings. `code_B56/sync_B56_mirrors.py/.out` records the final normalization and regenerated TeX/Markdown mirrors. No hidden generator is required to reconstruct the source. The complete C5 Hurewicz proof and its separate references remain preserved.


---

## Cote150 inherited statements and attached-file corrections

# Audit of inherited cote 150 claims

This records actual checks made in this run, not inherited authority. Source paths and line numbers refer to the supplied, once-unpacked study. Exact primary-source locators and opened status are in C_source_manifest.tsv. The TeX contribution is frozen; this file changes only the research record.

## Main corrections

- Bare a)-c) do not imply pi-control; the original hexagon is nevertheless explicitly called commutative. One radius level records less than a whole radial control germ.
- The raw topological nerve needs a complete-Segal interpretation and, where necessary, Reedy/Rezk replacement. The Exit comparison is a separate coherent collage theorem. Moduli require whole incidence-chain groupoids, including ineffective stabilizers.
- The literal finite recursive section8 data already retain transverse old/new collars, so the cutting gives precylindricity. Manifoldness is a further local criterion. Ordinary coarse moduli can fail it in the interior.
- Proper Hurewicz fibrancy is weaker than PL bundle or smooth regular source data. The PL and smooth mixed-manifold assertions are false for raw fibrancy. The proper smooth u-to-u-squared source also refutes automatic smooth collar transversality.
- Finite-dimensional connected TOP components do not suffice for the component-order conclusion. The full collared ray/pseudoarc counterexample satisfies the geometric hypotheses. Open path-connected components, or open proper sources, give corrected statements.
- Finite metric HSS suffice for the pro-neighbourhood comparisons; full Mather radial control is not necessary there. For V_d versus an actual face, cofinal radii must vary recursively, producing horn regions. Arbitrary sheaf cohomology uses an exact cover, not a homotopy replacement.

## Exact inherited-ID table

| Prior ID | Supplied source and line | Current result | New proof |
|---|---|---|---|
| SA10-R150b-11 | sources/RESEARCH_SA10_study/study/readings/150_017-030_CHECK_EVENTS.tsv:12 | Used part re-proved | C1.03;C2.05 |
| SA10-R150b-21 | sources/RESEARCH_SA10_study/study/readings/150_017-030_CHECK_EVENTS.tsv:22 | Qualified and completed | C3.01;C3.04 |
| SA10-R150c-14 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:15 | Used and re-proved | C1.03;C3.04 |
| SA10-R150c-16 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:17 | Used and re-proved | C1.03;C3.04 |
| SA10-R150c-19 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:20 | Confirmed with incidence qualification | C1.04;C3.02-C3.04 |
| SA10-R150c-20 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:21 | Confirmed under typed fibrancy | C1.01-C1.02;C1.04 |
| SA10-R150c-21 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:22 | Confirmed under typed fibrancy | C1.01-C1.02;C1.04 |
| SA10-R150c-23 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:24 | Confirmed by explicit example | C1.04 |
| SA10-K150c-15 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CORRECTIONS.tsv:16 | Confirmed by explicit example | C1.04 |
| SA10-R150c-30 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:31 | Confirmed with exact finite certificate | C3.02 |
| SA10-R150c-31 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:32 | Confirmed and strengthened | C1.02;C1.B1-C1.B3 |
| SA10-R150c-32 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:33 | Confirmed and strengthened | C1.02;C1.B1-C1.B3 |
| SA10-K150c-14 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CORRECTIONS.tsv:15 | Confirmed and strengthened | C1.02;C1.B1-C1.B3 |
| SA10-R150c-37 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:38 | Confirmed original slip; construction completed | C1.03 |
| SA10-R150c-41 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CHECK_EVENTS.tsv:42 | Confirmed original slip; construction completed | C1.03 |
| SA10-K150c-12 | sources/RESEARCH_SA10_study/study/readings/150_031-043_CORRECTIONS.tsv:13 | Confirmed original slip; construction completed | C1.03 |
| SA10-R150e-16 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:17 | Confirmed with textual qualification | C2.01-C2.02 |
| SA10-R150e-17 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:18 | Confirmed with textual qualification | C2.01-C2.02 |
| SA10-K150e-02 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:3 | Confirmed with textual qualification | C2.01-C2.02 |
| SA10-R150e-34 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:35 | Confirmed typed correction | C2.01-C2.02 |
| SA10-K150e-01 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:2 | Confirmed typed correction | C2.01-C2.02 |
| SA10-R150d-23 | sources/RESEARCH_SA10_study/study/readings/150_044-057_CHECK_EVENTS.tsv:24 | Confirmed and strengthened | C5.04-C5.05 |
| SA10-K150d-08 | sources/RESEARCH_SA10_study/study/readings/150_044-057_CORRECTIONS.tsv:9 | Confirmed and strengthened | C5.04-C5.05 |
| SA10-R150e-21 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:22 | Confirmed and strengthened | C5.04-C5.05 |
| SA10-K150e-08 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:9 | Confirmed and strengthened | C5.04-C5.05 |
| SA10-R150d-25 | sources/RESEARCH_SA10_study/study/readings/150_044-057_CHECK_EVENTS.tsv:26 | TOP part confirmed; unconditional PL/smooth extension refuted | C5.03;C5.05-C5.06 |
| SA10-K150d-09 | sources/RESEARCH_SA10_study/study/readings/150_044-057_CORRECTIONS.tsv:10 | TOP part confirmed; unconditional PL/smooth extension refuted | C5.03;C5.05-C5.06 |
| SA10-R150e-14 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:15 | TOP part confirmed; unconditional PL/smooth extension refuted | C5.03;C5.05-C5.06 |
| SA10-K150e-07 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:8 | TOP part confirmed; unconditional PL/smooth extension refuted | C5.03;C5.05-C5.06 |
| SA10-R150e-10 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:11 | Bare independence confirmed; fibrant/local-trivial conflation corrected | C5.02;C5.05;C5.08 |
| SA10-K150e-09 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:10 | Bare independence confirmed; fibrant/local-trivial conflation corrected | C5.02;C5.05;C5.08 |
| SA10-K150e-05 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:6 | Source reading used; alternative treated explicitly | C5.08 |
| SA10-R150e-23 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:24 | Confirmed for path components; connected scope qualified | C5.01;C5.07-C5.08 |
| SA10-K150e-11 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:12 | Confirmed for path components; connected scope qualified | C5.01;C5.07-C5.08 |
| SA10-R150e-26 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:27 | Unrestricted TOP conclusion refuted; stronger corrections proved | C5.01;C5.07-C5.08 |
| SA10-K150e-12 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:13 | Unrestricted TOP conclusion refuted; stronger corrections proved | C5.01;C5.07-C5.08 |
| SA10-R150f-02 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:3 | Unrestricted TOP conclusion refuted; stronger corrections proved | C5.01;C5.07-C5.08 |
| SA10-K150f-13 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CORRECTIONS.tsv:14 | Unrestricted TOP conclusion refuted; stronger corrections proved | C5.01;C5.07-C5.08 |
| SA10-R150e-27 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:28 | Conditional proof confirmed; unrestricted scope refuted | C5.01;C5.07-C5.08 |
| SA10-R150e-28 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:29 | Conditional proof confirmed; unrestricted scope refuted | C5.01;C5.07-C5.08 |
| SA10-R150e-29 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:30 | Conditional proof confirmed; unrestricted scope refuted | C5.01;C5.07-C5.08 |
| SA10-K150e-17 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CORRECTIONS.tsv:18 | Conditional proof confirmed; unrestricted scope refuted | C5.01;C5.07-C5.08 |
| SA10-R150e-30 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:31 | Conditional proof confirmed; unrestricted scope refuted | C5.01;C5.07-C5.08 |
| SA10-R150e-32 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:33 | Used and re-proved with completion qualification | C1.02-C1.04;C1.B1-C1.B3 |
| SA10-R150e-33 | sources/RESEARCH_SA10_study/study/readings/150_058-071_CHECK_EVENTS.tsv:34 | Used and re-proved with completion qualification | C1.02-C1.04;C1.B1-C1.B3 |
| SA10-R150f-13 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:14 | Strengthened; Mather control not necessary for these pro comparisons | C4.01 |
| SA10-R150f-16 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:17 | Strengthened; Mather control not necessary for these pro comparisons | C4.01 |
| SA10-R150f-19 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:20 | Strengthened; Mather control not necessary for these pro comparisons | C4.01 |
| SA10-R150f-29 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:30 | Strengthened; Mather control not necessary for these pro comparisons | C4.01 |
| SA10-R150f-30 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:31 | Confirmed failure without domination | C4.01-C4.02 |
| SA10-R150f-28 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:29 | Confirmed with actual sheaf cover and finite scope | C4.03 |
| SA10-R150f-33 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:34 | Confirmed with actual sheaf cover and finite scope | C4.03 |
| SA10-R150f-34 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:35 | Confirmed with actual sheaf cover and finite scope | C4.03 |
| SA10-R150f-35 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:36 | Confirmed against original scans | C4.06 |
| SA10-K150f-14 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CORRECTIONS.tsv:15 | Confirmed against original scans | C4.06 |
| SA10-R150f-36 | sources/RESEARCH_SA10_study/study/readings/150_072-084_CHECK_EVENTS.tsv:37 | Confirmed with a repaired cofinality argument | C4.05 |

## Detailed dispositions

### SA10-R150b-11

The cone quotient and collar-absorption reconstruction used here are proved by explicit quotient maps. No broader untyped category of all continuous maps is inferred.

### SA10-R150b-21

The local cubical product is correct. It is a manifold with the specified corners exactly when its transverse open-face base is a manifold in the chosen category; the Cantor product refutes an unconditional manifold conclusion.

### SA10-R150c-14

For the actual finite recursive data, retained old and new boundary collars are part of /036(22). Their product compatibility gives the induction and topological reconstruction without source fibrancy. Original /036 visually checked.

### SA10-R150c-16

For the actual finite recursive data, retained old and new boundary collars are part of /036(22). Their product compatibility gives the induction and topological reconstruction without source fibrancy. Original /036 visually checked.

### SA10-R150c-19

A global stratum orbit-poset can forget local branches and self-incidences. The moduli statement uses fixed incidence chains and full automorphism groupoids; manifoldness of the coarse space is a separate issue.

### SA10-R150c-20

Nonfinal flag deletions are the collared face embeddings. Initial-segment maps are composites of base changes of the assumed source fibrations; weak mapping-cone data do not imply those fibrations.

### SA10-R150c-21

Nonfinal flag deletions are the collared face embeddings. Initial-segment maps are composites of base changes of the assumed source fibrations; weak mapping-cone data do not imply those fibrations.

### SA10-R150c-23

For Mbar_0,4 use three point objects, a sphere with three open discs removed, and three boundary circles. The cylinders fill the three discs and recover S2. Literal open strata or boundary-circle point objects are different conventions.

### SA10-K150c-15

For Mbar_0,4 use three point objects, a sphere with three open discs removed, and three boundary circles. The cylinders fill the three discs and recover S2. Literal open strata or boundary-circle point objects are different conventions.

### SA10-R150c-30

The interval of flags with fixed final vertex is Boolean. Exhaustive naturally-labelled posets of sizes0..5 give4135 flags and10603 tested intervals; the subset proof covers every finite size.

### SA10-R150c-31

Strict Segal reconstruction is valid with only identity arrows over identical grades. Hurewicz source fibrations make the pullbacks homotopy pullbacks. Raw Reedy fibrancy is not automatic; geometric Exit identification requires the separate collage proof.

### SA10-R150c-32

Strict Segal reconstruction is valid with only identity arrows over identical grades. Hurewicz source fibrations make the pullbacks homotopy pullbacks. Raw Reedy fibrancy is not automatic; geometric Exit identification requires the separate collage proof.

### SA10-K150c-14

Strict Segal reconstruction is valid with only identity arrows over identical grades. Hurewicz source fibrations make the pullbacks homotopy pullbacks. Raw Reedy fibrancy is not automatic; geometric Exit identification requires the separate collage proof.

### SA10-R150c-37

Original /043 genuinely writes p=long d-prime. The selected-prefix count is p=cardinality(d). The full colimit needs three transition families, including initial-prefix identifications; the two-point counterexample and cell-quotient program verify their necessity.

### SA10-R150c-41

Original /043 genuinely writes p=long d-prime. The selected-prefix count is p=cardinality(d). The full colimit needs three transition families, including initial-prefix identifications; the two-point counterexample and cell-quotient program verify their necessity.

### SA10-K150c-12

Original /043 genuinely writes p=long d-prime. The selected-prefix count is p=cardinality(d). The full colimit needs three transition families, including initial-prefix identifications; the two-point counterexample and cell-quotient program verify their necessity.

### SA10-R150e-16

The twist counterexample is valid for bare a)-c), and a compact smooth enhancement verifies the other geometric clauses. However /065 already calls its hexagon commutative: if that is included as an axiom, pi-control is written. The invalid inference is that commutativity follows from the bare subset identities.

### SA10-R150e-17

The twist counterexample is valid for bare a)-c), and a compact smooth enhancement verifies the other geometric clauses. However /065 already calls its hexagon commutative: if that is included as an axiom, pi-control is written. The invalid inference is that commutativity follows from the bare subset identities.

### SA10-K150e-02

The twist counterexample is valid for bare a)-c), and a compact smooth enhancement verifies the other geometric clauses. However /065 already calls its hexagon commutative: if that is included as an axiom, pi-control is written. The invalid inference is that commutativity follows from the bare subset identities.

### SA10-R150e-34

The inverse image must be s_jk^{-1}(Sigma_ij) inside Sigma_jk. The written b_ij^{-1} has the wrong ambient space.

### SA10-K150e-01

The inverse image must be s_jk^{-1}(Sigma_ij) inside Sigma_jk. The written b_ij^{-1} has the wrong ambient space.

### SA10-R150d-23

TOP face-manifold deduction is false, now with compact F times square and every source proper Hurewicz. PL/smooth collar cancellation and the full boundary formula hold in those categories.

### SA10-K150d-08

TOP face-manifold deduction is false, now with compact F times square and every source proper Hurewicz. PL/smooth collar cancellation and the full boundary formula hold in those categories.

### SA10-R150e-21

TOP face-manifold deduction is false, now with compact F times square and every source proper Hurewicz. PL/smooth collar cancellation and the full boundary formula hold in those categories.

### SA10-K150e-08

TOP face-manifold deduction is false, now with compact F times square and every source proper Hurewicz. PL/smooth collar cancellation and the full boundary formula hold in those categories.

### SA10-R150d-25

TOP fails even for a genuine locally trivial bundle. Proper PL and smooth maps that are Hurewicz fibrations can also have a nonmanifold fibre, by the boundary-spin/Ferry construction. Positive PL-bundle and full smooth-source-system statements are proved with their exact regularity assumptions.

### SA10-K150d-09

TOP fails even for a genuine locally trivial bundle. Proper PL and smooth maps that are Hurewicz fibrations can also have a nonmanifold fibre, by the boundary-spin/Ferry construction. Positive PL-bundle and full smooth-source-system statements are proved with their exact regularity assumptions.

### SA10-R150e-14

TOP fails even for a genuine locally trivial bundle. Proper PL and smooth maps that are Hurewicz fibrations can also have a nonmanifold fibre, by the boundary-spin/Ferry construction. Positive PL-bundle and full smooth-source-system statements are proved with their exact regularity assumptions.

### SA10-K150e-07

TOP fails even for a genuine locally trivial bundle. Proper PL and smooth maps that are Hurewicz fibrations can also have a nonmanifold fibre, by the boundary-spin/Ferry construction. Positive PL-bundle and full smooth-source-system statements are proved with their exact regularity assumptions.

### SA10-R150e-10

The bare other axioms do not imply collar transversality. Local product triviality of the full face diagram suffices. Merely smooth proper Hurewicz sources do not suffice: the compact u-to-u-squared example is a homeomorphism on each source component but has zero normal derivative.

### SA10-K150e-09

The bare other axioms do not imply collar transversality. Local product triviality of the full face diagram suffices. Merely smooth proper Hurewicz sources do not suffice: the compact u-to-u-squared example is a homeomorphism on each source component but has zero normal derivative.

### SA10-K150e-05

The source letter is consistent with /062 p1 and /065-066. If the doubtful alternative b is read literally, product-collar transversality of a nonempty target boundary embedding to itself is impossible, rather than an automatic condition; the strict-arrow case then becomes empty.

### SA10-R150e-23

Path lifting gives the pullback surjection on path components. The unrestricted statement for connected components is false; the collared pseudoarc-ray counter satisfies the stated TOP hypotheses. Locally path-connected cases and the open proper-source alternative are proved.

### SA10-K150e-11

Path lifting gives the pullback surjection on path components. The unrestricted statement for connected components is false; the collared pseudoarc-ray counter satisfies the stated TOP hypotheses. Locally path-connected cases and the open proper-source alternative are proved.

### SA10-R150e-26

Finite connected dimension alone is insufficient: a compact finite-dimensional connected ray compactification has a strict internal arrow with proper Hurewicz source and collared target. For ordered spaces with open path-connected components no dimension assumption is needed. General-category manifold and PL proofs use local sections and invariance of domain, without assuming local triviality.

### SA10-K150e-12

Finite connected dimension alone is insufficient: a compact finite-dimensional connected ray compactification has a strict internal arrow with proper Hurewicz source and collared target. For ordered spaces with open path-connected components no dimension assumption is needed. General-category manifold and PL proofs use local sections and invariance of domain, without assuming local triviality.

### SA10-R150f-02

Finite connected dimension alone is insufficient: a compact finite-dimensional connected ray compactification has a strict internal arrow with proper Hurewicz source and collared target. For ordered spaces with open path-connected components no dimension assumption is needed. General-category manifold and PL proofs use local sections and invariance of domain, without assuming local triviality.

### SA10-K150f-13

Finite connected dimension alone is insufficient: a compact finite-dimensional connected ray compactification has a strict internal arrow with proper Hurewicz source and collared target. For ordered spaces with open path-connected components no dimension assumption is needed. General-category manifold and PL proofs use local sections and invariance of domain, without assuming local triviality.

### SA10-R150e-27

Once no strict arrow remains inside a component, the component partial order, redundant monomorphism condition, and incomparable incoming-face disjointness follow. C5.01 proves that premise for the stated path-connected scope; C5.07 refutes it for arbitrary connected TOP components.

### SA10-R150e-28

Once no strict arrow remains inside a component, the component partial order, redundant monomorphism condition, and incomparable incoming-face disjointness follow. C5.01 proves that premise for the stated path-connected scope; C5.07 refutes it for arbitrary connected TOP components.

### SA10-R150e-29

Once no strict arrow remains inside a component, the component partial order, redundant monomorphism condition, and incomparable incoming-face disjointness follow. C5.01 proves that premise for the stated path-connected scope; C5.07 refutes it for arbitrary connected TOP components.

### SA10-K150e-17

Once no strict arrow remains inside a component, the component partial order, redundant monomorphism condition, and incomparable incoming-face disjointness follow. C5.01 proves that premise for the stated path-connected scope; C5.07 refutes it for arbitrary connected TOP components.

### SA10-R150e-30

Once no strict arrow remains inside a component, the component partial order, redundant monomorphism condition, and incomparable incoming-face disjointness follow. C5.01 proves that premise for the stated path-connected scope; C5.07 refutes it for arbitrary connected TOP components.

### SA10-R150e-32

The two-stratum realization is the mapping-cylinder gluing. Complete-Segal/Exit comparison is now proved under proper recursive conical collars. Mapping spaces are homotopy fibres of (s,b); a geometric outgoing link retains its variable target and is not automatically the mapping space to one fixed point in a noncontractible target stratum.

### SA10-R150e-33

The two-stratum realization is the mapping-cylinder gluing. Complete-Segal/Exit comparison is now proved under proper recursive conical collars. Mapping spaces are homotopy fibres of (s,b); a geometric outgoing link retains its variable target and is not automatically the mapping space to one fixed point in a noncontractible target stratum.

### SA10-R150f-13

For finite metric HSS, one fixed Quinn nearly strict stratum-preserving deformation and cofinal shrinking prove (51),(56),(57),(69) as compatible pro-homotopy equivalences. Independent retractions at separate levels would not suffice. Domination remains required.

### SA10-R150f-16

For finite metric HSS, one fixed Quinn nearly strict stratum-preserving deformation and cofinal shrinking prove (51),(56),(57),(69) as compatible pro-homotopy equivalences. Independent retractions at separate levels would not suffice. Domination remains required.

### SA10-R150f-19

For finite metric HSS, one fixed Quinn nearly strict stratum-preserving deformation and cofinal shrinking prove (51),(56),(57),(69) as compatible pro-homotopy equivalences. Independent retractions at separate levels would not suffice. Domination remains required.

### SA10-R150f-29

For finite metric HSS, one fixed Quinn nearly strict stratum-preserving deformation and cofinal shrinking prove (51),(56),(57),(69) as compatible pro-homotopy equivalences. Independent retractions at separate levels would not suffice. Domination remains required.

### SA10-R150f-30

For a reversed incident pair, V_J^L is empty while the overlapping tube germ is nonempty; the domination condition is retained. Strict-holink language separately requires disjoint bands; overlap uses the all-paths relative model.

### SA10-R150f-28

Choose upper-band neighbourhoods inside the open upper union, so the covering equality is stagewise exact. The finite flag-poset/flabby double complex proves (73); no homotopy invariance of arbitrary coefficient sheaves is used.

### SA10-R150f-33

Choose upper-band neighbourhoods inside the open upper union, so the covering equality is stagewise exact. The finite flag-poset/flabby double complex proves (73); no homotopy invariance of arbitrary coefficient sheaves is used.

### SA10-R150f-34

Choose upper-band neighbourhoods inside the open upper union, so the covering equality is stagewise exact. The finite flag-poset/flabby double complex proves (73); no homotopy invariance of arbitrary coefficient sheaves is used.

### SA10-R150f-35

Str_inf is cote147. Original147/173-177, including(286)-(294), were opened visually. The quotient puncture removes every coordinate hyperplane, not only the zero section.

### SA10-K150f-14

Str_inf is cote147. Original147/173-177, including(286)-(294), were opened visually. The quotient puncture removes every coordinate hyperplane, not only the zero section.

### SA10-R150f-36

Actual compatible proper conical tubes give cofinal triangular variable-radius regions, not fixed rectangles over the deepest face. Their natural projection and the inward-face homotopy yield V_d equivalent to Sigma_d. HSS alone need not provide an actual deployed collar model.

## Scope boundary

No divisibility or dense-order assumption from the separate SA21 material is imported. Nonfaithful gradings retain component incidences; ineffective orbifold actions retain their full stabilizers. Empty labels, disconnected strata, rank-zero normal quotients, and empty diagrams are treated explicitly. The finite manuscript scope is not silently extended to arbitrary non-locally-finite families.


---

## C5 Hurewicz construction and discarded source route

# Independent resolution of the C.5 Hurewicz gate

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), `/root/hypercovers_finite_sets`, 19 November 2026. No priority claimed. Full proof and exact maps: `C5_Hurewicz_review.tex`. Bibliography: `references_C5_Hurewicz.bib`. Please integrate as C5.06 (or parent-selected numbering). This supersedes the earlier suggestion to apply Chapman directly to a PL collapse map.

## Result

There is a proper PL Hurewicz fibration from a closed PL six-manifold to the circle with a nonmanifold fibre. Separately there is a smooth proper Hurewicz fibration from a closed smooth six-manifold to the circle with a nonmanifold fibre and exactly one critical point. Thus mere proper Hurewicz fibrancy does not imply the fibre-manifold statements of 150/051 and 150/063, even in the PL or smooth category. Positive statements require PL bundle or neat smooth submersion hypotheses (or another genuinely stronger hypothesis that is separately justified). The face-manifold claim of 150/067 is a different statement and is unaffected by this counterexample.

## Construction and proof structure

1. Start with a smooth contractible Mazur four-manifold A having nontrivial boundary group. Raise its dimension by a boundary spin, not by multiplying by an interval: W=(A×S1)∪(D3×D2), attaching along D3×S1. Van Kampen kills the circle and Mayer–Vietoris shows acyclicity, so W is contractible. Its boundary is the spin of ∂A, and has the same nontrivial fundamental group.
2. Let M=double(W). Since W×I is a contractible six-manifold with simply connected boundary, the h-cobordism theorem shows W×I=D6 and M=S5.
3. Collapse only W×{0} inside M×S1. Project to S1. All regular fibres are M; the exceptional fibre Y=M/W has local model cone(∂W) and is not a manifold because the punctured local fundamental group is nontrivial and persistent. Local homology excludes a boundary point.
4. Establish Hurewicz lifting for this ordinary quotient map using Ferry's exact strong-regularity theorem. The collapse f:M→Y has homotopy inverses and inverse homotopies supported in arbitrarily small collar enlargements A_eta of W. Construct them by extending a contraction of W within W to A_eta, fixed on its outer boundary, using the homotopy extension property of the compatible polyhedral pair. The final map factors through the quotient; the whole homotopy descends after postcomposing with the quotient. This simpler version was supplied in the C agent’s independent audit. In the quotient total space, the supports at small base heights have arbitrarily small diameter. This proves all of Ferry's movement estimates, not merely homotopy equivalence of fibres.
5. Obtain a PL map by replacing a polyhedral neighbourhood of the collapsed W with the abstract cone on its sphere boundary, and using linear cone extension of the height. A complete explicit height-preserving homeomorphism with the ordinary quotient is given. There is no assumption that the original collapse map is PL.
6. Obtain a smooth map independently using a smooth vector field V=beta(s)∂s+t∂t, with beta positive outside W and flat at its boundary. A suitable smooth Lyapunov neighbourhood has sphere boundary. Backward flow gives the exact local formula p(r,theta)=r h(theta), with h smooth and zero a regular value. Radial domain reparametrization r→g(r), flat at zero and identity near the outer boundary, makes p=g(r)h(theta) smooth, preserves the Hurewicz property by a domain homeomorphism, and has a unique critical point.
7. Put Sigma0=S1, Sigma1=E×I, Sigma01=E×∂I, target the whole-boundary embedding and source p on each component. There are no strict triples, and Sigma0 has no boundary. The manuscript properness, Hurewicz source and object-manifold hypotheses hold, but the fibre Y disjoint-union Y is not a manifold.

The proof is now complete. The C agent independently audited the PL cone, smooth flow and Ferry arguments and reported that they pass; his HEP simplification of the inverse-homotopy construction is incorporated. Every mathematical gate from the preliminary Chapman route has been replaced with a direct argument and an opened theorem.

## Opened sources and exact status

- **Used, primary full text:** E. C. Zeeman, *On the dunce hat*, Topology2(1964),341–358, printed p.347, passage before Theorem(5). It explicitly constructs the Mazur manifold and records the nonzero boundary fundamental group, with locator Mazur1961 p.227. Dotted M is boundary notation; visually inspected. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/dunce001.pdf
- **Used, primary full text:** J. Milnor, *Lectures on the h-Cobordism Theorem*, Princeton1965, Theorem9.1 p.107, PropositionA pp.108–109; PDF zero-based pages111–113. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hcobord.pdf
- **Used, primary full text:** S. Ferry, *Strongly regular mappings with compact ANR fibers are Hurewicz fiberings*, PacificJMath75(1978),373–382, Definition p.373, Theorem1 pp.373–374. This is the exact theorem used for lifting. https://msp.org/pjm/1978/75-2/pjm-v75-n2-p07-s.pdf
- **Auxiliary only, book full text:** D. Rolfsen, *Knots and Links*, §11E pp.355–357, Exercise3 p.356; corrected AMS2003 scan visually inspected. The boundary group presentation is used solely for a finite nontrivial quotient certificate. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rolfsen.pdf
- **Opened, consulted, not used as a premise:** T. A. Chapman, *Piecewise linear fibrations*, PacificJMath128(1987),223–250, §2 p.227 item3. Its cylinder is simplicial, and the ordinary collapse of a codimension-zero W need not itself be PL. Direct application to our ordinary collapse was withdrawn. https://msp.org/pjm/1987/128-2/pjm-v128-n2-p02-s.pdf
- **Opened, consulted, not used as a premise:** M. M. Cohen, *Simplicial structures and transverse cellularity*, AnnMath85(1967),218–245, §4 p.225, §9 Props9.3–9.8 pp.238–240, Prop10.2' p.241. The simplicial/topological cylinder homeomorphism is not stated to preserve the required ordinary height, and standard extensions can add convex-cell fibres. We therefore avoided this route. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mcohen.pdf
- **Opened, corroboration only:** E. C. Zeeman, *A note on an example of Mazur*, AnnMath76(1962),235–236. https://www.lms.ac.uk/sites/default/files/1962%20A%20note%20on%20an%20example%20of%20Mazur.pdf
- **Opened abstract only, not used:** D. F. Addis, *A strong regularity condition on mappings*, GeneralTopologyAppl2(1972),199–213. Full-text fetch failed. Ferry provides the needed opened full theorem.
- **Original Mazur1961 full text not opened:** DOI10.2307/1970288; the bibliography/abstract was opened, JSTOR displayed no full text. No claim of opening that original article is made; the used primary source is Zeeman1964.

Fetched full copyrighted sources, OCRs and source screenshots under `references_B56/` are research scratch and must be excluded from the deliverable ZIP. Include our proofs, bibliographic locators, check events, scripts and outputs.

## Finite certificate

`code_B56/check_C5_boundary_group.py` and `.out` independently check the group presentation

    <x,y | y^5=x^7, y^4=x^2*y*x^2>

with permutations x=(0 1 2 3 4 5 6), y=(0 3 1 4 2). All 504 five-cycles are checked for fixed x; 14 solve the relation. The chosen pair generates A7, of order2520. Both relators are explicitly evaluated. UTC run2026-11-19T04:58:03.585352, runtime0.006783651seconds. This proves nontriviality of the recorded group; it does not replace geometric verification of a handle presentation.

## Other independent Part C checks

C1.03 simultaneous-cylinder formula originally omitted lower-prefix identifications. For I={0<1} and all Sigma spaces a point, the old transition families preserve max(e) and leave an isolated Sigma0 beside the interval. This was reported, acknowledged and corrected by the C agent using the additional maps C(d∩e_<a,e_≤a)→C(d,e) for every selected a∈d. A finite interval certificate is owned by the C agent.

For resolution, Albin2016 Theorem6.3(a–c), printed p.48, was opened and sent to C agent, together with the warning that collective boundary hypersurfaces retain disconnected links. ALMP2012 Props2.3 and2.7 use a minimal/connected-fibre collapse convention and cannot silently replace Albin's full collective statement in the nonnormal case.

## Follow-up original-source retrieval, 05:19–05:21 UTC

The exact original is Barry Mazur, *A note on some contractible 4-manifolds*, Annals of Mathematics73(1961)221–228, DOI <https://doi.org/10.2307/1970288>. Searches by full title, DOI and author-hosted location found its JSTOR record and Celebratio bibliography/abstract. The direct PDF <https://www.jstor.org/stable/pdf/1970288.pdf> and DOI redirect were inaccessible to the retrieval tool; the landing page exposed no paper text. **The Mazur original remains not opened.** Bibliographic metadata and a reproduced abstract are not treated as a full-text opening.

The primary E.C.Zeeman, *A Note on an Example of Mazur*, Annals76(1962)235–236, was fully opened at <https://www.lms.ac.uk/sites/default/files/1962%20A%20note%20on%20an%20example%20of%20Mazur.pdf>. Its p236 describes the handle construction and the untwisting after multiplication by an interval. It does not supply the boundary-group calculation, so it is contextual and is not an additional premise of the proof. The existence and auxiliary group claims continue to use the actually opened Zeeman1964p347 and Rolfsen11E.3p356, with their respective scope stated above.


---

## Independent C5 boundary/category audit

# Independent final audit of C5.04, C5.05, C5.07, C5.08

Auditor: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/homotopy_levels`; 19 November 2026. This records actual targeted checks, not an additional theorem or an independent source attribution.

I read the final sections in `C_sections.tex`, the complete Hurewicz example in `C5_Hurewicz_C.tex` insofar as it bears on the matrix, and the transcriptions of 150/051, /062, /063, /067, /070, and /071. I also visually opened all six corresponding primary-scan PNGs in `work/literature_C`. The connected-component wording on /070–071 is clear. The two readings of /051(d) must remain distinguished: an attempted consequence versus an extra manifold-face axiom. The uncertain source letter on /063(d) is handled in the paper by the typed source interpretation from /062; no new palaeographic certainty is claimed here.

## C5.04: passes the full hypothesis check

The compact square version satisfies the surrounding hypotheses, including properness of every source. The square is locally a plane or half-plane, including at its vertices; since `F × R` is a five-manifold, `F × [0,1]^2` is a six-manifold with boundary `F × S^1`. Each specified collective incoming face is closed and properly embedded, the two face collars form the explicit product coordinates, their intersection is the stated source inverse image, and projection control holds. The source `s12` is a product Hurewicz bundle with compact fibre `F ⨿ F`; the remaining source maps have point targets and compact domains. The lower interval at a corner is the three-element chain, so the order condition also holds.

The nonmanifold-face conclusion is valid. At an interval-interior point, `F × [0,1]` is a five-manifold. At an interval endpoint its local homology vanishes in every degree. If it were a manifold with boundary, its entire intrinsic boundary would therefore be `F × {0,1}`, which is not a manifold. This refutes the attempted inference in /067 and the consequence reading of /051(d), without claiming to satisfy the alternate extra axiom that every flag space is already a manifold.

## C5.05: passes after the identified boundary-regularity clarification

The PL cancellation argument uses the product PL structure, not a topological cancellation assertion. A product simplex over a top-dimensional simplex of the Euclidean factor has the same normal PL link as the relevant vertex of the fibre. The manifold link criterion therefore gives the fibre's PL manifold structure. The stated PL-bundle hypothesis is stronger than Hurewicz fibrancy, as required.

The smooth argument must explicitly establish submersion on the vertical corner faces before using a corner submersion/Ehresmann argument. In the full incidence system this follows from the existing hypotheses, rather than becoming an extra conclusion assumed in advance. For `i < k < j`, projection control gives

`sij|Σikj = sik ∘ (skj|Σikj)`.

The restricted second map to `Σik` is a submersion by the horizontal pullback and product-collar condition, and the first map is a submersion by the regular-source assumption. Iterating gives the same statement on every vertical corner stratum. Horizontal lifts can then be chosen tangent to all vertical faces; local partitions of unity preserve those linear tangency conditions, and properness permits their flows over a sufficiently small base chart. The horizontal base-boundary coordinates are handled by the supplied product collars. This proves the intended corner-bundle conclusion. An isolated proper smooth submersion with only horizontal behavior would not suffice; this logical step was sent to the root and C owner for insertion.

The boundary decomposition into horizontal lower-label faces and vertical intermediate-label faces then follows from the full incoming-face decomposition and the source inverse-image identities. It does not conflate the intrinsic boundary of the fibre with the whole boundary of the arrow space.

## C5.07: passes, including the full Hurewicz property

The pseudoarc argument proves that every path in the remainder is constant: a nonconstant path image would express an indecomposable subcontinuum as a finite union of proper continua. The ray construction is compact and connected, and its cluster set is precisely the chosen nondegenerate continuum. A path entering the ray from the remainder would have ray parameter tending to infinity. The intermediate value theorem forces every sufficiently short path interval to visit an entire ray tail; continuity would force that whole tail to converge to a single remainder point, contradicting its cluster set. Thus the specified source point has singleton path component.

The strict arrow is an isolated clopen component of the closed relation. Both projections are proper; the target is locally embedded and its one strict target germ is genuinely collared at the endpoint of the ray. The source lifting proof works for every parameter space: split it into the clopen inverse image of the strict arrow and its complement, then use the constant strict lift and the diagonal lift. This is Hurewicz lifting, not merely path lifting. Transversality is vacuous on the strict component because its source is outside the target collar, and is the identity on the diagonal. The single connected component is open and has finite covering dimension. The extra monomorphism condition for distinct components is vacuous. The example therefore refutes the literal connected-component scope of /070–071 even with all the additional hypotheses listed in the section.

## C5.08: the manifold/category argument passes

The identity section is closed as an equalizer in a Hausdorff arrow space. It is open because target-local injectivity, together with continuity of the identity section, makes a sufficiently small target chart contain only the identities over a smaller base neighborhood. Strict arrows are consequently clopen, so source lifts preserve strictness and keep their target in the same component.

For a hypothetical strict arrow inside one manifold component, source path lifting moves its source into an interior coordinate ball. The Hurewicz lifting property applied to a contraction of that ball gives a continuous source section. After shrinking, its image lies in a target-injective arrow chart; composing with the target gives an injection of an open `n`-ball into an `n`-dimensional target corner chart. Invariance of domain forces its image to be open in Euclidean `n`-space and hence to avoid the orthant boundary. Its target image is therefore open in the component, contradicting the assumed locally nowhere-dense strict target germ. Dimension zero is covered directly. The proof is valid for manifolds with boundary and corners.

Transitivity follows by source lifting to align middle objects. If component arrows exist in both directions, the two resulting composites lie within components and must be identities; the arrows are inverse, contradicting the assumption that all invertibles are identities unless the components coincide. No thinness is used in this argument. The later monomorphism conclusion correctly returns to ordered spaces with totally ordered lower intervals.

For the PL-polyhedron extension, the target local embedding must explicitly be PL, so its locally rare image has a compatible local triangulation of dimension at most `n−1`. The compact-subball/Baire argument then excludes an embedded open `n`-ball in that image. This precision was sent for insertion. The matrix correctly distinguishes raw proper Hurewicz fibrancy, regular PL bundles, regular smooth sources, and the stronger full-face product-triviality hypothesis. The raw PL/smooth Hurewicz example has manifold arrow spaces as well as manifold objects, so it remains a counterexample under the stronger reading of /051(d).

## Outcome

No remaining mathematical gap was found in C5.04, C5.07, or the general manifold/category part of C5.08. C5.05 and the PL extension of C5.08 require the two explicit clarifications above; both have been transmitted for integration. The examples and positive statements otherwise have the claimed manuscript scope.


---

## Final publication verification

# Final PDF publication check

**PASS.** The published LuaLaTeX PDF has **74 pages** and **762,332 bytes**. Its SHA256 is `1786ba59ec32382ec60392f23bd95ef926d14872f851478dbeb0771e12a79301`.

| Metric | Last retained failing draft | Final PDF |
|---|---:|---:|
| Overfull boxes, all sizes | 7 | 2 |
| Overfull boxes exceeding2pt | 4 | 0 |
| Largest overfull box | 142.84079pt | 1.42430pt |
| Missing-character warnings | See retained draft log | 0 |
| Undefined citations | See retained draft log | 0 |

The baseline is `logs/build_history/20261119T052014525518Z/build_pass2.out`. Its four excessive boxes are15.27339,142.84079,97.10779 and13.91151pt. Earlier intermediate failures remain in the build history; this comparison does not silently count only one of those earlier errors as the entire history. The final source repairs the affected titles, raw paths/URLs and obsolete metadata. Final successful build time: 23.495529s. Poppler render time: 23.081229s.

Every page was rendered at110dpi and visually reviewed in seven contact sheets. **49 distinct full pages** were separately inspected: 1, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29, 31, 33, 35, 36, 37, 42, 43, 45, 47, 48, 50, 55, 56, 57, 58, 60, 61, 62, 63, 66, 68, 69, 70, 71, 72, 73, 74. These include every identified former overflow location and a spread through every Part. Actual page-by-page observations are in the three inspection records. No clipping, overlapping text, unreadable glyph, footer collision or excessive display was found. Two nonblocking editorial observations are preserved in the B audit: separate bibliography entries for some works consulted by different subruns, and the explicit B4.8 equation tag preceding B4.7. They do not change statement IDs, references or mathematical content.

The C5 matrix is fully visible on page68. The former long C2 source title and C1 moduli citation line are fully visible on pages47 and43. The B3 heading, B56 file paths and bibliography wrapping were checked at full size. We have not inferred visual quality merely from a successful compile.


---

## Final statement and citation register audit

# Read-only final statement/register audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/hypercovers_finite_sets. No priority claimed.

Snapshot: 2026-11-19T05:37:57.187464+00:00. Runtime: 0.012551097 seconds.

The audit recursively follows the actual inputs of RESEARCH_SA10_paper.tex. It matches numbered theorem/statement headings against the five requested CSV registers and exact statement IDs in source and aggregated check events. Equation tags and older drafts are excluded. The script is read-only for all root and other-agent files.

## Counts

- Included TeX files: 10.
- Numbered statement IDs: 74.
- CSV rows: 74.
- Cited bibliography keys: 36.
- Bibliography keys: 40.

## Mechanical findings

- missing_includes: `[]`.
- missing_result_rows: `[]`.
- duplicate_result_rows: `{}`.
- register_ids_without_included_heading: `[]`.
- duplicate_statement_headings: `{}`.
- missing_exact_source_check_events: `[]`.
- missing_exact_aggregate_check_events: `[]`.
- inherited_C_ids_missing_exact_aggregate_event: `[]`.
- missing_bibliography_keys: `[]`.
- duplicate_bibliography_keys: `{}`.
- cited_bibliography_keys_missing_access_status: `[]`.
- cited_bibliography_keys_explicitly_not_opened: `[]`.

These checks verify recorded source-status labels and citation linkage; they do not claim a new independent opening of every cited source. The JSON inventory records every statement's exact source/result/event counts and SHA256 hashes of all inputs, so this snapshot is distinguishable from later integration changes.

## Actual included files

- `RESEARCH_SA10_paper.tex`.
- `sections_A.tex`.
- `B_levels.tex`.
- `B56.tex`.
- `C_sections.tex`.
- `C1_collage_B.tex`.
- `C4_path_proof_B.tex`.
- `C4_collar_proof_B.tex`.
- `C5_Hurewicz_C.tex`.
- `unresolved.tex`.


## Final integration of audit findings

The two additions requested by the independent C5 audit are present in the final PDF: the vertical-face submersion derivation on pages61–62 and the explicit PL target-local-embedding condition on pages69–70. The C proof source was frozen before final rendering. Historical requests for integration in contribution records do not indicate an unfinished step. The final register audit and PDF digest identify the delivered version.

The final aggregate contains **74 numbered-result rows** and **302 actual check events**. Exact source and event normalization files are included.
