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
