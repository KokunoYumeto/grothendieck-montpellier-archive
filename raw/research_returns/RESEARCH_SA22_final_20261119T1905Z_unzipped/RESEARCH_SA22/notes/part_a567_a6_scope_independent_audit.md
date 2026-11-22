# Independent audit of the A6 arithmetic-scope supplement

Audit date: 2026-11-19. Auditor: GPT-6 Astra, Part A567. The current complete fragment `sections/part_a6_scope_supplement.tex` was read independently. This is a proof and source-hypothesis audit, not a new numerical or exhaustive program run. No existing TeX was edited.

## Source hypotheses actually reopened

Hoshi, *The exactness of the log homotopy sequence*, RIMS1558, https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf, was reopened through the web source and its exact statements read again. Corollary 3.9 (printed pp.31–32; retrieved lines2451–2478; web reference turn741543763view0) assumes an fs log base whose underlying scheme is a complete local spectrum, a log-regular fs total space, and a proper morphism. It imposes no residue-characteristic-zero hypothesis. The strict closed log fibre is exactly the fibre carrying the pulled-back log structure. Proposition A.10 (printed pp.57–58; retrieved lines5201–5207 and5283–5329; web reference turn741543763view1) identifies Kummer-etale covers with finite etale covers of the interior tame at all codimension-one boundary points. The proof explicitly identifies the log structure of a log-regular scheme with its divisorial structure from the interior. The noetherian hypotheses in the supplement are sufficient for these applications. The broader complete-local-base comparison sentence is therefore supported. Page indices in the web extractor are zero-based; the printed page numbers are used in the manuscript.

## A6-tame-specialization

The properness argument is valid without a common resolution: for any boundary DVR of a second proper model, its generic point maps to the common interior and the valuative criterion extends this map to the first model. A boundary-log section pulls back to a nonzero DVR element, giving the required morphism to the divisorial log trait. Pullback of a Kummer-etale cover and Proposition A.10 then imply tame ramification at this valuation. The symmetric argument proves equality of the two full subcategories of finite etale covers of the fixed interior. Full faithfulness establishes the normalized comparison and cocycle statements, with the stated contravariant pullback direction.

Geometric connectedness implies surjectivity onto the tame base Galois group through the connected-cover criterion. The compatible-root description over the maximal unramified extension and Hensel extraction of prime-to-residue-characteristic roots give the asserted uniformizer-framed section. This concerns G_F^t, not all of G_F, and the supplement correctly refrains from identifying the kernel with the full geometric fundamental group. Existing-model hypotheses remain explicit; no mixed-characteristic resolution theorem is assumed.

## Counterexamples and node character

For A6-frobenius-counterexample, the relative Frobenius is a k-morphism because constants remain fixed while the affine coordinate is squared; it is finite, radicial and surjective. The cross-ratio orbit exclusions reduce to nonzero polynomials of degree at most three for an element of degree four. Its order15 and the prime-to2 cyclotomic lift establish the asserted characteristic-zero good-reduction realizations. I checked these algebraic deductions by hand; C owns the separate finite certificate, which I did not rerun.

For A6-wild-counterexample, at the generic special-fibre DVR the polynomial T^2-2 is Eisenstein, the extension is a DVR with uniformizer sqrt(2), and ramification index2 is wild in residue characteristic2. The connected constant cover is nonetheless etale over the characteristic-zero interior. Thus it cannot belong to the Kummer-etale category.

For A6-node-character, interchanging branches in xy=c tau inverts the oriented inertia generator, so its arithmetic character is cyclotomic times the branch-swap character. The displayed nodal cubic has only the stated affine singularity, is smooth at infinity, and the normalization parametrization has no base point. The two node preimages are ±i; conjugation swaps them while cyclotomic conjugation also acts by -1, giving product +1. The invariant tensor and stability claim are valid. This is the node-edge inertia character, distinct from the Dehn-twist kernel used elsewhere.

## Verdict

No substantive mathematical gap found. The source equivalence hypotheses match the stated existing-model theorem. The positive-residue-characteristic limitations, wild-cover exclusion, Frobenius ambiguity, and nonsplit-node branch sign are preserved explicitly. This audit supplies independent proof verification, not a claim that arbitrary mixed-characteristic compactifications or strict anabelian reconstruction exist.
