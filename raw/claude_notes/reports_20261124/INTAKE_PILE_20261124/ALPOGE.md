# Cluster ALPOGE: Alpöge's theorem, its machinery, and L-functions beyond it

Intake pile of 24-25 Nov 2026, for the conference (Claude Fable 5.2, after the weekly reset). Written 24 Nov 2026 by
Claude Opus 5.5 at effort high (cluster reader ALPOGE), launched by the main session 329fb1e6 (Claude Opus 5.5 at
effort max). Every run here is GPT-6 Astra (ChatGPT Pro mode); the runs record their own effort as "inherited, not
exposed".

**A** below is L. Alpöge's theorem (20 Nov 2026, Lean-formalized): the Riemann hypothesis for every Dirichlet
L-function, ζ included. It is used as a theorem. **M** (GRH for the Hecke L-functions of Masullo's draft) is not a
theorem; nothing below rests on it except where said.

**Earlier intakes.** Six of the eight runs were taken in at their newest checkpoint before tonight, by Claude Opus 5.5
at effort high (agents abcaba9b, afa2696b, ad855737, af2a18f6, a25c2acb). Their intakes and primers (23 Nov) are in
`field_experts/intake_20261121/intakes/<RUN>/`. For those runs this file restates and ranks; it adds a spot check each.
**BEYOND_DIRICHLET (cp10) and MOONSHINE_AFTER_ALPOGE (cp01) had no intake.** They are read here for the first time.

Files: `ALPOGE_ITEMS.tsv` (one row per item); `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` (my checks, one file per run);
`ALPOGE_s5cert_check.py` (my recomputation of two S₅ certificates); work file
`agent_notes/20261124T2111Z_Intake_pile_Alp_ge_cluster_NOTES.md`.

Paths: `RR` = `grothendieck_archive_transcription_20261110/research_returns/`; `BD` =
`RR/BEYOND_DIRICHLET_checkpoint_10_20261124T2010Z_unzipped/workbench/`; `MO` =
`RR/MOONSHINE_AFTER_ALPOGE_checkpoint_01_20261124T2045Z_unzipped/`.

---

## The cluster's most interesting items, by usefulness

1. **Ihara's kernel question at every Vandiver prime (NIGHT_AFTER_ALPOGE, C.IHARA).**
   - **Statement:** for odd p with X_p⁺ finite, in particular every Vandiver prime and every odd p < 2³¹, the fixed field
     of the kernel of G_Q → Out(π₁(P¹ − {0,1,∞})^{(p)}) is Ω_p. Ω_p is the maximal pro-p extension of Q(μ_p) unramified
     outside p.
   - **Why it matters:** this is the Anderson-Ihara question for the pro-p fundamental group. It was recorded as open
     at irregular primes (Sharifi, RIMS Kôkyûroku 2120 (2019), p. 222). It is the strongest theorem in the cluster.
   - **Inputs:** Hain-Matsumoto, Brown, Wake-Wang-Erickson, Fukaya-Kato. It does not use A.
   - **Checks:** every step by ad855737 (Claude Opus 5.5 at effort high), 21-23 Nov. Tonight I re-proved its Vandiver
     lemma (7.1).
   - **Where:** deposited as hexagon:2611.00939 (board H06b). Three small fix-ups of the posted text are open.
   - **Path:** `RR/NIGHT_AFTER_ALPOGE_checkpoint_13_20261123T1154Z_unzipped/workbench/k-theory-and-galois-groups-workbench/papers/ihara/main.tex`.

2. **Galois orbits of CM points with an explicit exponent (NIGHT_AFTER_ALPOGE, A.ORBIT).**
   - **Statement:** every CM point x ∈ A_g(Q̄) has |Gal·x| ≥ c_g D_x^{1/(4g)}, with explicit c_g, for every centre
     order.
   - **Where A enters:** A removes the Siegel zero in Stark's lemma, through imaginary quadratic subfields. This is
     the cleanest use of A as a tool in the cluster.
   - **Checks:** every step by ad855737, constants recomputed. The literature gate is passed: effectivity is known
     (Banks, Cureton-Thorner, Liu), and the exponent 1/(4g) with explicit constants is the new part.
   - **Where:** the H15 note, `reports_20261123/h15_note/`; ready for the user's word.

3. **Artin's conjecture for S₅-extensions under a weaker real-zero hypothesis, and four unconditional fields
   (BEYOND_DIRICHLET Paper II, BD-S25/S26, BD-S12/S14/S15/S16; strengthens MAS_ARTIN MA-FQ-004).**
   - **Family:** L/Q with group S₅ and complex conjugation of type (12)(34). There is no condition at 5:
     Pilloni-Stroh, Théorème 0.3, replaces Calegari's Lemma 3.2.
   - **Hypothesis:** the two entire quadratic Hecke functions B = ζ_H/ζ_F and C = ζ_{J'}/ζ_J (J = L^{S₂×S₃},
     J' = L^{S₂×A₃}) have no common real zero in (0,1) other than 1/2. Central zeros of any order are allowed.
   - **Conclusion:** Calegari's GL₅ representation matches ρ₅ at every place (standard local factors), and every
     nontrivial irreducible Artin L-function of L is automorphic and entire.
   - **Comparison with Calegari:** his Theorem 1.2 assumed ζ_H(σ) ≠ 0 on all of (0,1).
   - **Mechanism, two parts:**
     - every comparison pole is a common zero of B and C, through the odd-rank exterior square (Belt Thm 6.2);
     - an excess central zero gives an integer-valued positive-definite function on ℝ_d, which Cohen's idempotent
       theorem rules out.
   - **Four explicit fields:** real nonvanishing of B is certified by Miller's strip-positive explicit-formula test
     for discriminants 8249, 60061, 30301 and 48976. Artin's conjecture holds unconditionally for these fields.
   - **Checks:**
     - the run: author proofs, same-model statement-only re-proofs, and MPFR and Arb interval certificates;
     - mine: a targeted check of the common-zero step;
     - mine: a recomputation of the 8249 and 60061 certificates, which gave margins 0.90 and 0.13.
   - **Caveat:** Dwyer 2014 (Bull. LMS 46, 51-58) already certified S₅ examples by the explicit formula. The run never
     opened his list (LITERATURE.md l. 17), so whether these four fields are new is undetermined.
   - **Where:** `BD/papers/paper_II/main.tex` (43 pp.).

4. **What A makes unconditional in computation (CX_GRH).**
   - **From A alone:** Miller's primality test with Bach's cutoff is deterministic polynomial time (CX-N01). An r-th
     nonresidue in F_p, for a specified prime r | p−1, is found in poly(log p) (CX-N02), and in any supplied F_{p^m} in
     poly(m log p) (CX-N13). A primitive root comes from the factorization of p−1 (CX-N03).
   - **Koiran:** his Nullstellensatz-in-AM argument needs RH only for ζ_E of the solution field (CX-K01), so A covers
     abelian solution fields (CX-K03).
   - **Why it matters:** deterministic polynomial-time quadratic nonresidues and square roots modulo p were classical
     GRH-conditional results. A makes them unconditional. The run's contribution is the exact accounting of which
     L-functions each algorithm needs; the algorithms are Bach's, Ankeny's, Shoup's and Koiran's.
   - **Checks:** 21 of 39 findings checked step by step by af2a18f6 (21 Nov). Tonight I checked CX-N13 again.
   - **Where:** `RR/CX_GRH_final_20261121T0005Z_unzipped/CX_GRH.tex`. The GRH_ALGORITHMS run and board row H29 carry
     it on.

5. **The 3-primary K-groups of Q(ω, ∛269) in every degree, and the exact 7-adic class module (BEYOND_DIRICHLET
   Paper I with its seven-primary supplement; BD-K01, BD-R20; closes ALP_CONNES G219/G220).**
   - **K-groups:** for e ≥ 1, K_{2e}(O_E)_(3) ≅ Z₃[ω]/λ^{5+2v₃(e)+[e≡2 mod 3]}, from logarithmic class-group
     certificates.
   - **New tonight:** the faithful cubic components of the cyclotomic 7-adic class module of E are exactly
     Z₇[[T]]/(7,T). Every continuous strict specialization is O/(7, u−1). So s(e) = 1 at every weight of the matched
     coefficient-7 family.
   - **Consequence:** this empties the exceptional class that G219 left open, and fixes the family's cost in the
     cubic-RH budget at exactly 2(T−1) log 7 (BD-R21).
   - **Checks:** my targeted check of the descent steps, given the class numbers h(F)₇ = h(F₁)₇ = 7, which I did not
     replay.
   - **Use:** a complete, rerunnable K-theory/Iwasawa computation for a non-abelian field. It is not a famous
     question; its use is as an exact test case.
   - **Where:** `BD/papers/paper_I/main.tex`, `BD/papers/paper_I/supplement_seven/proof.tex`.

6. **The size floors of Alpöge's step 8, and the coefficient-field constraint (ALP_MACHINE LIFT54/55, LIFT110-113).**
   - **Size floors:** any datum satisfying the formal SizesAt has a chain of m theta lifts with
     x^{1/2−29ε/400} ≤ m ≤ x^{1/2−21ε/400}, so m > 2^7778, and a CM host of degree 2f > 2^33599. No bounded-length
     literal instance exists.
   - **Coefficient field:** over imaginary quadratic K with μ(K) = {±1}, a normalized ideal generator in an abelian
     F/K forces [J]² = 1 (Kronecker, then Schinzel). So the literal instance needs a metabelian CM coefficient field of
     relative degree h_K (LIFT112-113).
   - **Use:** these are facts about the formal interface, useful to anyone formalizing or shortening step 8. They are
     not facts about theta lifting.
   - **Checks:** targeted checks by abcaba9b (22-23 Nov). Claude Fable 5.2 at effort max re-derived the chain length.
     Tonight I recomputed the floors.
   - **Where:** board H30, H30b; `RR/ALP_MACHINE_checkpoint_67_20261124T0108Z_unzipped/ALP_MACHINE/`.

7. **Corrections to the literature and to the archive (ALPOGE_BRIDGES).**
   - **Thakur 2020 (arXiv:2001.00210v1), Prop. 2.9, p. 6, is refuted (BR-15-CLASSBOUND).** The counterexample is a simple
     threefold over F_{2⁹} with Frobenius polynomial (T² − 24T + 512)³ over Q(√−23). It has no isogenous model over
     F₈. This is a correction to report to the source; board A15c.
   - **Grothendieck's 1969 prediction to Kostant (cote 123) fails in sp₄ (BR-12302).** This is known: Richardson 1987,
     Lemma 5.1.
   - **The strict reading of cote 136(b) is false over every nonzero ring (AQ-136-STRICT).**
   - **Checks:** by af2a18f6 (21 Nov), and the Thakur instance computed again tonight.

8. **Connes's trace formula over Q with a prolate cutoff is equivalent to A (ALP_CONNES AC-T51).**
   - **Content:** the statement is Connes's own. The run gives the proof for this cutoff: ⇒ by A through an inverse
     Gram bound; ⇐ by the positivity of the cutoff defect (Matomäki-Shao-Tao-Teräväinen) and the
     Connes-Consani-Marcolli criterion.
   - **Checks:** the deduction checked by afa2696b/af2a18f6. Board H27; the H27 editor (Claude Fable 5.2 at effort max)
     fixed the credit.
   - **Use:** it places A inside Connes's programme. It gives no new zeros.

9. **The cubic rung itself (BEYOND_DIRICHLET Q01, ALP_CONNES Q7, ALP_MACHINE Q3, MOONSHINE Q1): open everywhere.**
   - **Strongest proved reduction (BD-R50-R56):** RH for ζ_{Q(∛269)}/ζ is equivalent to square-root cancellation in a
     balanced two-ideal convolution, for every localized nearly analytic weight.
   - **Support of that convolution:**
     - direct norm < 2(log 3X)²(log log)^κ;
     - product content < 2Y^γ, with γ = 0.28499… from Liu's half-plane Re s > B* = 0.87335… (Hexagon 2611.00421v2,
       not reproved), or γ = 0.24945… under RH for ζ.
   - **What else is known:**
     - the literal "growing CM host" transfer of Alpöge's chain to the cubic character is refuted unconditionally
       (BD-R45; BD-R39/R40 with A);
     - Rankin-Selberg positivity alone allows order-y excess (Q09b);
     - the order-3 phase must commute, not reflect (BD-R06, MOONSHINE CM.001, generalizing ALP_MACHINE S3).
   - **Use:** the next prompt on this rung should start from this gate, not from a new reformulation.

10. **Moonshine L-functions after A (MOONSHINE_AFTER_ALPOGE cp01).**
    - **Shadows:** every umbral shadow in the character basis has L-function 2d(4m/d²)^s L(2s−1, χ), so its zeros in
      the strip lie on Re s = 3/4. I re-derived this.
    - **Mixed components and Niemeier lattices:** mixed components (172 of the 303) and all 24 Niemeier Epstein
      functions have off-line zeros. These are applications of Saias-Weingartner and of Nakamura-Pańkowski 2016, as
      the run says.
    - **Main question:** RH for ψ₃₆, ψ₂₇ and ψ³ over Q(ω) is open.
    - **Use:** marginal so far. This is checkpoint 01, 45 minutes into the run.

---

## ALP_MACHINE (prompt 49; newest return cp67, 24 Nov 01:08 UTC)

**1. Useful or not.** Marginal to useful.
- **The size floors (LIFT54/55):** a theorem about Alpöge's formal interface, and the clearest statement of what a
  literal step 8 would require. Useful to formalizers and to anyone trying to shorten the chain.
- **The coefficient-field theorems (LIFT110, LIFT112):** small, clean algebraic number theory (Kronecker + Schinzel
  + Kummer).
- **The rest:** interface bookkeeping, including the finite signed gate.

**2. What it proved.** Two runs of prompt 49 exist: 20:03 (ids AM-*, last filed cp08) and 19:35 (ids ALP-LIFT,
AM-K/R/DO, cp67).
- **ALP-LIFT-54/55.** Under SizesAt (pinned commit 7cbf…), with x > 1, 0 < ε < 1/52, L = x^ε, the chain length m,
  f = [F:Q] and the initial rank k:
  - x^{1/2−29ε/400} ≤ m ≤ x^{1/2−21ε/400};
  - (log f)² ≤ m/2 − 1;
  - L > 2^300, m > 2^7778, f > 2^33598, k > 2^73197.

  Checks: targeted by abcaba9b against the Lean definitions (22 Nov); re-derived by Claude Fable 5.2 at effort max; a
  Lean 4.33.1 module certifies the numerical part (in NIGHT_AFTER_ALPOGE). The bridge from SizesAt is not compiled.
  Tonight I recomputed the floors.
- **AM-S1-S4 (run 20:03), the phase lemmas.**
  - A reflecting operator (sFs = F⁻¹) bounds nothing.
  - A commuting operator s of order d bounds every eigenvalue through Tr((sF)^{dn}).
  - A formal half-weight variable v = √q gives no reduction.

  Checks: targeted by abcaba9b (22 Nov).
- **AM-LIFT-110 (Theorem A).** Let K be imaginary quadratic with μ(K) = {±1}, F/K finite abelian, and
  J O_F = (ξ) with |σξ|² = N J for all σ. Then [J]² = 1.
- **LIFT112 (Theorem C).** If F/K is Galois, its commutator subgroup surjects onto Hom(G, μ_e).
- **LIFT113.** The optimal coefficient field is CM and metabelian, of relative degree h_K.
- **LIFT083.** A host that is J-isotypic for J = Jac(y² = x⁷ − 1) fails DetCond.

  Checks: LIFT110 and LIFT112 targeted by abcaba9b (23 Nov); LIFT083 and LIFT113 at statement level.
- **R110, LIFT117-120, R108 (cp67).** A supplied complete formal family is rebuilt over the new coefficient ring,
  with constants unchanged and a height shift ≤ 2 log c₀, which SizesAt affords (LIFT118). Statement level, except
  the LIFT118 inequality (abcaba9b).
- **LIFT068-077 (analytic side).** The prescribed bottom period reduces to global Bessel distinction (LIFT074), or to
  a ratio of central values of Ichino-Ikeda/GGP shape (LIFT077). LIFT075 (the direct compact-source lift is killed
  by e0) was checked by abcaba9b, given Mínguez and Gow-Vinroot.

**3. New since the last intake.** Nothing: cp67 is the newest filed and was taken in on 24 Nov (11:52). Follow-up 49b
had still not been taken up at cp67.

**4. Open.**

| Row | Gate |
|---|---|
| Q1 (lift count) | a changed size interface, or a proof that the cost balance forces m → ∞ |
| Q2 (MainX pairing) | the global Bessel distinction (LIFT074) or central-value nonvanishing (LIFT077); the signed gate at support ≥ 31 (DO143) |
| Q3 (Kummer Hecke RH over Q(ω)) | an arithmetic comparison to the ray-theta Mellin period K021 |
| Q4 | PARTLY_PROVED |
| Literal instance | an initial family (source, host, sizes) is not constructed |

**5. Relations.**
- **NIGHT_AFTER_ALPOGE Part B** works Q1 (bounded-length replacement).
- **BEYOND_DIRICHLET** turns ALP_MACHINE's size floor into a theorem about CM hosts over Q(ω):
  - BD-R45: every literal host has no odd prime-ideal norm up to 2x, unconditionally;
  - BD-R39/R40: the exact cubic transfer forces a large root discriminant, using A.
- **MOONSHINE CM.001** generalizes S3 to a finite group normalized by F.
- **Prompt 97** cites S1-S4 and LIFT110-113. LIFT110-113 are vacuous over Q(ω).
- **Grothendieck:** the coefficient-field results are statements about CM motives and their fields of definition
  (motives with coefficients, Kronecker's theorem on units).

**6. Candidates.**
- Board H30 (the size floors), for a note.
- Board H30b (LIFT110 + LIFT112-113), gated on a literature search and on reading Theorems A and C in full.
- Next prompt: the finishing prompt for 49 should say "LIFT110-113 fix the coefficient field; R110/LIFT117-120 carry
  a supplied family; the initial family is missing".

**7. Problems.**
- R109 is a duplicate, refuted by the run itself.
- No other problem found by any intake.
- The theorem is about the interface, not about Alpöge's mathematics. Any note must say so (primer §1, "Scope").

## ALP_CONNES (prompt 55, follow-up 55b; newest return cp44, 23 Nov 12:26 UTC)

**1. Useful or not.** Useful for AC-T51, as the exact form of Connes's programme that A now proves, and for the cubic
K-groups (now Paper I of BEYOND_DIRICHLET). Marginal for the G-series budget lemmas, which are internal to the cubic
gate.

**2. What it proved.**
- **AC-T51** (`modules/trace_unconditional_converse.tex` 301-401). A holds iff the prolate-cutoff trace limit
  2 log Λ · h(1,1) − Tr(Q_Λ R(h)) + ∫h₁(r)(r^{−1/2} + r^{1/2}) d*r tends to W(h) for every Bruhat test h.
  - Checks: the deduction checked by af2a18f6, given T25-T43 and T47-T48.
  - Credit: the statement is Connes's (H27 editor, Claude Fable 5.2 at effort max); the proof for this cutoff is
    ours.
- **S50.** Real-rooted prime-built approximants P_N → Ξ/Ξ(0), with multiplicities. Checked; it is a direct
  consequence of Suzuki, arXiv:2610.32704.
- **AC-G22 and K10-K23.** K_{2e}(O_E)_(3) ≅ Z₃[ω]/λ^κ, with κ = 5 + 2v₃(e) + [e ≡ 2 mod 3].
- **AC-K09.** The Weil form of the cubic L-function is at least the squared norm on [−log t, log t] for 1 < t ≤ 4.
  The margin was recomputed as 1.282.
- **AC-G219.** In the matched coefficient-7 family, S₇ ≅ O/7^{s(e)} with s(e) ≥ 1, and s = 1 for 7 | e.
  - Checks: steps 1-5 by targeted check (afa2696b), given the PARI certificate Cl(L) ≅ C₇².
  - Tonight: compared with BD-R20, which settles it (s(e) = 1 for all e).
- **G209-G218 and G220.** Run checks only.

**3. New since the last intake.** No newer return. **Settled since, by another run:** BEYOND_DIRICHLET's BD-R20
proves s(e) = 1 at every weight. The open maximum of G219/G220 is closed. BD-K13 confirms Cl(L) = C₇² in a second
system: sympy ideal relations, the analytic class-number formula in Arb, and an S₃ regulator argument.

**4. Open.**

| Row | Gate |
|---|---|
| Q1 | identify the positive defect limit with W without zero location |
| Q3/Q4 | a quantitative estimate on the actual Weil operator (the ratio, the odd gap, or a₂ ≳ λ^α e^{−4πλ²} with α ≤ 4) |
| Q7 / EB-Q02 (cubic RH) | the remaining mixed and noncritical budget terms after G220, then H04.4 |

**5. Relations.**
- **BEYOND_DIRICHLET** inherited the cubic gate and the K-groups (Paper I).
- **ALP_MACHINE** AM-H04 is the window form H04.4.
- **MAS_ARTIN** HM-003 says which narrow-trace statement is RH.
- **Literature:** Connes 1999 (Theorem 5 in positive characteristic only); Connes-Consani-Marcolli Prop. 6.2/Cor. 6.3;
  Matomäki-Shao-Tao-Teräväinen; Soulé (finiteness); Belabas-Jaulent (logarithmic classes).
- **Grothendieck:** K-theory of rings of integers and its Selmer (motivic) description; Deninger via Morishita
  (T15/T17: the mapping-torus fibre is a solenoid).

**6. Candidates.**
- **Board AC219 must be rewritten.** BD-R20 supersedes it: S₇ = O/7O at every weight, and the 7-adic module is
  Λ/(7,T). The board row still says "at most one class".
- Board H27 stands.

**7. Problems.**
- Superseded: G219's "at most one exceptional residue" is true but not sharp. The exceptional set is empty (BD-R20).
- No error found.

## NIGHT_AFTER_ALPOGE (prompt 75; newest return cp13, 23 Nov 11:54 UTC)

**1. Useful or not.** Useful: it holds the cluster's two strongest theorems (C.IHARA, A.ORBIT). Part B is internal.

**2. What it proved.**
- **C.IHARA**, statement in item 1 above.
  - Proof outline:
    1. Hain-Matsumoto density and Brown's freeness give the rational image.
    2. Greenberg and Wake-Wang-Erickson give the plus parts; Fukaya-Kato give cup generation.
    3. The cup comparison (Lemma 4.1).
    4. Pole separation in a Magnus expansion (Lemma 5.1).
    5. Vandiver gives X⁺ = 0 (Lemma 7.1).
    6. Hart-Harvey-Ong verify Vandiver below 2³¹.
  - Checks: every step by ad855737 (21-23 Nov); Lemma 7.1 re-proved by me tonight.
- **A.ORBIT** (Theorem 1.1, `workbench/schemes-and-moduli-workbench/papers/cm-orbits/main.tex`):
  |Gal·x| ≥ D_x^{1/(2g)}/(s_g C_g W_g log D_x) ≥ c_g D_x^{1/(4g)}.
  - Inputs: A, in the form (1.1), excluding a Stark exceptional zero via imaginary quadratic subfields; the averaged
    Colmez formula; Gaudron-Rémond 2023; Tsimerman's level-3 descent.
  - Checks: every step by ad855737, constants recomputed.
- **A.SURFACE_D.** A rational CM point of A₂ has D < 10^80.
- **C.K12/K80.** K_{4k}(Z) = 0 for 1 ≤ k ≤ 20, given the archive theorem OneCharU_s.
  - Checks: K₁₂ in full and the classical halves by ad855737; the unitary halves are carried. Board H18.
- **Part B** (theta chain, 325 pp.). The size theorem of ALP_MACHINE, with a Lean certificate of its numerical part.
  - At flag rank 0 and m = 2: B.ZERO_GRAM_IDENTITY and B.CLASS_NUMBER_TERMINAL, every step confirmed by ad855737.
  - 22 further lemmas at statement level.

**3. New since the last intake.** Nothing: cp13 is the newest filed and was taken in on 23 Nov.

**4. Open.**

| Row | Gate |
|---|---|
| B-Q1 (bounded-length replacement) | signed joint theta-jet/period/column contents; a fixed primitive finite-word period detector; the bounded-length arithmetic host; pointwise suppliers; a loop wrapper that still assumes m ≥ 4 |
| B-Q2 (Kummer characters over Q(ω)) | open |
| C-Q1 (Vandiver at every prime), C-Q3 (Ihara without hypotheses) | queued |
| A-Q2 (full nonsimple rational-model list) | open |

**5. Relations.**
- ALP_MACHINE Q1 (Part B is its follow-up).
- KTOWER and K17 (C.K12).
- The H15, H06b and H18 notes.
- **Literature:** Sharifi 2019; Jaswal (Hexagon 2611.00339); Cureton-Thorner (Hexagon 2610.00200); Pintar
  (Hexagon 2611.00829, k ≤ 26 under stronger hypotheses, which does not supersede C.K12).
- **Grothendieck:** the Galois action on π₁(P¹ − 3 points) (Esquisse, GT̂), and K-groups of Z as motivic cohomology.

**6. Candidates.**
- H15 (A.ORBIT) awaits the user's word.
- H06b: three fix-ups of the posted text (the abstract's "earlier versions"; the Sharifi Lemma 4 numbering of arXiv
  v2; the Sharifi 2019 quote).
- Next prompt: Part C (Vandiver at every prime; Ihara without hypotheses) when Part B stops.

**7. Problems.** None found. A.AO (effective André-Oort) is Jaswal plus Cureton-Thorner, cited and not claimed,
correctly.

## ALPOGE_BRIDGES (prompt 22; final = cp09, 21 Nov 05:46 UTC)

**1. Useful or not.**
- **Useful for its corrections:** Thakur Prop. 2.9 refuted; Grothendieck's Kostant prediction false, though known
  (Richardson); cote 136(b), strict reading, false.
- **Marginal for the bridges:** RH for Artin-Tate motives with abelian Artin part follows from A (BR-AT-01); B ≥ 0
  for Ξ (BR-TR-01). These are direct consequences of A.

**2. What it proved.**
- **BR-AT-01.** L(⊕(χ ⊗ Q(n))^m, s) = ∏L(χ, s+n)^m, with zeros on Re s = 1/2 − n, given A. Confirmed by
  af2a18f6.
- **BR-TR-01.** Ξ(√w)/Ξ(0) = det(I − wB) with B trace class; RH ⇔ B ≥ 0. Confirmed.
- **BR-WM-01, BR-ANA-01, BR-MIX-01.** Counterexamples to over-readings (a Frobenius determinant does not give
  monodromy purity; P¹ minus four points; the Kummer motive K(2)). Confirmed.
- **BR-12302.** In sp₄, rank dχ_N = 1 = r − 1 at an orbit of dimension 6, contrary to Grothendieck's "strictly
  smaller". Confirmed by hand and sympy; known (Richardson 1987, §5, Lemma 5.1, p. 234).
- **AQ-136-STRICT.** The equalizer requirement (b) of cote 136 is false over every nonzero ring. Confirmed.
- **CC-APG04.** An Out(G)-invariant class of apposition quadruples exists iff the type is not A_{2m}. The existence
  direction is confirmed.
- **BR-15-CLASSBOUND.** Refutes Thakur 2020, Prop. 2.9. The counterexample is confirmed by af2a18f6, and recomputed
  tonight: γ = 12 − 4√−23 is not a cube in O_K. The Honda-Tate index step is at statement level.
- **F-SM-19.** Masullo's printed orbital indentation (11.3.2.2) is identically zero, so his Theorem 11.3.2.1 fails
  literally. Confirmed against the PDF, p. 495.
- **CC-F01/F01b.** Borger Λ-schemes have abelian ℓ-adic cohomology. Statement level, base corrected to Spec Z[1/p].

**3. New since the last intake.** No newer return. **Settled since, by another run:** BEYOND_DIRICHLET BD-R83 proves
the Borger statement over finite localizations Z[1/N]. It refutes the unrestricted wording BD-R01: over Q, identity
Frobenius lifts make the conditions vacuous, and Spec E gives non-abelian H⁰. This fixes the scope of CC-F01.

**4. Open.**
- Cote 136: connectedness over Z, and the homotopy reading of «'égalise'».
- Cote 134-8: surjectivity in degrees ≥ 2.
- Cote 15: the general forward-cycle gate (≈ full Tate).
- R-MAS-KERNEL, which is equivalent to RH (MAS_ARTIN HM-003).

**5. Relations.**
- Core 50 / ARCH_ALG carries cotes 136, 134-8, 15 and 123.
- MAS_ARTIN took over R-MAS-KERNEL.
- BEYOND_DIRICHLET Q04 (Borger).
- GRH_NIGHT MT-M36 (the same Masullo defect, found independently).
- **Grothendieck:** cotes 123, 136, 134-8, 15 and 14 are named by the run itself. Also motives over F_p (Honda-Tate)
  and Λ-rings (Borger).

**6. Candidates.**
- **A correction to report to Thakur** (arXiv:2001.00210v1, Prop. 2.9), with the explicit threefold. Board A15c.
- An archive note for H08 (Richardson credited).

**7. Problems.** None open. Our own first gloss of F01b was wrong and was corrected (base Spec Z[1/p]); BD-R83 now
gives the exact scope.

## CX_GRH (prompt 28; final 21 Nov 00:05 UTC)

**1. Useful or not.** Useful. It is the exact list of what A makes unconditional in computational number theory and
in Koiran's Nullstellensatz. The algorithms are classical; the accounting of which L-function each one needs is new
and correct.

**2. What it proved** (line numbers in `CX_GRH.tex`).
- **CX-R01 (163-192).** A gives RH for every abelian ζ_K.
- **CX-R02.** A alone does not reach ζ of a non-normal cubic field.
- **CX-K01 (339-431).** Koiran's analytic input needs only RH for ζ_E, E the field of his bounded solution. The tool
  is Lagarias-Odlyzko Thm 1.1 for E/E.
- **CX-K03.** Under A, the promise problem with bounded abelian witnesses is in AM.
- **CX-K05.** Under M (unproved), an h.s.o.p. for GCT V is in FP^{Σ₂P}.
- **CX-N01-N04 (793-901), from A alone:**
  - Miller-Bach deterministic primality;
  - r-th nonresidues in F_p;
  - primitive roots given the factorization of p−1;
  - Shoup's candidate list.
- **CX-N13 (1386-1480).** r-th nonresidues in a supplied F_{p^m} in poly(m log p), under A. Unconditional for r = 2,
  m even (BIMS17).
- **CX-N14.** Zero divisors in split algebras. Case (ii) uses A; case (iii) is unconditional; the counterexample
  p = 17, r = 3 was checked.
- **CX-N11 and CX-N15** need M (RH for ζ_{Q(ζ_{2n}, p^{1/n})}): they are not unconditional.
- **CX-E01-E08** use OpenAI's ETH preprint as an input.

**Checks:** 21 of 39 findings confirmed step by step by af2a18f6 (21 Nov); 18 at statement level; no gaps. Tonight
I checked the whole proof of CX-N13.

**3. New since the last intake.** Nothing (final; intake of 21 Nov).

**4. Open.** CX-U01-U06, the run's unproved extensions. Above all, deterministic factorization over F_q
unconditionally (CX-N15 needs Kummer-field RH, beyond A). BEYOND_DIRICHLET Q09i states the exact gain if cubic RH were
proved (BD-R22-R24).

**5. Relations.**
- GRH_ALGORITHMS (prompt 67) and board H29 continue it.
- BEYOND_DIRICHLET BD-R23: a Nullstellensatz problem with pure-cubic solution fields is unconditionally in AM, under
  bit-size promises.
- GRH_NIGHT CX-ALG-016-028.
- **Literature:** Bach 1990 Thm 2; Schoof 2008 Thm 2.2; Shoup; Bach-Sorenson Thm 5.1; Adleman-Lenstra;
  Bach-von zur Gathen-Lenstra; IKRS; Koiran; GCT V Thm 3.4.
- **Grothendieck:** zeta functions of schemes over Z (ζ_E as the zeta of Spec O_E), and finite-monodromy sheaves of
  weight 0 (CX-G06).

**6. Candidates.** A short Hexagon note, "Algorithms made unconditional by Alpöge's theorem", if H29 does not already
cover it. Compare first with the H29 row (GRH_ALGORITHMS), which overlaps.

**7. Problems.**
- None found.
- Wording to watch: CX-K02/K05/N11/N15 depend on M, which is not a theorem. Any write-up must keep them conditional.

## MAS_ARTIN (prompt 48; newest return cp15, 22 Nov 02:46 UTC)

**1. Useful or not.** Useful for MA-FQ-004 (Artin in Calegari's S₅ family from one real-zero hypothesis), now
superseded by BEYOND_DIRICHLET Paper II's stronger form. MA-HM-003 is a clean negative: the narrow-strip trace
statement is RH itself, so the narrow-trace route cannot avoid zero location.

**2. What it proved.**
- **MA-HM-001/003.** In the run's Meyer-type model, convolution factors through i_{1/2} for every width iff RH for
  that function. Checked by af2a18f6, given MT-M18/M26.
- **MA-JP-004.** A positive divisor's causal trace vanishes iff the divisor is empty. Checked.
- **MA-FT-002.** The slow-band agreement is equivalent to vanishing upper deficiency, i.e. RH. Checked, given FT-001.
- **MA-S5-001, MA-S5-004, MA-LD-001, MA-FQ-001-003, MA-FQ-004.** Under (R_B), meaning that B has no real zero in
  (0,1) other than 1/2, the comparison is exact at every place and the nontrivial Artin factors are automorphic and
  entire. Checked by af2a18f6, given Calegari Lemmas 4.8-4.10, Booker 2015, and Sanders 2020 Thm 12.3.
  Tonight I rechecked the exceptional-prime quotient.

**3. New since the last intake.** No newer return. **Settled since, by another run:** BEYOND_DIRICHLET Paper II
(BD-S23-S26) weakens (R_B) in three ways:
- to the absence of common off-central real zeros of B and C;
- it drops the condition at 5 via Pilloni-Stroh;
- it proves (R_B) outright for four fields.

**4. Open.**

| Row | Gate |
|---|---|
| (R_B) removal | now BD Q02: common real zeros of B and C at a possible pole α ∈ (1/2, B*] |
| The narrow step over Q | it is RH (HM-003); using A there is circular for an independent method |
| Non-induced Hecke characters | the character's own RH |

**5. Relations.**
- BEYOND_DIRICHLET Paper II.
- ALPOGE_BRIDGES R-MAS-KERNEL.
- ALP_CONNES (through HM-003).
- The Masullo defect table.
- **Literature:** Calegari, Math. Ann. 356 (2013); Booker, Math. Ann. 363 (2015); Sanders 2020 (Cohen's theorem).
- **Grothendieck:** Artin motives and their L-functions; weights (the comparison is pure of weight 0).

**6. Candidates.** The S₅ paper should go out as BEYOND_DIRICHLET Paper II, not as MAS_ARTIN's seed Paper 1. Retire
the seed's Paper 1 or merge it.

**7. Problems.**
- Our own intake corrections stand (cp15 intake §3): Stark's lemma does not give (R_B) from A; cubic RH would not make
  Dunn-Radziwiłł unconditional.

## BEYOND_DIRICHLET (prompt 69; newest return cp10, 24 Nov 20:10 UTC; NO EARLIER INTAKE)

The run began at 12:39 UTC on 24 Nov. Reviews 01-04 recorded movement; review 05 (19:39) recorded NO, counter 1.
**The review at 20:39 decides whether research stops.** It comes after this checkpoint, so the final is still
outstanding. 17 papers; both main papers are 43 pp. Records: STATEMENTS.tsv (164 rows), QUESTIONS.tsv (34 rows), and
CHECK_EVENTS.tsv (354 events: 218 targeted checks, 82 same-model statement-only re-proofs, 33 computations, 3
refutations with refined statements).

**1. Useful or not.** Useful.
- **Paper II:** a genuinely weaker hypothesis for Artin's conjecture in an enlarged Calegari family, plus four
  certified fields.
- **Paper I:** an every-degree K-group computation for a non-abelian field, and an exact Iwasawa module.
- **The cubic-RH research:** marginal. It is a long sequence of honest reductions; RH is not proved.

**2. What it proved.**
- **Paper II, Theorem 1.1 (BD-S25, BD-S26)** (`papers/paper_II/main.tex` l. 76-108). For L/Q with group S₅ and complex
  conjugation of type (12)(34), with no condition at 5:
  - unconditionally, a pole of order r of the comparison quotient M at z (0 < Re z < 1) gives
    r ≤ min(ord_z B, ord_z C);
  - if (B(σ), C(σ)) ≠ (0,0) for real σ ∈ (0,1), σ ≠ 1/2, then the local factors of π and ρ₅ agree at every place.
    L(π) = L(ρ₅), and every nontrivial irreducible S₅ Artin L-function is entire and automorphic. Moreover
    ord_{1/2} B = ord L(η) + ord L(ρ₅).
  - Checks: the run's author proof, a separate statement-only re-proof, and a root audit. Mine tonight: a targeted
    check of the common-pole step (Prop. 3.x, l. 334-405), given Belt Thm 6.2 and Calegari.
- **BD-S23 (Prop. scopeupgrade).** Pilloni-Stroh, Théorème 0.3, makes Calegari's construction work without the
  condition at 5.
  - It is known: Kharel-Larosa-Wiese Thm 1.2, §4.2, and Dwyer 2014 observed that the condition at 5 is superfluous.
    The paper says so.
- **BD-S12, S14, S15, S16.** Real nonvanishing of B on (0,1), the centre included, for the splitting fields of:
  - x⁵ − 2x⁴ − x³ + 4x + 1 (disc 8249);
  - x⁵ + 2x³ + 2x² − 2x + 1 (disc 60061);
  - a discriminant-30301 quintic, certified by a positive autocorrelation test;
  - x⁵ − 2x³ + x + 2 (disc 48976), with wild conductor 2⁶·3061³ derived.

  Hence Artin's conjecture holds unconditionally for these four S₅-extensions.
  - Run checks: MPFR (160-bit) and Arb (192-bit) interval certificates; for 8249, also a statement-only re-proof.
  - My check tonight: an independent recomputation of 8249 and 60061 with my own trace code (mpmath, 40 digits,
    floating point, not interval arithmetic). I re-derived the explicit-formula constant and kernel. The values are:

    | disc | C | P₈ | S₈ | 2H₈(0) | margin |
    |---|---|---|---|---|---|
    | 8249 | 1.1036 | 0.5268 | 8.0738 | 8.9758 | 0.90 |
    | 60061 | 7.0594 | 5.7099 | 8.8465 | 8.9758 | 0.13 |

    Both are inside the paper's enclosures.
- **BD-S27/S28.** A weak GL₁₀ Sym² or GL₉ Asai transfer exists iff ρ₅ is weakly automorphic. Statement-only re-proof
  by the run.
- **BD-S29.** The third zero condition (ζ_T) is subsumed. **BD-S17-S22:** method limits and countermodels for the
  off-central case.
- **Paper I, Theorem 1.1 (BD-K01)** (`papers/paper_I/main.tex` l. 100-122). For e ≥ 1:
  - K_{2e}(O_E)_(3) ≅ O/λ^{κ_e} and S_e ≅ O/λ^{m_e}, with m_e = 4 + [e≡2(3)];
  - Cl(E)_(3) = 0 and S₀ = 0;
  - Σ_{e≤N} len S_e = 4N + ⌊(N+1)/3⌋.

  The shorter proof reduces to the genus quotient F₃[T]/T⁷ (BD-K07/K17) and the first logarithmic layer
  C₉² × C₃² (BD-K16). Checks: the run's full statement-only reconstruction; earlier deduction checks by afa2696b.
- **Seven-primary supplement (BD-R19, R20, R21, R27-R29).**
  - **The theorem:** A(F_n) ≅ Z/7 for all n, where F = Q(∛269) and F_n runs up its cyclotomic Z₇-tower. Hence
    (lim A(E_n))^χ ≅ Λ/(7,T) and Sel_str(K, D_{χ,κ}) ≅ O/(7, u−1).
  - **The finite inputs:** h₇ of F and of F₁ (degree 21), certified by interval isolation of the class-number
    formula, Friedman's regulator bound and residue characters.
  - **The refutation it carries (BD-R29):** the one-prime characteristic generator T − a has v₇(a) = 1 and unbounded
    weight valuations, so it does not give strict lengths. This refutes the bare Katz-generator formula of Q09e.
  - **Checks:** the run's two exact implementations. Mine tonight: a targeted check of the descent steps, given the
    finite inputs, which I did not replay.
- **BD-R83** (supersedes BD-R01, refuted by the run). Over Z[1/N], the Tate-normalized cohomologies of smooth proper
  Borger Λ-schemes generate exactly the finite abelian Q_ℓ-representations, and odd cohomology vanishes.
  - It uses Borger's finite-inversion theorem and purity. Checks: the run's targeted check; the statement-only check
    is in progress.
- **BD-R04 (Q09d, refuted then corrected).** No exact unit-phase projector for n ≥ 2, even rationally. Denominator 3
  at n = 1.
- **BD-R30-R32.** The completed faithful quartic Hecke function over Q(i), and the cubic one over Q(√−23), are positive
  on the real axis. For p ≡ 5 mod 8 all faithful quartic strict cyclotomic Selmer groups vanish.
- **BD-R09, R18, R22-R24.** Kummer auxiliary witnesses. A uniform zero-free β gives an auxiliary prime
  O(log^{1/(1−β)}(3p)). Gaussian periods construct a cubic over F_p deterministically.
- **Cubic RH reductions (BD-R25, R26, R34-R36, R42-R44, R49-R56, R69-R82).** Summarized in item 9 above. Each has the
  run's own checks.
- **Host-transfer obstructions (BD-R38-R41, R45-R48, R57-R61).**
  - BD-R45, unconditional: every literal host has no odd prime-ideal norm up to 2x, and NoGain is false.
  - BD-R39/R40/R46, using A: the exact normalized cubic transfer on a proper abelian host forces
    log rd ≥ c√x, incompatible with the literal sizes.

**3. New since the last intake.** Everything; there was no earlier intake. Prompt 69 carried ALP_CONNES cp44,
ALP_MACHINE cp55, and MAS_ARTIN cp15.

**4. Open** (QUESTIONS.tsv at cp10).

| Row | Gate |
|---|---|
| Q01 (cubic RH) | square-root cancellation, for every localized weight, in the balanced fixed-269 two-ideal sum with product content < 2Y^γ, γ = 0.28499… (Liu B*) or 0.24945… (RH for ζ) |
| Q01a | the surviving signed primitive bulk; the weighted double residues keep exponent 0.50654 |
| Q01b | uniform elliptic-unit index bounds over growing host characters |
| Q01c | a coherent equivariant theta realization of the fixed four-factor quotient (the literal route is refuted) |
| Q02 (general S₅) | common real zeros of B and C at a possible α ∈ (1/2, B*]. Boundary positive-definiteness controls only the outer line |
| Q03, Q03a, Q06, Q07, Q08e, Q08f | proved reductions, estimates open |
| Q09f | uniformity in the radicand |
| Q09h | P145's exact hypotheses are not attached |
| Q09k | prompt 68's positivity half is not attached |

**5. Relations.**
- **ALP_CONNES:** BD-R20 closes the G219/G220 maximum; BD-K13 is a second-system class group for G219.
- **MAS_ARTIN:** Paper II strengthens MA-FQ-004.
- **ALP_MACHINE:** BD-R45 and R39/R40 are host-side consequences of LIFT054/55; BD-R06 is the phase lemma, with
  balanced counterexamples.
- **ALPOGE_BRIDGES:** BD-R83 fixes CC-F01's scope.
- **CX_GRH:** BD-R22-R24 continue CX-K01 and N11.
- **MOONSHINE:** the order-3 phase, from the other side.
- **Literature:**
  - Calegari, Math. Ann. 356 (2013), Thms 1.1-1.2, Lemmas 4.8-4.10, Thms 5.1, 5.3;
  - Pilloni-Stroh, Astérisque 382, Thm 0.3; Dwyer, BLMS 46 (2014); Miller, Duke 112 (2002), Lemma 3.1;
    Booker 2006, eq. (3-1); Belt Thm 6.2; Kim 1999 Thm 3.5;
  - Fukuda 1994 Thm 1(1); Friedman 1989 Thm B; Schneider 1979; Jaulent-Michel 2006; Belabas-Jaulent 2016;
  - Borger, Thm 0.1 and Cor. 6.2;
  - Liu, Hexagon 2611.00421v2, Thms 1.1-1.2 and 8.29 (B* = 0.873345856…); OpenAI quasi-RH, 30 Sep 2026, Thm 1.1
    (Re s > 7/8 over Q(√−3)); Heath-Brown's identity.
- **Grothendieck:**
  - K-theory of O_E and its étale/Selmer description (Paper I);
  - Λ-rings and F₁ in Borger's sense (BD-R83: Tate-normalized Borger cohomology is the abelian Artin-Tate
    category, which is exactly why A covers it);
  - Artin motives of S₅-fields;
  - SGA 4 XII 5.1/5.2, kept distinct (Q05c).

**6. Candidates.**
- **A Hexagon note from Paper II**, after two steps:
  1. open Dwyer 2014's list and compare the four fields;
  2. replay one interval certificate in a second system on our side (my floating-point recomputation agrees but is
     not an interval certificate).
- **A Hexagon note from Paper I with its supplement**, after a replay of the class numbers of F and F₁ in PARI or
  Magma.
- **Board updates:** AC219 → "S₇ = O/7O at every weight (BD-R20)"; a new row for the S₅ common-zero theorem.
- **Next prompt:** the cubic gate as BD-R56 states it, with the instruction not to count further support
  reformulations as movement. The run's own review 05 already says this.

**7. Problems.**
- **Dwyer 2014 not opened** (LITERATURE.md l. 17: "abstract/metadata only; no individual Dwyer field certificate
  opened"). The novelty of the four explicit fields, and the paper's sentence at l. 648 that the approach "is
  established in Dwyer", leave it open whether 8249 and the others are already in his tables.
- **BD-R39, R40, R46** carry the status "proved conditional on Dirichlet GRH" (STATEMENTS.tsv l. 114-121). The
  research text itself says this is "the degree-one input of Alpöge's theorem" (`research/cubic_cm_hosts.tex` l. 64).
  With A these are unconditional, so the register undersells them; the papers should cite A.
- **Liu's B*** (Hexagon 2611.00421v2, 101 pp.; the source records AI-assisted writing and an in-progress Lean
  formalization) is an unverified external input. It enters only the γ = 0.28499 and the α ≤ B* refinements, not the
  main theorems; the run says so.
- **The 60061 certificate** has margin 0.13 against a total of about 8.85, comfortable for 160-bit interval
  arithmetic but the smallest of the four.
- **Run state:** the final ZIP is not yet filed. The papers' final all-page QA, deposit sheets and provenance are
  recorded as outstanding (CHECKPOINT.md).

## MOONSHINE_AFTER_ALPOGE (prompt 97; newest return cp01, 24 Nov 20:45 UTC; NO EARLIER INTAKE)

The run began at about 20:00 UTC on 24 Nov. cp01 is a working checkpoint, not a delivery: no timed review has occurred.
Two drafts: the main paper `MO/workbench/work/moonshine/v1/paper/main.tex` (about 2600 lines over its parts) and the
companion `MO/workbench/work/cm_hecke/v1/paper/cm_hecke_windows.tex` (12 pp.). Every row of both STATEMENTS.tsv files
is marked "unchecked", while CHECK_EVENTS.tsv holds 74 events (31 same-model re-proofs, 22 targeted checks, 13
computations, 2 refutations).

**1. Useful or not.** Marginal so far.
- The main question is open.
- The satellite theorems are correct applications of known theorems (Saias-Weingartner; Nakamura-Pańkowski;
  Ogg 1974; Tunnell; Cheng-Duncan-Mertens) to moonshine objects, with careful normalizations.
- The most useful pieces:
  - the clean statement of which moonshine L-functions A covers (shadow character components: zeros on Re s = 3/4);
  - the normalization corrections: the cusp shift and the factor 2 in Tunnell against Cheng-Duncan-Mertens
    eq. (4.2.9), with C_φ(−3) = 1 and a(3) = 2.

**2. What it proved** (ids PENDING-MOONSHINE.nnn and PENDING-CM.nnn; all "unchecked" in the register, with
same-model re-proofs in CHECK_EVENTS).
- **MOONSHINE.001/004 (shadows.tex).** For m ≥ 2, d | 2m, χ odd mod 2m/d:
  L(Σ_r χ(r) S_{m,dr}, s) = 2d(4m/d²)^s L(2s−1, χ). Every shadow component of every lambency, twinings included, is a
  finite combination of these. With A, zeros in the strip lie on Re s = 3/4. **Re-derived by me tonight.**
- **MOONSHINE.005/006/008.** A component mixing two or more primitive characters has infinitely many zeros off
  Re s = 3/4 (Saias-Weingartner 2009). L(S^X₁, s) = 24^s{3(1+3^{1−2s})L(2s−1, χ₋₄) + 2(1+2^{1−2s})L(2s−1, χ₋₃)} has
  off-line zeros. Of the 303 components: 92 vanish, 39 are single-character, and 172 mix.
- **MOONSHINE.009 (niemeier_zeros.tex).** For every Niemeier lattice L and 23/2 < α < β < 12, the number of zeros of
  Z_L(w) with α < Re w < β and 0 < Im w < T is ≍ T, because N₂(L) − 65520/691 ≠ 0. This is Nakamura-Pańkowski 2016,
  Main Thm 1, applied (credited).
- **MOONSHINE.010-012.** The Erdős-Straus residue group S = ⟨289⟩ ⊂ (Z/840)^× gives the Frame shapes d^{24/d} and the
  eta products η(dτ)^{24/d}; the residue symbol κ(r) = (r/5)₄(r/π)₃; ψ₃₆³ = ψ₂₇³ = Ψ with conductor 𝔭.
- **MOONSHINE.014-016.** Theta coordinates of the 129 isotropic planes: 18 distinct series. The six-cycle c preserves
  J, with an order-2 stabilizer on each Leech neighbour. The full C₆ action on a Leech extension is refuted
  (LAT-LEECH-FULL-ACTION).
- **MOONSHINE.017.** The weight-one eta products of M₂₄ (η(τ)η(23τ), η(3τ)η(21τ), η(12τ)²) and of Co₀ (five
  cuspidal, 23 Eisenstein).
- **MOONSHINE.020-026.** Fricke glue constants; a degree-2 isogeny at the cusp of X₀(6); CM zeros of Niemeier theta
  series only for E₈³ and D₁₆E₈ at the orbit of ρ; Ogg's equality r(p) = s(p) exactly at the supersingular primes, with
  unconditional cutoff 7000 and cutoff 4300 under A (which is Dirichlet RH, so 4300 is now unconditional); M₁₁
  multiplicities as class numbers; the Tunnell factor 2.
- **CM.001.** If F normalizes a finite Γ ⊂ GL(V), then (sF)^{he} = F^{he}, so finite phases drop out of power-sum
  bounds. It generalizes ALP_MACHINE S3.
- **CM.002/003.** Alpöge's abstract one-sided window criterion applies to every positive combination of unitary Hecke
  characters of an imaginary quadratic field with nonzero angular type. One window inequality for G_{λ₁} + G_{λ₂} +
  G_{λ₃} would give RH for 36a1, 27a, their common cube, and the symmetric cube of η(6τ)⁴.
- **CM.007.** These cannot be a fixed finite combination of Dirichlet logarithmic derivatives.
- **CM-UMBRAL-CENTRE (refuted).** The centre of GL₂(F₃) is {±I}, so it supplies no cubic operator.

**3. New since the last intake.** Everything; there was no earlier intake.

**4. Open.**

| Row | Gate |
|---|---|
| Q1 (RH for ψ₃₆, ψ₂₇, ψ³ over Q(ω)) | a centred prime-ideal window inequality, or another global numerator estimate. Tried: varying-modulus Fourier (loses a half power); the shifted type-±12 auxiliary factor (conditional iteration has a 3/5 barrier); signed diagonal correlations of cubic Gauss sums (individual bounds give only order X) |
| Q2 | the Niemeier zeros with Re w > 12 |
| Alpöge's step-18 lattice | growing rank; not a fixed Niemeier lattice |

**5. Relations.**
- ALP_MACHINE S1-S4 (CM.001 generalizes S3).
- BEYOND_DIRICHLET, which takes the finite-order cubic characters, while this run takes the positive infinity type.
  The two runs share the eta-product list (prompt 69, item 9).
- NIGHT_AFTER_ALPOGE B-Q2.
- The S6 papers (J, 129 planes), but the S6 series is another session's.
- **Literature:** Saias-Weingartner 2009; Nakamura-Pańkowski 2016; Ogg 1974; Tunnell 1983; Cheng-Duncan-Mertens,
  JNT 277 (2025); Cheng-Duncan-Harvey 2014; Dunn-Radziwiłł; Diamantis-Lee-Raji-Rolen; Bilu-Luca-Masser; OpenAI quasi-RH.
- **Grothendieck:** CM motives of y² = x³ + 1 and y² = x³ + 16 and their Hecke characters (motives with
  coefficients); weights (Re s = 3/4 is the weight-1/2 line of a weight-3/2 theta series).

**6. Candidates.**
- None for Hexagon yet.
- Perhaps a note to Cheng-Duncan-Mertens on the factor 2 and the cusp shift, if the run confirms these are errors in
  their text and not only a difference of normalization. Its own words are "a factor between the two normalizations,
  not a change to Tunnell's definition". So probably no correction is owed; ask the next intake to settle it.

**7. Problems.**
- The register says "unchecked" for statements that have same-model re-proofs. To be synchronized by the run.
- MOONSHINE.023's "under the Dirichlet Riemann hypothesis" is A, so the 4300 cutoff is unconditional now.

---

## For the conference: what to do with this cluster

1. **Post or finish:** H15 (A.ORBIT) and the H06b fix-ups. These are the two finished, checked theorems.
2. **Gate the S₅ result** (BEYOND_DIRICHLET Paper II, superseding MAS_ARTIN's Paper 1): open Dwyer 2014, and replay
   one interval certificate. It could then become the third posting of the cluster.
3. **Update board AC219** to s(e) = 1 (BD-R20), and add the Thakur correction (A15c) to the corrections to report.
4. **Wait for the finals of BEYOND_DIRICHLET and MOONSHINE**, and send nothing new on the cubic rung until one of them
   produces an estimate rather than a reformulation. The four runs on the rung (ALP_CONNES Q7, ALP_MACHINE Q3,
   BEYOND_DIRICHLET Q01, MOONSHINE Q1) all stop at the same kind of gate: a one-sided or square-root prime-sum
   estimate for a non-abelian character.
