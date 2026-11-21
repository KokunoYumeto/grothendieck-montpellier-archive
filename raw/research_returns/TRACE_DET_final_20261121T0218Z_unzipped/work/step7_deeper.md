# Step 7 continued: interlacing selectors and the actual period functional

Run TRACE_DET_20261121. Date 21 November 2026 (Europe/Berlin). Agent `/root/delivery_audit`, GPT-6 Astra Pro; effort setting not exposed. All source paths are relative to `work/external_lean/lean/src`, the public release-mirror snapshot whose provenance is recorded by the parent. No Lean replay or audit of the stipulated RH theorem was performed.

## Outcome and change in the gate

This pass gives an exact elementary determinant encoding of the **actual source interlacing predicate**, and identifies the actual period scalar and the signed exterior decomposition more precisely. It does **not** identify the historical functional W in Remark steps 4/6/7. In particular, the threshold matrix below is a construction of this audit from the inspected predicate; it was not located as a determinant declaration in the source. It must not be attributed to Alpöge as the missing timeline matrix.

The source gate therefore narrows in mathematical interpretation: the “0,1 meaning interlacing” phrase has an explicit finite selector model that exactly matches a predicate used by the GGP source. Its exact historical realization, normalization and relationship to W remain unproved. The identification gate is not counted as closed.

## STEP7-01. Exact threshold determinant for the inspected predicate

### Source definitions

`Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean:256–259` defines `InterlaceS` for u of length k and lambda of length n>=k by

\[
\lambda_i<u_i,\quad u_{i+1}<\lambda_i\quad(0\le i<k-1),
\qquad \lambda_{k-1}<u_{k-1}\ (k>0).
\]

`Formalism/FormalDegreeBessel/StatementDS.lean:11–12` defines `IsHCParam lambda` as strict decrease together with membership in the appropriate half-integral coset. The duplicate definition in `Formalism/PeriodIntegrals/UpqRep.lean:228–229` agrees.

In the source GGP range k>=2, `Formalism/PeriodIntegrals/BesselPeriodGGP.lean:20–30` defines lambda by concatenating

\[
(v_0,\ldots,v_{k-2},-b_0,\ldots,-b_{2r+1}),
\]

and defines `InterlacingCondition` by u_i>v_i>u_(i+1) for i<k-1 and u_(k-1)>-b_0. It is consequently exactly the displayed `InterlaceS` condition for this lambda. The same file's lines 32–33 impose u_i-lambda_j in Z+1/2, ensuring no cross equality. The count of appended b-parameters is 2r+2 and the ambient rank is k+2r+1. This exact count does not itself identify the timeline's parameter m or prove what “up to m non-interlacing” meant historically.

### Proposition (audit construction, not a located source matrix)

Let k>=0, n>=k, and let u_0>...>u_(k-1) and lambda_0>...>lambda_(n-1) be real sequences with u_i unequal to lambda_j for i,j<k. Define the k-by-k real matrix

\[
C(u,\lambda)_{ij}=\mathbf 1_{\{u_i>\lambda_j\}},\qquad 0\le i,j<k.
\]

Then its determinant is either zero or one, and

\[
\det C(u,\lambda)=1
\quad\Longleftrightarrow\quad
\operatorname{InterlaceS}(u,\lambda).
\]

When the determinant is one, C is the upper triangular matrix with every entry on or above its diagonal equal to one. For k>=2 that matrix is not selfadjoint, even though all its eigenvalues equal one. This scalar selector positivity is not positive-operator structure.

### Complete proof

For each row i let t_i be the number of j<k such that lambda_j>=u_i. Since lambda is strictly decreasing, row i consists of t_i zeros followed by k-t_i ones. Since u is strictly decreasing, 0<=t_0<=...<=t_(k-1)<=k. If any t_i=k, that row is zero, and the determinant vanishes. If two t_i agree, their rows agree, and the determinant again vanishes. Otherwise the t_i are k distinct elements of {0,...,k-1} in increasing order, hence t_i=i for every i. The matrix is then upper triangular with diagonal entries one, so its determinant is one. These cases cover all possibilities.

The equality t_i=i is equivalent to lambda_i<u_i and, for i>0, u_i<lambda_(i-1), because cross equalities were excluded. Reindexing the second inequality gives precisely `InterlaceS`. Conversely, those inequalities give t_i=i and the same upper triangular matrix. If k=0, both the empty determinant and the vacuous predicate have the required value. For k>=2 the (0,1) entry is one and the (1,0) entry is zero, so C is not selfadjoint. Its eigenvalues are its diagonal entries because it is triangular. This proves every assertion. ∎

The cross-equality qualification is material. Without it, the same threshold determinant tests a mixed strict/weak predicate; for example u=(2,1), lambda=(1,0) gives determinant one but violates the strict source inequality u_1<lambda_0. The half-integral difference condition in the GGP setting excludes this example.

### Actual source consequence, with hypotheses retained

Under the numerical hypotheses in `BesselPeriodGGP.lean:108–110`, including k>=2 and even k, this audit's selector determinant equals one. The proposition at lines 105–120 then asserts nonvanishing of a matrix-valued Bessel period for suitable translated vectors, subject also to its discrete-series, finite-dimensional representation, lowest-vector and Haar-measure hypotheses at lines 111–116. It does **not** say the value of the period is one. The determinant above records a finite admissibility condition; it is not an equality between the period's numerical value and a determinant.

The source definition `InterlaceBlocksW` in `Formalism/FlagUnipotentLattices/InterlaceBlocksW.lean:9–15` is another exact finite interlacing statement for lists with appended arithmetic-progression blocks. Its suffix W is not a definition of a scalar arithmetic functional. `MemLpTwoOfOneTop.lean:41–50` defines those blocks and the list predicate. The spectral-residue propositions in `InterlaceBlocksW.lean:37–68` concern finite mutually orthogonal algebraic idempotents in a tensor representation and their contractions by a Bessel map; they are not an ordinary Fredholm determinant assertion.

## STEP7-02. The actual period scalar and a genuine finite-rank positivity statement

`Development/AbelianVarietyTheory/Definitions/Jets/SideFam.lean:30–32` defines `IsCoef R l l' F s`. It requires a finite expression

\[
F(g)=\sum_i\langle x_i,\sigma(g)y_i\rangle X_i,
\qquad
s=\sum_i\langle l(x_i),X_i l'(y_i)\rangle,
\]

where x_i,y_i lie in R.TK and X_i are continuous linear maps from Wq to Wp. This is the actual scalar attached to a finite matrix-coefficient representation with two period maps. The definition is a relation carrying a specified expansion. This pass has not independently proved a universal well-defined extension to arbitrary test functions, and does not rename it the historical W.

`Development/AbelianVarietyTheory/Definitions/Jets/SumIoPrAlt.lean:135–139` defines `IsBeL`, including the normalized Bessel-period factorization

\[
\operatorname{be}(x,v)=(\operatorname{innerSL}(l(v))).\operatorname{smulRight}(l(x)).
\]

With inner products conjugate-linear in the first argument, the right side sends xi to <l(v),xi> l(x). The actual `BesselPeriodPositivityStatement.lean:11–12` **takes** the Bessel maps and these factorization equalities as hypotheses, along with the displayed representation, gap and Haar hypotheses; it then gives nonvanishing and a normalized amplitude description. It must not be paraphrased as constructing those factorizations without hypotheses.

### Proposition (complete elementary consequence)

If `IsBeL` holds and v belongs to both the stated smooth domain and R.TK, then the operator be(v,v) on Wp is positive, has rank at most one, is trace class, and

\[
\operatorname{Tr}(\operatorname{be}(v,v))=\|l(v)\|^2,
\qquad
\det(1-z\operatorname{be}(v,v))=1-z\|l(v)\|^2.
\]

**Proof.** Put a=l(v). The factorization states that P(xi)=<a,xi>a. It is a bounded operator of norm ||a||^2, since Cauchy–Schwarz gives ||P xi||<=||a||^2||xi||, with equality on xi=a/||a|| when a is nonzero. For every xi, <xi,P xi>=<a,xi><xi,a>=|<a,xi>|^2>=0. The corresponding polarization, or direct equality <xi,P eta>=<P xi,eta>, gives selfadjointness. Its image is contained in the one-dimensional span of a. If a=0, P=0 and the claimed trace and determinant are immediate. Otherwise a/||a|| is an eigenvector of eigenvalue ||a||^2 and its orthogonal complement is killed. Thus P is trace class with the one nonzero eigenvalue shown, and the trace and Fredholm determinant have the displayed values. ∎

This is affirmative source-based positivity. It does not make the separately occurring signed Gram matrix positive, and its degree-one determinant does not equal the infinite-zero Xi determinant. The construction depends on v and the specified period map; a link to the Xi operator still requires the independent identification/limit gate DET-05.

## STEP7-03. The exterior-period identity is signed and includes nontrivial coefficients

The source explicitly records the relevant tensor form, not just an abstract exterior power:

- `SumIoPrAlt.lean:88–94`: `TensH` supplies signs ep_I in {+1,-1}; the inclusion of the I-th representation has form ep_I times its Hilbert inner product, and distinct summands are orthogonal for that possibly indefinite form.
- `SumIoPrAlt.lean:104–110`: `cmp l g` is the l-th compound matrix of g, with entries l-by-l minors; `wedge f` has determinant coordinates.
- `Development/AbelianVarietyTheory/Proofs/FlagMeasures/PairingEqLeadingMinor.lean:11–19`: the exterior Hermitian pairing equals the specified leading minor of Zhat, with a short source proof by the compound-matrix wedge identities.
- `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BlockProjectionBesselStatement.lean:9–10`: the actual period decomposition is, with its complete representation and analytic hypotheses retained,

\[
h_\Gamma(\rho(g)\omega',\omega)\,d_R\,\mathrm{amp}_R(g)
=\sum_I\epsilon_I\kappa_{1,I}\overline{\kappa_{0,I}}\,d_{R_I}\,\mathrm{amp}_{R_I}(g).
\]

Specializing rho to cmp_l turns the leading factor into D_l. This is exactly the identity used in `FirstNormAddSubsetIndicatorLe.lean:269–289`; the theorem `line_of_tens` has its assumptions at lines 180–215 and its conclusion at lines 216–221. Its final normalized coefficients a_I are supported on a predicate gd and satisfy the norm estimate

\[
|a_I|\le\sqrt{d_R/d_{R_I}}\,|\kappa_{0,I}\kappa_{1,I}|.
\]

The exact support hypothesis is `not gd I -> kappa0 I=0 or kappa1 I=0` at line 213. This formulation does not declare that these complex coefficients equal 0 or 1; it separately assumes whatever good/bad support predicate is being used. The signs, kappas and formal-degree factors therefore cannot be dropped to identify it with the threshold determinant in STEP7-01.

The source also has a nonnegative weighted orbital sum: `LeadMinorK.lean:218–221` defines BSum(X,W) as a sum over IsBPt of `ENNReal.ofReal(wPt * ptWeightG * W)` times JSq. `JSq` is a product of squared orbital norms at lines 180–182; the weight W here is a function on finite-dimensional arithmetic orbit data. Nonnegativity is built into the ENNReal codomain and ofReal truncation. This is not, by its displayed definition, a real or complex linear functional on one-variable explicit-formula test functions. `WFromLoc.lean:133–154` separately constructs vector-valued local Whittaker/Bessel functions Wloc on unitary groups, not a scalar test functional.

## Searches and read scope

This pass avoided repeating only the earlier exact-name search. It selected 527 source files containing an interlacing spelling and then 175 of those with determinant syntax; the path index is `step7_interlacing_det_paths.txt`. A bounded multiline threshold-matrix search produced 414 lines, retained in `step7_threshold_matrix_hits.txt`. A determinant/interlacing/staircase expression search is in `step7_det_interlace_named.txt`. These are candidate inventories, not complete mathematical reads of all candidates.

The read candidates included the exact files and ranges cited above, the source numerical sign polynomials in `HermitianCurvature/StatementI.lean:9–33` and `StatementM.lean:337–362`, and the cut-sign proofs in `CuspSpanNormBounds/OscillatoryIntegralBounds.lean:38–178`. They concern finite products of affine parameter factors, with signs set by interlacing; their variable Y is not identified with the Xi spectral parameter. The Gelfand–Tsetlin defect in `GelfandTsetlinTopCoefficient/InterlacingDefectEqCard.lean:19–82` is an integer/cardinality defect under interlacing, not a 0/1 period determinant.

Files whose titles suggest more than their content were not promoted to matches. For example `BesselGapDimensionFormula.lean` was inspected at its final norm-identity statement; it gives an integral norm identity, not a complete “dimension equals interlacing indicator” theorem merely by virtue of its name. `BesselMultiplicityOneL2.lean:22–27` states linear dependence of two L2-bounded Bessel maps under decay; it is a uniqueness statement with hypotheses, not the full missing historical determinant formula.

## Check and remaining exact information

Both new elementary proofs were read in their entirety after composition. The threshold count argument, determinant orientation, cross-equality endpoint, empty case and nonselfadjoint conclusion were checked. The period rank-one argument checks the source inner-product convention, domain requirement, zero-vector case, boundedness, selfadjointness, eigenvalue, trace and determinant. Source identities are cited source readings, not independent re-proofs of their lengthy analytic dependencies.

The remaining exact source gate is unchanged in its core: define the W and S from Remark steps4/6; give the matrix/declaration of step7 together with the test-function substitution and normalization; and prove that this correspondence is the one meant by the timeline. The present explicit selector and period identities are useful, sharply delimited components, not permission to erase that gate.
