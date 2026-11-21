# Intake of THETA3 checkpoint 01 (prompt 37, HODGE_THETA: three signatures)

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent), launched by the main session (Claude Opus 5.5 at effort
max), 21 Nov 2026, under `field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`, with the extra item "Hexagon readiness"
(`field_experts\HEXAGON_CANDIDATES.md`). Work file: `agent_notes\20261121_intake_HODGE_SIGN_NOTES.md`. Check events:
`INTAKE_THETA3_20261121_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\THETA3_checkpoint_01_20261121T0134Z_unzipped\`. It is checkpoint 01, the only THETA3
folder present when I started.
- The run is GPT-6 Astra (ChatGPT Pro mode). It began at 00:49 UTC, and this checkpoint is from 01:34 UTC, 45 minutes in.
- **The run is still going.** Its main question, Q1 (the sketch's 1.7), is OPEN. Q2, Q3 and Q4 are PARTLY PROVED.

**What I read:**
- `THETA3.tex` in full: Q1–Q9 and C12;
- `LEDGER.md`, `QUESTIONS.tsv`, `TRANSCRIPTION_NOTES.tsv` and `PACKAGE_STATUS.md`;
- from `documentation\agent_noncm_integral.md`, the statements of C06, C07 and C11.

**What I did not read:**
- the working proofs of A1–A5, B0–B13 and C01–C11. They are in `documentation\`, and the run itself says they are not yet
  integrated.

**Scope:**
- **Read in full with a targeted proof check (10):** Q1, Q2 (numbers re-estimated by hand), Q3, Q4/Q5 (given A1), Q6, Q7
  (given A1), Q8, Q9 and C12.
- **Statement level (4):** A1, C06 and C07 (I checked the derivative arithmetic), and C11.
- **Not read:** B0–B13, A2–A5, C01–C05 and C08–C10. I used only their QUESTIONS rows.

## 1. Verdicts, finding by finding

- **Q1, perturbation of the period: confirmed.** This is Cauchy–Schwarz and the reverse triangle inequality. The sign is
  right: ∫ξ∧ξ̄ > 0 for (2,0)-forms on a surface. The factor d comes from pullback under a cover of degree d. Elementary.
- **Q2, Gaussian isolation: confirmed.**
  - The shell count (2j+3)^d follows from disjoint balls of radius ρ/2.
  - r e^{−πλr²/2} ≤ 1/√(πeλ).
  - The wedge error is a direct expansion.
  - I re-estimated the certificate: c = 2πe^{−2π} ≈ 0.011733; E(6) ≈ 2.15 · 5⁶ · e^{−9π} ≈ 1.77·10⁻⁸; and
    c² ≈ 1.3767·10⁻⁴ > 1.37·10⁻⁴. The margin is thin but positive. The run's interval arithmetic is the certificate; I did
    not rerun it.
- **Q3, rational rounding: confirmed.** Elementary.
- **Q4/Q5 and Q7: confirmed, given A1.**
  - A1 says the averaged theta coefficient over the compact unipotent quotient equals Φ(0). I read it at the level of the
    statement.
  - The maximum is at least the mean; automorphy and the rounding grid do the rest. The Lipschitz constant (eq. L-bound)
    is the shell argument again.
- **Q6, the Fock determinant: confirmed.** ‖P_{u,v}‖² = 2(‖u‖²‖v‖² − |⟨u,v⟩|²). The value 1 is a convention, as the run
  says.
- **Q8: confirmed.** dz₁∧dz₂∧dz̄₁∧dz̄₂ = 4 dvol, and vol(B_r) = π²r⁴/2.
- **Q9, resultant projectors: confirmed.**
  - On ker f(T), uf + vg = R gives e = 1; on ker g(T), e = 0.
  - DP ∈ O_K, and the norm is at least 1.
  - This is the same device as HECKE_DIV's P1.
- **C12, the period of 500 on Schoen's surface: confirmed, from the construction outward.** I did not check the
  construction itself.
  - Y → C₀² has degree 5·5·5. C²/C₀² is Galois of degree 4, so the two extensions are linearly disjoint.
  - The total degree is 500, and ∫_{F²} η∧η̄ = 1.
  - F (j = 2048) is non-CM: 2048 is not one of the 13 rational CM j-invariants.
  - As the run itself says, the cycle is 500 times a product of two diagonal divisors. **It is not a new Hodge case.**
- **C06 and C07: statement level, with the arithmetic checked.**
  - C06: Den(X) = (1−X)(1+(q−q²)X+X²) gives Int = −Den′(1) = q + 2 − q², which is negative for q ≥ 3.
  - C07: Den(X) = (1−X)Σ_{j≤a} X^{2j} gives Int = a + 1.
  - I did not check the local density formulas themselves (Cho–Yamauchi type).
  - A negative derived local intersection for L = πI₃ is possible because Z(x₁)∩Z(x₂)∩Z(x₃) need not be proper. Whether
    this is already in Li–Zhang's proof of the Kudla–Rapoport conjecture, or in its examples, has to be looked up.
- **C11: statement level.** An exact digit-sum bound for derivatives of height-two formal groups. This bears on step 2,
  and on our suggestion 2 (divided powers).

**Counts:**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 10 (Q1–Q9, C12) |
| Statement level | 4 (A1, C06, C07, C11) |
| A gap | 0 |
| Refuted | 0 |
| Not read | B0–B13, A2–A5, C01–C05, C08–C10 |

**The main question is open.** The run's useful negative results so far, at statement level:
- B10: there is no direct rank-three specialization of the global matching.
- B4 and B6: scalar rescaling and two rank-one projections give no lower bound.
- C01: on congruence ball quotients the whole Albanese is CM.

## 2. What is new

- **Q1–Q9:** elementary, explicit forms of 032's continuity step (Prop. 4.5, Cor. 4.7). They are useful as named
  constants, but none is a new theorem.
- **C12:** a construction, not a Hodge case.
- **C06/C07:** possibly new as stated examples. This needs a literature check.

**Against our results.** The run reads 032 §§4.5–4.7 as Taylor tensors with Gaussian concentration and continuity, with no
Rallis or Bessel identity. That agrees with the sketch's 3.1 (the non-vanishing is positivity plus continuity). It
corrects the sketch's Route 1, which reads 032's non-vanishing as a seesaw pairing: that is the sketch's 1.7, still
unproved.

**Against tonight's runs.**
- Q9 is the resultant projector of HECKE_DIV's P1.
- C01 ("on congruence ball quotients the Albanese is CM") is the same wall that HECKE_DIV's R24D and HODGE_SIGN's SG-04
  meet from the other side: everything built from CM elliptic powers is divisor-generated.

## 3. The two proofs, and HODGE_SIGN

- **Alpöge:** cited background. THETA3 uses no RH or GRH in any finding read.
- **Masullo:** not used.
- **Overclaims:** none.
- **SG-08–SG-11 (the sign-only proof, Hexagon candidate H01):** THETA3 neither uses nor changes them.
  - Its "local positive determinant" (Q6) is Fock-space positivity: a Hermitian form on a Schwartz space.
  - HODGE_SIGN showed that the step-5 sign carries no form (SG-01, SG-08). So the two positivities are different objects,
    and THETA3 rightly does not identify them.

## 4. Integration

- **Scan numbering. THETA3 cites printed folios, not our scans.**
  - "Cote 16, scans 43–46, the letter to Coates dated 4 January 1967 … date on scan 43" is our scan 044. Our
    `16_scan044.tex` opens "4.1.67. Dear Coates" and carries `\mspage{43}`.
  - "Cote 44, scans 7–8" is our 008–009: our `44_scan008.tex` has "Bures le 12.8.1964, Mon cher Serre".
  - This is the folio/PDF-page convention that HECKE_DIV documents (folio = PDF page − 1). Our `\scanpage` is the PDF page
    and our `\mspage` is the folio.
  - So THETA3's "date on scan 43, not scan 44" is not a correction. In our numbering it is scan 044.
- **Hodge sketch** (`reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`):
  - **Route 1:** after "the same slot as the lifts of Hecke characters", add: "THETA3 ckpt 01 (prompt 37): 032 §§4.5–4.7
    state no Rallis/Bessel identity. The non-vanishing is Gaussian concentration plus continuity, and 1.7 is unproved. The
    nearest rank-three matching (B10) has the wrong signature range."
  - **3.1:** add "quantified in THETA3 Q1–Q8 (checked)".
- **Open rows:** none settled. The rows of THETA3's own `QUESTIONS.tsv` stand as the run states them.
- **Successor and parallel prompts:** prompt 41 (DEGREES_ARE_L_VALUES) can use Q9 and Q4–Q7 as the denominator and
  constant bookkeeping.

## 5. Hexagon readiness (the five tests of HEXAGON_CANDIDATES.md)

| Finding | 1 Complete | 2 Self-contained | 3 Stable | 4 Checked | 5 Of interest | Verdict |
|---|---|---|---|---|---|---|
| Q1–Q9 | yes | yes (032 cited) | no: the run is going | targeted check only | low: bookkeeping lemmas | not a candidate |
| C12 | yes | yes | no | targeted check | low: product of diagonals | not a candidate |
| C06/C07 | not read in full | yes | no | arithmetic only | medium, if new | watch: needs a full read, the density formulas checked, and a literature search (Li–Zhang) |
| Main question (1.7) | open | – | – | – | high if proved | not yet |

**None is ready, and none is one gate away.** Nothing to flag.

## 6. Prompt updates (THETA3 successor; to the run if it is reachable)

1. **Main attack: 1.7.** Use B11/B12, the totally definite U(2) inside the original U(2,1), to recover the ball pairing.
   Prove that A5's positive correction operator is algebraic, or locate the obstruction exactly.
2. **Instantiate the located `ValLastX.lean` step-12 laws on the 032 data.** Give the exact signature tower in which they
   apply.
3. **Archive:** cite cote 16 and cote 44 by PDF page (our scans) with the folio in parentheses. Use our text of record:
   cote 16 scans 044–050 and cote 44 scans 008–009.
4. **Write all proofs in the paper** (A1–A5, B0–B13, C01–C11). At this checkpoint they are in working notes only.
5. **Check C06 against Li–Zhang** and the literature on Kudla–Rapoport local densities. State whether a negative
   Int(L) is known.
