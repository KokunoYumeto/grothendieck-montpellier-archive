# Full intake of RESEARCH_SA08 and RESEARCH_SA08_C3_D031, statement by statement

- **This intake.** Claude Opus 5.5 at effort max (agent a34c04448e8299803), 21-22 Nov 2026, as asked by the coordinator
  (the user, 21 Nov ~23:5x UTC: [the user's words, omitted]).
- **The lists.** The statements of each newest register that no intake had checked, from `field_experts/INTAKE_LEDGER.md`
  section 9: RESEARCH_SA08, 118 statements; RESEARCH_SA08_C3_D031, 108.
- **Check events.** `INTAKE_RESEARCH_SA08_20261121_full_CHECK_EVENTS.tsv` holds the events of both runs; the run is named
  in the who column.
- **Computations.** `intake_scripts/full_intake_sa08_checks.py`, with its output, for Part I (B-09, B-12, D-027), and
  `intake_scripts/full_intake_c3d031_checks.py`, with its output, for Part II. Neither runs a program of the return.
- **Earlier intakes, cited instead of redone.**
  - `INTAKE_RESEARCH_SA08_20261119.md`, with events INT-SA08-E01 to E20.
  - `INTAKE_RESEARCH_SA08_C3_D031_20261120.md`.

## Part I. RESEARCH_SA08 (final 20261119T1027Z, GPT-6 Astra, ChatGPT Pro mode)

### 1. What was checked

121 events cover all 118 statements.

| Check type | Events |
|---|---|
| targeted proof check | 68 |
| independent re-proof | 26 |
| carried as background without fault found | 24 |
| computation or formal certificate | 3 |

Of the 24 background events, 16 are statements I read without their proofs:
- D-028;
- C19, C22, C23, C24, C27, C28, C29, C30, C31, C32, C34, C36;
- D-029, D-030, D-032.

These are the bar and repair constructions of C.3. Their outcome fields say so plainly. The other 8 are known results
whose sources I did not open:
- A-019 (Horel, Toën, Cartan, Ekedahl, Hedenlund-Moulinos);
- B603 (Berger-Fresse);
- D006M (Mandell);
- D013, D018, D019, D021 (Breen; Milne);
- D-024 (Zakharov).

**Read with their proofs and checked:**
- **Part A (all of it):**
  - A-001 to A-018, A-020 to A-026;
  - A-004 and A-026 carried from the first intake, where they were re-proved and checked.
- **Part B (all of it):**
  - B-01 to B-17;
  - B601, B602, B604, B605.
- **Part C:**
  - C01 to C18;
  - C21 (items 1-3);
  - C20 and C25 (their obstruction groups re-derived);
  - C26, C33 (items 1 and 3) and C35 (on an instance).
- **Part D:**
  - D001 to D012, D006E;
  - D014 to D017, D020;
  - D022, D023, D-025, D-026, D-027;
  - D-031 (carried from the C3_D031 intake, where it was checked against the source).

**Computations:**
- **B-09.** The run's 6-vertex RP², recomputed: 64 one-cocycles, 32 coboundaries, and Alexander-Whitney square 1 on
  the nonzero class.
- **B-12.** gcd(i+1, j+1) divides C(i+j, i) for i, j ≤ 150.
- **D-027.** The boundary identity (D-27e) and the unit alternating sum (D-27f), in 3971 cases.

### 2. Refuted or corrected

- **By this intake:** nothing. No statement of the run is refuted, and no step I checked fails.
- **The run's own refutations, all confirmed where read:**
  - A-004 (L1 literal);
  - A-009 (ordinary tails at t = 0);
  - A-016, A-021, A-022, A-024 and A-026 (L2 and the binomial bridges);
  - B-02 (the three printed conditions; the 2-invertible margin);
  - B-07 (L4);
  - B-09 (the RP3 sphere test);
  - B-11 (L8, exclusive reading);
  - B-13 (the decompositions of 208);
  - B-15 (automatic continuity);
  - B601 and B604 (the half-algebra and the pointwise reading of 360);
  - C03 and C07 (L5 as contraction; strict equalization);
  - C11 (tensor closure);
  - D004, D009, D010, D014, D015, D018 (on Breen's authority, not opened), D020;
  - D-031 (Caradot-Lin Prop. 3.10).

### 3. What is new

The run's new results, as I read them, are listed below. The run credits Cartan (1976, §7) for the endpoint and
products of A.1.
- **A.1-A.3.** The literal against graded answer, and the formula for all PD triples through derived tails (A-002 to
  A-009). The integral descent algorithm for divided powers (A-010 to A-014). The T = 1 specialization to Sullivan's
  forms (A-025).
- **A.4.** The obstruction to any filtered numerical lift: A-026, with its forerunners A-016, A-023 and A-024. Also the
  numerical Kähler associated graded with its 2-torsion (A-017).
- **A.2.** The shadows with an exact left adjoint, built on the mechanism of the Pro notes of MPL_136_235-281 (D001 to
  D006E).
- **B.**
  - The structure of Ω: the corrected three-data theorem, the binary parametrization, ind-affine but not affine (B-01 to
    B-04).
  - The action on cohomology and the Steenrod question (B-05, B-06, B-08, B-10).
  - The discontinuous automorphism (B-15).
  - The half-algebra criteria (B602, B605).
  - Natural convolution PD laws (D007 to D012).
- **C.** The faisceautisation results: L6 (C01), C02 to C06, C07, and C08 to C10 (Q-algebras, Z_(p)-algebras, positive
  characteristic).
- **C.3 over Z.** The finite-prime theorem C17, the obstructions C11 to C15, C19, C26, C31 and C35, and the conditional
  reductions C30, C32 and C34.
- **The Breen comparison of 374-376** (D013 to D021). It corrects Grothendieck's page: the missing +1 (the ink has
  v_p(i), INT-SA08-E11), the Q^i, and Frobenius semilinearity.

### 4. Errata

None in the mathematics I checked.
- **One point of wording.** A-016 calls its statement "Refuted" in the register while its paper text proves a
  nonexistence theorem. The register's "Refuted" means the strict L2 bridge is refuted. This is consistent.
- **Locators left to check.** Breen 1978 (D013, D018, D019, D021), Mandell 2006 (A-018, D006M), Christensen-Holm (C05),
  Berger-Fresse (B603) and Lurie HA (D006E) were not opened by me. A-018 and D006M rest on Mandell, and B.8 rests on
  Breen.

### 5. Hexagon readiness (the five tests of field_experts/HEXAGON_CANDIDATES.md)

- **A-026,** no filtered numerical lift of the PD cochains (with A-023 and A-024).
  - **Complete:** yes, and **Checked:** yes. Part 1 was re-proved and computed, part 2 checked step by step
    (INT-SA08-E02-E04, E20), and the run re-proved it independently.
  - **Self-contained:** needs the weightwise comparison R1, which is proved in A-001 to A-003.
  - **Stable:** C.3 runs on in RESEARCH_SA08_C3_D031, but it does not touch A-026.
  - **Of interest now:** to people working on binomial rings and integral models of homotopy types (Horel,
    Kubrak-Shuklin-Zakharov, Toën).
  - **Verdict:** a candidate. The one thing missing is a literature check that the numerical-tail pairing classification
    (A-023) and A-026 are not already in Horel or KSZ. The run searched; I did not.
- **D-031,** the refutation of Caradot-Lin Prop. 3.10. This is a correction of others' work, so it goes to the authors
  first (outreach plan), not to Hexagon.
- **B-15,** an abstract discontinuous automorphism of the completed PD de Rham algebra. Complete and checked; of narrow
  interest.
- **Nothing else** passes "of interest now".

## Part II. RESEARCH_SA08_C3_D031 (checkpoint 08, 20261119T2043Z, GPT-6 Astra, ChatGPT Pro mode)

### 1. What was checked

119 events cover all 108 statements of the list (`field_experts/INTAKE_LEDGER.md` section 9).
- **The four statements the list leaves out** were treated in the intake of 20 Nov
  (`INTAKE_RESEARCH_SA08_C3_D031_20261120.md`):
  - B-001, B-003 and B-004 were checked there;
  - A-L10 had only its bridge link checked there, and its proof is still unread.

| Check type | Events |
|---|---|
| targeted proof check | 92 |
| independent re-proof | 10 |
| computation or formal certificate | 5 |
| carried as background without fault found | 12 |

- **Upgraded rows.** Six statements were first read without their proofs: A-004, A-005, A-006, AT04, AT07 and A-S09-04.
  Their proofs were read later in this intake, and each now also has a targeted proof check. The earlier background
  events stay in the table as history.
- **Caveats now resolved.** The events of A-S09-24, -27, -28, -30 say they rest on A-004 and A-006 at statement
  level, and those of AT16, AT18, AT22 say the same of AT04. Those caveats are settled by the later upgrade events.
- **Statements still at background level:**
  - A-S09-02 and A-S09-03 re-prove SA09 A2.2 and A3.1-A3.2. Those results were checked in the SA09 full intake.
  - A-S09-05 is a known result whose source I did not open.
  - A-CS, A-TL and A-SA09 are open-question status paragraphs. There was no proof to check, and their accounts of the
    reductions agree with the rows as checked here.

**Read with their proofs and checked (TP or IR):**
- A-001 to A-006, IC01 to IC03, A-S09-01, A-S09-04, and A-S09-06 to A-S09-31;
- AT01 to AT29b, with AT10-lattice, AT14-H1, AT15-restoration and AT16-comparison;
- A-P01, A-H01, A-SAT01, A-WF01 and A-WF02;
- A-L01 to A-L09 and A-L11 to A-L21;
- B-002 and B-005 to B-008.

**Computations.** They are in `intake_scripts/full_intake_c3d031_checks.py`, with its output; the script runs no program
of the return.
- **AT10-lattice:** the p-unit factorial quotients, in 6721 cases.
- **AT11:** the two binomial facts behind the nonlifting.
- **AT12:** the normalized complex of the triple parameter C_n (bases, differential, acyclicity, e_012 closed).
- **A-S09-22**, a symbolic check in the rational free algebra over Q[t]:
  - d^2 = 0, both twisted and untwisted;
  - dB = 2 zeta and dB = 2 zeta_tw;
  - dK and dJ;
  - the detector (-2,0,0,2,0,0), with value 1 on zeta.
- **A-L20 at p = 3:**
  - dB = 3 zeta;
  - dK and dJ;
  - the detector (0,6,0,0,3,0), with value -1 on zeta;
  - the d^2 test that exposes the erratum below.

**Not opened by me.** These external results are carried:
- Nagpal-Snowden, Thm 7.1(a) and Thm 8.3;
- Fu-Nuiten, Theorem C and Thm 4.2 (behind A-S09-11 and A-S09-12);
- Kubrak-Shuklin-Zakharov (A-S09-15);
- Bhatt-Lurie-Mathew (A-WF01, A-WF02);
- Castiglioni-Cortinas (A-S09-06, A-S09-07);
- Herscovich-Rey (A-L18; the run's own proof of that remark was checked);
- Stacks 0CRM (A-S09-29);
- Richter (A-L05).

### 2. Refuted or corrected

- **By this intake:** nothing is refuted. Every proof I checked holds.
- **An erratum, in two places of the same family.**
  - (AL.110) in B_p3_second_repair.tex and (AL.124) in B_odd_prime_second_repair.tex print dl = -ur + t sigma.
  - The weights do not match: l has unshifted weight p^2, and t sigma has weight p^2 - p + 2.
  - The column (u, -t^{p-1}) of the periodic matrix N gives dl = -ur + t^{p-1} sigma, which is t^2 sigma at p = 3.
  - With the printed formula d^2 l is not zero. With the corrected one it is, and d(dJ) = (t^p - pcu) sigma = 0. My
    script confirms this at p = 3.
  - No assertion of A-L20 or A-L21 uses dl, so their results stand.
- **A point about another author's proof.**
  - A-L14 observes that the unqualified uniqueness sentence in the proof of Nagpal-Snowden Thm 7.1(a) fails for a zero
    restriction.
  - The run's counterexample is correct: the zero map on (T)<p-1> extends both by 0 and by T^[p-1].
  - I did not check the source's wording, and the theorem itself is not affected.
  - If the point is confirmed against the source, it is a correction to others' work. It goes to the authors under the
    outreach plan, not to Hexagon.
- **The run's own refutations, confirmed where checked:**
  - AT12 (a prescribed C21 model with no growing local completion depth);
  - AT28 (even a fully exact reference does not supply the C34 truncation agreements);
  - A-L01 to A-L03 and A-L07 (prescribed tail primitives);
  - A-L09 (saturation can create horizontal homology);
  - A-L11, A-L12 and A-S09-22 (the resolved-tail comparison fails in degrees one, two and three);
  - A-L19 (saturation does not give flat terms);
  - A-S09-06 to -08 (three rectifications);
  - A-S09-09 to -12 and -23 (bounded cotangent support);
  - A-S09-15 (the binomial Rees lift);
  - A-S09-17 (a coefficient-residue obstruction);
  - A-S09-25, -26 and -28;
  - A-WF01 and A-WF02 (Frobenius saturation and completion);
  - AT23 (prime transfer).

### 3. What is new

These are the run's new results, as I read them.
- **Obstruction classes.** AT11 gives obstruction classes chi_{M,L} for every tail and every length. AT12 turns them
  into a refutation of the sufficient arithmetic-completion route of SA08 C30/C34 for prescribed partial maps. AT28 keeps
  that refutation when the reference is exact.
- **Explicit integral repair machinery:**
  - AT13-AT17: coefficient-resolution and two-cell repairs with actual target maps;
  - AT21-AT27: boundary correction, carriers, the global prism, reference-controlled completion;
  - AT29 and AT29b: integral completion through form three, with local reference paths;
  - A-SAT01: iterated saturation.
- **The exact period residues and their vanishing.**
  - The residues: AT15 (q = 3), AT18, and A-L13 (simultaneous criterion).
  - Their vanishing for the specified quadratic classes: AT19, AT20, AT22, and A-L20 and A-L21 at every odd prime.
- **Defect constructions:**
  - A-P01: deep resolved tails create degree-two torsion at every prime;
  - A-L11, A-L12 and A-S09-22;
  - AT23: a p-primary repair creates r-torsion for every prime r.
- **The PD cotangent complex.** For every fixed N >= 2, the PD cotangent complex of Gamma(T)/I_N has unbounded
  prime-local homological support (A-S09-09 to A-S09-12; the last two rest on Fu-Nuiten's Theorem C). A-S09-23 is the
  consequence for second skeletons.
- **Reductions of both main questions to smaller gates:**
  - A-S09-24: global low-degree exactness;
  - A-S09-27: one disk per weight;
  - A-S09-29: countable objects;
  - A-S09-30: at most three disks per weight;
  - A-S09-28: the single-disk localization is not faithful.
- **Smaller exact results:**
  - A-S09-26: the Hadamard image (Tor_1 = I_1/I_1^2, of order p in weight p^e);
  - A-S09-13 and A-L05: integral bar integration;
  - A-H01: coefficient tails kill horizontal homology;
  - A-L14 to A-L18: flatness from bounded-below freeness.
- **Still open:** the two main questions, A-CS (common sources) and A-TL (terminal localization).

### 4. Errata

- **(AL.110) and (AL.124):** dl = -ur + t sigma should read dl = -ur + t^{p-1} sigma (section 2).
- **Nothing else** in the mathematics I checked.

### 5. Hexagon readiness (the five tests of field_experts/HEXAGON_CANDIDATES.md)

No finding of this checkpoint is ready. Stable fails for most of it: the run is a checkpoint (cp08), the C.3
construction is still going on, and most rows are steps of that construction.

- **The closest is A-S09-11 with A-S09-12:** unbounded prime-local support of the PD cotangent complex of every
  truncation Gamma_Z(T)/I_N.
  - **Complete and self-contained:** yes, given Fu-Nuiten's Theorem C.
  - **Stable:** yes; it does not depend on the ongoing construction.
  - **Checked:** this intake checked the deduction. Fu-Nuiten was not opened.
  - **Of interest now:** possibly, to people working on derived divided powers.
  - **Needed first:** opening Fu-Nuiten, and a literature check that the computation is not already there.
- **A-S09-26 and A-WF02** are small exact observations and do not pass "of interest now" on their own.
