# Bourbaki rédaction 230: complete Hilbert-section inspection

Recorded 20 November 2026, 03:58–04:00 UTC, by geometry_analysis, GPT-6 Astra Pro, inherited effort. This is a documentary comparison for geo-H-history and SA23-49. It is not a new mathematical proof check or a manuscript-date certification.

## Exact source and reading scope

The primary source is the IECL/Delsarte copy of *Rapport sur la théorie spectrale*, rédaction 230, Part I B, Chapter III, §3, **Opérateurs compacts dans un espace hilbertien**, typed pages **188–203**, physical PDF pages **102–117**. Every one of these sixteen pages was displayed individually, including its margins, and read directly. The printed page numbers confirm the physical-to-typed offset throughout this range. No conclusion below relies on the absence of an OCR keyword.

Local original: `sources/category_bourbaki_r230_original_1.pdf`, 29,100,237 bytes, 156 physical pages, SHA256 `2ecd5627b5e9878a362a237fcadbac6ccdbb85e076551d7c4f6f37d31f19eba1`.

Exact publicly advertised archived payload, retrieved by category:

http://web.archive.org/web/20260213200334if_/https://archives-bourbaki.ahp-numerique.fr/files/original/49e6e904fbc99a10207673c09e068fa7.pdf

Its source/retrieval and catalogue history are retained in `notes/category_bourbaki_r187_r230_date_audit.md`. Geometry reused that preserved public source and made no new network request. The scan's 2019 creation metadata are digitization data.

The catalogue's March 1956 attribution explicitly refers to handwritten wording on **a different ENS copy**, not a date directly seen in this IECL scan. None of the sixteen inspected Hilbert pages bears a dated letter, an enclosure identification, or a reference to the Montpellier cote 1 leaves. This route does not authenticate the other copy's handwriting, authorship or date of inscription.

## Complete page map

| Typed page | Physical page | Material actually read |
|---|---:|---|
|188|102|Compact normal operators: spectral decomposition, algebraic/geometric multiplicities and the Picard solvability criterion.|
|189|103|Proposition 1, normal operator with a compact positive power is compact; Hermitian positive/negative eigenvalue sequences; Proposition 2, variational characterization.|
|190|104|Completion of Proposition 2; dense invariant subspace remark; Proposition 3, minimax principle.|
|191|105|Corollary 1 to Proposition 3: sum, finite-positive-rank perturbation, operator-norm perturbation and monotonicity estimates for Hermitian eigenvalues; proof.|
|192|106|Completion of that proof; Corollary 2, compression eigenvalue inequality; Proposition 4, compactness of T equivalent to compactness of abs(T).|
|193|107|Proposition 5, singular-value expansion and its converse; operator-norm convergence and norm formula.|
|194|108|Completion of Proposition 5; corollary comparing products of absolute eigenvalues, with algebraic multiplicity, to products of singular values; proof begins.|
|195|109|Completion of the product inequality through finite-dimensional triangularization and compression; vague reference to a recent Grothendieck paper for further inequalities; Proposition 6, nuclearity of T equivalent to that of abs(T), with equal nuclear norms.|
|196|110|Completion of Proposition 6; Proposition 7, the basis-diagonal criterion for nuclearity and the basis-diagonal trace formula; finite-rank and trace-norm approximation arguments.|
|197|111|Completion of Proposition 7 by Hermitian real/imaginary decomposition; Corollary 1, Hermitian spectral trace and trace norm; Corollary 2 for arbitrary nuclear eigenvalues begins.|
|198|112|Corollary 2 proves absolute eigenvalue summability with sum bounded by the nuclear norm, using finite primary spaces and triangularization; construction of the Hilbert tensor product begins.|
|199|113|Hilbert tensor norm and its canonical injection into bounded operators; orthonormal-coordinate calculation.|
|200|114|Hilbert–Schmidt operator definition; Proposition 8, bounded functoriality of Hilbert tensor products with norm estimate.|
|201|115|Corollaries: composition ideal estimate and equivalence with abs(T) for Hilbert–Schmidt operators; Proposition 9, orthonormal-basis square-sum criterion.|
|202|116|Completion of Proposition 9; singular-value square summability; Proposition 10 (Lalesco), product of two Hilbert–Schmidt operators is nuclear and its trace is their Hilbert–Schmidt pairing.|
|203|117|Completion of Proposition 10; square-summability bound for the eigenvalues of a Hilbert–Schmidt operator; extension to maps between different Hilbert spaces; positive nuclear square roots are Hilbert–Schmidt. End of §3.|

## Critical trace distinctions

The section contains three different trace assertions which must not be conflated.

1. **Proposition 7, typed pp. 196–197:** for an arbitrary nuclear Hilbert operator T, its trace is the absolutely convergent sum of diagonal coefficients in any orthonormal basis. The stated criterion quantifies over orthonormal families. The proof treats finite-rank operators, passes to the nuclear norm limit, and reduces the converse criterion to Hermitian real and imaginary parts. It does not assert that an arbitrary orthonormal basis consists of eigenvectors.
2. **Corollary 1, typed p. 197:** when T is explicitly **Hermitian and compact**, nuclearity is equivalent to summability of its eigenvalues in absolute value, and the trace is their sum. This follows from the Hermitian orthonormal spectral decomposition used in that corollary. The hypothesis cannot be dropped merely because Proposition 7 holds for general T.
3. **Corollary 2, typed pp. 197–198:** for an arbitrary nuclear Hilbert operator, the sum of the absolute values of its eigenvalues, with algebraic multiplicity, is at most its nuclear norm. The proof chooses a finite direct sum of nonzero primary spaces, triangularizes the restriction in an orthonormal basis, and applies Proposition 7's diagonal estimate. The conclusion displayed as equation (2) is the inequality. **It does not conclude that the full trace equals the spectral sum.** In particular, it does not prove that the trace on a quasinilpotent quotient is zero.

The distinction also applies to **Proposition 10 (Lalesco), pp. 202–203**: its formula expresses the trace of a product of Hilbert–Schmidt operators as a Hilbert–Schmidt inner product. That is not a spectral eigenvalue-sum identity for a general nonnormal operator.

## Comparison with the particular cote 1 argument

The entire Hilbert section has now been read. It does **not** contain an entire Fredholm determinant factorization, a genus-zero theorem, an elimination of a linear exponential in Hadamard factorization, or the three rotated factors g(z), g(omega z), g(omega squared z) used in the cote 1 proof. There is therefore no matching three-sector argument here that could serve as a dated textual witness to the distinctive proof.

There is a mathematically relevant partial correspondence: the finite-primary-space argument in pp. 194–195 and 197–198 handles algebraic multiplicity correctly and proves product/sum bounds. Those are standard ingredients adjacent to the manuscript's trace problem and also to the completed modern proof in geometry_H.tex. They do not identify this report with the handwritten pages or establish the missing genus-zero deduction by themselves. No new proof or priority attribution is inferred from this comparison.

Immediately after the product inequality, **typed p. 195** mentions a recent paper of Grothendieck as a source for further inequalities. It gives no title, year, letter date, draft identifier or enclosure description there. It is not an exact manuscript witness. Identifying that vague reference with a particular publication would require separate evidence; this audit does not make that inference.

The subsequent Fredholm section, typed pp. 204–221, is being inspected independently by category. This note makes no negative assertion about that not-owned range or about the rest of the 156-page document. The combined conclusion must wait for its exact reading.

## Reproducibility and limitations

`code/geometry_r230_hilbert_render.py` rendered all sixteen assigned pages at a 2300-pixel longest dimension, using four workers, and ran English Tesseract solely as a finding aid. `logs/geometry_r230_hilbert_render.json` preserves each command, stdout, stderr, status, page-image size/hash and elapsed time. Total measured runtime was **81.92391865399259 seconds**; there were no render or OCR exit failures. OCR of the faint purple type is incomplete and sometimes poor, especially for formulae, and was not used as an absence certificate.

Exact original-page images: `sources/geometry_r230_hilbert/physical_102.png` through `physical_117.png`. OCR texts: `notes/geometry_r230_hilbert_ocr/physical_102.txt` through `physical_117.txt`. One attempted image display of physical106 occurred before its PNG had finished writing and returned an invalid-image error. It was **not counted as a reading**. After rendering completed for that page it was displayed successfully and read; physical107 was also subsequently displayed. Every page in the table above was successfully delivered as an image and visually inspected.

No new source download, account, contact, access bypass, mathematical computation or formal-review movement is claimed. The smallest historical gate remains an explicit dated identification of the particular Montpellier leaves or their distinctive proof.
