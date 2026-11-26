# Intake of ALP_MACHINE checkpoint 48, lifts / seesaw / oscillator / sign / frameworks half

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026. The Hecke half (AM-H ids) is agent
af2a18f62da23b48e's.

- **Return:** `research_returns\ALP_MACHINE_checkpoint_48_20261123T0950Z_unzipped\ALP_MACHINE\` (09:50 UTC).
- **Run:** the run opened 21 Nov 19:35:32 UTC; GPT-6 Astra (ChatGPT Pro mode); active; review 36 at 09:35 UTC recorded
  movement.
- **Check events:** `INTAKE_ALP_MACHINE_20261123_cp48_CHECK_EVENTS.tsv`.

## 0. Which baseline

My checkpoint-04 intake was of the **other** ALP_MACHINE run (opened 20:03:51 UTC). That run's ids (AM-L, AM-SS,
AM-ST, AM-S) do not occur here. Checkpoint 48 continues the run of my checkpoint-25/29/32/35 intakes, so I diffed it
against that run's own frozen register of review 26 (`research\review_26_QUESTIONS.tsv`, the state at checkpoint 35).
The lifts/seesaw findings of the 20:03 run have no newer return filed.

## 1. What I read

- The register diff: 82 new rows, 81 proved in stated scope and 1 refuted in stated scope (R096-EXPLORATORY). No state
  changes of old rows.
- Every new LIFT row (LIFT078–LIFT099) in full, cut at 480–600 characters.
- Review 36.
- The Q2 finite-gate text.
- A search of the ledger for 49b and for the size-interface questions.

No proof file was read. No script was run.

## 2. What moved

- **Main questions:** Q1, Q2, Q3 OPEN, Q4 PARTLY_PROVED, Q5 PROVED_IN_STATED_SCOPE. No change since checkpoint 25.
- **The finite gate:** the support floor of the all-top J⁵⁶ kernel rose from 25 to 27. The error arrays are 128/31,
  with both sums below 2^−230. DO120 and R097 work at supports 27–31.
- **49b: still not taken up.** The ledger contains no entry for the follow-up, no `SizeM` consumer list, no exponent
  program and no bounded-chain row by 09:50 UTC, ten hours after 49b was sent.

## 3. What the run now has on the mechanism of Alpöge's step 8

- **LIFT54 and LIFT55 are unchanged**: the size predicates force m ≍ x^{1/2}, m > 2^7778 and m ≠ 2.
- **New, all statement level for me, all about the formal host and its objects rather than the lift count:**

| Finding | Content |
|---|---|
| LIFT079 | The literal `CMObj`, and independently both `LamObjGood` copies, force the target to be isogenous to a power of one CM elliptic curve. Dropping `IsTen` or bypassing `CMObj` while keeping `Good` does not free the target |
| LIFT083 | A J-isotypic fibre (J = Jac(y² = x⁷ − 1)) cannot meet the pinned determinant condition at any stage. Over Q(√−7) the Lie multiplicities are (2a+b, a+2b), so DetCond needs p ≤ 2q and q ≤ 2p; other host fields give the balanced (3N/2, 3N/2). The pinned profiles p_j = k + j − 1, q_j = m − j are unbalanced at every stage (k ≫ m) |
| LIFT080–082 | A conditional height transfer for mixed-type eigenlines, effective lower line degrees on J¹⁴/J⁵⁶, and one frame polynomial for every local and archimedean Step-5 clause |
| LIFT084–092 | For any given source host: literal objects and frame points, nonzero detection at a CM point in a seed isogeny class at unchanged level, good integral models, explicit fields of definition and their degrees, root discriminants and conductors |
| LIFT093–099 | A sharpened torsion-field degree; conditional effective Hecke escape for a fixed indefinite family, with an explicit recursion; an integral hyperbolic pair in every selfdual relative-unramified indefinite lattice of rank ≥ 3; bounds for the bad locus, the very-ampleness exponent h_d = 2^{d+1}(d+1)(d+2)! and the automorphic volume; bounded component entry |

**In plain terms:**
- the run has shown that **no J-based (Fermat-type) host** can be a literal instance of step 8 (LIFT079, LIFT083,
  with LIFT54/55);
- it is building, with explicit constants, the **general-host** objects that a literal instance needs;
- none of this bounds the chain length, and none of it tests whether a shorter chain is possible. That question is
  being worked in NIGHT_AFTER_ALPOGE Part B (intake `INTAKE_NIGHT_AFTER_ALPOGE_20261123_cp11_partB.md`), not here.

**Verdicts:**
- targeted proof checks: 0;
- used and rechecked: LIFT54/55;
- the LIFT083 arithmetic rechecked from the row;
- everything else statement level;
- refuted by me: 0.

## 4. Hexagon readiness

Nothing new in this half is ready. LIFT079 and LIFT083 are clean obstruction statements and could become one section
of the chain-length note (NIGHT_AFTER_ALPOGE Part B), once their proofs are read. Their gate is a targeted proof read
of their files.
