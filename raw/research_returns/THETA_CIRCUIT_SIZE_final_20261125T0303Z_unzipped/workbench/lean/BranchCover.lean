/-
A compact formalization of the graph part of the first-branch argument.

Status: UNCOMPILED in this run. Lean 4.36.0 is available, but the complete
project import environment was not assembled. See BranchCoverCore.lean for
a separately compiled certificate of the ordered-group result.
This file is intentionally conditional on the ordered-group hypotheses;
it does not claim to formalize the circuit-to-group construction or the
concrete 18-gate circuit lower bound. Its mathematical statements are proved
in full in the paper and research note. No source proof has been copied.

Expected imports: the pinned project's Mathlib and PEqualNP.Defs.
Only standard permitted axioms (propext, Classical.choice, Quot.sound) may
occur; inspect the #print axioms output after a successful compilation.
-/
import Mathlib
import PEqualNP.Defs

namespace PEqualNP.Outside.ThetaCircuitSize.BranchCover

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- An explicit common-neighbor form of absence of a four-cycle. -/
def NoFourCycle (G : SimpleGraph V) : Prop :=
  ∀ u w p q : V, u ≠ w → G.Adj u p → G.Adj u q →
    G.Adj w p → G.Adj w q → p = q

/-- A vertex has a neighbor in a strictly later group. -/
def LaterNeighbor (G : SimpleGraph V) (label : V → ℕ) (cut : ℕ) (u : V) : Prop :=
  ∃ v : V, cut < label v ∧ G.Adj u v

/-- Active vertices in one group are twins when restricted to later groups. -/
def LaterTwins (G : SimpleGraph V) (label : V → ℕ) (cut : ℕ) : Prop :=
  ∀ u w : V, label u = cut → label w = cut →
    LaterNeighbor G label cut u → LaterNeighbor G label cut w →
    ∀ v : V, cut < label v → (G.Adj u v ↔ G.Adj w v)

/-- One selected vertex meets every edge from a residual twin group to later groups. -/
theorem later_twins_form_star [Nonempty V]
    (G : SimpleGraph V) (label : V → ℕ) (cut : ℕ)
    (squareFree : NoFourCycle G) (twins : LaterTwins G label cut) :
    ∃ c : V, ∀ u v : V, label u = cut → cut < label v →
      G.Adj u v → u = c ∨ v = c := by
  classical
  by_cases active : ∃ u : V, label u = cut ∧ LaterNeighbor G label cut u
  · obtain ⟨u, hu, uActive⟩ := active
    by_cases unique : ∀ w : V, label w = cut → LaterNeighbor G label cut w → w = u
    · refine ⟨u, ?_⟩
      intro w v hw hv edge
      exact Or.inl (unique w hw ⟨v, hv, edge⟩)
    · push_neg at unique
      obtain ⟨w, hw, wActive, different⟩ := unique
      obtain ⟨p, hp, up⟩ := uActive
      have uActive : LaterNeighbor G label cut u := ⟨p, hp, up⟩
      have wp : G.Adj w p := (twins u w hu hw uActive wActive p hp).mp up
      refine ⟨p, ?_⟩
      intro z q hz hq zq
      have zActive : LaterNeighbor G label cut z := ⟨q, hq, zq⟩
      have uq : G.Adj u q := (twins z u hz hu zActive uActive q hq).mp zq
      have wq : G.Adj w q := (twins u w hu hw uActive wActive q hq).mp uq
      exact Or.inr ((squareFree u w p q different.symm up uq wp wq).symm)
  · refine ⟨Classical.choice inferInstance, ?_⟩
    intro u v hu hv edge
    exact False.elim (active ⟨u, hu, ⟨v, hv, edge⟩⟩)

/-- A vertex-cover predicate with no external theorem dependencies. -/
def IsVertexCover (G : SimpleGraph V) (C : Finset V) : Prop :=
  ∀ u v : V, G.Adj u v → u ∈ C ∨ v ∈ C

/--
An ordered partition with k earlier groups and one final independent group
has a cover of at most k vertices if every earlier group meets its later
edges in a star. Equal labels may never contain an edge.
-/
theorem cover_of_ordered_stars {k : ℕ}
    (G : SimpleGraph V) (label : V → Fin (k + 1))
    (independent : ∀ u v : V, label u = label v → ¬ G.Adj u v)
    (stars : ∀ r : Fin k, ∃ c : V, ∀ u v : V,
      (label u).val = r.val → r.val < (label v).val →
      G.Adj u v → u = c ∨ v = c) :
    ∃ C : Finset V, C.card ≤ k ∧ IsVertexCover G C := by
  classical
  let center : Fin k → V := fun r => Classical.choose (stars r)
  let C : Finset V := Finset.univ.image center
  have center_mem (r : Fin k) : center r ∈ C := by
    exact Finset.mem_image.mpr ⟨r, Finset.mem_univ r, rfl⟩
  have small : C.card ≤ k := by
    have image_bound : C.card ≤ (Finset.univ : Finset (Fin k)).card := Finset.card_image_le
    simpa using image_bound
  refine ⟨C, small, ?_⟩
  intro u v edge
  have different : (label u).val ≠ (label v).val := by
    intro same
    exact independent u v (Fin.ext same) edge
  have forward {a b : V} (ab : G.Adj a b)
      (before : (label a).val < (label b).val) : a ∈ C ∨ b ∈ C := by
    have a_lt : (label a).val < k := by
      have last_bound := (label b).isLt
      omega
    let r : Fin k := ⟨(label a).val, a_lt⟩
    have selected := Classical.choose_spec (stars r) a b rfl before ab
    change a = center r ∨ b = center r at selected
    rcases selected with h | h
    · exact Or.inl (h.symm ▸ center_mem r)
    · exact Or.inr (h.symm ▸ center_mem r)
  rcases lt_or_gt_of_ne different with before | after
  · exact forward edge before
  · exact (forward edge.symm after).symm

/-- The ordered residual-twin partition has a vertex cover with at most k vertices. -/
theorem cover_of_ordered_twins [Nonempty V] {k : ℕ}
    (G : SimpleGraph V) (label : V → Fin (k + 1))
    (squareFree : NoFourCycle G)
    (independent : ∀ u v : V, label u = label v → ¬ G.Adj u v)
    (twins : ∀ r : Fin k, LaterTwins G (fun v => (label v).val) r.val) :
    ∃ C : Finset V, C.card ≤ k ∧ IsVertexCover G C := by
  apply cover_of_ordered_stars G label independent
  intro r
  exact later_twins_form_star G (fun v => (label v).val) r.val squareFree (twins r)

/-- A lower bound for all vertex covers is a lower bound for the earlier group count. -/
theorem cover_lower_bounds_groups [Nonempty V] {k t : ℕ}
    (G : SimpleGraph V) (label : V → Fin (k + 1))
    (squareFree : NoFourCycle G)
    (independent : ∀ u v : V, label u = label v → ¬ G.Adj u v)
    (twins : ∀ r : Fin k, LaterTwins G (fun v => (label v).val) r.val)
    (minimum : ∀ C : Finset V, IsVertexCover G C → t ≤ C.card) : t ≤ k := by
  obtain ⟨C, small, covers⟩ := cover_of_ordered_twins G label squareFree independent twins
  exact (minimum C covers).trans small

#print axioms later_twins_form_star
#print axioms cover_of_ordered_stars
#print axioms cover_of_ordered_twins
#print axioms cover_lower_bounds_groups

end PEqualNP.Outside.ThetaCircuitSize.BranchCover
