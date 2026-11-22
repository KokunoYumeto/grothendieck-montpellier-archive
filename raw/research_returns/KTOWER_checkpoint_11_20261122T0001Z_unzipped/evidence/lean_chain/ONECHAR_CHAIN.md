# KT-ONECHAR-CLOSED: direct source proof-term trace

Date: 2026-11-21. Investigator: GPT-6 Astra Pro, agent `/root/lean_chain`; effort setting not exposed. All source locators are at commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of `CocoSgt/riemann-hypothesis-lean`. The source bytes, hashes, and an uncompiled closed proof term are included in this directory.

## Result and scope

**Under the prompt's convention of citing the archive's declarations as theorems, `UpperTheory.V.Z.J.OneCharU_s` is a theorem with no additional mathematical hypotheses.** This conclusion follows by direct substitution of the nine proof terms actually displayed in the source. It no longer depends on the intake's estimated declaration closure. This session did not install or run Lean and did not obtain a new `#print axioms` result. The supplied `OneCharUClosed_UNCOMPILED.lean` is a reproducible witness to be checked in the archive's environment, not a claimed kernel certificate.

Write `AV/` for `src/Development/AutomorphicArithmetic/AutomorphicVarieties/` and `DTC/` for `AV/ModularityArgument/ThresholdArguments/DenseThresholdCases/`. The implication is `UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy`, `DTC/FOneCharU.lean:75–95`; the nine arrows are on line 76. Its actual application, with all arguments, is `DTC/LinkedUnlE.lean:49–54`.

## All nine hypotheses and their discharge

| No. | Exact proposition | Proof term used in `LinkedUnlE.lean:53–54` | Declaration locator |
|---|---|---|---|
| 1 | `UpperTheory.V.U3.CohInp` | `UpperTheory.V.HV.Core0.cohInp_alt hH.litN hK` (the local `hC`) | `DTC/CohInp.lean:16–17` |
| 2 | `UpperTheory.V.Alg.LemmaM` | `UpperTheory.V.Alg.M.main_holds` | `AV/CommutativeAlgebra/GradedModulesLength/MainCotSpan.lean:32–70` |
| 3 | `UpperTheory.V.Alg.LemmaM'` | `UpperTheory.V.Alg.M.mprime_holds` | `AV/CommutativeAlgebra/GradedModulesLength/Mprime.lean:38–80` |
| 4 | `UpperTheory.V.Alg.LemmaP` | `UpperTheory.V.Alg.lemmaP` | `AV/CommutativeAlgebra/LemmaP.lean:256–424` |
| 5 | `UpperTheory.V.Z.Kato.WeilSphericalRecords.KatoTwoW` | local `hKa`; its caller supplies `UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH hH` | `DTC/KatoTwoWOfPublishedH.lean:48–49`, called at `DTC/WindowBoundOfLiteratureLevel.lean:29` |
| 6 | `UpperTheory.V.Th.RigidityFirstCase` | `UpperTheory.V.Z.J.rigIUE_alt hC hH (UpperTheory.V.HV.DescentVanishingReductions.adjoint_lifting_of_cohomology hH) hE` | `DTC/ERigIU.lean:80–146` |
| 7 | `UpperTheory.V.Th.RigiditySecondCase` | `UpperTheory.V.Z.Win.RR.rigII_a_alt hC hH (UpperTheory.V.HV.DescentVanishingReductions.adjoint_lifting_of_cohomology hH)` | `DTC/RRRigII.lean:25–102` |
| 8 | `UpperTheory.V.Z.J.AdmI_s` | `UpperTheory.V.Z.J.admissible_typeI_even_level_alt hC hH hE` | `DTC/AdmissibleTypeIEvenLevel.lean:76–136` |
| 9 | `UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt` | local `h3`; its caller supplies `UpperTheory.V.HV.Core0.automorphyUnramified_of_litN_of_gdEnd hH.litN (UpperTheory.V.Z.Win.Dn.ends0_alt hH).1` | `DTC/CohInp.lean:18`, `DTC/DnEndsTop.lean:15–16`, and `DTC/WindowBoundOfLiteratureLevel.lean:27–29` |

The supporting local terms in that displayed application are:

- `hK := UpperTheory.V.ZK.lemmaK_litN_alt hH.litN`, declared at `DTC/KFinal.lean:11` and supplied by `WindowBoundOfLiteratureLevel.lean:26`.
- `hE := unlEnd3E (UpperTheory.V.Z.J.linkedUnlE_alt hH)`, defined locally at `LinkedUnlE.lean:51`; `linkedUnlE_alt` is the full expression on lines 43–48. The imported implication `unlEnd3E` is declared at `AV/ModularityArgument/LinkedUnramifiedChains/LogarithmicNormBounds/BlockValuationRep.lean:234`.
- `UpperTheory.V.HV.DescentVanishingReductions.adjoint_lifting_of_cohomology hH` is declared at `DTC/AdjointLiftingOfCohomology.lean:31`.

The propositions retain their own universal arithmetic hypotheses. For example, `OneCharU_s` requires `GD Ω K l e ψ` for each specialization (`DTC/NumberU3US.lean:49–59`). Calling the proposition closed does not remove those conditions from its content.

## Closing `hH` and tracing the root

The replacement

```
hH := published_hypotheses_from_patching_alt
        UpperTheory.V.SmallClassNumbers.litN UpperTheory.V.Z.Tf.SR.descWeak
```

is closed. `published_hypotheses_from_patching_alt` is the explicit record expression in `DTC/PublishedHypothesesFromPatching.lean:98–103`. Its `litN` argument is the closed theorem in `AV/SmallClassNumbers/CorGKOf.lean:20–23`. The other argument, `UpperTheory.V.Z.Tf.SR.descWeak`, is the closed theorem at `AV/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean:29–30`, directly from `descWeakAll` at lines 26–27. The same `CorGKOf.lean` file already repeats the full nine-term application in `corGK_of` at lines 10–18, then supplies this closed `hH` to obtain `corGK` at line 25. Thus the extraction of a closed `OneCharU_s` proof is particularly direct: take the inner term from `corGK_of` after making exactly the substitution used by `corGK`.

The actual named route used by the root is:

1. `src/Main.lean:4`: `riemannHypothesis := rhOfAll`.
2. `src/Supplements/Kernels/MainTheorems.lean:7–9`: `rhOfAll` uses `allChi`, which is `UpperTheory.FinalTheorems.everyCharacter`.
3. `src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7–11`: `everyCharacter` supplies `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` to `everyCharacter_of_row`; that expression uses `UpperTheory.One.vwin_of_row`.
4. `DTC/VwinOfRow.lean:4–5`: `vwin_of_row` supplies the open-image record, `UpperTheory.BaseChangeIdentities.baseChangeN`, and the same Galois row to `UpperTheory.One.Join.automorphic_window_of_inputs`.
5. `DTC/TopMainZj.lean:71–74`, then 55–58: `automorphic_window_of_inputs` supplies the CM record and `v_window_of_depth_zero_residual_bc_cm` constructs the four-field `LiteratureRankNHypothesis` record.
6. `DTC/WindowBoundOfLiteratureLevel.lean:30–34`: that record supplies `published_hypotheses_from_patching_alt hN ...descWeak` to `vwin_of_hypotheses_H_E_alt`.
7. `DTC/WindowBoundOfLiteratureLevel.lean:25–29`: the latter supplies `hK`, `katoTwoW_of_printsH hH`, and the automorphy term to `count_i_of_printed_bound_k_kato_automorphy`.
8. `DTC/LinkedUnlE.lean:49–54`: the full nine-term `OneCharU_s` application is present literally.

The closed Galois-row declaration is `src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean:6`:
`galoisLocalGlobalStrong_recParameter := galoisRepresentations_of_thetaLift UpperTheory.TP.K.tLiftK`.
These imported theorems are cited as archive results, as requested; this trace does not claim to reprove their mathematical contents.

## Exact multiplicity condition

`DTC/NumberU3US.lean:57–59` states that the finite set `X` consists of actual three-dimensional Galois representations. It requires

```
∀ ρ ∈ X, ∀ ρ' ∈ X, Af.RepIso ρ ρ' → ρ = ρ'
```

in addition to membership in the union of the `Adm3U_s` and `Adm2A` classes. This is distinctness of isomorphism classes, not distinctness of the trace at a single Frobenius. `FOneCharU.lean:59–65` proves the needed injectivity; lines 66–74 transport the sum through `Finset.image` and use `Finset.sum_image`. Consequently, a pointwise unit check needs coverage of every admissible representation, while a numerical valuation upper bound by a Hecke product must retain enough indices to cover all pairwise nonisomorphic systems. Colliding traces cannot be deduplicated merely because they have the same value at one prime.

## Check performed

The complete proof of `oneCharU_of_katoTwoW_rig_admI_automorphy`, including its private helper, was read. Every argument of the application in `LinkedUnlE.lean:49–54` was matched to its declared proposition. The whole source expressions along the eight-step outer chain, the closed `CorGKOf.lean` construction, and the top-level proofs listed in the table were read. Imported supporting theorems remain cited background. No Lean elaboration, kernel check, global no-axiom scan, or full verification of every transitive dependency is claimed.

## Geometric interpretation

This closes a source-level gate on a bound for strict Galois-cohomology groups attached to Tate twists over `Spec Z[1/l]`. The implication controls the length of the corresponding integral l-adic extension classes by valuations of congruences between an Eisenstein trace and automorphic traces. It is not itself a vanishing theorem and introduces no new statement about the rational mixed-Tate Ext groups. The relation to the motivic K-groups uses K17's carried `VK-PT` bridge, not a new consequence of formal-language reachability.
