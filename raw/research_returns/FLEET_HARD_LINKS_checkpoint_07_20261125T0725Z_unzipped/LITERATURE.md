# Literature search log

## 2026-11-25, Part A

Searches: permanent level spaces all-ones matrix; rook polynomial logarithm connected partitions; Fourier minors composite/square-free order; recent VP/VNP claims; workbench format.

The primary public proof repository redirects from brilliant-hq to open-goat. Its own README distinguishes machine checking from claims about the mathematical interpretation. The dated local graph remains the status baseline.

Fourier search found Loukaki (2025), *Chebotarev’s theorem for cyclic groups of order pq and an uncertainty principle*, Bulletin of the London Mathematical Society 57(12), 3841–3856, DOI 10.1112/blms.70192; and Caragea, Lee, Malikiosis, and Pfander, arXiv:2505.24326, Theorem 1.2. These concern principal or specially matched minors, not all minors at composite order.

Workbench FORMAT.md fetched from the user-designated public raw URL, SHA-256 b6cff6c746787fc706e3db621a372b83ab49b84e76b218776807154a7cd92832. It is cited, not included in the return. Pending registry numbers must not be invented.

## 2026-11-25, further Part A sources

Searches `MacMahon master theorem permanent determinant inverse coefficient squarefree`, `level spaces permanent dimension`, and `Fermat linear subspace cubic power sums` led to Goulden and Jackson (1992), Corollary2.2,p608, opened in the author-hosted PDF. The determinant coefficient formulation is classical and is cited accordingly. Blokhuis and Seidel (1983), Theorem4.2,p7, was opened through the web service; a local byte fetch returned403, so no local hash is claimed for that unread byte stream. Full worker-specific search logs remain in their research directories and are part of this workbench.

## 2026-11-25, Part B beginning

Queries `Fischer1974 circuits limitednegations logn Beals Nishino Tanaka`, `Jukna read1 circuits quadratic`, `C4free monotone circuits`, `four quadratic witnesses circuits`, and subsequent primary-source searches were used to locate the exact limited-negation and read-k literature. Jukna's 2022preprint has a published2024/2025 successor; the exact versions are being checked. The dated graph's additivity formal statements553558559659 have hypotheses of cycle/hub separation or forest overlap that do not hold automatically for the affine-plane completion. These statements are not used as an additivity theorem for that completion.

### 2026-11-25 — B and C primary-source checks

Jukna author pages and ECCC revision pages were searched for C4-free monotone graph circuits and read-k witnesses; no prior resolution of the specific unrestricted target was located. The opened author manuscript of On Graph Complexity numbers the formula result Theorem7.1 (pp15–16), whereas the prompt refers to a differently numbered version; the source version must accompany every locator. Jukna read-k arXiv manuscript Lemma1 p7 is the support criterion; Definition1 p8 distinguishes semantic read1 from wire occurrence. The current journal article is Discrete Applied Mathematics360(2025),307–327.

Stienstra1987 Theorem1 printedp907 and the base-change paragraphp908 were visually opened. Artin–Mazur1977 II Corollary4.2 printedp109 and special casep110 give the complete-intersection formal group; II Corollary4.3p110 identifies Witt cohomology. The height1/2 proof in the paper uses Stienstra and elementary formal-group algebra, not an unstated crystalline comparison.

## 2026-11-25, C classical congruences and computational scope

Queries: `formal group height counting complexity Calabi Yau`, `Hasse-Witt Mod complexity SAT`, domain searches at ECCC and Hexagon for formal-group height, `formal group logarithm coefficients height criterion Stienstra Vlasenko`, and `Calabi-Yau height two Hasse polynomial`. Primary arXiv and journal/author pages located Vlasenko, Formal groups and congruences (2019), arxiv1509.06002v5, Theorem2(i), p3. It already proves the valuation characterization; the paper credits it and keeps only the coordinate-specific elementary proof needed for the quotient interpretation. The searches also located unit-root congruences and Goto's algorithm for weighted Delsarte threefolds; those special presentations do not establish the general circuit-input complexity claim. No prior instance of the precise formula-replica completeness theorem was located; this is not a priority claim.

Lauder-Wan's published chapter was opened at Theorem1p580 and Theorem37p610. Wan's Theorem6.3/Cor6.4p571 supplies exact Newton multiplicities. Artin-Mazur III Cor3.4p119 was visually read. The algorithm uses these existing theorems, not a newly claimed zeta algorithm.

Queries on character-table all-minors nonvanishing, imaginary-quadratic classgroups, and Bach-Sorenson prime bounds found the classical distinction between prime-order Fourier minors and composite-order singular minors. Tao's attached primary LaTeX Lemma1.3 was read. The Bach-Sorenson institutional bibliographic page was read, but both attempted AMS PDF URLs returned403; no full-paper theorem or hash is claimed from that failed fetch. The class-group counterexample requires no analytic theorem.

Theta-source searches and their exact locators are recorded in research/c_theta/SOURCES_AND_HYPOTHESES.md. They identify the odd-coset statement as classical Gopel combinatorics, not a priority claim. EGA editions were explicitly searched in the attachment: only SGA7_FR is present, so the external EGA references do not duplicate an attached edition.

## 2026-11-25 — weighted cubic dimension argument

Searched general terms “permanent level spaces all ones cubic dimension bound rook polynomial linear subspace”, “weighted Fermat cubic quadratic linear spaces coordinatewise product Kneser Mirandola Zemor”, and targeted primary searches for permanent level spaces and permanull subspaces. No matching weighted bound was located. Mirandola–Zemor Theorem3.3 (p7) was reopened and is the precise product-dimension input, not a priority claim for the application. Ghasemi–Gross–Kopparty, *Permanental rank versus determinantal rank of random matrices over finite fields*, ECCC TR25-206, authorPDF https://www.math.toronto.edu/swastik/permanents-mod-p.pdf , was opened at the introduction, definitions2.2–2.3 and statement4.8 (printedpp3–5). Joint permanullness permits independent choices of columns, unlike correlated row/column projections of a level space; no unproved transfer is used. The full later proof was not yet read and the result is not a dependency.

## 2026-11-25 04:58 UTC — weighted cubic bound and border comparison

The general-term search for permanent level spaces and weighted coordinatewise-product cubic bounds did not locate the displayed weighted transform; no priority claim is made. The primary author manuscript of Landsberg–Manivel–Ressayre was opened at Theorem1.0.1,p1 (April2010 numbering) and compared with the exact coefficientwise-affine definition in the public Lean GCT definitions. OpenAI’s September24 cubic-border preprint was located by the repository API, fetched, hashed, and opened at Theorem1.1,p2 and its earlier-work discussion,p3. It states an asymptotically stronger cubic bound with explicit constants. Only its statement and context were inspected; its proof is not a premise. The new level bound gives N≥m²−2m+1−floor((m²−2)/3), e.g.74 at m12, through the separately cited graph transfer. Source files remain outside the return.

## 2026-11-25 05:12–05:29 UTC — uniform characteristic and a possible space bound

Searched general terms counting modulo small primes / Chinese remainder / counting classes, then verified primary Beigel–Gill author page and TCS source (Theorem30 already used for fixedprimepowers). The variable-characteristic oracle argument is written out completely, with a parsimonious shift, explicit O(p²) height-two gadget, and an elementary primorial bound; no priority claim is made. Searched zeta-function computation with PSPACE, parallel algorithms and Newton polygons. Mittmann–Saxena–Scheiblechner author manuscript §1.1,p3 discusses Lauder–Wan and the exponentialdegree space issue; it is contextual, not a theorem that the height algorithm is in FPSPACE. The primary Lauder–Wan finite-trace algorithm is being examined for a rigorously uniform parallel implementation. The current accepted upper bound remains FEXPTIME pending proof and independent review of that stronger claim.

## 2026-11-25 05:52 UTC — finite trace formulas and uniform division

The possible space bound from the earlier search is now proved and independently rederived. Opened Lauder–Wan's published finite trace construction at Theorem28 pp600–601, Algorithm29 pp602–603, the standard simplex pp607–608 and lifting/coefficient lemmas. Opened Hesse–Allender–Barrington's author manuscript at uniformity pp4–6 and division Corollary6.3 p16, and the 2014 corrigendum pp1–2. The corrigendum retracts bounded-arithmetic consequences in Corollary6.6, not uniform division. The new FPSPACE proof derives polynomial depth and gate addressing; neither source is represented as stating this height complexity classification. Exact primary PDF hashes are in SOURCES.tsv.

Searched Schönhage–Strassen1971 with logical-networks and summary/page terms to tighten the circuit-size citation. Author bibliography confirms Computing7,281–292 and DOI10.1007/BF02242355; publisher primary summary was requested. Secondary search hits are discovery only and not proof sources.

05:54UTC follow-up: Springer primary Summary explicitly states the O(N logN loglogN) bound for logical nets with a binary logical element as a step. Its HTML was fetched and hashed6a42aa4f24dbe68324a7c398162fe15884045998515720bcd8e406589a73d3d8 outside the workbench. The exact paper citation uses Summary, without inventing a theorem number or claiming the inaccessible full text was read.

## 2026-11-25 05:57–06:15 UTC — further main complexity and low-square routes

Searched exact strings Hasse–Witt/PSPACE, formal-group height/complexity/polynomial-space, and coefficient/PSPACE-hard/arithmetic-circuit/bounded-degree. These did not provide a matching hardness theorem. A stronger primary-source search on quasi-F-split height/hypersurfaces/algorithm/matrix located Batubara–Garzella–Pan2025 and its Kawakami–Takamatsu–Yoshikawa2022/2025 input. Their papers were opened in full by the resource-analysis worker; exact primary PDF versions/hashes/locators are in research/c_quasi_height/SOURCES.tsv. The operator and matrix algorithm are prior work. A separate resource analysis for binary-prime circuit inputs is under independent review. The original Lauder–Wan proof remains valid, but the paper will credit the simpler existing algorithm directly. A search on coefficient/PSPACE/arithmetic circuits also located Koiran's VPSPACE transfer paper as context, not an invoked hardness theorem.

For A, searched codes/small-square/dimension/classification; linear-codes/Vosper/minimum-distance/Schur-product; and Castelnuovo/Schur/codes/square-dimension. Follow-up primary-source queries used Reed–Solomon/Mirandola–Zemor, Castelnuovo/codes/2k, and linear-codes/small-product-dimension/classification. Many hits were irrelevant barcode material or secondary summaries and are not used. Reopened Mirandola–Zemor's exact Theorem4.2 in the already-hashed primary manuscript: its equality classification explicitly assumes both codes MDS. The weighted code's row/column barycentric dependencies violate the needed general-position premise in the dimension15 case. No valid classification giving a smaller level-space gate was found. Research/a_low_square_route/GATE.md states the exact remaining obstruction.

## 2026-11-25 06:36 UTC — unary-height and matrix complexity searches

Queried the two search engines for quasi-F-split complexity, Artin–Mazur height counting complexity, cyclic-orbit matrix coefficients and unary height; included explicit ECCC and Hexagon queries. The primary prior algorithm is Batubara–Garzella–Pan (2025), using Kawakami–Takamatsu–Yoshikawa's criterion already present in 2022. Their exact matrix, Delta and iteration statements were opened and are credited in the paper; hashes and page locators are in the source tables. The searches did not establish an earlier unary-height modular-complexity classification; that absence is not a priority conclusion. Results also identified a recent Newton-strata paper and derived-Morita-height preprint for further primary inspection, and a Hexagon invariant-derivation paper whose topic differs from the counting reduction. No uninspected result is a proof premise.

## 2026-11-25 06:46 UTC — primary recent follow-up

Opened Batubara–Garzella–Huang–Mellberg, Newton strata realization for hypersurfaces via explicit p-adic cohomology, Research in Number Theory12,Article110, published16November2026; read primary PDF pp1,3–5, especially Section1.5 and Theorem1.4. It supplies practical controlled-reduction implementations and explicit Newton-stratum examples, not a proof premise for our uniform complexity bounds. PDF SHA a2bc25cd161dd65baa25cb5823e20ae5b837383977651f4b9e29518af295ad23. The current arXiv page for2502.12428 confirms version3 and authors Batubara,Garzella,Pan; a differing author list in the recent article's reference10 does not replace the primary record. Matsumoto's2611.20424 abstract was found, but direct arXiv page/PDF retrieval failed; no theorem from it is invoked. Hexagon2611.00938v1 was opened; its invariant-derivative divisibility question is distinct from computing a hypersurface's height.

For the unresolved full-height hardness route, read KTY Example6.7 and Claims6.8–6.10 pp43–45. Their smooth characteristic-two construction has degree and variable count2^h+1 and height2h; it provides no polynomial-size encoding of a binary-time computation by itself. The smoothness mechanism uses a (b+c)g perturbation, forcing b=c at singular points. Its potential use in a computational embedding remains an unproved route.
