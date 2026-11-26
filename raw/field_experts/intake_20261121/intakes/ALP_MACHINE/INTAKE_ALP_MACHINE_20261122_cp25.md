# Intake of ALP_MACHINE checkpoint 25 (lifts expert), with the newest zip of the baseline run

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 22 Nov 2026. Seed, written first:
`reports_20261122\paper_seeds\SEED_ALP_MACHINE.md`. Check events: `INTAKE_ALP_MACHINE_20261122_cp25_CHECK_EVENTS.tsv`.
Extracted members and lists: `reports_20261122\overnight_intake\ALP_MACHINE\`.

## 0. Two runs

| | Run 19:35 | Run 20:03 |
|---|---|---|
| Opened | 21 Nov 19:35:32 UTC | 21 Nov 20:03:51 UTC |
| Newest found here | `<local>/Downloads\ALP_MACHINE_checkpoint_25.zip` (review 19, 16:35 UTC, movement) | `<local>/Downloads\ALP_MACHINE_checkpoint_08(1).zip` (review 04, 02:03 UTC) |
| Also | research_returns checkpoint 23 | checkpoints 02, 03, 07 "(1)" in Downloads |
| Ids | ALP-LIFT, AM-K, AM-R, AM-DO | AM-L, AM-SS, AM-ST, AM-S, AM-O, AM-H |
| Model | GPT-6 Astra (ChatGPT Pro mode) | GPT-6 Astra (ChatGPT Pro mode) |

**A diff from my checkpoint-04 intake to checkpoint 25 is not meaningful: they are different runs.** The "(1)" zips are
not duplicates and must not be deleted as such. Checkpoint 23 and 25 of run 19:35 are one run.

## 1. What I read, and what I did not

**Run 19:35, checkpoint 25:**
- README and the opening and review 19 of the ledger;
- the gate text of Q1 and Q3 (printed partly) and every register row at the level of id, state and the first 105
  characters of its question; a few rows in full (R003, R023, LIFT26, LIFT59);
- IMPLICATIONS, its first section in part and its headings;
- `universal_size_scale_floor.md` in full; `literal_size_chain_length_obstruction.md` §§1–5 to the contradiction, and
  the end of §7 with §8;
- the Lean definitions those proofs cite: ElevenLe 1–50 and 118–141, DataParams₂ 1–47, Params 1–48, ParConsts 25–48,
  FamCore 70–86;
- by hash, both proof files match the run's recorded SHA-256, and are byte-identical in checkpoint 23.

**Run 20:03, checkpoint 08:** `oscillator_sign.tex` 392–655 (AM-S1–S4 and the closing section); the register rows
AM-Q1 and AM-Q2, cut; the ledger's last headings.

**Not read:** the 4.9 MB paper; every construction proof (K, R, DO and the other LIFT findings); the support-elimination
proofs; the Kummer part (Q3); the dictionary; the recovery folders; run 20:03's findings after checkpoint 04 other than
the above. No code of either run was run. The Hecke part of run 20:03 is agent af2a18f6's.

## 2. What is new

| Finding | Statement | Verdict |
|---|---|---|
| LIFT54 | `SizesAt` ⇒ (log f)² ≤ m/2 − 1; m = 2 impossible; f = 42, 168 impossible at any scale | confirmed against the Lean definitions |
| LIFT55 | `SizesAt` ⇒ L > 2^300, m > 2^7778, f > 2^33598, k > 2^73197 | confirmed; exponents recomputed |
| my addition | `SizeM` is two-sided: x^{1/2−29ε/400} ≤ m ≤ x^{1/2−21ε/400} | author's check |
| R003, R023 | the CM Jacobian's hosts are not instances of the formal host | statements |
| K031–K044, LIFT26, LIFT56–59 | explicit mixed kernels, nonzero two-edge composite, injective towers, nonzero bottom cusp space | statements, scoped |
| recent reviews | signed finite gate reduced to support ≥ 12 | ledger statement; internal bookkeeping |
| AM-S1–S3 (run 20:03) | when a phase can replace the sign | reread; confirmed |

The register has 234 rows: four main or partly main gates are open (Q1 lift count, Q2 pairing, Q3 Kummer RH, Q4 in
part). The run says in its README that none of the three main theorems is established.

## 3. False or superseded in what we hold

**By the returns:**
1. Any plan to promote the two-edge J¹⁴/J⁵⁶ family, or the L = 343 profile, to an instance of Alpöge's proof by repairing
   ranks, degree or primes is refuted (LIFT54, LIFT55). The DP_MULT Q3e "lift count" question survives only with a
   changed size interface.
2. My checkpoint-04 intake and prompt updates treat ALP_MACHINE as one run. There are two, with separate gates.

**In my intake of 21/22 Nov (`INTAKE_ALP_MACHINE_20261121_lifts.md` and its events):**

3. **False reading claims.** AM-ST01, ST02, ST09, ST12, SS06 and G01 are recorded "statement read"; I never opened
   them. For ST05, ST11, ST13, ST14, SS09, SS15, SS16 I read only the first lines of the statement. For L12 I did not
   read the proof ("proof structure read" is false), and L11's only in part.
4. **Inflated types.** L8, L9, L13, L15, SS13, SS17, ST03, ST06, ST08, ST10 are recorded as targeted proof checks; each
   rested on a statement or part of a proof plus my own argument. L4 and O4 are recorded as independent re-proofs;
   they were computations.
5. **The totals are wrong.** "Targeted 26, re-proof 2, every finding checked" becomes: **14 targeted proof checks**
   (S1–S4, L1–L3, L5–L7, L10, SS02, SS04, SS12), **0 independent re-proofs**, L4 and O4 computations, the rest
   carried, or certificate runs only.
6. **Scripts** were run without reading their code, and the signed-torus rerun was judged from one filtered flag. Their
   passes certify what the scripts print, which I did not audit.

The new events file appends the corrections. The old files are left as they were, so read them with this section.

## 4. How it bears, and the attack

- **A (Alpöge's theorem):** unaffected. The size theorem locates what a simplification must change.
- **DP_MULT Q3e:** the comparison of chain lengths has to be made over a replacement interface. The attack is a finite
  linear program over the exponent constraints of the consumers of `SizeM`, `SizeK` and log f ≤ √r_S (seed, routes
  1–2).
- **THETA3 G1:** nonvanishing is no longer the gate in the run's stated models; the arithmetic bottom period and mass
  are.
- **Cote 16:** AM-S2 is the effectivity point of H01: a reflected trace is a virtual class, and cancels.

## 5. Hexagon (register not edited)

| Candidate | Tests | Gate left |
|---|---|---|
| The chain-length theorem | complete and elementary; self-contained over Lean definitions; of interest now | a Lean proof or an independent check; a search; the licence of the quoted source; confirm that the pinned commit is current |
| AM-S1–S3 | complete, checked | short alone; a section of the same paper or a remark in H01 |
| The constructions | not checked | full proof reads |

## 6. For the prompts and the filing

1. File by the run's opening time, not the checkpoint number. Both Hodge and ALP_MACHINE have twins, and other prompts
   may too.
2. The successor's main question is bounded chain length under a replacement interface, starting from the consumers of
   the size clauses.
3. Do not publish the ZIP: it carries 831 of Alpöge's Lean files and many other sources (list: `sources_cp25.txt`).
