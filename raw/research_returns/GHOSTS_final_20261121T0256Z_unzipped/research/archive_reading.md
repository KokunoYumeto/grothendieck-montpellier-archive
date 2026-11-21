# Direct archive image reading and comparison with the standard conjectures

Source readers: root and an independent follow-up by GPT-6 Astra Pro, inherited reasoning effort not separately exposed, run `/root/cm_transport`, 21 November 2026. These are image readings and scope checks, not a fresh proof of every assertion in the correspondence.

Public catalog: https://grothendieck.umontpellier.fr/archives-grothendieck/ . The actual PDFs are https://grothendieck.umontpellier.fr/14.pdf and https://grothendieck.umontpellier.fr/16.pdf . PDF scans below are one-based and include the cover; the archive folio is one less. The cited images, rather than their largely empty text extraction, were inspected.

## Cote 14

| PDF scan | Archive folio | Reading and precise scope |
|---|---:|---|
| 9 | 8 | Handwritten cone/effectivity discussion, including the notation Eff(G) and a map into it. The page does not provide a quantitative degree bound or an effective-cycle lifting theorem usable here. We do not silently identify an abstract effective-motive cone with the cone of effective cycles of one fixed degree. |
| 38–39 | 37–38 | Section3, on l-adic homomorphisms associated with an abelian family of cycles. Theorem3.1 compares the cycle-induced map u_Z with an l-adic map a(Z); the statement is accompanied by a question mark and a marginal caution about the converse. The next page reduces along an ample curve in the parameter abelian variety and discusses the middle Kunneth component. We do not extract an unqualified certified biconditional from these annotations. |
| 44 | 43 | Beginning of the Serre letter dated27 August1965. C^i(X) is explicitly cycles of codimension i modulo algebraic equivalence, tensored with Q. Its Conjecture A asks for a Lefschetz isomorphism on these groups. This is stronger in equivalence level than a statement only about cohomology classes of cycles. |
| 45 | 44 | The hyperplane variant A', a distinction between algebraic-equivalence and homological reformulations, and a correction to an earlier claim of equivalence with Kunneth. The primitive positivity assertion B, for n=2m, has the explicit factor (-1)^m in E(xx'). Its discussion of consequences for equivalence relations must retain that hypothesis and the letter's definition of C^i. |
| 46 | 45 | Conditional semisimplicity and correspondence-image assertions from the Lefschetz and positivity package; an affine complement variant A''. These statements do not supply numerical degrees for algebraic inverse correspondences. |
| 47 | 46 | Further conjectural comparisons of homological and tau/algebraic equivalence, and the proposal to deform lower-dimensional cycles toward infinity. This is not an unconditional proof that effective special-fiber cycles lift effectively. |

The distinction matters for the present research. Our complexity is measured using the cohomological equality of signed integral cycles. B01–B06 concern finite parameter spaces for such equalities and specialization. The archive's stronger assertions concerning algebraic equivalence cannot be inferred from those results. The letters' labels A and B are local notation; our comparison uses the written mathematical condition rather than assuming a universal lettering convention.

## Cote 16: two separate Coates letters

The initial local memo grouped scans44–50 as one letter of4 January1967. That grouping was inaccurate. A fresh image reading shows:

* Scans44–47, folios43–46: the letter dated **4.1.67**.
* Scans48–50, folios47–49: a new salutation, “Dear Coates,” and a handwritten date reading **6.1.1966**. The enlarged date region was inspected. We report this date as written; we do not silently alter its last digit or infer another year from the ordering of the archive.

### Letter dated4 January1967, scans44–47

Scan44 couples Lefschetz-type algebraicity with the index conjecture and writes an implication of the form A + index implies B. It explains that, in characteristic zero, Betti cohomology supplies independence of the chosen l; it expressly cautions about what was not yet established in positive characteristic. Scans45–46 formulate and prove equivalences involving products with X and a hyperplane section Y, and algebraic left or right inverses to the relevant restriction or Gysin maps. The proof uses transpose correspondences and Lefschetz operators. Scans46–47 discuss known low-dimensional cases and the outstanding threefold/one-cycle difficulty.

The local condition called C_l in these pages concerns algebraicity of Lefschetz inverse-type correspondences; it must not automatically be read as the modern shorthand “C = algebraic Kunneth projectors.” A complete dictionary for every letter is unnecessary for our application, and is not asserted without its original definitions.

### Letter whose date reads6 January1966, scans48–50

Scan48 states equivalent criteria involving an algebraic isomorphism H^(2n-i)(X) -> H^i(X) and rational characteristic-polynomial coefficients for algebraic endomorphisms. The proof composes the chosen isomorphism u with the algebraic Lefschetz isomorphism v. For w=uv, Cayley-Hamilton expresses w^(-1) as a rational polynomial in w, because the constant coefficient is nonzero. It follows that v^(-1)=w^(-1)u is algebraic.

Scan49 applies the same method to an algebraic cohomological isomorphism between varieties satisfying the stated condition. Algebraic identifications with their duals make an adjoint algebraic; composing with it reduces the inverse assertion to an algebraic automorphism and the same characteristic-polynomial calculation. The page then distinguishes a general monomorphism: its desired algebraic left inverse requires more, and the text explicitly invokes the Hodge index relation to obtain the splittings and semisimplicity of correspondence algebras. Scan50 records weak-Lefschetz variants and their implications for the full relations.

These arguments establish qualitative algebraicity of inverse correspondences under their hypotheses. They neither assert that the inverse preserves the effective cone nor bound its rational coefficients, a denominator clearing those coefficients, or the degree of its cycle representative. Thus they do not by themselves close the quantitative T5 or T9 gate. Our explicit projector, translated-intersection, and isogeny calculations supply the separate numerical information where claimed.

## Source-correction boundary

The corrected grouping/date is an amendment to our own source metadata, not a mathematical correction forced on a user-provided transcription. No earlier user text of record was available for a line-by-line transcription comparison. `TRANSCRIPTION_NOTES.tsv` remains header-only. The metadata correction is recorded separately in `sources_audit/SOURCE_CORRECTIONS.md`; the unsigned primitive pairing in Milne's report is a distinct mathematical source finding with its own proof in `research/milne_sign_correction.md`.

## Actual independent check event

On21 November2026, `/root/cm_transport` visually inspected cote14 scans9,38–39,44–47 and cote16 scans44–50, and enlarged the date on cote16 scan48. Outcome: exact scan/folio mapping confirmed; the two-letter separation and written date corrected; algebraic-equivalence and index/splitting scopes retained; no new assertion of the archive conjectures, and no certified handwritten biconditional claimed.
