# Intake of the ZETA_HEAT final (prompt 62): diff from cp03, and the posting judgement

Written 24 Nov 2026 by Claude Opus 5.5 at effort high (agent afa2696b67cad55de), at the request of the main session
329fb1e6 (Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode).
- Read: the final, sealed 23 Nov 22:19 UTC (`research_returns/ZETA_HEAT_final_20261123T2219Z_unzipped`).
- Checkpoints 05 (20:53) and 06 (21:38) were filed into the final under `_from_earlier_checkpoints/`. Their content is
  carried in the final's workbench; I diffed cp03 against the final's workbench.
- Brief: `INTAKE_WAVE_20261123_EVENING.md`. Previous intake: `INTAKE_ZETA_HEAT_20261123_cp03.md`.
- Paper standard: `pro_prompt_builds/PAPERS_20261122/core/HOW.md`.

A is Alpöge's theorem: RH for every Dirichlet L-function, ζ included.

## 0. Scope: what was read
- **Diff by hash:** 196 files new, 50 changed, 1 removed (the cp03 manifest).
- **Registers:**
  - FINAL_STATUS.md, in full;
  - QUESTIONS.tsv: the status diff;
  - STATEMENTS.tsv: rows 063–090 are new, 28 statements;
  - CHECK_EVENTS.tsv: 356 events against 217 at cp03. By type: 134 targeted proof check, 126 independent re-proof,
    10 independent statement-only re-proof, 29 used and rechecked, 27 computation, 7 background, 2 source checks,
    2 refuted;
  - DEPOSIT_SHEET.md;
  - paper/BUILD.md.
- **The paper:**
  - `main.tex`, read in full apart from the inputs: title, abstract, Section 1 frame, Proof overview, note on method;
  - the diff of `arithmetic_compressions.tex`, which adds prop:finite-simple-deflation, read with its proof;
  - `arithmetic_precision.tex`, read in full;
  - `inertia_density.tex`: the definitions, prop:fd-inertia-complete with its proof, and the two theorem statements;
  - `uniform_cosine_sampling_lower.tex`: the statement;
  - a scan of the whole text for the words that HOW.md bans;
  - the PDF: 169 pages; SHA256 1c6183b2…25cd7e matches FINAL_STATUS.
- **Not read:**
  - the proofs of thm:strong-inertia-density, thm:fd-inertia-density and thm:cosine-lower-rate;
  - the Möbius, Nyman–Beurling, sawtooth, Burnol and prime-commutator sections;
  - the improved survival proof;
  - the Hermite–Biehler and conductor drafts;
  - the 60-odd audit and visual-QA files.

## 1. Verdicts (this task)
- **thm:fd-arithmetic-complete: all six certificate rows are now replayed independently.** The answer to the
  coordinator's question about rows N = 5, 6 has three parts:
  1. **The run has not replayed them.** Its records show the worker's Arb program passing levels 1–6
     (ZH.ARITHMETIC.NUMERIC), a proof-read of that program by root, and root's re-run of the same program at levels
     1–3 only (ZH.ARITH.COMPUTE: "not an independently authored arithmetic implementation").
  2. **My replay covers them.** Script:
     `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\replay_weil_flint.py`.
     - It is my own code, written from the paper's formulas: 150-digit Arb arithmetic, Gauss–Legendre quadrature with
       24 nodes on each dyadic interval, and the primitive kernel as a cumulative sum of one-step blocks. S_k comes from
       a Cauchy-FFT Taylor series of ξ(½+iz) and its formal logarithm.
     - It reproduces my cp03 mpmath values for N = 2 and N = 4 to every printed digit. The new rows:

       | (N, k) | D (replay) | U (run) | threshold 2/T^{2k} |
       |---|---|---|---|
       | (5, 2) | 1.31802357404e−7 | 1.318023575e−7 | 1.3180436e−7 |
       | (6, 3) | 2.30927091610e−12 | 2.309270917e−12 | 2.3092815e−12 |

       Both agree with U to 10 digits and lie just below it.
     - The relative margin at height 97.632 is 4.6e−6, against a disagreement of about 1e−10.
     - The replay is not rigorous: the quadrature error is not bounded, although the integrands are analytic at
       distance ≥ π from each interval of length 2^{−N}.
  3. **The run's certificate remains its rigorous Arb enclosure.**
- **prop:fd-inertia-complete (the integer test).** Confirmed by a targeted proof check and a computation.
  - The proof:
    - the congruence gives ι_N(T) = #{eigenvalues of C_N above 1/T};
    - interlacing under compression;
    - eventual equality by norm convergence when Ξ(T) ≠ 0;
    - the Schur-complement form −G₋ + T²KᵀG₊⁻¹K, by Haynsworth inertia additivity. I recomputed the sign.
  - From my replay matrices, ι₄(39.913) = 6, ι₅(62.413) = 14 and ι₆(97.632) = 28, each equal to n(T). The compression
    eigenvalues invert to 14.1347, 21.022, 25.011, 30.4249, … at N = 6.
- **prop:finite-simple-deflation.** Confirmed by a targeted proof check: deleting simple coordinates subtracts u^{−2k}
  from both S_k and the trace, so the excess 2Σ(m_γ − 1)γ^{−2k} is unchanged. The matrix updates are rank one.
- **prop:fd-arithmetic-precision.** Confirmed by a targeted proof check of the perturbation step: the relative pencil
  gives ‖B̃ − B‖ ≤ 2τ with ‖B‖ ≤ ‖C‖ = 1/γ₁ < 1/14, and |Δtr| ≤ 4kdτ. The eigenvalue bounds for G_N use the coercivity
  rate of thm:cosine-lower-rate, which I did not check.
- **Everything else new** is at statement level, carried by the run's events.

## 2. What is new since cp03, usefulness first
1. **An integer form of the exact test** (prop:fd-inertia-complete, checked by us).
   - The packet through T is simple iff ind_+(TH_N − G_N) ≥ n(T) for some N. This is a signature count, cheaper than
     high moments, and the Schur form halves the size.
   - Usefulness: the cleanest finite statement of all-height simplicity. Main gate (FINAL_STATUS): the integer deficit
     n(T) − ind_+(TH_N − G_N) must vanish for finite N at unbounded zero-free heights.
2. **The distinct-zero density, realized in arithmetic matrices** (thm:strong-inertia-density and thm:fd-inertia-density;
   statement level).
   - ind_+(TH_N − G_N) ≥ (d_MT − η)n(T) with N = ⌈A_η log T⌉, where d_MT = 0.83625…
   - Localized spectral coordinates for a (c_MT − η)-fraction of simple ordinates, with ‖CU_N − U_NΛ‖ ≪ 1/(T² log T).
   - Usefulness: a quantitative finite-dimensional version of the known density results.
   - Credit: Alpöge–Furman (and the Claude manuscript), Lamzouri and Knausgård obtain these proportions (Section 1).
     The exact split, theirs against the transfer to the certificate, is a posting gate (§5).
3. **An unconditional all-window lower rate** (thm:cosine-lower-rate; statement level).
   - a₁(L), a₂(L), b_L ≥ exp{−Cμ^{1/d_MT}log μ(1 + log log μ)}, with μ = e^{2L}.
   - This improves Mori's μ^{6/5} (cited at Theorem 4.3, pp. 11–13), since 1/d_MT = 1.1958….
   - The target is λ^{9+α}e^{−4πμ}, so the gap is now exactly the power μ^{1/d_MT} against μ in the exponent.
   - Usefulness: the first lower bound on the window side, for prompt 68 item 5.
4. **The survival interval improves to the Montgomery–Taylor proportion 0.67250…**, from 2/3 (PERSISTENCE-Q1, which
   now uses Montgomery–Taylor's cosine approximation; statement level).
5. **Approaches closed with precise obstructions** (FINAL_STATUS table, statement level):
   - **Prime-form multiplication:** the proposed closed extension fails, by a constructed graph residual
     (prop:fd-multiplication-domain).
   - **Hermite–Biehler:** an explicit subharmonic counterexample to the proposed boundary inference.
   - **Fixed two-jet Burnol cutoff:** the Rayleigh quotient grows like cL.
   - **Finite simple deletion:** it leaves the multiplicity excess unchanged.
   - **Conductor variation:** the count (r/12)log q − C gives no smaller gate.
   - **Nyman–Beurling:** the adaptive constant retains Σm(m−1)/|ρ|².
6. **Status.** No row changed status. The 9 open rows are INCOMPLETE under the two-reviews-without-movement rule
   (21:09 UTC review). Totals: 9 proved, 2 refuted, 9 INCOMPLETE. The main question is open.

## 3. Scope of the inputs
- A enters as a named input, its Lean development not replayed. Cited inputs: Suzuki's convergence, Voss's sampling
  theorem, Mori, Montgomery–Taylor, Olshanski. Masullo is not used.
- The certificates use only Λ(n) for n < e^{12} and archimedean integrals.

## 4. The paper as a posting candidate (HOW.md, the eight boxes)
One paper: "The simplicity question for the Riemann zeros after Alpöge's theorem", 169 pages, 48 inputs. The run
reports zero overfull boxes and image coverage of every page. We have not rebuilt it; the pre-publication PDF check of
AGENTS.md is still to be done on our side.

| box | state | what is missing |
|---|---|---|
| 1 title | names the question and Alpöge, but states a question rather than a theorem; "after" is used in time, not for carrying out someone's idea | a title stating the theorem, per paper (see the split below) |
| 2 abstract | first sentence on Alpöge's theorem ✓; last sentence on production and no human review ✓ | it lists about ten results; it does not name the outside checkers (they are in the note on method) |
| 3 theorem in words | Section 1 states the finite-detection, local, arithmetic, motion, survival, CUE and spectral claims | for an omnibus, Section 1 cannot state each main theorem with its meaning in a phone-readable opening |
| 4 why care | context paragraphs ✓ (Λ = 0, GORZ, Montgomery, Bui–Heath-Brown) | no plain sentence on what changes; the main question is open |
| 5 credit | Suzuki ✓; Alpöge–Furman/Claude, Lamzouri, Knausgård, Mori, Cobeli–Zaharescu each cited with statement and page | the density and survival proportions coincide with Alpöge–Furman's and Lamzouri's; what is new here (the transfer to arithmetic matrices with N = O(log T), the common heat interval) must be split exactly against their rank inequality. We have opened none of these sources |
| 6 context | extensive, including AI-lab work (Bondarenko–Heap with ChatGPT, Knausgård with Codex/Claude) ✓ | — |
| 7 scope | open_questions.tex and Section 1 ✓ | — |
| 8 proof overview | Section 2 is headed "Proof overview", in prose, before the proofs ✓ | where A is used is said only in passing |

**Further against HOW.md:**
- The text has no run names, statement ids, prompts or paths ✓.
- "actual" appears 12 times and "supplied" 5 times as process words. For example "the actual finite search", "For the
  actual zeta heat family", "the actual restriction" and the heading "The coupling retained in the lower certificate".
  Most of the 19 uses of "retained" are mathematical.
- The note on method names Claude Opus 5.5 at effort high and Claude Fable 5.2 at effort max ✓. It predates our cp03
  and final checks (the arithmetic theorem, all six rows, the integer test, the constants, the orbital bound), which
  should be added.
- The workbench URL must be live before posting.

**What blocks it, statement by statement:**
- **thm:fd-arithmetic-complete.** The proof is checked by us. It rests on Suzuki's Hilbert–Schmidt convergence
  C_N → C, which no one on our side has opened. Gate: open Suzuki arXiv:2610.32704 at that locator.
- **Certificate rows 1–6.** The run's rigorous Arb certificate stands, and our independent non-rigorous replay
  covers all six rows. Gate, if Hexagon's "100% sure" bar asks for it: an independent enclosure. My script would need
  rigorous quadrature (acb integration in place of Gauss–Legendre), which is about a 5-minute change and a 2-minute run.
- **prop:fd-inertia-complete:** checked, and computed at three heights; no gate.
- **cor:fd-global-growth-numeric:** the constants are checked. The upper comparison uses 𝔯_m ≤ π√(m−1), unchecked.
- **thm:fd-limits:** the analytic part is checked. The local Hermite/orbital part is unchecked by us; the run re-proved
  it.
- **thm:local-orders, thm:phase-orders:** unchecked by us.
- **thm:strong-inertia-density, thm:fd-inertia-density, thm:cosine-lower-rate:** unchecked by us, and with the credit
  gate of box 5 (Alpöge–Furman, Lamzouri, Mori).
- **The motion, survival and CUE theorems:** checked by us only in parts, at cp01 and earlier: the Hurwitz sign, the
  CUE agreement value and the isolated-pair κ = 0 term.

**Judgement.** The 169-page omnibus is not a posting candidate as one paper. Its opening cannot tick boxes 1, 3 and 4
for eleven families of results, and its main question is open. Split it. Most ready first:
- **(A) "A finite arithmetic test for simplicity of the Riemann zeros, after Suzuki".**
  - Contents: thm:fd-arithmetic-complete, prop:fd-inertia-complete, prop:fd-even-operator, prop:fd-certificate-size,
    prop:finite-simple-deflation, prop:fd-arithmetic-precision, the certificate through 97.632,
    lem:fd-multiplicity-log, prop:orbital-unimodal-bound and cor:fd-global-growth-numeric, with thm:fd-limits stated
    as the heat-flow translation.
  - Everything in it except Suzuki's locator and the upper radius bound is checked by us. About 15 pages.
- **(B) The complete local multiplicity partition** (thm:local-orders, with thm:phase-orders). It needs our check.
- **(C) CUE collision laws** (Weibull-3/2 first collision, Poisson early collisions, label agreement
  0.666546601837…). Partly checked.
- **(D) Heat motion and survival** (directions, the isolated pair, Montgomery–Taylor survival, the nonreal height). It
  needs the credit split.
- **(E) The window side** (the prolate upper bounds, thm:cosine-lower-rate, the b_L sandwich, the finite lower
  certificate). It needs a proof check and the Mori credit split.

## 5. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`; for the main session)
| title | statement | what it adds | gate left |
|---|---|---|---|
| A finite arithmetic test for simplicity of the Riemann zeros, after Suzuki | Under A: D_{N,k} = S_k − tr C_N^{2k} ≥ 2E(T)/T^{2k}; sup_{N,k}(2/D_{N,k})^{1/(2k)} = γ_*; equivalently ind_+(TH_N − G_N) = n(T) for some N at zero-free T; lim a·j_*(−a) = γ_*²/2. Certified: all zeros with 0 < Im ρ ≤ 97.632 are simple, from prime powers < e^{12} | an exact, zero-free, terminating finite test at every height | Suzuki HS locator; optional rigorous independent enclosure |
| Explicit constants for the de Bruijn–Newman finite tests | m_γ < ¾ log γ (γ ≥ 10); L_T > 216.88, L_J > 4766.003712; two-sided L_T–L_J comparison; 𝔯_m² ≥ 4π²(m+1)/(3m²) | numbers for the heat-flow limits | 𝔯_m ≤ π√(m−1) (upper comparison only); merge into row 1's paper |
| The complete local multiplicity partition for heat-flow Newton determinants | ord_{t=0} det[S_{u+v}(t)]_{u,v<k} = Σ_{j≤k} b_j, recovering every multiplicity in a contour, with positive leading coefficients | a finite contour test that sees the whole partition | our proof check |
| An all-window lower rate for the Weil form | a₁(L), a₂(L) ≥ exp{−Cμ^{1/d_MT}log μ(1+log log μ)}, μ = e^{2L} | improves the μ^{6/5} exponent of Mori, Thm 4.3 | proof check; credit split with Mori; open Voss |
| Collision laws for the CUE heat flow | the first collision is Weibull-3/2; early collisions are Poisson with intensity (3/2)√v; the adjacent label agreement is 0.666546601837… | random-matrix model for zeta heat collisions | whole-proof check (the agreement value is checked) |

These replace the two cp03 rows: row 1 absorbs the earlier "finite arithmetic test" and "trace certificate" rows.

## 6. Integration (applied)
- `field_experts/structural_maps_20261123/NCG_ZETA.md`:
  - §3(a), the failure-scale cell: added the unconditional lower rate;
  - §4.3: added the integer test and the remaining exponent gap.

  Backup: `NCG_ZETA.md.bak_before_final`.
- The primer was updated in place. Backup: `PRIMER_ZETA_HEAT_20261123.md.bak_cp03`.
- **For the main session:** the board rows (§5), the prompt-68 edits (§7) and the paper split (§4).
- Log: `INTEGRATION_ZETA_HEAT_20261123.tsv`.

## 7. Prompt updates: prompt 68 (CONNES_AFTER_RH, waiting), as edits for the main session
1. **Item 6 (lines 71–90).**
   - Replace "(`ours/ZETA_HEAT_cp03/`, its checkpoint 3 of 23 November 2026, still going)" with:

     > "(`ours/ZETA_HEAT_final/`, its final of 23 November 2026, 22:19 UTC; the run ended INCOMPLETE on the main
     > question under the two-review rule, with 9 rows proved, 2 refuted and 9 open)".
   - After the sentence on prop:fd-certificate-size, insert:

     > "Its final adds an integer form of the same test, prop:fd-inertia-complete: the packet through a zero-free
     > height T is simple iff ind_+(TH_N − G_N) ≥ n(T) for some N, with G_N, H_N the arithmetic Gram and primitive
     > matrices. thm:strong-inertia-density: ind_+ ≥ (d_MT − η)n(T) already with N = O(log T), d_MT = 0.83625….
     > thm:cosine-lower-rate: a_1(L), a_2(L), b_L ≥ exp{−Cμ^(1/d_MT) log μ (1 + log log μ)} with μ = e^(2L),
     > improving Mori's exponent μ^(6/5). prop:finite-simple-deflation: deleting certified simple coordinates leaves the
     > multiplicity excess unchanged."
   - Replace the sentence on our check with:

     > "Claude Opus 5.5 at effort high followed the proofs of thm:fd-arithmetic-complete and prop:fd-inertia-complete
     > and recomputed all six certificate rows with its own code (high precision, not rigorous). They match the run's
     > bounds to 10 digits, and the integer test gives n(T) at heights 39.913, 62.413 and 97.632."
   - **For the main session to decide.** "That run has the simplicity of the zeros and every route to it": the run has
     ended. Either keep the division, if a ZETA_HEAT follow-up is planned, or let this run state any estimate it finds
     on a_2 or b_L. The current final sentence already allows that.
2. **Item 5, line 65.** After "(ALP_CONNES cp44, (RZ.5); …so α ≤ 4 is forced)", add:

   > "The best unconditional lower bound is a_2(log λ) ≥ exp{−Cλ^(2/d_MT) log λ (1 + log log λ)} (ZETA_HEAT final
   > thm:cosine-lower-rate), so what is missing is the exponent: λ^(2/d_MT) = λ^2.391… against λ^2."
3. **Research item 3 (the D_N question).** Add:

   > "and its integer form ind_+(TH_N − G_N) = n(T) (prop:fd-inertia-complete): is the number of eigenvalues of the
   > cutoff above 1/T in T50's sense the same count, and does T50's positivity bound the deficit n(T) − ind_+?"
4. **Research item 5, bullet "One mechanism in four places".** Before "If your work on the cutoff gives such a rate…",
   add:

   > "On the window side the gap is now a single exponent: the unconditional rate exp{−Cμ^(1/d_MT)…}, μ = λ², against
   > the needed λ^(9+α)e^(−4πμ)."
5. **Attachments (line 299).** Replace `ours/ZETA_HEAT_cp03` with `ours/ZETA_HEAT_final`: the final's `workbench/paper/`
   and its registers, leaving out the audit and visual-QA drafts. Refresh `ours/intakes/ZETA_HEAT/` with this intake and
   the primer, and `ours/structural/NCG_ZETA.md`.
6. **Literature.** The final's bibliography carries Mori (Thm 4.3, pp. 11–13), Alpöge–Furman, Lamzouri and
   Knausgård. If 68 is to touch the a_2 rate, attach Mori, in LaTeX if it exists.

## 8. For the P vs NP fleet
The cp03 map (L-gct-128 and L-gct-138, the Descartes bounds against prop:fd-certificate-size) carries over.
prop:fd-inertia-complete sharpens it into a signature count: positive inertia of a Hermitian pencil counts distinct
roots above a threshold. That matches the sign-variation counting of the Descartes nodes even more directly. The bridge
work is as stated at cp03, with ind_+ in place of the moment defect. No new node.
