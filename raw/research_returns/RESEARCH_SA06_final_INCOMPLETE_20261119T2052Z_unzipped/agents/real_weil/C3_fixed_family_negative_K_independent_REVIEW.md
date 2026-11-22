# Independent complete audit of the fixed-product negative-K obstruction

**Verdict: PASS**, for the exact characteristic-p hypotheses in `../frobenius/C3_fixed_family_negative_K.tex`, FF.1–FF.3. Full typed proof and source ledger read at 15:57–16:02 UTC on 19 November 2026. This is an unnumbered auxiliary statement, not a new ordinary-Chow range conclusion.

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not separately exposed.

## Full proof check

The product B=Spec(R)×P is Noetherian, but is not local. The proof correctly retains its K0 term. Proper base change of the modification gives an abstract blow-up square with centre P. The n-th exceptional scheme and E×P have the same reduction, since the coefficient field is perfect and P is smooth. Their closed immersion is nilpotent on this Noetherian scheme.

Geisser–Hesselholt applies separately to each nilpotent affine pair and every integer degree. Finite affine Mayer–Vietoris then globalizes its equivalence after inverting p. No common p-exponent across n is asserted or needed. The resulting identifications with K(P)[1/p] and K(E×P)[1/p] commute with the thickening transitions.

An exact additive functor on abelian groups induces an exact levelwise functor on pro-abelian groups: after reindexing, the finite kernel/cokernel constructions are represented levelwise. Thus localization of the KST pro-exact sequence remains exact. Its terms in the displayed segment are now constant pro-objects; the constant embedding is fully faithful and exact and reflects exactness. This produces the ordinary exact sequence stated in the proof without forming an inverse limit.

Z×P is smooth over regular Z, hence regular; P is regular. Their negative K-groups vanish. The K0(P) contribution is already in the image of K0(Z×P), by the actual projection to P. These facts give exactly the cokernel isomorphism FF.1. There is no claim that classes are represented by compatible bounded-rank bundles.

In the negative segment for a point parameter, the two adjacent regular terms vanish, giving K−2(E)[1/p] ≅ K−3(R)[1/p]. External products are compatible with the relative module fibres and their boundary maps. In FF.3 the parameter degree is two, so no additional sign appears. The text correctly keeps both the construction of the tetrahedral coefficient and its product with the boundary conditional. Neither nonzero κ-boundary nor existence of a proper-curve K2 evaluation establishes injectivity or zero for this product.

## Fresh primary-source inspection

1. Kerz–Strunk–Tamme, arXiv:1611.08466v4, dated 16 August 2017 on the cover (author date 17 August), full 48-page PDF: <https://arxiv.org/pdf/1611.08466>. Theorem A, author p.2, and exact formulation (1.6), p.3, read directly; fresh retrieval `turn194617360view0`. The Noetherian abstract-blow-up scope is exactly sufficient. I did not independently re-prove the published theorem.
2. Geisser–Hesselholt (2011), full 21-page journal PDF: <https://math.mit.edu/~larsh/papers/025/bounded.pdf>. Theorem A, printed p.29, and its complete proof, p.39, read directly; `turn194617360view1`, `turn532809224view3`. It explicitly covers Bass-completed groups in every integer degree and nilpotent p. The source's preceding p.38 paragraph also states that constant pro-abelian groups form a full abelian subcategory.
3. Thomason–Trobaugh (1990), full 189-page primary scan: <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf>. Section6.5, printed pp.360–361, Proposition6.8(b) and its complete proof, pp.362–363, and Theorem8.1 with its complete proof, p.367, were freshly read; `turn532809224view0`, `turn532809224view1`, `turn532809224view2`. These verify the module structure, regular negative vanishing, and finite-cover globalization actually used.

No program or independent build was run for this proof audit. It settles the stated obstruction formula only, not the vanishing of the obstruction or the residual top ordinary quotient.
