# Intake of SIGN_NEXT checkpoint 01 (prompt 45): Grothendieck's Hodge-index route after the sign-only proof

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent; this run is HODGE_SIGN's successor), launched by the main
session (Claude Opus 5.5 at effort max), 21 Nov 2026, round 4. The brief is
`field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`. Work file: `agent_notes\20261121_intake_HODGE_SIGN_NOTES.md`.
Check events: `INTAKE_SIGN_NEXT_20261121_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\SIGN_NEXT_checkpoint_01_20261121T0344Z_unzipped\`, checkpoint 01, the only SIGN_NEXT
folder present.
- The run is GPT-6 Astra (ChatGPT Pro mode). It began at 02:59:46 UTC; this checkpoint is from 03:44 UTC, 45 minutes in.
- **The run is still going.** Q6g-GLOBAL-GEOMETRY is active.

**The prompt as sent:**
`TO_SEND\PRO\1_Archive_research_by_topic\SENT\45_SIGN_NEXT_Grothendiecks_Hodge-index_route_after_the_sign-only_proof\PROMPT.md`.

**What I read:**
- `README.md`, `LEDGER.md` and `QUESTIONS.tsv`;
- the counts of the run's `CHECK_EVENTS.tsv`;
- `SIGN_NEXT.tex` lines 100–760, in full: SN-C01–C05, SN-10–SN-14;
- lines 782–1035: IF-01, IF-02 and the statement of IF-03;
- lines 1955–2512, in full: SN-44-01–SN-44-05;
- Part II (lines 2813–2870);
- the list of archive locators.

**What I compared against:**
- the JAC1964 intake (JAC-T4.3, H9-C1, H9-T1, H9-T2);
- H01 v5 (`reports_20261120\deligne_sign_only_paper\deligne_sign_only_v5.tex`, the remark at lines 319–324);
- our text of record: cote 16 scans 014, 034, 040, 044–050; cote 44 scans 004 and 008.

**Computation.** I recomputed IF-03 on the Boolean exterior model with my own code (`scratchpad\hs\ext_order.py`).

**Scope:**
- **Read in full with a targeted proof check (14):** SN-C02, SN-C03, SN-C04 (as a deduction from Kleiman 2.13),
  SN-C05, SN-10, SN-11 (as a cited deduction), SN-12, SN-13, SN-14, IF-01, SN-44-01, SN-44-02, SN-44-04 and SN-44-05.
- **Independent re-computation (1):** IF-03, all eight indices, n = 1–4.
- **Read with the argument followed, not all steps rederived (1):** SN-44-03.
- **Statement level (7):** SN-C01 (the reading of the source), IF-02, IF-04 to IF-09, SN-44-06.

**Archive locators: all checked against our text of record.**
- SIGN_NEXT cites by our scan numbers (PDF pages), with folios where given. "Cote 16 scan 050 (folio 49)" matches our
  `\mspage`.
- Cote 16: scans 044–047 are the letter of 4.1.1967; 048–050 the letter dated 6.1.1966; scan 049 holds the
  semisimplicity passage; scan 050 the Proposition; scans 034 and 040 the restriction/Gysin and Λ_Y = φ^*Λ_X²φ_*;
  scans 014–018 are §7, Φ₀.
- Cote 44: scan 004 holds Th. 5 on manuscript page 2 (our `\mspage{2}`); scan 008 holds the primitive-decomposition
  margin.

  Every locator matches.

## 1. Verdicts, finding by finding

### Main question: scan 050's Proposition, C and I

- **SN-C01, the reading of the source: statement level, and it bears on our transcription.**
  - Our `16_scan050.tex` reads `\unsure{C|A}_χ(X) is equivalent to ... C_χ(Y)+A′_χ(X×X)⁰+A″_χ(X×X)⁰`. The run reads the
    left letter as **C**, i.e. C_G(X), Kleiman's B(X).
  - Its evidence: the CSG transcription L11d p. 3; the Proposition (i), (ii bis) of the 4.1.67 letter; and Kleiman 1968,
    Th. 2.13(i), (ii′), whose statement is exactly C ⟺ C(Y) + the critical L² on X×X.
  - I agree that the mathematics forces C. **A row for the second pass** (below).
- **SN-C02: confirmed.** The literal lower critical Gysin reading, j_*Alg^{m−1}(W) = Alg^m(T), fails.
  - On P¹×P¹ with a (1,1) curve: j_*1 = a + b spans a line, while Alg¹ = Qa ⊕ Qb.
  - The same holds on E×E.
- **SN-C03: confirmed.** The ingredients:
  - L_T² = g·L_W·r = L_T·j_*·r;
  - A₀(T) ⟺ R₀ + G_{L,0} (weighted Gysin);
  - G_{L,0} ⟺ G₀ + A₀(W).

  Each direction is a few lines, using hard Lefschetz injectivity and the weak Lefschetz isomorphisms r and g.
- **SN-C04: confirmed as a deduction from Kleiman 2.13.** C_G(X) ⟺ C_G(Y) + R₀(T,W) + G_{L,0}(T,W). Here W is a
  hyperplane section of X×X, not Y×Y.
  - This is **the corrected form of Grothendieck's scan-050 Proposition.** The factor L_T missing from his A″ is restored
    as a hypothesis.
- **SN-C05: confirmed.** The formal module gives g∘r = L_V and r∘g = L_U (both checked), with R₀ and G₀ true and A₀ false.
- **SN-10: confirmed.** The classical abelian Lefschetz theorem (Kleiman 2A11; Lieberman) makes Λ algebraic. The identities
  s∘j^* = 1 and j_*∘t = 1 follow from the string ranges; Λ_Y = j^*Λ_A²j_* is our scan 040. Classical.
- **SN-11: confirmed as a cited deduction, conditional on 032** (Theorem 1.1, claimed; human proof van Hoften–Sempliner,
  Hexagon 2610.00259).
  - The chain: 032 → Milne 2002 Th. 3.3 (Hodge standard conjecture for abelian varieties, hom = num) → Kleiman 3.11,
    3.12 and 3.14 → semisimplicity and algebraic splittings, for all products of abelian varieties.
  - For powers of CM elliptic curves it is unconditional (SG-04 + Milne Remarks 3.7–3.8).
  - **The Q2c disposition is the one my HODGE_SIGN intake proposed.** The run adds the version crosswalk: Milne 2002
    Theorem 3.3 in the published version (`2002aP.pdf`, pp. 8–9) is Theorem 4.6 in the original `2002aS.pdf` that the
    human deposit cites.
- **SN-12: confirmed.** A simple CM fourfold with E = FK, where F = Q(α), f = T⁴ − 5T² + T + 1, and K = Q(i).
  - I checked the four real roots by sign changes, irreducibility mod 3 (no root), and the factorization mod 2,
    (T+1)(T³+T²+1). So Gal(f) = S₄, and K is the only proper CM subfield.
  - With a CM type of K-signature (2,2): NS rank = [F:Q] = 4, and products of divisors have K-bidegree (2,2). So the Weil
    lines, of bidegrees (4,0) and (0,4), are not divisor-generated. By 032 they are algebraic.
  - **This refutes the literal U-02 wording.** The phenomenon is classical (Weil 1977; Moonen–Zarhin; from memory). The
    explicit field is new as an example. It agrees with my HODGE_SIGN intake, which closed Q2c as positivity, not as
    Lefschetz generation.
- **SN-13: confirmed.** v = (u^†u)^{−1}u^† in eRf. Positivity makes u^†u invertible on eR, and the inverse is a polynomial
  in u^†u.
- **SN-14: confirmed.** In the rigid tensor countermodel, N is a single Jordan block, F = c·exp(N), and
  Tr(aF^s) = 3a₀c^s. So all traces factor through R/rad R, while τ(N^†N) = 0.
  - **The sign-only method cannot by itself supply scan 049's positivity**, even with correspondences as coefficients.
  - This is the precise form of HODGE_SIGN HS-05 and U-01, extended to correspondence algebras.

### Q6g: the Fock model and the integral indices

- **IF-01, the integral Fock intertwiner Φ_n: F_n → Λ*(Z^{2n}): confirmed.** It is a bijection of integral bases, with
  y_a∂_{x_a} ↔ p_a∧ and divided powers preserved. This is **the attack my HODGE_SIGN intake proposed** (the Fock model as
  the candidate intertwiner). It is exact at the level of the coefficient lattice. The run itself states that it does not
  identify a global theta integral (Part II).
- **IF-02: statement level.** The divided-power order Z[L^{(r)}, D^{(r)}] is saturated, and equals Q[L,D] ∩ End_Z, of
  rank (n+1)(n+2)(2n+3)/6, for every n. Consistent with the IF-03 recomputation (index 1 for the divided-power order).
- **IF-03: independently recomputed. All eight indices agree.**

  | n | [A^ext : Z[L,D]] | [A^ext : Z[L,D,π]] |
  |---|---|---|
  | 1 | 1 | 1 |
  | 2 | 2⁷ | 2² |
  | 3 | 2²⁷·3⁴ | 2¹⁰·3² |
  | 4 | 2⁸¹·3³³ | 2³²·3¹⁰ |

  My code is my own lattice closure with Smith reduction on the Boolean blocks v = 0, …, n, with no use of the run's
  program. **These are the indices on Grothendieck's actual exterior model Φ₀ ⊂ End(ΛM₀)** (our cote 16 scan 014, §7).
  They answer the scope correction of my HODGE_SIGN intake: SL-09 had computed only the string model.
- **IF-04 to IF-09: statement level.** In particular:
  - IF-09: the actual m = 2 two-step partitions, the primitive period 1, and all Smith factors 1;
  - IF-06: the full oscillator is not a finite Lefschetz module;
  - "U05-LIFTCOUNT refuted" (IF-05, IF-07, IF-09).
- **Q6g-GLOBAL-GEOMETRY:** active, not yet decided.

### Cote 44: the corrected Theorem 5 (H04)

- **SN-44-01, the corrected Th. 5: confirmed.**
  - The formula: ⟨z,z′⟩_G = (−1)^m(deg ZZ′ − Σ_s a_s(Z)^t G_s⁻¹ a_s(Z′)).
  - The proof is orthogonal projection onto the vertical classes modulo the radical:
    - smooth-fibre classes are radical, since N_F is trivial;
    - an admissible extension exists (Kahn 2024, cited);
    - the Gram correction follows.
  - The identification with Néron–Tate on the higher Picard variety is cited: Chen, arXiv 2512.22788, Th. 7.9, over C;
    SN-44-06 for any characteristic, at statement level. **That identification rests on Kahn and on Chen's preprint.**
    The formula as an identity for the geometric height of Kahn does not.
  - **It is the same correction as JAC1964 H9-T1**, with the same existence gate (admissibility). Two runs agree.
- **SN-44-02, the node form deg(DD′) = (−1)^m·ν(D)·ν(D′), with ν = u − v on the exceptional quadric: confirmed.**
  - I followed the blow-up computation: p^*D = D̄ + (−1)^{m+1}δE^m; N = O(−2Q); E^{2m} = −1.
  - It uses the quadric table of HODGE_SIGN SG-02, which I checked in the HODGE_SIGN intake.
- **SN-44-03: argument followed.**
  - E_van ≠ 0 ⇒ no correction. The local defect map is injective when δ_s ≠ 0, and the vanishing cycles are conjugate
    (SGA 7 XVIII 6.6).
  - E_van = 0 ⇒ the height is zero. The fixed part makes the variation constant, and constant abelian varieties have only
    constant points over C(t).
  - This matches JAC1964 H9-T2 and the dichotomy my HODGE_SIGN intake proposed.
- **SN-44-04: confirmed; I rederived it. The three nodes contribute 1 each.**
  - D_i = {x = e_i, s = s_i} × P²_y lies in M, because d_i(s_i) = 0. It is the plane through the node: the non-Cartier
    Weil divisor my HODGE_SIGN intake predicted.
  - N_{D_i} = Q_y^∨, c₂(Ω¹(1)) = 1, so D_i² = 1.
  - π^*Z·D_i = b² = 1.
  - c₂(Q_y^∨ ⊗ O(a+t)) = Z + t(2a − b), and t(b − 2a) is vertical, isotropic and orthogonal.
  - **0 = 3 − (1+1+1).**
- **SN-44-05: confirmed.** p_s = (−1)^m D_s × D_s are orthogonal idempotents onto L^m.

### Counts

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 14 |
| Independent re-computation, confirmed | 1 (IF-03) |
| Argument followed, confirmed | 1 (SN-44-03) |
| Statement level | 7 |
| A gap | 0 |
| Refuted | 0 |
| Scope notes | SN-11 and SN-12 are conditional on 032; SN-44-01's Néron–Tate identification rests on Kahn and Chen (preprints); SN-12's phenomenon is classical |

**The run's own refutations, which I confirm:**
- the literal lower-Gysin reading of scan 050 (SN-C02);
- the formal trace-only route to positivity (SN-14);
- the literal U-02 (SN-12).

## 2. What is new

- **The corrected scan-050 Proposition (SN-C03/C04)** is a correct, citable form of Grothendieck's remark. The missing L_T
  is made explicit, and C is read for the overtyped letter. In substance it is Kleiman 2.13. What is new is the exact
  form of the "weak" conditions A′ and A″ and the proof that the literal A″ fails (SN-C02, SN-C05).
- **SN-44-04 completes H04.** With JAC1964's quadric pencil (H9-C1), there are now two worked counterexamples to the
  displayed Th. 5. Both have per-node unit contributions, and the general corrected formula has been proved twice (H9-T1,
  SN-44-01).
- **IF-03:** exact indices of Z[L,D] in Grothendieck's actual exterior order up to rank 4. They are new as computations,
  and now independently confirmed.
- **SN-14:** a formal limit of the sign-only method, stated as a theorem.
- **Known or classical:** SN-10, SN-11 (through 032), SN-12's phenomenon, SN-13.

**Against tonight's runs.**
- JAC1964's H9-T1 and H9-T2 and SIGN_NEXT's SN-44-01 and SN-44-03 are the same corrected Th. 5. Cross-reference them as
  two independent derivations.
- JAC-T4.3 (Th. 4 for abelian varieties) and SN-11 use the same 032 → Milne chain.

## 3. The two proofs, and H01

- No finding uses RH or GRH.
- Masullo is not used.
- 032 is used in SN-11 and SN-12, marked conditional.
- **H01** (hexagon:2611.00789) is used as settled input (SG-08–SG-11). Nothing in SIGN_NEXT changes it.
  - SN-14 states what H01 cannot do: give semisimplicity or positivity, even with correspondence coefficients. H01 v5
    already says it gives no semisimplicity (line 93).
  - **For H01 v2:** a one-line remark citing SN-14, and a locator refinement. H01's remark (lines 321–323) cites
    "cote 16, scan 40" for E^{n−1}. In our text of record E^{n−1} is defined at the end of scan 034 as
    Ker(φ_{n−1}: H^{n−1}(Y) → H^{n+1}(X)), and is named "partie évanescente" on scan 040. Write "cote 16, scans 034–040".

## 4. Integration (edits listed, not made)

**Hodge sketch** (`reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`):
- **3.2:** after "C(X) ⟺ C(Y) and A(X × X) in the critical degree", add: "(corrected form, SIGN_NEXT SN-C03/C04, checked:
  C_G(X) ⟺ C_G(Y) + R₀ + L_T·j_*-surjectivity on a hyperplane W of X×X; the literal A″ fails, SN-C02. For abelian
  varieties C and I hold, conditional on 032: SN-11.)"
- **3.4:** add "Th. 5 corrected: SIGN_NEXT SN-44-01 and JAC1964 H9-T1. P²×P²: one unit per node (SN-44-04)."
- **Route 4:** add "IF-03: indices of Z[L,D] in the actual exterior order, 1, 2⁷, 2²⁷3⁴, 2⁸¹3³³ for n = 1–4 (checked
  independently). With degree projectors: 1, 2², 2¹⁰3², 2³²3¹⁰. IF-01: the integral Fock intertwiner."

**HODGE_SIGN rows:** U-01 stays (SN-14); U-02 is closed for positivity and refuted literally (SN-11, SN-12); U-03 is
solved (SN-44); U-04 is partly constructed (IF-01, IF-08); U-05 is refuted as a lift-count assertion (IF-05, IF-07,
IF-09).

**A second-pass transcription row:** cote 16, scan 050, line "Proposition": our reading `\unsure{C|A}_χ(X)` → read **C**.
The reason: Kleiman 2.13 (C ⟺ C(Y) + critical A on X×X); the 4.1.67 letter's Proposition (ii bis), our scans 044–045;
the CSG transcription L11d, p. 3. Rating: high on the mathematics; check the image.

**The H04 row in `HEXAGON_CANDIDATES.md`:** the gate "compute each fibre's contribution" is now done (SN-44-04), and the
corrected formula is proved twice.

## 5. Hexagon candidates

- **H01 v2:** unchanged in substance. Add the SN-14 remark and the scans 034–040 locator. The gates stay as recorded.
- **H04 (cote 44 Th. 5 fails as displayed; the corrected formula):**
  - **Now complete at the level of mathematics:** two counterexamples (AR-01 with SN-44-04, three units; H9-C1, two
    units), and the corrected formula (SN-44-01 and H9-T1, with the E-dichotomy SN-44-03 and H9-T2).
  - The counterexample and the per-node computation are self-contained (pure intersection theory). Only the height
    identification uses Kahn and Chen.
  - **The gates left:**
    1. a check of the scan image of our 44_scan004 (the "géom. intègres..." ellipsis);
    2. the run's final, for stability;
    3. a write-up and my read of every page.
  - Test 5: moderate, for readers of the archive. **One to two gates away.**
- **H11 (Th. 4 for abelian varieties in every characteristic):** SN-11 adds C_G and I(A×A) and semisimplicity on the same
  032 → Milne chain. Test 2 is unchanged (032 is unrefereed). It could be combined with SN-C03/C04 into a cote-16
  companion. The gate is still 032's status.
- **H12 (ghost classes):** not changed by SIGN_NEXT.

## 6. Prompt updates (SIGN_NEXT successor, or to the run)

1. Decide Q6g-GLOBAL-GEOMETRY. Use IF-08's transported global block matrices on one fixed CM datum, and compute their
   Smith factors.
2. **The main question beyond the abelian case.** Test SN-C04 on varieties with known B but unknown I: for example a
   smooth complete intersection in an abelian variety, or a quadric bundle. Ask whether R₀ and G_{L,0} hold on X×X there.
3. **Cote 44:** decide the E ≠ 0 nodal-fibre factoriality claim in positive characteristic (SN-44-06), and give a cubic
   fourfold pencil (E ≠ 0) as the positive example of the uncorrected formula.
4. **Archive:** the run should carry the second-pass row for scan 050 (C, not A) into its `TRANSCRIPTION_NOTES.tsv`.
