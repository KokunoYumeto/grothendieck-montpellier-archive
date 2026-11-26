# Intake of ALP_MACHINE checkpoint 32 (run 19:35), by diff from checkpoint 29

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026.

- **Return:** `grothendieck_archive_transcription_20261110\research_returns\ALP_MACHINE_checkpoint_32_20261122T2150Z_unzipped\ALP_MACHINE\`
  (21:50 UTC; checkpoint 29 is retired inside, with its manifest).
- **Baseline:** `INTAKE_ALP_MACHINE_20261122_cp29.md`.
- **Check events:** `INTAKE_ALP_MACHINE_20261122_cp32_CHECK_EVENTS.tsv`.
- **Run:** GPT-6 Astra (ChatGPT Pro mode), opened 21 Nov 19:35:32 UTC, active. Review 24 at 21:35 UTC recorded movement.
  Follow-up 49b has not been sent.

## 0. What I read and how I compared

**Compared, all by content:**
- the register by id and state against checkpoint 29: 289 rows against 265, 24 new rows, no state changes;
- the text of every row against my extracted checkpoint-25 copy: only Q1 and Q2 changed;
- the gates of Q3, Q4 and Q5, byte-identical to checkpoint 25;
- these files, by SHA-256 against checkpoint 29's manifest:
  - LIFT54 (`agents/literal_size_chain_length_obstruction.md`) and LIFT55 (`agents/universal_size_scale_floor.md`)
    unchanged;
  - K021 (`agents/kummer_relative_height_period.md`, edc67705…) unchanged.

**Read:**
- all 24 new rows in full, cut at 700 characters;
- reviews 23 and 24;
- the Q2 gate's "current finite nonvanishing gate";
- R067 (`research/joint_all_top_twenty_three_place_remainder.md`) in full;
- LIFT075 (`agents/all_positive_gap_theta_obstruction.md`) §§1–4, about 14 of its 17.5 kB;
- the two Lean clauses LIFT075 uses: `Formalism/CyclotomicNorms/StatementT.lean` 19–29 (IsGood) and
  `Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean` 996–1007 (goodTuple, e0), in the return's copy.

**Not read:**
- the proofs of the other 22 new findings, including LIFT072–074 and LIFT076;
- the inputs R067 cites (DO086, DO088, DO089, R066, K069, DO064, DO085, R058, R061) and Mínguez 2008 and Gow–Vinroot
  2007, which LIFT075 cites;
- every script.

## 1. Answers

1. **No main question changed status.** Q1, Q2 and Q3 are OPEN, Q4 PARTLY_PROVED, Q5 PROVED_IN_STATED_SCOPE. Only the
   texts of the Q1 and Q2 gates changed; they now carry the floor 23 and the new local results.
2. **LIFT54 and LIFT55 are unchanged** (same hashes). The size floors of step 8 stand: two lifts are impossible, and
   m > 2^7778.
3. **Yes, level by level.** The all-top J⁵⁶ support floor went from 18 to 23:
   - R064 exhausts supports 18–20 (floor 21), R065 support 21 (floor 22), R067 support 22 (floor 23);
   - review 24 records movement with the floor still at 23, on partial removals at supports 23 and 24 (DO091, DO092,
     R069, R070, DO093);
   - the uniform H8192 floor is still 11;
   - outside the floor, R068 removes the whole fixed class F of rank 2 through support 110, rank 3 through 154 and
     ranks 4–33 through 168, and DO086 removes F of rank 1 through 94;
   - all error sums stay below 2^−230.
   The gate is still the sufficient inequality Re Σ w(h) > −1 + 2^−230, now over s ≥ 23.
4. **49b still fits.** It needs the replacements in section 4.
5. **K021 did not change.** Its file has the same SHA-256 as at checkpoint 29, and the Q3 row is byte-identical to
   checkpoint 25. That agrees with Codex's report that it matched its attachment.

## 2. What moved: new findings and check levels

| Findings | Content | My check |
|---|---|---|
| R064, R065, R067 | floor 18 → 23 | R067: targeted check of the assembly (coverage tables at support 22 and error sum 2^−231 + 67·2^−358 < 2^−230), inputs as stated |
| DO086–DO093, R063, R066, R068–R070 | containing-set removals at supports ≥ 18 | statement level |
| LIFT072, LIFT073 | the canonical local Bessel factors at G and at the away-G/T spherical places, conditional on the genuine source package | statement level |
| **LIFT074** | conditional global detector: **if** the two embedded occurrences are globally Bessel-distinguished, then ⟨F, Pu(T)⟩ = c_Per·b̄ ≠ 0, with c_Per > 0 explicit | statement level |
| **LIFT075** | for a split type-II theta from GL_a to GL_r, d = r − a > 0, every principal-level constituent has a linear Green factor of multiplicity ≥ d. So e0 kills the direct compact-to-bottom cuspidal theta projection for every even m ≥ 2 (d = m − 1): for d ≥ 2 by squarefreeness, for d = 1 by the goodTuple clause for degree 1. This excludes one construction, not the prescribed period | targeted proof check, given Mínguez Th. 1(2) and Gow–Vinroot Th. 3.2 (not opened); both Lean clauses checked at source (squarefree; IsGood line 27 with a = 1, since 2 ≤ r) |
| LIFT076 | the bottom constituents selected by e0 have a simple generic Arthur parameter and are tempered at every finite place | statement level |
| K092, K093, K094 | integral structure of the selected family, the decoration matrix and the corner column | statement level |

## 3. The strongest results, and converging or not

**Strongest results.**
- Still LIFT54 and LIFT55.
- New and important for THETA3 G1: LIFT074 with LIFT072/073/076. They reduce the prescribed bottom period to **one
  global statement**, that a nonzero global Bessel functional exists on the two specified embedded occurrences. The
  local factors are computed, and the representations involved are tempered with simple parameters.
- LIFT075 rules out the simplest way to get that distinction, a direct compact-source theta lift. The run's §4 names
  the remaining routes: a relative Poincaré series (Muić) needs a shrunken level, and the globalization of
  Prasad–Schulze-Pillot needs supercuspidal data. Fixed-level global distinction is the open point.

**Converging or not.** Formally the run moves: reviews 19–24, all MOVEMENT. In substance:
- the floor gained 5 levels in about 2 hours out of 168;
- the inequality, even when closed, gives one finite nonvanishing statement;
- no main question has changed state since checkpoint 25.

The new content worth having is not in the floor. It is the reduction of the bottom period to fixed-level global
Bessel distinction. That is a precise, classical-looking question, and it deserves to be one of 49b's routes.

## 4. Prompt 49b: sentences outdated by checkpoint 32, with replacements

1. Heading. **Old:** "## Where the run stands (your checkpoint 29)". **New:** "## Where the run stands (your checkpoint 32)".
2. **Old:** "Since checkpoint 25, your main questions Q1, Q2 and Q3 have not changed status, and Q4 is partly proved."
   **New:** "Since checkpoint 25, and still at checkpoint 32, your main questions Q1, Q2 and Q3 have not changed status, Q4
   is partly proved, and the gates of Q3, Q4 and Q5 are word for word those of checkpoint 25."
3. **Old:** "All the movement since then is in one sufficient inequality, Re Σ w(h) > −1 + 2^{−230}, over supports
   s ≥ 18. The support floor of the all-top J⁵⁶ kernel rose from 12 to 18 (R057, R060, R062), while the uniform H8192
   floor stays at 11. At support 18 the same count gives a positive exponent, so every further level needs a new
   argument." **New:** "Most of the movement since then is in one sufficient inequality, Re Σ w(h) > −1 + 2^{−230},
   now over supports s ≥ 23. The support floor of the all-top J⁵⁶ kernel rose from 12 to 23 (R057, R060, R062, R064,
   R065, R067), and review 24 counted movement with the floor still at 23, while the uniform H8192 floor stays at 11.
   Each level needs its own argument (R062 notes that its support-17 count gives a positive exponent at 18)."
4. **Add after that bullet:** "- Your LIFT072–074 and LIFT076 reduce the prescribed bottom period to one global
   statement: a nonzero global Bessel functional on the two specified embedded occurrences, at the fixed level.
   LIFT075 excludes the direct compact-source theta construction of it. That fixed-level global distinction is open."
5. **Add to the routes list as route 6:** "6. Prove fixed-level global Bessel distinction for the two occurrences of
   LIFT074, or show that the level must grow. Your §4 of LIFT075 names the candidates: relative Poincaré series (Muić
   2015, Lemmas 6-1, 6-2, Theorems 6-7, 6-9) at a prescribed level, and the globalization of Prasad–Schulze-Pillot
   (2008, Th. 4.1) adapted to the finite types of e0."

The sentence on LIFT54 and LIFT55 stays as it is: they are unchanged.

## 5. Outreach, Hexagon, Masullo

- **Outreach:** nothing new. The note to Alpöge about the size floors (cp29 intake, section 4) stands.
- **Hexagon:** unchanged. LIFT075 is a clean local lemma, but on its own it is an exclusion of one construction.
- **Masullo:** no new mention. The rule holds: anything resting on his draft is conditional on GRH for the Hecke
  L-functions concerned, an open hypothesis, and nothing is a fix of it.
