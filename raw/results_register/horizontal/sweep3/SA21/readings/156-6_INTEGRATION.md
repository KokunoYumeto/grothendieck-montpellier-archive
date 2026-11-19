# 156-6: integration

Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8 (reader A), horizontal sweep 3, 19 Nov 2026. The full reading is `156-6.md`.

## STUDY

**156-6, "Analysis situs (deuxième mouture)", GF VI, 18-22 June 1986, scans 2-94: the atelier.** I read it in full and checked 41 points (SA21-R6-01 to -41).

**Data (scans 2-19).**
- **Lieux 𝓛 ⊂ multistrates 𝓜 ⊂ figures 𝓕.** Each figure has its déployement F̃ (its strata), its grande ombre Omb(F) = {X ∈ 𝓜 | X ≪ F} and its multiombre Multomb(F) = {Omb(X) | X ∈ F̃} (on scan 5 the ink of (1.8) has a slip; the formula defines Omb(X), SA21-K6-01). The petites versions omb and mulomb are the traces on 𝓛.
- **"l'ombre d'une figure est formée des lieux qui la raffinent"** (scan 7).
- **The six relations:** ◁, ≤, ≪, ≼, ⋈, ∥ (scan 12).
- **The primitive data are (𝓕, ≤, ≪)**, reversing 156-4's fourth system, where ≼ was primitive. The reason he gives: in 156-4 the antisymmetry of the derived ≪ cost extra axioms. His "réflexivité" on scan 14 is a slip for antisymmetry.
- At 1-At 3 are 156-4's C1-C3: the figures are families of closed sets in (𝓜, ≤), described by a compatibility relation.

**The change of 19 June (scans 21-22).** Refinement is no longer "a sub-figure of a subdivision". It is now strata-wise refinement of the set-theoretic figures, modelled on tame simplices:
- **At 4:** G ≪ F iff each stratum of G refines a stratum of F.
- **At 5:** a smallest stratum is refined.
- **At 6:** compatible + ≪ ⇒ ≤.
- **At 7:** "intérieur de" (≪°) is transitive.

With At 4, F ↦ Omb(F) embeds (𝓕, ≪) in the subsets of 𝓜. That answers his doubt of scan 5 on injectivity; it also makes a clause of the corollary on scan 28 superfluous (SA21-K6-05).

**The Théorème-Scholie (scans 29-34).** An atelier is a family 𝓕_𝓜 of set-theoretic figures in 𝓜 satisfying At*1-At*5. He describes (𝓜, ≪) in the language of a T₀ Alexandrov topology ("parties fermées irréductibles ... admettant un pt générique").

**Examples, set-theoretic ateliers, morphisms, sub-ateliers (scans 35-45).**
- The examples: PL triples, affine simplices, the pseudo-disc with its "structure de reliement".
- Set-theoretic ateliers: mulomb is injective and reflects ≤, ≪ and ⋈.
- Morphisms, and sub-ateliers as closed parts.
- Spacious parts ↔ closed parts of 𝓜 (re-derived).

**At 8 and the Scholie (scans 46-47).** At 8 (a lieu in each open ombre) is 156-4's Contr 3. With it, 156-4's Scholie (X ≤ Y ⇔ omb X ⊂ omb Y ⇔ …) follows, now through At 5 instead of finite dimension.

**Comorphisms and set-theoretic ateliers (scans 48-59).**
- Comorphisms and coplongements; quasi-set-theoretic ateliers, defined by At ens 1.
- **Scholie:** such ateliers are the sub-ateliers of Fig(L) containing the points.
- **The polyhedral condition (1.57)** appears here for the first time in cote 156 (scan 59).

**The axioms on lieux and on gluing (scans 60-81, 20-21 June).**
- **At 9** (disjunction by lieux), At 9′ and At 9″ (compatibility by lieux), **At 10** (lieux of distinct open strata are disjoint).
- **At 11** (gluing of refinements) and At 11′.
- **At 12** (compatibility by intersection).
- **Σ-ateliers** with At 9_Σ, and the diagram of implications (scan 80).
- The bare systems: At 9_Σ, At 10, At 11 bis, or At 9, At 11 bis, At 12.
- The induced refinement is an Inf for ≪: a theorem here, where in 156-4 it was the axiom Cond 8 and Lemma 2 was abandoned.

**Subdivision (scans 82-88).**
- **At 13, the "axiome du support",** is the axiom 156-4/42 asked for. With it, "subdivision" = refinement with the same disjoint figures = refinement maximal for ≤ (Cor 1, word for word 156-4/42-43).
- Subdivision is an order and glues.
- At 14 (extension of subdivisions = 156-4's C7₀) with 14 bis and 14 ter (the cone axiom) are facultative. On 22 June: "Je présume qu'on doit pouvoir prouver qu'un tel F′ est unique".

**The plan (scans 89-94).** The set-theoretic translation (At ens 1-4); simplicial and strict simplicial ateliers; sub-ateliers épais, quasi-denses, Sous-at 3-4. And the plan: "Étudier l'opération de saturation d'un atelier", taken up at 156-9/3.

**What is wrong, all corrected in my tables:**
- four slips of his, decided on the scan (scans 5, 14, 19, 22);
- (1.24 b) "⇐", which he marked "Vérifier", is false under At 1-At 10;
- (1.13) needs At 9;
- the finite-type bijection of scan 19 needs the hypothesis he states on scan 57;
- the f_strat description of morphisms needs an intersection condition;
- "𝓛-plein suffices" needs At 8;
- At 8 for trivial ateliers forces dim 0, not ≤ 1;
- the pull-back of figures must drop members with empty open strata;
- Σ must contain ∅.

**Open on the page:**
- the converse of the Théorème-Scholie;
- At 9_Σ + At 10 ⇒ At 12;
- the uniqueness in At 14 bis;
- the saturation.

## HUNCHES

**H6-1. The points of an atelier are its multistrates under ≪, a T₀ Alexandrov space (sharpens H6 and H9).**
- **Grounds:** 156-6/30, in his words, and the embedding of (𝓕, ≪) by Omb (SA21-R6-14).
- **What it says:** the grande ombre is the representation of an atelier inside the closed sets of the Alexandrov space (𝓜, ≪); the petite ombre on 𝓛 is the "spatial" case, where the lieux suffice (set-theoretic ateliers, Scholie 156-6/55). The maquettes of 156-8/3 ("un espace ultra top. … T₀") are this space promoted to the main object.
- **Literature:** P. Alexandroff, "Diskrete Räume", Mat. Sb. 2 (44) (1937), 501-519 (locator to be checked).

**H6-2. The change of 19 June moves the Hauptvermutung out of refinement and into subdivision alone (sharpens H2).**
- **Grounds:**
  - 156-6/21-22: Y ≪ X for tame simplices "n'implique sans doute pas l'existence d'une subdivision de X telle que Y en soit une multistrate".
  - At 1-At 13 never ask for common subdivisions; only At 14, 14 bis and 14 ter (extension of subdivisions, facultative) and the 156-4 notion "modérée" do.
- **The hunch:** in an o-minimal model, with 𝓜 the definable simplices or cells of all definable cell decompositions, ≤ the face relation and ≪ strata-wise refinement, At 1-At 13 hold without any triangulation theorem. Shiota-type results (H2) are needed only for At 14 and for "modérée".

**H6-3. The pseudo-disc is the basic non-spatial atelier (sharpens H5).**
- **Grounds:** my countermodels to (1.24 b) and (1.13) (SA21-R6-06, -08) are a disc c with two interior lieux a, b that do not form a figure. That is his pseudo-disc of 156-4/45 and 156-6/36.
- **The hunch:** the axioms on lieux (At 9, At 9_Σ, At 10, At 13) and Atens 2 ("deux lieux sont toujours compatibles") are exactly what the pseudo-disc violates. A classification of ateliers satisfying At 1-At 8 but not Atens 2 would be a classification of "chord structures" as on cote 154.

**H6-4. H11 is refuted.**
- "Axiome ... VI p.52" at 156-7/13 is GF VI p. 52 = 156-6/53, the axiom At ens 1.
- **Grounds:** the reciprocal margin "Pour correctif voir GF VII p. 12" on 156-6/53, and the polyhedral form of At ens 1 next to the reference on 156-7/13 (SA21-R6-28).
- The transcription's "Cat PL" is probably a misreading of the axiom's name. There is no earlier text on PL categories to look for.

**H6-5. Σ-ateliers choose the shapes of intersections (sharpens H9 and H10).**
- **Grounds:** 156-6/78-79 and 89: Σ = all ordered sets gives the spacious set-theoretic ateliers; Σ = {∅} ∪ {ordered sets with a largest element} gives the simplicial and polyhedral ones ((1.57), 156-7/14).
- **The hunch:** with Σ = face posets of convex polytopes together with ∅, Σ-ateliers whose multistrates are such face posets are exactly the polyhedral complexes. With Σ = boolean lattices (simplices), they are the simplicial complexes. "Au moins deux prédécesseurs" (156-6/89, 156-7/15) is the first condition of the face-poset characterization of regular CW complexes (Björner 1984, H9).

**H6-6. 156-6's At 1-At 7 make (𝓜, ≤, ≪) the right data for the 1981 tubular structures.**
- **Grounds:** ≪° (X "suffisamment intérieur de" Y) is the relation "the open part of X lies in the open stratum of Y"; At 7 is its transitivity; At 5 is the existence of a smallest stratum containing a point's neighbourhood.
- **The hunch:** in a stratified space with the frontier condition, these are the incidence data that the voisinages tubulaires V_{X_i,X_j} of 151/44-71 parametrize. A test is to build (𝓜, ≤, ≪) from a Whitney or o-minimal stratification and its refinements and check At 1-At 7 (links H7, H8; SA10).

## PACKAGES

**P6-1. The atelier axioms of 156-6: implications, countermodels, models.**
- **The question:**
  - Complete the diagram of 156-6/80: prove or refute At 9_Σ + At 10 ⇒ At 12, and At 11 bis + At 11′ ⇔ At 11.
  - Decide the uniqueness of the coarsest extension in At 14 bis ("Je présume ... unique") and its equivalence with At 14 ter for finite figures.
  - Prove or refute the converse of the Théorème-Scholie (156-6/33-34).
  - Decide which of At 1-At 14 hold in four models: Fig(L), strict simplicial complexes, the o-minimal cell model of H6-2, and the pseudo-disc.
  - Give a countermodel for each non-implication.
- **Why it matters:**
  - This is the most complete axiom system of the deuxième mouture, and the base from which the troisième mouture (156-7) and the magasins (156-8) depart.
  - P7 (the systems side by side) needs it closed.
- **What it rests on:** this reading (156-6.md, 41 check events, 13 corrections); STUDY §2 (156-4); 156-7/10-15.
- **Strongest known reduction:** the implications checked in SA21-R6-33 to -41. Countermodels exist for (1.24 b) and (1.13) under At 1-At 10 (SA21-R6-06, -08), and for the margin claims of SA21-R6-18, -19, -23, -25 and -26.
- **Material:** `c156-6.txt` with the .tex of J156-6-01 to -12 and 156-6.pdf scans 20-94; 156-4 per STUDY §2; Johnstone, *Stone spaces* (1982), ch. II; van den Dries, *Tame topology and o-minimal structures* (LMS LN 248, 1998), ch. 3-4 (locators to be checked).
