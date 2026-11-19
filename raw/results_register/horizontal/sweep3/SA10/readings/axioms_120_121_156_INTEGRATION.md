## STUDY

**The axiom systems of cotes 120, 121 and 156 against each other** (Claude Opus 5.5 at effort max, aff4deb18a6ec3192, for
a6d42bf6fe2b0d8a8, 19 Nov 2026; full working `readings/axioms_120_121_156.md`). Sources: the readings of cote 120
(ac69efa38b3a951d7), 121/49-73 (mine), 121/1-48 (a9e0641820ca2be57, in progress) and cote 156 (SA21); every correspondence
below was checked on the transcriptions of both sides (16 check events).

**Three kinds of system.** Coordinate families M_n ⊂ P(Rⁿ) (cote 120; 121/054-073); one space with a Boolean family of
subsets (121/004-017; the admissible partitions of 121/049-052); and the pointless figures, contrées and ateliers of 1986
(cote 156). The closed-strata axioms a)-d) of 151/45-52 (1981) link the second and third.

**120 against 121 (coordinate families).**
- 120's M1 + M4 is 121/070's C_* a)-d). 120 adds M2 (inverse images along diagonals) and derives intersections, the axiom
  whose absence leaves 121/070's intersection Proposition unprovable.
- M6 and M7 are 121/061's 6° (zero loci) and 5° (extension). The pushout theorem of 120/013-014 is 121/061-062, and it
  answers the question 121/073 leaves open ("à tirer au clair"). The separation clause of M6 comes, in both cotes, from the
  same products (121/067-068; 120/023-024).
- M11 (x − y, xy, inverses) is the correct form of 121/056's field claim, which fails under 1° and 2° alone.
- The reconstruction of 120/008 needs conservativity and an image axiom (ac69efa38b3a951d7). 121/059 Ⓐ-Ⓑ gives the exact
  form: images along maps mono on the set; all images (M1) correspond to Ⓑ, effective-epi images preserved by the functor.
- Compactness, neighbourhood bases, the sheaf of moderate maps, locally moderate spaces and M8 match 121/071-073.
- At each gap or question of 121/054-073 (intersections, the pushout, the field, the image axiom), 120 has the repaired
  statement. By content, 120 consolidates the 121 drafts; no page is dated.
- None of these systems excludes wild compact sets. Only the triangulation axiom of 121/065 gives finiteness in dimension one.

**One space (121/004-017).** The only system in 120-121 with complements and finitely many components (the ingredients of
o-minimality), on one space only. Its existence theorem (015-017) proves the coarsest admissible decomposition, starting from
the complement of the union of the boundaries: the first open stage that corrects 121/049. Cor 2 of 016 gives coarsest
common refinements. 121/014: finite stratifications are open maps onto finite T₀ spaces.

**Closed strata, 1981-1986.** 121/052 II is 151/45-52 a)-d) plus rarity of proper inclusions; 156-4/2-3's figure is 121/052
II clause by clause, plus non-emptiness (the proviso missing on 052), local compactness, connected manifold strata and a
dimension condition. 156-4/2 places its model explicitly in "un espace modéré … pour une théorie modérée donnée", the
moderate space of 120/020 and 121/072.

**156 against 120-121.**
- **"Contrée modérée" (156-4/70)** is the existence of common subdivisions. It fails in the topological model (a diameter and
  an arc crossing it infinitely often), holds in o-minimal models by the stratification theorem, and is Cor 2 of 121/016 in
  the Boolean setting. It is the common-refinement property of tame geometry, not the Hauptvermutung.
- **The Inf for ≪ (156-5/29)** is the same corollary; 156-4/70's "parfois un inf" fits, because the coarsest decomposition
  of 121 need not have manifold leaves.
- **Intersections (156-3/20)** exist only "en position relative modérée" in 1986; 120 derives them for all pairs and 121/070
  asserts them. So the coordinate systems exclude the non-mutually-tame pairs that 156-3 allows on non-total tronçons.
- **Faithful ateliers (156-9/4):** every atelier built from a 120-121 tame space is faithful, and in 121/004 its supports
  form a Boolean algebra.

**Hunches tested:** H7 confirmed; H2 refined (its identification with the Hauptvermutung refuted); H9-3 confirmed for spatial
models; H5-4's second clause corrected. **Dependencies:** the candidate SA21-13 row is replaced by read rows, with 12 more.

## HUNCHES

**HAX-1. Cote 120 is the fair copy of the 121 coordinate drafts** (confirms H20-121_049-073_153_155-2 in substance).
- *Grounds:* the four repairs (M2 for 121/070; M6-M7 for 121/073; M11 for 121/056; the conservative reconstruction of
  121/059 behind 120/008), all checked on the pages.
- *To settle:* the dates (120/002's pencil "1978" is a label; 121/041 and 067 carry notes to Fujii Guruji Nichidatsu).

**HAX-2. 156-4/70's "contrée modérée" is the common-refinement axiom of tame geometry; the Hauptvermutung is the
strengthening his margin announces** (refines H2 and H5-4; supports H6-2).
- *Grounds:* the disc counterexample in the topological model; the o-minimal stratification theorem; Cor 2 of 121/016.
- *Test:* the strengthening needed for At 14 of 156-6 (extension of subdivisions), where uniqueness of the PL structure
  (Shiota) is the natural requirement.

**HAX-3. The Boolean setting of 121/004-017, coordinated across products and projections, would be an o-minimal structure.**
- *Grounds:* complements, finitely many components (f), finite chains (e) on each space, and coordinate closure in cote 120.
  Joining them over all Rⁿ is the missing step: a family of Boolean algebras on the Rⁿ, closed under coordinate images and
  inverse images, with f). Finitely many components on R is the o-minimal condition.
- *Links:* SA20-10 (prompted question 3), SA21 H3-1 (156-3's tame line is o-minimal), the Pro notes TC12-TC14.

## PACKAGES

**P-AX1. One axiom system for tame geometry from cotes 120, 121 and 156.**
- **Question:** state the system that HAX-3 describes (Boolean families on all Rⁿ with M1-M4, M5, compactness and the
  component axiom f)), prove or refute that it is the definable sets of an o-minimal structure, and derive from it the
  canonical decompositions (121/015-017), the gluing (120/013-014), and the contrée axioms of 156-4 including "modérée".
- **Why:** the three cotes come at tame geometry from three sides; none has the whole. This is the precise form of SA20-10
  and of SA21's P2 (the o-minimal contrée).
- **Rests on:** this comparison; the readings of 120, 121/1-48, 121/49-73 and cote 156.
- **Strongest known reduction:** 120 derives intersections and gluing; 121/015-017 proves the canonical decompositions on
  one space; 121/065's triangulation gives finiteness in dimension one; 156-3 gives o-minimality on lines.
- **Material:** the three Pro packages, the 156 Codex returns, and van den Dries (1998), van den Dries-Miller (Duke Math. J.
  84, 1996), Shiota (1997), Pillay-Steinhorn (1986).
