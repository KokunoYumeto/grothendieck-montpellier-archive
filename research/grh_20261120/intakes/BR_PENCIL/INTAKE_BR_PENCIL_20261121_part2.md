# Intake of BR_PENCIL (prompt 44), part 2: checkpoint 02, the run's final return, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a17221e5; launched by the main session, Claude Opus 5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode), run BR_PENCIL-20261121-R1. Its newest return is checkpoint 02 of 04:29 UTC.
By the user's rule (20 Nov) the run has ended at that return.

## 0. What was read

- **Return folder:** `research_returns\BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped`. Part 1 read checkpoint 01.
- **Read in full, with proofs:**
  - `sections\det7_global.tex`: R-08 and R-09;
  - `sections\per7_global.tex`: R-10, the cover and the certificate table;
  - `sections\per7_last_higher.tex`: P-19, through the reduction to the eight fixed extensions and the (2,2)
    obstruction set-up.
- **Read at statement level:**
  - `QUESTIONS.tsv`, all rows (Q-07, Q-18, Q-19 now settled; Q-16, Q-17 open);
  - `LEDGER.md` after 03:43 UTC;
  - P-09, P-12 to P-18, P-20, P-21, R-11.
- **Computations, mine** (scratchpad `brpencil2\`):
  1. *The run's suite.* `checks\verify_all.py` from a copy: all **22** checker jobs PASS. These include R-08
     (2997 minors), R-10 (6041 minors and the cover), P-09, P-12 to P-19, R-11, P-17 and P-20.
  2. *The 25 determinant ideals* (`det7_ideals.py`). I enumerated the 7-element order ideals of P×P myself and got
     exactly 25. On them, support and A-factor Koszul bounds (my own code) reach 14 on 9 ideals: 2 by support, 7 by
     A-Koszul. This matches the run's table row for row.
  3. *The permanent seventh cover* (`per7_indep.py`). It takes only the list of orbit representatives from the run's
     certificate and recomputes everything else:
     - the number of support-below-14 seven-subsets, by full enumeration of the 8,347,680 subsets: **1,543,608**;
     - the orbits of the 1517 representatives under the 1152-element group: pairwise disjoint, covering exactly
       those 1,543,608 subsets;
     - my own A-Koszul bound: at least 14 on **1503** representatives. The 14 that fall short are exactly the run's
       3 B-Koszul and 11 prolongation cases.
  4. *The support-factor Koszul maps* (`bkoszul2.py`, my code, in the run's orientation Λ^pB ⊗ C* → Λ^{p+1}B ⊗ A,
     by torus weight blocks, mod p):
     - the three permanent cases have ranks **6457, 6457, 6515**;
     - the two determinant cases have rank **6501**;
     - all above 13·495 = 6435, so each case has a bound of 14.

     These are exactly the run's numbers. (My first orientation, A* ⊗ Λ^pB → Λ^{p+1}B ⊗ C, gives only about 4970.
     The bound depends on the orientation, and the run's is the effective one.)

## 1. What the run settled about 43 (Q-07)

**Q-07 is PROVED in characteristic zero.**
- *The statement.* μ_7 = 14 for both polynomial families (R-08 for det, R-10 for per). Hence
  **BR(det_4) ≥ 43 and BR(per_4) ≥ 43** (CP border rank of the coefficient tensors over C, so also symmetric border
  rank): 36 − 7 + 14 = 43.
- *The minima after it.* μ_8 = 15 and μ_9 = 16 (R-09, R-10) give the same 43.
- *The field scope.* The all-field statement stays at 42 (R-05). The 43 is only claimed in characteristic zero,
  because the seventh-minimum certificates are modular minors mod 1000003 lifted to Q. No positive-characteristic
  upgrade is claimed.
- *Upper witnesses.* An anchored 3×3 shape with 7 edges gives μ_7 ≤ 14 (P-06). The minimum is therefore exact,
  and this route cannot give more than 43 at j = 7.

**My verdict on R-08 and R-10: confirmed, with independent computation covering all but 25 cases.**
- *The architecture.* P-01/P-07 reduction, the exhaustive cover, the Koszul costs and R-01: read and confirmed.
- *What I recomputed.* Across both families, by my own code:
  - the cover (count, orbits, disjointness);
  - every A-factor and support-factor Koszul case.
- *What remains.* 14 determinant ideals (P-09, P-12, P-14, P-15) and 11 permanent representatives (P-13, P-15, P-16,
  P-19) rest on prolongation (border-apolarity) certificates.
  - I read P-19's argument in full through its reductions and checked that its necessary condition is closed and
    proper.
  - The run's own verifiers for all of these pass on rerun.
  - I did not recompute these 25 cases independently: my simple unique-extension test (the one that settled R-04)
    is inconclusive on them, because rank Φ_A(A⊗U) < 78, so their proofs need the run's finer weight-block
    arrangements.

**44 (Q-17): open at the run's end.**
- *The condition.* 44 needs μ_10 ≥ 18 (36 − 10 + 18).
- *Determinant.* 35 of the 59 Borel ideals still unresolved (P-17 excludes 18, Koszul 6).
- *Permanent.* 17 ≤ μ_10 ≤ 18, with the upper 18 from P-20's finite-difference curve.
- *Verdict.* No 44 claimed.

## 2. Other new findings

| id | statement | check | verdict |
|---|---|---|---|
| R-08 | det μ_7 = 14, BR(det_4) ≥ 43 (char 0) | proof read; my computation on 11 of 25 ideals; the run's verifier for the rest | confirmed (computation independent except the 14 prolongation ideals) |
| R-09 | det μ_8 = 15, μ_9 = 16 | proof read (R-07 + P-06) | confirmed |
| R-10 | per μ_7, μ_8, μ_9 = 14, 15, 16; BR(per_4) ≥ 43 (char 0) | proof read; my independent cover and Koszul on 1506 of 1517 orbits | confirmed (independent except the 11 prolongation orbits) |
| P-19 | the last permanent seven-plane has BR ≥ 14 (higher prolongation P_22) | argument read; the run's checker passes | confirmed as read; stages are computational, rerun via the run's checker |
| P-13, P-15, P-16, P-09, P-12, P-14 | prolongation exclusions for the remaining seven-planes | statement; the run's checkers pass | carried (computation by the run, rerun by me) |
| R-11 | the seventh to ninth minima for every n ≥ 4; BR ≥ C(n,2)² + 7 (char 0) | statement; checker passes | not read in full |
| P-11 | row determinant cubic pencil: BR 8 (char ≠ 2), 6 (char 2); permanent 6 | statement; checker passes | not read in full |
| P-18 | polynomial cubic seeds: per in [21, 24], det in [21, 27]. The cubic two-plane route is capped at 41 (det) and 38 (per), so it cannot beat 43 (closes Q-19) | statement; checkers pass | not read in full |
| P-17, P-20, P-21 | 18 determinant ten-plane Borel ideals excluded; row permanent μ_j = j+1; the per ten-plane upper bound 18 | statement; checkers pass | not read in full |

**Counts for this return:**
- 3 main findings confirmed with independent computation: R-08, R-10, and R-09 (whose proof is read).
- 1 argument read: P-19.
- About 12 at statement level, with the run's checkers rerun and passing.
- None refuted. Part 1's verdicts stand: R-05's 42 is unchanged and remains the all-field statement.

## 3. What the run settled, what it left open

- **Settled.**
  - BR(det_4), BR(per_4) ≥ 43 over C.
  - The exact residual minima μ_2 to μ_9 at n = 4 (6, 8, 9, 11, 12, 14, 15, 16) and their extension to every n ≥ 4
    (R-11): BR ≥ C(n,2)² + 7.
  - The b = 3 cubic route cannot beat 43 (P-18 caps).
  - The row-family cubic seeds are exact (P-11).
- **Open.**
  - 44 (Q-17: μ_10 ≥ 18);
  - the exact cubic polynomial seeds (Q-16);
  - 43 in positive characteristic;
  - the general-b numerical formulas (Q-06);
  - a generic efficient α algorithm (Q-09).
- **New against the literature.** As in part 1: no published border lower bound of 39 or more for these
  polynomials was found by the run's audit or by my searches. 43 improves Farnsworth's 38 (symmetric, det_4) and the
  catalecticant 36 (per_4). It stays below the Waring lower bounds (det_4 ≥ 50, Boij-Teitler; per_4 ≥ 40,
  Landsberg-Teitler), which are a different quantity.

## 4. Scope of the two proofs

No use of Alpöge or Masullo.

## 5. Integration

- **GCT_GINEQ F-23 (39).** Superseded twice, by 42 (all fields) and by 43 (char 0).
- **Grothendieck's frameworks.** As in part 1: closed Segre-secant and prolongation incidences in Grassmannians,
  proper images (EGA II 5.4-5.5), exterior-power bundle maps, Borel-fixed points (SGA 3 split tori and root
  subgroups). The new P-19 condition P_22 is a determinantal kernel condition on a tautological tensor bundle.
- **GCT_KRON and CUE_GCT.** No bearing on H13 or H14. The shared tool is still the unit or modular Jacobian/minor
  certificate.

## 6. What the successor prompt needs

1. **Main question: 44.**
   - *Determinant.* The 35 remaining Borel ten-plane ideals, attacked with substitution in a used-variable factor
     (the run's own next step) and exact treatment of the Borel parameter families.
   - *Permanent.* μ_10 ∈ {17, 18}: either a 17-term degeneration or a hereditary seven-subset bound.
   - *Attach.* The run's certificate files (det10_borel, per10_upper18), so the successor starts where this run
     stopped.
2. **43 in every characteristic.** Ask for unit-minor (integer determinant ±1) versions of the 2997 + 6041 modular
   minors and of the prolongation certificates, or the exact primes where they fail.
3. **An independent recomputation route for the 25 prolongation cases.** Ask the run to state for each case the
   torus-invariant extension enumeration in a form a short independent script can redo. My simple unique-extension
   test does not reach them.
4. **b = 3 exactly.** The cubic seeds per in [21, 24] and det in [21, 27]. They no longer bear on 43 but matter for
   general n.
5. **Provenance.** GPT-6 Astra (ChatGPT Pro mode). No ways out, no minimums.

## 7. Hexagon readiness: H03, now "border rank ≥ 43 for det_4 and per_4 (over C); ≥ 42 over every algebraically closed field"

1. **Complete:** yes. Every case of the cover is proved, the 25 prolongation cases by their own written proofs.
2. **Self-contained:** yes. The inputs are Landsberg-Michałek Prop. 2.3 and Conner-Huang-Landsberg Prop. 2.1
   (published), and the paper re-proves both in the needed form.
3. **Stable:** now yes for 43. The run has ended. 44 was open at its end, and a successor (point 6.1) could raise
   the bound.
   - *If 44 follows.* A post on 43 would be strengthened, not contradicted.
   - *The literature.* The run's audit and my searches found nothing of 39 or more.
4. **Checked:** yes, with one limit.
   - *What is checked.* The intake proof check; independent computations of mine (the cover; all Koszul cases,
     1506 permanent orbits and 11 determinant ideals; R-04); the run's 22 verifiers rerun.
   - *The limit.* The 25 prolongation cases are checked by the run's certificates and my reading, not by my own
     independent recomputation.
5. **Of interest now:** moderate to high.

**Gates left:** a self-contained write-up, and my reading of every page before submission. If the user wants a fully
independent check before posting, add an independent recomputation of the 25 prolongation cases (point 6.3). The
decision whether to wait for a 44 successor is the user's; 43 is stable as stated. **Flag to the main session: H03
passes tests 1-4 for 43 over C, with the stated limit on test 4.**
