# Mathematical core of a Pro successor prompt: the division bound for Weil classes (Hodge line)

By Claude Opus 5.5 at effort high, 21 Nov 2026, from `HODGE_DIVISION_ATTACK_20261121.md` (same folder). This is the
mathematics a prompt needs. The house frame (push rule, three-hour review, checkpoints, CHECK_EVENTS, lint) is added by
the main session when the prompt is built.

## The target, in one sentence

For Weil-type abelian 2n-folds with an imaginary quadratic K, bound the **detector degree** δ_W (the least degree of an
effective n-cycle with nonzero projection to the Weil plane) uniformly on a Zariski-dense set of a Weil family. Weil
classes are then algebraic on the whole family, with an explicit division bound.

## Proved inputs (cite; do not re-prove)

1. **Reduction.**
   - Algebraicity on every fibre ⟺ c_t is bounded on a Zariski-dense set ⟺ on one Hecke orbit ⟺ on the CM points.
     Integral numerators of bounded degree force bounded multipliers. (HECKE_DIV R21–R23 + P0; GHOSTS B06; attack file
     R1, R2.)
   - Arithmetic form: GHOSTS B02/B03 and HECKE_DIV P6 (precedent: Brünjes–Serpé, arXiv 0901.4853, Thm 3.4).
2. **Theorem W** (attack file §1, R4): δ_W ≤ c_t ≤ C_{n,a}(δ,T)·δ_W⁴ for every Weil class t, every K and every n, with an
   explicit constant (scripts in `division_attack_scripts\`).
3. **Lemma Dom:** bounded δ_W on a dense set ⟺ one irreducible family of bounded-degree detecting n-cycles dominates the
   family (dimension ≥ n²).
4. **Propositions O, O′ and Corollary O″.** Cyclic-cover and genus ≥ 1 Prym–Tyurin detector families have image
   dimension ≤ 3n. A genus-0 Hurwitz source needs an irreducible ρ of dimension m ≥ (n² − 2n + 3)/2, with all but
   2n + 2m − n² − 3 local monodromies complex reflections.
5. **Known finite cases:**
   - Q(ω), n = 2, principal component: δ_W ≤ D₀ = 132,269,760 (GHOSTS R12, from Schoen 1988/1998, **published**).
   - Every polarization: D₆ = 57,854,793,024,000 (GHOSTS R20–R24, statement level).
   - n = 2, all K: Markman (**preprint**).
   - n = 4, Q(ω) split: Severn (**unrefereed**).
6. **J is not the quantity (Theorem E):** on the Q(ω) principal component, J_W is unbounded on CM points while
   δ_W ≤ D₀. Graph detectors give δ_W ≤ C(n,K)·J_W (Proposition G). Fixed-source transport is of order √J (DEG_L B19,
   checked; B21, statement level).

## Targets, in order

1. **Q(i), n = 2, principal component.**
   - Compute the polarization type of Θ restricted to the (±i)-Prym B of an unramified cyclic 4-cover of a genus-3 curve.
     The kernel has order 2⁸; decide whether it is B[2].
   - Run GHOSTS R12's Bézout scheme: W₄(C) ∩ T₀ in J(C) embedded by 3Θ, with deg W₄ = 3⁴·9!/5!, and (1 − σ²)^*Θ ≤ 4Θ.
   - Prove Schoen's dominance in this case, with the exact locator.
   - Output: an explicit D₀(Q(i)) and C₄(Q(i)).
2. **n = 3 (sixfolds), every K with h_K = 1 and every determinant.**
   - Decide whether Schoen's sixfold Prym family (unramified cyclic covers of genus-4 curves; 9 = 9 dimensions) dominates
     each Weil sixfold family, by computing the differential of the period map.
   - Where it does, extract D₆-type constants. Where it does not, prove the image dimension and name the missing
     components.
3. **n = 4: identify the reflection-group source.**
   - Confirm that Severn's monodromy group (order 39,191,040, 756 roots, K⁶) is G₃₄.
   - Then **reprove Severn's dominance from Corollary O″ and published inputs:** Chevalley–Weil branch data for G₃₄-covers
     of P¹ giving an isotypic part of dimension 8 and signature (4,4), and the cycles (Schoen-type suppliers, then
     Brauer transfer).
   - Output: a proof of bounded division for Q(ω) Weil eightfolds that does not depend on the unrefereed manuscript.
4. **n ≥ 5: the imprimitive groups G(d,e,m), m ≥ (n² − 2n + 3)/2.**
   - For K = Q(ω) (d ∈ {3, 6}) and K = Q(i) (d = 4), determine the Hurwitz families of P¹-covers with G(d,e,m) monodromy
     whose Prym–Tyurin part is of Weil type with signature (n,n).
   - Compute the image dimension in the Weil family, and decide dominance for n = 5.
5. **The non-curve alternative:** one weakly G-semiregular perfect complex E₀ on one fibre, with e^{B₀}ch(E₀) = λt + P(θ)
   (DEG_L S-14; Perry's deformation theorem; Markman's secant sheaves for n = 2). Construct it for n = 3 or n = 4 at the
   CM point E^{2n} (balanced action), where all classes are divisor-generated (HODGE_SIGN SG-04, HECKE_DIV R24F).

## Gates and how a run checks itself

- Every bound is integral and effective: integral cycles, effective positive and negative parts, a stated polarization,
  and the class normalization (δ, T).
- Dominance claims carry the rank of the period-map differential, computed exactly.
- Every use of Markman, Severn or 032 is marked conditional, with its exact statement number.
- Every result is also stated in the project's frame:
  - c_t and δ_W are the integral, uniform form of Grothendieck's condition A (cote 16, scan 050, corrected in SIGN_NEXT
    SN-C03/C04);
  - the positivity step is condition I (scan 049) and cote 44's Th. 4;
  - the resultant projector is the Cayley–Hamilton inverse of scans 048–049;
  - a counterexample would be a ghost (GHOSTS B03).

## What a run must not assume

- That J, the core index, or any isogeny degree controls c_t. **It does not** (Theorem E).
- That positivity (Hodge index, Rosati, Rallis norms, Alpöge's sign) produces cycles. It only divides classes that
  cycles already give (HECKE_DIV A3; SIGN_NEXT SN-14).
- That GRH bounds anything here. The Rallis L-values sit at s = 3/2 (DEG_L B1), and Hecke equidistribution gives no cycle
  bound (HECKE_DIV A1).
- That Schoen-type cyclic Prym families reach n ≥ 4 (Proposition O).
- That a nonzero period, or algebraicity at one point or at each prime separately, gives a uniform bound (R1, R3).
- That 032, Markman or Severn are refereed. Use them as conditional inputs only.
