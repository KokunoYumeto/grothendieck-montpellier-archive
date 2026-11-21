# Intake of BR_PENCIL (prompt 44), checkpoint 01, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a17221e5, which also took in GCT_GINEQ, GCT_KRON and CUE_GCT;
launched by the main session, Claude Opus 5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode), run BR_PENCIL-20261121-R1, started 02:59 UTC, still going. It is the
successor of GCT_GINEQ; my GCT_GINEQ intake was its brief.

## 0. What was read

- **Return folder:** `research_returns\BR_PENCIL_checkpoint_01_20261121T0344Z_unzipped`, the only one present.
- **Prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\44_BR_PENCIL_border_rank_of_det4_and_per4_by_multi-dimensional_substitution\PROMPT.md`.
  A copy is in `intake\BR_PENCIL_PROMPT.md`.
- **Read in full, with proofs:**
  - `sections\substitution.tex`: R-01;
  - `sections\pencils.tex`: P-01 to P-08;
  - `sections\uniform.tex`: the certificate set-up, R-02, R-03 and R-05 with its table of 26 orbits;
  - `sections\permanent_apolar.tex`: the border-apolarity lemma and R-04;
  - `sections\uniform_n.tex`: R-07.
- **Read at statement level:**
  - `README.md`, `QUESTIONS.tsv` (Q-01 to Q-15), `LEDGER.md` (to 03:43:40 UTC), `IMPLICATIONS.md` (§§1-2);
  - the literature section;
  - R-06;
  - FL-01 to FL-05, S-01, S-02, O-01, O-02, P-09 to P-12.
- **Computations.**
  1. *The run's suite.* `checks\verify_all.py`, run from a copy: all nine checkers PASS (P-03 to P-06, P-08, R-04,
     R-02/R-03/R-05, R-06, P-09, P-12, P-10/P-11, S-01).
  2. *My own enumeration* (scratchpad `brpencil\mu_lower.py`, `mu_lower_fast.py`). For every j-subset of the 36
     coordinate minors (or 2×2 permanents) it computes a border-rank lower bound for the residual tensor: the larger
     of the support size and the A-factor Koszul bounds ⌈rank K_p / C(j−1, p)⌉, ranks mod 2147483629. Mod-p ranks
     bound the characteristic-zero ranks from below, so these are valid lower bounds over C. Results:
     - j = 2: minimum 6 for both, with histogram 144/288/198. This matches the run's P-05 counts exactly.
     - j = 3: minimum 8 for both.
     - j = 4: minimum 9 for both.
     - j = 5, determinant: minimum **11** over all 376,992 subsets.
     - j = 5, permanent: minimum 10, attained on exactly 576 subsets, the full orbit of {0,1,3,6,7} under row and
       column permutations and transpose (`orbit576.py`: orbit size 576). Every other subset has a bound of at least 11.
  3. *My own exact check of R-04* (`r04_check.py`, SymPy over Q, built from the five quadrics without the run's
     certificate): dim U = 9; rank Φ_A(A⊗U) = 40; the space Ẽ = {X : Φ_A(A⊗X) ⊆ Φ_A(A⊗U)} has dimension 10;
     rank Φ_B(Ẽ) = 82 > 80.

## 1. The main result and its check

**R-05.** CP border rank ≥ 42 for the polynomial det_4 and per_4: the coefficient tensors in (C^16)^{⊗4}, and in the
integral divided-power convention over every algebraically closed field. Hence also symmetric border rank ≥ 42.

**How it is proved.**
- *Substitution (R-01).* BR(T) ≥ q − j + μ_j, where q = 36 is the dimension of the image of the 2|2 flattening and μ_j
  is the minimum border rank of a j-plane of 2×2 minors (or permanents) taken as a tensor in C^j ⊗ E ⊗ E.
- *Torus reduction (P-01).* The minimum over the Grassmannian equals the minimum over coordinate j-subsets.
- *The fifth minimum.* μ_5 = 11 (R-05, with R-04 for the exceptional permanent orbit) gives 36 − 5 + 11 = 42.

**Verdicts on the proofs:**
- **R-01: confirmed.** In an approximating decomposition, a j-plane L ⊂ U' ∩ M, with M spanned by d − q + j atoms,
  gives P_L rank at most r − q + j. The incidence E_{q,j,s} is closed because it is a proper image (EGA II 5.4-5.5),
  and the limit lies in it. For three factors this is Landsberg-Michałek Prop. 2.3, as the run says.
- **P-01: confirmed.** The minors have distinct torus weights. Echelon-pivot rescaling gives a curve whose limit is the
  coordinate plane of the pivots, and border rank is lower semicontinuous.
- **R-04: confirmed**, by reading and by my independent exact computation. The background lemma is the (210)/(120)
  necessary part of border apolarity: Conner-Huang-Landsberg, Prop. 2.1, as cited. Its proof by proper incidence
  was read.
- **R-05.**
  - *Lower bound: confirmed independently.* Over C my enumeration gives μ_5 ≥ 11 for every coordinate 5-plane of
    det_4. For per_4 it gives the same except on one orbit, which R-04 settles; I rechecked R-04 myself.
  - *Upper bound.* The anchored shape (P-06) gives 11, so μ_5 = 11.
  - *The all-field claim (integer unit minors, characteristic 2 through the identity of the two tensors).* Checked
    through the run's verifier only.

**So BR(det_4) ≥ 42 and BR(per_4) ≥ 42 over C are confirmed, with an independent re-proof by computation of their
decisive step.**

## 2. Verdicts, finding by finding

| id | statement | check | verdict |
|---|---|---|---|
| R-01 | multidimensional substitution, all fields, proper incidence | proof read | confirmed |
| P-01 | the Grassmannian minimum equals the coordinate minimum | proof read | confirmed |
| P-02 | two-plane minima reduce to one adjacent pair | proof read | confirmed |
| P-03 | star S_{k,δ} has BR k+1, all characteristics | proof read; the run's checker passes | confirmed |
| P-04 | μ_2: 3 (rows), 6 (polynomials); bounds 7 and 40 | proof read; my enumeration (min 6, same histogram) | confirmed (+ computation) |
| P-05 | Koszul certificates for the pencils | proof read; the run's checker passes | confirmed |
| P-06 | anchored collections: BR = h+r+s+1 | proof read (flattening; explicit t^{-2} curve) | confirmed |
| P-07 | determinant minima reduce to order ideals (Borel) | proof read | confirmed |
| P-08 | BR(T_5) ≤ 11, BR(T_6) ≤ 12 by finite differences | proof read; the run's checker passes | confirmed |
| R-02 | μ_3 = 8, bound 41 | proof read; my enumeration min 8 | confirmed (+ computation) |
| R-03 | μ_4 = 9, bound 41 | proof read; my enumeration min 9 | confirmed (+ computation) |
| R-04 | the exceptional permanent 5-plane has BR ≥ 11 | proof read; my exact recomputation over Q | confirmed (+ independent computation) |
| R-05 | μ_5 = 11; **BR(det_4), BR(per_4) ≥ 42** | proof read; my exhaustive enumeration with R-04 | confirmed (+ independent computation over C) |
| R-07 | μ_j − j is nondecreasing; μ_6 = 12 | proof read (substitution applied to P_W itself) | confirmed |
| R-06 | the minima for j = 3, 4, 5 hold for every n ≥ 4; BR ≥ C(n,2)² + 6 | statement; the run's checker passes | not read in full |
| FL-01 to FL-05 | integral models; all fields; seeds; small-characteristic powers | statement | not read in full |
| S-01, S-02 | DPS: α = 3/4 exactly on a C²⊗C³ subspace; dimension-dependent error | statement; S-01 checker passes | not read in full |
| O-01, O-02 | orbit supremum of α is 1, with an attainment criterion; the Plücker condition | statement | not read in full |
| P-09 to P-12 | determinant seven-planes BR ≥ 14 (partial); cubic seeds | statement; checkers pass | not read in full |

**Counts:**
- 14 confirmed by targeted proof check: R-01, P-01 to P-08, R-02, R-03, R-04, R-05, R-07.
- 5 of these also have an independent computation of mine: P-04, R-02, R-03, R-04, R-05.
- 10 at statement level: R-06, FL-01 to FL-05, S-01, S-02, O-01, O-02, and P-09 to P-12 as a group.
- None refuted.

## 3. What is new

- **42 for both polynomials.** It improves GCT_GINEQ's F-23, 39, which it supersedes.
  - *Literature.* Against what we know: Farnsworth's symmetric border bound 38 for det_4 (Th. 1.6), and the
    catalecticant 36 for per_4 (Landsberg-Teitler, Table 3). Landsberg-Teitler's 43 and 40 are Waring-rank bounds, and
    Boij-Teitler's 50 for det_4 is a Waring rank too; none is a border bound. The run's literature audit
    (Han-Ju-Kim, Han-Song, Han 2026, border apolarity 2021 and 2026, Houston-Goucher-Johnston) found no polynomial
    size-4 border lower bound of 39 or more. My own searches in round 2 found none either.
  - *Novelty.* New as far as both searches go; the run claims no priority. The method (substitution and
    Koszul/apolarity certificates) is known. The evaluated minima are the contribution.
- **For general n.** BR ≥ C(n,2)² + 6 (R-06), from the b = 2 slice only. This is not the best general-n bound.
- **Still open: 43.** Q-07 is the open row: μ_7 ∈ {13, 14}. If μ_7 = 14, the bound becomes 43. Several determinant
  seven-planes are excluded (P-09, P-12); a support-9 case awaits its certificate.

## 4. Scope of the two proofs

No use of Alpöge or Masullo. The work is purely algebraic.

## 5. Integration

1. **GCT_GINEQ.**
   - *F-23 is superseded.* F-23's 39 is superseded by R-05's 42. F-23's exact identity min_U BR = BR(T_b) stays as the
     j = 1 case.
   - *F-23's own check.* R-01 (j = 1) re-proves F-13/F-23 with proper incidence over every algebraically closed
     field. This is the field translation my GINEQ intake asked for (section 5.5 there). It is now done.
2. **The tensor rank of the 4×4 determinant and permanent.**
   - *Where 42 sits.* 42 ≤ BR(det_4) ≤ Waring rank; Waring rank ≥ 50 for det_4 (Boij-Teitler).
   - *The attack this opens.* Two routes: μ_7 = 14, giving 43 (in progress); or the b = 3 residual images (prompt 44's
     P-10/P-11 cubic seeds), which feed F-23's recursion with BR(T_3) values. The run has the row permanent cubic
     seed exact (6) and the row determinant cubic seed in [7, 9].
3. **Grothendieck's frameworks.** The run states each step as the avoidance of closed relative Segre-secant and
   prolongation loci in Grassmannians: proper images (EGA II 5.4.1, 5.4.2, 5.5.3(i)), exterior-power bundle maps,
   unit minors over Z. Its dictionary section gives the translation the prompts ask for.
4. **GCT_KRON and CUE_GCT.** Their Jacobian-rank certificate method is the one the run and I used. There is no other
   overlap.

## 6. Prompt updates for the successor

1. Main question: μ_7 = 14 (bound 43), with every seven-plane certified. Then the b = 3 slices at n = 4: is μ_2 or μ_3
   of U_{4,3} known exactly?
2. Ask for R-06 and the general-n slices with b = ⌊n/2⌋, so as to state the strongest general-n bound from the method.
3. Provenance: GPT-6 Astra (ChatGPT Pro mode). No ways out.

## 7. Hexagon readiness: H03, now "border rank ≥ 42 for det_4 and per_4"

1. **Complete:** yes, for R-01, P-01, R-02 to R-05 and P-06.
2. **Self-contained:** yes. The inputs are published: Landsberg-Michałek Prop. 2.3 and Conner-Huang-Landsberg
   Prop. 2.1; both are also re-proved in the paper.
3. **Stable:** not yet.
   - *The open row.* The run is working on 43 (Q-07), which would supersede 42.
   - *The literature.* Two searches found nothing of 39 or more.
4. **Checked:** yes. An intake targeted proof check, plus an independent re-proof by computation of the decisive
   step (my exhaustive enumeration and the exact R-04 recheck).
5. **Of interest now:** moderate to high.

**Gate left: the run's final, to see whether it reaches 43.** Then a self-contained write-up and my read of every page.
H03's former gates are passed: the independent check of F-23 (R-01, and 40-42 by my computation), and a bound above 39
(42). **Flag to the main session.**

H13 and H14 are not affected by this run.
