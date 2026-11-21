# Intake of ALPOGE_BRIDGES (prompt 22, "Alpöge's RH and GRH bridged into Grothendieck's programme"), checkpoint 01, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), a parent agent and delegated sub-researchers. It started 20 Nov
23:01:47 UTC and **is still going**. This intake reads a 45-minute snapshot.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ALPOGE_BRIDGES_checkpoint_01_20261120T2346Z_unzipped`. This was the newest present
  at the start and again at the end of this intake (the run's checkpoint 01, made 23:46:48 UTC after 45 min of work). No
  final exists.
- **Prompt as sent:** `SENT\22_ALPOGE_RH_bridges_into_the_programme\PROMPT.md` (read in full).
- **Read:** CHECKPOINT_STATUS.md, LEDGER.md (full: 58 question rows, gates, approaches), the head of IMPLICATIONS.md,
  `research/root_core.tex` (all 607 lines), and `research/consequences_criteria.md` §§1-3 (lines 9-260). I grepped the
  statements of AQ-FINITE (`archive_questions.md`) and of F-SM-01/02/13 (`source_and_masullo.md`,
  `source_masullo_numeric.md`).
- **Not read:** the assembled `ALPOGE_BRIDGES.tex` (it assembles the modules above), `archive_questions.md/.tex` beyond
  AQ-FINITE's statement, the stable-curve and GT addenda, `root_weight_criterion.tex`, `root_deligne.tex`,
  `root_methods.tex`, `source_masullo_numeric.tex`, CC §§4-7, and the 530 KB inventory.
- **Read in full, with every step of the proof checked (14 findings):** BR-AT-01, BR-MIX-01, BR-TR-01, BR-TR-02, BR-WM-01,
  BR-NODE-01, BR-DER-01, BR-DER-02, BR-ANA-01, CC-F02, CC-F03, CC-F03b, CC-C01 and CC-C02 (as scope statements).
- **Read at the level of the statement:** CC-F01, CC-F01b, CC-C03 to C08, AQ-FINITE, F-SM-01, F-SM-02, F-SM-13, and the
  ledger rows (BR-WM-02, BR-DET-01/02, CC-ST01-03, CC-GT03, CC-P01-P09, CC-F04-F06, AQ-*). I take their states as the
  run reports them.

**Settled and still moving.** At checkpoint 01:
- *Settled:* the abelian Artin-Tate block (R-AT); the refutations R-MIX, R-ANA and R-DER-TATE; the cote 1 trace reading
  (R-TR); the classical-consequence scope map (R-CL-SCOPE); and several archive questions (AQ-Q-15-EXIST, 18-TWIST,
  18-STRONG, 18-REAL, 67-ISO, 67-INV-*, FINITE, SA08-D031).
- *In progress:* R-134-LINEAR; R-RESIDUE (its categorical comparisons); R-KGROUP ("assertion not yet specified"); R-MAS-NUM
  and R-MAS-KERNEL; R-GTHAT; D-WM; and the original-scan identifications for cotes 14 and 134-8.
- No three-hour review was due, and no PDF had been built.

## 1. Verdicts, finding by finding

| id | statement (short) | uses | verdict |
|---|---|---|---|
| BR-AT-01 | L(⊕(χ⊗Q(n))^m, s) = ∏ L(χ, s+n)^m; nontrivial zeros on Re s = 1/2 − n, none cancelled by poles; mixed objects: good-prime L equals that of gr^W; deleted factors add zeros on Re s = −n | A_D | **confirmed** (Euler factors; poles at integer real part versus zeros at half-integer real part). It is the same result as our bridges F1/F2 of 20 Nov. |
| BR-MIX-01 | the Kummer motive K(2) and Q(0)⊕Q(1) are non-isomorphic with the same good Euler factors | none (Deligne-Goncharov §1.1, Prop 1.7) | **confirmed** (v₂(2) ≠ 0 makes the class nonzero in Q^×⊗Q). It is standard: good-prime L-data see only gr^W. |
| BR-TR-01 | F(w) = Ξ(√w)/Ξ(0) = det(I − wB) with B = diag(t_j^{−2}) trace class; RH ⇔ B ≥ 0 for this normal realization; other realizations need not be self-adjoint; Ξ(t) is no Fredholm determinant in affine t | RH (A_D) | **confirmed**: Σ\|t_j\|^{−2} < ∞; order ≤ 1/2 gives genus 0; the finite-rank Jordan perturbation; Σ 1/\|ρ − a\| diverges by Riemann-von Mangoldt. The classical reformulation; its value is the exact reading of cote 1. |
| BR-TR-02 | under RH the Hankel matrices of m_r = Σ b_j^{r+1} are positive definite, and (−1)^r H^{(r)}(x) > 0 | RH | **confirmed** (a positive discrete measure with infinite support). Elementary. |
| BR-WM-01 | the Frobenius determinant and FNF^{−1} = q^{−1}N do not determine monodromy purity | none | **confirmed** (two-dimensional example, monodromy filtration computed correctly). |
| BR-NODE-01 | for a split nodal curve, 0 → H¹(Γ) → H¹(C) → ⊕ H¹(C_v) → 0, with weights 0 and 1 | none (Weil for curves) | **confirmed** (normalization sequence). Standard. |
| BR-DER-01 | for a presentable stable Q-linear 𝒞 with unit 𝟏, hocolim of the constant 𝟏 detects exactly the rational homology equivalences | none | **confirmed** (splitting of complexes over Q; retract argument). |
| BR-DER-02 | M(G_m) ≃ 𝟏 ⊕ 𝟏(1)[1], so the DER_LOCALIZERS intake formula needs the *reduced* motive | none (Voevodsky 2000) | **confirmed** (Mayer-Vietoris on P¹; Pic(k) = 0). A correction to our DER_LOCALIZERS intake. |
| BR-ANA-01 | U₂ = P¹∖{0,1,∞,2} and U₃ = P¹∖{0,1,∞,3} are non-isomorphic over Q̄ with the same ℓ-adic cohomology and the same zeta at every p ∉ {2,3} | none | **confirmed** (the cross-ratio orbits {2,−1,1/2} and {3,−2,1/3,−1/2,3/2,2/3} are disjoint; the point count is p^r − 3). |
| CC-C01 | LO77 Thm 1.1 for L/K holds under A_D when L/Q is abelian, not merely when L/K is abelian | A_D; M otherwise | **confirmed** as a scope statement; it agrees with CX_GRH CX-K01. |
| CC-C02 | a prime in every class a mod q below (φ(q) log q)² (LLS 2016 v3 Cor 1.2) | A_D | confirmed as scope; LLS not opened. |
| CC-C03 to C08 | Miller (A_D); Bach's witnesses (A_D) versus the class-group corollary (Hecke); Littlewood, LLS h(−q) bound (A_D); Cramér, Selberg, Montgomery (RH) | as stated | statement level; the scope assignments are right. CC-C04 records honestly that the original Bach 1990 article was not retrieved (HTTP 403); CX_GRH did retrieve it (Thm 2 p. 372; Thm 4 p. 375 and corollary p. 376), so that gate can be closed by citing CX_GRH CX-N01/N07. |
| CC-F02 | an effective Siegel bound L(1,χ) ≥ c_ε q^{−ε} with an algorithm for c_ε | A_D | **confirmed** (LLS Thm 1.5 for q ≥ 10^{10}, plus a certified finite check below Q). Classical in substance: Littlewood 1928 gives L(1,χ) ≫ 1/log log q under GRH. |
| CC-F03 | over K = Q(√−23) the class character of the cubic H/K (H the splitting field of x³−x−1) induces an irreducible two-dimensional Artin representation of S₃ | none | **confirmed**: the factorization (x−10)²(x−3) mod 23 checks; H/K is unramified; character norm 1. |
| CC-F03b | if H_K/Q is abelian (for instance K imaginary quadratic with 2-torsion class group), the class-character L-functions are Dirichlet products | A_D | **confirmed** (the semidirect product with inversion). |
| CC-F01, CC-F01b | for a Λ-scheme in Borger's sense (smooth proper over Z[1/M], resp. separated of finite type over Z) the rational ℓ-adic cohomology is a sum of χ⊗Q_ℓ(−m) with χ of finite abelian image, so its L-data satisfy RH by A_D | A_D | **statement level**. The deduction from Borger (2009) Thm 0.1, Thm 5.3 and Cor 6.2 was not checked against Borger. The run's "weight-space descent" in F01b is the step to check before this is used. |
| AQ-FINITE | two semisimple abelian Artin-Tate motives with Artin parts through (Z/N)^× are isomorphic iff their Frobenius traces agree at all good primes below B = (φ(Q) log Q)², Q = lcm(N,4) | A_D (LLS) | statement level; the mechanism is right (one prime in every residue class determines every character). |
| F-SM-01, F-SM-02 | a full zero trace equal to its restrictions to narrow strips forces the zeros onto the line; the shrinking-strip identity is equivalent to GRH for a fixed character | none / A_D | statement level (the parent agent read F-SM-01 independently, by the run's record). |
| F-SM-13 | the exact numerical statement of Masullo's Thm 12.5.1.1 (pp. 519-520) holds for Q and every allowed test function, from A_D | A_D | statement level. If it holds, it cross-checks the two proofs: Masullo's trace identity over Q is true. It does not check his operator realization, and the run says so. |

**Counts at checkpoint 01.**
- Confirmed with every step checked: 14 findings (BR-AT-01, BR-MIX-01, BR-TR-01, BR-TR-02, BR-WM-01, BR-NODE-01,
  BR-DER-01, BR-DER-02, BR-ANA-01, CC-F02, CC-F03, CC-F03b; CC-C01 and CC-C02 as scope).
- Statement level, no fault found: the rest that I touched (CC-F01, CC-F01b, CC-C03 to C08, AQ-FINITE, F-SM-01, F-SM-02,
  F-SM-13) and the ledger rows.
- Gaps: 0. Refuted: 0.

## 2. What is new

- **Against the literature.** Little of the confirmed part is new mathematics. BR-AT-01, BR-MIX-01, BR-TR-01/02, BR-NODE-01,
  BR-DER-02 and CC-F02 are standard, and BR-ANA-01 is an elementary example. Their value is exact scope: they say where
  Alpöge's theorem reaches, and they correct three of our intakes:
  - DER_LOCALIZERS (the reduced motive: BR-DER-02);
  - RESIDUE H.3-H.6 (the singular fibre is not the nearby fibre: BR-NODE-01);
  - SA23 §4.1 (cote 1/079-080, 111-112 contain no ξ and no RH, and the RH use is a later application: BR-TR-01).

  Two items may be genuinely new and deserve the check they have not had:
  - CC-F01b (every Λ-scheme of finite type over Z has abelian Artin-Tate rational cohomology, hence RH for its L-data
    from A_D alone);
  - F-SM-13 (Masullo's Theorem 12.5.1.1 over Q follows from Alpöge).
- **Against tonight's other run (CX_GRH).** The two runs agree independently:
  - LO77 needs RH for the top field (CC-C01, CX-K01);
  - a non-abelian cubic obstructs the Dirichlet factorization (CC-F03 with x³−x−1, CX-R02 with x³−2);
  - the class-group corollary needs Hecke characters (CC-C04, CX-N07);
  - Masullo's 13.3.1.2 has no body (source_and_masullo; CX_GRH §1.1).

  CX_GRH retrieved the original Bach 1990, which closes CC-C04's bibliographical gate.
- **Against our own results.**
  - BR-AT-01 is our bridges F1/F2 again.
  - Bridges Q03 (34/64) is still "open" here as well. R-WM and D-WM restate the gate as purity in the geometric case, as
    our Q03 did.
  - Bridges Q06 (step 17) is still unspecified (R-KGROUP).

## 3. The scope of the two proofs

- **A_D (theorem):** BR-AT-01, BR-TR-01/02 (RH), CC-F01/F01b, CC-F02, CC-F03b, CC-C01 (abelian top field), CC-C02, CC-C03,
  CC-C05 to C08, AQ-FINITE, F-SM-13, and AQ-CM-HEX's trace-zero primes. For the CM curve over Q(ω), the trace-zero primes
  are the primes inert in Q(√−3): a Dirichlet condition.
- **M (conditional):** the general case of CC-C01, the class-group part of CC-C04, and Hecke-character GRH over non-abelian
  class fields (CC-F03). The run does not use M as an input anywhere I read; it compares Masullo's route but does not
  build on it.
- **More than both:** the run correctly marks as outside both:
  - the L-function of the CM elliptic curve, a Hecke character of infinite type (AQ-CM-HEX: "DirichletGRH does not
    directly cover the nonzero-infinity-type CM Hecke L-function");
  - the weight-monodromy conjecture (R-WM);
  - the standard conjectures B and Hdg (G-STD-B, G-STD-HDG).

  Masullo's claim is about finite-order characters in our reading of it (CX_GRH §1.1), so it would not cover the CM
  L-function either. A successor should check whether his §1.2 includes Grössencharacters.
- **Flags:** none of the statements I read claims more than its input gives.

## 4. Integration: where each finding goes, and the attacks it opens

1. **Our intakes.** Each edit goes in the intake named, at the row named; I made no edit outside my folder.
   - **DER_LOCALIZERS intake:** at the G_m formula, replace Z_tr(G_m)[−1] by the reduced motive
     M̃(G_m)[−1] ≃ 𝟏(1) (BR-DER-02).
     - Next attack on the linear Thm(?) of cote 134-8/048-054: BR-DER-01 settles only constant rational coefficients. The
       open case is a localizer seen by a *non-constant* coefficient system, the reduced Tate object 𝟏(1). The test case
       is whether hocolim over A of the diagram constant at 𝟏(1) detects more than rational homology. It does not, since
       𝟏(1) is invertible, so the next interesting case is a non-invertible coefficient. The run's R-134-LINEAR is on
       this.
   - **RESIDUE intake, H.3-H.6:** add "ordinary H¹ of the singular fibre is H¹(Γ) ⊕ (weight 1); the weight-2 quotient
     belongs to the nearby fibre (BR-NODE-01)".
   - **SA23 intake, §4.1:** add "cote 1/079-080 and 111-112 prove the trace and Fredholm theorems; the ξ-determinant
     reading is ours (BR-TR-01). Under Alpöge, B = diag(t_j^{−2}) ≥ 0, but no geometric construction of B follows".
     - Next attack, for prompt 33's successor: build B from primes and correspondences, a Hilbert-Pólya operator that is
       not read off the zeros. The obstacle is exactly that BR-TR-01's B is defined by its spectrum. A trace formula with
       a positive kernel, for example Connes-Consani's archimedean Weil positivity (attached to prompt 22), gives B ≥ 0
       only on a test-function cone, which is the gap to measure.
2. **Bridges 20 Nov, `reports_20261120\alpoge_rh\bridges\QUESTIONS.tsv`.**
   - **Q01/Q02:** add "ALPOGE_BRIDGES BR-AT-01 (= F1/F2); CC-F01b: every finite-type Λ-scheme over Z, if CC-F01b checks".
     The attack it opens: CC-F01b turns "X has a Λ-structure" into "RH for ζ_X holds unconditionally".
     [Correction: that gloss is false; Spec Z[1/p] is a Λ-scheme and its ζ has the zeros 2πik/log p on Re s = 0
     (ZETA_TWO ZT05; DP_MULT DP11). Read: "CC-F01b gives RH for L(H_c(X_Q̄), s) with its canonical (inertia-invariant)
     Euler factors, A_D; ζ_X itself differs by the finite factor R_{X,S} of ZETA_TWO ZT04, whose divisors lie on lines
     Re s = v/2 (Weil II 3.3.1 on the bad fibres) and can be non-real (ZT05: Spec Z[1/p])." (corrected 21 Nov 2026
     after the intake of ZETA_TWO, Claude Opus 5.5 at effort high)] The next class to
     try is the schemes whose cohomology is abelian Artin-Tate without a Λ-structure, for instance toric varieties and
     their quotients by finite abelian groups, and cellular schemes over Z.
   - **Q06:** BR-MIX-01 shows why the L-data cannot compute the Ext groups of step 17. The gate stays with prompt 31.
3. **Cote 1/079-080 and 111-112** (BR-TR-01). The reading changes: these sheets are the analytic theorem, not an RH
   statement. Cote 34/64 and 74 are unchanged.
4. **Effective recognition (AQ-FINITE).** The bound (φ(Q) log Q)² is a ready certificate for the cyclotomic coordinate of
   the finite levels of GT̂₀. This was prompt 30's third item. Its successor should cite AQ-FINITE and CC-C02 and not
   re-derive them.
5. **Masullo cross-check (F-SM-13, F-SM-01/02).** These go into prompt 33's successor, alongside the empty 13.3.1.2 and
   the missing §12.3 deconstruction, both found by this run and, for 13.3.1.2, also by CX_GRH. The attack: the run names
   the exact missing step, trace-norm convergence or an integrable diagonal domination for the lifted kernel
   (R-MAS-KERNEL). That is a precise target for checking Masullo's draft, and it is the one place where our runs can test
   the draft rather than cite it.
6. **Prompts 30-35** are in `SENT\` (moved 21 Nov 00:04 +01:00). What this checkpoint feeds into their successors:
   - 30: CC-C01, CC-C02, AQ-FINITE;
   - 31: BR-MIX-01, R-KGROUP;
   - 32: BR-WM-01, G-STD-C (Katz-Messing), BR-NODE-01;
   - 33: BR-TR-01/02, F-SM-01/02/13, R-MAS-KERNEL;
   - 34: nothing yet;
   - 35: BR-AT-01, CC-F01/F01b, and the Brauer remark of the CX_GRH intake §3 (conditionally on M, every Artin L-function
     is zero- and pole-free off the line).

## 5. Prompt updates: what a successor of this run needs

1. **Language and framework.** The checkpoint already writes in the language of motives, ℓ-adic sheaves and weights; no
   translation is missing in what I read.
2. **The main question is barely moved.** The run has settled the scope (abelian Artin-Tate) and refuted reconstruction
   rules. Of the archive questions of Grothendieck and Deligne, it has settled mostly known cases (AQ-15-EXIST, 18-a-CM,
   18-b) and readings (18-TWIST, 18-REAL). A successor should be pointed at the open ones that A_D could actually touch:
   - Q03 at 34/64: the openness of [π₀, H], via Deligne's purity;
   - the effective forms at cote 149 (prompt 30);
   - AQ-Q-18-a-NONCM, the non-CM period gate, which is not an RH question and should be routed elsewhere.
3. **Check CC-F01b.** Ask for a full check of the weight-space descent from Borger Cor 6.2. If it holds, it is the most
   consequential item of this checkpoint: an unconditional RH for a whole geometric class of schemes over Z.
4. **Use CX_GRH's sources.** Attach CX_GRH's checked Bach 1990 locators (Thm 2 p. 372; Thm 4 p. 375; the corollary on
   p. 376) so that CC-C04's gate closes.
5. **Model and effort.** As for CX_GRH: the run writes "GPT-6 Astra Pro"; it is "GPT-6 Astra (ChatGPT Pro mode)".
6. **Re-intake the final.** This intake is of checkpoint 01 only. When the final lands, re-intake R-134-LINEAR, R-RESIDUE,
   R-KGROUP, R-MAS-KERNEL, BR-WM-02, BR-DET-01/02 and CC-ST01-03; resume this agent (af2a18f62da23b48e) for it, by the
   field-expert rule.
