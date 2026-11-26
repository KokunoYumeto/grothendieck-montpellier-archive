# Intake of ALP_MACHINE checkpoint 29 (run 19:35), by diff from checkpoint 25

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 22 Nov 2026, about 22 UTC.

- **Return:** `grothendieck_archive_transcription_20261110\research_returns\ALP_MACHINE_checkpoint_29_20261122T1935Z_unzipped\ALP_MACHINE\`
  (checkpoints 23–28 are retired into its `_from_earlier_checkpoints`).
- **Baseline:** `INTAKE_ALP_MACHINE_20261122_cp25.md` (the ZIP of checkpoint 25).
- **Check events:** `INTAKE_ALP_MACHINE_20261122_cp29_CHECK_EVENTS.tsv`.
- **Seed:** updated, in a section "Update at checkpoint 29".
- **Run:** opened 21 Nov 19:35:32 UTC; GPT-6 Astra (ChatGPT Pro mode); active; review 22 at 19:35 UTC.

## 0. What I read

- The register diff by id and state: 265 rows against 234. There are 31 new rows and no state changes in old rows.
- All 31 new rows in full (the gate text as printed, up to 900 characters each).
- The text of the Q1 and Q2 gates now. The Q3, Q4 and Q5 gates are byte-identical to checkpoint 25, by hash.
- The ledger headings after checkpoint 25, and reviews 20, 21 and 22 (up to 1,800 characters each).
- `research/joint_all_top_eighteen_place_remainder.md` (R062) in full.
- `agents/actual_selected_operator_obstruction_word_correction.md` (DO079-C1) in full.
- The four mentions of Masullo in ALP_MACHINE.tex.

**Not read:** the proofs of the other 29 new findings, among them LIFT068–071, K089–091, R055–061, DO075–085 except
the two above; the cited proofs that R062 rests on (K067–K069, DO064, R050, R051, R058–R061, DO083, DO084); every script.

**Run 20:03 (the AM-H Hecke rows, agent af2a18f6's part):** nothing newer than its checkpoint 08 is filed. The stray
copies in Downloads are outside this brief. So there is no Hecke-row diff. In run 19:35 the Hecke question is Q3 (RH
for the Kummer Hecke L-function), and its gate is unchanged.

## 1. What moved since checkpoint 25

| Group | Rows | What they give | My check |
|---|---|---|---|
| Finite signed gate of Q1/Q2 | R055–R062, K087, K088, DO075–078, DO081–085 | the all-top support floor rose from 12 to 18 (R057: 13; R060: 15; R062: 18). Further high-support cuts. Uniform floor still 11. Error sums still < 2^−230 | R062 targeted check of its own argument (the cited partitions taken as stated); exponent −726048945/4096 and the error sum recomputed. Others statement level |
| Local period factors at T | LIFT067–071 | LIFT068: nonzero positive-rank split Bessel test with exact phase and modulus, under generic tempered local premises. LIFT069/070: those premises hold for the chosen bottom and the initial constituents under the full size package. LIFT071: canonical Hilbert/GGP factor q/[(q−1)(q^k−1)] | statement level |
| Integral structure | K089, K090, K091, LIFT066 | unit content at 11 of the auxiliary sections; integral Mram generators; integral left inverse of the selected Weyl substitution | statement level |
| Operator estimates | DO079, DO080 | DO079: a lower bound 7/8 that refutes a proposed exponent-1/3 operator bound. DO080: a trace fidelity bound | DO079-C1 targeted check |
| **In-run correction** | DO079-C1 | the word-invariance sentence of DO079 and the earlier PASSes endorsing it were false; with r_i fixed and m_i → m_i − ℓ, the differences stay ≥ B | targeted check: the coefficient 4(a−i)−ω_i ≥ 7 for i ≤ 166. This needs ℓ > 83, which I did not verify |

**Proved, refuted, new.** All 31 new rows are proved in stated scope. One refutation sits inside DO079 (the proposed
operator bound) and one correction in DO079-C1. No main question changed state: Q1, Q2 and Q3 are open, Q4 is partly
proved, Q5 is proved in its stated scope.

## 2. The strongest results now, in the project's terms

1. **Unchanged, and still the strongest:** LIFT54 and LIFT55, the size floors of Alpöge's step 8: two lifts are
   impossible, and m > 2^7778. With the two-sided SizeM of my seed, the length is x^{1/2+O(ε)}. In the project's terms
   this is the DP_MULT Q3e lift count, settled for the literal interface.
2. **New and useful:** the local T-place factors LIFT068–071. These are exactly the local factors that the global
   Bessel/Mram period of THETA3 G1 needs: a nonzero test vector and its canonical normalization. They are conditional
   on the genuine source package, which does not exist for any short chain (by result 1).
3. **The finite gate:** support ≥ 18 for the all-top J⁵⁶ kernel. R062's own last line: "Applying this same estimate at
   support18 gives a positive exponent and proves no bound there." My substitution gives +160198. So the full-column
   count stops at 17, and every further level needs a new structural cut.

## 3. Converging or stalled?

**Formally converging, in substance not on the main questions.**
- Reviews 19, 20, 21 and 22 all record MOVEMENT, with zero reviews without it. Each counts a complete removal of
  support levels, which the user's rule counts.
- But all the movement is in one sufficient inequality, Re Σ w(h) > −1 + 2^−230 over supports s ≥ 18. Supports run up
  to f = 168, and the uniform H8192 floor has been stuck at 11. Even when exhausted, it gives one finite nonvanishing.
  The global period, the arithmetic image, the 032 pairing and the DP44 sign stay open by the run's own statement.
- Q3 (Kummer Hecke RH) and Q4 have not moved since checkpoint 25 or earlier.
- My extrapolation, not a run statement: at about two support levels an hour, each needing a new argument, the finite
  gate alone would take days.
- **Recommendation:** the successor (or a follow-up message) should take the main question of the seed, a replacement
  size interface with bounded chain length, and stop the support-by-support exhaustion. Its prompt should not count
  support-floor raises as movement unless they close the inequality.

## 4. Outreach and Hexagon

- **Alpöge.** He may want to know the result on his formal hypotheses: SizeM pins m to x^{1/2+O(ε)}, and m = 2 is
  excluded. This is not an error in his proof, and it should be stated that way. It is worth one line once the seed's
  paper exists, through the main session's drafting rules; nothing is sent from here.
- **No other author is affected.** DO079-C1 is internal to the run.
- **Masullo (the user's rule of 22 Nov).** The run carries "Masullo's consequences remain conditional"
  (ALP_MACHINE.tex 3941) and a table row "Use Masullo's claimed all-Hecke theorem: Conditional only" (4427). No register
  row uses Masullo. Restated: anything that depended on his draft is conditional on GRH for the Hecke L-functions
  concerned, an open hypothesis, and nothing is a fix of his draft.
- **Hexagon readiness.** Unchanged: the chain-length theorem passes completeness and interest, and has two gates, a
  Lean proof or independent check, and a search. LIFT068–071 need their proofs read, and are local lemmas that belong
  in a paper only once a global period uses them.
