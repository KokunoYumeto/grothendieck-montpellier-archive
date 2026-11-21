# Grothendieck archive: original-scan locator audit

Run: HECKE_DIV_20261121. Agent: /root/reductions. Model: GPT-6 Astra Pro. Reasoning effort: not exposed. Date: 21 November 2026 (UTC).

## Finding

The official original scan of Montpellier **cote 16** has been retrieved and visually inspected for the requested passages. The sketch's PDF-page pointers are substantially accurate, but its attribution of all of PDF pages 44–50 to the letter of 4 January 1967 conflates **two separate letters**. PDF page 48 begins a second letter whose handwritten date reads **6.1.1966**. The CSG transcriptions agree with this reading; no original-versus-CSG transcription error is established.

The PDF contains 56 pages. On every inspected content page its printed archive folio is **one less than the one-based PDF page number**. The sketch's “scan 44”, “scan 45”, etc. align with PDF page numbers, not the printed archive folios. A reference should give both.

## Retrieval and authenticity record

The official catalogue is <https://grothendieck.umontpellier.fr/archives-grothendieck/>. It identifies cote 16 as a dossier dated 1966–1967, of 55 content pages, concerning algebraic correspondences and Poincaré–Hodge algebras. Its warning that reverse sides may contain unrelated material makes precise page attribution important.

The catalogue's original HTML was downloaded and inspected, rather than inferring a PDF identifier from the desired content. Its cote-16 entry contains `data-src="../web/viewer.html?file=../16.pdf"`, identifying the official PDF:

<https://grothendieck.umontpellier.fr/16.pdf>

HTTP HEAD returned 200, Content-Length 21774525, and Last-Modified 11 May 2017. Two downloads, one whole-file and one assembled from HTTP byte ranges, have identical SHA-256:

`a03bc009230a8742f58d1e9252305c65db10a8df1a1272c9211636f78f1de1ca`

The PDF is unencrypted, has 56 A4 pages, and reports a creation/modification date of 11 May 2017. Local research copies are `work/grothendieck_cote16.pdf` and `work/grothendieck_cote16_ranges.pdf`. These are original PDF bytes, not an OCR reconstruction or an edited edition. Original scans were rendered for reading with Poppler at 95 dpi; PDF pages 14, 15, 17, and 18 were additionally rendered at 145 dpi. No textual alteration was made to the research PDF.

## Exact locators and observations

| Material | One-based PDF page(s) | Printed archive folio(s) | Visual observation and scope |
|---|---:|---:|---|
| Universal integral Lefschetz ring, §7, opening construction | 14 | 13 | The manuscript starts with a free rank-2n integral module and an alternating form nondegenerate over the integers. The parenthesis “(sur Z !)” is visible. It defines the exterior algebra, exterior multiplication by the form, contraction by the inverse form, and the subring Φ₀=Z[L₀,Λ₀] of integral endomorphisms. |
| Continuation of §7: generators, relations, universal property and discussion | 15–17 | 14–16 | These handwritten pages continue the ring construction. They were visually read; several heavily revised lines remain difficult to decipher. This audit does not supply a diplomatic transcription of those lines. |
| §8, Lefschetz terminology | 18 | 17 | The manuscript introduces a graded algebra with a distinguished Lefschetz operator. In the edited terminology near the upper third, the phrase “anneau de correspondances” and the designation “Lefschetzien” are visible. Because of overwriting, do not present a longer verbatim sentence as a verified transcription. |
| First Coates letter, opening and date | 44 | 43 | A new typewritten letter begins. The handwritten date at the upper right is 4.1.67. The opening discusses the index conjecture and its relation to A and B. |
| First Coates letter, critical-degree equivalences | 45 | 44 | The displayed proposition lists formulations equivalent to C(X), including C(Y) together with the A-condition on X×X in the critical degree H^{2n−2}→H^{2n+2}. |
| First Coates letter, proof and qualifications | 46–47 | 45–46 | The proof continues and records limits of known results and an abandoned attempted reduction. The first letter ends on PDF page 47. |
| Second Coates letter, opening and date | 48 | 47 | A distinct letter begins. The handwritten date reads 6.1.1966. It discusses algebraic isomorphisms and the use of Cayley–Hamilton to obtain an algebraic inverse. This is the date as written; the audit does not silently emend it to 1967. |
| Second Coates letter, semisimplicity | 49 | 48 | Near the bottom, C(X) together with the index relation I(X×X) is said to imply semisimplicity of the ring of correspondence classes, with left and right inverses as a consequence. |
| Second Coates letter, Weil conjectures and A′, A″ | 50 | 49 | The top continues the proposed deduction of the Weil conjectures from C and A. The remainder introduces weaker Lefschetz-type variants and their relation to full statements. The letter closes here. |

Useful direct links: [integral ring construction](https://grothendieck.umontpellier.fr/16.pdf#page=14), [first letter](https://grothendieck.umontpellier.fr/16.pdf#page=44), [critical degree](https://grothendieck.umontpellier.fr/16.pdf#page=45), [second letter and manuscript date](https://grothendieck.umontpellier.fr/16.pdf#page=48), [semisimplicity](https://grothendieck.umontpellier.fr/16.pdf#page=49), [Weil-conjecture passage](https://grothendieck.umontpellier.fr/16.pdf#page=50).

## Comparison with the CSG transcriptions

1. **Grothendieck, A. (1967, January 4). Letter to J. Coates.** Montpellier, Archives Grothendieck, cote 16, printed folios 43–46 (= PDF pages 44–47). CSG draft transcription edited by M. Carmona (April 2024): <https://csg.igrothendieck.org/wp-content/uploads/2024/04/L10d.pdf>. Its actual transcription has printed pages 1–4. The bibliographical page identifies Montpellier cote 16. Its treatment of the opening and critical-degree statements agrees with the inspected original at the level used here.
2. **Grothendieck, A. (1966, January 6, as dated in the manuscript). Letter to J. Coates.** Montpellier, Archives Grothendieck, cote 16, printed folios 47–49 (= PDF pages 48–50). CSG draft transcription: <https://csg.igrothendieck.org/wp-content/uploads/2024/04/L11d.pdf>. Its printed pages 1–3 contain the algebraic-inverse, semisimplicity, and Weil-conjecture discussion. The manuscript's visible year agrees with the CSG heading. Whether the date itself is an authorial chronological slip is not settled by this audit and is not necessary to identify the letter.
3. CSG correspondence catalogue: <https://csg.igrothendieck.org/correspondence/> separately lists these two letters under cote 16.

These comparisons are targeted source readings, not complete line-by-line collations of either letter. No claim is made to have corrected the CSG transcription.

## Consequences for the bounded-division paper

The integral construction at §7 is abstract linear algebra on an integral exterior algebra. Identifying it with the cohomology of a principally polarized complex abelian variety is an interpretation compatible with that construction; the original page does not assert the existence of bounded effective cycles. The Coates passages concern algebraicity of operators, inverse correspondences, positivity and semisimplicity. They supply historical structural context, not a uniform degree or denominator estimate for the cycles in HECKE_DIV.

The precise correction to the sketch is therefore bibliographical: split its 44–50 range into 44–47 and 48–50, preserve the second date as written, and distinguish PDF pages from printed folios. The audited pages do not justify silently replacing rational algebraicity by an effective uniform bound.

## Check events

- 2026-11-21, GPT-6 Astra Pro, effort not exposed, agent /root/reductions: **used and rechecked in this run** — official catalogue and original HTML inspected; exact original PDF locator recovered.
- 2026-11-21, same checker: **targeted source check** — original PDF pages 14–18 and 44–50 visually inspected; formula, dates, page boundaries, semisimplicity and critical-degree locators checked.
- 2026-11-21, same checker: **independent source comparison** — L10d and L11d compared with the corresponding original scan passages. Two-letter conflation in the sketch confirmed. No full diplomatic transcription or complete proof audit of the archival texts claimed.
