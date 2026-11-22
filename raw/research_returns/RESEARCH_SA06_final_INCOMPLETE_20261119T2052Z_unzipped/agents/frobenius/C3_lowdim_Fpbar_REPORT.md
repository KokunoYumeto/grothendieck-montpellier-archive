# C.3bd: isolated surface and threefold germs over an algebraic closure of a finite field

## Final statement and scope

The final proof is `C3_lowdim_Fpbar_top.tex`. Let R be the strict henselization at a closed Fpbar-point of a normal local ring essentially of finite type over Fpbar. If 2 <= dim R <= 3 and the punctured spectrum X is regular, then CH^(dim R - 1)(X) with rational coefficients is zero. Consequently its ordinary quotient by algebraic equivalence is zero. The puncture condition is automatic in dimension two and remains an explicit hypothesis in dimension three. Every positive characteristic is included.

This is a restricted corollary of C.3bc. It does not assert resolution in higher dimension, integral torsion bounds, vanishing over transcendental extensions of Fpbar, or vanishing for a threefold germ with a singular puncture. It is not recorded as a reset of the main research gate. We make no priority claim.

## Exact construction

We first apply Cossart–Piltant Theorem 1.1 to the affine scheme Spec R. Its affine-projectivity clause and its regular-locus clause provide the initial regular projective resolution simultaneously. Kollár–Witaszek's desired ample exceptional divisor is then constructed on a further modification without invoking another unspecified projective resolution.

More precisely, write L2 for the coherent rank-one sheaf occurring in Kollár–Witaszek Lemma 8. On the initial regular resolution, its torsion-free pullback M embeds in the invertible reflexive hull M**. Thus J = M tensor (M**) inverse is an ideal, equal to the unit ideal on the puncture and at all codimension-one points. In dimension three Cossart–Piltant Proposition 4.4 principalizes this ideal by blowups in regular centres in its nonprincipal locus. In dimension two its support consists of finitely many closed regular points, and Stacks Lemma 54.4.1 gives the corresponding point blowups. These constructions preserve regularity, projectivity, and the entire punctured open. The resulting invertible quotient of the pulled-back L2 defines the required map to Kollár–Witaszek's second Proj. Lemma 8 now applies directly.

We next embedded-resolve the entire reduced closed fibre, whose dimension is at most two, using Cossart–Jannsen–Saito Corollary 0.4. This precise choice avoids an additional identification between a named exceptional locus and the full closed fibre. Kollár–Witaszek Lemma 6 and relative ampleness restore an ample exceptional divisor after this step.

Finally normal Hartogs identifies the global sections of a sufficiently positive power of the exceptional divisor sheaf with an ideal I of R. Global generation gives I O_Z = O_Z(nF), inside the common rational function field, so -nF is effective. If I were the unit ideal, the trivial line bundle would be relatively ample, making the birational projective morphism finite and hence an isomorphism over normal R. In the singular case this is impossible. Thus I is m-primary, and -nF has strictly positive coefficient along every component of the full closed fibre. All hypotheses of C.3bc are now verified.

## Material correction in the audit

The first draft inferred simultaneous projectivity and preservation of the regular puncture from separate resolution statements. That inference was not justified: Kollár–Witaszek's convention does not require a resolution to be an isomorphism over the regular locus, and the general projectivization assertion in BMP+ does not preserve the SNC open automatically. Root identified this source-scope gap before checkpoint13. The earlier peer endorsement was explicitly withdrawn on that step.

The final proof replaces the inference by the explicit principalization construction above. The exact new primary inputs are Cossart–Piltant Proposition 4.4, current author version p. 141, and Stacks Lemma 54.4.1, Tag 0AHH. The revised complete peer review passed at 12:31:59 UTC. Root freshly read the same inputs and the revised proof, recorded final PASS at 12:35:36 UTC in notes/ROOT_C3bd_LOWDIM_FPBAR_AUDIT.md, and authorized finalization after checkpoint13 was saved. The earlier endorsement is not represented as certification of the corrected proof.

## Primary-source record

- Cossart and Piltant (2019), current arXiv v2 dated 8 January 2019: Theorem 1.1, author pp. 3–4, and Proposition 4.4 with proof, author p. 141. The downloaded source and its hash are retained. We use the theorem and do not claim an independent verification of the full resolution algorithm.
- Kollár and Witaszek (2026), complete four-page arXiv author version dated 5 February 2021: Lemmas 6 and 8, pp. 2–3, and surrounding construction. Publisher metadata records online publication in January 2024 and issue publication in July 2026. The publisher PDF retrieval returned HTTP 429; all proof locators here explicitly refer to the opened author version.
- Cossart, Jannsen, and Saito (2013), current 169-page author v2: Corollary 0.4 and its proof, p. 5. This is the author-version numbering, not an invented locator in the later book.
- Stacks Project Proposition 28.27.13(7), Tag 01Q3; Remark 31.17.2, Tag 0BCS; and Lemma 54.4.1, Tag 0AHH. Complete statements and relevant proofs were opened and read.
- BMP+ current v3, Proposition 2.14 and Remark 2.15, were checked as neighboring scope; they are not cited as supplying the missing preservation assertion.

The full bibliography includes opened markers and these limitations. Acquisition scripts, timed outputs, SHA-256 hashes, the standalone wrapper, and compilation script are retained alongside the proof.

## Validation

The revised mathematical draft compiled in four LuaLaTeX/BibTeX passes starting at 12:31:03.836361 UTC, with total runtime 3.173785748 seconds. All passes returned zero; the three-page PDF was 120925 bytes and the log contained no warnings or box errors. The original revised-draft build JSON and output were preserved separately before promotion to the final filename. The final-path rebuild is recorded in the current build JSON and canonical check-event file.

This compilation checks rendering and references; it is not a substitute for the independent mathematical and source audits. The canonical statement register and check events use the required seven-column and five-column schemas, respectively.
