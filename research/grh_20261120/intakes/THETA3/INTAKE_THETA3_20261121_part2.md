# Intake of THETA3, part 2: checkpoint 03 (prompt 37)

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent), 21 Nov 2026, round 3. The brief is
`field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`. Part 1, on checkpoint 01, is `INTAKE_THETA3_20261121.md`.
Check events: `INTAKE_THETA3_20261121_part2_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\THETA3_checkpoint_03_20261121T0304Z_unzipped\`, the newest present. The run is GPT-6
Astra (ChatGPT Pro mode); it began at 00:49 UTC, and this checkpoint is from 03:04 UTC. **The run is still going.** Its
first formal review was due at 03:49 UTC. The paper has grown from 31 KB to 390 KB (7,447 lines).

**What I read:**
- `QUESTIONS.tsv`, in full;
- `LEDGER.md`, from checkpoint 01 to 03:00 UTC;
- the outline of the paper;
- in full: C13;
- the statements of A6, B17, C14, C20 and C22, and of C06 against its new Li–Zhang citation;
- Part II, the statements not asserted ("G1–G4").

**Changed since checkpoint 01:**
- Q1–Q9 and C12 are unchanged in statement. The Q1 text matches what I checked.
- C06 now cites Li–Zhang, Theorems 3.4.1 and 3.5.1, for the local formula.
- A1 (the anisotropic zero-orbit identity), A5 and C12 are now marked as having passed independent checks in the run.

**Nothing I confirmed in part 1 is withdrawn.**

## 1. Verdicts on the new findings

There are about thirty new findings: A6–A8, B14–B18, Q10–Q11, C13–C22, and several "PROVED" refinement rows. I read in
full only the one that bears on the Hodge line's open problems. The rest I read at the level of the statement.

- **C13, an explicit algebraic projector onto the Weil space: confirmed.**
  - a = M + b₀, with b₀ purely imaginary and M large, gives 0 < arg a < 1/(2n), so the λ_j = a^j ā^{2n−j} are distinct.
  - The resultant projector e_W = R⁻¹v(T)g(T), composed with the Künneth projector π_{2n}, is built from [N]^* and [a]^*.
  - a^{2n} ∉ Q, so a single nonzero projection α gives α and Tα spanning W.
  - Since ∫_X b^*w = ∫ e_W cl(b_*[X]) ∪ w, one nonzero period is enough.
  - **This is the same result as HECKE_DIV P1 and P3.**
- **C14, curve-product constructions miss the Weil space when NS(A)_Q = Qθ: statement level.** The proof reduces to the
  stability of the divisor (Lefschetz) algebra under pushforward by homomorphisms and Pontryagin product (Milne 1999,
  from memory). The conclusion is plausible and agrees with HECKE_DIV R24D and R24F.
- **A6, direct balanced 2n-factor CM cycles on an n-ball (Liu's exact theorem in every rank): statement level.** The run
  says itself that all sources stay CM, so the algebraicity is already covered by 032. What is new is the direct
  construction.
- **B17, the actual wedge as a literal double lift V → P → V with a common positive Q⁻¹, plus the last-step Bessel
  seesaw: statement level.** The run's own Part II (G1) states the limit: **B17's upper space is A ⊥ H, of signature
  (3,1) at every real place. It is not a totally definite inner form.** So the sketch's 1.7 (one seesaw pairing that
  links 032's signature-(2,1) machine with Alpöge's totally definite groups) is **still not proved**. The analytic half
  is closed; the arithmetic `MainX` matching is open.
- **C20, a genus-two Jacobian with End = Z (y² = (x−a)φ(x), a = x(P), P ∈ E[7]) as a quotient of the Albanese of a
  ball cover of degree ≤ 1764: statement level.** The End = Z claim rests on two reductions over F₃₇ and F₃₇²; the run
  checked them twice, and I did not recompute them. It is a real enlargement of non-CM weight-one sources on ball
  quotients. But by C14 it cannot by itself reach a Weil class with NS = Qθ.
- **C22, the weaker slope is sharp for an actual theta section (y² = 4x³ − 4x, p = 7): statement level.** It refutes the
  stronger extension (Q4-individual-strong) with a sharp refinement.
- **C06:** now cited to Li–Zhang's local formula. Whether a negative Int(L) for L = πI₃ is already noted in that
  literature is still unsearched.
- **The rest** (A7, A8, B14–B16, B18, Q10, Q11, C15–C19, C21): statement level, from their QUESTIONS rows and the
  ledger. Nothing in them conflicts with HODGE_SIGN, HECKE_DIV or the sketch.

**Counts for part 2:**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 1 (C13) |
| Statement level | 6 read (A6, B17, C14, C20, C22, C06), plus the remaining ~24 from their rows only |
| A gap | 0 |
| Refuted | 0 |

**The state of the main question (Q1, the sketch's 1.7): PARTLY PROVED, open.** The gate is now exact. The two-step
`MainX` case needs:
- a totally definite middle space (by A7, exactly when the selected first-list CM types agree);
- the arithmetic kernel/covolume and terminal-mass equations;
- an arithmetic meaning for the analytic correction operator.

## 2. What is new

- **The exact gate of the sketch's 1.7.** B17 together with Part II (G1) locates it: **analytic seesaw yes; arithmetic
  definite matching not yet**.
- **C20 and C16:** infinitely many non-CM, and simple non-CM, weight-one sources on covers of one ball surface. This may
  be new; it needs checking against Schoen 2014 and the literature on Albanese varieties of ball quotients.
- **C13** duplicates HECKE_DIV P1/P3; **C14** is the generic mirror of HECKE_DIV R24D.

**The common wall.** Every curve-product or divisor construction misses the Weil plane on very general Weil-type
members (C14). On CM elliptic powers everything is divisor-generated (HODGE_SIGN SG-04, HECKE_DIV R24F). The exceptional
non-CM summand (G3) needs a correspondence that does not factor through curves.

## 3. The two proofs

- No new finding uses RH or GRH.
- Masullo is not used.
- **H01, the sign-only proof:** not used and not changed. THETA3's positivities (Fock determinants, definite Bessel
  periods, Q11) are Hermitian forms on automorphic spaces. They are not the step-5 effectivity sign. They are correctly
  kept apart.

## 4. Integration

- **Hodge sketch, Route 1 and 1.7:** replace "Prove the sketch's 1.7" in its status by: "THETA3 ckpt 03: the analytic
  seesaw is realized (B17, a double lift V → P → V), but its upper space has signature (3,1) everywhere. The definite
  matching with Alpöge's MainX remains (G1). A7: the multiplicity space is totally definite exactly when the first-list
  CM types agree."
- **Same file, Route 1 gate (non-CM):** add "THETA3 C16 and C20: non-CM, including simple genus-two, sources occur as
  Albanese quotients of covers of one ball surface (degree ≤ 1764). C14: maps from curve products miss the Weil space
  when NS = Qθ."
- **Scan numbering:** THETA3 still cites folios: "cote 16 scans 43–46" is our 044–047. Edit as in part 1.

## 5. How it bears on the running prompts, and the attacks it opens

- **38 and 39:** C13 and C14 are the extraction tools. One nonzero Weil projection suffices, and it cannot come from
  curve products when NS = Qθ. **For GHOSTS:** a ghost Weil class at p, algebraic on the special fibre with no lift,
  must be cut out by a correspondence that does not factor through curves. That gives a test.
- **The next attack (THETA3 successor):**
  1. Choose CM types for which A7's multiplicity space is totally definite.
  2. Solve the `MainX` kernel/covolume equations there.
  3. Then the definite Bessel periods (B12, Q11) bound the ball norm, and Alpöge's step-7 determinant applies.

## 6. Hexagon readiness

| Candidate | 1 | 2 | 3 | 4 | 5 | Verdict |
|---|---|---|---|---|---|---|
| C20 (a simple non-CM source in a ball tower) | proof present | yes | no: the run is going | statement level | medium | not yet |
| C06 / C22 (local theta-arithmetic examples) | yes | yes | no | statement level | low to medium | not yet |
| 1.7 | open | – | – | – | high | not yet |

**None is ready.** Nothing to flag.
