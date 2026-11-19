# Sub-agent "delta": the character Δ on GT̂, across every run (brief, 18 Nov 2026)

You are Claude Opus 5.5 at effort max, sweep 2, sub-agent delta. Read
`<local>/Documents\results_register\sweep2_global\COMMON_BRIEF_FOR_SUBAGENTS.md` first. Your folder:
`<local>/Documents\results_register\sweep2_global\sub_delta\`.

## Why you

The main question of the Longue Marche line, E.3 of the programme map, is whether the CM parity character Δ vanishes
on GT̂ (`LM7_PUSH:E.3`, Open in its run; `LM7_PUSH:E.65` defines Δ). Six runs in two sweep-1 scopes work on it, and the
two sweep-1 agents each saw half:
- sweep1_tower (SUMMARY §3, CORRECTIONS 1-4): EXIT_TOWER E.49 claims Δ|GT̂ = 0 from E.44 (𝒥(A) = A for every A ∈ GT̂,
  through Boggi–Zalesskii Theorem A(iii) for C₂²); GT_TOWER_CHECK A.1 confirms E.44, A.3 repairs E.49's label
  comparisons, A.7 gives Δ|GT̂ = 0 for every multiplier; DELTA_ON_GT A.84 keeps it open with the reduction
  A.112/A.103/A.87; LM8_PUSH C.21 shows E.3 is exactly Δ|GT̂ ≠ 0; "everything rests on 𝒥(A) = A". It also found two
  markings of C^φ (C_L and C_P) and a notation clash (Δ also means Gal(K̄/K^ab) in LM8_PUSH).
- sweep1_sections (SUMMARY point 4): SECTION_GHOSTS E.191 proves Δ|GT̂ = 0 "for the character of GT_TOWER_CHECK A.7",
  E.198 gives GT̂ ⊊ ker Δ ⊊ GT̂₀ with a witness, and E.201 suggests this is the same parity as LM7_PUSH E.3/E.65; it
  read statements only.

No one has put these together. You do.

## What to do

1. **One Δ or several.** For every run that names Δ (start from `sub_delta/INPUT_delta_rows.tsv`, 116 rows, and add all
   of DELTA_ON_GT, whose register statements are short titles), write down its definition of Δ with the locator: the
   group it is defined on (GT̂₀, the multiplier-one subgroup, GT̂), the frames and markings, the normalization
   (ε₃(T) + ε₂(W), CM pair (T₄, W₃)), and what "GT̂" and "GT̂₀" mean there. Decide, as mathematics, whether they are the
   same character, and where they differ, how they compare. Do the same for C^φ, C_L, C_P and the descent map D (and
   D_P).
2. **Every claim that Δ|GT̂ = 0, and its route.** At least EXIT_TOWER E.44, E.46, E.49; GT_TOWER_CHECK A.1, A.3, A.5,
   A.7, B.2.1, B.2.3, B.2.25; SECTION_GHOSTS E.191, E.198, E.201 (read them in the SECTION_GHOSTS **final** return,
   which the register does not have yet); LM8_PUSH C.8, C.19, C.21, C.23, C.24, C.30; LM4_SUCCESSOR A.13, A.105, A.111;
   DELTA_ON_GT A.84, A.87, A.103, A.112, P.11, B.15; LM7_PUSH D.50, D.52, E.58, E.61, E.64, E.65, E.67; LM4 D.32, D.34;
   FERMAT_SUCCESSOR C.15; CYCLOTOMIC_KERNEL E3. For each: what it proves, from which inputs (other runs' rows included),
   and whether it passes through 𝒥(A) = A or Boggi–Zalesskii. Draw the dependency chain.
3. **The gate.** Read the step that everything rests on (EXIT_TOWER E.44 and its use of Boggi–Zalesskii; GT_TOWER_CHECK
   A.1's supplement) and work it through: state Boggi–Zalesskii's theorem exactly as published (locate it: it is cited
   in the returns; give the paper, statement and page), check that its hypotheses hold as used, and that the
   conclusion transfers exactly. Say what you checked and what you did not.
4. **Independence.** Is there a route to Δ|GT̂ = 0 that does not pass through 𝒥(A) = A? Is SECTION_GHOSTS's?
5. **Consistency.** Rows that treat E.3 as open (as a hypothesis or a question) against rows that treat it as decided:
   is any proved row inconsistent with Δ|GT̂ = 0, or does any use "Δ|GT̂ ≠ 0" as if true? The space of quadratic
   characters vanishing on GT̂ (LM8_PUSH C.30, GT_TOWER_CHECK B.2.25): the same space? Which run had it first (dates
   from the returns)? What does Δ|GT̂ = 0 decide downstream (LM7_PUSH E.3, FERMAT_SUCCESSOR C.15, LM4_SUCCESSOR A.13,
   LM8_PUSH C.8 for C_L, GT_TOWER_CHECK B.1 for C_P)?
6. **The canonical items.** Write the cluster as the handbook should hold it: the definition of Δ (one notation), the
   theorem Δ|GT̂ = 0 with its hypotheses and its proof route, the strict inclusions, the open questions that remain
   (with their strongest proved reductions), and the status line with what is checked and by whom.

Write FINDINGS.tsv, CLUSTERS.tsv, CHECK_EVENTS.tsv and REPORT.md as the common brief says. The REPORT's first
paragraph answers, in plain words: is Δ|GT̂ = 0 proved, on what, and checked by whom.
