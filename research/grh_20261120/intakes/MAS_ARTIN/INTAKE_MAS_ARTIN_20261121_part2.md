# Intake of MAS_ARTIN (prompt 48), part 2: checkpoint 10, 21-22 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it is still going. Part 1 read checkpoint 02.

## 0. What was read, and the scope

- **Return folder:** `research_returns\MAS_ARTIN_checkpoint_10_20261121T2301Z_unzipped` (23:01 UTC). The register has
  197 questions and 1,513 check events; the paper has 421 pages.
- **Movement reviews:** reviews 01-05 (18:31-22:31 UTC) all found movement, so the stall count is 0. Review 06 was due
  at 23:31 UTC.
- **Read:**
  - LEDGER.md lines 308-440: MO014-MO023, the checkpoint 09 receipt, review 05 with its "main-question gates", and the
    checkpoint 10 preparation;
  - the QUESTIONS rows Q-MA-ALLTEST-001/002, Q-MA-CHAR-SLOW-001/002, MA-Q1-MO024-B and MO024-W;
  - **MA-FT-002 in full** (`modules/full_test_slow_band.tex`, line 305 on);
  - in `modules/characters.tex`, the data of the cubic character (lines 455-510).
- **Statement level, from the ledger:** MA-GA-001/002, MA-MO012-MO029, PI001, PR006-PR011, TN001-TN002, RB008-RB010.

## 1. What moved since checkpoint 02

1. **The main gate is now exact on the full test class: MA-FT-002, confirmed by me given MA-JP-004.**
   - For each sector (Q, a primitive Dirichlet character, or the non-induced cubic character), at fixed width α and
     weight s, the following are equivalent:
     - (i) the actual local and global trace limits agree for every compact smooth g with g(0) = 0;
     - (ii) the same, for every g ∈ C_c^∞((0,∞));
     - (iii) the upper deficiency δ⁺_ρ vanishes at every zero;
     - (iv) the full strip multiplicity r_ρ^{st} = m_ρ at every zero.
   - Requiring this for every 0 < α < 1/2 is exactly RH for the sector.
   - **The proof.** (ii) ⇒ (iii) because, for positive tests, the difference is the trace functional of the nonnegative
     integer divisor D⁺ = Σ δ⁺_ρ [λ_ρ], which vanishes on all such tests only if D⁺ = 0 (MA-JP-004). (iii) ⇒ (iv) by the
     symmetry ρ ↦ 1 − ρ̄ (the completed functional equation composed with conjugation; no self-duality needed).
     (iv) ⇒ (i) directly. The every-width statement holds because a zero off the line is exterior to a narrow enough
     strip.
   - This is the full-test form of part 1's MA-HM-003. **The gate is unchanged in substance:** the corrected identity is
     equivalent to RH in its own sector. The run states that its trace and matrix refinements (MO014-029) "do not shrink
     FT002".
2. **General number fields (MA-GA-001; statement level; the one movement witness of review 05).** The annular rates
   and the actual nuclear lift hold for every fixed number field, structural S and fixed unitary compact character, on
   the coordinate-flat additive subspace. This is infrastructure. Masullo's local annular transport is now available in
   M's full scope.
3. **Polar completion (MO016-MO021; statement level).** This is conditional on an explicit zero-free right half-plane,
   i.e. a zero-location premise:
   - the full prime-bearing matrix exists, with an exact rank-2 outgoing polar defect (MO020);
   - trace and determinant additivity hold, and the raw trace equals the omitted finite-prime sum (MO021).

   The run keeps the premise explicit throughout.
4. **S₅.** β = b + n under (R_B) is unchanged (MA-FQ-004, part 1). Without (R_B), the strongest gate is the exclusion
   of a shared real zero in the discriminant-aware interval of RB008, with normal-closure multiplicity ≥ 9k. RB009/010
   add no exclusion and find no field with positive excess.
5. **PF26:** unchanged and complete at its outside-input scope.

## 2. Against the programme of 21 Nov, items (1)-(3)

**(2) The order-3 question meets the run directly.** The run's first test case beyond A is a cubic residue character
of Q(ω):
- MA-CH-003 takes K = Q(ω), E = K(269^{1/3}), η = ψ_{269,3}, with conductor (269) (269 ≡ 2 mod 3 is inert) and
  Q_η = 3·269². Its L-function is L_K(s, η) = ζ_{Q(269^{1/3})}(s)/ζ(s).
- This is the class of Hecke L-functions over Q(ω) on which Dunn-Radziwiłł's GRH hypothesis rests, and whose
  normalized cubic Gauss sums are the Fourier coefficients of Patterson's cubic theta on Kubota's cover.
- What the run proves for this sector:
  - the actual full-test trace formula;
  - the ideal-domain endomorphism;
  - the evaluated nuclear local-source return;
  - the full common matrix, but only under a dual half-plane premise.
- **The every-width narrow identity is equivalent to RH for L_K(s, ψ_{269,3})** (FT002 in that sector; MO024-W).
- So the trace route gives no leverage on the first case beyond A. Whatever proves RH there must supply FT002's
  condition (iii): δ⁺_ρ = 0, no zero exterior to a narrow strip.

**(1) Where Alpöge's mechanism would enter.**
- The run uses no sign or positivity mechanism. MA-POS-001 found no faithful full-jet positivity in the draft, and
  GRH_NIGHT MT-M20 shows that faithful positivity is equivalent to GRH with simple zeros.
- The structural match is MA-HM-003. Its proof is the number-field form of the power-sum lemma: an eigenvector of U_1
  with eigenvalue e^{ρ−a}, on a space where ‖U_n‖ ≤ C e^{vn}(1+n²)^{s/4}, forces Re(ρ − a) ≤ v.
  - In the function-field proof, the bound on the "power sums" comes from the trace identity R = QN − M^k with one
    global sign (−1)^{D−1}, which makes R an honest trace on V^{⊗k} + K.
  - In MAS_ARTIN the bound (MA-HM.28) is only the weight's, not an arithmetic bound on the Euler-twisted operator. That
    is exactly why FT002 stays open.
- **The attack.** Make the power-sum input arithmetic in the cubic sector: an identity in which the remainder for the
  averaged cubic family (χ ↦ χ(disc) twisted by normalized cubic Gauss sums of order #μ₆, i.e. through Patterson's
  theta on the 6-fold, or cubic, Kubota cover) is c_k·ζ₃^n times an honest trace, with |c_k ζ₃^n| = 1.
  - The power-sum lemma then holds verbatim with that unit-modulus factor in place of the sign (the programme's
    item (1)), and it bounds each eigenvalue.
  - In MAS_ARTIN's language, this would prove δ⁺_ρ = 0 for the cubic sectors, i.e. FT002(iii), hence RH for
    L_{Q(ω)}(s, ψ) for the cubic Kummer characters.

**What a proof in the cubic sector would settle on our record.**
- **PF26's residual list at d = 3:** MA-PF-005 gives 𝓑(p,m,3) = {3}. The residual RH is then exactly that of
  L_{Q(ω)}(s, ψ_{p,3}) = ζ_{Q(p^{1/3})}/ζ, through GRH_NIGHT CX-ALG-024 (P − 1 = Ind ψ on AGL₁(F₃) ≅ S₃). So
  deterministic polynomial factoring of cubics would follow under PF26 + A.
- **Koiran's counterexample field:** CX_GRH CX-K04 uses x³ − 2. Its solution field Q(2^{1/3}) has
  ζ_{Q(2^{1/3})} = ζ · L_{Q(ω)}(s, ψ_{2,3}). So Koiran's analytic input for pure cubic solution fields is this same
  family.
- **Dunn-Radziwiłł's** Patterson bias becomes unconditional, since their stated hypothesis is GRH for Hecke L-functions
  over Q(ω).

**(3) Items of ALPOGE_BRIDGES and our runs that bear.**
- **AQ-CM-HEX** (ALPOGE_BRIDGES; my part-1 intake).
  - Alpöge's hexagonal CM curve C/Z[ω]: its trace-zero primes are the primes inert in Q(√−3), equidistributed under A
    through χ₋₃.
  - The run recorded that A "does not directly cover the nonzero-infinity-type CM Hecke L-function". For a CM curve
    y² = x³ + D, that is the Grössencharacter of Q(ω) built from the sextic residue symbol, i.e. the μ₆ = μ₂ × μ₃ phase
    of item (1).
- **CC-F03** (ALPOGE_BRIDGES; confirmed): the cubic class character of Q(√−23) from x³ − x − 1 is a cubic Hecke
  character of an imaginary quadratic field beyond A. Its group is S₃, as for the Kummer cubics, so it is the same type
  of case.
- **Dirichlet-side cases.** The Erdős-Straus separating characters (quartic mod 5, cubic mod 7) and
  Δ = χ₁₂ ∘ u with χ₁₂ = χ₋₄χ₋₃ are Dirichlet characters: their L-functions are in A. Their Kummer and cubic-residue
  counterparts over Q(ω) are the first family beyond A, the sector of (2).
- None of MAS_ARTIN's statements treats Kubota's cover, Patterson's theta or Gauss sums. The only metaplectic reference
  is a citation (Takeda 2015) in the Booker-Rankin module.

## 3. Verdicts

| id | verdict |
|---|---|
| MA-FT-002 | **confirmed** (targeted check), given MA-JP-004, which is statement level |
| MA-GA-001, GA-002 | statement level |
| MA-MO014-MO029, PI001 | statement level; conditional on an explicit zero-free half-plane where stated |
| MA-PR006-PR011, TN001-TN002 | statement level; equivalent criteria, not smaller gates |
| MA-RB008-RB010 | statement level |
| part-1 findings (MA-HM-003, MA-FQ-003/004, MA-POS-004) | unchanged; no corrections in the ledger |

**Counts.** Confirmed: 1. Statement level: about 25 ids. Gaps: 0. Refuted: 0.

## 4. Prompt updates and the defect table

- **Defect table** (`cores\MASULLO_DEFECTS_20261121.md`): no row changes. The §12.3-§12.4 row stands as updated in
  part 1. FT002 is its full-test form, and GA-001 extends the local transport to general fields.
- **A successor** should stop extending the trace route and take the cubic sector:
  - an order-3 (μ₆) phase version of Alpöge's power-sum identity for cubic residue characters of Q(ω), through
    Patterson's cubic theta;
  - its target stated as FT002(iii) for ψ_{p,3};
  - its consequences named: PF26 at d = 3, pure cubic Koiran fields, and Dunn-Radziwiłł.
