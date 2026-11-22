# Root source and proof audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 20 November 2026.
We make no priority claim.

## Original manuscript

We retrieved the original cote22 PDF from the Montpellier archive and visually read scans13,14,22,23. The archive's printed leaf numbers differ from the PDF scan indices; the supplied transcription's scan numbering is retained. Definition4.7 explicitly restricts to noetherian rings and includes adic completeness, conditionP and formal smoothness. Its preceding definition of P is not in the retained dossier. We prove preservation of both formal projectivity and strict formal projectivity, with each definition stated explicitly.

## Primary mathematical sources opened

The exact theorem locators and opened/not-opened flags are in notes/root_references.bib. We opened Stacks10.138,10.158,15.41,15.50,92.16,92.6,10.97,10.51,37.15,10.137.16 and33.12.6, checking the topology, noetherianity, finite-presentation and coefficient hypotheses at each use. We opened Neeman's original1992 scan, Lemma2.12 p527, for residue-field detection in the unbounded derived category. We opened Blickle–Fink2025 v1 in PDF and original arXiv LaTeX; Theorem2.10 explicitly concerns arbitrary noetherian ring maps and asserts regularity iff the cotangent complex is flat in degree0. Its F-finiteness restriction elsewhere is not imported into that theorem. We opened Pérez Rodríguez2008, Definition1.3 and Corollary4.3, and retrieved the preferred original LaTeX source. That formal-scheme smoothness convention includes pseudo finite type.

Hochster1973 was located through the author's bibliography; the original article has not been opened. The noetherian cusp construction is fully proved here, so the attribution is not used in place of a proof. A secondary locator for Matsumura's discussion of power-series formal smoothness is recorded as not opened. We searched for prior treatments of discrete formal smoothness, infinite p-rank and adic square-zero lifting; no originality or priority claim is made for our proofs.

## Cross-section audits by root

We checked the full arguments in B2, C1–C8, D1–D4 and D7–D16, E, F's fixed-order and formal-local finite-order claims, H's analytic determinant proof, I1–I9 and the announced I10 counterexample, J1–J8, L1–L8, and the indicated K counterexamples. Agent check-event fragments record these targeted audits separately from the construction of the proofs. Every claimed computational check has an actual saved program and output; mathematical arguments over infinite rings are not described as finite exhaustive computations.

## Additional historical source work

We opened the original Palais–Terng article text through two OCR mirrors, checking Definition0.1, MainTheorem0.3 and Propositions0.5–0.6. The author Terng's publication list confirms Topology16(1977),271–277; a Celebratio bibliography has an incorrect volume19. Publisher retrieval of the full article and of Epstein–Thurston was unsuccessful. The official Epstein–Thurston page verifies bibliographic metadata, but an attempted public first-page image fetch returned403. We do not count it as an inspected page. The original Palais–Terng revision note is a primary witness attributing removal of the smooth-parameter hypothesis to Epstein–Thurston; it is not an algebraic finite-order theorem.

We also opened the1956 Grothendieck Erratum, Annales de l'Institut Fourier6 pp117–120. Page119 explains the mismatch between planned Hilbert spectral results and the Fredholm article. It does not itself quote the genus-zero statement or date the unpublished cote1 sheets.

## Record correction

Checkpoint01's automated event builder labelled all PartA records as independent re-proofs, including source remarks and Known statements. We corrected the current register to targeted proof checks or sources used and rechecked, as appropriate, and retained separate attributed agent audits. Checkpoint01 remains immutable.

## Final source and scope checks, 20 November 2026

We independently checked the full added C9 counterexample and its complete-filtered-module repair, the actual sign directions on the original EGA IV erratum page, and the full D17 proof of the literal chapter-zero infinitesimal-testing statement. The algebra event fragment records these checks. We visually inspected original ICM 1970 p.435, confirming the precise reconstruction and essential-image questions used by J9.

The completion step in A14 now cites the exact opened Stacks Lemma 15.38.4, tag 07ED, separately from Proposition 15.50.2. We reopened tag 06PL and verified that its flatness and finite-presentation criterion supports the quotient-stack argument in K(c).

We inspected the original Bourbaki 91 scan, including printed pp.383–384: the Hilbert product formula occurs on p.383 and the author’s final text date is June 1957 on p.384. This is a dated textual witness. We do not silently turn the date of a lecture, a later collected edition, or a dossier’s dated letter into the physical publication date or the date of every manuscript sheet.

The Montpellier catalogue, https://grothendieck.umontpellier.fr/archives-grothendieck/, describes cote 1 as undated functional-analysis notes and a 1953 letter. We are inspecting the original dossier for the scope of that date. The catalogue alone does not date the crossed-out trace-formula sheets.

The whole 382-page fourth-printing memoir was OCRed by code/root_ocr_memoir.py in 44.677766108 seconds. Its source SHA256 is 85b3ba9324fbadcd41c55090a20e7fdf3e886318c838aff2311ea78755ea2802. The search inventory is logs/root_memoir_genus_hits.json. We read the title page, contents, PDF pp.214–221 (the relevant Chapter II passage), and the appended pp.377–382. Chapter II p.13 announces the Hilbert genus-zero assertion; subsequent arguments use it to obtain the two-thirds nuclear result. The discovered Hadamard argument removes a quadratic exponential after passing to a square and is not the manuscript’s three-sector removal of a linear exponential. A whole-source OCR search is an aid to source checking, not a certificate that OCR never omitted a word.

We fully audited the new pointed-versus-unpointed jet example, the complete finite locally free Hopf-comodule torsor description, and the arbitrary-base idempotent/matrix classification in K(h). The finite jet certificate checks four automorphisms of a sixteen-element algebra and all twenty-four candidate equivariant bijections on the four-element coefficient ring. The root audit of its categorical conclusion distinguishes failure of equivalence from failure of faithfulness of a restriction functor.

For the standard cohomological inputs in K(g,h), we opened the Stacks Project at https://stacks.math.columbia.edu/tag/03P2 (Theorem 59.22.4), /tag/01XB (Lemma 30.2.2), /tag/0BXJ (Lemma 31.29.5), and /tag/01XS (Lemma 30.8.1). These give the fppf comparison and affine vanishing, the field-valued Picard group of projective space, and the precise twist cohomology used in the splitting proof.
