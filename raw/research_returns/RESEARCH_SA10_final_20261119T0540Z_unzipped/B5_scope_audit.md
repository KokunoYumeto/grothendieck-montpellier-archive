# B.5 final scope and implication audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run `/root/hypercovers_finite_sets`, 19 November 2026. No priority claimed. This rereads the current `B56.tex` against the exact B.5 request and the opened primary sources. The current LaTeX is authoritative; its Markdown mirror is regenerated after these edits.

## Coverage and exact conclusions

| Requested question | Complete result and proof | Necessary qualifications |
|---|---|---|
| What are the manuscript's comparison maps? | B5.1 defines the cocontinuous extension by its coend and identifies Hyp1,2,2′ as terminal, binary-product and cospan comparisons of representables. | Objects of the topos are interpreted by their slice topoi for shapes, not by global sections or component sets. |
| Do those hypotheses give all forest comparisons? | B5.1 proves the equivalence for finite oriented forests, including the empty forest. Local finite zigzags extend representable comparisons to arbitrary presheaves; leaf deletion finishes. | This is an equivalence of collections of tests, not a classification of each indexing category separately. An index with an initial object has an automatic comparison. |
| Is full (Hyp) left exactness? | B5.1 proves both directions. Two added limiting cone vertices make the comparison the original comparison's diagonal; epic diagonals are invertible. | Includes the empty diagram. The single-dot diagram in151/015 is an identity test. |
| Does full (Hyp) suffice for descent? | B5.6 proves terminal derived colimit in the associated 1-localic infinity-topos and hence after hypercompletion. | First lift the geometric morphism to the associated 1-localic infinity-topos, then compose its inverse image with hypercompletion. Do not call the latter 1-localic without further hypotheses. |
| Are forest conditions sufficient? | No: B5.2 is the C2 orbit counterexample, failed equalizer and nonzero H1. B5.3 is the symmetric group example with a complete all-cospan proof. | Finite computations supplement the unbounded proofs. |
| What is the arbitrary-index criterion? | B5.6.2 is exact for the specified pro-space comparison. B5.10.1 gives an explicit necessary-and-sufficient subdivision-filling scheme for terminality after hypercompletion. | The filling scheme is sufficient, not asserted necessary, for shape equality alone. Subdivision depth may vary locally; no algorithmic decision claim. |
| What is original Artin–Mazur homotopy? | B5.6.3 identifies AM(X)=q(shape(X_infty^hat)) for locally connected X; B5.6.4 gives exact bijective π0 tests in Pro(Ho Spaces). | First form the colimit in Pro(Spaces), then apply q. No interchange of π0 with the A-limit, no preservation of the colimit by q, and no converse from pro-homotopy isomorphism to pro-space equivalence is asserted. |
| How do Verdier hypercovers arise? | B5.7 proves proper-face representable identities. For Δop they give degrees≥2; degrees0,1 are separate. For Fin_nonempty^op they give degrees≥1; degree0 is separate. | Hypercover realizations are infinity-connected before hypercompletion and terminal after it. An explicit comma contraction proves Δop→Fin_nonempty^op homotopy final. |
| Can matching degrees be omitted? | B5.8 constructs symmetric systems failing just the mth condition, for every m≥0, with noncontractible hocolimit. | Empty system, constant two-point system and cocycle K(F2,m−1) treat all cases; the latter has a full normalized-complex proof and32 finite checks. |
| Are hypercovers strictly between forests and flatness? | No. In ordinary indexing, flatness and hypercovers are incomparable. In symmetric indexing, flatness implies hypercover strictly, but hypercover need not imply forests. | Čech, flat Δ[1] and symmetric continuous-simplex examples prove each nonimplication. Symmetric flat systems are inhabited powers E^S. |
| Does the symmetric group nerve realize to BG? | Derived hocolimit and ordinary simplicial realization give BG; the naive affine symmetric coend is contractible for finite G. | The three constructions are named separately. |
| Can one diagram of component sets be used? | B5.9 disproves this even under full (Hyp), using the terminal diagram in Sh(S2). Slice shapes may be replaced by components if each individual comparison is an equivalence. | In general the complete hypercover pro-system is retained. A single terminal hypercover is not generally a model of shape via components. |

## Hypercompletion audit

No remaining implication in B.5 derives full nonhypercomplete shape descent merely from a local weak equivalence. The actual implications are:

1. Full ordinary (Hyp) ⇔ left exactness ⇒ terminal derived colimit in the associated 1-localic infinity-topos ⇒ full shape comparison.
2. Verdier matching epimorphisms, or the explicit arbitrary-index scheme B5.10.1, give terminal derived colimit **after hypercompletion**, hence hypercomplete shape descent and the locally connected Artin–Mazur comparison.
3. They also give the protruncated comparison, since truncated constant objects are hypercomplete.
4. Full shape without hypercompleteness requires the exact tests B5.6.2, or another proof of terminality before hypercompletion. No local model-category appeal silently establishes this stronger conclusion.

B5.6.2 uses equivalences of mapping spaces; B5.6.4 uses bijections after π0. Their proofs use the appropriate fully faithful pro-Yoneda embeddings. B5.10.1 supplies the constructive all-index replacement, beyond the constant-space tests. Original Artin–Mazur's additional localization, noted in Barnea–Schlank Remark8.5(3), may be applied subsequently; every isomorphism proved here survives it.

## Newly opened primary sources

- **Barnea–Harpaz–Horel, _Pro-categories in homotopy theory_, AGT17(2017)567–643.** Full publisher PDF: <https://msp.org/agt/2017/17-1/agt-v17-n1-p17-s.pdf>. Theorem6.0.4 and proof, printed pp625–626, identify derived topological realization with the shape of the **hypercompletion**. Corollary6.0.5 p626 states the scheme Artin–Mazur comparison. Key `B56BHH2017`.
- **Barnea–Schlank, opened arXiv v9.** <https://arxiv.org/html/1109.5477v9>. Definition8.2 pp62–63, Proposition8.4 pp63–64, Remark8.5(2) p65 extend the Artin–Mazur identification to every locally connected topos. Remark8.5(3) records the further localization. Introduction p6 states that the functor to Pro(Ho Spaces) does not reflect isomorphisms. Key `B56BarneaSchlank2015`.
- **Haine, _On the homotopy theory of stratified spaces_, arXiv1811.01119v6.** Full requested PDF: <https://arxiv.org/pdf/1811.01119>, dated27March2023. Definition1.1.1 p7; Definition1.1.4 and Theorem1.1.7 p8 identify conservative infinity-categories over a poset with finite-flag décollages. Theorem3.2.4 p27 concerns Exit after localization at strata/link equivalences; Comparison3.4.2 p30 relates conically smooth spaces. **No premise in B.5.** Theorem1.1.7 is cited in `C1_collage_B.tex` after C1.B2 for the flag-Segal framework, with the geometric Exit comparison still proved separately. Key `B56Haine2023`.

Previously opened sources and locators remain in `references_B56.bib`. Fetched full copyrighted texts are excluded from the deliverable package.

## Preservation of the C.5 proof

The complete proper PL/smooth Hurewicz counterexample remains unchanged in `C5_Hurewicz_review.tex` and `.md`, with `references_C5_Hurewicz.bib`, finite A7 quotient code/output and check events. Root and C agents independently audited it. Original Mazur1961 has **not** been opened: the sources actually opened are Zeeman1964 p347 for the construction and nontrivial boundary statement, Rolfsen11E.3 p356 for the boundary-group presentation, Milnor1965 Th9.1 and PropositionA, and Ferry1978 Definition/Th1. The abandoned direct Chapman route remains recorded and unused.

## Residual status

B.5 has no unresolved mathematical step under the explicit targets and hypotheses above. The visual ambiguity in the last low-degree relation of151/005 belongs to B.6: both mathematical alternatives are settled and retained, while the ink subscript remains unresolved. No theorem depends on choosing that reading.
