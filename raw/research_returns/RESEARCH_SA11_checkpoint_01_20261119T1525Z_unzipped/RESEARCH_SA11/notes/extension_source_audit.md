# Extension-space branch: source and proof audit

Date: 19 November 2026. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. A source marked opened was actually opened in full-text form; the locators below identify what was checked, not a claim that every line of the source was independently verified.

## Sources opened and used

### Sturmfels and Ziegler (1993)

**APA:** Sturmfels, B., & Ziegler, G. M. (1993). Extension spaces of oriented matroids. *Discrete & Computational Geometry, 10*, 23–45. https://doi.org/10.1007/BF02573961

**Status:** Opened, complete published PDF and author preprint. The published version supplies the page locators used in the paper. URL: https://link.springer.com/content/pdf/10.1007/BF02573961.pdf. Author preprint: https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/020PREPRINT.pdf. Local files: `sources/extension_SZ1993_published.pdf`, its text extraction, and `sources/extension_SZ1993_preprint.pdf` with extraction. Published PDF SHA256: `8c2a94707acb7ae4cc44fa427d22221c31ea4add988ae57e4e6ed30826321560`. Fetch metadata, hashes, and runtimes are in `audit/extension_fetch_sources_output.json`.

Checked locators:

- Theorem 1.2, p. 25: sphere conclusion for the stated Euclidean class; Corollary 4.5, p. 40, supplies every rank-three matroid in this task.
- Theorem 2.3, p. 28: the extension poset for a realizable rank-r matroid is the Baues poset for the specified n-cube projection to a dimension n−r zonotope. This does not identify the local nu-cubes with that global n-cube and does not state the manuscript's cyclic selector.
- Lemma 3.2, p. 29: Babson's point-fiber and upward-slice criterion. E3 and E4 explicitly verify that restriction to any full inverse-image subposet retains those fibers and slices.
- Partially directed program graph and directed-path convention, pp. 30–31; Definition 3.8(i) and Proposition 3.9, p. 33: Euclidean programs have no directed cycle in the stated sense. Corollary 3.12, p. 35, gives the associated contractibility. T1 uses strict edges inside its lune.
- Lemma 4.1, p. 37: proper upper interval of a parallel extension is the contraction extension poset.
- Proposition 4.2, pp. 37–38: the explicit contraction map to the suspension poset and its fiber proof.
- Corollary 4.5, p. 40: rank at most three is strongly Euclidean.

The action used here reorients only the new labelled element. It does not divide by old-element reorientation or permutation. E1 proves equivariance of the actual map and derives its projective quotient; E4 gives the additional marked argument needed before puncturing. Neither quotient nor puncturing is inferred from an arbitrary unmarked sphere equivalence.

### Mnëv and Richter-Gebert (1993)

**APA:** Mnëv, N. E., & Richter-Gebert, J. (1993). Two constructions of oriented matroids with disconnected extension space. *Discrete & Computational Geometry, 10*, 271–285. https://doi.org/10.1007/BF02573981

**Status:** Opened, complete published PDF. URL: https://link.springer.com/content/pdf/10.1007/BF02573981.pdf. Local PDF/text: `sources/extension_MRG1993.*`. SHA256: `307f5d3073e5ccbe94bf9e1240c7fd5d62848dfc099cd0a0313572b7b3f1b619`.

Checked introduction and Section 1, pp. 271–273, and the ranks of the stated constructions. Their disconnected examples have rank four. The introduction explicitly contrasts this with the rank-three sphere result. The paper is used for scope, not to limit E1–E4.

### Billera, Kapranov, and Sturmfels (1994)

**APA:** Billera, L. J., Kapranov, M. M., & Sturmfels, B. (1994). Cellular strings on polytopes. *Proceedings of the American Mathematical Society, 122*(2), 549–555. https://doi.org/10.1090/S0002-9939-1994-1205482-0

**Status:** Opened, complete published scan in the UC Davis mathematics archive. URL: https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Billera/BilleraKapranovSturmfels.pdf. Local PDF: `sources/extension_BKS1994.pdf`; full OCR: `sources/extension_BKS1994_ocr.txt`; all page renders and OCR files retained in `audit/extension_BKS_render/`. SHA256: `135fb07c11b7ef45e7658ae1b40833c7d6902fba8e7c53f3fbe6d397aaa59440`. Initial AMS and JSTOR PDF routes were blocked, but this was resolved by opening the published scan. It is not an unopened citation.

Checked Theorem 1.2, p. 550 (also visually inspected); Proposition 2.1 and Theorem 2.3, p. 552 (also visually inspected); coherent strings and the monotone-path-polytope boundary, p. 553; generalized Baues problem and scope, pp. 554–555. The generic-functional theorem gives the appropriate sphere for cellular strings. The higher-dimensional projection is posed as a generalized problem, not solved universally here. No theorem in the paper identifies the cyclic port rule of E6 with coherence.

### Goodman and Pollack (1980)

**APA:** Goodman, J. E., & Pollack, R. (1980). On the combinatorial classification of nondegenerate configurations in the plane. *Journal of Combinatorial Theory, Series A, 29*(2), 220–235. https://doi.org/10.1016/0097-3165(80)90011-4

**Status:** Opened, complete published two-up scan. URL: https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/PollackRichard/Pollack5.pdf. Local PDF: `sources/extension_Pollack5.pdf`; full OCR: `sources/extension_GP1980_ocr.txt`; renders and page OCR retained. SHA256: `e46c8b421e4cedcca61daa85075e1b2ca32531eafc189c173bb11c5dfb6b103c`.

Checked Definition 2.1, p. 222; Remark 2.3 and Definition 2.4, p. 223 (visually checked against scan); Proposition 2.6, p. 224. These define simple allowable circular sequences through adjacent switches and a complete set of pair switches per half-period, and recover the sequence from its ordered switches. Their stated nondegeneracy assumptions are retained; this source is not silently applied to multiple-intersection packets.

### Felsner and Goodman (2017 author chapter)

**APA for the version actually opened:** Felsner, S., & Goodman, J. E. (2017, July 16). *Pseudoline arrangements* [Author version of Chapter 5, pp. 125–157, for the third edition of the Handbook of Discrete and Computational Geometry]. https://www.csun.edu/~ctoth/Handbook/chap5.pdf

**Status:** Opened, complete 33-page author chapter at the URL above. Checked Theorem 5.1.4, p. 127 (wiring representation); Theorem 5.2.6, p. 132 (allowable-sequence realizations); wiring construction, pp. 132–133; and Theorem 5.5.10, p. 146 (isotopy to a wiring diagram). This is an explicit source for terminology and the scope of general wiring statements. It attributes the original results to Goodman and to Goodman–Pollack. The surface proof itself instead uses the directly opened Sturmfels–Ziegler program theorem, so no mathematical dependency passes through an unavailable original.

## Sources not opened in full; no theorem imported from them

- Goodman, J. E. (1980). Proof of a conjecture of Burr, Grünbaum, and Sloane. *Discrete Mathematics, 32*(1), 27–35. DOI `10.1016/0012-365X(80)90096-5`. Publisher abstract and metadata retrieved; article/PDF routes returned access errors. **Not opened in full.** No theorem is cited from this unopened paper as a proof dependency.
- Goodman, J. E., & Pollack, R. (1984). Semispaces of configurations, cell complexes of arrangements. *Journal of Combinatorial Theory, Series A, 37*(3), 257–293. DOI `10.1016/0097-3165(84)90050-5`. Metadata and citations located. **Not opened in full.** General wiring statements were checked in the opened coauthor handbook instead.
- Goodman, J. E., & Pollack, R. (1993). Allowable sequences and order types in discrete and computational geometry. In J. Pach (Ed.), *New trends in discrete and computational geometry* (pp. 103–134). Springer. DOI `10.1007/978-3-642-58043-7_6`. Publisher chapter/abstract/reference page opened; the full-PDF route redirected to subscription preview. DIMACS TR 92-1 listing has no downloadable report link. **Not opened in full.** No mathematical dependency uses it.

Several anonymous university-archive filenames were downloaded and their title pages opened solely to identify them. `extension_Pollack8` concerns affine Grassmann convexity; `extension_Pollack9` and `extension_Pollack7` concern semialgebraic Betti/cell bounds; `extension_Goodman1`–`extension_Goodman3` are Chaim Goodman-Strauss tiling papers; `extension_Goodman4` concerns polygon equidissections. They are excluded as irrelevant. Their title-page OCR, downloads, checksums, and retrieval program output are retained to document the search. They are not mathematical sources for this result.

The *Oriented Matroids* book and Las Vergnas source were assigned to the polygons branch; their exact open status and locators are recorded there, not asserted by this branch.

## Search coverage and limits

Searches used the exact titles and authors of the required sources; the phrases `extension space parallel extensions punctured`, `oriented matroids extension space Möbius`, `Goodman Pollack wiring diagram theorem original paper pdf`, `Proof of a conjecture of Burr pdf`, `Semispaces of configurations filetype:pdf`, and `Allowable Sequences and Order Types pdf`; author and publisher sites; the UC Davis bibliography archive; and the DIMACS technical-report listing. Both available search engines were used for primary-source discovery and verification. No arXiv LaTeX source was located for the 1993/1994 papers; publisher or author PDFs were used.

Within the opened classical sources we found no statement of the fixed-vertex identity E3, the marked puncture comparison E4, or the precise cyclic selector and relative-cell formula E6. In particular neither the rank-three sphere theorem nor the coherent-cell theorem states the manuscript selector. This records the actual search coverage; it is not a claim that no prior statement exists. Complete proofs are supplied and no priority is claimed.

## Independent finite checks retained

`code/extension_compare_cells.py` reads the complete finite certificates for the five simple bases with n=3,4,5,6,6. It reconstructs all 3^nu principal refinement intervals; verifies the fixed-vertex alternating sums; reconstructs ordinary cover edges and all possible incidence diamonds; reconstructs every rank-two parallel boundary circle, its antipodal fiber edges, and its flag rectangles; and compares all these with the computed gluing. It also supplies the eight explicit stable descendants of the six-line added point `(0,0,1)`.

The check ran in 0.035359 seconds. Its complete output is `audit/extension_compare_cells_output.json`, with console output retained as `audit/extension_compare_cells_run.txt`. It is a finite independent comparison, not a substitute for the general proofs. In the six-line test with c=(80,150,75,10), B has cell counts (315,720,480,80), while the embedded dual surface selects 300 of 420 ordinary diamonds and adds all 60 band rectangles. The relative CW structure has 120 additional squares and 80 cubes, accounting for the Euler-characteristic difference 40. In the three examples with n<=5 there are no omitted cells.

`code/extension_ocr_bks.py` rendered and OCRed the full eight-page scan in 55.804 seconds. `code/extension_ocr_goodman_pollack.py` rendered and OCRed the eight two-up pages in 63.941 seconds. Source-fetch programs and their per-file runtimes/checksums are retained under the matching `code/extension_*` and `audit/extension_*` names. No computation claimed in this audit was merely planned.
