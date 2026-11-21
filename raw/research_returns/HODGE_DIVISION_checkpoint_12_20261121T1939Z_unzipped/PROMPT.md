**The attached files.** Besides this file there is one ZIP, `HODGE_DIVISION_bounding_the_detector_degree_of_Weil_classes.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Markman_Hodge_abelian_fourfolds_2502.03415.zip` is the folder `LIT_Markman_Hodge_abelian_fourfolds_2502.03415/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# HODGE_DIVISION: bounding the detector degree of Weil classes

This prompt continues the Hodge line of 20-21 November 2026: our prompts 37 to 41 (THETA3, HECKE_DIV, GHOSTS, JAC1964,
DEG_L) and 45 (SIGN_NEXT). Their returns and our intakes of them are attached, with an attack on their reduction by
Claude Opus 5.5 at effort high (`HODGE_DIVISION_ATTACK_20261121.md`, with its check events and scripts).

**What is settled.** Algebraicity of a Hodge class on every fibre of a family is equivalent to a bounded division bound c_t
on one Zariski-dense set: one Hecke orbit, the CM points, or infinitely many primes. With the rational Hodge conjecture for
CM abelian varieties (032), the Hodge conjecture for abelian varieties is equivalent to the finiteness of the supremum of
c_t over the CM points of every special subvariety, and a counterexample would be a ghost. For Weil classes, c_t is
controlled by one integer, the detector degree δ_W. This run bounds it.

## The target, in one sentence

For Weil-type abelian 2n-folds with an imaginary quadratic K, bound the **detector degree** δ_W (the least degree of an
effective n-cycle with nonzero projection to the Weil plane) uniformly on a Zariski-dense set of a Weil family. Weil
classes are then algebraic on the whole family, with an explicit division bound.

## Proved inputs (cite; do not re-prove)

1. **Reduction.**
   - Algebraicity on every fibre ⟺ c_t is bounded on a Zariski-dense set ⟺ on one Hecke orbit ⟺ on the CM points.
     Integral numerators of bounded degree force bounded multipliers. (HECKE_DIV R21–R23 + P0; GHOSTS B06; `HODGE_DIVISION_ATTACK_20261121.md`
     R1, R2.)
   - Arithmetic form: GHOSTS B02/B03 and HECKE_DIV P6 (precedent: Brünjes–Serpé, arXiv 0901.4853, Thm 3.4).
2. **Theorem W** (`HODGE_DIVISION_ATTACK_20261121.md` §1, R4): δ_W ≤ c_t ≤ C_{n,a}(δ,T)·δ_W⁴ for every Weil class t, every K and every n, with an
   explicit constant (scripts in `division_attack_scripts/`).
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

1. **Q(i), n = 2, principal component: the even half is done; check it, and do the odd half.**
   - Done in the attack (§5): Θ restricted to the (±i)-Prym is of type (2,2,2,2) (the kernel is B[2]). The principal
     component splits into an even part (reached by Prym lattices) and an odd part (E_i⁴ with the product polarization).
     On the even part D₀(Q(i)) = 914,248,581,120, with C₄(Q(i)) explicit. Its inputs:
     - Schoen 1988 (Compositio Math. 65, 3-32, attached), Theorem 2.0 (pp. 11-12) and Corollary 3.1 (p. 25);
     - the attack's own proof of dominance for (h, m) = (4, 4), via a base-point-free pencil and a Hurwitz count. Schoen's
       p. 26 lists that case only as possible, and his Theorem 3.2 proves (4, 3).
   - Check that dominance proof independently, step by step.
   - Then find a cycle source for the odd component, and give its D₀ and C₄.
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

## The attached files

- `HODGE_DIVISION_ATTACK_20261121.md`, `HODGE_DIVISION_ATTACK_20261121_CHECK_EVENTS.tsv` and `division_attack_scripts/`:
  the attack this prompt continues.
- `RETURN_<RUN>_*/` for GHOSTS, HECKE_DIV, DEG_L, THETA3, JAC1964 and SIGN_NEXT: each run's paper and registers.
- `INTAKE_*`: our intakes of these runs, with their check events.
- `PREVIOUS_PROMPT_39.md` and its attachments (the GHOSTS prompt as sent, with its sources).
- `Schoen_1988_Hodge_classes_on_self-products_Compositio_65.pdf` (Compositio Math. 65 (1988) 3-32, from Numdam).
- `032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf`, the van Hoften-Sempliner deposit
  (Hexagon 2610.00259) and Milne's report (Hexagon 2611.00244).

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: a uniform bound for the detector degree δ_W of Weil classes on a Zariski-dense set of each Weil family, in the order of the targets above: Q(i) with n = 2, then n = 3, then n = 4 through G₃₄-covers, then n ≥ 5 through G(d,e,m). Give it most of the time.
When one approach stalls, take the next one. Deliver nothing while an item is undecided and an untried approach
remains. A gap in a proof is an undecided step: attack it, never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the strongest
proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less. Cited statements you use get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with
who, how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `HODGE_DIVISION_checkpoint_<NN>.zip` with `NN` counting up.
Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every deliverable written so far
and everything that documents the work, so that a new session can continue from it and the attached files. It is never
a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `HODGE_DIVISION_final.zip`, holding:
1. **The paper**, `HODGE_DIVISION.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change: for our programme on Grothendieck's work (cote and scan),
   for our runs' open rows (run and statement id), and for the open conjectures named in the task.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
