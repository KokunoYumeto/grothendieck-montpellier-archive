# Referee chunk: Δ on GT̂, both routes (18 Nov 2026)

Written by the main session (Claude Opus 5.5 Max) for one Claude Fable 5.2 at effort max, read in on this chunk only.
The user, 18 Nov 2026 ~14:4x UTC: [the user's words, omitted]; and,
on a new Fable reader for it, "do make it read in. That's good."

## The question
Our runs, all by GPT-6 Astra (ChatGPT Pro mode), claim Δ|GT̂ = 0 and GT̂ ⊊ ker Δ ⊊ GT̂₀. Sweep 2 (Claude Opus 5.5 at
effort max) found that every run uses the same character, that of LM7_PUSH E.65, and that there are two routes. You are
the referee from another model family, and you check against the field.

1. **Route 2:** SECTION_GHOSTS E.176–E.191 (final return of 18 Nov). Its gate, E.179–E.181, claims that every normalized
   element of GT̂ satisfies relation (IV) of Nakamura–Schneps 2000, and so lies in the group Λ of Hatcher–Lochak–Schneps
   2000. Those papers left this open.
   - Is the argument of E.176–E.191 correct, step by step?
   - What exactly do Nakamura–Schneps 2000, Hatcher–Lochak–Schneps 2000 and Lochak–Nakamura–Schneps 2026
     (arXiv:2602.12462) prove and leave open about (IV), Λ and GT̂?
   - Does LNS 2026 settle, use or contradict the claim?

   Sweep 2 checked E.181's normalization step and found it correct.
2. **Route 1:** EXIT_TOWER E.44 → E.49 → GT_TOWER_CHECK A.1, A.3, A.7. Its gate is 𝒥(A) = A, through Boggi–Zalesskii's
   Theorem A(iii) for C₂² in Γ_{0,[10]}. On 16 Nov we wrote to Boggi and Zalesskii about one step:
   - the step: ⋂ closure(Z(x_i)) = closure(⋂ Z(x_i)), in Boggi's Prop. 2.4 and in their Thm 5.1(iii); no reply so far;
   - our note argues that the step holds for solvable groups, by their own normalizer result.
   - Check that solvable-case argument, and whether Route 1's use of Theorem A(iii) at p = 2 for C₂² needs the step.
     If it does, check whether the solvable case covers it.
   - Also check EXIT_TOWER E.28, which sweep 2 left unchecked.

For each gate, the verdict is one of: proved (you checked every step), gap (exactly where, and what would close it), or
refuted (with the counterexample). "Partly settled" is not a verdict: when a step is unclear, attack it until it is
decided, or state precisely what remains and why.

## Read (in this order; name every folder you search, no recursive search over Documents)
- `<local>/Documents\results_register\sweep2_global\CONSISTENCY.md` (the Δ part, around lines 60-100),
  `CORRECTIONS.md` (the SC01 items) and `CLUSTERS.tsv` (row SC01).
- `<local>/Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped\`:
  E.176–E.191 and what they cite.
- `...\answers\EXIT_TOWER_checkpoint_28_20261116T1443Z_unzipped\` (E.28, E.44, E.49);
  `...\answers\GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped\` (A.1, A.3, A.7);
  `...\answers\DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\` (A.84), for comparison.
- `<local>/Documents\pro_intake_20261114\NOTE_BOGGI_ZALESSKII_STEP.md` (item 3: the solvable case) and the
  e-mail as sent, `<local>/Documents\outreach_drafts\2026-11-16_boggi_zalesskii.md`.
- **The papers, as TeX wherever it exists:**
  - arXiv e-prints: https://arxiv.org/e-print/2602.12462 (LNS 2026), 2406.08639 (Boggi–Zalesskii), 2408.12486 (Boggi).
    The last two are also in the LM4 background material, under
    `longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped\`.
  - Nakamura–Schneps 2000 (Invent. Math. 141) and Hatcher–Lochak–Schneps 2000 (J. reine angew. Math. 521): find open
    copies (arXiv, the authors' pages). If you cannot open one, say so and work from what LNS 2026 states about it,
    with locators.
  - Put downloads in `<local>/Documents\results_register\delta_referee_20261118\papers\`.

## Write
Write to `<local>/Documents\results_register\delta_referee_20261118\`:
- `REFEREE_REPORT.md`: for each gate, the verdict and the argument, step by step with locators. Then what the
  literature says, with exact theorem numbers. If route 2's gate is proved, say what that means for the field (it would
  answer a question HLS and NS left open) and what a mathematician would check first.
- `CHECK_EVENTS.tsv`: one row per check, in six columns: `id, date_utc, who, how, result, where`. `who` is
  "Claude Fable 5.2 at effort max, <your agent id>, Δ referee".

If the harness refuses the report, put it in your final message.

Sub-agents allowed: 0.
Compute bound: about 200k tokens of context (the user's figure); spend it on the gates, not on surveys.
