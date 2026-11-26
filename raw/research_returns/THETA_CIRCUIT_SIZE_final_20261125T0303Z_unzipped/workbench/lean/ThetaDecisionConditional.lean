/-
Exact project-model target, with the two remaining formal bridges explicit.

UNCOMPILED against the pinned Mathlib/PEqualNP environment in this run.
This file is a conditional theorem, NOT an unconditional Lean certificate
for the eighteen-gate result. The mathematical paper proves the two bounds;
this file shows precisely which formal interfaces would complete the
literal HasCircuitSize statement. No axiom or sorry is declared.
-/
import Mathlib
import PEqualNP.Defs

namespace PEqualNP.Outside.ThetaCircuitSize

open PEqualNP.CircuitLowerBounds PEqualNP.MetaComplexity

def thetaF (x : Fin 12 → Bool) : Bool :=
  ([(0, 1), (0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1),
    (0, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 1)] :
    List (Fin 12 × Fin 12)).any (fun e => x e.1 && x e.2)

def isNot (g : Gate) : Bool :=
  match g.op with
  | GateOp.not => true
  | _ => false

def notCount (C : Circuit) : Nat := (C.gates.filter isNot).length

def ComputesTheta (C : Circuit) : Prop :=
  ∀ x : Fin 12 → Bool, C.eval (List.ofFn x) = thetaF x

def NoNot (C : Circuit) : Prop :=
  ∀ g ∈ C.gates, g.op ≠ GateOp.not

lemma noNot_of_notCount_zero (C : Circuit) (h : notCount C = 0) : NoNot C := by
  intro g membership operation
  have filtered : g ∈ C.gates.filter isNot := by
    apply List.mem_filter.mpr
    exact ⟨membership, by simp [isNot, operation]⟩
  have positive : 0 < (C.gates.filter isNot).length := List.length_pos_of_mem filtered
  change (C.gates.filter isNot).length = 0 at h
  omega

/--
Conditional target theorem. The first hypothesis is the formal interface
for the normalized binary-gate bound. The second is the positive lower
bound. Neither is silently imported or asserted as an axiom.
-/
theorem theta_not_size_seventeen_of_bounds
    (binary_bound : ∀ s : Nat, HasCircuitSize 12 thetaF s →
      ∃ C : Circuit, FanInTwo C ∧ C.size ≤ s ∧ ComputesTheta C ∧
        17 + notCount C ≤ C.size)
    (positive_bound : ∀ C : Circuit, FanInTwo C → NoNot C →
      ComputesTheta C → 18 ≤ C.size) :
    ¬ HasCircuitSize 12 thetaF 17 := by
  intro candidate
  obtain ⟨C, fanin, size, computes, binary⟩ := binary_bound 17 candidate
  have noNots : notCount C = 0 := by omega
  have positive := positive_bound C fanin (noNot_of_notCount_zero C noNots) computes
  omega

theorem theta_lower_of_not_seventeen
    (no17 : ¬ HasCircuitSize 12 thetaF 17) :
    ∀ s : Nat, HasCircuitSize 12 thetaF s → 18 ≤ s := by
  intro s candidate
  by_contra bad
  have small : s ≤ 17 := by omega
  obtain ⟨C, fanin, size, computes⟩ := candidate
  exact no17 ⟨C, fanin, size.trans small, computes⟩

#print axioms noNot_of_notCount_zero
#print axioms theta_not_size_seventeen_of_bounds
#print axioms theta_lower_of_not_seventeen

end PEqualNP.Outside.ThetaCircuitSize
