# Part B source and search log

All entries below are activity of GPT-6 Astra (OpenAI), run `/root/part_b`, on 2026-11-20. Sources were opened and read where marked; search metadata alone was not treated as a theorem. No claim of original discovery is made.

## Inputs and exact manuscript passages

- Full task prompt: `upload/PROMPT(20261120-001029).md`, Part B, L6, proof and delivery rules.
- Pro transcription: `inputs/RESEARCH_SA12_transcriptions/transcriptions/Pro_MPL_29_049-094/MPL_29_049-094_transcription.tex`, scans071–077 (approximately lines916–1188).
- Parallel Codex witnesses: `Codex_K29-05/K29-05_transcription.tex`, scans071–076, and `Codex_K29-06/K29-06_transcription.tex`, scan077 at the beginning.
- Prior study: `readings/c29a.md`, lines338–389, and CHECK_EVENTS rows for MPL_29_049-094 (29:71–76), SA12-9 H07T and SA12-10 H061. These were used as claims to check, not as authority.
- Scan076 says **there exists** an integer n(K/k); scan077 says genus of a generic curve in a fixed projective model is an allowable value. Thus our genus bound addresses the indicated constant, not merely an unrelated inequality.
- The tensor K⊗k kbar in scan076 need not be a single field when k has nontrivial finite separable constants in K; the proof includes the disjoint-component correction.

## Opened mathematical sources

1. Andrea Marrama, *On the restriction of finite torsors*, CR Math364 (2026),431–435, DOI10.5802/crmath.836. Published PDF downloaded and full text read. Proposition3 p432 is full faithfulness over normal bases; Theorem6 pp433–434 is Moret–Bailly purity for every finite flat group over a regular base and complement codimension≥2. The PDF says online27July2026. Direct web parser403; local fetch succeeded. Its complete proof was checked, including the finite Isom scheme and the Auslander step. An early index result wrongly associated the title with arXiv2512.00235; opening that arXiv paper found unrelated set theory. That identifier is excluded.
2. Original Moret–Bailly1985 paper was located at author URL `https://perso.univ-rennes1.fr/laurent.moret-bailly/articles/PurCourbesWeb.pdf`. Web open timed out and local fetch returned503. Its Lemme2 is credited through Marrama's fully opened proof; no claim yet that original PDF has been read.
3. Michel Raynaud, *Spécialisation du foncteur de Picard*, PMIHES38(1970),27–76. Original Numdam PDF opened and downloaded. Proposition6.2.1 and proof pp50–51 read. Universal H0 condition and Cartier-dual orientation checked explicitly. Agent C independently found the same locator in Mehidi–Poiret2025 Theorem2.2.
4. Steven Kleiman, *The Picard scheme*, arXiv math/0504020 (2005), full TeX source and PDF opened. ArXiv numbering: Theorem5.4, Remark5.6 normal proper Pic0; Theorem5.11 and Corollary5.13 tangent/dimension; Remark6.19 Picτ finite type and NS finiteness. The arXiv source is a gzip-compressed single TeX file although downloaded with a `.tar` suffix.
5. Chatzistamatiou–Rülling, arXiv0911.3599v2 (2011), Corollary3.2.7, p47; statement permits arbitrary ground field and proper birational smooth schemes. Published ANT5(6),693–775, DOI10.2140/ant.2011.5.693. Authors' one-page erratum also opened in full: it corrects the domain of a correspondence functor to proper morphisms and does not alter this result or its proof.
6. Joseph Lipman, *Desingularization of two-dimensional schemes*, AnnMath107(1978),151–207. Author-hosted original PDF opened; Introduction Theorem p151 explicitly includes excellent surfaces.
7. Stacks Tag0G4F (Lemma37.32.3) read with proof: generic geometric irreducibility for basepoint-free linear systems satisfying the codimension-two triple condition. Used on finite pullbacks as well as original model. Tags0FD4 and0FD6 (Lemma33.47.3) read for generic smoothness. Tag0A3P (Lemma59.63.6) read for Artin–Schreier field-extension invariance; its proof uses finite-dimensional semilinear linear algebra rather than fundamental groups. Tag0A4T read for proper coherent fibre-dimension vanishing. Tags0EC0 and03RP read for Frobenius flatness and abelian torsion/divisibility; Tag0BFH read for etaleness of multiplication by invertible n.
8. Hogadi–Mehta, *Birational invariance of the S-fundamental group scheme*, arXiv1006.5306, PDF and source opened. The initial local PDF name `Biswas_Parameswaran_1006.5306.pdf` was a mistaken descriptive filename; actual authors are Hogadi and Mehta. Theorem2.1 gives anti-ample H1 vanishing for numerically flat bundles on normal projective varieties, but its n depends on the chosen variety, so it is not used as an unproved uniform assertion.
9. Stefan Schröer, *Albanese maps for open algebraic spaces*, IMRN2024(6),4963–5004, DOI10.1093/imrn/rnad187. Opened author's second revised version1July2023, 34pages. Theorem2.2: Picτ quotient is affine for modifications over proper regular target (source may be nonnormal). Proposition3.3 and Lemma4.1 concern abelian parts, not all infinitesimal Picard structure. Page12 explicitly retracts an earlier Macaulayfication argument: it need not produce a normal source. This warning is recorded and no such inference is used.
10. ILO source shared by root: `RESEARCH_SA12/sources/ILO2012/tex/exposes/de-Jong.tex`. Read the definitions around lines1380–1410 distinguishing separable Galois alterations from de Jong Galois alterations admitting a purely inseparable intermediate extension. Original de Jong1997 source located (DOI10.5802/aif.1575), being opened for the remaining constancy gate.

## Searches used to test prior literature and remaining gates

Searches (both available engines used where coverage was thin) included:

- finite flat torsor purity regular normal codimension two; Moret-Bailly purity; Raynaud Proposition6.2.1 Picard Cartier duality;
- normal projective models function field irregularity bounded Picard scheme birational characteristic p;
- Picard scheme birational normal models inductive limit bounded H1;
- normal varieties Picard scheme birational finite height stabilization;
- "birational" "Picard" "essentially constant";
- "normal" "irregularity" "bounded" "models";
- "Picard" "birational" "infinitesimal" characteristic;
- "birational Picard" "scheme"; "Picard" "Riemann-Zariski";
- "Picard" "birational" "smooth quotient"; "schémas de Picard" "birationnel" "constant";
- "birational" "fundamental group scheme" "normal" "models";
- "Picard scheme" "modifications" "normal" "finite";
- "Albanese maps for open algebraic spaces";
- "Galois alteration" "regular" "purely inseparable" de Jong; de Jong1997 Theorem5.9 and Corollary5.15;
- Stacks searches for Bertini, proper Artin–Schreier base change, fibre dimension cohomological vanishing, Frobenius flatness, abelian multiplication and torsion.

The searches found authoritative inputs for B.1 and the generic-curve proof, but no opened theorem stating full Picτ stabilization for arbitrary normal models of one function field. This is a statement about this search, not a claim that the assertion is absent from the literature.

## Executed code and reproducibility

- `code/finite_certificates_B.py`: 3 Hopf algebra cases p=2,3,5, 38 source monomials, plus F2/F4 cubic checks (70 nonzero projective triples). Output in `code/output/finite_certificates_B.json`; runtime recorded there, all checks passed.
- `code/fetch_sources_B.py`: concurrent independent source downloads, PDF-to-text extraction, source SHA256 values, HTTP failures, durations; output in `code/output/fetch_sources_B.json`. This reproduces or reuses the prior manual fetches and captures actual source bytes.
- Prior exploration used `rg`, `sed`, `cat`, `pdftotext`, and small Python/urllib downloads and gzip extraction of the two arXiv single-file sources. These are document inspection/extraction operations, not unrecorded mathematical computations. The source bytes, extracted texts, URLs and provenance are retained.

## Independent audit received

At this run's first-draft stage, root independently read B.2a–b and the arbitrary-field reduction. It checked the common geometric generic curve, that E-defined Frobenius-fixed classes descend to k before applying finite-cover Bertini, and the differential/conormal injection. No gap was found in these audited steps. Logged as a targeted proof check, not an independent discovery.

### 2026-11-20 01:45--01:53 additional opened sources and searches

- Milne, Algebraic Groups, 2nd ed.2022, official author URL https://www.jmilne.org/math/Books/iAG2022.pdf. Opened Theorems5.14/5.28 (quotient existence), Proposition5.25 (faithful flatness), Theorems5.34/5.39 (monomorphisms and image factorization), pp102--108. The generic URL AG.pdf failed; corrected canonical iAG2022.pdf was verified by title page. These results include nonreduced finite-type group schemes over arbitrary fields.
- Stacks Tag0CCJ, Lemma39.25.3, opened proof: effective descent for a quasi-projective scheme under a finite locally free base change. Used in B.2h.
- Stacks Tag0BXT, Lemma33.27.4, opened proof: geometric normalization after finite purely inseparable ground extension. This gives a field-extension model, not a geometrically normal model over the original k; hence it does not close B.2-U.
- Schröer2024 revised author PDF §§6--7, Theorem6.1/Proposition6.2/Theorem7.5 read: base-change defect of open Albanese under purely inseparable extension; Weil restriction has abelian anti-affine kernel. Does not provide the desired geometric-normal graph theorem.
- Search strings: "geometrically normal" "common" "birational" models; "geometrically normal" "blowup" normalization imperfect; "geometrically normal" "modification" "dominating"; "geometrically normal" "birational models" "filtered"; "geometrically normal" "graph" "normalization"; Picard scheme "models" "stabilizes" normal; "Picard" "birational" "eventually constant"; "Picard" "Riemann-Zariski" scheme; "Picard scheme" "generic curve" normal; Milne Algebraic Groups quotient theorem5.28; SGA3 VIA3.2 quotient groupe corps; Stacks quasi-projective descent datum effective field.
- A search located Kollár--Smith--Corti, Rational and Nearly Rational Varieties, Exercise3.8, concerning blowup of (x^p-a,y^p-b). The full exercise was visible only through a nonpublisher mirror; we do not cite it as an opened primary source. Our B.2i proof explicitly computes all needed local rings.
- Root A audit primary source: https://www.jmilne.org/math/Books/ADTnot.pdf opened, local copy RESEARCH_SA12/sources/Milne/ADTnot.txt, II2.3a pp166--167, II3.1/3.2 pp177--178, I2 pp27--29. Targeted independent check, not independent discovery.

### 2026-11-20 02:02--02:08 finite-group detection and imperfect descent

Opened local canonical MilneAG2022 text: relative Frobenius2.24--2.29 pp47--49; Barsotti--Chevalley Theorem8.27 pp154--155; commutative affine decomposition Theorem16.13 pp328--329. Opened Kleiman Proposition6.12, Remark6.14, Remark6.19 pp57--60 for finite type and proper nonprojective Picard representability. Checked all hypotheses rather than assuming geometric normality. Searches used both engines: geometrically normal Albanese compactification graph; normalization graph abelian variety imperfect; geometrically normal rational map abelian variety; regular scheme rational map abelian variety extension. Found Kollár2026 Néron models/minimal models (arxiv2502.13800) and Achter--Casalaina-Martin--Vial2025 Albanese base-change paper as possible primary sources; no graph lemma asserted from their metadata.

### 2026-11-20 02:20--02:47 primary sources and rejected shortcuts

- Cotner--Zavyalov, *Lefschetz theorems in flat cohomology and applications*, Compositio160(2024),1850--1870, DOI10.1112/S0010437X24007231, arXiv2204.06121v3 PDF/TeX read, Lemmas3.4.1--3.4.3 pp14--16. The isomorphism criterion includes geometric torsion points, Lie algebras, and fppf surjectivity on all p-power torsion group schemes. Related to B.1; it is not a model-stabilization theorem.
- Stacks02KH,0EBJ,0BCY,0BD2 opened including proofs for B.2j--k: flat base change, reflexive extension, line-bundle norm, and compatibility for finite locally free norms. Arbitrary parameter schemes are covered.
- Achter--Casalaina-Martin--Vial, author manuscript dated17March2025 at https://www.math.colostate.edu/~achter/math/alb.pdf: Theorem3.2 pp11--12 proper geometrically reduced/connected Albanese and all-field base change; Proposition4.5 pp15--17 descent of a pointed morphism to a fixed k-abelian variety through pure constants; Lemma5.3 p19 smooth-open invariance. These do not supply geometric normality of the normalized graph. The final AIF volume is76(2026), not a publication-year2025 inference from the manuscript date.
- Kollár, arXiv2502.13800, Section35 p11 and Section33 read: extension via a Poincare family invokes vanishing of R^1p_*O in that argument. We do not apply it to an arbitrary normal source.
- Geisser, corrected primary manuscript https://www2.rikkyo.ac.jp/web/geisser/picard_corrected.pdf: Theorem3 and footnote5 on p5 read. The latter reports Gabber's private2020 construction, not an explicit construction available here; no counterexample is inferred from it.
- Ravindra--Srinivas, arXiv math/0511134v1, *The Grothendieck-Lefschetz theorem for normal projective varieties*, §5 pp17--18 opened. The author-hosted math.umsl.edu and cs.umsl.edu URLs timed out; arXiv PDF downloaded successfully and extracted. The arbitrary-field Weil-Picard sentence does not assert a geometrically normal graph or Cartierizing modification; Theorem5 itself assumes algebraically closed k.
- Boissiere--Gabber--Serman, arXiv1104.1861v4 dated27May2019, *Sur le produit de variétés localement factorielles ou Q-factorielles*, pp1--4 and Proposition3.2 opened. The entire paper assumes algebraically closed k. No imperfect-field graph statement is imported.
- Stacks01ZM,038O,038P opened including proofs for B.2l: finite-presentation descent (with morphisms and equalities), normality over the perfect closure, and field independence of geometric normality.
- Search strings (both engines, adaptively): Weil Picard imperfect; Weil Picard base change; normalized blow-up divisorial geometrically normal; reflexive blowup geometrically; divisorial ideal base change normalization; divisorial Rees imperfect; Albanese modification geometrically normal; graph Albanese imperfect normal; rational map abelian variety geometrically normal graph; geometrically normal smooth alteration; geometrically normal alteration imperfect; alterations smooth separable imperfect field. Recent automatically generated course pages and discussion sites were not used as mathematical authorities.

### 2026-11-20 02:53--02:57: arbitrary alteration constants

Opened Stacks Section97.11, Tag05Y8, including Lemma97.11.2 (base change), Proposition97.11.5 (algebraic-space representability) and proofs. B.2m only requires the separated Weil-restriction sheaf; closedness of its diagonal is checked by coefficient equations. Existence of Y uses the already opened de Jong1997 alteration over kbar and finite-presentation descent, with no restriction on finite constants l/k.

### 2026-11-20 02:59--03:04: surface upper-cone argument

Opened original Lipman1969 Numdam PDF https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf. Read Definition1.1 and Proposition1.2(2), printed199--200, including the quadratic-transform proof; read Theorem12.1(i) and proof, printed220--221. The theorem assumes proper fibres of dimension at most1 and H1(O)=0 and says degree0 on every integral exceptional curve is equivalent to triviality over a local base. These locators are now used in B.2n--o. Full local PDF download is slow and is being resumed; opening/verification is complete through the primary web PDF.

### 2026-11-20 03:07--03:17: first direct-image vanishing

Re-read Marrama2026 primary text Proposition3 p432 and Theorem6 pp433--434: locally Noetherian normality suffices for full faithfulness, and every regular base with codimension-at-least2 complement admits finite-flat torsor purity. No perfectness or field-base hypothesis occurs. Opened Stacks06DI (normality under strict henselization),06LN (regularity),02KE Lemma30.5.2 (flat cohomology base change),03DW Proposition35.9.3 (quasi-coherent cohomology independent of fppf/Zariski topology). These exact locators support L6c. Lipman1969 local full PDF download completed before03:07:28,9460787bytes,86pages; pdfinfo validated it.

## 2026-11-20 03:43 — primary sources for the threefold cofinal counterexample

- Opened Stacks Tags045M (tensor products of fields are Cohen–Macaulay in the stated Noetherian scope),0339 (flat ascent of Serre conditions),031S (normal iff R1 and S2). These justify geometric S2 and the partial-graph normality argument; they do not assert that every normal scheme is geometrically normal.
- Opened Milne, Elliptic Curves, second edition2021, official EC2.pdf, ChapterI§3 Theorem3.1 printed25–27: chord-and-tangent group law. The characteristic3 flex calculation is proved and program-checked here, not inferred from an unverified Hasse invariant.
- Reopened Achter–Casalaina-Martin–Vial author manuscript alb.pdf, Theorem3.2 printed12 and Remark3.3 printed13: proper geometrically connected geometrically reduced schemes have Albanese data compatible with field extension; the Albanese is dual to the maximal abelian subvariety of Pic. Bibliography key C_ACMV2026 is supplied in the shared C bibliography. This applies to the normal geometrically integral comparison graph even though it need not be geometrically normal.
- Exploratory only: opened Cossart–Piltant2019 author draft Theorem1.1 printed3–4 (regular resolution of quasi-excellent threefolds); Laurent–Schroer2024 primary Springer article on maximal abelian subvarieties and Albanese; Nagamachi–Takamatsu arXiv2110.03917 on imperfect-field Picard groups. None is cited as proving the residual weak image gate.

## 2026-11-20 04:05 — no-torus and regular-model inputs

- Reopened Tanaka arXiv1502.01381v4, Lemma2.2(2), pp6–8: normalization of the reduction after any field extension of a normal variety is a universal homeomorphism.
- Reopened Kelly July4,2018 manuscript, Corollary20 p9: finite universal homeomorphism admits a fixed Frobenius factorization when the structure-sheaf kernel is nilpotent. The proof is applied to all Picard parameter schemes by Frobenius on both factors.
- Opened Cossart–Piltant arXiv1412.0868v2 (January8,2019), Theorem1.1 pp3–4, and compared the earlier2014 author draft. Arbitrary-field quasi-excellent dimension-at-most3 regular resolution is explicit. Publication metadata confirmed in the primary Journal of Algebra page.
- MilneAG2022 Theorem5.39 is the faithfully-flat-onto-image theorem; Theorem8.27 is Barsotti–Chevalley. D reopened the exact pages.

## Closure of arbitrary-field weak stabilization

The exact de Jong1997 Galois-alteration inputs were reread, including Situation5.3 and condition5.12.1, Theorem5.13 and Corollary5.15. The construction is first used overkperf, and all finite separable constants and semilinear actions are retained during descent. The all-parameter Picard finite-constants identification is proved directly using a smooth affine open and a generator-open trivialization; it is not quoted as an equality of tau-components. Stacks0200 (Chow lemma30.18.1) was opened directly and used only to make the fixed normal divisor model projective; it is not used to assert geometric normality of an arbitrary refinement. Root, C and D independently audited the complete written chain within their recorded scopes.
