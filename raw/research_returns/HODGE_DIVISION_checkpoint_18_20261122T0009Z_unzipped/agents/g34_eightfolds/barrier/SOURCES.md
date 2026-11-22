# Sources and scope for the determinant barriers

## Published input actually used

**Michael Dettweiler and Stefan Wewers, _Variation of parabolic cohomology and Poincaré duality_, Séminaires et Congrès 13 (2006), 145–164.** Author version: <https://arxiv.org/pdf/math/0411119>, arXiv:math/0411119v1 (5 November 2004). Theorem 2.5, PDF page 12, gives the exact right-cocycle cup formula; its proof occupies PDF pages 13–14. Right-cocycle conventions and the product-one relation occur in the preliminary discussion, PDF pages 2–3. The theorem statement and proof were read, and the invariant-Hermitian-dual specialization was checked term by term. Local immutable copies: `../sources/DW_duality.pdf` and `../sources/DW_duality.txt`. Existing bibliography key: `G34:DWdual`.

**G24 and GF4 group arithmetic and geometry.** The published matrix/root seeds and the fully rebuilt finite-group certificates are documented in `../g24/SOURCES.md` and `../gf4/SOURCES.md`. The new determinant proofs use the exact established group descriptions: the natural G24 representation and its norm-two reflection roots over \(\mathbf Q(\sqrt{-7})\), and \(W(F_4)\sqcup W(F_4)z\) with \(z=t\Phi/2\) over \(\mathbf Q(\sqrt{-2})\). No Severn theorem is a premise.

## New results and their logical status

`determinant_barrier.tex` contains complete new proofs D-DET-01–03. D-DET-01 derives a determinant identity from the actual published cup pairing by a nondegenerate triangular Seifert form and an explicit coboundary/complement block calculation. The two universal barriers then follow from the local moving-space determinants together with necessary Hurwitz dimension bounds. The bounds do not establish dominance; the split witnesses have separately proved exact period rank nine.

The trace-Witt injectivity lemma in D-DET-03 is proved in the text by rational isotropy, splitting of Hermitian hyperbolic planes, and rational Witt cancellation. It is not inferred from real signature. The scalar normalization \(h((1-tA)x,(1-tA)x)=2x^tx\) is explicitly checked.

## Reproducible finite checks

Run `python check_unpaired_determinants.py`. It imports only the exact field/matrix/group constructors from the earlier certificates. It independently builds the relation spaces, coboundaries, quotient bases, ambient Seifert matrices and cup matrices for three unpaired generating tuples in each group. It checks the identities

\[
S+S^*=R^*HR,\qquad d^*S=HR,\qquad
N(\det T)\det S=N(\det B)\det S_P,
\]

and records explicit norm witnesses for each parabolic determinant. The fixed random seed is only a reproducible word selector. Every resulting identity is checked by exact quadratic-field arithmetic. No floating-point rank, numerical tolerance or inference from random sampling is used.

The same script enumerates all 163 nonidentity involutions of the 2304-element GF4 group, including its 24 outside involutions, and checks their exact moving-space determinants. This is an additional finite check; the universal outside-involution claim is proved without relying on this enumeration.

`unpaired_determinants.json` retains every selected branch matrix, all local determinants, the full six-dimensional parabolic Gram matrices, and the norm witnesses. None of the sampled words is the fully adjacent-doubled word used for the original rank-nine witnesses.

## Boundary of the result

The universal barriers concern these two faithful natural representations and connected curve covers whose monodromy generates the indicated finite group. They allow arbitrary initial inertia orders, ordering, Nielsen class and base genus. They do not classify all finite groups over an imaginary quadratic field, exclude other representations, or exclude other geometric sources of algebraic Weil cycles.
