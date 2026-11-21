# Addendum: GCT_KRON checkpoints 02 and 03, and the literature status of GCT_GINEQ F-23 (H03), 21 Nov 2026

Intake by Claude Opus 5.5 at effort high, the same agent that wrote `INTAKE_GCT_KRON_20261121.md` (launched by the main
session, Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode), still going.

## 0. What was read

- **Return folder:** `research_returns\GCT_KRON_checkpoint_03_20261121T0117Z_unzipped`, checkpoint 03 of 01:17 UTC.
  New since my first intake (checkpoint 01) are checkpoints 02 and 03; their ledger lists:
  - A-017 to A-026;
  - F011 to F021;
  - M011 to M015;
  - O016 to O020.
- **Read in full, with proofs:**
  - M-006 (`proofs\projection_bound.tex`, lines 1-80). Every later row exclusion rests on it, but it was already in
    checkpoint 01; I had not read it then.
  - M-013 (`proofs\jet_dominance.tex`, all 225 lines). This is the jet-dominance theorem behind the new staircase.
- **Read at statement level:**
  - the cp02 and cp03 blocks of `LEDGER.md`;
  - the QM010 to QM015 rows of `ROOT_QUESTIONS.tsv` and `QUESTIONS.tsv`;
  - the headings of A-021 to A-026, F-019 and O-016 to O-020 in `GCT_KRON.tex`.
- **Not read:** the proofs of A-017 to A-026, F011 to F021, M011, M012, M014, M015, O016 to O020. That is about
  4,000 lines of proof fragments, beyond this round's budget.

## 1. Verdicts

**M-006, projection containment compares all copies.** Confirmed (targeted proof check).
- *Statement.* If π(Y) ⊆ X for the projection to an r-dimensional quotient U, then
  mult_{S_λV} C[Y]_d ≤ mult_{S_λV} C[X]_d for every λ with at most r rows.
- *Proof.* In characteristic 0 the ideals are S_λV ⊗ J_λ, with J_λ a subspace of the same multiplicity space M_λ.
  An element of S_λU ⊗ J_{X,λ} depends only on π(y), so it vanishes on Y. The GL(V)-span then gives
  J_{X,λ} ⊆ J_{Y,λ}.
- *Novelty.* It is the inheritance principle in a comparison form. It is close to Kadish-Landsberg's padded-polynomial
  inheritance, which the run should cite.

**M-013, a determinant jet map with surjective differential.**
- *The pencil and its differential: confirmed.*
  - The pencil x_1 I − B(z) on 2h·C(R+ℓ, ℓ) vertices has nilpotent B. Its inverse entries between inward vertex
    (α, a) and outward vertex (β, c) are exactly z^α z_{ac} z^β, a unique path.
  - These entries span all polynomials of degree at most 2ℓ+1. Every monomial of degree 1 to 2ℓ+1 is a bridge
    variable times two multisets of size at most ℓ.
  - The cofactor identity d(det)(H E_ij) = H(1,z)(A^{-1})_{ji} with H = x_1 and H = z_t gives every monomial up to
    degree b = 2ℓ+2. The jet map is therefore dominant, by a unit Jacobian minor over Z.
- *The survival of every highest-weight copy: confirmed given F-016.* The step uses F-016 (j = 2): every coefficient
  in a highest-weight vector of weight λ has degree at most λ_2 outside the first coordinate. I did not read F-016.
  It is plausible, and it is consistent with the two- and three-variable cases I tried (Sym² Sym^n; the 3×3
  symmetric determinant in Sym³ Sym² C³). So the survival step is carried on F-016.
- *The uniform consequence λ_2 ≥ c+2 at n ≥ m^c (c ≥ 6): confirmed for odd c.* The bound
  2C(m²+ℓ−1, ℓ)/m^{2ℓ} ≤ 2C(ℓ+3, 3)/4^ℓ ≤ 5/8 is rechecked: the product formula decreases in m, and the ratio
  (ℓ+4)/(4(ℓ+1)) is below 1. For even c the proof uses O-012.a and F-014, which I did not read.
- *Consequence for the BIP range.* λ_2 ≥ 27 holds given F-016. The staircase λ_{2j} ≥ 28 − j also needs F-017,
  not read.

**A-026, the equal height-three rectangles.**
- *The run's claim.* g(h³, h³, h³) counts the solutions of 2a + 3b + 4c = h.
- *My check.* This agrees with the invariant ring of SL_3³ on C³ ⊗ C³ ⊗ C³. That ring is a polynomial ring on
  invariants of degrees 6, 9 and 12, so its Hilbert series is 1/((1−t^6)(1−t^9)(1−t^12)), and degree 3h gives
  2a + 3b + 4c = h. I take this from memory: Vinberg's theta-groups; Bremner-Hu-Oeding 2014. I did not open either.
- *The run's consequences follow.* There is a hole at h = 1, and the multiplicity is 2 at h = 4: (2,0,0) and
  (0,0,1). It is carried as background without fault found. The run itself calls the ring "known".

**The rest of checkpoints 02 and 03:** not read in full; statement level only. The constants (557, 420, the
staircases, n < P_d(dm)) were not recomputed. The run records independent complete readings for each by its own
sub-agents.

**Counts for this round:**
- 2 confirmed by targeted proof check. M-006 is confirmed outright. M-013 is confirmed in its own steps, and its
  survival step is carried on F-016.
- 1 carried as background (A-026).
- About 30 at statement level.
- None refuted.

**The cote 133 corrections of my first intake still stand.** A-001 to A-004, A-012 and A-013 are unchanged in
checkpoint 03.

## 2. What is new

- **The direction of the run.** It now makes a sustained, explicit reduction of the remaining actual multiplicity
  obstructions for the padded permanent against the determinant in the BIP range. The QMMAIN row reads:
  - m ≥ 190 and at least 52 rows;
  - the staircase λ_{2j} ≥ 28 − j for 1 ≤ j ≤ 26;
  - λ_3 ≥ 557 or λ_52 ≥ 3;
  - n < P_d(dm), and q ≥ 2.
- **Novelty.** I know of no such explicit staircase in the literature. It sits in the line of Kadish-Landsberg
  (row-length bounds from padding), Ikenmeyer-Panova and Bürgisser-Ikenmeyer-Panova. A literature check against
  Kadish-Landsberg and the Dörfler-Ikenmeyer-Panova "no occurrence" line is needed before anything is called new.
- **A-026.** Known.
- **The bridge to GCT_GINEQ.** The run's own F010 obstacle, the evaluation-tensor ranks, is still where GINEQ's
  border substitution (F-13, F-23) could enter.

## 3. Scope of the two proofs

Unchanged: no use of Alpöge or Masullo; the RH/GRH input supplies no step (GCT_KRON.tex, lines 58-63 and 1150-1155).

## 4. Hexagon readiness (the five tests of `field_experts\HEXAGON_CANDIDATES.md`)

1. **The cote 133 corrections (A-001, A-002, A-012, A-013).**
   - *What passes.* Tests 1 (complete), 2 (self-contained) and 4 (checked by intake and by computation).
   - *What fails.* Test 5: they correct an unpublished archive page and our own study. They belong in the cote 133
     companion, not as a post. A-002 is known (Bouc-Rökaeus). **Not a candidate.**
2. **The obstruction staircase (M-006 to M-015, F017, F018, A-021 to A-025).**
   - *Failed:* test 3, stable. The run is still going and the gates move every checkpoint (139, then 420, then 557 in
     one hour).
   - *Failed:* test 4, checked. Only M-006 and M-013 have an intake check.
   - *Not done:* the literature part of test 3 (Kadish-Landsberg and later).
   - *Interest (test 5):* moderate to high for the GCT community.
   - *What is left.* Wait for the final. Then do an intake of every proof the staircase uses (F-016, F-017, O-012.a,
     M-014), a computation re-proof of the constants, and a literature search. **Candidate, later.**
3. **A-026.** Known. Not a candidate.

## 5. The literature status of GCT_GINEQ F-23 (entry H03)

- **The searches.** Three web searches and two abstract reads, on 21 Nov:
  - Farnsworth, arXiv:1505.05079;
  - Landsberg-Teitler, arXiv:0901.0487;
  - Guan, arXiv:1510.00886;
  - Han-Ju-Kim, arXiv:2503.12032;
  - Kim, arXiv:2510.11051.
- **What they give.**
  - *Farnsworth, Theorem 1.6:* symmetric border rank of det_4 ≥ 38, up from 36 (Remark 1.7). Nothing for perm_4.
  - *Landsberg-Teitler:* for the polynomials, the border-rank bound is the catalecticant C(n, ⌊n/2⌋)² = 36 at n = 4.
    Their rank bound is C(n, ⌊n/2⌋)² + n(n − ⌊n/2⌋ − 1) = 40 for n = 4, as reported by the search; I did not open the
    paper. It is a rank bound, not a border-rank bound.
  - *Guan:* general Koszul-Young results with no numerical bound for det_4 or perm_4.
  - *Han-Ju-Kim and Kim:* about the n-way row tensors (BR(D_4) = 12, rank of perm_4 tensor = 8), a different object.
  - *Nothing found* gives 39 or more for the border rank, CP or symmetric, of the polynomials det_4 or perm_4. Nor did
    I find any CP border-rank bound for these polynomials above the catalecticant 36.
- **Status.**
  - For both polynomials, F-23's CP border rank ≥ 39 improves the best published figure found: 38 for det_4
    (symmetric border rank, Farnsworth), and 36 for perm_4 (the catalecticant).
  - Since CP border rank is at most symmetric border rank, F-23 also gives symmetric border rank ≥ 39 for both.
  - The searches did not cover Landsberg's book *Geometry and Complexity Theory* (CUP 2017), §§ on det_n and perm_n
    border rank, nor papers after 2025 by name. The book is the one remaining source that should be opened.
- **H03 gates left:**
  - Landsberg's book;
  - the successor (pushing F-23 asymptotically, as H03 says);
  - an independent re-proof. A computation would serve: for n = 4, b = 2, check by computer that every nonzero element
    of the 36-dimensional span of the 2×2 minors has rank at least 4 as a quadratic form. This holds by F-23's
    restriction argument, but a computation is the independent event the five tests ask for.
