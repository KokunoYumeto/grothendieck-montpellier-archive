# Intake of GCT_KRON (prompt 26), part 2: checkpoints 04 and 05, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high, the same agent that wrote part 1 and the checkpoint 03 addendum (launched by
the main session, Claude Opus 5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode), run GCT_KRON_20261120, still going. Its first timed review (02:00 UTC) found
movement.

## 0. What was read

- **Return folder:** `research_returns\GCT_KRON_checkpoint_05_20261121T0245Z_unzipped`, checkpoint 05 of 02:45 UTC,
  the newest present when I started.
- **Earlier reading:** part 1 read checkpoint 01; the addendum `INTAKE_GCT_KRON_cp03_20261121.md` read checkpoint 03
  (M-006, M-013).
- **What is new since checkpoint 03.** Read from the `LEDGER.md` blocks after "Checkpoint 03":
  - A-027 to A-031;
  - F022 to F026;
  - M016 to M020;
  - O021 to O027;
  - the timed review 01;
  - QA030: the run read the official facsimiles of cote 133 (scans 006, 008, 009, 019-029) and 8 more cote pages
    visually.
- **Read in full, with proof:**
  - A-030 (`GCT_KRON.tex`, lines 7921-8120);
  - the statement and the first part of the proof of F-024 (lines 2561-2650), which A-030 uses;
  - the statement and the witness of F-025 (lines 8254-8340);
  - A-029 (statement and proof).
- **Read at statement level:** everything else new (the LEDGER lines).
- **Computations, all mine** (scripts in `scratchpad\kron3\`):
  - `plethysm_check.py`: a_λ(d[n]) = 1 for λ = (d(n−2)+3, 3, 2^{d−3}) at the nine pairs (n,d) = (3,3), (3,4), (4,3),
    (4,4), (3,5), (5,3), (5,4), (4,5), (3,6). The method is weight multiplicities of Sym^d(Sym^n C^k) with Weyl
    alternation. I sanity-checked it on h_2[h_2] and h_2[h_3].
  - `hess.py`: the Mignon-Ressayre point for n = 3, 4, 5. P(A) = 0, ∂P/∂x_11 = (n−1)!, and the Hessian has full rank
    n².
  - `hdet.py`: H(det_n) = c_n det^{n(n−2)} with c_n = (n−1)(−1)^{n(n+1)/2−1}, at random integer points for n = 3, 4.
  - `f016_check.py`: a test of the support lemma F-016 on which M-013 and F-025 rest. Every coefficient in a
    highest-weight vector of weight λ has degree at most λ_j outside the first j−1 coordinates. Nine cases in
    Sym^d(Sym^n C^r): 10 highest-weight vectors found, no violation.
  - `f025_fast.py`: the F-025 integer witness A^0 has Jacobian rank 49 onto the 49 coefficients of Γ, computed mod
    2^61 − 1, which bounds the rational rank from below.

## 1. Changes to what parts 1 and the addendum checked

- **A-001, A-002, A-012, A-013: unchanged.** The run has now read the official facsimile of cote 133 and records
  "Previous mathematical corrections remain valid" (LEDGER, about 02:05 UTC). My replacement line for SA17's study
  (part 1, section 1) stands.
- **The scan 008 name.** It stays uncertified in the run (Laborde/Lazard). Our study's image decision, Lazard, stands.
- **M-006, M-013: unchanged.** M-013 was confirmed in the addendum given F-016. F-016 now has a computation event
  from me (9 cases, no violation), though still not a proof reading. M016 extends M-013's conclusion to every integer
  c ≥ 1 (λ_2 ≥ c+2); I did not read it.
- **A source-audit correction.** The run withdrew its own allegation of a factor-2 typo in Landsberg-Manivel-Ressayre,
  p. 476. This affects no finding I checked.

## 2. Verdicts on the new findings

**A-030: an explicit infinite family of actual obstructions at n = m ≥ 3.** Confirmed: targeted proof check plus
computation.
- *Statement.* Let R = n², q = R(n−2), d = R+1 and λ = (n+q+1, 3, 2^{R−2}). Then a_λ(d[n]) = 1, K_n(λ) = 0 and
  q^n_λ(d) = 1. Moreover the Kronecker coefficient g(λ, (d^n), (d^n)) is 0.
- *Proof checked step by step.*
  - The covariant Θ(F) = q·H(F)dF − nF·dH(F) has degree d in F and takes values in
    (det W*)² ⊗ S_{(a,1)}W* = S_λW*; Euler's identity makes it land in the Pieri kernel.
  - Θ(det) = 0, from H(D) = c_n D^{n(n−2)} and q = n²(n−2). I checked the identity numerically.
  - Θ(per) ≠ 0 at the Mignon-Ressayre point. There P(A) = 0, dP ≠ 0 and the Hessian has full rank; I checked this
    for n = 3, 4, 5.
  - So the simple module S_λW lies in the ideal of Ω_n and not in the ideal of the permanent closure.
  - F-024 (a_λ = 1) makes this copy the whole isotypic component. I read F-024's proof only through its Pieri set-up
    and checked its conclusion by computation at nine small (n, d), not at A-030's own pair (d = n²+1).
  - The vanishing g(λ, (d^n), (d^n)) = g((E−1, 1), (t^n), (t^n)) = 0 follows from det-twist removal and the classical
    formula for hooks: the number of removable corners of a rectangle, minus one.
- *What it is.* An occurrence obstruction, in fact a rectangular Kronecker-coefficient obstruction, for per_n against
  det_n with no padding.

**F-024, a_{(d(n−2)+3, 3, 2^{d−3})}(d[n]) = 1.** Confirmed by computation at nine (n,d) pairs. The proof was read
only through its Pieri set-up, so I count it as a computation event, not a full proof check.

**F-025: a multiplicity obstruction for per_3 against det_3 that is not an occurrence obstruction.**
- *Statement.* At d = 12 and λ = (19, 7, 2^5), q = 6 > K = 5.
- *The permanent side: confirmed by computation.* The 49×49 Jacobian minor of the explicit integer pencil is nonzero
  (rank 49 mod a large prime, so the rational rank is 49).
- *The support step: carried.* It needs F-016 with j = 3, which I tested but did not read.
- *The determinant side: carried as background.* a = 6 and one ideal copy are Landsberg-Manivel-Ressayre, Comment.
  Math. Helv. 88 (2013), §3.2, p. 476. I did not open it.
- *Verdict.* Confirmed for the permanent side. The obstruction depends on LMR's p. 476 values.

**A-029: Grothendieck's q_H^n on cote 133, scan 021.** Confirmed: targeted proof check.
- *Statement.* q_H^n(x) = q_H(τ^n(x)) with q_H([E]) = [H\E], so q_H^n([E]) = [Inj([n], E)/H].
- *Proof.* Orbits commute with disjoint union; τ^* was proved earlier (A-011).
- *What it gives the study.* The definition missing from our study, recovered from the original image by the run.
  It exhibits the subset operation as q_{S_n}^n.

**Read at statement level only:**
- A-027, A-028 (the closure gap), A-031;
- F022, F023, F026;
- M016 to M020;
- O021, O023, O025, O027.

The BIP gate constants (λ_2 ≥ 1000001 or λ_3 ≥ 29 or λ_4 ≥ 27, then λ_4 ≥ 27 or λ_2 ≥ 239063403) were not recomputed.

**Counts:**
- 2 confirmed by targeted proof check: A-030 (with computations) and A-029.
- 1 confirmed by computation without a full proof reading: F-024.
- 1 permanent side confirmed by computation, with its determinant side carried: F-025.
- 1 lemma tested by computation: F-016.
- About 25 at statement level.
- None refuted. No earlier verdict changes.

## 3. What is new

- **A-030.** An explicit infinite family of Kronecker (occurrence) obstructions for per_n against det_n at n = m.
  - *Inputs.* Mignon-Ressayre's Hessian point (2004, Prop. 3.1) and the Hessian equations of Landsberg-Manivel-
    Ressayre (2013) are known, as the run says. What it adds is the ambient multiplicity one (F-024), which turns LMR's
    single ideal copy into the full isotypic component, together with the vanishing of the Kronecker coefficient.
  - *Novelty.* I could not settle it in this round. Search first in Kumar, *A study of the representations supported
    by the orbit closure of the determinant* (Compositio 2015); Bürgisser-Ikenmeyer-Hüttenhain, *Permanent versus
    determinant: not via saturations* (PAMS 2017); Ikenmeyer-Kandasamy (STOC 2020); Dörfler-Ikenmeyer-Panova (2020);
    and Bürgisser's SLC survey.
  - *Bearing on GCT.* Occurrence obstructions are impossible at n ≥ m^25 (BIP), and A-030 shows they exist at
    n = m in explicit form. The open problem is the range between.
- **F-025.** A small multiplicity-not-occurrence example (q = 6 > K = 5) for per_3 against det_3. This is the kind of
  example Dörfler-Ikenmeyer-Panova showed must exist in other settings. To be checked against Ikenmeyer's
  computations for 3×3.
- **The BIP staircase.** It keeps shrinking (M016-M020, O025, O027). It is stronger than what I know in the
  literature, but it is still moving.

## 4. Scope of the two proofs

Unchanged. No new statement uses Alpöge or Masullo. The Hessian and Kronecker arguments are purely algebraic.

## 5. Integration

1. **Cote 133, SA17's study.**
   - *Scans 20-23.* Under "The operations q_H^n" add: "defined on scan 021 (lower half) as q_H^n(x) = q_H(τ^n x), with
     q_H[E] = [H\E]; thus q_H^n[E] = [Inj(I_n, E)/H], and the subset operation P_n is q_{S_n}^n (GCT_KRON A-029,
     read on the official facsimile)".
   - *Scan 19.* The scan-19 replacement of part 1 can now say that the run read the original image and found the
     mathematics as transcribed.
2. **GCT.**
   - *A-030 and the occurrence gap.* A-030 sets the lower end of the range where occurrence obstructions exist (n = m).
     BIP sets the upper end (n ≥ m^25). The attack it opens is to pad the Hessian bracket: find the largest n − m for
     which a Θ-type covariant of the padded permanent survives with ambient multiplicity one. F026 is the first test.
     It shows the size-3 obstruction does not transfer under the shifts tried, because O027 proves q ≤ K for n ≥ 4.
   - *How it meets CUE_GCT.* CUE_GCT's R-14 reaches the same middle range from the other side, with non-explicit
     four-row gaps at n = m+1 (see the CUE_GCT part 2 intake).
3. **H03 (GCT_GINEQ F-23, successor prompt 44 BR_PENCIL).** Neither checkpoint bears on it directly. They bound
   orbit-closure multiplicities, while F-23 bounds CP border rank of the same polynomials.
   - *The one shared tool.* KRON's unit-Jacobian certificates over Z (M-013, F-025) are the same kind of certificate
     prompt 44 can use to certify seeds BR(T_b), through dominance of decomposition maps.
4. **Prompts 30-36.** No change from part 1.

## 6. Prompt updates for the successor

1. Main question: the padding range of A-030-type covariants (item 5.2), and the literature check of A-030 and F-025.
2. Ask for a full written proof of F-016, the support lemma, as a numbered finding. Many results rest on it (M-013,
   F-025 and the jet theorems).
3. Ask for the LMR p. 476 values to be recomputed, not only cited, since F-025's determinant side rests on them.
4. As in part 1: name the run "GPT-6 Astra (ChatGPT Pro mode)"; no ways out.

## 7. Hexagon readiness

1. **A-030 (explicit occurrence obstructions at n = m).**
   - *Tests passed.* Test 1, complete: the proof is written in full; its one input, F-024, is proved in the paper
     and checked by me computationally. Test 2, self-contained: its inputs are published (Mignon-Ressayre,
     Landsberg-Manivel-Ressayre, Muir). Test 4, checked: my targeted check plus four computations.
   - *Gates left.* Test 3, stable: the literature search (section 3) has not been done, and the run may extend it.
     Also my reading of the rest of F-024's proof.
   - *Interest (test 5).* Moderate to high for GCT.
   - **State: one gate (the literature) away; flag to the main session.**
2. **F-025.** It needs LMR recomputed and a literature check. Later.
3. **The staircase.** Not stable. Later, as in the addendum.
