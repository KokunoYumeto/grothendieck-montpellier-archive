# SA20, Autour d'Esquisse d'un programme: sweep 3 study

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18-19 Nov 2026, with the readers named in each section, all Claude Opus
5.5 at effort max. The sections follow the order of `sweep2/SA20/WHAT_IS_WHERE.md`.

**Scope:** all of SA20: cotes 119, 120, 121, 122, 123, 125, 152, 153 and 155. Cotes 120-121 came to this topic on 18 Nov
at about 23:1x UTC from a6d42bf6fe2b0d8a8, which is near its context cap (the main session's decision).

**State of the sections:**

| Section | Cotes and scans | Items | Read by | State |
|---|---|---|---|---|
| Cote 119 | 119/144-161, 276-281 | SA20-2 to -6 | acf08879 (reader 119_144-161_276-281) | done |
| Cotes 152 and 120 | 152/001-013, 120/001-025 | SA20-7, SA20-12 | ac69efa38b3a951d7 | done |
| Cote 121, scans 1-48 | 121/001-048 | SA20-13, -14; the prompted questions SA20-8 to -11 | wave-2 reader | running |
| Cote 121, scans 49-73; 153; 155 | 121/049-073, 153, 155 | SA20-15, -16, -17 | aff4deb18a6ec3192 | done |
| Cote 122 | 122/003-035 | SA20-18; SA20-19 | ae4ae3dc; the comparisons and image checks by a wave-2 reader | SA20-18 done; SA20-19 and the image checks running |
| Cote 123 | 123 | SA20-W1, W3, W4 | ae4ae3dc | done |
| Cote 125 | 125 | SA20-W2 | wave-2 reader | running |

**Main findings so far** (the places are in the sections):
- **119, the Additif to the Esquisse:**
  - His collar conjecture I c) is false as written: the group is a concordance (pseudo-isotopy) space, and its π₀ is
    nonzero for suitable closed manifolds (Hatcher-Wagoner). I b) falls with it.
  - II c) is Alexander's trick; his "Alexandroff ?" is Alexander.
  - So the eleven functors of the cascade ("11 foncteurs"), claimed as ∞-isotopic equivalences, hold only with
    fibrewise or rigidified collars.
  - The foliation quotient of 145-146 is the monodromy quotient.
  - The "groupe trilitaire" of 156 is AGL₂(𝔽₃), and his "ordre 10" is an index (checked by computation).
- **152 and 120:**
  - The admissibility rule of 152/004 misses nested pairs; the dictionary of 010 is the consistent one.
  - The reconstruction of a tame theory from its category (120/008, 018) needs conservativity and an image axiom.
  - Generic triviality in his finite-diagram form fails for parallel arrows.
- **121/049-073:** the gluing proof of 062 is complete; the first stage on 049 is wrong; intersections must be an axiom
  (070). None of the five axiom systems is o-minimal as written.
- **153:** the binomial and λ analysers are a one-sided form of the plethories of Tall-Wraith and Borger-Wieland.
- **155:**
  - His coproduct condition makes the dual pro-ring a bialgebroid over k′ (Takeuchi's ×_{k′}-bialgebra; new in sweep 3).
  - His question on 155/004 is answered by Deligne's theorem (1990) for rigid categories with End(1) = k.
- **122:**
  - The Milnor fibration as an open book, a self-dual triangle that carries the variation, and the cohomology of the
    Milnor fibre from the link.
  - The step H^{n-1}(M) = 0 is not on the pages.
- **123:** the letter of 22 Oct 1969 is a dated statement of the dimension formula that Douglass-Röhrle attribute to a
  conjecture of Grothendieck.

**Personal data:** the minutes of a 17 July 1984 appointment commission on a 155 verso carry personal data. So does
the 1979 staff list 68/018 (SA22). The GitHub housekeeper is redacting both (19 Nov). These files describe such
documents in one line and reproduce no name, vote or date of birth.

**The brief** (the main session, Claude Opus 5.5 at effort max, 18 Nov ~22:2x UTC):

> Read every transcribed page in full; look at the scan image wherever the reading is in doubt; work through the
> mathematics of each item (what he defines, constructs or claims; what the page proves; re-derive the steps that carry
> it, each re-derivation a check event; what is wrong, with the correction; what is open, with the strongest reduction
> on the page); close the dependencies by reading; hunches with their grounds; research packages in concept; and per cote
> and scan range, the passes the transcription has had, the open readings, and whether it is ready to be edited and
> translated.

---

## 1. Cote 119, scans 144–161 and 276–281: the Esquisse dossier's notes and the Orsay report (SA20-2 to SA20-6)

By Claude Opus 5.5 at effort max (reader 119_144-161_276-281, horizontal sweep 3), 18 Nov 2026, for ae4ae3dc. The full
working is `readings/119_144-161_276-281.md`.

**What was read:**
- In full: the Pro transcription (GPT-6 Astra, ChatGPT Pro mode) of 119/144–161 and 276–281, with its notes N01–N80 and
  its doubts. 147 and 154 are blank.
- As a witness: Michel Hua's modernised reading of the same pages.
- Scan images: 144–146, 148–151, 153, 155, 156, 158, 160, 276, 281.
- Finite group statements: checked by exhaustive computation (`_checks_fin.py`, `_checks_pgl5.py`; output in
  `_checks_out.txt`).

**The leaves:**
- 144 is a cover, "Notes de math. oubliées par Jean Malgoire", with "(15 p)": the image reads 15, the number of written
  pages under it.
- 145–146: the foliation note, dated March 1986.
- 148–153: "Additif Esquisse d'un Programme", six numbered pages.
- 155–161: "Digressions combinatoires (pour Réflexions t. 4)".
- 158: a photocopied typed sheet of his own, with paired words ("Avenir – passé, destinée – histoire, …"), draft
  footnotes for pages 98–110 of a typescript, and polyhedral sketches.
- 276–281: a report of the Orsay mathematics commission (1968). Its pages 1–5 are in a hand that is not his; page 6 is
  typed.

### The foliation quotient, "Th" (145–146; SA20-2)

**What he writes:**
- He proposes the "topos quotient" of a space E "[ou topos ?]" by a local equivalence relation R, for example a
  foliation.
- Its model quotients are "(X, G)", with G discrete acting on X and "G est le groupe fondamental d'une 'feuille'".
- He states "Th": C ≃ C′.
  - C: pairs (X, R), with R locally open and with locally connected fibres.
  - C′: triples (X, 𝒴, f), with 𝒴 a "multiplicité topologique" and f: Top(X) → 𝒴 (locally) open, "à fibres locᵗ
    connexes et connexes".
  - C′ is a 2-category with discrete Hom(ξ, η).

**Reading decided on the image:** the third condition, which Hua's reading leaves unread, is "et connexes" (the fibres
are connected).

**Checked:**
- In the suspension model, the topos of sheaves locally constant along the leaves is B_G(X). Its isotropy at a leaf is
  π₁ of that leaf (re-derived).
  - So his quotient is the **monodromy** quotient, not the holonomy one.
- The discreteness of Hom(ξ, η) follows if open surjections of topoi are of effective descent (sketch; Joyal–Tierney,
  from memory).

**Open:**
- the exact statement. The round trip can enlarge R (Kock–Moerdijk 1992, Remark 6.5, per Pro N77), so a condition on R is
  needed.
- his question, "Quelles propriétés obtient-on avec des feuilletages ???".

**Related work,** credited to Michel Hua's project and the Pro notes: SGA 4 IV, exercise 9.8.3 (1972) has the functor
C → C′; Kock–Moerdijk (1992, 1996) have the converse for étendues and the monodromy topos.

### Collars and cones (148–149; SA20-3)

**Readings decided on the image (148):**
- "partie ⟨modérée⟩ quelconque": "quelconque" is underlined and live (Hua: struck).
- The strictness condition is "Ċ est bordant dans **X∖(C∖Ċ)**", with X written over B. The transcription's "<-B> (C∖Ċ)"
  drops the X and the set-minus.

**What he conjectures,** for B "bordant" in X:
- I a) a collar exists;
- I b) the space of strict collars is contractible;
- I c) the automorphisms of a collar inducing the identity on B, and "libres" on Ċ, form a contractible space.
- II a)–c) are the same for cones around a point, with "(Alexandroff ?)".
- Every choice is "anodin".

**Checked:**
- **II c) is true.** It is J. W. Alexander's trick (1923), re-derived for compact Y in a tame category: his "Alexandroff
  ?" is Alexander.
- **I c) is false as written.** For B a closed manifold the group in question is the concordance (pseudo-isotopy) space
  of B. Its π₀ is nonzero for suitable closed manifolds of high dimension (Hatcher–Wagoner 1973; the topological case
  through Burghelea–Lashof–Rothenberg; from memory). PL pseudo-isotopies are tame, so the obstruction carries over.
  Michel Hua's project made the same objection.
  - Refined: the fibrewise automorphisms (b, u) ↦ (b, h_b(u)) form a contractible group.
- **I b) falls with c).** His own struck line says the space of rigidified collars fibres over the space of collars,
  with fibre a torsor under that group. If the total space is contractible (as for smooth collar embeddings, from
  memory), b) fails exactly when c) does.
  - What survives of his conclusion: the choice of a strict **rigidified** collar is anodyne.

**Open:**
- I a) for a tame "bordant" subspace, an undefined notion;
- II b).

The apex of a cone absorbs any automorphism; the free end of a collar does not.

### The cascade, tubular neighbourhoods, filtrations (149–153; SA20-4)

**The cascade (149–150).**
- Six categories: PB, PBC and PBCR (bordant pairs, with a strict collar, rigidified), and EP, EPC and EPCR (pointed
  spaces, with a strict cone, rigidified).
- A diagram of functors claimed to be "équivalences de cat. ∞-isotopiques", with two 2-cells α and β, and variants for
  multipairs.
- The margin reads "11 foncteurs" (image; the "14" alternative is out). The first diagram has exactly eleven arrows.
- **Checked:** α and β are isomorphisms once a collar exists:
  - (X ∪_B B × I, B × 1) ≅ (X, B);
  - X ∪_B Cône(B) ≅ X/B.
- **The forgetful functors** are equivalences exactly when the choice spaces of I and II are contractible.
  - With I c) false, PBCR → PBC → PB cannot all be equivalences for B with a non-contractible concordance space.
  - The system holds with fibrewise collar automorphisms, or with rigidified collars throughout (open in the tame
    setting).

**Tubular neighbourhoods (151).**
- A tubular neighbourhood of Y is by definition a strict cone around the point Y in X/Y.
- **The construction:** f⁻¹([0, ε]) for a tame f with f⁻¹(0) = Y, "ε petit [et admissible]".
  - Re-derived through Hardt's triviality: for ε below the first bifurcation value of f on X∖Y, V/Y is a cone on V̇ and
    the cone is strict.
  - So "admissible" means no bifurcation value in (0, ε] (our reading).
- **The Y-admissible rigidification** is a mapping-cylinder presentation.
  - The exterior is X∖(V∖V̇), decided by the mathematics with the ink compatible. The transcription has
    "X∖([V̇|V]∖V̇)", Hua "X∖(V̇∖V)".
  - a) Existence: true for compact tame pairs (derived neighbourhoods; the route is Michel Hua's project's).
  - b) The homotopy class of φ: V̇ → Y is determined: re-derived, φ ≃ inclusion followed by a retraction.
  - His "Mais on voudrait plus précis" remains open.

**The equisingular case (152).**
- He presumes that φ can be taken fibrant, with an ∞-isotopic equivalence between equisingular pairs and data
  (X′, B, Y, φ). This is the later unzipping (Thom–Mather; Ayala–Francis–Tanaka; from memory).
- The NB "X∖Y, Y réguliers ↔ X′ variété à bord" is right.
- **The margin** "X∖Y régulier implique Y régulier":
  - false in general: the axes in ℝ² (Pro N29);
  - true under equisingularity, where it is nearly tautological.
- **His 2° condition,** dim φ⁻¹(y) = codim_y(Y, X) − 1, was tested on sphere bundles, on links of points and on the cross
  in ℝ².
  - It holds for a suitable structure and fails for derived neighbourhoods of finer triangulations, so it is a genuine
    selection criterion.
  - Whether it gives uniqueness is open.

**Filtrations (153).**
- He corrected "la plus fine" to "la **moins** fine de toutes". The correction is necessary: any regular equidimensional
  filtration can be refined by adding a point, so only the coarsest can be canonical.
- Its existence for tame spaces is open here. Known analogues: King's intrinsic stratification (1985) and minimal
  Whitney stratifications (from memory).

### The Digressions combinatoires (155–161; SA20-5)

**What the pages hold:**
- Two plans and calculations for a "géométrie des ensembles finis": orientations, contracted products, squares, the
  exceptional isomorphisms up to six elements, the duality S ↔ S* of six-sets (the outer automorphism of S₆), the
  bi-icosahedra, and the affine plane over 𝔽₃.
- **Readings decided:**
  - "Réflexions **t. 4**" on 155 (image; agrees with Hua);
  - "GP(**1**, 𝔽₃)" on 156;
  - "2·(**6**!)" on 156 (the mathematics).

**Checked by computation:**
- The dictionary of 155 and 157: (1,5) ↔ bi-icosahedron, {2,4} ↔ {2,2,2} = cube, {3,3} ↔ {3,3}.
- Ic(S) ≅ S* × ω(S), with exactly two equivariant identifications.
- The canonical bijection S∖{s} ≅ S*∖{s′}.
- The refined correspondences of 157:
  - bi-icosahedron + vertex ≈ bipentagon;
  - + edge ≈ square: his deletion of the factor Ens₂ is right;
  - + "biface" ≈ Ens₂ × Ens₃.
- **The torsor identities of 156–157** hold when **ω(Q) is the orientation of the square (its sense of rotation), not of
  the four-element set**:
  - ε ∧ ε* ∧ ω(Q) ≃ 1;
  - ω(Q) ≃ ω(Q*);
  - his derivation of "codiag Q* ≃ diag Q".
  - "Q* ≃ ε ∧ Q" is not a torsor identity; the twist it needs is undefined on the page.
- **The "groupe trilitaire" of 156 is AGL₂(𝔽₃),** of order 432 = 3·144. For each of the three pairings α of the four
  directions:
  - there is exactly one G_α ≅ S₆ in the symmetric group of the twelve lines: the graph of an outer isomorphism between
    the two six-sets of lines, containing the translations;
  - AGL₂(𝔽₃) permutes the three G_α;
  - the stabilizer of α, AΓL₁(𝔽₉) of order 144, embeds in Aut(G_α) ≅ Aut(S₆) (order 2·6! = 1440) with **index 10**;
  - the translations are a common Sylow 3-subgroup, with N(V₀)/V₀ ≅ D₄, "le groupe du carré".
  - So his "sous groupe d'ordre 10 de Aut(G_α) (d'ordre 2·(6!))" is right with "ordre" read as index. Hua's objection
    ("10 ne divise pas 72") rested on a misread ambient order. The Pro note N46's low-confidence lead is now proved.
  - "Trilitaire" is a triality; it explains the "Trialité des bi-di-triades" of 159.
- **The exact sequence III.5,** 1 → (𝔖₃ × 𝔖₃)′ → Aff(2, 𝔽₃) → 𝔖₄ → 1, is exact and does not split (Pro N48 confirmed).
- **The isomorphisms of 160:** 𝔖₃, 𝔖₄, A₅ and 𝔖₅ with PGL₂ over 𝔽₂ to 𝔽₅, and Frobenius for 𝔽₄.
  - The margin's monomial group has order 48 and needs "det 1" to give 𝔖₄.

**Re-derived (159):**
- the Steiner-system description of AG(2, 3), once "a ≠ b" is added;
- "b) résulte de a) et c)";
- the completion to the projective plane of order 3.
- "c implique card V = 9" is false without a): there is an 18-block counterexample.

**Open:**
- the "trois perspectives" of the skew icosahedron;
- the hexagram duality "par bihexagones";
- the twist ε ∧ Q;
- "les réalisations géométriques des configurations envisagées ici" (161), which he leaves to be written.

**The sheet 158.** Its octahedron sketches, with antipodal labels a, a′, b, b′, c, c′, fit the (2,2,2)-structure. The
sheet was probably used for this work.

### The Orsay report (276–281; SA20-6)

**What it is:** "Rapport de la Commission relative au recrutement des enseignants", Faculté des Sciences d'Orsay, 1968
("avant la rentrée d'Octobre 1968"). It is a collective document and contains no personal data.

**What it provides:**
- an École and a Laboratoire under an Assembly with one third students;
- two-thirds rules and a student veto for École appointments;
- detachments, and transfers "par les mêmes modalités qu'une première nomination".

**Checked:** the voting arithmetic of the Pro notes (N64, N68, N69).

**How it connects:** it has the architecture of part B of his June 1968 text (119/254–270, per Michel Hua's project),
under other names and numbers.

**For the edition:** a document by other authors, for the user's decision.

### Dependencies (read)

- SA20-4 uses SA20-3 (his pages 149–151):
  - the six categories are built on the collars and cones of I and II;
  - tubular neighbourhoods are strict cones.
- The sweep-2 rows SA20-2 ↔ SA20-5 ([the user's words, omitted]) have no basis on the pages.
- Within SA20-5:
  - 160 IV.2 sends to 155 Chap. 3;
  - 156 uses the ditriads and quadritriads of 160.
- The Additif depends on the Esquisse by its title.
- Placement corrections for sweep 2:
  - several MPL_119 rows list scans of other cotes (143, 147, 149, 150, the LM4 source);
  - #61 belongs to SA20-5.

### The transcriptions

**Passes:** one Pro transcription with notes and doubts. Read in full in sweep 3, with images for the doubtful places.

**Corrections to carry:**
- 144: "15 p";
- 148: X∖(C∖Ċ);
- 150: "11";
- 151: X∖(V∖V̇);
- 155: "t. 4";
- 156: GP(1, 𝔽₃) and 2·(6!).

**Open readings:**
- the margins of 145–146;
- "PS|A" and "resp. A" (148);
- φ(a) = o (149);
- "esselle", "ald" (152);
- "rien|bien" (153);
- the struck columns of 155–157;
- "Devenir|Durée" and "p. 7?9" (158);
- faded words on 279–280.

**Ready for an edition and translation** (GPT-6.2 Sol at reasoning effort max over the API):
- 145–146, 148–153 and 155–161: after one ink pass and the corrections above;
- the cover: as apparatus;
- 158 (his own typed sheet) and 276–281 (by other authors): for the user's decision.

**Not in any package:** 119/143 (page 2 of the [the user's words, omitted]), 274 and 275.

---

## 2. Cotes 152 and 120: plane trees (SA20-7) and the axioms of a tame topology (SA20-12)

By Claude Opus 5.5 at effort max (reader 152_120, horizontal sweep 3), 19 Nov 2026.

**What was read:**
- All 38 pages of the package MPL_152+120, in the corrected files of the two second passes of 17 Nov 2026:
  - 152/001-013 and 120/001-006 by this reader, which read them against the scans then;
  - 120/007-025 by the parallel block.
- The first pass's notes and doubts.
- The sweep-2 tables.

Full working: `readings/152_120.md`. Check events, corrections and dependencies are in the TSV files of the same name.

### 1. Cote 152: "Catégorie des types de mots [dont arbres plans]" (after 19 May 1982)

**The paper.** The sheets are pin-feed paper of a computer centre:
- 006, 009 and 012 are IBM job logs and JCL of job PREDONTA/1125, dated "19 MAY 82" (009) and SYS82139.T163912 (006): day 139 of 1982 is 19 May.
- 003 is written over the printout lines, so it is later.

**What he does, in order.**
- **002.** A sheet of drawings: one-, two- and three-letter "systèmes" (u, u^{-1}, uv, …), "syst. u^{-1}u" drawn as a circle cut by a chord between u^{-1} and u, families of pointed trees, and two boxed operations, "composition" and "insertion d'un cycle".
- **003.** The claim: "La cat. des ``types de mots'' de long. n équivaut : la cat. \unsure{isotypique|isotopique} des systèmes formés d'un disque D … d'un ``découpage par cordes'' de ce disque". The data are (D, ω, K, S_0) with n boundary vertices S, and a "reduced order" Σ_{α⊂R_0}(Card(α∩S) − 1).
  - Above it, corrected in the second pass: "disques or. découpés par cordes ⟷ arbres circularisés ⟷ contours à involution sans pt fixe [non pénétrante]". This is the whole correspondence of 010-011, already on the first sheet.
- **004.** "Admissible" graphs: a segment graph with an involution σ on its edges, defined by contracting an edge of an orbit of two consecutive edges.
- **005, "Arbres plans".**
  - Trees as (S, A ⊂ 𝔓_2(S)).
  - Plane trees as germs of embeddings, which are the bicircularisations (ε, c: ε → circ(Γ)).
  - In an oriented surface, circularisations, which depend only on the vertices of degree ≥ 3.
- **007-008.** Cutting a surface along a plane tree gives a polygon. For a general circularised graph one gets a contour on the arcs Ā, with the reversal σ and the rotation ρ. The rewritten formulas for σ_1^C and ρ_C follow.
- **010, "En résumé".**
  - Circularised graphs without isolated vertex ≃ oriented contours with a fixed-point-free involution on the edges.
  - The dictionary: ρ_Γσ_Γ ↤ ρ_C, ρ_Γ ↤ ρ_Cσ_C. The construction is called "déploiement du graphe plan donné".
  - A margin speaks of "la \unsure{carte} actuelle définie par Γ".
  - Boxed: "Γ un arbre ⟺ C est un polygone comb. (non ponctuel), et l'involution σ_C … est totalement non pénétrante".
- **011 and 013.**
  - |Γ| is the quotient of |C| gluing a with σ_C^a, orientations reversed.
  - For trees: C is the boundary of a disc, the paired edges are joined by disjoint chords, regions are vertices and frontiers are edges.
  - "La catégorie des arbres plans (pas néc. plus orientés) est équivalente : la catégorie \unsure{isotypique|isotopique} des disques … munis d'un tel découpage".

**What is proved and checked (re-derived).**
- The count of circularisations, Π_s(card A_s − 1)!, and the bicircularisations as germs.
- The dictionary of 010: faces are the orbits of ρσ, and (σ, ρ) ↦ (σ, ρσ) is invertible. Rows 2-3 force row 1 to read σ_Γ ⟷ σ_C; the ink is unresolved.
- The tree criterion: for a one-face map V − E + 1 = 2 − 2g, so tree ⟺ genus 0 ⟺ the pairing is non-crossing.
- The quotient |C| → |Γ|.
- The disc picture: n disjoint chords give n+1 regions and a tree; both sides are counted by Catalan numbers.
- His "d'ordre ≤ 1, il y en a un et un seul" (005) is the ink and is true. It is weaker than the ≤ 2 his preceding sentence gives.

**What is wrong.**
- **The head of 010 against the dictionary.** The head ("σ_Γ = σ_C, ρ_Γ = ρ_C") contradicts row 3 (ρ_Γ = ρ_Cσ_C) unless σ_C = id. The dictionary is the coherent version. Michel Hua's project notes the same disagreement.
- **The rule of 004.** It does not characterise non-penetrating involutions:
  - Read literally (one edge contracted, its partner left fixed), it admits only involutions whose 2-orbits are consecutive pairs. It rejects the nested (1 4)(2 3), whose chords do not cross.
  - Contracting both edges of the orbit gives the usual test for non-crossing pairings. The struck "deux" in "l'une des \deleted{deux} arêtes" is his hesitation at this point.
  - Fixed edges (σ = (1 3) on three edges) are outside the scan-10 criterion in either reading (the first pass's P05, @902).

**What is open.**
- "Type de mot" is defined nowhere on these pages, so the equivalence of 003 cannot be checked. The obvious reading (chords as cancelling pairs, reduced order as reduced length) does not fit the one-letter case.
- Whether "isotypique" (a category of types) or "isotopique" (isotopy classes) is meant. The user's eye on 003 and 013 decides.
- The operations of 002.

**How it connects.**
- The same objects carry the global tag H00J (SA10-18; not read here).
- The word [the user's words, omitted] for the planar structure, on paper of May 1982 or later, comes two years before the Esquisse's cartes and dessins (hunch H20-152_120-1).
- Cote 152 and cote 120 share a package, not a subject.

### 2. Cote 120: "Topologie modérée" (the axioms, 120/002-025)

**The title sheet (002).** "Topologie [over struck "Structures"] modérée", "(Autour de l'Eloge)", and a faint pencil \unsure{1978|1778}. Michel Hua's project reads 1978, a label rather than the date of writing.

**(I) Models (003-006).**
- **The axioms.** Classes M_n ⊂ 𝔓(Rⁿ) closed under the coordinate maps u^*: images (M1), inverse images under the injective ones (M2), traces u^{*-1}(B) ∩ A (M3), and products (M4). He reduces M1-M3 to generators (004). Re-derived.
- **Intersections.** "M1, M2, M4 impliquent que les [M_n] sont stables par intersection de deux": A∩B = δ^{-1}(A×B). Re-derived, with his inserted "(moyennant M1, M2, M4)". The page writes 𝔖_n for M_n, a slip.
- **The M3 reduction.** The mathematics requires "pour u injectif", since the standard projection is u^* for an injection. The ink, "surjectif|injectif", is open; Michel Hua's project reads "surjectif".
- **Trivial cases.** ∅, {∅} and filter bases are excluded; M′_n = M_n ∪ {∅}; and M_∅ = {∅, {e}}. All re-derived.
- **Points.** R_0 is the set of points x with {x} moderate. The revision "R_0 ≠ ∅" → "Card R_0 ≥ 2" gives ∅ ∈ M_1 (005, confirmed on the ink; @922). His "{x} ∈ Rⁿ" is a slip for M_n.
- **Examples.** Card ≤ 1, finite, all: "Aucun de ces exemples … pour nous!"
- **(II) The category.** Moderate maps are those with moderate graph. Identities, composites ("via M2", fitting the composite) and inverses of bijections are moderate. This gives Esp_{M_*}, with a faithful, conservative and transportable |·|. Finite limits exist with no hypothesis. The final object is the model {e} of R^∅, which is why he struck "(M5) R_0 ≠ ∅ … objet final" on 007.

**The reconstruction (008, 018) is incomplete.**
- His claim: "la donnée d'un M_* est équivalente à la donnée d'un système (E, R, X ↦ |X|)" with finite limits, |·| left exact, and every object embedding in some Rⁿ.
- The forward direction holds. The converse also needs:
  - |·| faithful, conservative and transportable, which he states on 006 and 018 but not here;
  - an image axiom, the categorical M1.
- Finite limits give M2-M4, and M1 only for maps injective on the set.
- Whether full M1 follows is open (package R20-152_120-2).

**Colimits (009-014).**
- **Finite sums** need Card R_0 ≥ 2 and M5 (finite unions; 009, 010). With Card R_0 = 1 the sum 1 ⊔ 1 cannot exist with |·| commuting. So 015's "Si R_0 ≠ ∅ … sommes disjointes" keeps a superseded hypothesis.
- **Colimits with a compatible structure** (009, proved on 012).
- **The amalgam criterion of 011.** For two inclusions X_1 ↩ Z ↪ X_2, the pushout exists iff finitely many pairs of moderate functions agree on Z and separate points. Re-derived both ways; "R^I" is a slip for R^A.
- **M6 (013)** ("Z a common fibre of finitely many functions that separate X∖Z") ⟺ the strict quotient X/Z exists. Re-derived.
- **M7** is the extension of moderate functions from Z to X.
- **"Moyennant M5, M6, M7, les sommes amalgamées … existent"** (014). Re-derived through the explicit embedding x ↦ (a_1, h_1, e_2), (a_2, e_1, h_2).

**Ind-spaces and topology (015-020).**
- **Ind-spaces.** Strict ind-moderate spaces are built under M8, R being the union of its moderate parts. Quotients by locally moderate parts exist (016). His warning that subobjects need not be locally moderate (017) holds: n ↦ 1/n from a countable discrete ind-space to R.
- **Continuity.** With R separated and moderate parts compact, moderate maps are continuous: graph projections. Re-derived.
- **The induced topology (018).** The colimit topology induces each moderate part's own topology. This holds for any directed system of compact Hausdorff pieces; his "ind-dénombrable" is not needed for it (it matters for products).
- **M10** gives moderate neighbourhood bases.
- **Locality (019).** Moderate maps form a sheaf, by compactness and M5. A structure is determined by its moderate functions with (M1)_0-(M4). Re-derived.
- **Locally moderate spaces (020).** "les parties compactes sont les parties contenues dans une partie modérée" is false as written ((0,1) ⊂ [0,1]). It is true for the relatively compact parts.
- **The margin of 020.** "Dire qu'une partie compacte et … d'un espace modéré est modérée" fails in every o-minimal model (the Cantor set) unless it reads "compacte et loc. modérée", which a struck "loc." beside it suggests. One look at the scan decides (hunch H20-152_120-6).

**The field (021-024).**
- **M11:** a) 0 [et|≠] 1 ∈ R_0; b) x−y and xy moderate; c) inverses bounded ("OPS B = A^{-1} !").
- a)-b) ⟺ the moderate functions form a ring. Re-derived.
- R_0 is a subring, and then a subfield (023). His "∈ M_1" for the inverse graph is a slip for M_2.
- **The Proposition of 024.** The zero set Y of finitely many moderate functions can be cut out by functions f_α, f_α g_β that separate X∖Y. Re-derived. "sépare les pts de X" is an overstatement (endpoints of [0,1]). The hypotheses "M1 : M7 et M11" can be reduced to M1-M4 and M11.
- **Consequence (hunch H20-152_120-5).** Under M11, M6 reduces to "moderate parts are common zero sets".

**À prouver (025).**
- Generic triviality of a morphism over the complement of a rare moderate part. This is Hardt's theorem in the o-minimal setting (from memory).
- His "Énoncé analogue pour un diagramme fini … ?!" holds for diagrams of inclusions, his example Z ⊂ X ⊂ Y × [0,1].
- It fails with parallel arrows: a semialgebraic family of rotations of S¹ over (0,1) has a varying rotation number. This agrees with the first pass's Q4-07.

**What is open on 120.**
- The reconstruction.
- Generic triviality (his "À prouver").
- The fragmentary slanted margins of 006-008, 013, 015.
- The reading of the 020 margin.
- The o-minimal comparison (SA20-10, SA20-11), left to the 121 reader with the prompted questions. The axiom list for it, as on the pages: M0 007, M1-M4 003, M5 010, M6-M7 013, M8 015, compactness 017, M10 018, M11 021.

### 3. The transcriptions

| Cote, scans | Passes | Open readings that matter | Ready to edit and translate |
|---|---|---|---|
| 152/001-013 | Pro first pass + audit; Claude second pass (17 Nov, Hua as witness); sweep 3 | 003 isotypique\|isotopique, arête\|cpt., non\|mais pénétrante\|pointés; 004 ε\|ξ; 008 boxed formulas; 010 row 1 (σ_C by the mathematics) | 004-005, 011, 013 yes; 003, 007-008, 010 after the user's eye on these places; 002 after a TikZ check; the printouts 006, 009, 012 (others' job logs) for the user's decision |
| 120/001-006 | the same | 003 surjectif\|injectif (injectif by the mathematics), the heading; 005 I ≠\|= ∅ | yes |
| 120/007-025 | the same (parallel block) | 015, 019, 020 margin, 021 [the user's words, omitted], 025; slanted margins fragmentary | yes, with the marks |

**Corrections to sweep 2.** The PLACEMENT, OBJECTS and CLAIM_LINKS rows of SA20-7 give cote 120 and places like "120/003": they are cote 152. The A120 rows cite context scans of cotes 147 and 149 as "120/1xx".

---

## 3. Cote 121 scans 49-73, cotes 153 and 155: tame topology, analysers, a Tannakian duality (SA20-15, -16, -17)

By Claude Opus 5.5 at effort max (agent aff4deb18a6ec3192), reader of the stretch `121_049-073_153_155`, 18 Nov 2026,
about 23:05-23:45 UTC. The full working is `readings/121_049-073_153_155.md`.

**Read in full:** the Pro package MPL_121_049-073+153+155 (transcription, notes, the doubt rows that carry the
mathematics). **Scan images:** 121/050 and 052 (two readings decided), 121/053, 064, 069 (blank). **Not used:** Michel Hua's
project (no reading in doubt needed a second witness); the scans of 153 and 155.

### 1. Cote 121, scans 49-73: five drafts of a tame topology (SA20-15)

**What he does, in order.**
1. **Admissible partitions (049-052).** Under "Contextes" (PL, semi-analytic, algebraic and analytic over C) he claims a
   coarsest strictly admissible partition adapted to a locally finite family of closed sets T_α, commuting with
   restriction to opens, and starts an induction on dimension that stops at "Soit". He shows that the incidence order is
   detected on any open set (050), replaces "connected leaves", which is not stable under restriction, by a stable
   condition (C) (051), and presents admissible partitions equivalently by their closed leaves (052).
2. **The moderate category (054-058).** A category with a left exact, conservative functor to compact spaces (he
   corrected "fidèle" into "conservatif", rightly: faithfulness follows); images; the effective-epimorphism question,
   answered by a graph lemma; special ind-objects for locally compact spaces; a moderate real line with rational
   rescalings, the point 1, sum and product (M4); the injective embedding M5; then the reconstruction of the whole
   category from the families M_n of moderate compact subsets of cubes (M′0-M′4).
3. **The categorical form and gluing (059-063).** The same reconstruction over any finitely complete category; image
   factorizations and unions; then the existence of moderate pushouts under two axioms, 5° (the interval is injective)
   and 6° (every subobject is a zero locus), with a complete proof on 062; and an unfinished translation into function
   families F_n (063).
4. **Triangulation and attaching (065-068).** A list adding finite unions, injectivity, zero loci, and triangulability
   with relative extension (065); a Chern-class fragment (066); a criterion for attaching spaces by kernel pairs (066);
   and the multiplication trick (x, y) ↦ (x, xy) that realizes the attaching space inside a cube (067-068).
5. **The C_* draft (070-073, his pages 1-2).** Families C_n ⊂ P(Rⁿ) closed under coordinate images and products; graph
   morphisms; C_*-models; compactness, neighbourhood bases, the sheaf of germs of morphisms and C_*-spaces (072); finite
   unions and finite closed-cover descent (073); the pushout question, "O.K." with the margin "? à tirer au clair".

**Proved and checked.** 27 check events. Re-derived and right: the incidence-order detection and its corollary (050),
open leaves are the maximal ones (051), the closed-leaf presentation (052), conservative and left exact imply faithful,
the effective-epimorphism lemma (054), local compactness of the special ind-objects (055), the moderate line and its
rational points and intervals (055), the reconstruction of the category from M_* (057-059), effective epis and monos
(059-061), **the gluing proof of 062, which is complete**, the graph criterion of 063, the attaching criterion and the
product trick (066-068), and the C_* propositions that need no intersections (070-073).

**Wrong, with the correction.**
- **049:** the first open stage X^[1] = ∪ T̊_α is wrong (the Pro notes' test: X = R, T = {0}). It is X − ∪ Fr(T_α),
  minus the singular locus for non-singular leaves; re-derived.
- **050:** the ink reads X^{i−1} for the next stage of a descending filtration (read on the image): his slip for X^{i+1}.
- **052:** the ink reads Φ_i = F_i without the bar (read on the image): his slip for F̄_i; also the Φ_i must be non-empty.
- **056:** under 1°, 2° alone the moderate maps do not form a vector space over the field R_mod: R_mod need not be a field
  (Pro notes), and when it is, scalar multiplication may fail (my test: rational slopes, real constants). With the
  product 3°, both claims hold.
- **057:** the graph of a composite is the projection of p⁻¹(Γ_f) ∩ q⁻¹(Γ_g), so the image axiom M′3 is used too.
- **058:** the equivalence with M′4 needs I = [−1, 1] (as on 065), not the I = [0, 1] of 056 (new).
- **063, 065:** two typing slips: a point is in F₀, not F₁; {0}, {1} are in M₁, not M₀.
- **070:** "X, Y ∈ C_n ⇒ X ∩ Y ∈ C_n" does not follow from the stated axioms (countermodels: the Pro notes' and a smaller
  one generated by [0,1], [1,2], R). Intersections must be an axiom; cote 120 has them through inverse images. Composition,
  pairing, images and inverse images of parts, and the sheaf property of 072 all depend on it.
- **065:** triangulability is a new axiom, not a consequence of the list (all compact sets satisfy the list; a Cantor set
  is not triangulable).

**Open.** The induction of 049 (a coarsest partition and its gluing); transportability of the ind-objects (055); F3 and
the converse postulate in 063; c) of the attaching criterion is not marked done (068; it holds with the products); the
pushout question of 073 (it follows if a zero-locus function is added, as on 061-062).

**What the pages bring to the prompted questions.** No "tubulure" or "ombre" (SA20-8); nothing on the remords (SA20-9);
five compact-model axiom systems, none o-minimal as written, with finiteness in dimension one only through the
triangulation axiom of 065 (SA20-10; the "M0-M5" here are not the M0-M11 of cote 120); the list of contexts on 049 and
051, without a comparison theorem (SA20-11).

### 2. Cote 153: the analysers (SA20-16)

His pages 1-5 are on printout of 19 April 1982. **What he does.** For a base ring k₀ he asks what structure the
operations on rings carry: a commutative pseudo-ring Ω with a composition F∘G, right composition a ring homomorphism, and
optional finite coaddition and comultiplication (006). The constants form a sub-ring, Ω acts on them, and Ω splits
additively as constants plus operations vanishing at 0 (006). Examples: all maps A → A, endomorphisms of the affine line
(k[T]), formal series (008); the relative case {F ∈ K₀[T] : F(k₀) ⊂ k₀}, with the binomial analyser for Z ⊂ Q, the
analyser of λ-rings, and the non-unital analyser of divided powers (004, 010).

**Checked.** The binomial structure (003) by computation: integral product and composition constants in the basis of
binomial polynomials, with a closed form, Vandermonde, and an integral comultiplication; the presentation of Int(Z)
(Newton interpolation). Re-derived: the free-module lemma of 004, the constants and the splitting (006), the examples and
the map to the maps on constants (008).

**Refined.** "OK si Ω est un module libre" (004) holds when k₀ is a domain with fraction field K₀, the hypothesis he
struck out; for an arbitrary inclusion the decompositions are not unique (the Pro notes' A26).

**Open.** The blanks e), f) on 002; uniqueness and coherence (A12); the divided-power analyser; injectivity of
Ω → App(Ω₀, Ω₀) (008). **In today's terms:** a one-sided form of the plethories of Tall-Wraith and Borger-Wieland.

### 3. Cote 155: a tensor category with a fibre functor over k′/k (SA20-17)

His pages 1-5 are on university documents of June-October 1984. **What he does.** For k′/k finite, he states that an
abelian k-linear ⊗-category with a faithful ⊗-functor to Modf(k′) is the same as a commutative augmented k′-algebra U
whose dual pro-ring A carries a coproduct that is multiplicative into the idealizer quotient J̃/J (002). The example
Modf(k) gives A = End_k(k′) (004). He asks for intrinsic conditions (rigidity, End(1) = k?) making the diagonal functor
M′ ↦ M′ ⊗_{k′⊗k′} k′ exact and faithful (004), and starts on rigidity: duality as Hom_A(−, U), an antipode a: A → A^o
(006), F′(D(M)) = M^∨ (008), and the evaluation pairing, reduced to M = A (010), where the pages stop.

**Checked.** The example and its Morita test (004); exactness for étale k′/k and its failure for inseparable k′/k
(Pro notes T11-T12, re-derived); End_A(U) ≅ A^o (006); F′(D(M)) (008); the reduction to M = A through finite quotients
(010). **New here:** J̃/J is Takeuchi's product A ×_{k′} A, so condition (ii) makes A a ×_{k′}-bialgebra, a bialgebroid
over k′.

**Open on the pages, settled later.** The equivalence of 002 is stated, not proved; the evaluation, coevaluation and
triangle identities are not reached. His question on 004 is answered by Deligne's theorem (1990) for rigid categories
with End(1) = k (Pro notes T09-T10).

### 4. How it connects

- **Cote 120 (SA20-12):** by content, 120's list (coordinate inverse images, unions, level loci and extension,
  compactness) consolidates the 121 drafts and closes the intersection gap of 070 (H20-121_049-073_153_155-2).
- **Cote 156 (SA21):** 052's closed leaves are the "figures" of 156-4; 065's triangulation is the existence half of the
  "contrée modérée" axiom of 156-4/70; 070's intersection claim reappears qualified in 156-3/20.
- **Cotes 150-151 (SA10):** the partition and incidence apparatus of 049-052 precedes the stratified topos; no citation.
- **SA20-W3 (cote 123):** the sweep-2 link to the filtrations of 123/018 is a subject link only; 155 shows no dependence.
- **SA22-0:** 155 is his own return, in 1984 or after, to non-neutral Tannakian reconstruction.

**Hunches** H20-121_049-073_153_155-1 to -3 (cote 121) and -51, -52 (cotes 153, 155). **Packages** R20-…-1, -2 (an
o-minimal reconstruction theorem; the canonical partition) and -51, -52 (analysers and plethories; 155 against Deligne
and the bialgebroids).

**Deliverables.** All four stretches of the package have had the Pro transcription (first pass and second audit) and are
ready for an edition and translation after one ink pass on the low-confidence words. The typed and printed versos (153:
computer printout of 1982; 155: a publishing-contract page, university notices and letters of 1984, including minutes
with candidates' names and votes) are by others and are left to the user's decision.

---

## 4. Cote 122: [the user's words, omitted] (undated; after April 1968) — SA20-18

**Read in full tonight:** MPL_122 (scans 003–035, 32 faces).
- His notes are on the odd faces and on 020–035.
- The other faces are reused paper:
  - 004–016: a typed Bourbaki draft, "n° 387", pages 42–48, exercises on valuations and linearly compact modules;
  - 018: an Institut Henri Poincaré announcement of Efimov's lectures, first lecture on 25 April 1968, so the notes are
    from 1968 or later;
  - 021–031: pages 4.11–4.15 of an English typescript on the absence of geometric quotients (Nagata's quintics,
    Hironaka's example). This has the shape of Mumford's GIT, ch. 4 (from memory).

**What he does, in order.**
1. **Duality for manifolds with boundary (003–011).**
   - H*(P) ≅ H*(P°), and H^i_!(P°) ≅ H^{n−i}(P, F^∨ ⊗ T)^∨.
   - For W = P ∪ Q with P ∩ Q = R = ∂P = ∂Q: the relative and Mayer–Vietoris sequences, and their duals.
   - The "Récapitulation" of 011 sorts them into two dual pairs (Φ, Φ′) and (Ψ, Ψ′).
2. **The open book (013–017).** P → S and Q → T are bundles with fibres M and N, glued along ∂P ≅ ∂N × ∂M ≅ ∂Q.
   - In the case at hand: W is the boundary sphere of the Milnor ball, P = W − W₀ is fibred over S¹ with fibre M (the
     Milnor fibre), Q = W₀ × D², and R = W₀ × S¹.
   - That is Milnor's fibration as an open book with binding W₀ (the link of the special fibre).
   - The margin of 017 counts "80 suites exactes".
3. **The "donnée fondamentale" (020–026), in the derived category of Λ[π] with π the monodromy group.**
   - K• = RΓ(M) with its monodromy, L• = RΓ(W₀) with trivial action, and ρ: K• → L• compatible with cup products.
   - Applying RΓ^π gives RΓ(W − W₀) → RΓ(W₀) ⊕ RΓ(W₀)[−1]: the maps α and β, β being the boundary map of the Gysin
     sequence.
   - If W is nonsingular, Poincaré duality turns the vertical arrow into u: RHom(K•, Λ)[−2n] → K•: compactly supported
     to ordinary cohomology of the Milnor fibre, the intersection form in degree n.
   - The triangle is "autotransposé", with "(signe ?)" left open. He extracts the pairings λ and μ between RΓ(W₀) and
     RΓ(W − W₀) and claims they are β and α ("je dis que c'est β … α").
4. **Cohomology when W is a sphere (026–034).**
   - **From the Gysin sequence:**
     - H^i(W − W₀) ≅ H^{i−1}(W₀) for i ≠ 0, 2n;
     - H^{2n}(W − W₀) = H^{2n+1}(W − W₀) = 0 and H^{2n−1}(W₀) ≅ H^{2n+1}(W) when W₀ is connected (always for n ≥ 2).
     - Re-derived, agrees.
   - **Local Lefschetz:** H^i(W) → H^i(W₀) is an isomorphism for i ≤ n−2 and injective for i = n−1, with the dual
     statement for the Gysin map. The reading "n−[2|1]" on 028 must be n−2 by the mathematics.
   - **Hence:**
     - H^i(W₀) = 0 except for i = 0, n−1, n, 2n−1;
     - H^i(W − W₀) = 0 for i > n+1;
     - the boxed H^i(M) = 0 for i > n, "indépendamment" of the nonsingularity of W and W₀.
     - The boxed claim is true (Milnor 1968, Hamm, SGA 7 I; from memory). His "passage à la limite" is a sketch: it
       works in étale cohomology, where H^i of the geometric Milnor fibre is the colimit over the tame covers.
   - **The relative sequence of (M, ∂M = W₀) (030–032):**
     - H^i(M) ≅ H^i(W₀) for i ≤ n−2;
     - H^i(W₀) ≅ H^{2n−1−i}(M)^∨ for i ≥ n+1 (the reading "n+[1|2]" must be n+1);
     - the six-term sequence 0 → H^{n−1}(M) → H^{n−1}(W₀) → H^n(M)^∨ → H^n(M) → H^n(W₀) → H^{n−1}(M)^∨ → 0, whose
       middle arrow is u.
     - Re-derived.
     - For W a sphere and n ≥ 3, H^i(M) = 0 for i ≠ 0, n−1, n (032, 034).
5. **Open on the page:** H^{n−1}(M) = 0, which makes M cohomologically a bouquet of n-spheres when the singular point
   is isolated and the total space smooth. Milnor proves it (1968). On these pages it is the next step after the
   six-term sequence (H20-7, R20-3).
6. **The note 035, separate:** with AB5 and S noetherian, the natural finiteness conditions on adic and co-adic
   inductive systems do not seem stable under cokernels (dually, under kernels). It concerns the adic formalism of
   SGA 5.

**How it connects.** It is the topological model of the local Picard–Lefschetz formalism of SGA 7 (I, XIII–XV):
vanishing cycles at an isolated singular point, the variation map, and the self-dual triangle. The comparisons with the
research-run rows (SA20-19) were not made tonight.

---

## 5. Cote 123: the adjoint quotient, Kostant's principal elements, and the letter to Kostant (SA20-W1, W3, W4)

**What was read:**
- In full: the Codex web transcriptions of K123-01 (scans 4–14), C123-01 (2–3, 16–20), K123-02 (15–36), K123-03
  (37–48) and C123-02 (22–23, 28, 40).
- Scan images: 123/016, 022, 023.
- The folder is a dossier of about 1968–69, on paper partly reused from typescript drafts:
  - 123/030, 032, 036 are leaves 8, 11, 6 of SGA 7, Exposé VIII, §2 "Accouplements définis par une biextension"
    (2.1.1–2.1.13). The section title is in our SGA 7 corpus, `sga7_port_20261109`.
  - 123/028 and 040 are leaves 22–23 of a text on morphisms of topoi (3.1.2–3.1.3, citing "I 2.11"). It matches SGA 4,
    Exposé IV §3 by content (my identification; the wording was not found in `sga4_port_20261112`).

### 1.1 "Lissification du morphisme de Kostant" (123/004–007) and "… de Steinberg" (123/008–014)

This is his simultaneous resolution of the adjoint quotient, done over an arbitrary base S.

**The Lie algebra (004–007).** G is semisimple adjoint over S; 𝔤 is its Lie algebra as a vector scheme; T is the maximal
torus of a Killing pair; 𝔱, W, J = 𝔱/W, J′ = 𝔱 → J.
- **The objects:** Bor and Kill (the schemes of Borels and of Killing pairs), the universal Borel ℬ ⊂ G_Bor, and its
  Lie algebra 𝓛.
- **The maps:**
  - q: 𝓛 → 𝔤, surjective (today the Grothendieck–Springer map);
  - f̄′: 𝓛 → 𝔱, through 𝓛/𝓛_u ≅ 𝔱_Bor.
- **Over the regular semisimple locus.** 𝓛^rss ≅ Kill ×_S 𝔱^rss, and W acts diagonally. If W acts freely on 𝔱^rss
  ("au moins si les car. résiduelles sont toutes ≠ 2"), the square with 𝔤^rss → J^rss is cartesian.
- **The quotient map.** f: 𝔤 → J extends the map on 𝔤^rss: 𝔤 is normal and J affine, so it suffices to check the generic
  fibre, which is Kostant's case.
  - His NB: the affine ring of J is the ring of invariants of 𝔤's, and f is universal for invariant maps to affine
    S-schemes.
- **The resolution.** With 𝔤′ = 𝔤 ×_J J′, he gets 𝓛 → 𝔤′ → 𝔤.
  - p: 𝓛 → 𝔤′ is projective and f̄′: 𝓛 → J′ is smooth.
  - p is birational: an isomorphism over 𝔤′^rss.
  - The largest open set where p is an isomorphism lies over 𝔤^reg, the elements contained in finitely many Borel
    subalgebras. He cites "Springer PM n°30, 5.3", that is T. A. Springer, Publ. Math. IHÉS 30 (1966), §5.3.
- **Questions 0) to g) on 007:**
  - 0) Does W act freely? No in characteristic 2 (A₁, B₂, …).
  - a), b) Is J regular? Is f flat, with flat ⇔ J regular and f equidimensional? Margin: "OK pour les 'bons' nombres
    premiers ?".
  - c) Are the fibres geometrically integral, each the closure of one orbit with a complement of codimension ≥ 2? Then
    𝔤′ is normal and 𝓛 → 𝔤′ → 𝔤 is a Stein factorization.
  - d) Are the smooth points of f the regular points, and those with a centralizer of dimension r?
  - e) An orbital structure for Chevalley groups over Z.
  - f) Kostant's section of the regular locus.
  - g) "the variety of Borel subalgebras of 𝔤 containing a given element: what is its dimension (relation with the
    dimension of the stabilizer)?" This is the question the letter to Kostant answers by a conjecture (§1.4).

**The group (008–014).** G is reductive over S, D = Bor(G), ℬ → D is the universal Borel, T is the canonical torus with
M = T̂, and I = T/W.
- f: G → I is the unique invariant map. In the margin he asks whether f is defined without G simply connected, and
  whether I must be smooth over S.
- G′ = G ×_I T; p: ℬ → G′ is given by h(g, B) = g and f̃(g, B) = the image of g in B/B_u ≅ T.
- **The theorem on 011:**
  - (i) p is projective and f̃ smooth (known).
  - (ii) p is an isomorphism ℬ^reg ≅ G′^reg, and G′^reg is the largest open set over which p is an isomorphism.
    - Proof: p is an isomorphism over the regular semisimple locus; the fibres over G′^reg are finite (Steinberg) and p
      is proper; G′^reg is normal; the Main Theorem.
  - (iii) ℬ − ℬ^reg has codimension ≥ 2, and G′ − G′^reg has all components of codimension 3, fibre by fibre (Steinberg).
  - (iv) For S normal and locally noetherian: Pic(ℬ) ≅ Pic(ℬ^reg) ≅ Pic(G′^reg), and Pic(D) ≅ Pic(ℬ) when
    H¹(Γ, M) = 0, a converse holding when S is regular. Sheafified: Pic_{ℬ/S} ≅ Pic_{D/S} = P (the weights). The ample
    cone of Pic_{ℬ/S} is the weight cone P⁺.
- **The lemma on 012.** For G semisimple simply connected over k and a Borel B: Pic(B) = Pic(T) = H¹(k, M).
  - Proof: T = Π T′ over a Galois extension k′/k, Hilbert 90, and the unit group of T′, which is k′* × M.
- **Remarks a)–d) (013–014):**
  - the exact sequence 0 → Pic(D) → Pic(ℬ) → H¹(Γ, M_ξ̄), with a 0 on the right when S is regular;
  - Pic(S) ≅ Pic(G′) for S normal and T untwisted;
  - 0 → Pic(S) → Pic(G) → Pic(G_ξ), a finite group that vanishes when G_ξ is simply connected and split;
  - Pic(G) → Pic(G^reg) is surjective (codimension 3).
- **The conclusion on 014:** "on ne peut trouver une résolution X̃ de f analogue à celle de f′, sans toucher à G^reg".
  - The finite Picard group of G^reg leaves no room for the relatively ample class that a projective resolution
    isomorphic over G^reg would need.
  - So the base change by the Weyl cover T → T/W is necessary.

**Checks** (CHECK_EVENTS.tsv):
- (iii), codimension ≥ 2: re-derived from the dimension formula of §1.4 and the bound dim{x : dim Z(x) = r + 2i} ≤
  dim 𝔤 − 2i − 1 for i ≥ 1. The preimage of that stratum has dimension at most dim 𝔤 − i − 1.
- The lemma Pic(T) = H¹(Γ, M): re-derived.

**Status:** the theorem is stated with proofs of (ii) and (iv), and references (Steinberg; EGA IV 21.4.13) for (i) and
(iii). Questions 0)–g) are open on the page.

**In today's terms:** Grothendieck's simultaneous resolution, known from Brieskorn (ICM Nice 1970) and Slodowy (LNM
815, 1980), there credited to Grothendieck (from memory). The over-a-base form and the Pic statements are worth
comparing with the published accounts (package R20-1).

### 1.2 Kostant's theory, in his summaries (C123-01, 123/002–003 and 016–020; K123-03, 041–048)

**Coxeter elements (002–003).** These are his complements to Kostant.
- The eigenvalues of any w ∈ W have order dividing some m_i + 1, so at most h.
- w has an eigenvalue of order h iff w is a Coxeter element, and then the eigenvectors are regular.
- **Corollaries:**
  - the centralizer of c is μ = ⟨c⟩ ≅ Z/h;
  - ν/μ ≅ (Z/hZ)*, where ν is the normalizer;
  - an eigenvector of c is regular iff its eigenvalue is a primitive h-th root of unity;
  - the cyclic lines are W-conjugate, |W|/h in number, and (Z/hZ)* acts freely on them.
- His margin asks "Quelle extension de (Z/hZ)* par Z/hZ obtient-on ?" (hunch H20-3).
- **Checks:** the necessity argument for regularity and the count |W|/h are re-derived (CHECK_EVENTS).

**Kostant's theorem on Dynkin pairs (016–017; a typescript with handwritten additions).**
- (i) For e ≠ 0 nilpotent and x with e ∈ 𝔤(2), the following are equivalent:
  - a) ad(e)^k: 𝔤(−k) ≅ 𝔤(k) for all k ≥ 1;
  - b) ad(e) is surjective, plus a handwritten addition: x = f(x₀) for some f: SL₂ → G;
  - c), c′) x ∈ ad(e)(𝔤), resp. x ∈ ad(e)(𝔤(−2));
  - d) there is f: SL₂ → G with f(e₀) = e and f(x₀) = x, and f is unique.
  - **Slip:** b) is typed "ad(e): 𝔤(0) → 𝔤(−2) est surjectif", read on the scan image. ad(e) raises the degree by 2, so it
    should read 𝔤(0) → 𝔤(2), as he writes himself in (iii). The slip is in the typescript.
- (ii) The f's through e are conjugate under Z = Cent(e); for e ≠ 0 they form a torsor under the unipotent group
  Z⁺ = Z ∩ U, and the x's an affine space a + (𝔤^e ∩ Fil¹), corrected by him from a + 𝔤^e.
- (iii) For a Dynkin x, the e's form the open set 𝔤(2)* ⊂ 𝔤(2), homogeneous under the reductive L = Cent(x).
- (iv) P (with Lie P = ⊕_{k≥0} 𝔤(k)), U and L are determined by u = exp(e); ad: U ≅ x + Fil¹, and U → e + Fil³ is
  surjective.

**Filtrations of the forgetful functor (018–020).**
- **The dictionary:**
  - A class c of filtrations, compatible with ⊗, of the fibre functor on finite-dimensional representations is a
    Γ-invariant element of M/W in the Weyl chamber.
  - The scheme Φ_c of such filtrations ≅ Par_{c′}, an open piece of the scheme of parabolics.
  - ST_c (the homomorphisms G_m → G of class c) ≅ (CL)_{c′} (Levi pairs).
  - In characteristic 0 ("j'ignore dans quelle mesure c'est vraiment nécessaire"): Dyn_c (SL₂ → G of class c) is
    homogeneous with stabilizer Z₀.
  - Un_c is the class of unipotents, and "Deligne nous fournit Un_c → Φ_c": the filtration attached to a unipotent.
- **The consequence:** a rational parabolic of a "Dynkin–Kostant" class forces G to be quasi-split. The argument works
  over a semi-local ring.
- **His NB for outer forms:** one must know whether c ↦ c′ (Dynkin class ↦ parabolic class) is injective. The margin
  says "Il n'est en effet pas le cas, p.ex. pour A₂, A₄ (cela l'est pour A₃)".
  - Check (sweep 3, correcting my sweep-2 part-1 event): c ↦ c′ is not injective for A₃ either.
  - In sl₄ the classes [3,1] (weighted diagram 202) and [2,1,1] (101) both give the parabolic P_{α₂}.
  - For A₂ and A₄ the collisions he means are regular/subregular, both giving a Borel (his margin on 020: "les
    paraboliques associés aux unipotents 'sous-réguliers' sont des Borels"); that part is right.
- **The principal case (020).** The principal class has P a Borel and Z₀ = 1; the converses fail (A₂, A₄).
- **What it anticipates:** the programme he draws, "déterminer exactement les classes de sous-groupes paraboliques de
  Dynkin–Kostant … et leur stabilisateur dans Autext(G₀)", is the theory of nilpotent orbits over non-closed fields and
  the Deligne filtration (my identification).

**Kostant's results over a base (K123-03, 041–048).**
- (i) The principal homomorphisms G_m → G (coordinates all 1 in the coweight basis, that is ρ^∨) correspond to Killing
  pairs. The normalizer of a principal rank-1 torus is N₀(T) ⊃ T, of index 2 (through w₀).
- (ii) Kostant homomorphisms κ: μ_h → G. The Z/h-grading has degree 0 = 𝔱, and 𝔤¹ = ⊕_{α ∈ Σ ∪ {−ψ}} 𝔤_α has rank
  r + 1. The stabilizer W_κ has the order of the centre of G̃, "isomorphe à P/R ou à son dual".
  - On 041 c) he had guessed the centralizer of a principal regular element is "probablement T"; 046 corrects this.
  - Re-derived: W_κ ≅ Ω ≅ P^∨/Q^∨, the stabilizer of the point of the fundamental alcove with equal Kac coordinates.
- (iii) Kostant (characteristic 0):
  - a) Σ x^α with all x^α ≠ 0 is semisimple regular;
  - b) with one x^α = 0 it is nilpotent;
  - c) such lines are T-conjugate, with stabilizer κ(μ_h).
  - His margin asks "nilpotente régulière ssi tous les autres ne s'annulent pas ?". My answer: only when the vanishing
    node is in the Ω-orbit of the affine node (label 1). In type A every node is. In general a zero at a node of label
    > 1 gives a distinguished nilpotent that is not regular (G₂, E₈). This is my reasoning, to check (R20-2).
- (iv) Cyclic lines: their centralizer is a maximal torus T′; Norm(D)/T′ ≅ μ_h is generated by a Coxeter element.
- 041 (a)–(b) mix two normalizations. The "admissible" homomorphisms have components 0, 1, 2 (Dynkin's α(h)), and "all
  components 1" is called principal. But the principal Dynkin element has all components 2; all 1 is ρ^∨ = h/2, which is
  his principal homomorphism of 044. Recorded as a refinement.
- 042 e): the stabilizer of a pair (T, g) with g a Coxeter element is an extension of W^σ by T^σ ≅ P/(1−σ)P(1), since
  H¹(Z/h, T) = 0. Re-derived: 1 − σ is an isogeny, and N = Σσ^i is 0 on X_*.

### 1.3 The homogeneous spaces and the rigidifications (K123-02, 024–035)

- **The tables (026, 027, 029).** A table of homogeneous spaces under G: Kostant elements, Coxeter elements, Kostant and
  Coxeter subgroups, pairs, tori in opposition, cyclic lines, Kostant–Killing pairs and their normalized forms. Their
  stabilizers run from Z·T down to 1.
  - Margin: "Valid. seulement en Car. 0 (ou car. p > h ?)".
  - The subgroup lattice: N ∩ N′ is an extension of (Z/hZ)* by μ_h × Z; its two halves lie in W′ and W, "des
    sous-groupes remarquables" of a Weyl group.
- **031.** "À prouver": every element of T normalizing D lies in κ(μ_h). He reduces it to the lemma
  det(I + 𝟙·nᵀ) = 1 + Σ n_i, with ψ = Σ n_i α_i.
  - **Re-derived:** a torus element normalizes k·(Σ e_{α_i} + e_{−ψ}) iff (α_i + ψ)(t) = 1 for all i. The matrix of the
    characters α_i + ψ in the basis α_j is I + 𝟙·nᵀ, of determinant 1 + Σ n_i = h. So the kernel in the adjoint torus has
    order h and equals κ(μ_h).
  - **His proof is complete.** The transcription's first entry of row 2 ("n₂|n₁|nx") must read n₁, and the last row
    (n₁, …, n_{r−1}, n_r + 1); the transcribed "n_r n_r …" is a reading to correct by the mathematics.
- **034.** Kostant's recollections, then a question:
  - cyclic lines mod μ_h* define a canonical line Δ over k, with Δ^{⊗2} ≅ 1;
  - "Il serait intéressant de calculer la repr. de E [outer automorphisms] sur Δ … et la comparer avec le car. provenant
    de la repr. de E sur 𝔤_ψ"; "A-t-on … un isom can 𝔤_ψ ≅ Δ ?" (package R20-2).
- **035, "Rigidifications de Kostant".** RigKos is the scheme of (T, T′, B, B′) with T, T′ in opposition and B ⊃ T,
  B′ ⊃ T′, for (h, p) = 1.
  - It is smooth, G acts freely, and RigKos/G is finite étale of rank w²/(φ(h) h z). It is split: Q × Q′ modulo
    Φ = N ∩ N′.
  - E acts through its sign on 𝔤_{−ψ}.
  - **Re-derived:** the count follows from the transitivity on pairs in opposition (Kostant), |N ∩ N′| = h z φ(h) (his
    diagrams), and the free action on Q × Q′ (T ∩ T′ = e).
  - It is the count of the letter.

### 1.4 The letter to Kostant (123/022–023, "Massy 22. 10. 1969"; SA20-W4)

Read on the images; see `sweep2/REPORTS/letter_to_kostant_123.md`. The letter has three parts.
- **The rigidifications** of §1.3 and the count card(W)²/hzφ(h). The count is derived on 035; re-derived (§1.3).
- **Subregular orbits:** the rank of the tangent map of 𝔤 → 𝔥/W at subregular points, with A–D–E ↔ Klein singularities
  (Brieskorn).
- **The dimension conjecture:** if the orbit of x has dimension 2N − 2i, the Borels containing x form a variety of
  dimension i. That is dim Z(x) = r + 2 dim B_x.
  - Literature, checked tonight against a survey abstract: Douglass and Röhrle, "The Steinberg variety and
    representations of reductive groups" (arXiv:0802.0764, 2008), say that Steinberg's insight "was to use such a
    variety of triples in order to prove a conjectured formula by Grothendieck".
  - The formula was proved by Steinberg (Invent. Math. 36 (1976) 209–224) and by Spaltenstein.
  - So the letter is a primary source for "Grothendieck's conjecture" on the dimension of Springer fibres. Steinberg's
    paper itself was not opened.
- **Rational singularities:** the inequality ≤ i would give rational singularities of the fibres, by a depth argument of
  Brieskorn.
- **His guess** that a single subregular orbit characterizes the simply-laced case is refined: the subregular class is
  unique in every type (Steinberg 1974, from memory).

### 1.5 Dependencies (closed by reading; DEPENDS.tsv)

| Item | Uses | Shown on |
|---|---|---|
| SA20-W1 (simultaneous resolution) | Kostant's quotient map (generic fibre), Steinberg (finiteness of fibres, codimension 3), Springer PM 30 §5.3, EGA IV 21.4.13 | 006, 007, 011, 012 |
| SA20-W3 (principal subgroups) | Kostant 1959, "The principal 3-dimensional subgroup …, Am. J. Oct. 1959, 3.4, 3.5, 3.6, 1.2, 9.3" | 016 |
| | Coxeter theory (002, "th. 9.2"); the determinant lemma; Deligne's filtration (019) | 002, 019, 031 |
| SA20-W4 (letter) | W1 (question g) on 007) and W3 (the count) | 035; the cover 015 "Résumé th. de conjugaison Kostant + lettre à Kostant" |
| SA20-17 (Tannakian duality) | linked to W3 by subject: filtrations of the fibre functor | — |

### 1.6 The transcriptions (DELIVERABLES.tsv)

- **Passes:** one Codex web transcription per folder, plus the Codex notes on the sheets and Work's math notes.
- **Checked here:**
  - the letter and the 016 conditions against the images;
  - the mathematics of all five folders, read in full.
- **Open readings:**
  - the matrix rows on 031 (decide by the mathematics: n₁ in row 2, and the last row);
  - minor accents and abbreviations throughout.
- **Ready for an edition and translation:**
  - the letter (two typed pages) and the 016–017 typescript: ready now;
  - the handwritten sheets: after one ink pass on the \unsure marks.
