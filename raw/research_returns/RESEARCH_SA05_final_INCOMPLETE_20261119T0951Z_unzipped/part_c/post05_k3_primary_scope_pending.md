# Post-checkpoint-04 K3 gate investigation — pending primary verification

Recorded 2026-11-19 at approximately 06:32 UTC during the checkpoint-05 main-file freeze. This note does not change any theorem or status in the integrated manuscript.

## Scope of the remaining gate

For a general complex K3 surface, the determinant projector on the appropriate exterior power of the transcendental motive remains the actual Chow-vanishing obstruction. The new unconditional finite criterion and uniform recursive arity bound reduce the number of tests, but do not establish the required rational equivalences. Composition-nilpotence of the determinant projector would imply its vanishing because it is idempotent; therefore merely renaming this as a nilpotence problem does not make a smaller established condition.

## Fresh literature check

A current secondary index, https://kisonecat.github.io/openai-math/algebraic-and-complex-geometry.html, lists an October 3, 2026 manuscript entitled *Algebraicity of Kuga–Satake Correspondences for K3 Surfaces* and an October 4, 2026 manuscript entitled *The rational Hodge conjecture for products of K3 surfaces*. Its corresponding GitHub file pages are:

- https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/manuscript.pdf
- https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/hodge-conjecture-products-k3.pdf

The pages were opened. The current file sizes are only about 3.63 KB and 3.66 KB, respectively, which makes a withdrawal or replacement notice a possibility. The contents must be read before either claim can be treated as a current theorem. Direct web retrieval of the raw October 3 PDF returned a DisabledError; a separate local retrieval is in progress. No primary theorem from either item has yet been used in the manuscript.

Other search checks did not supply a general finite-dimensionality proof. Pedrini's *On the finite dimensionality of a K3 surface* is the June 2011 arXiv item 1106.1115, despite misleading recent secondary indexing. Bolognesi–Laterveer, arXiv:2310.11981v2, Theorem 3.1 and Section 6 concern specified families with an order-three automorphism; the hypotheses are not removed. The recent hyper-Kummer construction likewise concerns special families. The complete proofs of those family statements have not been newly audited during this interval, so no new family theorem is asserted here.

## What algebraic Kuga–Satake would and would not supply

Even a valid theorem establishing an algebraic Kuga–Satake correspondence and an inverse modulo homological equivalence would not by itself produce a splitting in the Chow category. Lifting the homological splitting requires control of the homologically trivial error correspondence. The existing finite-dimensionality argument becomes circular if it invokes general Kimura nilpotence to eliminate that error. A primary algebraicity theorem could remove the algebraicity branch of this obstruction in its precise field and polarization scope, but it would leave the Chow-lifting branch unless its proof supplies a stronger rational-equivalence statement.

## Failed or unproved approaches retained

1. A uniform bound on the arity of cohomological relations does not bound the complexity of rational equivalences witnessing their Chow vanishing. Thus specialization to known finite-dimensional fibres does not presently imply generic vanishing.
2. At the first exterior-power relation, partial trace has the vanishing dimension factor. Contraction does not reduce the determinant relation to a lower-degree identity with a nonzero scalar coefficient.
3. Nilpotence for the endomorphism ring of the original K3 motive does not automatically imply nilpotence in all tensor powers. No such implication is used.
4. Possible consequences of zero-cycle commutativity concern an action on selected Chow groups; without a proof controlling all base changes and all Chow groups, they do not annihilate the exterior-power motive by Manin's identity principle.

The general K3 Chow-vanishing gate remains open in this note. A primary-source status update will be appended after the current PDFs are read.

## Primary-source status resolved at 06:33 UTC

Both current primary PDFs were successfully downloaded and their complete one-page contents read. **Both papers were withdrawn on October 6, 2026.** Each notice identifies an adaptation of the flawed stabilization-trace construction from *Algebraicity of Weil classes on split abelian eightfolds*. The sign error prevents the required signed-double-point cancellation. The October 3 notice states that its claimed algebraicity theorem is unproved; the October 4 notice states the same for its claimed rational Hodge theorem for products of projective K3 surfaces. Each explicitly distinguishes failure of the proof from falsity of the mathematical statement. Repository revision recorded in both notices: `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

The primary withdrawal notices are archived as `part_c/sources/k3_ks_oct3_2026_current.pdf` and `part_c/sources/k3_hodge_oct4_2026_current.pdf`, with complete text extractions alongside them. The October 3 PDF has 3,715 bytes and SHA-256 `8e46fd4f5d330e8befe0a8a81e2bdd405d1105afb09dc705cd157cb923d0f8e8`; the October 4 PDF has 3,748 bytes and SHA-256 `48515a3987802b299886e728a6e9f8394ccb2a359754259de64ce9b88a4a281b`. Exact download metadata are retained in `part_c/sources/k3_oct2026_withdrawal_fetch.json`.

**Outcome:** the secondary index does not supply a valid new algebraic Kuga–Satake or all-products Hodge theorem. No integrated theorem is modified, and the general K3 Chow gate remains open. The earlier conditional algebraicity-or-Chow-lifting discussion should not be strengthened on the basis of these withdrawn items.
