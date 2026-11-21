# Independent decision review: can higher height shorten the theta-lift chain?

Run: DP_MULT_20261121. Reviewer: `/root/formal_bound`. Model: GPT-6 Astra Pro (inherited). Effort: not exposed. Date: 2026-11-21, Europe/Berlin. This is a second mathematical/source review, not a Lean certificate.

## Current conclusion after primary-source recovery

The literal replacement that raises one-dimensional formal height while retaining the existing normalized logarithm/minor interface is **REFUTED** (GTR-11). The concrete attempt to restore the old alternating rank-one blocks by adjoining the Cartier dual and taking products or unramified restrictions of scalars also fails (GTR-10). The actual period-to-jet comparison has been recovered and independently checked in its stated form (GTR-6 and GTR-6/PATH); it is no longer an unidentified functional.

GTR-7 and GTR-8 give additional precise limits on pure numerical replacement. The unrestricted existence of a different theta construction with fewer lifts is not decided here, but is a separate extension question, not a remaining gate for the negative conclusion about the literal recipe. The initial broader-scope review below is preserved so that a refutation of the literal recipe is not silently promoted to a theorem that every possible shorter construction is impossible.

## GTR-1. Decision and logical scope

**The existential proposal that an appropriately constructed higher-height CM auxiliary object could yield the multiplicity of step 8 with fewer theta lifts remains OPEN. It has not been refuted.** The unconditional local formal-jet gain is proved. Several naive implications from that gain are false, but their counterexamples do not preclude a carefully normalized global construction.

Three statements must be kept separate:

1. A one-dimensional integral formal factor of height h gives the derivative divisibilities proved in FBA-1, FBA-8, FBA-9 and SHA-3. **Proved.**
2. Those derivative divisibilities, by themselves, force higher generic-fibre zero multiplicity of the local function. **Refuted** by GTR-2 below.
3. There exists a replacement for the particular global auxiliary/theta-lift construction in Alpöge's argument, with a verified comparison of its period/cancellation functional to those formal jets, which achieves the required global estimate using fewer lifts. **Undecided.** No counterexample to this existential claim is obtained from (2).

Alpöge's supplied *Remark*, p.4, timeline step 8, says that a chain with m lifts wins multiplicity m. This states an achieved gain. It does **not** state that one lift can never produce more than one unit, or that every shorter chain fails. Therefore the note cannot be used as an upper-bound theorem against the proposal.

## GTR-2. What the local counterexamples actually prove

Let F be any one-dimensional formal group in the hypotheses, and let f=1+T. The section f is a unit of R[[T]], so its divisor has no zero at the identity, even though it satisfies every universal derivative bound of the height-h theorem. This proves that the universal derivative bounds do not imply positive geometric vanishing order. It does not concern the unspecified automorphic cancellation functional of step 8.

Multiplying any nonzero local section by p^N adds N to every finite p-adic derivative valuation, while it leaves all generic-fibre zero orders unchanged. This again refutes only an unnormalized identification of valuations with zero multiplicity. The formal-height theorem uses a fixed integral lattice and a primitive invariant tangent vector. A scalar pD is no longer a primitive generator; its apparently improved slope has changed the normalization.

For an elementary global normalization check over Q, multiplication by p^N contributes -N log p to the logarithm of the p-adic operator norm and +N log p to the logarithm of the real operator norm. These cancel. Thus scalar multiplication cannot create an improvement in a correctly normalized adelic estimate merely by concentrating on its p-adic term. This is a direct calculation, not an invocation of an unspecified version of Bost's inequality.

## GTR-3. Routes tried and their actual stopping points

### Route A: substitute the improved derivative slope into the slope inequality

A filtered evaluation argument can use the local divisibility of jet-evaluation maps. In fixed lattices, replacing a proven lower bound for a finite-place valuation by a stronger one improves any inequality monotonically in that term. This is the genuine prospective entry point of the result.

The supplied note does not give the evaluation map used in step 13, its ranks, the global filtered spaces, or the formula by which step 10's divisibility enters that map. Hence there is presently no well-typed numerical substitution: the index a of a formal derivative has not been identified with the chain length m or with an index of the automorphic period/cancellation filtration. Nor are archimedean norms, levels, and covolumes held fixed when the CM object changes.

**Stopping point:** identify the exact integral functional or evaluation map at step 10/13 and prove its relation to invariant jets. After that, one can calculate whether the local gain exceeds the changed costs. Merely naming the Bost slope inequality does not provide this relation.

### Route B: increase CM dimension and use a one-dimensional height-h factor

The local gain is real. But a polarized CM p-divisible decomposition constrains its complementary data. Under the hypotheses stated in SHA-5, a factor with dimension 1 and height h>2 cannot be self-conjugate: its conjugate factor has dimension h-1 and height h. Thus the corresponding pair uses total abelian dimension h. The short counting proof is d_v+d_barv=h_v, so d_v=1 implies d_barv=h-1; if v=barv it instead gives h=2.

This proves that the higher-height replacement changes geometric data relevant to theta kernels, ranks, polarizations and norms. It does not prove that those changes always outweigh the gain. No universal inequality of that kind is in the supplied material, and the dimension count is not a nonexistence theorem for higher-height CM factors.

**Stopping point:** construct the intended polarized CM object and corresponding global theta/period data, then compare their actual costs. There is no valid deduction of impossibility from the complementary dimension alone.

### Route C: substitute total p-divisible height for directional height

This route is conclusively false. For F=(G_m-hat)^r, total height and dimension are both r. With D=(1+T_1)partial/partial T_1 and f=1+T_1, one has D^a f(0)=1 for every a. Thus using h=r in a one-dimensional positive-slope formula fails.

**Corrected route:** use an actual integral homomorphism from a one-dimensional height-h formal group into the formal completion of the abelian scheme (SHA-3), or an integral direct product of such factors. A special-fibre factor or rational isogeny factor alone does not supply the integral tangent/lattice comparison. Once the corrected data exist, the local theorem applies, but it still does not identify the step-8 functional.

### Route D: extract a numerical lift saving from c_h/c_2

The exact local ratio is

c_h/c_2=(p+1)(p^{h-1}-1)/(p^h-1)<1+1/p.

Thus the asymptotic local slope improvement over height 2 is bounded, not arbitrarily large. Under an additional model in which every lift contributes the same number of jet orders, all other costs remain unchanged, and the required global quantity is linear in the sum of these slopes, this ratio would bound the possible proportional saving. None of those modeling assumptions has been verified for the note's construction.

Even a bounded positive improvement can conceivably remove some lifts; the ratio therefore does not refute the proposal. Conversely it does not establish any saving, because a local slope is not a proved gain per global lift.

**Stopping point:** a quantitative comparison assigning a local jet filtration increment and a global cost to each higher-height lift.

### Route E: rescale derivatives or multiply local frames by units

A unit scalar multiplying a normalized invariant derivation does not change its valuation slope; a nonunit scalar changes the tangent lattice. Multiplying by an invertible formal function preserves the local zero divisor but can change individual derivatives. Both observations prevent an intrinsic global multiplicity from being read off an arbitrarily normalized derivative valuation.

**Outcome:** these operations provide no valid construction of fewer lifts. They also do not obstruct a construction using a fixed primitive tangent vector, an integral theta trivialization and a proved period comparison.

### Route F: use the Lefschetz/Arthur-SL2 proposal as the missing comparison

The supplied `FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md`, suggestion 6, explicitly labels the identification of the step-8 gain with a Lefschetz primitive-string length and an index of an integral Lefschetz order as **proposed**. Its checking instruction is to compare step 10 with a diagonal-form calculation. Neither that comparison nor a link from a height-h invariant jet ideal to the Arthur block is stated or proved in the supplied files.

**Stopping point:** the same missing comparison, now expressed through an additional proposed intermediate object. An analogy between two SL2 actions is not a way around the gap.

## GTR-4. Exact source audit for a bridge theorem

I inspected the supplied `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, the explicit theorem statements in `ALPOGE_LEAN_MAP_20261120.md` §3 (levels 0–4), §4 rows 1,2,8,9,10,12,13,14,15,18, and all occurrences in the map of `jet`, `multiplicity`, `derivation`, `Hasse`, `formal group`, and `height defect`.

**No theorem relating invariant jet ideals to theta-lift orders is stated in those supplied texts.** This is a statement about the supplied extracts, not a statement that such a theorem is absent from the complete Lean archive. The complete archive is not attached here.

The explicit top-level bridge in the map is a theorem with separate hypotheses for theta integrals, local matching, a covolume bound, local Langlands data and an analytic window condition: `every_character_of_theta_integrals_local_matching`, quoted in the map §3, level 4 from `ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69`. Its displayed statement contains no formal-height or invariant-jet parameter. That theorem cannot presently be specialized using the new local bound alone.

The map §4 row 2 calls the match for the CM/invariant-derivation step low confidence; row 8 gives candidate theta-lift paths; row 10 gives divisibility folders; row 13 gives slope-inequality paths; row 14 is a low-confidence cost match. These are retrieval targets, not the missing comparison theorem.

## GTR-5. Initial gate (partially closed by the recovery in GTR-6)

At the end of the supplied-extract review, the first gate was:

> Recover the exact definition and integral normalization of the step-10 divisibility/step-8 multiplicity functional for one lift, and prove that its relevant filtered piece is an invariant-jet evaluation along a one-dimensional formal factor, with an explicit conversion between derivative order and gained multiplicity.

Only after that gate is passed does a numerical question remain:

> For the explicit higher-height CM replacement, prove that its additional valuation exceeds every change in archimedean norm, level, rank, polarization and covolume cost, sufficiently to meet the original target with a shorter integer chain length.

The first actionable source step at that time was to read the actual declarations behind the map's step-10 divisibility folders and the `HypsAlt`/`DefiniteSideCondition` input in §3, level 4, rather than extrapolate from folder names. If the intended claim is to be a different construction, it needs those same data stated from scratch.

No attempted route above proves that this construction exists, and none proves that every such construction is impossible. The final package should therefore leave this existential row OPEN, while marking the local theorem and the precisely stated negative implications proved/refuted as appropriate.

## Genuine check events

- GTR-1: targeted logical-scope check, 2026-11-21, `/root/formal_bound`, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121. Checked that the counterexamples refute universal local-to-zero-order implications only; checked that the note's achieved m-step gain is not an upper-bound theorem. Passed.
- GTR-2: independent re-proof, same date/metadata. Checked f=1+T is a unit, multiplication by p^N leaves the generic-fibre divisor unchanged, D scaling contributes aN, and the two normalized Q-absolute-value logarithms cancel. Passed.
- GTR-3/C: independent re-proof, same date/metadata. Recomputed D^a(1+T_1)=1+T_1 on a product of formal multiplicative groups. Passed.
- GTR-3/B: targeted proof check, same date/metadata. Rechecked the short deduction from the CM height/dimension identities in SHA-5. The underlying CM decomposition theorem is carried from SHA-5 and its source verification; it was not independently re-proved here.
- GTR-3/D: independent re-proof, same date/metadata. Recomputed c_h/c_2 and its limiting upper bound; checked that no per-lift normalization is present in that arithmetic calculation. Passed.
- GTR-4: used and rechecked in this run, same date/metadata. Read the two supplied Lean files and quoted map statements and ran the targeted searches described above. No bridge theorem found in the supplied extracts. No claim about unseen complete-archive files.
- GTR-5: targeted whole-memo check, same date/metadata. Reread the memo against SHA-3 through SHA-6 and the supplied note/map; kept existential shortening undecided and separated it from the proved counterexamples. Passed. No formal verification claimed.


## GTR-6. Primary-source recovery and the actual period/jet interface

**Update:** the exact finite-place functional, a normalized period/path-to-jet interface, and the global gain/cost formulas have now been recovered. It is no longer accurate to say that only folder names or the short note are available. This closes the source-identification part of GTR-3/A and GTR-5, while leaving a specific mathematical generalization unproved.

### Recovery actions and provenance

The original public note is `https://alpo.ge/remark.pdf`. HEAD returned HTTP 200, content type PDF and length 245114 bytes. HEAD requests to `https://alpo.ge/lean.tar.gz.part01` and `part14` returned HTTP 200. A bounded GET requesting bytes 0–4095 of part01 received HTTP 200 rather than 206: the server ignored Range and reported Content-Length 18000000. Only 4096 bytes were read and the response was closed; the bytes begin with the gzip magic. At this initial recovery stage, this agent downloaded no complete archive part or multi-gigabyte unpacked archive. The later targeted author-archive verification by the root is recorded below.

A public reading guide was used strictly to locate primary declarations. The GitHub mirror is `https://github.com/CocoSgt/riemann-hypothesis-lean`, pinned for this review to tree/commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. The exact URL rule for every source path P below is:

`https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/P`

Unicode path components are percent-encoded when making HTTP requests. Search-service opening of GitHub/raw URLs returned DisabledError, but direct urllib GET of the public raw files succeeded. Small GitHub directory/tree metadata responses were used to select the next files. No unavailable complete-archive search is claimed. At first, archive identity was only asserted by the mirror README/verification files. Subsequently the root downloaded all 14 author-hosted parts (239275554 compressed bytes), streamed 175190 tar entries without unpacking the archive, and verified all 45 targeted Lean modules then present byte-for-byte against the author archive, with no mismatches and no unmatched targets. The observed verification record is `research/author_source_verification.json`. This establishes author provenance for those targeted files; it is not a claim that every file in the public mirror was compared. The subsequently recovered `GaussJetBounds/Statement.lean` was absent from that first manifest and awaits the root's additional targeted pass. A targeted check did verify byte equality between recovered `Main.lean` and the supplied `ALPOGE_Main.lean`: both are 433 bytes and SHA-256 `017645ca448f2fd1f6fd5c4c2cb2c6e96e472725be13f6e180ca6e1574360939`.

The downloaded code is the mathematical author-source text as distributed by that public mirror; the mirror host is not being treated as a new mathematical authority. This was source reading, not Lean compilation, execution, or an independent audit of RH. The accepted RH premise is untouched.

### Exact interfaces recovered

All line numbers below refer to the pinned file bytes. A `def ... : Prop` defines a required assertion; it does not, merely by existing, prove that assertion.

1. **The finite-place period functional.** `Formalism/SharpRestriction/Divisibility/LocalQuadraticParts.lean:206–221`: `adm2` requires the complex period `perCol` evaluated on specified integral lattices to equal the embedding of an algebraic scalar y, with y=0 or
   
   `floor(ur D w (L.sg u w)) <= vAdd (D.plEq w) y`.
   
   `UnroundedValuationBound` is the corresponding bound before flooring, and the actual theorem `valuation_bound_of_unrounded` at line 218 proves it implies `adm2`. Thus this is a valuation of a specified normalized algebraic period; it is not the vanishing order of an arbitrary local function.

2. **Integral paths and jet entries.** `Formalism/LocalToGlobal/Divisibility/JetBounds/IsExpansion.lean:133–181` defines `PathData`, its finite sum `val`, and `IsExpansion`. Each path is a product of a column coefficient, local jet entries, integral unit/last factors, and specified integer denominators. `ColsInt`, `RowsInt`, `LastInt`, `UnitsInt` and `StabDvd` fix the integral data and denominator D. `Statement.lean:52–71` defines `LocalValuationBoundAt` and `PlaceInputAtEntry`; its resulting lower valuation is
   
   `ramw(w) * sum_j (s_j - v_p(D))`.
   
   The actual theorem `valuation_of_entry_bounds`, in `JetBounds/JetBoundsProofs/ValuationOfEntryBounds.lean:13–31`, proves this conclusion from the expansion, integrality and entry norm bounds. Its proof applies `path_height_bound`, replaces the path sum by the period using `IsExpansion`, then converts the norm bound into an additive valuation using `embedding_lower_bound`. This is an explicit usable interface, not just a suggestive name.

3. **The local entries are richer than arbitrary one-variable derivatives.** `IsExpansion.lean:83–108`, constructors `IsSys7.caseA` and `.caseB`, require an unramified coefficient field, `BHyp` on a multivariate exponential kernel, and inverse-logarithm substitution identities. Case A requires even orbit length d and `entLog`; case B uses the two-letter logarithm `oneLog` and `BHyp l 2`. `PlaceInputAllEntries.lean:19–48` also allows integral entries and a ramified determinant/exponential case. The direct formal-height theorem does not establish those kernel and period identities.

4. **The actual local coefficients have several roles.** `IsExpansion.lean:55–58` defines `expA` using top terms, `gam`, a linear-programming expression `Fnum`, and a logarithmic loss. Lines 74–75 define `expB = rho * size - logarithmic_loss`. Here `rho=1/(p^2-1)` and `gam=p/(p^2-1)`; the same definitions occur in `ProductZerothFirstParts.lean:23–25`. Only gam equals our c_2. In particular, not every valuation input has the form c_2 times derivative order. Replacing p^2 by p^h everywhere would decrease rho and gam, whereas the formal-derivative coefficient c_h increases with h. A correct generalization must derive the new entry estimates, not replace a numeral uniformly.

5. **An actual theta/kernel comparison exists at height-two-type data.** `JetPolynomialLogs/DworkPowerSeriesWeights.lean:149–175` defines `TieB`, `KernelFromExponentialTwist` and `TieFrame`. `KernelFromExponentialTwist` requires the theta series, after a scalar of norm 1, to equal `thetaZ g U ε be`, with U integral and g inverse to `entLog`. The actual theorem `thmA_of` at line 177 derives the local lower-bound theorem from these comparisons. `UniformBoundAllData.lean:10–28` proves `tieB` using the exponential integrality supplied by `LetterLogIntegrality.integrality_of_letter_log`. In that latter file, the logarithmic monomials at lines 216–242 have exponent `(p^2)^e` and Frobenius shift `-2e`. Increasing orbit length d does not turn these fixed exponents into p^h. This is the most precise recovered place where a proposed height-h replacement would need new mathematical input.

6. **Cartier controlled nonvanishing has a separate role.** `CartierLocalBounds.lean:30` defines `vLe x b` as `p^(-b) <= norm(x)`: this is a valuation upper bound and forces nonvanishing. `ThmP`, `CHAt` and `ContentAt` are such controlled nonvanishing/content assertions. Its `AdmLoc` requires six local packages, including Frobenius-form, leaf and unit-minor information. In the direct consumer `FamilyThetaDenominatorValues.lean:648–659`, `OrbitContentCond` consists of Cartier `Conclusion5`, and `DepthFromContent` uses it to bound the denominator/depth error before the `OntoIndices` conclusion. This is not supplied by a theorem that merely makes every invariant derivative more divisible. The exact path from all these packages to a complete global instantiation has not been recompiled or independently audited here; the present claim is the displayed interface/dependency, not such an audit.

7. **The gain is a prime-power ramp with weights.** `Formalism/LocalRingCardinality/DataParams₂.lean:178–180` requires `wPart >= 1`; lines 203–223 define `sz`, `gainD`, `sg` and `Ga`; lines 240–242 define `vonMangoldtClassSum` by summing only odd i:
   
   `max(0, aT/p^i - wPart(j,t,p,i))`.
   
   `GlobalTheoremInputs.lean:122–140`, `LinkG_at`, uses a sum of these ramps, minus explicit losses and lattice costs, as a **lower** bound for the aggregate gain. It is not an equality or an upper bound for every possible gain.

8. **The global archimedean and lattice costs are explicit.** `GlobalTheoremInputs.lean:77–90`, `LinkDIV_at`, includes covolume/slope/norm bounds and compares them to `MAIN` plus error budgets. `DataParams₂.lean:231–234` makes `MAIN` linear in m. `GrowthBoundGivesRiemannHypothesis.lean:109–125` gives `SizeWindows`, an explicit error allowance, and the denominator used in the final normalized estimate. The local height does not occur as a free parameter in these recovered declarations.

### Current interpretation of the recovered comparison

There is now a precise period-to-jet comparison to target. Its inputs include normalized theta kernels, multivariate determinant jets, p-adic exponential integrality, controlled denominators and, separately, controlled nonvanishing. What remains missing is a **height-h analogue of those specific inputs and its global cost**, not the mere existence of a source file using jets.

## GTR-7. Prime-power ramp comparison: a proved limit on pure coefficient replacement

This lemma was suggested by the root's convergent coefficient-increment observation and independently proved here in the exact ramp form appearing in the recovered code.

For A>=0, p>=2, h>=2, and weights w_i>=0, put

R_h(A,p;w) = sum over i>=1 with h not dividing i of max(0,A/p^i-w_i).

The sums converge by comparison with the geometric series. For the code's stronger condition w_i>=1, all terms with p^i>A vanish, so its finite cutoff `log_p(toNat A)+2` agrees with this infinite sum when A is its nonnegative integer aT. The code's original odd-i ramp is exactly R_2.

**Claim.** Uniformly in h and the weights,

|R_h(A,p;w)-R_2(A,p;w)| <= A/(p^2-1).

**Proof.** Write b_i=max(0,A/p^i-w_i), so 0<=b_i<=A/p^i. The added indices are even i not divisible by h, and the removed indices are odd i divisible by h. Therefore

R_h-R_2 = sum_(i even,h∤i) b_i - sum_(i odd,h|i) b_i.

The positive sum is at most A*sum_(i even,i>=2)p^(-i)=A/(p^2-1). If h is even, the negative sum is empty. If h is odd, h>=3, and that sum is at most A*p^h/(p^(2h)-1), which is at most A/(p^2-1): after clearing positive denominators the inequality is p^h(p^2-1)<=p^(2h)-1, immediate for h>=2. The difference of two nonnegative quantities each bounded by the same constant has absolute value at most that constant. This proves the claim. The same bound permits varying h with p, the lift index or t.

Let C=sum over primes p of log(p)/(p^2-1). This is finite, since the terms are at most a fixed multiple of log(p)/p^2 and the sum over all integers converges by the integral test. Thus, for arbitrary prime subsets and cutoffs,

|sum_p log(p) [R_h(A,p;w)-R_2(A,p;w)]| <= C A.

The source's valuation-to-degree normalization uses `sz=2*lwP*ramIdx*y`. With its place-summing identity `FactEtaMean` (`DataParams₂.lean:265–267`), the corresponding change in the **ramp certificate**, holding other inputs fixed, is at most

2 C * sum_(j in lifts) sum_t A_t.

Restricting to `TTw`, dropping primes or imposing the same prime cutoffs only improves this uniform upper bound. This conclusion compares the proposed numerical certificate. Because `LinkG_at` gives only a lower bound on actual gain, it is not an upper bound on what some new geometric construction could really achieve.

For the zero-weight infinite sums, R_h=A*c_h, and

0 <= c_h-c_2 = 1/(p^2-1)-1/(p^h-1) <= 1/(p^2-1).

Consequently the pure replacement cannot change the coefficient of a leading A*log(X) prime sum whenever the baseline prime set has such a main term. It changes only O(A). This statement does not require proving a prime-distribution theorem here: the rigorous conclusion is the uniform O(A) difference; preservation of any supplied divergent logarithmic coefficient follows algebraically.

**Precise scope of the resulting obstruction.** For a family in which each lift has the same nonzero leading coefficient A*log(X), replacing height two by h while keeping the certificate weights/costs fixed cannot compensate a fixed positive proportional reduction in the number of lifts as X tends to infinity. It does not exclude deleting one lift when m itself grows faster than log(X), since O(mA) may then exceed A*log(X). Nor does it rule out a benefit after leading terms cancel against archimedean/period terms. Those lower-order effects are exactly where a normalized global construction must be analysed. No absolute 'fewer lifts impossible' theorem is claimed.

## GTR-8. The fixed global error allowance and the square-root balance

Here is a separate elementary obstruction to obtaining a polynomially shorter chain merely by improving the coefficient in an otherwise unchanged error estimate.

Abstract the actual allowance in `GrowthBoundGivesRiemannHypothesis.lean:115–116` as

B = nT*A*(1+m^2/k) + m*(2*n*m*b*x^eps + nT2*k*b*x^eps/(n*(n*x^(-eps)))),

and its normalizing coefficient at lines 104 and 121 as

S = nT*m*b*((nT2/n)/2).

Assume x>=1, eps>=0, b,m,n,nT,nT2,k>0, A>=x*b, nT<=n and nT2<=n. The cardinality conditions hold when nT and nT2 are cardinalities of subsets of the finite ambient H, as in `GrowthInequalityDataExists`; the scale `Scale.a` in `DataParams₂.lean:31` is x*b, and `ErrorFormsWeakWindowsFalse.lean:27–30` explicitly requires x*b<=a. This is a statement under those actual lower-scale conditions, not under only the weaker generic `SizeWindows` definition, which by itself allows A=0.

Put d1=nT/n, d2=nT2/n. Direct division gives

B/S = [2A/(m*b*d2)]*(1+m^2/k) + 4m*x^eps/(d1*d2) + 2k*x^(2eps)/(d1*n^2)
     >= 2x/m + 4m.

Every discarded term is nonnegative. Hence for m<=x^(1/2-delta), delta>0, the **displayed allowance divided by its signal coefficient** is at least 2*x^(1/2+delta). Dividing by any fixed positive bounded improvement factor cannot change that exponent. The same allowance therefore cannot certify an x^(1/2+eta) target with eta<delta for all large x by a pure bounded-coefficient substitution. The two terms also exhibit the square-root balance directly.

This is a limitation of that fixed **upper-bound budget**. A lower bound on the budget is not a lower bound on the actual error. A new construction or sharper error estimate can in principle have smaller actual error. The argument does not prove that the chain itself cannot be shortened, and it does not resolve a finite or lower-order saving.

## GTR-9. Updated decision and smallest remaining gate

The source-recovery route succeeded. The next task is a mathematical construction/generalization, not another blind archive search:

1. Specify a polarized CM object with the intended integral one-dimensional height-h direction, including the conjugate dimension and the actual Frobenius/Hodge signature. Changing the even orbit length in the existing alternating model is not the same operation.
2. Prove a height-h replacement for the normalized `KernelFromExponentialTwist` / `IsSys7` / `PlaceInputAtEntry` data, including the multivariate exponential, integral theta frame and path denominator controls. The invariant one-dimensional theorem alone is only one prospective ingredient.
3. Supply the controlled nonvanishing/content estimates needed by `DepthFromContent`, or an alternative denominator argument. Stronger lower divisibility does not imply these upper valuation estimates.
4. Recompute `LinkG_at`, `LinkDIV_at`, the period main term and the explicit error allowance with the changed dimension, rank, polarization, levels and lattices. Only this produces a justified comparison of the admissible integer m.

**Final status:** the theorem 'the one-dimensional local derivative slope improves with h' is proved. The drop-in claim that a higher total or orbital height alone supplies the existing theta inputs is false or ill-typed in the precise ways recorded above. Pure coefficient replacement has the rigorous limitations GTR-7 and GTR-8. The existential claim that some properly constructed higher-height auxiliary system achieves the step-8 target with fewer theta lifts remains OPEN; neither the successful source recovery nor the numerical obstructions justify changing it to REFUTED.

## Additional genuine check events

- GTR-6, source-recovery and typed-interface check, completed check recorded 2026-11-21 00:21:48 UTC (01:21:48 Europe/Berlin), `/root/formal_bound`, GPT-6 Astra Pro inherited, effort not exposed, run DP_MULT_20261121. Inspected the HTTP metadata/range response, public raw primary module text, definitions and the proof of `valuation_of_entry_bounds`; checked SHA-256 of the two Main.lean copies. No Lean compilation or whole-mirror identity verification claimed. The later targeted author comparison is separately recorded above. Recovery succeeded; the limited failed search-service opens do not imply mathematical absence.
- GTR-7, independent re-proof and targeted whole-proof challenge, 2026-11-21, same agent/model/effort/run. Root suggested summability of c_h-c_2. Independently proved the exact positive-ramp difference bound, checked both parity cases of h, source wPart>=1, the finite cutoff, place-weight factor 2, and the distinction between a lower-bound certificate and an upper bound on actual gain. Checked the failure of the tempting 'not even one fewer lift' inference when m grows. Passed.
- GTR-8, independent re-proof and targeted whole-proof check, 2026-11-21, same metadata. Divided each of the three budget terms by S, checked positivity assumptions and the extra A>=xb hypothesis absent from bare SizeWindows, and distinguished the allowance from actual error. Passed. No numerical testing or formal certificate claimed.
- GTR-9, updated logical-scope check, 2026-11-21, same metadata. Reconciled successful bridge recovery with the earlier supplied-extract gate, distinguished lower divisibility from controlled nonvanishing, and retained the existential question OPEN. Passed.

## Pinned source hashes for the main new findings

Full retrieval metadata is in `research/external_lean/targeted_metadata*.json`; `research/global_transfer_source_manifest.tsv` records all currently retrieved Lean-file hashes and whether they appear in the first author-verification manifest. Inclusion in that complete file inventory does not itself assert that a file was read or proved. The paths in this table are relative to the pinned raw `/src/` base above; each line range is given in the discussion, not inferred from file names.

| Source path | SHA-256 |
|---|---|
| Formalism/SharpRestriction/Divisibility/LocalQuadraticParts.lean | 7b0dcf3680ea9942d350110db269931f859b2276885b417445ecf5629be1dc5c |
| Formalism/LocalRingCardinality/DataParams₂.lean | 39d84d7e7db5196715f955ac44f45e61a23fcf4ebd5065ca41444f836efd3099 |
| Formalism/SharpRestriction/GlobalTheoremInputs.lean | 4d51ccc0586441a159ad6d09ebc0a46b3c462e3c5b296d5a5bd7613266e17bfb |
| Formalism/SharpRestriction/Divisibility/CartierLocalBounds.lean | 0f0120efa881ef873bd42e489a9ff3df0c61773aa5d697cafd2b225990177475 |
| Formalism/SharpRestriction/Divisibility/FamilyThetaDenominatorValues.lean | de1fc5cc148ccc4212b62685cd36d02af0dbcd219a58f37c99f3621678521c46 |
| Formalism/SharpRestriction/Divisibility/ProductZerothFirstParts.lean | a4497cc9cb1cde587594b937544de8a91e90838506d36415cee06355e627226d |
| Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/DworkPowerSeriesWeights.lean | 1dbc04215e158dffce88c8dd642dbaef6270edd882c98c24dc4f1ea765a0fb33 |
| Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/LetterLogIntegrality.lean | c25442236b2c7925960b76463e4acfd433dec7d3c841ad0a65804dec565df75d |
| Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/UniformBoundAllData.lean | cb50a9446e59d285e03cf68f1f837dbf684c68b685ee37f39d1f230c0e1e2619 |
| Formalism/LocalToGlobal/Divisibility/JetBounds/IsExpansion.lean | 9f7abd94b7a01b490590600456e08e600a29d353a3c4385eab19af98d9aea90c |
| Formalism/LocalToGlobal/Divisibility/JetBounds/Statement.lean | 5f3d2af856b15b456542bbc02873eae1999e7fe4139fc448b35881362779779f |
| Formalism/LocalToGlobal/Divisibility/JetBounds/PlaceInputAllEntries.lean | 292cf2fff3f2c2dc2ad1eaf07df59b2786d194fe570374ba96a7c6b1807c87c9 |
| Formalism/LocalToGlobal/Divisibility/JetBounds/JetBoundsProofs/ValuationOfEntryBounds.lean | 654a9b066b52043e7a1731681c06361279759e3788dfe6c9a4606c566c984b72 |
| Formalism/SizeWindowBrackets/GrowthBoundGivesRiemannHypothesis.lean | 8143a96da8be39cf426ef142bccbff94bac7706e5bd8e97719a8feebf3272309 |
| Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean | 8b8613a5e3934127fb8b52ba402e658414662f63bff8f0e9fb52bedddd1173f2 |


## GTR-10. A concrete alternative tried: a Lubin–Tate line paired with its Cartier dual

### Construction being tested

Let K/Q_p be unramified of degree h>2, and let G be a Lubin–Tate p-divisible formal group for K, viewed over a common unramified splitting base. It has height h and dimension 1. Put

H = G x G^D,

where D denotes Cartier duality. Then H has height 2h and dimension h, and the canonical evaluation pairing gives it a perfect alternating self-duality, represented by the exchange matrix with signs. Granting whatever global algebraization/polarization is needed can only strengthen this attempted route; the obstruction below is already local. The hope is to use the one-dimensional factor for the improved derivative slope while its dual restores the balanced total dimension, then feed H (or a restriction of scalars of H) into the unchanged alternating CM theta blocks.

### Proposition: this product/restriction route does not preserve the alternating rank-one blocks

The explicit H above, any positive direct power of it, and any finite unramified restriction of scalars of such a power cannot be isogenous to a product of the unchanged rank-one alternating CM blocks. Thus balanced total height and dimension do not make this proposed replacement compatible with those blocks.

**Proof by CM type.** The two primitive CM idempotents give separate Frobenius-stable factors. On their length-h embedding orbits, the Hodge-type counts are respectively 1 and h-1. An alternating rank-one orbit of even length h has count h/2. If h is odd, the even-orbit requirement already fails; if h is even and greater than 2, neither count is h/2. A CM-linear relabelling can permute primitive idempotents but cannot merge their two Frobenius orbits into one orbit of length 2h. Direct products repeat these incompatible blocks.

**Invariant proof, also covering restriction of scalars and a change of CM labelling.** The Newton slopes of G and G^D are respectively 1/h and (h-1)/h. A rank-one alternating CM orbit has slope 1/2. The local CM formula used here is Tate, Bourbaki exposé 352, §5, definition and dimension/height counts on p.106, formula (10*) and Theorem 3 on p.107: the slope equals the number of selected embeddings divided by the size of the local orbit. These pages were independently visually reread for this check. In a cyclic rank-one Dieudonné description the same calculation says that one Frobenius circuit has valuation equal to the selected count, and division by the circuit length gives the displayed slope.

Products take the union of slope multisets. For a finite unramified restriction of scalars, base change to an algebraic closure splits the Weil restriction into a product of conjugates; conjugation and base extension preserve the normalized slopes. Hence restriction of scalars repeats the slopes 1/h and (h-1)/h. For h>2 neither is 1/2. Newton slopes are invariant under isogeny, so none of these groups can become a product of rank-one alternating blocks, and none acquires a slope-1/2 p-divisible isogeny factor. This completes the obstruction.

This is a substantive failed construction, not merely a restatement that a comparison theorem is missing. It explains why adding the Cartier dual does not repair the local mismatch. It does **not** assert that the entire higher-rank `LocD` is always isoclinic: the source allows larger ranks and defects. Embedding these mixed-slope groups into a new higher-rank construction, changing the relevant blocks, or proving a different minor/period interface would be a different construction with new costs. Such a construction is not excluded by this proposition.

### Source/check record

- Primary source read: https://www.numdam.org/item/SB_1968-1969__11__95_0.pdf ; web reference `turn955799573view0`. Read original rendered pp.106–108 (`tate352-13.png`, `-14.png`, `-15.png`), including formula (10*) and Theorem 3, independently of the sibling's earlier source check.
- GTR-10: independent proof and whole-proof challenge, 2026-11-21, `/root/formal_bound`, GPT-6 Astra Pro inherited, effort not exposed, run DP_MULT_20261121. Checked the height/dimension pairing, the per-orbit type-count obstruction, the impossibility of merging Frobenius-stable primitive CM factors by relabelling, and the slope preservation under direct product and unramified restriction of scalars. Explicitly limited the target to the unchanged rank-one alternating blocks, rather than asserting an unsupported theorem about all higher-rank `LocD`. Passed. No Lean compilation claimed.


## GTR-6/PATH. Independent proof of the recovered path-valuation bridge

The source theorem `valuation_of_entry_bounds` can be understood and checked without treating Lean syntax as a certificate. Let J be the finite lift index set, with a distinguished j1 in J. Suppose the normalized period is a finite sum of terms

x_pi * [product_(j in J) gamma_(pi,j)^(-1) * epsilon_(pi,j) * e_(pi,j)] * r_pi * gamma_(pi,P)^(-1) * y_pi.

Assume all x_pi, y_pi, epsilon_(pi,j) and r_pi are integral; v_p(e_(pi,j))>=s_j; every integer gamma_(pi,j) and gamma_(pi,P) divides a fixed nonzero integer D; and gamma_(pi,j1)=1. Divisibility into nonzero D ensures that the denominators are nonzero. There are at most |J|-1 nontrivial lift denominators plus the final denominator, hence at most |J| contributions bounded by v_p(D). Each term has valuation at least

sum_j s_j - |J|*v_p(D) = sum_j (s_j-v_p(D)).

The nonarchimedean triangle inequality gives the same bound for their finite sum. Under the normalized embedding `EmbAt`, additive number-field valuation equals ramification index times this normalized p-adic valuation, giving exactly `LocalValuationBoundAt`, including its zero alternative. This accounts for the distinguished denominator condition rather than silently losing an extra v_p(D).

GTR-6/PATH check: independent re-proof and whole-proof check, 2026-11-21, `/root/formal_bound`, GPT-6 Astra Pro inherited, effort not exposed, run DP_MULT_20261121. Checked the number of denominators, their nonzero status, all integral coefficients, finite-sum inequality and ramification factor against `IsExpansion.lean:161–175` and `ValuationOfEntryBounds.lean:13–31`. Passed; no Lean compilation claimed.

## GTR-11. Literal unchanged-logarithm substitution is impossible for h>2

The exact source has now been recovered: `Formalism/GaussJetBounds/Statement.lean:175–177` defines

oneLog(T) = sum_(e>=0) T^(p^(2e))/p^e.

The coefficient at T^(p^2) is **+1/p**. This agent independently read the definition in the pinned bytes; SHA-256 is `5db560c0efb876e30b084b6480501338be2250b1e694cb2cb8e881aa678a137b`. The companion `letterLog` at lines 74–76 has the same coefficients with orbit shift -2e; `entLog` is at lines 120–123. The normalized inverse requirement for the one-letter input is `IsSys7.caseB.hg` in `JetBounds/IsExpansion.lean:102`.

**Proposition.** Let F/W(k) be a one-dimensional integral commutative formal group of finite height h>2. Its normalized logarithm cannot equal this `oneLog` after an invertible integral change of coordinate and a unit rescaling of the logarithm. Equivalently, its exponential cannot satisfy the unchanged one-dimensional `oneLog` inverse requirement in that integral normalization.

**Proof.** Put q=p^h and write [p]_F(T)=pT+sum_(n>=2)g_n T^n and L_F(T)=T+sum_(n>=2)l_n T^n. Height h gives g_n in pW(k) for every n<q. From L_F([p]_F(T))=pL_F(T), the degree-n coefficient identity is

(p-p^n)l_n = g_n + sum_(2<=j<n)l_j*[T^n]([p]_F(T)^j).

For n<q, inductively all l_j with j<n are integral. Every coefficient of [p]_F through degree n is p-divisible, so the displayed right side is p-divisible. The factor p-p^n is p times a unit, hence l_n is integral. In particular l_(p^2) is integral, because p^2<p^h.

An integral coordinate u(T) with u(0)=0 and u'(0) a unit preserves integrality of the logarithm coefficients through degree p^2 under composition; a unit rescaling preserves it as well. But `oneLog` has coefficient 1/p at that degree. Equality is impossible. The equivalent inverse statement follows by formal inversion, or by observing that the inverse of `oneLog` begins T-(1/p)T^(p^2)+higher terms, while the inverse of an integral truncation is integral to the same order. This proves the claim.

In particular, if a proposed defect-free rank-one transplantation identifies the source coefficient `alC[2]` with the degree-p^2 coefficient of this scalar logarithm, the source requirement that p*alC[2] have a unit 1-by-1 minor is impossible: p*l_(p^2) is p-divisible. This last assertion retains the stated scalar identification; it does not identify every coefficient of an arbitrary higher-rank source chart with a one-variable group logarithm.

**Decision consequence.** The literal recipe 'raise the one-dimensional height and retain the present normalized logarithmic/minor/theta interface' is refuted. There is no reason to keep that recipe open merely because arbitrary alternative theta kernels have not been excluded. The broader existential question in GTR-1 concerns a different construction with different interface and cost estimates; it is not an unresolved step in the proof of this negative conclusion.

GTR-11 check: independent coefficient-induction proof and whole-proof challenge, 2026-11-21, `/root/formal_bound`, GPT-6 Astra Pro inherited, effort not exposed, run DP_MULT_20261121. The sibling independently identified the same obstruction; this agent independently read the exact positive coefficient, checked the p-divisibility induction, integral coordinate/unit normalization and formal inversion, and limited the conclusion to the literal unchanged-logarithm identification. Source reading was observed at 00:26:34 UTC. Passed. No compilation claimed.
