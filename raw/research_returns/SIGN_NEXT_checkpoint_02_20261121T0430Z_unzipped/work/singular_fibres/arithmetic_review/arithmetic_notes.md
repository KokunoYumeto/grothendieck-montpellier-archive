# Arithmetic specialization follow-up: source and scope record

Author: `/root/singular_fibres`, GPT-6 Astra Pro; reasoning effort not exposed.
Run: SIGN_NEXT. Date: 2026-11-21. This is a human mathematical/source review,
not a Lean compilation or a formal-kernel audit.

## Current proved results

1. **SF-Q6-01** (`no_global_numBig.tex`): neither `numBig` nor `numEx`
   can be the `ofRecord` specialization of an actual global `D7` having
   its declared rank and host. The actual `Host.qd_big` requires
   `541 < q,d`, whereas these numerical records use `q=11,d=7`.
   The numerical inequalities remain valid on their numerical domain.
2. **SF-Q6-02** (`actual_m2_jets_scope.tex`): the archive has a genuine
   inhabited two-step theta-jet coefficient construction, with rationality
   in the homogeneous degrees used by the kernels. Its selected witness
   has `u_last=-1/2`, `k=8`, and nonempty `host.TT`; these force `bT=-3`
   in `SizeData₂`, contrary to `bT≥b'>0`. Thus the selected coefficient
   construction does not give a full `DivInputs` instance.
3. **SF-Q6-03** (`asymptotic_rank_scope.tex`): the fixed ranks
   `(k,m,t,r,f)=(8,2,15,9,8)` cannot satisfy `RankVal` at any scale:
   its last equality would read `24=580+TOv*nWv`. More generally,
   `RankVal` and `m=2` imply `x<81`. This excludes the specific
   rank-growth constructor route, not all direct `SizeData₂` choices.
4. **SF-Q6-04** (`true_stabilizer_and_full_local_bound.tex`): the actual
   column denominator is an lcm of genuine finite lattice-automorphism
   orders, whose prime divisors are at most `2*f*N_m+1=641`. At a
   residue-class-zero inert prime with `hP=0`, the fully tied source
   expression for the large constant weights below is
   `(96*M+3456)/(p^2-1) - 76800*log_p(a)`. Its specialization at
   `p=863, x=10^1000, eps=1/100, J=1000, M=ceil(exp(10^10))`
   is strictly greater than `22020927106278400000/3879`.
   The formula is conditional on its explicitly listed ties; those
   actual global realizing data have not yet all been assembled.

5. **SF-Q6-07** (`untwisted_model_obstruction.tex`): the generic
   `RowsRestModel.model` completion has `muAt=mu0` everywhere, forcing
   `F=0` through `SizeData₂.untwisted`. At the inert place of SF-Q6-04,
   `FDef` instead forces a strictly positive value. This is a proved
   incompatibility of that particular completion, not only missing data.

The first three proofs were read in full and independently checked by
`/root/critical_lefschetz`; the independent reviewer owns the review
records. Root independently read SF-Q6-04 and verified its full formula
and exact positivity calculation. The author owns the accompanying exact arithmetic script and
certificate. The script checks integers, rational HC interlacing, and
the two concrete contradictions; it does not prove the source bridges.

## Source roots and exact archive identity

All source locators in the TeX notes are relative to `lean/src/` in the
supplied 14-part Lean archive. The original parts are in
`/workspace/scratch/3c0a202771c9/lean_parts/part01` through `part14`.
The archive has 175190 members, of which 175187 have `.lean` suffixes.
The existing selected Formalism cache is
`/workspace/scratch/3c0a202771c9/lean_selected/Formalism/`.
Additional exact source copies are in this directory's `source_cache/`,
with `lean/src/` removed from their paths. Search/extraction manifests
record copied files, source-relative paths, content hashes and searches.

Scripts in the parent work directory:

- `scan_global_specialization.py`: exact numerical-record/global-input
  names, 31 selected files; no theorem-inhabitation inference from a hit.
- `scan_arithmetic_route.py`: regex searches with recorded terms.
  The final implementation uses `re.MULTILINE`. The first two manifests
  (`character_and_nonvanishing`, `global_character_construction`) were
  generated before that addition, so their anchored alternatives must
  not be treated as exhaustive. Their unanchored positive hits remain
  valid source findings.
- `extract_arithmetic_dependencies.py`: read-only exact path extraction.

The global-realization scan selected 386 files. The two dependency
extractions copied 13356 files (71470181 bytes) from the relevant
definition/Iwasawa/decoration directories and 1298 files (7157535 bytes)
from `Proofs/GlobalInterpolation/`. These caches are research support;
the parent agent should curate, rather than indiscriminately package,
the source copies. No source archive member was edited.

## Real coefficient construction and derivative convention

`Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/
ExistsHypJetsAll.lean:73–115`, `JetsInhab.exists_colIn_jets`, proves
`∃ B, X:PreX B, I:ColIn B X, HasLetters B ∧ I.Ok ∧ I.JetsIn`.
The proof uses actual Hecke-character/frame/column constructors and a
finite coefficient-field enlargement. It is not a toy matrix assignment.

The precise finite jet-field bridge is in
`Definitions/AutomorphicMembership/JetsInIffStepField.lean`, especially
`jetNum`, `JetsIn`, `jetsIn_iff`, `JetsIn.isAlgebraic`. The ordinary
iterated derivative convention is fixed by
`Formalism/LocalToGlobal/KernelLattices/ThDistC.lean:56–61`:
`jetC = (product cD^alpha) * derivAt0`. There is **no division by
`alpha!`**. The rationality statement is restricted to each kernel's
prescribed homogeneous multidegree; it is not the all-degree predicate
`Amb.JetsRat`.

`Proofs/IwasawaDecomposition/DegreeEqTotDeg.lean` gives the finite
algebraic-coefficient construction, `exists_replace`, and
`exists_jetsIn`. Replacement preserves the Hecke frame, excluded primes,
and twisting-character range, but resets the chosen ambient normalization
and the relevant index exponents. It does not preserve every initial
normalization datum.

The selected witness has
`v=(24,20,16,12,8,4,0)`,
`u=(49,45,37,29,21,13,5,-1)/2`,
`b=(1,37)`, `e=(19,55)`, and `N=(8,24,40)`.
These equalities refine the construction proof; they are not properties
of every witness of the unrefined existential theorem.

The author read the complete proofs of `ExistsHypJetsAll`,
`ExistsNatBoundPre`, `ExistsHarishChandraWeights`,
`HarishChandraParameterFormula`, `DegreeEqTotDeg`,
`ExistsColInJetsIn`, `ExistsColumnInputAssembled`, and the jet-field
bridge. Some deeper imported analytic/algebraicity theorems have not
all been audited here. `/root/integral_fock` owns IF11 and its further
normalization/algebraicity check.

## Constructor limitations actually established

`Examples₂.H0` in
`Formalism/LocalRingCardinality/SpanPowerMembership/
ExampleLayerExistsGenerators.lean` is a valid full host with
`q=571,d=599`, `TT=∅`, and `splitBound=2`. It is not by itself the
stronger `Pre` datum: its displayed `pde=751`, `pde'=991` do not satisfy
the `Pre.level_cond` requirement `p≡1 mod QS*q*d`, where the modulus
is 5472464. In particular, SF-Q6-02's nonempty-TT hypothesis is not
silently applied to H0.

`Proofs/GlobalInterpolation/ExistsExplicitParameters.lean` and
`Proofs/IwasawaDecomposition/SizeParametersNonempty.lean` use `RankVal`.
Their full source passages were read for SF-Q6-03. The initial explicit
size datum sets gain, F, E, tau and io to zero and `NuLat=⊥`; subsequent
filling and arithmetic constructions are required before it is a full
bound on a genuine full-rank lattice. `DivInputs0.Nu_lat` and
`a_pos` prevent treating a zero lattice as a nonzero arithmetic example.

The definition `DivInputs.val2` proves a valuation inequality **or the
period is zero**. The definition does not itself include a nonzero period.

There is also a direct obstruction to using `TrueColsTest.later` as
the required arithmetic completion. Its proof at
`Definitions/AutomorphicMembership/ExistsOkPins.lean:194–203` chooses
`RowsRestModel.model (fits l) 1 1 1`. In
`ModelLamPDef.lean:130–135`, this model sets `muAt w=C.mu0` for every
place. `SizeData₂.untwisted` therefore forces `F_j(w)=0` at every
place. This contradicts `FDef` at a residue-class-zero inert prime
with `hP=0`, positive `e_j`, and `p≤X''`, where `Fval` is strictly
positive. The actual column maps/compact period in the completion are
retained, but the auxiliary row model does not supply the needed
arithmetic twisting and Poincare structure.

`TwDat.untw B pl` in `CmQuadraticFormEqAlternatingForm.lean` is
available for arbitrary finite rational-prime support `pl`, and the
`MuIs.on/off` fields would provide the desired support once an actual
row stage is constructed. The existence of this twist datum alone
does not construct that row stage. `PtRows` in
`Definitions/LatticeFrames/PtRows.lean:18–27` explicitly includes
`1≤rS`; its standard assembled wrapper therefore also excludes m=2.

## Global nonvanishing interfaces checked

`Definitions/LatticeFrames/ChainParSucc.lean` defines actual theta-chain
steps and the `Reach`/`OntoAll` interface. `ThetaChainLValuesNonvanishing`
proves its declared `ChainLW`; passage to theta surjectivity also uses
the separate adjunction, metric, spanning and representation-theoretic
inputs in `ThetaLiftOntoAll`.

`FamilyLinkOnto.linkOnto_of_ontoAll` has no `rS≥1` restriction, but
requires an actual family/W datum, `PkHyp`, and `RowOK`.
`TrueGeometryFamilyRowData.famAllQ_of_allTrue` and
`MainTheoremFromPublishedResults.miStar2_of_allTrue` explicitly require
`1≤rS`; for `m=2`, `rS=0`. This rules out those particular wrappers,
not every global two-step period.

Positive row-space ranks, individual local-kernel nonvanishing and a
nonzero terminal branching map do not by themselves prove that the
composite global theta image has nonzero terminal period. The independent
reviewer is checking the direct period-anchor/surjectivity route.

## Remaining arithmetic target

No fully instantiated nonzero global two-step period or certified
positive full `sg=sum_j(gainD+F-E)` has been produced by this follow-up
as of this checkpoint. Raw positive `F` is not the requested bound.
The direct large-weight route must retain: actual Hecke and theta data,
the used rational/integral lattices, a full `SizeData₂`, exact gain and
error definitions, stabilizer factors, and the bridge to period valuation.
The scope lemmas above do not assert that such a direct construction
is impossible.

## Pointwise valuation and fixed ambient level checks (04:22 UTC)

Read the complete relevant period-integrality proofs in
`Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean:700–1116`,
including `stmtPair`, the three place branches, and
`l2_bound_of_inputs`. The ordinary inert branch at `hP=0` can avoid
served-orbit gains: `VV=∅` follows from `Cand`, which would require
`x^(eps/4)≤addOrderOf(0)=1`. The local length estimate still requires
the actual `MediumInertPrimeLengthBound`, actual compact-period
integrality, and their lattice/twist ties. No positive numerical RHS
has been promoted to a period valuation bound. The generic
`GandSy.servedModel_of_params` wrapper also requires `3≤x^(ez/5)`,
which the displayed candidate scale does not satisfy; it is not used.

Read the full `Formalism/LocalToGlobal/SiegelLatticeTheory/
HaarTransversals/HidaSetting.lean` definition in the independent
reviewer's exact source cache. `K2` is fixed as
`Kset ∩ K2cong(g0*g1,e0,z0,bw)`; `L_eq` fixes the full base lattice,
`g_eq` fixes the modulus, and `e_eq` fixes the projector. No arbitrary
extra principal subgroup can be inserted into those fields.
`LevelSubgroupNormalized` includes `Kg(g)⊆K2`. Therefore a nonzero
period constructed after an arbitrary small auxiliary level refinement
does not yet imply the fixed-`D7` `PuNZ` assertion. This does not rule
out a separate argument using a new allowable choice of `g0,g1`.

## SF-Q6-08: fixed inert prime without the packaged rank bound

The complete conditional pointwise proof is in
`pointwise_inert_valuation.tex`; exact arithmetic is in
`verify_pointwise_inert.py` and `pointwise_inert_certificate.json`.
Its actual gates are ThetaExpansionRealPlaces, KForm(sp=1), PairInt,
DGamDef, LevelFree, and the specified input and row lattices.
The one-orbit constant-one local theorem only requires p<=A and
partition-size<=A, so Shape.rankA is legitimately absent. At fixed
p863 the 5<=p hypothesis also bypasses the packaged splitBound>=3
wrapper. Finite-jet algebraicity does not discharge theta factorization.

For the variable gap G, the actual row partitions have sizes
8M+179 and 8M+24G-205. The resulting strong bound is
(128M+192G-208)/744768-9216*(2log_863(a)+1).
It exceeds the full conditional sg expression
(96M+48G+1728)/744768-76800log_863(a), for M>=0,G>=16,log_863(a)>=1.
With M=ceil(exp(10^10)), the previously proved positive lower bound
therefore persists for G>=36. The exact NodeGap definition allows
N=40 because rankX'=39; its bound is128016, so G=10^9 satisfies it.
This discharges that numerical gate only, not full theta surjectivity.
Root independently checked the complete SF08 algebra/composition proof;
critical reviewer is checking the source chain at this checkpoint.

## Actual row/twist stage boundary

`CmQuadraticFormEqAlternatingForm.lean:196-206` constructs genuine
TwDat.untw for every finite pl, including pl containing863. Its psi is
1 and Q empty. The actual MuIs.on/off fields140-148 would then identify
muAt863 with muTw863, whose character xiTw equals f.del at863!=pde.
Thus the constant-mu model obstruction is avoidable at the level of
available twist data, but TwDat is not the actual row-stage constructor.
`RowsRestWordColumnUnitBaseTupleAlt.lean:356ff` preserves W0.muAt
in Pk.what2. The full file's RealDat3, PkT, PerD, Nums and rational
reading fields tie those rows to actual geometric forms, Petersson
matrices, theta maps, lattices and periods. These fields still need a
joint actual witness before PairInt or the global DivInputs theorem
can be applied. Assigning arbitrary Euclidean row lattices would not
supply that witness.

## Independent review of SF-Q6-06

The complete revised diamond/Fourier/refined-level contribution was
independently checked; see `review_SF_Q6_06.md` for exact hash and
source-check scope. It passes for its stated definite ambient group.
The actual m2 Hida ambient is signature(8,1), so its Poincare map
requires an additional analytic nonvanishing argument; arbitrary
compact-open refinement also is not an existing fixed-K2 parameter.
