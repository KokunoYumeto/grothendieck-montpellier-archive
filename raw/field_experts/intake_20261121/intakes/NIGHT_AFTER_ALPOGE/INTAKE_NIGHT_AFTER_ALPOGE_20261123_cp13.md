# Intake of NIGHT_AFTER_ALPOGE (prompt 75), checkpoints 11 → 13, by diff

By ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026 (evening), for the main session 329fb1e6 (Claude Opus 5.5 at
effort max). The brief is `INTAKE_WAVE_20261123_EVENING.md`.

The run is GPT-6 Astra (ChatGPT Pro mode). The filed checkpoints are 11 (10:24 UTC) and 13 (11:54 UTC); checkpoint 12
was not filed. The Riemann hypothesis for all Dirichlet L-functions is Alpöge's theorem (20 Nov 2026) and is cited
as a theorem.

## Usefulness first

- **Parts A and C have not changed since checkpoint 11.** I compared the files byte for byte: the CM-orbit paper, the
  K-groups paper and the Ihara paper are identical; only build logs were added. Their two strongest results are now
  in our pipeline:
  - **A.ORBIT** (every CM point of A_g has |Gal·x| ≥ c_g D_x^{1/(4g)}) is the H15 note, `reports_20261123/h15_note/`,
    and is useful as the first explicit-exponent orbit bound for all centre orders.
  - **C.IHARA** (Anderson-Ihara's kernel question at every Vandiver prime) was deposited as hexagon:2611.00939 on
    23 Nov, after my gate and second reading. It answers a question recorded as open (Sharifi, RIMS 2120 (2019),
    p. 222).
- **Part B (the theta chain) is the only part that moved: 24 new statements.** They are bookkeeping lemmas that close
  sub-gates of B-Q1 at flag rank zero and length m = 2. B-Q1 asks whether Alpöge's theta-chain method extends with
  bounded chain length (a "bounded-length RH replacement"), or whether the method diverges intrinsically.
  - On its own, no new B statement answers a question someone outside asked. Their value is internal: they shrink the
    gate of B-Q1.
  - The run's review 07 counts movement.
  - B-Q1 stays open. Still open: signed joint theta-jet/period/column contents, a fixed primitive finite-word period
    detector, the complete bounded-length arithmetic host, and the pointwise Hilbert-Schmidt, critical-level, loop
    and nongeneric suppliers.
  - B-Q2 is unchanged.
- **Part C main research (Vandiver at every prime; unrestricted Ihara) is still queued behind B.**

## 0. What I read

- **Diffs, cp11 → cp13:**
  - the file lists;
  - byte comparison of every .tex/.md/.tsv;
  - LEDGER.md: all 124 new lines, including scheduled review 07;
  - QUESTIONS.tsv;
  - the B STATEMENTS.tsv diff (24 new rows).
- **Read in full and checked:**
  - `zero-gram-identity.tex` (B.ZERO_GRAM_IDENTITY);
  - `class-number-terminal.tex` (B.CLASS_NUMBER_TERMINAL).
- **Statement level only:** the other 22 new B statements, as their ledger entries and STATEMENTS rows describe them.
- **Parts A and C:** unchanged. My cp11 verdicts stand. Since cp11 I also did the H15 note (my checks) and the H06b
  gate and second reading (`reports_20261123/h06b_note/REVIEW_ad855737_v1.md`). Those check events are recorded there
  and are not repeated here.
- **Not opened:** the theta-chain `main.tex` (325 pp.) and the other B section files; the formal-build records.
  Part B's expert is abcaba9b. Nothing at a cited source was opened in this task.

## 1. Verdicts

| Id | Statement (short) | Verdict |
|---|---|---|
| B.ZERO_GRAM_IDENTITY | At flag rank 0 and m = 2: G_term = 0 iff the term is in the identity cell; so K_pp = K_2 = 0 | **confirmed, every step** (Lemma zg:congruence, Prop. zg:primitive-vectors, Cor. zg:original-cell). I recomputed h(z,y) = 0 and h(y,y) = T(q q̄ − TT') for y = Tz' + qz. Then a = −q/T is a unit with a ā = 1, a − 1 = gβ, and \|N(a−1)\| ≤ 2^{2f} < g^{2f} for g ≥ 3. The attachment to the original terms (g = g_0 g_1 ≥ 4, signature (k,1)) is as stated. |
| B.CLASS_NUMBER_TERMINAL | h_E ≤ (π²/9)^f r_E^{2f}; Q·9^f ≤ (4π²k r_E^{5/2})^f ≤ H under (cnt:retained-size), (cnt:uniform-C), for every even m ≥ 2 | **confirmed, every step**: the injective ideal-to-tuple map and Σ N(I)^{-2} ≤ (π²/6)^n; M_E ≤ (2/π)^f √D_E; h_E ≤ M_E²·(π²/6)^{2f}; the budget algebra. The Minkowski bound and the archive's normalization are carried. |
| B.ZERO_FLAG_FRAME_COUNT, B.PRIMITIVE_CORANK_ONE, B.ZERO_FLAG_PRIMITIVE_COUNT, B.ZERO_FLAG_PARTNER, B.ZERO_FLAG_VOLUME, B.ZERO_FLAG_MEAN_ANALYTIC, B.ZERO_FLAG_LOCAL_MOMENT, B.ZERO_FLAG_HAAR_CONTRACTION, B.ZERO_FLAG_AMPLITUDE_MAP, B.ZERO_FLAG_STANDARD_REGION, B.ZERO_FLAG_LOOP_SCALARS | zero-flag counts, means, volume 1, local radius Q = 8k, contraction (operator norm ≤ 1), amplitude = orbital integral | statement level |
| B.FIXED_LENGTH_FRAME, B.LINEAR_SCALE_DEGREE (D ≤ 27fNxb + 3fN²), B.EV0_QUOTIENT_DICTIONARY, B.WORD_SPECTRAL_VOLUME, B.TERMINAL_OFFDIAGONAL_BUDGET, B.DIAGONAL_TERMINAL, B.NONGENERIC_EXACT_PRIME, B.PRIMITIVE_CORE_PROJECTORS, B.PRIMITIVE_DETECTOR_QUOTIENT, B.GOOD_TYPE_GRID_FULLNESS, B.WHOLE_ROW_TWO_THETA_KERNEL, B.RAMIFIED_SELECTED_ADJOINT, B.SCALAR_CLASS_OPERATOR, B.POINTWISE_TWO_STEP, B.DIVISOR_SUM_EXACT, B.RANK_ZERO_GRAM, B.AGGREGATE_SELECTED_RANK, B.CORE_BASE_LVALUES | consumer and supplier lemmas | statement level |
| A.*, C.* | unchanged | cp11 verdicts stand |

**Counts:** 24 new B statements: 2 confirmed by a full proof check, 22 at statement level, 0 refuted. Parts A and C:
no new statements.

## 2. What is new

- **Part B.** At flag rank 0 and m = 2, the following are now proved by the run:
  - the zero-flag frame count, the primitive mean and the exact generic determinant;
  - the class-number factor, with no flag-rank restriction;
  - the zero-Gram cell;
  - the volume (exactly 1);
  - the local moment radius and the Haar contraction.

  The derivative interval is now ⌈35 + 5 log₂ f + 18 C₂⌉ ≤ q ≤ 2k. One loop wrapper still assumes m ≥ 4, so its use at
  m = 2 is not asserted. No bounded-length RH replacement or divergence theorem is proved.
- **Formal build:** a recovery after a disconnect; no closed `OneCharU_s` and no axiom print are claimed.

## 3. Scope of the inputs

- **A:** (1.1), a special case of Alpöge's theorem, together with published theorems. Effective André-Oort (A.AO) is
  Jaswal and Cureton-Thorner, cited and not claimed.
- **C:** the archive intermediate theorem `OneCharU_s` for the K-groups. For Ihara: Fukaya-Kato, Wake-Wang-Erickson,
  Brown, Hain-Matsumoto. No Alpöge input.
- **B:** Alpöge's mechanism over Q(ω) and its theta-chain inputs (the source archive's numerical records).
- **Masullo:** nowhere.

## 4. Integration

**Applied** (backups in `integration_backups/20261123/NIGHT_AFTER_ALPOGE/`; log in `INTEGRATION_NIGHT_AFTER_ALPOGE_20261123.tsv`):
- `reports_20261122/paper_seeds/SEED_KTOWER.md`:
  - Paper 1 literature: the H06b gate result, the deposit hexagon:2611.00939, and the Pintar gate;
  - Paper 2 literature: the H15 pass (Banks, Cureton-Thorner, Liu; GR23 Thm 1.9(5) against 1.8; Jaswal Prop. 3.3;
    Tsimerman Thm 5.1).

  The Paper 2 header update to A.ORBIT had already been applied (an update block dated 23 Nov was present).

**For the main session** (shared registers I may not edit):
- **`field_experts/hexagon/HEXAGON_BOARD.tsv`, H15 row:**
  - set the note to `reports_20261123/h15_note/h15_note.pdf`;
  - the gate is closed (literature pass done);
  - state: ready for the user's word.
- **H06b row:** deposited as hexagon:2611.00939 (WB-0006); open fix-ups:
  - the abstract's "earlier versions" wording;
  - the Sharifi Lemma numbering (Lemma 4 in arXiv v2);
  - add the Sharifi 2019 quote.
- **H18 row:** Pintar gate passed (main session, 23 Nov); the remaining gates are the axiom print and the KMSW
  background.
- **`field_experts/HEXAGON_CANDIDATES.md` H15 and H06b:** as in my cp11 intake §6, now superseded by the rows above.

## 5. Prompt updates (run or successor)

1. Part C is queued. When it starts, attach `reports_20261123/h06b_note/REVIEW_ad855737_v1.md`; the Ihara paper
   needs only the three fix-ups listed above.
2. Part B:
   - give the m = 2 loop wrapper replacement (Params still assumes m ≥ 4);
   - attack the signed joint theta-jet/period/column content directly. It is the named first gate.

## 6. Hexagon readiness and board candidates

| Title | Statement | What it adds | Gate left |
|---|---|---|---|
| (H15, existing) Galois orbits of CM points in A_g with an explicit exponent | \|Gal·x\| ≥ c_g D_x^{1/(4g)} for every CM point of A_g | the first explicit exponent for all centre orders | the user's word; the main session's page reading |
| (H06b, deposited) Anderson-Ihara at every Vandiver prime | Ω_p* = Ω_p for odd p with X_p^+ finite | settles the question at all irregular p < 2^31 | the posted text's three small fix-ups |

**No new board candidate from cp13.** The B lemmas are internal to the theta chain. B.CLASS_NUMBER_TERMINAL's bound
h_E ≤ (π²/9)^f D_E is a known kind of Minkowski estimate and adds nothing on its own.

## 7. For the P vs NP fleet

I searched `<local>/pequalnp_work/fleet_map/PROOF_GRAPH.tsv` (1519 rows) for lattice, ellipsoid, class number,
isogeny, CM, Galois orbit, Magnus and pro-p. Its only "theta" nodes are theta graphs (monotone circuit lower bounds,
L-meta-493/517/595/615/657/722), which are unrelated.

**No node maps onto these results; no bridge is constructed.**
- The nearest translatable item is B.ZERO_FLAG_FRAME_COUNT, a count of integral points on a positive ellipsoid,
  ≤ 9^{fj}(N Q_Δ)^j. It would bear on counting nodes only through a lattice-point counting node, and the graph has
  none.
- A.ENUMERATION is a terminating algorithm without a complexity bound.
