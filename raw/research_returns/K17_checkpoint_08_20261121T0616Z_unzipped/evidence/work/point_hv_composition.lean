/-
K17 review fragment, 2026-11-21.
This is an uncompiled composition of source theorem declarations inspected
at the pinned mirror revision. It is not a new Lean execution certificate.
Every argument is supplied by the cited source; no numerical LayerLe bound
is assumed here, since LayerLe remains a premise inside PointHV itself.
-/
import Development.AutomorphicArithmetic.AutomorphicVarieties.SmallClassNumbers.CorGKOf

namespace K17Review

theorem host_point : UpperTheory.V.HV.PointHV := by
  have hN := UpperTheory.V.SmallClassNumbers.litN
  have hH :=
    UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt
      hN UpperTheory.V.Z.Tf.SR.descWeak
  have hK := UpperTheory.V.ZK.lemmaK_litN_alt hN
  have h23 :=
    UpperTheory.V.HV.DescentVanishingReductions.countII_and_countIII_of_printsH_of_sp4In
      hH hK (UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt hH)
  have h5 :=
    UpperTheory.V.Z.J.count_v_of_printed_bound_k_reduced_unitary_lift
      hH hK (UpperTheory.V.Z.Win.Dn.ends0_alt hH).2
  obtain ⟨CK, hL⟩ := hK
  exact UpperTheory.V.HV.pointHV_of_counts
    (UpperTheory.V.HV.U.pt_s hN) hN.coh.lfK hN.coh.ltK hL
    (UpperTheory.V.U3.countI UpperTheory.V.SmallClassNumbers.corGK)
    h23.1 h23.2 h5
    (UpperTheory.V.HV.countZ UpperTheory.V.X.propZ)

end K17Review
