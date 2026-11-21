# Author checks for the actual cubic twisted obstruction

Author: `/root/archive_kummer`, GPT-6 Astra Pro. Date: 21 November 2026.

## Scope and saved objects

The complete mathematical source is `work/cubic_twisted_obstruction_section.tex`, final SHA256 `46013fd13c4f54c9969ce5dae1774452a342330b311af422d71d4634af9f1994`. The initial whole-read version had hash `62bf8ed7ab7dcf1b9bfcf7fc941879161be354a020a63cb60a6c7450b50fa06f`; the only subsequent addition is the explicitly proved localized H1 representative paragraph described below. The new bibliography fragment is `work/cubic_twisted_bibliography.tex`, SHA256 `c5172393f85053fc16bbc6b7a2ad65f11a8e30c577707142d79dc19c6f96181f`.

Finding IDs: **K17-CUBIC-TRIANGULAR**, **K17-CUBIC-TWISTED**, **K17-CUBIC-CYCLOTOMIC-INPUTS**. Author whole-proof verdict: **PASS at the stated algebraic and cochain scopes; no arithmetic Triple-NV is asserted.** The parent independently passed all three complete proofs and CT.11--14. Tripod independently passed the full section and then the final added paragraph, recording the final hash in `work/cubic_uppertriangular_tripod_audit.md` and check TC107. No arithmetic nonvanishing was certified by either review.

The prior algebraic note `work/cubic_uppertriangular_bridge.md` was read back completely. Its final wording clarification specifies that h_i(z_i) is the bounded series in z_i-1 after the stated involution; hash `f16bd65d4a5eee982f6dfed7e7cf02e059f9b93d3ae4e5a4d6e575f464708af0`. The parent and tripod independently passed its full argument. Tripod's complete audit and denominator lemma were both read in full here: `work/cubic_uppertriangular_tripod_audit.md`, `work/cubic_compact_denominator_lemma.md` (latter hash `8dfcbe259ec8bbc950830210c259915c8efc1827891553d694ff06332b10b7a4`).

## Whole-proof reconstruction

1. The actual degree-two extension determines the two proper-pair coordinates uniquely by applying an annihilator and dividing by its nonzero value on the relevant pair product. The pair products remain nonconstant on the full triple divisor, so the denominators are nonzero even when an odd root equals an even root numerically. No even cyclicity or Pair-NV is used for existence of these coordinates.

2. The matrix-bracket central functional retains the mixed [Q,Tplus] terms. It respects Jacobi, has the exact triple Gamma eigenvalue and Delta character, and pushes out the actual degree-three module. The two-term cyclic resolution gives the literal companion-error scalar as its Ext class, including repeated roots. No derivative or unsupported semisimplicity claim occurs.

3. Rescaling the first and third coordinates by the two proper-pair denominators clears those denominators in the pair maps. A common power of p clears all remaining rational basis and degree-three exponential/logarithm denominators. It scales the central residue by a nonzero factor only.

4. The pair **group** coordinates include the half-products of the first coordinates. Direct multiplication gives CT.11 and the precise signs dB=-cup. Their Leibniz differentials cancel in CT.9. The central coefficient module has the product character, not trivial action.

5. The rank-four coefficient extension was independently multiplied through: L and R0 are representations, the top-right line in M2(A) has character chi1*chi2*chi3, kappa'=U R0^{-1} modulo that line is a cocycle, and CT.13 equals c times the top-right unit. The (1,4) subgroup is central in the unipotent group and normal, with nontrivial character action, in the diagonal semidirect product.

6. CT.14 is algebraic flat localization of an A-module complex. It is not a claim about all continuous K-valued cochains. A zero localized class has one denominator and therefore gives a bounded matrix lift. Its logarithm respects assigned degrees 1/2/3; exact Delta parity kills a possible odd central term on even torsion lifts. Only three completed tensor degrees occur. The resulting extension of psi makes the actual companion scalar zero.

7. Conversely, a zero companion scalar permits central value zero on the finite cyclic conjugate basis. The final relation is compatible exactly by that scalar's vanishing, including repeated roots. A finite R-basis of Q supplies a Gamma-equivariant section with a single p-denominator, because the actual compact Lie lattice has a continuous Lambda action. Thus the full matrix lift has one common denominator and gives a cochain in the algebraically localized complex. No infinite sequence of independently growing denominators is hidden in the argument.

8. Hasse's unit-index theorem and the valuation of the norm p make the relevant finite-level cyclotomic Kummer inputs nonzero. The inflation kernel has odd cyclotomic Delta character, whereas these inputs have even character. The earlier explicit norm transfer therefore supplies nonzero rank-one multipliers and kills all Iwasawa torsion. The integral formal coordinate change for z3 proves each multiplier stays nonzero on the triple divisor. The dual variables and character are u^3/alpha and omega^(3-a).

9. At tripod's suggestion, added and read back the exact localized H1 input comparison. Once restrictions to H match, the difference eta inflates from Gamma times Delta. Subtracting the coboundary of eta(gamma)/(z_i-1) kills Gamma. The commuting gamma/delta cocycle identity then gives (z_i-1)eta(delta)=0, hence kills Delta as well. This uses one denominator and does not change the specified pair defining system. Tripod independently checked this final paragraph; parent was sent its exact text location and hash.

## Primary source actually inspected

Sharifi's complete Iwasawa notes, Theorem4.3.3 and its full proof pp108–109, Proposition6.1.5 and its full proof p152, were read during the preceding algebraic construction. Tripod independently repeated those complete reads. The exact author URL was verified in that construction.

For the final cochain section, freshly opened the primary author PDF `https://www.math.ucla.edu/~sharifi/publ/augmentation.pdf` (web reference `turn879738362view0`) and read the local complete text of Definitions3.1.3 and3.2.1–2, all of Section3.3 with its proofs, and all of Section4.1 through Theorem4.1.2 and its proof, pp22–29. The important scope distinction is explicit in the source: the general UGMA definition allows arbitrary twisted coordinate modules; only after Definition3.2.2 does the paper restrict the later proper-system/Bockstein statements to one nontrivial module and untwisted outer coordinates. The final section states this distinction accurately and proves its own twisted identity.

## Typesetting verification actually run

A standalone wrapper `work/cubic_twisted_draft.tex` was compiled in draft mode. The first attempt could not locate the standard TeX package tree. Repeating with the existing local pdflatex format and explicit standard TEXINPUTS/TFMFONTS succeeded with exit code0 and five pages processed. The remaining log warnings concern first-pass/external references and the environment's unused font map in draft mode. No mathematical TeX error or overfull-box warning was reported. No PDF visual verification is claimed.

## Boundaries retained

No published Bockstein comparison is silently applied outside its printed hypotheses. The finite rank-four coefficient extension is proved explicitly; it is not identified with an augmentation-graded Iwasawa module having a vanishing cokernel. No arithmetic nonzero-support assertion, new Triple-NV instance, or new full-kernel theorem follows from this note alone.

The parent's purely editorial four-heading change to the selected-pair theorem was not overwritten; its reported current hash was verified as `f159ab038c70310d7674cae78a8e34d94935451e06794f12ca033889ce89d8c5`.
