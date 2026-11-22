# Intake of RESEARCH_SA22 (run 1) and RESEARCH_SA22_run2 (run 2), 20 Nov 2026

By Claude Opus 5.5 at effort max (agent af3526fc4890c92f1, the sweep-3 reader of cote 67, scans 003–046 and 084–101),
resumed by the main session (Claude Opus 5.5 at effort max) for this intake. The brief is
`field_experts/intake_20261120/INTAKE_BRIEF.md`. Both runs are GPT-6 Astra (ChatGPT Pro mode), answering the same
prompt, `pro_prompt_builds/RESEARCH_SA22/PROMPT_as_sent_20261119.md` (drafted by ae4ae3dc, Claude Opus 5.5 at effort
max).

## 0. What I read, and my scope

**Return folders (both final, both marked INCOMPLETE by the runs themselves):**
- Run 1: `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA22_final_20261119T1905Z_unzipped`
  (final after checkpoint 09). Register `RESEARCH_SA22_results.csv`, 159 rows.
- Run 2: `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA22_run2_final_20261119T2149Z_unzipped`
  (final after checkpoint 09). Register `RESEARCH_SA22_results.csv`, 202 rows.

**My rows:** every row of both runs, in packets 37–39 (159 + 202 = 361 rows). No earlier intake exists for either run.

**Scope** (filled in as the reading proceeds; section 7 gives the final list):
- read in full (proof read and checked): the main results and the rows the programme rests on, and the rows of
  Part A that bear on the cote-67 readings;
- read at the level of the statement: the remaining rows, with the run's own status and proof locator.

**Final scope.**
- 38 rows have a check from me, either made today or, for rows that state what we proved on 18–19 Nov, made then (§7
  lists them).
- 323 rows were read at the level of the statement, with the run's status and its proof locator. Of these, 17 agree with
  a checked row of the other run or with our earlier check, as the table says.

Each run counts each row's status in its own terms (Proved, Proved under stated hypotheses, Known, Refuted, Open).
"My check" below says only what I did.

**Not read (honest scope, 21 Nov).** These remain at the level of the statement:
- run 1's toric rows: `A1-toric-domain`, `A1-toric-noninjective`, `A1-toric-nondescent`, `A1-pant-third-jet`,
  `A1-four-point-plumbing-jet`, `A1-nontoric-cut`, `A1-cut-not-algebraic`;
- the anabelian rows (A.6) of both runs;
- run 2's subject-21 counterexample (`C:subject21-torsion-counterexample`, `C:Nagata-input`, `C:Goldman-branches`,
  `U:henselian-comparison`);
- the inputs `A2b-energy`, `A2b-recession` and `A2b-image` of the checked reduction `A1-graph-range`;
- most of Part B.3 and Part C.

The intake was done at effort max (my launch setting), not at effort high as planned.

## 1. Verdicts, row by row

**Counts:**

| My check | Rows |
|---|---:|
| targeted proof check, confirmed | 15 |
| refutation by the run, counterexample checked and confirmed | 5 |
| independent re-proof (ours), agrees | 18 |
| statement read; agrees with a checked row or with our earlier check | 17 |
| statement read only (some with a note) | 306 |

No row I checked failed. I found no gap in what I read.

The full table is at the end of this file (§8), 361 rows in register order.

## 2. Where the two runs agree, and where they differ

Both runs are GPT-6 Astra (ChatGPT Pro mode), answering the same prompt on 19 Nov 2026. Both stopped under the
two-reviews rule and mark themselves INCOMPLETE only for original sources not obtained. Neither leaves a mathematical
item of the Parts undecided, except run 2's `U:henselian-comparison`.

### Agreement (the main conclusions are the same)

**A.1, the main question: the section-6 maps (67/074–082) are not isomorphisms onto the stated target.**
- Same certificate in both runs. In the nodal (0,4) curve, a tensor q of norm 17 has no preimage, because each node
  cap has conformal radius < 4 (Koebe) and |q| is the product of the two radii (run 1 `A1-global-refutation`, run 2
  `A:04`).
- The exact image is the open subbundle cut out by the Jenkins–Strebel support inequalities. For nodal (0,4) in the
  normalization 0, 1, ∞ it is 0 < |q| < 16.
- The tangent map is invertible and the inclusion is a π₁-isomorphism (run 1 `A1-graph-range`, run 2
  `A:graph-radius-domain`, `A:graph-pi-one`).
- External-only admissibility fails (run 1 `A1-bordered-landing`, run 2 `A:MDB-forgetting-admissibility`).
- Local plumbing (Kra, Earle–Marden, Wolpert, Hubbard–Koch) gives charts, not a global inverse; Hinich's mechanism is in
  both runs.

**A.2, capping.**
- (a) **"Each cap depends only on its own length" (67/068 "?") is false** (run 1 `A2-independence`, run 2
  `A:pants-cap-dependence`).
- (b) The cap-radius map is injective, with an open convex logarithmic image (run 1 `A2b-energy`, `A2b-image`; run 2
  `C:A2b-energy`, `C:A2b-image`).
- (c) The limits are Jenkins–Strebel cells for the limiting weights; one dominant end gives Koebe's slit and radius 4
  (run 1 `A2-cap-limit`, `A2-explicit-limits`; run 2 `C:A2b-strebel-limit`, `C:A2b-pants-extremes`).
- (d) The cusp norms and the decorated bundle (L3).
- (e) The metric comparison after removing a collar (021) is not monotone in general.

**A.3.** Welding needs quasisymmetric gluing for existence and removable seams for uniqueness. L5 holds: section 6
glues analytically.

**A.4.**
- The orange-slice model is false; the extremal-length argument is Michel Hua's project's, with Pro's constants.
- The enlarged Teichmüller space with cusps and the intrinsic action of [0,∞)^I come from Mondello's grafting theorem.

**A.5.**
- The Theorem of 089 holds in every characteristic ≠ 2.
- The Proposition of 086 fails in characteristic 5 (as our sweep 2).
- Stack and coarse space over ℤ[½, i] are kept distinct.
- In characteristic 3 the exceptional automorphism group of a four-point set is 𝔖₄: the set ℙ¹(F₃).

**A.7.**
- The classification of real elliptic curves: hexagonal ratio 3, j(a) = j(1/a).
- The PID count: ℤ[(1+√−11)/2] has three non-split classes.
- **Both runs refute our correction R5, "the corollary of 091 needs Spec k connected"** (run 1
  `A7-domain-counterexample`, which I checked; run 2 `A:eigenmodule-correction`).

**B.**
- B.1(a), L1: numerical and homological equivalence agree for 2-cycles on fourfolds in characteristic 0. This is
  classical.
- B.1(b), abelian fourfolds in characteristic p: both runs go through Broe's 2026 preprint. Both say Ancona's Hodge
  standard conjecture alone gives positivity only on the numerical quotient (run 1 `prop:B1b-gap`, run 2
  `B:ancona-scope`).
- B.1(c), 1-cycles on threefolds, numerical against τ-equivalence: false, by a quintic threefold with two lines
  (Griffiths, Clemens), as his margin says.
- B.2: both questions false. The square of the algebraically trivial divisor pr₁*(p−q) + pr₂*(p′−q′) on E × E is
  2(p−q)×(p′−q′) ≠ 0 in CH₀; Mumford answers the Albanese question.
- B.3: all 28 subjects and the nine "Pour mémoire" headings, with locators.

**C.**
- The corrected exponential theory: the struck (iii′) repair, the differential automorphisms, the intertwining for
  locally nilpotent maps, the K-functor criteria.
- Condition K is false by a C₄ certificate (L8 refuted).
- The symmetry question (020): run 1 proves "prétassé is symmetric for all functions iff G is abelian"; run 2 refutes it
  on 𝔖₃. These are consistent.

### Differences

1. **A.1, toric models: run 1 only.**
   - Run 1 adds the broader model with unequal paired lengths: the same image with an extra real parameter per seam
     (`A1-toric-domain`), and non-injectivity (`A1-toric-noninjective`).
   - Raw toric surgery does not descend to isotopy classes (`A1-toric-nondescent`, via the jet computations
     `A1-pant-third-jet` and `A1-four-point-plumbing-jet`).
   - Arbitrary analytic cuts fail (`A1-nontoric-cut`), and the natural cut cover of type (0,4) is not of finite type
     (`A1-cut-not-algebraic`).
   - Run 2 has none of these. They concern definition choices the pages leave open (the cuts of 074 and 079–082).
   - Not checked by me; they are run 1's main results, and an independent check of the jets is the first successor
     task (§6).
2. **A.2(a), strength.**
   - Run 1 shows by a second jet that the cap at 0 moves with ℓ₁ at fixed ℓ₀.
   - Run 2 proves much more (`A:single-cap-all-lengths`, checked): **one positive cap determines every boundary length,
     and hence the whole system.** The proof uses the grafting projective structure and an argument on its holonomy.
3. **A.6 (the anabelian sheets 048–051): different routes, no conflict found at the level of the statements.**
   - Run 1 works with framed logarithmic fundamental groups: tame specialization by all-DVR tests, wild and Frobenius
     counterexamples, and a node inertia character equal to the cyclotomic character times the branch sign.
   - Run 2 works with tangential groups:
     - `A:tangential-anabelian`;
     - the polycurve compactification theorem (`A:polycurve-coarse-compactification`, its main result) and its
       intrinsic definition;
     - the arithmetic quilts (Known);
     - the real-place obstruction on M_{0,4} (`A:real-Galois-obstruction`, main).
   - None of these was checked by me.
4. **Subject 21 (66/004): run 2 goes further; there is no conflict.**
   - Run 1's `thm:B3-21` is the affine statement (Gabber 1994, Theorem 1, opened by the run). That is the case on his
     sheet ("X = Spec A, A I-adic, séparé et complet").
   - Run 2 agrees there (`B:henselian`). It adds the general quasi-compact quasi-separated case:
     - universal degree-0 comparison is equivalent to geometric henselianity (Known);
     - **a Nagata-type non-noetherian, non-separated pair with universal H⁰ comparison and no H¹ comparison for any
       ℤ/n, n > 1** (`C:subject21-torsion-counterexample`);
     - a positive theorem for separated schemes of finite type over a noetherian henselian pair.
   - So the answer to his "suffit-il de le savoir en degré 0 ?" is yes for affine X and no for general quasi-compact
     quasi-separated X (run 2, not checked).
   - Run 2 leaves `U:henselian-comparison` open.
5. **B.3, the choice of results.** The runs cite different literature for several subjects, and both refute different
   over-readings, for example:
   - subject 3: run 1 refutes "rank plus local types" with characteristic-7 curves, run 2 cites Pink;
   - subject 11: run 2 adds the piecewise and Greenberg results;
   - subject 16: both refute full π₁ invariance.

   No statement of one run contradicts one of the other that I read.
6. **Status labels.**
   - Run 1 marks the cap limit "Proved under stated hypotheses" (a fixed compactification); run 2 marks its Strebel
     limit "Proved".
   - Run 1 has 62 Known and 28 Refuted rows; run 2 has 64 Known, 37 Refuted and 1 Open.

## 3. What is new

**Against our own results (what changes in our records):**
1. **Our correction of 67/091 is wrong.** In sweep 3 (my CORRECTIONS row SA22-9, 67/091) and in the prompt's R5, we
   wrote that the corollary needs Spec k connected, e.g. a domain.
   - Run 1's counterexample, which I checked: R = ℤ[x,y,z]/(x² + yz − 1), σ = (x y; z −x). Here σ² = 1 and σ ≠ ±1, and
     P = coker(σ − 1) has a two-dimensional fibre at the maximal ideal (2, x−1, y, z).
   - Correct sufficient hypotheses: R a Dedekind domain, or 2 invertible and Spec R connected.
2. **Subject 24, second question, is not open in characteristic 0.** ae4ae3dc's H22-4 and STUDY §1 call it the first
   open case of the standard conjecture D.
   - It is classical. I re-derived the proof:
     - hard Lefschetz H² ≅ H⁶ and Lefschetz (1,1) make the Lefschetz components of algebraic classes in H⁴ algebraic;
     - Hodge index and Hodge–Riemann give definiteness on the three orthogonal pieces.
   - Run 1 cites Kleiman 1994.
   - In characteristic p it is known for abelian fourfolds through Broe's 2026 preprint (unchecked), and open in
     general.
3. **Our capping hunches are confirmed**, and one in a stronger form:
   - H22-67_003-046_084-101-1, the slit limit: run 1 `A2-explicit-limits` (Known; I checked the computation);
   - -2, not a box: `A2-nonbox`, by Lavrentiev;
   - -3, coupling: run 2 proves that a single cap determines every length.
4. **The orange slices are right in exactly one limit.** The letter's cells Q_i (67/019–020) are the Jenkins–Strebel
   circle domains of equal weights. The quadratic differential is −(z² − z + 1)dz²/(z²(z−1)²); its zeros are his poles
   e^{±iπ/3}; Q₀ has radius 4/(3√3). So **the admissible caps tend to his orange slices exactly when the three lengths
   grow at equal rates** (run 1 `A2-explicit-limits`, checked). The model is false as a description of all admissible
   systems, and true as that limit. This is the strongest positive statement about the letter.
5. **The structure behind capping.** Log cap radii are the gradient of a strictly convex potential in the squared
   lengths. Their image is cut out by the Jenkins–Strebel support function, the extremal problem of non-overlapping
   discs. This answers R22-2 (b) and the January Conjecture in corrected form.

**Against the literature:**
- Both runs claim no priority, and I have not searched the literature.
- New as statements of these runs:
  - the image theorem for the cap radii in Jenkins–Strebel terms;
  - the rigidity "one cap determines all lengths";
  - run 1's toric non-descent;
  - run 2's subject-21 counterexample beyond the affine case;
  - the explicit counterexamples (C₄ for Condition K, ℤ[(1+√−11)/2], the 091 ring).
- Known results the runs re-derive with locators:
  - Koebe and Lavrentiev;
  - Strebel's differentials;
  - Mondello's grafting;
  - Wolpert's cusp norm;
  - Gabber 1994;
  - the char-0 standard conjecture D for 2-cycles on fourfolds;
  - Mumford's 0-cycles;
  - Alling–Greenleaf.

## 4. Implications

**For the reading of the archive, by cote and scan:**
- **67/074–082 (section 6):** his maps are not isomorphisms onto the bundle of nonzero tensors. The image is a proper
  open domain (for (0,4): 0 < |q| < 16), with the right tangent map and π₁. The edition's note should say so, citing run 1
  `A1-global-refutation`, `A1-graph-range` and run 2 `A:04`.
- **67/068 "?":** answered no, in the strong form of run 2. **67/068–069, the Conjecture:** false as stated; the corrected
  image theorem replaces it.
- **67/019–020:** the orange slices are the equal-growth limit of admissible caps, and the general model is false.
  **67/021:** the collar question has no monotone answer.
- **67/091:** replace our refinement by "R Dedekind, or 2 invertible and Spec R connected". **67/086, 089, 097–098, 100,
  101:** as in sweeps 2 and 3, now confirmed twice.
- **66/004:** subject 24 is false for the first question and true in characteristic 0 for the second. Subject 21 holds
  for affine X (Gabber); for general X run 2 says degree 0 does not suffice (unchecked).
- **66/005:** subject 25 is false in both questions.
- **68/017–022:** Condition K is false (C₄). **68/036–046:** the corrections of sweep 3 stand, extended by both runs.

**For the programme:**
- Records to correct (ae4ae3dc integrates):
  - my `67_003-046_084-101_CORRECTIONS.tsv` row on 67/091;
  - STUDY §1 (subject 24) and HUNCHES H22-4;
  - STUDY §2 R2 and RESEARCH_PACKAGES R22-2, which are settled in large part;
  - R22-4 (Condition K: false);
  - the prompt's R5.
- No third run on A.1–A.5, A.7, B.1(a), B.2 or C is needed: two independent runs agree.

## 5. Bridges (redone 20–21 Nov 2026 under the corrected criterion of the brief, step 4)

**The frame.** Algebraic geometry from Weil through Grothendieck and Deligne was built as the road to the Riemann
hypothesis.
- Deligne's purity (*La conjecture de Weil* I, II) is its proof over finite fields: the Frobenius weights of Tate
  twists and of every pure motive.
- L. Alpöge, *Remark* (https://alpo.ge/remark.pdf, with the Lean archive), proves RH and GRH for Dirichlet L-functions.
  These are the L-functions of the twisted Tate motives χ ⊗ ℚ(n), since L(χ ⊗ ℚ(n), s) = L(χ, s+n). By sums, the
  result covers every Artin–Tate motive over ℚ with abelian Artin part, including the Dedekind zeta functions of abelian
  fields.

For every row below I state, as mathematics, one of three things: what RH/GRH (Alpöge) or purity (Deligne) gives
there; what the row gives back; or why that particular link carries nothing. The anchor is §5.0, the hexagons, which
the coordinator asked for in particular. Literature not opened today is marked "from memory". I read pages 2–3 of
Alpöge's note as text; I did not read his Lean files.

### 5.0 The hexagons: the (2,3,6) triangle group, the CM curve ℂ/ℤ[ω], the pants of 67, and the GT hexagon relation

**What Alpöge's note says** (remark.pdf, pages 2–3, read today).
- Page 2 credits a "(2, 3, 6)-triangle group trick" as strictly dominating "the Siegel argument", and reads it as
  "Stepanov without multiplicity".
- In his timeline (page 3):
  - step 2 works on "a CM curve for p inert in K" with the invariant derivation D;
  - step 3 makes the measure μ "automorphic from θ on sixfold cover of GL5 as a period integral of thetas", with the
    quadric x₁x₂ + ⋯ + x_{k−1}x_k interpreted on "corresponding CM e.g. ℂ/ℤ[ω]", and "Poincaré bundle on the edges".
- Footnote 3 puts the normalized Gauss sum "of order #|μ_K|" on the "#|μ_K|-fold cover of GL2".
- For K = ℚ(ω), ω = e^{2πi/3}, #μ_K = 6. The six of the sixfold cover is the order of μ₆, the unit group of the
  Eisenstein integers.

**1. The Euclidean case: one lattice, one group.**
- The triangle group Δ(2,3,6) has 1/2 + 1/3 + 1/6 = 1, so it is Euclidean.
  - Its orientation-preserving part is ℤ[ω] ⋊ μ₆. Its translation lattice is the hexagonal lattice ℤ[ω]. Its tiling of ℂ
    is the hexagonal tiling, whose hexagons are the Voronoi cells of ℤ[ω].
  - The rotation centres are of order 6 at the hexagon centres (the lattice points), of order 3 at the vertices, and of
    order 2 at the edge midpoints.
- The quotient E₀ = ℂ/ℤ[ω] is the elliptic curve with j = 0, Aut(E₀, 0) = μ₆, and CM by ℤ[ζ₃] = ℤ[ω]: **Alpöge's CM
  curve**.
- E₀/μ₆ is ℙ¹ with three cone points of orders 2, 3, 6. So E₀ → ℙ¹ is a Belyi map, and the hexagonal tiling is a
  regular dessin on the torus: the Euclidean case of the canonical geometry of maps (cartes) in the Esquisse d'un
  programme (from memory).
- **On Grothendieck's sheets this is cote 67, scans 094–100** (SA22-9), in my reading of sweep 3, confirmed by both runs
  (run 1 `A7-real-classification`, run 2 `A:real-elliptic`):
  - the lattice of his "cas hexagonal" (098) is ℤ + ℤ(1+i√3)/2 = ℤ[ζ₆] = ℤ[ω], so his curve is E₀;
  - its group G = D₆ of order 12 (094–095) is the point stabilizer of the extended (2,3,6) reflection group at a
    hexagon centre;
  - his two classes of reflections, "sommets" and "côtés" (095, 098), are the two conjugacy classes of mirrors of the
    (2,3,6) group through that centre. The mirrors through the hexagon's vertices and through its edge midpoints are not
    conjugate because 6/2 is odd;
  - they give the two real forms E′₃ and E′_{1/3}, i.e. y² = x³ ± 1 up to scaling, each with one real component;
  - his matrix (1 1; 0 −1) on 100 is the reflection of the regular hexagon in the diagonal 0e₀.
- The "same hexagons" are therefore literally the same: **the fundamental hexagon on 67/098–100 is a tile of the
  (2,3,6) tiling, and his curve there is Alpöge's ℂ/ℤ[ω].**
- *What the method gives on these sheets:*
  - The arithmetic Alpöge uses on E₀ lies at the finite places of K = ℚ(ω): D^p ≡ 0 at primes p inert in K, which is
    Deuring's supersingular reduction, a_p(E₀) = 0 for p ≡ 2 mod 3.
  - Through GRH it also gives RH for ζ_K(s) = ζ(s)L(χ₋₃, s), the zeta function of the CM field.
  - The sheets study E₀ at the real place, where K has none. So the method gives no step of the sheets' classification.
- *What the sheets give back:* the complete real-place data of E₀, which his argument (over the CM field) does not need:
  - its two real structures and their non-conjugacy;
  - E(ℝ) connected for both;
  - H¹(ℝ, E) = 0 (101; the E′ type).
- *Note on scope.* L(E₀/ℚ, s) is the L-function of a Hecke character of ℚ(ω) of infinity type (1,0), not a Dirichlet
  L-function. RH for it is outside the stated scope of the *Remark*, which expects the extended RH "with more time".

**2. The hyperbolic case: pants, right-angled hexagons, and the CM point of M_{0,4}.**
- A hyperbolic pair of pants with boundary lengths (ℓ₀, ℓ₁, ℓ_∞) is two right-angled hexagons glued along their
  alternate sides, the seams.
- Cap it canonically and place the cap centres at 0, 1, ∞ (A.2 of both runs; his letter to Bers, 67/016–021). The
  anticonformal involution z ↦ z̄ fixes the three seams, so the two hexagons are the pants' halves in the upper and
  lower half-planes.
- **When ℓ₀ = ℓ₁ = ℓ_∞,** the order-3 symmetry z ↦ 1/(1−z) acts on each hexagon. Its fixed points, the hexagon centres,
  are the roots of λ² − λ + 1 = 0, λ = e^{±iπ/3} (computed today).
  - These are exactly the λ where the Legendre curve y² = x(x−1)(x−λ) has j(λ) = 256(λ²−λ+1)³/(λ²(λ−1)²) = 0, that is,
    E_λ ≅ ℂ/ℤ[ω].
  - **So each right-angled hexagon of an equilateral pants is centred at a CM point of M_{0,4} lying over Alpöge's
    curve.**
- **The orange slices of the letter (67/019–020).**
  - His poles P^± = e^{±iπ/3} are the same two CM points.
  - The equal-weight Jenkins–Strebel differential, whose circle domains are the orange slices (run 1
    `A2-explicit-limits`, checked in §2–3), is a pullback from the j-line:
    −(λ²−λ+1)dλ²/(λ²(λ−1)²) = −¼ · dj²/(j(j − 1728)). The identity (dj)²/(j(j−1728)) = 4(λ²−λ+1)dλ²/(λ²(λ−1)²) was
    checked by computer algebra today.
  - The critical trajectory of −dj²/(4j(j−1728)) on the j-line is the segment [0, 1728]. Its preimage under the
    degree-6 map λ ↦ j is the theta graph of the three arcs through −1, ½, 2 (over 1728) joining e^{±iπ/3} (over 0).
  - **So the orange slices are the faces of the dessin d'enfant of the Belyi map λ ↦ j/1728 on M_{0,4}**, the clean
    dessin of Γ(2) ⊂ PSL₂(ℤ).
  - His model is false for all admissible systems (both runs) and **exact as the equal-growth limit** of the caps
    (run 1).
- **The triangle groups.**
  - PSL₂(ℤ) = Δ(2,3,∞) is the hyperbolic member of the family Δ(2,3,n), whose Euclidean member n = 6 is the hexagonal
    group above. Its order-3 point is the CM point j = 0, again ℂ/ℤ[ω].
  - Γ(2)/±1 = Δ(∞,∞,∞) = π₁^{orb} of M_{0,4} has index 6 = |𝔖₃| (the degree of λ ↦ j).
  - The (∞,∞,∞) triangle is the ℓ → 0 degeneration of a right-angled hexagon: the pants with three cusps is two ideal
    triangles.
- **The presentation on 67/050** (SA22-5; checked in sweep 3): SL(2,ℤ) = ⟨ρ, σ | ρ³ = σ², ρ⁶ = 1⟩, the amalgam
  μ₄ *_{μ₂} μ₆. Here ρ = ST of order 6 generates the stabilizer of ω, which is Aut(ℂ/ℤ[ω]) = μ₆. The same μ₆ makes
  Alpöge's sixfold cover.
- **The degenerations, in one line:**
  - ℓ → 0: hexagons → ideal triangles, pants → Γ(2)\H;
  - all ℓ → ∞ at equal rates: caps → orange slices, and the hexagons collapse onto the two trivalent vertices of the
    theta graph at the CM points (the ribbon-graph limit of hyperbolic surfaces with long boundaries; Mondello 2009,
    from memory);
  - one ℓ dominant: the cap → Koebe's slit domain, radius 4 (both runs; my hunch of sweep 3).
- *What the method gives here:* RH/GRH concern the zeros of ζ and L(χ, s). The pants geometry, the caps and the
  section-6 maps are real-analytic constructions on Teichmüller spaces. **His method gives nothing to them,** because
  the questions of A.1–A.4 contain no L-function.
- *What the sheets give back:* a geometric locus for his curve in the moduli of the 1984 programme. ℂ/ℤ[ω] sits at:
  - the centres of the right-angled hexagons of the equilateral pants;
  - the poles of the orange slices;
  - the trivalent vertices of the j-dessin on M_{0,4};
  - the order-6 element ρ of 67/050.

  No step of his argument uses this.

**3. The Grothendieck–Teichmüller hexagon relation.**
- An element (λ, f) of GT̂ (Drinfeld 1990; Ihara; from memory) satisfies, besides the 2-cycle and pentagon relations,
  the hexagon relation f(x,y) x^m f(z,x) z^m f(y,z) y^m = 1 with xyz = 1 and m = (λ−1)/2.
- In π₁ of M_{0,4} = ℙ¹ ∖ {0,1,∞} with tangential base points at the cusps, its six factors are:
  - the three paths along the three real intervals (0,1), (1,∞), (∞,0): **the three seams of the pants**, in the cusp
    limit;
  - the three half-turns around the cusps.

  This hexagon is the boundary of the upper ideal triangle, the ℓ → 0 limit of the upper right-angled hexagon. The
  relation is invariant under the order-3 rotation z ↦ 1/(1−z) about its centre e^{iπ/3}, **the CM point of
  ℂ/ℤ[ω]**.
- Ihara's reading (from memory): the hexagon relation expresses that the Galois action respects this order-3 symmetry.
- *What purity and RH give.* The G_ℚ action on π₁(M_{0,4}) factors through mixed Tate motives over ℤ (§5.2).
  - Purity gives its weight filtration: the graded pieces are ℚ_ℓ(n), on which Frobenius at p acts by p^{−n}.
  - The arithmetic content of GT (the Soulé characters, the periods ζ(2m+1)) is special values at integers, about which
    RH says nothing.
- *What the sheets give:* 67/048–051 (SA22-5) and 084–089 (SA22-8) contain the Teichmüller groupoid of type (0,4) with
  its 𝔖₄ ⊃ V symmetry. They contain no hexagon relation as such.

**Check events** for 5.0 are in the intake's CHECK_EVENTS.tsv: the j-identity and the fixed points (computation), the
lattice identification and the reflection classes (re-derivation against 67/094–100), and the triangle-group facts
(re-derivation).

### 5.1 Tate twists in anabelian geometry: purity gives the graph, and GRH makes the Frobenius tests effective

Rows:
- run 1: `A6-kummer`, `A6-cyclotomic-detection`, `A6-graphic`, `A6-normal-kummer`, `A6-anabelian`, `A6-procyclic`,
  `A6-node-character`;
- run 2: `A:Kummer-faithfulness`, `A:inertia-maximality`, `A:tangential-anabelian`, `A:log-graphicity`,
  `A:tensor-log-comparison`.

All the flagged ones are in `BRIDGE_FLAGS.tsv` except `A6-node-character`, `A6-normal-kummer` and `A:log-graphicity`,
which I add.

1. **What purity gives (used, through the cited theorems).**
   - Take a stable curve over a field K finitely generated over ℚ. The Tate module of its generalized Jacobian has a
     weight filtration: the toric part, one copy of ℤ_ℓ(1) for each cycle of the dual graph, has weight −2; the abelian
     part, the H¹ of the normalized components, has weight −1.
   - The weights are read off the Frobenius eigenvalues at primes of good reduction of a model. On the abelian part they
     are Weil numbers of absolute value q^{1/2}, by Weil's RH for abelian varieties over finite fields, the first case
     of Deligne's purity. On the toric part they are q, the eigenvalue of the arithmetic Frobenius on ℤ_ℓ(1).
   - This weight separation is how the dual semi-graph (vertices, nodes, cusps) is recovered from the Galois action in
     Mochizuki's semi-graphs of anabelioids and in Hoshi–Mochizuki, which the rows cite for `A6-graphic` and
     `A:tangential-anabelian` (from memory).
   - So **purity gives** the graphicity statements: an element of the geometric fundamental group lies in a cusp or node
     inertia group exactly when its image is in the weight −2, Tate-twisted part with the cyclotomic action
     (`A6-cyclotomic-detection`).
   - The rows give nothing back to purity.
2. **What GRH gives (not used; it would make the tests effective).**
   - The rows use only qualitative facts:
     - ℤ̂(1)^{G_K} = 0 and the injectivity of K^× → H¹(G_K, ℤ̂(1)): these hold because K ∩ ℚ(μ_{ℓ^∞}) is finite;
     - the existence of a Frobenius with cyclotomic value ≠ 1.
   - **The node character of run 1, `A6-node-character`: "the node inertia character is cyclotomic times the
     branch-interchange sign".**
     - As a Galois module, the inertia at a non-split node is the rank-one Artin–Tate motive ε ⊗ ℤ_ℓ(1). Here ε is the
       quadratic character of the field ℚ(√d) over which the two branches are defined (for K = ℚ).
     - GRH for L(ε, s) is the Riemann hypothesis for ε ⊗ ℚ(1), since L(ε ⊗ ℚ(1), s) = L(ε, s + 1).
   - **The consequence, now unconditional if Alpöge's claim holds.** Bach's explicit bound, under GRH for Dirichlet
     L-functions: the least prime p with ε(p) = −1 is at most 2 (log |d|)² (from memory; Bach 1990). So the branch sign
     of a node is detected by Frobenius at a prime of size O((log |d|)²).
   - In the same way the least prime p ≡ a (mod ℓ^k) is polynomial in ℓ^k under GRH for the characters mod ℓ^k. So a
     Frobenius with cyclotomic value ≠ 1, as `A6-kummer` and `A:Kummer-faithfulness` use it, is found below an
     explicit bound.
   - Effective GRH does **not** reach the Kummer fields K(μ_n, a^{1/n}) themselves, as Hooley's conditional proof of
     Artin's conjecture needs: their Artin part is non-abelian. The brief's extension covers only abelian Artin parts.
3. **`A:inertia-maximality` (run 2, refuted).** "Invariant, ≅ ℤ̂, acted on cyclotomically" does not single out the nodes
   and cusps: finite-index subgroups have the same weight. The weight −2 condition, from purity, is necessary and not
   sufficient. The link carries nothing further.

### 5.2 The Galois action on M_{0,4} and the Teichmüller tower: the bridge is to mixed Tate motives over ℤ

Rows: run 2 `A:arithmetic-quilts` (Known), `A:real-Galois-obstruction` (Proved, main); run 1 `A6-matrix-presentations`,
`A6-four-punctures`, `A6-projective-line` (statement level).

- π₁ of M_{0,4} = ℙ¹ ∖ {0, 1, ∞} is the classical case.
  - The G_ℚ action on its pro-unipotent or pro-ℓ completion factors through the motivic Galois group of mixed Tate
    motives over ℤ (Deligne–Ihara; Deligne–Goncharov; Brown 2012, from memory).
  - Its weight graded pieces are sums of ℚ_ℓ(n).
  - The Soulé characters κ_{2m+1} correspond to the generators of K_{4m+1}(ℤ) ⊗ ℚ, each of rank 1 (Borel), whose periods
    are ζ(2m+1).
- **What the bridges give.**
  - Purity gives the weight filtration: the lower central series graded pieces are pure of the weights of ℚ_ℓ(n), and
    Frobenius at p acts on ℚ_ℓ(n) by p^{−n}.
  - RH and GRH give nothing about the Soulé characters or their periods. Those are special values at integers ≥ 3,
    where ζ converges absolutely, not zeros in the critical strip.
- **What the rows give.**
  - `A:arithmetic-quilts` restates the known G_ℚ action in quilt coordinates.
  - `A:real-Galois-obstruction` concerns the real place. Complex conjugation acts on ℚ(n) by (−1)^n: the real Frobenius
    of the Betti realization. That enters L-functions only through the Gamma factors Γ_ℝ(s + n), which do not concern
    the location of zeros.
- **So the link carries nothing to RH**, and nothing from RH to these rows, beyond the weight bookkeeping that purity
  provides.

### 5.3 The standard conjectures for 2-cycles on fourfolds: the positivity in Grothendieck's road to the Weil conjectures

Rows:
- run 1: `thm:B1a-betti`, `lem:B-basechange-num`, `thm:B1a-etale`, `prop:B1b-criterion`, `prop:B1b-gap`,
  `thm:B1b-abelian`, `prop:B1b-scope`, `B1b-correspondence`, `B1b-blowup`, `B1b-fermat`;
- run 2: `B:betti`, `B:num-basechange`, `B:charzero`, `B:integral`, `B:ancona-scope`, `B:abelian`, `B:criterion`,
  `B:subject24`.

1. **Characteristic 0** (`thm:B1a-betti`, `B:betti`, `B:charzero`, `thm:B1a-etale`).
   - The positivity used is the Hodge–Riemann relations, the archimedean form of the Hodge standard conjecture.
   - Neither purity nor RH enters, and none could: the statement is about intersection forms on algebraic classes in
     H⁴, not about Frobenius eigenvalues.
   - The row gives back the char-0 case of conjecture D for 2-cycles on fourfolds (classical; re-proved in §3).
2. **Characteristic p** (`prop:B1b-*`, `thm:B1b-abelian`, `B:abelian`, `B:ancona-scope`, `B:criterion`).
   - **What purity gives.** For X over 𝔽_q, H⁴(X̄, ℚ_ℓ(2)) is pure of weight 0 (Deligne, Weil I). The Tate classes are in
     the generalized eigenspace of geometric Frobenius for the eigenvalue 1. If Frobenius acts semisimply there and the
     Tate conjecture holds, numerical and homological equivalence agree (Tate 1994, Theorem 2.9, from memory).
   - So purity places the problem, but purity alone gives neither D nor the Hodge-type positivity. Deligne's proof of
     the Weil conjectures went around the standard conjectures.
   - **What the rows give back.** For abelian fourfolds over 𝔽_q, through Broe's 2026 preprint (unchecked):
     - numerical = ℓ-adic homological equivalence for 2-cycles;
     - hence, with Jannsen's semisimplicity of numerical motives (from memory), Frobenius acts semisimply on the image of
       the cycle class map in H⁴(Ā, ℚ_ℓ(2)).
   - That is one half of the Tate-conjecture package at s = 2. The other half, surjectivity onto the Tate classes, is
     not claimed. RH for ζ over ℚ gives nothing here.
3. **The Fermat cubic fourfold** (run 1 `B1b-fermat`, Proved): here GRH (Alpöge) gives a concrete statement.
   - F = {z₀³ + ⋯ + z₅³ = 0} contains the planes {z_{i₁} = −ζ z_{i₂}, z_{i₃} = −ζ′ z_{i₄}, z_{i₅} = −ζ″ z_{i₆}}, ζ ∈ μ₃,
     which are defined over ℚ(μ₃). So the span A ⊂ H⁴(F_ℚ̄, ℚ_ℓ(2)) of their classes is an Artin representation of G_ℚ
     factoring through Gal(ℚ(μ₃)/ℚ).
   - A ⊗ ℚ(−2) is therefore an Artin–Tate motive with abelian Artin part. Its L-function is ζ(s−2)^a L(χ₋₃, s−2)^b, with
     a + b = dim A and χ₋₃ the character of ℚ(√−3).
   - **GRH (Alpöge) puts every nontrivial zero of this part of L(H⁴(F), s) on Re s = 5/2,** the centre (w+1)/2 for weight
     w = 4.
   - **What the row gives back:** numerical = homological equivalence for all cycles on F. The cycle classes then form
     the numerical motive, whose L-function, for the part spanned by the planes, is the Artin–Tate L-function just
     written.
   - The two facts are independent. GRH places the zeros; the row identifies the cycle group. The pole at s = 3, of order
     a, is the Tate-conjecture statement, which neither gives.
4. **`B1b-correspondence` and `B1b-blowup`.** D transfers along correspondences and blow-ups:
   h(Bl_Z X) = h(X) ⊕ ⊕_j h(Z)(−j). The Tate twists (−j) shift weights by 2j, which is purity's bookkeeping. Nothing
   about zeros enters.
5. **`B:subject24`.** The summary row of subject 24: as items 1–2.

### 5.4 Trace formulas, Euler characteristics and conductors: these rows give the degree of an L-function, and purity gives the absolute values of its zeros

Rows:
- run 1: `thm:B3-trace`, `thm:B3-index`, `thm:B3-operators`, `thm:B3-pprimary`, `thm:B3-holomorphic-lefschetz`;
- run 2: `B:subject3`, `B:subject4`, `B:subject5` (in `BRIDGE_FLAGS`), `B:subject6`, `B:p-Euler`.

1. **The ℓ-adic trace formula** (`thm:B3-trace`, `B:subject6`) is the cohomological form
   Z(X/𝔽_q, t) = ∏ᵢ det(1 − Frob·t | H^i_c)^{(−1)^{i+1}}. **Purity** (Deligne, Weil I) is RH for this Z.
   - The rows give the trace formula, and purity gives the absolute values of the zeros. Together they are the Weil
     conjectures.
   - RH for ζ over ℚ is only an analogy here.
2. **Euler–Poincaré and conductor formulas** (`thm:B3-index`, `thm:B3-operators`, `B:subject4`, `B:subject5`).
   - For a lisse sheaf 𝓕 on an open curve U over 𝔽_q, the L-function L(U, 𝓕, t) is a rational function of degree
     −χ_c(U, 𝓕). The Grothendieck–Ogg–Shafarevich formula computes this degree from the rank and the Swan conductors.
   - So **the rows give the number of zeros** (Raynaud's formula with operators in `thm:B3-operators`; the
     Kato–Saito Swan class in `B:subject4`). **Purity** (Weil II, 3.2.3) gives their absolute values for pure 𝓕.
   - For `B:subject5`, an abelian scheme A over U with an operator algebra:
     - the L-function of A over the function field, through j_*V_ℓA on C, has −χ(C, j_*V_ℓA) zeros (from the row);
     - all of them have weight 2, |α| = q (from purity).
   - This is the function-field side of BSD. GRH over ℚ gives nothing.
3. **The p-primary formula** (`thm:B3-pprimary`, `B:subject3`, `B:p-Euler`). The p-rank Euler formula (Deuring–
   Shafarevich) counts the unit-root zeros, those of slope 0, of the zeta function of a curve. Purity gives the complex
   absolute values of the same zeros; the row's refutation of "rank plus local types determines the p-rank" (the
   characteristic-7 curves y² = x³ − x and y² = x³ − x + 1) says the slope count is not a local-type invariant. RH over
   ℚ: nothing.
4. **`thm:B3-holomorphic-lefschetz`** (Atiyah–Bott) is the archimedean, analytic analogue. The link carries nothing
   arithmetic.

### 5.5 Motivic cohomology, K-theory and special values: the rows are the coefficient formalism, and RH says nothing about special values

Rows: run 1 `thm:B3-motives` (in `BRIDGE_FLAGS`), `thm:B3-arithmetic-duality`; run 2 `B:subject28` (in `BRIDGE_FLAGS`),
`B:subject7`.

- **What the rows give.**
  - Beilinson motives DM_B(X) over schemes of finite type over ℤ, with the six operations (Cisinski–Déglise).
  - For X = Spec 𝒪_K and the Tate motive ℚ(n), Hom(1, 1(n)[1]) is H¹_M(𝒪_K, ℚ(n)) ≅ K_{2n−1}(𝒪_K)_ℚ. Its rank is r₂, or
    r₁ + r₂ for n odd (Borel; from memory, through the Adams decomposition of rational K-theory, Riou and
    Cisinski–Déglise 14.2).
  - Geisser's duality (`thm:B3-arithmetic-duality`, `B:subject7`) is the duality for the étale cycle complexes ℤ(n)
    over number rings. It is an input of Lichtenbaum's Weil-étale formulation of ζ_X at integers.
- **What the bridges give.**
  - Borel's theorem identifies these ranks with the order of the zero of ζ_K at s = 1 − n, read off the Gamma factors
    of the functional equation. Its regulator gives ζ_K(n) up to a rational factor, at a point of absolute convergence
    for n ≥ 2.
  - Beilinson and Bloch–Kato for ℚ(n) refine this.
  - **None of this uses or is touched by RH or GRH.** They locate the nontrivial zeros, not special values at integers.
    For abelian K, GRH (Alpöge) gives RH for ζ_K = ∏ L(χ, s), which is independent of these special values.
- **What the rows give back:** nothing to RH. The link is the standard road (special values of ζ and L-functions at
  integers through motivic cohomology), along which RH carries no information.

### 5.6 The square of an algebraically trivial cycle: over number fields the conjectured answer is the opposite, and RH gives nothing toward it

Rows: run 1 `lem:B2-mumford`, `thm:B2-square`, `prop:B2-kernel`; run 2 `B:trace`, `B:square`, `B:alb-kernel`,
`B:subject25`.

- **What the rows give.**
  - On E × E over ℂ with points in general (transcendental) position, D = pr₁*(p−q) + pr₂*(p′−q′) is algebraically
    trivial.
  - D² = 2 (p−q)×(p′−q′) is a nonzero, indeed non-torsion, element of the Albanese kernel T(E×E) ⊂ CH₀.
  - These exterior products generate T (run 2 `B:alb-kernel`).
- **The bridge, stated as mathematics.**
  - The Bloch–Beilinson conjecture predicts, for a surface X over a number field (or over ℚ̄), that the Albanese kernel
    is torsion: T(X_ℚ̄) ⊗ ℚ = 0 (from memory). This is equivalent to the injectivity of the Abel–Jacobi map on
    CH²_hom ⊗ ℚ over number fields, and it is tied to the orders of vanishing of L(h³(X), s) at s = 2.
  - So for p, q, p′, q′ ∈ E(ℚ̄) **the conjectured answer to the "pb du carré" is yes up to torsion**. The rows' "no"
    rests essentially on transcendental points.
  - That is consistent with the conjecture, and it is the precise arithmetic content of the question on 66/005.
  - RH and GRH (Alpöge) give nothing toward Bloch–Beilinson. Its L-functions are those of E × E, and its content is
    orders of zeros at the centre, not their location.

### 5.7 Purity in the sense of absolute cohomological purity: the Tate twist is weight bookkeeping

Rows: run 1 `thm:B3-purity`; run 2 `B:PM2`, `B:subject23` (Chow pullback with "pure" codimension).

- Gabber's absolute purity, R i^! ℤ/n = ℤ/n(−c)[−2c] for a regular immersion of codimension c, carries the Tate twist
  (−c).
- Over a finite field the Gysin map therefore shifts Frobenius weights by 2c, which is compatible with Deligne's purity.
- The word "purity" names two different theorems here. The link carries nothing beyond this weight bookkeeping.

### 5.8 Tannakian categories, adèles, and duality with Tate modules: the link carries nothing

- **Tannakian categories** (run 1 `thm:B3-tannaka`, `thm:B3-nonneutral`; run 2 `B:subject22`). The Tannakian formalism
  is what defines motivic Galois groups, for example that of mixed Tate motives over ℤ with its periods, the multiple
  zeta values. The rows prove the formalism (Deligne–Milne; Deligne 1990). They assert nothing about L-functions, and RH
  gives nothing to them.
- **Adèles** (run 1 `thm:B3-adeles`; run 2 `B:subject27`, in `BRIDGE_FLAGS` by the word "Motives" in a neighbouring
  heading). These rows are the Parshin–Beilinson adèle resolution of quasi-coherent sheaves. The one-dimensional
  adèles of ℚ are the road to Tate's thesis (the functional equation of ζ and L(χ, s)), but these rows contain no zeta
  integral. The link carries nothing.
- **Local duality for abelian varieties** (run 1 `thm:B3-abelian-duality`, in `BRIDGE_FLAGS` by "Tate module"):
  Suzuki's duality over local fields of characteristic p. It is an input of the local factors of BSD (Tate–Shafarevich
  and Tamagawa terms), with no RH content.

### 5.9 Periods of real elliptic curves: the archimedean factor of BSD

Rows: run 1 `A7-real-classification`, `A7-real-topology`; run 2 `A:real-elliptic`, `A:real-topology` (67/091–101).

- The rows give the period lattices ℤ + i√a ℤ and ℤ + ((1 + i√a)/2) ℤ, and E(ℝ) with 2 or 1 components.
- That is the archimedean data of the BSD formula: c_∞ ∈ {1, 2}, and the real period Ω = c_∞ ∫_{E(ℝ)⁰} |ω|.
- The Gamma factor of L(E, s) is the same for all real forms. RH and GRH give nothing here, and the rows give nothing
  back to them.

### 5.10 Rows matched by the words "positivity", "weight", "Euler" or "zeta" in another sense: the link carries nothing

- **Real-analytic convexity of the cap energy** (run 1 `A2b-energy`, `A1-dimensions`; run 2 `C:A2b-injectivity`,
  `C:A2b-normal-families`, `A:bordered-radius-algorithm`, `A:single-cap-with-cusps`). The positivity is the positive
  definite Hessian of the cap potential S, or the positivity of lengths.
  - The underlying extremal problem (Jenkins–Strebel; Lavrentiev) is a real variational problem on Teichmüller-type
    spaces. It has no Frobenius, weight or L-function.
  - "Weights" in `C:A2b-pants-extremes` are the Jenkins–Strebel weights p_i, the squared lengths.
- **Euler characteristic of a surface** (run 1 `A2-collar`, `A4-grafting`; run 2 `C:A2e-nonmonotonicity`): Gauss–Bonnet,
  χ < 0. Nothing arithmetic.
- **ζ as a variable name** (run 2 `A:tensor`).
- **Combinatorial positivity on cote 68** (run 1 `C-rearrangement`, `C-K-counter`, `C-K-replacement`; run 2
  `C:majorization`, `C:determinant-incidence`): rearrangement and majorization inequalities for convolutions on finite
  groups, and incidence positivity in the graded-determinant sign computation. They have no arithmetic content.
- **Dominant weights and approximation** (run 2 `B:subject20`, the dominant weights of Kempf vanishing; `B:subject13`,
  Artin approximation): different meanings of the words.

**Summary of the bridges.**
- **The hexagons are the same** (5.0).
  - The fundamental hexagon of 67/098–100 is a tile of the (2,3,6) tiling, and the curve there is Alpöge's ℂ/ℤ[ω]
    (μ₆ = #μ_K, the six of his sixfold cover).
  - The right-angled hexagons of the equilateral pants, the poles of the orange slices (67/019–020) and the vertices of
    the j-dessin on M_{0,4} all sit at the CM point j = 0.
  - The orange slices are the faces of that dessin: the circle domains of −¼ dj²/(j(j−1728)) pulled back to the λ-line.
  - The Grothendieck–Teichmüller (GT) hexagon relation is the boundary path of the upper ideal triangle, the cusp limit
    of a pants hexagon, and it is invariant under the order-3 rotation about that CM point.
- **What his method gives there.** RH for ζ_{ℚ(ω)} = ζ·L(χ₋₃), and Deuring's supersingular reduction at inert primes.
  It gives no step of the real-analytic questions of A.1–A.4.
- **What the sheets give back.** The real-place data of ℂ/ℤ[ω] and its geometric locus in the 1984 moduli. Neither is
  used by his argument.
- **Purity.** It is used, through the cited anabelian theorems, to separate the weight −2 Tate-twisted part (5.1). It
  gives the absolute values of the zeros whose number the trace and Euler-characteristic rows compute (5.4). It places
  the characteristic-p standard-conjecture rows (5.3).
- **GRH.** It gives an effective branch-sign test for non-split nodes, by Bach's bound (5.1). It puts the zeros of the
  Artin–Tate part of L(H⁴, s) of the Fermat cubic fourfold on Re s = 5/2 (5.3).
- **Where the link carries nothing.** In 5.2 and 5.5–5.9 the link runs to special values, periods, Chow groups or
  Tannakian formalism. RH concerns the location of zeros and says nothing there; each row is named with that reason.

## 6. Prompt updates (for a successor of RESEARCH_SA22)

1. **Close and do not reopen:** A.1 (the main question), A.2, A.3, A.4, A.5, A.7, B.1(a), B.1(c), B.2 and C. Both runs
   agree, and I checked the key steps.
2. **Correct the prompt's inputs:**
   - R5's "needs Spec k connected" is false;
   - L1 is classical;
   - L2 and L8 are refuted;
   - L4 holds in corrected form (limits are Jenkins–Strebel cells; one dominant end gives the slit);
   - our hunches on capping are settled.
3. **What a successor run should do:**
   - (a) independently check run 1's toric non-descent: the third-jet computations of `A1-pant-third-jet` and
     `A1-four-point-plumbing-jet`, by computer algebra;
   - (b) check run 2's subject-21 counterexample (`C:subject21-torsion-counterexample` with `C:Nagata-input` and
     `C:Goldman-branches`) and settle `U:henselian-comparison`;
   - (c) check A.6 against Mochizuki and Hoshi: run 2's `A:polycurve-coarse-compactification` and
     `A:real-Galois-obstruction`, run 1's `A6-intrinsic-tame` and `A6-tame-specialization`;
   - (d) check Broe's 2026 preprint (abelian fourfolds in characteristic p), on which both runs' B.1(b) rests;
   - (e) the original sources still missing in both runs: Fujiwara 1995, Pfluger 1960, Lieberman 1968, and Alling–
     Greenleaf beyond pp. 60–66.
4. **No new research questions arise for Part A of cote 67.** The remaining analytic questions (an explicit formula for
   the metric after removing a collar; explicit cap shapes) are low priority for the archive.

## 7. Rows checked, and how

**Today, proof read and checked:**
- Run 1:
  - `A1-dimensions`, `A1-cap-bound`, `A1-tensor`, `A1-global-refutation` (refutation confirmed), `A1-zero`,
    `A1-retained-discs`, `A1-first-order`;
  - `A1-graph-range` (the reduction; its inputs at statement level);
  - `A2-schwarzian`, `A2-independence` (refutation confirmed), `A2-explicit-limits` (the computations), `A2-nonbox`,
    `A2-cusp-norm`;
  - `A7-domain-counterexample` (refutation confirmed), `A7-PID-count`, `A7-real-classification`, `A7-ratio-j`
    (refutation confirmed).
- Run 2: `A:orange`, `A:single-cap-all-lengths`; `A:eigenmodule-correction` is confirmed through run 1's counterexample.

**Independent re-proofs:**
- Today: `thm:B1a-betti` and `B:betti`, `B:charzero` (Betti case), and the construction in `thm:B2-square` and
  `B:square`.
- Sweeps 2–3 (18–19 Nov), with statements compared today:
  - `A4-orange-extremal`;
  - `A5-normalizer`, `A5-six-points`, `A5-faces`, `A5-groupoid`;
  - `A7-gluing-modules`, `A7-real-topology`;
  - `A:octahedron`, `A:octahedron-certificate`, `A:fourpoint-groupoid`;
  - `A:real-elliptic`, `A:pid-involutions`, `A:real-topology`.

**Statement level:** all other rows (§8). That includes run 1's toric rows and run 2's A.6 and subject-21 rows.

The check events are in `INTAKE_RESEARCH_SA22_20261120_CHECK_EVENTS.tsv` (38 rows).

## 8. The table

| Run | Row | Run's status | My check | Note |
|---|---|---|---|---|
| 1 | `A1-dimensions` | Known | targeted proof check, confirmed | graph count sum(3g_v-3+n_v)+/E/ = 3g-3+n re-derived; the peripheral-marking witness a->ab re-derived (as in sweep 3) |
| 1 | `A1-cap-bound` | Known | targeted proof check, confirmed | area-theorem proof of the Koebe bound read; it is the bound of our sweep-3 check (letter 019) |
| 1 | `A1-tensor` | Proved | targeted proof check, confirmed | seam zeta*eta = c; /q/ = product of the conformal radii |
| 1 | `A1-global-refutation` | Refuted | refuted (by the run); counterexample checked, confirmed | nodal (0,4), q = 17 against the cap bound 4*4 = 16; holds for every stable type of positive complexity (norm-17 tensors on a trivalent graph curve) |
| 1 | `A1-zero` | Proved | targeted proof check, confirmed | (0,3): no essential cut; capping inverse to cap removal |
| 1 | `A1-retained-discs` | Proved | targeted proof check, confirmed | equal circumferences make the toric identification an isometry; collar metric dr^2 + cosh^2 r ds^2 glues |
| 1 | `A1-first-order` | Known | targeted proof check, confirmed | Ext^1(Omega_A, A) = A/(x,y) for A = C[[x,y]]/(xy); the tensor t d_x (x) d_y is coordinate-free at first order |
| 1 | `A1-nontoric-cut` | Refuted | not read in full: statement read |  |
| 1 | `A1-graph-range` | Proved under stated hypotheses | targeted proof check of the reduction, confirmed; its inputs A2b-energy, A2b-recession, A2b-image read at statement level | log/q_e/ = dPsi/ds_e with Psi = sum_v S_v(A_v s) strictly convex; recession function gives the image; radial retraction gives the pi_1 statement |
| 1 | `A1-small-ranges` | Proved | not read in full: statement read |  |
| 1 | `A1-bordered-landing` | Refuted | not read in full: statement read; agrees with our earlier independent check | consistent with run 2 A:MDB-forgetting-admissibility |
| 1 | `A1-bordered-shadow-range` | Proved | not read in full: statement read |  |
| 1 | `A1-bordered-shape-image` | Proved | not read in full: statement read |  |
| 1 | `A1-toric-domain` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A1-toric-noninjective` | Refuted | not read in full: statement read |  |
| 1 | `A1-toric-full-discs` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A1-pant-third-jet` | Proved | not read in full: statement read |  |
| 1 | `A1-four-point-plumbing-jet` | Proved | not read in full: statement read |  |
| 1 | `A1-toric-nondescent` | Refuted | not read in full: statement read |  |
| 1 | `A1-cut-not-algebraic` | Refuted | not read in full: statement read |  |
| 1 | `A1-welding-plumbing` | Proved | not read in full: statement read |  |
| 1 | `A1-kra-comparison` | Known | not read in full: statement read |  |
| 1 | `A1-wolpert-comparison` | Known | not read in full: statement read |  |
| 1 | `A1-hinich-counterexample` | Known | not read in full: statement read |  |
| 1 | `A1-Earle-Sipe-comparison` | Known | not read in full: statement read |  |
| 1 | `A1-Earle-Marden-original` | Known | not read in full: statement read |  |
| 1 | `A2-schwarzian` | Known | targeted proof check, confirmed | T(z) = a0/z^2 + a1/(z-1)^2 + (a_inf - a0 - a1)/(z(z-1)), a_j = (1 + l_j^2/4pi^2)/2; double pole a_inf at infinity and b = (a0 + a1 - a_inf)/(2 a0) re-derived |
| 1 | `A2-independence` | Refuted | refuted (by the run); counterexample checked, confirmed | b = 1/2 for (2pi,2pi,2pi) and b = 5/4 for (2pi,4pi,2pi): the cap at 0 changes with l_1 at fixed l_0; answers 67/068 '?' negatively |
| 1 | `A2-cusp-norm` | Known | targeted proof check, confirmed | cusp coordinate unique up to rotation gives the norm; horocycle of length h has radius exp(-2pi/h) |
| 1 | `A2-collar` | Proved | not read in full: statement read |  |
| 1 | `A2b-regularity` | Proved | not read in full: statement read |  |
| 1 | `A2b-energy` | Proved | not read in full: statement read |  |
| 1 | `A2b-recession` | Proved | not read in full: statement read |  |
| 1 | `A2b-image` | Proved | not read in full: statement read; agrees with our earlier independent check | consistent with run 2 C:A2b-image (JS support inequalities) |
| 1 | `A2-strebel-deficit` | Proved | not read in full: statement read |  |
| 1 | `A2-cap-limit` | Proved under stated hypotheses | not read in full: statement read; agrees with our earlier independent check | consistent with run 2 C:A2b-strebel-limit |
| 1 | `A2-explicit-limits` | Known | targeted proof check of the explicit computations, confirmed; the limit theorem A2-cap-limit used at statement level | q_p for p = (1,0,0) pulls back by k(u) = 4u/(1+u)^2 to -du^2/u^2 (slit domain, radius 4); for p = (1,1,1) the critical graph bounds Q_0 = {/z/<1, Re z<1/2}, radius 4/(3 sqrt 3): the orange slices are the equal-growth limit |
| 1 | `A2-nonbox` | Known | targeted proof check, confirmed | Lavrentiev r0 r1 <= 1 (half-planes extremal) with individual suprema 4: not a box; this is our hunch H22-67_003-046_084-101-2 |
| 1 | `A2-collar-general` | Proved | not read in full: statement read |  |
| 1 | `A2-collar-shape` | Proved | not read in full: statement read |  |
| 1 | `A2-collar-explicit` | Proved | not read in full: statement read |  |
| 1 | `A3-boundary-chart` | Proved | not read in full: statement read |  |
| 1 | `A3-rectifiable` | Proved | not read in full: statement read |  |
| 1 | `A3-welding` | Known | not read in full: statement read |  |
| 1 | `A3-graph` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A3-slit` | Known | not read in full: statement read |  |
| 1 | `A3-L5` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A4-orange-extremal` | Refuted | independent re-proof (ours), agrees | the extremal-length refutation re-derived by us in sweep 3 (Michel Hua's project's argument); statement compared |
| 1 | `A4-orange-jets` | Refuted | not read in full: statement read; agrees with our earlier independent check | consistent with A2-explicit-limits (checked): the slices are the equal-growth limit only |
| 1 | `A4-grafting` | Known | not read in full: statement read |  |
| 1 | `A4-action` | Proved | not read in full: statement read |  |
| 1 | `A5-normalizer` | Proved | independent re-proof (ours), agrees | sweep 3: iz and (z+1)/(z-1) give S_3, kernel V, /N(V)/ = 24 |
| 1 | `A5-six-points` | Refuted | independent re-proof (ours), agrees | sweep 2: octa.py p <= 29 and the S_5 = PGL_2(F_5) argument; char 5 exception |
| 1 | `A5-faces` | Proved | independent re-proof (ours), agrees | sweep 3: one face has stabilizer C_3, a pair of opposite faces S_3 |
| 1 | `A5-groupoid` | Proved | independent re-proof (ours), agrees | sweep 3: the Theorem of 089 uses only V(I) and X/V = Z(J); every char != 2 |
| 1 | `A5-moduli` | Proved under stated hypotheses | not read in full: statement read; agrees with our earlier independent check | consistent with run 2 A:unordered-stack; char 3 inertia S_4 (P^1(F_3)) is right |
| 1 | `A6-ordinary-counterexample` | Refuted | not read in full: statement read |  |
| 1 | `A6-kummer` | Proved | not read in full: statement read |  |
| 1 | `A6-graphic` | Known | not read in full: statement read |  |
| 1 | `A6-normal-kummer` | Known | not read in full: statement read |  |
| 1 | `A6-anabelian` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A6-procyclic` | Refuted | not read in full: statement read |  |
| 1 | `A6-cyclotomic-detection` | Known | not read in full: statement read |  |
| 1 | `A6-three-classes` | Refuted | not read in full: statement read |  |
| 1 | `A6-blowup` | Proved | not read in full: statement read |  |
| 1 | `A6-SNC-existence` | Known | not read in full: statement read |  |
| 1 | `A6-log-specialization` | Known | not read in full: statement read |  |
| 1 | `A6-canonical-compactification` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A6-matrix-presentations` | Proved | not read in full: statement read |  |
| 1 | `A6-four-punctures` | Proved | not read in full: statement read |  |
| 1 | `A6-binary-S3` | Proved | not read in full: statement read |  |
| 1 | `A6-projective-line` | Proved | not read in full: statement read |  |
| 1 | `A6-birman` | Known | not read in full: statement read |  |
| 1 | `A6-presentation-types` | Known | not read in full: statement read |  |
| 1 | `A6-model-system` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A6-model-specialization` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A6-special-fibre-counterexample` | Refuted | not read in full: statement read |  |
| 1 | `A6-tame-specialization` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `A6-frobenius-counterexample` | Refuted | not read in full: statement read |  |
| 1 | `A6-wild-counterexample` | Refuted | not read in full: statement read |  |
| 1 | `A6-node-character` | Refuted | not read in full: statement read |  |
| 1 | `A6-intrinsic-tame` | Proved | not read in full: statement read |  |
| 1 | `A7-gluing-modules` | Proved | independent re-proof (ours), agrees | sweep 3: preimage construction and multiplication by 2 |
| 1 | `A7-domain-counterexample` | Refuted | refuted (by the run); counterexample checked, confirmed | R = Z[x,y,z]/(x^2+yz-1), sigma = (x y; z -x): sigma^2 = 1, P = coker(sigma-1) has 2-dimensional fibre at (2, x-1, y, z); refutes our own sweep-3 refinement 'needs Spec k connected (e.g. a domain)' |
| 1 | `A7-PID-count` | Proved | targeted proof check, confirmed | classes = kappa^x / im R^x plus the split class; Z[(1+sqrt-11)/2] norm-Euclidean (15/16 < 1), units +-1, kappa = F_4: three non-split classes (as in sweep 3) |
| 1 | `A7-real-classification` | Known | targeted proof check, confirmed | proof read; agrees with our sweep-3 re-derivation (two families, a <-> 1/a, square {E_1, E'_1}, hexagonal {E'_3, E'_1/3}) |
| 1 | `A7-ratio-j` | Refuted | refuted (by the run); counterexample checked, confirmed | Q(2w-u)/Q(u) = 3; j(a) = j(1/a) against c log a (as sweep 2 and 3) |
| 1 | `A7-real-topology` | Proved | independent re-proof (ours), agrees | sweep 3: 2y in Z (two circles), y in Z (one); H^1 = Z/2 and 0 |
| 1 | `thm:B1a-betti` | Proved | independent re-proof (ours), agrees | re-derived today: hard Lefschetz H^2 = H^6 and Lefschetz (1,1) make the Lefschetz components of algebraic classes in H^4 algebraic; Hodge index and Hodge-Riemann give definiteness on each orthogonal piece; so num = hom for 2-cycles on fourfolds over C (classical; Kleiman 1994) |
| 1 | `lem:B-basechange-num` | Proved | not read in full: statement read |  |
| 1 | `thm:B1a-etale` | Proved | not read in full: statement read | follows from thm:B1a-betti (re-proved) by comparison |
| 1 | `prop:B1b-criterion` | Proved | not read in full: statement read |  |
| 1 | `prop:B1b-gap` | Proved | not read in full: statement read |  |
| 1 | `thm:B1b-abelian` | Known | not read in full: statement read |  |
| 1 | `prop:B1b-scope` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `thm:B1c` | Refuted | not read in full: statement read; agrees with our earlier independent check | consistent with his margin 'Reponse negative Griffiths' |
| 1 | `lem:B2-mumford` | Proved | not read in full: statement read |  |
| 1 | `thm:B2-square` | Refuted | independent re-proof of the construction (ours), agrees; nonvanishing carried as background (Mumford 1968, Bloch 1980) | D = pr1*(p-q) + pr2*(p'-q') is algebraically trivial, D^2 = 2 (p-q)x(p'-q') is Albanese-trivial; its nonvanishing is the Mumford-Bloch input |
| 1 | `prop:B2-kernel` | Proved | not read in full: statement read |  |
| 1 | `thm:B3-21` | Proved | not read in full: statement read | affine statement; Gabber 1994, Theorem 1 (the run opened p. 326) |
| 1 | `thm:B3-fujiwara` | Known | not read in full: statement read |  |
| 1 | `thm:B3-flat-crys` | Known | not read in full: statement read |  |
| 1 | `thm:B3-approx` | Known | not read in full: statement read |  |
| 1 | `thm:B3-topos` | Known | not read in full: statement read |  |
| 1 | `thm:B3-raynaud-flatness` | Known | not read in full: statement read |  |
| 1 | `thm:B3-picard` | Known | not read in full: statement read |  |
| 1 | `thm:B3-descent` | Known | not read in full: statement read |  |
| 1 | `thm:B3-tannaka` | Known | not read in full: statement read |  |
| 1 | `thm:B3-motives` | Known | not read in full: statement read |  |
| 1 | `thm:B3-flat-duality` | Known | not read in full: statement read |  |
| 1 | `thm:B3-analytic-duality` | Known | not read in full: statement read |  |
| 1 | `thm:B3-neron` | Known | not read in full: statement read |  |
| 1 | `thm:B3-nonneutral` | Known | not read in full: statement read |  |
| 1 | `thm:B3-rosenlicht` | Known | not read in full: statement read |  |
| 1 | `thm:B3-pprimary` | Refuted | not read in full: statement read |  |
| 1 | `thm:B3-trace` | Known | not read in full: statement read |  |
| 1 | `thm:B3-index` | Known | not read in full: statement read |  |
| 1 | `thm:B3-operators` | Known | not read in full: statement read |  |
| 1 | `thm:B3-arithmetic-duality` | Known | not read in full: statement read |  |
| 1 | `thm:B3-positive-cones` | Known | not read in full: statement read |  |
| 1 | `thm:B3-abelian-duality` | Known | not read in full: statement read |  |
| 1 | `thm:B3-specialization` | Refuted | not read in full: statement read |  |
| 1 | `thm:B3-homogeneous` | Known | not read in full: statement read |  |
| 1 | `thm:B3-adeles` | Known | not read in full: statement read |  |
| 1 | `thm:B3-dmodule` | Known | not read in full: statement read |  |
| 1 | `thm:B3-riemann-roch` | Known | not read in full: statement read |  |
| 1 | `thm:B3-stacks` | Known | not read in full: statement read |  |
| 1 | `thm:B3-artinian` | Known | not read in full: statement read |  |
| 1 | `thm:B3-holomorphic-lefschetz` | Known | not read in full: statement read |  |
| 1 | `thm:B3-homotopy` | Known | not read in full: statement read |  |
| 1 | `thm:B3-chow-pullback` | Known | not read in full: statement read |  |
| 1 | `thm:B3-resolution` | Known | not read in full: statement read |  |
| 1 | `thm:B3-purity` | Known | not read in full: statement read |  |
| 1 | `thm:B3-regular-bc` | Known | not read in full: statement read |  |
| 1 | `thm:B3-local-biduality` | Known | not read in full: statement read |  |
| 1 | `thm:B3-finiteness` | Known | not read in full: statement read |  |
| 1 | `thm:B3-affine-cd` | Known | not read in full: statement read |  |
| 1 | `thm:B3-grauert` | Known | not read in full: statement read |  |
| 1 | `thm:B3-rigid` | Known | not read in full: statement read |  |
| 1 | `thm:B3-sga2` | Refuted | not read in full: statement read |  |
| 1 | `B1b-correspondence` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `B1b-blowup` | Proved | not read in full: statement read |  |
| 1 | `B1b-fermat` | Proved | not read in full: statement read |  |
| 1 | `C-exp-log` | Proved | not read in full: statement read |  |
| 1 | `C-filtered` | Proved | not read in full: statement read |  |
| 1 | `C-differential` | Proved | not read in full: statement read |  |
| 1 | `C-other-autos` | Refuted | not read in full: statement read |  |
| 1 | `C-intertwine` | Proved | not read in full: statement read |  |
| 1 | `C-functor-criterion` | Proved | not read in full: statement read |  |
| 1 | `C-functor-counter` | Refuted | not read in full: statement read |  |
| 1 | `C-qcoh` | Known | not read in full: statement read |  |
| 1 | `C-rearrangement` | Proved | not read in full: statement read |  |
| 1 | `C-chain-true` | Proved | not read in full: statement read |  |
| 1 | `C-K-counter` | Refuted | not read in full: statement read |  |
| 1 | `C-K-replacement` | Proved | not read in full: statement read |  |
| 1 | `C-literal-class` | Proved under stated hypotheses | not read in full: statement read |  |
| 1 | `C-extension` | Proved | not read in full: statement read |  |
| 1 | `C-symmetry` | Proved | not read in full: statement read |  |
| 1 | `C-packed-asymmetry` | Refuted | not read in full: statement read |  |
| 2 | `A:shadowdef` | Proved | not read in full: statement read |  |
| 2 | `A:tensor` | Proved | not read in full: statement read; agrees with our earlier independent check | same as run 1 A1-tensor |
| 2 | `A:koebe` | Known | not read in full: statement read; agrees with our earlier independent check | same as run 1 A1-cap-bound |
| 2 | `A:04` | Refuted | not read in full: statement read; agrees with our earlier independent check | same refutation as run 1 A1-global-refutation (checked): image 0 < /q/ < 16 |
| 2 | `A:alltypes` | Proved | not read in full: statement read |  |
| 2 | `A:arbitrarycuts` | Proved under stated hypotheses | not read in full: statement read |  |
| 2 | `A:fullcaps` | Proved | not read in full: statement read |  |
| 2 | `A:graph-radius-domain` | Proved | not read in full: statement read; agrees with our earlier independent check | same structure as run 1 A1-graph-range (reduction checked) |
| 2 | `A:graph-pi-one` | Proved | not read in full: statement read |  |
| 2 | `A:04-exact-image` | Proved | not read in full: statement read | the image 0 < /q/ < 16 follows from the cap radii r(l) in (0,4) of C(l,0,0) and all twists |
| 2 | `A:bordered-radius-algorithm` | Proved | not read in full: statement read |  |
| 2 | `A:plumbing` | Known | not read in full: statement read |  |
| 2 | `A:cap-plumbing-equation` | Proved | not read in full: statement read |  |
| 2 | `A:plumbing-sources` | Known | not read in full: statement read |  |
| 2 | `A:EarleMarden-local` | Known | not read in full: statement read |  |
| 2 | `A:hinich-explicit` | Refuted | not read in full: statement read |  |
| 2 | `A:single-cap-all-lengths` | Proved | targeted proof check, confirmed | grafting projective structure, Q = {w,z} + ((1+lambda^2)/2)(w'/w)^2; if D_i = D'_i with lambda_i != lambda'_i the holonomy lies in the normalizer of {0, inf}, against the non-virtually-abelian Fuchsian holonomy; then Q = Q' and the double-pole coefficients give all lengths |
| 2 | `A:single-cap-with-cusps` | Proved | not read in full: statement read | extension of A:single-cap-all-lengths (checked) to cusps |
| 2 | `A:MDB-forgetting-admissibility` | Refuted | not read in full: statement read |  |
| 2 | `A:pants-cap-dependence` | Refuted | not read in full: statement read; agrees with our earlier independent check | same conclusion as run 1 A2-independence (checked) |
| 2 | `A:grafting` | Known | not read in full: statement read |  |
| 2 | `C:A2b-regularity` | Known | not read in full: statement read |  |
| 2 | `C:A2b-energy` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-injectivity` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-support` | Known | not read in full: statement read |  |
| 2 | `C:A2b-support-integral` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-gap` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-collar` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-image` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-normal-families` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-strebel-limit` | Proved | not read in full: statement read |  |
| 2 | `C:A2b-pants-extremes` | Proved | not read in full: statement read; agrees with our earlier independent check | same as run 1 A2-explicit-limits (checked computations) |
| 2 | `A:cuspnorm` | Proved | not read in full: statement read; agrees with our earlier independent check | same as run 1 A2-cusp-norm |
| 2 | `A:collar` | Proved | not read in full: statement read |  |
| 2 | `C:A2e-nonmonotonicity` | Proved | not read in full: statement read |  |
| 2 | `A:welding` | Known | not read in full: statement read |  |
| 2 | `A:slit` | Proved | not read in full: statement read |  |
| 2 | `A:fold` | Proved | not read in full: statement read |  |
| 2 | `A:L5` | Proved under stated hypotheses | not read in full: statement read |  |
| 2 | `A:orange` | Refuted | targeted proof check, confirmed | proof read: the same extremal-length argument and constants as our sweep-3 re-derivation |
| 2 | `A:action` | Proved | not read in full: statement read |  |
| 2 | `A:octahedron` | Proved | independent re-proof (ours), agrees | sweep 2 and 3 |
| 2 | `A:octahedron-certificate` | Refuted | independent re-proof (ours), agrees | sweep 2 (char 5, P^1(F_5), five Klein groups) |
| 2 | `A:fourpoint-groupoid` | Proved | independent re-proof (ours), agrees | sweep 3 |
| 2 | `A:unordered-stack` | Proved | not read in full: statement read; agrees with our earlier independent check | same as run 1 A5-moduli |
| 2 | `A:inertia-maximality` | Refuted | not read in full: statement read |  |
| 2 | `A:three-types` | Proved | not read in full: statement read |  |
| 2 | `A:ordinary-nodal-loss` | Proved | not read in full: statement read |  |
| 2 | `A:log-graphicity` | Known | not read in full: statement read |  |
| 2 | `A:tensor-log-comparison` | Proved | not read in full: statement read |  |
| 2 | `A:Kummer-faithfulness` | Proved | not read in full: statement read |  |
| 2 | `A:tangential-anabelian` | Proved | not read in full: statement read |  |
| 2 | `A:nodal-q-test` | Proved | not read in full: statement read |  |
| 2 | `A:compactification-obstruction` | Proved | not read in full: statement read |  |
| 2 | `A:polystable-compactification` | Known | not read in full: statement read |  |
| 2 | `A:polycurve-coarse-compactification` | Proved | not read in full: statement read |  |
| 2 | `A:anabelian-compactification-definition` | Proved | not read in full: statement read |  |
| 2 | `A:intrinsic-anabelian-compactification` | Proved | not read in full: statement read |  |
| 2 | `A:polycurve-four-dimensional-anabelian` | Known | not read in full: statement read |  |
| 2 | `A:canonical-log-model-product` | Proved | not read in full: statement read |  |
| 2 | `A:log-specialization-higher` | Known | not read in full: statement read |  |
| 2 | `A:SL-GL-presentations` | Proved | not read in full: statement read |  |
| 2 | `A:four-puncture-MCG` | Proved | not read in full: statement read |  |
| 2 | `A:Birman` | Known | not read in full: statement read |  |
| 2 | `A:reflection-generators` | Proved | not read in full: statement read |  |
| 2 | `A:arithmetic-quilts` | Known | not read in full: statement read |  |
| 2 | `A:real-Galois-obstruction` | Proved | not read in full: statement read |  |
| 2 | `A:real-elliptic` | Proved | independent re-proof (ours), agrees | sweep 3; same as run 1 A7-real-classification |
| 2 | `A:pid-involutions` | Proved | independent re-proof (ours), agrees | sweep 3; same as run 1 A7-PID-count |
| 2 | `A:eigenmodule-correction` | Refuted | refuted (by the run); confirmed by run 1's counterexample A7-domain-counterexample, which I checked | connectedness of Spec k does not repair the 091 corollary |
| 2 | `A:real-topology` | Proved | independent re-proof (ours), agrees | sweep 3 |
| 2 | `B:betti` | Known | independent re-proof (ours), agrees | as thm:B1a-betti |
| 2 | `B:num-basechange` | Proved | not read in full: statement read |  |
| 2 | `B:charzero` | Proved | independent re-proof (ours) of the Betti case, agrees; the l-adic transfer read at statement level | num = hom for 2-cycles on fourfolds over any field of char 0 |
| 2 | `B:integral` | Proved | not read in full: statement read |  |
| 2 | `B:ancona-scope` | Refuted | not read in full: statement read |  |
| 2 | `B:abelian` | Known | not read in full: statement read |  |
| 2 | `B:criterion` | Proved | not read in full: statement read |  |
| 2 | `B:tau` | Refuted | not read in full: statement read; agrees with our earlier independent check | same construction as run 1 thm:B1c (Griffiths/Clemens input) |
| 2 | `B:trace` | Proved | not read in full: statement read |  |
| 2 | `B:square` | Refuted | independent re-proof of the construction (ours), agrees; nonvanishing carried as background | as thm:B2-square |
| 2 | `B:alb-kernel` | Proved | not read in full: statement read; agrees with our earlier independent check | as run 1 prop:B2-kernel |
| 2 | `B:henselian` | Known | not read in full: statement read; agrees with our earlier independent check | affine case: same as run 1 thm:B3-21 (Gabber 1994, Theorem 1) |
| 2 | `B:henselian-general` | Known | not read in full: statement read |  |
| 2 | `B:H1-gate` | Proved | not read in full: statement read |  |
| 2 | `C:torsion-degree-two-reduction` | Known | not read in full: statement read |  |
| 2 | `C:henselian-flat-trait-proper` | Proved | not read in full: statement read |  |
| 2 | `C:henselian-trait-comparison` | Proved | not read in full: statement read |  |
| 2 | `C:henselian-proper-closed-fibre` | Known | not read in full: statement read |  |
| 2 | `B:henselian-local-flat-proper` | Proved | not read in full: statement read |  |
| 2 | `C:local-curve-avoidance` | Proved | not read in full: statement read |  |
| 2 | `C:henselian-horizontal-proper` | Proved | not read in full: statement read |  |
| 2 | `C:henselian-noetherian-pair-comparison` | Proved | not read in full: statement read |  |
| 2 | `C:henselian-noetherian-closedpoint-criterion` | Proved | not read in full: statement read |  |
| 2 | `C:Nagata-input` | Proved | not read in full: statement read |  |
| 2 | `C:Goldman-branches` | Proved | not read in full: statement read |  |
| 2 | `C:subject21-torsion-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `C:henselian-affine-closed-fibre` | Known | not read in full: statement read |  |
| 2 | `B:henselized-affine-cover` | Proved | not read in full: statement read |  |
| 2 | `B:henselized-Cech-obstruction` | Refuted | not read in full: statement read |  |
| 2 | `B:constant-integer-rigidity` | Refuted | not read in full: statement read |  |
| 2 | `B:H0-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `B:nontorsion-rigidity` | Refuted | not read in full: statement read |  |
| 2 | `B:Fujiwara` | Known | not read in full: statement read |  |
| 2 | `B:specialization` | Refuted | not read in full: statement read |  |
| 2 | `B:p-Euler` | Refuted | not read in full: statement read |  |
| 2 | `B:subject1` | Known | not read in full: statement read |  |
| 2 | `B:subject2` | Known | not read in full: statement read |  |
| 2 | `B:subject3` | Known | not read in full: statement read |  |
| 2 | `B:subject4` | Known | not read in full: statement read |  |
| 2 | `B:subject5` | Proved | not read in full: statement read |  |
| 2 | `B:subject6` | Known | not read in full: statement read |  |
| 2 | `B:subject7` | Known | not read in full: statement read |  |
| 2 | `B:subject8` | Known | not read in full: statement read |  |
| 2 | `B:subject9` | Known | not read in full: statement read |  |
| 2 | `B:subject10` | Known | not read in full: statement read |  |
| 2 | `B:subject11` | Known | not read in full: statement read |  |
| 2 | `C:piecewise-graph-category` | Proved | not read in full: statement read |  |
| 2 | `C:piecewise-group-fullness` | Proved | not read in full: statement read |  |
| 2 | `C:piecewise-group-algebraization` | Proved | not read in full: statement read |  |
| 2 | `C:absolute-flat-piecewise` | Proved | not read in full: statement read |  |
| 2 | `C:absolute-flat-group-algebraization` | Proved | not read in full: statement read |  |
| 2 | `B:finite-Greenberg-piecewise` | Proved under stated hypotheses | not read in full: statement read |  |
| 2 | `B:uniform-partition-obstruction` | Refuted | not read in full: statement read |  |
| 2 | `B:finite-cover-partition-obstruction` | Refuted | not read in full: statement read |  |
| 2 | `B:complete-Greenberg-points` | Known | not read in full: statement read |  |
| 2 | `B:Witt-localization-witness` | Proved under stated hypotheses | not read in full: statement read |  |
| 2 | `B:perfect-Greenberg-cohomology` | Known | not read in full: statement read |  |
| 2 | `B:subject12` | Known | not read in full: statement read |  |
| 2 | `B:subject13` | Known | not read in full: statement read |  |
| 2 | `B:strong-approximation` | Known | not read in full: statement read |  |
| 2 | `B:nonlinear-Artin` | Refuted | not read in full: statement read |  |
| 2 | `B:subject14` | Known | not read in full: statement read |  |
| 2 | `B:pointless` | Refuted | not read in full: statement read |  |
| 2 | `B:Boolean-localization` | Known | not read in full: statement read |  |
| 2 | `B:subject15` | Known | not read in full: statement read |  |
| 2 | `B:Lie-comparison-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `B:Lie-comparison-integral-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `B:integral-affinization` | Known | not read in full: statement read |  |
| 2 | `B:unipotent-homotopy` | Known | not read in full: statement read |  |
| 2 | `B:formal-homotopy` | Known | not read in full: statement read |  |
| 2 | `B:subject16` | Refuted | not read in full: statement read |  |
| 2 | `B:nori-finite-flat` | Known | not read in full: statement read |  |
| 2 | `B:nori-base-change-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `B:Picard-general` | Known | not read in full: statement read |  |
| 2 | `B:subject17` | Known | not read in full: statement read |  |
| 2 | `B:Picard-double-fibre` | Refuted | not read in full: statement read |  |
| 2 | `B:subject18` | Known | not read in full: statement read |  |
| 2 | `B:descent-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `B:descent-criterion` | Proved | not read in full: statement read |  |
| 2 | `B:subject19` | Known | not read in full: statement read |  |
| 2 | `B:subject20` | Known | not read in full: statement read |  |
| 2 | `B:subject21` | Known | not read in full: statement read |  |
| 2 | `B:subject22` | Known | not read in full: statement read |  |
| 2 | `B:super` | Refuted | not read in full: statement read |  |
| 2 | `B:subject23` | Known | not read in full: statement read |  |
| 2 | `B:regular-pullback` | Proved | not read in full: statement read |  |
| 2 | `B:subject24` | Refuted | not read in full: statement read |  |
| 2 | `B:subject25` | Refuted | not read in full: statement read |  |
| 2 | `B:subject26` | Known | not read in full: statement read |  |
| 2 | `B:subject27` | Known | not read in full: statement read |  |
| 2 | `B:subject28` | Known | not read in full: statement read |  |
| 2 | `B:PM1` | Known | not read in full: statement read |  |
| 2 | `B:PM2` | Known | not read in full: statement read |  |
| 2 | `B:PM3` | Known | not read in full: statement read |  |
| 2 | `B:PM4` | Known | not read in full: statement read |  |
| 2 | `B:PM5` | Known | not read in full: statement read |  |
| 2 | `B:PM6` | Known | not read in full: statement read |  |
| 2 | `B:PM7` | Known | not read in full: statement read |  |
| 2 | `B:PM8` | Known | not read in full: statement read |  |
| 2 | `B:PM9` | Known | not read in full: statement read |  |
| 2 | `B:local-Hurewicz` | Refuted | not read in full: statement read |  |
| 2 | `C:explog` | Proved | not read in full: statement read |  |
| 2 | `C:unipotent` | Proved | not read in full: statement read |  |
| 2 | `C:filtered` | Proved | not read in full: statement read |  |
| 2 | `C:differential` | Proved | not read in full: statement read |  |
| 2 | `C:conormal` | Proved | not read in full: statement read |  |
| 2 | `C:squarezero` | Proved | not read in full: statement read |  |
| 2 | `C:counterexamples` | Refuted | not read in full: statement read |  |
| 2 | `C:intertwine` | Proved | not read in full: statement read |  |
| 2 | `C:proof-correction` | Proved | not read in full: statement read |  |
| 2 | `C:module-actions` | Proved | not read in full: statement read |  |
| 2 | `C:functor-criterion` | Proved | not read in full: statement read |  |
| 2 | `C:functor-counterexamples` | Refuted | not read in full: statement read |  |
| 2 | `C:functor-basechange` | Proved | not read in full: statement read |  |
| 2 | `C:functor-separate-obstructions` | Proved | not read in full: statement read |  |
| 2 | `C:sheaf-globalization` | Proved | not read in full: statement read |  |
| 2 | `C:majorization` | Proved | not read in full: statement read |  |
| 2 | `C:pretasse-cones` | Proved | not read in full: statement read |  |
| 2 | `C:K-counterexample` | Refuted | not read in full: statement read |  |
| 2 | `C:K-repair` | Proved | not read in full: statement read |  |
| 2 | `C:group-classification` | Proved under stated hypotheses | not read in full: statement read |  |
| 2 | `C:integer-system` | Proved | not read in full: statement read |  |
| 2 | `C:C3-coverage-obstruction` | Proved | not read in full: statement read |  |
| 2 | `C:classification-scope` | Proved | not read in full: statement read |  |
| 2 | `C:symmetry` | Refuted | not read in full: statement read |  |
| 2 | `C:graded-determinant-sign` | Proved | not read in full: statement read |  |
| 2 | `C:determinant-ordinary-basechange` | Refuted | not read in full: statement read |  |
| 2 | `C:determinant-basechange-repair` | Proved | not read in full: statement read |  |
| 2 | `C:determinant-trace-splitting` | Proved | not read in full: statement read |  |
| 2 | `C:determinant-incidence` | Proved | not read in full: statement read |  |
| 2 | `U:henselian-comparison` | Open | not read in full: statement read |  |
