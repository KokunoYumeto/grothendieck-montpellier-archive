# Implications of the mathematics that came back, 20-21 November 2026

Drafted by Claude (Claude Opus 5.5 at effort high) for the main session (Claude Opus 5.5 at effort max), 21 Nov 2026,
from the intakes listed in section 0. It draws on the intakes and on Fable's notes. Nothing in it was re-proved for this
report. Where a statement is called confirmed, the check is the intake's (Claude Opus 5.5 at effort high in every intake
named here), and the kind of check is given.

**Conventions.**
- **A** is Alpöge's RH and GRH for Dirichlet L-functions (*Remark*, alpo.ge/remark.pdf, 20 Nov 2026, Lean-checked). It is
  cited as a theorem.
- **M** is Masullo's claimed GRH for Hecke L-functions of every number field. It is an unrefereed draft (section 3.13
  lists the located defects), so everything "under M" is conditional.
- **U** means unconditional. "032" is OpenAI's family-032 proof of the rational Hodge conjecture for CM abelian varieties,
  used through Milne's Hexagon report. That is a third input, posted and formalized but not refereed.
- Check levels, as the intakes use them:
  - *confirmed*: a targeted proof check of every step;
  - *computation*: an independent recomputation;
  - *proof read, cited theorems carried*;
  - *statement level*: read as a statement, no fault found, not checked.
- The research runs are GPT-6 Astra (ChatGPT Pro mode) unless named otherwise. The bridges run of 20 Nov is Claude Opus 5.5
  at effort max.

## 0. Sources

- **Intakes of 21 Nov**, in `field_experts\intake_20261121\intakes\<TAG>\`:
  - round 1: CX_GRH, ALPOGE_BRIDGES, GCT_GINEQ, GCT_KRON, GCT_PLETH, ALPOGE_GCT, GCT_NSRH;
  - round 2: ZETA_TWO, DP_MULT, HODGE_SIGN;
  - round 3: the part-2 files of ALPOGE_BRIDGES, AN_GRH, ALPOGE_GCT, GCT_PLETH, GCT_NSRH, TRACE_DET, DP_MULT, K17,
    GCT_KRON, CUE_GCT, HECKE_DIV and THETA3, with the part-1 files of AN_GRH, TRACE_DET, K17, CUE_GCT, HECKE_DIV and
    THETA3, and the new intakes GRH_NIGHT, JAC1964, DEG_L and GHOSTS.
- **Intakes of 20 Nov:**
  - `field_experts\intake_20261120\intakes\` (DER_LOCALIZERS, RESIDUE, REVLOC);
  - `results_register\horizontal\sweep3\SA**\INTAKE_RESEARCH_*_20261120.md`: SA06, SA07, SA08 (C3/D031), SA11, SA12,
    SA14_SA19, SA15 (parts 1-2), SA17, SA20, SA22, SA23.
- **Fable's notes:** `reports_20261120\alpoge_rh\bridges\FABLE_PROGRAM_SUGGESTIONS_20261120.md`, by the war-game agent
  (Claude Fable 5.2 at effort max), with its `_EXPLAINED` companion.
- **Our own files:**
  - the bridges run, `reports_20261120\alpoge_rh\bridges\` (QUESTIONS.tsv, LEDGER.md, BRIDGES_20261120.tex);
  - the Hodge sketch, `reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`;
  - the Hexagon register, `field_experts\HEXAGON_CANDIDATES.md`.
- **Not taken in:** the DELTA23 run's newest checkpoint. Its expert is a Fable agent that needs the user's approval.
- **Integration:** every edit made to our files is a row of `field_experts\intake_20261121\INTEGRATION_LOG_20261121.tsv`.

## 1. The five most important findings

1. **A sign-only proof of Deligne's purity theorem.**
   - *Source:* HODGE_SIGN SG-08 to SG-11. Every step had a targeted check in the intake, and the Fable check (Claude Fable
     5.2 at effort max) re-proved every step.
   - *What it proves:* Weil I, Théorème 1.6, and Weil II 3.3.1 for H_c of constructible sheaves, with no monodromy and no
     Lefschetz pencil.
   - *In Grothendieck's terms,* it is his own hyperplane induction of cote 16, scans 034-040, with Parseval. It goes around
     his route through C, A and I(X×X) on scans 049-050.
   - *Status:* deposited as hexagon:2611.00789 (H01).
   - *Sharpened by GCT_NSRH F50 (confirmed):* the path sign can always be manufactured, so the whole content lies in the
     pointwise stalk bound.
2. **A1 of cote 149 is proved without GRH.**
   - *Source:* AN_GRH A05, read in full in the intake, a rebuild of our own ANABELIAN_A1 checkpoint 03.
   - *The statement:* prime-to-p point separation for hyperbolic curves over fields finitely generated over F_p.
   - *What it corrects:* our records carried A1 as open. Route 2, theta incidence in characteristic 2, is now a separate
     question (A18, A19, confirmed).
3. **Ihara's kernel question is answered at every Vandiver prime, and at 2.**
   - *At 2:* K17-P2-MOMENT, confirmed with the cited theorems carried.
   - *At every odd Vandiver prime,* hence every p < 2^31: K17-VANDIVER-KERNEL. The proof was read, the class-field steps
     were checked, and Fukaya-Kato and Wake-Wang-Erickson are carried.
   - *In Grothendieck's terms:* the first floor of the Teichmüller tower, π_1(P¹ − {0,1,∞})^{(p)}, sees all of the maximal
     pro-p extension unramified outside p.
   - *Step 17 of Alpöge's note* is a polynomial Selmer bound (the Lean theorem corGK). It is not the vanishing of K_{4k}(Z).
4. **GCT positivity: PH3 fails for ordinary plethysm.**
   - *Source:* ALPOGE_GCT P-F31, with P-F23 and P-F30, all confirmed.
   - *The failure:* the cubic-invariant stretching series has a simple pole at every primitive 2^{n−1}-th root of unity, so
     every positive form needs denominators of weight at least 2^{n−1}.
   - *Mechanism:* equivariant localization of the Hilbert series of the GIT quotient P(Sym³V*)//SL_n. That is a graded-ring
     form of the Lefschetz-Riemann-Roch of SGA 6, Exp. VII.
   - *Alongside it, obstructions on both sides of the padding range:*
     - explicit occurrence obstructions at n = m (GCT_KRON A-030, confirmed with four computations);
     - four-row multiplicity obstructions under genuine padding, n = m+1, m ≥ 8 (CUE_GCT R-14, confirmed).
5. **The Hodge line is reduced to one arithmetic quantity.**
   - *The equivalence:* bounded division along a Hecke orbit is equivalent to algebraicity (HECKE_DIV R21-R23 and P6,
     checked; precedent Brünjes-Serpé).
   - *Ghosts:* a non-algebraic Hodge class would be a ghost in the strict sense, algebraic modulo every good prime with
     complexity tending to infinity (GHOSTS B03 with 032 Remark 8.5).
   - *An explicit integer:* on the principal Q(ω) Weil fourfold component, bounded division is proved from Schoen's
     published construction with D₀ = 132,269,760 (GHOSTS R10-R12, checked).
   - *The rate:* in a CM isogeny class the witness degree is of order √J, where J = [Λ : Λ^−] is the core index of the
     lattice (DEG_L B19, checked).
   - *The L-values are not the obstacle:* in the Rallis formulas they sit at s = 3/2, in absolute convergence, and are
     bounded without GRH (DEG_L T6.11, B1).

## 2. Scope: what A and M do and do not reach

- **What A gives** (all checked):
  - RH for ζ_K with K abelian (CX_GRH CX-R01; ZETA_TWO ZT01, ZT03);
  - RH for every scheme over Z with abelian Artin-Tate point counts at every prime (bridges F1 = ALPOGE_BRIDGES BR-AT-01
    = ZETA_TWO ZT01);
  - Miller's test with quadratic characters (CX-N01);
  - nonresidues (CX-N02, N13);
  - the explicit class-number bounds of LLS (ZETA_TWO IA02, IA03);
  - unit generation of (Z/N)^× below 3 log² N, Bach 1990 Thm 3, not 2 log² N (AN_GRH T01).
- **What needs M:**
  - every non-abelian field: Koiran's Nullstellensatz in AM (CX-K01, K02), Hooley's Artin density (AN_GRH A02), ring-class
    fields, Kummer division fields;
  - every Artin L-function in the zero-location sense, by Brauer induction (ZETA_TWO ZT02 = the CX_GRH Brauer remark);
  - odd two-dimensional Artin, with Khare-Wintenberger (GRH_NIGHT MT-ART01);
  - CM motives (ZETA_TWO CM01), which need M for unitary Hecke characters of *infinite* order.
- **Beyond both:**
  - non-CM GL₂ of weight ≥ 2 (first case h¹(E), E non-CM; ZETA_TWO ZT07 shows its off-line zeros cannot cancel in ζ_E);
  - Artin holomorphy;
  - standard U(2) L-values at the edge (DEG_L T6.13).
- **Corrected glosses:**
  - "RH for ζ_X of every Λ-scheme" (the ALPOGE_BRIDGES intake's gloss of CC-F01b) is false. Spec Z[1/p] is a Λ-scheme
    (DP_MULT DP11), and its ζ has zeros 2πik/log p on Re s = 0 (ZETA_TWO ZT05). CC-F01b gives RH only for the canonical
    L-function of H_c(X_Q̄); ζ_X differs by the bad-fibre factor R_{X,S} of ZT04.
  - F1 needs its point-count identity at every prime, conductor primes included (ZT04/ZT05 caution, now in
    BRIDGES_20261120.tex).
  - *Superseded in part: see §9.1 (proper flat Λ-schemes; Z[ζ₅] is not a Λ-ring).*

## 3. The lines of work

### 3.1 RH for zeta functions over Z and motives over Q (bridges Q01, Q02; prompt 35 ZETA_TWO)

- **Established:**
  - F1/F2 = BR-AT-01 = ZT01 (U identity, A for the zeros);
  - ZT03 (Spec O_K, abelian K under A);
  - ZT04, ZT05, ZT07, ZT08 (confirmed);
  - BR-MIX-01 and SV01/SV02 (confirmed): good-prime L-data see only gr^W, so they cannot compute the Ext groups of step 17.
- **Conditional on M:**
  - ZT02, every Artin-Tate count and every Spec O_K;
  - CM01, every pure motive in Anderson's CM category. CM01 is confirmed given Anderson Cor. 5.7.2, which was not opened.
- **Reduction:** Q01 for general X reduces to finitely many L^S(H^j(Y_a)) plus the bad fibres (ZT06, confirmed as an
  algebraic reduction; one clause, on the CM summands, needs a decomposition the proof does not give).
- **Open (gate):** RH for the non-CM summands up to Tate twist. That is not a weight condition.
- **What it makes possible:** for a given X, compute its finite list (Bittner's generators and Faltings' semisimplicity)
  and say exactly which non-CM L-functions its RH waits on.
- **For Λ-schemes:** the correct unconditional target is that every non-real divisor lies on Re s ∈ ½Z (ZETA_TWO §5.2).
  The conjecture to test is that every bad-fibre factor of a flat Λ-scheme is a product of (1 − ζp^{j−s})^{±1}.
  *Superseded: ZETA_NEXT decided it (refuted for nonseparated, claimed for proper); see §9.1.*

### 3.2 Purity by a sign (prompt 32 HODGE_SIGN; prompt 24 GCT_NSRH; Fable suggestions 3 and 4)

- **Established:**
  - HODGE_SIGN SG-08 (the effective Gysin remainder), SG-09, SG-10 (smooth proper purity) and SG-11 (Weil II 3.3.1 over
    any base), all confirmed;
  - GCT_NSRH F03, F04, F17: the abstract sign-only theorem (confirmed in its intake);
  - F50 (confirmed): Gaussian encoding realizes the path-sign hypothesis for any coefficient space; the pointwise bound is
    then exactly the purity of C. As a by-product |Gauss sum| = √q without weights.
  - TRACE_DET TOY-01 (confirmed) is Fable's toy made correct, with a composite-modulus correction.
- **Refuted:** the identification of the step-5 sign with the Hodge-index sign (HODGE_SIGN §1 Q2; Fable suggestion 4).
  The sign is the class of E^{n−1}(Y) = Ker φ_* in a Grothendieck group, with sign (−1)^{n−1}: a parity with no bilinear
  form. HECKE_DIV A3 and THETA3 agree that purity "sees nothing of cycles".
- **Open:** for the nonstandard quantum groups of GCT, a trace system with independently bounded stalks whose cohomology
  carries the nonstandard coefficients (GCT_NSRH, gate R).

### 3.3 The Hodge line (prompts 37-41: THETA3, HECKE_DIV, GHOSTS, JAC1964, DEG_L; the Hodge sketch)

- **Route 1, theta lifts:**
  - THETA3 (Q1-Q9, C13 confirmed): 032 §§4.5-4.7 state no Rallis or Bessel identity; the non-vanishing is Gaussian
    concentration plus continuity.
  - The sketch's 1.7, one seesaw linking 032's signature (2,1) with Alpöge's definite groups, is not proved. The analytic
    seesaw exists (B17, statement level), but its upper space has signature (3,1).
  - The gate is a totally definite middle space. By A7 (statement level) that happens exactly when the first-list CM types
    agree.
  - C13 is the same resultant projector as HECKE_DIV P1/P3.
- **Route 2, bounded division:**
  - **Established:**
    - R21-R23 (2.1-2.3 with corrected hypotheses) and P6 (algebraic ⟺ uniform integral effective degree at infinitely many
      good primes);
    - R24C, R24A′ (2.4's endomorphism-degree and signed-degree readings false), R24E, R24F;
    - GHOSTS B02, B02a, B03, B06, the ghost dichotomy;
    - GHOSTS P09, P13: minimum complexity 16 at every good prime on E⁴;
    - GHOSTS R10-R12 (the explicit D₀) and C18 (transport cost constant, (1,16,16));
    - DEG_L B19: a witness of degree O(√J) and complexity O(J).
  - **Statement level:** DEG_L B21 (√J cannot be beaten by any bounded source); GHOSTS R20-R24 (general polarization,
    D₆ = 57,854,793,024,000).
  - **Conditional on preprints:** HECKE_DIV M10 (fourfolds, Markman) and P4/SQ9 (E⁸, Severn).
  - **Open:** uniformity along a CM sequence with J → ∞. The two exits DEG_L names are a uniform bound on J on a dense set
    of CM points, or one weakly equivariant semiregular perfect complex at one fibre (S-14, statement level). The latter is
    the variational Hodge route of Grothendieck's de Rham paper (IHÉS 29, the footnote; locator to verify).
- **Degrees as L-values (DEG_L):**
  - T6 is refuted as worded: T6.2, the 032 output class has degree 0 against the product polarization.
  - The exact finite identities are T6.11 (Hecke L at 3/2, bounded by B1 without GRH) and T6.13 (standard U(2) L at 1).
  - Universal semiregularity is refuted at deep levels (S-05, S-06). A fixed smooth image is open.
- **Cote 44 (JAC1964, confirmed):**
  - Th. 4 holds on the primitive part for abelian varieties in every characteristic (JAC-T4.3), under 032 Cor. 8.4 through
    Milne's report.
  - Th. 5 fails as displayed:
    - on a quadric pencil for every m ≥ 2 (H9-C1);
    - on P²×P² (HODGE_SIGN AR-01).
  - The corrected Th. 5 is his formula plus one Schur term per singular fibre whose specialization map is not injective
    (H9-T1), with no correction when specialization is injective (H9-T2). That is the "variante locale" of his margin on
    scan 004.
  - Th. 6 and Th. 7 are at statement level: Th. 7 is false in characteristic 0 (Griffiths type) and true over F̄_p for
    abelian type under 032 (JAC-P15).
  - The arithmetic sibling (sketch 3.5) is open.
  - *Th. 5 is now corrected twice and H04 is complete mathematically; scan 050's Proposition is corrected; see §9.3.*

### 3.4 Cote 34, scan 064, Remark 1.17 (bridges Q03)

- **Refuted:** the literal statement (HODGE_SIGN Q3-01; GRH_NIGHT AG-C34-TYPE).
- **Proved, confirmed:**
  - the intrinsic commutator subgroup K of H is open, with H/K = (H^ab)_{π₀} and [H:K] ≤ |I(ℓ)_{π₀}|, by his own
    Theorem 1.1 of cote 34 (PDF p. 53) (GRH_NIGHT AG-C34-REPAIR; HODGE_SIGN Q3-03, Q3-04);
  - with a chosen section and finite derived length, the action commutators are open (AG-C34-SECTION);
  - curve purity suffices (Q3-02).
- **Open:** the non-solvable case with a section. The attack runs through the pro-ℓ outer Galois action on a hyperbolic
  curve (Ihara, Deligne, Anderson-Ihara, Hain-Matsumoto).

### 3.5 Cote 1: trace, determinant and the Ξ operator (SA23; ALPOGE_BRIDGES BR-TR-01; TRACE_DET)

- **Established, and classical in substance:**
  - Ξ(√w)/Ξ(0) = det(1 − wB), B = diag(γ_j^{−2}) trace class, with RH ⟺ B ≥ 0 (BR-TR-01, TRACE_DET B-01);
  - no trace-class T has Ξ itself as its determinant (B-02);
  - det(I − s(1−s)C) = 2ξ(s) (DET-11, independently re-proved);
  - B ≥ 0 ⟺ the explicit-formula kernel k is of positive type ⟺ RH (DET-16), now unconditional by A.
- **Reading of the archive:** cote 1, sheets 079-080 and 111-112, prove the trace and Fredholm theorems. The ξ-determinant
  reading is ours. The archive has neither Ξ nor B.
- **Corrections to his lemmas, confirmed:**
  - scan 112: θ ∈ (π/3, π/2), h(|z|), ω² (ARC-01);
  - scan 110: order 1/α (ARC-02);
  - scan 113: liminf (ARC-03) and the prefactor n₁ (ARC-04).
  - Whether each is his slip or our transcription needs the images (second pass).
- **Alpöge's determinants** are finite algebraic (Gram, Capelli, period) determinants carrying an inertia sign
  (DET-10, statement level). They are not compressions of B.
- **Conditional on M:** MAS-10, an ordinary Fredholm Ξ determinant on Masullo's weighted quotient, needs only his
  Theorem 10.2.2.1 (p. 446); confirmed as far as read.
- **Open:** a positively normalized actual determinant equal to W_std(q₀ + q_{−log X}) (Q-DIRECT-BRIDGE).

### 3.6 Step 17, K-groups of Z and Ihara's question (prompt 31 K17; bridges Q06; Fable suggestion 5)

- **Established:**
  - K17-FIELD-DESC, K17-S17-Q (confirmed);
  - the identification of step 17 as the Lean theorem corGK (`AV/SmallClassNumbers/CorGKOf.lean`), a polynomial bound on
    Selmer groups (source fact);
  - K17-P2-MOMENT (confirmed);
  - K17-VANDIVER-KERNEL (proof read, inputs carried);
  - F149-UNIT (confirmed).
- **Statement level:**
  - VK-EXP7, log|K_{4k}(Z)| ≤ C_7(2k)^7 with C_7 unevaluated;
  - K17-2-ALL and K17-INTEGRAL-CLASSIFICATION: integral odd generation holds at 2 and at regular primes, and fails at
    every irregular Vandiver prime;
  - K17-K12-TWO-RANKS: K_12(Z) = 0 reduces to H_4(GL_9(Z); St ⊗ Z[1/13!]) = 0 and H_3(GL_10(Z); St ⊗ Z[1/13!]) = 0.
    *Superseded by the three-rank form, with an unverified gap in DEKM's enumeration; see §9.5.*
- **Open:**
  - no new K_{4k}(Z) is proved zero;
  - the kernel question at a prime where Vandiver fails;
  - Soulé 2003 has not been compared.
- **What it makes possible:**
  - compute gcd(n_7(2k), n_11(2k)) for k = 3, 4, 5;
  - compute the two Steinberg groups from the Voronoi complexes of GL_9 and GL_10.

### 3.7 Step 2 as divided powers (prompt 34 DP_MULT; Fable suggestions 2 and 9)

- **Established:**
  - DP1-DP3, DP6 (confirmed): the bound v_p(D^n f) ≥ c_h n − (h−1) for every one-dimensional formal group of height ≥ h
    over W(k), with optimal slope and constant. Alpöge's exponent a/p + a/p³ + … is exactly c_2, with error −1.
  - DP34 (confirmed): constant 1 on every Honda-dual direction.
  - DP42 (confirmed, DP41 carried): along every primitive mixed line of G × G^D, the line a theta kernel follows, the slope
    is at most ρ_2 = 1/(p²−1) at every height.
  - DP10, DP11-DP13 (classical, correctly applied).
- **Refuted:**
  - "higher height shortens step 8", along primitive mixed lines (DP42, DP48);
  - total-height use (DP8);
  - "differentiating whole numbers" on the formal disc (DP14).
- **Reading of cote 54, scans 5-7:** the boxed "t_A^∨ … puiss. p-ième nulle" concerns the additive kernel of the
  universal extension and holds for every abelian variety (DP10). The comparison with Cartier duality is answered by Oda
  1969, Cor. 5.11.
- **Open:**
  - non-primitive mixed lines or selected harmonic operators (the `HaO` of the source theta);
  - the global cost (DP44's formula).

### 3.8 Anabelian, cote 149 (prompt 30 GRH_ANABELIAN = AN_GRH; K17 F149)

- **Established:**
  - A05 (A1, as in section 1);
  - A01, A03, A04, A06 (with computation), A18, A19, T01;
  - A13 (arithmetic by computation).
- **The A1 status** is recorded in `pro_intake_20261114\INTAKE_ANABELIAN_149_FINAL_20261114.md`, §0.
- **Conditional on M:** Hooley-type densities (A02, A17); G06's explicit surjectivity bound (Mayle-Wang).
- **Open:**
  - route 2 for every genus-two curve over F̄₂: an odd n with ⟨2, −1⟩ = (Z/n)^× and a theta point of exact order n;
  - section surjectivity;
  - higher dimension;
  - scan 85's intrinsic characterization of the geometric splittings (F149-UNIT shows "comes from H¹(S,T)" is not
    enough).
- **What it makes possible:** an Artin-type problem for the sequence #J(F_{Q^d}) = Res(P, T^d − 1) as d varies. That is
  where route 2 meets GRH, under M (AN_GRH part 2, §4.3).

### 3.9 Complexity under GRH (prompt 28 CX_GRH; GRH_NIGHT; bridges Q07, Q08)

- **Established:**
  - Koiran's input localizes to RH for ζ_E of one bounded solution field, with no Galois closure (CX-K01, confirmed);
  - under M, Hilbert's Nullstellensatz for circuit systems is in AM ⊆ Π₂P (K02);
  - under A, the bounded abelian promise version is in AM (K03);
  - the abelian-witness route is refuted, since x³ − 2 has no root in an abelian extension (K04);
  - under M, the h.s.o.p. search is in FP^{Σ₂P} (K05);
  - Miller's test with quadratic characters (CX-N01, Q08 settled);
  - Evdokimov factoring localized to RH for the Kummer fields Q(ζ_{2ν}, p^{1/ν}), ν ≤ d² (CX-N15, modulo the cited
    algorithms).
- **Narrowed by GRH_NIGHT (confirmed):**
  - the case r | m is unconditional (CX-ALG-023);
  - under A, RH(ζ_{Q(p^{1/r})}) ⟺ RH(ζ_{Q(ζ_r, p^{1/r})}) (CX-ALG-024).
  - So the factoring gate is RH for one order-r Kummer Hecke character over Q(ζ_r) per encountered prime r.
    *Superseded in degree dependence by the polynomial-time route through OpenAI's PF26; see §9.4.*
  - A BIMS17 resolvent can vanish (CX-ALG-016); the repair is CX-ALG-017, and CX-ALG-018 covers the even quadratic case.
- **ETH:** OpenAI's fixed-width #k-SAT counter refutes ETH, SETH and their counting and gap forms. It touches none of
  VP/VNP or GCT's border-hardness premises (CX-E01, E06).
- **Open:**
  - Koiran with A alone (the gate is ζ_E for non-abelian E);
  - Alpöge's method extended to one Hecke character over Q(ζ_r).

### 3.10 Geometric complexity theory (prompts 23, 25, 26, 27, 36: ALPOGE_GCT, GCT_PLETH, GCT_KRON, GCT_GINEQ, CUE_GCT)

- **Positivity hypotheses:**
  - PH1 in homogeneous form is gone (Kahle-Michałek; repaired by shifted counting, P-F1).
  - GCT VI Theorem 1.6.1(d) is false as printed (P-F12/PL-Q22, the D_5 Kleinian series). The Cohen-Macaulay form follows
    from (c). The erratum is drafted as note E1.
  - PH3 ⇒ PH2 holds with an explicit bound (P-F12).
  - PH3 fails for inner shape (3) (P-F31).
  - §3.3's SH(a), PH2 and PH3 fail as stated (P-F14, P-F15, statement level).
  - What remains is PH2 and SH for irreducible-inner families. On the cubic family the gate is
    limsup n⁻⁴ log₂ U_n < 1/24, against the proved log₂3/6 (P-F34, P-F42), a factor of about 6.3 in the exponent.
- **Positive formulas (GCT_PLETH):**
  - stable-range positive formulas for tails of width ≤ 6 (T-012, T-013, confirmed on Sarkar's Theorem D);
  - outer degree 4 (T-037) and most of 5 (G-021), by computation only.
  - Plethysm in outer degree k becomes interpolation for k points of P^{k−2}, with the Cox ring of the blow-up (G-015,
    G-016, G-021).
- **Obstructions:**
  - occurrence, n = m, explicit (GCT_KRON A-030, confirmed);
  - multiplicity but not occurrence for per_3 (F-025, permanent side by computation);
  - four-row multiplicity under padding n = m+1 (CUE_GCT R-14, confirmed);
  - ternary multiplicities equal the ambient ones (G-05 = O-007, Beauville).
  - The middle range, between n = m+1 and the Bürgisser-Ikenmeyer-Panova bound n ≥ m^25, is open. The exact obstacle is
    the ranks of the evaluation tensors at the first open shapes (GCT_KRON F010).
- **Border rank (GCT_GINEQ, all 23 findings confirmed):**
  - the exact residual reduction F-23 gives BR(det_4), BR(per_4) ≥ 39; no published bound of 39 was found
    (*superseded: ≥ 42, BR_PENCIL; see §9.2*);
  - norm-based rank bounds fail (F-05);
  - the norms are not GL-invariant, so they do not bear on the padded-permanent orbit problem (F-19).
- **Archive:** the GCT runs touch only cote 133 (section 3.11) and the Résumé (CSG17), whose norms and fundamental
  inequality give rank information only through the image method.

### 3.11 Cote 133, λ-operations (SA17's study, corrected)

- **Scan 19:** the boxed 2λ²(E) + E = E² fails for finite G-sets, at the free C₂-orbit (fixed-point marks 2 against 0).
  - It was found independently by four runs: ALPOGE_GCT PL-01, GCT_PLETH A-001, GCT_KRON A001/A002 and CUE_GCT G-01, with
    a table-of-marks computation.
  - The identity holds in K₀ of vector bundles: V² = 2Λ²V + ψ²V.
  - GCT_KRON read the official facsimile and found the mathematics as transcribed.
- **Scans 20-23:** q_H^n(x) = q_H(τ^n x), so P_n = q_{S_n}^n (A-029).
- **Scans 24-27:** "direct summands of H_I" is false for a single H_I (A012, A-013). Whether the slip is the page's or the
  study's needs the image.
- **Scans 28-29:**
  - the monomial Cauchy terms are virtual (A004, A-007);
  - yes for Z_p-lattices (A013);
  - characteristic 0 of the ring is not sufficient (Z_(2)[ε]/(2ε, ε²), A-023).
- **SA17-21, the split WG:** not special in characteristic 3 (A-003, re-proved); exterior powers do not descend to the Witt
  group (PL-08).
- **Pending:** the Esnault-Kahn-Viehweg 1993 locator for the hyperbolic Stiefel-Whitney formula.

### 3.12 Archive questions read directly in algebraic geometry (20-21 Nov)

- **Cote 136, SA08 C.3 (ALPOGE_BRIDGES part 2):**
  - The strict form of his uniqueness conjecture (b) for admissible divided-power de Rham theories is false over every
    nonzero ring, by an explicit square-zero extension (AQ-136-STRICT, confirmed). The sheet's quotation marks around
    « 'égalise' » leave the homotopy form undecided.
  - (a) and terminality hold over Q-algebras, Z_(p)-algebras and in characteristic p (statement level). Z is the gate.
  - Five integral constructions fail, each with its obstruction.
  - Attack: an arithmetic fracture square inside 𝒜_Z. *Carried out for finitely many primes; see §9.5.*
- **Cote 123, the 1969 letter to Kostant:**
  - The prediction fails in sp₄ (BR-12302, confirmed with its own computation).
  - An outer-invariant "distinguished" class exists exactly outside type A_{2m}: the existence half is confirmed (CC-APG04),
    the converse rests on CC-AP04-05.
  - Counts, opposition table and rank r − 1 at the subregular class are at statement level.
- **Cote 134-8 (DER_LOCALIZERS; F-SM-29-35):**
  - The linear Thm(?) is proved for AB4 categories with enough projectives (statement level). The gate is the coproduct
    compatibility SM32.1.
  - The constant-coefficient localizer of a motivic derivator is ordinary Λ-homology (DER_LOCALIZERS); the G_m motive
    there is the reduced one, 𝟏(1) (BR-DER-02).
- **Cotes 14-15 (SA06; ALPOGE_BRIDGES CC-ALB, CC-AG):**
  - Theorem 3.1 of 14:38 holds in every positive characteristic with an integral premise (SA06 E.3e).
  - Its converse fails over C even rationally (E.3u, on a degree-14 section of the split 6-quadric; the class restricts to
    0 in H⁶ by HODGE_SIGN SG-07).
  - The letter's A, A′, A″ fail modulo algebraic equivalence (C.1a-b).
  - The supersingular count is S_p = c_p h(−D_p), with unconditional bounds under A (ZETA_TWO IA03).
- **Cote 18 (SA07):** the "Conj. de transcendance forte" holds conditionally exactly when v = u, and five of its values are
  false whenever v < u. The explicit counterexample is h¹ of y² = x³ − x + 1.
- **Other cotes:**
  - cote 31 (SA12): a persistent counterexample to Conjecture 1° of 31/085;
  - cote 57 (SA14_SA19): a very ample counterexample to Kodaira vanishing for H¹ in characteristic 2;
  - cote 4 (SA15 part 2; his 8.6): the monodromy of the Hasse-Witt local systems is computed exactly;
  - cote 154 (SA11): the surface of relative positions is #^{…}RP²;
  - cote 67 (SA22): the section-6 maps of 67/074-082 are not isomorphisms onto their target;
  - cote 119 (SA20): the Additif's conjectures I b), I c), II b) are false and II c) is true;
  - cotes 126-133 (SA17): a counterexample to the locally quasi-finite form of his representability criterion, and a proof
    of Murre's announced analogue;
  - cote 1 (SA23): the corrected determinant extends Hochs-Kaad-Schemaitat;
  - M̄_{g,n} and exodromy (RESIDUE H.3-H.6): the nodal fibre's H¹ is H¹(Γ) extended by ⊕H¹(C_v);
  - Whitehead torsion (REVLOC I.5, I.8b).
  - These carry no GRH input. Their RH/purity links are recorded in each intake's bridges section.

### 3.13 Masullo's draft: the located defects (one list, for the scope tables)

Every "conditional on M" should carry this list.
- **§9.3.2, pp. 425-426** (GRH_NIGHT, checked against the PDF):
  - Lemma 9.3.2.4 is false for general φ: Mφ(s) = e^{s²} sin(s²) (MT-M01);
  - Theorem 9.3.2.6 inverts an inclusion of intersections (MT-M02);
  - Lemma 9.3.2.5 lacks the closure of the ideal (MT-M05).
  - Each has a repair for the case needed. The live gate is an absolute Mellin-jet basis for an infinite arithmetic
    divisor (Q-MAS-INFINITE-BASIS). *Changed: the run reports §9 repaired unconditionally (MT-M18-M26); see §9.4.*
- **§11.3, p. 495:** the printed formula is identically zero; a typo with an evident fix (ALPOGE_BRIDGES F-SM-19/20).
- **§12.3-§12.4:** the global-to-local intertwiner (ALPOGE_BRIDGES F-SM-21/22). Our runs can test the draft at the
  trace-norm step R-MAS-KERNEL.
- **(10.3.2.4), p. 454:** one derivative order too many at odd s (TRACE_DET MAS-BOUND).
- **Theorem 13.3.1.2, p. 522:** blank ("Insert statement"), seen by three runs.
- **The trace formula of 12.5.1.1** excludes convolution squares, so it is not a positivity statement (MAS-03, ML02).
- **Holds as stated:** F-SM-13 (statement level), the exact numerical identity of 12.5.1.1 for Q from A.
- **Errata:** these go to the author as one drafted note, sent only on the user's word.

## 4. The bridges into algebraic geometry and Grothendieck's frameworks, by cote

| Cote, scans | Result (id, check) | How it reads in his terms | What it now makes possible |
|---|---|---|---|
| 16, 034-040 | HODGE_SIGN SG-08-SG-11 (confirmed); GCT_NSRH F50 | the hyperplane induction: the "definite sign" is the class of the evanescent part E^{n−1}(Y) = Ker φ_* in K₀, sign (−1)^{n−1}; Parseval finishes | RH over F_q without C, A, I; H01 v2 with F50's worked cases; the stalk side of the sign route for GCT |
| 16, 044-047 and 048-050 | HECKE_DIV numbering: two letters (4.1.67; "6.1.1966" as written); folio = our scan − 1 | C(X) + I(X×X) ⟹ semisimplicity (049) and Weil from C and A (050) are in the second letter | correct citations in every successor; GCT_NSRH and THETA3 cite folios |
| 16, 014-017 | HODGE_SIGN SL-04, SL-08, SL-09 | the universal Lefschetz ring Φ₀ = Z[L₀, Λ₀] "sur Z !"; the primitive scalar is r!d!/(d−r)!; string-model order indices 1, 32, 2^13·3^10 | the integral form of no 7 (hunch H8, corrected); transcription rows 015, 017 for the second pass |
| 44, 002-009 | JAC1964 JAC-T4.3, H9-C1, H9-T1, H9-T2 (confirmed); HODGE_SIGN AR-01 | Th. 4 = Hodge standard positivity on P^m(A)_prim via curve tests; Th. 5's "variante locale" = one Schur term per non-injective singular fibre | a companion paper on cote 44 (H04, H11); the cubic fourfold pencil (E ≠ 0) as the test of H9-T2 |
| 34, 053-074 | GRH_NIGHT AG-C34-*; HODGE_SIGN Q3-01-Q3-04 | Remark 1.17's intrinsic form is a corollary of his Theorem 1.1 | the non-solvable case through Ihara's outer action |
| 1, 078-113 | BR-TR-01; TRACE_DET B-01, DET-11, DET-16, ARC-01-04 | the trace and Fredholm theorems (Lidskii), with his own genus-zero lemma corrected | a cote 1 companion paper after the image check; DET-16 states B ≥ 0 without zeros |
| 133, 19-29 | four runs on scan 19; A-029; A-003; G-021 | λ-structures on the Burnside ring forget the S₂-torsor Mon(I₂,E) → P₂(E); in K₀ they are right | the oriented-subset ring and its specialness ("λ^i(xy) = ?"); plethysm as H⁰ of twisted ideal sheaves |
| 149, 33-38 | AN_GRH A05, A18, A19 | point separation for the prime-to-p geometric quotient, with the full arithmetic quotient | section surjectivity; route 2 as an Artin problem for #J(F_{Q^d}) |
| 149, 79-85 | K17 F149-UNIT, F149-RELATIVE | the cusp normalizer is π₁ of the punctured normal line; its obstruction is the Kummer Chern class of the conormal line | an intrinsic profinite characterization of the geometric splittings (Q5-GEOM) |
| Esquisse §2 (Teichmüller tower; no cote) | K17-P2-MOMENT, K17-VANDIVER-KERNEL | the first floor of the tower sees the maximal pro-p extension unramified outside p | the Greenberg-extension route at non-Vandiver primes; a Hexagon note (H06b) |
| 54, 5-7 | DP_MULT DP10; Oda 1969 Cor. 5.11 | the restricted p-Lie algebra of the universal vector extension; Cartier duality recovers H¹_dR with its filtration | DP1-DP3 as a statement on the divided-power envelope of the Hodge filtration of the Dieudonné crystal |
| 4, scan 3 | DP_MULT | Tor_1^W(H^{i+1}_crys(X/W), k): keep the index i+1 | none new |
| 136, 117-121 | AQ-136-STRICT (confirmed) | admissible strict PD de Rham theories: (b) strictly false | (a) over Z by a fracture square |
| 123, 22-23 | BR-12302; CC-APG04 | apposition quadruples (Kostant) | a literature search, then the cote 123 post |
| 134-8 | F-SM-29-35; BR-DER-01/02 | connective localization by maps inverted by Lφ | the coproduct gate SM32.1 |
| 60, 3-9 | ZETA_TWO ZT08, AR01 | the determinant functional equation carries no purity; scan 9 assumes the Weil conjectures | a companion reading note (no cote 60 note exists yet) |
| 14, 044-047; 16, 048-049 | GHOSTS framework map; R11 | C^i modulo algebraic equivalence; R11 is the integral form of the Cayley-Hamilton inverse | the ghost line in the letter's own terms |
| CSG17 (Résumé, §4 no. 2) | GCT_GINEQ F-05, F-13, F-23 | the projective/injective norms and the fundamental inequality give rank only through the image method | BR seeds for F-23 by Jacobian-rank certificates (CUE_GCT R-13's method) |

**The algebraic-geometric translations the intakes added:**
- **P-F31.** The stretching ring is the coordinate ring of P(Sym³V*)//SL_n. The pole is a fixed-locus contribution of μ_M
  (SGA 6 VII). The obstruction is invisible in K₀(GL_n) and visible in μ_M-equivariant K₀ of the quotient stack.
- **PH3 in projective terms.** An h.s.o.p. is a finite map Proj T → P(a_1, …, a_r) (graded Noether normalization, EGA IV 5,
  EGA II 6). Reciprocity is local duality for the canonical module.
- **CUE_GCT R-14** compares the Hilbert polynomials of the multiplication image P³ × P(P_{m,4}) → P(Sym^n C⁴) and the
  quaternary determinantal locus (EGA II 5.5).
- **GCT_GINEQ F-23** is a statement on the incidence scheme I_{q,s} ⊂ Gr(q,W) (EGA II 5.4-5.5). It works over every
  algebraically closed field, with Zariski border rank.
- **DEG_L B19.** The Hom lattice of a CM isogeny class is the ideal (Λ : I₀) of O_E. J is the conductor of End(A).
  Bounded division is controlled by the Néron-Severi/Hom lattice of the CM motive, not by its L-function.
- **ZETA_TWO ZT01** is a class [Rf_!Q_ℓ] = Σ[𝒱_i(−i)] in K₀(D^b_c(Spec Z[1/Sℓ], Q_ℓ)) with finite monodromy.

## 5. Fable's suggestions of 20 Nov, one by one

Each entry gives the suggestion, what has been done on it since, and what is open.

1. **"Δ is a reciprocity defect at the primes 2 and 3", Δ(F) = χ₁₂(u(F)).**
   - *What it says:*
     - u(F) ∈ (Z/12)^× is the frame unit of LM7_PUSH E.65;
     - χ₁₂ = χ₋₄·χ₋₃ is the character of Q(√3);
     - Δ = ε₂ + ε₃ mod 2.
     - So E.3 becomes "do the hexagon and pentagon force ε₂ = ε₃?", a product formula over the harmonic and equianharmonic
       points.
   - *Its link to ghosts:* an element with unequal bits passes each local test and fails the product formula.
   - *Done:* none of the 20-21 Nov intakes tests it. The DELTA23 run is the one aimed at it, and its newest checkpoint is
     not taken in. What the intakes do give around it:
     - checked certificates for the cyclotomic coordinate of every finite level of GT̂₀ (AN_GRH T01, with coefficient 3,
       and T02-T07 for the 53 identified moduli; ALPOGE_BRIDGES AQ-FINITE);
     - the bridges run's F3, the (2,3,6) orbifold E₀/μ₆ of the hexagonal CM curve as the exact object of the note's hexagon
       trick;
     - K17's results on the Galois action on the tripod.
   - *Fable's own hand checks* (χ₁₂ values; the Hilbert symbol (−1, −3) at 2, 3 and ∞) are "numerology to test", as its
     note says.
   - *Open:* proving Δ = χ₁₂ ∘ u from E.65's definitions; expressing ε₂, ε₃ as local symbols; evaluating them on E.58;
     whether hexagon and pentagon force ε₂ = ε₃.
2. **Step 2 as a divided-power structure of height 2.**
   - *Done:* DP_MULT proved the bound, and a sharper one (DP1-DP3, DP6, DP34). Alpöge's exponent is c_2, with error −1.
   - *Refuted:* the proposed use, faster gain at larger height. Total height fails (DP8), and every primitive mixed line has
     slope ≤ ρ_2 at every height (DP42).
   - *Open:* non-primitive or harmonic selections, and the global cost (DP44). Candidate H09.
     *Changed: DP51 closes the harmonic selections (statement level); only the global count is open; see §9.5.*
3. **The count qN = M^k + R as the k-th moment of "multiply, then Fourier".**
   - *Done:* the toy bound is proved and sharp, with a composite-modulus correction (TRACE_DET TOY-01). Its norm part is
     GCT_NSRH F01. Open paths are matrix coefficients, not traces (DET-02). The general form is H01.
   - *The link to cote 1* is refuted as a realization: Alpöge's determinants are not compressions of B (TRACE_DET). B ≥ 0 is
     RH, stated without zeros as DET-16.
   - *Open:* the direct bridge Q-DIRECT-BRIDGE.
4. **The sign-only proof as the Hodge-index route of cote 16, reaching cote 44.**
   - *Refuted* as an identification (HODGE_SIGN §1; Hodge sketch 3.6). The sign is a parity of E^{n−1}, with no form.
   - *What came of it* is better than the suggestion: the induction of cote 16, 034-040, proves Weil's absolute values (H01).
   - *Cote 44:* Th. 5 is false as displayed (AR-01, H9-C1) and corrected (H9-T1, H9-T2). Th. 4 is proved for abelian
     varieties under 032 (JAC-T4.3).
5. **Step 17 and the pro-ℓ kernel; an integral form of bridge B3.**
   - *Done:* step 17 is a Selmer bound (corGK), not the vanishing. The kernel question is proved at 2 and at every Vandiver
     prime (K17). The integral-generation clause is false at 37 and 691 (T-INTEGRAL37/691, McCallum-Sharifi). Integral odd
     generation holds at 2 and at regular primes (statement level).
   - *Open:* non-Vandiver primes; evaluating C_7; K_12(Z).
6. **The SL₂ of the lift chain as the Lefschetz sl₂ of cote 16.**
   - *Refuted* in its unnormalized form (HODGE_SIGN SL-07: FL = qLF). The integral comparison is a gate.
   - *Hunch H8 corrected:* the primitive scalar is r!d!/(d−r)! (SL-04), and the string-model indices are 1, 32 and
     2^13·3^10 (SL-09). The Wilson range (SL-01) is at statement level.
7. **What A gives our files directly.**
   - *Corrected:* the Bach constant is 3 log² N for units (AN_GRH T01).
   - *A1:* route 2 is not needed, because A1 is proved without GRH (A05).
   - *Route 2 itself* now meets M through a Hooley-type density (A17 and the Artin problem for #J(F_{Q^d})).
8. **Period multiplicities as interlacing counts for GCT positivity.**
   - *Done:* made exact by GCT_NSRH F13.
   - *The limit:* F18 shows that a homogeneous integral interlacing model cannot count Kronecker coefficients (saturation
     fails), so a theta chain needs congruence or lattice data.
   - *Nearest checked positive formulas:* GCT_PLETH T-012, T-013 and the interpolation reading.
9. **F₁ after Borger; binomial structures.**
   - *Affirmative* in the sense of DP11-DP13: torsion-free binomial rings are those with identity Frobenius lifts (Elliott
     Thm 4.1), and Horel reconstructs spaces from binomial cochains.
   - *Refuted:* "differentiating whole numbers" on the formal disc (DP14). The honest bridge is DP12, finite differences on
     Int(Z).
   - *It also produced* the Λ-scheme counterexample to the CC-F01b gloss, Spec Z[1/p] (section 2).

**The war game's directly algebraic-geometric material** stays worth pursuing on its own, with no RH input:
- the hunches H8 and H9 (corrected as above);
- the Hodge sketch's Routes 2-5;
- the archive questions of section 3.12 (cotes 136, 123, 134-8, 14-15, 18, 31, 57, 67, 119, 126-133, 154).

These are where the night's checked results land in Grothendieck's frameworks most directly.

## 6. The Hexagon candidates the intakes name

The five tests (`field_experts\HEXAGON_CANDIDATES.md`) are:
1. complete;
2. self-contained;
3. stable, with the literature searched;
4. checked, with an independent re-proof or computation;
5. of interest now.

| # | Candidate (source) | 1 | 2 | 3 | 4 | 5 | Gate left |
|---|---|---|---|---|---|---|---|
| H01 | Sign-only proof of Deligne's purity (HODGE_SIGN SG-08-SG-11); F50 folds in | yes | yes | deposited as hexagon:2611.00789 | intake plus the Fable re-proof | very high | a v2 with F50's worked examples (GCT_NSRH part 2) |
| H02 | PH3 fails for ordinary plethysm (ALPOGE_GCT P-F31; companions: the 1.6.1(d) erratum, P-F14/P-F15) | yes (P-F27 read only by the run) | yes | no: the run is live on PH2; literature (Kahle-Michałek; later GCT positivity papers) | P-F23, P-F30, P-F31 checked; P-F30 exhaustive at n = 3, 4 | high | the run's final, a literature search, a read of P-F27/P-F28; note E1 to Mulmuley on the user's yes |
| H03 | BR(det_4), BR(per_4) ≥ 39 (GCT_GINEQ F-23) | yes | yes | no: the GINEQ successor pushes it | all 23 findings confirmed; scripts rerun | moderate to high | an independent check, the successor |
| H04 | Cote 44 Th. 5 fails and is corrected (HODGE_SIGN AR-01; JAC1964 H9-C1, T1, T2) | yes | yes | yes | targeted checks | moderate (archive) | the scan image; optionally the P²×P² local terms; the companion write-up |
| H05 | RH for every CM motive under M (ZETA_TWO CM01) | yes | no (M) | — | confirmed given Anderson Cor. 5.7.2 | moderate | Masullo's proof refereed or checked |
| H06a | What Alpöge's step 17 proves (K17-S17, S17-Q, VK-EXP7) | yes | Alpöge's Lean theorem | no | partial | high, timely | the Soulé 2003 comparison; the exponent-7 chain; ideally an evaluated C or a gcd certificate |
| H06b | Vandiver implies a positive answer to Ihara's question; every p < 2^31; ℓ = 2 (K17) | yes | yes (Fukaya-Kato as a preprint version) | literature not searched | partial (POLE-GENERAL not read by an intake) | high | a literature search, an intake read of POLE-GENERAL, FK/WWE against their texts, an independent re-proof |
| H07 | A1 without GRH (AN_GRH A05) | yes | yes (SGA 1, Saïdi-Tamagawa) | literature not searched | read in full; Steps 1-2 at argument level | moderate to high | the literature search (is removing Saïdi-Tamagawa's exceptional set known?); an independent re-proof of Steps 1-2 |
| H08 | Grothendieck's 1969 prediction to Kostant fails (BR-12302), with CC-APG04 | yes (CC-APG04 modulo CC-AP04-05) | yes | literature not searched | confirmed by hand and by computation | moderate | Brieskorn/Slodowy/Kostant 2010 search; a check of CC-AP04-05 |
| H09 | Divided powers in step 2 (DP1-DP3, DP32, DP34, DP42) | yes (DP42 with DP41 carried) | yes | no: the run is live | checks plus 115 recomputations for DP1/DP3 | moderate to high | the final, a literature search, DP41, a computation of DP42 at p = 3, h = 3 |
| H10 | Biró's Conjecture 1 against Louvel (S6_05 A.5.7) | yes | yes | stable | sense check | high for Biró | only if Biró wants a citable note |
| H11 | Cote 44 Th. 4 for abelian varieties, every characteristic (JAC-T4.3) | yes | only if 032 and Milne's report count as inputs | probably | targeted check | high | an independent re-proof including JAC-P01, a literature search (Milne, Ancona), the write-up |
| H12 | Ghost classes: the dichotomy and an explicit bounded division (GHOSTS B03, P09/P13, R10-R12) | yes | yes (Schoen 1988, 1998) | final; no search | targeted checks; W04 rerun | high (Hodge line) | a literature search (effective Hodge, Schoen, Markman); an independent re-proof of R12 and R20-R24 |
| H13 | Occurrence obstructions at n = m (GCT_KRON A-030) | yes | yes | literature not searched | targeted check plus four computations | moderate to high | a literature search (Kumar 2015; Bürgisser-Ikenmeyer-Hüttenhain; Ikenmeyer-Kandasamy; Dörfler-Ikenmeyer-Panova) |
| H14 | Four-row multiplicity obstructions under padding (CUE_GCT R-14) | yes | yes | literature not searched; the run extends the range | targeted check; c_m recomputed for m = 4-8 | high if new | a literature search (Kadish-Landsberg; Landsberg ch. 8-9; Ikenmeyer-Kandasamy; Gesmundo-Ikenmeyer-Panova) |
| — | AQ-136-STRICT (cote 136) | yes | yes | stable; the reading caveat must be in the post | intake check only | low to moderate | an independent re-proof; best posted with (a) over Z |
| — | DEG_L B19 + B21 (Weil witnesses of degree Θ(√J)) | B19 yes, B21 statement level | needs B6-B8 included | run live | B19 checked | moderate | B6-B8 and B21 checked, a literature search, a numerical g = 2 example |
| — | GRH_NIGHT CX-ALG-023-026 (the factoring gate) | parts | yes | — | 023, 024 checked | moderate | later (*superseded by the PF26 route; see §9.6*) |

*H03, H04, H06b, H09 have changed, and H15 and H16 are new: see §9.6.*

**Not posts (errata and corrections):**
- Masullo's defects (section 3.13). These go to the author as one drafted note.
- Milne's report on 032, §3.6: a missing sign (GHOSTS C15). This goes to Milne.
- The cote 1 lemma corrections (TRACE_DET ARC-01-04). These belong in a cote 1 companion after the image check.
- The cote 133 corrections (test 5 fails: they correct an unpublished page and our study).

## 7. Successor prompts the findings call for (seeds)

Each seed is tied to its findings. None is a prompt yet. Every successor states its results also in Grothendieck's
frameworks, by cote and scan and our ids, and every prompt goes through the lints before it is sent.

1. **ZETA_TWO successor (prompt 35).**
   - Main question: RH for ζ_X of a given scheme X, its finite list of non-CM L-functions computed (ZT06).
   - Second: the bad fibres of Λ-schemes, with the conjecture of §3.1 and Borger's Frobenius lifts (CC-F01b, ZT05, DP11).
   - Attach MT-ART01, DET-16, DET-18, MAS-10, MAS-11 and the Masullo defect list.
2. **HODGE_SIGN / GCT_NSRH successor (prompts 32, 24).**
   - The stalk side: for the rank-three objects of F44 and F46, a sheaf on affine space with stalks pure of known lower
     weight whose H_c is the coefficient object (F50's remaining input).
   - The non-solvable case of cote 34 Remark 1.17 with a section, through Ihara's outer action.
3. **Hodge line (prompts 37-41).**
   - THETA3: the totally definite case of MainX (A7, B17, G1).
   - HECKE_DIV/GHOSTS: the E⁸ analogue of R12 by a Schoen-type Prym construction (removing Severn), or P2b seeds with P6
     at split ordinary primes.
   - DEG_L: a uniform bound on J on a dense set of CM points, or the S-14 semiregular complex (Markman-type).
   - JAC1964: Th. 4 beyond abelian varieties; Th. 5 on the cubic fourfold pencil (E ≠ 0); the P²×P² nodal terms; the
     arithmetic sibling (Q35-full).
   - GHOSTS: the first place a ghost could live, a Hodge class on a simple non-CM abelian sixfold of exceptional
     Mumford-Tate type, bounded at ordinary primes through canonical lifts (C07, conditional on 032).
4. **K17 successor (prompt 31).**
   - The Soulé 2003 comparison.
   - A literature search on Ihara under Vandiver, with Fukaya-Kato (published) and Wake-Wang-Erickson attached.
   - The K_12 gate by Voronoi homology of GL_9 and GL_10.
   - gcd certificates n_7, n_11 for k = 3, 4, 5.
   - The Greenberg-extension route at non-Vandiver primes.
5. **AN_GRH successor (prompt 30).**
   - Theta incidence as the main question, framed as an Artin-type problem for #J(F_{Q^d}) under M (A17).
   - Section surjectivity and higher dimension on cote 149.
   - A literature check of A05, A18, A19.
   - Attach ANABELIAN_A1 cp03 and the successor finals.
6. **DP_MULT successor (prompt 34).**
   - Selected harmonic operators and non-primitive mixed lines against DP42's ceiling.
   - The sign of g_j − e_j − H in DP44's cost formula.
   - SGA 7 I, Exp. VII-VIII as the framework locator.
7. **TRACE_DET successor (prompt 33).**
   - A full check of MAS-10.
   - Q-DIRECT-BRIDGE (DET-05, DET-13, DET-14 at varying level).
   - The cote 1 images as a transcription task.
   - Q-MAS-INFINITE-BASIS and R-MAS-KERNEL as the two concrete tests of Masullo's draft.
8. **GRH_NIGHT successor.**
   - The two Masullo gates.
   - Alpöge's method for one order-r Kummer Hecke character over Q(ζ_r) (CX-ALG-024).
   - Split the input column into A, M and other.
9. **CX_GRH successor.**
   - A log-free zero-density estimate for ζ_E uniform at exponential degree, or Lang-Weil on the field of definition of a
     component (the A_D route of Koiran).
10. **GCT successors (prompts 23, 25, 26, 27, 36; prompt 44 BR_PENCIL).**
    - ALPOGE_GCT: PH2 for the cubic family (the 1/24 gate) through the Weyl-Brion expansion and the n = 5 ball-quotient
      ring; the Kudla-Millson/Borcherds comparison with Alpöge's lifts.
    - GCT_PLETH: the central region of outer degree five; the interpolation route at k = 6; the Foulkes-Howe annihilator
      for r = 3, 4.
    - GCT_KRON and CUE_GCT: one shared ledger of the multiplicity-obstruction range (m, n). Make R-14's gaps explicit at
      (8, 9). Pad A-030's Hessian covariant. Give a full proof of F-016. Recompute the LMR p. 476 values.
    - GCT_GINEQ: F-23 with more than one substituted dimension (Koszul flattenings of pencils); the GL-invariant
      Kempf-Ness use of α.
    - Prompt 44: certify seeds with R-13's Jacobian-rank method.
11. **Archive research (prompt 14's successor, the SA08 C.3 line).**
    - Cote 136 (a) and terminality over Z by the arithmetic fracture square.
    - The strict-versus-homotopy reading of « 'égalise' ».
    - Cote 123: the literature search for the A_{2m} exclusion.
12. **LM7_PUSH / DELTA successor.** Fable's suggestion 1 as one item: prove Δ = χ₁₂ ∘ u from E.65, express ε₂ and ε₃ as
    local symbols, evaluate on E.58, and decide whether hexagon and pentagon force ε₂ = ε₃. This waits on the DELTA23
    checkpoint and its Fable expert, the user's call.

## 8. What was integrated, and what is left open

- **The log:** `field_experts\intake_20261121\INTEGRATION_LOG_20261121.tsv`, three rounds.
- **Edits made in our files:**
  - the bridges ledger (Q01-Q09);
  - BRIDGES_20261120.tex (Q04, F1);
  - Fable's suggestions 2, 4, 5, 6, 7, 9;
  - the Hodge sketch (3.1-3.6, Routes 1-5, T5-T9, section 5);
  - SA17's study, hunches and packages (cote 133);
  - the SA06, SA07, SA08, SA19, SA20 and SA23 records;
  - the DER_LOCALIZERS, RESIDUE and REVLOC intakes;
  - the war-game hunches H8, H9;
  - the 14 Nov anabelian intake (A1);
  - note E1;
  - the CX_GRH, ZETA_TWO, ALPOGE_BRIDGES, GCT_NSRH, HECKE_DIV and HODGE_SIGN intakes.
- **Left open for lack of a target file:**
  - an LM6 intake carrying A.44-A.45;
  - a cote 123 archive note;
  - companion notes for cotes 1, 14, 16, 60 and 149;
  - a standing Masullo defect register (section 3.13 holds it for now);
  - the shared GCT row-gate ledger.
- **For the second pass of the transcription:**
  - cote 1 (16 rows);
  - cote 133 (9 rows);
  - cote 149 (scans 36, 80-85);
  - cote 16 (014-017, 034-038);
  - cote 44 (002, 004);
  - cote 34;
  - cote 54 (scans 5, 7);
  - cote 47 (scan 9).
  - The text of record was not edited.

## 9. Round 4 (21 Nov, ~06:00 UTC)

**Sources.** In `field_experts\intake_20261121\intakes\`:
- the new intakes ZETA_NEXT (prompt 43, final), BR_PENCIL (prompt 44, cp01) and SIGN_NEXT;
- GRH_NIGHT part 2 (cp04);
- the part-3 files of ALPOGE_BRIDGES (cp06), ALPOGE_GCT (cp06), GCT_PLETH, GCT_NSRH (cp06), K17 (cp05), DP_MULT, THETA3
  and CUE_GCT (cp04).

Every intake is by Claude Opus 5.5 at effort high. The register numbers are those of `field_experts\HEXAGON_CANDIDATES.md`,
"Round 4 of the intake".

### 9.1 Zeta functions over Z, Λ-schemes and the non-CM gate (ZETA_NEXT)

- **Established (confirmed):** NX01-NX04, NX-L01, NX-L04, NX-L06 given NX-L03, NX-L07.
  - NX01: for every normal K ≠ Q, κ_K = Res_{s=1}ζ_K > 1/(173 log D_K), under A, by Stark's 1974 descent of a real zero
    to a quadratic subfield.
  - NX02: degree-n version with n!.
  - NX03: effective Brauer-Siegel for normal fields.
  - NX04: h_K ≤ √D_K(1 + ½ log D_K)^{n−1}, unconditional.
  - These are transfers of Stark and Garcia-Lee, now with an absolute constant.
- **Proof read, cited theorems carried:** NC01 and NC03.
  - NC03 makes Tsimerman's Galois-orbit lower bounds for CM points in A_g effective, with exponent 1/(16384g³), from A
    alone. Earlier effective versions assumed GRH for the CM fields.
  - NC04, exponent 1/(28672g⁴), is at statement level.
  - André-Oort itself is not made effective: the Pila-Wilkie counting step stays ineffective.
- **Λ-schemes.**
  - **Supersedes §2's corrected gloss and §3.1's conjecture:**
    - the conjecture "every bad-fibre factor is (1 − ζp^{j−s})^{±1}" is refuted for nonseparated Λ-schemes (NX-L01,
      confirmed: two copies of A^d_Z glued along A^d − |Z|; for y² = x³ − x over F₅ the bad factor has inverse roots of
      modulus √5);
    - Z[ζ₅], and abelian rings of integers in general, are not Λ-rings, though their local factors are cyclotomic (NX-L07,
      confirmed). The ZETA_TWO intake had listed them among the cases where the conjecture holds.
  - **For proper flat Λ-schemes**, the run proves that every bad fibre is integral Artin-Tate and that every non-real zero
    or pole of ζ_X lies on Re s ∈ ½Z: the global ones on j + ½ by A, the local ones on integers.
    - NX-L03 is at statement level, and so is NX-L02's perfectoid step.
    - NX-L06 is confirmed given NX-L03.
  - The separated nonproper case is open.
- **The non-CM gate.**
  - NG01, at statement level, gives the canonical splitting M = C(M) ⊕ N(M) for abelian-type motives (Deligne-Milne). It
    closes ZT06's one-clause gap for every abelian-type piece.
  - NG07 (statement level, by computation): Jac(y³ = x⁵ − x − 1), absolutely simple and non-CM, has a rank-two CM summand
    in h⁴. So the Q02 gate concerns N(M), not h¹.

### 9.2 Border rank (BR_PENCIL)

- **Established:** BR(det_4) ≥ 42 and BR(per_4) ≥ 42, as CP border rank in (C^16)^{⊗4}, hence also symmetric border rank
  (R-05).
- **The proof:** multidimensional substitution BR(T) ≥ q − j + μ_j (R-01), the torus reduction to coordinate subsets (P-01)
  and the fifth minimum μ_5 = 11.
- **The checks:**
  - 14 findings were confirmed by proof check.
  - The decisive step was re-proved by an independent exhaustive enumeration over all 376,992 five-subsets.
  - The exceptional permanent orbit (R-04) was recomputed exactly over Q.
- **Supersedes §3.10's "≥ 39"** (GCT_GINEQ F-23, which stays as the case j = 1).
- **In Grothendieck's terms:** R-01 is the avoidance of closed relative secant loci in Grassmannians, as proper images (EGA
  II 5.4-5.5), over every algebraically closed field.
- **Open:** 43, which would follow from μ_7 = 14 (Q-07).

### 9.3 Cotes 16 and 44 (SIGN_NEXT)

- **Scan 050, the Proposition.**
  - The literal lower-Gysin reading fails (SN-C02, confirmed, on P¹×P¹).
  - The corrected form is C_G(X) ⟺ C_G(Y) + R₀ + L_T·j_*-surjectivity on a hyperplane section W of X×X (SN-C03/C04,
    confirmed). This is Kleiman 1968, Th. 2.13, with the missing L_T restored.
  - The letter `\unsure{C|A}` in our `16_scan050.tex` should read C. That is a row for the second pass, rated high on the
    mathematics, image not checked.
- **Conditional on 032:** C and I hold for abelian varieties (SN-11, confirmed as a cited deduction, 032 → Milne 2002
  Th. 3.3 → Kleiman).
  - U-02 is refuted literally by an explicit simple CM fourfold whose Weil lines are not divisor-generated (SN-12,
    confirmed).
- **What the sign-only method cannot give:** trace data alone, even with correspondence coefficients, cannot give scan
  049's positivity (SN-14, confirmed).
- **Cote 16, scan 014 (no 7):** the indices of Z[L,D] in Grothendieck's actual exterior order Φ₀ ⊂ End(ΛM₀) are 1, 2⁷,
  2²⁷3⁴, 2⁸¹3³³ for n = 1-4 (IF-03, independently recomputed). This supersedes, for the actual model, the string-model
  indices of §5 item 6.
  - IF-01, the integral Fock intertwiner, is confirmed.
- **Cote 44, Th. 5:** the corrected formula is proved a second time, independently (SN-44-01, confirmed; the same correction
  as JAC1964 H9-T1). On P²×P² each of the three nodes contributes 1, so 0 = 3 − (1+1+1) (SN-44-04, rederived).
  - H04 is complete mathematically.
  - The Néron-Tate identification rests on Kahn 2024 and Chen's preprint; the formula as an identity for Kahn's geometric
    height does not.

### 9.4 GRH_NIGHT part 2: factoring, Masullo §9 and cote 1

- **Factoring (supersedes §3.9's factoring gate in degree dependence).**
  - If OpenAI's PF26 (*Deterministic Polynomial Factorization over Prime Fields*, 4 Oct 2026, Thm 1.2, Prop 10.1) holds,
    then under M deterministic factoring over a supplied F_{p^m} is polynomial, poly(d, m log p) (CX-ALG-027, confirmed as a
    transfer, PF26 not opened).
  - Its GRH localizes to A plus RH for the pure fields Q(p^{1/r}) at the bad primes r (CX-ALG-028, partly read).
  - PF26 is an outside unrefereed preprint: a separate input class.
- **Masullo.**
  - The run reports §9's infrastructure repaired unconditionally (MT-M18, MT-M19, MT-M24, MT-M26, statement level).
  - MT-M20 (confirmed given M18/M19): for a fixed L(s, η), GRH with simple zeros is equivalent to a faithful positive
    completion of the full jet quotient.
  - MT-M23: such a completion fails for ζ_L, L nonabelian, by Hu-Kaneko-Martin-Schildkraut's multiple zeros (immediate from
    ζ_L = ∏ L(ρ)^{dim ρ}).
  - So a "Hilbert-Pólya" reading of cote 1 with a faithful positive B cannot go beyond the abelian case. Scalar trace
    positivity is the most it can give.
  - The open defects of the draft are now §12.3-§12.4 and the blank 13.3.1.2. §3.13's §9.3.2 entries stand as "false as
    stated"; their repair is the run's, not checked.
- **Cote 149 (statement level):** AG-Q28 is refuted on a type (0,4) family over y² = x³ − x. This bears on the normal-bundle
  Kummer route, not on A1.

### 9.5 The part-3 files

- **ALPOGE_BRIDGES cp06, cote 136.**
  - Terminality holds over every ring with finitely many non-unit primes (AQ-136-SEMILOCAL). Step 1, the arithmetic
    fracture sequence, is confirmed; the rest is at statement level.
  - That is §3.12's fracture-square attack, carried out for finitely many primes. Z needs uniform weight cutoffs as P grows.
  - **Scope flag:** the abelian-sector results (G-STD-HDG, the abelian AQ-Q-15 rows, BR-EFF) rest on three cited 2026
    preprints (van Hoften-Sempliner 2610.00259v2; Madapusi 2610.00226v1; Milne 2611.00244v1). They are a fourth input
    class, neither A nor M; the tag is now in the ZETA_TWO intake §3.
- **K17 cp05 (statement level).**
  - Ihara's kernel question needs only X^+ finite, Greenberg's conjecture (K17-GREENBERG-KERNEL). No new primes.
  - Cote 149, scan 85: the geometric tangential sections are recognized exactly when the generic arithmetic marking of scans
    83-84 is kept, and not without it (F149-GENERIC, F149-MARKED-RECOGNITION, F149-UNMARKED-CURVE). This is the first full
    answer our runs give to a question on that sheet.
  - K_12(Z) now reduces to three Steinberg groups at ranks 8, 9 and 10 (K17-K12-THREE-RANKS). **This supersedes §3.6's
    two-rank form.** The run reports a gap in DEKM's published enumeration, which it handled conservatively. That gap is
    **unverified** and is not to be reported to anyone before it is checked.
- **DP_MULT (statement level).**
  - DP51: over every polynomial selection, including the source's `HaO` submodule, the universal slope is
    c_* = 1/((p−1)(p^{h−1}+1)) < ρ_2.
  - DP50: p-divisible tensor exponents are cancelled by the source normalization.
  - So every local route to a shorter step-8 chain through higher height is closed. Only the global lift count (DP44,
    DP52) is open.
- **ALPOGE_GCT cp06.**
  - P-F31 is unchanged.
  - The P-F42 extension is confirmed: the refutation route for PH2/SH(a) on the cubic family is narrowed to the lower four
    fifths of B_n's coefficients (P-F42ah-ak).
  - The next attack is Kirwan's partial desingularization of P(Sym³V*)//SL_n, to bound the lower Todd-class coefficients.
  - SH(b) is untouched (P-F48).
- **GCT_NSRH cp06.**
  - F57 is confirmed with an exact recomputation: a P-word ω on the rank-four simple module N^# has trace with coefficient
    −1 at v^{±18}.
  - INT-NSRH-4: the same ω leaves the C⊗C cone. **The positive word basis of part 1 (INT-NSRH-2) is a rank-three
    phenomenon.**
  - Whether Ȟ₄ has some basis in the cone is open (IV, Remark 11.19).
  - The part-1 identification of the cone with simple objects in graded category O is withdrawn as unjustified.
- **CUE_GCT cp04:** the claimed range of R-14's four-row gaps reaches every fixed n/m < √2 (R-22, statement level). The
  dimension method cannot pass √2.
- **GCT_PLETH:** outer degree five nonvanishing is decided (G-031, strict chamber by computation). R-031 is known
  (Cheung-Ikenmeyer-Mkrtchyan, Ikenmeyer).
- **THETA3:** C25 is a geometrically simple Q(i)-Weil fourfold as a test object (statement level). 1.7 is still partly
  proved.

### 9.6 Hexagon candidates, as the register now numbers them

| # | Candidate | Change in round 4 | Gate left |
|---|---|---|---|
| H01 | sign-only purity | v2: an SN-14 remark, the locator "cote 16, scans 034-040", F50 folded in | the user's check of v2 |
| H02 | PH3 fails (P-F31) | unchanged (cp06) | the run's final; a literature search |
| H03 | **border rank ≥ 42 for det_4 and per_4** (BR_PENCIL R-05) | strengthened from 39; independent re-proof by enumeration; two literature searches found nothing ≥ 39 | the run's final (does it reach 43?); a write-up. One gate away; flagged |
| H04 | cote 44 Th. 5 fails, and the corrected formula | **complete mathematically** (SN-44-01 with H9-T1; SN-44-04) | the scan-004 image; the run's final; the write-up |
| H06b | Greenberg (formerly Vandiver) ⇒ Ihara | strengthened (statement level) | a literature search; intake reads of POLE-GENERAL and GREENBERG-KERNEL; FK/WWE against their texts; an independent re-proof |
| H09 | divided powers in step 2 | complete in content (DP51) | the run's final; a literature search; DP41 and DP51 read in full; one independent computation |
| H15 | **effective Tsimerman bounds for CM points in A_g** (ZETA_NEXT NC03-NC04, with NX01-NX03) | new | NC02 and NC04 read in full; a literature search (Tsimerman 2012; any 2026 version); an independent check of the constants. Timely |
| H16 | **cote 149, scan 85 answered** (K17 F149-*) | new | an intake read of the proofs; a literature search (tangential section conjecture: Nakamura, Hoshi, Saïdi); the scan images |
| — | the factoring reduction | superseded by the PF26 route (CX-ALG-028) | a check of PF26; a literature search; a re-proof of CX-ALG-028 |
| — | MT-M20/M23 (no faithful positive full-jet realization for nonabelian L) | possible new candidate | an intake check of MT-M18/M19; a literature search |

H05, H07, H08, H10-H14 are unchanged. H14's claimed range grows with R-22 (unread).

### 9.7 Seeds added by round 4

- **ZETA_NEXT successor.**
  - Effective André-Oort for A_g: NC04 with an effective point-counting theorem (Binyamini; Binyamini-Schmidt-Yafaev).
  - Separated nonproper Λ-schemes.
  - NG07's CM character.
- **BR_PENCIL successor:** μ_7 = 14 (bound 43); the b = 3 slices; R-06 for general n.
- **SIGN_NEXT successor:** Q6g-GLOBAL-GEOMETRY through IF-08's transported block matrices.
- **GRH_NIGHT successor:**
  - attach PF26 and ask for its own analytic hypothesis and an independent check of its Thm 1.2;
  - Masullo's §12.3-§12.4 intertwiner as the main question.
- **ALPOGE_BRIDGES successor:** Z for cote 136, with the uniformity-in-P obstruction.
- **K17 successor:** the three Voronoi computations at ranks 8-10, localized at 13!; a full read of F149-MARKED-RECOGNITION
  with the tangential-section literature.
- **DP_MULT successor:** only the global lift count.
- **ALPOGE_GCT successor:** PH2 through Kirwan's desingularization.
- **GCT_NSRH successor:** an exact linear-programming search for a C⊗C-cone basis of Ȟ₄.
- **CUE_GCT successor:** five-variable projections.
- **THETA3 successor:** the quartic cup test F_X of C27 on one cover over C25.

**Integration of round 4:** 33 rows in the log.
- 9 applied:
  - the ZETA_TWO intake §5.2 and §3;
  - SA06 B.4e;
  - the GCT_GINEQ intake (F-23 superseded);
  - the Hodge sketch 3.2, 3.4 and Route 4;
  - the HODGE_SIGN intake (U-rows);
  - SA19's cote 44 note.
- 14 pending, at statement level in the intakes.
- 1 transcription row (cote 16, scan 050).
- 2 open: an LM6 intake; the GCT row-gate ledger.
- The rest: for the successors, already in the register, or in the runs' own returns.
