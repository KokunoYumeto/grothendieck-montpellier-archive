<!-- Saved by the main session (Claude Opus 5.5 Max) from the agent's final message, 18 Nov 2026: the harness refused the sub-agent's own write of this file. Agent ae4ae3dc17acaa440, Claude Opus 5.5 at effort max. -->

# Sweep 1, scope tower: summary (text of SUMMARY.md)

By Claude Opus 5.5 at effort max (sweep 1, scope `tower`), 18 Nov 2026, from `results_register/REGISTER.tsv` and the returns. The runs are by GPT-6 Astra (ChatGPT Pro mode). No sub-agents were used, and nothing outside this folder was written.

## Files

| File | What it holds |
|---|---|
| `PLACEMENT.tsv` | the outline place of each of the 2,239 rows |
| `MERGES.tsv` | 90 rows in 60 clusters |
| `CROSS_RUN_EDGES.tsv` | 149 resolved cross-run links |
| `FLAG_VERDICTS.tsv` | 158 verdicts |
| `CHECK_EVENTS.tsv` | 7 checks |
| `CORRECTIONS.md` | 17 items |

How to read `MERGES.tsv`: each row is canonical, member, relation. The canonical is the item the handbook keeps.
- **same:** the same mathematics. The member may be Open in its own run and decided by the canonical.
- **stronger / weaker:** the member says more / less than the canonical.
- **refines:** the canonical sharpens the member.
- **corrects:** the canonical corrects the member's statement or written proof.
- **refuted by:** the member is refuted by the canonical.

## 1. Counts

**Rows:** 2,239, of which 1,865 Proved, 179 Refuted, 85 Known and 110 Open.

| Run | Rows |
|---|---:|
| LM4_SUCCESSOR | 401 |
| LM8_PUSH | 304 |
| EXIT_TOWER | 283 |
| LM4_FINITE_GROUP_ACTIONS | 272 |
| DELTA_ON_GT | 221 |
| GT_TOWER_CHECK | 180 |
| LM8_LIE_APPROXIMATIONS | 167 |
| LM5_MULTI_GALOIS_TOPOI | 129 |
| LM1_GROUP_SCHEMES_rerun_20261112 | 84 |
| LM2_LOOP_EQUATIONS | 79 |
| EXIT_ONE_TYPE | 63 |
| CYCLOTOMIC_KERNEL | 56 |

**Placement:** 2,192 rows by script, 47 by reading.

| Chapter | Rows | Proved | Refuted | Known | Open |
|---|---:|---:|---:|---:|---:|
| I.1 GT̂ and its finite subgroups | 1,326 | 1,108 | 97 | 45 | 76 |
| I.2 The tower and its Lego | 471 | 386 | 56 | 22 | 8 |
| I.3 Dessins and the Galois action | 17 | 9 | 4 | 2 | 2 |
| I.4 Anabelian geometry and sections | 364 | 316 | 15 | 15 | 18 |
| I.5 The Fermat curves | 24 | 16 | 2 | 1 | 5 |
| IV.1 Stratified spaces | 36 | 30 | 5 | 0 | 1 |

The sections under these chapters are in `PLACEMENT.tsv`; E.3 is section I.1.2.

**Flags:**
- **Proved rows that cite a Refuted row (83):** all sound. Each uses the refutation or the corrected form, because most Refuted rows state the refutation itself (CORRECTIONS 13).
- **Dependencies that name no id (75):**
  - 35 are literature locators.
  - 32 are other runs' ids: LM7_PUSH E.58/E.61/E.65/D.50; SECTIONS_OVER_Q A.44/A.65/A.72/A.196; LM4_FINITE_GROUP_ACTIONS D.31/D.35/D.49; LM4_SUCCESSOR A.39/A.42/A.81; LM8_LIE G.10.
  - 7 are sub-items of the run's own statements.
  - 1 is literature plus an unlabelled locator.
- **Proved rows that rest on an Open row of the same run (15):** sweep 0 does not flag these. I read one: EXIT_TOWER E.49 ← E.24 is context, not a step.

**Lineage:** sweep 0 has 19 cross-run links in this scope; with TeX underscores and the short run names resolved there are 149.

## 2. Corrections that matter most

1. **E.3 is proved on record but stands on one model** (CORRECTIONS 1).
2. **C^φ (the descent group of §47) has two markings under one formula** (CORRECTIONS 2–3).
   - LM8_PUSH's C^φ is the physical C_L. So LM8_PUSH C.3, the second half of LM8_LIE B.28 and LM2 E.3 are decided by GT_TOWER_CHECK B.1.8.
   - The open "C^φ ⊆ ker Δ" is two different questions (C_L and C_P).
   - Sharpening: C_P ∩ GT̂ = {1, c}.
3. **The quadratic characters vanishing on GT̂ form a space of dimension ℵ₀: LM8_PUSH C.30 has it unconditionally, a day before GT_TOWER_CHECK B.2.25** (CORRECTIONS 4). B.2.25's family Δ∘D_Pⁿ vanishes on GT̂ only through A.7.
4. **LM6's Fermat theorem (outside this scope):** LM8_PUSH D.22 refutes a divisibility step cited for it, and D.23 re-proves it with the corrected cusp constant (CORRECTIONS 7). I checked the arithmetic core: q = λ²/256 (1 + O(λ)), so v₂ = −8.
5. **The register needs three repairs** (CORRECTIONS 12–14):
   - the lineage parser;
   - Refuted rows split into the claim and the refutation;
   - Proved rows that carry an open part split in two.

## 3. E.3: what is proved, by whom, and what each run did with it

**The question.** LM7_PUSH E.3 (Open) asks whether GT̂ reaches the extra CM coset. Δ is LM7_PUSH E.65's CM parity character, Δ = ε₃(T) + ε₂(W).

| Run | What it did with E.3 |
|---|---|
| LM8_PUSH cp17 (16 Nov 02:52) | C.21: the GT̂ CM image is one of two, according to Δ\|GT̂, so E.3 is exactly Δ\|GT̂ ≠ 0. C.23: a gentle Δ = 1 element whose descended Δ is 0. C.8 leaves Δ\|GT̂ open. |
| DELTA_ON_GT cp05 (16 Nov) | A.84 Open. Reduction (A.112, A.103, A.87): Δ\|GT̂ = 0 ⟺ ν₄ ≡ κ_d mod 2 ⟺ d₂ = e₃. Shows what cannot see Δ; proves GT̂ ⊊ GT̂₀ (P.11); a second witness of parity (0, 1) (B.15). |
| EXIT_TOWER cp28 (16 Nov) | E.49 claims Δ\|GT̂ = 0, from E.44: 𝒥(A) = A for every A ∈ GT̂, via Boggi–Zalesskii Theorem A(iii) for C₂². |
| GT_TOWER_CHECK cp10 (17 Nov) | A.1 confirms E.44 and supplies its missing parts. A.3 repairs E.49's two label comparisons. A.7: Δ\|GT̂ = 0 for every multiplier, and G_Q ⊆ GT̂ ⊊ ker Δ ⊊ GT̂₀. A.5 proves DELTA_ON_GT A.103's two vanishing assertions. A.4, the independent finite census, is Open: every level computed has Δ = 1 survivors. |
| LM4_SUCCESSOR cp40 | A.105: (−1)^Δ = ε_A ε_u. With A.7, the GT̂ half of A.13 closes. |

**Who has checked what:**
- The intake by Claude Fable 5.2 at effort high checked the algebra of (A.C6), the conjugation table and the last parity step.
- I checked that E.49 does not rest on the open E.24.
- Unchecked outside GPT-6 Astra: (A.C14), 𝒥(A) = A, and the use of Boggi–Zalesskii.

**The gate.** Everything rests on 𝒥(A) = A on all of GT̂. It would be new in the literature and needs a referee from another model family.

## 4. Per chapter: what is proved, what is open, and the strongest reduction

### I.1 GT̂ and its finite subgroups

**Proved:**
- Δ|GT̂ = 0.
- GT̂ ⊊ ker Δ ⊊ GT̂₀ (GT_TOWER_CHECK B.2.1, B.2.3; also DELTA_ON_GT P.11, LM8_PUSH P.4, LM7_PUSH D.52).
- The quadratic characters vanishing on GT̂ form a space of dimension ℵ₀ (LM8_PUSH C.30; GT_TOWER_CHECK B.2.25).
- The §47 condition holds on GT̂ in the physical marking (GT_TOWER_CHECK B.1.8).
- C(c) = N(⟨c⟩) = {1, c} in 𝒫 and in GT̂ (LM4_SUCCESSOR A.6, A.36).
- The GT̂ monoid is a group (C.31). The literal form of Furusho's Question 14 is false (C.34).
- The finite-subgroup catalogues. LM4_SUCCESSOR C.5–C.23 and D.1–D.6 re-prove LM4 D.42, D.70, D.74–D.78 and C.88–C.92.

**Open, with the strongest reduction:**
- **G_Q = GT̂? (EXIT_TOWER E.24)**
  - E.77: CS and RGC hold for every closed subgroup between G_Q and GT̂.
  - No separator is known: same images in the exponent-11 quotients of class 3–10 (B.2.2); the origami invariant is constant on GT̂ (B.4.3).
- **Main A: are all involutions conjugate to c? (LM4_SUCCESSOR A.14; GT_TOWER_CHECK B.3/B.6; LM4 D.12)**
  - Reduced to one third-cusp equation x^d u⁻¹ y^d u ~ (xy)^d at d = d_α (A.39, A.45).
  - On GT̂ this is the hexagon for (d_α, u) (A.37).
  - The method of E.44 fails here (B.3).
- **Levels and parity (A.12, A.13):** A.13's GT̂ half follows from A.7. For GT̂₀ the reduction is A.105/A.111.
- **Main B: 𝒦 = 1? (B.38, B.39, B.34; LM4 F.7)**
  - Reduced to the uniform finite-cover condition B.75.6, locally 𝓘 = 𝒦_loc^δ (B.164–B.166).
  - Known: 𝒦 ∩ G_Q = 1; abelian ⟹ trivial; Sylows free pro-p of rank ≥ 2; 𝒦 lies in the closure of [P, P]; 𝒦_N = 1 for N = 2, 3, 4, 6.
- **C_L ⊆ ker Δ? (LM8_PUSH C.8)** Its form is the twisted Lang equation of hunch H4 in the GT line intake.
- **C_P ⊆ ker Δ? (GT_TOWER_CHECK B.1)** d₂ = 0 is proved; the comparison e₃ = ε₃(T) + Ψ₃/2 is left.
- **Graded and envelope questions:**
  - LM8_PUSH G.1–G.3 (λ in degree eight; G.6 gives the index for δ = λ − 31/20).
  - LM2 B.g11 (integral lift of the weight-7 solution); LM8_LIE B.24d.
  - LM1's nine open rows: the dictionaries are proved, the comparisons are open.
- **Level-zero comparison (LM4 C.12; LM4_SUCCESSOR D.9–D.12):** reduced to an injectivity of π₁ (D.12); D.17 fills through maps, not homeomorphisms.
- **LM4_SUCCESSOR C.4 (K = 1?):** K is pro-odd, and a counterexample would need an infinitely generated free pro-p quotient.

### I.2 The tower and its Lego

**Proved:**
- GT̂ acts on the full profinite tower (EXIT_TOWER E.42 + GT_TOWER_CHECK A.6).
- Injective, with closed image, for g ≥ 3 (E.47).
- The MDT and exit systems.
- Cote 148: 542 objects, 1620 arrows, 16 S₅-orbits, 1080 relators for one realization.
- LM5's topoi: gluing and hole filling.

**Open:**
- **E.45, surjectivity in genus ≥ 3:** only steps toward it, E.50–E.107.
- **GT_TOWER_CHECK B.4:** proved in genus zero with all branch points marked, and for the hyperelliptic quotient of genus two.
- **Germs (LM8_PUSH F.1, F.3, F.5):** special cases proved.
- **DELTA_ON_GT B.28 and LM5 F.45.**
- **DELTA_ON_GT B.33:** closed only for the specified realization, since the path classes form a torsor.

### I.3 Dessins and the Galois action

**Proved:**
- The arithmetic outer congruence image is units modulo squares (LM2 C.r1).
- GT̂₀ injects into Out (C.r5).

**Open:** LM2 C.d5 and D.6.

### I.4 Anabelian geometry and sections

**Proved:**
- Cusp inertia and arithmetic centralizers (CYCLOTOMIC_KERNEL A–C).
- The fixed subgroups of packet sections are the cusp inertia (LM8_PUSH A.1, A.9).
- Section ghosts:
  - finite support gives a rational point;
  - there are exactly 24 class-two sections above each ordinary pair.

**Open:**
- GT_TOWER_CHECK C.1–C.5.
- LM8_PUSH A.2, A.7, A.45, D.9 (A.2 is reduced to R_nil(π′)).
- CYCLOTOMIC_KERNEL D13, D15, E3, E4.
- LM8_LIE F.12, G.16, G.20.
- EXIT_TOWER E.T3 and LM5 F.44.

### I.5 The Fermat curves

**Proved:**
- Every Selmer section of U_n/Q is cuspidal for odd n ≥ 3.
- The full section set is the three cusp packets (LM8_PUSH D.23 with D.56).

**Open:** LM8_PUSH D.5, D.6 and H.1–H.3.

### IV.1 Stratified spaces

**Proved:** the exit categories, good compactifications and dual complexes of EXIT_ONE_TYPE.

**Open:** P3c-general.

## 5. Runs no intake had taken in, and what I found in them

**LM8_PUSH cp17** (not taken in; 304 rows):
- C.30 comes first on the quadratic characters vanishing on GT̂.
- C.1 and C.25 define C_L and show it equals the solution set of the harmonic primitive GF0; this decides C.3.
- C.21, C.23 and C.27 bear on E.3 and on descent.
- D.22 and D.23 correct the step cited for LM6's Fermat theorem.
- The CM curve y² = x³ − x over Q(i):
  - the fixed subgroups are the cusp inertia;
  - the sections are cuspidal for every first cover (S₃, D₈, Q₈);
  - 24 Eisenstein–Kronecker certificates, checked twice.
- A notation clash: Δ means both the CM character and Gal(K̄/K^ab).
- The report is 2.2 MB; I read its lead table and the rows named here.

**LM1_GROUP_SCHEMES_rerun_20261112:**
- No intake document names any of its 84 rows.
- Sixteen of its Refuted rows correct manuscript formulas (A.6, C.4, D.12, E.4–E.7).

**Taken in thinly:**

| Run | Rows the intakes name |
|---|---|
| EXIT_TOWER | 47 of 283 (parts A–D, E.50–E.107 and E.T1–E.T13 never read) |
| LM4_FINITE_GROUP_ACTIONS | 21 of 272 |
| LM4_SUCCESSOR | 84 of 401 |
| GT_TOWER_CHECK | 31 of 180 |

`PLACEMENT.tsv`, `MERGES.tsv` and `CROSS_RUN_EDGES.tsv` map these for a next intake. For example, LM4_SUCCESSOR C, D and E are, row by row, re-proofs of LM4 and LM6 statements.
