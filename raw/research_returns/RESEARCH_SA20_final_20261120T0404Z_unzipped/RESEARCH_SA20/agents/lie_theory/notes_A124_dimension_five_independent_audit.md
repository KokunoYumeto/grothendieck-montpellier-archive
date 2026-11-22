# Independent audit of A.124

**Auditor:** `/root/lie_theory`  
**Completed:** 2026-11-19 17:09 UTC  
**Outcome:** **PASS**, with the source-scope and typo qualifications below.  
**Draft audited:** `agents/singularities_duality/logs/A124_dimension_five_draft.tex`, read in full. No included source was changed during the checkpoint08 freeze.

The proposed theorem concerns a compact connected PL five-manifold, possibly with boundary, whose second homotopy group is zero. It identifies the full component group of pseudoisotopies with the already constructed countable stable group presentation `E(K)`. This audit does not extend the theorem to a nonzero second homotopy group in dimension five or to higher homotopy groups.

## 1. Full exact-sequence input

Igusa, *The second obstruction to pseudoisotopy*, arXiv:2502.19147v2 (23 March 2025), Theorem 7.1, printed p.23, explicitly states the full exact sequence for compact smooth manifolds of dimension at least five when the second homotopy group vanishes. Section 7 defines pseudoisotopies fixing both the bottom and the side boundary. Thus the stated boundary model and dimension-five hypothesis are covered directly by the imported theorem.

The same theorem applies to the rounded product with an interval. Projection identifies its fundamental group with the old fundamental group, and its second homotopy group remains zero. The group-theoretic map `chi` is natural, as proved in Section 4, pp.14–16; in particular the two images of `chi` are the identical subgroup under the product identification. The argument uses this full theorem. It must not replace it by the first/second coefficient computations alone. The author's characterization of the geometric proof as partial remains accurately reported in the draft.

Original opened and read: https://arxiv.org/pdf/2502.19147 . Local original: `source_external/lie_theory/igusa2025.pdf`, with corresponding `.txt`.

## 2. Positive suspension is a group homomorphism on components

Igusa, arXiv:2112.08293, Section 4.1, p.8, gives positive suspension on the collar-normalized model by the fixed polar-ray formula: apply the original concordance to the radial variables and leave the angular variable unchanged. For two normalized concordances, applying this operation successively equals applying it to their composition. The collar and corner conditions in that construction guarantee the required bottom and full side boundary conditions. Collar normalization is the already used equivalence on components. Thus the comparison is an actual homomorphism of component groups, not merely a correspondence between obstruction sets.

Original opened and read: https://arxiv.org/pdf/2112.08293 . Local original: `source_external/igusa2021_dim3.pdf`.

## 3. Available indices and the first invariant

The Hatcher–Wagoner original, Part I, Chapter V, Theorem 3.1(a), printed p.184, has the **non-strict** range `2 <= i <= n-2`. The original scan was visually checked; its OCR can lose the equality bars. Part II, Section 2, p.244, explicitly uses the same range to represent every component with adjacent indices `i,i+1`. Therefore indices 2 and 3 are allowed when the manifold dimension is five. No two-parameter index-range assertion from Theorem 3.1(b) is used.

The first invariant is unchanged under suspension by Part I, Section 5(5.2), p.60, and the remark on p.130. The ordered handle-slide matrices and labels are unchanged by adjoining the positive quadratic coordinate.

Original opened: https://www.maths.gla.ac.uk/~mpowell/Hatcher-Wagoner.pdf . Local originals: `source_external/hatcher_wagoner.pdf` and `.txt`; visual excerpt `source_external/lie_theory/hw_p184.png`.

The older source's boundary conventions need not be identified with the fixed-side convention by assertion: the latter is supplied directly by Igusa 2025, Section 7.

## 4. Entire framed invariant, including the Z/2 term

I reread Igusa 2025, Section 7, items (1)–(12), p.24. The inverse-matrix cut-and-reassembly operation produces, for each nonidentity group label, a closed framed one-manifold. Its stable framed bordism class supplies the Z/2 coefficient of the second obstruction. Under positive suspension:

- the intersection paths, paths to the chosen basepoint, group labels, and inverse handle-slide matrix remain the same;
- the framed one-manifold lies in the equatorial copy of the original intersection space;
- its normal framing gains the same constant extra normal vector everywhere;
- the framing matching at handle additions and birth/death points is consequently preserved;
- smoothing its corners commutes with this product stabilization.

Appending a trivial normal line does not change its class in stable framed one-dimensional bordism. Any ordering sign is also immaterial in the Z/2 coefficient. This proves the required compatibility on the whole kernel coefficient group and its quotient by `im(chi)`, not just a second-homotopy-group projection. Igusa 2021, Section 4.2, pp.8–9, additionally states the full marked-lens compatibility with positive suspension.

The proof does not invoke the realization lemma requiring `i,n-i >= 3` for arbitrary second-homotopy coefficients. The vanishing hypothesis removes that coefficient, and the imported full dimension-five theorem supplies the realization and full kernel statement actually needed.

## 5. Group-theoretic conclusion

The two exact sequences have the same left and right terms, and positive suspension induces the identity on both under the stated identifications. The short five-lemma argument is valid for the group extensions, with no splitting or commutativity hypothesis needed. Thus positive suspension from dimension five to dimension six is an isomorphism of groups. A.122 then identifies the target with `E(K)`, including its extension law.

## 6. Compatible smoothing and the boundary

I downloaded and opened the full Kirby–Siebenmann original, *Foundational Essays on Topological Manifolds, Smoothings, and Triangulations* (1977), from https://www.maths.ed.ac.uk/~v1ranick/papers/ks.pdf . Local original: `source_external/lie_theory/kirby_siebenmann1977.pdf` (364 PDF pages); extracted text: the corresponding `.txt`.

Exact checked printed locators:

- Essay IV, Appendix B, p.211 (PDF page 219): the handle-by-handle argument identifies the obstruction at an index-k handle with the class of a twisted (k-1)-sphere in `Gamma_(k-1)`.
- Essay I, p.39 (PDF page 47): compatible smoothings exist and are unique up to concordance in the low dimensions at most four.
- Essay IV, p.200 (PDF page 208): explicitly states `Gamma_4=0` and applies this to smoothing a PL five-dimensional homotopy sphere.

The handle argument applies to all compact PL five-manifolds, with collars for the boundary, because every index is at most five and all the required groups vanish. The draft correctly chooses a compatible smoothing of the entire PL manifold; it does **not** assert extension of an independently prescribed boundary smoothing. The already checked relative smooth/PL component comparison in A.103 then transfers the result. The definable and real-closed-field comparisons are exactly the previously established relative statements A.113 and A.115.

## 7. Printed source errors to retain explicitly

Igusa 2025 contains two relevant printed slips. On p.23, item (a), it prints `H_2(GL(Z pi)') = K_3(Z pi)` where the degree is `K_2`. In the introduction, p.2, a displayed or described pseudoisotopy component term is printed with `pi_1 P`, whereas the complete theorem in Section 7 correctly uses `pi_0 P`. Neither slip changes the theorem used in the argument, but both should remain recorded as source corrections rather than silently copied.

## Audit conclusion

The proof legitimately lowers the complete component-group computation to dimension five under the additional hypothesis `pi_2 M = 0`. The remaining five-dimensional case with nonzero second homotopy group is not addressed by this audit. No finite experiment or numerical calculation is needed for this geometric and source-theorem argument.
