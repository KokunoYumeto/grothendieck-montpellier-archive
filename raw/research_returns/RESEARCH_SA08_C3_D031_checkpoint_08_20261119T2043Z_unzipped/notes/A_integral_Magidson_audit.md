# Magidson primary-source audit

The v2 PDF and complete arXiv source were fetched and opened on 2026-11-19. Local files are `sources/A_integral_Magidson/Magidson_v2.pdf`, `Magidson_v2.txt`, `source.tar`, and extracted `DPDR.tex`. The author's PDF at <https://kirillmagidson.com/wp-content/uploads/2025/06/pd.pdf> displays the same arXiv v2 date. The bibliographic key is `IC-magidson-derived-pd`.

## Exact constructions inspected

- Definition 4.1.1, printed page 51: the Hodge-filtered derived de Rham object is the left adjoint of `gr^0` from nonnegative filtered derived PD algebras; its dg object is the left adjoint of `ev^0` from the stated category of dg derived PD algebras.
- Theorem 4.1.4, printed page 52: the associated graded object is identified with `LΓ_A(L_{A/R}[-1])`; the first two grades identify the differential with the universal derivation.
- Proposition 4.1.6, printed pages 52–53: for a smooth discrete input, the shear construction gives the classical exterior algebra of differentials with its de Rham differential. This is an actual stated comparison, with its smoothness hypothesis retained.
- Construction 4.2.1 and Lemma 4.2.2, printed page 53: the explicit map is `ε: LΩ^{≥*}_{A/R} → Tot(A ⊗^{•}_{LΩ_{A/R}} A)`. The lemma proves that it becomes an equivalence after Hodge completion.
- Proposition 4.2.4, printed page 54: Hodge-completed derived de Rham cohomology is the totalization of the cosimplicial completed derived PD envelopes of the diagonal ideals in the iterated tensor powers of `A` over `R`.
- Corollary 4.3.5, printed page 56: the typed base-change diagrams give the derived crystalline comparisons relative to a specified derived PD base.

## Application checked

The constructions give explicit maps and equivalences with the sources and targets just listed. To apply their adjunction to a particular strict simplicial PD DGA `A^{w,q}` from cote 136, one still has to supply the corresponding derived PD object, its independent weight grading, and the input map on the zero grade; to return to the requested category one must construct actual strict maps and verify both separate eventual conditions. This audit has not constructed those maps or verified those two conditions for a replacement obtained from the cited functors. No conclusion about common sources or terminal localization is taken from the literature comparison alone.

The smooth comparison has been recorded rather than replaced by an assertion that no comparison exists. The completion in Lemma 4.2.2 is likewise retained explicitly: the displayed `ε` is the morphism whose completed equivalence is proved in that lemma.
