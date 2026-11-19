# SA22, Autour de l'enseignement (cotes 66, 67, 68, with 162-1 and 162-6): sweep 3 study

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026, from about 22:25 UTC. The transcriptions are read in
full, in the order of `sweep2/SA22/WHAT_IS_WHERE.md`.

**State of the sections** (19 Nov 2026):

| Section | Cotes and scans | Items | Read by | State |
|---|---|---|---|---|
| 1 | 66/002-005 | SA22-0 | ae4ae3dc | done |
| 2 | 67/002 (title sheet), 048-083, and the rest through the notes | SA22-5, -6, -7 | ae4ae3dc | done; corrected after wave 2 |
| 3 | 67/003-046, 084-101 | SA22-13, -3, -4, -8, -9 | af3526fc4890c92f1 (reader 67_003-046_084-101) | done |
| 4 | 68/002-056 | SA22-1, -2, -10, -11, -12 | ae4ae3dc; the images by a8afd9e2a259051c4 (reader 122_125) | done |
| - | 162-1, 162-6 | - | - | not transcribed by us |

All readers are Claude Opus 5.5 at effort max.

**Changed after wave 2:**
- The capping "Conjecture" of 67/068-069 cannot hold as stated: the shadows are bounded (Koebe), and the letter to Bers
  withdraws it (019). H22-6 and R22-2 (b) are restated.
- The letter's "orange-slice" model is false as stated: an extremal-length argument from Michel Hua's project.
- The Theorem of 67/089 holds in every characteristic other than 2, characteristic 5 included. The Proposition of 086
  still fails exactly in characteristic 5.
- The dependence between SA22-4 and SA22-9 runs the other way: 028 uses the real-curve sheets.
- The words of cote 68 are decided on the images: "prétassé(s)", "tassé(s)", "en gardant", "et si n'existe de".

**Personal data:** the 1979 staff list 68/018 is being redacted by the GitHub housekeeper (19 Nov), and 67/012-013 carry
a name and an address on envelopes. These files describe such documents in one line and reproduce no name, address, vote
or date of birth.

**The brief** (the main session, Claude Opus 5.5 at effort max, 18 Nov ~22:2x UTC):

> Sweep 3: read every transcribed page in full, look at the scan image wherever the reading is in doubt, work through the
> mathematics of each item (what he defines, constructs or claims; what the page proves; re-derive the steps that carry
> it, each re-derivation a check event; what is wrong, with the correction; what is open, with the strongest reduction on
> the page), close the dependencies by reading, write down every hunch with its grounds, sketch research packages
> (question, why it matters, what it rests on, the strongest known reduction, the material a run would need), and say per
> cote and scan range which passes the transcription has had, which readings are open, and whether the stretch is ready to
> be edited and translated. Known results are cited with exact locators, not proved again.

## Sources and conventions

- **Literature citations:** where I name a later result from memory, it says "from memory" and is listed in
  RESEARCH_PACKAGES.md for checking against the paper. None of them was opened tonight unless said.
- **Scan readings:** a reading decided on the scan image says so.

---

## 1. Cote 66: "Travaux de thèses" (1964), four sheets (SA22-0)

- **Transcription and notes:** `inputs/SA22/codex/H66-01_transcription.tex` (Codex web) and `H66-01_notes.md`.
- **Read in full**, scans 2–5.

### What the sheets are

A numbered list of 28 thesis subjects.
- Scan 2: the title "Travaux de thèses" and the year 1964 in a three-sided frame.
- Scan 2: his remark "Numéros cerclés sont sans doute difficiles" (the circled numbers are no doubt difficult).
- Scan 2, margin: his classification by theme:

| Theme | Subjects |
|---|---|
| Essentially cohomological | 1–10, 20, 21, 26–28 |
| Intersection theory | 10, 19, 23, 24, 25 |
| Néron theory | 11–13 |
| Topos theory | 14, 15, 22 |
| The "yoga de représentabilité" of functors | 17, 18 |

- The circled, "difficult" subjects are 2, 3, 4, 7, 8, 9, 10, 11, 13, 15, 16, 18, 19, 20, 21, 24, 25 and 28.
- Several of these also carry a small × or * (10, 19, 23, 24, 25).
- Later marginal notes record what became of some subjects (see "The margins" below).

### The 28 subjects, in today's terms

The cohomological block:

| No. | His subject | In today's terms |
|---|---|---|
| 1 | fppf topology and cohomology | the general formalism; an inserted "relation with crystalline cohomology" |
| 2 | duality, local and global | "subordonné à 1), 11)" |
| 3 | the p-primary part of the Ogg–Shafarevich formula | "subordonné à 2)" |
| 4 | Riemann–Roch in étale cohomology with discrete coefficients | the relation with higher Artin representations; the χ formula for étale covers of a proper scheme |
| 5 | the χ formula for abelian varieties with a ring of operators | a variant of Ogg–Shafarevich |
| 6 | explicit Lefschetz formulas | discrete étale or "continuous" coherent coefficients; Artin representations from the coherent side |
| 7 | the cohomology of schemes of finite type over Z | "satisfactory" global duality theorems "improving Artin" |
| 8 | a duality formalism from complexes of differential operators | coefficients with an integrable connection; an inserted "link with 'cristaux'" |
| 9 | analytic duality | |
| 10 | Riemann–Roch for pseudo-coherent sheaves | analytic or algebraic; "cf SGA 6" |

The Néron and topos blocks:

| No. | His subject | In today's terms |
|---|---|---|
| 11 | the category of "schémas morcelés" | Néron's functor over a discrete valuation ring |
| 12 | Néron models, refinements and extensions | |
| 13 | asymptotic theorems for Greenberg functors | over a complete or henselian noetherian local ring |
| 14 | the structure of topoi | the existence of fibre functors; representable stacks |
| 15 | the homotopy type of a topos | π_i with "noyaux infinitésimaux", Hurewicz theorems, exact homotopy sequences, comparison theorems |
| 16 | a "true" fundamental group | the specialization of the fundamental group for a family of curves (cancelled) |
| 17 | separation of functors, and when Pic_{X/S} is representable | X of relative dimension 1 (cancelled) |
| 18 | passage to the quotient in the Artinian case | the effectivity of flat descent data |

The later subjects:

| No. | His subject | In today's terms |
|---|---|---|
| 19 | ampleness for cycles of any dimension | |
| 20 | vanishing theorems | the case of homogeneous spaces |
| 21 | étale cohomology along a closed subscheme | see the next paragraph |
| 22 | abelian categories with a ± rigid tensor product | linear representations of proalgebraic groups and of gerbes; "a preliminary to the theory of motives" |
| 23 | Chow theory of regular schemes with an ample invertible sheaf | the pullback f: X′ → Y should be defined when Y alone is regular |
| 24 | a 1-cycle numerically equivalent to 0 on a smooth projective threefold | is it τ-equivalent to 0? and, on a fourfold, is numerical = homological equivalence for 2-cycles? |
| 25 | two products of algebraically trivial cycles | is the product of two algebraically trivial cycles rationally trivial ("pb du carré")? is an Albanese-trivial 0-cycle on a surface rationally trivial? |
| 26 | relative Rosenlicht theory | over an arbitrary base |
| 27 | adèles of schemes of any dimension | local Jacobians |
| 28 | an abstract theory of motives | over preschemes of finite type over Z, by a general categorical construction |

Subject 21 in full: for X₀ closed in X and étale cohomology, when is H*(X, F) → H*(X₀, F₀) an isomorphism? Does it
suffice to know it in degree 0? The case X = Spec A with A I-adic, separated and complete; and étale localization along
X₀ ⊂ X with X affine.

**"Pour mémoire"** (scan 4) is a diagram:
- **What it starts from:** resolution of singularities (⊗), cohomological purity (⊗), and regular base change
  ("régu?lier") in cohomology.
- **What it should give:** local duality = biduality for the étale topology, and finiteness theorems for morphisms of
  finite type.
- **What follows it:** the cohomological dimension of affine morphisms, finiteness theorems "genre Grauert" (⊗), and
  rigid-analytic theories (⊗). Then "Questions dans SGA 1961|1962".

### The margins

These are his later notes; I checked them against the transcription in sweep 1.

| Subject | Margin |
|---|---|
| 12 | "commencé par Raynaud" |
| 13 | "S'impose moins depuis les résultats d'approximation d'Artin" |
| 15 | "fait partiellement par Mazur-Artin. Réflexions de Quillen en train" |
| 16 | "contre-exemple de Artin, situation peu engageante" |
| 17 | "résolu par Raynaud" |
| 22 | "travail Saavedra en train" |
| 24 | "Réponse négative Griffiths pour question 1°" |
| 25 | "faux, cf Mumford" (beside the 0-cycle question) |

The latest work they cite is from about 1968–1971: Artin–Mazur's étale homotopy (1969), Griffiths (1969), Mumford's
0-cycles (1968), and Saavedra's thesis (1972). So the margins date from those years (my inference).

### What became of the subjects

All from memory. These are hypotheses for the literature package R22-1, not checked tonight.

| No. | Later development |
|---|---|
| 21 | The affine analogue of proper base change: for a henselian pair (A, I) and a torsion étale sheaf, H*(Spec A, F) ≅ H*(Spec A/I, F). Gabber (1994) and Fujiwara (1995). His case "A I-adic, separated and complete" is a henselian pair. |
| 22 | Saavedra, *Catégories tannakiennes* (LNM 265, 1972); Deligne–Milne (LNM 900, 1982); Deligne, "Catégories tannakiennes" (Grothendieck Festschrift II, 1990). |
| 27 | Parshin's adèles for surfaces (1976) and Beilinson's in general (1980). |
| 28 | Motives over a base: Voevodsky, Ayoub, Cisinski–Déglise. |
| 15 | Artin–Mazur, *Étale homotopy* (LNM 100, 1969), and Friedlander. The "π_i with infinitesimal kernels" points at infinitesimal or crystalline homotopy types, later schematic homotopy types (Toën). |
| 23 | Refined Gysin maps (Fulton, *Intersection theory*, 1984, chapter 8). |
| 24, first question | Answered negatively, as his margin says (Griffiths 1969). |
| 24, second question | Numerical against homological equivalence for 2-cycles on fourfolds is the first open case of the standard conjecture D. It is still open in general. |
| 25, second question | False by Mumford (1968), as his margin says. |
| 25, first question ("pb du carré") | Not settled here; see HUNCHES.md, H22-3. |
| "Pour mémoire" | Purity (Gabber), finiteness for finite-type morphisms (Deligne, SGA 4½, "Th. finitude", and Gabber), affine Lefschetz (Gabber), rigid geometry (Raynaud, Berkovich, Huber). |

### What is proved, checked, wrong, open

| | |
|---|---|
| Proved on the page | nothing (it is a list of problems) |
| Checked | the margins against the transcription (sweep 1). The theme classification in the N.B. matches the numbers. |
| Wrong | nothing on the page |
| Open | subject 24, second question (standard conjecture D for 2-cycles on fourfolds); subject 25, first question as stated |

### Connections

- **Within SA22:** none.
- **Elsewhere:**
  - SA20-17 (the Tannakian duality of cotes 153 and 155) and SA20-W3 (filtrations of the forgetful functor, cote 123)
    take up subject 22.
  - The topos and motive subjects (14, 15, 22, 28) lead to the Pursuing Stacks and motives topics.

### The transcription

- **Passes:** one Codex web transcription (H66-01) with its notes on the sheets. The margins were checked against it in
  sweep 1.
- **Uncertain readings:** about 45 \unsure marks, mostly accents and abbreviations ("Théorémes", "algébriqmt") and
  alternative singular/plural forms.
- **Ready for an edition** after one ink pass on the \unsure marks. It is short (four sheets) and important for the
  history of the SGA era: a good first deliverable.

---

## 2. Cote 67: "Chirurgie des surfaces conformes" (1976–78, and Dec 1983 – Apr 1984)

**Read in full:** 053–083 (the 1984 welding notes) and 048–051 (the anabelian sheets).
**Checked on the scan images:** 002, 014, 048, 054, 086, 091, 098 (sweep 2).
**Known through the Pro notes and research leads, which I read in full in sweep 2, part 1:** 003–046 and 084–101. Their
transcriptions were not reread page by page tonight; DELIVERABLES.tsv says so.

### 2.1 The 1976–78 layer (SA22-13, SA22-3)

- **The title sheet** "Chirurgie des surfaces conformes I" is dated "(1976 ou 77 ?)" (read on the image). Whose hand
  wrote the date is not decided (reader 67_003-046_084-101).
- **The surgery operations (003–007):** découpage, recollage, rétrécissage, élargissage and panachage on collars. The
  pages then turn to moduli by rigidification and a piecewise-homographic gluing, with Euler-characteristic counts.
- **The envelopes (009–014).** One is metered at Nagoya University on 20.12.77. They describe an elliptic curve as
  C*/λ^ℤ with a multiplier, a primitive class and an oriented closed geodesic, and the trace condition: |λ| ≠ 1 iff
  α ∉ [−2, 2] (checked).
- **The letter to Lipman Bers** ("Les Aumettes 15.4.1984"; 016–021) belongs to the second layer by date but continues
  this surgery. Its content:
  - an enlarged Teichmüller space in which boundary circles may collapse to marked points;
  - the expected intrinsic action of (R⁺)^I;
  - admissible discs;
  - a tentative "orange-slice" model, with direct questions to Bers. The model is false as stated, by an
    extremal-length argument from Michel Hua's project (reader 67_003-046_084-101).

### 2.2 The 1983–84 layer

**The canonical metrics (024–046, SA22-4; undated, on computer paper; known through the notes).**
- "Métriques canoniques sur surfaces conformes".
- The exceptional surfaces, and canonical metrics: hyperbolic by descent from H; flat of area 1; spherical on the real
  projective plane, from a free antiholomorphic involution.
- An invariant spherical metric under a compact group H, obtained by averaging a positive Hermitian form.
- The summary proposition "En résumé et sauf erreur": the invariant metric is unique iff X^H = ∅.
- Bordered surfaces through their double, with geodesic boundary.

**The anabelian sheets (048–051, SA22-5).**
- **The date.** 048 is dated "15. 1."; 049 and 051 are on printout paper of a CRAY 2 job of 16 AUG 82, with "DERNIERE
  MISE A JOUR DE JOURNAL : 11-08-82". So the sheets are from 15 January 1983 or later. Their vocabulary, "conjecture
  fondamentale en géom. alg. anabélienne", is that of the letter to Faltings (June 1983). So 15.1.1984 (my inference).
- **048:**
  - For X smooth of type (g, ν) over Q̄ and Y stable, not smooth, with a "propagateur normal" N, a Teichmüller
    isomorphism gives an isomorphism of outer fundamental groups. With base points it gives an isomorphism of groups.
  - The outer isomorphism "n'est pas compatible avec les actions ext. de Gal(Q̄/K)" for K large.
  - The NB asks for three conjugacy classes of homomorphisms Ẑ(1) → π₁(X).
- **049, "À examiner":**
  - a) extend the fundamental anabelian conjecture to singular stable curves with a normal propagator;
  - b) recover Sing(Y) ∪ the marked points from the classes of subgroups ≅ Ẑ that are invariant under π₁(K), which
    acts on them through the cyclotomic character;
  - c) "s'inspirant des compactifications MD des M_{g,ν}, définir ce que c'est qu'une compactification anabélienne
    d'une variété lisse anabélienne … Comportement par spécialisation ???".
- **050, "Je m'attends à trouver trois types de présentations":**
  - by pants (triades);
  - by a complete Lego box of pieces with deformation paths;
  - by involutions.
  - Examples: T⁺_{1,1} ≅ SL(2, Z) = ⟨ρ, σ | ρ³ = σ², ρ⁶ = 1⟩, and T_{1,1} ≅ GL(2, Z) generated by three reflections with
    (r₁r₂)² = (r₂r₃)³ and (r₁r₂)⁴ = 1.
  - Checked: the SL₂ presentation is the standard one with σ = S and ρ = ST. In the GL₂ one, z = (r₁r₂)² is central
    with z² = 1, as it must be (−1).
- **051:**
  - T⁺!_{0,4} ≅ Π_{0,3}, the sequence 1 → Π_{0,3} → T⁺_{0,4} → 𝔖̃₄ → 1, and T⁺!_{0,4} ≅ SL(2, Z)/±1;
  - SL(2, Z)/Borel ≅ P¹(Q);
  - the Birman sequence 1 → Π_{g,ν−1} → T_{g,ν} → T_{g,ν−1} → 1.
- **Where this belongs:** the Lego and Teichmüller-tower material of La Longue Marche and of the Esquisse (January
  1984), here on the welding pages of the same weeks.

**The welding notes ("Chirurgie conforme", 053–083, SA22-6 and SA22-7; dated 11 or 16.1.84, 12.1, 13.1).**

*Théorème 1 (054–056).* The conformal structure of a bordered surface is determined by its interior.
- The proof: the boundary charts are exactly the topological open embeddings U → H̄, boundary to boundary, that are
  conformal inside (Schwarz reflection).
- Then a power series a_n zⁿ must have n = 1, because a half-disc has to go into H̄: the angle π becomes nπ.
- Re-derived (CHECK_EVENTS).
- **A slip of wording:** the general reflection lemma on 055 has "hol." struck out, so as written it reads "toute
  fonction continue complexe … réelle sur U ∩ R est holomorphe". It needs "holomorphe dans U ∩ H".

*Théorème 2 (bracketed).* Compact bordered conformal surfaces ≅ smooth proper real algebraic curves. This is the
classical correspondence for Klein surfaces (Alling–Greenleaf, LNM 219, 1971; from memory).

*Théorème 3 and Lemma 2 (056–058).* Cutting along a topological 1-complex K gives a bordered conformal surface.
- He asks "rectifiabilité suffit ?".
- My reasoning: no regularity is needed for cutting. One-sided boundary charts exist for any Jordan arc, by Riemann
  mapping and Carathéodory's extension (prime ends).
- The Scholie on 058 (two real-analytic structures on K, one from each bank) is right.

*Théorème 4 (059–061), the welding equivalence.* Pairs (X, K, S) correspond to (X̃, S̃, σ) with σ an involution of the
cut boundary, "assez régulier (rectifiable suffit)".
- Lemma 3 c) (061, dated 12.1): a continuous function holomorphic off a rectifiable curve is holomorphic. This is
  right: rectifiable curves are removable (Painlevé, Besicovitch; from memory). It gives the uniqueness of the welded
  structure.
- **Existence is the issue.**
  - Not every homeomorphism of an arc is a conformal welding.
  - "Rectifiable" is not the right condition for a homeomorphism of an interval: every monotone one has a rectifiable
    graph, as the research lead on 073 notes.
  - The right condition is quasisymmetry (Pfluger 1960; Lehto–Virtanen; from memory). For the smooth gluings he uses
    from 074 on ("avec la condition différentiable"), welding exists and is unique.
- **Correction (CORRECTIONS.tsv):** in Th. 4 and in the Scholie of 073, read "quasisymmetric" (or "smooth") for
  "rectifiable". The map from rectifiable slits to homeomorphisms is injective, by removability, but not onto all
  homeomorphisms.

*Lemma 4 (071–074): uniformization by the slit disc.* NB 1, uniqueness through the simply transitive action of Aut(𝔻)
on positively ordered triples, is right. The Scholie a)–d) holds with "quasisymmetric" for "rectifiable".

*The capping (061–070).*
- A projective structure on a boundary circle corresponds to capping it with a disc.
- The choice of a centre corresponds to a toric structure, and gives the inclusion D ⊂ T_{X′,a} and the "ombre" o(D),
  a Euclidean disc in the tangent line.
- **Admissible disc systems:** those where the toric structures from D_i and from the canonical metric of X* = X − ∪D_i°
  (geodesic boundary in the hyperbolic case) agree.
- The bordered Teichmüller space TB_{g,ν} ≅ C^{3g−3+ν} × R^ν maps to T_{g,ν} by capping. He presumes this is the
  projection; it rests on the (0,3) claim marked "?" on 068: "each disc depends only on its own length ℓ_i".
- **"Conjecture"** (068–069): for a punctured surface, at least in the hyperbolic case, (D_i) ↦ (o(D_i)) is a bijection
  from admissible disc systems to systems of Euclidean discs. That would give a principal (R*⁺)^I-bundle
  TB_{g,I} → T_{g,I} with a canonical section, and canonical Euclidean metrics on the T_{X,a_i}.
- **Corrected after wave 2:** the Conjecture cannot hold as stated.
  - By Koebe's quarter theorem the shadows are bounded (Michel Hua's project, §VIII; re-derived by reader
    67_003-046_084-101).
  - The letter to Bers withdraws it (019).
  - What stays open is the image of (D_i) ↦ (o(D_i)) and whether that map is injective.
- He finds g = 0 "étrange" (no canonical metric on X). But a punctured sphere with ν ≥ 3 has its complete hyperbolic
  metric, whose cusp coordinates give canonical Euclidean structures on the tangent lines at the punctures (my
  reasoning; HUNCHES H22-6).

*Section 6 (074–082, dated 13.1).*
- Cutting along C and capping canonically gives the normalization of a Mumford–Deligne stable curve X‴. Each node
  carries an element of T_{x₁} ⊗ T_{x₂}: today's plumbing (smoothing) parameter.
- This defines morphisms MDB_{g,ν} → M_stND_{g,ν} (real-analytic) and MD_{g,ν} → M_stN_{g,ν} (algebraic), with the
  right dimensions (checked).
- "Question: ces flèches sont-elles des iso ?" The inverse would glue polar pairs of discs. His own heuristic for
  independence is "tout à fait vaseux … (c'est probablement tout à fait faux !)".
- The key case is (0,4): gluing two Thurston pants with lengths and a twist. Next steps: the map on fundamental groups,
  and étaleness through the tangent map.
- **Open on the page.** The questions are those that plumbing and horocyclic coordinates later answered (Kra 1990;
  Earle–Marden; Wolpert; from memory). See HUNCHES H22-6, R22-2.

**"Moduli M0,4 et l'octaèdre" (084–089, SA22-8).** The Proposition on 086 is stated for characteristic ≠ 2. It fails
exactly in characteristic 5 (sweep 2: image, computation for p ≤ 29, argument). Its V-torsors and the canonical
octahedron (085–089): the Theorem of 089 holds in every characteristic other than 2, characteristic 5 included (reader
67_003-046_084-101).

**"Courbes elliptiques réelles", Déc 83 (091–101, SA22-9).**
- Real structures on elliptic curves through lattices with an involution.
- The two types E_a and E′_a; the dihedral groups D_n (n = 2, 4, 6); two real forms for each real j.
- His own presumption (095) is withdrawn and replaced by a classification (097–098).
- The hexagonal ratio on 098 is his slip, √3 for 3 (image and computation).
- The topology of the real locus and H¹(R, E) are computed on 101.

### 2.3 Dependencies (closed by reading; DEPENDS.tsv)

| Item | Uses | Shown on |
|---|---|---|
| SA22-6 | SA22-3, the surgery principle | 070: "5. Retour sur le principe de chirurgie conforme" |
| SA22-6 | SA22-4, the canonical metric | 065: "il y a sur X* … une métrique canonique" |
| SA22-7 | SA22-6 | 074–082 cut along C and cap with the welding of 053–073 |
| SA22-8 | SA22-7, the (0,4) case | 080: "Le cas-clef … (g,ν) = (0,4)"; then 084 "Moduli M0,4" |
| SA22-5 | the anabelian conjecture of the letter to Faltings | 049: "la conjecture fondamentale" |
| SA22-5 | the MD compactifications | 049 |
| SA22-9 | SA22-4 | the notation E_a^! on 028 and 101 |

---

## 3. Cote 67, scans 003-046 and 084-101 (reader 67_003-046_084-101: af3526fc4890c92f1, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader `67_003-046_084-101` for ae4ae3dc, 19 Nov 2026. These parts were known
before only through the Pro notes; they are now read in full, with the readings in doubt looked at on the scan images.
The full working is in `67_003-046_084-101.md`. Literature named from memory says so.

---

### The 1976–78 layer (SA22-13, SA22-3)

**The title sheet (002).**
- The title "Chirurgie des surfaces conformes I" is in his fine pen. The date "1976 ou 77 ?)" is in a darker, heavier
  pen.
- Michel Hua's project attributes the date to the archivist. On the image, its "1" is unflagged like his own, while the
  archive's pencil numbers on the same sheet and on 013 have a flagged 1. Not decided.
- The only printed date of these sheets is the Nagoya meter stamp of 20.12.77 on 014.

**The surgery programme (003–007).**
- The operations: cutting along a rectifiable 1-complex; regluing by an "admissible" relation; removing, adding or
  exchanging boundary collars (rétrécissage, élargissage, panachage).
- The cut complex K̃ (006), and rigidification of S ⊂ K ⊂ X by an isotopy class.
- A count of real moduli, N = Σ_{faces not discs} (6g(f) + 4ν(f) − 6): the bordered Teichmüller dimension plus one
  rotation per boundary circle.
- Checked:
  - the Euler identity 2 − 2g = Σ(2 − 2g(f) − ν(f)) + 1 − λ, with λ the first Betti number of K;
  - his comparison N − (3g − 3) = Σ(3g(f) + 5/2·ν(f) − 3) + 3/2·(μ + 1 − λ). It fixes the uncertain readings.
- Wrong:
  - an intermediate line has 3/2 for ½ (image);
  - his "≥ 0 ?" fails when every face is a disc (N = 0, and the difference is 3(1 − g) < 0);
  - "g(f) = 0 tjrs" in genus 1 needs K not inside a disc (Michel Hua's project gives the same counterexample);
  - "composantes de deg 0, 1" (005) must mean genus 0, 1.
- Open:
  - "homographiques" or "horocycliques" (007): looked at on the image, not decided.

**The envelopes (009–014): a genus-one dictionary.** The data are equivalent:
- an elliptic curve with a closed geodesic class;
- a real subtorus;
- a primitive lattice element;
- ℂ*/b^ℤ with |b| ≠ 1;
- a loxodromic automorphism of a projective line;
- a discrete non-unipotent ℤ ⊂ PGL₂.

There are two-element sets of orientations, generators, trivializations, fixed points and Borels. The trace criterion
|λ| ≠ 1 ⇔ α ∉ [−2, 2] is on 014. All re-derived; nothing wrong. It is the Tate-curve description of a marked elliptic
curve.
- 013 carries a third person's sender address and 012 a name; they are for the user's decision.
- 008 is a printed estate-agency list (no personal names), reused as paper.

**The letter to Lipman Bers, 15.4.1984 (016–021; 022 is a carbon of 021, not blank).**
- What it asks:
  - the relation between the algebraic Teichmüller space and Thurston's bordered one;
  - an intrinsic retraction by capping;
  - admissible disc systems and their radii;
  - and, for pants, the "orange-slice" model, asking Bers whether it holds "or is definitely false".
- Checked:
  - dim TB = 6g − 6 + 3ν;
  - "a homotopy equivalence" is too broad for a rigidification. It must keep orientation and peripheral classes. Pro's
    witness φ(a) = ab, φ(b) = b, after Michel Hua's project, was re-derived.
- **The orange-slice model is false as stated.** The extremal-length argument is Michel Hua's project's; Pro gives
  explicit numbers.
  - With cusps at 1 and ∞, the model puts the cap D₀ inside the cell Q₀ = {|z| ≤ 1, Re z ≤ ½}.
  - Then the annulus 4/3 < |z + ½| < 7/5 lies in the pants, and the extremal length of the boundary class is
    ≤ 2π/log(21/20) ≈ 128.8.
  - The hyperbolic metric gives ≥ L²/2π, ≈ 163 for L = 32.
  - Re-derived.
- **The January Conjecture (068–069) cannot hold as stated.** It asks for a bijection from admissible systems onto all
  systems of Euclidean discs.
  - Koebe's quarter theorem bounds the shadows: r(D₀, 0) < 4 in the coordinate of (ℙ¹; 0, 1, ∞).
  - This is Michel Hua's project's footnote to §VIII; re-derived.
  - The letter's revision to bounded radii r_i < ρ_i (019) is his own withdrawal.
  - R22-2 (b) and H22-6 should be restated: the questions are the image and the injectivity, not the bijection.
- Open (H22-67_003-046_084-101-1 to -3):
  - Is an admissible system determined by its radii? My hunch: the set of radii is not the box he expects, because
    Lavrentiev's inequality r₀r₁ ≤ 1 couples them (from memory).
  - Does each disc depend on all three lengths? Probably yes, as his own doubt on 020 suggests.
  - My hunch for the limit as ℓ₀ → ∞ with two cusps: the cap tends to Koebe's slit domain Σ ∖ [1, +∞].
  - The collar question of 021.

### The metric dossier "Métriques canoniques sur surfaces conformes" (024–046, SA22-4)

**Reading order.** His sheets 1–18 are on 027–044, with two inserts 1′, 2′ on 045–046. The text joins give the order
027, 045, 028, 046, 029–044, as Michel Hua's project proposed. The edition should print it so.

**What he does.**
- 025: equivalent data on a conformal sphere (antipode and inversion; round metric and great circle; toric structure on
  a circle; poles and an orbit).
- 026: H¹(⟨σ⟩, E) ≅ H²(σ, Π) ≅ Π^σ/(1 + σ)Π, with "H²" read on the image. It is 0 for the rhombic lattice and ℤ/2 for
  the rectangular one.
- 027 and 045: hyperbolicity, by five equivalent conditions and three corollaries.
- 045 and 028: the non-hyperbolic surfaces without boundary: ℙ¹, ℂ, ℂ*, elliptic curves, ℝP², the open Möbius band,
  and the Klein bottles E_a^!.
- 046 and 029–031: their canonical metrics.
- 031–039: the sphere with a compact group H. Proposition (037): an H-invariant normalized round metric exists, and it
  is unique iff X^H = ∅; the cases with fixed points are listed. The Récapitulation (038–039) adds R(X) ≅ hyperbolic
  3-space.
- 039: an NB on maps.
- 040–044: bordered surfaces through the double. The exceptions are ℂ, the half-plane, ℙ¹ and the disc.

**Checked.** Everything re-derived:
- his "à vérifier" (033) is confirmed: for H⁺ ≠ 1 the invariant forms are the diagonal ones;
- his margin "C'est l'inverse!" (034) is right: az̄ inverts the rotation torus, b/z̄ commutes with it;
- the extensions split as he finds;
- the Proposition holds case by case;
- the classification of the non-hyperbolic surfaces is complete.

**Wrong.** Slips only:
- card(X ∖ X′) for card(X′ ∖ X) in Corollary 3 (045, ink checked);
- "rev. universels" for the orientation covering of the punctured ℝP² (028);
- 037 a) lacks "invariante par H".

The readings "2g + ν ≥ 3" (027), "2g − 2 + ν ≥ 1" (040) and "carte" (039) were decided on the images.

**What stands out.** The NB on 039: a map on the sphere with no facet fixed by its automorphism group carries a unique
invariant round metric. I re-derived it: a finite group fixing a facet has a fixed point in it. This is the canonical
metric of a map; H22-67_003-046_084-101-4 relates it to the cartes of the Esquisse (from memory). The dossier as a whole
is classical uniformization, organized for capping: the letter uses its geodesic-boundary metric of 041.

### "Moduli M0,4 et l'octaèdre" (084–089, SA22-8)

**What he does.**
- The Klein group V(I) of a 4-set I acts on the projective line through I. Its six fixed points form an octahedron. Its
  normalizer Γ ≅ 𝔖₄ acts on the four pairs of antipodal faces, which form a V-torsor I(V).
- An orientation of the octahedron is a choice of √−1.
- Proposition (086): a 1–1 correspondence V ↔ Γ ↔ S.
- Twisting by torsors (088): X/V ≅ Z(J), the line of the three bipartitions.
- **Théorème (089):** the groupoid of (X, I ↪ X) is equivalent to that of pairs (I, ζ ∈ Z(J)*).

**Checked.** The normalizer: iz and (z + 1)/(z − 1) give 𝔖₃, with kernel V. The splittings are four S₃'s, simply
transitive under V. The orientation is canonically {±√−1}. The quotient is q = z² + z⁻². The Theorem is right on objects
and automorphisms (generic V, D₄, A₄). **The Theorem holds in every characteristic ≠ 2, 5 included**: it never uses
the failed part of the Proposition.

**Wrong.**
- The Proposition in characteristic 5 (sweep 2). The (X, S) form of the margin corollary fails there too; the repair is
  to keep the antipodal pairing (Pro).
- "Pour un tel triplet" (085): a single face has stabilizer C₃. The splitting is the stabilizer S₃ of a pair of
  antipodal faces (Pro and Michel Hua's project, re-derived).
- "droite projective [réelle]" over an algebraically closed field (086): a slip or a misreading.

**Open.** The canonical model X(I) is asserted, and his attempt on 087 is struck. It exists by twisting the standard
model by Isom(I, I₀) (my reading).

### "Courbes elliptiques réelles", Déc 83 – 9.2. (091–101, SA22-9)

"9.2." is in the margin of 101 (image): presumably 9 February 1984.

**What he does.**
- 091–092, 100: involutions of 2-regular modules over any ring, classified by triples (P, Q, m).
- 093: real elliptic curves as lattices with an orientation-reversing involution. There are two types: E_a, with
  Q = x² + ay² on ℤe₊ ⊕ ℤe₋, and E′_a, on the index-2 overlattice. Real automorphisms are ±1 only.
- 094–098: the real structures on a given curve. They exist iff j is real, and G ≅ D_n has two classes of
  reflections. His presumption of 095 (one E_a and one E′_a) is withdrawn on 097–098: outside the square both are of
  the same type with parameters a and 1/a, and the square gives E₁ and E′₁.
- 099: τ = i√a, (1 + i√a)/2; the real loci (two circles for E_a, one for E′_a).
- 101: H¹(ℝ, E_a) = ℤ/2 and H¹(ℝ, E′_a) = 0, so the only genus-one real curves without real points are the E_a^!.
  Their quotients are the Klein bottles.

**Checked.** All re-derived. The full picture is classical (Alling, *Real elliptic curves*, 1981; from memory):
- E_a covers j ∈ [1728, ∞);
- E′_a covers j ∈ (−∞, 1728], with j = 0 at a = 3;
- a and 1/a are the two real forms of one complex curve.

The module classification over ℤ is that of ℤ[C₂]-lattices (from memory).

**Wrong.**
- The hexagonal √3 for 3 (098; sweep 2).
- "j = c·log a ?" (097): no, since j(a) = j(1/a); in fact j(i√a) ≈ e^{2π√a}.
- The Cor of 091 needs Spec k connected (k = ℚ × ℚ fails).
- The two-class count of 100 needs his struck proviso k^× → (k/2k)^× onto. ℤ[(1 + √−11)/2] has three non-split
  classes (Pro, re-derived).
- 101's struck "sans [bord]" must stand: the torsors give Klein bottles.

**Readings decided on the images.**
- "inhomogènes", not "intrinsèques" (101; with Michel Hua's project);
- "Ker(id + σ)" (091, + over −);
- "l'ens des sommets" (100, by the sense).

### Dependencies (closed by reading)

| Item | Relation | Other | Shown on |
|---|---|---|---|
| SA22-3 (letter) | uses | SA22-4 (041) | 016, 018, 020: the hyperbolic metric with geodesic boundary, "existence and unicity"; the same object as 041, uncited |
| SA22-3 (letter) | uses and revises | SA22-6 (062–069) | 018: admissibility and the shadow as on 062–065; 019 withdraws the bijection of the Conjecture of 068–069 |
| SA22-3 (003–007, letter) | related, not used | SA22-13 | neither cites the envelopes; 007's genus-one line is a count (replaces "uses, our reading") |
| SA22-3 (005) | related, not used | SA22-4 (044) | 005's "disques non ponctués: pas de métrique nat const." is answered on 044 (a metric per interior point) |
| SA22-4 (028) | uses | SA22-9 (093, 101) | 028 quotes the E_a^! of 101 in the notation of 093 (turns round the sweep-2 row "SA22-9 uses SA22-4") |
| SA22-9 | related, not used | SA22-13 | lattices with involution, not the multiplicative picture (replaces "uses, our reading") |
| SA22-8 | motivated by, does not use | SA22-7 (080) | 080 names (0,4) the key case; 084–089 use no welding or plumbing |
| SA22-8 | related | SA22-5 (051) | the 𝔖₄ ⊃ V picture of T⁺_{0,4} → 𝔖̃₄ |

### The transcription

- **Passes.** One Pro pass (GPT-6 Astra, ChatGPT Pro mode), with notes and doubts. Read in full in sweep 3, with 17
  places looked at on the images.
- **Open readings.**
  - the hand of the date (002);
  - "homographiques|horocycliques" (007);
  - "1′|19" (045);
  - "[réelle]" (086);
  - "[¼|4]" (097);
  - the second "inhomogènes" (101).
- **Ready for an edition and translation after one ink pass:** 002–007, 009–014, 024–046 (in the reading order),
  084–089, 091–101. The letter (016–021) is ready after a light pass.
- **For the user's decision:**
  - 008, a printed list by others;
  - 012 and 013, personal data;
  - 022, the uncatalogued carbon.
- **Languages** (DELIVERABLES, with reasons):
  - en first; ja and es for the surgery, the dossier and the octahedron;
  - es for the real curves;
  - the letter is in English already.

---

## 4. Cote 68: games, rearrangements, exponentials, orientations (undated; some sheets after 1979)

**Read in full tonight:** MPL_66+68_002-032 (68/002–032) and MPL_68_033-056+162-1+162-6 (68/033–056).
- Despite its name, the second package transcribes only cote 68. Cotes 162-1 and 162-6 appear in its notes as context
  from Hua's readings and are not transcribed in it (DELIVERABLES.tsv).

**Dating.** No mathematical sheet carries a date.
- 68/018 is the typed list "PROPOSITIONS RELATIVES A L'AVANCEMENT POUR L'ANNEE 1979" of the Université des Sciences et
  Techniques du Languedoc. The rearrangement sheets around it are therefore of 1979 or later, if they belong together.
- 68/051, 053 and 055 are three revised copies of the typed page "XVIII Les épousailles (2)": paired words of the
  yin-and-yang kind, one copy numbered 82 by hand. The orientation notes 050, 052 and 054 are written on the same run of
  paper.
- The typed text is not identified tonight. Éloge de l'Inceste (1979) is a candidate (from memory); the notes record
  Hua's suggestion of Récoltes et Semailles.
- **Privacy.** 018 gives the names and dates of birth of seventeen staff members. An edition should describe the sheet
  rather than reproduce the table; that is for the user to decide.

### 4.1 Positional games (SA22-1): two drafts and a restart

**What he defines (002–003, again on 024–025):**
- positions C with a successor relation R, and terminal positions C₀ = {R(x) = ∅};
- players J, with the player to move α(x) for x ∉ C₀;
- for each player j, a set G₀(j) ⊂ C₀ of terminal wins;
- plays, finite or infinite; positional strategies Σ(x) ⊂ R(x), nonempty, for x ∈ C(j);
- a winning strategy for x: every compatible maximal play from x is finite and ends in G₀(j);
- G(j), the set of positions from which j has a winning strategy.

**First draft (002–014).**
- The recursion C_i = {x : R(x) ⊂ C_{i−1}} gives "every play from x has length ≤ i". C = ∪C_i is equivalent to a
  height function l with l(y) < l(x) for y ∈ R(x). If C is finite, "no infinite play" implies C = C_{N−1}.
  - Re-derived, agrees.
- **Th. 1 (004–006):**
  - The statement: for x ∈ C(j) ∖ C₀, x ∈ G(j) ⟺ R(x) ∩ G(j) ≠ ∅; for an opponent's position, x ∈ G(j) ⟺ R(x) ⊂ G(j).
  - The proof of the second "⟸" takes the greedy strategy Σ(z) = R(z) ∩ G(j) and needs the hypothesis written in the
    margin, "no infinite play". Without it the greedy strategy can loop: a j-position x with x → x and x → t ∈ G₀(j).
  - The cancelled sheet 007 tries a well-order on R(x) and stops.
- **Corollary, the largest winning strategy on a successor-stable Γ ⊂ G(j) (006, 008–009):**
  - It holds under the margin's hypothesis.
  - It fails in general: take two j-positions x ⇄ y, each with a move to t ∈ G₀(j). The union of the two winning
    strategies allows the play x, y, x, …
  - Re-derived; the notes give the same obstruction.
- **§4, acceptable strategies and Th. 2 (009–012):** x ∉ G(j′) iff the coalition J ∖ {j′} has a strategy whose
  terminated plays from x all avoid G₀(j′). He then reduces to an auxiliary two-player game: "on a fait deux fois le
  même raisonnement".
- **"? Th 3", G_∞(j) = ∪_{i∈ℕ} G_i(j) = G(j) (013).** His margin proves it under C = ∪C_i.
  - It holds more generally whenever every R(x) is finite, C finite included and infinite plays allowed: the attractor
    then closes at ω.
  - It fails in general, for an opponent's position whose successors have unbounded finite ranks. There the iteration
    must be transfinite.
  - Re-derived; the notes (G13–G17) give the finite-height reduction and the transfinite convention.
- "6. Élimination des parties circulaires (cas C fini)" (014) is a heading with nothing under it.

**Second draft, "Jeux de position" (024–034).** Plays may now be infinite, and "gagnée" means finite and ending in G₀(j).
- **The general proof.** The theorem on 026 (a: G(j) ∩ C(j) = {R(x) ∩ G(j) ≠ ∅}; b: G(j) ∩ C̄(j) = {R(x) ⊂ G(j)}) is
  proved in general.
  - In a) ⊃, a return to x₀ is excluded because x₀ would then be winning for Σ₁.
  - In b) ⊃ (027–029) he well-orders R(x₀). For each position x he takes the least y ∈ R(x₀) from which some
    Σ_y-compatible play reaches x, and plays Σ_{ε(x)}.
  - Along a play, ε is non-increasing, hence eventually constant. From then on the play follows one winning strategy
    from a position where it wins, so it is finite.
  - Re-derived; correct, with choice for the family Σ_y and the well-order (the notes say the same).
- **Admissibility theorem (029–030).** x₀ ∉ G(j) ⟺ x₀ is admissible against j ⟺ x₀ is admissible for the explicit
  strategy Σ′. Σ′ keeps the play outside G(j): at j's positions by a), at the others by b).
- **Corollary (030), for two players with G₀(j) ∩ G₀(j′) = ∅:** C = G(j) ⊔ G(j′) ⊔ N, where N is the set of positions
  drawn by infinite play or by a neutral terminal position.
  - This is positional determinacy for reachability (open) games, the Zermelo and Gale–Stewart theorem (from memory),
    proved without ordinal ranks.
  - Re-derived, agrees.
- **Alternating games (031–034).**
  - The criterion for extending α to α̂ with α̂(y) ≠ α̂(x) on moves (032) is re-derived and agrees.
  - Then x ∈ G ⟺ R(x) ∩ P ≠ ∅ and x ∈ P ⟺ R(x) ⊂ G.
  - The Proposition on 034 characterizes G and P as the unique complementary pair with 1)–4) when there is no infinite
    play: the kernel characterization (von Neumann–Morgenstern; from memory). Re-derived by well-founded induction.
- "Jeux à N joueurs" (048) restarts with circular games, a cyclic permutation ρ of the players. Definitions only.

### 4.2 Rearrangements and convolution (SA22-2, 015–022)

- **019–020, rearrangements and majorization:**
  - f′ ∼ f when f′ is a rearrangement of f (éparpillement).
  - |f, g| = sup ⟨f′, g⟩ is attained exactly when all level sets are nested: the classical rearrangement inequality.
  - Weak majorization f′ ≺ f, by three equivalent conditions (pairings with all g ≥ 0, with all finite sets, partial
    sums of decreasing rearrangements).
  - Re-derived by the layer-cake formula; agrees. His correction "d'ordre" → "de préordre" is right.
- **020–021, peak and majorization extremality on a group:**
  - "Couples prétassés" (read on the image, 19 Nov; first transcribed "priorisés"): |f, g| = ‖f ∗ g‖_∞.
  - "Couples tassés" (read on the image; first transcribed "bons"): f′ ≺ f, g′ ≺ g ⇒ f′ ∗ g′ ≺ f ∗ g.
  - "Condition K" for a convolution-stable family S.
  - He doubts symmetry in a non-commutative G. The notes confirm the doubt with S₃: 1_H ∗ 1_{Hs} against
    1_{Hs} ∗ 1_H.
- **017, the model case and its axioms:**
  - Symmetric intervals E_i = [−i, i] and F_j = [m−j, m+1+j] in a cyclic group, closed under convolution with
    nonnegative coefficients. Re-derived: a convolution of symmetric intervals is symmetric and unimodal.
  - Then axioms for a general group: G̃ → G with kernel ₂G, and totally ordered families 𝒜(g̃) of finite sets,
    symmetric up to translation by ρ(g̃), whose convolutions fall in the cones C(g̃h̃).
  - 022 begins the proof that such a system gives Condition K and stops at the need for a common point of all level
    sets.
- **Open on the page:** whether the axioms of 017 imply Condition K, and for which groups such systems exist (H22-9,
  R22-4).
- The classical cases (from memory): ℤ, Hardy–Littlewood–Pólya ch. X; cyclic groups, Gabriel 1932.

### 4.3 Exponentials in characteristic 0 (SA22-10, 036–046)

**I. Generalities (036).**
- exp: N(A) ≅ 1 + N(A), with inverse log; additive on commuting elements.
- L ≅ 1 + L for a subspace of nilpotents closed under powers.
- If L is also closed under products, 1 + L is a group, commutative iff L is.
- Example 1 holds with J only nil, because a finitely generated ideal generated by nilpotents is nilpotent.
- Example 2 needs J nilpotent, as he inserted: with J nil only, u(M) ⊂ JM does not make u nilpotent.
- The margin "exp 1 = 0" is "log 1 = 0" (the notes, after Hua).
- All re-derived.

**II. One-parameter formal groups (037–044).**
- **Th. 2 is right:** U ≅ Hom(Ḡ_a, Un(U)) and N(U) ≅ Hom(G_a, Un(U)). The coefficients satisfy n a_n = a₁ a_{n−1}.
- **On 039, for a module M,** the G_a-statement (**) is right only for M finitely generated. In general a morphism
  G_a → End(M) is Σ u_n λⁿ with finite support on each vector, not globally. Hom(G_a, Aut M) then corresponds to the
  locally nilpotent endomorphisms (the notes, after Hua).
- **040–042, (4) exp(v)f = f exp(u) ⇒ (3) vf = fu:** right, by δ = ρδ with ρ nilpotent. The coefficient is
  c_ij = −1/(i+j+1)!, not 1/(i+j)! as written (immaterial; the notes say the same).
- **042–043:** applied to the multiplication map, it gives "exp u is an algebra automorphism ⟺ u is a derivation" for
  nilpotent u. Re-derived.
- **044, globalization:**
  - "E_{Θ+Θ′} = E_Θ + E_Θ′" must read E_Θ ∘ E_Θ′ (a slip).
  - "Θ loc nilpotent" must mean nilpotent locally on X. For a locally nilpotent derivation in today's sense, such as
    d/dt on ℚ[t], exp is the translation, not the identity on X_red.
  - The question whether u ↦ ē_u and u ↦ e_u are bijective for K-functors in modules is open on the page.

**Unipotent automorphisms (045–046).**
- **Prop. 1), (i) ⟺ (ii) ⟺ (iii):** re-derived. For a ring automorphism, [u, a] = (u(a) − a)·u, so u has order ≤ n
  iff J^{n+1} = 0.
- **Part 2), with his inserted "(u − id)^{n+1} = 0":** right.
- **His "est-ce nécessaire ?"** No. On A = ℚ[x]/(x²), u(x) = 2x is a differential automorphism of order 1 that is not
  unipotent.
- **What fails as written** (Hua's example in the notes is the same):
  - the corollary on 045 listing (iv) "u = exp Θ, Θ nilpotent" among the equivalent conditions, and its bijection;
  - the first corollary on 046;
  - the margin NB "u induit l'identité sur gr_J(A)": u acts by 2 on J/J².
- **The last corollary on 046** (Θ(A) ⊂ I ⇒ Θ^{N+1} = 0, Θ^i A ⊂ I^i; exp: L_K(A, I) ≅ G_K(A, I)) fails as written.
  - Counterexample: A = ℚ[ε]/(ε³), I = (ε), Θ = ε d/dε, with Θ^k(ε) = ε for every k.
  - The repair is his own struck margin (iii′): require the filtration conditions Θ(I^k) ⊂ I^{k+1}, and u = id on
    gr_I(A). Then (u − 1)^{n+1} = 0 and the bijection holds.

### 4.4 Orientations and graded determinants (SA22-11, SA22-12; 050–056)

**Orientations (050–052).**
- Lemmas 1–2 on two-element sets and their contracted product P ∧ Q.
- An "orientation theory" is a functor Ω on real vector spaces and isomorphisms, with Ω(0) ≅ {±1} and Stokes
  bijections St_{V′}: Ω(V) → Ω(W) for a half-space V′ with boundary W, changing sign with the opposite half-space.
- **The theorem:** every morphism of theories is an isomorphism, and any two theories are uniquely isomorphic, by
  induction on the dimension.
- **Existence ("[?]" on the page):** the compatibility ε_n(u_n) = sg(λ) ε_{n−1}(u_{n−1}) forces ε₁ = sg and
  ε_n = sg ∘ det, since the only characters GL(n, ℝ) → {±1} are 1 and sg ∘ det. The standard orientation torsor with
  a fixed Stokes convention exists.
- Re-derived.

**054.** ω′ × ω = (−1)^{pq} ω × ω′. With the normal vector last, St(ω × ω′) = (−1)^q St(ω) × ω′ when the boundary lies
in the first factor, and ω × St(ω′) with no sign in the second. This agrees with his striking of (−1)^p. Re-derived.

**Graded determinants (056).**
- Axioms for a determinant functor Δ from free modules of finite type and isomorphisms to graded lines with the Koszul
  rule:
  - multiplicativity;
  - Δ(V) = V in degree 1 for rank 1;
  - independence of the complement, which he restates as "Δ(u) = id for u unipotent with respect to W₁ ⊂ V".
- These are the axioms of Knudsen–Mumford's det (1976; from memory). The conditional SK₁ point is in the notes.
- Link: H0DV (SA23-41).

### 4.5 Dependencies (closed by reading)

| Item | Relation | Other | Shown on |
|---|---|---|---|
| SA22-1 (024–034) | uses | SA22-1 (002–014) | 024 restates the definitions; 026 is Th. 1 of 004 with the general proof |
| SA22-1 | **not** used | SA22-2 | read: the rearrangement sheets lie between the drafts but share no notion with them (the sweep-2 row was our reading) |
| SA22-10 (044) | uses | SA22-10 (036–043) | E_Θ = exp Θ with Th. 1 2° for E_{Θ+Θ′} |
| SA22-10 (045–046) | uses | SA22-10 (036, 040–043) | log of 036; the corollary "u K-automorphism ⟺ Θ K-derivation" rests on 042–043 |
| SA22-12 | related, not used | SA22-11 | 056 does not cite 050–054; the orientation torsor is the sign quotient of the determinant line (H0DV) |

### 4.6 Readings decided on the images (wave 2, 19 Nov)

Reader 122_125 (a8afd9e2a259051c4, Claude Opus 5.5 at effort max) read these on the images; the details are in
`readings/68_images.md`.
- 004 reads "en gardant", not Hua's "en changeant Σ".
- The margin of 013 reads "et si n'existe de". The "et" is right against Hua's "ou", and it removes the flaw Hua found in
  his own reading.
- On 015 the three adjectives read "tassé(s)".
- On 020–022 every "priorisé" is "prétassé" and every "bon(s)" is "tassé(s)", as Hua reads them.
- "élémentaire ?" stays.
