# Final-status audit: unopened references and actual dependencies

Audit by GPT-6 Astra, inherited effort, `crystalline_categories`, 20 November 2026, approximately 04:21–04:28 UTC.

## Conclusion and scope

**No settled statement was found whose operative cited theorem is supported only by an unopened source.** This is a dependency audit of the bibliography's uninspected-source qualifications against the paper's actual uses, with additional attention to I/J/L. It is not a fresh proof audit of all the mathematics or a claim to have reread every source in full.

The inspected aggregate bibliography has 99 entries and SHA256 `a9552d8973c8631676548bf48ac616d6c68b58bd2cc0396173da026f0c28e1a5`. The first extraction snapshot was taken at 04:21:13 UTC. The same hash was confirmed after the extended inspection. The master has `\nocite{*}`; an entry's appearance in the printed bibliography therefore does not establish a mathematical dependency. The scripts inspect all section files, including historical fragments that the master does not separately input; the actual integrated historical passages were checked in `geometry_H.tex` and `unresolved.tex`.

Two active statements use an opened later formulation of a theorem whose original publication was not opened. Both cases are expressly disclosed in the paper. The remaining qualifications concern unused leads, alternative translations, limited page-inspection scopes, or historical editions. None was silently promoted to a proof or a date for the Montpellier sheets.

## The two active original-source qualifications

### B.1: minimal Cohen factorization

`sections/algebra_B1.tex`, lines 3–43, labels SA23-B1-1 Known and derives the manuscript form from Nasseh–Sather-Wagstaff, *Cohen factorizations: Weak functoriality and applications*, arXiv:1205.2119v3, Definitions 2.3 and 2.5 and Fact 2.6(a). The source was already opened by the algebra agent and was independently reopened in this audit at `https://arxiv.org/pdf/1205.2119` (web reference `turn911883448view0`; retained raw output `notes/category_status_source_web01.json`).

The exact source distinguishes weakly regular maps, which have a regular closed fibre, from weakly Cohen maps, which additionally have separable residue extension: Definition 2.1, PDF p. 3, extracted lines 223–230. Definition 2.3, PDF pp. 3–4, lines 240–254, defines a Cohen factorization using the former condition and a complete intermediate ring. Definition 2.5 and Fact 2.6(a), PDF p. 4, lines 288–308, give minimality and existence when the target is complete. The separability hypothesis in Fact 2.6(c), lines 318–322, concerns a comparison assertion and is not imposed on existence.

The paper then obtains the exact degree-zero and degree-one associated-graded isomorphisms from the common residue field, minimal embedding dimension, regular closed fibre, and the opened flat-local dimension formula, Stacks Lemma 10.112.7. Thus the operative existence theorem is actually opened and its match to the requested form is explained. `algAvramovFoxbyHerzog1994` records the original attribution, not an independently inspected proof. This audit does not claim to reprove AFH's existence theorem.

### K(e): descent of abelian schemes

`sections/geometry_K.tex`, lines 213–230, first descends the proper flat finitely presented algebraic space and its group maps using the opened Stacks Lemma 99.13.3 (0D1G), then descends smoothness using Lemma 74.11.26 (0429). The geometric fibre conditions transfer across the cover. It invokes Robert, *Theory of abelian varieties and their moduli spaces*, Theorem 2.3.2, printed p. 12, to make the resulting abelian algebraic space a scheme.

The exact opened theorem is retained in `notes/geometry_web_abelian_stack_exact.json`, source `https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/books/avtheory.pdf`, extracted lines 758–767, PDF pp. 18–19. It states that an abelian algebraic space over the base is an abelian scheme. Its proof line refers to Faltings–Chai I, Theorem 1.9. The paper explicitly says that this older book page was not opened. `notes/category_status_source_Robert_support.json` retains the inspected exact context. The later source's actual theorem, rather than a search snippet or a catalogue title, is the operative cited statement. No original Faltings–Chai inspection or new proof of Raynaud's theorem is claimed.

## Bibliographic qualifications and their actual uses

Locators below refer to the audit snapshot; later editorial changes can move line numbers without changing the cited theorem.

| Entry or source | Qualification | Actual use and finding |
|---|---|---|
| `algLidskii1959` | 1965 English translation not opened. | The original Russian issue pp. 485–487 was opened. `geometry_H.tex:651` uses the directly inspected p. 487 discussion, footnote and references. No reliance on the unopened translation. |
| `algMetricResumeFacsimile` | Original issue cover/publication date uncollated. | The official facsimile and the relevant original-pagination pages were inspected. `geometry_H.tex:681` uses pp. 53–56 and note 8 bis, p. 77, for their mathematical content. Edition qualification remains explicit. |
| `algAvramovFoxbyHerzog1994` | Original full text not opened. | Active B.1 use is mediated by the opened exact NSW theorem and the written derivation above. |
| `catIllusie1972` | Original Chapter VIII not opened; errata only. | No citation in any section. L5 instead uses opened Beilinson–Drinfeld. |
| `catTate1967` | PDF access failed. | No citation in any section. J8 instead uses opened Ax 1970, main theorem p. 417 and proof §3, pp. 425–426. |
| `catKotheA201`, `catKotheI6` | Catalogue records opened; original letters/problem bundle not read. | No mathematical citation in the sections. These are bounded history routes, with no inference identifying or dating the target sheets. |
| `catSchnepsChapter4` | Career-change statements do not identify the manuscript. | Finding aid only; no active theorem citation. |
| `catBourbaki179`, `catBourbaki187` | Pencil author/date annotations not authenticated as to authorship or inscription time. | The originals were fully read; `unresolved.tex:78,84` reports bounded content comparisons and does not date cote 1. |
| `catBourbaki230` | Author/March 1956 attribution refers to an inscription in a different, uninspected ENS copy. | The relevant IECL Hilbert/Fredholm sections were directly read. `unresolved.tex:89` cites actual p. 219, where the general Hilbert result is an announcement. It does not identify the Montpellier leaves. |
| `geoGohbergKrein1965` | English translation unopened. | The relevant original Russian pages were opened. No mathematical dependency on the English edition, and no active section citation in this snapshot. |
| `Grothendieck1955Memoir` | First printing uncollated; fourth printing opened. | `geometry_H.tex:534,545` uses the actually inspected text and distinguishes its stated Hilbert inputs from proofs. The full modern trace reconstruction is separately proved from opened 1956 ingredients. No first-printing date for particular manuscript sheets is asserted. |
| `PalaisTerng1977` | Publisher scan unopened. | The original article text was opened in two OCR reproductions. `geometry_F.tex:330–339` derives the precise smooth theorem from Definition 0.1, Propositions 0.2, 0.5–0.6, Main Theorem 0.3 and §4.3. It does not infer the algebraic theorem's locality hypotheses from a title alone. |
| `rootHochster1973` | Original article unopened; author metadata opened. | `root_A4.tex:1–10` expressly separates attribution from the complete proof given in the paper. The cusp construction and the needed locus assertions do not rest on an unopened theorem. |
| `rootMatsumura1989` | Identified page not opened. | No active citation and explicitly not used as proof. |
| `rootGrothendieckThesisCatalogue1953` | Catalogue opened; original 130-folio thesis unopened. | `unresolved.tex:60–62` reports that exact limit and does not identify it with the target sheets. |
| `rootPaumierSchwartz2014` | Selected contexts read; not every page visually inspected. | `unresolved.tex:72` uses the actually read p. 64, note 73, as a finding aid. The referred Bourbaki draft was subsequently opened. |
| `algMontpellierArchiveMethod`, `rootSchwartzSeminarIntroduction1954` | Text does not identify the target leaves. | The sources themselves were opened. These qualifications bound historical inference; they do not denote missing theorem evidence. |

## I/J/L: match of operative theorems to opened locators

* **I6.** `category_I.tex:555–616` gives the model-theoretic construction of the relative classifier and its full 2-pullback universal property. The two external steps are exactly Makkai–Reyes Theorem 9.1.1 and Propositions 9.1.4–9.1.5, opened in the 2019 retypeset author text preserving theorem numbers. I1–I5 and I7–I12 are proved in the paper; no unopened Makkai–Paré or unread SGA 4 theorem is silently substituted for those proofs.
* **J5–J7.** The operative Fontaine locators are §6.2 for BT compatibility, §5.2 for the crystalline tensor category and comparison, §§3.6–3.7 and 3.10 for the Hodge–Tate comparison, and Proposition 1.6(iii) for faithfulness. Colmez–Fontaine Theorem A and §4.1 Theorem 4.3/corollary supply the weakly admissible replacement after setting N=0. Kisin Theorem (0.3) and Corollary (2.2.6) supply the weight-[0,1] isogeny statement. The opened introductions cover perfect residue fields; the paper's rational scope avoids claiming an unrestricted integral comparison at p=2.
* **J8–J9.** The finite S3 argument uses opened Ax, not the failed Tate PDF. The historical comparison uses the directly inspected ICM 1970 facsimile §5, pp. 434–435, especially Remarks 2–3, plus Colmez–Fontaine's explicit Introduction p. 3/reference [23]. It expressly distinguishes the actual BT category from the refuted literal all-Hodge–Tate category.
* **L5–L8.** The operative source is the opened Beilinson–Drinfeld author Chapter 1, §1.4.14(ii), §1.4.15 Proposition/construction and coefficient exercise, printed pp. 41–45. The paper derives the extra groupoid and symmetric-graded hypotheses in L3–L4 and retains the pro-algebra convention. The subsequent finite-order contraction, derived-completion and crystal comparisons are given as proofs. Neither unopened Illusie nor an unproved exactness assertion for ordinary sheaf inverse limits is an operative substitute.

These comparisons use the exact source record in `notes/category_source_search_log.md` and the actual current section text. They do not create additional independent proof checks of arguments already audited.

## Preserved audit material and limits

* `code/category_status_source_audit_extract.py`, its log, and `notes/category_status_source_audit_extract.json`: first 99-entry snapshot and ten explicit unopened/uncollated hits.
* `code/category_status_source_extended_extract.py` and its log: an overbroad first finding aid, retained. Its unbounded `not` pattern also matched the word `note`, and substring key matching could include longer citation keys. No mathematical conclusion rests on its hit count.
* `code/category_status_source_extended_extract_v2.py`, log and JSON: corrected word boundaries and exact citation-key extraction; twenty documentary qualification hits, manually classified above.
* `code/category_status_source_support_extract.py`, log and `notes/category_status_source_Robert_support.json`: retained exact Robert theorem context from the earlier raw retrieval.
* `notes/category_status_source_web01.json`: newly reopened NSW source.

The conclusion is scoped to the inspected source qualifications and actual dependencies. It does not authenticate unread editions or annotations, turn metadata into an original reading, reopen every source, or settle the still-unproved date of the particular Montpellier sheets. No section or master file was changed by this audit.

## Checkpoint 06 bibliography delta, 04:35 UTC

The later completed checkpoint build has **103 entries**, bibliography SHA256 `62dd216afe44e6629eed8e98dd7803a397cafbf12af8fbc051e45008e29c22a0`. The four added keys were compared with the earlier 99-key snapshot by `code/category_status_source_checkpoint06_delta.py`; output and exact added entries are preserved in its log and `notes/category_status_source_checkpoint06_delta.json`.

* `algCartier211` is an opened complete fourteen-page facsimile, with its first-printing qualification explicit. It has no active section citation in this snapshot.
* `algGrothendieckCR1951Tensor` is an opened three-page original facsimile. The new `geometry_H.tex` paragraph uses p. 1557 for the printed announcement and explicitly says the proof is not supplied there. It uses the presentation date actually recorded on the first page and makes no date transfer to the Montpellier leaves.
* `geoBourbakiTribu39` and `geoBourbakiTribu40` have opened complete main fascicles and explicitly unread appendices. `unresolved.tex` confines its inference to dated report-identifier circulation, matching the completed original-reading record in `notes/geometry_bourbaki_congress_date_audit.md`; no exact-copy collation or trace-sheet identification is asserted.

These additions introduce no unopened-only theorem dependency or change to the source-audit conclusion. This addendum checks the actual uses and source-status records; it does not claim a new independent original-page reading of these four sources.
