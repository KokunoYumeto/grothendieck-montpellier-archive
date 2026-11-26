# Intake of ALP_MACHINE checkpoint 59, by diff from checkpoint 55

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026, ~23 UTC, under
`INTAKE_WAVE_20261123_EVENING.md`.

- **Return:** `research_returns\ALP_MACHINE_checkpoint_59_20261123T1805Z_unzipped\ALP_MACHINE\` (18:05 UTC; newest filed
  when I finished).
- **Which run:** the ledger opens "Run opened 2026-11-21 19:35:32 UTC". This continues the 19:35 run of prompt 49
  (ids ALP-LIFT, AM-K, AM-R, AM-DO), not the 20:03 run of the phase lemmas AM-S1–S4. The model is GPT-6 Astra (ChatGPT
  Pro mode). Reviews 42–44 record movement.
- **Check events:** `INTAKE_ALP_MACHINE_20261123_cp59_CHECK_EVENTS.tsv`.
- **Integration:** rows appended to `INTEGRATION_ALP_MACHINE_20261123.tsv`.
- **Primer:** updated in place; the old version is backed up.

## 0. Scope

**Read:**
- the register diff, 440 rows against 422: 18 new, all PROVED_IN_STATED_SCOPE, no state changes;
- the 18 rows in full, up to 650 characters;
- the ledger headings of reviews 42–44;
- **LIFT112** (`agents\exact_normalized_coefficient_degree.md`) §§1–2.

**Not read:** the other proofs, and the scripts. **49b:** still not taken up; no ledger entry or row through
checkpoint 59.

## 1. Verdicts

| Type | Findings |
|---|---|
| Targeted proof check | LIFT112 Theorem B (§2) |
| Carried as background (statement level) | LIFT112 A and C, LIFT111, 113–116, R104–105, DO131–136, K124–127 |
| Refuted | none |

**Main questions:** Q1, Q2 OPEN (only their gate texts changed), Q3 OPEN, Q4 PARTLY_PROVED, Q5 PROVED_IN_STATED_SCOPE.

## 2. What is new, usefulness first

1. **The exact coefficient-field degree for Alpöge's normalized ideal law (LIFT112, with LIFT113).**
   - *Good for:* it completes the LIFT110 obstruction into an if-and-only-if on degrees. A literal instance of step 8
     needs a coefficient field F with h_K | [F : F ∩ K^ab]. Such a field exists: B(α_i), with α_i^{h_i} = γ_i the
     roots of the class generators, is CM, has degree exactly h_K over B, and its Galois closure with μ_e is
     metabelian (LIFT113).
   - *For whom:* a formalizer of Alpöge's step 8, or anyone writing the interface note.
   - *Checked:* Theorem B. Over A = B(μ_e), the classes of b_i = γ_i^{e/h_i} in A^×/A^{×e} are independent, because a
     relation gives a normalized generator of some J in the abelian A/K. Then [J]² = 1 by LIFT110, and [J] = 1 since
     G has odd order. Kummer theory then gives degree g.
2. **Cost of the new field (LIFT111).** rd(F_+) ≤ g³ rd(F_0). Reconstruction of the formal datum after a change of
   integral coefficient ring (LIFT114–116, R104), with explicit lattice and slope costs. One obstruction to a scalar
   repair (R105: the fixed-input error law survives only when c = 1). *Good for:* the same formalizer; these are the
   interface's bookkeeping. Statement level.
3. **The finite signed gate.** Support 28 is exhausted, with a second nonnegative completion P28 (DO133, DO135). The
   gate is Re Σ_{support ≥ 29} w(h) > −1 + 2^{−230}. Bookkeeping only. Statement level.

## 3. Scope of the inputs

- **LIFT112 §2:** uses LIFT110 (checked by me at checkpoint 55) and Kummer theory (Milne, *Fields and Galois theory*,
  Th. 5.30; standard).
- **Not used:** Masullo; any unrefereed input.

## 4. Integration (applied; rows appended)

- `reports_20261122\paper_seeds\SEED_ALP_MACHINE.md`: a checkpoint-59 bullet with LIFT112/113 and the gate.
- `PRIMER_ALP_MACHINE_20261123.md`: updated to checkpoint 59 in place. The old copy is
  `integration_backups\20261123\ALP_MACHINE\PRIMER_ALP_MACHINE_20261123_before_cp59.md`.

## 5. Prompt updates, for the main session

**Prompt 97 (MOONSHINE_AFTER_ALPOGE).**
- The phase lemmas S1–S4 it carries are from the 20:03 run and are unchanged by checkpoint 59. S3 remains the right
  test for an order-3 operator: a bound on Tr((sF)^{3n}) bounds the eigenvalues only if s commutes with F on an actual
  module.
- *Edit:* where 97 quotes the primer's §3, add one sentence:

  > The coefficient-field constraints LIFT110–113 are vacuous over K = Q(ω). That field has class number one, and its
  > roots of unity are μ₆, so LIFT110's hypothesis μ(K) = {±1} fails and the class group is trivial. They give no
  > obstruction to the sixfold-cover route.

- Nothing in checkpoint 59 bears on the Grössencharacters of 36a1, 27a or ψ³.

**Prompt 69 (BEYOND_DIRICHLET, the cubic rung).**
- *Edit:*

  > ALP_MACHINE Q3 (RH for the Kummer Hecke L-function over Q(ω)) is unchanged since checkpoint 48. Its gate remains an
  > arithmetic comparison to the ray-theta Mellin period of K021, the prime-norm and conductor costs, and an
  > every-ε window. Checkpoint 59 adds no input to the cubic rung.

**Prompt 49 (ALP_MACHINE itself).** 49b has not been taken up through checkpoint 59. Resend it at a turn boundary, or
fold it into the finishing prompt, with LIFT110–113 added to "where you are": the coefficient field must be
metabelian, of relative degree h_K.

## 6. Hexagon readiness

| Candidate | Gate left |
|---|---|
| LIFT110 + LIFT112 + LIFT113, as one section of the chain-length note: the exact coefficient-field degree for normalized ideal generators | a literature search for these statements (normalized generators of principal ideals, Kummer theory over abelian extensions of imaginary quadratic fields); a read of LIFT107–109 and LIFT113; LIFT112 Theorems A and C |

## 7. Board candidate (row for `field_experts/hexagon/HEXAGON_BOARD.tsv`, for the main session)

| Title | Statement | What it adds | Gate left |
|---|---|---|---|
| Normalized generators of class-group ideals need metabelian fields of exact degree | K imaginary quadratic with μ(K) = {±1}, G ⊂ Cl(K) odd of order g. A field F in which every J ∈ G has a generator ξ with \|σξ\|² = N J for all σ satisfies g \| [F : F ∩ K^ab]. Over any abelian B the root field B(γ_i^{1/h_i}) attains g exactly; it is CM, with metabelian Galois closure | turns the LIFT110 obstruction into an exact degree, and gives Alpöge's formal interface its minimal coefficient field | literature search; LIFT112 A/C and LIFT113 proof reads |

## 8. For the P vs NP fleet

No result of checkpoint 59 bears on complexity. There is no map to construct beyond the one in the checkpoint-55
intake (AM-S4 → L-gct-011).
