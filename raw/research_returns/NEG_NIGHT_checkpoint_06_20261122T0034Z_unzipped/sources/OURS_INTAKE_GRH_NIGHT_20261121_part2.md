# Intake of GRH_NIGHT (prompt 42), part 2: checkpoint 04, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it writes "effort not exposed". It is still going. Part 1
(`INTAKE_GRH_NIGHT_20261121.md`) read checkpoint 02.

## 0. What was read, and the scope

- **Return folder:** `research_returns\GRH_NIGHT_checkpoint_04_20261121T0402Z_unzipped` (checkpoint 04, 04:02 UTC). It
  was the newest present.
  - Size: 273 catalogue rows (from 199), 162 questions (from 106), 683 check events (from 378); the paper has 14,991
    lines (from 6,960).
  - Scheduled movement review 1 (04:02 UTC): movement yes. The next review was due at 05:02.
- **Read:**
  - LEDGER.md, every dated entry from 02:30 UTC to the end of review 1;
  - the states of the changed and new key question rows (Q-MAS-*, CX-Q22 to CX-Q39, AG-Q11, AG-Q27, AG-Q28);
  - in GRH_NIGHT.tex, **CX-ALG-027 (in full)**, the statement and the first part of the proof of CX-ALG-028, **MT-M20
    (in full)** and **MT-M23 (in full)**;
  - the PF26 entries in BIBLIOGRAPHY.tsv.
- **Statement level:**
  - MT-M10 to MT-M19, MT-M21, MT-M22, MT-M24 to MT-M26;
  - NT-L15 to NT-L17, NT-Z17, NT-Z19, NT-E01 to NT-E05;
  - AG-C149-NORMAL, AG-C149-FULLLIFT, AG-C149-CUSP; AG-THETA-*, AG-CM-INTEGRAL-MODEL;
  - CX-GEO-010 to CX-GEO-013;
  - MT-ART09, MT-ART10.
- **Changes to part-1 findings:** none withdrawn or corrected. The rows for MT-M01, M02, M05, CX-ALG-016 to 018,
  CX-ALG-023 to 026, AG-C34-* and MT-ART01 keep their states.
  - **One change of weight to report, from part 1 §1.1:** the open gate there, Q-MAS-INFINITE-BASIS, has largely been
    closed by the run itself (§1.2 below). My part-1 sentence "M carries a substantive gap at §9.3.2 (infinite-divisor
    basis)" must now read: "§9.3.2 contains false general lemmas (MT-M01, M02, M05); the infrastructure they were meant
    to supply is proved unconditionally by other means (MT-M18, M19, M24, M26), except prescribed individual jet
    coordinates (MT-M16)".

## 1. Verdicts on the new findings

### 1.1 Factoring: a polynomial-time transfer through an outside preprint

| id | statement | uses | verdict |
|---|---|---|---|
| **CX-ALG-027** | assume PF26 (OpenAI, *Deterministic Polynomial Factorization over Prime Fields*, 4 Oct 2026, Thm 1.2 and Prop 10.1). Then under M, factoring of degree d over a supplied F_{p^m} is deterministic in time poly(d, m log p). The analytic input is RH for ζ_Q and for E_{p,r} = Q(ζ_{12r}, p^{1/r}), r ≤ d prime, with an explicit auxiliary prime ℓ ≤ [16r² log(12r²) + 16r(r−1) log p + 10r² + 5]² | PF26 + M | **confirmed as a transfer, with PF26 as a cited outside input that I did not open.** I checked: the discriminant bounds; Bach-Sorenson for the class of a nontrivial element of Gal(E/K); the meaning of the Frobenius conditions (ℓ ≡ 1 (12r), p^{(ℓ−1)/r} ≠ 1); the exclusion of 2, 3, p, r by ramification; the small-characteristic branch p ≤ B^{200000} (Berlekamp plus enumeration of scalars); and the passage to F_{p^m} through the Berlekamp subalgebra C₀ ≅ F_p^t, the minimal polynomial of b, and gcds. |
| CX-ALG-028 | the same with A_D plus PF26's primary-table assertion, and RH only for ζ_{Q(p^{1/r})} at primes r ≤ d with r ∤ (p−1)m and higher valuation (through CX-ALG-024); PF26 alone if every r divides m or has valuation one | PF26 + A_D + the pure fields (M) | statement level, and the first part of the proof (the primary table: quadratic entry, R = r, r \| p−1, r \| m) read with no fault found. |

**Weight.** If PF26 holds, deterministic factoring is polynomial under GRH, not quasipolynomial. Its analytic input
localizes to A_D plus RH for the pure prime-degree fields Q(p^{1/r}) at the "bad" primes r. That supersedes, in degree
dependence, the quasipolynomial route CX_GRH CX-N15 → GRH_NIGHT CX-ALG-025. PF26 is an outside, unrefereed preprint. The
run's root read its norm-solver proof and prerequisites "without a gap found", and keeps it as an explicit extra input.

### 1.2 Masullo's §9 infrastructure: repaired, and one exact positivity obstruction

| id | statement | verdict |
|---|---|---|
| MT-M18, MT-M19 | unconditionally, the canonical arithmetic quotient has closed-ideal synthesis, an adapted absolute block basis and nuclear convolution; trace positivity of C_{h∗h♯} is equivalent to GRH | statement level. Proofs not read; the run records author, root and NT readings. |
| MT-M24, MT-M26 | the specified Masullo smooth quotient (the draft's literal test topology and map) is Meyer's zeta-summation quotient; the fixed-character strip Hilbert quotient is trace class with the exact kernel | statement level. |
| MT-M16 | prescribed individual jet coordinates need one leading-coefficient / weighted-cluster-product condition | statement level. |
| **MT-M20** | for a fixed L(s, η): GRH with all nontrivial zeros simple ⇔ there is a faithful positive-definite continuous inner product on the full jet quotient with bounded convolutions and every C_{h∗h♯} ≥ 0 | **confirmed, given MT-M18/M19** (the realization of the local jet algebras inside Q, and the involution formula M19.6). (1)⇒(2): diagonal trace class from the zero count; under GRH h♯ has conjugate entries. (2)⇒(1): an off-line pair of idempotents gives h∗h♯ = −(e + e†), negative; a multiple zero gives a nilpotent N with iN self-adjoint, from h_u = e + iun at u = ±1, hence N = 0. Both steps are right. |
| **MT-M23** | for every nonabelian Galois L/K, ζ_L has infinitely many multiple zeros (Hu-Kaneko-Martin-Schildkraut, Thm 1.1), so its full-jet quotient has **no** faithful positive Hilbert completion; also limsup I_L(X)/(log X)³ > 0 for the Möbius mean square | **confirmed, given HKMS and NT-L16.** The multiplicity is in fact immediate from ζ_L = ∏ L(ρ)^{dim ρ} with some dim ρ ≥ 2. The positivity conclusion follows from MT-M20. |

**Weight for Masullo and for cote 1.**
- MT-M20/M23 do not refute Masullo. The run does not claim that the draft uses faithful full-jet positivity, and scalar
  trace positivity (MT-M19) survives.
- They do make one thing precise. Any argument, Masullo's or a "Hilbert-Pólya" reading of Grothendieck's cote 1
  (det(1 − wB) with B ≥ 0; ALPOGE_BRIDGES BR-TR-01), that uses a *faithful positive operator* on the full zero-jet space
  of ζ_L must fail for nonabelian L. Scalar trace positivity is the most such a route can give.
- This is a finite-monodromy (Artin-motive) obstruction: higher-dimensional irreducible ρ forces nilpotent blocks.

### 1.3 Other new rows (statement level)

| id | statement | note |
|---|---|---|
| AG-C149-NORMAL, FULLLIFT, CUSP | cote 149: for the torsion-line-bundle family the cusp-inertia normalizer comparison is proved; AG-Q28 refuted by a type (0,4) family over E: y² = x³ − x (a global order-2 class, nonzero and rationally zero; every Galois section lifts through the full profinite cusp normalizer) | statement level. This bears on the normal-bundle Kummer route of cote 149, not on A1, which AN_GRH A05 proves. |
| CX-GEO-010 to 013 | orbit-closure intersection for reductive actions: a polynomial HN reduction, hence AM under M for closed target orbits; CX-GEO-013 refutes a width claim by F_s = (X, XY^{2^s}) | statement level. GCT-relevant; bears on CX_GRH CX-U05 (equation access). |
| NT-L15-L17, NT-Z17, NT-Z19 | a weak-Mertens mean-square hypothesis implies GRH, simple zeros and the normalized-point basis; Kummer fields obstruct universal weak Mertens; CCM-type zero bounds for all unitary infinity types | statement level. |
| AG-THETA-*, AG-CM-INTEGRAL-MODEL | Alpöge step 2 (formal height): integrality closed for two elliptic-function families and a class-number-one Hecke-value sector; good unramified CM models exist for imaginary quadratic fields with finitely many prescribed inert primes | statement level. This feeds prompt 34 (DP_MULT). |
| MT-ART09, MT-ART10 | solvable Artin holomorphy: a relative-zero gate with Wong's thresholds; the Fröhlich root-number bridge | statement level. |

**Counts for part 2.**
- Confirmed with every step checked: 3 (CX-ALG-027 as a transfer, MT-M20, MT-M23).
- Partly read, no fault: 1 (CX-ALG-028).
- Statement level, no fault found: about 30 ids.
- Gaps: 0. Refuted: 0. Changes to part 1: none withdrawn; one weight changed (Q-MAS-INFINITE-BASIS).

## 2. What is new

- **Factoring is polynomial-time under GRH if PF26 holds.** Its GRH localizes to A_D plus pure prime-degree fields.
  This changes the factoring Hexagon candidate (§6).
- **Masullo:** the §9 functional-analytic infrastructure is repaired unconditionally by the run. The located gaps that
  remain are ALPOGE_BRIDGES's §12.3-§12.4 intertwiner and the blank 13.3.1.2. MT-M20/M23 add an exact limit:
  faithful positivity on full jets is equivalent to GRH plus simple zeros, and fails for every nonabelian top field.
- **Against my other intakes:** CX-GEO-010/011 move CX_GRH CX-U05 (orbit closure with no equation access) to "AM under M
  for closed target orbits". AG-C149-* bear on the cote 149 Kummer route, not on A05.

## 3. The scope of the two proofs

- **New outside input:** PF26 (OpenAI, 4 Oct 2026), unrefereed, for CX-ALG-027/028. Tag it separately from A_D and M.
- MT-M18, M19, M20, M23 and M24 are unconditional. M enters only through "M ⇒ trace positivity" (MT-M19).
- No statement claims more than its inputs give.

## 4. Integration, with the attack each opens

1. **CX_GRH intake, CX-U02/U03.** U03 ("a general polynomial degree bound for deterministic factoring") is met under
   PF26 + M, or PF26 + A_D + pure fields. Edit U03's gate to: "PF26 (outside preprint) verified".
   - The attack on the analytic input is unchanged from part 1: RH for ζ_{Q(p^{1/r})}, which is one order-r Kummer Hecke
     character over Q(ζ_r) (part 1 §4.2), via Alpöge's method over CM fields.
2. **Cote 1 / SA23 (geo-H-lidskii) and ALPOGE_BRIDGES BR-TR-01.** Add: "a faithful positive operator realization on the
   full jet space exists iff GRH + simple zeros (MT-M20); it fails for ζ_L, L nonabelian (MT-M23). The cote 1 trace route
   gives scalar trace positivity, not a faithful positive B, beyond the abelian case."
   - The attack: Grothendieck's det(1 − wB) for ζ_L must use the semisimplified (Artin-isotypic) model. Ask whether
     each L(ρ) separately admits a faithful positive B_ρ; that requires simplicity of the zeros of each L(ρ), which is an
     open conjecture, not RH.
3. **The shared Masullo defect list** (part 1 §4.3): mark §9.3.2 as "false as stated; replaced by MT-M18-M26"; the gaps
   still open are §12.3-§12.4 and 13.3.1.2.

## 5. Prompt updates

- Attach PF26, and ask for its own analytic hypothesis by exact locator, and for an independent check of its Thm 1.2.
- For Masullo: the main question should now be the §12.3-§12.4 intertwiner (ALPOGE_BRIDGES R-MAS-KERNEL), and whether
  the draft anywhere uses faithful full-jet positivity (MT-M20). §9 is settled.

## 6. Hexagon candidates

- **The factoring reduction:** changed by PF26. In degree dependence, PF26's polynomial algorithm supersedes the
  quasipolynomial composition (CX_GRH CX-N15 → CX-ALG-025). A post on "what GRH deterministic factoring needs" should be
  built on CX-ALG-028:
  - its content would be that PF26's analytic input reduces to A_D plus RH for ζ_{Q(p^{1/r})} at bad primes, and to A_D
    alone when there are none;
  - test 3 (literature) must check whether PF26 already states its GRH that narrowly;
  - test 2 (self-contained) needs PF26 itself to be checked, since it is an outside preprint.

  **Gates left:** a check of PF26 (Thm 1.2, Prop 10.1, the primary table), the literature on PF26's own hypothesis, an
  independent re-proof of CX-ALG-028, and the run's final.
- **H07 = A05:** not touched by GRH_NIGHT checkpoint 04; AG-C149-* concern a different route. Gates unchanged: a
  literature search and an independent re-proof of A05's Steps 1-2.
- **The cote 123 letter with CC-APG04:** not in this run; unchanged.
- **New possible candidate, MT-M20/M23** ("no faithful positive Hilbert-Pólya realization of the full zero-jet space of
  ζ_L for nonabelian L"). It is complete given HKMS and MT-M18/M19, and of interest now, since Masullo and Hilbert-Pólya
  are topical.
  - Not stable: it depends on MT-M18/M19, which no intake has checked.
  - Not literature-searched: a similar remark may be folklore, given HKMS.
  - **Gates:** an intake check of MT-M18/M19, and a literature search.
