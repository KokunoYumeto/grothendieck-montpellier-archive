# Sources and scope for D-BI-01–22, including D-BI-14a and D-BI-18a

## Published classification

Robert M. Guralnick and Jan Saxl, *Generation of finite almost simple groups by conjugates*, Journal of Algebra **268** (2003), 519–571, DOI [10.1016/S0021-8693(03)00182-0](https://doi.org/10.1016/S0021-8693(03)00182-0). The precise input is Theorem 7.1 and Remark (3), pp. 548–549, specialized to characteristic zero and degree greater than eight. The paragraph immediately before Theorem 7.1 defines the tensor convention: groups permuting tensor factors are included in its tensor-indecomposable case. The cross-characteristic exceptional case is also discussed in Lemma 7.4, pp. 550–551.

The complete published article text was read through the [public copy](https://www.academia.edu/95917548/Generation_of_finite_almost_simple_groups_by_conjugates), including the relevant theorem, remarks and proof reduction. Its original journal pagination and DOI are visible there. Direct publisher, Elsevier API, CORE and direct mirror download attempts returned HTTP 403. **No locally downloaded immutable PDF of this article is claimed.** This is a published theorem premise, not an assertion inferred from search snippets or from a secondary paper.

The restricted conclusion used is: a primitive tensor-indecomposable complex finite group of degree greater than eight containing an element with a fixed subspace of codimension two is a scalar extension of a deleted alternating/symmetric representation, or normalizes the degree-ten representation of U5(2). The defining-characteristic classical cases do not occur in characteristic zero. The proof here independently supplies the tensor, scalar, similitude, branch-budget and field arguments needed to apply this classification.

## The ten-dimensional exception

Robert M. Guralnick and Pham Huu Tiep, *Decompositions of small tensor powers and Larsen’s conjecture*, Representation Theory **9** (2005), 138–208, DOI [10.1090/S1088-4165-05-00192-5](https://doi.org/10.1090/S1088-4165-05-00192-5). Table II gives the symplectic type of the degree-ten Weil module of SU5(2); Table I lists its symplectic normalizing extension. The retained author version is [arXiv:math/0502080v1](https://arxiv.org/pdf/math/0502080), Table II p. 7, Table I p. 5. Proposition 7.10 and the subsequent Proposition 7.11 occur on author-version p. 52. The latter inputs are read for context; the proof does not assume their additional moment hypotheses for the Hurwitz source.

The primary [ATLAS U5(2) page](https://brauer.maths.qmul.ac.uk/Atlas/clas/U52/) supplies [U52G1-Ar10B0.M](https://brauer.maths.qmul.ac.uk/Atlas/clas/U52/mag/U52G1-Ar10B0.M), containing two generators over Z[i], an alternating form of determinant one, a positive Hermitian form of determinant 32, and the stated rational character/Schur-index-two metadata. The numerical matrices are retained in `u52_witness.json`. The new checker verifies their row-action invariance, positivity, orders, and one-dimensional commuting algebra exactly. It does not enumerate the group or use the table metadata as a substitute for the classification premise.

Downloaded source sizes and SHA256 values are in `sources/retrieval.json`. Full external documents and the unmodified ATLAS source are under `sources/`; only the compact mathematical matrix witness is needed to rerun the certificate.

## Rank-three and rank-seven reflection inputs

Arjeh M. Cohen, *Finite complex reflection groups*, Ann. Sci. École Norm. Sup. (4) **9** (1976), 379–436: Lemma 2.7, pp. 389–390 (the unique imprimitivity system and its four exceptions); §4.16, p. 412 (rank-three data, including G25); Theorem 5.12, p. 435 (classification). Primary PDF: <https://www.numdam.org/article/ASENS_1976_4_9_3_379_0.pdf>. The corrected normalizer proposition is not needed in these new low-degree proofs.

Gunter Malle, *On the rationality and fake degrees of characters of cyclotomic algebras*, J. Math. Sci. Univ. Tokyo **6** (1999), 647–677: Table 8.2 p. 675 and the explanation of its splitting-field column and omissions on p. 676. Primary PDF: <https://www.ms.u-tokyo.ac.jp/journal/pdf/jms060402.pdf>. These sources were already downloaded and read in this run under the central `research/sources/` directory. The new rank-three proof only needs the inclusion of the inducing character field in the tabulated splitting field, not equality of those fields.

## Internal inputs and logical limits

- O'' supplies only the necessary parameter dimension and total moving-rank identity.
- D-MON-01–03 excludes dominant nonsplit monomial sources, including inducing characters with larger fields.
- D-DET-02 gives the actual split polarization of a rank-nine natural G24 sixfold source.
- D-FIELD-03 supplies the written polarized Shapiro comparison; the new proof checks the field-of-definition condition before using it.
- The all-determinant Eisenstein sixfold theorem already settles the omitted field Q(omega); no new exclusion for every Eisenstein representation is asserted here.

No unrefereed Severn, rStation, Markman or 032 theorem is a premise. The source barrier does not settle the remaining Hodge-conjecture cases. It narrows the next finite-cover search to degree at least fifteen with no inducing complex representation of dimension at most three.

## Scalar alternating extension D-BI-08

The new proof is independent of any unrefereed assertion. Its only additional internal input is D-MON-02–03: Looijenga's published cyclic-cover monodromy theorem with the already written finite-index commutant proof and actual-polarization calculation. The scalar/permutation budget, quotient genus zero, induced representation identity, and rational multiplicity [Q(zeta_d):K] are proved in full here. The argument applies to every subgroup A_n ⊂ J ⊂ C* S_n, not only a direct scalar product. Root completed a whole-proof check and checked this generalized subgroup case explicitly on 2026-11-21.

## Essentially self-dual extension D-BI-09–10

The only classification inputs are the same published Guralnick–Saxl Theorem7.1/Remark3 and the already verified symplectic type of its degree-ten exception. The new argument independently proves the intermediate-genus reduction, nontrivial multiplier and isotropic-fixed-space bound, reflection-product reduction, projective tensor counting, absence of linear self-twists for primitive representations, multiplier descent to K, and parity. D-BI-08 is used only in its now independently reviewed generalized form with arbitrary inducing field. Root read both whole proofs and found no issue on 2026-11-21.

For further investigation only, the published Guralnick–Tiep paper *A problem of Kollár and Larsen on finite linear groups and crepant resolutions*, JEMS14(2012),605–657, DOI10.4171/JEMS/313, was retrieved from https://ems.press/content/serial-article-files/31824?nt=1 (511699bytes; SHA2563c58846260fe4b0b7f60473ae7448f8691d8a99ddac01d34f05066e693d34f55). It is not a premise of D-BI-01–10. No inference is made from an age bound without checking its exact hypotheses.

## Four-dimensional inducing fields D-BI-11

The full normalizer inputs were reread: Cohen1976 Lemma2.12 and Proposition2.13, pp391–392; Theorem5.12 and Proposition5.14, p435; Cohen1978 erratum, Ann. Sci. ENS11(1978),613, which deletes the apparent rank-four exception. Malle's table is used as a model-field inclusion, not a universal equality of character and splitting fields. The real F4 length-switch model was already reconstructed on all48 roots in D-GF4-01. The new scalar degree≤2 and full cyclotomic/biquadratic list are proved independently. The larger-field exception is explicit; L=K is eliminated only after a multiplicity-one projector supplies the K-model and actual-polarization transfer. The final proper-field paragraph is explicitly restricted to Qi and Q(sqrt−2).

## Real-boundary theorem D-BI-12

Joel Brewster Lewis and Victor Reiner, *Circuits and Hurwitz action in finite root systems*, New York J. Math.22(2016),1457–1486. Primary published PDF https://nyjm.albany.edu/j/2016/22-63v.pdf,496913bytes,SHA256a432c982a2b36eb81d450bf8ac42e19ad9161c12071ea88499a34d0066cb6bb0. Corollary1.4 p1459 and its complete proof §4.3 pp1480–1481 were read; Proposition4.1 p1473 supplies Carter's independent-root criterion. The corollary applies to every element of a finite real reflection group, including H4, not only Coxeter elements. The new argument does not claim to rederive the published classification/computer calculations behind Lemma1.2. Section6.3 pp1484–1485 explicitly warns that the corresponding reduction fails for general complex reflection groups; no such extension is assumed.

## Arbitrary inducing images D-BI-13 and unramified scalar models D-BI-14

Cohen Proposition2.13, Theorem5.12, and the corrected Proposition5.14 are used with their complete exceptions. The sole corrected complex normalizer exception G25 has degree three and is already removed by the separately proved inducing-dimension-three theorem. Malle Table8.2 and its explanation give Q(omega)-models for G33/G34; the real E6/E7/E8 normalizers have the explicit rational chamber models. The larger inducing character field is contained in the scalar-extended model field, not identified with K. The scalar p-primary character, unramified-field obstruction, repeated-minimal-polynomial fixed-space estimate, and branch-rank contradiction are new complete arguments. The p=7 case preserves the earlier G24 actual-polarization exclusion as an explicit prerequisite.

D-BI-14 uses the elementary Eisenstein proof for Phi_p(X+1) over every unramified completion of the arbitrary model field. It therefore does not infer linear disjointness merely from an intersection calculation without justification, and does not assume the model field is Galois.

## Full Guralnick–Saxl radical bound D-BI-14a

On 21 November 2026 the entire Theorem7.1 statement, all exception families, Remark3, and Lemma7.4 were reread in the complete published article copy cited above. The theorem gives the minimum eigenspace codimension strictly greater than max(2,sqrt(e)/2), outside its stated exceptions. In characteristic zero and e at least42, only the scalar deleted alternating/symmetric exception survives; D-BI-08 removes it. The tensor-factor permutation convention and the degree-eight tensor-cube exception are explicitly accounted for. Root independently reopened these same primary passages. The printed radical is displaced by the copy's text extraction; the proof's implication e<=alpha(G)^2/4 from nu<=sqrt(e)/2 confirms its placement. No unread trireflection classification is invoked.

## Symmetry obstruction D-BI-15

This new proof uses elementary finite-group character theory, algebraic central projectors, the Galois correspondence for the actual connected cover, finite Hurwitz fibres, and the explicit classification of finite-order automorphisms of P1. No classification theorem asserting uniqueness of imprimitivity systems is assumed. Uniqueness is an explicit sufficient hypothesis, and the nonnormal/nonunique cases remain open.

## Rank-six and rank-seven inducing blocks D-BI-16–17

The classification and normalizer inputs are the same fully checked Cohen/Malle statements used in D-BI-11–13. The Q(omega) model for G34, its center mu6, and the real E6/E7 models are used with their explicit previously reconstructed scalar actions. The new proof independently classifies scalar extension degrees, the eight possible moving-rank profiles, all seven residual rank-four eigenvalue pairs, and the two-embedding age constraint. Published finite-group data are distinguished from new profile deductions. Neither a signature equation nor a branch-dimension equality is used to assert dominance. Root and imprimitive read the full proofs, and the exact arithmetic checker was rerun.

## Character ratios D-BI-18 and D-BI-18a

Hülya Duyan, Zoltán Halasi, and Károly Podoski, *Random bases for coprime linear groups*, Journal of Group Theory23(2020), no1,133–157, DOI10.1515/jgth-2019-0043. The actual published PDF was opened and read at https://www.degruyterbrill.com/document/doi/10.1515/jgth-2019-0043/pdf. Exact locators: Definition2.3 p137; Lemma2.4 and full proof pp137–138; Lemma3.1 and full proof p139; Theorem4.1(2), its attribution proof paragraph, and Remark4.2 p141. The character estimate is for ordinary irreducible complex characters and has no coprime representation hypothesis. The finite-field support lemmas are not imported without their hypotheses: the required complex support proof is supplied completely in D-BI-18.

The bound for a quasisimple Lie-type group over F_q, with nonalternating simple quotient and q>9, is max{1/(sqrt(q)−1),9/q}. The denominator is sqrt(q)−1, not sqrt(q−1). Root independently read the published passages and checked the printed denominator; imprimitive independently read the same journal passages and audited every use of them.

The updated eighteen-page author PDF is https://zhalasi.web.elte.hu/papers/16_CoprimeRandomBase.pdf,382916bytes,SHA256e43400fb6f8fa32bd7e6680c1abe3c49dc95f8868a9885058b6a4f7f13b8f7d8. In that version the same character bound is Theorem4.1(2),p7, and Lemma3.1 is on pp5–6. The seventeen-page arXiv v1 https://arxiv.org/pdf/1903.00692v1 instead numbers it Theorem3.1(2),p5. These versions and locators are not interchanged.

DHP attributes the estimate to David Gluck, *Sharper character value estimates for groups of Lie type*, Journal of Algebra174(1995),no1,229–266, DOI10.1006/jabr.1995.1127. The original Gluck full text was not retrieved in this audit; DOI access failed and searches supplied only attribution/metadata or other papers. The theorem premise actually read is DHP's published exact restatement. Liebeck's primary survey Theorem2.4 was read as a corroborating source lead, not substituted for that statement.

The broader search did not establish a universal moving-rank fraction for every primitive finite group. Guralnick–Tiep2012 Proposition2.22,p621, supplies only the weaker nonalternating character ratio19/20 in general; its Weil-module Lemmas3.5–3.6 are family-specific. Gluck–Magaard's fourth-moment bounds have additional tensor-moment hypotheses and a weaker fraction. Theorems asserting the existence of an element with a small fixed space do not control prescribed local inertias. Small Lie-type fields, alternating factors, arbitrary mixed cores and reducible normal restrictions were not silently excluded by those sources.

## Direct structure theorem D-BI-19

The complete characteristic-zero proof is given in `normal_core_section.tex`: homogeneous Clifford restriction, the full matrix-algebra normalizer, the trace-zero abelian minimal-normal case, the elementary characteristically-simple decomposition, perfect derived preimages, commuting quasisimple factors, and uniqueness of the minimal normal quotient. Thus no generalized-Fitting theorem, finite-field specialization or unverified classification is required for this reduction. DHP Theorem5.1 and proof, journal pp148–151 (updated author pp12–14), were read for the analogous published structure argument. That theorem assumes a maximal coprime finite-field group, and it is cited for comparison only; its maximality hypothesis is not asserted here. The finite character-ratio input remains exactly DHP Theorem4.1(2).


## Lie-field refinement D-BI-20

Corneliu Hoffman, *Cross Characteristic Projective Representations for Some Classical Groups*, Journal of Algebra229(2000),666–677, DOI10.1006/jabr.2000.8300. The full author copy was read at https://www.academia.edu/31207891/Cross_Characteristic_Projective_Representations_for_Some_Classical_Groups. The precise input is Table1 on numbered author p14, covering nontrivial cross-characteristic projective representations of the classical groups. Characteristic zero is included. The classical rows and their complete small-parameter exceptions were inspected. The paper's exceptional E-type rows attributed to an unpublished [H] are not used. Publisher PDF retrieval was unavailable; no immutable local Hoffman PDF is claimed.

Frank Lübeck, *Smallest degrees of representations of exceptional groups of Lie type*, Communications in Algebra29(2001),2147–2169, DOI10.1081/AGB-100002175. Complete author PDF retained from https://www.math.rwth-aachen.de/~Frank.Luebeck/preprints/smdegexc.pdf. Theorem2.1 on numbered p4 and all first-degree tables in §5.1–5.10, pp8–22, were read. These are characteristic-zero degrees of the simply connected groups, with all small-parameter exceptions stated. The author's square-root parameter in the Suzuki and Ree rows is explicitly converted to the actual field size in the arithmetic certificate. These published tables, rather than Hoffman's unpublished-source rows, cover the exceptional types.

Gerhard Hiss, WilliamJ.Husen and Kay Magaard, *Imprimitive irreducible modules for finite quasisimple groups*, Memoirs AMS234(2015),no1104, DOI10.1090/memo/1104. The complete author version https://arxiv.org/pdf/1211.6350v2 is retained. Introduction numbered p4 distinguishes ordinary Lie-type covers from exceptional multipliers; Chapter5, Table1, numbered p35 gives the complete exceptional multiplier list. None has q in {29,31,32,37,41,43}. For PSL2 the exceptional field sizes are4 and9, so the relevant quasisimple covers are SL2(q) and its central quotients. The original GAP/ATLAS multiplier and outer-order rows at https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/ctbltoc/views/simplebyorder.html were checked as corroboration, not as a replacement for this published cover input. No imprimitive-character classification theorem from the monograph is used.

DonaldL.White, *Character degrees of extensions of PSL2(q) and SL2(q)*, Journal of Group Theory16(2013),1–33, DOI10.1515/jgt-2012-0026. Actual journal PDF https://www.degruyterbrill.com/document/doi/10.1515/jgt-2012-0026/pdf read in full relevant passages: TheoremB p4 for the SL2(37) degree list; pp2–3 and6 for all diagonal/field automorphisms; §3 pp5–7 and Lemma3.1 p7 for the class action. The author PDF https://www.math.kent.edu/~white/papers/sl2.pdf is retained separately and has different pagination; the TeX locators refer to the published33-page article. The inverse-conjugacy and class-inverting arguments in D-BI-20 are newly written elementary2×2 proofs, including the full special-linear cover and its perfectness.

The exact checker recomputes all six rational ceiling sets, minimum-degree comparisons and the empty q37 degree intersection. It does not recompute the published character-degree classifications. No unrefereed theorem is a premise. Whole-proof peer/root reviews were requested after the complete proof was written; their outcomes are recorded separately when received.

## All rank-one cores D-BI-21

The character-table premise is the published ATLAS of Finite Groups as accessed through CTblLib1.3.11, whose source archive was retained by the imprimitive agent (SHA256 f201e9da571c681a7bbfb1e4683bdb2c80a23b005099ed0453521f59cb443434). The official manual §3.7-3 defines `ExtensionInfoCharacterTable`, the universal-cover naming convention and the outer metadata; §3.7-6 defines `InfoText`. These were freshly read at https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc/chap3.html in the preceding sporadic audit. Every one of the33 retained table records has an explicit ATLAS-origin source string. The complete input `a1/a1_character_inputs.json` is334499bytes with SHA256 5ed905449e1f6f64f3eb18b27a213fc5c72e0731dbd591670166e8763ad7fc88. The compact12-core/19-extension inventory was independently assembled by imprimitive; an unchanged copy is `a1/table_inventory.json`, SHA256 922053929af2571dec062a9eb23f4ab14c721b4a87b9a3e3cdd8f0085e451d92.

The ATLAS subgroup labels were checked directly in the original CTblLib data files. In `ctoalter.tbl`, lines1754–1757 identify2.A6.2_1 as SigmaL(2,9); lines4476–4479 identifyA6.2_2 asPGL(2,9); line4589 identifiesA6.2_3 asM10. In `ctoline1.tbl`, lines2187–2190 identifyL2(25).2_1 asPGL(2,25), and lines2270–2273 identifyL2(25).2_2 asPSigmaL(2,25). Together with the three distinct subgroups of the outerV4, this identifies the third subgroup as mixed diagonal-field. The proof supplies the new center-negative obstruction and uses the actual quotient extensions3.A6.2_3 andL2(25).2_3. It never assumes a missing universal-cover extension.

White's actual published33-page PDF was reopened on21November2026. Lemmas4.4–4.5 and their complete proofs onp9 show that the two half-degree characters are exchanged by the diagonal automorphism. Lemma4.6 and its full proof onp10 show that the field automorphism fixes each. The earlier explicit automorphism formulas and the published multiplier input in Hiss–Husen–Magaard remain as recorded above. The degree-five endpoint is consequently the exact natural S6 normalizer of the deleted A6 matrix image; no generic assertion about every outer automorphism is substituted for this character stabilizer.

The finite computation is new, exact arithmetic on published data. GAP computes every spectrum by `EigenvaluesChar`; the independent Python program uses rational normalized traces and Ramanujan sums for every nonscalar class, imports no selected-row list, and checks every core fusion for order preservation, identity kernel, full normal-class unions and prime power-map compatibility. The first GAP attempt stopped before computation because `Encode` is a read-only name; the routine was renamedA1Encode and both full corrected runs passed. This failure is retained in the event log. The arithmetic does not rederive the ATLAS tables or their group identifications. The universal fifth/quarter bounds, cyclic-normalizer scalar normalization, mixed-outer obstruction, tensor argument and geometric conclusion are proved in full in the TeX.

## All Suzuki and Ree cores D-BI-22

The five complete inputs are CTblLib1.3.11 tables `2^2.Sz(8)`, `2^2.Sz(8).3`, `R(27)`, `2F4(2)'`, and `2F4(8)`. The first four retain explicit ATLAS-origin strings. The last is the complete table supplied by Gunter Malle, explicitly recorded in the original `ctonews.tbl` at lines740–742; its simple-group and outer-order metadata are at lines1189–1190. The official table page is https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2F4%288%29.html . The complete immutable JSON is161615bytes, SHA25610dd43bccf28471f0c8725086666385aba1dc9970fe9d53bd1478e9ad6a1637b.

Hiss–Husen–Magaard Chapter5 Table1 and the preceding paragraph, numbered p35, were freshly reread for the complete exceptional multiplier list: only Sz(8) among these series has an exceptional cover. The full universal Suzuki cover has noncyclic center, and all nonlinear rows are retained; no faithful representation of that whole center is assumed. The same monograph §10.2, numbered p131, immediately before Proposition10.4, explicitly documents the complete Ree character table in CHEVIE and credits Malle's unipotent calculation. The complete paragraph and the start of the following proof were read.

Malle's original published computation is G. Malle, Die unipotenten Charaktere von 2F4(q²), Communications in Algebra18(1990),no7,2361–2381, DOI10.1080/00927879008824026. Publisher metadata and the journal reference were verified. Its complete proof was not freshly retrieved; the actual complete-table premise is the explicit CTblLib data, corroborated by the published HHM provenance passage. It is not relabelled as an ATLAS table.

Lübeck's complete primary author PDF was freshly reread at the §5 introduction (numbered p8), Suzuki §5.1 and small Ree §5.2 (p9), and large Ree §5.5 (pp14–15), including all first-degree rows and parameter exceptions. In actual field-size notation, the minima used are (q−1)sqrt(q/2), q²−q+1, and (q−1)sqrt(q/2)(q+1)²(q²−q+1). Their first relevant large-field values are124,58807 and134090748. These are characteristic-zero minima, with exceptional covers treated separately. DHP Theorem4.1(2), published p141, is the exact all-character-ratio premise already recorded above; its attribution paragraph was reread.

The new proof supplies every normalizer scalar-rescaling step, the commutator workaround for missing outer tables, all mixed-type tensor permutations and the actual intermediate-cover rank contradiction. GAP and an independent same-author Ramanujan implementation both passed all213 selected rows and15,471 nonscalar entries. Root and imprimitive subsequently completed whole-proof/primary-source reviews and actual independent arithmetic checks, all PASS. No new table classification, unrefereed assertion or finite-to-infinite extrapolation is claimed.

## Linear Weil family, D-BI23

Gérardin1977, Proposition4.2 and full proof pp82–83, was freshly read in the complete published article copy at https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields ; DOI10.1016/0021-8693(77)90394-5. OCR drops the minus-one from the displayed deleted degree, but the full proof on p83 states it explicitly; the retained derivation independently counts that degree. The new SL restriction proof uses the complete ordered-pair orbit count and does not assume GL restriction irreducible.

Direct ATLAS primary page https://brauer.maths.qmul.ac.uk/Atlas/lin/L34/ was opened and read: order20160, multiplierC3×C4×C4, OutD12, cyclic outer-extension inventory and actual natural triple-cover matrices. Its site-level work-in-progress notice is retained as part of the source; numerical premises are the complete published ATLAS character tables in CTblLib1.3.11, with explicit source strings, all rows/powers and normal fusions. Full six-table input SHA12becae3b988a84d6820b658da1ac3dcba4a2a83ff3be85c1342e6cd9bed5e76. New full spectra independently reconstructed from those published inputs; no classification proof is claimed.

### Linear endpoint source cross-check after peer review

Canonical D-BI23 now explicitly retains the general WORK IN PROGRESS warning on the ATLAS L34 webpage. The order is independently derived from63×60×48 and two factors3. HHM Chapter5 Table1 p35 was reread: it establishes exceptional status, not the exact multiplier structure. The latter is freshly read in Breuer CTblLibXpls §2.7-4, which gives C4²×C3 and explicitly attributes it to printed ATLAS p23; §2.6-4 separately records OutD12 and its three order2 types. Breuer §11.5-7 gives the diagonal/field/graph descriptions; their explicit action yields C3 semidirect(C2×C2), with both involutions inverting C3. Exact URL locators are in the new BI:BreuerL34 bibitem. Numerical tables and previous1288-spectrum certificate are unchanged.

## D-BI24 unitary Weil gate (2026-11-21, about17:57–18:09UTC)

- Gérardin1977, Theorem4.9.2, published pp99–100, complete proof(a)–(e) freshly read at https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields . This supplies the exact total character for all characteristics. The restriction irreducibility used here is independently derived by the q+1-vector-orbit argument in the authored proof.
- Guralnick–Magaard–Saxl–Tiep2002, Journal of Algebra257,291–347, p293, full published page read from the sibling-retrieved primary PDF (now copied to sources/). Ordinary degrees and extensions are explicitly stated. The earlier author copy at https://www.academia.edu/14851735/Cross_characteristic_representations_of_symplectic_and_unitary_groups is distinguished from the published page.
- Guralnick–Liebeck–OBrien–Shalev–Tiep2018, Inventiones213,589–695, DOI10.1007/s00222-018-0795-z, complete §4.3 read in author version https://www.ma.imperial.ac.uk/~mwl/burnside.pdf, p16, equations4.3–4.4. Version-specific pagination retained.
- Yang–Wu–Revin–Vdovin2023, Sbornik Mathematics214,108–147, DOI10.4213/sm9698e, §2.2 and Lemma6, published p114 read in full text and visually. It is the published automorphism restatement actually read; underlying GLS Theorem2.5.12 is cited there, not claimed independently reproved. https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=9698&wshow=paper .
- Complete seven published ATLAS character tables supplied by official CTblLib1.3.11, exact source strings retained in unitary_weil/unitary_weil_inputs.json. Outer groups also independently checked from the standard unitary automorphism description. All17selectedrows754spectra reconstructed in GAP and a separate exact Python implementation. No unrefereed input used.
- Katz–Tiep2025 monograph author-version kt18_141.pdf was examined as a corroborating lead, but its338-page pagination differs from later published/final versions; no essential statement in this theorem depends on that version.

### Unitary source-domain recheck (2026-11-21,18:15–18:17UTC)

Gérardin's unitary section3.1, publishedp70, starts with an arbitrary finite field. Theorem3.3(a''') onp73 explicitly handles even q and records its exceptional n2,q2 normalization. Theorem4.9.2/equation4.22 onpp99–100 is therefore valid for even as well as odd characteristic; the odd restriction applies to the symplectic section2 and Theorem4.9.1. These exact original-domain passages were freshly reopened and read. Yang–Wu–Revin–Vdovin section2.2/Lemma6,p114 was also reopened with its preceding definitions: the simple n≥3 unitary domain used here excludes only PSU3(2), already excluded in the theorem. Every small endpoint PSU3(3),PSU4(2),PSU5(2),PSU6(2),PSU3(4),PSU3(5) is covered. The proof now states these domain facts explicitly; no mathematical estimate or hypothesis changed.

### Independent audits of ESC and E822 (2026-11-21,18:12–18:19UTC)

EVEN_SYMPLECTIC_PEER_AUDIT.md records a fresh official complete-table/correction-source check and full proof reading. Its independent parser and Fourier reconstruction pass all4549 generic inequalities and3442 small-group spectra. Lübeck's exact primary author text was read locally after the browser rejected its application/x-pdf content type.

COUPLED_SURFACE_PEER_AUDIT.md records the complete SF-E822 proof review and independent first-jet/exterior certificate. Stacks Lemma33.47.3 (https://stacks.math.columbia.edu/tag/0FD4) and Remark37.32.4 (https://stacks.math.columbia.edu/tag/0G4G) were freshly read in full. Published BF and embedding GRR retain their earlier checked status; supplied invariant compatibility is not relabelled as a new refereed theorem.

## Complete PSL3(4) compatible-normalizer coverage, L34--1..3

Breuer–Malle–O’Brien, Reliability and reproducibility of Atlas information, Contemporary Mathematics694(2017),21–31, DOI10.1090/conm/694/13960. Complete section3.3 and3.3.1 including Lemma3.1 were read in authorpp5–6 of https://agag-malle.math.rptu.de/~malle/download/atlas.pdf . Local PDF204316bytes, SHA0f619a98eb52cdb2622b6c4fa6a71d1c454442c1d141ab77d18f28bdf4d3512f. Publisher https://doi.org/10.1090/conm/694 confirms chapter range. Browser PDF opening timed out, but the actual local HTTP download and full text conversion succeeded. The source explicitly lists all36 bicyclic extensions up to isoclinism. The authored proof supplies the conjugation-isoclinism and scalar-power normalization bridge, so no assumption that isoclinism preserves character tables is made. The source centralization-label inconsistency is documented and bypassed by covering both order4 quotients and all3 involution types. Independent exact multiplier action gives20kernels,8orbits,36pairs. All36 retained input names and28 normal fusions also checked. Imprimitive independently whole-reviewed the proof/source and rebuilt the finite count, PASS.

## Conditional higher-even-symplectic peer audit, HES01–03

HIGHER_EVEN_SYMPLECTIC_PEER_AUDIT.md preserves the still-unverified GM1998 proper-parabolic semisimple estimate as an explicit condition. All new elementary arguments and finite data checks pass. Fresh original Gow1981p583/section3pp589–591, Liebeck survey definitionsp2/Theorem2.4pp3–4 and GM2006authorp25 were read. Their exact URLs and the source boundary are in the report. The independent reconstruction passes279rows and45209entries, with symbolic all-rank arithmetic. No GM1998 verification is claimed.

## Complete A2 and unitary-rank-three peer audit

A2_CORES_PEER_AUDIT.md records full A2-01–03 proof/source/code reading and independent reconstruction of46 generic row types/386 inequalities and47 finite tables/1603 selected rows/141024 spectra/34 fusions. Simpson–Frame1973 original publisher PDF, §§1–2 and4–5/7, pp486–493, was read; exact URL and locators are in the report. The complete official GCT inventory and all correction notes in immutable commit87231738271ed548f62e7f1c98ff2bbfc1ed30d3 were read. The full Geck1990 original was not newly retrieved; this remains an explicit source boundary. HHM Chapter5 Table1 and preceding paragraph, numberedp35, were freshly reread. The constructed universalL34 table is accurately recorded as redundant; all essential bounds use the eight published cyclic-center core tables. The initial provenance assertion failure and correction are retained. Final status-only A2 hash7ca6bcfa77cfe087b22a4511eadd7f51e9acf442ee895e8c2ae28e6ee3958035 was reread in full.

## Complete finite Sp8/10/12 peer audit

HIGHER_EVEN_SYMPLECTIC_FINITE_PEER_AUDIT.md records the unconditional-on-GM finite theorem with full normalizer/tensor/larger-field scope. The new independent arithmetic reconstructs all756 rows/271785 entries, including the entire newSp12 table, PASS0.585070s. The provenance assertion originally failed because S12 is computed byChristophKöhler, while S8/S10 are ATLAS. Exact input strings are now checked individually; no failed mathematical inequality occurred. The official S12 page https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/S12%282%29.html was freshly read:477classes, exactorder208114637736580743168000, sameKöhler provenance. Its generatedCTblLib1.3.10 record is distinguished from retainedpackage1.3.11. No separate refereed table-construction source is claimed. The earlier fresh GM2006/HHM classification readings retain their recorded scope; pendingGM1998 is not used in this finite theorem.

## Unconditional higher-even-symplectic replacement

The full new HES01–03 proof has independent whole-proof audit PASS at72e295707440f2e06e39658d2b3528f61d9587227e99e6f18196b075515dbc3c. HIGHER_EVEN_SYMPLECTIC_UNCONDITIONAL_PEER_AUDIT.md records the complete elementary parabolic/shear/weight-orbit argument, elliptic Hermitian centralizer and all-rank support bound. The sole missingGM1998 estimate is no longer used. Exact independent symbolic certificate PASS0.041217sec; finite symbolic identities are not represented as an all-rank proof. Previously checked Gow/Gluck-restatement/GM2006/HHM inputs retain their precise scope. Essential endpoint data are onlyATLASSp8/Sp10; KöhlerSp12 is redundant for this new theorem.

## All even fields, HES04–06 independent audit

HIGHER_EVEN_SYMPLECTIC_ALL_FIELDS_PEER_AUDIT.md records complete proof reading, actualclock19:04:29UTC, and own exactF4certificate PASS0.019795sec. Fresh visualLiebeckp4 check refuted the proposed c8<1/2 because the denominator is sqrt(q)minus1; the corrected9/16/7/32/7/64 constants are checked. Li–Xia2022 authorv3§2.2.2/Table2.1numberedp14 was read locally and rendered; PDFhash4ef16aa4308f8c487a06e9c8e84ece77247d0e763146f0215d8e109e443e3a93. BrowserarXivopeningdisabled, not misreported as a successfuldownload. The final source boundary and exact all-rank versus finite arithmetic scopes are preserved in the report.

## Complete odd C3 normal-core gate

The full source/version/data boundary is in csp6_odd/SOURCES.md. New D-C3-01–03 proves the all-odd-field Sp6 normal-core exclusion with arbitrary compatible outer/scalar/mixed-tensor actions and inducing fields. Original complete Luebeck CSp6.1 data, cyclic Clifford restriction and semisimple fusion, the published unipotent estimate, q9 projective descent and all q3 endpoint spectra are distinguished. Actual final checks:8811 universal coefficient inequalities,228rows31428spectra, and the separate F9 dimension2 witness. Parent complete proof/source/code reading and all reruns PASS; second independent whole-proof audit pending. Initial exploratory dimension-assumption failure and harmless GAP warning are recorded honestly. Actual record time2026-11-21 19:18:55UTC.

C3 final promotion: parent and imprimitive whole-proof/source/code audits PASS. Peer independently rebuilt every8811 generic inequality,228rows31428spectra and all auxiliaryF9 finite witnesses. Its original report and arithmetic are under agents/imprimitive/audit_odd_c3/. Canonical status-only proof hash5f60952a684ac63ae6df6be85193ecb422688f23e1eb1aca1bcfbaa0eb6f4aba; reviewed mathematicalhash3aec637863bd7c2e7773af72805b518b3f909ab64d1235b9aeeed2a09f5116eb. Parent also reran final exact source-to-input assertions, PASS2.484827s. Record time19:24:39UTC.

## First-overlap obstruction with free summands, SF-E825

FREE_SUMMAND_OVERLAP_PEER_AUDIT.md records the complete independent frozen34af017d proof reading and an independently authored symbolic/exterior certificate PASS0.601104s. The variable-b terms were independently reconstructed as actual boundaries and incorporated by the author asE825.13a; the final wording covers all normal and tangential derivatives. BF2008 Theorem5.1.3, Proposition5.2.2 and their complete proofs plusCorollary5.2.3 were freshly read in originalauthorpp24–27. Earlier completeBF6.2/6.4 and Mumford16 source checks retain their exact scope. SuppliedS21 is not relabelled as a new refereed theorem. No semiregular seed or positive-determinant exclusion is asserted. Actual record19:43:44UTC.

## All odd C2 and finite endpoints peer audit

ODD_C2_PEER_AUDIT.md records whole-proof/source/code PASS on10d17b9a and finite7eed128e. Fresh complete Dabbaghian published author text620–624, VinrootTh1author1, LiXia2.2.2Table2.1author14 and HHM5Table1p35 were read, together with official table/outer provenance pages. The four inconsistent indexed restriction formulas are explicitly replaced only by direct publishedTable2 entries; their failed diagnostic remains retained. Independently authored Fraction parsing plus reviewer-owned Fourier reconstructs43types258 universal inequalities,485rows37502spectra5fusions, and a separate exact186-row full finite transcription match. FinalPASS1.602889s, actualrecord19:48:54UTC. No generic erroneous C2 table, binary-PDF inspection, or full character-table construction is claimed.

## Higher odd symplectic cores, D-HOS01–06

The elementary carrier and degree lemmas were whole-read and passed by parent and imprimitive on1e719294; their canonical status-onlyhash isa29d62b4. The new complete447-lineD-HOS03–06 proof is frozeneb760afa97ee57230236ce9058085a4225a78a502e2aa57df5c9efb9637a9ccc pendingindependentwholeaudit. It cites only existing BI:HHM, HES:LiXia2022 andHES:Liebeck2017. The full exact unipotent statement and simplyconnectedconventions onLiebeckauthor2–4 were reread, retaining denominator1/(sqrt(q)−1); this is the published Gluck restatement actually read. LiXiaTable2.1author14 andHHMChapter5Table1p35 were freshly reread duringthe adjacentC2audit. No new table or degree-classification input is used. The explicit rational/symbolic certificate passes0.047655s, including64F9scalarrepairs and729dualweights; it does not replace the universal finite-field form and period arguments. Parent preliminary whole-proofPASS recorded separately, finalexposition/peerauditpending. Actualrecord19:59:18UTC.

## Two-slope extension audit, SF-E826

TWO_SLOPE_EXTENSION_PEER_AUDIT.md records whole frozen58eb0b23 proof/source/code PASS. The actual triangle invariant inequality, intrinsic HN/block actions, rational-B cap comparison, arbitrary-size brick construction and actual indecomposable Cech extension were read in full. Fresh suppliedS21 through(S21.8) retains its supplied status. Original Mumford16 printed150–153 and162–163 full invoked statements/proofs were reread; prior complete BF checks retain their recorded scope. Independent pair-rational Q(sqrt2) and finite matrix certificate checks all16coordinates,240crossindices,20unitcases,148capacities,the printed33vertex tree,36bricks,and ranks18/6 in0.04080446s. An unnecessary nondegeneracy assertion in the first auditor run was repaired without changing the mathematical proof; attemptsJSON retains it. Actual record20:10:26UTC.

HOS03–06 independent sibling final audit PASS at frozeneb760afa; full report/code/output are agents/imprimitive/audit_higher_odd_symplectic/. Its independent different-basisF9 checker and full-source reading are recorded separately from author and root checks.

## Linear and unitary non-Weil finite rank reductions

NONWEIL_CUTOFFS_PEER_AUDIT.md records complete independent frozenUNW10addbba/LNW8f66c40c whole-proof/source/code PASS. Fresh LTaccepted-authorTheorems4.4/5.5 fullproofs19–20/25–26 and visualconstant, publishedGLT2020complete8.1/8.3 andspecialrestriction/degree proofs51–52,67–68, andHHM4/35 were read. Annalsmetadata independently reopened; authorversionlocators not confused withjournalpagination. Independent exact certificatePASS0.124358891s reconstructs all universalconstant/exponent/error/normalizer/sourcebudgetreductions. Actualrecord20:13:34UTC. The enormousfinite range is not enumerated or declared solved.

## Diagonal Yoneda survival, SF-E827

DIAGONAL_YONEDA_PEER_AUDIT.md records finalabe42293 complete independent mathematicalPASS at20:16:14UTC. Both actual triangleboundaries and all multiplicity/invariant projections were checked, along with every nondegenerate index and one-factor degenerateKunnethcase. The author repeated the already-required nonzero crossdifference qualifier. No new numericalpremise or computation is claimed. Full source scopes retain the immediately precedingMumford/S21 reads and priorBF/Mukai checks; suppliedstatus preserved.

## Higher symplectic cores over F5, D-HOS07–10

The full new proof is frozen3fb15463d75bfa8da6167a57e2905b76f6e42a46ec7f7148b641b611d0a47a67 pending independent review. Its only representation-classification inputs are the complete cover exceptions in HHMChapter5Table1p35 and outer automorphisms in Li–Xia2022authorv3Section2.2.2Table2.1p14, both freshly reread. Vinroot2004Theorem1, authorp1, was freshly opened and read with its full characteristic-not-two field domain; it restates the published Wonenburger factorization. Source https://www.math.wm.edu/~vinroot/gspfactor.pdf downloaded224313bytes, SHA594e0fffbf9d2efacd6fc96f74e157351eb4e41224d48db9eeb00d82464108cd, exact retrieval record and full text retained in sources/. The original factorization proof is cited, not claimed as a new reproof. No unipotent character bound, full character table, or Weil character formula is a premise. All Heisenberg, radical-generation, finite-field commutator, and period-budget arguments are written in full. Exact check_higher_symplectic_five.py/.json PASS0.603973s; finite scopes and universal proof scopes are explicitly distinguished. Actual record20:32:20UTC.

D-HOS03–06 final root integration was reported20:16:08UTC, status-onlycanonicalSHA3d8275bb5111c56afce136e112dbc26e094e62484d239ddd5a633b672b332265. Root and independent peer whole-proof/source checks passed before integration.

## Classical character-level source versions

GLT2024_classical.pdf is the49-page NSF-hosted author version (662522bytes,SHA c9d1f96921de681dec19ab867a290068bc670f3a3a83f391ee5c150d9f7747c7). GLT2024_classical_published.pdf is the60-page Springer published article, Inventiones235(2024)151–210, DOI10.1007/s00222-023-01221-5 (1605824bytes,SHA ad6f1d3bf9e0acc60220f9098033513b521f96668967002914da7d5a91ced957). Their separate retrieval records retain URL/version details. Proposition3.8 and Corollary4.7 supply nonzero top-level constituents, not an asserted irreducibility/exhaustion theorem; no all-element low-level bound has been inferred from that positivity.

## Orthogonal level/cover peer reduction, D-OL01–03

ORTHOGONAL_LEVELS_PEER_AUDIT.md records full independent frozen889ddcc6 proof/source/code PASS. The complete published GLT2024 proofs of3.7/6.3/7.3, definition/range/upperdegree inputs, and LTaccepted-author5.5 with exactSpin support were freshly read. The report gives version-specific locators and the deliberately unbounded residual natural-rank scope. Independent exact arithmeticPASS0.044676667s; its initialauditorstructural-polynomialequalityassertion andrepair are retained. Parent integratedstatus-onlyb1d19dcc asQ2bn.

## D-HOS07–12 checked scope and records

Imprimitive whole HOS07–10 proof/source/code auditPASSactual20:34:28UTC, own finite reconstruction0.468551252s; report inagents/imprimitive/audit_symplectic_five/. Root integratedq5 at20:42:24UTC asQ2bo, canonicalstatus-onlyad7fa808aaad30f10000cf776b8c0ce81d924b2237a4e854b78d818aa91f076c. The reviewedmathhash3fb15463 remains in the author certificate and reviews.

D-HOS11–12 is a separate frozen43d9154a proof: fullnormalizer bound13/108 for allordinarySp(3)irreps andsourceexclusion onlyforselfdual q3cores, mixed withq5allowed. Exactanisotropicshear carriers1/4/4 are derived from the actualSchrodingeroperator. Noall-q3reality assertion. AuthorcertificatePASS0.050566796s; rootcompleteproof/codePASSreported; independentpeerqueued. ExistingHHM/LiXia cover/outer sources retain their freshly checked scopes.

## Surface and actual elliptic extension gates E829/E830

SURFACE_SUPPORT_WEDGE_PEER_AUDIT.md and ACTUAL_ELLIPTIC_COUPLING_PEER_AUDIT.md record full independent frozen4cab77bf/dbe5e856 proofsPASS. Actualrationalcomplement/isogenyline,trace/Kunneth,actualtriangleboundaries andinvariantmatrixprojections,entry-specificellipticcoefficientsandgluableindecomposableexample were checked. Independent exact exteriorcertificatePASS0.032552646s, withall12rank/indexcasesandexplicitwedge/thresholdsystems. OriginalMumford150-153rereadandHermitianindexcorollary162-163visuallyreread; fullsuppliedS21andpriorBFstatuses preserved. Actualrecord20:45:16UTC.


## OL04–05 independent review and q3 integration — recorded 2026-11-21 20:53:43 UTC

Freshly read the full published Kim–Trefethen–Vinroot2023 introduction39–40, exact subgroup definitions41–43 and Theorem1p44 at https://www.advgrouptheory.com/journal/Volumes/16/KimTrefethenVinroot.pdf (retrieval ref turn802634082view0). This confirms full-O strong reality in both characteristics and exact determinant/spinor derived quotient. The original Wonenburger/Ellers–Nolte/Gow proofs are not newly reconstructed. Freshly reread published GLT2024 Definition3.2(ii), Lemma3.3/full proof160 and Theorem3.7/k1proof165 in the retained full journal PDF. Whole OL04–05 proof audit PASS at final tag-repaired2f40c6da; independent orbit/stabilizer/constants check PASS0.221892491s. See ORTHOGONAL_LOWLEVEL_PEER_AUDIT.md.

SF-E831 whole proof and exact independent supplement are complete, with inherited source scopes and no geometric realization claim for the hypothetical incidence example. See VERTEXWISE_COUPLING_PEER_AUDIT.md.

Sibling HOS11–12 whole-proof/source/code audit PASS at43d9154a, actual20:49:41UTC; parent whole-proof/code/peer read and integration20:51:29UTC, Q2br, status-only canonicale9a25444f9b21a196035c64eafb29e8713489f9b5ee0f233cb20aca52f211984. The nonselfdual higher-Sp3 gate remains open.


## E832/E832R — independent complete reviews, 2026-11-21 20:58:56 UTC

The complete frozen base0542dce9 and reversed addendumdc18d6bf passed separate whole-proof reviews, with actual E825 determinant interface reopened in full. No new external premise is used: published BF and supplied S21 retain their previous exact statuses. ELLIPTIC_STAR_PEER_AUDIT.md records all universal arguments and the precise actual unit/free architectures. Independent exact algebra passed after an auditor structural-equality predicate repair, which is retained honestly in audit_elliptic_star_attempts.json. No new numerical check is claimed for the sign-only reversed addendum.


## HOS13–15 — characteristic-three cutoff, author completion 2026-11-21 21:08:58 UTC

Full new proof is higher_odd_symplectic_three_cutoff_section.tex, frozen42ccec86bd4fa25e91c9156204e215e901f3b8ea6a175c9012ba2948dae72bba. It proves every order3 element has projective support at least2a/9, then uses the uniform published character theorem only for semisimple elements with no±1 eigenvalue, whose algebraic-closure natural support is at least half the natural dimension. Nonselfdual q3 full normalizers are scalar times inner by the actual class-inverting diagonal automorphism. Arbitrary nonselfdual tensor cores of natural ranks at least10^30 are excluded; with HOS12, transitive q3 sources satisfy n<10^30. Smaller nonselfdual ranks remain open.

Freshly reopened https://arxiv.org/pdf/2403.09046 (turn495157790view0/1) and read the complete Theorem5.5 proof, author pp25–26, in retained author text. It explicitly covers Sp(V), denominator is dim(V), and exact sigma is1/(6507*2^21*10^18)>7e-29. The proof uses the weaker10^-29. Publication metadata Annals200(2024)1–70, DOI10.4007/annals.2024.200.1.1, retains the prior verified scope; journal PDF retrieval was not newly claimed. Vinroot2004 Theorem1 authorp1 was reread in the full retained original source, confirming all characteristic-not-two symplectic elements factor into anti-symplectic involutions. Complete HHM exceptional cover listp35 and LiXia Table2.1p14 retain the prior fresh source checks; their q3/n≥4 applications were rechecked. Existing bibliography keys suffice, so no duplicate bibliography is introduced.

The new full proof received an initial complete parent reading PASS, then added its requested explicit unitary-carrier normalization. Independent peer audit is pending. The author's exact first run passed0.223845771s; its finite scope is explicit. No successful TeX compilation is claimed.


## E833 mixed-star cubic audit — 2026-11-21 21:10:42 UTC

Full frozen2a74ada9 passed independent whole-proof and author-code reading. MIXED_STAR_CUBIC_PEER_AUDIT.md records the universal singular/invertible compound arguments, actual full cubic, and precise actual E825 defect interface. Independent eight-generator exterior reconstruction passed on its first run0.285877600s. No new external source is needed; reviewed E832/E825, published BF and supplied S21 retain their exact scopes. This closes only the stated single-center square-zero architecture.

## D-HOS16: published restricted-support sharpening (2026-11-21 21:17:38 UTC)

Primary full published source: M. Larsen, A. Shalev, P. H. Tiep, The Waring problem for finite simple groups, Annals174(2011)1885–1950, DOI10.4007/annals.2011.174.3.10. URL https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf . Frozen local sources/LST2011_Waring_published.pdf, SHA256 dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e; retrieval21:12:31UTC,796737bytes. Read Definition4.1.1 and (4.1.1)p1907; complete Theorem4.3.6 and proofpp1917–1923; Remark4.3.7p1923. Rendered/read publishedp1918 andp1923 to verify sqrt(N/7), the exact allowed scalar set mu2, and the remark's full conclusion. Published domain is the rational points of a simple simply connected classical algebraic group, including Sp perfect covers and nonfaithful inflated ordinary characters. No new classification/table proof claimed.

New separate proof higher_odd_symplectic_three_sharp_section.tex freezes at ce8fc689891738dbf571cdae6f92879bca88937129ac66bf278b6ec6f72cdd3f. The standard support gives n>=567; the explicit published mu2 support gives n>=284 because the residual no-±1 semisimple element has restricted support2n. Rational certificate first actual PASS0.001372407s; delta189312302221/1024000000000>1/6, degree ceiling1536000000000/55936906663<28. Combined actual intermediate Hurwitz and nonselfdual normalizer argument leaves transitive half-ranks4..283. Parent/sibling review remains separate. D-HOS13–15 frozen text is unchanged.

## Independent D-OL06–08 audit (2026-11-21 21:25:01 UTC)

Full frozen fefeade2 proof and author code PASS; report ORTHOGONAL_SUPPORT_PEER_AUDIT.md. Fresh original corrected Taylor author book complete invoked statements/proofs pp57–58,138–140,157–163 at https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf ; full published Taylor–Vinroot2018 Lem2.1p383 at Cambridge DOI10.1017/S144678871800006X. Li–Xia Table2.1p14, Liebeck2017 conventions/Th2.4pp2–4 and full published GLT2024Th3.7pp165–167 reread. Exact source domains and reused KTV/OL interfaces are itemized in report. Own direct hyperbolic-basis/full-GL2 reconstruction first PASS2.739600632s; no author data/code imported. It does not certify universal dimension by finite enumeration.

## Received independent HOS13–16 audits (2026-11-21 21:25:01 UTC)

Sibling /root/imprimitive completed HOS13–15 frozen42ccec86 whole proof/source/code PASS21:17:03UTC (audit_symplectic_three_cutoff/PEER_AUDIT.md SHA8c8b1a5c...) and HOS16 frozence8fc689 PASS21:22:53UTC (audit_symplectic_three_sharp/PEER_AUDIT.md SHA9ee67f20...). The latter report was read completely here. Their actual independent certificates and source scopes are distinguished from author execution in CHECK_EVENTS. No author text status or frozen mathematics changed.

## SF-E834 peer source check — 2026-11-21 21:30:18 UTC

Bando–Siu1994 original author images pp39–40 visually read, admissibility and Theorem3, plus relevant full proof textpp45–49. Source https://people.math.harvard.edu/~siu/bando_joint_paper/index.html . Biswas2011 published complete paper, pp71–78, especially Theorem3.2 and complete proofp77, freshly read via primary J-STAGE PDF https://www.jstage.jst.go.jp/article/kodaimath/34/1/34_1_71/_pdf/-char/en . Retained sources/Biswas2011_extension_published.pdf SHA6fa0c6645b1e7bb5797b2f4fb983d957d945afce363772fd4e9e11e29da70e42. Upstream Harris–Tonegawa full proof was not retrieved; only exact published Biswas use is claimed. Full mathematical audit REFLEXIVE_MIXED_CURVATURE_PEER_AUDIT.md; no numerical certificate.

## SF-E835 peer source check — 2026-11-21 21:31:49 UTC

Fresh full statements/proofs at https://stacks.math.columbia.edu/tag/0G7P (regular-sequence local cohomology), https://stacks.math.columbia.edu/tag/0A39 (support triangle and spectral sequence), https://stacks.math.columbia.edu/tag/0AVZ (depth characterization). Entire current E818 canonical theorem read, including strict surface positivity and final equivariance interface. Fulton support-cycle input reused in precisely earlier-reviewed scope, not freshly reconstructed. Full new actual-extension proof independently checked; SEMISTABLE_REFLEXIVE_REDUCTION_PEER_AUDIT.md.

## HOS17–19 finite-form and subgroup-invariant source inputs — 2026-11-21 21:39:34 UTC

Taylor, The Geometry of the Classical Groups (1992), corrected author https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf, full finite Hermitian classification/norm/order derivationpp115–118 and full finite orthogonal order derivationpp138–141 freshly read. Retained sibling orthogonal_lowlevels/cache/TaylorClassicalGroups.pdf/.txt. Full ordinary U/O group orders, not special/projective orders. Larsen–Shalev–Tiep2011 full published Proposition4.2.3 and entire proofpp1909–1912 freshly read from sources/LST2011_Waring_published.pdf/.txt: exact restriction subgroup, N≥8, fixed fraction<q^(8/3−N/2); symplecticstep4 and finalsumstep6 read. PublishedprimaryURL https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf . No new proof of the known branching result claimed. Entire new universal orbit/support proof authored in higher_odd_symplectic_three_involution_section.tex; exact supplement separate.

## D-OL09–11 peer source check — 2026-11-21 21:43:33 UTC

Exact published LST2011 conventionp1907, Theorem4.3.6pp1917–1918, proof finalparameterpp1922–1923 and Remark4.3.7p1923 rechecked for Spin/mu2 characteristic2. Full theorem proof was read in the immediately earlier HOS16 source review; no new Gluck proof reconstruction. Author primary https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf . All prior OL06–08 generation, arbitraryq natural-normalizer and cyclic descent proof interfaces reread. Prior full Taylor/LiXia/GLT source checks remain precisely identified in ORTHOGONAL_SUPPORT_PEER_AUDIT.md. New whole proof report ORTHOGONAL_NONEXTENDIBLE_PEER_AUDIT.md.

## HOS20–22 source scope — 2026-11-21 21:52:57 UTC

New semisimple quotient/primary/centralizer proof does not import a finite character classification. Taylor corrected author book Theorem11.4/fullproofpp139–140 gives O2±(3)orders4/8; Lemma10.2/Cor10.3/full finite Hermitian decompositionpp116–117 used after explicit trace-duality construction. LST2011 Proposition4.2.3/fullproofpp1909–1912 was freshly read for the preceding HOS18 and its exact restriction scope rechecked here; Lemma4.3.1p1912 and its complete one-paragraph column-orthogonality proof read. Existing HOS:Taylor1992/HOS:LST2011 bibitems suffice. No new upstream classification or Gluck proof claim.

## SF-E837 peer scope — 2026-11-21 21:58:21 UTC

Entire frozen196-line proof and author code/output read. The preceding E836 whole draft was reread, especially both actual companion matrix orders; E819 published BF/local supertrace bridge retains its previously checked scope. The general Eisenbud–Ulrich Jacobian theorem is not needed by this square quotient argument and was not newly audited. No new external source premise. Complete report SQUARE_ARTIN_MATRIX_PEER_AUDIT.md; independent15-graph/four-parameter symbolic certificate audit_square_artin_matrix.py/.json.

## Received complete HOS17–22 peer reports — 2026-11-21 21:59:07 UTC

Both sibling reports were read completely here: audit_symplectic_three_involution/PEER_AUDIT.md SHA1be0a857 and audit_symplectic_three_semisimple/PEER_AUDIT.md SHA83a3fbdb. Their full proof/source/code checks and independently executed finite witnesses PASS, with actual times and frozen author hashes in CHECK_EVENTS. The latter reuses the full LST/Taylor primary passages freshly read in the immediately preceding former audit and says so explicitly. No claimed fresh re-reading or re-proof of the published inputs beyond those stated scopes.

## Fomin–Lulov1995 original proof source — 2026-11-21 22:03:11 UTC

Complete original §§1–2 pp219–223 freshly read through the official Mathnet full-text link and a clean indexed extraction of the same published paper. Theorem1.1 and character equalityp220, Corollary2.2/Theorem2.3p221, full Möbius proofpp222–223 and final theorem deductionp223. Exact factorial normalization confirmed. Record https://www.mathnet.ru/eng/znsl4388; direct ordinary full-text https://www.mathnet.ru/php/getFT.phtml?jrnid=znsl&option_lang=eng&paperid=4388&what=fullt . Fresh web PDF8pages succeeded; local binary downloads403 and screenshot textplaceholders mean no visual claim. Retrieval/source JSON retains these distinctions. Author oldPS502, newhost404; subscription translation not accessed.

## HD-ALT07 complete peer check — 2026-11-21 22:06:39 UTC

Final frozen78ffa543 proof/bib and authorcode/output read in full. New original Fomin–Lulov source check is recorded above; fresh entire GKT2019 Th9.7 proofpp312–313 at https://msp.org/tunis/2019/1-3/tunis-v1-n3-p01-p.pdf confirms exact degree-only consequencep312. No semisimple-regular premise imported, no fresh Rasala reconstruction. Report ORDINARY_ALTERNATING_FIXED_FREE_PEER_AUDIT.md; independent15578partition exact supplement and corrected strictness witnessPASS.

## D-OL12–13 independent review — 2026-11-21 22:13:25 UTC

Fresh complete KTV2023 invokedpp39–45 read at https://www.advgrouptheory.com/journal/Volumes/16/KimTrefethenVinroot.pdf : fullO realityTh1p44 andexactquotients§2. No fresh Wonenburgeroriginal audit. Exact LST bound/finalparameter/Remark4.3.7 rechecked fromretainedpublishedtext; fullproofpreviouslyread. GLT2024Th3.7 invokedproofpp165–167 reread. Complete new proof and authorcode/output checked; full report ORTHOGONAL_ODD_NONSELFDUAL_PEER_AUDIT.md. Separate exact216distribution/13Dsymbolic supplementPASS, initialserializationfailurehonestlyretained.

## SF-E839 source and independent audit — 2026-11-21 22:19:10 UTC

Whole frozen proof7d17ecc2 and all invoked E838/E836 interface passages checked. Fresh complete published Eisenbud–Ulrich Theorem7.1/A.1/A.3/A.5 statements and proofs read at pp210,222–225 from author-hosted published PDF; precise source hash and scope in sources/EisenbudUlrich2019_source_check.json. No visual claim and no reconstructed upstream different theory. Separate exact quotient-ring/all36minor certificate passed; full scope in RANK_FIVE_JET_PEER_AUDIT.md.

## D-OL14–15 peer audit — 2026-11-21 22:26:14 UTC

Full frozen7d0e8c1e proof and whole author program checked; new all-order negative-reflection classification and actual12-generator contradiction pass. Fresh Taylor11.47–48 complete proof161–162 and LiXia2.2.2/Table2.1p14; precise LST/reusedKTV/GLT scopes in ORTHOGONAL_THREE_ODD_PEER_AUDIT.md. Own exact fractions,252norm distributions,distinctorder8/17Dand12reflection/15D matrices pass. No new classification premise or failed run.

## D-ATT01–03 two-box alternating tensors — 2026-11-21 22:30:42 UTC

Fresh full EX/UP spectral proofs and root scalar/conductor proof read; all new rational k2normalizer and trace premises proved in full. Milne v4.03 ChapterV exactcompleteExample3.2p157,Remark3.8p158,Examples3.10–11p159 freshly read through primary web PDF; details in sources/MilneCFT2020_two_tail_source.json. No equality of original and inducingfields. Exact finite supplement passed; peer pending.

## D-ATT04–06 two-factor all-degree refinement — 2026-11-21 22:37:21 UTC

Separate frozen fullproofb7a5a8d6; no changes to ATT01–03. Commonindex follows from the complete previouslyrecheckedUP/EX proofs. Scalarfields/normalizers follow reviewedATT02. New weighted-swap and actual2n-letter quotient Riemann–Hurwitz arguments are written in full. No new published classification or numeric premise. Exact supplement passes; peerpending. SiblingATT01–03report52e5c87c was wholly read and recorded.
