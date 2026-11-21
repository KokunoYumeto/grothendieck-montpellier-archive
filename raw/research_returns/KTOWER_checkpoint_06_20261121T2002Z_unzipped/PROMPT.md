**The attached files.** Besides this file there is one ZIP, `KTOWER_the_Galois_action_on_the_tower_the_K_groups_of_Z_and_.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Brown_mixed_Tate_motives_over_Z.zip` is the folder `LIT_Brown_mixed_Tate_motives_over_Z/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# KTOWER: the Galois action on the tower, the K-groups of Z, and cote 149

This prompt continues three runs of 20-21 November 2026, all by GPT-6 Astra (ChatGPT Pro mode): **K17** (prompt 31, "step 17,
the K-groups of Z, Soulé and the pro-ℓ kernels"; final return checkpoint 08), **AN_GRH** (prompt 30, the anabelian and Galois
line, cote 149; final return) and **GRH_NIGHT** (its AG-C149 rows). Their returns and our intakes of them are attached; the
intakes record which findings were checked and how. Cite the settled findings; do not re-derive them. Alpöge's theorems and
his Lean archive are cited as theorems (L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with its Lean archive).

## Where it stands

**The K-groups of Z.**
- **K17-S17** (step 17 of Alpöge's note): the Lean theorem `UpperTheory.V.SmallClassNumbers.corGK` bounds the strict Selmer
  groups S_ℓ(Q, e) = ker(H¹(Z[1/ℓ], Q_ℓ/Z_ℓ(−e)) → H¹(Q_ℓ, Q_ℓ/Z_ℓ(−e))), which are dual to K_{2e}(Z){ℓ} (VK-PT). Over Q:
  log|K_{4k}(Z)| ≤ C_7(2k)^7 (VK-EXP7, C_7 not evaluated; the exponent-7 source chain was read by the run, not by our intake).
- **K17-S17-UNIT** (checked by our intake): the archive's statement `OneCharU_s` (`DenseThresholdCases/NumberU3US.lean`) bounds
  the Selmer length by 2Σ_{ρ∈X} v_ℓ(tr ρ(s) − t) over the source-admissible representations (`Adm3U_s`, compact U(3) over an
  imaginary quadratic field E; `Adm2A`, rank two); so if every difference tr ρ(s) − t is an ℓ-adic unit, the length is zero.
- **K17-K12-VANISH: K_12(Z) = 0.** For ℓ > 2^31: E = Q(√−3), e = 6, s = σ^{−1} at the split prime 7, t = 7^{−6} + 1 + 7^6. The
  U(3) branch has the single trace 157899/7^6; the GL_2 branch has traces 1 + a_7(f)/7^6, f in S_13(Γ_0(3), χ_{−3}). The product
  N_7 = 2^15·3^19·7·13^5·37·43³·47³·61·271³ has only primes ≤ 271. For ℓ < 2^31, Hart-Harvey-Ong's verification of Vandiver's
  conjecture. **Checks:** our intake recomputed the GL_2 half independently (T_7 on M_13(Γ_0(3), χ_{−3}) has characteristic
  polynomial (x − (1+7^12))²(x − 40250)²(x + 153502), and the cuspidal factor P_7 gives P_7(1 + 7^12) = 2^12·3^14·7·13^4·37·43²·47²·
  61·271², exactly N_7/(E_7 − 157899)). **Not independently checked:** the U(3) value 157899 (theorem u3-hecke), and the two
  coverage theorems (u3-coverage: every `Adm3U_s(ι,6,2)` representation is a level-one compact U(3) form of weight (6,0,−6);
  gl2-conductor: every `Adm2A(ι,6,6)` representation comes from S_13(Γ_0(3), χ_{−3})).
- **K17-K16-K20-K24, K17-K28-K36, K17-K32-VANISH, K17-K40-K44-K48: K_{4k}(Z) = 0 for 1 ≤ k ≤ 12**, with the auxiliary field
  Q(√−7) where Q(√−3) leaves a large prime (statement level in our intake; the run reports root and independent readings and exact
  replays). Q2-HIGHER4 (K_52, K_56, K_60) was open at the end, its computations pending.
- **The standing of `OneCharU_s`.** In the archive, `oneCharU_of_katoTwoW_rig_admI_automorphy` (`FOneCharU.lean`, line 75) proves
  `OneCharU_s` from nine propositions: `U3.CohInp`; `LemmaM`, `LemmaM'`, `LemmaP`; `KatoTwoW`; `RigidityFirstCase`,
  `RigiditySecondCase`; `AdmI_s`; `AutomorphyUnramifiedCoefficientsAlt`. It is an implication. Our syntactic estimate of the
  declaration closure of the archive's `riemannHypothesis` (the root takes no hypotheses) contains this implication,
  `propGK_of_numberU3U_of_oneCharU`, the definition `OneCharU_s`, and theorems discharging several of the hypotheses
  (`katoTwoW_of_printsH`, `UpperTheory.V.Alg.lemmaP`, `cohInp_alt`), all reached through
  `count_i_of_printed_bound_k_kato_automorphy`. If that estimate is right, `OneCharU_s` is a theorem of the archive.
- **Positive components** (K17-POSITIVE-COMPONENTS, numerical input checked): every prime factor of the numerators of B_2, …, B_32
  is below 2^31, so reflection kills the positive even components 2, …, 32 at every prime, independently of Alpöge.
- **The Voronoi route** (K17-K12-THREE-RANKS): K_12(Z) = 0 would also follow from H_5(GL_8), H_4(GL_9), H_3(GL_10) with
  St ⊗ Z[1/13!] vanishing. Our intake confirmed, against arXiv:1910.11598v1, that the endpoint cases of DEKM's Theorem 4.5
  (N = 8, k = 12; N = 9, 10, k = 11) are not supported by its displayed enumeration (Tables 3-4 index cells by perfection rank r,
  while §1.2.1 and Proposition 1.5 use projective dimension r − 1). That route is no longer needed for K_12.
- **Never done:** a comparison with C. Soulé, "A bound for the torsion in the K-theory of algebraic integers", Documenta Math.,
  Extra Volume Kato (2003), 761-788.

**The tower (Ihara's kernel question).** Write Ω_p for the maximal pro-p extension of Q(μ_p) unramified outside p, and Ω_p^* for
the fixed field of the kernel of G_Q → Out π_1(P¹ − {0,1,∞})^{(p)}.
- K17-P2-MOMENT (checked in full by our intake, with Gras-Jaulent, Hain-Matsumoto and Brown carried): Ω_2^* = Ω_2.
- K17-VANDIVER-KERNEL (proof read; the class-field steps checked; the Fukaya-Kato and Wake-Wang-Erickson inputs carried):
  Vandiver at p ⇒ Ω_p^* = Ω_p; K17-GREENBERG-KERNEL (statement level): X^+ finite suffices. Hence every prime below 2^31.
- **Q3-IRREG, open:** the remaining plus characters at primes where Greenberg's conjecture is not known; the cubic route needs
  arithmetic Triple-NV (K17-CUBIC-ODD, conditional).
- Integral odd generation of the tripod Lie algebra: at 2 (K17-2-ALL) and at regular primes; it fails at every irregular Greenberg
  prime (K17-INTEGRAL-CLASSIFICATION). Statement level.

**Cote 149.**
- AN_GRH A05: the anabelian statement A1 of cote 149, scans 35-36 (point separation), holds without GRH for hyperbolic curves
  over fields finitely generated over F_p, with the prime-to-p geometric quotient and the full arithmetic quotient (proof read by
  our intake; three same-model checks in the run).
- K17 F149-GENERIC, F149-MARKED-RECOGNITION: with the generic Galois marking π_1(U) → G ← G_K → G_k of scans 83-84, the geometric
  tangential sections of scan 85 are functorially determined; F149-BARE-EXTENSION and F149-UNMARKED-CURVE: without it they are not.
  Statement level in our intake.
- GRH_NIGHT AG-C149-NORMAL, -FULLLIFT, -CUSP: for the torsion-line-bundle family the cusp-inertia normalizer comparison is proved;
  AG-Q28 is refuted by a type (0,4) family over E: y² = x³ − x. Statement level.
- AN_GRH route 2 (an alternative mechanism for A1): A46 (checked in full by our intake) gives the rational primitive criterion in
  all characteristics and genera; A33 reduces point separation for genus-two curves in characteristic 2 to ordinary genus-two
  curves with Rosati-fixed O_5 multiplication (steps 1-2 checked); A36-A44 are failed constructions, A45-A52 criteria.

## The task

1. **Main question: Vandiver's conjecture through K_{4k}(Z) = 0 for every k.** K17's certificate proves K_{4k}(Z) = 0 for
   k ≤ 12 by finite Hecke computations on compact U(3) over Q(√−3) (and Q(√−7)) and on S_{2e+1}(Γ_0(3), χ_{−3}) (and level 7).
   Make the mechanism uniform in k:
   - (a) For e = 2k, determine the space of level-one algebraic modular forms on the definite unitary group U(3) over Q(√−3) of
     weight (e, 0, −e) (its dimension formula, its decomposition into endoscopic and stable parts) and S_{2e+1}(Γ_0(3), χ_{−3})
     (its dimension, its CM and non-CM parts), as functions of e.
   - (b) Determine the Hecke eigenvalues at the split prime 7 (or another fixed split prime) of every form in those spaces in a form
     uniform in e, or bound the prime factors of the certificate N_7(e) = ∏(E_7(e) − tr) uniformly; prove that for every e the
     certificate has no prime factor above 2^31 that is not removed by the Bernoulli/reflection argument K17 used at 9496386083 and
     8361790201, or find the first e where it does and treat it by a second auxiliary prime or field.
   - (c) Prove the resulting statement: K_{4k}(Z) = 0 for every k ≥ 1, which by the equivalence of Kurihara (Vandiver at ℓ ⇔
     K_{4k}(Z){ℓ} = 0 for all k) is Vandiver's conjecture at every prime. Where a degree e resists the fixed auxiliary data, change
     the auxiliary split prime, the field E or the level, and continue; record each such degree and the data that settle it.
   - (d) First, close Q2-HIGHER4: K_52, K_56, K_60, by the same criterion.
2. **The U(3) half of the K_12 certificate, by a second method.** Recompute the value 157899 (the Hecke eigenvalue at the split
   prime 7 on the level-one compact U(3) space of weight (6,0,−6) over Q(√−3)) by a method independent of K17's: an endoscopic or
   base-change description of that space (for instance its expression through Hecke characters of E and forms on U(2) or GL_2), or
   an independent lattice computation. Then prove the two coverage theorems (u3-coverage, gl2-conductor) against the published
   local-global compatibility and base-change theorems they rely on, with exact locators.
3. **The standing of `OneCharU_s`.** Name the nine hypotheses of `oneCharU_of_katoTwoW_rig_admI_automorphy` (FOneCharU.lean:75)
   exactly, and for each the theorem of the archive that discharges it in the chain used by `riemannHypothesis`
   (`count_i_of_printed_bound_k_kato_automorphy` and what it calls), with file and line. State whether `OneCharU_s` is then a
   theorem of the archive with no further hypotheses. The archive is public (https://alpo.ge/lean.tar.gz.part01 through part14;
   K17 used the mirror https://github.com/CocoSgt/riemann-hypothesis-lean at commit 7cbf7a0c32fca1badf05931879a37c3f8a2b03b4);
   our estimated closure (140 MB, not attached) was built syntactically from the source text, so trace the chain directly in the
   source files.
4. **The Soulé 2003 comparison.** State Soulé's bound for the torsion of K_m(O_F) with its exact constants and locator, compare
   it with VK-EXP7 (log|K_{4k}(Z)| ≤ C_7(2k)^7), and evaluate C_7 from the archive's constants.
5. **Q3-IRREG.** Settle Ihara's question Ω_p^* = Ω_p at the primes and characters not covered by K17-GREENBERG-KERNEL: the plus
   characters where X^+ may be infinite, by a positive-rank argument or an arithmetic proof of the Triple-NV condition of
   K17-CUBIC-ODD. Use the vanishings of item 1 (they kill components of the class groups of the cyclotomic tower) wherever they
   bear.
6. **Cote 149 after scan 36.**
   - (a) Section surjectivity (the section conjecture) for the prime-to-p quotient of π_1 of a hyperbolic curve over a finite field,
     starting from A05's configuration method.
   - (b) Point separation in higher dimension: hyperbolic polycurves and Artin neighbourhoods, from A05.
   - (c) A full read of F149-MARKED-RECOGNITION and F149-UNMARKED-CURVE against the literature on tangential sections and the section
     conjecture for tangential base points (Nakamura, Hoshi, Saïdi, Stix), with exact locators: say what is known, what is new.
   - (d) The relation of GRH_NIGHT's AG-C149 normalizer comparison to F149-RELATIVE.
7. **Route 2 as a geometric question.** For an ordinary genus-two curve E over F̄_2 whose Jacobian has Rosati-fixed O_5
   multiplication, and a point P, construct a pointed odd cyclic cover with primitive factor of 2-rank 0 (A33 + A46), or prove that
   such covers fail for some (E, P). Use A45-A52 and the failures A36-A44 as known data; the named next steps are a universal
   exponent or index bound for the primitive p-primary group (A51, A52) and prescribed reflection-orbit incidence (A36-A43).
8. **In Grothendieck's terms.** State every result also in his frameworks and on his sheets: the K-groups as the motivic
   cohomology of Spec Z and the Ext groups of mixed Tate motives (Deligne-Goncharov); the tower as the Teichmüller tower of the
   Esquisse (§2) and the letter to Faltings (1983); cote 149 by scan (35-36, 79-85); our row ids (K17, AN_GRH, GRH_NIGHT, LM6
   A.44-A.45, bridges Q06).

## The attached files

- `RETURN_K17_checkpoint_08_20261121T0616Z/`: the run continued: paper (K-group certificates, kernel theorems, F149 rows), QUESTIONS, LEDGER, CHECK_EVENTS, evidence (pinned Lean modules, certificates, scripts) (782 files: the run's paper, registers, scripts and certificates)
- `RETURN_AN_GRH_final_20261121T0821Z/`: A05 (A1 without GRH), route 2 rows A33-A52, its proof sources (1564 files: the run's paper, registers, scripts and certificates)
- `RETURN_GRH_NIGHT_checkpoint_07_20261121T0617Z/`: the AG-C149 rows (normalizer comparison, AG-Q28 counterexample) (207 files: the run's paper, registers, scripts and certificates)
- `INTAKE_K17_part1.md`: checks of step 17, the 2-kernel proof, F149-UNIT
- `INTAKE_K17_part2.md`: check of K17-VANDIVER-KERNEL (class-field steps), scope of FK/WWE
- `INTAKE_K17_part3.md`: Greenberg kernel, K12 three ranks, F149 recognition (statement level)
- `INTAKE_K17_part4.md`: K12 certificate (GL2 half recomputed), DEKM decision, the OneCharU_s addendum
- `INTAKE_K17_part4_CHECK_EVENTS.tsv`: our check events on the final
- `INTAKE_AN_GRH_part3.md`: what is checked of A05, A33, A46; the section-6 list
- `INTAKE_GRH_NIGHT_part2.md`: AG-C149 rows and their scope
- `INTAKE_gl2_weight13_T7.py`: our independent T_7 computation on M_13(Gamma_0(3), chi_-3) for the K12 certificate
- `LIT_DEKM_Voronoi_K8/` (arXiv:1910.11598, LaTeX source): the Voronoi route and the endpoint gap of Theorem 4.5
- `LIT_Chen_partially_regular/` (arXiv:2602.05090, LaTeX source): used by K17-BOTH-COMPANIONS (Thm 1.1, Cor. 1.4)
- `LIT_Brown_mixed_Tate_motives_over_Z/` (arXiv:1102.1312, LaTeX source): rational Deligne-Ihara, used throughout the kernel results
- `LIT_Soule_2003.pdf`: task 4: the comparison never made

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: Prove K_{4k}(Z) = 0 for every k ≥ 1, and with it Vandiver's conjecture, by making K17's unit-trace certificate for compact U(3) and S_{2e+1}(Γ_0(3), χ_{−3}) uniform in the weight. Give it most of the time.
When one approach stalls, take the next one. Deliver nothing while an item is undecided and an untried approach
remains. A gap in a proof is an undecided step: attack it, never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the strongest
proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less. Cited statements you use get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with
who, how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `KTOWER_checkpoint_<NN>.zip` with `NN` counting up.
Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every deliverable written so far
and everything that documents the work, so that a new session can continue from it and the attached files. It is never
a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `KTOWER_final.zip`, holding:
1. **The paper**, `KTOWER.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change: for our programme on Grothendieck's work (cote and scan),
   for our runs' open rows (run and statement id), and for the open conjectures named in the task.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
