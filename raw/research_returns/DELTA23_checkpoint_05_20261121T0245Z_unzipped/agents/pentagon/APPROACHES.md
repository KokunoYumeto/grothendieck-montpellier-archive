# DELTA23 pentagon branch

Actor: GPT-6 Astra Pro, inherited effort (not exposed by runtime), run DELTA23, agent /root/pentagon.
Dates: 20 November 2026 UTC / 21 November 2026 CET after 23:00 UTC.

## Current proved reduction

D23.P10 computes the cubic bit a3 as the first translation coordinate in the explicit marked affine quotient E0=F3^2 ⋊ SL2(F3), order216. Its joint marked map with S4 is onto of order5184, with F′ image (F3²⋊Q8)×A4 of order864. After the supplied full-GT constraints a_f=rho and a2=nu4, twelve states remain, six of mixed parity. Compared with P3–P4, the source groups shrink nine-fold; the number of candidate states does not decrease. A.84 remains open: no mixed state has been proved to lift or proved impossible for actual full GT.

## Approaches tried

1. Re-read E.65 and FP.32/37. The prior exact gate is nu4=kappa_d mod2. No gap found in the portions used; E.58's lifting input depends on D.50 not attached, and is carried as a supplied input, not independently reproved.
2. Primary literature check, Lochak–Nakamura–Schneps 2026 arXiv:2602.12462v1, Theorem1.1 and §8. Theorem gives mapping-class actions with 0/1 puncture. Section8 explicitly does not provide full-GT cutting/Lego compatibility. The source does not fill the CM comparison. https://arxiv.org/html/2602.12462v1 .
3. Primary literature context, Lochak–Schneps, Open problems in GT theory, §1 Questions1.2 and1.8. Question1.2 asks whether full-GT abelianization is cyclotomic. Nonzero Delta on fullGT would refute that assertion, since Delta vanishes on Galois and cyclotomic is onto. Question1.8 concerns overlapping character definitions. https://webusers.imj-prg.fr/~leila.schneps/farb.pdf . No current-state theorem inferred from old problem list.
4. Common polyhedral S4 frame. Six octahedral points admit quartic but no invariant cubic-plus-fixed-point four-subset; cube's eight points admit both. Finite p-subgroup normalizer theorem of Boggi–Zalesskii (arXiv:2406.08639v2, TheoremA/6.2) helps with finite symmetries but does not supply arbitrary-solvable normalizer topology automatically. Even assuming a common full S4 frame, its four-point finite projections have independent central flips: proved D23.P1–P2. This defeats the naive finite common-frame argument. It does not survive FP.32's additional affine five-point comparison and is not a new full-GT counterexample.
5. D23.T1–T2 whole-proof review requested by root: passed, plus independent symbolic check of both transvection identities, integral braid relations, C^5, characteristic polynomial and cyclic basis. See transvection_check.txt.
6. New affine modular detector: successful, D23.P3–P4 with exact finite certificate. This is the strongest new main reduction on this branch.
7. Extend the detector through twisted rank-four symplectic B4/B5 module: refuted for that module, D23.P5. All affine cocycles are inner; the detector is not. Full exact linear systems and a short rank-free proof retained.
8. Induce the detector from an open subgroup fixing a strand using a forgetful map: construction possible in principle, but it belongs entirely to the forgetful family already annihilating the pentagon defect (prior FP.30). It cannot decide the main parity. No claim of a new tested obstruction.

## Unfinished next routes

- A genuinely Brunnian relative extension which retains the order-1944 cubic detector and the S4 evaluation simultaneously.
- A nontrivial comparison of the resulting relative cohomology lines; global Hilbert reciprocity alone does not provide it (root's independent calculation).
- Finite Krammer/BMW representations outside the special Burau families, retaining exact common-word correlations.

## Krammer continuation, 00:30–00:43 CET

9. All four nonzero Krammer specializations over F3 were checked. The largest five-point image has order102036672, but its evaluation pairs have nilpotent second derived subgroups. This branch fails by the actual FP.36 witness, despite the large full image.
10. Parameter choice q=i,t=−i overF9 succeeds in retaining the cubic detector. D23.P6 proves exact Frobenius-contragredient identification of the invariant B3 block with the order1944 affine detector, and a valid projective B4/full-twist quotient. First-pair group46656 has nonnilpotent second derived image. Root independently checked the whole proof and intertwiner.
11. Agentfive proved the full first-pair value is one of six exact matrices indexed by(rho,a3): quotient D8 is killed by the gentle three-cycle, and the remaining central C3 phase is uniquely fixed by the two-cycle (D23.F13). Characters proved the mixed pair splits into a solvable108 block and a unitary24192 block, and recovered a full six-dimensional three-cycle correlation with a non-scalar central correction (D23.C9-C10).
12. D23.P7 exactly enumerated the new reduced matrix pentagon: 163296 mixed commutator values against the six first values give36 solutions for each,216 total, no negative-scalar solutions. Direct multiplication of the original five factors rechecked all216. Both cubic signs therefore survive this finite equation; no profinite lift is asserted.
13. Common-word audit is continuing. Agentfive proves no S4 quotient of the joint Krammer source image (D23.F14), so at finite-word level its V4 phase can be changed while retaining all five Krammer evaluations. Solvable mixed blocks are independently attained by F′, via a determinant-phase Goursat argument. Characters is checking the perfect-block common-word correlation. Actual gentle or GT liftability remains distinct.

## Completed common-word audit and smaller gate

14. D23.P8–P9 complete the common-word audit. The full derived joint image of the first pair and three mixed orientations is the product of their derived groups. Consequently all216 matrix pentagon solutions come from one ordinary commutator word, including the reversed-pair correlations. Agentfive independently checked the proofs and reran the exact certificate. This does not give an actual gentle element. Agentfive's stronger no-S3 argument makes the S4 A4-coordinate independently variable at this finite-word level; hence this Krammer family cannot alone establish the main parity.
15. D23.P10 projects the affine cubic detector to order216 with literal marked generators X=(0,-U²), Y=(e1,-L²). The cubic bit is exactly translation coordinate1. Direct surjectivity and all six formulas are proved and checked. Joint order5184/derived864 replaces46656/7776, while the twelve actual candidate states and six mixed candidates remain unchanged. Root whole-proof/script check passed. No proper quotient of E0 retains the E58 translation witness; this is minimality only inside quotients of this detector.
16. Hurwitz representations from fixed-product four-tuples, modulo the product centralizer, give genuine B4/Z quotients when the product is nontrivial. The first GL2(F3) product1 family was caught as forgetful and discarded. For noncentral productU, all tested first-pair derived groups are too shallow to retain the cubic detector. This does not claim untested mixed pairs are blind.
17. AGL2(F3), order432, reflection class36: fixed producttranslation and fixed productpureunipotent give degrees198 and630. All braid/full-twist identities and all three pair types on each orbit were checked; every second derived pair group is nilpotent, so supplied FP.36 defeats these complete tested families. Affine-unipotent and cubic-product families are still being computed; no claim yet.
18. The degree9 permutation triple of P10 has passport [6,2,1]^3 and genus1. Primary BelyiDB has two orbits for this passport. Root is handling the exact match and geometry (first orbit j=0, second j=9261/8); this branch will not duplicate that investigation. Invariance of the cover alone is already gentle and cannot prove the parity.

## Further actual-source identity and completed finite tests

19. D23.P11–P12: two genuine noncentral Hurwitz tests (affine432 orbit648, affine3888 orbit20736) have nonnilpotent mixed second-derived groups; the first also retains a marked S4 quotient. An explicit904-letter word nevertheless gives the exact E58 cubic value, markedS4identity, complete F13 firststate, and identity on the entire NielsenS3 closure of both families. Its free two-cycle is exact. Its Krammer pentagon fails, so this word was not misreported as satisfying the combined test.
20. D23.P14 repairs that last finite-word issue: all496 Hurwitz pair components have only primes2,3, while the three simple KrammerSU factors have prime7. Goursat makes the latter independently adjustable while retaining the explicit firststate and every Hurwitz value. Choosing one of the three P7 solutions with identity solvable block gives one common ordinaryword satisfying all listed combined finite cycle/pentagon constraints. C15/F24 verify full Nielsen cycles; all216 also pass the legitimate q∘Phi generation test. This remains finite-word work, not actualgentle lifting or GT-kernel rigidity.
21. RootD1–D2 distribution no-go: independently whole-proof checked and N2 certificate rerun; exact normal-generation argument allows all fixed-target indices simultaneously. Primary Enriquez theorem and convention rechecked. See distribution_check.txt.
22. D23.P13 is an actual-source result, not a finite-shadow observation: the cubic descent DE preserves the complete harmonic affine96 evaluation. Hence a2DE=a2 and DeltaDE=d2=a2+a2DP universally on actualgentleH. Root and agentfive whole-proof checks and reruns pass. This identifies the harmonic duplication defect as a descended Delta character; it does not prove its vanishing.
23. Next live target is the half-character afterDE. Its offdiagonal order12mod2 target has no direct B-extension, so an exact induced degree24 B-action was constructed instead. B-image3456/E-image1728 are verified. The correction bDE+b is a literal scalar on its zero fiber. Both corrections survive the currently imposed finite source/cycle/frame/generation constraints, even jointly with originala2,b; no actual-preservation or nonpreservation result yet.

24. D23.P15 proves a limitation of the identity relative R2 method: if its normal seed subgroup makes the Kummer48 image nilpotent, B-normality forces the harmonic48 image nilpotent too. Any residual coordinate then has a2=b=0. This excludes that construction of a2=1,b=0, not the existence of such an actual element or nonidentity relative seeds.
25. D23.P16 completes the iteration probe with an actual correction formula b(DEh)+b(h) and a proved gentle-stable core quotient Q3456. Genuine finite automorphism extension, original-B compatibility, full relevant cycles and a simultaneous three-target N3 distribution test leave eight candidates, four for each correction. The finite test is exhausted at this level; neither vanishing nor an actual nonzero correction is proved.


## DELTA23 continuation: genuine Hurwitz stability and orthogonal blocks (2026-11-21)

- Negative class check: the fixed-point-free order3 class in affine216 loses the marked translation9 quotient already on the joint triple action. Stopped that four-tuple family; no main conclusion.
- Positive replacement, P17: the order6 class containing the literal cubic generators yields a unique degree1344 genuine B4/Z orbit. Its first image retains marked216 and a mixed degree72 image retains markedS4. Both statements are image-group quotient assertions, not transitive set maps. Complete17-orbit inventory and exact relations checked; root and five independently passed.
- Actual-source upgrade, P18: mixed Artin functoriality preserves the entire conjugacy-class tuple space for multiplier-one fullGT. The unique1344 and unique36 orbits are stable, yielding actual permutation covariance. Root and five independently passed. Coordinate deletion of tuples is restriction to a free factor; it was NOT silently treated as quotienting a meridian. Root later used intrinsic canonical block systems instead.
- Orthogonal structure, C23/F30: the1344 action has12blocks of112 singular projective points of Q6minus(F3), with localPSO6minus, independent simple socleS^12 and binarycode9. These are other agents' proved inputs; their exact certificates remain separately located.
- P19: independently derived the canonical twisted relative cup pairing and its exact Gram matrix. It literally equals C23Q; an actual fixed-block multiplier-one GT map is an isometry. Both other agents independently checked the entire proof and reran the certificate. This restriction does not exclude the existing H3 candidates, all of which already have multiplier1.
- P20: actualrho0 conjugator lies inN by localH propagation and (F2^12/C)^Q=0. Algebraic proof plus complete4096-vector replay. VA=AV reduces the four H3 lists to9quadruples. This is a necessary finite constraint, not actual existence.
- F32 audited independently: suppliedFP37 and markedBurau identification make signedF=R=I for normalizedrho0,a2=0; propagation then puts actualV inS^12. No circular assumptionV∈Γ.
- P21: the firstB3 action on four detector blocks is a centralC3 extension of the36point detector. Exact two-cycle uniquely fixes each of6 lifted f-values. Bcovariance and rootH4 pin a unique four-blockV, indices(0,0,0,2) for hypothetical normalizedmixed state. Remaining eight blocks and mixed/pentagon compatibility are open. A.84 remains OPEN.


## DELTA23: complete global list and raw cover (through 2026-11-21 01:58 UTC)

- P22 reduces the entire actual normalized1344-point conjugator to144 literal permutations, then72 after the two mixed72 components and their common-word graph. Completeness uses only two local seed centralizers, oforders18 and8, together with exactA/z3commutation and P21. Characters independently whole-proof checked and reran both certificatesPASS.
- FiveF34 reduces these to36 per cubicbit via normalization of the FULL firstB3 image. Every survivor has the explicit firstvalueF=[AB,V], inP′, with actual448restriction and bothcycles. RootH7/characters subsequently find ordinarysame-word(F12,R34) witnesses. These statements do not imposepair45 orfullgentleclosure.
- P23 reconstructs the raw product-fixed8064 cover as36 exactlinearframings of224vectors. Actualaction is linear because boundaryproduct is fixedexactly. Sixchoices perprojectiveblock reduce to6^4 rawlinearA/z3-commutinglifts for EVERY72candidateperbit. Thus canonicallinearity alone is blind; this is a provednegativefinite-testresult.
- RootH6 raworbitstability and construction independently audited/rebuiltPASS. It is not assumed that raw→base kernel is only globalC6; exactfirst/mixedgroup orders separately showmarkedprojection isomorphisms on those two evaluationgroups.
- P24 computes unique rawF/R from all36H7samewordwitnesses using exactSGS straight-lineprograms. Every witness admitsfullrawA/B/Ccovariance, with6globaldeckchoices. This closes this particularrawcovarianceattempt without excludingmixedstates; not a proof ofactualgentlemembership orfullpentagon.
- P25 derives the remaining exactpentagonvalue H45=[D,FR] with the reversinghalf-twistD andactualD^-1. All36base/rawfivefactorreplaysPASS byconstruction. MembershipinM45′ andcommon-wordrealizationwithF,R remain genuineadditionaltests. Root now computes those; characters imposegentleS3closure. A.84 remainsOPEN.

## DELTA23: actual necessary raw pentagon reduction (2026-11-21 02:07 UTC)

- F36 independently whole-proof checked and rerun PASS: the complete first associator value is uniquely F_V, not only a convenient witness. This closes the first-value loophole in subsequent exclusions.
- Root H8 independently read and exhaustively rerun PASS: all36 candidate V and every216 common-word R in the exact fiber were tested in full M45 derived, leaving12 V each3 R.
- P26 gives a genuine further necessary reduction to6 V each3 R. The raw45 and base45 marked pair groups are isomorphic. The eighteen rejected raw products have nonconstant order2 deck phases0/3. The literal raw pentagon is required: its universal central discrepancy has zero exponent sum, while z4 has exponent12, forcing the discrepancy to vanish. This source-level proof is explicit.
- P27 closes the updated raw covariance check: all18 remaining pairs have exactly6 canonical linear full raw covariance lifts. This removes no further candidates. Characters reports full mixed S3 common-word and norm checks also retain all18; root is testing the joint third-pair common-word constraint. A.84 remains OPEN.

## DELTA23: remaining finite source tests and five-puncture extension

- P28: all18 mixed-source candidates generate the entire induced finite B image via explicit permutation intertwiners. Six, one for every remaining V, have the intertwiner inside the derived pure image. Thus even the stronger integral-source cubic frame condition A in F-prime and harmonic allowed zero abelian class do not eliminate a remaining V. Root independently whole-proof checked/replayed PASS.
- Colored inverse class inventory yields unique5376 orbit; direct mixed markedS4 is absent on each of68 separate components, which is explicitly NOT a conclusion about their complete joint image. Whole joint testing delegated to characters. Two fixed-point-free order3 alternatives3888/7776 and one order4 alternative10752 also retain the first detector; these exploratory scans are paused for root's order5 priority.
- The original1344 and colored5376 sectors glue literally to a6720-point full spherical five-puncture action. All Artin/sphere relations and rho order5, Xi to Xi+3 were checked. A newly added pure-generator off-by-one was caught by author and root before use, corrected, and rebuilt. Full18 f12 values satisfy5norm and have explicit block-preserving cochains; membership in actual pure image is still being determined.

- F39 independently whole-proof checked and exact replay PASS: sixty simple factors are globally independent in the pure image, and every finite C5 cocycle is a pure coboundary. All18 explicit primitives lie even in its derived group. Thus this order5 frame test is exhausted without excluding a mixed candidate.
- P30 extends all18 prescribed oldV to exact four-generator covariance on the complete6720 spherical orbit. Together with rootH9/F38 full first-plus-cyclic-core common-word theorem, no omitted one of these finite source/covariance tests supplies a decision. Remaining main question staysOPEN.

- P31 proves a structural limit of the suggested central648 extension: since the original order6class has cyclic centralizer, every selectedliftedclass maps bijectively and equivariantly to it in ANYcentral extension. All its tuple braid actions are therefore identical. Noncentral extensions and different class unions remain outside this no-go.

### 2026-11-21T02:40:23.881545+00:00 — Full spherical covariance closes negatively

D23.P30 now proves all eighteen complete spherical covariance permutations lie in the independent derived-pure product S^60 from F39. The exact replay checks all four generator equations and all 1080 local memberships. Thus the full finite spherical action is implemented by derived-pure inner conjugation for every surviving pair. This adds no actual full-GT existence claim and supplies no new exclusion.

### 2026-11-21T02:42:23.051590+00:00 — Independent audit of a new actual-source reduction

Characters D23.C34 passes independent whole-proof and complete fresh replay. The actual same-associator last-meridian formula from F40 imposes eight correlated E0 evaluations; exhaustive six-orientation cycles reduce3456 raw assignments to nine labels(1,j,0),(53,j,0),(61,j,0). Their cubes all equal(1,0), so actual normalized mixed existence has a single remaining finite form. This is a genuine necessary exclusion, not a realization of that last form.
