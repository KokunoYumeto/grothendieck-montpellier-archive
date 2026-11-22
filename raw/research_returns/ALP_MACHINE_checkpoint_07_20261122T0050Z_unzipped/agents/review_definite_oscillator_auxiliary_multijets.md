# Independent whole-proof review of AM-DO-030

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC. Runtime reasoning effort is not separately exposed.

**Result: PASS for the stated theorem and its retained limitations.** This is an independent mathematical and source-interface review, not a Lean build or an executable test of a global automorphic instance.

The reviewed file is `definite_oscillator_auxiliary_multijets.md`. I read its complete proof, reconstructed the auxiliary-translation and interpolation arguments, and then checked the amended final source audit. The precise saved-file hash and observed completion time are in my check-event log.

## Checked mathematical points

1. The hypothesis is the nonvanishing of the actual vector \(\mathcal O\phi_0\), not merely nonvanishing of an abstract Heisenberg operator. Combining representatives modulo the finite vacuum lattice gives distinct translated vacua and the stated orthogonal squared norm \(\sum_j|b_j|^2\).
2. For auxiliary torsion of common odd order prime to 29 and 11, choosing \(z_j=M^{-1}t_j\) and the representative \(r_j=M z_j\) makes the correction at 29 lie in \(M\Lambda\). Its Heisenberg commutator with the entire permitted 29 half-orbit is consequently trivial. The remaining fixed scalar includes the quadratic Heisenberg phase; it does not depend on the selected half-orbit tuple.
3. The analytic translation identity compares the correct translated line. The point \(z_j\) need not belong to the theta group kernel of \(L^{M^2}\). Pullback by the prime-to-11 auxiliary multiplication map places the required comparison in the finite theta group of the pulled-back line; its finite-order normalized lift is integral and primitive. Formal étaleness then descends the unit fibre comparison. This argument asserts neither a global theta-group automorphism before pullback nor a unit value of a translated theta section.
4. The auxiliary points remain distinct on the special fibre: their torsion order is prime to 11, and the 29-isogeny is invertible on that torsion. The simultaneous interpolation proof has the exact sufficient bound \(M\ge 3s(D+1)-1\). At each selected point, products of pair-separating sections of \(L^3\), each raised to \(D+1\), kill the other jets; local-parameter monomials use degree \(3D\), and the remaining exponent is at least 2. The resulting local multiplication is by a unit, so the argument spans every ordinary integral jet without inverting factorials.
5. The selected differential coefficient retains its ordinary derivative factorial, the minimum auxiliary coefficient valuation, the fixed finite norm, and the additional compact stabilizer index. Selecting one actual 29 half-orbit tuple uses integrality of the coefficient expansion, not an unspecified archimedean height bound for that expansion.

## Checked literal source audit

I directly checked `IsIdemAt` in `Formalism/LocalToGlobal/HeckeThetaElements/IsHeckeElt.lean`, lines 68–70; `IsSplitIdem` and `IsPlaceIdem` in `Formalism/LocalToGlobal/BesselHermitianTheta/TiedWeil.lean`, lines 68–72; and `infPart_split` in `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/EqZeroOrEqOfPlaceIdem.lean`, lines 134–140. The component argument in DO030 §6.1 follows exactly: an idempotent supported at another prime Q would make \(e/x\) nonintegral for some \(x\in Q\setminus P\), contradicting the defining equivalence for `IsIdemAt`. The P-component must be one, and the infinite component is zero.

The literal `IsIdemSum` clause is an existential sum of these prime idempotents, with \(e\overline e=0\); it is not an unprovided function named `IdemSum`. The distinction between the index named `mu0`, its empty Q-set, and the family of reference characters named `mu0` is correct. The reference-character ramification clause is separately retained. Thus avoiding 29 in `Sall` fixes the 29 vacuum; it does not silently authorize an additional affine translate there.

The support obstruction for pure position translations is correctly scoped. Linear source/target actions send a vacuum to an indicator of a lattice containing zero, whereas a nonintegral pure position translate has support missing zero. This rules out equality of those particular local vectors. It does not rule out cancellation or equality of an isolated global theta value, a finite span of group translates, the zero half-orbit tuple being sufficient, or an enlarged datum.

The report therefore proves the auxiliary simultaneous-jet theorem while leaving the literal raw-Xi matching equation, prescribed later image saturation, terminal class mass, and MainX inequalities open. No unsupported transfer to a full source instance is present.
