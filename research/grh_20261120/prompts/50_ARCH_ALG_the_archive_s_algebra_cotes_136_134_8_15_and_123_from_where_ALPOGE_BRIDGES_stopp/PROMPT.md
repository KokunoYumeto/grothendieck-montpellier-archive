**The attached files.** Besides this file there is one ZIP, `ARCH_ALG_the_archive_s_algebra_cotes_136_134_8_15_and_123_fr.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Kostant_cyclic_elements_and_Coxeter_tori.zip` is the folder `LIT_Kostant_cyclic_elements_and_Coxeter_tori/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# ARCH_ALG: the archive's algebra, cotes 136, 134-8, 15 and 123, from where ALPOGE_BRIDGES stopped

This prompt continues ALPOGE_BRIDGES (our prompt 22), GPT-6 Astra (ChatGPT Pro mode), on the original questions of
Grothendieck's archive that it opened and largely settled. Its final return (checkpoint 09) and our intakes of it,
parts 1-4, are attached. So are our transcriptions of the pages concerned, as one file per scan, named by cote and scan.
Build on the return and cite it by statement id. Do not redo what it settled: its findings below are inputs.

**Where it stands.** "Confirmed" means that our intake (Claude Opus 5.5 at effort high) checked the proof in full;
"statement level" means that the run's three-reader record stands and our intake read the statement only.

- **Cote 136: the divided-power de Rham conjectures**
  - **Where they are.** Physical PDF pp. 111, 113, 115, 117, 119 and 121, archive footers 110-120; our scans 111-121.
  - **The setting.** The run made Grothendieck's conditions precise as a category 𝒜_k. Its objects are simplicial,
    nonnegatively bigraded, strictly commutative differential divided-power algebras over S = Γ_k(T), satisfying:
    - (136.3), uniform in the simplex: S^i → H^{i,0} is an isomorphism for large i, and H^{i,p} = 0 for i ≥ λ(p);
    - (136.4): π(i) → ∞, where π(i) is the least p for which the row C^{i,p}_* is not flasque (normalized chain complex
      acyclic, including degree 0).
  - **Conjecture (b), strict form.** AQ-136-STRICT (confirmed): Grothendieck's « il existe un homomorphisme C″ → C qui
    'égalise' » is false over every nonzero ring k, Z included, in its strict reading. The counterexample is j₀, j₁ :
    B ⇉ B ⋉ M, with j₁ given by the universal relative PD derivation. The sheet puts 'égalise' in quotation marks; the
    homotopy reading is open.
  - **The admissible model.** AQ-136-DP-MODEL (confirmed): B_n = Γ_k(x₀..x_n) ⊗ Λ_k(e₀..e_n)/(Σe_j), with dx_j = e_j, is
    admissible over every ring.
  - **Terminality.** AQ-136-SEMILOCAL: the localized groupoid is terminal over every ring in which all but finitely many
    rational primes are units. Its step 1, the arithmetic fracture sequence 0 → M → (⊕M_i) ⊕ M₀ → M₀^{⊕s} → 0, is
    confirmed; the rest is at statement level. AQ-136-RATIONAL and PLOCAL are the earlier cases.
  - **Conjecture (a), common sources.** AQ-136-COSPAN and SEMILOCAL-SOURCES (statement level) give strict common
    admissible sources for any finite family over the same rings. AQ-136-CONNECTED-SOURCES (statement level): over any
    ring, (a) is equivalent to connectedness of the category.
  - **Toward Z.** AQ-136-FIRST-SKELETON (statement level) gives a shared free integral first skeleton for any finite
    family. Eight failed routes to (a) over Z are on record, each with its obstruction: INTEGRAL-TAIL, WEIGHT-ONE,
    MULTIWEIGHT, DERHAM-CELLS, TENSOR (prime-power Tor₁), PATH-OBSTRUCTION, FREE-ZERO-FORMS, and HIGHER-COMPLETION (the
    equation p·a = w·T^{[w]}).
  - **The obstruction we isolated.** The weight cutoff of SEMILOCAL's tensor lemma (136.S2), w ≥ q·max N_i + Σ N_i,
    grows with the prime set P.
- **Cote 134-8: the linear "Thm(?)" of the Dérivateurs**
  - **Where it is.** Manuscript footers 47-54 = physical pp. 48-55; the Thm(?) is at footer 48 = physical p. 49; our
    scans 046-056.
  - **The statement.** Localizing by the maps that Lφ inverts gives the connective derived category.
  - **Proved (all statement level).**
    - BR-13401-06: the linear lemmas and the field and Z cases.
    - F-SM-29: every scalar ring in the projective-generator realization.
    - F-SM-30: every k-linear Grothendieck abelian category with enough projectives.
    - F-SM-32: whenever ⊕F(X_i) → F(⊕X_i) is an equivalence; AB4 suffices.
    - F-SM-33: countable compatibility plus the all-free counit.
    - F-SM-39: the raw counit for locally scalar-projective categories.
    - F-SM-42: the split-interval criterion.
  - **Limits.** F-SM-31 and F-SM-43 show that AB5 and AB4 do not follow automatically. In both the conclusion still
    holds.
  - **The gate.** F-SM44 proves injectivity in all degrees and reduces the compatibility gate to surjectivity in
    degrees ≥ 2. The raw ordinary-G counit keeps the Tor/coinduced-product acyclicity test SM25.2.
- **Cote 15: motives over F_p and the "conjecture forte"**
  - **Where it is.** Physical pp. 94-106: Q′ on p. 94 (footer 93), the norm on p. 98 (footer 97), the boxed purity on
    p. 100 (footer 99); our scans 092-107.
  - **The abelian sector** (statement level), classified after coefficient extension: CC-AG01-17, with the finite descent
    procedures and source-field profiles; BR-EFF01-03 (spectral integrality ⇔ full Tate); CC-XC01-15 (a terminating
    rational certificate verifier).
  - **Forward cross-cycles** by actual Chow correspondences (statement level), CC-XC16-23:
    - low-degree Chow-generation classes, in particular rationally chain connected surfaces and threefolds;
    - quadric fibrations over curves;
    - supersingular K3 classes;
    - supersingular abelian classes.

    They use Vial 2013 (Thm 4.2, Cor 4.4, Cor 4.8, Prop 3.11) and Kahn-Sujatha (3.1.4(2)).
  - **Conditional on outside preprints**, all unrefereed:
    - van Hoften-Sempliner, *The Hodge Conjecture for CM abelian varieties*, Hexagon 2610.00259v2;
    - *Milne's rationality conjecture*, Hexagon 2610.00226v1 (contributor K. Madapusi);
    - Milne's note, Hexagon 2611.00244v1.

    The rows that depend on them are CC-TATE01-04, the abelian CC-AG rows, and BR-EFF's abelian cone.
  - **A correction.** BR-15-CLASSBOUND refutes Thakur 2020 (arXiv:2001.00210v1), Prop 2.9: a threefold over F_{2^9}
    with Frobenius polynomial (T² − 24T + 512)³ over Q(√−23), h = 3. Its class-number half is confirmed; the
    Honda-Tate index computation CC-AG14 is at statement level.
  - **The gate.** The forward cross-cycle gate for an arbitrary smooth projective X, which is full Tate.
- **Cote 123: Grothendieck's letter to Kostant of 22 Oct 1969**
  - **Where it is.** Physical pp. 22-23, footers 21-22; our scans 022-024.
  - **Answered in every simple complex type.**
    - Dimension of the variety of Borel subgroups: Steinberg 1976, Thm 4.6 and Thm 6.5.
    - Rational singularities: F-SM-23.
    - Tangent rank: BR-12301 (type A, confirmed); BR-12302 (the sp₄ counterexample to the predicted strict drop,
      confirmed by hand and by computation); CC-RK01-05.
    - Subregular uniqueness, and rank r − 1 in every type: this is Richardson 1987, §5 and Lemma 5.1, p. 234,
      attributed there to Slodowy (CC-RK04, confirmed). So the rank answer is a known theorem.
    - Apposition quadruples: classified by an explicit finite group of order hzφ(h) (CC-APG01 confirmed; APG02
      statement level).
    - Opposite Borels: some choice is always opposite; all choices are opposite exactly in A_r with r + 1 prime,
      B₂ = C₂ and G₂ (CC-APG03, CC-APG06-11, statement level).
    - Outer-invariant ("distinguished") classes: they exist iff the type is not A_{2m} (CC-APG04; existence confirmed,
      the converse modulo the normal form of CC-AP04-05).
    - Automorphism groups: CC-APG05.
  - **Not searched in the literature:** the A_{2m} exclusion and the opposition table.

## The task

1. **Main question: cote 136 over Z.** Decide connectedness of the category 𝒜_Z.
   - By AQ-136-CONNECTED-SOURCES this decides Grothendieck's conjecture (a), a common admissible source C″ → C, C″ → C′
     for any two admissible theories over Z. Then decide terminality of the groupoid obtained by inverting all
     morphisms, which is the connected and simply connected groupoid of physical p. 121.
   - **The obstruction to locate.** It is uniformity in the prime set. The SEMILOCAL gluing works for each finite P, but
     its weight cutoff grows with max N_i and Σ N_i. Either construct sources whose cutoffs (136.3)-(136.4) are bounded
     for all primes at once, or prove that no admissible theory over Z can serve, refuting (a) over Z.
   - **Data to start from.** The eight failed routes say where any construction must differ. FIRST-SKELETON gives the
     first skeleton for free, so the question is about the higher simplices.
   - **The homotopy reading.** State and decide the homotopy reading of « 'égalise' »: for two parallel morphisms
     f, g : C ⇉ C′, an admissible h : C″ → C with fh and gh homotopic, in a homotopy notion on 𝒜_k that you specify and
     justify from the sheet. Over Q, and over the semilocal rings, decide whether it follows from terminality. Then
     decide it over Z.
   - Give every result as a statement about the sheets: physical page, footer, and our scan file. Give it also in
     Grothendieck's language: admissible generalized de Rham theories, divided-power envelopes, and crystalline
     cohomology as in SGA 4 and Berthelot.
2. **Cote 134-8: the higher-surjectivity gate.**
   - Prove surjectivity in degrees ≥ 2 of F-SM44's comparison map under Grothendieck's own hypotheses at footer 48 /
     physical p. 49: scalars, tensor and interval. That gives the Thm(?) in full.
   - Or construct a category satisfying those hypotheses in which it fails, and check whether the localization
     conclusion fails there too (F-SM-31 and F-SM-43 are examples where only the auxiliary property failed).
   - Treat the raw ordinary-G counit test SM25.2 in the same way.
3. **Cote 15: the first forward cross-cycle beyond CC-XC16-23.**
   - Construct the forward cross-cycles by actual Chow correspondences for classes of smooth projective varieties not
     covered by CC-XC16-23. Take, in this order: cubic fourfolds; K3 surfaces of finite height; products of a curve of
     genus ≥ 2 with itself. For each class, prove the construction, or prove that it is equivalent to a stated case of
     the Tate conjecture for that class.
   - **Tag every input:**
     - A (Alpöge's GRH for Dirichlet L-functions, a theorem);
     - M (Masullo's GRH for Hecke L-functions, conditional);
     - an outside preprint, named (the three Hexagon preprints above);
     - a published theorem;
     - none.

     Wherever an abelian-sector step rests on an outside preprint, replace that input by a published theorem if one
     suffices: Deligne's absolute Hodge cycles for CM abelian varieties; Milne's published results on the Tate and
     Hodge conjectures for abelian varieties. Where none suffices, say so.
   - Check BR-15-CLASSBOUND's Honda-Tate index computation (CC-AG14) in full, and record the check.
4. **Cote 123: the companion section.**
   - Write one self-contained section answering every question of the letter to Kostant (physical pp. 22-23), each
     with its proof or exact citation:
     - credit Richardson (1987, Lemma 5.1) and Slodowy for the rank;
     - give BR-12302 as the explicit sp₄ instance;
     - include the apposition classification, the opposition table, the outer-invariant criterion and the automorphism
       groups.
   - Before calling CC-APG04 or the opposition table new, search the literature: Kostant 1959 and 2010
     (arXiv:1003.0046); Steinberg 1965, §9; Richardson 1987; Slodowy 1980 (LNM 815); the work on cyclic elements and
     Coxeter tori. Name the result if it is known.
   - Check the normal form CC-AP04-05 on which CC-APG04's converse rests.

The links between these questions and Grothendieck's texts are real. Where a route meets an obstacle, locate it exactly
and take the next route; an obstacle is never an end point.

## The attached files

- `RETURN_ALPOGE_BRIDGES_checkpoint_09_*/`: the run's paper (ALPOGE_BRIDGES.tex), QUESTIONS.tsv, LEDGER.md and its
  modules, including `research/aq136_*`, `research/source_cote1348_*`, `research/consequences_criteria_*`,
  `research/root_springer_archive.tex` and `research/cc_sources/` (Richardson 1987 and other primary snapshots).
- Our intakes of ALPOGE_BRIDGES (checkpoints 01, 03, 05, 06 and 09), with their check events.
- Our transcriptions:
  - cote 136, scans 108-123;
  - cote 134-8, scans 046-056;
  - cote 15, scans 092-107;
  - cote 123, scans 022-024.
- `LIT_Kostant_cyclic_elements_and_Coxeter_tori/` (arXiv:1003.0046), as LaTeX.

## The attached files

- `RETURN_ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z/`: Final return (cp09): AQ-136-*, F-SM-24-44, CC-AG01-17, CC-XC01-23, CC-TATE01-04, BR-15-*, G-123/CC-APG/CC-RK rows, research/cc_sources (Richardson 1987). EXCLUDE any Masullo page images or text copies if present (not needed here) (302 files: the run's paper, registers, scripts and certificates)
- `INTAKE_ALPOGE_BRIDGES_20261121.md`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_cp03_20261121.md`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_20261121_part2.md`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_20261121_part3.md`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_20261121_part4.md`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_cp03_20261121_CHECK_EVENTS.tsv`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_20261121_part2_CHECK_EVENTS.tsv`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_20261121_part3_CHECK_EVENTS.tsv`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `INTAKE_ALPOGE_BRIDGES_20261121_part4_CHECK_EVENTS.tsv`: Our intake of ALPOGE_BRIDGES: verdicts, scope, integration and successor needs for cotes 136, 134-8, 15, 123
- `ARCHIVE_136_scan108.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan109.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan110.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan111.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan112.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan113.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan114.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan115.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan116.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan117.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan118.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan119.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan120.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan121.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_136_scan123.tex`: Cote 136, divided-power de Rham theories: conditions (3a,b),(4) and conjectures a), b) (physical 111-121)
- `ARCHIVE_134-8_scan046.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan047.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan048.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan049.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan050.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan051.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan052.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan053.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan054.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan055.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_134-8_scan056.tex`: Cote 134-8, the linear Thm(?) and its lemmas (footers 47-54 = physical 48-55)
- `ARCHIVE_15_scan092.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan093.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan094.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan095.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan096.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan097.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan098.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan099.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan100.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan101.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan102.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan103.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan104.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan105.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan106.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_15_scan107.tex`: Cote 15, Q-prime, norm, boxed purity and the conjecture forte (physical 94-106)
- `ARCHIVE_123_scan022.tex`: Cote 123, letter to Kostant of 22 Oct 1969 (physical 22-23, footers 21-22)
- `ARCHIVE_123_scan023.tex`: Cote 123, letter to Kostant of 22 Oct 1969 (physical 22-23, footers 21-22)
- `ARCHIVE_123_scan024.tex`: Cote 123, letter to Kostant of 22 Oct 1969 (physical 22-23, footers 21-22)
- `LIT_Kostant_cyclic_elements_and_Coxeter_tori//` (arXiv:1003.0046, LaTeX source): Kostant 2010: apposition, principal elements (CC-APG inputs) and literature check for task 4

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: Decide whether the category of admissible divided-power de Rham theories of cote 136 is connected over Z, that is, whether Grothendieck's conjecture (a) of physical p. 121 holds over Z, by constructing sources with prime-uniform weight cutoffs or proving that none exist. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `ARCH_ALG_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `ARCH_ALG_final.zip`, holding:
1. **The paper**, `ARCH_ALG.tex`, in LaTeX:
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
