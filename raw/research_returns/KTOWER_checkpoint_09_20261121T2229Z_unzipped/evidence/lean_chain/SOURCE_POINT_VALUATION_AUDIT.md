# What the archive source actually gives toward the cubic extraction

## Conclusion

The inspected construction of actual OneChar source points does not supply either the inequality v_pi(p)>3d or the sparse logarithmic support in (SJ.7). It supplies characteristic-zero local points, residual congruence, normalization, the global inertia condition, and the ordinary component. It also has separate first-order tangent-extension statements. Those first-order statements do not imply the independent two-parameter cubic jet.

This is an exact scope conclusion about the checked chain, not a theorem that no individual arithmetic point can satisfy the conditional extraction hypotheses. No new Lean kernel build was run.

All source locations below are in the pinned repository CocoSgt/riemann-hypothesis-lean at commit 7cbf7a0c32fca1badf05931879a37c3f8a2b03b4, below src/Development/AutomorphicArithmetic/AutomorphicVarieties. The full local paths and hashes are in source_point_valuation_manifest.json.

## Exact clauses and conclusions

| Source | Actual conclusion | Limit relevant here |
|---|---|---|
| UnitaryThreeGroups/GRepresents.lean, 41–44 and 140–141 | GLift is an adically continuous residual lift. IsLocPt means every maximal-ideal element has image of norm strictly less than one. | This gives positive valuation only. No comparison with one-third of v_pi(p) occurs. |
| UnitaryThreeGroups/RhoKApply.lean, 76–83 | IsPt contains multiplier, continuity, integral entries, entrywise residual congruence, Normalised, Kill, and a local point annihilating It. | No uniformizer depth, sparse expansion, or two-parameter Artin family is part of the predicate. |
| UnitaryThreeGroups/IsPtOf.lean, 124–166 | isPt_push sends every local point of the represented global ring to IsPt. Its residual proof is 137–145. | The proof transports the strict norm inequality; it does not sharpen it quantitatively. |
| UnitaryThreeGroups/ConjStable.lean, 94–99 | TwoPt adds failure of Upper and Lower; CoversPt is a finite covering up to torus conjugacy. | It does not choose nonzero first-order classes of equal depth or impose sparse support on their logarithm. |
| UnitaryThreeGroups/UnitaryThreeReflectionRight.lean, 280–289; NormEx.lean, 155–217 | Normalised imposes the c matrix and two marked entry equations; exists_normalised constructs a congruence-one conjugation. | The Hensel normalization eliminates those marking equations. It does not globally remove every other Lie direction or intermediate coefficient power. |
| UnitaryThreeGroups/TanDet.lean, 110–138 and 182–216 | The quotient by the square of a local point kernel is finite over the base coefficient DVR. | This supplies a finite coefficient order and qualitative boundedness. It gives no ramification index or leading-entry valuation estimate. |
| UnitaryThreeGroups/ExistsTorusTwistEqLocalPointOfWeightedPres.lean, 95–137 | A torus translate of an algebraic model point extends to a local point of the completed source ring. | The conclusion is still a point into the p-adic algebraic closure, with no specified finite ramification or Taylor support. |
| UnitaryThreeGroups/ModelUpper.lean, 103–111 and 149–250 | Produces a finite covering set of local points, together with the normalized cotangent-length/trace-valuation inequality. | Its valuations are used in that length inequality. No small-depth upper bound for the selected point's entries is asserted. |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean, 31–74 and 75–95 | Constructs the local/global rings and model, passes each TwoPt to the exact admissible representation families, then deduplicates up to representation isomorphism. It first passes to an unramified base coefficient ring. | An unramified base ring is not a claim that every point's finite coefficient field is unramified, nor a source of a large ramification/depth ratio. |

## The tangent statements are first order

ConjStable.lean 79–80 asserts that an already-specified point derivation annihilating the model equations extends to a homomorphism into dual numbers over the characteristic-zero coefficient field. The complete implementation is ExistsDualNumberPointOfPointDerivationVanishing.lean 136–225, with the extension and boundedness lemmas on 13–134. Its target is DualNumber(PadicAlgCl l). No second- or third-order integrability is concluded.

ConjStable.lean 81–85 has a different base-point lifting property: a specified weight-minus-one derivation with finite coefficients and a compatible local lift gives a derivation on the ambient graded model A. This is not a homomorphism from the global source ring to a two-variable cubic Artin algebra. The complete construction in ExistsBasePointDerivationOfWeightHomogeneous.lean 48–134 only uses linear coefficients and the Leibniz rule.

The local chart in ConjStable.lean 25–37 takes values in power series over FractionRing O. Its infinitesimal comparison explicitly allows multiplication by a nonzero coefficient c. Thus rational local charts cannot silently be treated as the integral sparse global expansion needed in (SJ.7).

## Valuation invariance makes the missing estimate precise

For a fixed point in a fixed integral basis, let d be the common leading order required in (SJ.7), with at least one nonzero first-order coefficient. Then d is a genuine entry valuation, and the normalized valuation is d/v_pi(p). The extraction requires this number to be less than 1/3. IsLocPt only requires it to be positive.

If a coefficient extension has relative ramification index a, both the valuation of p and every existing nonzero entry valuation multiply by a. The ratio is unchanged. Passing to a larger ramified coefficient field therefore cannot establish the inequality for a point that did not satisfy it.

A torus conjugation adds v_pi(t) to the valuation of a weight-one entry and subtracts it from a weight-minus-one entry. Their sum, equivalently the valuation of their product, is unchanged. Thus torus balancing is not an operation that makes both opposite directions arbitrarily small relative to p. This is consistent with the exact point-extension theorem above, which only promises a local point.

The source compares residual entries with the original cyclotomic-character lift. The conditional extraction uses a finite Teichmüller lift. Once the strong depth inequality is assumed, its characteristic-p quotient makes those inertia characters constant as proved in the extraction lemma. The source's residual comparison alone does not produce that larger characteristic-p truncation.

## Proof-reading scope

In this audit I read in full GRepresents, RhoKApply, IsPtOf, ConjStable, NormEx, DefNorm, FOneCharU, ExistsTorusTwistEqLocalPointOfWeightedPres, ExistsBasePointDerivationOfWeightHomogeneous, and ExistsDualNumberPointOfPointDerivationVanishing. I read ModelUpper through its complete point-covering proof, and the complete fin_gen/pow_le/fin_quot proof chain in TanDet. The exact Normalised declaration was separately inspected. The final conditional cubic-extraction proof was independently read in full and passed after the formal-action clarification.

The inspected source therefore leaves a quantitative and higher-integrability gate. The flat-domain counterexample in KT-EQUIVARIANT-POINT-NOT-CUBIC-JET shows why a general formal inference from a characteristic-zero point, flatness, and the two symmetries would be invalid. It does not replace the missing arithmetic analysis of the actual source.
