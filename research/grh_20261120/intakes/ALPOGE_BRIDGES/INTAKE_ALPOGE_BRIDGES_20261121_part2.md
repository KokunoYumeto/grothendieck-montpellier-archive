# Intake of ALPOGE_BRIDGES (prompt 22), part 2: checkpoint 05, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it writes "effort not exposed". It is still going.

Part 1 is in two files: `INTAKE_ALPOGE_BRIDGES_20261121.md` (checkpoint 01) and `INTAKE_ALPOGE_BRIDGES_cp03_20261121.md`
(checkpoint 03, written in round 2). This part covers what is new from checkpoint 03 to checkpoint 05.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ALPOGE_BRIDGES_checkpoint_05_20261121T0246Z_unzipped`. It was made 02:46:53 UTC,
  after 225 min of work, and was the newest present when I started. QUESTIONS.tsv has 100 rows.
- **The run's own movement review 01 (02:02 UTC): movement yes.** Review 02 was due at 03:01 UTC and is not in this
  checkpoint.
- **Read:**
  - LEDGER.md, lines 374-600: checkpoint 03 saved, the movement at 01:37, formal review 01, checkpoint 04, and the
    checked advances at 02:36 and 02:45;
  - the changed QUESTIONS.tsv rows G-123-*, AQ-Q-14-F, AQ-Q-15-GROUP, AQ-Q-SA08-CS, AQ-Q-SA08-TL, AQ-Q-134-SCOPE and
    AQ-Q-136-*;
  - in ALPOGE_BRIDGES.tex, lines 2780-3153: the cote 136 conventions, AQ-136-DP-MODEL and **AQ-136-STRICT, in full**;
  - `research/consequences_criteria_apposition_general.md`, lines 1-110 and 239-305: the setup, **CC-APG01 in full**,
    the statement of CC-APG02, and **CC-APG04 in full**.
- **Statement level:**
  - the rest of cote 136 (AQ-136-COMPARISON, RATIONAL, PLOCAL, PLOCAL-LOCALIZATION, COTENSOR, INTEGRAL-TAIL,
    WEIGHT-ONE, MULTIWEIGHT, DERHAM-CELLS, TENSOR);
  - cote 134-8 (F-SM-29, 30, 32, 33, 35);
  - cote 123 (CC-APG02, 03, 05 to 11, CC-RK01-05, the opposition counterexamples in F₄, E₈ and G₂);
  - cote 14 (CC-ALB01-02) and cote 15 (CC-AG04-08).
- **Changes to findings I checked in part 1:** none withdrawn or corrected.
  - BR-12302 stands, and is now extended. Row G-123-RANK-STRICT reads: "unique subregular nilpotent and unipotent classes
    in every simple complex type, differential rank always r − 1, including all nonsimply-laced types" (CC-RK04/05). So
    Grothendieck's strict rank prediction fails in every non-simply-laced type.
  - F-SM-19, BR-66-01/02/03 and BR-12301/03/04 are unchanged.
  - CC-F01b keeps the correction of the cp03 intake.

## 1. Verdicts on the new and changed findings

| id (run's form) | statement (short) | uses | verdict |
|---|---|---|---|
| AQ-136-DP-MODEL | for every ring k, B_n = Γ_k(x₀..x_n) ⊗ Λ_k(e₀..e_n)/(Σe_j), dx_j = e_j, T ↦ Σx_j, is an admissible theory in the explicit category 𝒜_k: S → B_n is a homotopy equivalence in every weight, and row B^{w,p}_* is contractible for w > p | none | **confirmed** (the change of variables to (T, x₁..x_n) by functoriality of Γ, the one-variable contraction h(x^{[a]}e) = x^{[a+1]}, and the integral PD lattice argument). |
| **AQ-136-STRICT** | **Grothendieck's conjecture (b) on cote 136 (physical p. 121, footer 120), that two homomorphisms C ⇉ C′ are equalized by some admissible C″ → C, is false over every nonzero ring k, Z included.** Counterexample: j₀, j₁: B ⇉ D = B ⋉ M with j₁ = (id, δ), δ the universal relative PD derivation | none | **confirmed for the strict reading.** I checked every step: δ(T) = 0, ker δ = S at each simplex over any k (the β_j coefficient is the exterior partial; the α_j coefficient is the divided-power partial, with no division); D admissible (M vertically contractible, rows of M contractible for w > p + 1); then any equalizing u: E → B factors through the constant S and splits S → E, so k·T^{[w]} is a constant summand of E^{w,0}_* for every w, contradicting the eventual acyclicity (136.4) of the zero-form rows. **Reading caveat:** the sheet writes « qui 'égalise' », in quotation marks. Grothendieck may have meant equalizing up to homotopy, as in the groupoid question on the same sheet. The run proves exactly the strict form false and keeps the groupoid and terminality questions separate (AQ-136-RATIONAL, PLOCAL-LOCALIZATION). Say it so wherever it is cited: "the strict form of (b) is false". |
| AQ-136-RATIONAL, PLOCAL, PLOCAL-LOCALIZATION, COTENSOR | conjecture (a), a common admissible source for any finite family, and terminality of the localized groupoid, proved over Q-algebras, Z_(p)-algebras, finite products of these, and rings of positive characteristic; open over Z | none | statement level. |
| AQ-136-INTEGRAL-TAIL, WEIGHT-ONE, MULTIWEIGHT, DERHAM-CELLS, TENSOR, PATH-OBSTRUCTION | five natural integral constructions of a common source fail (the one-generator tail, independent disks in every weight, high-weight cells, the flat tensor square through prime-power Tor₁); admissibility does not force an acyclic weight-one row | none | statement level. These are failed routes to (a) over Z, each with its obstruction, not refutations of (a). |
| CC-APG01 | all ordered apposition pairs (T, T′) form one G-orbit (Kostant); T ∩ N_G(T′) = ⟨c⟩ and T ∩ T′ = 1; every quadruple (T, B, T′, B′) has trivial inner stabilizer and automorphism group = its Out(G)-stabilizer | none (Kostant 2010 Prop 1.1, Thms 1.2, 1.3, 1.9) | **confirmed** (α_i(t) = λ = (−θ)(t), so λ^h = 1 and t = c^j; N_G(T) ∩ B = T). |
| CC-APG02 | the quadruples are classified by a free action of an explicit finite group K of order hzφ(h) on W × W; the letter's two counts are \|W\|²/(hzφ(h)) and \|W\|²/(hz) | none | statement level. |
| **CC-APG04** | **an outer-automorphism-invariant class of apposition quadruples, which the letter (cote 123, physical p. 22, footer 21) asks for as a "distinguished" class, exists iff the type is not A_{2m}**; outside A_{2m} there is a quadruple with full automorphism group Out(G) | none | **existence direction confirmed.** Γ-orbits of simple roots are pairwise orthogonal outside A_{2m}; n = ∏_O φ_O(s) lifts a Coxeter element and is Γ-fixed; T₀ = Z_G(n)°; a Γ-stable Borel comes from a Γ-fixed generic cocharacter of a torus S ∋ n in (G^Γ)°. **Converse (A_{2m}): read in full**, but it rests on the diagonal/Fourier normal form of CC-AP04-05, which I did not open. Given it, the argument (an affine map j ↦ aj + b reversing an ordering forces a = −1, then the translation c ↦ c − d must reverse an ordering, impossible for odd n) is right. |
| CC-APG03, CC-APG05-11, BR-123-OPPF4/OPPE8/OPPG2, CC-RK01-05 | some opposite choice always exists; all choices are opposite exactly in A_r with r + 1 prime, B₂ = C₂ and G₂; D_r (r ≥ 4), F₄, E₆, E₇ and E₈ admit nonopposite choices; differential rank r − 1 at the subregular class in every type | none | statement level. |
| F-SM-29, 30, 32, 33, 35 (cote 134-8) | the linear "Thm(?)" (connective localization by the maps inverted by Lφ): proved over every scalar ring in the projective-generator setting; then for every Grothendieck abelian category with enough projectives; then whenever ⊕F(X_i) → F(⊕X_i) is an equivalence (AB4 suffices); countable compatibility suffices; exact copowers and products imply AB4 | none | statement level. The remaining gate for the bare abstract (a)-(d) is exactly the coproduct compatibility SM32.1. |
| CC-ALB01-02 (cote 14) | the integral characteristic-p parameter-relation gate is closed: projective versus smooth quasiprojective parameters give the same Albanese relation over algebraically closed fields in every characteristic | none | statement level. |
| CC-AG04-08 (cote 15) | the abelian sector: the base-field/germ passage; exact finite transitions; rational object descent is characterized by Galois orbits and Schur-index divisibility; a quaternion example rules out a Q-neutral fibre replacement | none, plus the cited 2026 Tate/standard-conjecture source for abelian varieties | statement level. The 2026 source is still unidentified by me (the cp03 intake asked for it). |

**Counts for part 2.**
- Confirmed with every step checked: 3 (AQ-136-DP-MODEL, AQ-136-STRICT, CC-APG01).
- Partly confirmed: 1 (CC-APG04; existence direction in full, converse modulo CC-AP04-05).
- Statement level, no fault found: about 25 ids.
- Gaps: 0. Refuted: 0. Changes to part 1: none.

## 2. What is new

- **Cote 136 (SA08 C.3, Grothendieck's uniqueness conjecture for admissible generalized de Rham theories).**
  - The strict form of (b) is false over every ring, by an explicit square-zero extension. That is new as a proof from the
    recovered original conditions. Our SA08 intake had carried an earlier refutation, "C07", whose proof was never
    supplied.
  - (a) and terminality hold away from Z: over Q-algebras, Z_(p)-algebras, and in characteristic p. The integral case is
    now the single gate, with five failed constructions recorded.
  - This is the deepest movement on an original archive question in this run.
- **Cote 123.** The letter to Kostant is now answered question by question in every simple type: counts, opposition,
  the distinguished class (A_{2m} excluded), automorphism groups, and rank r − 1 everywhere.
  - Literature: Kostant's own later work (Kostant 2010, arXiv:1003.0046) is the input. Whether the A_{2m} exclusion and
    the opposition table are in the literature has not been searched by me.
- **Cote 134-8.** The Dérivateurs' linear Thm(?) is proved far beyond fields and Z. The remaining gate is a precise
  coproduct condition.
- **Against tonight's other runs.** No other run touches cotes 123, 134-8 or 136. GRH_NIGHT and AN_GRH do not overlap.

## 3. The scope of the two proofs

Nothing in part 2 uses A_D or M. All of it is unconditional algebra and geometry. No statement claims more than its
input gives.

## 4. Integration, with the attack each opens

1. **SA08 intake (`INTAKE_RESEARCH_SA08_C3_D031_20261120.md`, rows A-CS, A-TL).**
   - Row A-CS: "(a) proved over Q-algebras, Z_(p)-algebras, finite products, and characteristic p (AQ-136-RATIONAL,
     PLOCAL); open over Z".
   - Row A-TL: "terminality proved in the same scope; strict (b) false over every ring (AQ-136-STRICT, explicit
     square-zero extension)".
   - Replace the C07 citation by AQ-136-STRICT, which has a complete proof.
   - **Attack on (a) over Z:** the obstruction in every failed integral construction is the zero-form row in high weight,
     which must be acyclic integrally. The p-local proofs exist for every p. The natural next step is to glue the
     p-local sources and the rational source by an arithmetic fracture square, Z = Q ×_{A_f,Q} ∏ Z_p, inside 𝒜_Z, and to
     test whether the admissibility conditions (136.3)-(136.4) survive the homotopy pullback. If they fail, the failure
     is a lim¹ or Tor term that names the integral obstruction exactly.
2. **Cote 123** (letter to Kostant, physical pp. 22-23, footers 21-22):
   - in the archive notes, every question of the letter now has an answer with an id (G-123-* rows);
   - the "distinguished class" question has a negative answer in type A_{2m} and an affirmative existence answer
     otherwise (CC-APG04);
   - the strict rank prediction fails in all non-simply-laced types (BR-12302, CC-RK04/05).
3. **Cote 134-8 and the Dérivateurs:** the DER_LOCALIZERS intake row on the linear Thm(?) should read "proved for AB4
   categories with enough projectives (F-SM-32); general gate SM32.1".
4. **Cotes 14 and 15:** AQ-Q-14-F is closed in its stated scope. The cote 15 abelian sector is closed after coefficient
   extension. The remaining gate is full Tate for arbitrary numerical motives.
5. **Prompts:** none of prompts 30-35 or 42 asks about cotes 123, 134-8 or 136. Their natural home is the archive
   research prompts. The SA08 C.3 line (prompt 14's successor) should receive AQ-136-* as its starting point.

## 5. Prompt updates for the successor

- Main question for cote 136: (a) and terminality over Z, with the fracture-square attack above and the five failed
  constructions as known data.
- Ask the run to state, in its paper, the strict-versus-homotopy reading of « 'égalise' », and to prove or refute the
  homotopy-equalizer form over Q, where it appears to follow from terminality.
- Cote 123: a literature search for the A_{2m} exclusion and the opposition table (Kostant 1959, 2010; Steinberg 1965
  §9).
- Name the 2026 Tate source behind CC-AG*.

## 6. Hexagon readiness

- **AQ-136-STRICT (strict form of Grothendieck's conjecture (b), cote 136).**
  - 1, complete: yes.
  - 2, self-contained: yes; it uses only the explicit category, from the recovered original conditions.
  - 3, stable: the counterexample is stable, but the reading caveat on 'égalise' must be in the post.
  - 4, checked: an intake targeted check (mine). It still needs an independent re-proof or a computation.
  - 5, interest now: low to moderate (the archive; p-adic de Rham specialists).
  - **Candidate later.** It is best posted together with (a) over Z when that is settled, as a note on Grothendieck's
    divided-power de Rham conjectures of cote 136.
- **CC-APG04 with the cote 123 answers.**
  - 1, complete: yes, modulo CC-AP04-05.
  - 2, self-contained: yes.
  - 3, stable: no literature search yet.
  - 4, checked: partly.
  - 5, interest now: moderate.
  - Together with BR-12302 and CC-RK04/05, this makes the cote 123 post already listed in part 1 ("Grothendieck's 1969
    letter to Kostant: what holds and what does not"). **Candidate; gates: the literature search and a check of
    CC-AP04-05.**
- **F-SM-32 (cote 134-8).** Not stable: the run is still moving the gate. Wait for the final.
