/-
The ordered-group part of the branching lower bound, using only core Lean.
Kernel-checked in this run with official Lean 4.36.0 on 2026-11-25.
This certificate states every graph/partition hypothesis explicitly. It does
not formalize the separate circuit-to-partition argument.
-/
import Std
import Lean.Elab.Tactic.Omega

namespace PEqualNP.Outside.ThetaCircuitSize.BranchCoverCore

variable {V : Type}

def NoFourCycle (E : V → V → Prop) : Prop :=
  ∀ u w p q : V, u ≠ w → E u p → E u q → E w p → E w q → p = q

def LaterNeighbor (E : V → V → Prop) (label : V → Nat) (cut : Nat) (u : V) : Prop :=
  ∃ v : V, cut < label v ∧ E u v

def LaterTwins (E : V → V → Prop) (label : V → Nat) (cut : Nat) : Prop :=
  ∀ u w : V, label u = cut → label w = cut →
    LaterNeighbor E label cut u → LaterNeighbor E label cut w →
    ∀ v : V, cut < label v → (E u v ↔ E w v)

theorem later_twins_form_star [Nonempty V]
    (E : V → V → Prop) (label : V → Nat) (cut : Nat)
    (squareFree : NoFourCycle E) (twins : LaterTwins E label cut) :
    ∃ c : V, ∀ u v : V, label u = cut → cut < label v →
      E u v → u = c ∨ v = c := by
  classical
  by_cases active : ∃ u : V, label u = cut ∧ LaterNeighbor E label cut u
  · obtain ⟨u, hu, uActive⟩ := active
    by_cases other : ∃ w : V, label w = cut ∧ LaterNeighbor E label cut w ∧ w ≠ u
    · obtain ⟨w, hw, wActive, different⟩ := other
      obtain ⟨p, hp, up⟩ := uActive
      have uActive : LaterNeighbor E label cut u := ⟨p, hp, up⟩
      have wp : E w p := (twins u w hu hw uActive wActive p hp).mp up
      refine ⟨p, ?_⟩
      intro z q hz hq zq
      have zActive : LaterNeighbor E label cut z := ⟨q, hq, zq⟩
      have uq : E u q := (twins z u hz hu zActive uActive q hq).mp zq
      have wq : E w q := (twins u w hu hw uActive wActive q hq).mp uq
      exact Or.inr ((squareFree u w p q different.symm up uq wp wq).symm)
    · refine ⟨u, ?_⟩
      intro w v hw hv edge
      by_cases equal : w = u
      · exact Or.inl equal
      · exact False.elim (other ⟨w, hw, ⟨v, hv, edge⟩, equal⟩)
  · refine ⟨Classical.choice inferInstance, ?_⟩
    intro u v hu hv edge
    exact False.elim (active ⟨u, hu, ⟨v, hv, edge⟩⟩)

/-- A cover presented by k choices; repetitions are permitted. -/
def CoversBy {k : Nat} (E : V → V → Prop) (center : Fin k → V) : Prop :=
  ∀ u v : V, E u v → (∃ r : Fin k, center r = u) ∨ (∃ r : Fin k, center r = v)

theorem cover_of_ordered_stars {k : Nat}
    (E : V → V → Prop) (symmetric : ∀ u v, E u v → E v u)
    (label : V → Fin (k + 1))
    (independent : ∀ u v : V, label u = label v → ¬ E u v)
    (stars : ∀ r : Fin k, ∃ c : V, ∀ u v : V,
      (label u).val = r.val → r.val < (label v).val →
      E u v → u = c ∨ v = c) :
    ∃ center : Fin k → V, CoversBy E center := by
  classical
  let center : Fin k → V := fun r => Classical.choose (stars r)
  refine ⟨center, ?_⟩
  intro u v edge
  have different : (label u).val ≠ (label v).val := by
    intro same
    exact independent u v (Fin.ext same) edge
  have forward {a b : V} (ab : E a b)
      (before : (label a).val < (label b).val) :
      (∃ r : Fin k, center r = a) ∨ (∃ r : Fin k, center r = b) := by
    have a_lt : (label a).val < k := by
      have last_bound := (label b).isLt
      omega
    let r : Fin k := ⟨(label a).val, a_lt⟩
    have selected := Classical.choose_spec (stars r) a b rfl before ab
    change a = center r ∨ b = center r at selected
    rcases selected with h | h
    · exact Or.inl ⟨r, h.symm⟩
    · exact Or.inr ⟨r, h.symm⟩
  by_cases before : (label u).val < (label v).val
  · exact forward edge before
  · have after : (label v).val < (label u).val := by omega
    exact (forward (symmetric u v edge) after).symm

theorem cover_of_ordered_twins [Nonempty V] {k : Nat}
    (E : V → V → Prop) (symmetric : ∀ u v, E u v → E v u)
    (label : V → Fin (k + 1))
    (squareFree : NoFourCycle E)
    (independent : ∀ u v : V, label u = label v → ¬ E u v)
    (twins : ∀ r : Fin k, LaterTwins E (fun v => (label v).val) r.val) :
    ∃ center : Fin k → V, CoversBy E center := by
  apply cover_of_ordered_stars E symmetric label independent
  intro r
  exact later_twins_form_star E (fun v => (label v).val) r.val squareFree (twins r)

theorem cover_lower_bounds_groups [Nonempty V] {k t : Nat}
    (E : V → V → Prop) (symmetric : ∀ u v, E u v → E v u)
    (label : V → Fin (k + 1))
    (squareFree : NoFourCycle E)
    (independent : ∀ u v : V, label u = label v → ¬ E u v)
    (twins : ∀ r : Fin k, LaterTwins E (fun v => (label v).val) r.val)
    (minimum : ∀ center : Fin k → V, CoversBy E center → t ≤ k) : t ≤ k := by
  obtain ⟨center, covers⟩ := cover_of_ordered_twins E symmetric label squareFree independent twins
  exact minimum center covers

#print axioms later_twins_form_star
#print axioms cover_of_ordered_stars
#print axioms cover_of_ordered_twins
#print axioms cover_lower_bounds_groups

end PEqualNP.Outside.ThetaCircuitSize.BranchCoverCore
