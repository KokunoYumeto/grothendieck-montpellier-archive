# Fresh full review: all-variable tensor dimension

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

Complete target: agent_soergel_top_module_all_variables.md, SHA256 b5a655cbc1748433c10cb29912d07f4af929ed60c03b52314f97cec739925de1.

Result: PASS. I read the entire report and independently reconstructed the complete module application and its top-cohomology consequence. I also independently opened and read the exact primary theorem and completion contexts.

## Primary theorem and retrieval scope

Lichtenbaum's original author-uploaded article, Theorem 2, printed pp222--223, supplies parts (2), (4), (1) in the order used: nonnegative higher Tor Euler characteristics, the torsion-free equality clause for chi_1, and rigidity of Tor vanishing. Direct source turn707593017view0, https://www.researchgate.net/publication/247050802_On_the_vanishing_of_Tor_in_regular_local_rings. The web extraction loses some mathematical subscripts; I therefore also read Hochster's own Math615 Winter2012 notes, supplementary lecture April18 p169, Corollary (S. Lichtenbaum), field case(1), direct source turn707593017view1, https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/10/615W12.pdf. That statement explicitly corroborates the precise chi_i and higher-Tor indices in the equicharacteristic case used here.

I independently opened Stacks Lemmas10.97.2/10.97.3, tags00MB/00MC, direct sources turn281442546view1/turn281442546view2, and read their flatness and faithful-flatness statements and proofs. An original-article PDF download or visual audit is not claimed. These are primary published/author texts, not secondary theorem attributions.

## Complete application checks

The N-variable Koszul resolution and minimality correctly make the graded free resolution finite; the proof never assumes projective dimension at most one in higher dimension. Fraction-field rank gives its alternating free rank, and the finite-dimensional tensor complex gives chi_1=dim(V tensor Q)-rank(Q)dim(V), with the correct sign convention.

The finite-dimensional graded module V is supported at the homogeneous origin and killed by a power of the maximal ideal. Completion therefore leaves it unchanged and leaves the actual tensor complex unchanged. The completed residue field is k, so lengths coincide with k-dimensions. Every Tor has finite length.

A finite torsion-free module embeds in a finite free module by clearing denominators of a finite generating set. Flat completion preserves that injection, proving that the completed module is torsion-free over the complete power series domain. Thus Lichtenbaum's exact torsion-free equality hypothesis applies.

If equality held for a nonfree module, its last nonzero minimal free term would contribute a nonzero socle kernel after tensoring V. There is no later free term contributing boundaries. This gives nonzero last Tor, contradicting the known theorem's rigidity. The argument needs neither a general projective-freeness theorem nor an inference that Euler-zero implies acyclic without the cited rigidity.

I checked both cases for the full torsion quotient. Strictness passes through the tensor surjection if the torsion-free quotient is nonfree. If it is free, a graded left splitting and the nonzero tensor of residue generator spaces force strictness unless the torsion submodule vanishes. No bimodule splitting is asserted.

The actual top-cohomology consequence uses the independently checked positive-grading nonzero-square argument before proving that global top survives generic localization. The scalar multiplicity then equals generic rank, exactly as required. For support e and the simultaneous two-root involution tau, coprimality survives every fixed spectator coordinate, and the fixed-coordinate right actions equal their left scalars by torsion-freeness.

The note correctly leaves the descending argument to the separately assembled report. It supplies a known-theorem-based module input, not a generic K0 shortcut or an unpublished Grothendieck theorem.

No main paper or shared master log was edited.
