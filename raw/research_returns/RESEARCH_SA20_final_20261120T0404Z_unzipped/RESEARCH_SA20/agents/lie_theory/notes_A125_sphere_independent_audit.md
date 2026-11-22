# Independent audit of A.125

**Auditor:** `/root/lie_theory`  
**Completed:** 2026-11-19 17:23 UTC  
**Outcome:** **PASS for the repaired draft**, including its TOP intermediate path and its explicit boundary-jet triangle.  
**Draft:** `agents/singularities_duality/logs/A125_sphere_draft.tex`, read in full; revised category passage and jet passage reread at 17:22 UTC.

## Restriction fibration and frame calculation

Cerf's original Cartan seminar, *Théorèmes de fibration des espaces de plongements. Applications* (1962/63), Theorem 1, printed p.8-01, gives the restriction fibration. Section 2, item 3, p.8-05, covers a target with boundary and prescribed boundary incidences. Its application to a closed embedded inner three-ball is valid. The local extensions can be supported in the interior of the outer ball, so they restrict to diffeomorphisms of that ball without imposing a new outer-boundary condition.

The finite-family shrinking argument is valid in the stated C-infinity topology. For a compact parameter family, the minimum singular value of the derivative at the center has a positive common lower bound, the derivative is uniformly continuous, and the affine images fit inside the open outer ball after a common sufficiently small shrink. The error from the affine map has Lipschitz constant strictly smaller than the affine map's minimum singular value. Therefore every straight interpolation is injective and immersive. Convexity keeps its image inside the outer ball. Moving the centers and using polar decomposition also preserve embeddings after the same shrink is made sufficiently small.

For a based loop the center and derivative at its basepoint are zero and the identity, respectively. Thus the only basepoint motion is the radial shrink of the standard inclusion. At the final rotation loop, the same radial shrink is the basepoint motion. Their transports cancel. The loops in the embedding space are therefore represented by restrictions of actual rotation loops in the diffeomorphism group. This proves the required surjection on fundamental groups without imposing a compact-target hypothesis on the interior of the ball.

Path connectedness of the embedding space plus the restriction fibration gives surjectivity of restriction. Cerf's three-ball connectedness theorem, as explicitly stated in Laudenbach, Chapter I, Theorem 1.2, printed p.8, then makes the stabilizer of the pointwise fixed inner ball path connected by the exact sequence.

## Inner boundary jets and relative isotopies

Fixing the inner ball pointwise gives identity infinite jets on its boundary. Conversely, identity infinite jets on the inner boundary of an annulus allow smooth extension by the identity over the ball. The inverse has the same property. Restriction and extension preserve the smooth mapping-space topologies, so they also preserve paths. This is an identity-jet condition, not an assertion that the annulus map fixes an open collar.

A bottom-fixed annulus diffeomorphism preserves orientation, and its top restriction therefore belongs to the identity component of the orientation-preserving two-sphere diffeomorphism group. The displayed cutoff isotopy removes that top restriction while preserving the bottom.

I visually inspected Cerf's original p.8-06. The range is **i >= 0**, despite an OCR error that can remove the equality bar. The exact first arrow in Proposition 1 is

`Diff(A; all boundary jets) -> Diff(A; boundary pointwise; jets on M)`.

Its special case gives the composite to `Diff(A; boundary pointwise)`. The repaired draft explicitly uses the two isomorphisms and two-out-of-three to deduce the needed assertion for the intermediate inclusion. This is correct on components. It produces an annulus map extending to the pointwise-inner-ball stabilizer. Contracting there and restricting gives the desired bottom-fixed path.

The original scan inspected is saved as `source_external/lie_theory/cerf1962_p8_06_audit.png`. Full original PDF/text read in `agents/singularities_duality/logs/cerf_cartan1962.pdf` and `.txt`. Its original source is https://www.numdam.org/item/SHC_1962-1963__15__A2_0/ .

## Repaired PL passage

The initial version spoke of a jointly PL isotopy ending at a smooth map in the fixed coordinates. Root correctly requested avoiding that unnecessary literal category identification. The revised proof first obtains an unrestricted TOP path from the given PL map to a smooth map. Along this path each boundary component stays fixed as a component. Correcting its bottom by the product of the inverse bottom restriction with the identity interval gives a TOP path with fixed bottom and smooth final map. The smooth assertion contracts that endpoint.

The original PL map and the identity are thus TOP-isotopic. Laudenbach, Chapter I, Section 1, printed pp.7–8, explicitly supplies injectivity on components from PL to TOP for a compact three-manifold. It consequently gives a jointly PL isotopy between these two actual PL endpoints.

For that PL isotopy, the total bottom family `(x,s) -> (c_s(x),s)` is a PL homeomorphism. Its inverse is PL. Taking its product with the collar coordinate and composing with the total PL isotopy gives the displayed jointly PL bottom correction. Both endpoint bottom maps are the identity, so the endpoints remain unchanged. This is a valid relative conclusion from an unrestricted comparison.

Full Laudenbach original read: `agents/singularities_duality/logs/laudenbach1974.pdf` and `.txt`; printed pp.7–9. Original URL: https://smf.emath.fr/system/files/filepdf/AST_1974__12__1_0.pdf .

## Scope

The argument proves the asserted two-sphere component computation. The transfers to definable models and arbitrary real closed fields use exactly the prior component comparison results A.113 and A.115. It does not establish a higher-parameter equivalence or an equivariant analogue for the projective plane. No finite experiment or numerical computation is involved.
