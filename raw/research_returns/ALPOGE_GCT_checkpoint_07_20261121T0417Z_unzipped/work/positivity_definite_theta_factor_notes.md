# P-F51: exact definite-unitary theta factor

## Result and scope

The actual positive factor in P-F46, the three-component theta vector of the positive (E_6) lattice, is the ordinary theta integral of an explicitly normalized nonnegative lattice-class selector on a definite (U(3)) quotient. Its right group is the derived split group (SU(1,1)=SL_2), with the action fixed by the canonical orthogonal Schrödinger model. The exact orthogonal/unitary seesaw sits inside the same (Sp_{12}).

This identifies a concrete definite-unitary source for the actual input, including the lattice, coset level, finite Weil type, Haar normalization, and real factor (y^{3/2}). It does not choose the additional central splitting needed for the full (U(1,1)), or identify the resulting function with a selected irreducible representation in the supplied iterated lift. Multiplication by (delta^{-1}) and the regularized multiplicative lift remain separate operations. The latter outputs the single cubic discriminant, not every graded invariant space.

## Whole-proof self-check, 2026-11-21 02:56 UTC

Read the complete written proof in two bounded output chunks. Reconstructed the simultaneous (A_2)-rotation preserving the actual glue, Hermitian trace formula, inverse-different integrality and duality, exact alternating tensor form, algebraic equality (SU(J)=SL_2), and both mutual-centralizer statements after scalar extension. Checked the canonical commuting orthogonal/derived action, the finite lattice-and-coset stabilizer, and both finite Weil matrices. Reconstructed compactness/openness and positive finite measure of the identity double class, invariance of its theta kernel, and the exact integral without a class-number factor. Finally recalculated the real dilation and the rational finite-support condition. Absolute convergence follows from the Gaussian absolute-value series and compact selector support.

No mathematical gap was found. Root requested two precision edits, both applied before the final log: define the Hermitian dual using the inverse different, and distinguish Gaussian absolute-value convergence from positivity at nonzero real part of (	au). Also defined (K_p) and clarified that the HLS theta constructions are applied to our explicitly fixed actions; no unproved compatibility of a full-unitary splitting is used.

## Primary sources actually read

* Kudla, *Notes on the local theta correspondence*, Definition II.4.2 and Proposition II.4.3, printed pp. 37–38, plus the canonical orthogonal splitting p. 39 and the seesaw definition IV.1 p. 59. These are used for the finite-place action; the needed archimedean value is computed directly. URL: https://www.math.toronto.edu/~skudla/castle.pdf . Fresh refs: `turn448348982view0`, `turn699449633view0`–`turn699449633view3`.
* Harris–Li–Sun, *Theta correspondences for close unitary groups*, equation (1.1.1), printed p. 3, and equations (1.2.1)–(1.2.5), p. 4. The theta construction and necessary full-unitary character restrictions are used, not any conditional irreducibility claim. URL: https://webusers.imj-prg.fr/~michael.harris/closeunitaryweb.pdf . Fresh refs: `turn705412043view0`, `turn578538582view0`, `turn578538582view1`. The actual rendered p. 4 was visually inspected at 02:56 UTC.
* Scheithauer, *The Weil representation of SL2(Z) and some applications*, Proposition 4.3, printed p. 14, states the principal-congruence kernel. The convention is dual to the displayed theta convention, which leaves the kernel unchanged. URL: https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/scheithauer/publications/Weil_representation.pdf . Fresh refs: `turn193839044view1`, `turn904553565view0`, `turn904553565view1`. The actual rendered p. 14 was visually inspected at 02:56 UTC.
* Supplied `work/ALPOGE_remark.txt` reread in full at approximately 02:47 UTC: item 8 uses iterated lifts between totally definite unitary groups; the note does not specify the additional spaces, vectors, or splitting characters that would identify that construction with this exact factor. The explicit difference in right-hand signature is not asserted to prohibit other seesaw comparisons.

## Peer status

Root reports a complete mathematical read and no gap, with source audit underway. At approximately 02:58 UTC, plethysm reported a completed independent whole-proof and exact-primary review: PASS, including the final inverse-different convention, all centralizers, the fixed actions, the compact selector, and exact normalization. Plethysm records that actual review in its own audit log; this sentence reports the received result rather than claiming another review by bridges.
