# Independent review of G-21

Reviewer: /root/rectangular_bridge; GPT-6 Astra Pro; effort inherited/not exposed; run CUE_GCT-20261121.

## Scope and outcome

Read the complete statement, proof, and exact-scope paragraph in work/root/g21_fragment.tex. **PASS**, conditional only on the explicitly cited R23 and R27 results, whose proofs have already been read in this run. No new rank computation was performed for this review.

## Re-derivation

The open locus where all m² quaternary cofactors are independent is nonempty by R23. The open locus where the quaternary differential has rank4m²−2m+2 is nonempty by R27. Irreducibility gives one common pencil. When this pencil is regarded in r variables with the new coefficients zero, each new coefficient block is x_k times the independent cofactor family. It has dimensionm², and different k occupy disjoint multidegrees in the new variables, also disjoint from the original block. The resulting rank is rm²−2m+2. The row/column torus preserving the permanent has effective dimension2m−2 on the generic coefficient space for every r, so this lower bound is exact. No generic smoothness statement at the zero-new-coefficient point is needed: a nonzero minor there defines a nonempty open.

In degree m, the specialized first resolution complex is C^(2m−2)→(S_r)_1^(m²)→(S_r)_m. The old relations are independent on a nonempty open, and the last map has kernel dimension exactly2m−2 by the proven image dimension. Exactness of this one graded piece follows. The degree m−1 map is the independent cofactor map; all lower source pieces vanish. This proves the stated Tor1 vanishing without an unjustified regular-sequence claim. The tensor complex is valid for any graded algebra homomorphism R→S_r, including r>m².

An optional stronger endpoint observation was sent to root: if r>=m², a general linear specialization embeds R as a polynomial coordinate subring of S_r (with equality of rings up to coordinates when r=m²). Thus S_r is flat over R and all higher Tor vanish in all degrees. This is not needed for G21's stated claim.

Checked UTC: 2026-11-21T05:16:16.443553+00:00
