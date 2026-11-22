# Intake of GCT_KRON (prompt 26), part 3: checkpoints 06 and 07, the run's final return, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a17221e5; launched by the main session, Claude Opus 5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode), run GCT_KRON_20261120. Its newest return is checkpoint 07 of 04:15 UTC.
By the user's rule the run has ended there. It made three timed reviews (02:00, 03:01 and 04:00 UTC), all with
movement.

## 0. What was read

- **Return folder:** `research_returns\GCT_KRON_checkpoint_07_20261121T0415Z_unzipped`. Part 2 read checkpoint 05.
- **New since checkpoint 05.** Read from the LEDGER blocks of 03:01-04:15 UTC (timed reviews 02 and 03):
  - A-033 to A-038;
  - F-028, O-029, O-031;
  - QA033-RJ, QA033-SYM.
- **Read in full, with proof:** A-034 (`GCT_KRON.tex`, lines 9001-9330).
- **Read:** the statement of A-030 in checkpoint 07 (line 8382, unchanged), and the final QMMAIN row of
  `QUESTIONS.tsv`.
- **Read at statement level:** the rest.
- **Computation, mine** (`scratchpad\kron3\a034_check.py`): at A_* (all ones, entry (1,1) = 3 − n),
  per(A_*) = 2(n−1)! and det Hess(per)(A_*) = 0, for n = 3, 4, 5. The Hessian is nonzero at the Mignon-Ressayre point
  (entry 1 − n), so H(per) is not identically zero.

## 1. Changes to parts 1 and 2

- **A-030 unchanged.** It is now the s = 1 case of A-034.
- **F-025 unchanged** in the final QMMAIN row (K = 5 < q = a = 6 < sk = 10 < g = 11).
- **The cote 133 corrections (part 1) unchanged.** Nothing is withdrawn.

## 2. Verdicts on the new findings

**A-034: every stretch gives a strict actual multiplicity gap, unpadded n = m ≥ 3.** Confirmed: targeted proof check
plus computation.
- *Statement.* For λ_n = (E+1, 3, 2^{R−2}), D = R+1 and every s ≥ 1:
  - q(sλ_n) ≥ p_n(s) > h_n(s) = K_n(sλ_n) = sk = g, where p_n and h_n count partitions of s into parts of size at
    most n and into parts from {2, ..., n} respectively;
  - the gap is at least p_n(s−1) > 0;
  - the determinant ray algebra is exactly C[U_2, ..., U_n], and the permanent ray algebra contains
    C[Z, U_2, ..., U_n].
- *Proof checked step by step.*
  1. The binary-coefficient invariants I_i are invariant under x ↦ x + ty, by centering.
  2. Their characters under upper triangular g are as stated.
  3. Binary-pencil evaluations are genuine SL(W)-orbit evaluations.
  4. At A_* the permanent's Hessian vanishes while P(A_*) ≠ 0 (checked by me). The diagonal-pencil Jacobian
     (A-034.13) makes I_2, ..., I_n algebraically independent on permanent pencils.
  5. Valuation along an irreducible factor h of H(P) through A_*: ord_h Z = e − 1 and ord_h U_i = ie. So the
     summands of any relation have distinct valuations es − j. This proves the injection, and q ≥ p_n(s).
  6. Determinant side: H(det) = c_n det^{n(n−2)}, so U_i = H_0^i I_i are independent on the domain C[D_n], and
     K ≥ h_n(s).
  7. The ordinary Kronecker value g = h_n(s) comes from the determinant twist to the two-row core (A-030.15). It is
     consistent with the classical two-row rectangle formula p_k(box) − p_{k−1}(box) = partitions of s into parts
     2..n.
  8. Hence K = sk = g = h_n(s).
- *What it adds.* A-030 (s = 1) becomes an infinite family of multiplicity obstructions along the whole stretching
  ray, with both multiplicities positive for s ≥ 2. A positive but non-saturated normal model is realized in the
  actual determinant ring.

**Read at statement level only:**
- A-033: q ≥ 3 > K = 1 at s = 2;
- A-035, A-036: the partial-Hessian route is closed for every proper internal padding m < n, so the Hessian algebra
  cannot transfer to padded obstructions;
- A-037: the pair algebra has 3 copies against ambient and determinant 4, so the pair algebra is not exhaustive;
- A-038: q_3 = K_3 = a for every cubic type of length ≤ 4, via the classical cubic-surface theorem, so every
  internally padded per_3 four-row type has q ≤ K;
- F-028, O-029, O-031, QA033.

**Counts:** 1 confirmed by targeted proof check with computation (A-034); about 10 at statement level; none refuted.

## 3. What the run settled in the end, and what it left open

- **Settled.**
  - *The cote 133 audit* (A-001 to A-029): the subset/λ^B distinction, the non-specialness of λ^B, the finite-sums
    correction, the Z_p lattice answer, and the q_H^n definition read from the official facsimile.
  - *Explicit unpadded obstructions* (A-030, A-034) and a multiplicity-not-occurrence example (F-025).
  - *A large ledger of necessary conditions* for any obstruction in the IP/BIP padded ranges: m ≥ 190, rows ≥ 52, the
    staircase λ_{2j} ≥ 28 − j, λ_3 ≥ 557 or λ_52 ≥ 3, M019's λ_4 ≥ 27 or λ_2 ≥ 239063403, and jet dominance.
  - *Method boundaries.* The Hessian and partial-Hessian algebras do not transfer to padding (A-035, A-036). The pair
    algebra is not exhaustive (A-037).
- **Open.**
  - *The main comparison in the large-padding range* (QMMAIN). Its precise obstacle is the evaluation-tensor ranks
    (F010).
  - *The arbitrary-size permanent endpoint* (QA033): the mixed and charge maps.
  - *Extra highest-weight copies* outside the constructed algebras.

## 4. Scope of the two proofs

No use of Alpöge or Masullo at any checkpoint.

## 5. Integration

- **H13 and CUE_GCT.** A-034 is the strongest form of H13. Its padded continuation is closed by A-035/A-036 within the
  Hessian algebra. So the explicit-obstruction route needs a covariant not built from Hessians.
- **CUE_GCT's padded existence results** (R-14 to R-27, H14) are non-explicit four-row gaps for n/m < sqrt 2. They
  complement KRON's explicit unpadded families and its padded exclusions. Together they bracket the problem:
  - explicit at n = m;
  - non-explicit existence up to n ≈ sqrt 2 · m (CUE);
  - strong necessary conditions in the BIP range (KRON);
  - no occurrence obstructions at all for n ≥ m^25 (BIP).
- **Cote 133.** The SA17 study edits of parts 1 and 2 stand. Nothing new for the archive in checkpoints 06-07.

## 6. What the successor prompt needs

1. **Main question: an explicit padded obstruction.** A-035/A-036 exclude Hessian-algebra covariants. Ask for
   covariants outside that algebra: the extra copies A-037 exhibits (S(F)F_0²I_2), or Θ-type covariants built from
   higher-order derivative determinants. Attach A-034's ray-algebra theorem as the template.
2. **Meet CUE_GCT's range.** For (m, n) = (8, 9), where CUE R-14 proves a four-row gap exists, ask for an explicit
   four-row λ and degree. Use KRON's exclusions (λ_1 ≥ d(n−m)+4; the row conditions) to prune.
3. **The evaluation-rank formulation (F010)** in the BIP range, with GCT_GINEQ/BR_PENCIL substitution tools.
4. **Write F-016 (the support lemma) as a numbered finding with a full proof.** My computation tests it in 9 cases.
5. **Recompute LMR p. 476**, the determinant side of F-025.
6. **The literature check of A-030/A-034** against Kumar 2015, Bürgisser-Ikenmeyer-Hüttenhain 2017,
   Ikenmeyer-Kandasamy 2020 and Dörfler-Ikenmeyer-Panova.
7. **Provenance:** GPT-6 Astra (ChatGPT Pro mode). No ways out.

## 7. Hexagon readiness

**H13 (explicit obstructions for per_n against det_n with no padding): now A-030 strengthened by A-034.**
1. *Complete:* yes. A-034's proof is complete as read; it uses A-030.15 for g.
2. *Self-contained:* yes. The inputs are Mignon-Ressayre, Muir and the classical two-row Kronecker formula.
3. *Stable:* yes. The run has ended. A-035/A-036 show the Hessian route stops at n = m, so A-034 will not be
   superseded by our own work soon.
4. *Checked:* yes. My targeted proof checks of A-030 and A-034, with computations: F-024 at nine (n, d); the
   Mignon-Ressayre point; H(det); A_*.
5. *Of interest now:* moderate to high for GCT.

**Gate left: the literature search** (point 6.6), especially whether such stretched occurrence/multiplicity families
at n = m are known. Then the write-up and my read of every page. **H13 is one gate away: flag to the main session.**

**F-025.** A possible companion to H13. Its gate is the recomputation of LMR p. 476.

**H03, H14.** Not affected by this run.
