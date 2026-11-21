# Intake of HODGE_SIGN (prompt 32): the sign-only proof of Weil and Deligne as the Hodge-index route of cotes 16 and 44

By Claude Opus 5.5 at effort high, launched by the main session (Claude Opus 5.5 at effort max), 21 Nov 2026, under
`field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`. Work file: `agent_notes\20261121_intake_HODGE_SIGN_NOTES.md`.
Check events: `INTAKE_HODGE_SIGN_20261121_CHECK_EVENTS.tsv` (same folder).

The run: GPT-6 Astra (ChatGPT Pro mode), root and three sub-agents (`/root/sign_geometry`, `/root/q03_openness`,
`/root/arithmetic_sl2`). The run writes "effort not exposed"; our records give it as GPT-6 Astra (ChatGPT Pro mode). It ran
from 00:14 to about 00:56 UTC on 21 Nov 2026, **42 minutes**. It saved no checkpoint, because it finished before the first
one was due at 00:59.

## 0. What I read, and my scope

**The return folder:** `grothendieck_archive_transcription_20261110\research_returns\HODGE_SIGN_final_20261121T0057Z_unzipped\`.
It is the final, and the only HODGE_SIGN folder present. It holds 3,330 files, 3,174 of them retrieved Lean sources
under `evidence\`.

**What I read:**
- `HODGE_SIGN.tex`, lines 60–1300, 1490–1740 and 2062–2600: Part I up to SL-04, SL-06 to SL-09, the Q03 section, and
  Part II;
- `README.md`, `LEDGER.md`, `QUESTIONS.tsv`, `IMPLICATIONS.md`, `TRANSCRIPTION_NOTES.tsv`, `SOURCE_CORRECTIONS.tsv` and
  `VERIFICATION.md`;
- `normalized_order_indices.py`;
- the counts of the run's `CHECK_EVENTS.tsv` (209 events);
- the prompt as sent.

**Our files for comparison:**
- the GCT_NSRH intake;
- the Hodge sketch, sections 0–2, Routes 3 and 4, and section 5;
- the task sections of prompts 37–41;
- in our text of record: cote 16 scans 034, 036, 038, 040, 049 and 050; cote 44 scan 004; cote 34 scan 064;
- the bridges run's `QUESTIONS.tsv`, rows Q03–Q05.

**Outside source:** Katz, *Affine cohomological transforms, perversity, and monodromy* (JAMS 6, 1993). I read pp. 179–181
(Lemma 3.0.1, Theorem 3.4, Corollary 3.4.1) and pp. 218–219 (Appendix A.1–A.3) in the author's PDF
(web.math.princeton.edu/~nmk/old/ACT.pdf).

**Scan numbering: checked.** The supplied `ARCHIVE_16_scan014–018`, `034–040`, `049`, `050`, cote 44 scans 002, 004, 008
and 009, and cote 34 scans 053, 057, 063, 064 and 074 are byte-identical to our
`text_of_record\pages\<cote>\<cote>_scanNNN.tex`. HODGE_SIGN cites them by file name, so **its cote 16 numbers are ours**.
The offset of one found in GCT_NSRH does not occur here. Every cote 16 locator of the run that I checked is right in our
numbering:
- 034, 036, 038 and 040 are handwritten: restriction, Gysin, E^{n−1}, Λ_Y;
- 035, 037 and 039 are printed material;
- 049 has C(X) + I(X×X) ⟹ semisimplicity;
- 050 announces "the deduction of the Weil conjectures from the conjectures C and A".

**Scope:**
- **Read in full with a targeted proof check (29):**
  - HS-01–HS-05;
  - SG-01–SG-11;
  - AR-01, AR-02, AR-03, AR-05;
  - SL-02, SL-04, SL-05, SL-07, SL-08;
  - Q3-01–Q3-04.
- **Recomputed independently with my own code (1):** SL-09.
- **Read at the level of the statement, with spot checks (9):**
  - HS-06, the source inspection of the Lean archive;
  - AR-04, a list of cited background;
  - SL-01, SL-03, SL-06;
  - Q3-05–Q3-08.

## 1. Verdicts, finding by finding

### The main result: a complete sign-only proof of Deligne's purity (Q1)

- **HS-01, effective power sums: confirmed.** The generating function has radius at least 1/B. A positive multiplicity
  gives a genuine pole at 1/λ_j. The proof needs no semisimplicity.
- **HS-02, tensor amplification: confirmed.** For fixed k, the limit in n comes first, then k → ∞, with c_k/k → 0. The
  constants, the dimension of K_k and the extension degree may all depend on k.
- **HS-03, path Parseval: confirmed.**
  - K K* = Q^d I holds because each b_i is nondegenerate and h ≠ 0.
  - The norms are: each kernel Q^{d/2}, each diagonal factor B, each endpoint vector B Q^{d/2}. The product is
    B^k Q^{d(k+1)/2}.
  - The zero mode is M^k. The remainder is at most B^k Q^{d(k+1)/2+1}.
  - This is the same estimate as GCT_NSRH F01, in the slightly weaker form.
- **SG-08, the effective Gysin remainder: confirmed. This is the decisive step.**
  - I rederived the whole computation:
    - Artin vanishing (SGA 4 XIV 3.1) with duality gives H_c^j(U) = 0 for j < d.
    - The dual of the restriction hypothesis is a Gysin map H_c^j(Y)(−1) → H_c^{j+2}(X). It is an isomorphism for
      j > D−1 and surjective for j = D−1.
    - The sign is (−1)^{D−1}R = Σ_a (−1)^a Tr W_a(−1) + Σ_b (−1)^b Tr T_b.
    - For a ≥ 1 the terms cancel in pairs, W_a(−1) ≅ T_{a+1}.
    - What remains is [W_0(−1)] − [T_1] = [K_k], plus T_0 = H_c^d(U,F)^{⊗k}, by Künneth in the lowest degree.
  - The edge case Y = ∅ is consistent.
  - **In Grothendieck's terms:** K_k = ker(H_c^{D−1}(Y)(−1) → H_c^{D+1}(X)) is the compact-support, affine form of his
    evanescent part E^{n−1}. Our scan 034 (end) writes E^{n−1} ≃ Ker(φ_{n−1}: H^{n−1}(Y) → H^{n+1}(X)), and our scan 036
    has the Corollaire Ker φ_* = E^{n−1}(Y). So the "definite sign" of Alpöge's step 5 has this meaning: the evanescent
    part of the hyperplane section enters the trace formula with the single sign (−1)^{dim Y}. All the rest of H^*(Y)
    cancels against X through Gysin. That is "one off" from (−1)^D on M^k.
  - The run does not name K_k as E^{n−1}. The translation above is mine.
- **SG-09, the affine middle-degree bound: confirmed.**
  - **The cited input, checked at its source.** Katz ACT, Corollary 3.4.1, p. 181: V a separated scheme of finite type,
    a local complete intersection of pure dimension d; f: V → A^1 arbitrary; π: V → A^n quasi-finite; F lisse. Then there
    is a dense open set of (A, b) for which H^a(V,F) → H^a(V ∩ (f + Aπ + b = 0), F) is an isomorphism for a < d−1 and
    injective for a = d−1. This is exactly the hypothesis of SG-08, with V = U^k, f the path form composed with π, and π the
    vertex-coordinate closed immersion.
  - **The input is weight-free.** Katz works over an algebraically closed field (p. 179). The appendix (Deligne's proof,
    pp. 218–219) uses the universal hyperplane, Künneth and generic base change; no Frobenius enters.
  - The other steps:
    - Bertini, through the graph immersion (z, f), with the last coefficient rescaled to 1, gives smoothness on a dense
      open.
    - Both opens are Galois-stable, so a point exists over some F_{q^{e_k}}.
    - Noether normalization (Stacks 00OY) bounds the fibre lengths by B.
    - The vertex weights a_{i,h} absorb the g_i. HS-03 then gives
      |R| ≤ (BC)^k q^{e_k n(k(w+d)/2 + d/2 + 1)}.
    - HS-01 and HS-02 finish.
- **SG-11, compact-support bounds for constructible sheaves: confirmed.** The bound is weight ≤ w+i on H_c^i.
  - Degrees i ≥ d+1: a generic smooth hyperplane section, by Katz 3.4.1 with f = 0, dualized; surjective at d+1, an
    isomorphism above. Then induction on the dimension.
  - General X: a stratification and the localization sequence in the same degree, so nothing is lost to a shift.
  - **What follows at once (mine, one line).** Weights ≤ w are a pointwise condition at closed points, and
    (Rf_!F)_s = RΓ_c(X_s, F_s) by proper base change (SGA 4 XVII 5.2.6, locator from memory). So SG-11 gives Deligne's
    Weil II, Théorème 3.3.1, over any base: Rf_! preserves mixedness of weights ≤ w.
- **SG-10, smooth proper purity: confirmed.** The upper bound comes from SG-11; the lower bound from Poincaré duality with
  F^∨ of weight −w. This is the absolute-value part of Weil I, Théorème 1.6, for smooth projective varieties. The proof
  uses no monodromy, no Lefschetz pencil, no Rankin–Selberg step, and no Hodge standard conjecture.
- **HS-04/HS-04B: confirmed.** I recomputed:
  - for xy = 1 in A^2: M = r, N = r − 1, R = −r;
  - for the Kummer example: M = −1, N = ε^n(q^n − 3), and R = (εq²)^n − 3(εq)^n − 1, so −R is not effective.

  So smoothness alone fails, and genericity is needed.
- **HS-05: confirmed.** The countermodel diag(1,1) against diag(1,−1) is elementary.

**My verdict on Q1.** Alpöge's footnote 3, made complete:
- generic weak Lefschetz and Gysin give an effective remainder;
- Parseval on the path form gives square-root size;
- tensor powers turn this into the Riemann hypothesis over finite fields.

It is proved, without weights, for H_c of every constructible sheaf, and for smooth proper purity. It also gives the
hypothesis (S2) of GCT_NSRH F03 geometrically, for every k. The "take k even" of the GCT_NSRH intake is not needed for
the general theorem.

### Item 2: the sign and the Hodge-index route (Q2)

- **SG-01: confirmed.**
  - I checked the self-intersection of a maximal plane: the coefficient of t^r in (1+t)^{r+1}/(1+2t) is (1+(−1)^r)/2.
    This holds for r = 1 and r = 2.
  - (a−b)² = 2(−1)^r.
  - The trace sign of E^{2r} is always +, while the raw square alternates.
  - On the cubic curve the evanescent form is alternating.

  The substantive point is not the quadric sign, which the Hodge–Riemann normalization (−1)^r absorbs. It is that the
  step-5 sign is defined in K_0 of Frobenius modules, with no pairing at all (SG-08).
- **SG-02: confirmed** (the cell count, the zeta function, ζ(s−3)).
- **SG-03: confirmed.** This is the positive-Rosati linear algebra. The cyclicity step and the minimal-polynomial step are
  right.
- **SG-04: confirmed.** The ingredients:
  - NS rank n² = dim H^{1,1};
  - H^{r,r} = Λ^rU ⊗ Λ^rW is spanned by products of (1,1) classes;
  - the ordinary case uses balanced monomials, since α/β is not a root of unity;
  - in the supersingular case the NS rank is C(2n,2) = dim H²;
  - rational descent goes through the intersection matrix.

  **Not new:** the Hodge conjecture for powers of an elliptic curve is classical (Tate; Murasaki 1969; Imai; from memory,
  to verify). The run does not say that it is known. The finite-field part is the classical Tate conjecture for E^n.
- **SG-05: confirmed as a deduction** from Milne's *Abelian varieties*, Theorems 13.2 and 14.1 and Theorem 11.1(b). I did
  not reopen those locators.
- **SG-06 and SG-07: confirmed.**
  - SG-06 is a factorization statement.
  - SG-07 uses j_*j^*ζ = d·hζ = 0 and that j_*: H^6(Y) → H^8(Q^6)(1) is an isomorphism (weak Lefschetz for an ample
    section).
  - That primitive middle classes restrict to zero on a hyperplane section is standard.

**My verdict on Q2.** The proposed identification (Fable's suggestion 4: the step-5 sign is the Hodge-index sign on the
evanescent part) is **refuted as an identification**. It agrees with the Hodge sketch, 3.6, and with the GCT_NSRH intake,
item 2. The run turns that reading into a theorem:
- the sign is the sign of the class of E^{n−1} in the Grothendieck group;
- the absolute values follow by Grothendieck's own hyperplane induction of cote 16, scans 034–040, together with Parseval;
- the route needs neither C (Λ algebraic) nor I(X×X), the inputs of scans 049–050.

So **Weil's theorem is proved by the induction of cote 16 without the Hodge standard conjecture**. That is not the route
of scans 049–050, and it proves nothing about B, C or I. For CM elliptic powers and quadrics, the index statement is
independently classical. The run left Q2c (higher-genus CM curves, all CM abelian varieties: U-02) at a gate; see
section 5.

### Item 4: cote 44 (Q4)

- **AR-01: confirmed. It refutes the displayed Th. 5 of cote 44 (our scan 004) and hunch H9(a).**
  - I rederived the whole example.
    - On P²×P², the class Z = a² − ab + b² has HZ = a³ + b³ = 0 and Z² = 3a²b².
    - The pencil diag(λ, λ+μ, λ+2μ) has three rank-two members, each with one ordinary double point at (e_i, e_i), off
      the base locus.
    - Its generic member is K-isomorphic to the flag threefold.
    - On the flag threefold, c(E) = 1 − a + a² gives a² − ab + b² = 0 in CH² (Fulton, Remark 3.2.4). The degree check
      also holds: Z|_Y·a = 0 − 1 + 1 = 0 and Z|_Y·b = 1 − 1 + 0 = 0.
  - Scan 004 states its hypotheses as: "ζ = Z.Y … alg. équiv. à 0 sur Y", with Y the generic member of a pencil "dont les
    fibres sont géom. intègres...". The example meets them, so ⟨ζ,ζ⟩ = 0 ≠ (−1)²·3. Grothendieck's struck "[au signe près
    ??]" and the trailing "..." are recorded in our text.
  - **What the example shows (mine; proved by localization, with the singular-fibre geometry from memory).**
    - Z restricts to zero on the generic fibre, so π^*Z on the blown-up total space is a sum of cycles supported on
      fibres.
    - Cycles i_*D with D Cartier on a fibre are isotropic and orthogonal to every vertical class, because O(F)|_F is
      trivial.
    - So Z² = 3 must come from Weil divisors that are not Q-Cartier on the three nodal fibres.
    - Here E = 0, since H³ of the flag threefold is 0. In that Lefschetz-pencil case (SGA 7 XVIII; Weil I §§4–5) the
      vanishing cycles are zero, and the nodal threefolds are not Q-factorial: a plane through the node is a Weil divisor
      that is not Q-Cartier.
    - Three singular fibres against Z² = 3 fits one unit each. I have not computed the contribution of each fibre.
  - So the missing qualification in Th. 5 is the correction from the singular fibres in the case E = 0. This is the
    higher analogue of Shioda's component corrections, carried by fibres that are geometrically integral.
- **AR-02 and AR-03: confirmed.** These are elementary countermodels.
  - In AR-03 the Green function shifts by t, deg(x·a(t)) = t/2 and a(t)² = 0, so the self-intersection is x² + t.
  - They show that slopes, norms and metrics do not fix the sign of a form.
- **AR-05: confirmed.** φ/d is integral of norm at most C/d, and the slope inequality gives
  log d ≤ μ_max(M) − μ(L) + log C. In equal rank: log[M:φL] ≤ r log C + deg M − deg L.
- **AR-04: statement level.** It lists cited background:
  - Moriwaki, Theorems A and B;
  - Künnemann 4.1;
  - Shioda 8.x;
  - Bost 4.5 and 4.6;
  - Milne, *Jacobian varieties*, 6.6.

  I did not reopen these locators. They are carried as background, without fault found. The run's read of the Lean
  `Formalism.F.SlopeInequality` is source inspection, as it says.

**Verdict on Q4.** The proposed arithmetic Hodge-index statement from steps 5 and 13 is **refuted as an implication**.
What remains true is the size inequality AR-05. No case of Th. 4 or Th. 5 is newly settled. Th. 4 for abelian varieties
comes from 032 Cor. 8.4 (claimed) through Milne (sketch, 3.4), not from this run.

### Item 5: cote 34, scan 064 (Q5)

- **Q3-01: confirmed.** The ambient group π′ is impossible: Spec F_q with H = 1; G_m over F_2 with H = Z_3(1). Our text
  of record reads "ouvert dans π′" (scan 064, line 17), so the refutation applies to the text as transcribed.
- **Q3-03 and Q3-04: confirmed.** H/[P,H] = (H^ab)_Γ is a quotient of I(ℓ)_Γ, which is finite by Theorem 1.1 (scan 053)
  for every open subgroup.
  - This is nearly tautological once 1.1 is in hand, which may be why Grothendieck struck the remark.
  - The real content is in the version with a section (Q3-05 and Q3-06): the subgroup generated by h^{−1}σ(h) does not
    contain [H,H] automatically.
- **Q3-02: confirmed** (finite coinvariants from a Frobenius with no eigenvalue 1).
- **Q3-05–Q3-08: statement level.** I read Q3-07 in part; the derived-series induction is sound in what I read.

**Verdict on Q5.** The BRIDGES Q03 row changes from "open" to:
- the literal statement is refuted (Q3-01);
- the canonical corrected statement is proved (Q3-04);
- the soluble version with a section is proved (Q3-05–06, statement level).

Only purity for curves is needed, not purity "en dim. quelconque".

### Item 6: the Lefschetz sl_2 (Q6)

- **SL-02: confirmed.** For i = 2 the block is J_n − I_n, with Smith form (1,…,1,n−1). L^n on H^0 is n!.
- **SL-04: confirmed.** DL^r v = r(d−r+1)L^{r−1}v. For n = 2, D²L²(1) = 4. This was already in our files (Hodge sketch,
  Route 4: "Λ₀²L₀² = 4 on H⁰ for n = 2"), so it is not new against our results.
- **SL-05: confirmed.** On Γ_0 the operator e^{(m)} sends y^{m+1} to (m+1)x^m y, so its invariant is m+1. On the binomial
  lattice Γ_1 the invariant is 1. Γ_1 is the image of the symmetric tensors, so it is stable.
- **SL-07: confirmed.** FL = qLF. A commuting Arthur factor cannot be the untwisted L; Tate twists remove this particular
  obstruction.
- **SL-08: confirmed.** B = 1 − LΛ_N is the projector to the string bottoms, Q_d is a bottom projector, and the matrix
  units are L^β Q_d Λ^α.
- **SL-09: independently recomputed: indices 1, 32 and 2^13·3^10 = 483,729,408.** With normalized lowering the index is 1.
  I wrote my own lattice closure with integer echelon forms (`scratchpad\hs\order_check.py`), without the run's code.
  - **Scope:** these are indices in the *string model* ∏ M_{n−i+1}(Z), one string per primitive degree. That is not
    Grothendieck's Φ₀ = Z[L₀, Λ₀] ⊂ End_Z(ΛM₀) on the actual exterior algebra (scan 014), whose strings come with
    multiplicities and an integral structure of their own.
- **SL-01 and SL-03: statement level.** The Wilson range t ≤ k ≤ v−t and the Ghorbani Corollary 3 locator were not
  checked. The SL-03 table was not recomputed.
- **SL-06: statement level** (the Lean `ColChain` and the step-10 local bound). This is source inspection, not a proof
  check.

**Verdict on Q6.**
- The unnormalized identification of the Arthur SL_2 with the Lefschetz sl_2 is **refuted** (SL-07).
- Rational data do not fix integral indices (SL-05).
- The normalized comparison, an integral intertwiner, is **left at a gate** (U-04 and U-05). The run delivered with it
  open after 42 minutes. See section 6.

### Counts

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 29 |
| Independent recomputation, confirmed | 1 (SL-09) |
| Statement level (carried as background without fault found) | 9 |
| A gap | 0 |
| Refuted | 0 |
| Framing corrected | 3: SG-04 is classical; the scope of SL-09 is the string model; U-02 is closed by 032 (section 5) |

The run's own refutations, which I confirm: Q1a (HS-04), Q2 as an identification, Q3a (SG-07), Q4a and H9(a) (AR-01), Q4b
as a deduction, Q5a (Q3-01), Q6b (SL-04), Q6d (SL-07) and Q6e (SL-05).

## 2. What is new

**Against the literature (from memory, to verify):**
- **SG-08–SG-11 as a written proof are new, as far as I know.** They prove Deligne's theorem (Weil I 1.6; Weil II 3.3.1
  fibrewise) using only:
  - the trace formula, Künneth, Artin vanishing and duality;
  - generic weak Lefschetz (Katz ACT 3.4.1, weight-free);
  - Noether normalization;
  - Parseval for bilinear character sums;
  - the tensor-power trick.

  The idea is Alpöge's footnote 3 (p. 3, steps 3 and 5). The complete argument, the identification of the effective
  remainder as a Gysin kernel, and the genericity inside the Fourier-compatible family are the run's.
- **What it is not.** Deligne's Weil I uses monodromy of Lefschetz pencils and Rankin–Selberg positivity; Laumon's Fourier
  proof of Weil II still rests on the case of curves. Neither is the route here.
- **AR-01 is new as a counterexample to Grothendieck's displayed formula.** The phenomenon, vertical non-Cartier Weil
  divisors on nodal fibres when E = 0, is classical geometry.
- **The rest is classical or elementary:** SG-02, SG-03, SG-04 (Hodge for E^n), SG-05, SG-07, AR-02, AR-03, AR-05,
  SL-01, SL-02, SL-04 and SL-07. SL-08 and SL-09 are new exact statements in a specified model.

**Against tonight's other runs.** GCT_NSRH F03, F04 and F17 give the abstract criterion with (S1) and (S2) as hypotheses.
HODGE_SIGN SG-08 proves (S2) geometrically, so together they give the sign-only theorem in full. The two runs agree on the
sign: it is the degree of E^{n−1}, not the sign of an intersection form.

**Against our own results:**
- The Hodge sketch, 3.6, is confirmed and made into a theorem.
- SL-04 is already in the sketch's Route 4 and in H8.
- SG-07 confirms the reading of SA06 E.3u.

## 3. Scope of the two proofs

- **Alpöge (RH, cited as a theorem):** used only in SG-02, to place the zeros of ζ(s−3) on Re s = 7/2. That is classical
  RH, shifted.
- **Dirichlet GRH:** not used in any proof.
- **Masullo:** not used. The run states this.
- **Nothing claims more than its input gives.** The run is explicit that there is no number-field GRH for the H³ of a
  quintic (SG-06 table), and no Hodge standard conjecture.
- The finite-field results SG-08–SG-11 use neither RH nor GRH.

## 4. Integration (edits listed, not made)

**Open rows of earlier runs.**
- **BRIDGES Q03** (prompt 22): from "open" to "literal refuted (HODGE_SIGN Q3-01); canonical [P,H] open in H (Q3-04);
  soluble version with a section (Q3-05–06); curve purity suffices (Q3-02)".
- **BRIDGES Q05:** unchanged, open.
- **BRIDGES Q01 and Q02:** unchanged.
- **GCT_NSRH, the intake's prompt-32 question** ("for which Y do scans 034–040 give (S2)"): answered. For every smooth
  affine U and lisse F, the generic member of f + Σg_i + c on U^k gives it (SG-08, SG-09).
- **ALPOGE_GCT Q-ALPOGE-METHOD** (prompt 23): the abstract theorem is now GCT_NSRH F03 together with HODGE_SIGN SG-08–09.
  Its gate, identifying the object, stays.
- **WARGAME H8:**
  - add the Wilson range t ≤ k ≤ v−t (SL-01);
  - the primitive scalar is r!d!/(d−r)!; (r!)² holds only at d = r (SL-04);
  - H8(iv) needs a specified order; in the string model the indices are 1, 32 and 2^13·3^10 (SL-09).
- **WARGAME H9(a):** refuted (AR-01). **H9(b):** its deduction fails.
- **SA06 intake, C.1a–q:** finite-field absolute values by SG-10; no cycle statement changes (SG-06).
- **SA06 intake, E.3u:** ζ restricts to 0 on the degree-14 hypersurface (SG-07).
- **Fable's suggestion 4:** refuted as an identification. **Suggestion 6:** the unnormalized identification is refuted
  (SL-07); the integral comparison is a gate.

**Grothendieck's texts.**
- **Cote 16, scans 034 and 036 (ours):** the "definite sign" of step 5 is the class of E^{n−1}(Y) = Ker φ_*, with sign
  (−1)^{n−1}. With Parseval, the induction of scans 034–040 proves Weil's absolute values. **Note for the companion:**
  "Grothendieck's hyperplane induction (cote 16, 034–040) carries a proof of the Riemann hypothesis over finite fields
  that bypasses his route of 049–050 (C, A, I)."
- **Cote 16, scans 049–050:** unchanged. C, A and I(X×X) stay open in general.
- **Cote 16, scans 014–017:** the normalization flags (SL-04, SL-08). Scan 015's range 2n−i should be n−i; scan 017's
  projector order is a candidate correction.
- **Cote 44, scan 004, Th. 5:** the displayed formula fails (AR-01). The intended qualification after "géom.
  intègres..." must exclude the case E = 0 or add singular-fibre terms.
- **Cote 34, scan 064, Remarque 1.17 (struck):** as for BRIDGES Q03 above.

**Rows for the second pass of the transcription** (from the run's `TRANSCRIPTION_NOTES.tsv`; my ratings):

| Cote/scan | Place | Candidate | My rating |
|---|---|---|---|
| 16/034 | first diagram, target | H^{2n−i}(Y), φ_{2n−i} (P^i(Y) = ker L_Y^{n−i} on a variety of dim n−1) | high, mathematically; check the image |
| 16/036 | after "s'identifie donc à L_X" | L_X^j P^i(X), not P^j | high |
| 16/038 | first two sums; Λ_Yφ^* formula | P^i for P^j; p_Y^j for p_X^j | high |
| 16/015 | matrix-unit range | 0 ≤ α,β ≤ n−i | high |
| 16/017 | inverse relation | projector order | medium; two possible repairs |
| 16/014–016 | ordinary contraction against the inverse identity | normalization flag | a flag, not a reading |
| 44/002 | Th. 3 | P^{n+1−i} | high |
| 44/004 | Th. 5 | P^j | high |
| 34/057, 063, 064, 074 | as in the run | – | as the run rates them |
| 34/053 | SGA 1 VIII | published locator: SGA 1 IX 6.1 | medium |

**Study and companion notes:**
- **`reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`, 3.6:** after "proved as GCT_NSRH F03/F04/F17 (checked
  in the intake of GCT_NSRH)", add: "; the hypothesis (S2) is supplied geometrically by HODGE_SIGN SG-08–SG-09 (generic
  weak Lefschetz, Katz ACT Cor. 3.4.1, for the family f + Σg_i + c on U^k). The effective remainder is
  H_c^d(U,F)^{⊗k} ⊕ E^{D−1}(Y), the evanescent part of cote 16 scans 034/036. Hence Weil I 1.6, and Weil II 3.3.1
  fibrewise, without weights (checked in the HODGE_SIGN intake)."
- **Same file, Route 3, first test:** add "HODGE_SIGN answers (a): the sign is the parity of E^{n−1}, not the
  Hodge–Riemann sign. The even-k restriction is needed only for the E^k path-bundle test, not for the theorem."
- **Same file, 3.4:** add "Th. 5 as displayed is false: HODGE_SIGN AR-01, P²×P² with Z = a² − ab + b², a pencil with
  E = 0. H9(a) is refuted. The correction lives on the nodal fibres."
- **Same file, Route 4:** add the H8 corrections and the SL-09 indices, marked "string model, not Φ₀ on ΛM₀".
- **Same file, section 5, cote 16 row:** add "HODGE_SIGN cites cote 16 by our numbering (checked)."

## 5. How the findings bear on the Hodge prompts 37–41, now running, and the attacks they open

- **40, HODGE_JACOBIANS_1964 (cote 44): bears directly.**
  - **What is closed.** Its task 3 asks to use step 5 and step 13 for the sign. HODGE_SIGN shows they cannot give a
    sign: step 5 is an effectivity sign in K_0 (SG-08), and step 13 gives only a size bound (AR-02, AR-05).
  - **Its task 2 (H9(a)):** refuted by AR-01.
  - **The attack this opens:** the corrected Th. 5.
    1. In the case E ≠ 0, for a Lefschetz pencil with fibres of odd dimension 2m−1 ≥ 3, prove that the vertical classes
       are Cartier restrictions, which are isotropic. Then ⟨ζ,ζ′⟩_{BB} = (−1)^m Z·Z′ for the Beilinson–Bloch height
       over k(P¹), which is defined by intersection on the total space.
    2. In the case E = 0, compute the term at each nodal fibre. Test it on P²×P²: three nodes, total 3.
    3. Then a cubic fourfold pencil, where E ≠ 0.
    - [State, 21 Nov 2026: steps 1 and 2 are done. Step 1 by JAC1964 H9-T2 (no correction when specialization is
      injective at every singular fibre); step 2 on the quadric pencil by H9-C1 with H9-T1 (each node contributes 1;
      the P²×P² local terms are not yet computed). Step 3 is the next test of H9-T2's hypothesis. (corrected 21 Nov 2026
      after the intake of JAC1964, Claude Opus 5.5 at effort high)]
    - [Rows of this run, 21 Nov: U-01 stays (SIGN_NEXT SN-14: trace data alone cannot give scan 049's positivity, even
      with correspondence coefficients); U-02 is closed for positivity, conditional on 032 (SN-11), and refuted
      literally (SN-12, a simple CM fourfold over F = Q(α), f = T⁴ − 5T² + T + 1, K = Q(i)); U-03 is solved (SN-44-01,
      SN-44-04). U-04 and U-05: see the SIGN_NEXT intake (IF-01 checked; IF-05 to IF-09 at statement level).
      (corrected 21 Nov 2026 after the intake of SIGN_NEXT, Claude Opus 5.5 at effort high)]
  - Th. 4 for abelian varieties stays on the sketch's route through 032 Cor. 8.4. SG-04 gives it for powers of CM elliptic
    curves without 032.
- **38, HODGE_HECKE_DIVISION:**
  - Its task 3 lists "the positivity of Alpöge's step 5". **That positivity carries no bilinear form** (SG-01, SG-08,
    HS-05) and cannot see cycle-class kernels (SG-06). It can give weights in families, nothing on division.
  - **The attack that does bear comes from SG-04's finite-field part.**
    1. On a fibre at an ordinary prime v of a variety isogenous to E⁴ (E = C/Z[ω]), every Tate class is a Q-polynomial
       in divisors.
    2. Its denominators are bounded by the determinant of the intersection matrix of a divisor-product basis.
    3. At split primes, End(E_v) = End(E) (Deuring, from memory), so that determinant is independent of v.
    4. Test whether this bounds the division at every ordinary prime of the Hecke orbit.
    5. Supersingular primes, where NS has rank C(8,2), are the residual case.
- **39, HODGE_GHOST_CLASSES:** the same SG-04 input answers part of task 4.
  - At ordinary primes, the least complexity of the reduction t_v of the Weil class is "a quadratic polynomial in divisor
    classes" (degree 4 on a fourfold).
  - At supersingular primes, all even cohomology is divisor-generated.
  - **Next:** compute the coefficients and denominators of t_v in a divisor basis as functions of v (task 4 made
    concrete).
- **37, HODGE_THETA:** SL-05, SL-06 and SL-07 bear on tasks 2 and 4.
  - The Arthur SL_2 is not the untwisted Lefschetz sl_2.
  - Integral indices need a specified lattice.
  - The run found that the Lean `StatementB.lean` uses a factorial-weighted Fock pairing. That is the divided-power
    (binomial) lattice Γ_1 of SL-05.
  - **The attack:** take the Fock model of Howe duality (sl_2, Sp_{2n}) on Λ^*(Z^{2n}) as the candidate integral
    intertwiner, which fits the sketch, 3.3. Compute the index of Z[L, D] in End_Z(Λ^*Z^{2n}), the actual exterior
    model and not the string model, for n ≤ 4, and compare it with the step-10 data of SL-06.
- **41, HODGE_DEGREES_ARE_L_VALUES:** **AR-05 is the tool for a degree bound against a divisibility.** With the Rallis
  degree as an L-value and the lattice metrics fixed, log d ≤ μ_max(M) − μ(L) + log C bounds the denominators along an
  orbit. Otherwise there is no direct bearing.
- **Our prompts 30–36:**
  - 35 (ZETA_TWO): SG-11 is a weight-free purity theorem for any zeta function of a scheme over a finite field. Offer it
    as the route.
  - 33 (TRACE_DET): HS-01 and HS-04 state when traces lose roots.
  - 30, 31, 34 and 36: no bearing.

## 6. Prompt updates for the successor of HODGE_SIGN

1. **Cite** SG-08–SG-11, with GCT_NSRH F03, as the sign-only theorem, checked. Do not re-prove them.
2. **The Hodge-index route, the next step.** With purity proved weight-free, Grothendieck's route of scans 049–050 needs
   C(X) and I(X×X).
   - Attack his Proposition on our scan 050: A(X) ⟺ C(Y) + A′(X×X)⁰ + A″(X×X)⁰. Where the critical-degree conditions hold
     (abelian varieties through 032 Cor. 8.4; CM elliptic powers through SG-04), derive C and I.
   - Ask whether the sign-only identity, applied to X×X with correspondences as coefficients, gives Grothendieck's
     semisimplicity (scan 049). State what positivity it would need.
3. **Q2c (U-02):** closed by 032 (Hodge for CM abelian varieties, claimed; human proof Hexagon 2610.00259) with Milne 2002
   Th. 3.3. Attach 032 and state it so.
4. **Q6g (U-04, U-05):** the run stopped at a gate after 42 minutes, against the push rule ("deliver nothing while an
   item is undecided and an untried approach remains"). The successor attacks:
   - the integral intertwiner, by the Fock model (section 5, under 37);
   - the indices on the actual exterior model;
   - a test against the step-10 m = 2 data.
5. **Cote 44:** prove the corrected Th. 5 (section 5, under 40). Compute the nodal-fibre contributions in the
   P²×P² example.
6. **Archive:** the convention holds (file names = our scans). Keep citing by file name.
7. **Effort record:** write "GPT-6 Astra (ChatGPT Pro mode)". The push paragraph, the ledger and the three-hour review
   stay. Add: "a gate that depends on data not supplied is an item to construct, not a reason to deliver."
