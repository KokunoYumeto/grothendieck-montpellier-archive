# SA22: hunches (sweep 3)

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. Each hunch gives what may be true, its grounds (the
pages), and its links. "From memory" marks literature not opened tonight.

## Cote 66, the thesis problems of 1964

**H22-1. Subject 21 is the affine analogue of proper base change, proved thirty years later.**
- *What it says:* for X = Spec A with A I-adic, separated and complete, he asks when H*(X, F) → H*(X₀, F₀) is an
  isomorphism in étale cohomology.
- *Grounds:* 66/004.
- *The answer:* for a henselian pair (A, I) and torsion coefficients the map is an isomorphism. Gabber, "Affine analog
  of the proper base change theorem", Israel J. Math. 87 (1994); Fujiwara, Duke Math. J. 80 (1995). From memory.
- *Link:* the "Pour mémoire" diagram on the same sheet (purity, regular base change, finiteness) is the programme Gabber
  completed.

**H22-2. Subject 15 asks for homotopy groups of topoi with infinitesimal coefficients.**
- *What it says:* the homotopy type of a topos "incluant une définition des π_i à [coefficients, struck] … infinitésimaux".
- *Grounds:* 66/003. The word before "infinitésimaux" was read on the image: "nouveaux" or "noyaux"; it has no
  descender, so "noyaux" is less likely; not decided.
- *What it anticipates:* Artin–Mazur did the étale part (his margin says so). The infinitesimal part points to de Rham
  and crystalline homotopy types: Toën's schematic homotopy types, and Katzarkov–Pantev–Toën. From memory.
- *Links:* Pursuing Stacks; subject 8's "lien avec 'cristaux'".

**H22-3. The "pb du carré" (subject 25, first question) has a negative answer by exterior products.**
- *The argument* (from memory):
  - On E × E, for an elliptic curve E over C, pr₁*(p − q) and pr₂*(p′ − q′) are algebraically trivial divisors.
  - Their product is the 0-cycle (p − q) × (p′ − q′). It is Albanese-trivial.
  - Such products generate the Albanese kernel T(E × E), which is nonzero by Mumford.
  - So some products of two algebraically trivial cycles are not rationally trivial, and the square of
    x = pr₁*(p − q) + pr₂*(p′ − q′) is 2·(p − q) × (p′ − q′).
- *Grounds:* 66/005; his own margin "faux, cf Mumford" is on the neighbouring question.
- *To check:* Bloch, *Lectures on algebraic cycles* (1980), lecture 1.

**H22-4. Subject 24, second question, is still open.**
- *What it says:* numerical against homological equivalence for 2-cycles on fourfolds. This is the standard conjecture D
  in its first open case.
- *Grounds:* 66/004, the inserted line "En dim 4, cycle de dim 2 équiv. num = équiv. hom ??".
- *Assessment, revised 19 Nov:* over a field of characteristic 0 the answer is yes, by Hodge theory (my sketch, to be
  checked by RESEARCH_SA22, B.1):
  - an algebraic class in H^4 has algebraic Lefschetz components, by hard Lefschetz and the Lefschetz (1,1) theorem;
  - the decomposition is orthogonal;
  - the intersection form is definite on each part: the Hodge index theorem on primitive divisor classes, and
    Hodge-Riemann on primitive (2,2) classes.
  So the form is non-degenerate on algebraic classes. In positive characteristic this is the first open case of the
  standard conjecture D.

**H22-5. The list is a map of the SGA programme in 1964, and its margins of about 1968–71 record its progress.**
- *What it is:* subjects 1–10 became SGA 4, 5 and 6 and their sequels; 11–13 Néron models (Raynaud); 14, 15 and 22
  topoi, étale homotopy and Tannakian categories; 27 and 28 adèles and motives over a base.
- *What it is good for:* a historical deliverable in its own right, for Part V of the handbook.

## Cote 67, conformal surgery (1976–78, 1983–84)

**H22-6. The 1984 capping is the cusp-coordinate and decorated picture, and his g = 0 worry dissolves.**
- *What may be true:*
  - At each puncture a of a hyperbolic surface, the complete metric has a cusp coordinate z, unique up to rotation, in
    which it reads |dz|²/(|z| log|z|)². Its derivative gives a canonical Hermitian norm on T_{X,a}.
  - This is the "canonical Euclidean metric on T_{X,a_i}" that he expects on 069–070. It exists for every hyperbolic
    punctured surface, a sphere with ν ≥ 3 punctures included.
  - His principal (R*⁺)^I-bundle TB_{g,I} → T_{g,I} with a canonical section cannot exist as conjectured on 068–069.
    The shadows of the capping discs are bounded (Koebe's quarter theorem; Michel Hua's project, re-derived by reader
    67_003-046_084-101), and the letter to Bers withdraws the conjecture (019).
  - What keeps the shape of Penner's decorated Teichmüller space (a horocycle at each puncture, 1987) is the space of
    horocycle decorations, with the cusp norms as its canonical section. Restated 19 Nov.
  - The norms are the Hermitian metrics on the tautological lines ψ_i studied by Wolpert and by Takhtajan–Zograf.
  - All literature here is from memory.
- *Grounds:*
  - 067/061–070: projective and toric structures on boundary circles, the shadow o(D), admissible disc systems, the
    "Conjecture" of 068–069, and "semble étrange" for g = 0 on 070;
  - the letter to Bers (016–021) asks the same questions.
- *Links:* SA30-9 and SA30-10 (cote 146, sewing in the Teichmüller tower); the Lego of the Esquisse.

**H22-7. Nothing after 073 depends on "rectifiable"; with smooth gluing the programme of 074–082 stands as written.**
- *What may be true:*
  - The welding statements (Th. 4, Lemma 4 B, the Scholie of 073) are right for quasisymmetric gluing maps: existence by
    the fundamental theorem of conformal welding (Pfluger 1960; Lehto–Virtanen, ch. III), and uniqueness because
    quasicircles are removable.
  - For "rectifiable" only the uniqueness half survives: rectifiable seams are removable (his Lemma 3 c).
  - From 074 on he glues smooth (even real-analytic) boundary circles. There the glued complex structure comes from
    charts and Schwarz reflection, with no welding theorem at all.
- *Grounds:*
  - 067/059–061 and 072–073 (the "rectifiable suffit" clauses);
  - 074 ("avec la condition différentiable").
- *What would refute it:* a step after 073 that uses a non-smooth seam. I found none in 074–083.

**H22-8. The anabelian sheets of January 1984 ask for what later became combinatorial anabelian geometry.**
- *What may be true:*
  - 049 b), recovering the nodes and marked points of a stable curve from the Ẑ-subgroups on which π₁(K) acts through
    the cyclotomic character, is the group-theoretic recognition of cuspidal and nodal inertia. This is the subject
    of:
    - Nakamura's Galois rigidity (1990);
    - Mochizuki's semi-graphs of anabelioids (2006);
    - Hoshi–Mochizuki on nodally nondegenerate outer representations (2011).
  - 048, the Teichmüller isomorphism for Y with a normal propagator and its failure to be Galois-equivariant, is the
    tangential base point at a boundary point of M̄_{g,ν}, as in Ihara–Nakamura on maximally degenerate curves and
    Oda's problem (1997).
  - 049 c), "compactification anabélienne … comportement par spécialisation", has no single answer in the literature
    that I know of.
  - All from memory.
- *Grounds:*
  - 067/048–051;
  - the dating (15.1.1984) puts them in the weeks of the Esquisse and of the welding notes.
- *Links:* SA28, SA31-7, SA31-9 (the anabelian parts of La Longue Marche), and the research runs on those.

## Cote 68

**H22-9. The axioms of 68/017 are meant to give "Condition K"; his question asks which groups carry such a system.**
- *What may be true:*
  - A system of totally ordered families 𝒜(g̃) of finite sets, symmetric up to translation and closed under
    convolution into the cones C(g̃h̃) (017 a)–d)), gives Condition K for the convolution-stable family it spans
    (021–022).
  - Then the rearrangement inequality for three functions, Σ f(a)g(b)h(c) over a + b + c = 0 maximized by the
    arranged functions, holds in every group with such a system.
- *Grounds:*
  - the model case on 017, symmetric intervals in a cyclic group;
  - the proof begun on 022, which stops where a common point of all level sets is needed;
  - the S₃ example of the notes, which shows the property is not general.
- *Literature, from memory:* Hardy–Littlewood–Pólya, Inequalities, ch. X (ℤ); Gabriel 1932 (cyclic groups); discrete
  Riesz–Sobolev results on ℤ/pℤ (Lev's name comes to mind; unverified).
- *Links:* the convolution scratch strings of 015–016; SA23-39 (H0DS) for the games of the same folder.

**H22-10. The games are a complete, choice-based proof of positional determinacy for reachability games, written as a
course.**
- *What may be true:*
  - The second draft (024–034) proves the Zermelo and Gale–Stewart theorem for reachability games with positional
    strategies, by a well-order device in place of ordinal ranks.
  - With the kernel characterization on 034 it is a finished teaching text.
- *Grounds:* 026–030, re-derived tonight; 048 restarts with N players.
- *Use:* a deliverable for the edition, not a research question.

## Cote 67, scans 003-046 and 084-101 (reader 67_003-046_084-101: af3526fc4890c92f1, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader `67_003-046_084-101` for ae4ae3dc, 19 Nov 2026. Each hunch gives what may be
true, its grounds (the pages), and its links. "From memory" marks literature not opened.


### The letter to Bers: admissible capping of pants (67/016–021)

**H22-67_003-046_084-101-1. With two cusps and a long boundary, the capped disc tends to Koebe's slit domain.**
- *What may be true.* Take the pants C(L, 0, 0) (one geodesic boundary of length L, cusps labelled 1 and ∞), capped at
  0. As L → ∞, the disc D₀ converges (Carathéodory kernel convergence at 0) to Σ ∖ [1, +∞]. Its conformal radius at 0
  tends to 4 in the coordinate z, the extremal value of Koebe's quarter theorem. So the true picture behind his
  "orange slices" is a slit, not a cell.
- *Grounds:*
  - **Koebe.** For every admissible system, r(D₀, 0) < 4. This bound is the one in Michel Hua's project, §VIII, footnote,
    and I re-derived it (CHECK_EVENTS).
  - **Symmetry.** D₀ is invariant under z ↦ z̄ and under the reflection in |z − 1| = 1 (the cusp-exchanging symmetry of
    C(L, 0, 0), z ↦ z/(z − 1) composed with conjugation). So D₀ ∩ ℝ = (−b/(1 − b), b) with 0 < b < 1. Any limit
    complement that is an arc from 1 to ∞ avoiding 0 and stable under conjugation is [1, +∞]: an involution of an arc
    that fixes both ends is the identity.
  - **Degeneration.** In C(L, 0, 0) the orthogeodesic α from the boundary to itself, separating the cusps, has length
    → 0. The boundary circle then splits into two arcs of length about L/2, one per cusp lobe. Each arc is a long spike
    side on either end and a body part of length O(1) in the middle.
  - **Harmonic measure matches.** The cap's harmonic measure from 0 is arclength. It gives about ¼ to each of the four
    spike sides and o(1) to the bodies. For Σ ∖ [1, ∞] (z = 4w/(1 + w)², boundary z = sec²(θ/2)) the four half-sides
    of [1, 2] and [2, ∞] each carry harmonic measure ¼ from 0, and the tips none.
- *What would refute it:* a sequence of caps whose complements keep a "body" of positive area at 1 or at ∞. That would
  put harmonic measure bounded below on the body arcs, against the arclength count.
- *Links:* SA22-6 and SA22-7 (062–069, the shadows; ae4ae3dc's reading); R22-2. Pro's notes S19–S21 on 053–083 (the
  dependence on the lengths, the failed surjectivity, simultaneous realizability).

**H22-67_003-046_084-101-2. The set of admissible radii is not the box his letter expects.**
- *What may be true.* On 019 he expects the admissible radii to be exactly {r_i < ρ_i}, with independent bounds. They
  are not: the radii are coupled.
- *Grounds:*
  - Lavrentiev's inequality for non-overlapping simply connected domains, r(D₀, 0)·r(D₁, 1) ≤ |0 − 1|² = 1 (from
    memory; equality for the two half-planes Re z < ½, Re z > ½).
  - The configuration is S₃-symmetric, so a box would need ρ₀ = ρ₁ ≤ 1 in the coordinate metrics.
  - But by H22-67_003-046_084-101-1, r₀ alone approaches 4 when the other two discs are degenerate. So no box. It is
    enough that some admissible D₀ has r(D₀, 0) > 1.
- *Status:* conditional on H22-67_003-046_084-101-1, or on any admissible system with r₀ > 1.
- *Links:* his own reservation on 019 ("does'nt quite match"); Pro's S21 ("simultaneous realizability").

**H22-67_003-046_084-101-3. Each disc depends on all three lengths; his doubts on 020 and 068 are right.**
- *What may be true.* In an admissibly capped pair of pants, D_i depends on all of (ℓ₀, ℓ₁, ℓ_∞), not on ℓ_i alone. This
  is the "?" on 068 and the "Maybe it is unreasonable to expect …" of 020.
- *Grounds:* the coupling of H22-67_003-046_084-101-2. If D₀ depended only on ℓ₀, then for large ℓ₀ (D₀ near the slit
  domain, r₀ near 4) the discs D₁(ℓ₁) and D_∞(ℓ_∞) would have to fit, for every ℓ₁, into the thin complement. Lavrentiev
  then forces r₁ ≤ 1/r₀ for all ℓ₁, against r₁ → 4 as ℓ₁ → ∞ with the others degenerate.
- *Status:* conditional on H22-67_003-046_084-101-1 applied at each puncture. It settles R22-2 (a) negatively if that
  hunch holds.

### The metric dossier (67/024–046)

**H22-67_003-046_084-101-4. The NB on maps (039) is an early written form of the canonical metric of a map.**
- *What may be true.* The bracketed NB on 039 is the statement that a map on the sphere with no facet fixed by its
  automorphism group carries a unique invariant normalized round metric. It is the spherical case of the canonical
  geometry of a map that the Esquisse d'un programme (January 1984) describes for dessins (from memory: the canonical
  spherical, Euclidean or hyperbolic structure of a map). The NB reads "On pense notamment au cas où X est associé à
  une carte, et H est le groupe des autom. de cette carte, qui est fini — … pas de facette de la carte fixe par H".
- *Grounds:* 039, with "carte" read on the image; the Proposition of 037; my re-derivation of the fixed-facet criterion
  (CHECK_EVENTS).
- *Use:* a dated or datable source for the "cartes" material of the Esquisse. The dossier is undated; its paper and
  vocabulary place it in 1983–84 (my inference). To compare with the dessins and maps topics of the archive (cotes
  142, 148; the La Longue Marche readers), not read here.

### The real elliptic curves (67/091–101)

**H22-67_003-046_084-101-5. The sheets rederive Alling's classification of real elliptic curves, and extend the
classification of ℤ[C₂]-lattices to principal rings.**
- *What may be true:*
  - 093–101 give the classification of real elliptic curves by lattices with involution (two families, the real loci,
    the torsors E_a^!) as in N. L. Alling, *Real elliptic curves* (North-Holland Mathematics Studies 54, 1981; from
    memory).
  - 091–092 and 100 classify involutions of 2-regular modules by (P, Q, m). Over ℤ this is the classical classification
    of ℤ[C₂]-lattices (trivial, sign, regular: Diederichsen; Reiner; from memory). Over a principal ring with k/2k a
    field, the non-split classes are k₀^×/im(k^×) (re-derived; Pro's E04–E05).
- *Grounds:* the re-derivations in CHECK_EVENTS; the dates Déc 83 (091) to 9.2. (101).
- *Use:* the edition's notes should cite the classical results, not claim them as new.

### The octahedron (67/084–089)

**H22-67_003-046_084-101-6. The Theorem of 089, with the twisted model X(I), is a characteristic-free description of
M_{0,[4]} over ℤ[½, i].**
- *What may be true:*
  - The groupoid of four-pointed projective lines over a base on which 2 is invertible and −1 has a chosen square root
    is equivalent to the groupoid of pairs (I, ζ ∈ Z(J(I))*): a V(I)-gerbe over the quotient of P¹ ∖ {3 points} by 𝔖₃.
  - The canonical model is X(I) = ℙ¹ ×^{Γ₀} Isom(I, I₀).
  - Characteristics 3 and 5 need no exception for the Theorem. They affect only the Proposition of 086 (characteristic
    5) and the 6 + 12 + 8 picture (characteristic 3).
- *Grounds:* my re-derivation that the Theorem uses only V(I) and X/V ≅ Z(J) (CHECK_EVENTS); Pro's O07 (the
  orientation torsor as a descent datum) and O15 (the octahedral cover of the Fermat conic in La Longue Marche, LM_140-2
  scans 363, 549–571, not read here).
- *Links:* SA22-5 (051, T⁺_{0,4} and 𝔖̃₄); SA30-2 (the four-point model); SA28-15 and SA29-18 (platonic
  configurations).
