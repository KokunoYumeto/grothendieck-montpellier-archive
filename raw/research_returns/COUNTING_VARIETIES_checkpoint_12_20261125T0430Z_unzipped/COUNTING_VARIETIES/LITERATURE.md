# Literature search and source audit

Initial undated entries refer to 24 November 2026; later entries carry their own dates. Research clocks and timed entries use UTC. Public sources are cited and linked, not redistributed. Attached sources are read in place.

## Core searches

- Search engine 1: `"Hasse invariant" "smooth" "affine line" hypersurface stabilization`; `"Frobenius" "#P" smooth hypersurface Hasse Witt complexity`; `site:hexagonmath.org Frobenius counting hypersurfaces Katz`; `site:eccc.weizmann.ac.il polynomial counting finite fields sparse`. Found Katz-related Hasse--Witt computation and recent Dwork-family work; no matching complexity theorem established by the search. This is not a proof of absence.
- Search engine 2: `"KokunoYumeto" "mathematics-workbenches" "FORMAT"`; `"Wan" "Theorem 1.1" "sparse" "p-adic"`; `"Hasse-Witt invariants of Calabi-Yau varieties" 2026`; `"Huang" "Lian" "Yau" "Yu" "Frobenius splitting"`. Found Cao--Elmi--Movasati arXiv:2603.03055 and HLYY author manuscript; source audit continues.
- Katz author PDF opened. Printed pp. 35--36 visually read: Algorithm (2.3.7.14), Special Case (2.3.7.17), Dwork pencil (2.3.7.18)--(2.3.7.23). Attached byte copy SHA to be recorded.
- Wan attached PDF pp. 1--3 read, including Theorem 1.1 on p. 3. The requested author URL returned HTTP 502 through retrieval.
- Workbench FORMAT.md GitHub and raw URLs both failed retrieval; public search did not recover the text. Exact format conformance is not yet verified.
- Hexagon 2611.00789v1 opened; scope and provenance recorded. Its earlier third-party checks do not certify the new paper.

## Subsequent retrieval and recent comparisons

- The raw `main` branch of `KokunoYumeto/mathematics-workbenches/FORMAT.md` was successfully retrieved after the initial failures. Format 1 is dated 22 November 2026. It requires a version directory, statement tags, typed additive check events, source links and hashes, and a version manifest. The user reserves the work number and permanent page for filing; no number or public commit has been invented. The packaging records distinguish this predeposit state from an already deposited immutable version.
- Queries concerning Betti bounds, zeta-function information, smooth projective multiplicities, and recent Dwork cohomology led to Wan–Zhang, arXiv:2501.12623v1 and arXiv:2207.12633v2, and to DiPippo–Howe, arXiv:math/9803097v3. The author PDFs were downloaded and hashed. Read locators: Wan–Zhang Betti bounds, introduction, Theorem1.1.2 (p.2), Corollary1.1.4 (p.3), Theorem1.2.2 (p.4), and the projective Corollary5.5.8 (p.38); visibility, introduction and Theorem1.3 (p.2), with publication metadata and journal renumbering checked; DiPippo–Howe, pp.1–3 including Theorems1.1–1.4 of the corrected 2000 author version. The projective bound is Corollary5.5.8, not the affine Corollary1.1.4. These are comparison results, not premises for the elementary information bound.
- Search-engine1 queries for recent AI-laboratory mathematical advances led to OpenAI's updated *Ten advances in mathematics and theoretical computer science*. The official PDF, updated6August2026, was opened and downloaded. The abstract and Chapter5, pp.114–116, were read, especially Theorems1.1–1.3. It reports formal symbolic permanent lower bounds over C; the counting paper compares that model with numeric finite-field permanent evaluation and does not use those preprint results as a dependency. The full lower-bound proofs were not checked in this task.
- Queries for sparse polynomial factorization, bounded individual degree, sparse cofactors, and sparse rational interpolation led to ECCC2026/036,2026/105,2026/108 and CCC2026 paper20, with the precise revisions checked in the presentation contribution. The October revision of ECCC2026/108 removes the characteristic restriction of its original June version. A separate smoothness obstruction shows why a fixed individual-degree bound on the input multiples cannot cover growing-dimensional anticanonical hypersurfaces.
- The requested complete English SGA2 edition was read in contiguous divisions covering its mathematical front matter, all fourteen exposés, and indexes. Exact reader-specific coverage and source caveats are recorded separately. The French XII.3.7 statement was also checked. Reading the book does not turn its existence theorems into effective polynomial-size compression results.

## Saturation algorithms: 21:10–21:35 UTC

- Searches for sparse factorization, low-total-degree factors, and low-degree cofactors found Kumar–Ramanathan–Saptharishi (SODA2024) and Dutta–Sinhababu–Thierauf (RANDOM2024). Their sparse-input bounds do not directly give the proposed polynomial algorithm at fixed small characteristic. This factorization route was not used to assert such an algorithm.
- Kaltofen–Trager (1990), *Computing with polynomials given by black boxes for their evaluations*, §3 pp310–311, was read in full for its gcd mechanism. It constructs general gcd evaluation using randomized projections and addresses extra common factors after specialization. The saturation promise in the theorem here gives a unit ideal of cofactors on every affine line, which removes that particular exceptional-line issue. The source is credited for black-box gcd context; no priority claim is made for the resulting special-case algorithm.
- Search queries included `Klivans Spielman deterministic sparse polynomial interpolation arbitrary finite fields degree bound reconstruction Theorem 3.2 Chuyoon Shpilka 2026` and `Klivans Spielman 2001 Randomness efficient identity testing multivariate polynomials pdf Theorem 11`. The author-hosted Klivans–Spielman PDF was downloaded and hashed. Its encoded text layer is unreadable, so §§6.2–6.3, authorpp11–12, were rendered/OCR-read. Theorems10–11 state the finite-field extension version with polynomial numeric degree dependence. The proof's illustrative scaling by2 was checked through the arbitrary scaling variable in Chuyoon–Shpilka's explicit generator, which works also in characteristic2.
- Chuyoon–Shpilka arXiv:2603.07589v1, §3 pp16–17, was opened both as HTML and PDF. The field-size setup, Definition3.1, and Theorem3.2 give ordinary sparse-polynomial reconstruction in arbitrary characteristic. The separation of exponent vectors by integer-prime weight maps, followed by scaled-variable bivariate interpolation, was independently checked. Combining this established result with the line-gcd oracle proves polynomial scalar recovery for a designated cofactor with polynomially bounded numeric degree and sparsity. This use does not depend on the inaccessible October revision of the rational-interpolation paper.
- The original and revised ECCC2026/108 abstracts were distinguished. The October13 revision announces arbitrary-characteristic simultaneous rational interpolation, but its full revised PDF repeatedly returned a request-rejection page. The original June PDF was read and has a characteristic restriction. No theorem in the manuscript relies on the unread revised proof.
- Searches for `complete intersection colon ideal determinant change generators Wiebe theorem` and `Stacks projective complete intersection dualizing module Hom closed immersion canonical module colon ideal` located Coquand–Tête (2018), *An elementary proof of Wiebe's Theorem*, J.Algebra499,103–110, doi10.1016/j.jalgebra.2017.12.003. The entire statement and proof of Theorem11 in §2 were read from the publisher's indexed full text. It identifies both annihilator ideals for a determinant relating two regular sequences. Its possible algorithmic use for higher-codimension saturation is under proof checking.

## Bounded-excess saturation and finite slices, 22:00–22:25 UTC

Searches used both search engines, with general mathematical phrases rather than manuscript identifiers: complete intersection saturation Frobenius algorithm; annihilator random sparse polynomials ideal; geometric resolution lifting fibers finite fields; complete intersection annihilator algorithm sparse; ECCC saturation polynomial ideal; and Hexagon saturation Frobenius. Results were followed to publisher and author pages. No matching scalar-recovery theorem was established by these searches; this statement is not a priority or absence claim.

Giusti–Lecerf–Salvy's *A Gröbner Free Alternative for Polynomial System Solving* (Journal of Complexity17(1),154–211, DOI10.1006/jcom.2000.0571) was located on the authors' publication pages and primary author-hosted manuscript. Its geometric-resolution and lifting-fibre context is relevant, while the displayed summary assumes reduced regular sequences outside an inequation and concerns zero sets. The saturation algorithm here keeps the full nonreduced finite algebra and bounds the dimension of a graded colon kernel. A detailed formal-statement comparison remains a literature task; no uninspected theorem from this paper is used as a dependency.

Shoup's entire14-page author manuscript was read, including all Sections2–5 and references. The deterministic fixed-p claim used here follows from the complete Sections2–3; no GRH is required. The final comparison word in the optional Section5 proof has a source typo, visually confirmed and scoped in SHOUP_SOURCE_AUDIT.md. The source is cited, linked and hashed, not copied into the deliverable.

Coquand–Tête Theorem11 and Corollary12 were checked in primary publisher text. Their determinant-annihilator identity supplies the bounded-excess line; the finite-free projection and sampled-kernel argument are proved in full in the manuscript and independently reconstructed. The linear-system dimensions and all binary-degree dependencies are explicit. Recent coordinate-orbit and sparse-interpolation comparisons retain their characteristic restrictions; no characteristic-zero result is silently used at a fixed small prime.

## Deterministic fibre and linear-prefix refinements, 22:45–23:12 UTC

Queries to both search engines used: complete intersection linkage free specialization annihilator interpolation algorithm; sparse saturation complete intersection algorithm on arXiv; saturation complete intersection on Hexagon; annihilator interpolation on ECCC; and the titles of Giusti–Lecerf–Salvy and Hägele–Morais–Pardo–Sombra. Author pages and journal metadata were checked. The author PDFs were retrieved after web-open failures, hashed, and inspected at the exact locators in SOURCES.tsv. Their characteristic-zero reduced-system context is compared explicitly in the paper. These searches establish no absence or priority claim.

The deterministic centre subclass led to Saha–Saptharishi–Saxena (2013), final author PDF and ECCC TR11-021. Root read Definition1.1, Corollary3.3 with its proof, and all Section6; the research worker additionally read the complete Section3. The all-characteristic statement includes affine factors and formal numerical-degree bounds. The Galois-ring algorithm's arithmetic has polynomial bit complexity in the explicit finite-field representation and its polynomial p-adic precision. Applying it only to low-degree candidate rows is essential. Source metadata and the exact inspection scopes are in SOURCES.tsv and SATURATION_REFINEMENT_AUDIT.md.


## 2026-11-24, 23:46-23:47 UTC: bounded-degree Walsh multiplier

Queries used before integrating the transfer construction: “Walsh polynomial 3-adic support”; “ternary Walsh polynomial valuation”; “site:arxiv.org Boolean polynomial nonzero population divisibility three bounded degree”; “site:eccc.weizmann.ac.il OR MOD3 polynomial parity representation”; “site:hexagonmath.org Walsh valuation”; “polynomial support size mod 3 Kahn Meshulam”; “ternary Boolean cube divisibility polynomial”; “bounded degree Walsh 3-adic”. The first engine returned ternary bent-function/phase-sum literature and the author-hosted Green paper *Uniqueness of Optimal Mod 3 Polynomials for Parity*; the second returned mostly unrelated Boolean-cube and divisibility records. The exact fixed-weight-mask population-valuation assertion was not located in these results. This is a bounded search result, not a priority inference. No newly returned paper was relied on or quoted, and no proof from these hits was read. The already inspected Kahn--Meshulam comparison remains the paper's relevant finite-field uncertainty context. The all-parameter construction is proved directly by explicit local truth tables and triangular transfer matrices. Search results without opened primary proof are not recorded as authenticated theorem dependencies.


## 2026-11-25, 00:10–01:20 UTC: geometric constants, Cartier representations and linearized recognition

The saturation research contribution searched primary author pages, journals, arXiv, ECCC and Hexagon for multivariate Cartier operators, effective Christol bounds, finite-field automatic sequences, sparse composition and additive/linearized polynomial decomposition. Exact retained sources, hashes, locators and limits are in its SOURCES.tsv and the standalone comparisons cartier_and_constant_field_literature.md and linearized_block_literature.md. Root read both comparisons and the complete new recognition proofs. The Stacks Project geometric-integrality definitions and constant-field statements were also opened directly by root.

Giesbrecht (1998), Section6, Theorem6.1, authorpp22–24, already gives deterministic additive-polynomial decomposition polynomial in the Frobenius degree at fixed p, including p=2. This is explicitly credited in the manuscript. Its univariate additive input is specified; the theorem proved here recognizes an unknown additive polynomial and multivariate argument under an exponent gap. The comparison supplies context and makes no priority claim. Earlier skew-factorization proofs were not separately audited or used.

The Rowland–Yassawi, Bostan–Caruso–Christol–Dumas and Adamczewski–Bostan–Caruso comparisons distinguish an explicit reachable monomial graph from a minimal automaton or invariant linear space, and distinguish ordinary numerical-degree cost from sparse binary exponent cost. The exact Cartier-support example establishes only the explicit-support obstruction. Volkovich's multiquadratic theorem has an odd-characteristic hypothesis and is not used for characteristic two; bounded individual displayed degree also bounds ambient dimension in the anticanonical setting already treated. These routes therefore do not resolve the unrestricted saturation problem.


## 2026-11-25, 01:44–02:05 UTC: zero-sum additive relations

Before manuscript integration, root searched both engines with the exact queries: “sparse multivariate polynomial hidden additive composition Frobenius degree gap finite characteristic”; “linearized polynomial divided by x^p-x finite field composition”; “site:eccc.weizmann.ac.il sparse polynomial small characteristic saturation factor recognition”; “site:hexagonmath.org sparse polynomial Frobenius composition”; “sparse polynomial decomposition additive polynomial hidden inner multivariate positive characteristic”; “site:arxiv.org linearized polynomial composition x^p-x additive index”; and “site:hexagonmath.org polynomial saturation Frobenius linearized”. The hits concern classical additive composition, sparse factorization and interpolation, and sparse-coordinate equivalence. No priority inference is made.

Root opened Giesbrecht's primary author PDF directly and read the complete Section6, authorpp22–24, including the skew-polynomial correspondence, decomposition discussion and formal Theorem6.1. The PDF hash agrees exactly with the earlier source audit. The factor-through-T^p-T identity used here is a direct classical additive-polynomial calculation; the paper gives its explicit homogenized coefficients because that precise ideal-divisibility identity is needed. The new representation argument concerns unknown U,V, coefficient recovery, support growth and the smooth saturation family.

The forward search found von zur Gathen, Giesbrecht and Ziegler, “Counting invariant subspaces and decompositions of additive polynomials,” arXiv:1912.00212v2 (31December2019). Only the abstract and version history were inspected; the attempted HTML mathematical version was unavailable. Primary publisher metadata identifies the final publication as Journal of Symbolic Computation105 (2021),214–233, doi10.1016/j.jsc.2020.06.008. No formal theorem or proof from this work is used.

Demin and van der Hoeven, “Factoring sparse polynomials fast,” Journal of Complexity88 (2025), Article101934, doi10.1016/j.jco.2025.101934, was inspected through the primary author HTML version dated23February2025. Root read Section1.1 prose and the Section1.4 algorithmic overview. Its numerical-degree and input/output-support dependence and randomized setting do not supply the binary-exponent recognizer here. Formula images and the full factoring proofs were not audited, and no algorithm is imported from this comparison. The exact HTML hash and inspection scope are in SOURCES.tsv.

The primary ECCC TR14-056 page records the20May2014 withdrawal after an error in Claim4.12 and a positive-characteristic counterexample. That withdrawal notice was read directly. No result from the withdrawn report is invoked. All external source copies remain outside the deliverable and every archive.

At the close of this source search the zero-sum independent reconstruction was still in progress. Its subsequent completion and source comparisons are separate check events, not retrospectively part of this literature inspection.


# Literature and exact reading coverage

Date: 2026-11-24. This record identifies material actually read, not an assertion of independent verification of every classical theorem or an exhaustive novelty search. Source PDFs and attached files remain outside the returned deliverable; only this metadata and the new synthesis are included.

## SGA2

The attached complete English reader is source/latex_sources/SGA2_EN/02_SGA2_EN_COMPLETE_READER.tex, SHA256 dd4c7483c1ed9cfbde1a614452cbbf6473fc09e9b530b22eaad1d1a01fb0a774. This worker read the entire assigned Exposés X–XII, source lines6376–8275. Reading was staged: XII all lines7452–8274; XI §§2–3 lines7165–7451; then the missing X and XI§1 in contiguous blocks6376–6600,6601–6870,6871–7164. Earlier selected readings were subsumed by this final complete range. Root and other workers own the remaining exposés; this worker does not claim to have read the entire book alone.

Exposé X: formal étale coverings and nilpotent invariance; Lef and effective Lef conditions; Examples2.1 and2.2; comparison and connectedness/fundamental-group consequences2.3–2.6; purity definitions and descent; regular local purity in dimension≥2; local-complete-intersection purity in dimension≥3; all lemmas and proofs through3.10.

Exposé XI: nilpotent unit extensions and Picard obstruction/cohomology sequence; formal comparison; every argument in §§2–3, including the local parafactoriality criterion and complete-intersection dimension threshold, with all examples and remarks through3.18. Exposé XII: the whole projective comparison and Picard development, including its algebraization and Lefschetz dependencies and all results beyond the particular corollary used here.

The paper uses Corollary XII3.7 only in its precise global-complete-intersection form: over a field, a global complete intersection in projective space of dimension≥3 has Picard group freely generated by O(1). The French Laszlo edition was checked directly at printedp121/PDFp129, covering XII3.6–3.8 and the induction using H1,H2 vanishing. The corresponding old pagination is nearp153. It is not a surface statement. The source's inverse-limit notation in XII3.6 was checked, not silently changed. The English reader's editorial notes are distinguished from the published mathematical statements.

French source: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-98.pdf ; SHA256 41ad02c57321a8d2200ff32a929bc93adbc3de0d59dcd5a284d28d859fb87a90. Bibliography sp-sga2 records the editions.

## Presentation and counting sources

* Grenet–Koiran–Portier, arXiv1210.1451v1: full Lemma1 and Theorems5–6 with their construction/proofs. The ground-field variant is Theorem6 in this version; Theorem5 allows an extension. Journal of Complexity29(2),142–157(2013), doi10.1016/j.jco.2012.10.001. This is a comparison source for feasibility and arithmetic-circuit conversion; the paper's full scheme-isomorphism charts are proved separately.
* Gopalan–Guruswami–Lipton, author manuscript2006 §§3.1 and3.3, printedp5–8; extraction was checked against renderedp5,p6,p8. Algorithmica50(4),479–496(2008), doi10.1007/s00453-007-9097-3. The finite-field zero-indicator methods are relevant; no scheme-preserving statement is imported from them.
* Kudo, arXiv1704.08110v1, full Proposition4.2.1 proof and AlgorithmII, local TeX lines1370–1565. Journal of Symbolic Computation109,441–464(2022), doi10.1016/j.jsc.2020.07.015. The relevant Hasse–Witt coefficient formula is stated with its complete-intersection hypotheses and checked against the paper's Koszul basis.
* Valiant, Theoretical Computer Science8(2),189–201(1979), doi10.1016/0304-3975(79)90044-6: Lemmas3.1–3.2 on printedp193 and the proof opening were read. The full graph-gadget construction is used as published background, not claimed to have been independently reconstructed. The exact identity per(M)=4^t S and integer entries are essential at odd primes.
* Zak, Mathematical Annalen313,507–545(1999), doi10.1007/s002080050271: Proposition1.3(a), Theorem3.3, Example6.6, definitions and surrounding proofs/characteristic qualifications read in the author-uploaded article. The paper uses its own contraction argument for the needed arbitrary-characteristic secant assertion, not an unqualified characteristic-zero Terracini equality.
* Stacks Project Tags0E8R and0EKB: full Lemmas33.23.1–2 and graded Nakayama Lemma10.56.1(4), respectively. Used for the length-two embedding criterion and homogeneous minimal generators.

## New support and effective-compression comparisons

* Kaski–Koivisto–Nederlof, IPEC2012/LNCS7535,147–158, doi10.1007/978-3-642-33293-7_15; arXiv1203.4063v1: introduction through the beginning of§4, printedp1–7, including the rank-dependent dynamic-programming discussion before Theorem2. This is a conceptual precedent for coefficient/rank algorithms. Our weighted finite-additive-group recurrence is proved directly and does not use a characteristic-p Fourier transform.
* Cheng–Rojas–Wan, Journal of Complexity73,101681(2022), doi10.1016/j.jco.2022.101681; author PDF https://www.math.uci.edu/~dwan/computzeta.pdf : Theorem3.2 and full proof, local text lines300–445/author printedp7–9. Conditions q>rD^(r−1), equal positive degrees, radical equality, r output equations and the dense-degree complexity are all retained. This does not provide polynomial sparse-bit scheme compression over an arbitrary small input field.
* Dubé, SIAM Journal on Computing19(4),750–773(1990), doi10.1137/0219053: Theorem8.2 and Corollary8.3 printedp773 and relevant degree conventions read in the full downloaded article. The manuscript deliberately uses a looser exponent than the homogeneous theorem. It is an explicit finite elimination bound, not a polynomial-size claim.

## Saturation and factorization research, including recent versions

* Chuyoon–Shpilka, On Factorization of Sparse Polynomials of Bounded Individual Degree, CCC2026, doi10.4230/LIPIcs.CCC.2026.20; arXiv2603.07589/ECCC2026/036. Abstract and §§1.1–1.2 through Theorem14 read in the publisher HTML, including the field/bit-cost convention, arbitrary-characteristic variants and the distinct hypotheses for products of sparse factors. Fixed individual degree of the input multiples cannot alone settle the growing-dimensional smooth anticanonical problem: sp:lem:coordinate-degree forces dimension to be bounded in that case.
* Chuyoon–Shpilka, Factoring Products of Sparse Irreducibles of Bounded Individual Degree via Rational Interpolation, ECCC2026/108. OriginalJune28 metadata imposes characteristic0/sufficiently large characteristic. Revision1 ofOctober13 reports removal of that restriction. The opening revised statements were read before access became intermittent; the complete revised theorem/oracle/extension details were not verified. A public Request Rejected response later prevented direct PDF download. No proved conclusion in the paper depends on that unread revision: the exact geometric ratio oracle is proved directly, and the polynomial recovery conclusions use ordinary interpolation instead.
* Bhattacharjee–Kothary–Rai–Saraf, Deterministic Algorithms for Low Individual Degree Factors of Sparse Polynomials, arXiv2606.27293v1/ECCC2026/105, June25. Abstract and full introduction/formal Theorems1.1,1.6,1.7 and Remarks1.2–1.10 read. Theorem1.1 has characteristic0 or>individualdegree; Theorem1.7 permits arbitrary fields. Its output contains all nonmonomial bounded-individual-degree factors and may contain spurious entries. Remark1.9 bounds the explicit polynomial supports. The full Section5 and exact field dependencies were subsequently read and checked; their complete scope and the Remark5.2 discrepancy are recorded below. Download SHA256 c1d110f3ecd975de39681aa7ad13ba80638da4cdaaa6c97473d6ead9458f0aad.
* Nahshon–Shpilka, A new bound on cofactors of sparse polynomials, Forum of Mathematics,Sigma14,e52(2026), doi10.1017/fms.2026.10202: abstract, introduction and Theorem1.4/Corollaries1.6–1.7, printedp1–4, read. These are univariate coefficient-norm bounds over C/Z with nonzero constant term. They neither bound multivariate factor sparsity over fixed finite fields nor directly close the saturation problem. No characteristic transfer is asserted.
* Volkovich, Deterministically Factoring Sparse Polynomials into Multilinear Factors and Sums of Univariate Polynomials, APPROX/RANDOM2015, LIPIcs40,943–958, doi10.4230/LIPIcs.APPROX-RANDOM.2015.943: primary abstract/metadata located. The exact applicable algorithm hypotheses remain to be read before use. The elementary Newton-polytope observation that a multilinear divisor has at most as many monomials as its multiple is separately under consideration.

## Search scope and remaining gates

Searches used combinations of sparse projective equations, Hasse–Witt coefficient complexity, monomial support, finite-field counts with linear constraints, near-minimal support, permanent padding, sparse polynomial multiples, individual-degree factors, rational interpolation and coordinate-equivalence sparsification. Primary results were preferred. The general affine-orbit hardness problem is distinct from the smooth anticanonical subclass. The exact arXiv version and characteristic qualifications were subsequently checked, as recorded below.

No search was treated as proof of novelty. The contribution statements are proved mathematical refinements with named external ingredients. Unrestricted saturation, general fixed-c saturation-only lists, the intermediate support-excess range, and polynomial-size image equations over the original small field retain explicit gates.

## Reading completed after the initial literature register

Chuyoon–Shpilka arXiv2603.07589v1 Section3, the complete field setup, Definition3.1 and Theorem3.2 with proof, HTML lines561–602, were read directly. The integer prime used to separate exponent weights is distinct from the field characteristic. The field may be enlarged, the size requirement is polynomial in variables, sparsity and numerical individual degree, and no characteristic lower bound occurs. This is the exact ordinary sparse-interpolation ingredient for the designated-cofactor theorem, separate from the inaccessible rational-interpolation revision.

Bhattacharjee–Kothary–Rai–Saraf arXiv2606.27293v1: the full Section5 proof and Algorithms3–4, printedpp39–46, were read, along with Section2 field/bit conventions, Theorems2.13,2.30,2.34 and their relevant surrounding discussion. The stated arbitrary-field candidate theorem gives explicit sparse polynomial lists, not merely evaluation circuits. Remark5.2's parenthetical p>d was compared with the formal arbitrary-field Theorem1.7 and the actual proof dependencies; the separately stated deterministic finite-field univariate algorithm has no such characteristic restriction. The new simultaneous pruning avoids their characteristic-restricted divisibility tests entirely.

Kaltofen–Trager(1990), Journal of Symbolic Computation9(3),301–320, doi10.1016/S0747-7171(08)80015-6: introduction and the entire gcd-evaluation discussion in Section3, printedpp310–311, read. Their general randomized projection argument explicitly warns that specialization can introduce extra gcd factors. The new saturation proof uses the unit-ideal identity to prevent this on every affine line. Their characteristic-zero factorization theorem is not used as a fixed-field algorithm. Primary author PDF https://kaltofen.math.ncsu.edu/bibliography/90/KaTr90.pdf , SHA256118f646ad35440379b3b4dce5c440e3ed848ca30f116987aad356082c4de5f1e.

The constant-total-degree sparse factor algorithms discussed by Kumar–Ramanathan–Saptharishi and Dutta–Sinhababu–Thierauf were checked through the BKRS source comparison and primary metadata: they supply quasipolynomial bounds with their own field restrictions, not the proposed polynomial shortcut. The line-gcd proof does not rely on these algorithms. The October ECCC2026/108 revision remains only partially read, but no current proved conclusion depends on it.

Klivans–Spielman(2001), Randomness efficient identity testing of multivariate polynomials, STOC2001,216–223, doi10.1145/380752.380801: the primary author PDF's complete Section6.3/Theorem11 and the adjoining Section6.2 statement were read using OCR of PDF pages12–13 (printed11–12); Section6.4 was also read. Primary author PDF https://www.cs.yale.edu/homes/spielman/PAPERS/ran3.pdf , SHA2563c1f05f392cd55ea3e510fc265782e8d3ebb1eebe6f69db7048877a042f99326. Its informal exponent-recovery description uses scaling by2; that description alone is insufficient in characteristic2. The explicit proof in sp:lem:sparse-interpolation uses an independent scaling variable, as in the fully read CS26 Section3, and works in every characteristic. This is source-informed reproduction of a classical algorithm, not an independently discovered new theorem. The weight family, maximum-term-count selection and exact bit-field bounds are proved in the manuscript.

Baraskar–Dewan–Saha–Sinha(2024), NP-hardness of testing equivalence to sparse polynomials and to constant-support polynomials, arXiv2410.12251v1, doi10.48550/arXiv.2410.12251: abstract and introduction through Section1.3 Theorems1–3 and their definitions/remarks were read, including HTML lines243–409. Theorem1(2) proves hardness for homogeneous sparse input over every field; Theorem2(2) gives the stated s^(1/3−epsilon) approximation hardness for0<epsilon<1/3. Crucially, Theorem3's support threshold sigma≥5 also requires characteristic0 or>sigma+1, although that qualification is absent from the abstract. No assertion of smoothness or anticanonical degree appears in these theorem hypotheses. These are comparison results, not a solution of the restricted coordinate-sparsification question in the manuscript. This arXiv version strengthens the earlier ECCC support threshold6 to5; it does not remove the characteristic restriction.

Bhargava–Sengupta, Polynomial Identity Testing and Lower Bounds for Sparse Affine Orbits, ECCC TR26-283, submitted October27 and published October28,2026: fresh system1 searches with a90-day recency bound verified metadata on November24. The direct ECCC page/PDF initially returned RequestRejected/503, but following the author's public publications link and then the ECCC download link returned the complete22-page PDF through the research tool. Exact formal statements in Section1.1 (Theorems1.2,1.5; Lemma1.6; Remark1.7), proof overview Section1.2, the complete Section3 proofs, all of Section4, and all of Section5 through Remark5.4 were read. Primary URL https://eccc.weizmann.ac.il/report/2026/283/download/ . The opening convention is characteristic zero unless otherwise stated. Theorems1.2 and1.5 retain that convention; only the structural Hasse-derivative Lemma1.6 explicitly permits arbitrary characteristic. Remark1.7 identifies positive-characteristic bounded-derivative PIT as the remaining external ingredient. The lower-bound examples are powers of a cubic singular along a rational normal curve, and their quadratic-power derivative ranks use characteristic-zero results. No transfer of those bounds to fixed p is made.

Application to the current smooth family was also examined directly: away from the cone vertex, a smooth homogeneous hypersurface equation has shifted initial form of degree0 or1, hence Hasse-derivative dimension≤2. Thus the initial-form lower-bound route does not by itself yield a growing coordinate-sparsity bound for these equations, independently of the characteristic issue. This elementary limitation is proved in the manuscript's literature comparison; it is a targeted source-informed deduction, not a claim that all possible uses of the cited paper are excluded.


# Structured counts: literature searches and source audit

All searches and downloads below were performed on 24 November 2026 (UTC). Primary mathematical papers are the authorities used in the text. Searches were comparisons and attribution checks; failure to find a matching result is not evidence of novelty. No priority claim is made for the new combinations or specializations. Downloaded papers and their text extractions remain outside the deliverable; only citations, locators, URLs, byte counts, and hashes are returned.

## Search record

1. **Engine 1, affine inequations and sparse character counting.** Query families: affine linear inequations encoding OR over finite fields; Kahn–Meshulam finite-field uncertainty; Barbanchon parsimonious three-colourings; Hexagon Walsh/branching-program work. Located Kahn and Meshulam's author PDF, Barbanchon's journal/author records, and the relevant zero-sum and covering literature. The Hexagon query did not identify a directly relevant primary theorem. These families summarize the initial queries; no claim is made that their wording is a verbatim transcript.

2. **Engine 2, algorithms and full-support codes.** Query families: Björklund–Kaski fine-grained Tutte polynomial PDF; Kiefer forward-space weighted automata; sparse affine Walsh empty fibres; Barbanchon palette normalization. Located the primary arXiv versions of Kiefer and Björklund–Kaski. Read Kiefer's Algorithms 1–2 and Proposition 2.1, pp. 3–4, and Proposition 3.2, p. 5. Read Björklund–Kaski §1.3, Theorem 5 and Lemma 6, pp. 3–4. The latter explicitly states the Crapo–Rota critical theorem and the relation between base-field tuples and extension-field full support.

3. **Engine 1, exact comparison locators.** Query families: Barbanchon Proposition 5 and reference-palette pinning; Schaefer positive one-in-three satisfiability; ECCC Walsh branching programs. The old Barbanchon PostScript link failed, but the author's current PDF succeeded. Its Proposition 5 is on author-preprint p. 4, corresponding to journal p. 458; Definition 16 on preprint p. 6, journal p. 460, explicitly counts colourings modulo the trivial colour symmetries. Section 5 tracks reference palettes. Pinning two adjacent distinguished vertices to distinct named colours selects exactly one representative of each six-element orbit.

4. **Engine 2, arrangement zeta functions.** Queries concerned Athanasiadis (1996), Björner–Ekedahl (1997), and Schaefer's 1978 paper. Located Björner–Ekedahl's original arXiv PDF. Proposition 3.2, p. 5, supplies the finite-field count; Theorem 3.6(i), p. 7, gives the arrangement-complement zeta product. This is prior literature, not a new result of the paper. Schaefer's downloaded scan explicitly defines the positive one-in-three relation on p. 216, lists problem NP1 on p. 217, and applies Theorem 2.1 to it on p. 218. The accompanying reduction in the paper only needs decision NP-completeness.

5. **Engine 1, affine-hidden split coordinate recovery.** Queries concerned simultaneous diagonalization of quadratic forms over finite fields, rank-one matrix-span reconstruction, affine equivalence of Boolean cubes, and ECCC simultaneous diagonalization. Located He–Kressner, arXiv:2402.16557v3, and broader matrix/block-diagonalization and polynomial-reconstruction literature. He–Kressner §3, Algorithm 1, p. 7, and Theorem 7, p. 8, explain recovery from two random linear combinations over the reals. The paper credits this standard matrix-pencil mechanism, proves its finite-field specialization directly, and adds a deterministic bounded-degree coefficient curve using the full diagonal-span promise. No generic affine-equivalence or polynomial-identity-testing result is assumed.

6. **Engine 2, simultaneous-diagonalization publication metadata.** Queries concerned He–Kressner author/version data and Fang–Huang–Huang simultaneous block diagonalization. The He–Kressner cached file is v3, dated 28 April 2025, manuscript date 30 April 2025; this is the version cited and read. A 2026 journal record also appeared but is not substituted for the checked version. Fang–Huang–Huang, arXiv:2503.01166 and *Linear Algebra and its Applications* 737 (2026), 193–212, DOI 10.1016/j.laa.2026.02.016, is broader related literature and is not used as a theorem dependency.

7. **Engine 2, exact DOI/page verification.** Verbatim queries: `"Covering the cube by affine hyperplanes" "10.1006"`; `"A combinatorial problem on finite Abelian groups, I" "8" Olson`; `"Subspace arrangements over finite fields" "10.1006"`. Publisher primary records confirmed Alon–Furedi DOI 10.1006/eujc.1993.1011, volume 14(2), pp. 79–83; Olson DOI 10.1016/0022-314X(69)90021-3, volume 1(1), pp. 8–10; Björner–Ekedahl DOI 10.1006/aima.1997.1647, volume 129(2), pp. 159–187. The correct final word in the latter title is “Aspects”.

8. **Engine 1, final scope comparison.** Verbatim queries: `"sparse Walsh" "empty" fibres rank`; `"finite field" "simultaneous diagonalization" quadratic forms deterministic algorithm`. The first returned no directly matching theorem. The second located Christiaan van de Woestijne's author ISSAC 2005 manuscript, *Deterministic Equation Solving over Finite Fields*, DOI 10.1145/1073884.1073932, and his Leiden thesis. These concern deterministic solution of diagonal equations and ordinary quadratic forms; they do not by themselves provide the marked full-span coordinate-recovery theorem used here. They are background comparison only and were not copied or imported as a proof dependency.

## Primary-source locators and the comparisons they support

| Source | Exact location used | Role |
|---|---|---|
| Kiefer (2020), arXiv:2009.01217v1 | Algorithms 1–2, p. 3; Proposition 2.1, p. 4; Proposition 3.2, p. 5 | Forward reachable span and weighted-automaton equivalence background. |
| Kahn & Meshulam (1991) | Theorem 1, p. 17; Theorem 2, pp. 19–20; circuit discussion pp. 20–21; added-in-proof credit p. 21 | Finite-field uncertainty and mod-p parity representation context. |
| Schaefer (1978) | Positive relation p. 216; NP1 p. 217; application of Theorem 2.1 p. 218 | NP-completeness of positive one-in-three satisfiability. |
| Alon & Furedi (1993) | Main punctured-cube theorem, pp. 79–83; publisher abstract checked | A cover of all cube vertices except one needs at least its dimension many hyperplanes. |
| Bishnoi, Clark, Potukuchi, & Schmitt (2018) | Theorem 6.1(c), p. 324 | General finite-grid punctured-cover formulation, over fields. |
| van Emde Boas (1969) | Theorem 2.1, printed p. 18 (PDF page 20) | Records independent Kruyswijk and Olson proofs of the abelian p-group Davenport constant. |
| Olson (1969) | Publisher record, pp. 8–10 | Original paper and exact bibliographical attribution; the paper's needed elementary-abelian bound is also proved directly. |
| Barbanchon (2004) | Proposition 5 journal p. 458 / author preprint p. 4; Definition 16 journal p. 460 / preprint p. 6; §5 reference palettes | Earlier parsimonious SAT-to-three-colouring mechanism, with the colour-symmetry convention made explicit. |
| Athanasiadis (1996) | Article pp. 193–233; primary metadata | Finite-field method for characteristic polynomials; the formula is re-derived in full in the paper. |
| Björner & Ekedahl (1997) | Proposition 3.2 and Theorem 3.6(i), preprint pp. 5, 7 | Arrangement extension counts and zeta product; explicitly prior results. |
| Björklund & Kaski (2020) | §1.3, Theorem 5 and Lemma 6, pp. 3–4 | Crapo–Rota critical theorem, full-support codewords, and extension-field interpretation. |
| He & Kressner (2025) | v3, §3, Algorithm 1 p. 7, Theorem 7 p. 8 | Simultaneous diagonalization using two matrix combinations. |

## Download manifest

The hashes below identify the retrieved bytes. The files themselves are excluded from all returned ZIPs. Unversioned arXiv PDF URLs resolved to the versions identified above on this date.

| Local audit basename | Bytes | SHA-256 | Retrieval URL |
|---|---:|---|---|
| `kahn_meshulam.pdf` | 234474 | `f157b146e4eb944e23169f337139fe5e5fe3fd4454635bc1fad594a857a25597` | https://meshulam.net.technion.ac.il/files/2021/05/modp1.pdf |
| `bcps.pdf` | 236007 | `b9ff1181d56aa6113de1f2242ca3ec16eed8ab092c0ef7fa93c16789388d9716` | https://community.middlebury.edu/~jschmitt/papers/on_zeros_of_a_polynomial_in_a_finite_grid.pdf |
| `van_emde_boas.pdf` | 3254717 | `c2710d7632716bc617c2e1d4fff359129d08c3a1819b281f97a564dcf2abf330` | https://ir.cwi.nl/pub/7240/7240D.pdf |
| `kiefer.pdf` | 166295 | `db509226fae7243e165f856a30d0b1217e5c16b74c3cbcbb98239c660925cf07` | https://arxiv.org/pdf/2009.01217 |
| `bjorklund_kaski.pdf` | 408577 | `0de06472e5a6861b049f0ab82a2d49398575942e0aff732afff3d992201aeef6` | https://arxiv.org/pdf/2003.03595 |
| `barbanchon.pdf` | 425857 | `23ac19dac9d353d7b7bc7914f0ce9352a9ca46c28810b80a10783910ae68f150` | https://www.dil.univ-mrs.fr/~regis/papers/report-and-article.greyc-2003-and-tcs-2004.on-unique-3-colorability-and-linear-parsimonious-reductions-in-the-plane.pdf |
| `he_kressner.pdf` | 891623 | `ca8f8a57869d7b42ed86f92ec7880bd7baf10f3bc5f4a877a2f261817577535c` | https://arxiv.org/pdf/2402.16557 |
| `bjorner_ekedahl.pdf` | 302965 | `5acf58b91267c4f06839c3d7403aaec86d9224f61bcbad485e2ca8d036abbbb7` | https://arxiv.org/pdf/math/9612217 |
| `schaefer.pdf` | 1100724 | `19b30ef36869a7fa777a7d51d19ab1811a957f7479a423073a052b40f1319ef6` | https://www.khoury.northeastern.edu/home/lieber/courses/csg260/f06/materials/papers/max-sat/p216-schaefer.pdf |

The bibliography entries used by the paper are in `workbench/papers/counting/refs_structured.tex`. Publisher metadata pages that were retrieved through search, without a downloaded byte artifact, have no invented file hash. The claims attributed to them are limited to their bibliographical data and the explicitly stated abstract-level scope; the mathematical claims used in the argument have self-contained proofs or the separately downloaded primary sources listed here.


# Literature searches and inspection record

All entries are dated **2026-11-24**. This records this worker's search families, results and scope. A topic description below is not presented as a verbatim reconstruction of a lost query string. Exact query strings retained in the session are quoted in the screening entry. URL, byte hash, exact theorem/page locators and source-exposure scope are in `SOURCES.tsv`; bibliography metadata is in `refs_fixed.tex`. Other workers maintain their own records. No external paper or unchanged attached source is included in this contribution's returned files.

| Search or lookup | Result and action | Scope of use |
|---|---|---|
| Milovanov sparse polynomial roots, general fixed characteristic, journal versus preprint | Located the 2019 Information Processing Letters article, DOI 10.1016/j.ipl.2018.09.008; inspected the supplied complete three-page journal version. | General fixed-prime theorem is taken from the journal version, rather than inferring its scope from the older binary preprint. |
| Cao et al., fixed-output sparse gcd, v2 | Used supplied source for arXiv:2606.12144v2; inspected Lemma 7, Proposition 9 and equations (7)–(8). Direct web discovery was incomplete. | Records distinguish fixed coefficient field from roots over the algebraic closure. Search failure is not evidence that the supplied paper does not exist. |
| Pries–Zhu genus and p-rank of Artin–Schreier curves | Verified journal metadata and Lemma 2.6, p. 712, DOI 10.5802/aif.2692; read the relevant attached source proof. | Standard ramification/genus and Deuring–Shafarevich statements are imported, with the simple-pole application rederived. |
| Sign-only Deligne/Alpöge preprint on Hexagon | Located version 2611.00789v1 and matched supplied source; inspected Theorem 1(b), Proposition 4 and Section 8. | Purity theorem is background. The paper's explicit dimension-one application is checked; no efficient counting theorem is attributed to the preprint. A direct byte download received HTTP 403, so the local supplied source is the hashed evidence. |
| Asok–Dubouloz–Østvær geometric models for suspensions | Verified IMRN 2023 publication, DOI rnad094, and downloaded arXiv:2112.08241. Read Theorem 3.1.1 proof, Remark 3.1.3, Construction 4.2.1 and the cited purity statement. | Coherent use of the theorem's section/center/complement hypotheses; foundational purity remains imported. |
| Riou lambda operations and A1 representability | Downloaded author's operations.pdf and checked Theorem 2.3.1, Proposition 2.3.2, pp. 10–11, with Theorem 1.1.2 context. | Naturality of lambda operations under the motivic identifications; not a new representability theorem. |
| MVW motives, projective line, higher Chow comparison | An initial guessed IAS download was inaccessible; a Rutgers author-hosted copy was found and verified. Read Example 13.17, Theorem 15.2, Corollary 15.5 and Theorem 19.1. | Perfect-field hypotheses are retained; foundational motivic cohomology theorems are background. |
| Point-counting complexity: von zur Gathen–Karpinski–Shparlinski, Lauder–Wan, Harvey | Retrieved author/preprint PDFs and verified journal/book metadata. Read Gathen et al. Theorem 4.7 in Section 4, Lauder–Wan Theorem 1, Harvey Theorems 1.1–1.3 and uniformity remarks. | Sparse input, random reduction, characteristic, degree, dimension and fixed-scheme constants are kept distinct. The scanned Lauder–Wan page was rendered; the arXiv copy provided clean text. |
| Scheme and tensor universality | Retrieved Lee–Vakil arXiv:1202.3934, reading Definition 1.2 and Theorem 1.3. Checked Grochow–Qiao 2023 journal Theorems A/B and Corollary A, including the cubic-form characteristic restrictions; retained arXiv bytes separately. | Scheme singularity universality and orbit-isomorphism reductions are not silently transferred to parsimonious point counts or Frobenius multiplicities. A failed direct journal byte download did not prevent primary journal web inspection. |
| Forward context: polynomial-count varieties and misleading realizations | Discovered Katz–Rodriguez Villegas arXiv:2603.07062v1 and read all six pages. | Example 2.3 and Section 3 provide precise comparisons: polynomial counts need not imply affine space or eliminate all virtual cancellation. |
| Total Betti numbers of hypersurfaces and the Weil bounds | Verified Huybrechts's 2023 Cambridge book and author edition, Corollary 1.12, p. 18, and positive-characteristic Section 1.6. Retrieved Deligne's original Weil I from NUMDAM, inspecting Theorem 1.6, p. 276. | Formula rederived by Chern/Euler calculation; coefficient-counting and information bounds are current deductions. Full Weil theorem is imported. |
| SGA4 base change, trace and Kunneth | Inspected French text-edition XVII 5.2.6, 5.2.8, 5.4.3 and XVIII 2.8.1, 2.9; hashed downloaded HTML. | Used to prove the actual Rpi_! decomposition. The edition is identified; no original-scan page cote is invented. |
| Katz's congruence formula in SGA7 II | Found author-hosted congzeta.pdf, inspected Exposé XXII Section 2 and Theorem 3.1/Corollary 3.2 on p. 410. Verified Springer chapter metadata, pp. 401–438. | Proper-scheme coherent zeta congruence is imported. The F4 legacy specialization also has an elementary coefficient-sum parity proof in the paper. |

## Targeted broad screening

The following actual query strings were retained:

- `site.eccc.weizmann.ac.il counting points finite fields sparse polynomial #P smooth varieties`
- `site.eccc.weizmann.ac.il tensor isomorphism Grochow Qiao 2023`
- `site.hexagonmath.org Frobenius counting smooth hypersurface complexity`
- `site.eccc.weizmann.ac.il "counting" "sparse" "finite" "roots"`
- `site.hexagonmath.org "coherent" "Frobenius" "counting"`
- `Katz "Une formule de congruence" 400 437`
- `Katz "Une formule de congruence" 401 438`

The ECCC screening surfaced adjacent topics including sparse root bounds, univariate local zeta algorithms and exact-power questions; it did not supply a directly matching replacement for the rank-one smooth-projective construction. The Hexagon screening matched the sign-only preprint. Forward searches around tensor isomorphism also found later classical-group-action and commutative-ring papers; no unchecked theorem from those was imported. This was targeted screening, not an exhaustive priority search. The paper makes no priority claim from a search's failure to find a match.

The parent separately owns the later Wan–Zhang and DiPippo–Howe searches and their bibliography keys. Their verification should be credited to the parent's records, not to this worker.


# Primary literature and hypothesis checks

Source copies and PDF-to-text extractions are intentionally outside deliverable. The metadata-only source_manifest.json lists the exact downloaded bytes, SHA-256 hashes, and temporary scratch locators.

## Saha--Saptharishi--Saxena: positive result used in the paper

Saha, C., Saptharishi, R., & Saxena, N. (2013). A case of depth-3 identity testing, sparse factorization and duality. *Computational Complexity, 22*(1), 39-69. https://doi.org/10.1007/s00037-012-0054-4

Primary author PDF: https://www.cse.iitk.ac.in/users/nitin/papers/sparseFact.pdf

Checked Definition 1.1 (author p.4), Corollary 3.3 and its proof (p.11), and the complete Section 6 (pp.22-26). Affine linear factors are explicitly allowed. Corollary 3.3 bounds each product gate's numerical formal degree. Theorems 6.3/6.5 use polynomial p-adic precision and module pruning to cover every characteristic and finite extensions. For an explicit degree-h finite field, the Galois-ring elements and operations have polynomial bit size/cost. The application only supplies degree O(N) circuits, never the unrestricted high-degree rows. Full mapping and bit argument are in linear_prefix_deterministic.md. This source closes the linear-prefix centre-selection step.

The earlier ECCC version https://eccc.weizmann.ac.il/report/2011/021/ numbers the corresponding results Corollary 3.2 and Theorems A.1/A.3. The final source numbering is used in the manuscript. Web source refs: turn516580645view0 and turn630571585view0.

## Guo: general centre families do not give our polynomial bound

Guo, Z. (2024). Variety evasive subspace families. *Computational Complexity*. https://doi.org/10.1007/s00037-024-00256-1

Primary author PDF: https://zeyuguo.bitbucket.io/papers/chow.pdf

Checked the main construction and lower-bound statements (author Theorems 1.6/1.7), the Noether-normalization application, and the dimension-counting lower-bound argument in Section 4. For a centre of projective dimension c-1, the parameter n-k in this source equals N-c+1, which grows with the ambient dimension. General universal families therefore do not have the required polynomial bound when the complete-intersection degree grows. The lower bound concerns all degree-bounded varieties, not our sparsely presented subclass or input-dependent algorithms. Web source refs: turn389798774view0, turn757411161view2, turn757411161view3.

## Andrews--Garg: recent improved universal construction has the same mismatch

Andrews, R., & Garg, A. (2026). An improved construction of variety-evasive subspace families. In *Approximation, Randomization, and Combinatorial Optimization. Algorithms and Techniques (APPROX/RANDOM 2026)*, LIPIcs, 392, Article 56. https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.56

Primary proceedings page: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.56

Checked Theorems 1.4/1.5 and the Noether-normalization corollary. The simple explicit construction has size at most (nd+1)^(n-k); the improved construction remains exponential in n-k. At k=c-1 and fixed c this is not polynomial in our sparse input parameters, even though d is only polynomial in N. The theorem is valid in positive characteristic; its failure to close our gate is quantitative, not a characteristic-zero restriction. Web source refs: turn389798774view1 and turn757411161view5.

## Faithful-map lead retained as a failed reduction

Beecken, M., Mittmann, J., & Saxena, N. (2013). Algebraic independence and blackbox identity testing. *Information and Computation, 222*, 2-19. https://doi.org/10.1016/j.ic.2012.10.004

Primary author PDF: https://www.cse.iitk.ac.in/users/nitin/papers/alg-indep-InC.pdf

The faithful-map formal statements were inspected as a possible variable-reduction route, but no theorem is invoked in the manuscript from this lead. Preserving transcendence degree does not guarantee the no-common-projective-zero condition needed for a centre; an explicit two-equation counterexample is recorded in LEDGER.md. The finite-characteristic refinement by Chatterjee and Saptharishi (FSTTCS 2019, Article 11; https://doi.org/10.4230/LIPIcs.FSTTCS.2019.11) was likewise inspected only as a lead, not used as a claimed solution.

## Existing manuscript dependencies

The new residual-freeness proof uses the already audited Coquand--Tete form of Wiebe's identities. The new deterministic profile construction reuses the already audited fixed-characteristic Shoup irreducible-polynomial construction. Their bibliographic entries were not altered. Root separately audited and added the Giusti--Lecerf--Salvy and Hagele--Morais--Pardo--Sombra historical comparisons; their exact characteristic-zero/reduced-algebra hypotheses are preserved in the source paragraph supplied by root.


## Additional audit: Cartier states, constants, and sparse factor extraction (2026-11-25)

The full primary-source comparison is [cartier_and_constant_field_literature.md](contributions/saturation_residual/cartier_and_constant_field_literature.md). It records the precise characteristic and input-size hypotheses, the formal locators read, and the limits of each proof audit for Rowland--Yassawi (2015), Bostan--Caruso--Christol--Dumas (2019), Adamczewski--Bostan--Caruso (2023), Rowland--Stipulanti--Yassawi (2025), the Stacks Project, Giesbrecht--Roche, and Grenet. Numerical-degree and Newton-lattice bounds are distinguished from sparse binary-degree complexity; polynomial states, individual monomial states, invariant-space dimensions, and minimal automata are distinguished.

The source register is [SOURCES.tsv](workbench/SOURCES.tsv), with canonical columns source_id, kind, url, local_read_path, sha256, locators_used, and inspection_scope. Every local_read_path is marked external/not redistributed. Downloaded third-party PDFs and text extractions remain outside the deliverable. The new constant-field theorem is proved directly; the cited literature supplies context and identifies exactly which existing factorization or Cartier bounds do not settle the remaining gate. No priority inference is made from the search.

The generalized unsupplied-coefficient theorem has an additional focused comparison in [linearized_block_literature.md](contributions/saturation_residual/linearized_block_literature.md). Giesbrecht (1998), Section 6 and Theorem 6.1, is the exact classical additive-decomposition locator. Its fixed-characteristic complexity is already polynomial in the logarithm of ordinary degree; the distinction is the known univariate additive input versus the hidden multivariate U, monomial V, and coefficient vector in the present sparse homogeneous input. No novelty is asserted for additive polynomials or their constant-field property.


## Formal-group source audit and accepted realization — 25 November 2026

This dated integration retains the earlier search outcomes and records the subsequent completed formal follow-up. The complete source reports are `contributions/formal_height1_source/height_one_referee_report.md`, `contributions/formal_stienstra_source/SOURCE_AUDIT.md`, `contributions/formal_dp_mult/DP_MULT_SOURCE_AUDIT.md`, and `contributions/formal_height_complexity_sources/LITERATURE_AUDIT.md`. Exact source identities, hashes, locators and inspection scopes are in `workbench/SOURCES.tsv`; the primary PDFs and supplied DP manuscript remain outside the deliverable. This register integration adds no claim that its editor reread every original source or repeated a proof check.

The height-one audit directly checked Artin–Mazur's representability and smoothness hypotheses, including the curve exception, and Silverman's formal-group height definition and elliptic height bound. A characteristic-p principal-unit proof and a separately frozen integral-logarithm reconstruction agree. Stienstra's integral numerator is distinguished from the literal logarithm coefficient; the p-typical and unrestricted recursion conventions were checked against Hazewinkel. In particular, the next residue is only reduced after the preceding-height conditions make its division integral. The isolated proposal's dimension omission and the later p-primitivity terminology correction are preserved in their own correction records, without rewriting frozen historical proofs.

The supplied DP_MULT manuscript was resolved from its exact source archive, and only the relevant run/intake files were extracted once. The audit read the named DP1/DP3/DP34 hypotheses and complete proofs, with the additional named supporting results and exact line ranges recorded in `formal_dp_mult/canonical_events.jsonl`. The generic unramified Witt-lift derivative laws were proved completely in the contribution and separately reconstructed. The actual integral Honda-dual and direction hypotheses of DP34 were not replaced by equality of height or rational slope. The full source title is *Integral invariant derivatives at every formal height: Optimal affine error, divided-power distributions, Cartier duality, and binomial homotopy types* (unpublished research manuscript, 21 November 2026). No bibliographic author identity or archive cote is inferred from the intake filename.

The finite-height search located van der Geer–Katsura's cohomological upper bound and Fermat examples. The source audit supplies an explicit circuit/dimension bound and a finite stopping argument. Illusie's exact slope-[0,1) comparison and Artin–Mazur's Witt-module identification, supplemented by Yobuko's explicit finite-rank/zero dichotomy, justify the independent zeta route. The Lauder–Wan bound was kept with its degree, field, dimension and precision dependence; after dense expansion of the succinct equation, the complete arithmetic argument gives a genuine EXP upper bound, not merely decidability. A subsequent finite-operator criterion gives the stronger polynomial-space full-height algorithm. The exact collected-monomial representative, degree, target coefficient, first-exit invariance and stopping bound are stated and checked in the PSPACE proof and its separate reconstruction.

The initial existence search distinguishes fields carefully: KTY II proves nonemptiness over an algebraically closed field under its stated convention; that alone does not provide a prime-field point. The attempted finite-grid specialization and parameter-monomial route did not establish the required prime-field conclusion and remain in `formal_height_complexity_sources/FAILED_LEADS.md`. The accepted explicit integer coefficient seed bypasses this obstacle. Its exact multinomial valuation and finite-jet smoothing have a complete originating proof, a separate statement-only reconstruction, and post-freeze whole-proof comparisons. Every finite height now occurs over every prime field in degree p^h+p+1. The prime-field seed gate is closed, and the fixed-seed transfer makes exact finite-height completeness unconditional. No priority claim is inferred from these comparisons. The separate product/infinity research proposals are not adopted by this record integration; infinite-height hardness remains open.

Known small-dimensional existence results were also checked in their exact stated fields, rather than extrapolated: elliptic seeds over every prime field; complete quartic K3 height ranges over F2, F3, F5 and F7 in the cited sources; and the limited displayed higher-prime ranges in the more recent computations. The detailed source report states their precise ranges and limitations. Failed URLs, metadata corrections, the Pan/Mellberg filename discrepancy, source-locator corrections, and insufficient source leads are preserved. No absence theorem is inferred from failure to find an example.

The expert integration review `expert_formal_delta1/REPORT.md` checked the whole formal integration and its complete named supporting proofs in the exact frozen scope. It expressly excluded the new all-height seed proof. Yobuko was the only newly opened external primary PDF in that delta; other named source proofs were imported through their complete source audits. The separate newcomer reading covers the entire 30-input manuscript in 83 contiguous ranges, followed by eight scoped delta checks. These are whole-text proof readings, not additional source-free reconstructions or fresh program replays. Their 124 original events and eight nested delta events are retained canonically.

### Primary bibliography and exact formal-source locators

- van der Geer, G., & Katsura, T. (2003). On the height of Calabi–Yau varieties in positive characteristic. Documenta Mathematica, 8, 97–113. https://ems.press/content/serial-article-files/25920?nt=1

  **Locators:** Corollary 2.3, printed p. 100/PDF p. 4; Theorem 2.1, p. 99; Theorem 5.1, printed p. 107 and proof pp. 107–108/PDF pp. 11–12. **Recorded scope:** Statements and surrounding proofs read; Corollary 2.3 visually checked; Fermat theorem and rational Witt-module paragraph read. Not a full-paper reconstruction. **Use:** Finite-height cohomological bound and Fermat infinite-height examples.

- Lauder, A. G. B., & Wan, D. (2006). Counting points on varieties over finite fields of small characteristic. arXiv:math/0612147v1. https://arxiv.org/pdf/math/0612147

  **Locators:** Theorem 1, p. 2; Proposition 36, p. 27; reconstruction and degree/precision bounds pp. 28–29; Theorem 37, p. 29. **Recorded scope:** Exact general-input theorem and its complexity proof/reconstruction read; Theorem 37 visually checked. Does not claim independent reconstruction of the complete zeta algorithm. **Use:** Deterministic full affine zeta bit bound, with growing-dimension factors retained.

- Waterhouse, W. C. (1969). Abelian varieties over finite fields. Annales scientifiques de l’École Normale Supérieure, 4e série, 2(4), 521–560. https://www.numdam.org/article/ASENS_1969_4_2_4_521_0.pdf

  **Locators:** Theorem 4.1, printed p. 536/PDF p. 17, especially cases (1) and (5). **Recorded scope:** Exact trace classification and ordinary/supersingular distinction read and visually checked. **Use:** Ordinary and supersingular elliptic curves over every prime field, including p=2,3.

- Illusie, L. (1979). Complexe de de Rham–Witt et cohomologie cristalline. Annales scientifiques de l’École Normale Supérieure, 4e série, 12(4), 501–661. https://www.numdam.org/article/ASENS_1979_4_12_4_501_0.pdf

  **Locators:** II, Corollary 3.5, equation (3.5.3), and Remark (3.5.6), printed p. 616/PDF p. 117; K3 discussion §7.2, p. 653/PDF p. 154. **Recorded scope:** Exact slope-interval equation and nearby formal-group remark visually checked; K3 specialization read. Entire 162-page source not independently reconstructed. **Use:** Original crystalline slope [0,1) identification with rational Witt cohomology.

- Artin, M., & Mazur, B. (1977). Formal groups arising from algebraic varieties. Annales scientifiques de l’École Normale Supérieure, 4e série, 10(1), 87–131. https://www.numdam.org/articles/10.24033/asens.1322/

  **Locators:** II, Corollaries (4.3) and (4.4), printed p. 110/PDF p. 25; complete-intersection special case on the same page. **Recorded scope:** Exact page read and visually checked. Locator first supplied by affine_blind_v2; subsequent reading recorded as exposure. Source page range follows Numdam metadata rather than some references listing p. 132. **Use:** Cartier-module/Witt-cohomology identification and formal-Lie/finite-type hypotheses.

- Berthelot, P., Bloch, S., & Esnault, H. (2007). On Witt vector cohomology for singular varieties. Compositio Mathematica, 143(2), 363–392. https://arxiv.org/pdf/math/0510349

  **Locators:** Theorem 1.1 and equation (1.1), p. 2; §6.1, equations (6.1)–(6.2), pp. 33–34; Propositions 6.2–6.3, pp. 34–35 of arXiv v1. **Recorded scope:** Interfaces and zeta/valuation applications read. No claim to reconstruct the full descent proof. **Use:** Primary full-zeta slope-factor formula and rational Witt comparison.

- Katz, N. M., & Messing, W. (1974). Some consequences of the Riemann hypothesis for varieties over finite fields. Inventiones Mathematicae, 23, 73–77. https://web.math.princeton.edu/~nmk/old/katzmessing.pdf

  **Locators:** Setup, printed p. 73/PDF p. 2; Theorem 1, printed p. 74/PDF p. 3. **Recorded scope:** Both relevant pages read visually. Cover metadata says 73–78, while actual article and publisher bibliographic records say 73–77. **Use:** Crystalline/étale Frobenius characteristic polynomial comparison; corroborating route.

- Yobuko, F. (2019). Quasi-Frobenius splitting and lifting of Calabi–Yau varieties in characteristic p. Mathematische Zeitschrift, 292(1–2), 307–316. https://arxiv.org/pdf/1704.05604

  **Locators:** Definition on p. 1; §3, pp. 6–7; Theorem 4.5, p. 9, and complete proof p. 10 of arXiv v2. **Recorded scope:** Exact rational-rank/infinite-height dichotomy, finite-Witt criterion, and quasi-Frobenius/Artin–Mazur identification proof read. **Use:** Explicit dimension-h versus zero Witt module and height equality used by the finite operator.

- Kawakami, T., Takamatsu, T., & Yoshikawa, S. (2025a). Fedder type criteria for quasi-F-splitting I. arXiv:2204.10076v3. https://arxiv.org/pdf/2204.10076v3

  **Locators:** Theorem C and Delta definition, pp. 3–5; Theorem 5.8 and full proof pp. 37–39; Theorem 5.13 pp. 39–40; Example 6.2/Table 1 pp. 41–42; Example 6.7/Claims 6.8–6.10 pp. 43–45. **Recorded scope:** Operator statement and complete relevant proof read; examples and all-height-even proof read; key equation pages rendered and checked. Some typographical inconsistencies preserved in failed-lead notes. **Use:** Exact finite-dimensional height operator, base change, F3 quartic examples, and even heights over F2.

- Kawakami, T., Takamatsu, T., & Yoshikawa, S. (2025b). Fedder type criteria for quasi-F-splitting II. arXiv:2511.17270v1. https://arxiv.org/pdf/2511.17270

  **Locators:** Convention 4.15, p. 25; Theorem 4.18 and Claims 4.19–4.21, pp. 26–28. **Recorded scope:** Complete relevant all-height argument read; pages 25–28 visually checked, including the algebraic-closure overbar. Exact parameter exponent pattern inspected. **Use:** All finite heights over algebraic closure; explains why the source alone does not certify a prime-field point.

- Kedlaya, K. S., & Sutherland, A. V. (2016). A census of zeta functions of quartic K3 surfaces over F2. LMS Journal of Computation and Mathematics, 19(Special Issue A), 1–11. https://arxiv.org/pdf/1511.06945

  **Locators:** Page 2, after Computation 3; relevant census summary in introduction. **Recorded scope:** Explicit range claim read; census was not recomputed. **Use:** All allowable quartic K3 heights over F2.

- Batubara, R., Garzella, J. J., & Pan, A. (2025). K3 surfaces of any Artin–Mazur height over F5 and F7 via quasi-F-split singularities and GPU acceleration. arXiv:2502.12428v3. https://arxiv.org/pdf/2502.12428

  **Locators:** §3, pp. 5–7, Proposition 3.2 and Algorithms 2–4; Figures 4–5 pp. 17–18; Figures 6–7 p. 19. **Recorded scope:** Operator algorithms read and exact ranges checked; p. 19 tables visually checked. No recomputation of all equations. **Use:** Matrix implementation and explicit quartic prime-field height ranges. Local filename is historical; actual author is Alex Pan, not Maximus Mellberg.

- Batubara, R., Garzella, J. J., Huang, Y., & Mellberg, M. (2026). Newton strata realization for hypersurfaces via explicit p-adic cohomology. Research in Number Theory, 12, Article 110. https://link.springer.com/content/pdf/10.1007/s40993-026-00802-6.pdf

  **Locators:** Theorem 1.4(3); §6.3, PDF p. 19. **Recorded scope:** Published primary PDF range statement read and visually checked; underlying external computational dataset not redownloaded. **Use:** Quartic heights 1–4 over F17, F19, F23; primary current range statement.

- Stienstra, J. (1987). Formal group laws arising from algebraic varieties. American Journal of Mathematics, 109(5), 907–925. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/stienstra1.pdf

  **Locators:** Theorem 1, p. 907; Specialization paragraph, p. 908; Sections 1.2–1.4, p. 910; Section 2.2, p. 911; Section 3.9, p. 914; Sections 4.1–4.13, pp. 914–919. **Recorded scope:** Exact primary statement/proof ranges are documented in formal_stienstra_source/SOURCE_COVERAGE.json; no full-paper reading is inferred.

- Hazewinkel, M. (1977). Constructing formal groups I: The local one dimensional case. Journal of Pure and Applied Algebra, 9, 131–149. https://ir.cwi.nl/pub/9959/9959D.pdf

  **Locators:** Theorems 2.3 and 2.5, p. 133; Theorems 2.8 and 2.10, Corollary 2.11, p. 134; Equations (4.3.1) and (4.3.3), p. 138; Proof 7.4 and Corollary 7.5, p. 146. **Recorded scope:** Exact primary statement/proof ranges are documented in formal_stienstra_source/SOURCE_COVERAGE.json; no full-paper reading is inferred.

- Ravenel, D. C. (2003). Complex cobordism and stable homotopy groups of spheres (2nd ed.; author's online revision uploaded April 29, 2026). AMS Chelsea Publishing. https://www.sas.rochester.edu/mth/sites/doug-ravenel/mybooks/ravenel.pdf

  **Locators:** A2.1.17–A2.1.25, pp. 347–349; A2.2.1–A2.2.4, pp. 353–355; A2.2.7–A2.2.9, pp. 356–357. **Recorded scope:** Author textbook corroboration and explicit proof; Stienstra and Hazewinkel are primary research sources.

- Artin, M., & Mazur, B. (1977). Formal groups arising from algebraic varieties. *Annales scientifiques de l’École Normale Supérieure, 10*(1), 87–131. https://doi.org/10.24033/asens.1322

  **Height-one locators:** II(1.3)–(1.4), pp.103–104; II Corollaries2.4–2.6, p.106; Corollaries2.11–2.12, pp.106–107; II§4 andCorollary4.2, p.109; complete-intersection Special Case, p.110. Original extracted text and page images were read. These supplement the separately recorded Witt-module locators above.

- Silverman, J. H. (2009). *The arithmetic of elliptic curves* (2nd ed., Graduate Texts in Mathematics, Vol.106). Springer. https://doi.org/10.1007/978-0-387-09494-6

  **Locators:** III Proposition3.4, pp.61–63; IV§7, p.132; Remark7.1 andProposition7.2, p.133; Theorem7.4 andCorollary7.5, p.134. Each used page was read as extracted text and as a rendered original. No whole-book proof audit is claimed.

### Nth-prime bound added to the original counting construction

Rosser, J. B., & Schoenfeld, L. (1962). Approximate formulas for some functions of prime numbers. *Illinois Journal of Mathematics, 6*(1), 64–94. https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf

Root read the extracted statement and visually inspected printed p.69, Corollary(3.13), at04:04–04:05UTC on25 November2026. This supplies the primary nth-prime bound used in the uniform construction; the entire analytic proof was not read or reconstructed. The subsequently checked squared-index consequence is recorded in newcomer delta_01. The source PDF has2,520,753bytes and SHA256 `8e37b06f82e09421bceb2502578c47b61469141f0287e6acedb70e01765ab556`; its raw path is outside the deliverable and its canonical source row is `root-rosser-schoenfeld1962`.
