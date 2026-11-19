# The Grothendieck–Teichmüller line: GT_TOWER_CHECK, DELTA_ON_GT, EXIT_TOWER read together (bounded intake)

Intake by Claude Fable 5.2 at effort high, 17 Nov 2026, 22:00 UTC (step 2 of the field-expert workflow; no
sub-agents). The three returns are by GPT-6 Astra (ChatGPT Pro mode). Nobody outside those runs has checked a proof
of theirs, except for the few steps listed in section 6.

- GT_TOWER_CHECK, checkpoint 10 (17 Nov 2026, 09:45 UTC; INCOMPLETE; the run is dead):
  `<local>/Documents\longue_marche_pro_pilot_20261104\answers\GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped\GT_TOWER_CHECK\`
  and its session transcript
  `<local>/Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111_work\GT_TOWER_CHECK\SESSION_TRANSCRIPT_GT_TOWER_CHECK_20261117.md`.
- DELTA_ON_GT, checkpoint 05 (16 Nov 2026, 06:50 UTC; INCOMPLETE):
  `...\answers\DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\DELTA_ON_GT\`.
- EXIT_TOWER, checkpoint 28 (16 Nov 2026, 14:43 UTC; INCOMPLETE):
  `...\answers\EXIT_TOWER_checkpoint_28_20261116T1443Z_unzipped\extracted_20261116\`.

## 0. What was already taken in, and what this intake adds

| Earlier note | By | What it covers | Counted here? |
|---|---|---|---|
| `pro_intake_20261116\EXPERT_GT_TOWER_AND_GHOSTS_20261116.md` | Claude Fable 5.2 at effort max (Longue Marche expert) | EXIT_TOWER checkpoint 28, register rows E.24, E.37, E.39–E.46, E.49, D.45 (rows only, no proof); the ghosts of SECTIONS_OVER_Q; four doubts D1–D4; items I1–I6 | No. I answer D1–D4 and I1–I4 from GT_TOWER_CHECK (section 2) and do not restate the rows |
| `pro_intake_20261116\EXPERT_E49_IMPLICATIONS_20261117.md` | the same expert | What follows across the programme if E.49 holds; the ranked referee points | No. Section 4 says which of its conditionals GT_TOWER_CHECK now supports |
| `pro_intake_20261114\EXPERT_DELTA_TAU.md` | the same expert, 14 Nov | `Δ` as the sign of an idempotent of `Z/12`; items T1–T5 | No. Section 4 gives the state of T2, T3, T4 |
| `pro_intake_20261114\apply_expert13_exit_tower_20261114.py` | main session (Claude Opus 5.5 at effort max) | An edit of the EXIT_TOWER prompt before it was sent (cote 150). Not an intake of a return | n/a |
| `longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\08_SECTION_GHOSTS\PROMPT.md` | main session (Claude Opus 5.5 at effort max), 17 Nov | GT_TOWER_CHECK **Part C** at checkpoint 10 is built into this unsent prompt (its R2–R7, L1, L5, Parts B and C) | Part C is summarized in six lines only |
| `pro_intake_20261117\LM4_SUCCESSOR_FINAL_INTAKE_20261117.md` | Claude Fable 5.2 at effort high | LM4_SUCCESSOR; it listed four cross-checks for these three runs | Answered in section 3 |

**New in this intake:** GT_TOWER_CHECK Parts A and B (checkpoint 10 and the transcript); DELTA_ON_GT checkpoint 05,
for which I found no intake in the four intake folders; what EXIT_TOWER checkpoint 28 holds beside the rows the
expert read (in the GT line only). **Not taken in by anyone, as far as those four folders show:** EXIT_TOWER Parts
A–D and its rows E.50–E.107, E.T1–E.T13 (exit categories, cote 143 and 146, higher genus). They are outside this
line; they need an intake of their own.

**Correction to my brief.** Checkpoint 10 on disk has **180** statements (165 Proved, 2 Known, 13 Open), not 189.
The figure 189 (174 Proved, 2 Known, 13 Open) is checkpoint 11, which was never downloadable.

**What I read.** GT_TOWER_CHECK: the report in full, the register rows of P.1, A.1–A.9, A.4.1, A.4.55, A.4.57,
A.4.59, the main rows of B.1–B.7 and C.1–C.5, `part_p.tex`, `part_a_cm.tex` in full (the proof of A.3 and A.7), the
transcript's narrative lines throughout and lines 2380–3189 in full. DELTA_ON_GT: the report in full, the register
(titles only; it carries no statements), the statements A.84, A.103, B.15, B.31–B.34, B.40, B.41. EXIT_TOWER: the
register rows named in section 1.3, the first lines of the report. The three prompts as sent were not read; task
labels are taken from the reports. **What I checked myself is in section 6; everything else is reported from the
runs.**

## 1. Each run

### 1.1 GT_TOWER_CHECK (an audit of EXIT_TOWER's GT theorem, of DELTA_ON_GT's open reduction and of the ghosts)

**State at checkpoint 10** (408 pages; counted by me in the register): 180 statements, 165 Proved, 2 Known, 13 Open.
By Part: A 72 Proved, 1 Known, 2 Open; B 43 Proved, 6 Open; C 50 Proved, 5 Open; P 1 Known. No row is labelled
Refuted; the refutations are Proved rows that refute a posed assertion. The 13 Open rows: A.4, A.8, B.1, B.2, B.3,
B.4, B.6, B.7, C.1–C.5.

**What the checkpoint holds: the main theorem and the audit of EXIT_TOWER.**
- **A.7 (with A.3):** `Δ = 0` on the full profinite `GT̂`, for the character of LM7_PUSH E.65 with its signed frames,
  and `G_Q ⊆ GT̂ ⊊ ker Δ ⊊ GT̂₀`, both right-hand inclusions strict. The first inclusion's equality is not decided.
- **A.3:** EXIT_TOWER E.49 is confirmed **after two repairs to its written proof**. (i) Its determinant `−1`
  relabelling permutes the four pairs of three-torsion labels, so it does not justify treating the four forgetting
  maps as individually preserved; at multiplier one the commutator of the punctured torus forces determinant `+1`,
  which gives a pure conjugator. (ii) The three added two-torsion branch labels may undergo one common permutation;
  it is carried until those labels are forgotten. The passage to all multipliers is by an element of `G_Q` with the
  same multiplier.
- **Where the proof lives** (`part_a_cm.tex`, read by me). The moduli of elliptic curves, rigidified, is identified
  with the fibre of the universal curve over the point `j = 0`, minus its origin, modulo `μ₆`, through the division
  quartic `t² = x⁴ + 2ax² + 4bx − a²/3` and `Y² = Z³ + D/108` (A.C6, A.C7). This gives
  `φ : (C₂ ∗ C₃)^ ≅ G₃ ⊂ Γ̂_{1,2}`. The chain of comparisons (translations by the three-torsion, the elliptic
  involution, four forgetting maps to five points, the double cover with ordered poles) yields **one** element
  `h ∈ Γ̂_{1,2}` with `Φ^A φ = Ad(h) φ α` (A.C14). The centralizer of the order-three element is the cyclic CM group
  (Boggi–Zalesskii, Theorem A(iii), at `p = 3`), so `q(h) = R₊^k` with one `k ∈ Z/6`. Reading
  `TC = R₊^k CM` modulo 3 gives `ε₃(T) = k`, modulo 4 gives `ε₂(W) = k`; hence `Δ = 0`. For the witness
  (`T = 5I`, `W = I`) `k` would be odd at 3 and even at 4.
- **Where the pentagon is used** (the expert's doubt D2). The run's statement: in the tower construction the
  pentagon is the line that reduces the mixed six-move relation on the twice-punctured torus to
  `f(W,X) f(Y,Z) f(V,W) f(X,Y) f(Z,V) = 1` (EXIT_TOWER (E.98); A.6.1, A.3(c)). My reading of the proof: the
  automorphism `Φ` is the action of the parameter on `B̂₄` modulo its centre, which is `Γ̂_{1,2}`, and an element of
  `GT̂₀` gives an automorphism of `B̂₃` only; so the argument has no starting point on `GT̂₀`. The run does not
  compute a pentagon value of the witness, and says so: the witness is excluded by the contrapositive.
- **A.1, A.1.1 (Known), A.1.2, A.9:** EXIT_TOWER E.44 (`𝒥(A) = A` for every `A ∈ GT̂`) is confirmed. Its input is
  Boggi–Zalesskii Theorem A(iii) (their Theorem 4.3(iii)) applied to the single group `C₂²` in a finite-index
  subgroup of `Γ_{0,[10]}`; it does not use the equality "intersection of closures = closure of the intersection"
  that LM4_SUCCESSOR B.1–B.3 found unproved. The full induced topology of the centralizer is by an explicit
  retraction; both index-two classes and both forgetting maps are carried. A.1.2 proves the solvable case in genus
  zero (normalizer density and the finite map to `Aut(H)`): a second proof of LM4_SUCCESSOR B.30/B.39's solvable
  repair.
- **A.2:** "the element of E.46 / E.58" is a non-empty **family** of lifts; every member has `λ = 1`, `ρ = 0`,
  `T = 5I`, `W = I` modulo 12, `Δ = 1`. EXIT_TOWER E.47 is not used by E.49.
- **A.6, A.6.1:** (E.200) is Lochak's compatible-pair equation (5.1) (Lochak 2025, Definition 5.4 to Proposition
  5.9, opened by the run). The tower action of every `A ∈ GT̂` is on the **full** profinite mapping class groups of
  all stable labelled surfaces, with sewing, capping and forgetting; no congruence-subgroup assertion in genus ≥ 3.
  The proofs of EXIT_TOWER E.29, E.32, E.33, E.35, E.38 were absent from the attachment; the run replaced them by
  its own proofs. So E.42–E.43 are re-proved here, not audited line by line.
- **A.5, A.5.1–A.5.3:** both vanishing assertions that DELTA_ON_GT A.103 reduced to hold on `GT̂`: `d₂ = 0` (the
  harmonic primitive, `c₂(f) = ρ`) and then `e₃ = 0` (from `Δ = d₂ + e₃ = 0`). A.5.3: the full profinite Kummer
  distribution `δ_N(f) = y^{c_N(f)} f` for every element of `GT̂` (Enriquez 2007, Theorem 8.1).

**What the checkpoint holds: the finite task A.4 (Open).** The prompt asked for an independent finite census of
pentagon shadows. It was not obtained.
- A.4.1: by compactness a finite quotient of `Γ̂_{0,5}` exists in which no element with `Δ = 1` has trivial
  pentagon. So "the exclusion exists only at an infinite level" is false for this system.
- A.4.57: one explicit characteristic five-point level at which every genuine pentagon shadow has `Δ = 0`, every
  multiplier. It is a finite form of the proof above, not an independent computation; the enumeration at that
  level was not run.
- Elements with `Δ = 1` that **pass** the five-point pentagon test: A.4.41 and A.4.43 (every finite family of
  odd-derived targets; the reversed-prime class-two source), A.4.48, A.4.50 (the ternary source with all odd
  refinements), A.4.55 (mixed modulus 6), A.4.59 (`Γ_{0,5}/(N′N^{12})`).
- A.4.42: finite CM descent and ordinary forgetting differ by exactly `C₃⁴` at the joined output.

**What the checkpoint holds: Part B.**
- **B.1.1, B.1.2, B.1.8 (the condition of §47).** Two markings of the descent: `D_L` (LM2's physical marking) and
  `D_P` (the literal current one), with `D_L = Ad_c ∘ D_P`. On `GT̂`: `D_L = id` and `D_P(F) = cFc`. So
  `GT̂ ⊆ C_L = Fix(D_L)`, and `GT̂ ⊄ C_P` (an element of `G_{Q^ab}` seen in `Q(ζ₈, 2^{1/8})`; `C_P ∩ G_Q = {1, c}`).
  `C^φ = GT̂` and `C^φ = ker Δ` are refuted for the literal marking; B.1.3: an element `k` with
  `D_P(k) = D_L(k) = 1`, `Δ(k) = 1`, so neither fixed group contains `ker Δ`. **Open (B.1): `C^φ ⊆ ker Δ`**, with
  `d₂ = 0` proved on it and the comparison `ε₃(T) + Ψ₃/2` left (B.1.7, B.1.9, B.1.10).
- **B.2.1–B.2.3 (`GT̂ ⊊ ker Δ`).** An element of `ker Δ` failing the pentagon in weight nine at 11 (B.2.1); the
  images in the free exponent-11 quotients of class 3 to 10 (B.2.2): `G_Q` and `GT̂` have the same image, `ker Δ`
  and `GT̂₀` have the same image, first separation of `GT̂` from `GT̂₀` at class eight; an integral weight-seven
  polynomial `h₇` with pentagon image `160((34) − (12))` (B.2.3).
- **B.2.4–B.2.31 (the quadratic characters of `GT̂₀` that vanish on `GT̂`).** The space `𝒳` of continuous
  characters `GT̂₀ → F₂` vanishing on `GT̂` has dimension exactly `ℵ₀` (B.2.25). `D_P` is onto `GT̂₀` (B.2.24). The
  characters `Δ ∘ D_Pⁿ` are linearly independent, already on the multiplier-one part; `Ξ = (Δ ∘ D_Pⁿ)_n` is onto
  `F₂^N`, kills `GT̂`, and turns `D_P` into the shift (B.2.25). A second family `η` (B.2.26–B.2.28) and one family
  `d̄_p` for each odd prime `p ≡ 3, 5 mod 8` (B.2.29–B.2.31) are independent of these and of each other;
  `𝒳/D*𝒳` is infinite-dimensional, so no finite set of characters generates `𝒳` under descent (B.2.30). `GT̂` has
  continuum index in `ker Δ` and in `GT̂₀` and is nowhere dense in both. B.2.4: a character in `𝒳` that factors
  through the actions on all free pro-`ℓ` groups, `ℓ` odd, is zero.
- **B.1.7, B.4.1–B.4.3 (the same parameter on quotients).** For a cyclic group of prime-power order rotating a
  sphere (two fixed points and three regular orbits marked), for every prime-power group acting on a punctured
  sphere with all branch points marked, and for the hyperelliptic quotient `Γ̂₂ → Γ̂_{0,[6]}`: the induced action of
  `F ∈ GT̂` has parameter `F`. The outer invariant of the two-step origami is constant on `GT̂` (B.4.3): it does not
  separate `G_Q` from `GT̂`.
- **B.5, B.5.1:** EXIT_TOWER B.25 re-derived: 542 objects, 1620 arrows, 541 tree edges, 1079 cycles, 1080 relators,
  all checked by the run. The run opened the Montpellier scans of cote 148 (folios 30–32, PDF scans 31–33; also
  29, 30, 34, 52–57): the lower fractional twist is **1/4**, where the first-pass transcription has 1/3. The path
  classes of the other arrows are a torsor under `Γ_{0,5}^{1068}`; the diagram alone does not fix them.
- **Open in B:** B.3 = B.6 (every involution of `GT̂` conjugate to `c`: the method of E.44 fails because no map
  realizes an arbitrary involution with three peripherals and a five-point structure; Herfort–Zalesskii and
  Wykowski 2026 need a discrete virtually free group that is not available); B.4 = B.7 (all genera, all frame
  characters, a separator of `G_Q` from `GT̂`); B.2 (further finite images).

**What the checkpoint holds: Part C (the section ghosts), in short.** Already built into `08_SECTION_GHOSTS`.
Finite support gives a rational point (C.1.1); for one fixed pair, non-empty fibres at every depth give one
compatible pronilpotent section (C.1.7); exactly 24 class-two sections above each ordinary pair (C.1.18, C.1.19);
selected original A.44 families fail first at class three (C.2.5, C.2.6), on an open dense set of choices (C.2.9);
SECTIONS_OVER_Q A.65 and A.72 certified with their arithmetic input rebuilt (C.2.10–C.2.12, C.2.17); a rigid
target `y² = x³ + 9` minus 27 points excludes one family (C.3.1–C.3.5), and its generalized Jacobian quotient
excludes nothing (C.3.8–C.3.10). Open: C.1–C.5 (finite support from survival at all depths; a uniform target).

**What only the transcript states (after checkpoint 10; nothing of it is on disk as a checked paper).**
All of it is task A.4; Parts B and C did not move, and the 13 Open rows stayed 13.
- A.4.61 (its working proof is inside checkpoint 10, uncounted): one element with `Δ = 1` whose pentagon vanishes
  in **every** coefficient of the relative-abelian tower at once; A.4.63: together with all stated odd refinements.
- A.4.62: the binary class-two target `Γ_{0,5}/(γ₃(N)N⁴)` and its common source; its canonical kernel
  `C₃ × C₂^{542}`; a genuine `Δ = 1` element with a non-abelian record there (the family of zero-defect records has
  `2^{4138}` members); the same element through the whole coefficient tower (transcript lines 2552–2784).
- Checkpoint 11: 440 pages, **189 statements (174 Proved, 2 Known, 13 Open)**. It was 759,708,947 bytes, over the
  Library's limit of 536,870,912, and was not saved (line 2989).
- `(Lie₃(K^{ab}))_G ⊗ Z₂ ≅ Z₂^{512} ⊕ C₂^{14}` (line 2889); a genuine `Δ = 1` survivor at **modulus eight**
  (A.4.72–A.4.74, `2^{4240}` zero-defect records; lines 3013–3101); the coefficient-sixteen system consistent,
  proof under way when the session ends (lines 3105–3186).
- The last build: 459 pages, **196 statements**, clean log, 108 pages inspected (lines 3155, 3184). Never packaged.
- The brief's three examples are in checkpoint 10 already: `GT̂ ⊊ ker Δ ⊊ GT̂₀` (A.7), E.49's label repair (A.3),
  the infinitely many independent quadratic characters (B.2.25–B.2.30). The transcript adds no conclusion on them.

### 1.2 DELTA_ON_GT (does `Δ` vanish on `GT̂`? attacked directly)

**State at checkpoint 05** (162 pages; counted by me): 221 statements, 175 Proved, 17 Refuted, 15 Known, 14 Open.
By Part: A 140 / 14 / 6 / 7; B 28 / 3 / 4 / 6; P 7 / 0 / 5 / 1. Open: P.6, A.24, A.51, A.53, A.70, A.84, A.85,
A.86, B.28, B.33, B.38, B.39, B.40, B.41. Refuted: A.3, A.7, A.8, A.9, A.16, A.17, A.25, A.29, A.33, A.48, A.68,
A.73, A.78, A.160, B.4, B.17, B.30.

- **The main question is Open there (A.84).** Neither `Δ|_{GT̂} = 0` nor an element of `GT̂` with `Δ = 1`.
- **The reduction (A.112, A.103, A.87).** The pentagon forces `ε₂(W) = ν₄`, with `ν₄` the evaluation
  `f((123), (1234))` in `S₄`; and `ε₃(T) = κ_d mod 2`. So `Δ = 0` on `GT̂` is exactly `ν₄ = κ_d mod 2`,
  equivalently `d₂ = e₃` with `Δ = d₂ + e₃`.
- **What cannot see it (the bulk of the run).** One element with `Δ = 1` passes: the whole adelic Burau family at
  every prime and level (LI.9); the full relative pronilpotent Ferrari quotient, as an automorphism (A.128); the
  covers of rank 129 and 4097, `L/D₂′` and `L/D₄′` at every prime and level (A.153, A.166, A.167). A.94: `Δ`
  survives beyond the third derived action; a finite detector of the `B`-source needs derived length four. A
  canonical detecting representation: the action on `N^{ab}` of rank 97, `N = ker q₁₂`, modulus 576 on the
  multiplier-one part (A.98, A.110); the rational homology has no `Δ` constituent (A.111).
- **`GT̂ ⊊ GT̂₀`** from R1 (P.11); `GT̂ ∩ ker Δ ⊊ ker Δ` (P.13).
- **The descent** (A.62, A.65, A.93, A.94, A.107; R12): `D_L = Ad_c ∘ D_P`, `D_P(σ) = cσc` on `G_Q`; the literal
  `GT̂ ⊆ Fix(D_P)` and `Fix(D_P) = ker Δ` are refuted (the field `Q(ζ₈, 2^{1/8})`); `d₂ = 0` on both fixed groups.
- **B.15:** the lift of LM7 D.46 repaired with one Frobenius at 7: an element with projective pair `(I, [i])`,
  parities `(0, 1)`, `Δ = 1`. **B.14:** the frame image of the multiplier-one part is `C₆ × C₄`, of `G_{Q^ab}`
  the equal-parity `C₁₂`. **B.1:** the characters that factor through the finite frame pair are `0` and `Δ`.
- **Cote 148 (B.31–B.34):** twelve pentagonal structures; the label action and the generator-power action have
  different cycle types (a correction of its own checkpoint 01); the automorphism groups of five-point sets are
  `C₂, C₄, D₃, D₅`; the 1620 arrows Open (B.33: only the graph count 1079).
- **Manuscript dictionary (R11, B.24, B.25):** in the convention of scan 12 the unrestricted `g = f⁻¹` is false;
  `g = f⁻¹ y^{(1−λ)/2}`, `β = (λ−1)/2`; `β = ρ` is refuted. From the first-pass transcription; scans not seen.
- Refuted leads of the prompt: the canonical gauge-invariant trivialization (A.3); pointed-category detection
  (A.25, A.29); the principal-level map over `j` (Lead 6, A.15/A.41); Lead 8's prime-power centre (A.7, A.8); Lead
  9's supersingular formulation (A.16); surjectivity onto the full projective norm-one product (A.73); universal
  rigid frames at six and seven points (B.30).

### 1.3 EXIT_TOWER, beside the rows the expert read

**State at checkpoint 28** (counted by me): 283 statements, 250 Proved, 18 Refuted, 12 Known, 3 Open. By Part:
A 12 / 2 / 1 / 0; B 29 / 2 / 1 / 0; C 7 / 0 / 2 / 0; D 96 / 6 / 4 / 0; E 106 / 8 / 4 / 3 (121 rows). Open: E.24
(`G_Q = GT̂`), E.45 (surjectivity of `GT̂ → Out^{I₀}` of one procongruence group of genus ≥ 3), E.T3 (which
structure cote 143 retains).

In the GT line, not in the expert's note:
- **E.47 (Proved):** `N_U(Δ_σ) = C_σ` in the procongruence group, and `GT̂ → Out^{I₀}(Γ̌_{g,[n]})` injective with
  closed image for `g ≥ 3`, also for the full completions. **E.48 (Refuted):** the diagonal Bers model in the proof
  of Boggi 2014, Theorem 6.3, is not injective. E.50–E.107 are steps towards E.45 and do not reach it.
- **E.77 (Proved):** `GT̂`, and every closed subgroup between `G_Q` and `GT̂`, has the CS and RGC properties of
  Hoshi–Mochizuki–Tsujimura 2025, Definition 3.3; the COF condition for `GT̂` is not evaluated.
- **E.37, E.41:** the index-24 map `Γ̂_{0,5} → Γ̂_{1,2}` and the genus-zero retractions onto multicurve stabilizers
  that carry E.44 and E.42.
- **B.25:** the 542-object, 1620-arrow realization with 1080 relators (re-derived in GT_TOWER_CHECK B.5).
- Refuted rows that touch published statements: E.14 (three assertions in Boggi 2026 and Boggi–Funar 2026 as
  printed), E.48, D.20 and D.26 (Boggi), D.12, D.72 (Minahan 2025), E.18. For the informing-authors list, after a
  referee.

## 2. The three together

**One question, three states.** DELTA_ON_GT left `Δ|_{GT̂} = 0` Open; EXIT_TOWER E.49 claims it; GT_TOWER_CHECK
A.3/A.7 confirms it with two repairs. These do not contradict: DELTA_ON_GT did not produce an element of `GT̂` with `Δ = 1`.

**What GT_TOWER_CHECK settles for DELTA_ON_GT.**
- A.84: proved (A.7). A.103's two vanishing assertions: both proved on `GT̂` (A.5.2). DELTA_ON_GT's gate
  `ν₄ = κ_d mod 2` then holds, both sides being `Ψ₃/2 mod 2`. The run gets `d₂ = 0` from the harmonic primitive of
  Nakamura–Tsunogai, proved on `GT̂` by the genus-zero tower square (A.5.1), and `e₃ = 0` from the sum.
- B.40 (is `𝒳` generated by `Δ`): **no**; DELTA_ON_GT could not show one descent iterate non-zero, GT_TOWER_CHECK
  shows all of them independent and `𝒳` of dimension `ℵ₀` (B.2.8, B.2.25, B.2.30).
- A.85 (the corrected inclusion): `GT̂ ⊆ C_L` proved (B.1.8). The cubic defect on the fixed groups stays Open in
  both runs (GT_TOWER_CHECK B.1).
- B.33 (the 1620 arrows): closed for the specified realization by EXIT_TOWER B.25 and GT_TOWER_CHECK B.5.
- Lead 10's question (a pentagon lift of the `Δ = 1` witness): no such lift exists.

**What GT_TOWER_CHECK settles for EXIT_TOWER** (the expert's doubts, `EXPERT_GT_TOWER_AND_GHOSTS_20261116.md`):
- D1 (E.44's three missing things): supplied in A.1 (the two pure classes, the topology of the centralizer by a
  retraction, the two parameters).
- D2 (where the pentagon is used; why the argument does not give `Δ = 0` on `GT̂₀`): section 1.1.
- D3 (the completion in genus ≥ 3): full completions throughout, no congruence-subgroup input (A.6(b), A.6.1).
- D4 (is (E.200) Lochak's definition): yes, his equation (5.1), opened (A.6(a)).
- E.49's proof as written in EXIT_TOWER has the label gap; the proof of record is GT_TOWER_CHECK A.3.
- E.46's "the element" is a family (A.2).

**Where the runs agree.**
- The descent: DELTA_ON_GT (A.62, R12) and GT_TOWER_CHECK (B.1.1, B.1.2) give the same conversion of markings,
  the same field `Q(ζ₈, 2^{1/8})`, the same refutations.
- `GT̂ ⊊ GT̂₀`: DELTA_ON_GT P.11 (from R1), GT_TOWER_CHECK B.2.1 (weight nine), B.2.3 (weight seven), and `Δ`.
  B.2.2's first separation at class eight is weight seven, where the Longue Marche handoff has the witness `q₇`.
- Finite tests do not see `Δ` on pentagon solutions: DELTA_ON_GT (Burau, Ferrari, ranks 129 and 4097) and
  GT_TOWER_CHECK (odd-derived targets, moduli 6, 12 and 8, the relative-abelian tower, binary class two) each
  found `Δ = 1` elements passing every pentagon test they computed.
- The counts of cote 148: 542, 1620, 1079 in DELTA_ON_GT, EXIT_TOWER, GT_TOWER_CHECK and LM4_SUCCESSOR.

**Where they differ.**
- Status of `Δ|_{GT̂} = 0`: Open (DELTA_ON_GT) against Proved (the other two). Settled as above.
- "The element of E.58" (EXIT_TOWER E.46, DELTA_ON_GT's R2 witness) against "a family" (GT_TOWER_CHECK A.2,
  LM4_SUCCESSOR B.42–B.45). The family reading is right; `Δ` and the frames are constant on it.
- Two different `Δ = 1` witnesses are in use: parities `(1, 0)` (E.58, E.46) and `(0, 1)` (LM7 D.46 as repaired in
  DELTA_ON_GT B.15). Texts that say "the witness" should say which.
- I found no contradiction between proved statements of the three runs. I did not compare proofs line by line.

**How far to trust `Δ|_{GT̂} = 0`.**
- GT_TOWER_CHECK auditing EXIT_TOWER is the same model, GPT-6 Astra (ChatGPT Pro mode): a second proof along the
  same route, with the attachment of the first; not an independent check.
- The independent finite check the prompt asked for (A.4) was not obtained. Every finite level either run
  computed has `Δ = 1` survivors; the level that excludes them (A.4.57) comes from the proof itself.
- The step everything rests on is `𝒥(A) = A` (E.44, A.1), that is, Nakamura–Schneps's genus-one relation on all
  of `GT̂`. By the run's own literature audit (P.1), Lochak–Nakamura–Schneps 2026 and Basualdo Bonatto–Robertson
  2026 still work with the subgroup. A statement open since 2000 needs a referee from another model family before
  it is relied on.

## 3. The cross-checks LM4_SUCCESSOR's intake asked for

1. **LM4_SUCCESSOR A.105/A.111 against E.49 (its Q6).** GT_TOWER_CHECK confirms E.49 (A.7), for every multiplier.
   With A.105, `ε_A = d mod 3` for every involution of `GT̂`: the `GT̂` half of A.13 is closed, conditionally on A.7
   and on A.105 using the same normalization of `Δ` (both say LM7_PUSH E.65; I did not compare the formulas). It
   does **not** give `α(N) = N`: `Δ` is one bit, the signed image of `ω_α` (A.111). Main A is not moved;
   GT_TOWER_CHECK B.3/B.6 tried the method of E.44 on involutions and records where it fails.
2. **LM4_SUCCESSOR E.30–E.40 against DELTA_ON_GT task B.3.** The counts agree (542 objects, 1620 arrows).
   LM4_SUCCESSOR E.32 ("orders 6 and 10 occur") agrees with DELTA_ON_GT B.32 (`D₃`, `D₅`). DELTA_ON_GT left the
   relations Open (B.33); EXIT_TOWER B.25 and GT_TOWER_CHECK B.5 give 1080 relators for one realization.
   LM4_SUCCESSOR's 14 families in 16 `S₅`-orbits and EXIT_TOWER's nine object families and fourteen arrow families
   are consistent as counts; I did not compare the family tables. Two runs (LM4_SUCCESSOR, GT_TOWER_CHECK) say
   they looked at the original scans, fetched from the archive's site; our own look at scans 31–36 is still due,
   now with a fourth point: 1/4 against the transcription's 1/3.
3. **LM4_SUCCESSOR B.42–B.45 against DELTA_ON_GT task B.5.** DELTA_ON_GT B.15 is an existence statement with
   invariants read on `B̂/R_nil(N)`, `N = ker q₁₂`; they are constant on the set of lifts, so B.15 stands under the
   lift-set reading. Its report says "the R2 witness" and "the repaired D.46 lift" as if each were one element:
   wording to correct wherever it is quoted. GT_TOWER_CHECK A.2 states the family reading outright.
4. **LM4_SUCCESSOR A.121 (Enriquez 2014, Proposition 2.20) against EXIT_TOWER's tower action.** Different inputs.
   EXIT_TOWER and GT_TOWER_CHECK build the genus-one action from the quilt presentation
   (Hatcher–Lochak–Schneps, Nakamura–Schneps) and the relation `𝒥(A) = A`, with the Schreier coefficient `c₂` and
   "no identification with the symmetrizer extension of the Kummer cocycle" (A.6.1). The Enriquez input of
   GT_TOWER_CHECK is another theorem (2007, Theorem 8.1, the profinite distribution relation; A.5.3, B.1.7).
   Nobody has proved that Enriquez's genus-one action of `GT̂` is the action of A.6.1. I did not open LM4_SUCCESSOR
   A.121 or either paper. LM4_SUCCESSOR A.1 (Known: Collas's genus-one theorems are for `IΓ`) combines with E.43
   and E.44: if `𝒥(A) = A`, then `IΓ` is the diagonal copy of `GT̂` and those theorems hold for all of `GT̂`.

## 4. Implications

**LM4_SUCCESSOR's 19 open rows.**
- **A.13:** `GT̂` half closed as in 3.1. For `GT̂₀`, `Δ` is now one of infinitely many characters vanishing on
  `GT̂` (and on conjugates of `c`): each is an invariant of conjugacy classes of involutions (hunch H3).
- **A.14, A.12, C.14 (gates A.39/A.45, `α(N) = N`):** not moved. New tools for a successor: `D_P(F) = cFc` and
  `D_L = id` on `GT̂` (B.1.8); the Kummer distribution for every element of `GT̂` (A.5.3); the same-parameter
  statements B.1.7, B.4.1, B.4.2. Routes to mark as tried: E.44's method on order two; Herfort–Zalesskii;
  Wykowski 2026.
- **B.12 (P5 on all of `GT̂`):** GT_TOWER_CHECK B.1.7 with `N = 5` is the statement LM4_SUCCESSOR's intake hoped
  for (the quotient by the rotation of order five, same parameter). Whether it is literally the resolvent identity
  of B.53 must be checked (hunch H2).
- **B.38, B.39, B.34 (gate B.75.6, `𝒦 = 1`):** not moved. Consistent with LM4_SUCCESSOR B.1–B.3: for `p`-groups and
  for solvable groups in genus zero the centralizer is the closure (A.1.1, A.1.2); `A₅` is untouched. A.4.38
  measures the difficulty at a finite level: in the 630-state ten-point quotient the image of the ordinary
  centralizer has index `2^{13}·3^{208}` in the finite centralizer.
- **A.105:** used in 3.1. **E.10:** EXIT_TOWER E.47 (faithfulness in genus ≥ 3) is context; nothing decides it.
- **B.26, B.27, B.40, B.41, C.4, C.26, D.9–D.12:** nothing here bears on them.

**`04_ANABELIAN_A1_SUCCESSOR\PROMPT.md`** (`TO_SEND\9_Archive_maths_prompts\`; I searched it, did not read it).
Nothing in the GT line changes an item. One piece of context for N4: EXIT_TOWER E.77. Its file was last written
at 21:49 UTC today, so someone is working on it.

**`08_SECTION_GHOSTS\PROMPT.md`** (already carries GT_TOWER_CHECK Part C).
- The transcript adds nothing to Part C; its line 26 says so correctly.
- **L5 needs one sentence.** It says the ghost of `GT̂₀` is killed "not level by level". GT_TOWER_CHECK A.4.1 and
  C.5 say the opposite for that ghost: a finite five-point level excludes it, by compactness (explicitly:
  A.4.57), though no relative-abelian, class-two or odd level does (A.4.41–A.4.61). For the section ghosts the
  compactness argument is not available (the prompt's L3). So the two kinds of ghost differ exactly there. Add
  A.4.1 and A.4.57 beside L5 and to task C.3 of the prompt.
- Its three-hour check and checkpoint paragraphs: GT_TOWER_CHECK shows the same pattern as LM4_SUCCESSOR. The
  Open rows were 13 at checkpoint 06 (transcript line 1424) and 13 at checkpoint 11; every hourly review said
  continue; checkpoint 11 was lost to the size limit.

**The expert's pages.**
- `EXPERT_E49_IMPLICATIONS_20261117.md`: its conditionals now rest on two runs of one model. Its referee points 1
  to 4 are answered by the run (section 2); point 2's finite level exists as a theorem, not as a computation. Its
  question 2 ("what separates `GT̂` from `GT̂₀` besides `Δ`") has an answer: `𝒳` of dimension `ℵ₀`. Its line
  "LM8_PUSH C.3 needs E.44" becomes: C.3 is **true for the physical marking and false for the literal one**.
- `EXPERT_DELTA_TAU.md`: T4 refuted (as the expert already wrote). T2: the characters that factor through the
  frame pair are `0` and `Δ` (DELTA_ON_GT B.1), but the full space vanishing on `GT̂` is infinite-dimensional, so
  the hunch H2 ("exactly one bit") holds only for the frames at the two elliptic points. T3 stays for `GT̂₀`.
- I3 (every prime-power subgroup of a sphere group): proved in genus zero with all branch points marked (B.4.1)
  and for the hyperelliptic quotient of genus two (B.4.2); all genera Open (B.4). I4: tried, fails as posed (B.3).
- Unsent LM7_PUSH successor and LM8_PUSH: S.1 and C.8 can cite A.7 after a referee; S.11 refuted; C.9 ("on `GT̂` no
  character trivial on Galois is known") stands, strengthened by B.2.2 and B.4.3.

**The Longue Marche companion and the editions.**
- §§46–47: the loop equations alone (`GT̂₀`) are too large by infinitely many independent signs; with the pentagon
  the condition of §47 holds in LM2's physical marking (B.1.8). The companion must state the marking: with
  `x_L = y_P⁻¹`, `y_L = x_P⁻¹` exchanged, the literal statement is false (B.1.2).
- Whether §47 alone gives the pentagon, or even `Δ = 0`, is Open (B.1). This is the companion's sharpest open
  question on these sections.
- Cote 148, scans 31–33: 1/4 against 1/3 in the first-pass transcription. Check our scan; if it is 1/4, the
  edition changes in every language. Scan 12 dictionary: DELTA_ON_GT R11, B.24, B.25.
- If E.42 with A.6 holds, the two-level principle of the Esquisse holds for the full completions in all genera.
- Before publication: nobody outside the runs has checked a proof; the PDF check is at step 1 only (section 6).

## 5. Hunches, as questions (mine, unchecked)

**For GPT-6 Astra (ChatGPT Pro mode).**

- **H1 (a referee task of its own).** *Prove or refute, in a self-contained note with every map written out:
  every element of `GT̂` satisfies Nakamura–Schneps's genus-one relation, that is `𝒥(A) = A` (EXIT_TOWER E.44,
  GT_TOWER_CHECK A.1), using only Boggi–Zalesskii Theorem A(iii) for `C₂²` on the ten-point sphere.* Why: `Δ = 0`
  on `GT̂`, the tower theorem E.42 and LM4_SUCCESSOR's use of genus one all rest on this one step, and it is the
  part that would be new in the literature. It should go to a different model family as well (Claude Fable 5.2 at
  effort max reading `part_a_centralizers.tex` and `part_a_tower.tex`), because both proofs so far are GPT-6 Astra.
- **H2.** *Is GT_TOWER_CHECK B.1.7 at `N = 5`, composed with forgetting to the twelve icosahedral points, the
  resolvent identity P5 of LM4_SUCCESSOR B.53 for every element of `GT̂`?* Why: it would close LM4_SUCCESSOR B.12
  by citation, and it tests B.1.7 against a statement proved another way for Galois.
- **H3 (involutions of `GT̂₀`, Lead 3).** `D_P` is onto (B.2.24), fixes `c` and commutes with conjugation by `c`
  (B.1.1); its kernel contains an element with `Δ = 1` (B.1.3), and all the characters of B.2.30 are independent
  on it. The involutions in the fibre `D_P⁻¹(c)` are the classes of `H¹(⟨c⟩, ker D_P)`.
  *Compute `H¹(⟨c⟩, ker D_P)` and the values of `Δ`, `η`, `d̄_p` on it.* Why: LM4_SUCCESSOR A.18 shows R2 has no
  equivariant form, so an involution with `Δ = 1` cannot come from R2; `ker D_P` is a structured subgroup where
  the `c`-action is explicit, and one class with a non-zero character is a second conjugacy class of involutions
  in `GT̂₀`. If every class is trivial, that is a first real restriction on Lead 3.
- **H4 (§47 against the pentagon).** On `C_L` every `Δ ∘ D_Pⁿ` equals `Δ` (B.2.28), so `Ξ(C_L)` lies in the two
  constant sequences. Take `g₀` with `Ξ(g₀) = (1, 1, 1, …)`; then `C_L ⊄ ker Δ` exactly when the twisted Lang
  equation `h⁻¹ · (g₀⁻¹ D_L(g₀)) · D_L(h) = 1` has a solution `h ∈ ker Ξ`. *Decide whether it has one (B.1.10
  holds the equation in the run's coordinates).* Why:
  it turns the Open row B.1 into one surjectivity statement about an endomorphism already proved onto (B.2.24),
  and its answer says whether Grothendieck's condition of §47 is weaker than Drinfeld's pentagon at the level of
  one sign.
- **H5 (the independent finite check, on the genus-one side).** The proof of A.3 reads `Δ` on `K^{ab}` modulo 12
  inside `Γ̂_{1,2}`, and the recognition of the CM centralizer is already effective at small levels (A.4.6, A.4.12,
  A.4.14, A.4.18: a detector of order `32·3^{14}`). What makes the level of A.4.57 enormous is the finite form of
  the naturality chain (A.C14) through the nine-, ten- and twelve-point configurations. *Find a finite quotient of
  `B₄` modulo its centre, compatible with `φ` and with the detector of A.4.18, on which (A.C14) can be tested
  directly for every pentagon shadow at that level, and run the census there.* Why: every `Δ = 1` survivor of
  both runs was found on relative-abelian or class-two quotients of `Γ_{0,5}`; the proof places the obstruction in
  the action on `Γ̂_{1,2}`, in which `Γ̂_{0,5}` has index 24. I have not checked that such a quotient exists at a
  feasible size.

**For the Longue Marche field expert (Claude Fable 5.2 at effort max).**

- **H6.** Is "Nakamura–Schneps's relation holds on all of `GT̂`" open in the literature as of 2026 (Lochak 2025;
  Lochak–Nakamura–Schneps 2026; Basualdo Bonatto–Robertson 2026)? The run's audit says the 2026 papers still use
  the subgroup. This decides whether H1 is a referee task or a publication candidate.
- **H7.** `𝒳` has dimension `ℵ₀` and is not finitely generated under descent. Does the idempotent picture of
  `EXPERT_DELTA_TAU.md` extend: is each `d̄_p` the sign of an idempotent at a pair of primes (2 and `p`), with
  `GT̂` the locus where all these signs are constant? Why: it would give the list of B.2.30 a meaning, and say what
  the full maximal elementary 2-quotient of `GT̂₀` over `GT̂` is.
- **H8.** EXIT_TOWER E.77 gives CS and RGC for `GT̂`. From memory, unverified: Hoshi–Mochizuki–Tsujimura confine
  subgroups with a further property to conjugates of `G_Q` (DELTA_ON_GT R10 quotes their Theorem 5.17(ii) for
  algebraically ample subgroups). Is the missing property for `GT̂` equivalent to `G_Q = GT̂`, and does the tower
  action of A.6.1 help to test it? Why: after B.2.2 and B.4.3 no invariant separating `G_Q` from `GT̂` is left on
  our table; this is the one structural handle in the returns.
- **H9.** Should the wording "ghost" keep covering the `GT̂₀` witness, now that a finite level kills it (A.4.1)?
  The memory note defines ghosts as passing every test at one prime, nilpotent level or finite level.

## 6. What I checked myself

Recorded in `<local>/Documents\pro_intake_20261117\CHECK_EVENTS.tsv`. My program (written from the
statements; no code of the returns was run):
`<local>/Documents\pro_intake_20261117\GT_LINE_checks_20261117.py` (14 checks, all pass).

- The three register counts, by status and by Part.
- GT_TOWER_CHECK A.3: the algebra of (A.C6) (forward and inverse identities; the quartic is the three-division
  polynomial divided by 3; `a = −3Z`, `b = −2Y` gives `D = 108(Y² − Z³)`); the conjugation table (A.C8) in `B₄`,
  through the Artin action on `F₄` (it holds for `g ξ g⁻¹`); the matrix facts behind (A.C2) and (A.C11)–(A.C13);
  the last step, from `TC = R₊^k CM` to `ε₃(T) = ε₂(W)`, for every even `j` and both signs `ε`; the contradiction
  for `T = 5I`, `W = I`.
- GT_TOWER_CHECK B.2.2: each order in the table is 11 to the cumulative dimension of the graded spaces recomputed
  by the Longue Marche expert (`KNOWLEDGE_HANDOFF_LM.md`: special invariants `0,0,1,0,1,0,2,1,4`; `grt₁`
  `0,0,1,0,1,0,1,1,1`). Consistency only.
- By hand: `[Q(ζ₈, 2^{1/8}) : Q] = 16`; `5!/10 = 12`; `1620 − 542 + 1 = 1079`; DELTA_ON_GT B.32's proof read and
  followed.
- Build logs: GT_TOWER_CHECK 408 pages, 0 overfull boxes; DELTA_ON_GT 162 pages, 0 overfull boxes. EXIT_TOWER has
  no log in the extracted folder. No page was rendered by me: step 2 of the PDF check is not done.

**Not checked by me:** the naturality equation (A.C14) and the chain of comparisons behind it; `𝒥(A) = A`; the
use of Boggi–Zalesskii's theorem; `part_a_label_repair.tex` (not read); every statement of Part B beyond the
arithmetic above; all of Part C; every computation of the runs; every citation.
