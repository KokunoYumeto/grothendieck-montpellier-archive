# Step 2 after recovery of the targeted Lean sources

Author/reviewer: `/root/step2_higher`, GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21 UTC. This memo supersedes any implication in the earlier source inventory that the named local interfaces remain unidentified. It does not change the instruction to cite Alpöge's theorems, and performs no RH/GRH audit.

## 1. Provenance and main conclusion

The newly read source is the public repository **CocoSgt/riemann-hypothesis-lean**, pinned to commit **7cbf7a0c32fca1badf05931879a37c3f8a2b03b4**, under `src/`. This is different from the Deicyde repository and its different commit mentioned by the external reading guide. The recovered files are under `research/external_lean`; the original recovery hashes are in `targeted_metadata.json`, and the six additional targeted files fetched for this memo are recorded in `step2_extra_metadata.json`. No branch-head content is silently substituted for this commit.

The one-dimensional theorem identifies the coefficient `p/(p²−1)` in the informal scalar step 2. The recovered code gives precise additional structure for its use in the global construction: a normalized multivariate theta expression, integral exponential coboundaries, a two-type Frobenius orbit, minors and Young-diagram degrees, integral path expansions, and controlled denominators. **Changing the height constant alone does not preserve these hypotheses.**

There are two different local estimates in the recovered material. The `JetBounds` interface supplies **lower valuation** bounds for global pairings. The `CartierLocalBounds` interface also contains **upper valuation / controlled nonvanishing** statements. They must not be conflated.

## 2. Exact locators and what they say

All paths in this section are relative to `src/` at the pinned commit. Line numbers locate the read revision; declaration names are the stable semantic locators.

| Source | Exact locator | Relevant content |
|---|---|---|
| `Formalism/SharpRestriction/Divisibility/CartierLocalBounds.lean` | `rho`, line 18; `gam`, line 20 | `rho(p)=1/(p²−1)`, `gam(p)=p/(p²−1)`; the exponent is fixed at two |
| Same | `vLe`, line 30; `vGe`, line 32 | `vLe(x,b)` is `p^(−b)≤‖x‖`, hence `v_p(x)≤b`; `vGe` is the opposite norm inequality |
| Same | `jetAt0`, line 48; `LamOf`, line 54; `ThmP`, line 80 | Multivariate factorial-weighted coefficient pairing, powers of two determinant operators, and existence of a derivative with controlled nonzero value |
| Same | `LocD.d_even`, line 107; `LocD.Alternating`, line 201 | Even Frobenius orbit and two types alternating according to parity |
| Same | `RankOneLocalSpread`, line 372; `RankTwoLocalSpread`, line 379 | Unit determinants of `p·alC[2]` after a shift by two and `p·beP[1]` after a shift by one, with explicit rank losses |
| Same | `AdmLoc`, line 467; `RealisationStatementAll`, line 471 | Six named local input packages; the global local-result interface is conditional on these inputs |
| Same | `Loc.ty_succ`, line 491; `ty_inj`, line 492; `loc_big`, line 502; `loc_alt`, line 506 | The index `d` parametrizes an actual Frobenius orbit of embeddings and its CM-type membership; it is not a free replacement for one-dimensional formal height |
| `Formalism/SharpRestriction/Divisibility/ProductZerothFirstParts.lean` | `B1`, line 37; `B2`, line 43; `B3`, line 47; `B4`, line 70 | Unramified coefficients, signed Teichmüller invariance, a bidegree exclusion, and integrality of two exponential coboundaries |
| Same | `Loc.B0`, line 192; `Loc.AdmB`, line 199 | The normalized theta pullback is an integral factor times a specified exponential twist after `jetLogG`; the rescaling parameter has norm one |
| `Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/UniformBoundAllData.lean` | `tieB_of`, line 10; `tieB`, line 26 | Converts `B1`–`B4` to the precise `BHyp` package by the previously established letter-log integrality statement |
| `Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/LetterLogIntegrality.lean` | `jetLog_rename`, lines 216–242 | The displayed proof explicitly uses orbit shift `−2e` and monomial degree `(p²)^e` |
| `Formalism/LocalToGlobal/Divisibility/JetBounds/IsExpansion.lean` | `IsSys7.caseA`, `caseB`, `IsEntry7`, `PathData`, `IsExpansion`, `StabDvd` | Precisely specified admissible jet entries and the expansion of the global pairing into products of such entries |
| `Formalism/LocalToGlobal/Divisibility/JetBounds/Statement.lean` | `PlaceInputAtEntry`, `LocalValuationBound` | Converts entry estimates, integral endpoint data and bounded denominators into the arithmetic lower valuation bound |
| `Formalism/LocalToGlobal/Divisibility/JetBounds/PlaceInputAllEntries.lean` | `IsEntryAll`, `PlaceInputAllEntries`, `LocalValuationBoundAllEntries` | Allows the additional integral, Weyl and ramified entry types; retains the exact path-expansion and denominator requirements |

A pinned source URL, for example, is <https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Formalism/SharpRestriction/Divisibility/CartierLocalBounds.lean>. The same prefix and commit apply to the other paths.

## 3. What is additional to the universal scalar derivative bound?

### 3.1 Literal scalar step 2

For a single integral one-dimensional formal group over `W(k)`, the derivative estimate requires no CM or theta-specific identity. To apply it to the analytically normalized expression in the note, one needs an integral formal function representing the chosen section, a compatible local frame or connection, and the comparison of the analytic differential divided by the period with the normalized invariant derivation. If the scalar is `u` and the coefficients have bounded denominator `p^M`, the correction is exactly `n v_p(u)−M`.

The recovered code now identifies the relevant kinds of normalization, rather than leaving them as unnamed possibilities:

* `ThetaFramePullback.lean`, `IsGenOver` (19), `IsGenAt` (25), `GenMatch` (28), and `ThetaFrame` (75), specifies an integral theta **generator of the section module** and compatible rigidified line-bundle pullbacks. A theta generator is not automatically a nonvanishing local trivialization of the line bundle on the abelian variety. Comparing it with an arbitrary generic-fibre generator uses `u∈T.Frˣ`; this means a nonzero field scalar, not a unit of the integral valuation ring.
* `LinePeriodExponential.lean`, `IsCurveExp` (53), `IsExp` (96), and `IsFamExp` (129), specifies complex analytic uniformizations and the identity `e(z)∘φ_a=ex(z·Pe(a))`. `HasPeriod` (61) is expressed through the mean of logarithms of archimedean Lie norms. These declarations are useful normalization data but should not be misquoted as a standalone `p`-adic period valuation identity.
* `Development/AbelianVarietyTheory/Definitions/CMLattices/IsDiffOf.lean`, `Ell` (35), includes an elliptic curve and an integral Lie basis. `IsTen` describes a Serre tensor construction from it. `HasType` and `CMObj.typeP/typeM` use the two embeddings of the specified quadratic subfield, with complementary signatures `(1,0)` and `(0,1)`.

This source reading identifies interfaces and hypotheses. It does not assert that the bare file containing a definition has independently constructed every object or checked every imported theorem.

### 3.2 The actual multivariate lower-bound interface

`ProductZerothFirstParts.Loc.AdmB` requires a scalar of norm one and an exponential series `be` satisfying all five conditions:

1. **B0: normalized theta expression.** After the specified logarithmic substitution, the theta expression equals an integral power series `U` times the exponential of a row sum of `be`, with sign `±1`.
2. **B1: coefficient field.** Every coefficient of `be` belongs to `Wfrac`, the closure of the field generated by prime-to-`p` roots of unity over `Q_p`.
3. **B2: torus invariance.** The finite Teichmüller action twists the even orbit coordinates and odd orbit coordinates with opposite characters.
4. **B3: vanishing conditions.** Every nonzero term has positive degree in both parity classes and does not have bidegree `(1,1)`.
5. **B4: biextension-type integrality.** Both addition coboundaries, one in each parity class, have exponential that becomes integral with constant term one after the fixed logarithmic substitution.

The actual bridge `tieB_of` reads these conditions and produces an unramified coefficient subfield, a primitive root of order `p^d−1`, and `BHyp`. Consequently the fact that intermediate expressions live over `O_{C_p}` does not mean the lower-bound theorem has omitted its unramified model: `IsSys7.caseA` and `caseB` explicitly require one. A base change of our theorem from an unramified integral group is harmless; mere residue height over an arbitrary ramified ring would not suffice.

`IsSys7.caseA` then requires an even orbit `d`, the `BHyp` series, a substitution inverse to the fixed `entLog`, integral unit-sign data, and specific products of minors, column heights, and degree constraints. `caseB` uses the corresponding two-coordinate `oneLog` setup. The coefficientwise derivative inequality for arbitrary `f` does not by itself produce B0–B4 or those minor identities.

Finally the global pairing must equal an integral path expansion. `PlaceInputAtEntry` and its all-entry variant require:

* a completion embedding with the specified normalization of valuation and ramification index;
* `IsExpansion`, the identity expressing the global pairing as a finite sum of path products;
* integral row and column coefficients, integral final factors and phase factors;
* a common stabilizer denominator `D`, together with one distinguished unit stabilizer in each path;
* admissible local entry bounds and a comparison of their sum, after subtracting denominator losses, with the claimed global valuation.

This is a concrete comparison theorem already represented in the recovered source. For a proposed height-`h` improvement, the missing result is a **new realization of this same interface, or a proved replacement interface**, with the desired stronger entries and all losses controlled. It is no longer accurate simply to say that no bridge has been located.

### 3.3 The separate Cartier content/nonvanishing interface

`ThmP` studies a specially normalized exponential with leading cross term

\[
 -p^{-e_i}\sum_{b,c}X_{bc}^{p^i}Y_{bc},\qquad
 e_i=1+p\sum_{0\le t<(i-1)/2}p^{2t},\qquad i\text{ odd}.
\]

It applies determinant operators `det_L^(p^i y)det_R^y` and finds an integer `y` in a controlled interval at which the result has bounded valuation **above**. `CHAt` likewise finds a Hodge–Tate determinant with bounded valuation above; `ContentAt` finds a determinant-product value with bounded valuation above. `UBAt` even asserts a unit value in its specified small-degree range.

These assertions require nonvanishing and control of leading coefficients. The six fields of `AdmLoc` are the Cartier–Frobenius recursion, a two-step rank-spreading condition, the Lie-leaf derivative identity, a one-step cross-type rank-spreading condition, a Frobenius normed ring/module realization, and the exact leaf-evaluation rule. The latter evaluates the prescribed global jet as an integral substituted series multiplied by an exponential cross term. `RealisationStatementAll` also uses a determinant differential identity and a linear-programming duality statement whose constraints involve **odd** orbit distances.

These are exact inputs of this richer local content argument. They are not asserted to be a minimal list of hypotheses for the informal one-variable scalar inequality in step 2.

## 4. Checked propositions about the proposed higher-height replacement

### SHA7. Lower divisibility cannot imply the required nonvanishing

**Proposition.** For any finite-height integral one-dimensional formal group, even the complete collection of the universal derivative lower bounds for an integral function does not imply that some prescribed positive-order determinant jet is nonzero or has any finite upper valuation bound.

**Proof.** Take the nonzero integral function `f=p^N`, with `N≥0`. Every invariant derivative of positive order is zero. On a product of formal groups the same is true for every positive-order monomial in the invariant derivations, and hence for every homogeneous differential operator of positive degree. In particular, for `n_0≥1` and `y≥1`, the determinant operator with symbol

\[
P=(\det X)^{p^i y}(\det Y)^y
\]

has degree `n_0(p^i+1)y>0`, so `jetAt0(P,f)=0`. It satisfies every lower valuation bound, with valuation `+∞`. But `vLe(0,b)` is false for every finite real `b`, because `p^(−b)>0` and `‖0‖=0`. This also uses a function that is a unit on the generic fibre. ∎

The counterexample refutes the implication from the scalar height estimate to the **nonvanishing part** of the Cartier interface. It does not satisfy the prescribed nonzero exponential main term and unit-minor hypotheses, and is not claimed to refute the actual source theorem. The role of those additional hypotheses is exactly what the example isolates.

### SHA8. Frobenius orbit length is not one-dimensional height

**Proposition.** Consider an unramified local CM factor of rank one over a degree-`d` local CM coefficient field. Enumerate its embeddings along a Frobenius orbit by `a∈Z/dZ`, and let `ε(a)∈{0,1}` indicate the CM type. Its height is `d` and its dimension is `Σ_a ε(a)`. If `d` is even and `ε(a)=1` exactly at even `a`, its dimension is `d/2`. Hence an alternating factor of this rank can be one-dimensional only when `d=2`.

If the orbit is self-conjugate, complex conjugation is the shift by `d/2`, and the CM type satisfies complementarity, then the alternating pattern is compatible with that complementarity only when `d/2` is odd.

**Proof.** The height and dimension counts are the local CM-type formula in Tate, exposé 352, §5, definition p.106 and Theorem 3/formula (10*) p.107, already source-checked in the earlier memo. Half the residues in an even cycle are even, proving the first assertion. In a self-conjugate unramified orbit, the nontrivial involution is the half-orbit shift. Complementarity is `ε(a+d/2)=1−ε(a)`. Parity reverses under this shift exactly when `d/2` is odd. ∎

The immediate obstruction for the user's proposed line is stronger than a numerical mismatch: a one-dimensional local CM factor of height `h>2` has just one selected embedding on its length-`h` orbit and a distinct conjugate factor with `h−1` selected embeddings. It therefore cannot be substituted for a rank-one **alternating** block while retaining the source's CM-type pattern. For odd `h`, evenness already fails; for even `h>2`, the dimensions differ. For example the complementary local patterns `(1,0,0,0)` and `(0,1,1,1)` of a height-four line and its dual have dimensions one and three, whereas the alternating pattern has dimension two on each orbit.

The actual `LocD` can have larger rank and a toric/rank defect. Thus its integer `d` is not its total height in general either. The precise claim above is about a rank-one local CM block. No claim is made that every orbit in the actual construction is self-conjugate; the half-orbit conclusion is explicitly conditional.

### SHA9. A naive two-step unit-minor rule fails at higher one-dimensional height

**Proposition.** Let `F/W(k)` have height at least `h≥3`, and let `L(t)=t+Σ_{m≥2}ℓ_m t^m` be its normalized logarithm. Then `ℓ_{p²}∈W(k)`, so `pℓ_{p²}` is never a unit. There is a strict integral coordinate in which both `ℓ_p` and `ℓ_{p²}` vanish. Consequently a defect-free rank-one rule requiring the `1×1` determinant `pℓ_{p²}` to be a unit cannot follow merely by replacing height two by height `h`.

**Proof.** Put `q=p^h`. Comparison of coefficients in `L([p](t))=pL(t)` gives

\[
(p-p^m)\ell_m=a_m+\sum_{2\le j<m}\ell_j[t^m][p](t)^j.
\]

For `m<q`, every coefficient of `[p](t)` used on the right is divisible by `p`. Induction gives `ℓ_m∈W(k)` for every such `m`. Since `p²<q`, this proves the first claim. The strict integral coordinate `z=t+Σ_{2≤m<q}ℓ_m t^m` makes the logarithm `z+O(z^q)`, proving the second. ∎

This is the precise coefficient-level obstruction to transplanting `RankOneLocalSpread` unchanged into a one-dimensional height-`h` logarithm: with rank one and zero allowed rank loss, that condition demands a unit minor of `p·alC[2]`. When that coefficient is identified with the degree-`p²` logarithm coefficient, the preceding proposition rules it out. This identification is stated as part of the proposed rank-one transplantation; the proposition does not assert that a coefficient in every higher-dimensional source chart has been identified with a scalar formal logarithm.

## 5. Consequences for fewer theta lifts

For a genuine integral one-dimensional height-`h` direction the universal bound gives the larger slope

\[
c_h=\frac1{p-1}-\frac1{p^h-1},\qquad
1<\frac{c_h}{c_2}<1+\frac1p\quad(h>2).
\]

This is a valid local improvement. The source's original quadratic-type construction fixes a two-step logarithm, an alternating type, and odd-distance interactions. The propositions above refute the claim that the full construction can be upgraded solely by replacing `p²` with `p^h` or `gam(p)` with `c_h`.

A shorter alternative chain remains a separate mathematical possibility. To establish one using the recovered architecture, one must produce replacement normalized theta data and admissible jet entries; prove their multivariate bounds; construct the path expansion with integral endpoints and controlled stabilizers; and show that the total period, rank and level costs improve. This is now a precise source-level comparison problem rather than an unidentified appeal to “multiplicity.”

There is also a valid but conditional dimension accounting observation. Distinct height-`h_i>2` one-dimensional CM factors, together with their distinct conjugate companions, consume `h_i` abelian dimensions per chosen line. For disjoint pairs, `Σ_i h_i≤g`. Therefore

\[
\frac{c_{h_i}}{h_i c_2}<\frac{1+1/p}{h_i}\le\frac12.
\]

It would disfavor higher height **if** cost were proportional to these consumed dimensions and gain counted just the selected lines. No identification of that toy accounting with the actual global cost functional is asserted here, and complementary higher-dimensional factors are not assumed to contribute no other gain.

## 6. Actual check events

| Event ID | Object | What was actually checked | Result |
|---|---|---|---|
| RSL-S-001 | `CartierLocalBounds.lean` | Read the complete file and all local structures/claims, including the direction of the norm inequalities and all six `AdmLoc` fields | Source statement check passed; not a kernel execution |
| RSL-S-002 | `CanonicalTranslateJets.lean` | Read the local structure and admissibility/jet statements; checked that `overG` concerns the auxiliary primes and that its low-degree integrality input is not the inert-prime `gam` estimate | Source identification passed |
| RSL-S-003 | `ThetaFramePullback`, `LinePeriodExponential`, `Definitions/CMLattices/IsDiffOf` | Read complete files; distinguished section generators, rigidified matching, complex periods and integral tangent bases | Source identification passed |
| RSL-S-004 | `JetBounds/IsExpansion`, `Statement`, `PlaceInputAllEntries` | Read complete files; mapped the local entry prerequisites and exact finite-path global valuation interface | Source identification passed |
| RSL-S-005 | `ProductZerothFirstParts` B0–B4; `UniformBoundAllData.tieB_of`; `LetterLogIntegrality.jetLog_rename` | Read these exact definitions and bridge arguments, including parity, unramified coefficients, exponential coboundaries and the explicit two-step logarithm | Source identification passed; not a claim to read every imported Gauss-jet proof |
| RSL-P-001 | SHA7 | Derived and reread the complete constant-function determinant counterexample, checking the quantifiers `n0,y≥1` and the strict positivity of `p^(−b)` | Passed |
| RSL-P-002 | SHA8 | Derived and reread the complete CM orbit-count proof and conditional self-conjugation parity test | Passed; Tate's CM decomposition is cited background |
| RSL-P-003 | SHA9 | Derived and reread the complete coefficient recurrence/integral-coordinate proof and its explicitly conditional comparison with the rank-one source minor | Passed |

All events occurred on 2026-11-21 UTC, by `/root/step2_higher`, GPT-6 Astra Pro, effort setting not exposed. The source identifier `admitted` in these files is a defined predicate packaging geometric inputs; it is not the Lean `admit` tactic. No inference about the final theorems' validity is drawn from the fact that an interface is defined conditionally.

## 7. Exact proved bridge declarations, and the remaining independent inputs

The following declarations are actual theorems in the recovered files. They should be distinguished from the proposition definitions in `JetBounds/Statement.lean`. This is a source-interface identification, not a new Lean execution or a repetition of the accepted global theorem's verification.

The long namespace prefix for the first group is `Formalism.MainNotions.DIV.Bridge`. The prefix for the Gauss theorems is `Formalism.DworkPowerSeriesWeights`.

| Proven step | Theorem and exact locator | Hypotheses and output |
|---|---|---|
| Exponential-coboundary integrality | `LetterLogIntegrality.integrality_of_letter_log`, `JetPolynomialLogs/LetterLogIntegrality.lean`, lines 322–328 | Prime `l`, nonzero `d`, and `B3`, `B4` give integrality and constant term one of both `exp(de1 be)` and `exp(de2 be)` after `letterLog` |
| The `B1`–`B4` package | `OneLetterJetKernel.tieB_of`, `JetPolynomialLogs/UniformBoundAllData.lean`, lines 10–24; `tieB`, line 26 | For `l≥5`, `d≥2` even, the four hypotheses produce a subfield `K0` satisfying `Unram`, a primitive root `ζ` of order `l^d−1`, and `BHyp l d K0 ζ be`. `tieB` supplies the preceding integrality theorem to `tieB_of` |
| The normalized kernel from `B0` | `OneLetterJetKernel.kernel_from_twist_holds`, `JetPolynomialLogs/OneLetterJetKernel.lean`, lines 54–90 | From `‖ep‖=1` and `L.B0 ep be`, constructs `g` with zero constant terms and `subst g entLog = X`, an integral `U`, and sign `ε=±1`; identifies the unit-rescaled theta with `thetaZ g U ε be` |
| The one-letter normalized kernel | `OneLetterJetKernel.kernel_twist_one_letter_vanishing`, same file, line 172, and `kernel_twist_one_letter_holds`, line 568 | From `‖ep0‖=1`, `B3 l 2 be` and the one-letter `B0`, produces the inverse of the fixed `oneLog`, integral `U`, sign and unit phase, and the corresponding `thetaOne` identity |
| Coefficient estimate to theta jet | `OneLetterJetKernel.tieFrame`, same file, lines 418–439; `tieFrameOne`, lines 534–566 | From bounds for coefficients of the minor frame jet of the unit-rescaled theta, deduces the corresponding `KvalGe`; homogeneity and the unit norm remove the rescaling without loss |
| Gauss bounds | `thmAGauss`, `GaussJetBounds/ThmAGauss.lean`, lines 8–9; `oneLetterGauss` and `thmAEntry`, `GaussJetBounds/OneLetterGauss.lean`, lines 7–8; `thmAEntryFull`, `GaussJetBounds/ThmAEntryFull.lean`, lines 8–14 | These are the proved entry estimates invoked by the bridge. Their statements include the unramified field, primitive root, `BHyp`, fixed logarithm inverse, integral factor, unit/sign data, and explicit minor size hypotheses. `thmAEntryFull` applies `thmAEntry` with the proved slope-saturation estimate |
| Assemble the local theta bound | `DworkPowerSeriesWeights.thmA_of`, `JetPolynomialLogs/DworkPowerSeriesWeights.lean`, lines 177–211; `thmOne_of`, lines 235–262 | The hypotheses `TieB`, the relevant normalized-kernel theorem, the relevant frame-comparison theorem, and `L.AdmB` give `L.ThmA 1` or `L.ThmOne 1`. The proofs invoke `thmAGauss` or `oneLetterGauss` with the constructed data |
| Convert entry norms into global arithmetic valuations | `Formalism.L2.DIV.valuation_of_entry_bounds`, `LocalToGlobal/Divisibility/JetBounds/JetBoundsProofs/ValuationOfEntryBounds.lean`, lines 13–31 | Requires the number field embedding `EmbAt`, exact pairing expansion `IsExpansion`, integral columns, rows, last factors and units, a common stabilizer denominator `StabDvd`, actual entry norm bounds, and the comparison of the target with the sum of exponents less denominator losses. Concludes `LocalValuationBoundAt`; its proof calls `path_height_bound` and `embedding_lower_bound` |

`PlaceInputAtEntry` is defined in `JetBounds/Statement.lean`, lines 56–63. It packages the geometric input and admissible entry descriptions needed for the last step. It is **not** an output forced by arbitrary `B0`–`B4` data. In particular, neither the normalized theta hypotheses nor the one-dimensional formal-group estimate by themselves construct a global path expansion, its integral endpoint lattices, or a common stabilizer denominator. No theorem name for such an unconditional implication is asserted here.

The source of the exact local extra hypotheses is now explicit: `GaussJetBounds/Statement.lean`, lines 85–93, defines `BHyp` as coefficient membership in `K0`, signed torus invariance, exclusion of low bidegrees, and the two integral exponential coboundaries with constant term one. `Unram`, lines 95–96, demands that nonzero elements of `K0` have norm an integral power of `‖l‖`.

**Recommended resolution of the earlier U1 gate.** The source-identification question can be closed: the leading scalar coefficient in step 2 is the universal height-two coefficient, while its theta application uses the integral theta/rigidification and period/tangent normalization. The recovered later multivariate implementation additionally uses precisely the data listed above. The substantive remaining question for a higher-height proposal is the construction and cost analysis of a replacement normalized theta and path system. It is not a missing source identification for the accepted height-two theorem, and no re-audit of Alpöge's final theorem is needed to make this distinction.

## 8. SHA10 / paper DP21: the fixed one-letter logarithm cannot be a higher-height scalar logarithm in integral coordinates

### Exact source input

`Formalism/GaussJetBounds/Statement.lean`, lines 175–177, defines, for one variable,

\[
\operatorname{oneLog}_p(T)=\sum_{e\ge0}\frac{T^{(p^2)^e}}{p^e}
=T+\frac{T^{p^2}}p+\cdots.
\]

The coefficient has positive sign: it is exactly `+1/p`. This follows directly by setting the coefficient multi-index to `single x (p²)` in the displayed finite coefficient sum: since `p≥2`, only `e=1` contributes. The corresponding definitions of `letterLog`, lines 74–76, and `entLog`, lines 120–123, have the same denominator and degree, with orbit index shifted by `−2e`. The inverse identity with `oneLog` is an explicit hypothesis in `OneLetterR`, line 189, and in `KernelFromTwistOneLetter`, `JetPolynomialLogs/DworkPowerSeriesWeights.lean`, lines 213–222. Thus the fixed height-two logarithm is actual data in the source, not an inference from a variable named `d`.

### Proposition SHA10 (literal scalar-logarithm obstruction)

Let `R=W(k)` with `k` perfect of characteristic `p`, and let `F/R` be a one-dimensional commutative formal group whose special fibre has height at least `h≥3`. Let `L_F(T)=T+Σ_{n≥2}ℓ_nT^n` be its normalized logarithm. For every integral coordinate change `φ(T)∈TR[[T]]` with unit linear coefficient and every unit `a∈R×`,

\[
[T^{p^2}]\,aL_F(\phi(T))\in R.
\]

Consequently `aL_F(φ(T))` cannot equal `oneLog_p(T)`. In particular no integral strict change of coordinate, with a unit change of differential normalization, makes a height-at-least-three scalar logarithm into the unchanged one-letter logarithm used in the source.

**Proof.** Put `q=p^h` and write `[p]_F(T)=Σ_{r≥1}a_rT^r`, where `a_1=p`. Because `R` is unramified and the special-fibre height is at least `h`, `a_r∈pR` for every `1≤r<q`. The logarithm identity is

\[
L_F([p]_F(T))=pL_F(T).
\]

Suppose inductively that `ℓ_j∈R` for `1≤j<n<q`, with `ℓ_1=1`. Degree `n` gives

\[
p(1-p^{n-1})\ell_n
=\sum_{1\le j<n}\ell_j\,[T^n]([p]_F(T))^j.
\]

Every coefficient of `[p]_F` appearing on the right has index at most `n<q`. For each `j` its contribution belongs to `p^jR`, so the entire right side belongs to `pR`. Since `1−p^{n−1}` is a unit, `ℓ_n∈R`. Induction therefore proves integrality of every logarithm coefficient of degree less than `q`, in particular of all coefficients of degrees at most `p²`, because `p²<q`.

In the composition `aL_F(φ(T))`, the coefficient of `T^{p²}` depends only on `a`, the coefficients of `φ` of degree at most `p²`, and the coefficients `ℓ_j` with `j≤p²`. All of them are integral; indeed the coordinate and scalar assumptions give units where a normalization requires them. The coefficient is therefore integral. The coefficient `1/p` of `oneLog_p` is not integral, proving the assertion. ∎

One can independently check the same obstruction directly: if an integral formal group had normalized logarithm `oneLog_p`, then its `p`-series would start

\[
[p](T)=pT+(1-p^{p^2-1})T^{p^2}+O(T^{p^2+1}),
\]

since `oneLog_p^{-1}(X)=X−X^{p²}/p+O(X^{p²+1})`. Its reduction would therefore have first nonzero degree `p²`, hence height exactly two. Integral coordinate changes preserve that height.

**Scope.** This refutes a literal replacement of the actual scalar formal group while keeping the fixed logarithmic coordinate identity. It does not prove that a particular theta function can never have a fortuitous alternative expression with the old kernel, that all higher-rank `LocD` objects have one fixed Newton slope, or that no different higher-height theta construction exists. Such broader conclusions do not follow from this coefficient comparison. The unramified hypothesis is essential for deducing divisibility by `p` from the residue-height condition; the statement also works over any base for which that stronger coefficient divisibility is separately assumed.

## 9. Additional source and proof check events

| Event ID | Object | What was actually done | Result |
|---|---|---|---|
| RSL-S-006 | `GaussJetBounds/Statement.lean` | Read the complete definition file and directly computed the `p²` coefficient of `oneLog`; checked `letterLog`, `entLog`, `BHyp` and `Unram` at their exact definitions | Source formula and sign confirmed |
| RSL-S-007 | Theorem chain in §7 | Read the bodies of `tieB_of`, `tieB`, `kernel_from_twist_holds`, `tieFrame`, `tieFrameOne`, `thmA_of`, `thmOne_of`, the named Gauss wrapper declarations, and `valuation_of_entry_bounds`; distinguished their assumptions from the separate path-construction input | Source implication map confirmed; no claim to read every imported proof or run Lean |
| RSL-P-004 | SHA10 / proposed DP21 | Derived and reread the complete coefficient-induction and integral-coordinate proof, checking `p²<p^h`, the unit `1−p^(n−1)`, the finite dependence of a composition coefficient, and the exact nonintegral target `1/p` | Passed |
| RSL-P-005 | Independent check of SHA10 | Computed the leading term of `oneLog_p^{-1}∘p oneLog_p`; verified its unit coefficient at degree `p²` and height preservation under integral coordinate change | Passed |

These events occurred on 2026-11-21 UTC, by `/root/step2_higher`, GPT-6 Astra Pro; effort setting not exposed. Additional downloads, all from the same pinned commit, are fingerprinted in `step2_extra_metadata_2.json` through `step2_extra_metadata_5.json`. The root agent separately verified recovered modules against the author's published split archive; that is a separate provenance check and is recorded by the root's own manifest, not misrepresented here as my independent archive extraction or kernel check.
