# SA22: research packages, in concept (sweep 3)

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. These are concepts only; no prompt is written tonight.
Each gives the question, why it matters, what it rests on, the strongest known reduction, and the material a run would
need.

## R22-1. The fates of the 28 thesis problems of 1964 (a literature run)

- **Question:**
  - For each of the 28 subjects on 66/002–005, and each item of the "Pour mémoire" diagram, who settled it, where (exact
    locators), and what remains open.
  - Settle in particular subjects 21 (Gabber, Fujiwara?), 25 (the "pb du carré") and 24 (second question).
- **Why:** a primary document of the SGA programme in 1964, annotated by him around 1968–71. It belongs in Part V of
  the handbook and in the history of the fonds. The answers are scattered across forty years of literature.
- **Rests on:** SA22-0, H66-01 (four sheets).
- **Strongest known reduction:** the from-memory list in STUDY.md §1: Gabber 1994 and Fujiwara 1995; Saavedra 1972;
  Deligne 1990; Parshin 1976 and Beilinson 1980; Fulton 1984; Griffiths 1969; Mumford 1968; Artin–Mazur 1969;
  Raynaud's Néron and Picard work.
- **Material:**
  - the transcription and the four scan images;
  - the SGA 4, 4½, 5 and 6 indexes (our French-school corpus);
  - Raynaud's thesis (1970);
  - Bloch's *Lectures on algebraic cycles*;
  - Gabber's and Fujiwara's papers.

## R22-2. The conformal-surgery programme of 1984: capping, admissible discs, and the stable-curve maps of section 6

This is one cluster, so the welding correction goes into this package and not into a run of its own.

- **Question:**
  - (a) Is the (0,3) claim of 067/068, marked "?", true: in an admissibly capped pair of pants, does each disc depend
    only on its own boundary length ℓ_i? Settle it by an explicit computation with hyperbolic pants.
  - (b) The "Conjecture" of 068–069 cannot hold as stated: the shadows are bounded (Koebe's quarter theorem; Michel
    Hua's project), and the letter withdraws it (019). Determine the image of (D_i) ↦ (o(D_i)) and whether the map is
    injective: is an admissible disc system determined by its radii, and what is the shape of the set of admissible
    radii (Lavrentiev's inequality suggests it is not a box)? Restated 19 Nov, after reader 67_003-046_084-101.
  - (c) Compare that bundle and its section with:
    - Penner's decorated Teichmüller space;
    - the cusp norms on the T_{X,a_i} (H22-6);
    - the g = 0 case he found strange.
  - (d) The maps of section 6, MDB_{g,ν} → M_stND_{g,ν} and MD_{g,ν} → M_stN_{g,ν} (074–082): are they isomorphisms?
    Compare with the plumbing constructions of the Deligne–Mumford compactification (Kra 1990, Earle–Marden, Wolpert,
    Hubbard–Koch 2014; from memory). Settle his key case (0,4) first, as the pages do.
  - (e) Write the welding statements of 059–061 and 071–073 in their correct form: quasisymmetric gluing for existence,
    removable seams for uniqueness.
- **Why:**
  - It is his own programme of January–April 1984, the analytic side of the Teichmüller tower in the Esquisse.
  - The letter to Bers shows he wanted it answered.
  - The answers decide whether the pages are an early form of plumbing and decorated coordinates or a different
    construction.
- **Rests on:** SA22-3, SA22-6, SA22-7, SA22-8; 067/016–021, 053–083; CORRECTIONS.tsv (the welding rows); H22-6, H22-7.
- **Strongest known reduction:**
  - Admissible capping is well defined: glue each unit disc along the arclength parametrization of the geodesic
    boundary.
  - So (b) is a fibre-by-fibre existence-and-uniqueness problem over T_{g,ν}.
  - (a) is its (0,3) instance.
- **Material:**
  - the transcriptions MPL_67_002-052 and MPL_67_053-101, with their notes and doubts files, and scans 016–021 and
    053–083;
  - Penner's decorated Teichmüller paper; Kra's horocyclic coordinates; Hubbard–Koch;
  - Lehto–Virtanen, ch. III.

## R22-3. The anabelian sheets of 15 January 1984 (067/048–051)

If the La Longue Marche anabelian packages already hold this question, merge it into them; one prompt per cluster.

- **Question:**
  - (a) Map 049 a), b) and c) and the NB of 048 onto the literature: what is proved, where, and what is open.
    - a): the anabelian conjecture for singular stable curves with a normal propagator.
    - b): recovering nodes and marks from the cyclotomically acted Ẑ-subgroups.
    - c): the anabelian compactification and its behaviour under specialization.
  - (b) Check the presentations of 050–051 (T⁺_{0,4}, T⁺!_{0,4} ≅ SL(2, Z)/±1, the Birman sequence) and his
    expectation of three kinds of presentation (pants, Lego, involutions) against the known presentations of the
    mapping class groups.
- **Why:**
  - A dated statement of the anabelian programme for stable curves, written in the weeks of the Esquisse.
  - The sheets connect the welding notes to La Longue Marche.
- **Rests on:** SA22-5; 067/048–051; H22-8; SA28, SA31-7, SA31-9.
- **Strongest known reduction:**
  - The SL(2, Z) and GL(2, Z) presentations on 050 are checked (CHECK_EVENTS).
  - The rest is from memory: Nakamura; Ihara–Nakamura 1997; Mochizuki 2006; Hoshi–Mochizuki 2011.
- **Material:**
  - MPL_67_002-052, with notes and doubts, and scans 048–051;
  - the La Longue Marche transcriptions of the same months;
  - the papers named, as arXiv sources where they exist.

## R22-4. Rearrangement inequalities for convolution on groups (68/015–022)

- **Question:**
  - (a) Do the axioms a)–d) of 68/017 imply Condition K (021) for the convolution-stable family they span? Equivalently,
    do f′ ≺ f, g′ ≺ g imply f′ ∗ g′ ≺ f ∗ g for the arranged functions?
  - (b) Which finite and discrete groups carry a system satisfying the axioms: cyclic groups, ℤ, and which others? Is
    the 2-torsion extension G̃ → G with kernel ₂G forced?
  - (c) Settle his symmetry doubt on 020 in general. The S₃ example settles one instance.
- **Why:**
  - His own open question on these sheets.
  - It sits between Hardy–Littlewood's rearrangement theorem and the discrete Riesz–Sobolev inequalities.
  - Finite, checkable cases exist, so computation can test it.
- **Rests on:** SA22-2; 68/015–022; H22-9; the notes R08–R12.
- **Strongest known reduction:**
  - The model case on 017 is checked: symmetric intervals are closed under convolution with nonnegative coefficients.
  - 022 reduces the general claim to a common point of the level sets of all A_i ∗ B_j.
- **Material:**
  - MPL_66+68_002-032, with notes, doubts and records/convolution_examples.json, and scans 015–022;
  - Hardy–Littlewood–Pólya ch. X; Gabriel (1932);
  - a computer search over small groups.

## Cote 67, scans 003-046 and 084-101 (reader 67_003-046_084-101: af3526fc4890c92f1, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader `67_003-046_084-101` for ae4ae3dc, 19 Nov 2026. Concepts only; no prompt is
written. Each gives the question, why it matters, what it rests on, the strongest known reduction, and the material a
run would need.


### R22-67_003-046_084-101-1. Capping pants: the questions of the letter to Bers (merge into R22-2)

This belongs to the cluster of R22-2 (the 1984 capping programme). It goes into that prompt, not a prompt of its own
(one prompt per cluster). What it adds to R22-2:

- **Question.**
  - (a) The limit shape: for C(L, 0, 0), does the cap D₀ tend to Σ ∖ [1, +∞] as L → ∞ (H22-67_003-046_084-101-1)?
    Describe D₀ for all (ℓ₀, 0, 0).
  - (b) The radii: the image of (ℓ₀, ℓ₁, ℓ_∞) ↦ (r₀, r₁, r_∞) in the coordinate metrics of (ℙ¹; 0, 1, ∞). Is the map
    injective, i.e. is an admissible system determined by its radii (his expectation, 019)? Is the image a box (his
    expectation; H22-67_003-046_084-101-2 says no)?
  - (c) Does D_i depend on all three lengths (his doubt, 020; the "?" on 068; H22-67_003-046_084-101-3)?
  - (d) The collar question of 021: the hyperbolic metric of X′ = X minus an open boundary collar, against that of X.
    He asks for an explicit formula in the multipliers λ_i.
- **Why.**
  - The letter of 15.4.1984 is his own question to Bers, and the answers decide the shape of the retraction
    M̃B → M̃ he was after.
  - The January Conjecture (068–069) and the orange-slice model (019–020) are both refuted as stated:
    - the conjecture by the boundedness of the shadows (Michel Hua's project, §VIII; Koebe);
    - the model by extremal length (Michel Hua's project; Pro's C03).
  - What replaces them is open.
- **Rests on:**
  - SA22-3 (016–022), SA22-6 (062–069);
  - CORRECTIONS of this reading (the orange-slice model, the January conjecture);
  - CHECK_EVENTS (the Koebe bound, the extremal-length refutation).
- **Strongest known reduction.**
  - The shadows are bounded: r₀ < 4 in the coordinate z.
  - The configuration of C(ℓ₀, 0, 0) has the Klein-four symmetry generated by conjugation and the reflection in
    |z − 1| = 1, so D₀ ∩ ℝ = (−b/(1 − b), b).
  - Ext(∂D₀) ≥ ℓ₀²/2π.
  - Lavrentiev's inequality couples the radii (from memory).
  - The cap is the conformal welding of the unit disc and the cusped pants along hyperbolic arclength, so every question
    is a welding computation.
- **Material.**
  - The transcription MPL_67_002-052 (016–021) with notes N14–N24 and the records research_checks.md (C03);
  - scan 022 (the carbon);
  - Michel Hua's project, §§III and VIII (credited);
  - a conformal-welding solver: the zipper algorithm, or the Schwarz–Christoffel toolbox applied to the double, a sphere
    with four cusps and a reflection;
  - for (d), the collar lemma and the hyperbolic metric of an annulus (from memory). Numerical evidence first (b and c
    are finite-dimensional), then proofs.

### R22-67_003-046_084-101-2. Locators for the edition's notes on 024–046 and 091–101 (merge with R22-1 into one SA22 literature run)

- **Question.** Exact locators for the classical results his sheets rederive, so that the edition cites them:
  - Klein surfaces and the double: Alling–Greenleaf, LNM 219 (1971);
  - real elliptic curves: Alling (1981); Silhol;
  - ℤ[C₂]-lattices: Diederichsen; Reiner;
  - the canonical metrics on maps in the Esquisse d'un programme;
  - Lavrentiev's inequality and Koebe's quarter theorem for the notes to the letter.

  For each sheet, say what is classical and what, if anything, is not.
- **Why.** The dossier and the real-curve sheets are correct and classical. An edition must say where the results stand
  in the literature and must not present them as new. The NB on maps (039) may matter for the history of the Esquisse
  (H22-67_003-046_084-101-4).
- **Rests on:** SA22-4, SA22-9; CHECK_EVENTS of this reading.
- **Strongest known reduction:** all statements are re-derived here; only the locators are missing.
- **Material:** the transcription MPL_67_002-052 (024–046) and MPL_67_053-101 (091–101); the books and papers named, as
  LaTeX sources where they exist (arXiv for the modern ones), otherwise PDF.

### R22-67_003-046_084-101-3. The octahedral M_{0,4} over ℤ[½, i] (merge into the La Longue Marche four-point package if one exists)

- **Question.**
  - Write the Theorem of 089 over schemes: the groupoid of four-pointed ℙ¹ over S/ℤ[½, i] as a V-gerbe over the quotient
    of ℙ¹ ∖ {3 points} by 𝔖₃, with the twisted model X(I) and the orientation torsor {±i}.
  - Check it at the primes 3 and 5, where the Proposition of 086 and the ramification picture change.
  - Compare it with the octahedral cover of the Fermat conic and the level-four model of La Longue Marche.
- **Why.**
  - It is his canonical form of the basic piece of the Teichmüller tower, written in the weeks of the Esquisse.
  - It connects cote 67 to La Longue Marche (Pro's O15) and to the four-point model of cote 146.
- **Rests on:** SA22-8; H22-67_003-046_084-101-6; sweep 2's report char5_67_086.md; Pro's notes O01–O16.
- **Strongest known reduction:**
  - over algebraically closed fields of characteristic ≠ 2 the Theorem is re-derived here;
  - the characteristic-5 exception of the Proposition is proved (sweep 2), and the characteristic-3 picture is computed
    (Pro's O08).
- **Material:** MPL_67_053-101 (084–089) with notes O01–O16; LM_140-2 (scans 363, 549–571); the cote-146 four-point
  pages (SA30-2).
