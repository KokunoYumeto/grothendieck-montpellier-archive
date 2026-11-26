# Intake of ALP_CONNES checkpoint 28 (prompt 55), by diff from checkpoint 26

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode) and is still going.

Return: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\ALP_CONNES_checkpoint_28_20261123T0010Z_unzipped\ALP_CONNES`.
Earlier intake: `INTAKE_ALP_CONNES_20261122_cp26.md`.

Masullo's draft is not a proof, and nothing here is a fix of it.

## 0. Method, read and not read
- **Baseline:** cp26 states rebuilt from movement review 19 plus the cp26 diff. Against it, 20 rows are new and 8
  changed state; 1039 rows in all.
- **Read in full:**
  - every new and changed row;
  - the opening and the main-gate table of reviews 21 and 22, compared row by row with review 20;
  - the G135 statement and its unit and saturation step.
- **Statements only:** G136-G139, as their rows give them.
- **Not read:**
  - the proofs of G136-G139, and the rest of G135 (the analytic class formula interval);
  - the Q-B08 sources: DELTA23, DELTA_ON_GT, LM7;
  - the cote 16 scan readings.

## 1. What moved
All new results are in the cubic branch at the coefficient prime 269.

| rows | result | our check |
|---|---|---|
| G135 (QG620-622) | Three more degree-12 quartic reflection fields, d = −11, 2, −22. Each has class number prime to 269, by the G129 method. | **computation, d = 2:** the five units have monic integral characteristic polynomials with constant term 1, equal to the JSON's. The 12 residue maps at ℓ = 40351 exist, and the saturation matrix has rank 5 over F₂₆₉, with determinant 30877898400 ≡ 106 mod 269 as printed. Our own code read the run's numbers, not its programs. The analytic interval step was not rechecked. |
| G137 (QG628-630) | The same for the three ramified quartic fields of the second residue | statement read |
| G136 (QG624-627) | A quartic auxiliary seed (q_aux = 16141) on a smaller host, with gap 3 < 4; native support and M1-M5 for the first quartic label at e ≡ 267 | statement read; retained modularity inputs |
| G138 (QG632-635) | The same at e ≡ 133, with its own ordinary branch | statement read; retained inputs |
| G139 (QG636-639) | Conjugate localizations and selected-component transport for ψ₅^σ τ₈^a τ₂₆₉^b, with σ = ±1 and a, b ∈ {0, 1}, at both residues. This gives **sixteen character/residue combinations** with M1-M5 and normalized length and counting bounds (moduli 10, 40, 2690, 10760). | statement read; retained inputs |
| Q-B08 (changed) | DELTA23's identity, recovered and checked by the run: (−1)^δ = χ₁₂(u_H) on H. On the full group, u is defined only modulo {1, 11}, and it is **not** the cyclotomic multiplier character. | statement read |

**What Q-B08 means for what we hold.** Our record cites "Δ on GT-hat = χ₁₂∘u (DELTA23 intake L1)", for instance in
the direction of 21 Nov, point (3). If the run is right, that holds only on the subgroup H. On the full group, u is
defined only modulo {1, 11}, and it is not the cyclotomic character. Before any further use, check this against the
DELTA23 intake itself.

**New work in progress, not promoted:**
- cote 16, scans 43-49: Grothendieck's 1966-67 pages on algebraic correspondences and the Lefschetz index, read
  against their publisher transcriptions, which are not ours;
- a "cutoff399 conditional transport";
- a q_t de Branges flow audit, with an exact mixed pairing but no positive estimate.

## 2. The four main gates
None moved: H04.4, RH for the cubic character, the T51 limit without zero location, and the lower bound for a₂.
Reviews 21 and 22 say "Movement: yes" for closing cubic host and model gates; in the main-gate table only the cubic row
Q7 and the Grothendieck-dictionary row changed.

## 3. The Connes-Consani F₁, Deninger and BC/BCM lines
Nothing appeared. Rows Q1-Q6 and the BCM follow-up row of review 22 are word for word those of review 20. No new
row concerns F₁, Deninger or BC systems.

## 4. Outreach and Hexagon
Nothing new. The G129 and G135 type certificates stay "not ready" until the interval runs are replayed and the
certification literature is compared.

## 5. Not for GitHub
- `input_material/`.
- The .lean interface files.
- `evidence/ALPOGE_remark.txt` and the other third-party texts named in the cp24 intake.
- The publisher transcriptions of cote 16 that the run read, wherever they sit in the return. Not located by me.
