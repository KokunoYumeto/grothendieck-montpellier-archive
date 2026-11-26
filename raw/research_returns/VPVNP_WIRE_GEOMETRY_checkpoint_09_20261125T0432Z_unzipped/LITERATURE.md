# Literature and source retrieval log

The searches began on24 November2026 and continued on25 November2026; individual dates are recorded below. The three separate literature logs and source inventories under workbench/records are part of this record. Only citations, locators, hashes, and our research notes are returned; source papers and their text extractions are excluded.

## Initial primary-source verification

Opened the official Anthropic VP/VNP release README and the OpenAI formalization scope note:

- https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md
- https://github.com/openai/math/blob/main/lean/docs/379.md

The first describes the circuit and border claims and their Lean development. The second distinguishes the exact separation formalization from the quantitative border assertions of the paper. Neither complete development was rerun here. The attached papers were read directly, and the queried public sources are corroborating release records, not substitutes for their text.

Fetched the requested workbench format from https://raw.githubusercontent.com/KokunoYumeto/mathematics-workbenches/main/FORMAT.md . SHA256 b6cff6c746787fc706e3db621a372b83ab49b84e76b218776807154a7cd92832. Its format1 version is dated22 November2026. Official WB numbers and permanent pages are assigned only by the registry; this work is unfiled and uses provisional stable local statement identifiers.

## Spectrum and extension searches

The explicit-spectrum worker's LITERATURE.md records the exact searches, dates, primary URLs, versions, page locators, and PDF hashes for Christandl-Vrana-Zuiddam, Sakabe-Doğan-Walter, Botero-Christandl-Fraser-Leigh-Nieuwboer, Alman-Li-Pratt, and Wigderson-Zuiddam.

Root independently opened the arXiv v2 full texts2604.18283,2601.21553,2604.01386 and the Wigderson-Zuiddam author PDF. Theorem4.16 in the latter, printed page53 and proof pages56-57, is the spectral extension theorem used here. Section12.7, Theorem12.23 in this author version, gives the singleton-anchor interpolation discussed in the paper; numbering differs in the published version.

Root also opened Bugár-Vrana, Interpolating Between Rényi Entanglement Entropies for Arbitrary Bipartitions via Operator Geometric Means, Annales Henri Poincaré26(2025),2779-2826, https://doi.org/10.1007/s00023-024-01486-3 . Theorem3.23 and Corollary3.25 give relevant upper-functional and extension context. We do not claim their full proofs independently checked here.

## Same-day and neighbouring searches

The query families included tensor prices, Euclidean squares, wire inequalities, spectral normalization, asymptotic tensor spectra, and graph tensors. Both general search and targeted arXiv, journal, author-page, ECCC, and Hexagon searches were used. No absence-of-search-result is treated as a priority claim.

Root opened Yilin Liu, A uniform exponent bound for asymptotic tensor rank, https://hexagonmath.org/2611.00972v1 and its web-rendered PDF https://hexagonmath.org/pdf/2611.00972v1 . Read Sections2-4, especially Lemma2.1, Theorem3.1, and the normalized wire inequality(8) on page4. This applies the Anthropic price-space geometry to tensor rank. The direct byte download returned403; therefore a PDF byte hash is unavailable and is not invented.

Root opened Huanyi Zhou, Asymptotic Rank of Weighted Graph Tensors via Completely Positive Bounds, https://arxiv.org/html/2610.34273v3 . Read Theorem1.1, Theorem1.2, Section3's shared-leg separation, Section5.1's quadratic constraints, and AppendixB's graph-subrank discussion. The PDF https://arxiv.org/pdf/2610.34273v3 was retrieved: SHA256 2ea10f76cfae4e8b90057074293a1b67d5c22e8949d7888cf99529d714e8ee16. The complete-graph rank bound is used as an explicitly cited input. The shortening worker rechecked the full Section3 construction; the entire82-page preprint has not been independently audited.

At the next root search the exact queries were:

1. price square VP VNP tensor, with30-day recency;
2. spectral wire Strassen normalization;
3. site.eccc.weizmann.ac.il tensor asymptotic spectrum quantum functional;
4. site:hexagonmath.org Euclidean price.

These found ECCC TR26-281 and TR26-298 concerning the recent matrix-multiplication work. The ECCC endpoints intermittently returned rejection or incomplete pages. The relevant accessible primary text was then found on arXiv:

Baitian Li, Semidirect sums of tensors and the matrix multiplication exponent, https://arxiv.org/abs/2611.04175v1 ,3 November2026. PDF SHA256 dbdecdd3cbff8929f66580b08bd30840c44f01fea55638ac992647683afe2d8d. Theorem2.1 printed page5, Lemma2.3 pages6-7, and the cancellation argument on page8 were read. Root opened the full HTML; the shortening worker checked these proofs. Its three-party untwisting mechanism prompted our exact copied-output rank test. Zhou's several-shared-leg construction is presented alongside that narrow failed lift so it is not mistaken for an obstruction to every higher-party construction.

Amir Shpilka, Exposition of OpenAI's Matrix Multiplication in Exponent9/4 (and an explicit algorithm), ECCC TR26-281,27 October2026, https://eccc.weizmann.ac.il/report/2026/281/ . The explicit-spectrum worker opened its53-page PDF and checked the statement of Theorem1.1 on page2 and the spectral appendix. We do not use the numerical9/4 bound to decide the square question.

The shortening worker retrieved and read Vrana-Christandl, Entanglement distillation from Greenberger-Horne-Zeilinger shares, arXiv:1603.03964v2,30 March2016, published Communications in Mathematical Physics352(2017),621-627. PDF SHA256 5c14c424554d3efc2c949bd2082e1b8e5f033e416e833fb3b3ef11bec4478810. Theorem1 on page3 and proof pages3-6 supply the graph-subrank context. The four-cycle special case is proved in our paper.

## Classical attribution checks

Root searched for Valiant's1979 algebraic-completeness paper and Bruhat-Tits'1972 source. Opened the ACM DOI record for Valiant and the primary Numdam/IHÉS record for Bruhat-Tits.

- L. G. Valiant, Completeness classes in algebra, STOC1979,249-261, https://doi.org/10.1145/800135.804419 . Retrieved the author-deposited scan at https://sites.math.washington.edu/~billey/colombia/references/valiant.completeness.1979.pdf ; SHA256 95ba81c4721bf31722bc052177d6260807f3ffb8281572bb0d031f6b0efd080d. Opening context on pages249-250 is cited.
- F. Bruhat and J. Tits, Groupes réductifs sur un corps local:I. Données radicielles valuées, Publications Mathématiques de l'IHÉS41(1972),5-251, https://doi.org/10.1007/BF02715544 . The modern CN and flat-rectangle locators are Bridson-Haefliger, ExerciseII.1.9(1)(c) and TheoremII.2.11, and the exact source-preprint proofs are Anthropic AppendicesC andO.

## Attached work and the limits of its use

The supplied integration note was treated as unchecked input. Its scaled finite-identity inequality has the reciprocal scale direction corrected explicitly in our paper. Its star-only picture is expanded to the2026 literature.

The attached B5 norm statements and B7 integral-witness arguments were rechecked where used. The Kronecker positivity notes motivate exact character computations but do not supply a price construction. The attached border-rank and pencil methods are discussed only for their fixed-layout obstruction scope; no earlier certificate is assumed to settle the square.

The GCT/field worker records primary retrievals and exact locators for Berkowitz, Mulmuley-Sohoni, Landsberg-Manivel-Ressayre, Bürgisser-Ikenmeyer-Panova, and curve selection. The independent padding variable changes the safe no-occurrence threshold to the one stated in the paper. Source bytes are inventoried by SHA256 in workbench/SOURCE_BYTES.tsv and are not returned.

## Crossing rank and Hurwitz searches, 24 November 2026, 22:05–22:24 UTC

Root searched for partial-transpose rank, the complex Hurwitz exponent, and crossing decompositions, then opened the following primary sources. The exact later queries were `"Hurwitz" "sqrt" "2026" "Khoruzhii"`, `"partial-transpose rank" "identity" lower bound`, and `"Hurwitz" "1.414" "composition" complex`, with one-year recency, followed by `Dugger Isaksen Hopf condition bilinear forms arbitrary fields 2007 K theory quadrics` and `Rossman Zhu sum of squares Lemma3.12 correction2026`.

- Benjamin Rossman and Davidson Zhu, Multi-Quadratic Sum-Of-Squares Lower Bounds Imply VNC1 != VNP, ITCS2026, LIPIcs362, article113, DOI10.4230/LIPIcs.ITCS.2026.113. Opened the full Dagstuhl HTML and PDF. Definition3.4 and Lemma3.5 on page113:8 identify the two-cut crossing rank. Lemmas3.12–3.14 on pages113:9–10 compare it with sums of squares. The unrestricted factor-one claim in Lemma3.12 has the explicit rank-one matrix counterexample recorded in our paper; our proof uses directly proved factor-two bounds. PDF SHA256 b60be6bbdb2b14909c627887926c226f0a089f7c943660c171c9ebeaafba53c6. Full version arXiv:2512.01227.
- Kirill Khoruzhii, Crossing Decomposition for Subquadratic Noncommutative Circuits, https://lemmata.iol.berlin/crossing-decomposition , v1 2November2026, revised4November. Lemma1 and Corollary3 already prove the square-root-two crossing/Hurwitz upper exponent from the Anthropic ETH crossing identity and a finite fermionic variant. This upper bound is credited to those sources, not claimed as new. The page reports kernel checks of six statements at commit a20ff2d299b3; we have not rerun that development. HTML SHA256 831d2b3a59de97bcd886318e7477fc039e32dc3d0f76ac370f4739d70e17e3da.
- Pavel Hrubes, A Subquadratic Upper Bound on Hurwitz's Problem and Related Noncommutative Polynomials, SIAM J.Comput.55(2)(2026),451–467, DOI10.1137/24M1666884, Theorem1. The publisher record and ECCC2024/026 were opened. The ECCC PDF download returned503. The explicit-spectrum worker later found the author's accessible PDF; its metadata are in that worker's records.
- Yilin Liu, Stretched-exponential circuit lower bounds for the noncommutative permanent and determinant, https://hexagonmath.org/2611.00994v1 ,24November2026. The abstract states the no-planar-shortening and shortening branches for row-ordered noncommutative polynomials. The PDF retrieval returned403 and the full proof has not been read; this is contextual evidence only, not a checked input to our new equivalence.

## CAT(0) equality and extension searches

Root opened Alexander Lytchak, Euclidean filling inequalities in CAT(0) spaces, arXiv:2611.13159v1,9November2026, Proposition1.4 and Section13.1. It proves a stronger equality/flat-convex-hull statement. Our cross-polytope proof instead uses the classical flat-square, tangent-cone and parallel-set results in Bridson–Haefliger, together with Lang–Schroeder's Kirszbraun theorem (GAFA7(1997),535–560, DOI10.1007/s000390050018). The precise extension statement is also Alexandrov Geometry: Foundations, Theorem10.14, p160, arXiv:1903.08539v6. The explicit-spectrum worker's source inventory contains the downloaded hashes.

## Quadratic forms, motivic cohomology and K-theory

Opened Daniel Dugger and Daniel C.Isaksen, The Hopf condition for bilinear forms over arbitrary fields, Ann.Math.165(2007),943–964, DOI10.4007/annals.2007.165.943. Theorem1.2 on943 gives binomial-parity conditions for composition formulas in characteristic different from two. Pages944–949 explain the deleted-quadric map and the motivic-cohomology argument. Also opened their Algebraic K-theory and sums-of-squares formulas, Doc.Math.10(2005),357–366, DOI10.4171/DM/192. These are a concrete connection between the Hurwitz reformulation and the requested Grothendieck-language dictionary. Their deep cohomological calculations are cited background, not presented as independently re-proved here. Retrieved byte hashes and access failures are recorded in records/root/KTHEORY_SOURCE_METADATA.json.

## 2026-11-24 22:49--22:58 UTC: Fermat curves and reconstruction

Opened the primary Stacks Project statements: Section53.9/tag0BYA (smooth Fermat curves), Lemma53.9.3/tag0BYD (genus), and Lemma53.5.2/tag0BS6 (Riemann--Roch and duality). The manuscript uses these to compute the precise total two-point jet budget on the full line-bundle section space, while keeping the determinant subspace separate. Download hashes and URLs are in workbench/records/root/STACKS_CURVE_SOURCE_METADATA.json; downloaded HTML is outside the deliverable.

Opened Haettel--Kielak--Schwer, arXiv1304.5990v2, official abstract and metadata, confirming the bounded graded complemented modular-lattice CAT(0) theorem and journal publication. The detailed source check and PDF hash are in the gct_field source ledger.

Searched the web in general mathematical terms for `"Fermat curve" "sum of squares" Hurwitz`, `"crossing" "tensor" "Fermat" characteristic two`, and `"Hurwitz" "partial transpose" amplification`. Results returned the previously cited Khoruzhii crossing decomposition and Rossman--Zhu PT framework, along with unrelated number-theory and quantum-information pages. No priority conclusion is drawn from this search.

## 2026-11-24 23:22–23:25 UTC: alternative composition and polynomial kernels

Searches: `Hurwitz sums of squares identities complex bilinear asymptotic exponent2026 partial transpose rank`; `Hurwitz composition formula tensor product twisted multiplication bilinear sum squares exponent`; `sum of squares partial transpose Hurwitz lower bound`. These returned the already used Hrubeš, Rossman–Zhu, Khoruzhii and Zhang–Zhu works, plus composition-algebra surveys. No new improvement is asserted. The primary author-page version of Hrubeš was located at https://users.math.cas.cz/~hrubes/PDFs/palindrome.pdf; it is not yet an additional proof dependency.

Searches: `orthogonal polynomials quadratic lattice Poisson kernel self dual Racah generating function primary`; `Meixner orthogonal polynomial exponential generating function classification quadratic energy`. DLMF18.25 (https://dlmf.nist.gov/18.25) identifies the Racah/dual-Hahn quadratic lattice; DLMF18.19 (https://dlmf.nist.gov/18.19) provides the weights and squared norms of the Hahn, Krawtchouk, Meixner and Charlier systems; DLMF18.2.41 (https://dlmf.nist.gov/18.2#E41) defines the usual Poisson kernel with linear spectral exponent z^n. The quadratic lattice is not itself the nonlinear energy grading needed in the crossing construction. Also located Albanese–Lawi, SIAM J.Math.Anal.38(3)(2006),977–984 (preprint2005), `Poisson Kernels as Expansions in q-Racah Polynomials`, DOI10.1137/S0036141003435035; no theorem from it has been used. These are candidate searches, not evidence of a classification or priority claim.

## 2026-11-25 00:45 UTC — octonion output spans and modular averaging

Queries: “octonion multiplication Gram matrix partial transpose sums of squares rigidity”; “SL2 characteristic two Reynolds operator tensor power invariant endomorphism”; “site:eccc.weizmann.ac.il Hurwitz sum squares tensor rank”; “site:hexagonmath.org spectral price square tensor centralizer”. These returned classical composition-algebra background, Hrubes's existing ECCC Hurwitz entry, and primary work on Reynolds operators and modular SL2 tensor powers. No exact identification of the fixed-output-span proposition was established, and no priority claim is made. The Hexagon-restricted query produced no relevant new source in this result set.

Opened Aryaman Maithani, *Splitting the difference: Computations of the Reynolds operator in classical invariant theory*, Bulletin of the London Mathematical Society58(2026),e70175, DOI10.1112/blms.70175, author PDF https://aryamanmaithani.github.io/math/papers/maithani_classical_reynolds.pdf . The introduction and contents distinguish classical characteristic-zero Reynolds operators from positive-characteristic splitting; §8 is the relevant further-reading lead. No theorem from this paper is used in the checkpoint proof, whose swap-projector calculation is elementary and written in full.

Opened the primary abstract and metadata for Coulembier, Etingof, Ostrik and Tubbenhauer, *Fractal behavior of tensor powers of the two dimensional space in prime characteristic*, arXiv2405.16786v2, Contemp.Math829(2025),85–138, https://arxiv.org/abs/2405.16786 . It studies indecomposable summand counts for modular SL2 tensor powers. This is a lead for further structural work; no rank-reduction theorem is imported. An octonion-rank search result for arXiv2608.16649 could not be opened, so no claim from it is used. The ECCC2024/026 landing page rejected this retrieval; the earlier checked Hurwitz sources remain the basis of that part of the paper.

## 2026-11-25 00:53–01:00 UTC — operator geometric means as a positive route

Followed the Bugár–Vrana citation in the higher-order quantum-functional paper. Queries: “Bugar Vrana Interpolating Between Renyi Entanglement Entropies Arbitrary Bipartitions operator geometric means spectral monotone alpha zero” and “site:arxiv.org upper quantum functionals power regularization crossing bipartitions”. Opened the primary arXiv abstract and Springer full article; downloaded the primary arXiv2208.14438v2 PDF outside the deliverable. Exact URL, SHA256 and pages are in records/root/OPERATOR_MEAN_SOURCE_METADATA.json.

Read the observable construction, the geometric-mean closure argument, and the upper/lower comparisons in Sections4–5. Proposition4.8 and Example4.10 give upper functionals for positive Rényi parameter. Proposition5.3 and Corollary5.5 evaluate flat-marginal states, including graph tensors, only for parameter at least1/2. That bound is not applied at the restriction boundary alpha=0. Theorem3.23 concerns the spectral regularization of an upper functional; raw finite-copy lower bounds do not automatically lower-bound that regularization. This is an active positive construction route, with no claimed price construction yet.

Separately reread CVZ Theorem3.5 and the 2026 higher-order paper's AppendixD. Their upper-functional submultiplicativity statement is restricted to noncrossing weights. The existing GHZ2 counterexample alone does not exclude a positive-power repair. A separate two-wire multiplicativity witness has been derived and is undergoing statement-only independent reconstruction. Arbitrary asymptotic regularization is a separate question.

### 2026-11-25 01:10 UTC — normalization hypothesis audited

Definition3.1 normalizes an upper functional only at1. Definition3.6 and Theorem3.23 require the stronger all-natural-unit condition g(U_r)=r. Theorem4.5 does not itself establish that condition for arbitrary crossing geometric means below alpha=1/2. Corollary5.5 establishes the relevant exact graph/GHZ values for alpha>=1/2. The active boundary criterion now includes an arbitrary GHZ factor and n=0, rather than assuming all-unit normalization.

## 2026-11-25 01:11–01:15 UTC — published operator means and graph-spectrum anchors

Primary searches: “Bugar Vrana geometric means 2026”, “operator geometric means asymptotic spectrum graph tensors alpha”, “2208.14438 GHZ”, “Wigderson Zuiddam graph tensors spectrum star convex gauge points 2026”, and exact log-star-convexity queries. Opened the authors’ quantum-information group publication list, the published Bugár–Vrana PDF, and Wigderson’s primary author-version Theorem12.23. The published operator-mean paper retains the all-N normalization hypothesis and the alpha>=1/2 flat-marginal range; exact printed pages and source hash are in OPERATOR_MEAN_SOURCE_METADATA.json. The anchor theorem applies to individual-vertex flattenings. That scope was already correctly recorded in the paper; it does not permit arbitrary crossing-cut interpolation. No additional main-gate reduction results from these searches. The AMS direct article endpoint returned an access error; the previously obtained author PDF is used with its own numbering.

## 2026-11-25 01:24–02:06 UTC — upper-functional normalization and precise source scope

Primary searches for “upper functional power regularization”, “subadditive submultiplicative normalization asymptotic spectrum” and “semiring unit growth submultiplicative spectrum normalization” located the Bugár–Vrana framework; no exact matching growth-normalization lemma was identified. No priority claim is made. The published article, DOI10.1007/s00023-024-01486-3, was checked at Definitions3.1/3.6, Theorem3.23, Proposition4.8, Example4.10 and Proposition5.1. Exact source bytes and pages are in SOURCE_BYTES.tsv and records/root/OPERATOR_MEAN_SOURCE_METADATA.json.

The published equation121 onp2817 has an extra outer exponent: equations1 and120 cancel it, and equation128 onp2819 uses the corrected moment. Root visually checked the published page; a separate worker checked the defining algebra and subsequent formula. This is a narrow typographic correction, alongside the already recorded G6 direction correction. Our raw functional follows the definitions.

Searches for “spectral prices negative type tensors”, “wire metrics cut cone”, “rank metric negative type binary” and related Euclidean-square phrases did not identify a theorem making all prices L1 or of negative type. The16-point square-root-rank obstruction therefore excludes cut combinations only. Wigderson–Zuiddam Theorem12.23 was rechecked: its centres are vertex flattenings, so arbitrary crossing cut interpolation is not justified by it.

Dvir–Edelman2019 Theorem1.3 does preserve convolution in its finite-field setting, but that setting does not supply complex Fourier diagonalization. Generic complex circulant nonrigidity may change convolution structure. Neither source yields the required Bell-diagonal construction; the source-conditioned scope is recorded in the explicit-spectrum records.

## 2026-11-25 02:15 UTC — inclusion matrices and Boolean majority

Queries: “Wilson inclusion matrices rank subsets characteristic two1990 diagonal form”; “square zero algebra elementary symmetric polynomial multiplication rank characteristic2”; “Boolean majority polynomial characteristic two high degree complement”. The search located R.M.Wilson, A diagonal form for the incidence matrices of t-subsets vs.k-subsets, European Journal of Combinatorics11(1990),609–615, DOI10.1016/S0195-6698(13)80046-7; and the primary author manuscript Inclusion Matrices and Chains, arXiv0709.3144. The degree-block full-rank fact is expected to be a special case of Wilson's rank formula; primary-statement/page comparison is pending. The paper presently gives its direct disjoint-subset proof as part of the required regular-algebra rank calculation, with no priority claim. The search also located work on symmetric Boolean polynomial degrees, but no source was identified for the exact high-ordinary-degree multiplication/PT statement in its present form. Search discovery is not a proof check.


## 2026-11-25 02:24–02:46 UTC — non-tree geometry, prices, and crossing exponents

The focused primary-source search and exact query log are in records/explicit_spectrum/TREE_PT_PRIOR_ART_SEARCH.md and TREE_DICHOTOMY_SOURCE_AUDIT.md. Bridson–Haefliger II.3.6, II.3.18–3.19, printed185 and190–192, supply first variation and completed tangent geometry. Kleiner's author preprint TheoremA(3), printedp2, identifies Euclidean balls among rescaled subset limits in its broader dimension theorem. The proof used here is a direct two-dimensional finite-configuration argument; no claim of priority for the geometry is made.

Root opened the primary Kleiner PDF, the Dragomir–Nicas journal PDF, and Liu's Hexagon2611.00994v1 PDF. Dragomir–Nicas's quadrilateral constant is scale-free; their quasi-hyperbolicity constant allows an additive error and is not the quantity used in the price gate. Liu, Section2 'Two crossing cuts', printedp3, already obtains the sharp complex Hurwitz exponent from absence of planar shortening. The current paper credits that implication. The additional price-space connection and complementary exponent-one conclusion are stated with all cited hypotheses. No matching full exponent-gap theorem was located in the focused search; absence of a search hit is not a priority claim.

Wilson's degree-block full-rank formula is now verified as the precise special case of the diagonal form stated by Ghorbani et al., arXiv0709.3144v1, Corollary3 printedp10. The paper credits Wilson1990 and that primary restatement, while retaining the short special-case proof needed for its complete multiplication-rank calculation. The original Wilson journal full text was unavailable through its direct endpoint; metadata and the primary proof restatement are distinguished.


### 2026-11-25 02:47–02:55 UTC — recovered original source bytes and width reduction

The author-linked Mulmuley–Sohoni DVI was recovered and its title/authors/introduction checked; its40-page PDF derivative is identified separately from the journal version. Original and derivative hashes are in records/explicit_spectrum/SUPPLEMENTARY_SOURCE_BYTES.json. The published Hrubeš–Wigderson–Yehudayoff2011 PDF was recovered by root after an earlier403, using the same author-hosted URL and a standard browser user-agent. Its SHA256 is9dcfe2e2b3246157e83910ad95aefef020dc98b6e1d8546172678f2d82c64829. The earlier audit's access limitation is preserved chronologically; SOURCES.tsv now records the recovered bytes.

The source's central-width reduction, with Propositions3.2/5.3 and Lemmas3.5/5.5, is an all-field route from fixed superlinear crossing width to exponential noncommutative-permanent circuit lower bounds. The integer-coefficient SOS lower bound cannot be imported as an unrestricted complex or PT lower bound. The paper includes this scoped classical context and distinguishes Liu's stronger unrefereed no-shortening claim.

The registry's referenced check_workbench.py was requested through its raw and GitHub source URLs; the web service returned DisabledError for both. No official validator run is claimed. The format specification itself was previously retrieved and is recorded as an external dependency; final pre-deposit preparation will keep the unassigned registry number explicit.

##25November2026,03:30–03:39UTC: primary-source recovery

The complete registry checker was recovered from its primary raw GitHub URL after the web retrieval routes had failed. SHA-25613042772b472b1a65f35fd8d8c349dc55a5e9cdabb5e6e5e4434aa1d4b6f0291,4955bytes. Its full source was read; it fixes exact table headers, requires assigned WB tags/folders, and accepts only its stated text suffixes plus PDFs beside own TeX. The filing exporter preserves original own-code bytes under portable text names and leaves the work number pending. This corrects the earlier availability limitation without changing the earlier records.

Naslund's primary arXiv1701.04475v3 PDF was recovered,255034bytes,SHA-2564d0059a326f700ca1ad7d3c702020bbe603b776d5546627b51d3eb9f19ea2eef. Problem12, printedp8, was read and matches the crossing question after the recorded permutation. No superlinear lower bound is claimed. The source bytes are outside the deliverable.

## 2026-11-25 03:50–04:15 UTC — rectangular Specht commutants

The focused search and source audit are preserved in the gct_field records and their literature log. Manivel, A note on certain Kronecker coefficients, Proc.AMS138(2010),1–7, primary preprint https://arxiv.org/pdf/0809.3710v1, was opened and checked at Schur–Weyl Section2 p2 and the optional multiplicity-free height-two Theorem1 p1, with complete proof Section3 pp3–4. Saved PDF SHA256868438909fb5ab2e06b6b3624c65aae9d0ed8833c39071a5b5ff9c71ed9aa0ca,120889bytes. Multiplicity-freeness is not needed in the general barrier.

Stanley, Irreducible symmetric group characters of rectangular shape, SLC50(2004),B50d, primary journal PDF https://www.mat.univie.ac.at/~slc/wpapers/s50stanley.pdf, was checked at Section1 pp1–2 for Specht dimensions and the hook formula only; its main character theorem is not imported. SHA256c336b13ccec91c6bffa940dabbcb94d50c4628a7bad2ee257e13a58ae99a5904,164858bytes. The present fixed-height rank conversion is fully proved and separately reconstructed, with no priority assertion and no claim about unrestricted matrices.

## 2026-11-25 04:28 UTC — canonical exterior contraction search

Queries: “partial transpose exterior Kneser”, “characteristic two Kneser rank matrix exterior”, “site:hexagonmath.org exterior contraction crossing rank Kneser”, “site:eccc.weizmann.ac.il crossing tensor exterior algebra”, “Kneser partial transpose”, and “exterior contraction rank characteristic two Kneser”. Two search systems were used because the first exact-phrase coverage was sparse. Results included classical incidence-matrix context, unrelated Kneser-neighbour/quadratic-form uses, ECCC tensor-rank papers, and positive-state partial-transpose spectral bounds. No exact match to this canonical characteristic-two grouping and its rank exponent was identified in those results. No new external theorem is imported, no modular diagonalizability is assumed, and the absence of a hit is not a priority claim. The proof is the full elementary subset calculation and entropy estimate in the paper.
