# Independent whole-proof audit: the global residual gate

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Verdict

The entire proof in `evidence/main_gate/residual_global_gate.tex` passes targeted review. Both KT-GLOBAL-RESIDUAL and KT-MULTI-HECKE are valid with their stated hypotheses. The first is an independently rechecked reformulation of the carried K17-S17-JOINT argument; it does not follow merely from the final quantified OneChar statement. The second is an algebraic clarification of the carried joint-operator test and does not use an automorphic classification. Neither is counted as a new arithmetic advance.

No new Lean build, kernel check, or verification of all imported foundations is claimed. The nine closed inputs retain the exact source-standing convention of KT-ONECHAR-CLOSED. The unramified coefficient hypothesis is explicit and includes the rational specialization O=Z_l.

## Full source read

All Lean paths below are relative to `evidence/lean_chain/source/src/Development/AutomorphicArithmetic/AutomorphicVarieties/`, at the pinned commit recorded in SOURCE_PROVENANCE.md.

I read these files in full:

- `UnitaryThreeGroups/ModelUpper.lean`, lines1–250, including the entire proof of `model_upper`.
- `UnitaryThreeGroups/IsPtOf.lean`, lines1–166, including every local-point integrality/continuity lemma and the complete `isPt_push` proof.
- `UnitaryThreeGroups/RhoKApply.lean`, lines1–98.
- `ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean`, lines1–96.
- `UnitaryThreeGroups/VlenLe.lean`, lines1–67.
- `UnitaryThreeGroups/ConjStable.lean`, lines1–116.

I additionally checked `GRepresents.lean:140–141` for IsLocPt; `UnitaryThreeReflectionRight.lean:235–305` for the torus, r0, and its matrix component; and `CharacterLevelBounds/ShaFamMono.lean:71–83` for the exact normalized-length definition and finiteness-sensitive monotonicity.

## Residual transport

`FOneCharU.lean:32–38` constructs D, g1, U, S and M and defines the restriction rho_f before using any selected Galois element or trace-separation hypothesis. Its finiteness and point hypotheses come from the same nine inputs used by the closed theorem. Consequently the new proof may reuse this construction without first having a common separating element.

`IsLocPt f` means that every element of the maximal ideal of S.R maps to an element of norm less than1. The lemma `ipo_le_one`, IsPtOf95–112, proves norm at most1 for every ring element. Its argument uses a nonzero image of a coefficient uniformizer and does not silently assume boundedness of an arbitrary algebra homomorphism.

The residual clause in `isPt_push`, IsPtOf137–145, uses exactly S.r.red and the residue-map compatibility to place each entrywise difference from r0 into that maximal ideal. Hence the pushed matrices are integral and reduce entrywise to r0. On the kernel of eta, `rhoK_apply`, RhoKApply73–74, gives their ordinary GL3 matrices. The torus definition has exponents1,0,-1, so reduction is precisely Psi-bar plus1 plus Psi-bar inverse, in the stated order. Applying the same integrality statement to inverse group elements proves integral inverse matrices. This supplies an actual integral model, not only equality of selected Frobenius traces.

`TwoPt` includes IsLocPt as its first clause, ConjStable94–95. The complete hadm argument, FOneCharU48–54, puts every such point into one of the two exact admissible source classes, with the rank-two level N times the absolute discriminant. Therefore the hypothesis that no actual admissible source has the indicated residual semisimplification excludes every TwoPt point. In fact the model point has split diagonal reduction before semisimplification, a stronger property.

## Why the identity element is legitimate

`model_upper`, ModelUpper103–111, permits any group element sigma satisfying eta(sigma)=1 and the nonzero trace-difference condition at every TwoPt. For sigma=1 the sign condition is automatic. Once TwoPt is empty, the trace-difference condition is vacuous even though the identity trace difference itself is zero.

The theorem returns finite M.len and a finite set T satisfying CoversPt. The first clause of CoversPt says that every member of T is a TwoPt, so T is empty. Its sum is zero. The normalization is `(M.len.toNat : Real)/eO.toNat`; finiteness is essential because toNat(top)=0 would otherwise lose information. Here finiteness is supplied by model_upper, and eO=1 is an explicit hypothesis. Thus the zero normalized bound gives M.len=0. The exact theorem `vlen_le`, VlenLe52–67, gives Vlen<=M.len and completes the proof.

There is no illicit assumption that OneChar's finite set X is independent of sigma. The proof uses the underlying fixed deformation model and emptiness of its TwoPt locus.

## Multi-Hecke criterion

For commuting operators, the algebra A they generate is finite-dimensional and commutative. By its definition as a subalgebra of End(M), M is faithful. The block matrix has image IM, where I is generated by the specified shifted operators. If I were proper and IM=M, localization at a maximal ideal containing I would give a nonzero finite faithful-support module satisfying its own maximal-ideal multiple; Nakayama excludes this. Hence full block rank is equivalent to I=A.

When I is proper, a maximal quotient of A/I embeds into the algebraic closure. Faithful support guarantees that this character occurs in the module after scalar extension. For a finite-dimensional module over a commutative algebra over an algebraically closed field, an occurring character has a nonzero simultaneous eigenspace: restrict to its local primary summand and take the last nonzero power of the maximal ideal. Thus the proof's equivalence between a composition-factor character and a joint eigencharacter is valid, including nonsemisimple operator actions.

The criterion is strictly stronger than checking individual determinants. For example, shifted operators diag(1,0) and diag(0,1) both have zero determinant, whereas their combined block has full row rank. No common target character survives.

Applying this to Hecke operators still requires the stated integral model, simultaneous normalization and coverage of each actual admissible branch. A deficient block at a finite set of primes does not prove a global residual congruence. A global residual congruence in turn is necessary, not sufficient, for nonzero Selmer length. The proof retains each of these distinctions.

Reviewed proof SHA256: `12a98493065e36e6294aaf8ab41fe857c9b5dadc01190d504b34d6b35e5fef1c`.

## Prior-art reconciliation

After the source review, geometry_tower located `input/RETURN_K17_checkpoint_08_20261121T0616Z/evidence/work/hecke_uniform/joint_trace_section.tex`. I then read that complete file. Its K17-S17-JOINT proof already contains the identical empty-TwoPt-at-identity argument, entrywise residual transport, and the stronger descent to arbitrary coefficient rings. Its K17-S17-GROUP-RING theorem and Joint operator test already supply finite operator combinations and a vertically stacked matrix test. The current residual-semisimplification formulation and horizontal-block criterion clarify the same mechanism. This review is recorded as a targeted independent recheck of carried material, not new progress.
