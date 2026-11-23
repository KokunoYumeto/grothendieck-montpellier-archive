**The attached files.** Besides this file there is one ZIP, `46b_HODGE_DIVISION_FOLLOWUP_1_DEG_L_open_rows.zip`. Unpack it once: it holds every file named below. Each folder named below is already unpacked inside, so there is nothing more to unpack.

# HODGE_DIVISION, follow-up 1: the four open rows of DEG_L, the run on Hodge degrees as L-values (22 Nov 2026)

This message adds to your task. Everything in the first message stands: the main question, the rule on finishing, the
reviews against the dated ledger, the checkpoint ZIPs and CHECK_EVENTS.tsv. Fold what follows into the work in progress;
do not restart it. Record the additions in the same ledger, and include them from your next checkpoint on.

## Added sources (in the attached ZIP)

- `DEG_L_checkpoint_06/`: the final return of DEG_L (prompt 41, "the degrees of the 032 cycles as L-values (Rallis), and the
  semiregularity of the 032 surface"), by GPT-6 Astra (ChatGPT Pro mode), 21 Nov 2026: its paper `DEG_L.tex`, `QUESTIONS.tsv` (72 proved,
  41 refuted, 4 open), `LEDGER.md`, `CHECK_EVENTS.tsv`.
- `OURS_INTAKE_DEG_L_part1.md`, `OURS_INTAKE_DEG_L_part2.md`: our intakes. Checked in full by us: T6.1-T6.3, T6.14, B1, B19 (all five
  parts), S-01, S-05, S-06. The rest, including T6.25, B22a and S-14-S-41, at statement level.

## What DEG_L settled, to cite and not re-derive

- **T6:** the degree of the 032 surface is a finite sum of Rallis L-values. T6.11 has Hecke L(3/2), bounded with no GRH by B1;
  T6.13 has standard U(2) L-values at 1. It is not one L-value, and the output class of 032, Prop. 3.1, has degree 0 (T6.2).
- **Transport:** in a fixed simple CM isogeny class, with J = [Λ : Λ⁻] the index of the largest O_E-stable sublattice, the least nonzero
  squared Hom norm has order J^{1/g}. A Weil witness of degree O(√J) and division complexity O(J) exist (B19). Every bounded-degree or
  maximal-order-source transport has degree at least c√J (B21, T6.25), and a source must grow like J^{1/4} to escape (B22a). This is
  the transport law your Theorem E uses.
- **Semiregularity:** the universal form is refuted at deep levels (S-05, S-06). S-14: one weakly G-semiregular perfect complex E₀
  on one fibre, with e^{B₀}ch(E₀) = λt + P(θ), gives bounded division on the whole family (with DER4/DER7's explicit multiplier).
  S-19-S-41 exclude named candidates. The survivors must have rank divisible by the squarefree RM radicand, and rank ≥ 4 if a
  vector bundle (S-30-S-36).

## Added items (each finishes only when proved, or refuted with the refined statement and its counterexample)

1. **Q-T7-REPLACEMENT, as your semiregular branch (Proposition O's non-curve source).** On one fibre of a Weil-type family of
   dimension 2n, n ≥ 3, construct a weakly G-semiregular perfect complex satisfying S-14's hypotheses and S-30-S-36's constraints. Or
   prove that no object meeting S-30-S-36 exists on such a fibre. Start from Markman's construction for n = 2: verify that it passes
   S-30-S-36, which it must since his theorem holds, and locate exactly which step fails at n ≥ 3.
2. **Q-T7-FIXED.** For a specified smooth surface Y ⊂ A, Schoen's Prym surfaces of your Theorem E first, prove or refute the
   conormal surjectivity of DEG_L S-02:
   H¹(A, O_A) ⊗ ∧³H⁰(Ω¹_A) → H¹(Y, N^∨ ⊗ K_Y).
   Then say what Bloch semiregularity of that surface gives for the detector δ_W along its family.
3. **Q-BOUNDS and Q-DIV against Theorem E.**
   - State and prove the exact relation between DEG_L's transport law (√J, B19-B22a, T6.25) and your target-dependent detectors.
   - On the principal component of Weil fourfolds over Q(ω), give δ_W(s_k) against J_W(s_k) along Lemma H's sequence.
   - Then decide DEG_L's open Q-BOUNDS items in the families where Proposition O allows bounded δ_W: intrinsic bounded realizations,
     nonmaximal sources, unbounded image multiplicities.
4. **In Grothendieck's terms, and our ids.** State every result also as a theorem in his frameworks: the variational Hodge conjecture
   (his "On the de Rham cohomology of algebraic varieties", 1966), semiregularity and the Hilbert and Chow schemes (FGA, Bourbaki 221),
   biextensions (SGA 7 I, VII-VIII) and Adams operations (SGA 6 V). Name the rows by our ids: DEG_L Q-BOUNDS, Q-T7-FIXED, Q-DIV and
   Q-T7-REPLACEMENT, and your own.
5. **Literature searches** for every finding you call new include Hexagon (hexagonmath.org) as well as arXiv and the journals.

**Check events.** For every statement, record its check events in CHECK_EVENTS.tsv: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This holds for DEG_L's rows as you take them up, under their DEG_L ids.

## Checkpoints, as in the first message

Keep saving a checkpoint ZIP in the execution environment once every 45 minutes of work, each under a new name,
`HODGE_DIVISION_checkpoint_<NN>.zip` with `NN` counting up from your last one. Never overwrite, rename or delete an earlier
checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other
time. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work; it is
never a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.
