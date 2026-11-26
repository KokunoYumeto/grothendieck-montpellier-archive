# Primer: the mathematics of TRACE_DET as of its final return (21 Nov 2026, 02:18 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), the intake agent of this run, 23 Nov 2026, for the main
session to read after a compaction. It restates; it does not develop.

## The run

- **Prompt 33,** "cote 1's trace formula and the determinants". The run is GPT-6 Astra (ChatGPT Pro mode); it records its
  effort as "not exposed".
- **The question.** Are Alpöge's determinants Grothendieck's det(1 − wB) of cote 1, so that his sign would be B ≥ 0? And
  how does Masullo's trace formula compare?
- **Final return:** `grothendieck_archive_transcription_20261110\research_returns\TRACE_DET_final_20261121T0218Z_unzipped\`,
  with the paper `deliverables\TRACE_DET.tex` (81 pp., 79 question rows, 426 check events).
  - It is INCOMPLETE on five rows, because the session ended.
  - Our intakes: `INTAKE_TRACE_DET_20261121.md` (checkpoint 02) and `_part2.md` (final), in this folder.
- **Input A.** Alpöge's theorem: RH for ζ and every Dirichlet L-function, 20 Nov 2026, formalized in Lean. Cite it as a
  theorem. **Masullo's draft** is unrefereed, and every result resting on it is conditional. See the memory note
  "Masullo's draft: not a fix, no credence".

### Check labels (from the intakes' check events)

| Label | Meaning |
|---|---|
| `[TPC]` | targeted proof check |
| `[IRP]` | independent re-proof |
| `[part]` | read in part |
| `[stmt]` | statement level |

## 1. The answer to the main question: no

Alpöge's determinants are finite algebraic determinants (Gram, Capelli and period determinants). They are not
compressions of B, and his sign is a balanced-inertia sign, not matrix positivity.

### B-01 `[TPC]` (cp02 lines 62–113)

- **Statement.** Ξ(√w)/Ξ(0) = det(1 − wB), with B = diag(γ_j^{−2}) on ℓ². B ≥ 0 iff RH.
- **Proof.** The genus-zero Hadamard product at order 1/2, with Σ|γ|^{−2} < ∞. γ^{−2} > 0 iff γ is real.
- **Good for:** the archive dictionary, Grothendieck's det(1 − wB) of cote 1. B is zero-coded: it is built from the zeros.

### Lemmas around it

- **DET-04 `[TPC]`.** A rank-one non-selfadjoint perturbation has the same determinant and traces. So a determinant does
  not force positivity of every realization.
- **B-02 `[TPC]`.** No trace-class T has det = Ξ itself, because Σ|γ − a|^{−1} diverges.
- **DET-01, DET-02, DET-03 `[TPC]`:**
  - the q = 3 Fourier matrix is not selfadjoint (eigenvalue i√3);
  - open paths are matrix coefficients a*A^{k−1}a, not traces;
  - a fixed finite determinant is a polynomial.
- **DET-11 `[IRP]`.** C = B(I + B/4)^{−1} gives det(I − s(1 − s)C) = 2ξ(s).
  - Eigenvalues: 1/(γ² + 1/4).
  - 1 − s(1 − s)c = ((s − 1/2)² + γ²)/(γ² + 1/4).
- **STEP6-03 `[stmt]` + lemma read.** One-sided bounds of G_ζ give zero-free half-planes (Landau, through the DET-11
  Mellin identity).

### The actual sign in Alpöge's Lean (DET-05 to DET-10, DET-12 to DET-14, STEP7-01, STEP7-02) `[stmt]`

- The finite determinants are those of FinalG.lean, lines 21–22.
- DET-06: the Gram matrix is indefinite. DET-10: the sign is an inertia balance.
- DET-05 names the bridge that would suffice: common-Hilbert-space positive finite-rank approximants converging in S₁.
  The finite arithmetic family it needs is the open gate.

## 2. Positive forms of RH and GRH on the cote 1 side (final return)

### DET-16, the arithmetic cosine kernel `[TPC]` (final lines 2319–2518)

- **The kernel.** k(t) = Σ_ρ N_ρ·e^{(ρ−1/2)t}/(ρ(1 − ρ)).
- **Statement.** RH ⟺ k is bounded ⟺ k is of positive type.
- **Proof.**
  1. Positive type gives boundedness, by the two-point Gram matrix.
  2. Boundedness gives G_ζ ≥ −K√X.
  3. Landau (STEP6-03) at θ = 1/2, with the functional equation, then gives RH.
  4. Atoms and integer multiplicities are recovered by Cesàro (sinc) averages; the cyclic model is L²(μ_K).
- **With input A** the positivity is unconditional. The result is classical in substance (explicit formula plus Bochner).
- **Good for:** the SA23 "B ≥ 0" without a zero list. It says B ≥ 0 ⟺ the explicit-formula kernel is of positive type ⟺
  RH, which is now a theorem.

### DET-18, a weighted-character determinant `[part]`

- **Statement.**
  - M = 2(3o + 1).
  - 𝒫_M(s) = det(I − s(1 − s)C_{𝓛,M}), with C diagonal: entries 1/(ρ(1 − ρ)), and 4 at the centre.
  - GRH ⟺ 0 ≤ C ≤ 4I.
- **With input A** this holds for Dirichlet characters.

### DET-15, DET-17, DET-19 `[stmt]`

- DET-15: infinitely many orthogonal rank-one Bessel convolution projectors, from Alpöge's Lean
  (MatrixOfBesselTwoSidedAction.lean, lines 47–48).
- DET-17: weights Λ(n)n^{−s} on them give Tr = −ζ′/ζ.
- DET-19: the natural boost is not the arithmetic flow.

## 3. Masullo's draft (all conditional on it)

- **MAS-10 `[TPC]`, as far as read** (final lines 3094–3213).
  - **Statement.** det(I − wR₊) = Ξ(√w)/Ξ(0) on Masullo's weighted quotient. It is conditional only on his Thm 10.2.2.1,
    spectral-annihilator density, p. 446. RH is not used.
  - **Proof outline.**
    1. The translation bound ‖T_v‖ ≤ e^{B₀|v|}.
    2. The sector estimate.
    3. The trace ideal T = A^{1/2}(I + iC)A^{1/2}.
    4. A Gram–Schmidt triangular basis on the jet blocks; its totality is exactly the density claim.
    5. R = K(I − μ²K)^{−1}, with eigenvalue −1/z_ρ².
  - **MAS-11, MAS-12 `[stmt]`:** fixed Hecke characters.
- **Defects of the draft.**
  - **MAS-BOUND `[TPC]`.** The printed (10.3.2.4) (p. 454) counts one derivative order too many at odd s. The norm of p. 434
    gives divergence at s = 3, m = 1.
  - **MAS-SRC-03 `[TPC]`.** Thm 13.3.1.2 (p. 522) is empty ("Insert statement").
  - **MAS-03 `[TPC]`.** The theorem cannot be evaluated on convolution squares.
- **MAS-04 `[TPC]`.** Weil squares: true for ζ and Dirichlet L-functions by input A; otherwise conditional.

## 4. Cote 1, the archive (scans 078–082, 110–113)

- **ARC-01 `[TPC]`.** The corrected genus-zero lemma (scans 111–112).
  - The sector bound |g| ≤ Ae^{−a|z|}, a = |b|·cos θ/2.
  - The triple product g(z)g(ωz)g(ω²z) decays, so b = 0 by Liouville.
  - Three corrections: θ ∈ (π/3, π/2); |f| ≤ h(|z|); the exponent in ω².
- **ARC-02 `[TPC]`.** ∏(1 − z/n^α) has order 1/α, not 1 (scan 110; Grothendieck wrote "sauf erreur").
- **ARC-03 `[TPC]`.** 1/ρ is a liminf, not a limsup (scan 113). Counterexample: N_k = 2^{2^k}.
- **ARC-04 `[TPC]`.** The product prefactor n₁ on scan 113.
- **The finite toy.**
  - TOY-01 `[TPC]`: the bound on F_q for k ≥ 2, sharp for t ≡ 1 at odd k.
  - It needs a composite-q correction (q = 4, k = 3: R = 64 > 48); the gcd-weighted bound is exact.
  - TOY-02 `[TPC]`: diag(1, −1/2).
- **PRG-FF `[stmt]`.** Normalized Frobenius on H¹ of a curve is unitary, not positive (P₁ = 1 + 3T²).

## 5. Open rows at the end

| Row | Gate |
|---|---|
| Q-STEP1, Q-STEP4, Q-STEP7 | The historical determinants of Alpöge's steps 1, 4, 7: the declarations in his Lean, with parameters |
| Q-DIRECT-BRIDGE (Q-PERIOD-FRAME-LIMIT) | A finite arithmetic family of positive finite-rank approximants on one Hilbert space converging in S₁ (DET-05) |
| Q-TRANSCRIPTION | The cote 1 scan images, for the 16 transcription repairs (proved in the final README) |

## 6. Where the results went

- **To Hexagon:** nothing.
  - MAS-10 and MAS-11 are conditional on the draft.
  - DET-16 and DET-18 are classical in substance.
  - ARC-01 to ARC-04 wait for the image check, then a cote 1 companion paper.
- **The Masullo register:** MAS-10 and MAS-11 as conditional consequences; MAS-BOUND and the empty Thm 13.3.1.2 as defects.
- **The SA23 companion note:** B ≥ 0 ⟺ DET-16 positive type ⟺ RH, now a theorem.
- **Prompt 35 (ZETA_TWO):** DET-16 and DET-18 as the cote 1 forms of RH and GRH.
- **Links to other runs:**
  - GCT_NSRH F50 contains H¹(C_k), the PRG-FF dictionary.
  - HODGE_SIGN: DET-10's inertia sign beside the Hodge index ("a definite form gives injectivity, not positivity of a
    basis").
- **pequalnp fleet:** no edge (not a GCT run).
