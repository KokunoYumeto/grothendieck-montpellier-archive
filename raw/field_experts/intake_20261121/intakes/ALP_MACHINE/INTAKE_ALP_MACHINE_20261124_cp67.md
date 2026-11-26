# Intake of ALP_MACHINE checkpoint 67, by diff from checkpoint 59

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 24 Nov 2026, under `INTAKE_WAVE_20261123_EVENING.md`.

- **Return:** `research_returns\ALP_MACHINE_checkpoint_67_20261124T0108Z_unzipped\ALP_MACHINE\` (01:08 UTC; newest filed).
- **Which run:** the ledger opens "Run opened 2026-11-21 19:35:32 UTC". This is the 19:35 run of prompt 49, as at
  checkpoints 23–59. The model is GPT-6 Astra (ChatGPT Pro mode). Reviews 45–50 all record movement.
- **Check events:** `INTAKE_ALP_MACHINE_20261124_cp67_CHECK_EVENTS.tsv`.
- **Integration:** rows appended to `INTEGRATION_ALP_MACHINE_20261123.tsv`.
- **Primer:** updated in place; the old version is
  `integration_backups\20261123\ALP_MACHINE\PRIMER_ALP_MACHINE_20261123_before_cp67.md`.

## 0. Scope

- **Read:**
  - the register diff, 463 rows against 440: 23 new, 22 proved in stated scope and 1 refuted (R109). No state changes
    of old rows;
  - all 23 rows, and LIFT117, LIFT118, R110 and LIFT120 in full;
  - review 50.
- **Not read:** every proof file and every script.
- **49b:** still not taken up; no ledger entry or row through checkpoint 67.

## 1. Verdicts

| Type | Findings |
|---|---|
| Computation (mine) | the LIFT118 affordability inequality, from its row |
| Carried as background | the other 22 findings |
| Refuted by the run itself | R109, a duplicate of R106 and K127 (I checked that its targets coincide with theirs) |
| Refuted by me | none |

**Main questions:** Q1, Q2 OPEN (only their gate texts changed), Q3 OPEN, Q4 PARTLY_PROVED, Q5 PROVED_IN_STATED_SCOPE.

## 2. What is new, usefulness first

1. **The formal family can be carried over to the new coefficient ring (R110, LIFT117–120, R108). This moves AM112.**
   - LIFT112–113 found the minimal coefficient field: metabelian, CM, of relative degree h_K.
   - Checkpoint 67 shows that a supplied complete formal family (FamP) can be rebuilt over the ring of integers of a
     fixed ambient field LL, with every constant, gain and quantifier unchanged and height change zero (R110),
     given stability and rational projection on all tuples. LIFT120 shows that the run's actual row construction
     supplies those premises.
   - The reconstruction cost is a row-height shift 0 ≤ Δ ≤ 2 log c₀ (LIFT117). It is affordable inside SizesAt
     (LIFT118): 2 log c₀ ≤ 32 x^{11+726ε/25} < 32 x^{12} ≤ exp(x^ε) once x ≥ max(2, 32 q!), q = ⌈13/ε⌉.
   - *Rechecked by me:* the exponent is 11 + 363/650 < 12, and exp(x^ε) ≥ x^{εq}/q! ≥ x^{13}/q! ≥ 32 x^{12}.
   - *Good for:* a formalizer of step 8. The coefficient-field constraint of LIFT110–113 does not break the rest of
     the interface. What is still missing is an initial family: a literal source, host and sizes. That is not
     constructed.
2. **The finite signed gate.** Supports 29 and 30 are exhausted through four more nonnegative completions; the open
   inequality is now at support ≥ 31 (DO143). Bookkeeping only.
3. **R109** is an honest self-correction by the run: it withdrew a proposed charge that duplicated R106 and K127.

## 3. Prompt updates, for the main session

- **97 (MOONSHINE_AFTER_ALPOGE):** no change from checkpoint 67. S1–S4 (from the 20:03 run) and the LIFT110–113
  statements cited there stand. LIFT110–113 remain vacuous over Q(ω). The new transport results concern Alpöge's
  formal family over prime-discriminant quadratic hosts and do not touch the Grössencharacters of 36a1, 27a or ψ³.
- **69 (BEYOND_DIRICHLET, the cubic rung):** no change. ALP_MACHINE Q3 is unchanged since checkpoint 48.
- **49 (ALP_MACHINE):** 49b has still not been taken up after 26 hours. In the finishing prompt's "where you are",
  add: "LIFT110–113 fix the coefficient field (metabelian, CM, relative degree h_K), and R110 and LIFT117–120 carry a
  supplied family over it; what is missing is the initial family."

## 4. Board

- **AM112** (LIFT110 + LIFT112 + LIFT113): moved. Add to the row's "what it adds": "and a supplied formal family can be
  rebuilt over this field with all constants unchanged (R110, LIFT120)".
- The gate is unchanged: a literature search, and reads of LIFT112 Theorems A and C and of LIFT113. Transport is a
  conditional interface result, not a new theorem for the note.

## 5. For the P vs NP fleet

Nothing in checkpoint 67 bears on complexity.
