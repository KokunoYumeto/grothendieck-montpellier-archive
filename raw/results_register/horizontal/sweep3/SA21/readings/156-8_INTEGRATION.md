## STUDY

**156-8, "Analysis Situs (quatrième mouture)", CF VIII, 26 June - 4 July 1986, scans 2-127 (SA21-15).**
- Read in full by Claude Opus 5.5 at effort max (reader C, sub-agent of a6d42bf6fe2b0d8a8); scans 4, 6, 31, 32, 86 checked on the images.
- His page p is scan p + 9 from p. 3 on. Scans 5, 7: Récoltes et Semailles typescript.

**The magasin replaces the atelier.**
- The data are (M, ≤, ≪, |∘|) with Mag 1-4 (scan 8), the |∘|-magasin of 156-7/111.
- From these four axioms alone he proves, and I re-derived:
  - compatible + ≪ ⇒ ≤ (156-6's At 5);
  - the transitivity of ≪° (At 7);
  - the induced refinement as Inf for ≪;
  - the compatibility and disjunction of refinements tested on the intersection (156-7's "axiomes obligatoires" At CD);
  - the gluing of refinements (At 11, 156-4's C7) (scans 10-14).
- This is what "l'innovation d'avant-hier faisant tomber tout le fouillis des axiomes de compatibilité-disjonction" (scan 31) means.
- Figures are the ≤-closed sets whose distinct elements are pairwise |∘|.

**28 June, "l'épurement intégral".** The primitive data become (M, ≤, ≪°, |∘|), with Mag 1′-4′ (scans 29-31); ≪ is recovered as "X ≪° Y′ ≤ Y".
- **His Mag 4′ is in the "comparable" form** (read on the image; Codex's "¬" is a struck false start). That form is too weak: in the maquette y, z < X with |∘| = {y–X, z–X}, X̃ is not a figure. The two-strata form of scan 8 is needed.
- The same weakening is in Magor 4 and Mag div 3.
- **The Proposition-Scholie of scans 16-17** (strictly divisible and pre-set-theoretic magasins from (≤, ≪) and a relation on the lieux) lacks the transitivity of ≪°. A five-element countermodel is computed. The ≪°-form repairs it.

**The classes (diagram of scan 3, written after 28 June):** general, local (|∘| from lieux), faithful (|∘| = no common ≪°-lower bound), ponctuaire (quasi-set-theoretic, Σ ≃ P(𝓛)), maquettes, set-theoretic, and tame set-theoretic.
- A maquette is a trivial magasin: an ordered set, a T₀ Alexandrov space (scan 34), ponctuel only if discrete.
- His margin: tame topologies "n'ont été développées à présent que pour la seule structure linéaire par morceaux sur ℝ".

**Oriented maquettes (scans 4, 6).**
- In dimension ≤ 1 they are Serre's graphs; Michel Hua's project gives the identification first, and I re-derived it.
- His "Sauf erreur" claim for dimension 2 is not right as stated. The axioms give 2-cells whose boundary is a vertex-disjoint union of directed cycles. The one-vertex torus is excluded, and cells bounded by two cycles are admitted. With "∂X connected" added, they are the 2-complexes whose cells are attached along closed edge paths through no vertex twice.

**Supports.**
- Support functions into a set P (scans 42-73): the indexed form of 156-5's Proposition 1 (scan 46 = "GF VIII pg 37"), its two infinite counterexamples (scans 53-54 = "pages 44, 45"), and the Théorème identifying homomorphisms into Figures(P) with support functions (scan 70).
- His own margin of 2 July withdraws the claim that faithful support functions always exist.
- Internal |∘|-supports (scans 74-89): Σ_M ≅ Σ_𝓛 under Mag L2, and P(𝓛) in the ponctuaire case.
- Axiome supp 1, the one-figure orthomodular law. He claims it for faithful magasins. **The claim is true, by a stronger fact:** for faithful magasins Σ_M is the complete Boolean algebra of regular open sets of the Alexandrov topology of (M, ≪°). His stated reason fails.

**1-4 July: the magasin of an ordered set L** (points P_x, segments S_{a,b}).
- It satisfies Mag 1-4 for every L. It is faithful iff L is total, and ponctuel iff L is total and divisible.
- P_x |∘| P_y iff x, y are comparable.
- The finite figures are the flags of flags, Drap(Drap*(L)).
- |∘| is the comparability relation of a positional order <_pos, the interval order when L is total (the name is Michel Hua's project's).
- Préfigures and constructible supports are classified (irredondant préfigures). The part breaks off in a complement duality (scans 126-127).
- This is the base of 156-9's restart: figures as flags.

**Counts:** 36 check events, 12 corrections.

## HUNCHES

**H8-1. Faithfulness is what makes the supports Boolean** (sharpens H3, H6, H7-2; corrected in the 156-9 reading).
- **What is proved:** for faithful magasins, Σ_M = RO(M, ≪°), a complete Boolean algebra (SA21-R8-25).
- **My first form is refuted.** "Distributive ⇔ faithful, under divisibility" fails for M = {x, y}, two lieux with |∘| = ∅: there Σ = {∅, M} is Boolean, yet the magasin is not faithful (SA21-R9-10).
- **The refined statement, re-derived in the 156-9 reading:** under divisibility and Mag L2, the magasin is faithful iff Σ_M is Boolean and x ↦ supp°x maps the lieux injectively onto atoms. That is his Question of 156-9/3 together with his presumption of 156-9/2-3.
- **The hunch that remains:** in the magasins of cords and strands (156-7/84, 156-8/90-127) the non-distributivity of Σ measures exactly the pairs of distinct lieux that are not disjoint.
- **Literature:** Halmos, *Lectures on Boolean algebras* (1963), §4 (locator to be checked); Kalmbach 1983.

**H8-2. Oriented maquettes are a combinatorial model of cellular chain complexes with ∂∂ = 0 built in** (sharpens H9, H7-1).
- Magor 6 a) is the signed diamond property.
- With "∂X connected", dimension 2 gives 2-complexes with simple attaching cycles.
- In every dimension the natural statement is: oriented maquettes with "every interval of length 2 is a signed diamond" and "the link of each cell is connected" are the regular CW complexes with an orientation of each cell, after excluding loops.
- **Literature:** Björner 1984 (locator to be checked); A. T. Lundell and S. Weingram, *The topology of CW complexes* (1969), ch. IV (locator to be checked).

**H8-3. His magasin of an ordered set is the comparability graph of an interval-type order, and the July restart (156-9) axiomatizes magasins whose |∘| is a comparability relation** (sharpens H10).
- **Grounds:** 156-8/106-107: X |∘| Y ⇔ X <_pos Y or Y <_pos X. 156-9/6-7: "X |∘| Y ⇔ X < Y or Y < X", and figures are flags.
- **The hunch:** the restart takes the "positional" order as primitive. Comparability graphs (Gallai 1967) and interval orders are its combinatorial theory.

**H8-4. Mag 1-4 are a first-order axiomatization in which every "facultatif" axiom of 156-6 and 156-7 except At L1, At supp and At 13 is a theorem** (sharpens P6-1 and P7).
- **Grounds:** SA21-R8-01 to -08.
- **What it predicts:** P6-1's open implications (At 9_Σ + At 10 ⇒ At 12; At 11 bis + At 11′ ⇔ At 11) become trivial in the |∘|-form. The open problems that remain are about lieux (divisibility) and supports.

## PACKAGES

**P8-1. The axiom of supports and the classes of magasins.**
- **The question:**
  - Decide Axiome supp 1 (156-8/88) in the magasin of an arbitrary ordered set. His margin "Oui !" on scan 89 says it fails for some disjunctive magmas, with no example on the page.
  - Measure the non-distributivity of Σ_M in the non-faithful magasins of cords and strands. The equivalence "faithful ⇔ Σ Boolean with lieux as distinct atoms" is re-derived under divisibility and Mag L2 (H8-1); the plain form "distributive ⇔ faithful" is refuted.
  - Find a faithful support function that is not fully faithful (his question, scan 88).
- **Why it matters:** the axiom of supports is the last "délicat" axiom of the magasin theory. Faithfulness is now shown to give Boolean supports, so the remaining question is exactly the non-faithful case of cords and strands.
- **What it rests on:** 156-8/74-127; 156-7/62-101 (reader B); SA21-R8-24, -25.
- **Strongest known reduction:** faithful ⇒ Σ_M = RO(M, ≪°), Boolean (re-proved here). Non-faithful counterexamples to distributivity and orthomodularity exist (156-7/84, 99).
- **Material:**
  - the 156-8 .tex with scans 74-127, 156-7 scans 62-101, and `156-8_checks.py`;
  - Halmos 1963; Kalmbach 1983; Birkhoff 1967, ch. V (locators to be checked).

**P8-2. Oriented maquettes and cell complexes in every dimension (refines P6 and P7-2).**
- **The question:** state and prove the classification of oriented maquettes (Magor 1-6, ≪° = id, |∘| = ≠) in every dimension.
  - Which axiom gives connected cell boundaries?
  - When is the structure a regular CW complex with oriented cells?
  - How do At pol 1 + At simp 1 (156-7/14-15) and the flags of 156-9 sit inside it?
- **Why it matters:** his own "Sauf erreur" claim (156-8/6) is now refined in dimension 2. It is the junction with finite T₀ spaces and the programme questions P01-P16.
- **What it rests on:** 156-8/4, 6; SA21-R8-32, -33; 156-7/14-15 (reader B); 156-9/5-7.
- **Strongest known reduction:**
  - dimension 1 = Serre graphs (exact);
  - dimension 2 = vertex-disjoint cycle boundaries (exact);
  - Björner's characterization for regular CW posets (locator to be checked).
- **Material:** the 156-8 .tex with scans 3-6; Serre 1977, ch. I §2; Björner 1984; Lundell-Weingram 1969.
