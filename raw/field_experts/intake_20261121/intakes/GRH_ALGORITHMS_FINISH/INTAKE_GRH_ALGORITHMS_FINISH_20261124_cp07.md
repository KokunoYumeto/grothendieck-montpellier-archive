# Intake of GRH_ALGORITHMS_FINISH (prompt 67c), checkpoint 07, and Codex's edition for Hexagon

Written 24 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), by diff from
`INTAKE_GRH_ALGORITHMS_FINISH_20261123_cp04.md`. The run is GPT-6 Astra (ChatGPT Pro mode). The edition is by Codex,
GPT-6.2 Astra at reasoning effort ultra.

## Verdict for the deposit: post as is
The five fixes Codex reports are correct, and all five are in the 191-page edition. The F₁₉ counterexample is also in
the edition; Codex's F₁₀₉³ example is in its review, not in the paper, and need not be.
- **P160.** Correct. The edition now reads "Two complementary degree-two elliptic quotients are". I recomputed: at
  t = 0, (x, y) ↦ (x², y) maps y² = x⁶ + 1 onto v² = u³ + 1, which has j = 0, while the displayed curves have
  j = 6912·125/16 = 54000.
- **P163.** Correct.
  - The quantifier "a supplied prime k | p^d − 1" is in the edition.
  - F₁₉: x = 4 has order 9 and y = 9 = x⁴, while the literal test sets are {1, 4, 16}, {1, 7, 11}, {1}.
  - F₁₀₉³: σx = 63x for x = (97, 7, 5); v = 97 has order 27; y = x⁴ = (v⁴, v¹³, v²²). The single-digit sets miss y,
    and v⁴ − y = (0, 23, 55).
  - The repair, digit extraction support by support on the components where x has full order, is correct. It is a
    standard Pohlig-Hellman argument, run componentwise.
- **P164.** Correct: "detects residue degree one". For p unramified, b^p − b vanishes at 𝔓 for an integral basis iff
  f(𝔓/p) = 1.
- **P156.** A wording change, not re-derived.
- **P149.** The sign b = (−1)^j f(0), with b^r = z^j, is present and right.

**Also recomputed:**
- P161: point counts over F₅₃ and F₅₃²: t = 5 gives (54, 3004, a₂ = 97); t = 7 and t = 41 give (54, 2860, 25).
- P150: over F₁₀₇ and F₁₀₇², t = 17, 98, 99 all give (108, 11716, a₂ = 133).
- Both match the paper and Codex.

**Not read by us:** the proofs of P147-P149 (the quantitative CM residue maps), checked only by the run and by Codex's
targeted reading, and P151-P159 and P162 beyond Codex's review.

The edition's method note names our earlier checks accurately. It does not mention our check of P145/P144 or these
recomputations; that is an understatement, not an error. An optional addition for a later version would name them.

## 0. Scope
- **Read:** the edition's P160, P163 (with the F₁₉ example and the repair) and P164 text; its abstract and method note;
  Codex's `review_147_155.md` and `review_156_164.md`, in full; the opening of `EDITORIAL_REVIEW.md`; the cp07
  `STATEMENTS.tsv` P147-P164.
- **Computed** by our own program, in the session scratchpad: the F₁₀₉³ example, the F₁₉ example, and the point
  counts.

## 1. What moved since checkpoint 04
- **P149** (Theorem 1.2), under A for fixed r, t: removal of every prime ℓ ≤ L with v_r(ℓ−1) ≤ t. The t = 0 case is
  P144. This makes Q01's unconditional gate strictly smaller again.
- **P151-P164:** cyclic-descent interfaces and their limits, genus-two collisions, local units, ideal profiles, and the
  corrections above.
- The changed mathematics is summarized in `PRIMER_GRH_ALGORITHMS_FINISH_20261123.md`, §8.

## 2. Verdicts
Confirmed by us at cp07:
- P160, P163, P164 (as corrected);
- P161 and P150, by computation;
- the P149 sign edit.

Statement level: P147-P149 (main), P151-P159, P162. Refuted: none in the corrected forms. In the uncorrected forms,
the run's P160 "the two quotients" wording and the P163-cited printed routine are wrong, as Codex says.

## 3. Scope of the inputs
- Unconditional: P144, P145, P149 at t = 0, P151 at period prime to r, P152, P157, P158, P164.
- Under A: P147-P149 at t ≥ 1.
- Tang's interfaces rest on the 2026 preprints named in the edition.
- Nothing uses Masullo.

## 4. Integration
- Applied: the primer's §8, after a backup.
- For the main session: board H29/H29b; fleet map ANT-07.
- Logged in `INTEGRATION_GRH_ALGORITHMS_FINISH_20261123.tsv`.

## 5. Board candidates
| title | statement | what it adds | gate left |
|---|---|---|---|
| Finite fields of prime degree beyond the small cofactor (P149) | as in §1 | the residual cofactor shrinks by every bounded-congruence prime | an expert check of P147's quantitative CM residue map |
| The edition as a whole (H29/H29b) | 164 statements | Lenstra's construction problem: two unconditional classes and fixed strata under A | none for v1, per this verdict |

## 6. For the P vs NP fleet
ANT-07 (succinct finite planes): P149 adds, under A, every q = p^r whose cofactor is small after removing primes
ℓ ≤ L with v_r(ℓ−1) ≤ t. The next work is unchanged: the decider, and the list of covered r for p = 2. For the main
session to apply.
