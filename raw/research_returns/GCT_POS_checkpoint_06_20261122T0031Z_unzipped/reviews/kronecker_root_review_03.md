# Whole-proof and independent arithmetic review: K-010 through K-014

Reviewer: `/root`; GPT-6 Astra Pro; effort not exposed; GCT_POS. Date: 21 November 2026 UTC.

**Outcome: PASS.** Read the complete proofs in N5_FINDINGS.tex, N5_LIFT_COVERAGE.tex, ANTIPODAL_STABILIZER.tex, ONE_PAIR_STABILIZER.tex, and N5_POLE.tex. The model review is mathematical proof review, not a proof-assistant formalization. Classical invariant-theoretic inputs retain the separate source attributions in those proofs and in P-F23/P-F60.

## Coverage and finite arithmetic

The recursive refinement argument preserves all torus-feasible spectra: every feasible fine mass pushes down, every multiplicity split is enumerated, and each coarse symmetry lifts. The prescribed determinant character is reduced at each stage, including zero targets; the generator retains every odd normalizing unit. Unsupported coordinates cannot carry a margin-one feasible mass. I inspected recursive_spectra.py, refine_character.cpp, and the prescribed-character driver in full. This is a proof/source review of orbit coverage, not a claim of a second independent n=5 orbit generator.

The independent root program verify_n5_spectral_certificates.py imports none of those engines. It clears denominators, checks all 125 coordinate triples in each Farkas separator, verifies every positive marginal, and checks each spectrum against the complete generated list. PASS: 291,310 primitive certificates; 700,302 target-two certificates; 2,418,383 target-four certificates. Separate JSON receipts retain every level count. The cutoff K-009 makes these lists exhaustive, including nonfaithful higher lifts. The 77 feasible target-two spectra at modulus32 and target-four spectra at modulus64 divide exactly to the primitive modulus16 list.

## Polystability, Lie and finite stabilizers

For the 76 simple-spectrum cases, full column rank and positive unique marginals give one centralizer orbit and a critical representative. The repeated case is treated by its actual two-dimensional eigenspace: the displayed frame has the claimed column norms and FF*=I. The pair-mass Hilbert–Mumford argument excludes coincident projective lines, and projective transitivity plus the thirteen independent coefficient weights gives one semistable centralizer orbit. Lie calculations are made on an equivalent all-one representative, not by assuming that an arbitrary torus-semistable tensor is polystable.

The proofs of K-012 and K-013 include the necessary projective central extension. The odd-rank hypothesis, faithful determinant character, centralizer, character orthogonality, and odd-power Parseval estimate are used in their stated order. In K-013 the sole antipodal pair comprises two simple eigenlines. The nonzero one-pair projection forces a finite SL2 action to have a fixed vector, hence to be trivial. The pointwise first-factor stabilizer is a unit group in a finite-dimensional vector-space algebra and therefore connected; the already established scalar identity component gives the needed projective-factor faithfulness. No invertible-slice hypothesis is silently inserted.

The original analyze_n5_types.py was read in full and replayed. A separate root program verify_n5_geometry.py rebuilds all infinitesimal matrices from the supports, uses prime10007 instead of1009, and evaluates a maximal incidence minor directly. Every Lie rank is73 and every chosen incidence determinant is ±16. It also checks the simple paired eigenlines and one-pair projections. Receipt: n5_geometry_root_verification.json.

## The global residue

The full stabilizer has faithful character, so the effective determinant-one stabilizer is trivial. The tangent calculation gives one-dimensional smooth fixed loci at every nonvertex point. Unique determinant-character elements distinguish the ordered orbits; the root verifier independently uses all256 scalar shifts per factor permutation, rather than only supported-edge shifts. It confirms 65 classes with multiplicity6, eleven with multiplicity3 and one with multiplicity1, totaling424 curves.

The restriction algebra of each nonzero grading orbit is a one-variable semigroup algebra with gcd16, hence has normalized density one. Its possible vertex holes do not change the residue. The normal determinant uses the point-pullback convention already checked in P-F60. Both the symbolic cyclotomic products and independent Fraction arithmetic agree on all77 local coefficients. Their weighted sum is

`(78,446,-211,-301,-301,-211,446,78)/32768`

in the basis1,z,…,z^7, z^8=−1. It is nonzero. The primitive partial fraction divides that numerator by2 because (1−t^16)/(1+t^8)=2 at a primitive sixteenth root. The multiple-component P-F23 formula applies, and zero-dimensional vertex strata do not alter the simple-pole coefficient. Thus K-014 is an actual global pole theorem in dimension5, not a conditional prequotient determinant calculation.
