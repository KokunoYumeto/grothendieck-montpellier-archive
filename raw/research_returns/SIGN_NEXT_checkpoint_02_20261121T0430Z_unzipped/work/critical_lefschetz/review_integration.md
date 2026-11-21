# Integration review of SIGN_NEXT

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/critical_lefschetz.
Review recorded: 2026-11-21 03:43:26 UTC.
Assembled file SHA256 at review: 7d32ce771e0cf2bf8bf060353af3d22a0c2643b59e6d6faa94fbb2d5dd396e04.
Boundaries SHA256: 6e38f20561828331e31c3aeed5ea2037cee6aaaaed8c5472010e10e9060be25b.

## Scope and verdict

I read the complete introduction and notation/check conventions, the complete positive-adjoint section, the complete Part II boundaries/framework map, the integral-section transitions and limitations, the final local-frame and ordinary-L-squared paragraphs, and the closing all-characteristic height conclusion. I compared these with the final component proofs independently reviewed in the reports listed below. This is an integration/scope review, not a new complete reproof of every assembled statement. In particular I do not claim a fresh independent reproof of IF-01, IF-03 or IF-05 in this integration pass. The complete IF-06 oscillator proof was read in this pass and its commutator and terminal-weight argument checked; no issue was found.

Two corrections are needed before this assembled snapshot is treated as final. Both were sent to root before the checkpoint. No further substantive mathematical fault was identified in the reviewed integration passages.

## Corrections

1. **Sufficient positive-adjoint inputs must not be presented as necessary for every semisimplicity argument.** The heading “Exactly what correspondence coefficients would have to add” and the application paragraph saying an extension of the method “would have to produce” the adjoint and positive form are broader than the proofs. Replace the heading by “The additional inputs for the positive-adjoint argument.” In the application, say that to complete the scan-049/Kleiman argument by this method one must establish its algebraic adjoint and nondegenerate positive form; SN-14 does not exclude a different semisimplicity argument. The displayed positive trace condition itself is accurately identified as the condition used by this particular argument. Algebraic adjoint plus positivity is a sufficient route, not a proved necessary criterion for all geometric semisimplicity.

2. **The assembly contains an earlier IF-08/09 snapshot.** The final independently checked kernel source has SHA256 `47c5163c4343d0a3a2bc48775a6451bd321f770f8e6f93446b8ffc4c838c9d15`. Its explicit coefficient-frame convention B=C^(-t) is missing from the assembled local-frame paragraph. The final ordinary-L-squared obstruction explicitly requires integral embeddings, saturated final image, and two applications of the same fixed ordinary L on one exterior lattice; the assembly has the older broader sentence. Reassemble from the final source. The final IF-04 weight-grading and diagonal-rowDiv clarifications are already present in the reviewed assembly.

## Scope checks accepted

- Historical C_G is consistently modern Lefschetz B, distinct from modern Kunneth C. Cycle A and normalized inverse-string lowering are not conflated with ordinary integral contraction.
- The literal lower-critical Gysin condition is refuted by the geometric P1 example. The weighted theorem is an explicit corrected formulation, not a claim that the missing weight was in the manuscript. The ordinary upper-Gysin variant requires A_0 on the actual hyperplane W of X squared; W is not Y squared.
- Kleiman 1968 Proposition 3.6 already gives D(W) plus hard Lefschetz implies A(W); I is not needed for this direction. Under the standing hard-Lefschetz assumption and I, Corollary 3.9 gives the converse. The note correctly labels these as cited classical implications, not consequences of trace purity.
- The abelian conclusion uses the stipulated CM Hodge theorem and the cited Milne/abelian-Lefschetz chain. It is not generalized to arbitrary varieties. SN-14 is explicitly a formal tensor-category and point-sheaf counterexample, not a counterexample to geometric standard conjectures.
- The height comparison separates the general Gram formula from the ordinary-node calculation. The final pencil conclusion is for algebraically closed fields of characteristic different from 2 and odd fibre dimension at least 1. Purely inseparable descent uses the full field degree. Characteristic 2 is not included in the nodal claim. The curve case and unequal complementary codimensions were already independently checked in the final singular-fibres contribution.
- The finite coefficient-kernel transport is proved with jets, dual lattices, determinant insertions, local frames, periods and stabilizers retained. It does not calculate an unspecified actual global Smith matrix merely from m=2. The exponential test is not claimed to be the global automorphic theta function. Q6g's stronger universal identification/global exact index assertion remains unestablished in this package. The stated fixed-operator obstruction does not rule out every possible normalized geometric realization.
- Motivic numerical semisimplicity, homological/numerical equality, and positivity on a chosen realization remain distinguished. The framework map does not infer arbitrary theta-moment algebraicity from tensor-polynomial formulas.
- Check types, source inputs, inherited model and unavailable effort setting are truthfully distinguished. This pass does not verify all bibliography locators anew.

## Component reports incorporated

- `review_root_SN10_SN14.md`: full independent root proof checks, including final 3D tensor countermodel and corrected Milne version crosswalk.
- `review_IF02_IF04.md`: full independent integral proofs and final grading/diagonal-root clarifications.
- `review_IF08_IF09.md`: full independent actual-kernel proofs, local/global transport and final normalization scopes.
- `review_SN44.md`: full independent SN44-01 through SN44-06 proof review, including m=1, incidence pairing and all-characteristic fixed part.
- `ordinary_gysin_DI_source_note.md`: exact classical D/I refinement and its limits.

No shared contribution file was edited by this reviewer.
