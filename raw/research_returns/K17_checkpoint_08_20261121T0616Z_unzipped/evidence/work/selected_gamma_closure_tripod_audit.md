# Independent audit of Gamma closure and reflection limits

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro. Date: 21 November 2026. Object: the complete `work/selected_gamma_closure_limits.md`. Verdict: **PASS for the exact closure formula, both formal compatibility examples, and the stated arithmetic reflection counterexample.** No arithmetic kernel counterexample is asserted.

## Entire proof reconstruction

The image in abelianization of the closed H- and Gamma-normal closure is precisely the closed Lambda-span of the selected generators. The Gamma defect of the chosen Delta-equivariant section is odd. Adding its closed Lambda-span makes the proposed sum stable under gamma; the same formula applied to gamma inverse, and the inclusion of gamma inverse in Lambda, gives inverse stability. Compactness makes each sum closed. This proves (GN.2). The quotient of M by that sum is the direct sum of the omitted even torsion and the quotient of odd torsion by the section defect. The inclusion of torsion gives the equivariant quotient identification, although its displayed coordinates use the chosen section. Finally, a nontrivial pro-p quotient has a nontrivial finite p-group quotient, hence a nontrivial abelian quotient. Thus zero abelianization implies the quotient is trivial, proving both directions of (GN.4) without a finite-generation assumption.

The graph-section calculation is exact over Z_p: gamma times s_1(1) is gamma X, while s_1(gamma) is gamma X+Y. Its defect is therefore -Y, independently of alpha. This section recovers the entire omitted cyclic odd summand, whereas the zero-graph section recovers none. There is no implication from this section-dependent generation fact to arithmetic nonvanishing.

The first group example is valid. The automorphisms phi_t compose additively and commute with generator inversion. Their action on abelianization is the indicated unipotent shear. The map to Z_p squared is injective on the chosen procyclic factor and all its conjugates under Gamma, while the Gamma-normal quotient kills x after killing y. The commutator has nonzero lowest Magnus coefficient. This proves that restriction faithfulness does not pass to the generated normal closure.

The stronger model preserves the additional structures claimed. The compact orbit basis of the free kernel has abelianization the stated finite free Lambda module, by its explicit universal property. Adding the procyclic free factor produces exactly the cyclic odd torsion summand. The actions of Gamma by shifts and alpha powers, and of Delta by Teichmuller powers, are continuous, commute, and have the stated orders. The Delta power maps compose exactly on each free generator, so there is no missing nonlinear character correction.

The target map is well-defined in every finite weight quotient. Finitely many bounded logarithms and their brackets lie in a bounded BCH-stable lattice after clearing the finitely many nilpotence-class denominators. Its group closure is pro-p, which permits the free pro-p universal property. The displayed formulas give exact equivariance. The Vandermonde argument spans the full target abelianization; induction in the lower central series then gives Zariski density in the entire finite nilpotent target.

For any permitted Q factor, its first nonzero Magnus coefficient lies in a finite direct sum of completed tensor powers of the rank-one Lambda modules. The linear target coordinates evaluate the corresponding bounded power series on the odd-weight grid. Higher source degree cannot contribute to this first target length. Repeated one-variable analytic uniqueness therefore forces a nonzero coefficient to survive. This argument only uses the free quotient coordinates and is unchanged by graph terms in the killed y factor or higher nonlinear changes of the chosen lifts. Thus all the claimed Q factors are faithful.

The chosen graph section nevertheless has Gamma-normal closure all of H by (GN.4), while the nonidentity y maps to 1. Its actual companion error is the identity, so its cubic numerator vanishes. This is a formal model with the stated free-group, Iwasawa-module, character, equivariance and dense-target properties. It proves the logical limitation without claiming a Galois realization.

For clarity concerning the infinite-rank free-basis step, one can justify the cited prior lemma without finite-rank Hopficity. The induced map of free pro-p groups is surjective by the Frattini criterion and splits because the target is free. If its nontrivial kernel had zero abelianized coinvariants, the pro-p fixed-vector argument on its discrete H1 would contradict the five-term exact sequence and the target's cohomological dimension one. Hence a surjective map inducing the abelianization isomorphism has trivial kernel here. This is the same compact projectivity argument used in the earlier selected-factor proof.

The reflection bookkeeping is also correct. Its direction is odd-zero implies reflected-even-zero; it cannot be reversed. At p=37, the Bernoulli index32 gives the nonzero odd eigenspace A^[5], while Vandiver gives zero A^[32]. The displayed factorization of B32 is consistent with that irregular index. Applying the character involution twice adds no new component. The selected-pair condition uses E intersect (2-E), whose integer interval is exactly the stated j=-12 through13 before reduction modulo p-1. Residue collisions must be handled as set operations modulo p-1, as the note expressly says.

## Fresh primary-source check

I reread Sharifi's complete Lemma2.1 and its proof, printed pp3–4 of `work/sharifi_galstr.txt` (the corresponding author PDF is already archived). The proof uses only a pro-p group with a coprime cyclic action and its separated lower central series. It preserves an abelian character projection and stays within a chosen stable open subgroup. Its use for convergent eigenlifts in the formal model is therefore valid; no arithmetic hypothesis is silently imported into that example.

## Scope

This audit establishes the limitations of the proposed normal-closure and reflection iterations. It proves neither arithmetic failure of faithfulness nor new arithmetic Triple-NV. The strengthened formal countermodel shows that the already checked algebraic inputs, even together with faithfulness of every allowed Q factor, do not alone remove the remaining arithmetic gate.

Reviewed source SHA-256: `1384ea1e3926c93fcbe12f85b37fa3daec619e33ad93e7cc84a5dc16c9651ffd`.
