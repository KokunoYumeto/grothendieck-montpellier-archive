# Intake of GHOSTS (prompt 39): Hodge ghost classes at supersingular and ordinary primes

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent), launched by the main session (Claude Opus 5.5 at effort
max), 21 Nov 2026, round 3. The brief is `field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`, with the item "Hexagon
readiness" (`field_experts\HEXAGON_CANDIDATES.md`). Work file: `agent_notes\20261121_intake_HODGE_SIGN_NOTES.md`. Check
events: `INTAKE_GHOSTS_20261121_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\GHOSTS_final_20261121T0256Z_unzipped\`, the final and the only GHOSTS folder.
- The run is GPT-6 Astra (ChatGPT Pro mode). It ran from about 00:5x to 02:56 UTC.
- The paper is 69 pages: `GHOSTS.tex` plus 17 section files.

**The prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\39_HODGE_GHOST_CLASSES_at_supersingular_and_ordinary_primes\PROMPT.md`.
Its tasks:
1. prove sketch 2.5;
2. check 032 Remark 8.5;
3. carry out T9;
4. compute the least complexity of the T5 Weil class at supersingular and ordinary primes;
5. bound it uniformly with the GRH results, and carry the bound to Route 2's gate.

**What I read:**
- `README.md`, `QUESTIONS.tsv` (21 rows), the final block of `LEDGER.md`, and `IMPLICATIONS.md`;
- in full: `sections\bounded.tex` (B01–B06);
- in full: `sections\local_weil.tex` (P06–P14, P02, P03);
- in full: `sections\family_checked.tex` (R10–R12);
- the statements of V01–V07, W04, R13a–c, R30, R31, C03, C04, C06, C07, C15 and C18;
- C16 and the archive readings (`sections\source_audit.tex`, `framework_map.tex`, `research\archive_reading.md`);
- the run's check events for the main findings.

**Computation:** I reran the run's self-contained W04 certificate (`research\w_exact24_certificate.py`, standard library
only) from a scratch copy. It ended "PASS W04: no certificate of cost below 24".

**Scope:**
- **Read in full with a targeted proof check (19):** B01–B06 (with B02a), P06, P07, P08, P09, P12, P13, P14, R10, R11,
  R12, R31 and C15.
  - P13: I rederived the case p > 3; I read the cases p = 2 and p = 3.
- **Read with a plausibility check (1):** R30.
- **Computation rerun (1):** W04. A rerun of the run's own program, not an independent derivation.
- **Statement level (about 25):** C01–C07, C16, C18, V01–V07, W01–W03, R13a–c, R20–R24, R40–R45, P02 and P03.

**Scan numbering:** GHOSTS uses our numbering. Its scans are one-based PDF pages, with folios given alongside. I
checked it against our text of record:
- `14_scan044.tex` opens "27.8.65, Mon Cher Serre", with `\mspage{43}`;
- cote 16 scans 044–047 and 048–050 are the two Coates letters (see the HECKE_DIV intake).

## 1. Verdicts, finding by finding

### Sketch 2.5: the bounded-specialization criterion

- **B01, bounded effective pairs: confirmed.**
  - The construction: FGA 221, Lemma 2.4 (bounded Hilbert polynomials) and Theorem 3.2 (projectivity); finite products
    of Hilbert schemes.
  - The relative cycle class: SGA 4½, *Cycle*, 2.3.7–2.3.8.
  - The class condition is open and closed, because Δ is a section of a lisse sheaf on a noetherian scheme.
- **B02, the corrected sketch Lemma 2.5: confirmed.** With N and D fixed, cycles exist (1) in characteristic 0, iff
  (2) at infinitely many places, iff (3) at every place. The argument:
  - the image of the projective class locus is closed;
  - a proper closed subset of the curve U is finite;
  - comparison does the rest.
- **B02a: confirmed.** The sketch's statement needs *integral* numerators: t = h^r/2 on P^g is rationally algebraic,
  but N = 1 fails. The run cites the precedent itself: Brünjes–Serpé (arXiv 0901.4853, Thm 3.4). **Sketch 2.5 is right
  in substance, needs that one correction, and is not new in principle.**
- **B03, eventual constancy or cofinite divergence: confirmed.** F_C is closed in U, and F_{C₀−1} is finite. This is
  the precise "ghost" theorem; see section 2.
- **B04, one prime outside an exceptional integer b_D: confirmed** (generic flatness, EGA IV₂ 6.9.1; going down).
- **B05, descent from C to Q̄: confirmed.**
- **B06, bounded numerator degrees bound the multipliers: confirmed.** Each connected component of H_D admits at most
  one N. This is the same mechanism as HECKE_DIV P6(iv).

### Task 4: the least complexity of the T5 Weil class

- **P06, the projector e_W = (9+S)(2−R−R²)/54: confirmed.**
  - On Λ^aV_σ ⊗ Λ^{4−a}V_σ̄: S acts by 9(−1)^a; R acts by ω^{2a−4} = ω^{2−a}.
  - (2 − R − R²)/3 is 1, 0, 1 at a = 0, 2, 4.
- **P07, the six-surface certificate 3w = PU − PV − QU − 2QV: confirmed at the level of the method.**
  - I checked RP = −P − Q and RQ = P.
  - I did not expand all six Z_{a,b}.
- **P08 and P09, c_θ(t_*) = 16 over C: confirmed.** I rederived:
  - z(Γ_a) = ā², z(t_*) = 2(1 − ω), |z| = 2√3;
  - Cauchy–Schwarz on (2,0)-forms gives |z(V)| ≤ √(ab);
  - deg V = 2(a+b+c), with c ≥ 2√(ab) by the Hodge index theorem on surfaces;
  - so a cycle of degree ≤ 14 has |z| ≤ √2, while 2N√3 > 2√2.
  - The upper bound is four graphs of degree 8, with N = 1.
  - I also checked t_*² = 4(4 − 2 + 4) = 24.
- **P13, exactly 16 at every geometric good reduction, ordinary and supersingular: confirmed for p > 3** (rederived) and
  read for p = 2, 3.
  - The algebraic coordinate z replaces the period: pairings against w and Rw, which are intersection numbers.
  - z(Γ_h) = conj(det h_K).
  - Budgets: a graph of degree ≤ 14 has T_h ≤ 6 − d. Then:
    - at most one non-K entry (I checked the three cases);
    - Schur gives |det h_K|² ≤ deg h ≤ 2;
    - nondominant surfaces with z ≠ 0 have degree ≥ 18.
  - For p = 2 (the Hurwitz order) and p = 3, the bounds 5/3 and √2 are read; the run checked them twice.
- **P14: confirmed.** At p = 5, h = [[2, j], [−j, 2]] with j² = −5 is an automorphism; I checked
  h·[[2, −j], [j, 2]] = −I. It has z = 4 and degree 40. So the complex bound |z| ≤ √(ab) **fails in characteristic p**,
  which is why P13 needs the low-degree classification.
- **P12: confirmed.** c(t_*) = 16k² for θ^k, and 8√3·M ≤ c(Mt_*) ≤ 16M.
- **V01–V07** (the primitive half-class t₀ = t_*/2 also has minimum 16 everywhere; V07 gives the integral Weil lattice
  Zu ⊕ ZRu with Gram matrix [[6, −3], [−3, 6]]): **statement level.** I checked V07's Gram matrix against t₀² = 6,
  consistent with t_*² = 24.
- **W01–W04** (the exact complex minimum of w = e_W[Γ₁] is 24): **computer-assisted.**
  - W01–W03, which reduce the problem to a finite abelian-surface catalogue, I read at statement level.
  - The W04 program: **rerun, PASS.**

**What these mean for the task.** The function asked for, "least complexity of t_v as a function of v", is constant: 16
for t_* and t₀, at ordinary and supersingular primes alike. Two cautions from the run:
- P12 and V04: the value is not a function of v and the Newton type alone. It depends on the class normalization and the
  polarization.
- P02/P03: on the E⁴ isogeny class, a prime is ordinary for p ≡ 1 mod 3 and supersingular for p ≡ 2 mod 3. That is
  false on the whole family: P03 is a K-action with other prime types.

### Task 5: the uniform bound and Route 2's gate

- **R10, bounded detection gives an integral Weil basis: confirmed.**
  - u = [18Z + 2S^*Z] − [9R^*Z + 9R²^*Z + (SR)^*Z + (SR²)^*Z].
  - Pullback by S multiplies the θ-degree by 3⁴/3² = 9, so each side has degree ≤ 36·D₀.
  - Comass gives d ≤ 729·D₀².
  - 1 + R + R² = 0 gives the Gram matrix d·[[1, −½], [−½, 1]].
- **R11, extraction cost C₄ = 531441·δ·D₀⁴·(1 + 4⌈√T⌉): confirmed** (Cramer's rule with Δ = 3d²/4; 729² = 531441).
- **R12, an explicit detecting degree D₀ = 132,269,760 on the principal Eisenstein component: confirmed, given Schoen's
  dominance** (Compositio 65, 1988, §3, pp. 26–30; Addendum, Compositio 114, 1998, p. 330). I checked:
  - type (1,1,3,3) and L⁴ = 216 for the Prym B of an unramified cyclic triple cover C → X (genus 7 over genus 3);
  - deg_{3Θ} W₄(C) = 3⁴·7!/3! = 68040, and deg_{3Θ} T₀ = 3⁴·216 = 17496;
  - Bézout for the components of an improper intersection (Fulton Ex. 8.4.6);
  - deg_L Z ≤ 68040·17496/9 = 132,269,760;
  - the descent by a maximal isotropic subgroup of order 9 to a principal polarization;
  - that the lattice is U ⊕ U (Meyer; O_K is a PID);
  - density on the component, and closedness (R13b).

  **This is bounded division on the principal Q(ω) Weil fourfold component, with an explicit integer, from published
  inputs.** R20–R24 extend it to every fixed polarization and determinant through a principal sixfold, with detector
  D₆ = 57,854,793,024,000. I read R20–R24 at statement level.
- **R30: plausible and correct in method.**
  - Under Dirichlet GRH for characters mod 3 (Alpöge, a theorem in our convention), with Lee's explicit constants, there
    is a prime p ≡ a mod 3 with p ∤ b and p ≤ max(e¹⁴, 4 log b + 4).
  - The method: θ(x;3,a) ≈ x/2 exceeds Σ_{p|b} log p ≤ log b.
  - **Strict scope note:** the modulus 3 is fixed, so unconditional explicit forms of the prime number theorem in
    progressions give the same O(log b) shape with other constants (Bennett–Martin–O'Bryant–Rechnitzer, from memory).
    **GRH improves constants here; it is not essential.**
- **R31: confirmed.** If the product of distinct primes exceeds b, some prime is outside b_D, and B04 applies. This is
  unconditional, as the run says.
- **R40–R45** (a terminating algorithm for the whole good-prime function): **statement level.**

### Tasks 2 and 3: Remark 8.5 and T9

- **C01** (Remark 8.5 as a deduction from 032 with CM transport; the auxiliary CM variety may have dimension n·dim A):
  statement level.
- **C02 refutes the sketch's 2.6 inference.** The sketch reads Remark 8.5 as "a CM point x_p of the same special
  subvariety". The source (p. 33) disclaims that. Statement level; the source quote is in the run.
- **C03–C06** (degree and denominator charges; transport data are not canonical in p): statement level.
- **C07** (at ordinary primes, every algebraic class lifts to the canonical Serre–Tate lift): **conditional on 032**,
  as stated; statement level.
- **C18, T9 made exact: confirmed** (it follows from P09/P13 with the identity marking). The transport cost is constant,
  (1,16,16) for t_* and (2,16,16) for t₀, at every prime. **So on this example the sketch's T9 question ("how do the
  degree and the denominator grow with p?") has the answer: they need not grow at all.** C06: growth is an artefact of
  the chosen transport.

### Source corrections

- **C15: confirmed.** Milne's report (Hexagon 2611.00244, §3.6) prints the primitive form without its sign (−1)^r. A
  primitive divisor on E×E has negative square: for example (F₁ − F₂)² = −2.
  - **This should be reported to Milne** (memory: report corrections; draft emails when a gap is found). I list it for
    the main session; I made no draft outside my folder.
- **C16:** van Hoften–Sempliner Th. 4.0.2 gives no numerical bounds. A checked limitation, statement level.

### Counts

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 19 |
| Plausibility, confirmed with a scope note | 1 (R30: GRH not essential) |
| Computation rerun, PASS | 1 (W04) |
| Statement level | about 25 |
| A gap | 0 |
| Refuted | 0 |
| Scope notes | R30 (GRH inessential); C07 and C01 (conditional on 032); B02 (precedent Brünjes–Serpé) |

**The run's own refutations, which I confirm:**
- the rational-cycle reading of sketch 2.5 (B02a);
- the same-family inference in sketch 2.6 (C02);
- prime type as a function on the whole family (P03);
- a complexity function of the prime alone (P12, V04, C06);
- the complex period inequality in characteristic p (P14);
- Milne's unsigned display (C15).

## 2. What is new, and the ghost theorem in the project's terms

**The project's term, made a theorem.** A *ghost* is an object that passes every test at one prime. B03 together with
032 Remark 8.5 gives the exact statement for Hodge classes on abelian varieties over Q̄:
- every Hodge class t has finite complexity c(v) at every good place v (032 R8.5, conditional on 032);
- if t is algebraic, c(v) equals the constant c_η outside finitely many places (B03);
- if t is not algebraic, then for every C only finitely many v have c(v) ≤ C (B03).

**So a non-algebraic Hodge class would be a ghost in the strict sense:** it passes the test at every single prime, and
fails only because its complexity escapes to infinity along every infinite set of primes. Conversely, bounded
complexity along infinitely many primes forces algebraicity (B02, B06; HECKE_DIV P6). There is no third behaviour.

**In Grothendieck's frameworks:**
- the Hilbert scheme of FGA 221 is the parameter space;
- specialization of cycle classes (SGA 4 XVI 2.2; SGA 4½ *Cycle* 2.3.8) gives the open-and-closed class condition;
- generic flatness (EGA IV₂ 6.9.1) gives the exceptional integer.

**Against the literature:**
- B02 is known in principle (Brünjes–Serpé 2009; the run says so). B03's exact eventual constancy may be new as stated;
  this needs a search.
- **R12 + R11 (+ R20–R24): new, as far as I know.** Explicit uniform degree and multiplier bounds for Weil classes on
  Q(ω) Weil-type abelian fourfolds, from Schoen's published Prym construction. Schoen proves algebraicity; the explicit
  constants are new.
- **P09, P13, V06 and W04** are new exact computations: minimum 16 at every good prime; minimum 24 for w.

**Against tonight's runs:**
- **HECKE_DIV M10** gives the fourfold bound from Markman's preprint, with astronomically larger constants. **GHOSTS R12
  makes the principal Q(ω) fourfold case unconditional on preprints**, with D₀ ≈ 1.3·10⁸.
- HECKE_DIV P6 and GHOSTS B02/B06 are the same principle. GHOSTS cites the precedent.
- HECKE_DIV P1/P3, THETA3 C13 and GHOSTS P06/R10 are the same projector idea.

**Against our results:**
- HODGE_SIGN SG-04's finite-field part (Tate classes on E^n are divisor products at ordinary and supersingular primes)
  is the setting of P13. GHOSTS computes the exact minimal cost of such a representative.
- My HODGE_SIGN intake proposed exactly this attack for prompt 39: complexity of t_v as divisor products, at ordinary
  versus supersingular primes. The answer is constant 16.

## 3. The two proofs, and HODGE_SIGN

- **Alpöge (Dirichlet GRH mod 3):** used only in R30, for constants. Not essential (section 1).
- **Masullo:** not used.
- **032** (CM Hodge; Remark 8.5) is used in C01 and C07, marked by the run as a cited input. **These are conditional on
  032 in our convention.** B01–B06, P06–P14, R10–R12 and W04 do not use 032.
- **H01 (the sign-only proof, hexagonmath.org/2611.00789):** not used and not changed.
  - GHOSTS's positivities are the surface Hodge index (P08, P13) and Hodge–Riemann on the Weil plane (R10). Those are
    intersection forms; the H01 sign is not.
  - In the project's terms: GHOSTS's lower bounds in characteristic p rest on the **Hodge index theorem for surfaces**
    (Grothendieck 1958, the one case of the Hodge-type standard conjecture known in every characteristic), never on
    purity. This again confirms HODGE_SIGN's distinction: purity sees nothing of cycles.
- **Overclaims:** none found. The run's statements of scope are accurate.

## 4. Integration (edits listed, not made)

**Hodge sketch** (`reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`):
- **2.5:** replace "(proved; arithmetic form)" by "(proved with integral numerators: GHOSTS B02, B02a, B06; precedent
  Brünjes–Serpé, arXiv 0901.4853, Thm 3.4). B03: an algebraic class has eventually constant local complexity; a
  non-algebraic one has local complexity tending to ∞ cofinitely."
- **2.6:** after "it would be a ghost", add: "GHOSTS B03 makes this exact. C02: Remark 8.5's transport goes through an
  auxiliary CM variety, possibly of dimension n·dim A, not a CM point of the same special subvariety. Correct 'a CM
  point x_p of the same special subvariety' accordingly."
- **First tests, T5:** add "Bounded division on the principal Q(ω) Weil fourfold component is proved with
  D₀ = 132,269,760 and C₄ = 531441·δ·D₀⁴·(1 + 4⌈√T⌉) (GHOSTS R10–R12, from Schoen 1988/1998, checked). General
  polarization: R20–R24 (D₆ = 57,854,793,024,000)."
- **T9:** add "On E⁴ with t_*: the transport cost is constant, (1,16,16), at every prime (GHOSTS C18). Growth in chosen
  transports is not intrinsic (C06)."
- **"Where GRH does and does not enter":** add "GHOSTS R30: Dirichlet GRH only bounds a finite prime search, and is
  inessential for modulus 3."
- **Route 5 / 032 Remark 8.5 row:** "conditional on 032; at ordinary primes C07 lifts every algebraic class to the
  canonical lift."

**Other runs' rows:**
- HECKE_DIV Q4-T5 (M10): the principal component is now also proved from published inputs (GHOSTS R12).
- HECKE_DIV P6 and GHOSTS B06: cross-reference.

**Grothendieck's texts:**
- Cote 14, scans 044–047 (letter to Serre, 27.8.65): C^i is defined modulo **algebraic** equivalence (scan 044). GHOSTS
  works modulo homological equivalence. The distinction is in the run's framework map.
- Cote 16, scans 048–049: the Cayley–Hamilton algebraic inverse. R11's integral Gram-matrix inversion is its integral,
  effective form.

**Outside correction:** Milne's report, §3.6, sign (C15).

## 5. How it bears on the running Hodge prompts, and the attacks it opens

- **38 (HECKE_DIV, final in):** R12 supersedes M10's dependence on Markman for the principal Q(ω) component.
  - Next attack: the E⁸ analogue of R12. Schoen-type Prym constructions in dimension 8 would remove the dependence on
    Severn.
- **40 (cote 44):** P08's mechanism (the surface Hodge index bounding periods) is the cote 44 positivity in its known
  case. It is a model for Th. 4 on Weil classes.
- **41 (degrees as L-values):** D₀ and C₄ are explicit benchmarks for any Rallis-type degree formula. The minimum 16 is
  the floor at E⁴.
- **The ghost line itself, the next attack.** On a very general Weil-type fourfold over Q̄, all classes are algebraic by
  Schoen and Markman, so B03 says c(v) is eventually constant. **The first place a ghost could live** is a Hodge class
  not yet known to be algebraic: on abelian varieties of dimension ≥ 5 outside the Weil/CM cases, or on non-abelian
  varieties.
  - The run's R40–R45 algorithm gives a computable test, but only for a known class.
  - The concrete attack: choose a Hodge class on a simple non-CM abelian fivefold or sixfold of Mumford–Tate type with
    exceptional classes (Mumford's example of a fourfold has none; dimension ≥ 6 is needed). Bound c(v) at ordinary
    primes through C07-type canonical lifts, conditional on 032.

## 6. Hexagon readiness

| Candidate | 1 Complete | 2 Self-contained | 3 Stable | 4 Checked | 5 Of interest | Verdict |
|---|---|---|---|---|---|---|
| **Explicit uniform bounded division for Weil classes on Q(ω) Weil-type abelian fourfolds** (R10–R13; R20–R24 for general polarization) | yes: complete proofs in a final return | yes: Schoen, Compositio 1988 and 1998; FGA; Fulton; Milne; Griffiths | final; no running prompt of ours supersedes it (HECKE_DIV M10 is weaker and conditional); **no literature search yet** | my targeted check of R10–R12; the run's independent re-proofs of R10 and R11; R12 independently read in the run | **medium to high:** an explicit integer for the Hodge conjecture's division gate in Schoen's family, timely after Markman 2025 | **two gates away:** (a) a literature search (effective Hodge, Schoen, Markman's degree remarks); (b) an independent re-proof of R12 and of R20–R24 outside the run. Then a self-contained write-up and my read of every page. **I recommend the main session flag it to the user as the strongest Hodge-line candidate after H01.** |
| Exact minimum 16 at every good prime (P09, P13, V06), plus minimum 24 (W04) | yes | yes | yes | targeted check (P09, P13 for p > 3) and the W04 rerun | low to medium: a neat exact example | one gate (the p = 2, 3 cases checked independently); a candidate for a short note together with the row above |
| B02–B06 (the ghost dichotomy) | yes | yes | yes | targeted check | medium | B02 has a precedent (Brünjes–Serpé). B03 alone needs a literature search. Best posted inside the row above, not alone |

**Correction to my part-2 note on HECKE_DIV:** P6's principle has the precedent Brünjes–Serpé (arXiv 0901.4853,
Thm 3.4), as GHOSTS records. I add this to the HECKE_DIV part 2 file.
