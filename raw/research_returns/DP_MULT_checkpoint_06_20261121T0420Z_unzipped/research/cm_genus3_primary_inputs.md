# Exact primary inputs for DP22

Agent `/root/archive_binomial`, GPT-6 Astra Pro, effort not exposed by the runtime. Source statements checked on 2026-11-21 UTC. These references replace the unspecified background locators in the first DP22 memo.

## Relative Jacobian over A=W(F_(11^3))

The following primary-source chain proves precisely what is needed.

| Input | Exact locator | Statement used |
| --- | --- | --- |
| Picard representability | A. Grothendieck, Bourbaki exposé 232 (FGA V), Theorem 3.1, pp.148--149 | For a projective flat morphism of locally noetherian schemes with geometrically integral fibres, the relative Picard functor is representable. The accompanying paragraph supplies separation. |
| Smoothness | A. Grothendieck, Bourbaki exposé 236 (FGA VI), Proposition 2.10(ii), p.236 | Vanishing of H^2(X_s,O_Xs) implies smoothness of the Picard scheme over a neighbourhood of s. The source uses the older word "simple" for smooth. |
| Open identity component | Same exposé 236, Corollary 1.7, p.229 | Universal openness near the fibrewise identity component, together with smooth geometric fibres, makes that component open. In particular this applies to a smooth group scheme. |
| Proper identity component | Same exposé 236, Corollary 2.3, p.232 | For a proper flat morphism with geometrically normal fibres and existing Picard scheme, the fibrewise identity component is proper over the base. |

Primary PDFs:

- https://www.numdam.org/article/SB_1961-1962__7__143_0.pdf
- https://www.numdam.org/article/SB_1961-1962__7__221_0.pdf

For our explicit curve, the finite morphism to P^1 makes the family projective. The two charts prove smoothness, and the nonsquare polynomial x^7-1 gives geometric integrality of each fibre. The same two affine charts have affine intersection. Their Cech complex for the structure sheaf has no terms in degree two, so H^2 of every fibre vanishes. Thus the Picard scheme exists and is smooth. Its identity component is open, proper and smooth with geometrically connected fibres: it is an abelian scheme. Its generic fibre is the Jacobian by the Picard-functor definition and base-change compatibility. The infinity section supplies the pointed Abel--Jacobi construction.

The precise special-fibre normality and H^2 hypotheses have therefore been checked, rather than inferred from the name "Jacobian". No general representability theorem over an unspecified base is being invoked. In the original PDF, the formula H^2(X_s,O_Xs)=0 on p.236 and Pic^0 on p.232 were inspected in rendered page images because the OCR omits them.

Suggested compact paper citation: FGA V, Theorem 3.1, pp.148--149; FGA VI, Corollaries 1.7 and 2.3 and Proposition 2.10(ii), pp.229,232,236.

## Connected p-divisible group and formal completion

J. Tate, *p-Divisible Groups*, in *Proceedings of a Conference on Local Fields* (Driebergen, 1966), Springer, 1967, pp.158--183:

1. **Section 2.2, Proposition 1, p.162** (proof sketch pp.163--164): over a complete noetherian local ring of residue characteristic p, divisible commutative formal Lie groups and connected p-divisible groups form equivalent categories. The formal Lie groups here are defined by power-series rings, so smoothness is included in the conclusion.
2. **Section 2.3, Examples b), p.166** explicitly identifies the connected component of the p-divisible group of an abelian scheme with its formal completion along zero.

Primary PDF: https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf

The PDF uses two printed pages per PDF page. The printed locators above were verified by local layout-preserving extraction: PDF page 3 contains printed pp.162--163, and PDF page 5 contains pp.166--167. These are not guesses from PDF page indices.

Apply these results as follows. Both factors G_1,G_2 in DP22 have strictly positive slopes, hence are connected. Thus J[p^infinity]=G_1 times G_2 is connected. The equivalence transports this integral product decomposition, including its inclusions and projections, to a product of smooth formal groups. Example b) identifies that product with the actual completion of J. The selected dimension-one factor is consequently an integral formal direct factor, not just an abstract formal group isogenous to one. Its tangent inclusion is split over A. This closes the formal-subgroup step without any additional classification theorem.

## Bibliographic entries and scope

The two Grothendieck papers are *Technique de descente et théorèmes d'existence en géométrie algébrique. V. Les schémas de Picard : théorèmes d'existence*, Séminaire Bourbaki, exposé 232 (February 1962), collected pp.143--161; and *VI. Les schémas de Picard : propriétés générales*, exposé 236 (May 1962), collected pp.221--243.

This is a statement-and-application check of these classical theorems. It does not claim an independent reproof of Picard representability or of Tate's equivalence. It verifies all hypotheses used by DP22 and the exact locators. The earlier complete DP22 proof check remains recorded as ABA-CE17; this additional source check is ABA-CE18, completed after rereading this complete memo at 2026-11-21 00:35:33 UTC.
