# Intake of ALP_CONNES checkpoint 44 (prompt 55, follow-up 55b), by diff from checkpoint 41

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent afa2696b67cad55de, a copy of af2a18f62da23b48e). The run
is GPT-6 Astra (ChatGPT Pro mode). Checkpoint 44 is the newest filed. Brief:
`field_experts/intake_20261121/INTAKE_WAVE_20261123_EVENING.md`.

A is L. Alpöge's theorem (20 Nov 2026): RH for every Dirichlet L-function, ζ included. Masullo's draft is not a proof,
and nothing here rests on it.

## 0. Scope: what was read
- **Register diff, cp41 → cp44:**
  - QUESTIONS.tsv: 1042 rows in both, 0 new, 0 removed, and one row changed (EB-Q02, the main arithmetic size gate,
    now citing G220);
  - movement reviews 32-34: all "Movement: yes";
  - the main-gate table of review 34 (Q3, Q4, Q7).
- **New modules:** G209-G220.
- **Read in full:** the statement of AC-G219 and the proof, steps 1-5 (of 8).
- **Read at statement level:** G209-G218, G220, the rest of G219 (steps 6-8: all levels, original rings, family
  cost).
- **Not read:** CHECK_EVENTS row by row, `work_in_progress.tar.xz`, `input_material/`.

## 1. Verdicts
- **AC-G219, steps 1-5: confirmed by a targeted proof check, given the PARI full class-group certificate
  Cl(L) ≅ C₇², which I did not replay.**
  - L = Q(ω, ∛269) has the defining polynomial (MRT.9), which I recomputed as the resultant of X − t − ω.
  - 7 splits in K with generators 2 − ω and 2 − ω², of norm 7. 269 ≡ 3 mod 7 is a noncube (the cubes mod 7 are
    0, ±1), so L/K is inert at both places over 7.
  - The two χ-eigenspaces of C ⊗ F₇ are lines, exchanged by τ.
  - The untwisted strict group is O/7O (MRT.14).
  - When 7 | e, (1+7x)⁷ ≡ 1 mod 49 gives D[49] = D⁰[49], so S₇ = O/7O exactly.
  - The lifting problem to Z/49 is an affine equation [B₀] + u[C_aff] = 0 with [B₀] ≠ 0. So at most one residue
    u = e mod 7 lifts. That is 𝓔, with |𝓔| ≤ 1.
- **G209-G218, G220:** not checked by us. They are carried with the run's own author and reviewer checks (by GPT-6
  Astra, ChatGPT Pro mode).
- No refutation.

## 2. What is new, usefulness first
- **The cubic gate's budget (Q7 / EB-Q02).** G219 is the first exact nonvanishing result in the budget.
  - Statement: at coefficient 7, for the matched mixed family (χ^j ξ₇^a c₇^{−e} with residual trivial), the strict
    group is O/7^{s(e)}O, with s(e) ≥ 1, for both cubic labels.
  - Most of it is pinned down: s(e) = 1 when 7 | e, and the weights with s(e) ≥ n lie in at most one residue class
    mod 7^{n−1}.
  - Hence Σ_{e≠e*} s(e) ≤ (N−1) + v₇((N−1)!).
  - G220 replaces the full sum by a maximum over one retained weight pair. The cost is ≤ (7/3)(N−1) log 7 < 7P, and
    the remainder is strictly smaller for T ≥ 3.
  - What it is good for: the H04.4 arithmetic budget can no longer be closed by "all strict groups vanish" at
    coefficient 7. It has to absorb an explicit, mostly bounded, nonzero contribution. This is the honest size of
    that term.
- **G209-G218:** strict vanishing at coefficient 7 for the remaining seven-factor families (cubic seven-factor, the
  quadratic cubic twists, the residual rational cubic, the split-prime and split-cube families). These close the
  coefficient-7 rows of the budget apart from the matched family.
- **Main gates** (H04.4, R_cub and cubic RH; the T51 limit without zero location; the a₂ lower bound): none moved.
  Review 34 Q3 and Q4 say "No spectral movement is assigned".
- **Connes-Consani F₁, Deninger, BC/BCM:** nothing new.

## 3. Scope of the inputs
- G219 rests on PARI 2.19's full certification `bnfcertify(B,0)` of Cl(L) ≅ C₇² (a software certificate, run
  10:58 UTC on 23 Nov), and on finite-coefficient Galois cohomology.
- It does not use A or Masullo.
- The window statements G220 inherit the retained source inputs of the H04.4 comparison (AC-K25-K35).

## 4. Integration
Applied, with a backup in `integration_backups/20261123/ALP_CONNES/`. Log: `INTEGRATION_ALP_CONNES_20261123.tsv`.
- `reports_20261122/paper_seeds/SEED_ALP_CONNES.md`:
  - Paper 1, after "Why it matters": the H27 editor's findings, cited to their record. T51's statement is Connes's
    own; Connes 1999 proves his Theorem 5 only in positive characteristic; S50 follows from Suzuki, arXiv:2610.32704.
  - Paper 2, after its research question: the cp44 state of the cubic budget (G130-G218, G219, G220).

For the main session (shared files, not edited by me):
- The shorthand "Δ on GT̂ = χ₁₂∘u" was listed in my cp41 intake as an edit. It does not occur in `claude_math_notes/`,
  `results_register/`, `reports_20261120/`, `reports_20261123/` or the paper seeds. If it survives in the RUNBOOK or in
  memory, correct it there: Δ vanishes on GT̂, and the formula holds on the gentle group, with u the CRT representative
  taken modulo {1, 11}, not the cyclotomic character.
- The Hexagon board rows below.

## 5. Prompt updates
- Prompt 69 (BEYOND_DIRICHLET) already carries cp44, built earlier today by af2a18f6.
- Nothing newer exists. No change.

## 6. Hexagon readiness
| result | state | gate left |
|---|---|---|
| AC-G219 (coefficient-7 strict groups O/7^{s(e)}, at most one exceptional residue at each level) | steps 1-5 checked by us; class group by PARI | a replay of the class-group certificate (Cl(L) ≅ C₇²) in a second system, and a check of steps 6-8. Then a literature comparison (Iwasawa-theoretic lifting at split primes) |
| AC-G185 (cp41) | re-proved by us | not new; no post |

## 7. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`, for the main session)
| title | statement | what it adds | gate left |
|---|---|---|---|
| Strict 7-adic Selmer groups of a cubic Kummer twist family | K = Q(√−3), L = K(∛269). For χ faithful on Gal(L/K), the conductor-7 character ξ₇ and the 7-adic cyclotomic c₇, with ξ₇^a = ω₇^e: S₇(K, (E/O)(χ^j ξ₇^a c₇^{−e})) ≅ O/7^{s(e)}O, s(e) ≥ 1. s(e) = 1 if 7 \| e. The weights with s(e) ≥ n form at most one class mod 7^{n−1}. | an explicit nonzero Selmer computation in a nonabelian (S₃) family, at all weights, with a nested exceptional class | replay of the PARI certificate; check of steps 6-8; literature |

## 8. For the P vs NP fleet
No result of this checkpoint bears on complexity. The new rows are Galois-cohomological. The proof graph
(`fleet_map/PROOF_GRAPH.tsv`) has no node for class-group or Selmer certificates. The "co-level of p-units" nodes
(L-lib-142 to 145) concern sums of p-units and are not the saturation used here. No map was constructed.
