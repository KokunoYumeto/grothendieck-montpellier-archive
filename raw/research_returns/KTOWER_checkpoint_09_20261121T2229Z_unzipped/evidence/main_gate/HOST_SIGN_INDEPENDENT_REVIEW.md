# Independent review of the actual ordinary adjoint points

Reviewer: `/root/geometry_tower`; GPT-6 Astra Pro; effort not exposed; run KTOWER; 2026-11-21 UTC.

## Verdict

**PASS** for the entire updated `../unitary_audit/host_sign_results.tex`, including KT-HOST-TANGENT-SIGN, KT-ORDINARY-ON-BASE-COMPONENT, KT-ADJOINT-ACTUAL-HOST-POINT and its obstruction corollary. The pass treats the named carried local component theorem and already checked automorphic inputs as explicit dependencies. It is a mathematical and source-predicate review, not a new Lean compilation.

The updated scope permits an arbitrary finite coefficient DVR O and requires the chosen marked element to satisfy D.Marked. Both amendments were read before the final verdict.

## Checked argument

The involution differential sends E21 to −E32 and vice versa. Hence the minus line has rational character Psi inverse, while the plus line has eta times Psi inverse. The source's shaInj_mat really is the minus line. The normalized adjoint basis (E,sH,F), with 2s²=−1, gives the plus line. These are tangent-space statements and do not restrict TypeI by themselves.

For the Borel family, the inertia composition factors of b and n have even exponents. Their Tate dual twists have odd, nonzero exponents modulo ell−1; consequently H² vanishes. The unramified outer involution merely changes the residual Galois module and does not invalidate the calculation. The map H¹(G,b)→H¹(G,t) is onto by H²(G,n)=0, and H¹(G,t)→H¹(I,t)^(G/I) is onto because the quotient has ell-cohomological dimension1. Thus one corrects the torus inertia after each small lift. The resulting framed fixed-inertia ring is formally smooth over O and a power series domain.

Adjoining the nine congruent-conjugation variables retains a domain. The ordinary polynomial relations vanish in the ordered flag: the rightmost factor drops to the second flag step, the middle to the first, and the leftmost kills it. The saturating element is nonzero on the diagonal unramified-twist family; the exact factor is ell*c0*c1²*c2*y^(−1)*(y−v)². Thus the family kills the saturated ideal and its radical. Its prime kernel is below the exact base-point kernel; uniqueness of the framed base map and the carried singleton primesAt0 theorem then force It into this kernel.

The split-residual lattice construction is valid after adjoining a square root of the original uniformizer. In a complex-conjugation eigenbasis one off-diagonal ideal is already in the maximal ideal; the half-uniformizer scaling makes both off-diagonal ideals lie in the enlarged maximal ideal. The diagonal characters remain exact after reduction.

For the cohomological dual, the ordinary unramified line is the first flag step and the second inertia character is epsilon^(−e). Its saturated integral line reduces to the first standard line because the residual inertia characters are distinct. A congruent-to-one change of basis therefore upper triangularizes it. Its adjoint preserves the trace form K and obeys theta(h)=D_c h D_c, which proves the semidirect conjugation identity in both split and inert cases.

The coefficient order A0=O+m(O') satisfies the exact IsCO predicate. It is finite over O, local with maximal ideal m(O'), and its residue field is k(O). Its maximal-ideal powers equal the corresponding powers of m(O'), and the maximal-ideal and ell-adic topologies are equivalent. Thus it is complete. Both the representation and its inverse have entries in A0 because their residual entries lie in k(O); s itself need not belong to A0.

The literal normalization theorem applies to A0 and the marked residual data, producing a congruent-to-one conjugate. This preserves the already established local component condition and the exact Kill condition. The universal property is a property of all IsCO coefficient algebras, so it gives the claimed ring map to A0. The inclusion into the algebraic closure gives IsLocPt. Absolute adjoint irreducibility on G_E gives TypeI and excludes both Upper and Lower, hence TwoPt. The whole IsPt_push proof was reread. CoversPt then necessarily includes its torus-conjugacy class.

## Exact files read

Under `../unitary_audit/host_sign_source/`:

- `PadicHodgeTheory/IsInertiaInfiniteCyclotomic.lean`: entire file, including ordIdeal, del, IY, Icr, primesAt0, It and On.
- `ModularityArgument/CrystallineOrdinaryIdeals/SaturatingElementUnramifiedTwistEqPowMulUnit.lean`: entire file and proof.
- `ModularityArgument/CrystallineOrdinaryIdeals/OrdinaryComponentUniquePrimeDimThirteenNearBase.lean`: entire component_basic proof. Its named LocalPublishedTheorems dependencies remain imported.

Under the pinned lean-chain source tree:

- `UnitaryThreeGroups/NormEx.lean`: entire file and proof of exists_normalised.
- `UnitaryThreeGroups/GRepresents.lean`: GLift, GRepresents, Univ, BoxCond, NormCond and IsLocPt definitions.
- `UnitaryThreeGroups/ConjStable.lean`: SRing, TwoPt and CoversPt, with their surrounding definitions.
- `UnitaryThreeGroups/RhoKApply.lean`: entire file, including Kill, Marked and IsPt.
- `UnitaryThreeGroups/BaseRepGL3NormalisedOfPsiEqOne.lean`: entire file, including TypeI, Upper, Lower and Marks.
- `UnitaryThreeGroups/IsPtOf.lean`: complete isPt_push statement and proof.
- `UnitaryThreeGroups/ShaInjGen.lean`: shaInj_mat and the complete equivariance proof.

The missing imported file `CommutativeAlgebra/ResMapBijective.lean` was fetched afresh at commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` and saved under `host_review_source/`. Its IsCO definition and residue-map construction were read directly. No assumption that IsCO required normality or a DVR was made.

## Computation scope

The complete `host_sign_matrix_check.py` was read. A byte-identical copy was saved under `host_review_source/` and freshly executed. All16 identities passed; the whole JSON report equals the author's report. Script SHA256: `53568d68c1f4368a3ea6873435d652da16a5273ab8d666ceb87b931b42fe6b2d`.

This numerical/symbolic replay is the same implementation, not an independent second implementation. It checks the displayed finite matrix and scalar identities only; the local deformation argument was assessed mathematically above.

## Consequence and boundary

The ordinary symmetric-square families really give points of the selected source ring, and every literal CoversPt set must cover those classes. Their residual trace is the Eisenstein trace for every element, including at the fixed certified prime697446897311 above2^31, while the corresponding rational K-primary group vanishes. Thus the selected-point restriction does not remove this family.

This does not contradict the one-way strict Selmer injection or prove a nonzero rational Selmer class. It also does not identify every possible witness of the existential OneChar statement with a particular CoversPt construction. A proposed sharpening must preserve the rational minus-line information beyond the tangent-space decomposition.
