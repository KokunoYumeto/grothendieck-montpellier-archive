# Intake of CUE_GCT (prompt 36), checkpoint 01, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high, the agent that also took in GCT_GINEQ and GCT_KRON (launched by the main
session, Claude Opus 5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode): run CUE_GCT_20261121_R1, started 00:49:46 UTC. Its first checkpoint was
written at 01:35 UTC, after 45 minutes of work. The run is still going.

## 0. What was read

- **Return folder:** `research_returns\CUE_GCT_checkpoint_01_20261121T0135Z_unzipped`, the only checkpoint present.
- **Prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\36_CUE_GCT_random_matrices_and_isolation_through_GCT\PROMPT.md`.
  I read its sections "The task" and "What to deliver".
- **Read in full, with proofs:** in `deliverables\CUE_GCT.tex`,
  - G-01 to G-06 (lines 1449-1528);
  - P-11 (lines 3152-3196);
  - I-18 (lines 2786-2850).
- **Read at statement and scope level:**
  - the zero-statistics dependency section, P-Z01 to P-Z05 and its dependency table (lines 3196-3300);
  - `LEDGER.md`, `QUESTIONS.tsv` (all rows) and `TRANSCRIPTION_NOTES.tsv` (all 9 rows).
- **Not read:** the proofs of R-01 to R-14, I-01 to I-17, P-01 to P-10, G-07 to G-09, and the finite certificates
  (R-12, R-13, G-08, I-13).

## 1. Verdicts

| id | statement | my check | verdict |
|---|---|---|---|
| G-01 | in B(G), s_2 = b_2 + E and E² = E + [Inj({1,2},E)]; 2b_2 + E = E² fails; in representation K_0, V² = 2Λ²V + ψ²V | the free C2-orbit (the same computation as in my GCT_KRON intake, `scratchpad\kron\marks.py`); the character identities | confirmed. An **independent second run** reaching the same correction to cote 133, scan 019, and to SA17's study as GCT_KRON A-001. Its K_0 form (ψ² in place of E) is the right replacement |
| G-02 | the universal formula for λ^i(xy) needs λ^i(x), λ^i(y); so cote 133 scan 006 lines 25-26 read λ^i | set y = 1; algebraic independence of e_1, ..., e_i | confirmed. It agrees with our study's scan 6 note and Michel Hua's correction |
| G-03 | for each D, two honest G_m-representations equal modulo F^{D+1}_γ with different weight multiplicities | the difference is (1−L)^{D+1}, in F^{D+1}_γ; the ranks are 2^D | confirmed |
| G-04 | integral orbit-closure coefficient matrices; base change is exact over Z[1/δ_d] | elimination with an invertible minor | confirmed (standard) |
| G-05 | Det_n contains every ternary form, so multiplicities with at most 3 rows equal the ambient ones | Beauville, Prop. 3.1(a), with an L in Pic^{g−1} outside Θ; GL dense in End; the highest-weight space lies in the ternary coefficients | confirmed. Classical input (Dickson, Beauville). **The same result as GCT_KRON O-007** |
| G-06 | the quaternary determinantal locus has dimension at most 2n²+2; the four-row gate is nonvacuous for n ≥ 4 | the stabilizer of (I, diag, generic) is scalar; the identity C(n+3,3) − (2n²+2) = C(n−1,3) checked algebraically | confirmed |
| P-11 | a common number-field point that encodes a hitting set is polynomially interconvertible, over Q, with an explicit integer hitting set; no GRH | grid interpolation; Lagrange denominators divide (M−1)!; Φ_ℓ irreducible of degree > d(M−1) | confirmed (elementary) |
| I-18 | regularize-then-specialize fails for width-2 ROABPs; the criterion is a unit Plücker minor | L(x)R(y) = (y−x)E_11; the regularized pair at 0 is triangular with (1,1) entry ε(1+ε) | confirmed |
| P-Z01 to P-Z05 | what A (Alpöge) and M (Masullo) discharge among the zero statistics | table read against the stated hypotheses | carried as background without fault found (see section 3) |
| R-01 to R-14, I-01 to I-17, P-01 to P-10, G-07 to G-09 | rectangular bridge, isolation, purity samplers, low-variable determinantal bounds | statement level | not read in full |

**Counts:** 8 confirmed by targeted proof check (G-01 also by computation); 5 scope statements carried without fault;
about 50 at statement level. None refuted.

## 2. What is new

- **The cote 133 corrections (G-01, G-02).**
  - G-01 confirms independently the correction to scan 019 and to our study that GCT_KRON A-001 made: two runs, with
    a computation, now agree.
  - G-02 confirms a reading already in our study.
  - `TRANSCRIPTION_NOTES.tsv` adds forced readings for cote 133: scan 019, line 10 (σ_t, not "σ_{unsure t}"),
    line 13 (the list λ^j, 1 ≤ j ≤ i, not "λ^{j|i}") and line 20 ((1 − tL)^{-1}, not "1 ∓ tL"); scan 028, line 10
    (ξ = cl(E), not "∈"). All are mathematically forced, and the ink was not inspected.
- **G-05.** Classical (Dickson; Beauville 2000), and duplicated across runs.
- **G-06.** A clean dimension count. It is likely known in substance: the generic quaternary form of degree ≥ 4 is not
  determinantal.
- **P-11.** Elementary but useful. It shows exactly where number fields cannot add anything to ROABP PIT: an explicit
  number-field encoding is already a hitting set. Only a Frobenius/Chebotarev encoding (P-08) could add something,
  and that is the gate.
- **I-18.** A small new counterexample that locates the obstacle of the isolation transfer (I-17 to all width two): a
  unit Plücker minor must survive specialization.
- **R-13.** The quaternary permanent dominates exactly for sizes 1-16 and fails for all sizes ≥ 17, with 3,348,864
  checked certificate entries. It may be new. It is not read, and the run's root review is in progress.
- **Against tonight's runs.** G-05 equals GCT_KRON O-007. The low-row exclusions of G-09 should be compared with GCT_KRON
  M-007 to M-015: two runs are attacking the same gate, the rows of an actual multiplicity obstruction, by different
  determinantal constructions. GCT_KRON's staircase is far stronger at present.

## 3. Scope of the two proofs

The dependency table (CUE_GCT.tex, after line 3240) is careful, and I found no overclaim:

- **Uses Alpöge (RH for ζ, GRH for Dirichlet L-functions), correctly:**
  - Montgomery's pair correlation with supp f̂ ⊂ (−1, 1) (P-Z01);
  - Rudnick-Sarnak, Theorem 1.2 for m = 1;
  - Hughes-Rudnick §8: Theorems 8.1 and 8.3, and Corollary 8.2, liminf_q min_{χ≠χ_0} x_{χ,1} ≤ 1/4;
  - Chebotarev encodings over abelian fields (P-08).
- **Conditional on Masullo, correctly:** Gao-Zhao's quadratic and quartic Hecke families over Q(i). Those
  characters define extensions that are in general non-abelian over Q, so Dirichlet GRH does not cover them. Also
  P-08 over arbitrary number fields.
- **Beyond both, correctly flagged:** Iwaniec-Luo-Sarnak (RH for GL_2 L(s,f) and for sym² f on GL_3; Hypothesis S),
  Rudnick-Sarnak m > 1, the CFKRS moment recipe, and Berry-Keating.
- **No statement claims more than its input gives.** P-11 explicitly needs no GRH.
- **For the "what Alpöge makes unconditional" catalogue** (HEXAGON_CANDIDATES.md, the IA list): Montgomery
  (supported range), Rudnick-Sarnak m = 1, and Hughes-Rudnick §8 are three entries with exact locators. They are
  classical consequences, not results of ours.

## 4. Integration

1. **Cote 133.**
   - *The study.* The SA17 study correction in my GCT_KRON intake, section 1, now has two independent runs behind it:
     GCT_KRON A-001 and CUE_GCT G-01. Cite both in the study's replacement line.
   - *Our text of record.* The nine rows of CUE_GCT's `TRANSCRIPTION_NOTES.tsv` go to the transcription record of
     cote 133 as notes of forced mathematical readings at scans 006, 008, 009, 019 and 028. They are not ink
     corrections: each needs a look at the scan image before the transcription changes. The scan 008 Laborde/Lazard
     row repeats the study's image decision (Lazard). Keep that decision.
2. **GCT.**
   - *Where the two runs meet.* G-05/O-007 (at most 3 rows), G-06 (4 rows nonvacuous) and G-09 sit at the same gate as
     GCT_KRON's staircase. Their successors should share one ledger of the row gate, so that neither run re-derives
     the other.
   - *How the obstruction attack goes on.* The bridge is GCT_KRON's F010 (evaluation ranks). The run's R-05 and R-06
     (closure multiplicities as ranks of integral orbit-coefficient matrices, G-04) are the same object; the attack
     is computing those ranks at the first unexcluded shapes.
3. **PIT.**
   - *The obstacle.* It is located by I-18 and P-11: a Frobenius-to-nonvanishing map with polynomial degree and
     log-discriminant (P-08).
   - *What Alpöge gives there.* Over abelian fields, Alpöge gives the effective Chebotarev bound needed. The missing
     piece is an encoding of an ROABP's coefficient matroid into such a field. That is the next attack, and the
     successor should ask for it by name.
4. **Prompts 30-35.** Untouched. The zero-statistics table can serve prompt 35 (ZETA_TWO) as a checked dependency list.

## 5. Hexagon readiness (the five tests of `field_experts\HEXAGON_CANDIDATES.md`)

1. **G-01/G-02 with GCT_KRON A-001/A-002.**
   - *What passes.* They are complete, self-contained and checked: two runs and a computation.
   - *What fails.* Test 5: they correct an unpublished archive page and our own study. They belong in the cote 133
     companion. **Not a candidate.**
2. **P-11 and I-18.**
   - *What passes.* They are complete and confirmed.
   - *What fails.* They are elementary, so test 5 is weak. Test 3 fails too: the run is going, and they are steps
     toward the isolation gate. **Not a candidate alone.** They could go into a later note on "why number fields alone
     do not help ROABP PIT", if the run reaches the P-08 encoding.
3. **R-13.**
   - *The candidate.* The exact range of quaternary permanent dominance, 1-16, with a dimension obstruction from 17.
   - *Interest.* A finite certified computation of interest to the GCT community. Possibly a candidate.
   - *Gates left:* the final; an intake of its proof and certificates (by recomputation); a literature search.
     **Later.**
4. **The dependency table.** Material for the Reddit post and the IA catalogue, not a Hexagon paper.

## 6. Prompt updates for the successor of CUE_GCT

1. **Isolation main question.** Construct the Frobenius-to-nonvanishing encoding of P-08 for width-w ROABPs over
   abelian fields, where Alpöge gives Chebotarev. State the unit-Plücker condition of I-18 as a required property.
2. **GCT gate.** Attach the GCT_KRON ledger of the row gate (M-006 to M-015, the BIP staircase) and ask the run to
   attack its open shapes, not to re-derive the at-most-3-rows and 4-rows cases.
3. **Cote 133.** Supply the scan images of cote 133, scans 006, 019 and 028, so that the TRANSCRIPTION_NOTES rows can be
   decided on the ink.
4. **R-13.** Ask for its certificates in a form an independent script can recheck: the matrices and the primes used.
5. **Provenance.** Name the run "GPT-6 Astra (ChatGPT Pro mode)".
6. **No minimums and no ways out**, as before.
