# Independent final audit of C5.04, C5.05, C5.07, C5.08

Auditor: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/homotopy_levels`; 19 November 2026. This records actual targeted checks, not an additional theorem or an independent source attribution.

I read the final sections in `C_sections.tex`, the complete Hurewicz example in `C5_Hurewicz_C.tex` insofar as it bears on the matrix, and the transcriptions of 150/051, /062, /063, /067, /070, and /071. I also visually opened all six corresponding primary-scan PNGs in `work/literature_C`. The connected-component wording on /070–071 is clear. The two readings of /051(d) must remain distinguished: an attempted consequence versus an extra manifold-face axiom. The uncertain source letter on /063(d) is handled in the paper by the typed source interpretation from /062; no new palaeographic certainty is claimed here.

## C5.04: passes the full hypothesis check

The compact square version satisfies the surrounding hypotheses, including properness of every source. The square is locally a plane or half-plane, including at its vertices; since `F × R` is a five-manifold, `F × [0,1]^2` is a six-manifold with boundary `F × S^1`. Each specified collective incoming face is closed and properly embedded, the two face collars form the explicit product coordinates, their intersection is the stated source inverse image, and projection control holds. The source `s12` is a product Hurewicz bundle with compact fibre `F ⨿ F`; the remaining source maps have point targets and compact domains. The lower interval at a corner is the three-element chain, so the order condition also holds.

The nonmanifold-face conclusion is valid. At an interval-interior point, `F × [0,1]` is a five-manifold. At an interval endpoint its local homology vanishes in every degree. If it were a manifold with boundary, its entire intrinsic boundary would therefore be `F × {0,1}`, which is not a manifold. This refutes the attempted inference in /067 and the consequence reading of /051(d), without claiming to satisfy the alternate extra axiom that every flag space is already a manifold.

## C5.05: passes after the identified boundary-regularity clarification

The PL cancellation argument uses the product PL structure, not a topological cancellation assertion. A product simplex over a top-dimensional simplex of the Euclidean factor has the same normal PL link as the relevant vertex of the fibre. The manifold link criterion therefore gives the fibre's PL manifold structure. The stated PL-bundle hypothesis is stronger than Hurewicz fibrancy, as required.

The smooth argument must explicitly establish submersion on the vertical corner faces before using a corner submersion/Ehresmann argument. In the full incidence system this follows from the existing hypotheses, rather than becoming an extra conclusion assumed in advance. For `i < k < j`, projection control gives

`sij|Σikj = sik ∘ (skj|Σikj)`.

The restricted second map to `Σik` is a submersion by the horizontal pullback and product-collar condition, and the first map is a submersion by the regular-source assumption. Iterating gives the same statement on every vertical corner stratum. Horizontal lifts can then be chosen tangent to all vertical faces; local partitions of unity preserve those linear tangency conditions, and properness permits their flows over a sufficiently small base chart. The horizontal base-boundary coordinates are handled by the supplied product collars. This proves the intended corner-bundle conclusion. An isolated proper smooth submersion with only horizontal behavior would not suffice; this logical step was sent to the root and C owner for insertion.

The boundary decomposition into horizontal lower-label faces and vertical intermediate-label faces then follows from the full incoming-face decomposition and the source inverse-image identities. It does not conflate the intrinsic boundary of the fibre with the whole boundary of the arrow space.

## C5.07: passes, including the full Hurewicz property

The pseudoarc argument proves that every path in the remainder is constant: a nonconstant path image would express an indecomposable subcontinuum as a finite union of proper continua. The ray construction is compact and connected, and its cluster set is precisely the chosen nondegenerate continuum. A path entering the ray from the remainder would have ray parameter tending to infinity. The intermediate value theorem forces every sufficiently short path interval to visit an entire ray tail; continuity would force that whole tail to converge to a single remainder point, contradicting its cluster set. Thus the specified source point has singleton path component.

The strict arrow is an isolated clopen component of the closed relation. Both projections are proper; the target is locally embedded and its one strict target germ is genuinely collared at the endpoint of the ray. The source lifting proof works for every parameter space: split it into the clopen inverse image of the strict arrow and its complement, then use the constant strict lift and the diagonal lift. This is Hurewicz lifting, not merely path lifting. Transversality is vacuous on the strict component because its source is outside the target collar, and is the identity on the diagonal. The single connected component is open and has finite covering dimension. The extra monomorphism condition for distinct components is vacuous. The example therefore refutes the literal connected-component scope of /070–071 even with all the additional hypotheses listed in the section.

## C5.08: the manifold/category argument passes

The identity section is closed as an equalizer in a Hausdorff arrow space. It is open because target-local injectivity, together with continuity of the identity section, makes a sufficiently small target chart contain only the identities over a smaller base neighborhood. Strict arrows are consequently clopen, so source lifts preserve strictness and keep their target in the same component.

For a hypothetical strict arrow inside one manifold component, source path lifting moves its source into an interior coordinate ball. The Hurewicz lifting property applied to a contraction of that ball gives a continuous source section. After shrinking, its image lies in a target-injective arrow chart; composing with the target gives an injection of an open `n`-ball into an `n`-dimensional target corner chart. Invariance of domain forces its image to be open in Euclidean `n`-space and hence to avoid the orthant boundary. Its target image is therefore open in the component, contradicting the assumed locally nowhere-dense strict target germ. Dimension zero is covered directly. The proof is valid for manifolds with boundary and corners.

Transitivity follows by source lifting to align middle objects. If component arrows exist in both directions, the two resulting composites lie within components and must be identities; the arrows are inverse, contradicting the assumption that all invertibles are identities unless the components coincide. No thinness is used in this argument. The later monomorphism conclusion correctly returns to ordered spaces with totally ordered lower intervals.

For the PL-polyhedron extension, the target local embedding must explicitly be PL, so its locally rare image has a compatible local triangulation of dimension at most `n−1`. The compact-subball/Baire argument then excludes an embedded open `n`-ball in that image. This precision was sent for insertion. The matrix correctly distinguishes raw proper Hurewicz fibrancy, regular PL bundles, regular smooth sources, and the stronger full-face product-triviality hypothesis. The raw PL/smooth Hurewicz example has manifold arrow spaces as well as manifold objects, so it remains a counterexample under the stronger reading of /051(d).

## Outcome

No remaining mathematical gap was found in C5.04, C5.07, or the general manifold/category part of C5.08. C5.05 and the PL extension of C5.08 require the two explicit clarifications above; both have been transmitted for integration. The examples and positive statements otherwise have the claimed manuscript scope.
