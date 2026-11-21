# Independent structural search for the note’s step 4

Run TRACE_DET_20261121, 21 November 2026. Agent `/root/step4_structural`, GPT-6 Astra Pro; effort not exposed. All Lean paths below are relative to `work/external_lean/lean/src`, the public release-mirror snapshot already documented by the parent. This is mathematical/source analysis, not a Lean replay or an audit of the stipulated RH theorem.

## Outcome

The exact historical identification of the note’s `W(1_S) >= 0 via a determinant` remains unresolved. The note, §2 step4 on p.3, defines neither W nor S, does not display a matrix and gives no declaration name. Calling W specifically the Weil functional is an inference from the adjacent Guinand–Weil discussion in step5, not an explicit definition. The independent routes below do not select a unique matching declaration.

A useful positive result was obtained: the finite signed-Gram propositions already used in DET-06 have actual theorem declarations and a finite-inertia proof. This confirms the precise mathematical kind of that source sign. It does not prove that the timeline’s W is this Gram expression.

## STEP4-SIGN / DET-06 source continuation

The actual declarations are:

* `Formalism/FormalDegreeBessel/FinalG.lean:21`: `theorem gGram : GGram := group_gram_holds`.
* `Formalism/FormalDegreeBessel/FinalG.lean:22`: `theorem gNonneg : GNonneg := gNonneg_of group_gram_holds`.
* `Formalism/FormalDegreeBessel/FormalDegreeRatio/ReverseCauchySchwarzHolds.lean:179–209`: the theorem body of `group_gram_holds` writes the Gram matrix in two-by-two blocks and reduces its determinant to the two leading minors.
* `Formalism/FormalDegreeBessel/FormalDegreeRatio/GNonneg.lean:302–397`: `gNonneg_of`. It treats the zero-eigenvalue case, then bounds the numbers of negative and positive eigenvalues each by r+1. Since the matrix has size2r+2, both counts equal r+1 in the nonsingular case. It then removes the sign from the eigenvalue product.

Thus the previously inspected `def GGram : Prop` and `def GNonneg : Prop` are indeed only proposition definitions at those particular locators; the later `FinalG` file supplies theorem declarations of those types. This source continuation should be stated so the audit does not accidentally imply no proofs exist.

### DET-10 / STEP4-SIGN: independent finite-inertia proof, complete

**Statement and source hypotheses.** Here A* denotes the conjugate transpose of a matrix A. Let k,r be arbitrary nonnegative integers, put n=2r+k+1, and let H=Hpk(k,r) be the n-by-n Hermitian matrix defined in `Formalism/FormalDegreeBessel/StatementG.lean:20–24`. Let z,z' be vectors supported on the middle coordinates r,...,r+k (`inWb`, lines28–29), assume T(z)>0 and T(z')>0 where T(w)=-h_H(w,w) (`Tz`, line31; this is real because H is Hermitian), and let g satisfy g*Hg=H (`UH`, lines11–12). For a=0,...,r-1 set f_a(z)=e_a, and set f_r(z)=z, as in lines61–62. Let B have the 2r+2 columns

f_0(z),...,f_r(z), g f_0(z'),...,g f_r(z'),

and put M=B*HB, which is exactly the source `gramM` (lines90–99; the matrix identity is also at `GNonneg.lean:143–151`). Assume the already-cited `GGram` identity

G_f(k,r,z,z',g)=(-1)^(r+1) det M.

Here the source embeds the real left side in C (`StatementG.lean:165–168`); det M is real because M is Hermitian. Then G_f>=0. More precisely, G_f=0 if M is singular, and G_f=product_j |lambda_j(M)|>0 otherwise. These are exactly the source `GNonneg` hypotheses at lines170–172; the second strict inequality T(z')>0 is not needed by the inertia step once `GGram` has been supplied.

**Proof.** Reorder the ambient standard basis by grouping e_a with the coordinate indexed by 2r+k-a, for a=0,...,r-1, and then take the middle coordinates r,...,r+k. The explicit definition of H makes different groups orthogonal. On each paired group the matrix is [[0,1],[1,0]], with eigenvectors (1,1) and (1,-1) and eigenvalues +1 and -1. The middle block is diag(1,...,1,-1), with k positive diagonal entries and one negative entry. Thus H is nonsingular Hermitian and has inertia (r+k,r+1), where the entries count positive and negative eigenvalues. This computation also covers k=0 and r=0; empty groups contribute nothing.

If M is singular, det M=0, and `GGram` gives G_f=0. Suppose now that M is nonsingular. The map B:C^(2r+2) -> C^n is injective: Bc=0 implies Mc=B*HBc=0 and hence c=0. Its image V therefore has dimension2r+2. The pullback of h_H restricted to V is represented by M, so this restricted Hermitian form is nondegenerate and has the same inertia as M.

Let L be the span in V of the first r+1 columns. These columns are linearly independent by injectivity of B, so dim L=r+1. By the definition of H, h_H(e_a,e_b)=0 for a,b<r. The middle-block support of z implies h_H(e_a,z)=h_H(z,e_a)=0: e_a pairs only with its outer coordinate 2r+k-a, where z is zero. Finally h_H(z,z)=-T(z)<0. Therefore the restricted matrix on L in the displayed basis is diag(0,...,0,-T(z)); in particular, every vector of L has nonpositive quadratic value.

Every negative definite subspace of V is a negative definite subspace of the ambient Hermitian space, whose negative index is r+1. Hence the negative index q of M is at most r+1. Every positive definite subspace P of V has P intersect L={0}, because a nonzero vector in this intersection would have both positive and nonpositive quadratic value. The dimension formula gives dim P + dim L <= dim V, so the positive index p of M is also at most r+1. Nondegeneracy gives p+q=dim V=2r+2, forcing p=q=r+1.

The Hermitian spectral theorem now gives real nonzero eigenvalues lambda_1,...,lambda_(2r+2), exactly r+1 of them negative. Consequently

(-1)^(r+1) det M = (-1)^(r+1) product_j lambda_j
                         = product_j |lambda_j| >0.

The claimed formula and nonnegativity follow from `GGram`. This completes both cases.

**Zero-parameter checks.** When k=0, the map B has 2r+2 columns in ambient dimension2r+1, so it cannot be injective; M is necessarily singular and G_f=0. Thus the nonsingular branch never silently assumes an available 2r+2-dimensional subspace in that case. When r=0, L is simply the negative line spanned by z, the claimed matrix has size2, and the same argument applies. If both parameters are0, the k=0 singular argument applies directly. The proof never divides by a minor, so a vanishing `Dmin` does not create an additional hypothesis.

**Scope and check.** The exact source hypotheses were reread in `StatementG.lean:165–172`. The proof was reread in full after composition, checking the block partition of all n coordinates, Hermitian conventions, injectivity only in the nonsingular branch, the dimension and nonpositive form of L, both inertia bounds, the real determinant/eigenvalue product, singularity for k=0, and r=0. No extra assumption k>=1, r>=1, nonzero leading minor, positivity of M, or positive trace-class operator is used. The argument proves the finite scalar sign conditional on the cited `GGram` identity; it neither identifies the historical W nor certifies all source helper declarations or a complete Lean build. The source's `gNonneg_of` in fact labels its unused second positivity hypothesis `_hT'` at `GNonneg.lean:303`, agreeing with the proof's dependency accounting.

## Routes tried and what each actually found

1. **Historical text and final endpoint.** The note’s steps4–6 were reread, together with the parent’s actual endpoint trace. The concrete step5 scalar is `Formalism/StatementOC.lean:11–13`. The examined predecessor `ChTop.lean:37–72` converts `gapA=ASK−Main` into an upper bound by `each_unit_bound_statement` in `Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean:175–197`. The latter uses slope, divisibility, counting and loss data; it does not define W or its indicator test. Reading these declarations narrowed the actual final argument to scalar inequalities, but did not retrospectively identify the earlier timeline object.

2. **Exact functional types, with false positives inspected.** A case-insensitive all-source search for the bounded identifiers `WeilFunctional`, `WeilForm`, `WeilPositivity`, `Guinand`, `PositivityCriterion`, `WeilCriterion` produced12 lines. The only substantive `weilForm` is the alternating tensor form `Algebra.trace F E (xi*tensHerm...)` in `GroundTheory/HeightsAndTheta/Theta/SchroedingerTranslates/ExistsInverseFontaineElementMemFilNegOne.lean:94–142`; the `WeilCriterion` module is an invariant-measure condition on homogeneous spaces. Neither defines the arithmetic W sought here. This is search evidence, not an absence theorem for unnamed equivalent constructions.

3. **Determinants with indicators.** The all-source same-line search `(indicator|Indicator).*([.]det|det_|qdet)|([.]det|det_|qdet).*(indicator|Indicator)` returned59 lines. The direct finite indicator determinant is `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/PPlueckerSpan.lean:13–36`: expanding a finite determinant through indicator coordinate rows. Its following exterior-power identity at38–64 is Plücker linear algebra, with no arithmetic test functional. Other sampled hits are Jacobian change-of-variable formulas, finite adelic lattice conditions, or automorphic determinant characters. Names alone were not promoted to a step4 identification.

4. **Period/exterior source neighborhood.** The full signature of `GlobalTheory.T.bessel_period_positivity` in `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BesselPeriodPositivityStatement.lean:10–11` was read, as was the signature of `GlobalTheory.T.block_projection_bessel` in `BlockProjectionBesselStatement.lean:8–9`. The former gives nonzero Bessel maps and a normalized period amplitude; the latter is the finite representation/period decomposition already appearing in DET-07. `Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean` supplies the actual minors, interlacing/gap hypotheses, scalar signed Gram functions, orbital squared norms and their weighted sums. These strengthen the finite period interpretation but do not name W(1_S).

5. **Alternative positivity routes.** `GroundTheory/AutomorphicForms/TraceFormulaWeil.lean` defines Weil quotient measures for centralizers; its name does not denote Weil’s arithmetic explicit formula. `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergCellIntegralFinitePartNonneg.lean`, especially229–274, constructs a nonnegative integrand from Whittaker coefficients, a nonnegative Fourier transform and a determinant-module weight; it is a Rankin–Selberg integral, not a selected matrix for W(1_S). `Development/WeilBound/CoreStatements/CentralCharts/TraceMulReNonneg.lean` is genuine finite positive-matrix linear algebra, conditional on PosSemidef/PosDef inputs; its hypotheses do not identify those matrices with the zeta operator. `DminNonneg.lean` in JacquetShalikaRigidity bounds a normalized height infimum; the name dmin there is not the Dmin leading determinant of StatementG. These false-positive distinctions were checked at their displayed definitions/statements.

6. **Signed Gram proof route.** Following GNonneg rather than searching for the historic W found FinalG and the inertia proof above. This is the useful source continuation. It settles what that actual sign means without assuming it is the exact timeline determinant.

One attempted broad indicator search included a nonexistent `Formalism/ExplicitFormula*` path; ripgrep reported that path error and still searched the existing directories. The separate explicit-formula source and the all-source searches were subsequently read/run. No conclusion of full coverage is based on that erroring command. An early broad `W` pattern also matched words such as `show`; it was used only to find candidates and was superseded by bounded identifier and structural searches. Its noisy output is not evidence of a mathematical assertion.

## Precise remaining gate and next step

The smallest source gate is a dictionary specifying (i) the domain and normalization of the historical W, (ii) the meaning of S and its characteristic function, and (iii) the finite matrix, determinant line or other operator meant by “via a determinant,” with a declaration-level correspondence to the released source or a dated earlier construction. The note’s own footnote4 says that timeline descriptions are paraphrases that may require correction. The final source may reflect the step5 replacement; this possibility must not be asserted as fact without historical evidence.

A built declaration dependency graph could establish whether any specific candidate participates in the exported theorem, but it cannot on its own recover an unprovided correspondence between that candidate and an undefined historical symbol. It would be inappropriate to call the unnamed step4 determinant a Fredholm determinant, or to call it definitively this finite Gram determinant, from the available evidence.

No new theorem that all possible positive arithmetic realizations are impossible is claimed. The parent’s DET-05 operator-limit gate remains the meaningful mathematical condition for the stronger possible identification.
