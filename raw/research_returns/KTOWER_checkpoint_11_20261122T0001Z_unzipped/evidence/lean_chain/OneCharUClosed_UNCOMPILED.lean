/-
An explicitly closed proof term extracted from the pinned archive.
Commit: 7cbf7a0c32fca1badf05931879a37c3f8a2b03b4.
This file has NOT been compiled in this session.  It is supplied to make the
source-level conclusion directly checkable in the archive's own environment.
-/
import Development.AutomorphicArithmetic.AutomorphicVarieties.SmallClassNumbers.CorGKOf

open UpperTheory.V UpperTheory.V.Z.J

theorem KTOWER_oneCharU_closed : UpperTheory.V.Z.J.OneCharU_s := by
  let hH : UpperTheory.V.Af.HypothesesH' :=
    UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt
      UpperTheory.V.SmallClassNumbers.litN UpperTheory.V.Z.Tf.SR.descWeak
  have hK := UpperTheory.V.ZK.lemmaK_litN_alt hH.litN
  have hC := UpperTheory.V.HV.Core0.cohInp_alt hH.litN hK
  have hE := unlEnd3E (UpperTheory.V.Z.J.linkedUnlE_alt hH)
  have hA := UpperTheory.V.HV.Core0.automorphyUnramified_of_litN_of_gdEnd
    hH.litN (UpperTheory.V.Z.Win.Dn.ends0_alt hH).1
  exact UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy
    hC UpperTheory.V.Alg.M.main_holds UpperTheory.V.Alg.M.mprime_holds
    UpperTheory.V.Alg.lemmaP
    (UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH hH)
    (UpperTheory.V.Z.J.rigIUE_alt hC hH
      (UpperTheory.V.HV.DescentVanishingReductions.adjoint_lifting_of_cohomology hH) hE)
    (UpperTheory.V.Z.Win.RR.rigII_a_alt hC hH
      (UpperTheory.V.HV.DescentVanishingReductions.adjoint_lifting_of_cohomology hH))
    (UpperTheory.V.Z.J.admissible_typeI_even_level_alt hC hH hE) hA

-- Run these commands only after compiling the archive and this file.
#check KTOWER_oneCharU_closed
#print axioms KTOWER_oneCharU_closed
