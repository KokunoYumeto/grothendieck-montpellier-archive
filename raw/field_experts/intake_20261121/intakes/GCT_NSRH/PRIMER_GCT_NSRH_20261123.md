# Primer: the mathematics of GCT_NSRH as of its final return (checkpoint 09, 21 Nov 2026)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), the intake agent of this run, 23 Nov 2026, for the main
session to read after a compaction. It restates; it does not develop.

**The run.** Prompt 24, "Mulmuley's nonstandard Riemann hypothesis (GCT IV, VII, VIII) against the sign-only purity of
Alpöge's step 5". GPT-6 Astra (ChatGPT Pro mode); the run records its effort as "not exposed".
- Final return: `grothendieck_archive_transcription_20261110\research_returns\GCT_NSRH_checkpoint_09_20261121T0545Z_unzipped\GCT_NSRH.tex`.
  It contains F01–F69 in 259 pages.
- Our intakes: `field_experts\intake_20261121\intakes\GCT_NSRH\`. They are part 1 (cp01), cp03, part 2 (cp05),
  part 3 (cp06) and part 4 (cp09).
- Line numbers below are those the intakes give, at the checkpoint named.

**Input A.** Alpöge's theorem, the Riemann hypothesis for every Dirichlet L-function, ζ included (20 Nov 2026, Lean),
is a theorem. This run uses only the *mechanism* of his footnote 3 (p. 3): sign-only purity by iterated Parseval. It does
not use the theorem itself.

**Check labels** (from the intakes' check events):
- `[TPC]`: targeted proof check by our intake;
- `[COMP]`: computation by our intake;
- `[stmt]`: statement level only;
- `[part]`: read in part.

## 1. The main question: a sign-only purity criterion (F01–F04, F17, F24, F32, F50)

### F03, the tensor-path purity criterion `[TPC]` (part 1)

**Statement.** Let a finite Weil system have:
- traces t_n with a pointwise bound |t_n(x)| ≤ B·Q^{a/2};
- a nondegenerate kernel K_h (path identity K_hK_h^* = Q^d·I);
- **opposite path-output signs at an unbounded set of path lengths k**;
- a dual system with the rational duality scalar q^{a+d}.

Then every visible Frobenius root has |α| ≤ q^{a/2}, and dually ≥, so the system is pure.

**Lemmas.**
- F01 (path identity and Parseval bound): the k-fold path sum is t^T K_h D K_h ⋯ K_h t, and it is at most
  (Q − 1)·Q^{d(k−1)/2}·‖t‖₂²·‖t‖_∞^{k−2}.
- F02 (finite spectral no-cancellation): the generating function has a genuine pole at each 1/α_j; Cauchy–Hadamard.

**Mechanism.**
1. The error is bounded: |R_{k,n}| ≤ B^k·Q^{k(a+d)/2 + d/2 + 1}.
2. The sign algebra: −ε^k R = Σβ^n + Σ_tuples (α₁⋯α_k)^n, with every multiplicity positive.
3. The diagonal tuple gives α^k, which cannot cancel.
4. Fix k, let n → ∞, then let k → ∞.

**Variants.**
- F04 allows o(k) errors in the exponent `[TPC]`.
- F17 allows an extension degree e_k that depends on k, and a separate dual system `[TPC]`.

**Good for:** the clean conditional form of Alpöge's footnote-3 mechanism. Deligne's Weil I skeleton, with the sign
replacing the weight. It was folded into the Hexagon note H01 (sign-only Deligne purity).

### F24, signed Euler spectra at even k `[TPC]` (cp03)

**Statement.** F03 holds with its input sign replaced by *real nonzero coefficients on a finite visible spectrum*, at even
k.

**Mechanism.**
1. Take the top-radius part F. F^k is not nilpotent (Vandermonde).
2. Its coefficient sum (Σc)^k is ≥ 0 at even k, so some top coefficient is > 0.
3. That coefficient cannot be cancelled by roots of smaller radius.

**Two counterexamples, both checked.**
- Without visibility: t_n alternating 0, 2.
- Without real coefficients: t = i, k ≡ 2 mod 4.

**Also: F32** (countable admissible spectra), read at the level of the generating-function proof.

### F50, Gaussian path signs and the exact weight gate `[TPC]` (part 2; cp05 lines 4563–4991)

**Statement.**
- In odd characteristic put G_ψ = H_c¹(A¹, 𝓛_ψ(x²)) and J_ψ(C) = 𝓛_ψ(x²) ⊗ p*(C ⊗ G_ψ^∨)[1].
- J_ψ encodes every effective finite Weil space: RΓ_c(A¹, J_ψ(C)) = C.
- It is fully faithful into perverse Weil sheaves.
- It satisfies F03's path-sign hypothesis exactly, at the unbounded good set k = 2pr.
- The pointwise and dual bounds that F03 needs hold **iff C is pure**.

**Mechanism.**
- The tridiagonal determinant d_k = (h/2)^k·U_k(1/h) is squarefree when p ∤ k + 1.
- RΓ_c(H_k, 𝓛_ψ(Σx_i²)) is concentrated in degree k − 1. Proof:
  - the pencil in h: the generic fibre is rank one;
  - at the simple roots, a Schur complement;
  - the Kummer factor χ(d_k) has monodromy −1;
  - no weight theorem is used.
- The trace identity: QN = −Tr(F^n | B_{k,ψ}).

**Good for:**
- It locates the whole obstacle of the sign-only route. **The sign is always free; all the content is an independent
  pointwise (stalk) weight bound.**
- By-product: a weight-free, sign-only proof that |Gauss sum| = q^{1/2}. The result is classical; the proof is new as far
  as we know.
- Folded into H01 v2.

## 2. No single finite Weil object carries the nonstandard traces (F26, F42, F48, F51–F55)

- **F26 `[TPC]`.** A rational normalization is not a finite Weil trace.
  - f(b^n) is an exponential polynomial iff f is Laurent.
  - 24 + 16x²/(x+1)⁴ has a pole at x = −1.
- **F42 `[TPC]`.** No common finite Frobenius spectrum carries all words.
  - 40·D_n^k = 40·Σ_j C(2k,j)·q^{(k−j)n} has 2k + 1 distinct roots.
  - A fixed finite F has boundedly many poles.
- **F48, F51, F52, F54 `[stmt]`.** "Frobenius retuning" forces monomial or root-of-unity spectra.

**Consequence.** The dictionary v = q^{n/2} can't come from one finite Weil object. Any nonstandard RH must use
word-dependent, completed or mixed objects (F35, F41, F45 `[stmt]`).

## 3. Positivity of the nonstandard Hecke algebra Ȟ_r: what survives

Notation: P_s = C′_s⊗C′_s + C_s⊗C_s in H_r ⊗ H_r, and D = (v + v⁻¹)².

### Rank three

- **F09 `[TPC]`.** The rank-one cone: P has entries −δ at (e, s) in the C′⊗C′ basis.
- **INT-NSRH-1, by our intake** (part 1; recognized in part 3 as Θ² of IV Prop. 11.6).
  - θ: T_s ↦ −T_s⁻¹ gives θ(C′_s) = −C_s, so θ⊗θ fixes Ȟ_r.
  - Hence C′⊗C′ coordinates = (−1)^{l(x)+l(y)} × C⊗C coordinates, for every r.
- **INT-NSRH-2, by our intake `[COMP]`.**
  - The ten alternating words 1, x, …, xyxyx in P₁, P₂ form a Z[v^±]-basis of Ȟ₃.
  - Every one of them has all C⊗C coordinates in N[v^±].
  - Positivity at r = 3 was known in another basis (IV Remark 11.19).
- **F43, F45, F46 `[stmt]`.** A positive module basis at rank three; word motives with hard Lefschetz; pure Weil End/Hom
  objects.

### Rank four, where strict positivity breaks

- **F57 `[TPC]`, `[COMP]`** (part 3; cp06 lines 8623–8934).
  - The word ω = P₂P₃P₂P₃P₂P₃P₁P₂P₁P₂P₁ has trace p(D) = −D⁹ + 20D⁸ − … − 1024D on the five-dimensional simple module
    N^# of Ȟ₄ (IV §11.8).
  - Its coefficients at v^{±18} are −1.
  - So no basis of N^# makes P₁, P₂, P₃ nonnegative.
  - Mechanism: Θ(P_i) = Q_i, the contragredient, and an exact sympy trace.
- **INT-NSRH-4, by our intake `[COMP]`** (part 3).
  - In the C⊗C basis of H(S₄)⊗H(S₄), the same word ω has 6 negative coordinates at the extreme degrees.
  - P₁, P₁P₃, P₂P₁P₃P₂ and P₁P₂P₁P₃P₂P₃ are positive.
- **F58 `[TPC]`** (part 4; lines 9153–9340). A strictly positive basis cannot respect source cells.
  - Support graphs of N[v^±]-matrices are the same generically and at v = 1.
  - On N₆ = M̌_{(3,1),(2,2)} the only top-to-bottom arrow (c₀ = (v − v⁻¹)²) dies at v = 1.
  - This excludes IV Conj. 19.1(ii)–(iii) together with strict positivity.
- **F67 `[TPC]`, `[COMP]`** (part 4; lines 15171–15330). Iterated tensor products.
  - Take R_i = N_i⊗N_i + (mI − N_i)⊗(mI − N_i) on Blasiak's M̌^{(3)}.
  - Tr(R₁R₂) has coefficient −12 at v^{±10}.
- **F59 `[part]`.** No bounded Soergel lift of P_s with P_s² ≅ δ²P_s over scalar coefficients. The Tor inequality
  (Lichtenbaum) was read; the generic-cohomology step was not.

**Summary.** Strict positivity of the nonstandard objects is a rank-three phenomenon throughout: algebra words, module
bases and tensor iterates. From rank four on, only signed or factored forms (IV, VIII) or derived forms can survive.

### Later answers to the rank-four question (GCT_POS, our intake of 22 Nov)

- **N-003:** a positive K-basis of B₄ in the C⊗C cone exists.
- **N-009:** the integral order is not free, so there is no Z[v^±]-basis.
- **N-002:** the first negative P-word has length 5 (P12132).

## 4. Other findings

- **F34 `[TPC]`** (cp03). VI Hypothesis 1.6.4(2) is false under compact binary input, and binary plethysm is not #P.
  - The two-row count c_k(N) = [z^N]·Π_{i=2}^k (1 − z^i)^{−1} has Ehrhart dimension k − 2, against VI's poly(O(log k)).
  - k = 2m, N = m(m+1) gives ≥ 2^{m−1} solutions on O(log m) bits.
  - It was a Hexagon candidate, gated by a literature search (Fischer–Ikenmeyer).
- **F05–F16 `[TPC]`.** Elementary lemmas and countermodels. F12 (Reynolds projector) is BIP's (4.1).

## 5. Open rows at the end (their final gates)

1. **Gate R/S, the stalk gate.** An independent local or dual weight bound for a trace system carrying the nonstandard
   coefficients. By F50 this is the whole task.
2. **Designated bases and global labels.** VIII's canonical bases; IV Conj. 19.1 at rank ≥ 4, now in signed/factored
   form only.
3. **Higher quotient and filtered composition (F69).** Bounded nonflat coefficients on both sides: F59's escape, through
   polynomial-differential bimodules.

## 6. Where the results went

- F03, F24 and F50 went into **H01** (sign-only Deligne purity; Hexagon hexagon:2611.00789).
- INT-NSRH-1, -2 and -4 went to the **consult** `reports_20261120\split_zero\consults\CONSULT_a8d75352_NSRH_WEIL.md`.
- The **E4 rank-three constants** (`reports_20261120\split_zero\consults\E4_RANK_FOUR_20261121.md`) gave P-F-E3-01 and the
  GCT VIII erratum **H23** (Conj. 3.2 has no minimum, N-012; unimodality fails at r = 3; the printed b₂ has the wrong sign).
- GCT_POS's nonstandard branch (N-001–N-016) answered the rank-four questions above.
- The successor targets proposed in part 4, section 6: the stalk gate; a positive basis of Ȟ₄; polynomial-differential
  lifts.
- **pequalnp fleet:** no edge. The joint lemma space (`<local>/pequalnp_work\fleet_map\JOINT_GCT_LEMMA_SPACE.tsv`)
  lists GCT_NSRH's 69 ids with no cross edge.
