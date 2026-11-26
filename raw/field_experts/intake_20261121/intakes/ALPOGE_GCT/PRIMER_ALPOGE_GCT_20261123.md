# Primer: the mathematics of ALPOGE_GCT as of its final return (checkpoint 09, 21 Nov 2026)

By agent a0805369bae2ebddc (Claude Opus 5.5 at effort high), for the main session to read after a compaction. It
restates; it does not develop. Run: prompt 23, GPT-6 Astra (ChatGPT Pro mode), effort not exposed. Final return:
`research_returns\ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped`. Files below are in its `work\`.

**Check labels**, from my intakes (parts 1-4, the cp03 addendum, all in this folder):
- `[TPC]`: targeted proof check by our intake;
- `[TPC+COMP]`: that, plus our own computation;
- `[COMP]`: our computation only;
- `[MAIN]`: targeted proof check with computations by the main session (Claude Opus 5.5 at effort max), 22 Nov;
- `[stmt]`: statement level only.

**Setting.** GCT VI is Mulmuley, *Geometric complexity theory VI: the flip via saturated and positive integer
programming in representation theory and algebraic geometry* (arXiv:0704.0229v4). A stretching function
f(s) = mult(sπ, sλ) is a quasi-polynomial. Its positivity index p(f) is the least shift making every constituent's
coefficients ≥ 0 (Def. 1.2.2), and its saturation index s(f) the least shift making every nonzero constituent > 0 at
all integers ≥ 1 (Def. 1.2.4). PH1 (1.6.4) asks for polytope counting, SH (1.6.5) for small s(f), PH2 (1.6.6) for small
p(f), and PH3 (1.6.7) for a positive rational form ∑ h_i t^i / ∏(1−t^{a_j}) with max a_j polynomial in the parameter.
For plethysm the parameter is h = O(n⁶) here; for Kronecker it is rank(x) = n² + 5n (Hyp. 3.3.4, §3.4).

## 1. The Kahle-Michałek ray and the printed Theorem 1.6.1(d)

- **P-K1 (cited: Kahle-Michałek, *Obstructions to combinatorial formulas for plethysm*, Thm 5) `[COMP]`.**
  φ(s) = mult of S_{(7s,5s)} in Sym^{4s}(Sym³C²) equals ⌊s/3⌋ + 1_{2|s}. φ(1) = 0 but −φ(−1) = 1, so φ is no
  homogeneous Ehrhart function: the literal homogeneous PH1 is false.
- **P-F1 `[TPC+COMP]`** (`positivity.tex`): a shifted two-dimensional polytope counts φ, and no eventually
  one-dimensional model exists in any ambient lattice. Proof outline: the affine hull stabilizes; the t-interval
  endpoints are eventually affine with slope difference 1/3; the jumps +2 at s ≡ 5 and −1 at s ≡ 0 mod 6 exclude
  both cases.
- **P-F2 `[TPC]`** (`positivity.tex`): every positive rational series ∑h_i T^i/∏(1−T^{a_j}) is one shifted polytope
  count. Construction: selector variables e_i (one equals 1), slack u, and ∑ a_j x_j = s − i.
- **P-F12 erratum, PL-Q22 `[TPC]`** (`positivity_ph3.tex`): GCT VI Theorem 1.6.1(d) as printed (numerator of degree
  d over d+1 factors, h₀ = 1) fails on the KM ray. Two factors with numerator 1 + cT force c = 0 and weights 2, 3, and
  then the coefficient of T⁴ is 1, not φ(4) = 2. The correct form is Cohen-Macaulay freeness over an h.s.o.p., with an
  unrestricted numerator. This is note E1 (`reports_20261120\errata\NOTE_E1_Mulmuley_GCT_VI_draft.md`).
- **PLE-F5, F6, F7 `[TPC]`** (`plethysm.tex`); **PLE-F8 `[TPC+COMP]`** (`positivity_actual_plethysm.tex`).
  - The ray's stretching algebra *is* the D₅ Kleinian ring ℂ[U,V,Z]/(Z² − UV² − 4U⁴) = ℂ[x,y]^Γ, Γ binary dihedral of
    order 12, with Hilbert series (1+t⁴)/((1−t²)(1−t³)).
  - It is Gorenstein with H(1/t) = t·H(t) (Stanley reciprocity, not Ehrhart's).
  - φ(qs) is Ehrhart exactly when gcd(q,6) > 1.
  - The quotient has the cohomology of A²: q² points over every F_q, compactly supported cohomology ℚ_ℓ(−2) in degree 4.
  - Good for: purity of the geometry does not force homogeneous Ehrhart counting.

## 2. PH3 implies PH2, with a bound

- **P-F11 `[TPC]`** (`positivity_modular.tex`): a positive rational form with modular index A (largest a_j), r
  factors and numerator degree h gives p(f) ≤ h + 128 r³A³. Mechanism: pole orders at roots of order ≤ A,
  |1−ζ^a| ≥ 4/d, Cauchy bounds on the principal parts, and a binomial comparison making the error ≤ 2/7. The period
  (an lcm) is not needed.
- **P-F12 `[TPC]`** (`positivity_ph3.tex`): for stretching families (plethysm, and Kronecker through
  GL_a × GL_b → GL_ab), r ≤ d_λ + 1 ≤ dim G + 1 by Weyl growth, so PH3 implies PH2 with
  p(f) < (d_λ+1)A + 128(d_λ+1)³A³. GCT VI only says that PH2 "may also follow" from PH3 (main.tex l. 3962).
- Its premise is now false for plethysm (§3) and for Kronecker coefficients (GCT_POS).

## 3. PH3 fails for plethysm with inner shape (3)

The family: μ = (3), λ = (n/g), π = det^{3/g}, g = gcd(n,3). f_n(s) is the dimension of the SL_n-invariant n-ary
cubic forms in the appropriate degree; T^{(n)} is that invariant ring, regraded. Put M = 2^{n−1}.

- **P-F19, the canonical clause `[TPC+COMP]`** (`positivity_cubic_counterexample.tex`).
  - The chain cubic F_n = x₁²x₂ + … + x_{n−1}²x_n + x_n³ is smooth, so the discriminant (degree n·2^{n−1}) does not
    vanish there. Every h.s.o.p. therefore has a member nonzero at F_n.
  - A = diag(ζ^{(−2)^i}), ζ of order 3·2^{n−1}, fixes F_n, and det A has order 3·2^{n−1}/g. Hence every invariant
    nonzero at F_n has stretch degree divisible by 2^{n−1}.
  - The modular index of the canonical (lexicographically minimal h.s.o.p.) form is ≥ 2^{n−1}.
  - Classical input: chain forms, Busé-Jouanolou Ex. 4.12.
- **P-F31, the existence clause `[TPC+COMP]`** (`positivity_actual_cubic_pole.tex`). For n ≥ 4 the Hilbert series of
  T^{(n)} has a simple pole at every primitive M-th root of unity. So every form has some a_j divisible by M, and
  both clauses of PH3 fail. Its lemmas:
  - **P-F23, the fixed-locus residue formula** (`positivity_noncancellation.tex`) `[TPC]`. At a primitive root of
    order M, the leading coefficient is e_Y / det(1 − g | N*_{Y/X}), from the Koszul resolution of the fixed-locus
    ideal. This is a Lefschetz-Riemann-Roch formula for graded rings. The several-component version is P-F23g.
  - **P-F26 `[TPC, in part]`** (`positivity_finite_lift.tex`): a nonzero μ_M-fixed quotient point lifts to a
    polystable F with a diagonal A of two-power order and det A of order exactly M.
  - **P-F30 `[TPC+COMP]`** (`positivity_full_cubic_support.tex`): maximal determinant order forces the chain support.
    Proof by Cramer and Hadamard; the case q = 0 uses **P-F27** (`positivity_graph_support.tex`), which the main
    session read on 22 Nov `[MAIN]`. My exhaustive check found maximum 2^{n−1}, attained only by chains, for n ≤ 4;
    the main session's check covers n ≤ 6.
  - **P-F24 `[TPC, in part]`** (`positivity_chain_smoothness.tex`): the quotient is smooth along the chain orbit
    (Luna), with a one-dimensional fixed locus.
  - **P-F28 `[stmt]`** (`positivity_chain_residue.tex`): e_Y = 1.
  - Classical check: at n = 4 Salmon's series (1+t²⁵)/((1−t²)(1−t⁴)(1−t⁶)(1−t⁸)(1−t¹⁰)) has the predicted simple pole
    at primitive 8th roots.
- **P-F35 `[COMP]`** (`positivity_quaternary_indices.tex`): for n = 4 both indices are 23. So a large pole does not by
  itself give large indices.

## 4. PH2 and SH(a) fail for the same family

- **P-F56 and P-F57 `[TPC+COMP]`** (`positivity_paired_wave.tex`, `positivity_dyadic_dominance.tex`,
  `positivity_dyadic_far_increment.tex`).
  - **Statement.** For every fixed 0 < c < 1/4 and all large n, p(f_n) > 2^{cn} and s(f_n) ≥ 2^{cn}. Explicitly
    p > 2^{n/8} and s ≥ 2^{n/8} for n ≥ 2·10⁸⁰. So narrow PH2 (1.6.6) and SH(a) (1.6.5(a)) are false. SH(b) is not
    claimed.
  - **Step 1, the dyadic wave.** The poles with two-part ≥ M are exactly the primitive M-th roots, all simple (P-F23
    with P-F30 at orders 2^a > M). So v₂ of the least period is n−1, and q_r − q_{r+L/2} = 2W_n(r) is constant.
  - **Step 2, the one-witness test.** If p(f) ≤ x then f_n(x) ≥ 2W_n(x), and the same holds for s + 1. So one x with
    2W_n(x) > f_n(x) gives both bounds.
  - **Step 3, the residue.** The exact residue is ∏_{b∈S_n}(1−ζ^{gb})^{−1}, from the conormal character
    Sym³V − V⊗V* at the chain, and log₂|Z_n| ≥ n⁴/24 − 2n³.
  - **Step 4, dominance (P-F57).** The other residues' mass E_n satisfies E_n/|Z_n| → 0 by a contraction
    Q_n ≤ ½Q_{n−1} + 2δ_n, with near-multiplier and far-multiplier (layer-cake) estimates. Then f_n(x) ≤ 2^{(c/6)n⁴+…}
    at x ≈ 2^{cn} is smaller than the wave.
  - My computation: E_n/|Z_n| for n = 5..16 falls to 3.7·10⁻⁵⁴, below 1/4 from n = 8.
- Later, in GCT_POS: the threshold was lowered to n ≥ 79,000 and a witness p(f₉) > 7 found (PNEW-002 to 006; not
  intake-proof-checked).
- **P-F34, P-F42 `[TPC]`** (`positivity_fourier_index_gate.tex`, `positivity_cubic_average_upper.tex`): the earlier
  gate. A bound on the coefficient norm U_n of the pole-at-1 part below 2^{n⁴/24} would force exponential indices.
  The top fifth of the coefficients is controlled (exponent log₂5/60 < 1/24).

## 5. Other checked results

- **P-F14, P-F15 `[TPC]`** (`positivity_torus.tex`). GCT VI's general Hypotheses 3.3.2(a), 3.3.3 and 3.3.4 fail as
  stated for subgroup restriction, because rank(x) omits the embedding weights. ρ_N = diag(t^{N+1}, t) gives modular
  index N at rank 5; σ_N gives p = s = N−2 at rank 6 (via P-F10).
- **P-F9, P-F10 `[TPC]`** (`positivity_bounds.tex`): the weighted plane has indices exactly ab−a−b.
- **P-F3 to P-F8 `[TPC]`** (`positivity.tex`): virtual versus effective, and P-F8: a strict multiplicity inequality
  obstructs orbit-closure containment, while support data alone does not.
- **PL-01 to PL-08 `[TPC]`** (`plethysm.tex`): cote 133 identities. PL-01: in the Burnside ring of C₂,
  2λ²(E) + E ≠ E² for the free orbit, which refutes our study's "checked" line on scan 19 (= GCT_PLETH A-001).
  PL-02: the Burnside structure is not special. PL-08: exterior powers do not descend to the Witt group.
- **C-GRH-01 to 03 `[TPC]`** (`complexity.tex`). Alpöge's theorem gives the Dedekind GRH of abelian fields
  (ζ_K = ∏L(s,χ), Washington Thm 4.3). C-GRH-03 (x³ − 2) shows that Koiran's HN ∈ AM needs nonabelian fields, so it
  stays unconditionally open; it holds conditionally on Masullo.
- **P-F60 `[stmt]`** (`positivity_tensor_chain_point.tex`): the chain tensor in (ℂⁿ)^{⊗3} has full stabilizer with
  character group μ_{2^{n−1}}, which refutes the canonical PH3 clause for Kronecker coefficients. GCT_POS later
  refuted the existence clause (K-023, R-NEW-004, K-024, PNEW-013 `[MAIN]`).

## 6. Open rows at the end

- SH(b), the density clause (1.6.5(b)), for plethysm and Kronecker. P-F48 shows the cubic family is exponentially
  sparse, so it does not refute SH(b).
- PH2, SH(a) for Kronecker: still open after GCT_POS. The gate there is PNEW-016c's coefficient-mass estimate.
- The nonstandard GCT VII-VIII positivity, the P-F52 to P-F74 branch `[stmt]`: canonical coefficient objects missing.
- The comparison with Alpöge's theta operations (Q-ALPOGE-METHOD), and any actual GCT obstruction: no complexity
  claim is made.

## 7. Where the results went

- **Hexagon register:** H02 (the 1.6.1(d) erratum, the PH3 ⇒ PH2 bound, P-F31, P-F57) and H02b (Kronecker, now
  numerical PH3 via GCT_POS). Note E1 is a draft to Mulmuley.
- **Prompts:** 52 (GCT_POS, my core), 54 (NEG_NIGHT), 56 and 56c (GCT_WRITEUP: Paper A's A1, A3, A5, A6, and note
  N1), 57 (GCT_FLIP, with H24).
- **Other runs:** GCT_POS built the Kronecker refutation on P-F23, P-F27, P-F30. NEG_NIGHT NN-G002, G004 and G018
  apply P-F31 and P-F57. GCT_PLETH found PL-01 and PL-08 independently.
