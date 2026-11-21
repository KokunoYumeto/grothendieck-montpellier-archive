# Actual determinant source follow-up — 2026-11-21

Agent/checker: GPT-6 Astra Pro, `/root/determinants_audit`; effort setting not exposed. This supersedes the earlier claim in `determinants_audit.md` that only the supplied two Lean files were available for analysis. They were the only ones **initially supplied**, but the root subsequently found a working direct HTTP retrieval route. The web search service's `DisabledError` was tool-specific, not a proof that the source was inaccessible. The failed retrieval attempts remain historical events, not the final gate.

**Provenance update.** Root subsequently retrieved the full archive from a public GitHub release mirror, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`, and extracted it at `work/external_lean/lean/src`. This agent compared every separately fetched file listed below byte-for-byte by SHA-256 with its counterpart from that mirror archive; all agree. The comparison is recorded in `determinant_retrieval_manifest.tsv`. Thus the exact definitions cited here are also verified contents of the downloaded full mirror archive, not merely unverified mirror content.

The following source files were fetched directly from the public mirror `https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/main/src/`, then inspected as mathematical definitions and proposition statements. BesselPeriodGGP, StatementG/BF/DS, and StatementE/B were read in full; UpqRep, IsLowUnitH, and Complexify were inspected at their imports and initial definitions. No Lean build has been run. The mirror's source provenance is separate from the user's attached Main/Statements files; root is acquiring the full source archive from the release mirror for byte comparison and broader search.

- `Formalism/PeriodIntegrals/BesselPeriodGGP.lean`
- `Formalism/PeriodIntegrals/UpqRep.lean`
- `Formalism/PeriodIntegrals/IsLowUnitH.lean`
- `Formalism/FormalDegreeBessel/StatementG.lean`
- `Formalism/FormalDegreeBessel/StatementBF.lean`
- `Formalism/FormalDegreeBessel/StatementDS.lean`
- `Formalism/RealPlaceAnalysis/StatementE.lean`
- `Formalism/RealPlaceAnalysis/StatementB.lean`
- `Formalism/RealPlaceAnalysis/Complexify.lean`

The first file is the source explicitly suggested by the supplied prior map as a medium-confidence match to step 7. It imports StatementG/BF/DS. That verifies a source dependency, **not** an identification of every determinant mentioned in note step 7 with one of the definitions below, and not a declaration-level proof dependency of the final RH theorem.

## DET-06. The signed Gram determinant is positive while its Gram matrix is indefinite

**Exact definitions.** In namespace `Formalism.QuantumDeterminants`, `Formalism/FormalDegreeBessel/StatementG.lean` defines:

- `herm` at line 9, with h_H(v,w)=w*Hv;
- `UH` at lines 11–12, by g*Hg=H;
- `Hpk` at lines 20–24, of size 2r+k+1;
- `inWb` at lines 28–29, requiring coordinates outside the middle k+1 block to vanish;
- `Tz` at line 31, T(z)=−Re h_H(z,z);
- `fvec` at lines 61–62, the r isotropic standard vectors followed by z;
- `Zhat` at lines 64–66, the (r+1)×(r+1) pairing matrix h_H(g f_b(z′), f_a(z));
- `Dmin` at lines 68–71, its leading minor of order l;
- `Gf` at lines 85–88,
  G=|D_{r+1}|²−T(z)T(z′)|D_r|²;
- `gramVec` and `gramM` at lines 90–99, the Gram matrix of the 2r+2 vectors f_a(z), g f_b(z′).

The named proposition `GGram`, lines 165–168, asserts G=(-1)^{r+1}det(gramM) for z,z′ in the middle block and g in UH(Hpk). The proposition `GNonneg`, lines 170–172, adds T(z),T(z′)>0 and asserts G≥0. These are proposition **definitions** at the cited locators; the following calculation checks their hypotheses and conclusion in one example without presuming that a `def … : Prop` itself is a proof.

**Finding.** All the hypotheses of both `GGram` and `GNonneg` hold for

\[
k=2,\quad r=0,\quad H=\operatorname{diag}(1,1,-1),\quad
g=I_3,\quad z=(0,0,1)^T,\quad z'=(\sqrt3,0,2)^T.
\]

For these inputs,

\[
G=3>0,\qquad
\operatorname{gramM}=\begin{pmatrix}-1&-2\\-2&-1\end{pmatrix},
\]

whose eigenvalues are 1 and −3. Thus the source's signed Gram determinant positivity is not positive-semidefiniteness of its Gram matrix.

**Proof with all domains checked.** The type is Fin(2r+k+1)=Fin3. At r=0 the first two cases in `Hpk` are absent; its middle-block clause gives exactly diag(1,1,−1). For every i∈Fin3 the condition i<r or r+k<i is false, so `inWb 2 0` holds for every vector, in particular z and z′. Also g*Hg=H for g=I_3, so g∈UH(H). Direct computation yields z*Hz=−1 and z′*Hz′=3−4=−1, hence T(z)=T(z′)=1>0. This verifies every hypothesis of `GGram` and `GNonneg`; no constraint on c, Harish-Chandra parameter, or representation occurs in those two definitions.

Since r=0, `fvec` has one entry z (respectively z′). Therefore Zhat=[z*Hz′]=[−2], its order-zero leading determinant is D_0=1, and its order-one determinant is D_1=−2. Thus G=|−2|²−1·1·|1|²=3. The two vectors in `gramVec` are z,z′; their Hermitian pairings give the displayed matrix. It has determinant −3, so G=(-1)^{r+1}det(gramM)=3, as required. Multiplication shows (1,−1)^T is an eigenvector of eigenvalue 1, while (1,1)^T has eigenvalue −3. In particular the latter vector has quadratic form −6<0, and the Gram matrix is indefinite. ∎

**Interpretation.** This is an actual finite determinant in the imports of the source suggested for step 7. Its positivity is a statement about a signed determinant for an indefinite Hermitian form; it is compatible with a negative direction and cannot be read as positivity of that matrix. It therefore supplies a more concrete obstruction than the generic −I_2 example. It neither refutes `GNonneg` nor proves that the author intended precisely this determinant in note step 4 or step 7. No Xi variable or compression of the diagonal B occurs in these definitions.

**Complete check.** All source domains and the whole proof were reread after composition. r=0 is allowed in both propositions; k=2 also satisfies the even and ≥2 conditions in the nearby BesselPeriodGGP definition, although that larger proposition has further representation data not needed or asserted here. The order-zero determinant convention is the standard finite determinant 1, not a division by zero. Direct symbolic matrix calculation independently confirms the values.

## DET-07. The actual quantum determinant is an ordered Capelli polynomial

`Formalism/RealPlaceAnalysis/StatementE.lean`, namespace `Formalism.REAL`, defines `Tm` at lines 9–10, `qminor` at lines 12–15, and `qdet` at lines 17–18. With n indices starting at zero and E=(E_ab) in an arbitrary complex algebra A, the definition is exactly

\[
q\det_E(u)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_{j=0}^{n-1}\bigl((u-j)\delta_{\sigma(j),j}+E_{\sigma(j),j}\bigr),
\]

where the product is ordered by increasing j. It is a monic degree-n polynomial in a central scalar variable with coefficients in A. Its definition uses no Hilbert space, adjoint, norm, summability, or trace-class operator.

**Proof of the polynomial assertion.** Each factor is affine in the central scalar u, so the finite ordered product is polynomial of degree at most n, and so is the finite permutation sum. A term of degree n must select the scalar part of every factor, which requires σ(j)=j for every j. Only the identity permutation contributes, with sign +1 and leading coefficient 1_A. Thus its formal leading coefficient is 1_A (monic unless A is the zero ring). ∎

The proposition `QDetHW` at StatementE lines 40–43 states, under the gl_n commutation relations and a highest-weight vector of weight ν,

\[
q\det_E(u)v=\prod_{j=0}^{n-1}(u-j+\nu_j)\,v.
\]

`Formalism/FormalDegreeBessel/StatementDS.lean` defines `rhoStd` at line 23 and `capP` at line 25, capP(λ,Y)=∏_{j=0}^{n-1}(Y+λ_j). Its `CapelliHW` proposition at lines 83–86 makes the central shift explicit:

\[
q\det_E\left(Y+\frac{n-1}{2}\right)v
=\prod_{j=0}^{n-1}\left(Y+\nu_j+\frac{n-1}{2}-j\right)v.
\]

After specialization to this vector, this is a finite characteristic-polynomial type product. By DET-03 a fixed such scalar polynomial cannot equal Ξ(√w)/Ξ(0) after an affine change of its parameter. Before specialization it is a noncommutative determinant in an algebra, and identifying it with a Hilbert-space Fredholm determinant would additionally require a representation, bounded/trace-class control, a normalization, and a spectral identity. None is part of these definitions. Calling it a “finite analogue” is meaningful in the Capelli/characteristic-polynomial sense, not as evidence that it is a finite compression of the specified zeta operator.

**Complete check.** Definition expansion, finite index range, column shift, product ordering, highest-weight scalar shift and monicity have all been reread and checked. The proposition statements are reported as source content; no proof replay or claim that a declaration of a proposition proves it is made.

## Historical intermediate gate after retrieving the first nine sources

At that intermediate point, the available data included actual finite minors, an indefinite Gram determinant and an ordered quantum determinant in the step-7 candidate's imports. The full mirror archive subsequently became available; the targeted search below and the actual RH endpoint trace in DET-09 supersede the general source-access gate. The exact historical mapping of the note's W(1_S) and its full period determinant remains more limited. Step-7 code location is still a source-neighborhood match, not a fully established timeline-to-declaration identification.

## DET-08. The exact finite determinant link for the toy is a rank-one variation

With A=D_t^{1/2}K_hD_t^{1/2} and a=(√t(x)) as in DET-02, define P=aa*. For every k≥1,

\[
S_k(h)=\operatorname{Tr}(A^{k-1}P).
\]

Near z=0, the path generating function therefore has the finite determinant identity

\[
\sum_{k\ge1}S_k(h)z^{k-1}
=a^*(I-zA)^{-1}a
=-\left.\frac{\partial}{\partial u}\log\det(I-zA-uP)\right|_{u=0}.
\]

**Proof.** The diagonal sum of A^{k−1}aa* equals a*A^{k−1}a by expanding the two finite sums, which is S_k(h) by DET-02. The convergent Neumann series near z=0 gives the resolvent identity. For any invertible finite matrix M, multilinearity of the determinant in its columns gives

\[
\det(M-uaa^*)=\det M\bigl(1-u a^*M^{-1}a\bigr).
\]

Indeed, after factoring M, the determinant of I−u(M^{-1}a)a* has constant term 1, linear coefficient −u∑_i(M^{-1}a)_i\overline{a_i}, and all higher terms vanish because two selected rank-one columns are proportional. Set M=I−zA, choose the logarithm locally near (z,u)=(0,0) where the determinant is nonzero, and differentiate at u=0. This proves the displayed identity. ∎

This is a constructive determinant relation, but it concerns a pair (A,P) and a perturbation parameter. It does not identify S_k with Tr(A^k), make A positive, or connect its rational generating function to the nonpolynomial Ξ determinant. If one wants an analogue in determinant-line language, it is a first variation of a finite determinant under a rank-one correspondence, rather than a new Frobenius trace formula.

**Check.** Complete proof reread: the rank-one orientation aa*, order A^{k−1}P, minus sign of the derivative, local invertibility/logarithm, and the k=1 coefficient were checked. No spectral simplicity or self-adjointness is assumed.

## Full-source targeted search and further locators

The full mirror archive was searched with ripgrep, with results retained in `w_exact.txt`, `w_defs.txt`, `ggp_files.txt`, `ggp_determinant_intersections.txt`, `search_stepanov.txt`, and `search_wronsk.txt`.

- A case-insensitive search for `Stepanov` in all source files found zero occurrences. This agrees with the supplied prior map but does not establish that the Stepanov mechanism is absent under another name.
- An exact-name search found 62 `def W`/`abbrev W` declarations (excluding W′ and theorem bodies). The scalar candidates inspected included `Formalism/LFunctionBounds/Statement.lean:17` (a probability-weight marginal on triples), `Formalism/ThetaLogCoordinates/ResidueClassEstimates/VandermondeRankEstimates/Branch.lean:90` (a Vandermonde product), and `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MainXOfStepXLastX.lean:16` (a product of lift-chain constants). None of these is the note's unqualified Weil functional W(1_S). This exact-name route therefore does not finish the historical step-4 match.
- Searching the literal name `BesselPeriodGGP` found 230 files. Of these, 35 also contain actual `.det`, `qdet`, `Dmin`, or `GramDet` references; most are invertibility determinants of group elements. The actual leading-minor and exterior-power references below are stronger structural evidence.
- `Development/AbelianVarietyTheory/Definitions/Jets/SumIoPrAlt.lean`, namespace `BranchingSupport`, lines 104–110 defines the compound matrix `cmp l g` from l×l minors and the coordinates of `wedge f` from l×l determinants. These are explicit finite exterior-power constructions.
- `CompanionTheory/AutomorphicTheory/BesselWaveGrids/ProductMoment.lean:15–19` defines a leading minor `mnr`; its theorem `herm_wedge` at lines 44–50 identifies a Hermitian pairing on the exterior power with the corresponding leading minor of `Zhat`. The displayed proof unfolds the finite exterior-power identity. The file's later moment bounds involve squared norms of Bessel functionals with these minors; their full lengthy proofs were not independently checked in this subtask.
- `Development/AbelianVarietyTheory/Proofs/FlagMeasures/FirstNormAddSubsetIndicatorLe.lean:269–289` invokes `block_projection_bessel` and `PrincipalMinorExterior.pairing_eq_leading_minor`, then writes the leading minor times an amplitude as a finite sum over subsets I of signed products of Bessel scalars and formal degrees times other amplitudes. This is an actual connection between finite minors, exterior powers and period amplitudes. It is stronger than a namespace guess, but it still does not identify a spectral determinant in the Ξ variable.
- `Formalism/PeriodIntegrals/ExplicitFormula.lean:16–26` defines a truncated explicit formula for Dirichlet L-functions (finite sums of zero contributions plus an error bound), not a Fredholm determinant. `Formalism/PeriodIntegrals/ExplicitFormulaCounts/ExplicitFormula.lean:8–10` gives a named theorem `explicitFormula_closed` assembled from zero-window and analytic estimates.
- `Formalism/PeriodIntegrals/DivisionRowsRationalLattice.lean:190–207` defines a valuation inequality for the determinant of a Hermitian Gram matrix on a lattice, `GramDetKernelValuation`, and its base-level proposition. The word “kernel” here is the kernel/cut of a lattice projection, not a Fredholm integral kernel.

These locators support a finite exterior-power/period/lattice reading of the actual sampled determinants. They do not justify claiming a complete dependency graph from every note step, nor do they justify an impossibility theorem about every conceivable limiting construction in the full source. The root owns the independent global search for Ξ/Fredholm/spectral determinant connections.

## DET-09. The examined RH endpoint is a scalar Chebyshev/Landau window argument

**Status and scope.** This section follows actual declarations and immediate calls in the full GitHub release-mirror archive. It is source analysis, with a separate short algebraic check of the residue weights; it is not a Lean replay, a complete proof audit of the archive, or a new proof of the cited RH theorem. All paths below are relative to `work/external_lean/lean/src/`. The received `Main.lean` and `Statements.lean` are independently reported by the root as byte-equal to the mirror copies. The archive provenance is the mirror; agreement with the author's original fourteen-part archive has not been established here.

### The entry-to-inequality chain

The immediate chain is as follows. Long intermediate theorem files have been inspected at the indicated declaration and call sites; the many imported proofs beneath them have not all been read.

| Actual file and locator | Declaration or immediate call | Mathematical role |
|---|---|---|
| `Main.lean:1–8` | `riemannHypothesis := rhOfAll`; `LFunction_ne_zero_of_half_lt_re := allChi` | Exports the RH and character nonvanishing results. |
| `Supplements/Kernels/MainTheorems.lean:7–9` | `allChi := UpperTheory.FinalTheorems.everyCharacter`; `rhOfAll := Formalism.VW.rh_of_every allChi` | Reduces RH to the right-half-plane nonvanishing assertion. |
| `Formalism/GammaFactorNonvanishing/CritLine.lean:29–33`; `Formalism/GammaFactorNonvanishing/RhOfRight.lean:5` | `rh_of_every`, `rh_of_right` | Specializes to the trivial mod-one character; functional-equation reflection converts right-half-plane nonvanishing to the critical-line conclusion. |
| `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7–11` | `everyCharacter_of_row`, `everyCharacter` | Supplies the character theorem from the arithmetic and theta-lift package. |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:810–812` | `every_character_of_literature_of_vWin` | Calls the theta-integral/local-matching assembly theorem. |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69–73` | `every_character_of_theta_integrals_local_matching` | Calls `UpperTheory.Top.every_character_of_green_v_win`. |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:12–18` | `zero_free_all_of_green_v_win`, `every_character_of_green_v_win` | Calls `zeroFreeAll_of_topG` with `la := 3/2`, then passes primitive to imprimitive characters. |
| `Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean:26–34` | `zeroFreeAll_of_topG` | Calls `zeroFreeOn_of_tiedWin_cyc`, supplying `level_gm_le_on_family_scales` and `formB`. |
| `Development/AutomorphicArithmetic/PrimitiveCosets/LevelGmLeOnFamilyScales.lean:28–30` | `level_gm_le_on_family_scales` | Supplies the scalar Chebyshev inequality on family windows. |
| `Development/AutomorphicArithmetic/PrimitiveCosets/WindowInequalityOfArtinInputs.lean:17–25`; `Development/AutomorphicArithmetic/PrimitiveCosets/CoreGm.lean:12–15,55–74` | `windowInequality_of_artinInputs`, `core_gm` | Converts the arithmetic/family data into the explicit real inequality displayed below. |
| `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/TopWin.lean:23–32,68–93` | `ChebyshevInequalityOnWindows`, `level_of_tiedWin`, `zeroFreeOn_of_tiedWin_cyc` | Chooses arbitrarily small ε and invokes the scalar Landau criterion to exclude each zero with real part above 1/2. |

`CoreGm.lean:55–60` in turn invokes `Deduction.ch_core` and `Deduction.ch_top`. The latter is `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean:37–72`: it bounds the real arithmetic discrepancy `gapA` by a nonnegative scalar error bracket. Its lines 47–54 identify `gapA = Dd.ASK − Dd.Main` and invoke `each_unit_bound_statement`. That statement is at `Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean:175–197`, assembled from slope/divisibility/counting/loss estimates. These calls support the actual scalar/arithmetic description; they are not an assertion that every upstream determinant has been reconstructed.

### The scalar whose size is controlled

To avoid confusing the von Mangoldt function with the source's `Level` variable, write a level as \(\mathcal L\), and write \(\Lambda(n)\) for von Mangoldt. `Formalism/StatementOC.lean:11–13` defines

\[
G_\zeta(y)=\sum_{1\le n\le\lfloor y\rfloor}\Lambda(n)(y/n-1)
-y\log y+(1+\gamma_E)y.
\]

This is the concrete smoothed von Mangoldt expression appearing in step 5 of the supplied note. For a nontrivial primitive character χ, `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Analytic.lean:9–24` defines the complex scalar

\[
g_\chi(y)=\sum_{1\le n\le\lfloor y\rfloor}\Lambda(n)\chi(n)(y/n-1)_+
+y\frac{L'(1,\chi)}{L(1,\chi)}.
\]

The same definition gives the corrected principal-character expression in its trivial branch. For the range \(y\ge1\) used in the final argument, \((y/n-1)_+=y/n-1\) on the displayed summation interval.

`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean:32–41` defines the finite set \(\mathcal L.Nt=\mathcal L.KEPT\setminus\{1\}\), real weights

\[
w_\psi=\begin{cases}1,&\mathcal L.psK=\mathrm{some}(\psi),\\
(3\mathcal L.o+1)^{-1},&\text{otherwise},\end{cases}
\]

and

\[
G_{\mathcal L}(y)=G_\zeta(y)+\sum_{\psi\in\mathcal L.Nt}w_\psi\,\Re g_{\psi.\chi}(y).
\]

Every weight here is a strictly positive real number because \(\mathcal L.o\in\mathbb N\). The source declares a finite weighted sum of scalar functions. It does not declare these weights to be an operator's eigenvalues, a Gram metric, or a quadratic form on a test-function Hilbert space. In particular, positivity of these weights does not say \(G_{\mathcal L}(y)\ge0\).

### Window quantifiers and conversion to zero-freeness

The core result has the following type, exactly at `Development/AutomorphicArithmetic/PrimitiveCosets/CoreGm.lean:12–15`: for a level \(\mathcal L\), real parameters \(e_D,e_L,K,c_{HH},e_K,C\), and \(\varepsilon>0\), there exists \(x_1\) such that every \(x\ge x_1\) satisfying the stated `EAtH` and `CoreAtH` arithmetic data obeys

\[
G_{\mathcal L}(x)\le x^{\frac12+(e_D+e_L+7)\varepsilon}.
\]

The family-window version `TopWin.lean:23–32` has two layers. `ChebyshevInequalityOnWindows` states that the family hypotheses imply the displayed bound for all sufficiently large \(x\) **in that family's window set**. `ChebyshevInequalityAtWindowScale` states that there are fixed \(e_D,e_L\) and \(\varepsilon_1>0\) such that for every \(0<\varepsilon<\varepsilon_1\) there is a suitable family whose window set contains intervals \([Y,Y^{\lambda}]\) at arbitrarily large \(Y\), with \(\lambda>1\). Precisely, `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Window.lean:7–8` defines

\[
\mathrm{HasWindows}(S,\lambda)\iff
\forall y_0\in\mathbb R\ \exists Y\ge y_0\ \forall x,
\quad Y\le x\le Y^\lambda\Longrightarrow x\in S.
\]

The same file, lines 30–33, defines `Level.FormBAt` and `Level.FormB`:

\[
\forall\theta\in(0,1),\quad
\mathrm{HasWindows}(\{x:G_{\mathcal L}(x)\le x^\theta\},\lambda)
\Longrightarrow
\forall\psi\in\mathcal L.KEPT\ \forall s\in\mathbb C,
\quad \Re s>\theta\Longrightarrow L(s,\psi.\chi)\ne0.
\]

For a putative zero at \(s\) with \(\Re s>1/2\), `TopWin.lean:68–81` chooses

\[
\theta=\frac12+\frac12\min\!\left(\Re s-\frac12,\frac12\right)
\quad\text{and sufficiently small }\varepsilon>0
\]

so that \((e_D+e_L+7)\varepsilon\le\theta-1/2\). Thus \(1/2<\theta<\min(\Re s,1)\), and the window bound implies \(G_{\mathcal L}(x)\le x^\theta\) after enlarging the lower cutoff to at least 1. `FormBAt` excludes the putative zero. `TopWin.lean:90–93` applies this to the cyclic level containing any primitive character. `Development/AutomorphicArithmetic/CharacterBoxes/Imprimitive.lean:5–35` then handles changes of level by the Euler factors; `CritLine` and `RhOfRight` give the RH conclusion.

### What the positive residue statement actually says

The actual implementation of `FormB` is `Development/AutomorphicArithmetic/PrimitiveCosets/Imports.lean:8–19`. It uses `Development/AutomorphicArithmetic/PrimitiveCosets/LevelFamily.lean:41–52` to replace \(G_{\mathcal L}\) by a `Deduction.CharFamily`, and applies:

* `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ZeroFreeOfRpowWindow.lean:11–14`, `zeroFree_of_rpow_window`;
* `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/lemmaL.lean:13–22`, `lemmaL`;
* `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/poleData.lean:248`, `poleData`;
* `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean:83–87`, `landau_window`.

`Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean:24–39` declares a **finite index type** \(I\), Dirichlet characters \(\chi_i\) of nonzero levels, and a finite array \(\alpha_i>0\), with the admissibility condition \(N_i=1\) or \(\chi_i\ne1\). It defines

\[
G_F(y)=\sum_{i\in I}\alpha_i\Re G_{\chi_i}(y),\qquad g_F(u)=G_F(e^u).
\]

The \(G_{\chi_i}\) use the same smoothed von Mangoldt/logarithmic-derivative expressions; `LevelFamily.lean:27–46` explicitly supplies the equality \(G_F=G_{\mathcal L}\). The finite \(\alpha_i\) are character-averaging coefficients. Their positivity is not positive definiteness of a Gram matrix.

`Development/AutomorphicArithmetic/DedekindLFunctions/LandauZeroFreeCriterion.lean:15–23` defines `PoleData`: \(g_F\) is a measurable real function with at most \(Ce^{2u}\) growth for \(u\ge0\); for \(\Re s>2\), its scalar meromorphic transform satisfies

\[
\Phi(s)=\int_0^\infty g_F(u)e^{-su}\,du.
\]

Its pole set is the zeros in \(\Re\rho>0\) of the finite character family and their conjugates (`LandauZeroFreeCriterion.lean:11–13`). Outside that set it is differentiable, the set is locally isolated, and at each pole \(\rho\) its local principal part is \(c_\rho/(s-\rho)\), with \(c_\rho\ne0\). The special positivity assertion is **only for a real pole**: then \(c_\rho\) is real and strictly positive. The source does not assert that arbitrary complex residues are positive real numbers.

Here the residues are explicit. `poleData.lean:137–144` gives an individual local residue

\[
-\frac{m}{\rho(\rho-1)}=\frac{m}{\rho(1-\rho)},
\]

where \(m\) is the zero multiplicity. The multiplicity identification comes from `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/LogDerivLocal.lean:9–11`, whose type explicitly identifies \(m\) with `analyticOrderAt`. `poleData.lean:250–261` averages the transforms for \(\chi_i\) and \(\chi_i^{-1}\); its lines 344–364 give

\[
c_\rho=\frac{S_\rho}{\rho(1-\rho)},\qquad
S_\rho=\sum_{i\in I}\frac{\alpha_i}{2}
\bigl(m_i(\rho)+m_i'(\rho)\bigr)>0,
\]

where \(m_i,m_i'\in\mathbb N\) are the multiplicities for \(\chi_i\) and \(\chi_i^{-1}\). Nonvanishing on \(\Re s\ge1\) ensures that a real pole in this pole set satisfies \(0<\rho<1\), and lines 368–383 establish \(c_\rho>0\) in that case.

**Independent algebraic check, complete.** Each summand of \(S_\rho\) is nonnegative because \(\alpha_i>0\) and both multiplicities are nonnegative. Membership in the pole set supplies one character with positive multiplicity in at least one of the two terms, so one summand is strictly positive and \(S_\rho>0\). For \(\rho\ne0,1\), this makes \(c_\rho\ne0\); for a real \(0<\rho<1\), the denominator \(\rho(1-\rho)>0\), giving the positive real residue. For nonreal \(\rho\), the same algebra gives nonvanishing but no real-order positivity. All assertions in this paragraph have been reread and checked; they do not reproduce the analytic proof of `landau_window`.

The underlying analytic theorem says that a scalar Laplace transform with these pole data, together with the one-sided window majorants, has all its poles in \(\Re\rho\le\theta\). For reference, `landauWindow.lean:40–46` supplies an inequality for the normalized scalar derivatives

\[
\left|\frac{(-1)^k\Phi^{(k)}(\sigma+i\gamma)}{k!}\right|
+\Re\frac{(-1)^k\Phi^{(k)}(\sigma)}{k!}
\le\frac{C e^{\eta U}}{(\sigma-\theta)^k},
\]

on the quantified windows, and `landau_window` uses pole and growth estimates. This is a scalar complex-analysis endpoint; its variable \(\gamma\) is a free real ordinate, not an eigenvector index.

### What this resolves, and the exact remaining boundary

The examined endpoint of the actual RH entry path is now identified affirmatively: arithmetic/slope/divisibility bounds imply a scalar bound on a weighted smoothed von Mangoldt sum on large power windows; a scalar meromorphic Laplace-transform argument excludes zeros; functional equations conclude RH. Neither the defining inequalities nor their immediate analytic bridge is a statement \(\langle Bu,u\rangle\ge0\) for the specified normal trace-class zeta operator, or an equality of a finite determinant with \(\det(I-wB)\).

Consequently, the justified route from this endpoint to positivity of the independently constructed normal \(B\) in B-01 remains **cited RH → real zero ordinates → \(B\ge0\)**. The shared rational factor \(1/[\rho(1-\rho)]\) in the residue calculation and the Li-polynomial construction B-03 is a genuine algebraic resemblance. It is not an identified operator representation, positive Gram metric, spectral compression, or determinant equality in the inspected source.

The outstanding historical-source question is narrowly stated: match the note's unqualified \(W(1_S)\) and timeline determinants in steps 1 and 4, and the full exact step-7 period determinant, to specific declarations or an author-supplied dictionary. Exact-name and adaptive functional searches did not complete that historical match. The actual finite minors/Gram/Capelli objects in DET-06/07 and the actual scalar endpoint in DET-09 are established source findings. A stronger claim that some other part of the archive contains no possible limiting determinant construction is neither needed nor made.

**Bounded supplementary search.** Case-insensitive searches for `Guinand`, `WeilFunctional`, `Weil.*positiv`, and `positiv.*Weil` in `PositivityTheory`, `Formalism/LandauZeroFreeBounds`, and `Formalism/PeriodIntegrals` returned no name matches (`work/adaptive_guinand.txt`). Searching variance/second-difference spellings in `Formalism/LandauZeroFreeBounds` returned nine lines (`work/adaptive_variance.txt`), chiefly scalar finite-difference bounds. The inspected `Formalism/LandauZeroFreeBounds/ExceptionalZeroBounds/AbsZeroTermSecondDifferenceLe.lean:21–24,68–70` gives absolute scalar error bounds for a zero contribution and a main term, not an operator positivity criterion. Those findings do not identify the note's historical “variance trick”; the entry-path trace above is stronger and resolves the mathematical type of the actual final analytic endpoint.

**Check discipline.** The formulas, window quantifiers, positive-weight distinction, real-pole qualification, immediate dependency edges, and their cited declaration locations were reread after writing. No Lean execution or replay was performed, and no independent verification of every upstream analytic/arithmetic proof is claimed.

