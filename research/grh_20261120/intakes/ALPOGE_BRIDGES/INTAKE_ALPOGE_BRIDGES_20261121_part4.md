# Intake of ALPOGE_BRIDGES (prompt 22), part 4: the final return (checkpoint 09), 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it writes "effort not exposed". Parts 1 to 3 read checkpoints 01,
03, 05 and 06.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z_unzipped`, made 05:46:53 UTC after
  405 min of work. By the user's three-hour rule this is the run's **final return**. Its formal reviews 03 (04:02) and
  04 (05:04) both found movement; review 05 (due 06:01) never happened. The run ended while still moving.
- **Read:**
  - LEDGER.md lines 732-1140: checkpoint 06 to the checkpoint 09 preparation, including the evidence for reviews 03 and
    04;
  - the final rows G-123-RANK-STRICT, G-123-DISTINGUISHED, AQ-Q-SA08-CS, AQ-Q-SA08-TL and AQ-Q-134-SCOPE;
  - in ALPOGE_BRIDGES.tex, **CC-RK04 in full** (lines 20845-20870, with the Richardson locator) and **BR-15-CLASSBOUND**
    (lines 12729-12800: the statement and the class-number half of the proof).
- **Statement level:** AQ-136-COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES, FIRST-SKELETON, FREE-ZERO-FORMS,
  HIGHER-COMPLETION, MULTIPLICATIVE, PD-OPERATIONS, PD-RIGIDITY; F-SM36-F-SM44; CC-AG12-17; CC-XC05-23; BR-14-SEP;
  BR-15-SLOPEBOUND, ORBIT-RETRACT, QUADRIC-DISCRIMINANT, QUADRIC-TATE; CC-XC13 (Deligne parity).
- **Changes to parts 1-3:** none withdrawn or corrected in the run. **One change of weight, from this intake (§2):** the
  rank statement behind BR-12302 is known in the literature (Richardson 1987, Lemma 5.1, attributed there to Slodowy).

## 1. What the run settled, and what it left open

**Settled (in the end).**
- **Cote 136** (SA08 C.3, Grothendieck's divided-power de Rham conjectures):
  - the strict form of (b) is false over every ring (AQ-136-STRICT, part 2);
  - (a), a strict common admissible source, is proved for any finite family over every ring with only finitely many
    non-unit primes (AQ-136-COSPAN, SEMILOCAL-SOURCES), and over any ring it is *equivalent to connectedness* of the
    category (CONNECTED-SOURCES);
  - terminality of the localized groupoid holds over the same rings (AQ-136-SEMILOCAL, part 3).
- **Cote 134-8** (the Dérivateurs' linear Thm(?)): proved for AB4 categories with enough projectives (F-SM-32). F-SM44
  reduces the original compatibility gate to surjectivity in degrees ≥ 2, with injectivity in all degrees proved. F-SM39
  settles the raw counit for locally scalar-projective connective-chain categories.
- **Cote 123** (letter to Kostant): every question has an answer in every simple type (part 2). The rank part rests on
  known theorems (Richardson 1987), which is the change of weight noted in §0.
- **Cote 14:** the parameter comparison is closed for every smooth connected separated finite-type parameter (BR-14-SEP).
- **Cote 15** (motives over F_p, the abelian sector):
  - complete finite descent procedures and source-field profiles (CC-AG12-17);
  - forward cross-cycles by actual Chow correspondences for low-degree Chow-generation classes: rationally chain
    connected surfaces and threefolds, quadric fibrations over curves, supersingular K3 and supersingular abelian classes
    (CC-XC16-23);
  - all conditional where stated on the 2026 preprints of part 3 (CC-TATE01-03).
- **Correction to a preprint:** Thakur 2020 (arXiv:2001.00210v1), Prop 2.9, p. 6, is refuted (BR-15-CLASSBOUND).

**Left open.**
- Cote 136: connectedness, and with it (a) and terminality, over Z.
- Cote 134-8: higher surjectivity, degrees ≥ 2.
- Cote 15: the general forward-cycle gate for arbitrary smooth projective X, which amounts to full Tate.
- Masullo: the R-MAS-KERNEL intertwiner, the same gate as GRH_NIGHT's Q-MAS-GEOMETRIC-NARROW.
- The non-CM period gates (cote 18) and R-GTHAT.

## 2. Verdicts on the main new findings

| id | statement | verdict |
|---|---|---|
| **CC-RK04** | for every complex simple 𝔤 there is exactly one nilpotent orbit of dimension N − r − 2, and at it rank(dχ) = r − 1 (Richardson 1987, §5 opening and Lemma 5.1, p. 234, attributed to Slodowy); the unique unipotent orbit follows by the polynomial exp/log isomorphism | **confirmed** (the exp/log transfer argument is right). **Consequence for H08:** the corrected answer to Grothendieck's strict rank prediction is a known theorem. BR-12302's sp₄ computation, which I checked by hand and by sympy, is an explicit instance of Richardson's lemma. |
| **BR-15-CLASSBOUND** | Thakur 2020, Def 2.3 and Prop 2.9, p. 6: a type IV(1,d) abelian variety has a model up to isogeny over F_{p^{h_K}}. Refuted by a geometrically simple threefold over F_{2^9} with Frobenius polynomial (T² − 24T + 512)³, K = Q(√−23), h_K = 3, which has no geometrically isogenous model over F₈ | **the class-number and Weil-number arithmetic confirmed; the Honda-Tate index computation (CC-AG14) statement level.** γ = 12 − 4s has norm 144 + 368 = 512 = 2⁹ and trace 24. (η) = 𝔭³ with N(η) = 8. No element of norm 2. The Minkowski bound 2√23/π < 4 gives h_K = 3. I did not open Thakur's preprint, nor CC-AG14's local-index computation. |
| AQ-136-COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES | strict common sources for semilocal rings; over any ring, (a) ⇔ connectedness | statement level. Three readings recorded by the run (author, peer, root). |
| AQ-136-FIRST-SKELETON, FREE-ZERO-FORMS, HIGHER-COMPLETION | a shared free integral first skeleton for any finite family; free weight-one zero forms cannot repair the integral source; arbitrary relative completion is refuted (p·a = w·T^{[w]}) | statement level; failed integral routes, each with its obstruction. |
| F-SM39, F-SM44 | the raw counit for locally scalar-projective categories; the compatibility gate reduced to higher surjectivity | statement level. |
| CC-XC16-23, CC-AG12-17, BR-14-SEP | as in §1 | statement level. They rest on the published Vial 2013 Thm 4.2 / Cor 4.4 / Cor 4.8 and Kahn-Sujatha, cited with locators. |

**Counts for part 4.**
- Confirmed with every step checked: 1 (CC-RK04).
- Partly confirmed: 1 (BR-15-CLASSBOUND, the arithmetic half).
- Statement level: about 45 ids.
- Gaps: 0. Refuted: 0. Changes to parts 1-3: none withdrawn; one weight changed (BR-12302 is an instance of a known
  theorem).

## 3. What is new

- **Cote 136** is the run's strongest original-question result. (b) is refuted in its strict form. (a) and terminality
  are proved except over Z. Over Z, (a) is equivalent to connectedness.
- **Cote 15:** forward cycles are constructed for several geometric classes. This is a real step on Grothendieck's
  question of 15/100-106, conditional where stated on the 2026 CM-Hodge preprints.
- **The Thakur correction** is new and checkable.
- **Cote 123:** the answers are complete. The rank part is known (Richardson, after Slodowy). The A_{2m} exclusion
  (CC-APG04) and the opposition table have not been searched in the literature.

## 4. The scope of the two proofs

Nothing new uses A_D or M. The cote 15 abelian results depend on the 2026 preprints (CC-TATE01-03), as flagged in part 3.
No statement claims more than its inputs give.

## 5. Integration

1. **SA08 intake** (`INTAKE_RESEARCH_SA08_C3_D031_20261120.md`):
   - row A-CS: "(a) holds over every ring with finitely many non-unit primes (AQ-136-COSPAN, SEMILOCAL-SOURCES); over any
     ring (a) ⇔ connectedness (AQ-136-CONNECTED-SOURCES); open over Z";
   - row A-TL: "terminality in the same scope; strict (b) false (AQ-136-STRICT)".
2. **Cote 123 notes** (physical pp. 22-23, footers 21-22):
   - "the rank question is answered by Richardson 1987, Lemma 5.1 (after Slodowy): rank r − 1 at the subregular orbit in
     every type; hence Grothendieck's predicted strict drop in non-simply-laced types is false (explicit sp₄ instance:
     BR-12302)";
   - "distinguished class: exists iff not A_{2m} (CC-APG04; literature not searched)".
3. **Cote 15 notes:** the abelian sector is classified (CC-AG*). Forward cycles exist for the classes of CC-XC16-23. The
   general gate is full Tate.
4. **Cote 14:** AQ-Q-14-F is closed for all separated finite-type parameters (BR-14-SEP).
5. **Corrections to report:** Thakur 2020, Prop 2.9 (BR-15-CLASSBOUND), and, from the run's notes, an erratum in an arXiv
   source's §5.9 subregular E₈(a₁) line (V₁₇ should be V₂₉; ledger near CC-RK03). Both go to their authors, following
   the memory rule "report corrections".

## 6. Prompt updates: what the successor needs

1. **Main question: cote 136 over Z.** Connectedness of the admissible category over Z, equivalently (a) over Z, and
   terminality over Z.
   - Known data: the five failed integral constructions, FREE-ZERO-FORMS, HIGHER-COMPLETION, FIRST-SKELETON (connectivity
     at the level of the first skeleton), and SEMILOCAL (uniform bounds fail as P grows).
   - The attack named in part 3: uniformity of the weight cutoffs across all primes, or a proof that it must fail. The
     latter would refute connectedness over Z.
   - Also ask for the homotopy reading of « 'égalise' » (part 2).
2. **Cote 134-8:** the higher-surjectivity gate (degrees ≥ 2) of F-SM44, or a counterexample satisfying Grothendieck's
   scalar/tensor/interval hypotheses.
3. **Cote 15:** the forward cross-cycle gate for a first class beyond CC-XC16-23 (for example cubic fourfolds or K3
   surfaces of finite height), with full Tate as the general target. Tag every abelian-sector input with the 2026
   preprints, or replace them by published results where possible.
4. **Cote 123:** a literature search for CC-APG04 and the opposition table (Kostant 1959, 2010; Steinberg 1965 §9;
   Richardson 1987; Slodowy 1980), and a write-up of the letter's answers as one companion section.
5. **Masullo:** move R-MAS-KERNEL to the successor of GRH_NIGHT or of prompt 33 (see GRH_NIGHT part 3, §6 item 1) rather
   than continue it here.
6. Write the model as "GPT-6 Astra (ChatGPT Pro mode)".

## 7. Hexagon register changes (no edit made; for the main session)

**H08 (BR-12302: Grothendieck's strict non-simply-laced rank prediction in the letter to Kostant is false; sp₄
counterexample).**
1. **Complete:** yes.
2. **Self-contained:** yes.
3. **Stable / not superseded: fails.** The run's own final reading (CC-RK04) cites Richardson 1987, §5 and Lemma 5.1,
   p. 234, which states rank r − 1 at the subregular orbit in every simple type and attributes it to Slodowy. The
   corrected answer is therefore known, and BR-12302 is an explicit instance. What is new is only the archival
   observation: Grothendieck's 1969 prediction was wrong, as the later literature implies.
4. **Checked:** yes (intake check plus an independent sympy computation).
5. **Interest:** low as mathematics; moderate as history of the archive.

**Recommendation:** remove H08 as a research post (memory rule "superseded results are not posted"). Keep it as a
paragraph of a cote 123 companion note, citing Richardson, together with CC-APG04. **The gate for the companion note:**
the literature search for CC-APG04.

**H07 (A05):** not in this run. See AN_GRH part 3: the gates are a literature search and an independent re-proof of
Steps 1-2.

**New entries from this run:**
- **AQ-136-STRICT, with (a) and terminality away from Z** ("Grothendieck's de Rham conjectures of cote 136: what holds
  away from Z, and what fails").
  - Tests 1, 2 and 4 hold for STRICT (my check in part 2).
  - Test 3: (a) and terminality over Z are open, and a successor would settle them.
  - Test 5: moderate (p-adic cohomology).
  - **Candidate later.** Gates: the Z case, or a decision to post the semilocal results with Z as an explicit open
    question; an independent re-proof of AQ-136-COSPAN or SEMILOCAL.
- **BR-15-CLASSBOUND** (refutation of Thakur 2020, Prop 2.9). Complete and checkable, but of narrow interest, and it
  refutes a 2020 preprint.
  - First send the counterexample to the author, under the memory rule "report corrections".
  - **Not a post.**
