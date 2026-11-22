# Whole-proof review: K-017, K-019 and K-020

- Date: 2026-11-21, 22:18 UTC.
- Reviewer: `/root`, GPT-6 Astra Pro; effort not exposed; GCT_POS.
- Type: targeted proof check (entire proofs), complete verifier reading and exact computation replay for K-019/K-020.
- Outcome: **PASS**, within the explicit limits below.

## K-017

I read the whole support/one-parameter-subgroup proof. Distinct factor weights prove freeness. The displayed traceless integer weights give strictly positive weight on every vector of the complete fixed support, so the instability claim concerns the entire fixed subspace. The auxiliary Smith form is not required for this conclusion. The finite 2-adic diagnostics are recorded as diagnostics only. Their logical role is to disprove chain dominance in that tested dimension; they do not exclude every valuation strategy. K-018 separately disproves the proposed bound even after polystability is required.

## K-019

I read the whole proof and local-factor discussion, and the entire verifier. The exact n=9 incidence and Lie computations were already independently rebuilt in the root K-018 verifier. The present replay additionally confirms complete fixed-tensor counts 25 and 30 modulo512 and256, fixed special-linear Lie counts24 and26, and consequently smooth fixed tangent dimensions1 and4. The Lie minor has rank241 modulo10007; the scalar kernel bounds it above by241 over characteristic zero. The simple spectra and antipodal-free factor satisfy the fully checked K-012 criterion, giving the full stabilizer and trivial effective special-linear stabilizer. The semigroup argument gives density one. The local factor uses the same point-pullback convention as K-014/P-F23; it is not a global residue sum.

## K-020

I read the entire gluing and spectral-induction proof, re-read K-016 in full, and read/replayed `verify_gadget_stabilizer_data.py`. Both pair-deletion coverage conditions, the absence of two-boundary edges, invariant mass interval, rank190 Lie minor, complete22-edge spectral support, and unique antipodal B-pair passed exactly.

The Lie gluing argument correctly first removes all off-block entries by coefficients with two old or two new coordinates. The two remaining tensor variations have intersection only in the boundary triple, where neither can contribute. Boundary scalar compatibility then restores the old removed edge. For the finite stabilizer, the boundary character has exact order256 because its unique rational coefficient vector has an odd numerator over256. Reducing all weights modulo the old period identifies a primitive old determinant character; collapsing the gadget blocks proves complete support and simplicity, while antipodal pairs are confined to the refined block. The dimension-two seed is used only for that spectral induction; the Lie induction begins at the separately checked dimension-nine tensor, avoiding an unjustified Lie assertion for the seed. K-016 applies thereafter in both parities.

The resulting family consists of actual smooth density-one quotient fixed curves of order `2*256^k` in dimensions `2+7k`. Other fixed components, their dimensions and their combined coefficients remain unclassified. No actual global Hilbert pole, PH3 refutation, or index bound is inferred from these local curves alone.
