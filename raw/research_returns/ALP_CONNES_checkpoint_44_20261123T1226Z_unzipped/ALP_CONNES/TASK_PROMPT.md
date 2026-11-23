**The attached files.** Besides this file there is one ZIP, `ALP_CONNES_Alp_ge_s_theorem_pushed_through_Connes_s_programm.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Borger_deSmit_Galois_Lambda_rings.zip` is the folder `LIT_Borger_deSmit_Galois_Lambda_rings/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# ALP_CONNES: Alpöge's theorem pushed through Connes's programme, and the next rung over Q(ω)

Alpöge's theorem (A) makes the Riemann hypothesis for ζ and for every Dirichlet L-function a theorem. Connes's
programme, alone and with Consani, Marcolli and Moscovici, has for twenty-five years built structures whose central
statements are equivalent to, or conditional on, exactly these hypotheses, or are stated as steps towards them. Nobody
has yet pushed A through that programme. Do it: take A as given and derive, with proofs, everything it makes true,
everything it makes constructible, and everything it forces, in each part of the programme; then take the programme one
rung up, to the field Q(ω), where A stops and where Alpöge's own method already lives.

## Where it stands

**A (Alpöge, Lean, 20 Nov 2026; cite as a theorem).** RH for ζ; no zero of any Dirichlet L-function L(s, χ) with
Re s > 1/2; all nontrivial zeros of primitive L(s, χ) on Re s = 1/2. Our map of the Lean archive is attached. The
number-field proof runs through theta lifts between definite unitary groups over CM fields and a Landau window theorem
(a one-sided bound on windows excludes zeros to the right); the function-field form of its sign mechanism is our H01
paper (attached): one global sign (−1)^{D−1} makes the remainder of a point count an honest trace. Alpöge's note describes
the family averaging through normalized Gauss sums of order #μ_K on the #μ_K-fold metaplectic cover, the CM curve
C/Z[ω], a sixfold cover of GL₅ and a (2, 3, 6)-triangle group trick: for Q(ω) the phase group is μ₆.

**What we found on 21-22 Nov (attached: OURS_ALPOGE_THROUGH_CONNES_CONSANI_20261122.md, a first pass; statements there
marked [std] were taken from search summaries where so marked and must be verified against the papers).**
1. A is Weil positivity on the whole idele class group C_Q = Ẑ^× × R₊^* (every Grössencharacter of Q is a Dirichlet
   character times |·|^{it}).
2. A gives Connes's global trace formula for Q in the form he states it. Checked in the attached source: his Theorem 5
   (§VIII) is stated and proved for global fields of positive characteristic (cut-off trace formula ⟺ RH for all
   Grössencharakter L-functions, through positivity of the Weil distribution); for number fields the end of §VIII gives
   "the analogue of Lemma 1, Theorem 5, and Lemma 3" for the Riemann zeta function (even functions, ψ ↦ ψ ⊗ 1_R), and
   the introduction states the equivalence for all Grössencharakter L-functions. Write the number-field equivalence out
   in full, for every character of Ẑ^× (every Dirichlet L-function), prove it, and state exactly what A then gives for
   the spectral realization.
3. A is RH for every number field that descends to F₁ in Borger's sense: by Borger-de Smit (attached) a Λ-ring finite
   étale over Q with an integral model lies in a product of cyclotomic fields; conversely A follows from RH for all
   ζ_{Q(μ_n)}. The boundary of A is the boundary of this descent: Alpöge's analytic interface supplies its window bound
   only for characters whose field embeds in a cyclotomic field, and our run ALP_MACHINE (attached, prompt 49) proves
   that the cubic Kummer field Q(ω, ∛p) lies in no cyclotomic and no CM field (AM-H03), while the analytic half of
   Alpöge's chain transfers to L_K(s, χ_{p,3}) = ζ_{Q(∛p)}(s)/ζ(s) (AM-H04); its gate is the arithmetic window bound
   H04.4.
4. Over K = Q(ω) the Kummer field is abelian, so it descends to "F₁ over Z[ω]" (Borger-de Smit's ray-class Λ-structures,
   attached); the Bost-Connes system of a number field (Laca-Larsen-Neshveyev; arithmetic models through Λ-rings,
   Yalkinoglu, both attached) is the Connes-side home of that rung.
5. A phase can replace Alpöge's sign only if it commutes with Frobenius, never as a reflection (ALP_MACHINE AM-S1-S3,
   intake-confirmed): a cubic version needs μ₃ acting by automorphisms, as on varieties with CM by Z[ω].
6. Our split-zero and counting constructions in Connes-Consani's F_{1²} terms (attached): the global zetas of
   sign-twisted Tate counts are Π ζ(s − j)^{a⁺} L(s − j, χ₋₄)^{a⁻}, all pure by A.

## The task

Work through every part of the programme listed here, with the attached LaTeX. For each part: state its central
statements that were conjectural, conditional on RH or GRH, or proved only in a restricted range; decide which A now
proves, and prove it; decide which A does not reach, and prove the precise reason (a counterexample, or the exact further
input needed); and give each construction A makes possible, built.
1. Connes's 1999 global trace formula and spectral realization (math/9811068), and the Connes-Consani-Marcolli
   reformulation of Weil's proof on the adele class space (math/0703392).
2. Weil positivity on windows: Connes-Consani's positivity at the archimedean place (2006.13771), and for every window
   [λ^{-1}, λ] the semilocal statement in which only the prime powers p^k ≤ λ² enter; what A gives for each window and
   what the semilocal operators (compressions of the scaling action) then satisfy.
3. ζ-cycles and spectral triples (2106.01715, 2207.10419) and the zeta spectral triples (2511.22755): with A, are the
   convergence statements these papers observe numerically now provable, and in what form?
4. The prolate wave operator and the semilocal prolate operator (2310.18423): with A, what is true of its spectrum.
5. The arithmetic and scaling sites (1603.03191, 1805.10501) and Riemann-Roch for Spec Z (2205.01391, 2306.00456): A
   gives the inequality a Hodge index theorem on the square would give; which statements of the Riemann-Roch strategy
   become theorems, and which construction of the square and its intersection pairing is now forced or excluded.
6. The absolute twistor line and F_{1²} (2609.00299), absolute cyclotomy (2112.08820), and the split-zero and
   counting constructions (attached notes).
7. The next rung: Connes's global trace formula for K = Q(ω), equivalent to RH for every Grössencharacter of Q(ω), of
   finite order (the cubic and sextic residue characters, starting with χ_{p,3}) and of infinite order (the Hecke
   characters of the curves with CM by Z[ω], such as x³ + y³ = 1). Determine what A together with the Q(ω) structures
   (the Bost-Connes system of Q(ω), its Λ_{Z[ω]}-model, Alpöge's chain over CM fields, μ₃ acting by commuting
   automorphisms) proves, and attack the cubic Kummer case to the end: H04.4 for χ_{p,3}, in ALP_MACHINE's notation, using
   its newest checkpoint (attached) as the starting point, not repeating its proved steps.

## The attached files

- `ALPOGE_remark.pdf`: A: Alpöge's note (public), with the timeline of his method
- `OURS_ALPOGE_LEAN_MAP_20261120.md`: our map of Alpöge's Lean archive: the proof chain, the window theorem, the CM-field automorphic end
- `OURS_H01_deligne_sign_only_v5.tex`: our H01 paper (hexagon:2611.00789): the sign-only mechanism written out over finite fields
- `OURS_ALPOGE_THROUGH_CONNES_CONSANI_20261122.md`: our first pass of this task (verify its [std] citations)
- `OURS_SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md`: the split zero and the counting construction in Connes-Consani's F_{1^2} terms (sections 1-15)
- `OURS_RESEARCH_NOTE_COUNTING_WITH_THE_BASEPOINT_20261121.md`: our research note: counting with the basepoint, sign-twisted Tate counts, the ladder
- `OURS_SHAPES_CHECKED_AND_INTAKE_20261121.md`: the phase programme checked: commuting C6 against reflected D3, the cubic Kummer case, A4
- `OURS_ES_AND_THE_RIEMANN_HYPOTHESES_20261121.md`: the Erdős-Straus bridge: the archimedean sign of a shell motive (a reflected coupling)
- `RETURN_ALP_MACHINE_checkpoint_04_20261121T2304Z/`: prompt 49's run (newest checkpoint): Alpöge's chain carried to the cubic Kummer character; AM-H01-H19, AM-S1-S4 (1478 files: the run's paper, registers, scripts and certificates)
- `RETURN_MAS_ARTIN_checkpoint_10_20261121T2301Z/`: prompt 48's run (newest checkpoint): the same cubic case psi_{269,3}; MA-FT-002 (RH for a sector iff delta^+ = 0) (679 files: the run's paper, registers, scripts and certificates)
- `OURS_INTAKE_ALP_MACHINE_20261121_hecke.md`: our intake of ALP_MACHINE's Hecke part, with its check events
- `OURS_INTAKE_ALP_MACHINE_20261121_lifts.md`: our intake of ALP_MACHINE's lifts, seesaw and sign parts, with its check events
- `OURS_INTAKE_MAS_ARTIN_20261121_part2.md`: our intake of MAS_ARTIN cp10, with its check events
- `LIT_Connes_1999_trace_formula_zeros/` (arXiv:math/9811068, LaTeX source): Connes 1999: the trace formula on the adele class space; global trace formula equivalent to RH for Grössencharacter L-functions
- `LIT_CCM_Weil_proof_adele_class_space/` (arXiv:math/0703392, LaTeX source): Connes-Consani-Marcolli: the Weil proof and the geometry of the adele class space
- `LIT_CC_Weil_positivity_archimedean/` (arXiv:2006.13771, LaTeX source): Connes-Consani: Weil positivity and trace formula, the archimedean place
- `LIT_CC_spectral_triples_zeta_cycles/` (arXiv:2106.01715, LaTeX source): Connes-Consani: spectral triples and zeta-cycles
- `LIT_CC_Hochschild_trace_zeta_cycles/` (arXiv:2207.10419, LaTeX source): Connes-Consani: Hochschild homology, trace map and zeta-cycles
- `LIT_CCM_zeta_spectral_triples/` (arXiv:2511.22755, LaTeX source): Connes-Consani-Moscovici: zeta spectral triples
- `LIT_CCM_zeta_zeros_prolate/` (arXiv:2310.18423, LaTeX source): Connes-Consani-Moscovici: zeta zeros and prolate wave operators
- `LIT_CC_geometry_scaling_site/` (arXiv:1603.03191, LaTeX source): Connes-Consani: geometry of the scaling site
- `LIT_CC_Riemann_Roch_strategy/` (arXiv:1805.10501, LaTeX source): Connes-Consani: the Riemann-Roch strategy (complex lift of the scaling site)
- `LIT_CC_Riemann_Roch_SpecZbar/` (arXiv:2205.01391, LaTeX source): Connes-Consani: Riemann-Roch for the Arakelov compactification of Spec Z
- `LIT_CC_Riemann_Roch_ring_Z/` (arXiv:2306.00456, LaTeX source): Connes-Consani: Riemann-Roch for the ring Z
- `LIT_CC_BC_absolute_cyclotomy/` (arXiv:2112.08820, LaTeX source): Connes-Consani: BC-system, absolute cyclotomy and the quantized calculus
- `LIT_CC_absolute_twistor_line/` (arXiv:2609.00299, LaTeX source): Connes-Consani: the absolute twistor line and the geometry of Spec Z-bar (F_{1^2}, the Gaussian avatar)
- `LIT_Borger_deSmit_Galois_Lambda_rings/` (arXiv:0801.2352, LaTeX source): Borger-de Smit: Galois theory and integral models of Lambda-rings (cyclotomic containment)
- `LIT_Borger_deSmit_Lambda_rings_of_integers/` (arXiv:1105.4662, LaTeX source): Borger-de Smit: Lambda actions of rings of integers (ray class / Deligne-Ribet monoid over K)
- `LIT_Yalkinoglu_BC_arithmetic_models/` (arXiv:1105.5022, LaTeX source): Yalkinoglu (appendix by Neshveyev): arithmetic models and functoriality of Bost-Connes systems via Lambda-rings
- `LIT_LLN_BC_systems_number_fields/` (arXiv:0710.3452, LaTeX source): Laca-Larsen-Neshveyev: Bost-Connes type systems for number fields

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: Derive, with complete proofs, every consequence of A in Connes's and Connes-Consani's programme (parts 1-6 of the task), and prove RH for the cubic Kummer characters of Q(ω), L_K(s, χ_{p,3}) = ζ_{Q(∛p)}(s)/ζ(s), by carrying Alpöge's window from the cyclotomic host to the ray-class host over Z[ω] through the structures that A and the programme supply (part 7). Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `ALP_CONNES_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `ALP_CONNES_final.zip`, holding:
1. **The paper**, `ALP_CONNES.tex`, in LaTeX:
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
