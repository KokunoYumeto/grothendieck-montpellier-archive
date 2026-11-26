# Primer: the mathematics of GCT_KRON as of its final return (checkpoint 07, 21 Nov 2026, 04:15 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), as the GCT field expert, 23 Nov 2026, for the main session
to read after a compaction. It restates; it does not develop.

## The run and the record

- **Prompt 26**, Kronecker coefficients and GCT obstructions, with cote 133's λ-ring pages. The run is GPT-6 Astra
  (ChatGPT Pro mode); it records its effort as "not exposed".
- **Final return:**
  `grothendieck_archive_transcription_20261110\research_returns\GCT_KRON_checkpoint_07_20261121T0415Z_unzipped\GCT_KRON_work\GCT_KRON.tex`.
  It has 117 finding ids. Some locations:
  - A-034: lines 9001–9330;
  - O-030: lines 9423–9764;
  - F-016: from line 15823;
  - QA033: lines 12273–12380.
- **Intakes**, all in this folder, all by a17221e5 (Claude Opus 5.5 at effort high):
  - part 1 (checkpoint 01);
  - the cp03 addendum;
  - part 2 (checkpoints 04–05);
  - part 3 (final).

  GCT_OBS's intake (checkpoint 15) adds O-030 and corrects the record on F-016.
- **Inputs:** neither Alpöge nor Masullo, at any checkpoint.

**Check labels.**

| Label | Meaning |
|---|---|
| `[TPC]` | targeted proof check |
| `[COMP]` | our computation |
| `[stmt]` | statement level |

## 1. Explicit obstructions for per_n against det_n without padding (Hexagon H13)

Notation:
- d[n] is the n-th symmetric power plethysm: the ambient degree-d coordinate ring of n×n matrices.
- a_λ is its multiplicity.
- K_n(λ) is the multiplicity in the determinant orbit closure's coordinate ring.
- q_λ is the multiplicity for the permanent.

### A-030 `[TPC]`, `[COMP]` (part 2)

**Statement.** Let R = n², q = R(n − 2), d = R + 1 and λ = (n + q + 1, 3, 2^{R−2}). Then:
- a_λ(d[n]) = 1;
- K_n(λ) = 0;
- q_λ^n(d) = 1;
- g(λ, (d^n), (d^n)) = 0.

So it is an occurrence obstruction, in fact a rectangular Kronecker obstruction.

**Proof.**
1. The covariant Θ(F) = q·H(F)·dF − n·F·dH(F) has values in S_λW* (Euler's identity).
2. Θ(det) = 0 by Muir's identity H(det_n) = c_n·det_n^{n(n−2)}.
3. Θ(per) ≠ 0 at the Mignon–Ressayre point, where P = 0, dP ≠ 0 and the Hessian has full rank (Mignon–Ressayre 2004,
   Prop. 3.1). We checked this for n = 3, 4, 5.
4. F-024 gives a_λ = 1 (checked by computation at nine (n, d)). So that copy is the whole isotypic component.
5. The Kronecker value: twist removal, then the hook formula.

### A-034, every stretch `[TPC]`, `[COMP]` (part 3, lines 9001–9330)

**Statement.** For λ_n = (E + 1, 3, 2^{R−2}), D = R + 1 and every s ≥ 1:
- q(sλ_n) ≥ p_n(s) > h_n(s) = K_n(sλ_n) = g, where p_n counts partitions into parts ≤ n and h_n into parts from
  {2, …, n};
- the gap is at least p_n(s − 1).

**Proof.**
1. The binary-coefficient invariants I_i are translation-invariant.
2. At the point A_*, the permanent's Hessian vanishes while P ≠ 0. A diagonal-pencil Jacobian makes I_2, …, I_n
   independent on permanent pencils.
3. Valuations along a factor h of H(P): ord_h Z = e − 1 and ord_h U_i = ie. So the terms of any relation have distinct
   valuations, and q ≥ p_n(s).
4. On the determinant side, U_i = H_0^i·I_i, and K = h_n(s), by the two-row rectangle formula.

### O-030, a three-parameter family `[TPC]`, with a two-row identity computed for n ≤ 8, k ≤ 15 (GCT_OBS intake)

**Statement.**
- Take n ≥ 3, u ≥ 0, a ≥ k ≥ 0, R = n², q = R(n − 2), d = a + uR, and
  Λ(u, a, k) = (na + u(q + 2) − k, 2u + k, (2u)^{R−2}).
- Then K_n(Λ) = sk = g = h_n(k), and q_Λ ≥ Σ_{j=0}^{min(u,k)} h_n(k − j).
- The gap is strict for k = 1, or k ≥ 3 with u ≥ 1, or k = 2 with u ≥ 2.
- A-030 is the case u = a = k = 1; A-034 is u = a = k = s.

**Inputs:**
- F-002: two-row rectangular Kronecker numbers;
- O-006: binary forms are determinants.

**Under padding.** Every member with u > 0 has n² rows, above both padding caps (m² and m² + 1), so q = 0 there.

### F-025, a multiplicity obstruction that is not an occurrence obstruction

**Statement.** For per_3 against det_3 at d = 12, λ = (19, 7, 2⁵): q = 6 > K = 5.

**What is checked.**
- The permanent side by computation (a 49×49 Jacobian minor).
- The determinant side cites Landsberg–Manivel–Ressayre (Comment. Math. Helv. 88 (2013), §3.2, p. 476).
- GCT_OBS S-002/S-003 later reconstructed both sides explicitly.

### F-016, the support lemma `[TPC]` (GCT_OBS intake; = GCT_OBS S-001)

Every coefficient c_α in a highest-weight vector of weight λ in Sym^d Sym^n has Σ_{i≥j} α_i ≤ λ_j.

### Good for, and gates

**Good for:** explicit representation-theoretic witnesses for per_n ∉ closure(GL·det_n) at n = m, along whole rays.
BIP shows that occurrence obstructions are impossible at n ≥ m^25. The separation itself is known: Mignon–Ressayre, and
pequalnp's checked L-gct-010.

**Novelty gate.** Kumar (Compositio 2015); Bürgisser–Ikenmeyer–Hüttenhain (PAMS 2017); Ikenmeyer–Kandasamy (STOC 2020);
Dörfler–Ikenmeyer–Panova.

## 2. The padded side: necessary conditions and universal determinants

- **M-006 `[TPC]`.** Projection containment.
  - If π(Y) ⊆ X for a projection to an r-dimensional quotient, then mult_{S_λV} C[Y]_d ≤ mult C[X]_d for every λ with
    ≤ r rows.
  - Proof: J_{X,λ} ⊆ J_{Y,λ} by GL-span.
  - It is close to Kadish–Landsberg inheritance.
- **M-007 `[stmt]`, arithmetic checked.** An explicit universal determinant.
  - For a degree-m form f in ≤ r variables and a linear form L, L^{n−m}·f is the determinant of an n×n matrix of linear
    forms for n ≥ S(m, r) = C(m+p, p) + C(m+q, q) − 1, with p = ⌊(r−1)/2⌋ and q = ⌈(r−1)/2⌉.
- **M-008 `[stmt]`.** If n ≥ S(m, r), then q ≤ K for every λ with ≤ r rows. So:
  - there is no multiplicity obstruction with ≤ 9 rows at n > 3m⁴;
  - none with ≤ 51 rows at n ≥ m^25.
- **M-013 `[TPC]`.** A determinant jet map with surjective differential.
  - The pencil x_1·I − B(z), with nilpotent B; the cofactor identity gives every monomial up to degree 2ℓ + 2.
  - With F-016: λ_2 ≥ c + 2 at n ≥ m^c (c ≥ 6, checked for odd c).
- **F-021 `[stmt]`.** For n ≥ m ≥ J_b(r): q = K = a for ≤ r rows with λ_2 ≤ b (internal padding).
- **The BIP-range ledger (QMMAIN) `[stmt]`.** Every padded obstruction at n ≥ m^25 needs:
  - m ≥ 190 and ≥ 52 rows;
  - λ_{2j} ≥ 28 − j for 1 ≤ j ≤ 26;
  - λ_3 ≥ 557 or λ_52 ≥ 3 (O-018, A-025);
  - λ_4 ≥ 27 or λ_2 ≥ 239063403 (M-019; under independent padding 238356708, by GCT_OBS S-004).
- **A-035, A-036 `[stmt]`.** The Hessian and partial-Hessian algebras do not transfer to any proper padding m < n.
- **A-037 `[stmt]`.** The pair algebra is not exhaustive.
- **A-038 `[stmt]`.** Every internally padded per_3 four-row type has q ≤ K.
- **O-011 `[stmt]`.** For λ_d = (d(n−2) + 2, 2^{d−1}):
  - K_n = a = 1;
  - q = 1 for d ≤ m², and q = 0 for m² < d ≤ n²;
  - detected by Hessians.
- **F-009 `[stmt]`.** Grenet's 2^m − 1 gives Z_{n,m} ⊆ Ω_n, and q ≤ K for every λ, at n ≥ 2^m − 1.

## 3. Cote 133 (λ-rings), the archive audit

- **A-001 `[TPC]`, `[COMP]`.** The subset reading of scan 019 contradicts its boxed 2λ²(E) + E = E². With G = C₂ and its
  free orbit:
  - σ² = p₂ + E and λ²_B = E² − σ² are right;
  - the "Checked" line of SA17's study is wrong.
  - Independently agreed by CUE_GCT G-01.
- **A-002 `[TPC]`.** The Burnside λ^B is not special (V₄ counterexample). Known: Bouc–Rökaeus Th. 1.1.
- **A-003, A-004, A-012 `[TPC]`.**
  - No nontrivial irreducible is the linearization of an effective G-set.
  - Monomial Cauchy summands are not effective.
  - "Finite sums of h_I = summands of one H_J" is false.
- **A-013 `[TPC]`.** The induction ring R_A(S_n) is polynomial for local Q-algebras and for Z_p-lattices; not for F_p,
  nor for Z_(2)[ε]/(2ε, ε²).
- **A-029 `[TPC]`.** Grothendieck's q_H^n (scan 021): q_H^n([E]) = [Inj([n], E)/H]. The definition our study lacked,
  read from the original image.

## 4. Open rows at the end

| Row | Gate |
|---|---|
| QMMAIN, the comparison in the large-padding range | The evaluation-tensor ranks (F010) |
| An explicit padded obstruction | Covariants outside the Hessian algebra: A-037's extra copies, or Θ-type covariants from higher derivative determinants |
| QA033 | The arbitrary-size permanent endpoint: the mixed and charge maps |
| Extra highest-weight copies | Outside the constructed algebras |
| Meeting CUE_GCT at (8, 9) | An explicit four-row λ and degree, pruned by λ_1 ≥ d(n − m) + 4 |

## 5. Where the results went

- **Hexagon:** H13 (A-030, A-034; now O-030); GPK rows. Prompt 56 GCT_WRITEUP, B1: "replace the ray by the three-parameter
  family".
- **GCT_OBS** (prompt 53) took the padded question. It produced S-001 = F-016, S-002/S-003 (explicit F-025) and S-004 (the
  padding conventions).
- **SA17's cote 133 study:** the corrections of A-001, A-012, A-013, A-029.
- **pequalnp fleet** (JOINT_GCT_LEMMA_SPACE), one line each:
  - **A-030, A-034, O-030** — parallel to **L-gct-010**: same separation, with explicit witnesses. A-030 uses
    **L-gct-013** (the Mignon–Ressayre point) and parallels **L-gct-012** (Muir's identity in rank form).
  - **M-007** — parallel to **L-gct-005** and **L-gct-007**: quantitative Valiant universality; Grenet is the permanent
    case.
  - **F-009** — uses **L-gct-007**, and is **L-gct-006** applied to it.
  - **M-008, O-018** — parallel to **L-gct-011**: barriers for few-row obstructions in the BIP range.
  - **F-021** — candidate parallel to **L-gct-011**. Work needed: the transfer from internal to independent padding, as in
    GCT_OBS S-004.
  - **O-011** — the checked **L-gct-215** (4×5 level spaces have dim ≤ 7) sits beside the O-011 Hessian.
    - At (p, q) = (4, 5) their bound 7 is below the quadratic-layer bound ⌊(pq − 1)/2⌋ = 9 that O-011's Hessian gives
      (PNP-MBR:A3).
    - O-011 is also a candidate parallel to **L-gct-013**.
  - **QA033** — the same statement as **L-gct-084**: the factorial transform perm(tJ + A) = T(matching polynomial),
    i.e. perm(J + t) = Σ(n − k)!·M_k(t).
