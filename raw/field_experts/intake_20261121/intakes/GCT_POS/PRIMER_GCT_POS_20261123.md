# Primer: the mathematics of GCT_POS as of its final return (22 Nov 2026, 02:19 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), 23 Nov 2026, for the main session to read after a
compaction. It restates; it does not develop.

## The run

- **Prompt 52, GCT positivity.** The run is GPT-6 Astra (ChatGPT Pro mode); it records its effort as "not exposed".
- It ran with two branches:
  - items 1–7, 10, 11: Kronecker, plethysm, saturation, density, formulas;
  - items 8–9: the nonstandard branch.
- It ended INCOMPLETE at 02:01 UTC on 22 Nov, after two reviews without movement.

**Files.**
- Final return: `grothendieck_archive_transcription_20261110\research_returns\GCT_POS_final_20261122T0219Z_unzipped\`.
  It holds `GCT_POS.tex`, `certificates\`, `branches\nonstandard\`.
- Intakes, in this folder:
  - `INTAKE_GCT_POS_20261121_kronecker.md` (checkpoint 03) and `INTAKE_GCT_POS_20261122_final.md`, both by a0805369
    (Claude Opus 5.5 at effort high);
  - `INTAKE_GCT_POS_20261121_nonstandard.md`, with its "Full depth" section, by a8d75352 (Claude Opus 5.5 at effort
    high);
  - the main session's check of the PH3 chain: `reports_20261122\gct_pos_ph3_check\CHECK.md` (Claude Opus 5.5 at effort
    max).

**Inputs.** Neither Alpöge's theorem nor Masullo's draft is used. The final intake verified this by a text search of 575
files.

**Check labels.**

| Label | Meaning |
|---|---|
| `[TPC]` | targeted proof check |
| `[COMP]` | computation by an intake |
| `[MS]` | the main session's check |
| `[stmt]` | statement level |

## 1. The main result: numerical PH3 fails for Kronecker coefficients (Hexagon H02b)

Notation: k_n(s) = g((s^n), (s^n), (s^n)), the triple-rectangular Kronecker coefficient. It is the Hilbert function of
ℂ[(ℂⁿ)^{⊗3}]^{SL_n³}. Put M = 2^{n−1}.

**Statement** (K-023, R-NEW-004, K-024, PNEW-013 `[MS]`). For every n ≥ 2 the series Σ k_n(s)t^s has a pole of order
M·3^r for some r ≥ 0. So every positive form of k_n has denominator weight ≥ 2^{n−1}. This refutes the existence clause of
GCT VI Hypothesis 3.3.4 (numerical PH3), with rank(x) = n² + 5n from §3.4.

**Proof.**
1. **K-023.** The cyclic permutation of the three tensor factors has trace b_n, an SL_n-invariant count on
   W ⊕ S_{(2,1)}W. Then k_n ≡ b_n mod 3, by the Adams operation ψ³ on Schur functors.
2. **R-NEW-004.** The hook-chain vector has zero Lie stabilizer.
3. **K-024.** b_n's series has a simple pole at order M, with residue a 3-adic unit. Its proof:
   - Lefschetz–Riemann–Roch at the unique fixed curve;
   - inputs ALPOGE_GCT P-F23, P-F27, P-F30 (ours, unpublished).
4. **PNEW-013.** Series congruent mod 3 transfer the pole, so k_n has one at some order M·3^r. Its printed citation is an
   erratum (final intake §4).

**Small cases.** The exact order M (r = 0) is known for n = 2, 3 (classical series) and for n = 4, 5:
- **K-008 `[COMP]`, n = 4.** The μ₈ fixed locus is 13 curves. The simple pole at the primitive 8th roots has residue
  (14 − 10√2)/256.
- **K-014 `[COMP]`, n = 5.** 424 fixed curves; the pole is at the primitive 16th roots. Confirmed given K-011's
  completeness.

**Good for:** GCT VI's flip hypothesis for the coefficients it names. It extends our plethysm refutations to Kronecker
coefficients. Those are H02, from ALPOGE_GCT and GCT_PLETH:
- P-F19 (SH(a));
- P-F31 (PH3);
- P-F57 (PH2);
- P-F14 had refuted 3.3.4 only for torus restriction.

## 2. Supporting Kronecker results

- **K-001 `[COMP]`.** n = 3: H₃ = 1/((1 − t²)(1 − t³)(1 − t⁴)) (Vinberg; Bremner–Hu, arXiv:1112.2949, Th. 2.4).
- **K-002 to K-007 `[TPC]`, `[COMP]`.** n = 4, order 8: 4 feasible spectral types among 2,285 (Farkas certificates); full
  stabilizers; smooth fixed curves; local residues; edge doubling; the lift bound.
- **K-009 `[TPC]`.** No pole at a primitive root of order above B_n = (3 − 2/n)^{(3n−2)/2}/n. Proof: 3n² nonzero minors,
  then AM–GM.
- **K-018 (Hexagon GPK18) `[COMP]` at n = 9.**
  - The premise "maximal order 2^{n−1}" is false.
  - Polystable free supports have determinant order 2^{n−1+⌊(n−2)/7⌋}; n = 9 gives 512.
  - K-020 and K-021 `[TPC]`: smooth density-one curves at n = 2 + 7k; the fixed scheme grows cubically.
- **R-NEW-003 `[TPC]`.** H₄ = (Σ_{j<3196} P_j t^j)/D₄(t), with an explicit denominator.
- **K-025 `[TPC]`.** n = 26: a stabilizer of order 3·2^25, so odd inertia exists. Why r = 0 doesn't follow.
- **R-DIAG-001 `[TPC]`.** Freeness doesn't give 3-integrality.
- **K-026 to K-038 `[stmt]`.** The r = 0 gate is one virtual coherent class on collision closures (K-031). It exists at
  n = 18 (K-037, K-038).
- **PNEW-014 `[stmt]`.** A formal model shows that K₀ congruences alone cannot decide PH2 or SH(a).
- **PNEW-016 `[TPC]`** (a, b on the lines read; c given PNEW-015 and K-024). For n ≥ 79004, either
  - p(k_n) > 2^{n/16} and s(k_n) ≥ 2^{n/16}, or
  - the coefficient mass is ≥ 2^{(17/240)n⁴ − 6n³ − 4}.

  This dichotomy decides neither PH2 nor SH(a).

## 3. Plethysm, formulas, density

- **PNEW-001 `[COMP]`.** n = 4, x = 19: 2W₄(19) = 1/8 > 0 = f₄(19), a corollary of P-F35.
- **PNEW-005 `[TPC]`, given PNEW-002 to 004.** p(f_n) > 2^{n/8} and s(f_n) ≥ 2^{n/8} for n ≥ 79,000.
- **PNEW-006 `[COMP]`, given the exterior identity f_n(s) = [det^n : Λ^{ns/g}(Λ³ℂ^{3s/g})].** The witness p(f₉) > 7.
- **PNEW-009 `[stmt]`.** Narrow SH(b) for fixed rank and fixed inner μ.
- **PNEW-010 `[stmt]`.** G-040's literal construction is superpolynomial in b (H21: "polynomial for each fixed b").
- **PNEW-012 `[stmt]`.** Outer degree six, two-row output: 330 polytopes (Pak–Panova–Swanson).
- **R-NEW-001 `[COMP]`.** The outer-six table: 5,214 coefficients, recomputed independently, 0 mismatches. It extends
  H20's checked range.
- **R-NEW-002.** The r = 3, 4 annihilators vanish by known rank laws (McKay; Cheung–Ikenmeyer–Mkrtchyan). Background.

## 4. The nonstandard branch (items 8–9; a8d75352's intake)

**Read with proofs or rerun.**
- **N-012 `[TPC]`.** GCT VIII Conj. 3.2, as printed, has no minimum. In the rank-one case y_n = q^{−n} lies in
  R^{−n} ∩ R̄^{−n}, of degree −n. This went to Hexagon **H23**, with P-F-E3-01.
- **N-002 `[COMP]`.** The first P-word of Ȟ₄ outside the C⊗C cone has length 5: P12132. The computation shares code
  lineage with our h4cone.py.
- **N-003 `[COMP]`, rerun 114/0.** A positive K-basis of B₄ in the C⊗C cone exists.
- **N-009 `[COMP]`, certificate rerun PASS.** The integral order is not free: Ȟ₄ has no Z[v^±]-basis.
- **N-004 `[TPC]`**, modulo Abedelfatah; **N-007, N-008, N-011 `[TPC]`**; **N-010**, exit status only.
- **N-006.** The stalk purity of π*M(1) equals the purity of M, which is circular, as F50 is in GCT_NSRH.

**Statement level:** N-013 to N-016. N-015's rerun was stopped.

## 5. Open rows, with gates

| Row | Gate |
|---|---|
| Exact order M (r = 0) for n ≥ 6 | K-031's moving Koszul class on collision closures must cancel a unit mod 3. Attack: evaluate it on the n = 18 component (K-038), or the C₃-equivariant refinement of K-023 |
| PH2 and SH(a) for Kronecker coefficients | the estimate U_Δ^+(n;P) < 2^{(17/240)n⁴ − 6n³ − 4} (PNEW-016c). A subquartic bound would also prove r = 0. Attack: a direct off-residue witness at n = 4 from R-NEW-003 |
| The K-018 orders | literature: Kravtsov; Franks–Reichenbach |
| Q3, Q4, Q5 | SH(b) in varying embeddings; uniform positive formulas; outer degree six beyond two rows |
| Nonstandard | a designated positive basis of Ȟ_r beyond K-bases; VIII's canonical bases |

## 6. Where the results went

- **Hexagon register:** H02b (Kronecker PH3; prompt 56 GCT_WRITEUP); H02 (plethysm); GPK08 (n = 4, 5 poles, absorbed in
  H02b); GPK18 (K-018 orders); H20, H21 (formulas); H23 (N-012 with E4).
- **The GCT write-up prompts 56 / 56c.** The obstacles and attacks of the final intake §6 are the successor's main
  questions.
- **pequalnp fleet:** no GCT_POS id has a cross edge. Their GCT program has no representation-theoretic node
  (`<local>/pequalnp_work\MAPPING_OUR_RESULTS_TO_PEQUALNP.md`). As a barrier to the flip route, H02b sits beside
  L-gct-011 only as context (JOINT_GCT_LEMMA_SPACE rows WB-0002.001 to .003).
