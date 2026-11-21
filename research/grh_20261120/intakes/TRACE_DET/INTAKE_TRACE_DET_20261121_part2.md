# Intake of TRACE_DET, part 2: the final return (what is new since checkpoint 02)

By Claude Opus 5.5 at effort high (the agent of part 1), for the main session (Claude Opus 5.5 at effort max), 21 Nov 2026,
about 03:50 UTC. The run is GPT-6 Astra (ChatGPT Pro mode); the run records its effort as "not exposed". Part 1:
`INTAKE_TRACE_DET_20261121.md`. Work file: `agent_notes\20261121_intake_GCT_NSRH_NOTES.md`.

## 0. What I read, and my scope

**Return:** `research_returns\TRACE_DET_final_20261121T0218Z_unzipped\`, the final return of 02:18 UTC. Its status is
INCOMPLETE on five rows, by the end of the session and not by choice:
- Q-STEP1, Q-STEP4 and Q-STEP7: the historical determinants of Alpöge's steps 1, 4 and 7;
- Q-DIRECT-BRIDGE: the direct transfer of the sign;
- Q-TRANSCRIPTION: the cote 1 scan images.

The final package has an 81-page paper, 79 question rows and 426 check events. Checkpoint 02's folder has been retired.

**Read:**
- the LEDGER blocks from 01:18 to 02:18 UTC, including the final-return record and its open-row table;
- the README.

**Read in full:**
- **DET-16**, the arithmetic cosine kernel and its full-multiplicity reconstruction (lines 2319–2518);
- **MAS-10**, the proof from the translations to the reciprocal-square multiplier (lines 3094–3213). Part 1 had read only
  the statement.

**Read in part:**
- DET-18: the setup and the proposition (lines 1765–1884);
- DET-15: the opening and the source hypotheses;
- DET-17: the proposition.

**At the level of the statement** (from the ledger and the README): DET-15(b–d), DET-19, MAS-11, MAS-12.

The 16 transcription rows were not re-diffed: checkpoint 02's folder has been retired, so they cannot be compared.

## 1. Verdicts on the new and changed findings

### MAS-10: an ordinary Ξ determinant on Masullo's weighted quotient (conditional on the draft). Targeted proof check, confirmed as far as I read it.

Part 1 left this proof unread. I read it as far as the reciprocal-square multiplier.

The steps I checked:
- The translation bound ‖T_v‖ ≤ e^{B₀|v|}.
- The jet-translation formula, which gives T_vV ⊂ V from the annihilator description.
- The sector estimate:
  - Re⟨(μ² − D²)h, h⟩ ≥ ‖h′‖² + δ‖h‖², with δ = μ² − B₀²;
  - |Im| ≤ 2B₀‖h′‖‖h‖ ≤ c(‖h′‖² + δ‖h‖²), with c = B₀/√δ.
- The trace-ideal lemma: T = A^{1/2}(I + iC)A^{1/2}, with ‖C‖ ≤ c. This is correct and standard.
- The Gram–Schmidt triangular basis on the jet blocks. Its totality is exactly the draft's density claim.
- The diagonal sum Σ N_ρ Re λ_ρ < ∞.
- The multiplier: R = K(I − μ²K)^{−1} has eigenvalue λ/(1 − μ²λ) = −1/z_ρ², independent of μ. So on the even part
  det(I − wR₊) = ∏(1 + w/z_ρ²) = G(w).

The final step (the exact spectrum of the compact operator, the inverse, and the even-sector determinant) I read only
through this identification.

Its scope is right. The proof is conditional only on Masullo's Theorem 10.2.2.1 (spectral-annihilator density, p. 446).
RH is not used.

### DET-16: the arithmetic cosine kernel. Targeted proof check, confirmed.

The kernel is k(t) = Σ_ρ N_ρ e^{(ρ−1/2)t}/(ρ(1 − ρ)). The proof shows:
- RH holds if and only if k is bounded, if and only if k is of positive type.
- One direction is the two-point Gram matrix. The other is boundedness, which gives G_ζ ≥ −K√X; then the Landau lemma of
  STEP6-03 at θ = 1/2, together with the functional equation, gives RH.
- The atoms and the integer multiplicities are recovered by Cesàro averages (the sinc argument with dominated convergence).
- The cyclic model is L²(μ_K). It has one dimension per distinct atom, so the multiplicities are restored separately.

This is classical in substance (the explicit formula plus Bochner). The run claims no novelty. With Alpöge's theorem cited
as a theorem, the positivity holds unconditionally.

### DET-18: a weighted-character ordinary determinant. Read in part; confirmed at that level.

- With M = 2(3o + 1), the product 𝒫_M(s) = det(I − s(1 − s)C_{𝓛,M}). Here C is diagonal, with entries 1/(ρ(1 − ρ)), and
  with 4 at the central point.
- The central multiplicity MS_{1/2}/2 is an integer, because ord_{1/2}F_χ = ord_{1/2}F_{χ^∨} and M is even. Checked.
- The GRH criterion 0 ≤ C ≤ 4I is immediate: ρ(1 − ρ) = 1/4 + γ² ≥ 1/4 if and only if ρ is on the line.
- C is zero-coded, as B is.

### Findings at the level of the statement

- **DET-15:** infinitely many orthogonal rank-one Bessel convolution projectors on one Hilbert space, from Alpöge's Lean
  (`MatrixOfBesselTwoSidedAction.lean`, lines 47–48), with source hypotheses kept. The zero weights γ_j^{−2} give B ⊕ 0.
  Not checked against the Lean.
- **DET-17:** prime weights Λ(n)n^{−s} on these projectors give Tr = −ζ′/ζ(s). The trace part is immediate. The claim that
  the determinant at s = 2 cannot be a Ξ candidate is read at the level of the statement.
- **DET-19:** the natural boost is not the arithmetic flow.
- **MAS-11 and MAS-12:** extensions of MAS-10 and MAS-09 to fixed Hecke characters, conditional on the draft.

**Withdrawn or changed against part 1.**
- Nothing I checked in part 1 is withdrawn.
- DET-14's finite-target obstruction is now restricted to that realization (ledger 01:42 UTC). Part 1 carried DET-14 only at
  the level of the statement.
- MAS-10 changes from "not read in full" to confirmed, with the caveat above.

**Counts for part 2.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 2: MAS-10 and DET-16 |
| Partial check, confirmed at its level | 1: DET-18 |
| Read at the level of the statement | 6: DET-15, DET-17, DET-19, MAS-11, MAS-12, DET-15(d) |
| Gaps or refutations | 0 |

## 2. What is new

- **The answer to the main question is stable.** Alpöge's determinants are finite algebraic determinants (Gram, Capelli,
  period). They are not compressions of B, and the sign they carry is an inertia sign (DET-10), not B ≥ 0.
- **The new positive constructions** (DET-15, DET-16, DET-18, MAS-10, MAS-11) all realize B, or its character analogues, by
  inserting the zero data or the RH-equivalent positivity.
- **The exact missing piece** is a positively normalized actual determinant equal to W_std(q₀ + q_{−log X}) for all large X
  (the final ledger). Through STEP6-03, that would transfer the sign.
- **MAS-10 and MAS-11** are the genuinely new conditional theorems: an ordinary Fredholm Ξ determinant (and L-function
  determinants) on Masullo's actual quotient, with full multiplicities and without RH.

## 3. Scope of the two proofs

- **DET-16's unconditional positivity:** Alpöge (ζ).
- **DET-18's GRH criterion:** Alpöge, for Dirichlet characters.
- **MAS-10, MAS-11, MAS-12:** Masullo's Theorem 10.2.2.1, conditional; GRH is not used.
- No over-claims found.

## 4. Integration

**Cote 1** (`ARCHIVE_1_scan078`–`082` and `110`–`113`):
- Unchanged from part 1: ARC-01 to ARC-04, and the 16 transcription rows, wait for the image check.
- New: the final README states that all 16 repairs are proved. They go to the transcription second pass as `\unsure`/`\sic`
  notes.

**SA23 intake, §4.1 (B for Ξ).** DET-16 adds the arithmetic reading: k(t) is computed from prime sums alone (G_ζ − b), and
its positive type is RH. So the "B ≥ 0" of SA23 can be stated without a zero list: as the positive type of the
explicit-formula kernel. Proposed edit to the companion note: "B ≥ 0 ⟺ the explicit-formula kernel k is of positive type
(TRACE_DET, DET-16) ⟺ RH, now a theorem (Alpöge)."

**Masullo register.** Add MAS-10 and MAS-11 as conditional consequences ("the spectral quotient carries an ordinary
Fredholm determinant equal to the completed L-function, conditional on Thm 10.2.2.1, p. 446"). Keep MAS-BOUND, and the
empty Theorem 13.3.1.2, as defects of the draft.

**The other runs.**
- GCT_NSRH F50 contains a curve H¹(C_k) inside the path count. That is the PRG-FF dictionary, and it fits.
- In HODGE_SIGN, compare the inertia sign of DET-10 with the Hodge index of the Hodge sketch (HODGE_BRIDGE 3.2). Both are
  "a definite form gives injectivity, not positivity of a basis".

**Successors.**
- **TRACE_DET successor**, with three tasks:
  - the identification row Q-DIRECT-BRIDGE, in the precise form of the final ledger;
  - the declarations of steps 1, 4 and 7 in Alpöge's Lean, with their parameters;
  - the cote 1 images, as a transcription task.
- **Prompt 35 (ZETA_TWO):** take DET-16 and DET-18 as the cote 1 forms of RH and of Dirichlet GRH, and MAS-10 and MAS-11 as
  the conditional arithmetic-quotient forms.

## 5. Hexagon readiness

| Result | Verdict |
|---|---|
| MAS-10 and MAS-11 | Fail test 2: they are conditional on Masullo's unrefereed draft. Hold. |
| DET-16 and DET-18 | Fail the novelty part of test 3: they are classical in substance (explicit formula, Bochner; zero-coded operators). |
| ARC-01 to ARC-04 | Unchanged: they belong in a cote 1 companion paper after the image check. |

Nothing passes, and nothing needs a flag.
