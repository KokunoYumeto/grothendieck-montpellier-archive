# Public archive follow-up for suggestion 9

Agent: `/root/archive_binomial`; model: GPT-6 Astra Pro, inherited; reasoning effort: not exposed by the runtime. Date: 2026-11-21 UTC. This is a bounded source-recovery and visual-reading task, not a full transcription or a proof audit of these manuscripts.

## Result

The four cotes mentioned in suggestion 9 are publicly cataloged, and selected pages were successfully recovered from the official University of Montpellier PDFs. Two precise substantive locators now replace the earlier blanket statement that only unattached cote numbers were known:

- **ABA-PUB1: cote 153, official PDF page 3, archive/manuscript label 2:** binomial polynomials, their integral product and composition laws, and the associated operations.
- **ABA-PUB2: cote 136, official PDF pages 4--6, archive labels 3--5:** rational homotopy and its loss of torsion; the integration-denominator obstruction over the integers; and a divided-power de Rham construction that needs a coefficient ring with specified divided-power data.

These readings strengthen the historical mapping to DP11--DP14 and the divided-power discussion. They do not supply a stated theorem transferring binomial homotopy reconstruction to the local derivative/multiplicity estimate. The supplied Fable text itself explicitly leaves this as an undeveloped proposal: `FABLE_PROGRAM_SUGGESTIONS_20261120.md`, lines 131--135; the explained version, lines 307--314. Neither the absence of a precise B7 statement in those supplied texts nor the absence of a proved comparison is cured merely by locating the manuscripts.

## Official catalog and chronology

The [official catalog](https://grothendieck.umontpellier.fr/archives-grothendieck/) was read through the web retrieval tool and its public HTML. Its actual `data-src` attributes link to the four PDF URLs below. The entries have the following scope:

| Cote and official source | Catalog date | Catalog scope, paraphrased | Archive pages / PDF pages |
|---|---|---|---|
| [133](https://grothendieck.umontpellier.fr/133.pdf) | 1974 onward, with material from at least 1975 | Witt groups, quadratic forms and formal groups | 53 / 54 |
| [136](https://grothendieck.umontpellier.fr/136.pdf) | From about 1975--1976 | Divided-power de Rham complex; the 1976 IHES lecture | 375 / 376 |
| [137](https://grothendieck.umontpellier.fr/137.pdf) | About 1975--1976 | Devissage of half-simplicial complexes and multiplicative structures | 85 / 86 |
| [153](https://grothendieck.umontpellier.fr/153.pdf) | From 1982 | Analyseurs | 10 / 11 |

In particular, the four entries must not all be dated to 1976. The counts on the right were checked against the actual linearized PDF headers. The inspected pages have an added PDF cover and printed archive labels one less than the PDF page index. This observation is local to these public PDF files. It must not be substituted for the names of the separately supplied scan transcriptions, whose numbering the parent checked independently for cotes 47 and 54.

## ABA-PUB1: exact binomial/operations page in cote 153

**Official PDF page 2, printed archive and manuscript label 1.** Composition `F o G`, associativity, unit `T`, and operations involving `W(Omega_0)` and `W(A)` are visible. The thematic reading was independently confirmed by `/root/step2_higher`.

**Official PDF page 3, printed archive and manuscript label 2.** The upper right defines

`F_n(T) = T(T-1)...(T-n+1)/n!`.

It displays product and composition expansions in this basis, explicitly indicates integer product coefficients, and places their Z-span inside `Q[T]`; formulas for sum/product operations follow. This is an exact numerical-polynomial and plethystic locator. It does not supply a historical proof of Horel's theorem or of the proposed multiplicity comparison.

Both pages were recovered as complete one-page extractions from verified original HTTP ranges and rendered without Poppler errors. The relevant files are `archive_public/cote153_pdfpages_2.pdf`, `archive_public/cote153_pdfpages_3.pdf` and the corresponding `cote153_pdfpage002.png`, `cote153_pdfpage003.png`.

## ABA-PUB2: precise divided-power motivation and extra data in cote 136

| PDF / archive / author page | Visible source content |
|---|---|
| 2 / 1 / folder | Divided-power de Rham subject. |
| 3 / 2 / circled 1 | IHES 1976 historical plan, including crystals and Sullivan. |
| 4 / 3 / circled 2 | Rational models and rationalized homotopy groups; loss of torsion. |
| 5 / 4 / circled 3 | Integration denominators; proposed divided-power remedy. |
| 6 / 5 / circled 4 | `1-sum X_i` is outside the PD ideal. Introduces `S`, a distinguished `t` in its PD ideal, and a de Rham quotient using `sum X_i=t`, `sum dX_i=0`. |

This identifies necessary extra data, not a complete comparison theorem or a PD structure on the formal-disc ring of DP1. Later pages were not audited.

The five viewed PDF pages 2--6 have complete selected-page PDFs and PNGs in `archive_public/`. Mathematical formulas on the later pages are faint in places; the source conclusion here is limited to the visible constructions and obstacles above, not a diplomatic transcription of every term.

## ABA-PUB3: narrower findings and limits for cotes 133 and 137

**Cote 133:** PDF pages 3--5 (archive labels 2--4) were visually inspected. Page 3 contains associativity-type tensor diagrams. Page 4 contains characteristic-class/quadratic-form expressions and a separate homological calculation; page 5 is extremely faint and supplies no reliable mathematical statement in this reading. These opening pages do not furnish an exact plethysm theorem locator. The catalog-level mapping is established; the specific plethysm/lambda-operation passage alluded to in the supplied Fable explanation has not been identified in this bounded search. This is not a claim that the passage does not exist elsewhere in the 53-page dossier.

**Cote 137:** PDF page 3 (archive label 2) is a typescript leaf headed Appendix H (Hirsch Method), with its own printed page number 112. It concerns rational de Rham models and Postnikov constructions. Its placement in Grothendieck's dossier does not establish his authorship of that typescript, and it must not be cited as a newly located autograph theorem. PDF page 4 (archive label 3) is a very faint handwritten complex calculation; the exact theorem statement could not be read confidently. The catalog establishes the dossier's topic, but no exact B7 theorem was recovered here. A request for PDF page 5 could not be completed from already cached source bytes, and no further network retrieval was attempted after access errors.

## Recommended main-paper replacement

The former statement that these cotes were absent from the supplied files can remain as an input-provenance statement, but should be followed by the successful public recovery. A concise accurate paragraph is:

> The cotes mentioned in suggestion 9 were not included among the supplied transcriptions. A targeted public-archive check now locates the binomial polynomials and their product/composition operations in cote 153, PDF p. 3 (archive p. 2), and the passage from rational Sullivan models through the integration-denominator obstruction to additional divided-power base data in cote 136, PDF pp. 4--6 (archive pp. 3--5). These pages clarify the historical motivation. The supplied proposal still gives no precise B7 comparison statement, and the recovered pages do not establish a transfer to the multiplicity estimate. The specific plethysm passage in cote 133 and an exact relevant theorem in cote 137 remain unlocated in this bounded inspection.

This is source attribution and scope clarification; it is not a new theorem or a stronger impossibility claim.

## Retrieval and check limits

The public HTML and linearized PDF headers were retrieved successfully. The web parser could not open the PDFs, but direct HTTP GET and range requests returned original PDF bytes. Full-file downloads were unnecessarily slow for the large cotes. An initial PDF-library accessor traversed more of the page tree than needed; later requests returned HTTP 503/403, at which point further network requests were stopped. A corrected page-tree descent subsequently extracted the selected pages **offline**, using only already cached original bytes and exact cross-reference offsets. All selected-page PDFs cited above reopen under strict pypdf and render without Poppler errors. No missing scan content was reconstructed or invented.

Only the twelve pages expressly listed above were visually read: cote 133 PDF pp. 3--5; cote 136 pp. 2--6; cote 137 pp. 3--4; cote 153 pp. 2--3. The rest of those dossiers were not audited. Original-byte caches and the extraction helper are intermediate retrieval evidence, not complete downloadable copies of all four dossiers. An initial partial full-file download and sparse placeholder are not source deliverables and are removed after the complete selected-page extractions are checked.
