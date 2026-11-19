# Brief: A1 after the full audit, the second reading (17 Nov 2026)

From the main session (Claude Opus 5.5 at effort max) to the A1 expert ab3f12f2 (Claude Fable 5.2 at effort max), who
did the first check (`pro_intake_20261116/EXPERT_A1_ANABELIAN_20261117.md`). The user asked for the returns of
17 Nov to be taken in. This one has the most riding on it.

- Effort: max (your own setting).
- Sub-agents allowed: 0.
- Compute bound: about 250k tokens.
- This account is near its weekly limit. Write your note as you go, after each step. If you are stopped, you will be
  resumed on the fresh account.
- If your context is compacted, the summary is not reliable. Reread this brief, your first check and your note so
  far, then continue.

## The return

03_ANABELIAN_A1 ran on your K-items. Its last checkpoint, 03, is its final; the session crashed after that.
Folder: `longue_marche_pro_pilot_20261104/answers/ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped/ANABELIAN_A1/`.
It holds `ANABELIAN_A1_report.md`, `ANABELIAN_A1_results.csv` (121 statements), `sections/`, `notes/`, `code/` and a
paper, `ANABELIAN_A1_paper.tex`.

Its claims:
- **A.1:** the universal geometrically prime-to-p point-section theorem for every smooth proper curve of genus >= 2 over
  every finite field, after every finite constant extension.
- K1-K6 are proved.
- A **second "support-field" proof** removes the finite-exception input (Saïdi-Tamagawa 2009, Prop. 1.8 (vi)) from the
  final contradiction.
- The theorem extends to hyperbolic curves over fields finitely generated over a finite field (A.33).

## The task, in this order

1. **The main chain, which you had read only a third of:** AG.39, the end of AG.41, AG.42, and AR.8-AR.9, in the
   form the audit now gives them. For each step: sound, or the exact gap.
2. **The second support-field proof:** is it complete without Saïdi-Tamagawa's finiteness?
3. **K1-K6:** check that each proof proves the K-item as you posed it.
4. **A.33** (the extension) and **B7** (the henselian counterexample): at the level of sense.
5. **Your verdict:** does A.1 stand as stated, on what you read? List what you did not read. Name what a second
   reader must still check before anything public.

## Write

`pro_intake_20261117/EXPERT_A1_SECOND_READING_20261117.md`, written as you go. Your final message is the verdict, in a
few lines.
