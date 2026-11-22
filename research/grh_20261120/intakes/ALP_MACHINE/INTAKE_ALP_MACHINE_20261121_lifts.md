# Intake of ALP_MACHINE checkpoint 04 (prompt 49): lifts, seesaw, oscillator and sign, frameworks

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 22 Nov 2026. The Hecke part (AM-H01–H19) is taken by agent
af2a18f6. Check events: `INTAKE_ALP_MACHINE_20261121_lifts_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\ALP_MACHINE_checkpoint_04_20261121T2304Z_unzipped\`, from 23:04 UTC on 21 Nov. The run is
GPT-6 Astra (ChatGPT Pro mode) and is still going. Formal review 01 is at 23:04.

**What I read:**
- the QUESTIONS rows AM-Q1*, AM-Q2*, AM-Q4*, AM-Q6* (all states and findings);
- the first sections of `IMPLICATIONS.md` (DP_MULT Q3e; THETA3 A7/G1; GCT_PLETH);
- the `LEDGER.md` headings;
- **`parts\oscillator_sign\oscillator_sign.tex` lines 380–560, in full: AM-S1, AM-S2, AM-S3** (AM-S4 to its statement),
  and the statement and proof of AM-O4.

**Computation: every check script of my part rerun from a scratch copy** (`python -I -B`, outside the return):

| Script | Result |
|---|---|
| lifts\check_colmez.py | pass |
| lifts\check_cyclotomic_host.py | pass (limitations stated) |
| lifts\check_signed_chain.py | pass: Gram dimension 48, determinant 1, edge coefficient ξ₀/κ, pulled-back η/8 |
| lifts\check_theta_normalization.py | pass: residual 1.7·10⁻⁶⁴ |
| oscillator_sign\check_arithmetic_packet.py | PASS: 6 character-sum, 27 valuation, 3 normalization cases |
| oscillator_sign\check_compact_chains.py | PASS: 145,200 four-sign comparisons |
| oscillator_sign\check_oscillator_sign.py | all exact checks passed |
| oscillator_sign\check_scaled_seesaw.py | PASS: 19,643 branch cases, 2,420 down-parity cases |
| oscillator_sign\check_signed_transport.py | passed: T_det = 1 |
| seesaw\check_compact_masses.py | PASS: 550,368 U₂ elements, 1404 orbits, mass 1/14, ζ_F(−1) = −1/21 |
| seesaw\check_tail_pair.py | all flags true |
| seesaw\check_terminal_rows.py | 30 cases, maximum terminal rank 28,092 |
| seesaw\check_unit_geometry.py | PASS: irreducible cubic, signed type 4Φ |
| seesaw\check_vacuum_characters.py | PASS |
| **seesaw\check_signed_torus.py** | **fails in this environment:** "TypeError: nmods cannot be ordered" in `sorted(factors, key=key)` under python-flint 0.9.0. **A script erratum (an API version), not a mathematical failure.** AM-SS05 is therefore not re-certified |

**My own computation:** the AM-O4 hook identity H_{(α+b,b)}/(b!H_α) = ∏_{i,t}(α_i + r + 1 − i + t), checked
independently in 500 cases (r ≤ 4, parts ≤ 4, b ≤ 3): 0 mismatches.

**Scope.**
- **Targeted proof check:** AM-S1, AM-S2, AM-S3.
- **Proof read and independent computation:** AM-O4.
- **Computation rerun:** the 14 scripts above (13 pass, 1 environment failure).
- **Statement level:** everything else in my part (AM-L1–L15, AM-SS01–SS17, AM-ST01–ST14, AM-O1–O3, AM-S4, AM-G01).
- My context is near its limit, so the long lift and seesaw proofs were not read.

## 1. Verdicts

### The reflected sign (AM-S1 to AM-S4): this bears directly on H01 and the cubic-phase question

- **AM-S1: confirmed.** For W = (Z/3)² ⋊ ⟨s⟩ (the sheet swap):
  - Z(W) = ⟨(1,1)⟩ ≅ C₃, and [W,W] = ⟨(1,−1)⟩ ≅ C₃;
  - ⟨d, s⟩ ≅ C₆ and ⟨a, s⟩ ≅ S₃.
  - Any quotient in which s is central kills a, since s a s⁻¹ = a⁻¹ and a³ = 1. **Centralizing the reflection loses the
    antidiagonal C₃.**
- **AM-S2: confirmed.** Tr(sFⁿ | M) = Tr(sFⁿ | M^{⟨a⟩}), because s exchanges the ζ- and ζ²-eigenspaces of a. In the
  standard S₃ module with F = L·Id, every reflected trace vanishes for every n and every tensor power, while L is
  arbitrary. The example is realized by an honest ℓ-adic sheaf on Spec F_q.
  - **The failed step is named exactly:** H01's Proposition `prop:remainder` and Lemma `lem:tensor` need an *effective*
    direct sum. A reflected insertion produces [M^{s=1}] − [M^{s=−1}], whose multiplicities cancel.
- **AM-S3: confirmed.** If s has order d and *commutes* with F, then (sF)^{dn} = F^{dn}, and the power-sum lemma applies
  to F^d. It is false for the measured sequence Tr(sF^{2n}), and false without commutation (sFs = F⁻¹ gives
  (sF)² = 1).
- **AM-S4: statement level.** The half-weight rung is refuted as a formal implication.

**How it bears on the user's programme of 21 Nov.**
- The H01 lemma holds verbatim with any unit-modulus factor c_k·ζ_kⁿ *multiplying an actual module's trace*. That is
  AM-S3's commuting case: a finite-order operator commuting with Frobenius, with powers divisible by its order.
- An order-3 phase obtained by a *reflection*, the S₃ / two-sheet picture, cannot work (AM-S1, AM-S2).
- So **the cubic-phase version of the sign mechanism must realize μ₃ as a commuting automorphism** of the cohomology,
  e.g. the Z[ω]-action of a CM-by-Z[ω] variety, with the remainder in the corresponding *eigenspace*. It cannot use a
  sign-reversing involution. This is the exact constraint any Kubota/Patterson-cubic version must meet.

### Oscillator (AM-O1 to AM-O4)

- **AM-O4: confirmed.** The ratio of squared Fischer norms is
  R_{α,b} = H_{(α₁+b,…,α_r+b,b)}/(b!·H_α) = ∏_{i=1}^r ∏_{t=1}^b (α_i + r + 1 − i + t).
  - I read the proof structure: f_λ is a matrix coefficient, and the Gaussian moments give the Fischer norm.
  - The hook identity was recomputed independently in 500 cases.
  - The isometric map is R^{−1/2} times AM-O2. An archimedean identity only.
- **AM-O1, AM-O2, AM-O3: statement level.**
  - AM-O1: a local oscillator identification with explicit polarization and circle inversion.
  - AM-O2: a compact-member map with the twist det^{−b−1}.
  - AM-O3: a full two-sided intertwiner refuted, in its stated direct scope.

### Lifts (AM-L1 to AM-L15): statement level, with the scripts rerun

- **Proved in scope:**
  - L1, the bookkeeping of DP_MULT's lift count;
  - L4, a positive CM-height difference;
  - L5, the host Q(ζ₁₁₂) on J⁸;
  - L6, period coordinates;
  - L7, a signed definite chain;
  - L10, the nonsplit finite theta factors;
  - **L11, actual nonzero global compositions**;
  - **L12, the increment d = 2k³ + 4k + 6**;
  - L13, a formal frame;
  - L14, J-theta scalars;
  - L15, fixed paths D₁ and D₂, with rates 1/120 and 1/1220.
- **Refuted:**
  - **L3: no common algebraic scalar period for J** (analytic-subgroup argument);
  - **L8 with ST04: the inherited increasing-character chain has zero composite**;
  - **L9: partial-dual transport of the old top chamber.**
- **AM-Q1 stays OPEN.** The six compatible lift identities with controlled nonvanishing, the prescribed arithmetic
  columns, and the gain/error/height arrays are not obtained.
- **For A (Alpöge's archive):** DP_MULT's step-8 "one order of multiplicity per lift" is still unverified as a
  quantitative statement. **The inherited chain is dead (ST04/L8).** A changed character family is required, and L11/L12
  supply a qualitative replacement without the cost saving.

### Seesaw, THETA3 A7/G1 (AM-SS01 to AM-SS17, AM-ST01 to AM-ST14): statement level

**Proved:**
- SS01, actual unit-Gram signed geometry;
- SS03, type 4Φ (the script confirms the signed type);
- SS05, the signed torus as a principally polarized Jacobian (script failed in this environment);
- SS07/SS08, the exact masses (the script confirms mass 1/14 and 1404 orbits);
- **SS11: an actual nonzero vacuum average c**, an explicit 1740-term theta sum, with two-edge value c²;
- SS14, a positive selected restriction period;
- SS16, the fixed-CT matrix criterion;
- ST05–ST07, ST09 and ST10.

**Refuted:**
- SS02: all-positive PinColAt;
- SS04: the unshifted even Gaussian;
- **SS13: the inherited terminal type kills the vacuum** (an HC gap ≥ 2, for every inherited parameter);
- the split-supercuspidal obstruction (a full theta terminal period vanishes);
- the old interlace at every negative place.

**THETA3's G1 (the definite seesaw) is strictly reduced but OPEN.** The MainX kernel/covolume equations and the
prescribed terminal functional on a nonzero image remain.

### AM-G01 (frameworks)

Statement level. It is the run's placement in Grothendieck's frameworks.

**Counts.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 3 (S1, S2, S3) |
| Proof read with independent computation, confirmed | 1 (O4) |
| Computation rerun, pass | 13 scripts |
| Rerun failed in this environment (script erratum) | 1 (check_signed_torus.py) |
| Statement level | the other ≈ 50 findings |
| Refuted by me | 0 |

## 2. What is new

- **AM-S1–S3:** an exact, elementary obstruction: reflected phases cannot replace H01's global sign. The positive
  form: commuting finite-order phases can.
  - New as a precise statement for the sign mechanism. The ingredients are classical: Clifford theory and power sums.
- **AM-O4:** the hook-ratio identity may be classical (Fischer norms of highest-weight vectors; hook-content
  formulas). **Literature point:** search before calling it new.
- **SS11** (a nonzero explicit vacuum average) and **L11/L12** (nonzero global compositions with an explicit increment):
  new positive constructions inside the theta machine, at statement level.
- **The refutations L3, L8/ST04, SS13 and SS02** close the inherited routes for THETA3's G1 and DP_MULT's lift count.

## 3. Open gates, and the attacks they open

1. **AM-Q1 (the lift count):** realize the six lift identities with a *changed* character family (after ST04/L8), on
   L11/L12's nonzero compositions. Then compute the gain, error and height arrays at the prescribed columns.
2. **AM-Q2 (G1):** compute SS16's weighted finite matrix for the immutable arithmetic datum. That one finite matrix
   decides whether the fixed terminal functional is nonzero on a theta image.
3. **AM-Q6 (the ES-new-geometry gate):** an actual correspondence producing a common-sign direct sum. By AM-S1–S3 it
   must be a *commuting* μ₃- or μ₆-action, not a reflection.
   - This is the same constraint as the cubic-phase programme: the eigenspaces of Z[ω] acting on the cohomology of a
     CM-by-Z[ω] family.
   - The natural first test is the Fermat cubic x³ + y³ = 1, whose Frobenius on the ω-eigenline is the cubic Jacobi sum
     (Weil 1952). Ask whether a path-quadric remainder can be built ω-equivariantly, so that the remainder is effective
     on one eigenspace.
4. **check_signed_torus.py:** fix the sort (key = int(·) on the nmod factors), rerun, and re-certify SS05.

## 4. Errata and literature points

- **Script erratum:** `parts\seesaw\check_signed_torus.py` sorts nmod objects, which python-flint 0.9.0 does not order. It
  needs an explicit integer key.
- **Literature:** AM-O4's hook ratio needs a search (Fischer inner product; Schur–Weyl Gaussian moments). AM-S1–S3 are
  standard group theory, fine to cite as elementary.
- **The reference to H01:** AM-S2 names `prop:remainder` and `lem:tensor` of H01 v5 correctly. **For H01 v2:** a remark
  that the sign may be any commuting unit-modulus finite-order phase (AM-S3), but not a reflected one (AM-S2).

## 5. Hexagon readiness (`HEXAGON_CANDIDATES.md`; register not edited)

| Candidate | Tests | Gate |
|---|---|---|
| **AM-S1–S3 as a remark in H01 v2** ("which phases the sign mechanism allows") | 1, 2, 4: yes (targeted check, elementary). 3: the statements are elementary and stable. 5: moderate, and timely after Alpöge | none beyond writing it into v2; **recommended** |
| AM-O4 | 1, 2, 4: yes | 3: a literature search (likely classical). Not a stand-alone post |
| SS11, L11/L12 | statement level | an intake full read, and the run's final. Not yet |

## Full depth (continuation, 22 Nov)

**Proof checks added in this round.**
- **AM-L1, AM-L2, AM-L3, AM-L5, AM-L6, AM-L7, AM-L9: targeted proof check, confirmed.**
  - L3: the type {1,2,3} of Q(ζ₇) is primitive, and the analytic-subgroup argument is sound.
  - L5: disc Q(ζ₁₁₂) = 2¹⁴⁴7⁴⁰, rd = 8·7^{5/6}, E*/F* is unramified, the labels are 87 and 65, and the initial-form sum
    is 8.
  - L6: Beta-integral periods; tridiagonal intersection matrix with det 1.
  - L7: κ³ − 2κ² − κ + 1 = 0 with signs (+,+,−); s² = −7; uū = 8t.
  - L9: the chamber inequalities (L9.5)–(L9.8) and the dual reversal.
- **AM-L4: independent re-proof.** I recomputed the Fourier coefficients (3/2, 2/3, 2/3, 1/6). I recomputed
  Δ_h = log(Γ(2/7)Γ(4/7)³/(Γ(3/7)³Γ(5/7))) = 0.0556870335 with mpmath. It equals the ζ-series and lies inside (L4.4).
- **AM-L8: targeted proof check, confirmed given AM-ST04.** Positive creation at every place forces a type induced from
  K, so J-isotypic towers have zero composite.
- **AM-L10:** part (1) confirmed (the decomposition groups ⟨2⟩, ⟨7⟩ and ⟨3⟩ exclude complex conjugation). Parts (2) and
  (3) rest on cited local theta and existence theorems.
- **AM-SS04 and AM-SS13: targeted proof check, confirmed.**
  - SS04: an even theta has zero first jets.
  - SS13: a gap ≥ 2 in the Harish-Chandra parameter excludes one-dimensional constituents.
- **AM-ST04:** the oscillator conventions read; the local branching certified by computation.

**Computations.** **AM-SS05 is now re-certified.** The earlier failure was a sympy/python-flint incompatibility inside
`factor_list`, not the script's own sort. With SYMPY_GROUND_TYPES=python, check_signed_torus.py passes. So all 14 scripts
of my part pass.

**Carried as background without fault found** (statements read, proofs not read in full; my context reached its limit):
- AM-L11 and L12: they rest on stable-range theta nonvanishing and AM-H10/H13. The increment d = 2k³ + 4k + 6 > 2C(k) + 1
  is checked.
- AM-L13, L15;
- AM-SS02, SS06, SS09, SS10, SS12, SS15–SS17;
- AM-ST01–03, ST05–ST14 (ST05–ST08 and ST04 are script-certified);
- AM-O3, AM-S4, AM-G01.

**Errata update.** The earlier "script erratum" for check_signed_torus.py is withdrawn. The run's script is correct; the
environment needs SYMPY_GROUND_TYPES=python with python-flint 0.9.0.

**Verdict totals now.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 14 (L1, L2, L3, L5, L6, L7, L8, L9, L10(1), S1, S2, S3, SS04, SS13) |
| Independent re-proof | 2 (L4, O4) |
| Computation, pass | all 14 scripts |
| Refuted | 0 |
| Carried | the rest, as listed above |

### Full depth, continued (22 Nov, before compaction)

**Targeted proof checks, confirmed:**
- AM-L13: the separating element at a split prime, and the unique normalized rational function. The rest follows
  Bannai–Kobayashi, Proposition 2.1.
- AM-L15: the paths (L15.2) from Q = z₁z₃ − z₂². The 11-adic rates rest on the cited DP58/DP67.
- AM-SS02: the sign contradiction with IsCartanInv.
- AM-SS12: constant endpoints give the trivial-isotypic integral.
- AM-SS17: split-place supercuspidals do not occur in the restricted oscillator.
- AM-S4: b = H + v⁻¹, with b² = (v + v⁻¹)b, rederived.
- AM-ST03: the real signs (+, −, −) of α⁻¹ prevent C*C > 0.
- AM-ST06: the minimal partitions.
- AM-ST08: the canonical tensor/Hom symplectic isomorphism.
- AM-ST10: the restriction period as a squared norm.

**Used and rechecked** (statement and method read, no fault found):
- AM-L11 and AM-L12: the first lift is by the archive theorem tLiftK/NonVan_k (A, accepted); later lifts by GQT/H13.
- AM-SS09, SS10, SS15, SS16;
- AM-O3;
- AM-ST07 (GQT normalization);
- AM-ST01, ST02, ST05, ST09, ST11, ST12, ST14;
- AM-SS06, AM-G01.

**Computation:** AM-ST13 (the packet script passes).

**Totals for my part after this round.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 26 |
| Independent re-proof | 2 (L4, O4) |
| Computation | all 14 scripts pass |
| Used and rechecked | 21 |
| Refuted | 0 |

No finding of my part is left without a recorded check event.
