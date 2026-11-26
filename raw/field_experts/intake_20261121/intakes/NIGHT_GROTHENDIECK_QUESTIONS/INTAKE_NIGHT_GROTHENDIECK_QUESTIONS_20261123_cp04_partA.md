# Intake of NIGHT_GROTHENDIECK_QUESTIONS (prompt 76), checkpoint 04, Part A: cotes 15, 123, 133

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), 23 Nov 2026, for the main session 329fb1e6 (Claude
Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode), effort not exposed. Its checks are by separate
instances of the same model. This is a first return, so all of Part A is new. Parts B and C are not active in this
checkpoint (README; QUESTIONS rows "NOT YET ACTIVE"), so the other two intakes have nothing to take in yet.

## 0. Return and scope

- **Return:** `research_returns\NIGHT_GROTHENDIECK_QUESTIONS_checkpoint_04_20261123T1648Z_unzipped`, frozen 16:48 UTC.
  It was the only checkpoint on disk when I started and still was when I finished (23:xx UTC).
- **Three paper projects:**
  - `papers\A133_lattices` (37 pp.);
  - `papers\A123_tori` (17 pp.);
  - `papers\A15_finite_fields` (19 pp.).
- **Read in full, with proofs:**
  - `A133_lattices\main.tex` lines 1-200 (the statement and overview);
  - `dual_numbers.tex`, `positive_characteristic.tex`;
  - `dual_numbers_all_primes.tex` (the theorem, the invariant, the lattice, the induction);
  - `A15_finite_fields\central_cm.tex`.
- **Read in part:** `arbitrary_idealizations.tex` (the detector and the torsion direction, about 140 of 315 lines);
  `A123_tori\main.tex` at the statements of Theorems 1.1, 1.2, 8.1 and Propositions 6.1, 7.1, 7.2, 9.1, with the
  proofs of 7.2 and the opening of 9.1.
- **Statement level only:**
  - A133: `regular_local`, `coherent_colimit`, `rational_nilpotents`, `reduced_counterexamples`, `singular_orders`,
    `normal_domain`, `ramified_dual_numbers`, `odd_ramification`, `even_truncations`, `uniform_torsion`,
    `tensor_formula`;
  - A15: `main.tex` beyond the statement list.
- **No code of the return was run.** My program is `dual.py`, in
  `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\ngq`
  (a temporary folder).
- **Pages read against the run's readings:** cote 133 scan 29 and scan 6, cote 123 scans 22-23, in the text of
  record (`grothendieck_archive_transcription_20261110\text_of_record\pages\`). For cote 15, only the run's locators
  (scan 100, footer 99; scan 106, footer 105); I did not open those pages.

## 1. Verdicts

### Cote 133 (paper "Grothendieck's question on symmetric-group lattices over local rings")

Notation: R(A) = ⊕ K_0(Lat_A(S_n)) with induction product, and Φ_A : ℤ[h_1, h_2, …] → R(A), h_n ↦ ρ_n.

| Statement | Read | Check | Verdict |
|---|---|---|---|
| Thm 1.1(ii): if m·1_A = 0 then P_m(ρ_1..ρ_m) = 0 | whole proof | targeted proof check: exterior Koszul complex of A^m (H(t)E(−t) = 1); V = ker(sum) ∋ v = Σe_i primitive since m = 0; alternating sum gives Σ(m−j)(−1)^j ρ_{m−j}ε_j = [t^m] tH′/H = p_m | **confirmed** |
| Thm 1.1(v), p = 2: L = A², T = [[1, ε], [ε, −1]] over ℤ_(2)[ε]/ε² | whole section | targeted proof check, with the invariant below | **confirmed** |
| Thm `dual-numbers-all-primes`: over ℤ_(p)[ε]/ε² and ℤ_p[ε]/ε², [M_p] − [A[S_p]] is nonzero, in the reduction kernel, detected mod 2 | whole proof | targeted proof check: additivity of ν_f (boundaries anticommute; δ identifies parities, so a−b+c = 2r₀); the lattice L_p; generator change u_{L^{(q)}} = q·u_L; Mackey over N(C_p)/C_p ≅ F_p^×, so only q = 1 contributes | **confirmed** |
| The identities used there | | computation (`dual.py`): T_p^p = I, the ε-part of N(T_p) upper right equals a·D_p(C), and a·D_p(C)·b = 1, for p = 2, 3, 5, 7, 11 | **confirmed** |
| Exact order two and ⊕_ℕ ℤ/2 summands (Prop. `truncation-torsion`, Cor. `all-prime-two-torsion`) | statements | none | carried |
| Thm `arbitrary-idealizations`: ℤ_(p) ⋉ M polynomial iff M is a ℚ-vector space; torsion gives ⊕_ℕ ℤ in degree p | detector χ_f, its additivity, the separating functional λ : M → ℚ/ℤ_(p) (Zorn), the rank-one modules s = 1 + aη with u = a | targeted proof check of those parts | **torsion direction confirmed as far as read**; the "if" direction (`rational_nilpotents`) carried |
| Thm 1.1(i): coherent regular local rings of characteristic 0, local ℚ-algebras | statement | none | carried |
| Thm 1.1(iii): Φ split injective in characteristic 0 | statement | none | carried |
| Thm 1.1(iv), (vii), (viii); normal two-dimensional counterexamples; ramified and truncated cases | statements | none | carried |
| Scan 6: the split Witt-Green ring is not special | statement | none (same answer as GCT_PLETH A-003, re-proved 21 Nov) | carried, consistent |

### Cote 15 (paper on finite-field isogeny descent)

| Statement | Read | Check | Verdict |
|---|---|---|---|
| Prop. 5.2 (`central-cm`): for D over a CM field K, the central-Frobenius model exponents are exactly the multiples of n = a·t·s, s ∈ {1, 2}; the minimum when D = K | whole proof | targeted proof check: I·Ī = (p)^a; u = ηη̄/p^{at} a totally positive unit, z² = N(z); necessity from slopes, ideal class and unit norm; existence by Honda-Tate and equal powers | **confirmed** |
| Recomputed on the threefold of ARCH_ALG (K = ℚ(√−23), p = 2, d = 3) | | by hand: a = 3, I = 𝔭𝔭̄², [I] = [𝔭]^{−1} of order 3, K⁺ = ℚ so s = 1; n = 9 | **consistent** with A15-PENDING-003 ("iff 9 divides") |
| Thm 1.1 (the threefold, no model over F₈) | statements | ARCH_ALG intake of 22 Nov (lines read and arithmetic recomputed) | as there |
| The Chow constructions (Thm 1.2, Props 7.3-7.7) | statements | none | carried |

### Cote 123 (paper on tori in apposition)

| Statement | Read | Check | Verdict |
|---|---|---|---|
| Thm 1.1(i)-(iii): count, opposition table, outer-fixed classes exist exactly outside A_{2m} | statement | inherited ALPOGE_BRIDGES, checked in part 21 Nov | as there |
| Prop. 6.1: type-A fixed-class formula | statement | my count of 22 Nov, n = 3..9 | consistent |
| Thm 1.2: natural rules under isomorphisms = Out-fixed classes; central isogenies add no selection | statement | none | carried |
| Prop. 7.1: in A₃, 16 of 18 classes opposite, all 8 fixed classes among them | statement | none | carried |
| Prop. 7.2: a split PGL_n quadruple over k ⊂ ℂ exists iff ζ_n ∈ k | whole proof | targeted proof check: Borels over k split the tori; the Fourier cross-ratio A₀₀A₁₁/(A₀₁A₁₀) = ζ_n is invariant under scalings and permutations | **confirmed** |
| Prop. 9.1: symplectic folding; \|𝒴\| = (2^m m!)²/(2nφ(n)) | statement and opening | arithmetic at n = 4 gives 4 | carried; the number is consistent |
| Thm 8.1: subregular rank r−1 (Slodowy; Richardson 1987, Lemma 5.1) | statement | known theorem, credited | background |

**Counts:**
- 6 confirmed by proof check: P_m relation, flat dual numbers at p = 2, all primes, idealization detector, central CM,
  Prop. 7.2;
- 1 computation;
- about 20 carried at statement level;
- 0 refuted.

## 2. What the return decides against the pages, and whether our reading stands

- **Cote 133, scan 29 (manuscript p. 28), `text_of_record/pages/133/133_scan029.tex`.** The page asks: "Pour quels
  anneaux k … l'anneau de polynômes sur ℤ engendré par les ρ_i ? Est-ce vrai si k est un anneau local (plus gén, tel
  que K(k) ← ℤ iso)?"
  - The run decides both clauses negatively. Flat dual numbers are local with K_0 = ℤ, of characteristic 0, with only
    ±1 as square roots of 1, and fail at every prime (checked).
  - Positively, regular local rings of characteristic 0 are a yes (statement level). Characteristic 0 of the ring is
    necessary (checked).
  - **Our reading stands, with two corrections to our study.** It omitted the parenthesis "(plus gén., tel que K(k) ≅
    ℤ)" (now added). And part 1 of my GCT_PLETH intake proposed a determinant-character criterion; it is refuted by the
    flat dual numbers, where all determinants are ±1 and generation still fails. Our earlier Z_(2)[ε]/(2ε, ε²) example
    (A-023) stands and is one instance of the run's Theorem 1.1(vii).
- **Cote 133, scan 6 (manuscript p. 5).** "Même dans ce cas j'ignore si c'est un λ-anneau": the run answers no for the
  split Witt-Green ring, as GCT_PLETH A-003 did. Our reading stands.
- **Cote 133, scan 28.** The tensor-power formula is explained integrally (`tensor_formula.tex`, statement level).
  This is consistent with our study's scan 28 entry.
- **Cote 123, scans 22-23** (the letter to Kostant). The page asks whether B and B′ are opposite and whether there is a
  distinguished class (scan 22), and asks about the rank on the subregular orbit, with the guess of rank r−1 for one
  root length (scan 23). The run's answers are the ones in our ARCH_ALG seed (Paper 4). Our reading of the questions
  stands.
- **Cote 15, scans 100 and 106** (footers 99 and 105): the boxed purity question and the weaker existence conjecture,
  by the run's locators. I did not open the pages. The A15 minimum question is our follow-up to the Thakur
  counterexample, not one of Grothendieck's questions.

## 3. What is new, and what it is good for

1. **Grothendieck's scan-29 question is answered in both directions** (cote 133 companion; a note to readers of
   λ-rings and integral representation theory). The flat-dual-number obstruction is new to us: a Bockstein boundary
   on Tate cohomology of C_p, squared, read mod 2 by primary lengths. It is a clean invariant of K_0 of lattices over a
   nilpotent thickening. It shows that integral K_0 of lattice categories sees nilpotent coefficient data that
   characters cannot.
2. **The square-zero classification over ℤ_(p)** is a complete answer in one natural class, with no finiteness
   hypothesis.
3. **The central CM formula** n = a·t·s generalizes the class-number example. It gives the sharp minimum when the
   endomorphism algebra is commutative, and is the right shape for the successor question on minimal fields of
   definition.
4. **Prop. 7.2** (split apposition needs ζ_n) says that no split-real positivity rule can choose a distinguished class.
   That is useful for the open "natural class" question.

Literature: I made no search. The run's LITERATURE.md cites Burroughs 1974, Swan 1963, Barthel et al. 2025 (Thm A),
Zibrowius 2015, Brooks et al. 2017 and Richardson 1987. I did not open them.

## 4. Scope of the inputs

No statement read uses Alpöge, Masullo or any GRH. A15 uses Honda-Tate, Tate's isogeny theorem and polarized
ideal-class theory (Brooks et al., Lemma 5.5), all published.

## 5. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`; for the main session)

| Title | Statement | What it adds | Gate left |
|---|---|---|---|
| Flat dual numbers do not satisfy Grothendieck's polynomiality for symmetric-group lattices | For every prime p, ⊕K_0(Lat(S_n)) over ℤ_(p)[ε]/ε² is not generated by the trivial classes; already in degree p | answers cote 133 scan 29 negatively for local rings with K_0 = ℤ; a new mod-2 Tate-boundary invariant | literature search (with Hexagon); proofs of the order-two and infinite-summand parts; a self-contained write-up |
| Characteristic zero is necessary | m·1 = 0 implies P_m(ρ) = 0 | an elementary general relation | literature (likely folklore); fold into the cote 133 note |
| Square-zero extensions of ℤ_(p) | polynomial iff the ideal is a ℚ-vector space | complete classification in a natural class | proof of the "if" direction checked; literature |
| Central minimum of isogeny descent over a CM center | central model exponents are the multiples of a·t·s, s ∈ {1, 2} | sharp when D = K; corrects Thakur Prop. 2.9 in general form | literature (Brooks et al.); noncentral case open |

## 6. For the P vs NP fleet (constructed, not graded)

None of Part A bears on complexity directly. The one mappable item:
- **Thm 1.1(ii), P_m(ρ) = 0 in characteristic m.** It is an identity in K_0 of lattice categories, the kind of "integer
  identity holding in every commutative ring of characteristic m" that the gct nodes L-gct-126 and L-gct-154 state
  for cubes (`PROOF_GRAPH.tsv`).
  - Translation: the Newton power sum is a relation among permutation-module classes that holds exactly when m = 0 in
    the coefficients. It is a characteristic-dependent collapse of the Schur-Weyl basis, the same phenomenon that
    makes integer identities like Fischer's fail or hold by characteristic.
  - Bridge work: state the K_0-relation as a proposed node under `maps/algebra_combinatorics.md` §4 (results whose
    only target is a proposed new node). There is no existing node it feeds.

## 7. Integration

- **Applied:** `results_register\horizontal\sweep3\SA17\STUDY.md`, the scan 28-29 entry:
  - the missing parenthesis of the question;
  - a block "Further answers" with the run's results and their check levels.
  - Backup: `field_experts\intake_20261121\integration_backups\20261123\NIGHT_GROTHENDIECK_QUESTIONS\STUDY.md`.
  - Logged in `INTEGRATION_NIGHT_GROTHENDIECK_QUESTIONS_partA_20261123.tsv`.
- **For the main session:**
  - the board rows of §5;
  - the seed `reports_20261122\paper_seeds\SEED_ARCH_ALG.md`, Papers 3, 4 and 5, is now overtaken by this run's three
    projects. Paper 5's research question (the exact class) is the run's open row A133-classification. Point the seed
    to `papers\A133_lattices`;
  - note E6 (Thakur) can cite Prop. 5.2 for the general central formula.

## 8. Prompt updates (for the continuation of prompt 76)

- **Part A open rows:**
  - A133-classification (singular mixed-characteristic rings);
  - A133-odd-truncations (the class killed by n, nonvanishing for odd n);
  - A133-ramified-odd (v₂(e) > v₂(p−1), and infinite residue fields);
  - A133-higher-orders;
  - A133-normal-singular;
  - A15-minimum (noncentral Frobenius);
  - A123-natural (folding constraints).
- Ask that each proof be checked by a reader of another model family, not only the same model. The run's
  "independent" checks are same-model.
- Parts B and C are still to start.

## 9. Hexagon readiness

| Candidate | Complete | Self-contained | Stable | Checked | Interest | Gate |
|---|---|---|---|---|---|---|
| Cote 133 note (dual numbers, characteristic, idealizations) | yes for those statements | yes | the run is active | proofs read here for the main ones | moderate-high | literature; the remaining proofs; run final |
| Central CM descent | yes | yes (published inputs) | yes | read here | moderate | literature (Brooks et al.); with the threefold |
| Apposition (A123) | partial: natural class open | needs ALPOGE_BRIDGES | active | in part | moderate | as in the ARCH_ALG seed |

None passes all five tests now.
