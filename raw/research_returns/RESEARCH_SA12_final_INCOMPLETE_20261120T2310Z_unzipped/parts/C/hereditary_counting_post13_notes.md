# Hereditary counting: exact surviving gates

Written during the pre-09:55 checkpoint freeze; new research note only.

## Proved input

The two included lemmas `D:cover-uniform-MCM-annihilator` and `D:cover-uniform-relative-jets` give a fixed ideal and fixed two-parameter jet depth for every finite normal dominant punctured cover A/R, including relative Artinian sources. They do not assert a linear-index count.

For fixed A-MCM modules M,N of ranks r,s and a cover of generic degree t, H=Hom_A(M,N) is R-reflexive: it is the kernel of maps between R-reflexive Hom modules, with torsion-free image. Its R-rank is trs. Thus, for the uniform parameter pair x,y and any b,

    length_R H/(x^b,y^b)H = trs length_R R/(x^b,y^b).

The prescribed-map lifting and intrinsic-Hom construction use this same depth for every cover. Consequently the intrinsic arrow jet has size O(trs). This does not provide an object atlas: the underlying R-module has rank tr, and raw matrix coordinates have size O(t^2 r^2). The averaged separability element is obtained only after multiplication by I^2. It is not a separability idempotent of the truncated algebra, and does not give a Morita equivalence there. B independently confirmed this distinction.

## Prescribed semilinear coefficient action

Let q=p^f, and let theta:H -> Gal(F_q/F_p) have image of order d. The coefficient algebra local system, tensored with k, has f embeddings. The monodromy image permutes them by steps f/d. It therefore has f/d connected components, each the fixed degree-d cover U_theta -> U. Absolute Frobenius cycles through those f/d components; after one such cycle it returns with a fixed deck transformation of U_theta.

Accordingly, an equivariant linear-index object atlas would encode a prescribed-theta semilinear representation by f/d stages on that fixed cover, with a deck-twisted final arrow. If the per-stage presentation has O(d r^2) variables and equations, and a fixed deck pullback is encoded with the same degree/size bounds, the total is O(f r^2). This would remove an unnecessary extra d or f factor. A numerical hereditary bound by itself does not imply this equivariant atlas assertion: descent-fixed classes cannot simply be divided out of an ordinary representation count.

The fixed-base algebra formulation is attractive here: a deck twist changes the fixed A-action, rather than requiring a new equivariant polarization whose degree might grow with d. However, the A-linear object-presentation gate above remains unchanged.

## Projective coefficient actions

Counting ordinary GL_r representations does not automatically count projective PGL_r representations. Passing to the adjoint representation has rank r^2 and turns a quadratic exponent into a quartic one. A projective lift involves a central obstruction and twisted vector bundles on its gerbe; controlling the number of obstruction classes alone does not produce a uniform quadratic atlas for these twisted bundles. This is a separate gate from prescribed field-semilinear action.

No full finite-generation consequence is asserted.
