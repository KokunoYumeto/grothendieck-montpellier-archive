# Intake of NIGHT_AFTER_ALPOGE (prompt 75), checkpoint 11, Parts A and C: effective CM orbits, and the K-groups of Z with Ihara's question

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max), 23 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode) and is still going. This is the first intake of
the run. Part B (the theta chain) is taken in by agent abcaba9b6ae84b747 and is not covered here.

**Inputs, and how they are treated.**
- **Alpöge's RH and GRH for Dirichlet L-functions** is a theorem.
  - Part A uses only the special case (1.1): L(σ, χ_d) ≠ 0 for 1 − 1/(4 log|d|) ≤ σ < 1.
  - Part C uses an intermediate theorem of the same Lean archive, `OneCharU_s`, and not the endpoint theorems.
- **Masullo's draft is not a proof.** Nothing in Parts A or C uses it.

## 0. What was read

**Return folder:**
`<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\NIGHT_AFTER_ALPOGE_checkpoint_11_20261123T1024Z_unzipped`
(10:24 UTC). The prompt as sent was not reread; the run's QUESTIONS.tsv gives its three questions.

**Read in full:**
- README, QUESTIONS.tsv, LEDGER.md (Parts A and C, the scheduled reviews, and the Part C mentions in later entries).
- LITERATURE.md, Pintar entry only.
- Part A, `workbench\schemes-and-moduli-workbench\`:
  - `papers\cm-orbits\main.tex`, all 825 lines, every proof;
  - `checks\a_literature.md`, §§1-8;
  - STATEMENTS.tsv.
- Part C, `workbench\k-theory-and-galois-groups-workbench\`:
  - `papers\k-groups\main.tex`: abstract and §§1, 3.3-3.4, 4.2, 7;
  - `papers\k-groups\verify_k12.json`;
  - `papers\ihara\main.tex`: abstract, §1 (theorem and its framing), §6 (the Vandiver lemma with proof), §8;
  - STATEMENTS.tsv.

**Not read:**
- `effective_ao.tex` (the finite-level passage to Jaswal's theorem): only its statement in main.tex §1 and the run's
  audit of it (a_literature §§1-3).
- The K paper's §§2, 4.1, 4.3, 5, 6.
- The Ihara paper's §§2-5 (cup comparison, Magnus separation, Greenberg arithmetic) and §7 (p = 2). I had checked
  the K17 versions of the pole theorem, the Vandiver deduction and p = 2 on 21-22 Nov. I have not compared the new
  text with them line by line.
- The 477 MB certificate data: not opened.
- No cited paper was opened.

**My computations** are in `partA_check.py` in this folder:
- the constants table of main.tex §1, for g = 1..6, agreeing to every printed digit;
- the D < 10^80 cutoff for rational CM surfaces: my evaluation gives about 10^78.1, consistent;
- the 13 class-number-one and 29 class-number-two order discriminants, by enumerating reduced forms up to |Δ| < 20000.

## 1. Verdicts, Part A (effective CM orbits)

**Results checked:**

| Id (run) | Statement | Verdict |
|---|---|---|
| A.RESIDUE (Prop 2.1) | κ_K > 1/(173 log D_K) for normal K ≠ Q; κ_K > 1/(173 n! log D_K) in degree n | **confirmed** (same as ZETA_NEXT NX01-NX02, checked 21 Nov) |
| A.BS (Cor 2.2) | two-sided effective Brauer-Siegel for normal fields | **confirmed** (= NX03) |
| A.RELATIVE (Prop 2.3) | h_E/h_F > c_r D_E^{1/4}/(log D_E)^r for CM E | **confirmed** (= NC01, checked 22 Nov) |
| **A.ZEROS (Lemma 3.1)** | Σ_{ρ≠β} Re 1/(1−ρ) < (75/2) log D_K | **confirmed, every step.** Zeros outside Stark's square have \|1−ρ\| ≥ t/4, t = 1/log D_K, so the termwise ratio at σ = 1+t is < 25. The archimedean terms plus 1/σ are negative in every signature of degree ≥ 2: −0.861 per real place, −1.415 per complex place, against 1/σ < 1. |
| **A.HEIGHT (Prop 3.2)** | h_F(A) ≤ a_r log D_E + b_r for CM by O_E, every CM type | **confirmed given averaged Colmez and GR14 Cor. 8.4.** The formula −L'/L(0) = Σ Re 1/(1−ρ) + ½ log(D_E/D_F) + (r/2)(ψ(½) − log π) was rederived from the functional equation. The exceptional zero contributes < 16 r! log D_E by Stark's Lemma 9 and (1.1). Isolating one CM type gives a_r and b_r exactly. |
| **A.SATURATION (Lemma 4.1)** | a K-isogeny A → B of degree ≤ I^{2g} with End B maximal; h_F(A) ≤ g(A_g + ½) log D + g B_g | **confirmed given Rémond Thm 1.2 and Raynaud's isogeny inequality.** End(B) = End_O(OΛ) is maximal because End^0 is E-linear. |
| **A.GALOIS (Lemma 4.2)** | S_ℓ ⊂ R⊗Z_ℓ ⊂ E⊗Q_ℓ with equal rational span; D divides ∏_ℓ disc(S_ℓ) | **confirmed given Faltings** (integral and rational Tate, semisimplicity). The Galois image is commutative because it lies in the commutant E⊗Q_ℓ; the integral Tate theorem and the centre then give the rest. |
| **A.ORBIT (Thm 1.1)** | every CM point x of A_g: \|Gal·x\| ≥ D_x^{1/(2g)}/(s_g C_g W_g log D_x) ≥ c_g D_x^{1/(4g)}, with D_x = \|disc Z(End A_x)\| | **confirmed given GR23 Thm 1.5(2), Notation 1.2 and Thm 1.8, and Tsimerman Lemma 4.1.** The passage from n to g in the exponent and constant, both cases k ≤ D and k > D, the level-3 descent (s_g) and the final log D ≤ (4g/e) D^{1/(4g)} were all checked. |
| A.SURFACE_D (Cor 6.1) | rational CM points of A_2 have D < 10^80 | **confirmed** (recomputed). |
| A.H1H2 | the 13 and 29 order discriminants | **confirmed** (recomputed); also the bound f ≤ 72 from φ(f)/3 ≤ h. |
| A.PRODUCT120 | 91 + 29 = 120 rational decomposable classes with Q-models | **confirmed** in count and argument (a rational symmetric pair is rational or conjugate, and a conjugate pair has one order). Product-polarization uniqueness was read, not checked. |

**Carried or read at the level of the statement:**

| Id (run) | Statement | Verdict |
|---|---|---|
| A.ENUMERATION (Prop 6.2) | a terminating algorithm for CM points of A_g of degree ≤ d | **proof read; algorithmic inputs carried** (Alpöge-Lawrence §§7-9, Appell-Humbert, the effective Hermite theorem). Termination is argued correctly at the level of the reading. |
| A.AO (Thm 1.2) | effective André-Oort and a listing algorithm for coarse A_g | **carried: a specialization of Jaswal (Hexagon 2611.00339v3) with Cureton-Thorner (Hexagon 2610.00200v2, Thm 1.1: Re s > 31/32 zero-free for every Dedekind zeta function).** It does not use (1.1) or Alpöge. I read the run's audit of the finite-level maps (a_literature §§1-3), not effective_ao.tex itself. |
| A.CURVE | the curve j_1 j_2 = 1 in A_2 contains no special subvariety | statement level (Bilu-Luca-Pizarro carried). |
| A.SIMPLE21 | the 21 published simple classes | statement level (Kılıçer-Streng carried). |

**Counts, Part A.** 15 findings:
- 8 confirmed by a full proof check (A.ZEROS, A.HEIGHT, A.SATURATION, A.GALOIS, A.ORBIT, and three already checked
  under ZETA_NEXT: A.RESIDUE, A.BS, A.RELATIVE);
- 3 confirmed by computation (A.SURFACE_D, A.H1H2, A.PRODUCT120);
- 1 proof read with algorithmic inputs carried (A.ENUMERATION);
- 3 carried or at statement level (A.AO, A.CURVE, A.SIMPLE21);
- 0 refuted.

## 2. Verdicts, Part C (K-groups of Z, Ihara)

| Id (run) | Statement | Verdict |
|---|---|---|
| **C.K12** | the exact K_12 certificate: N_7 = 2^15·3^19·7·13^5·37·43^3·47^3·61·271^3 | **confirmed a third time.** The run's new verifier gives the characteristic polynomial x³ + 73002x² − 10736848500x + 248682833875000 and the factorization I computed on 21 Nov, and the unitary scaled trace 157899. |
| C.K80 | K_{4k}(Z) = 0 for k ≤ 20, recorded as an inherited range | **unchanged from my KTOWER cp11 intake.** The run now labels it "not certified as a newly proved theorem" pending three things: the archive build and `#print axioms`; a primary-source closure of the KMSW introduction-wide background (Mok's endoscopic classification, the weighted fundamental lemma, stabilization; from memory all three are now published theorems); and the replay of the large unitary computations. |
| K paper §3.3 | `Keep.levelKA_alt` needs `P := hH.toClassicalTheorems` | **agrees** with the omission I reported on 22 Nov; the run has written the step into the paper. |
| **C.IHARA** | Ω_p* = Ω_p for every odd p with X_p^+ finite, at p = 2 with the real-place convention, and so for all p < 2^31 | **checked by me:** the Vandiver-to-X^+ step (Lemma 6.1, persistence of trivial p-class groups up a totally ramified Z/p tower, every step), the pole theorem (as K17-POLE-GENERAL, 22 Nov), the Vandiver kernel deduction and p = 2 (as K17, 21 Nov). **Not checked:** the extension from Vandiver to finite X^+ (§§3-5, through Fukaya-Kato and Wake-Wang-Erickson); the run's own same-model reconstruction PASS is recorded. |

**Counts, Part C.** 3 findings: 1 confirmed by recomputation (C.K12), 1 unchanged and carried (C.K80), 1 confirmed for
the Vandiver case with the finite-X^+ extension carried (C.IHARA). 0 refuted.

## 3. What is new, settled and still moving

**Settled in Part A.** The run counts it settled as a specialization of cited theorems.

**New in Part A, and ours:**
- **The orbit exponent improves from 1/(28672 g^4) (ZETA_NEXT NC04) to 1/(4g),** with explicit constants and every
  centre order, nonmaximal and nonsimple included. The new route bounds the centre discriminant directly by
  Gaudron-Rémond's 2023 invariant, in place of the isogeny-count argument.
- In this proof Alpöge's theorem enters only through the height bound: Stark's Lemma 9 and (1.1) remove the possible
  exceptional zero from −L'/L(0, χ_{E/F}) in the averaged Colmez formula. The class-number lower bound is not used at
  all.
- The run's register puts the CM-surface lists (120 decomposable classes, the 10^80 cutoff) under the same paper.

**Not ours: effective André-Oort for A_g in full.** It is Jaswal's theorem, which rests on Cureton-Thorner's
quasi-Riemann hypothesis for every Dedekind zeta function. Both are recent Hexagon preprints. The run records their
provenance:
- Jaswal: primarily AI-generated, with a human contributor who takes responsibility.
- Cureton-Thorner: mixed human and AI text, with proofs and a Lean formalization produced using AxiomProver.

Neither proof has been checked by the run or by us beyond the stopping tests the run audited. **If Cureton-Thorner is
right, the Galois-orbit lower bounds for CM points are effective unconditionally.** Our orbit theorem would then be
distinguished by its explicit exponent and constants and by resting on a formalized theorem, not by effectivity.

**Part C: no new mathematics in this checkpoint.**
- Two papers repackage K17 and KTOWER as an audited baseline, with one new verifier (K_12) and one new literature gate
  (the KMSW background).
- The run's main Part C research (Vandiver at every prime; unrestricted Ihara) is queued behind Part B.
- **Still moving:** Part B; the formal build (Statements built, Main not finished; no closed `OneCharU_s` or axiom
  print claimed); the Part C main work, not yet started.

**A finding that changes H18 (from the run's LITERATURE.md; I have not opened the source).** Leo Pintar, "Hecke
calculations for the conditional vanishing of K_4k(Z) through degree 104", Hexagon 2611.00829v1, 21 Nov 2026, reports
conditional certificates for k ≤ 26. Its hypotheses, as the run summarizes them:
- the strict Selmer comparison;
- representation coverage;
- simultaneous residual trace conditions.

If those are the hypotheses that `OneCharU_s` and the coverage theorems supply, our k ≤ 20 is not new as a set of
certificates. Our remaining contribution would be the proof that the hypotheses hold: the archive chain, the coverage
proofs and the `toClassicalTheorems` closure. By the rule that superseded results are not posted, and without any
priority claim, H18 must not go out before Pintar is read.

## 4. The scope of the two proofs

- **Part A:**
  - A.ORBIT, A.HEIGHT, A.RELATIVE and A.SURFACE_D use (1.1), a special case of Alpöge's theorem, together with
    published theorems.
  - A.AO uses no Alpöge input. It uses Jaswal and Cureton-Thorner, unrefereed recent preprints.
  - Nothing in Part A uses Masullo.
- **Part C:**
  - The K-groups use the Lean archive's intermediate theorem `OneCharU_s` and the record
    `hH.toClassicalTheorems`, and not RH.
  - Ihara uses no Alpöge input: Fukaya-Kato, Wake-Wang-Erickson, Brown, Hain-Matsumoto, Hart-Harvey-Ong.
  - Nothing in Part C uses Masullo.

## 5. In the project's terms

- **A.ORBIT** is a statement about the points of the coarse moduli scheme 𝒜_g/Q. It is proved through:
  - the Néron-Severi and Tate modules: Faltings, and the integral Tate isomorphism of Lemma 4.2;
  - the Hodge line bundle: the Faltings height through averaged Colmez, SGA 6 determinant algebra as in ZETA_TWO ZT08,
    cote 60 scans 3-9;
  - the arithmetic of Spec O_E: the relative class-number formula.
- The run assigns it to SA06 B.4a-e and SA07. The archive has no CM-orbit statement, and none is invented here.
- **C.IHARA:** the faithfulness of the pro-p tower action of G_Q on the tripod (Esquisse d'un programme §2; LM6
  A.44-A.45) at every prime below 2^31.
- **C.K80:** the Soulé characters of that action are integrally onto through κ_41, cote 149 indirectly.

## 6. Integration (edits to make; I have edited nothing outside this folder)

- **`field_experts\HEXAGON_CANDIDATES.md`, H15:** replace the exponent 1/(16384g³) or 1/(28672g⁴) by 1/(4g) (NIGHT_AFTER_ALPOGE A.ORBIT),
  "all centre orders". Add Jaswal and Cureton-Thorner as the effective André-Oort result, to be cited and not
  claimed. Gates now: literature novelty against Jaswal's orbit bound and Gaudron-Rémond 2023.
- **H18:** add "Pintar, Hexagon 2611.00829v1 (21 Nov), conditional certificates k ≤ 26: read before any post". Add
  the KMSW-background gate and the `toClassicalTheorems` step (now in the run's paper).
- **H06b (Ihara):** cite the run's 19-page Ihara paper (`papers\ihara\main.tex`) as the current text. Its abstract
  credits the Claude checks correctly: p = 2, Vandiver, pole separation.
- **My KTOWER cp11 intake §3** names effective André-Oort for A_g as the next theorem. It is now settled through
  Jaswal and Cureton-Thorner, if those preprints hold.
- **`reports_20261122\paper_seeds\SEED_KTOWER.md`, Paper 2:**
  - replace the main theorem by A.ORBIT: exponent 1/(4g); constants c_g, W_g, C_g as in main.tex §1; inputs GR23
    and Faltings in place of GR14 Polarisations;
  - replace its research question: effective André-Oort is answered by Jaswal and Cureton-Thorner; the open question
    is an unconditional or improved orbit exponent, and the effective format route (Binyamini, Log-Noetherian §10.4).

## 7. Prompt updates (for the run's continuation or successor)

1. **Part A:**
   - Compare A.ORBIT with every Galois-orbit lower bound in Jaswal (its torus-discriminant and level bounds) and in
     Gaudron-Rémond 2023, and state the exact difference.
   - Check Cureton-Thorner Theorem 1.1 against its proof and its Lean formalization: if it holds, it makes the
     arithmetic part unconditional and supersedes the Alpöge dependence.
2. **Part C:** read Pintar 2611.00829v1 and its supplement before anything else. State exactly which hypotheses it
   assumes and whether `OneCharU_s` and the coverage theorems discharge them. Then the queued Vandiver-at-every-prime
   work: order 5 and order ≥ 7, the third unit.
3. **KMSW:** cite Mok (Memoirs AMS 2015), the weighted fundamental lemma (Chaudouard-Laumon) and the stabilization
   (Mœglin-Waldspurger), with locators (my locators are from memory).

## 8. Hexagon readiness (the five tests: complete, self-contained, stable, checked, interest now)

| Candidate | Proved | Checked by us | New | Gate left |
|---|---|---|---|---|
| **A.ORBIT with A.ZEROS, A.HEIGHT, A.SATURATION, A.GALOIS** (\|Gal·x\| ≥ c_g D_x^{1/(4g)}, all CM points of A_g, explicit constants, from (1.1)) | yes, complete | yes: targeted proof check of every step, published inputs carried | new as an explicit, Alpöge-based exponent; effectivity itself may already follow from Cureton-Thorner via Jaswal | **one gate: the literature comparison with Jaswal's orbit bounds and Gaudron-Rémond 2023.** Self-contained, stable (Part A is settled in the run), of interest now. **The strongest candidate.** |
| A.SURFACE_D with A.PRODUCT120 | yes | recomputed | the 10^80 cutoff is new; the 120 list is a short consequence of known class-number tables | belongs in the A.ORBIT post |
| C.IHARA (all p < 2^31) | yes | Vandiver case yes; finite-X^+ extension no | likely new, but Sharifi's and Fukaya-Kato's work must be compared | **one gate: the literature** (Sharifi 2002/2007/2011, Fukaya-Kato, Ishii 2026, Hexagon). Post the Vandiver form; the X^+ form after a check of §§3-5. |
| C.K12 / C.K80 (H18) | yes, under the archive | K_12 three times, classical halves k = 13-20, deductions | **in doubt: Pintar 2611.00829 (k ≤ 26, conditional)** | **Pintar first**, then the axioms print and the KMSW citation. Not ready. |
| A.AO | not ours | — | — | cite only |
