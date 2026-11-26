# Intake of ALP_MACHINE checkpoint 35 (run 19:35), by diff from checkpoint 32

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026.

- **Return:** `grothendieck_archive_transcription_20261110\research_returns\ALP_MACHINE_checkpoint_35_20261123T0005Z_unzipped\ALP_MACHINE\`
  (00:05 UTC; checkpoints 32 and 34 are retired inside).
- **Baseline:** `INTAKE_ALP_MACHINE_20261122_cp32.md`.
- **Check events:** `INTAKE_ALP_MACHINE_20261123_cp35_CHECK_EVENTS.tsv`.
- **Run:** GPT-6 Astra (ChatGPT Pro mode).

## 0. What I read

- The register by id and state: 311 rows against 289, 21 new rows, all proved in stated scope. The main states are
  unchanged.
- Every new row at the level of its question. LIFT077, R078 and LIFT078 in full.
- Every ledger heading after checkpoint 32, and reviews 25 and 26 (up to 1,400 characters each).
- A search of the ledger for "follow-up", "49b", "bounded chain" and "bounded length". A check for a
  `PROGRESS_LEDGER.md`.
- No proof file. No script was run.

## 1. Did the run take up 49b? Not by checkpoint 35

- The ledger has no entry recording a follow-up, although 49b asks for one in its first paragraph. No
  `PROGRESS_LEDGER.md` exists.
- No new row concerns the size interface, the consumers of `SizeM` or `SizeK`, an exponent linear program or a bounded
  chain.
- Every ledger entry after 23:30 UTC (23:32 "complete support24 exhaustion", 23:35 review 26, 23:40, 23:48, 23:56,
  00:01, 00:03) concerns support levels 24–32 of the finite kernel.
- Review 26 (23:35) counts the floor 23 → 25 as movement, by the old rule, not by 49b's rule that a floor raise counts
  only if it closes the inequality.
- 49b went into the chat at about 23:30. The checkpoint ZIP is from 00:05, so the run may still have been in a turn
  begun before the message. **Whether it took up 49b can only be judged from checkpoint 36 or later**: look for a
  ledger entry on the follow-up, `PROGRESS_LEDGER.md`, and rows on the consumers of the size clauses.

## 2. What moved

| Findings | Content | My check |
|---|---|---|
| R074, R078 | support floor 23 → 25 (supports 23 and 24 exhausted); uniform floor still 11; error sums < 2^−230 | statement level |
| R071–R077, DO094–DO101, K095, K096 | containing-set removals at supports 23–32 | statement level |
| **LIFT077** | the global coupling b of LIFT074 is calibrated by an exact central-value formula: \|b\|²/(n_T n_F) = (explicit positive constant) · L^{G∪∞}-ratio(1/2) · ∏_G d_ς^{−1} · ∏_T q/[(q−1)(q^k−1)], in the scope of LIFT070/LIFT076 | statement level |
| LIFT078 | an averaged content-ideal bound with an explicit ζ_F(1.001) < 3003·5^167, without GRH | statement level |

**Main questions:** Q1, Q2, Q3 OPEN, Q4 PARTLY_PROVED, Q5 PROVED_IN_STATED_SCOPE. No change. LIFT54 and LIFT55 are not
among the changed rows.

## 3. The strongest new result, and converging or not

- **LIFT077 is the important one.** Together with LIFT074 it turns the bottom period into a central L-value: if the
  embedded pair exists, the prescribed period is nonzero exactly when the central value of the L-function at s = 1/2
  in its formula is nonzero. That is the usual shape of an Ichino–Ikeda/GGP formula, and it moves THETA3 G1 to a
  central-value nonvanishing question. It is statement level for me: the constants and the scope need a proof read
  before anyone uses it.
- **Converging:** no change from checkpoint 32. The finite floor gains about one level an hour, no main question has
  moved since checkpoint 25, and the run had not yet turned to the bounded-chain question.

## 4. Outreach, Hexagon, Masullo

- **Outreach and Hexagon:** nothing new.
- **Masullo:** no new mention.
