# SA21, Vers une géométrie des formes (cote 156): the study

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18-19 Nov 2026.

## What was read, and how

- **156-4, scans 2-89:** read in full by this agent (a6d42bf6fe2b0d8a8, Claude Opus 5.5 at effort max).
  - The source is the Codex web transcription J156-4-01 to J156-4-11, cleaned by `_tools_a6d42bf6/clean_tex.py`.
  - One scan image was viewed (scan 45).
- **156-3 and 156-5 to 156-9:** read by three readers, each Claude Opus 5.5 at effort max, briefed with `_tools_a6d42bf6/READER_BRIEF.md`:
  - **reader A (a4e5251e8164eb831):**
    - 156-6 in full, with scans 5, 14, 19 and 22 viewed;
    - 156-5 in full, with no scan viewed.
  - **reader B (ae747b2de9d398034):**
    - 156-7: scans 2-60 line by line, scans 61-114 for statements and proofs, five scans viewed;
    - 156-3 in full, with no scan viewed.
  - **reader C (a770b79a, launched by the main session):**
    - 156-8 in full, with scans 4, 6, 31, 32 and 86 viewed;
    - 156-9 in part: scans 2-9, 46-50, 78-80, 109-111 and 115-118 in full, the rest by statement lines.
  - **Where their work is:**
    - their full readings are in `readings/<part>.md`;
    - their study, hunches and packages are merged at the end of this file and of HUNCHES.md and RESEARCH_PACKAGES.md;
    - their check events and corrections are in the tables.
- **156-1 and 156-2:** studied in sweeps 1-2 through the Pro notes. The three readings left open there were decided on the scans in this run (§3).
- **156-7, scans 61-114,** were read page by page in round 2 by reader B (ae747b2de9d398034, resumed, Claude Opus 5.5 at effort max): readings/156-7_061-114.md, 31 check events, 17 corrections.
- **156-9, the rest:** read line by line in round 2 by reader C (a770b79afe0cb5100, resumed, Claude Opus 5.5 at effort max): readings/156-9_rest.md, 29 check events, 9 corrections. 156-9 is now read in full except the drawings of scan 112.
- **Michel Hua's project:** the readers used his modernised readings as a credited witness. The ink decided every reading.

**The checks** are in CHECK_EVENTS.tsv. Each re-derivation is one row.

## 0. Cote 156 after the readings (19 Nov 2026)

**What the series is.**
- Between 8 June and 15 July 1986, in nine parts, he axiomatizes tame geometric forms without points:
  - first the contrées (156-4);
  - then the ateliers (156-6, 156-7);
  - then the magasins (156-8);
  - after the word swap of 9 July, ateliers again, with the supports as ortholattices (156-9). The swap is on 156-9/41: "je dirai 'atelier' là où je disais 'magasin', et inversement".
- 156-3 and 156-5 are the one-dimensional and the set-theoretic models. 156-1/2 is the first one-dimensional theory.

**The main results of the readings, in mathematical order.**

1. **The line (156-3).**
   - For a totally ordered tronçon, the tame parts Mod(L) are exactly the finite unions of points and open intervals. These are the definable sets of the o-minimal structure (L, <).
   - So "modéré" on the line is the o-minimal condition, written down in June 1986, at the same time as Pillay and Steinhorn's 1986 paper (reader B; also in Michel Hua's project).
   - A tronçon is known up to reversal from its strict betweenness, and the betweenness is read off the cuts (re-proved).
   - For non-total tronçons this is not in Hilbert 1899 or Huntington-Kline 1917.
2. **The set-theoretic model (156-5).**
   - Admissible families of subsets are preorders on parts of L.
   - The set-theoretic figures, with their refinement and subdivision, satisfy C1-C3, C5-C7 and C8₀ of 156-4 (computed).
   - **His claim that C4 "est automatique" is false.** The multistrates of Fig(L) have 3 components on 2 points and 5 on 3 (SA21-K5-01).
   - The supports are P(L). From the figures one recovers P(L), not L.
3. **The atelier (156-6, 156-7).**
   - 156-6 makes refinement ≪ primitive, where 156-4 had subdivision, with At 1-At 14.
   - At 13, "l'axiome du support", is the axiom 156-4/42 asked for, and subdivision becomes maximal refinement.
   - The Théorème-Scholie of 156-7 is re-derived both ways. It represents spacious ateliers by (M, ≤, ≪) with a disjointness graph on the minimal elements.
   - His characterization of simplices (156-7/14-15) is false: the face poset of a square satisfies "polyédral + At simp 1". Simplices need distributivity.
   - "Axiome des Cat PL VI p.52" (156-7/13) is 156-6/53, the axiom At ens 1. H11 is refuted.
4. **The magasin (156-8).**
   - Mag 1-4 take "intérieurement disjoints" (|∘|) as primitive. From them alone, the compatibility-disjunction axioms of 156-6 and 156-7 and the gluing of refinements follow (re-derived). This is what he means by "l'innovation d'avant-hier faisant tomber tout le fouillis des axiomes de compatibilité-disjonction".
   - The weakened Mag 4′ of 28 June is too weak, by a maquette countermodel.
   - The Proposition-Scholie of 156-8/16-17 lacks the transitivity of ≪°. There is a five-element countermodel, and the ≪°-form repairs it.
   - Oriented maquettes of dimension ≤ 1 are Serre's graphs; Michel Hua's project gives the identification first.
   - His "Sauf erreur" for dimension 2 is not right as stated. The axioms admit 2-cells bounded by several disjoint cycles and exclude the one-vertex torus. With "∂X connected" added, they are the 2-complexes whose cells are attached along simple closed paths.
5. **The supports.**
   - The lattice Σ of supports (156-4/66-69) is not distributive in general. His own counterexample is the "ficelle à deux brins" (156-7/82-84).
   - **In faithful magasins Σ_M is the complete Boolean algebra of regular open sets of the Alexandrov topology of (M, ≪°)** (156-8, SA21-R8-25).
   - Under divisibility and Mag L2: faithful ⇔ Σ is Boolean with the lieux as distinct atoms (156-9 reading).
   - The plain "distributive ⇔ faithful" is refuted, by two non-disjoint lieux.
   - His "spatios" (156-9/78-80) are complete ortholattices.
   - Three of his statements are the **orthomodular law**: Lemma 1 and Cor 1 (156-9/109-111), the formal lemma of 156-7/97-99, and the "axiome des supports" (156-9/117).
   - The orthomodular law **fails on the hexagon O₆**, which arises from the fence a′ < a > b < b′.
   - **MO₂ is orthomodular but not Boolean.**
   - **The Théorème of 156-7/94 is false under all its hypotheses.** Reader B, round 2, built an eight-element atelier with a seven-lieu disjointness graph that satisfies L1-L3, CL(spac), At D, At supp and At supp 1, yet both conclusions fail. The theorem holds where distinct lieux are disjoint, which is why 156-8/88 has to pose it as Axiome supp 1.
   - **Round 2 (reader C, 156-9_rest):**
     - **Axiome supp 1 holds in the magasin of an ordered set.** He proves it for figures inside one flag (156-9/21-22, re-derived), and it holds for all 4,724 figures of the magasins of the 203 connected orders with at most 5 elements (computed).
     - **His duality theorem cosupp°Φ = Omb°Φ* (156-9/16) is re-proved,** and it held on 21,492 polygons.
     - **The Question of 156-9/3 is true for magasins of connected ordered sets** (proved, with explicit separating strata). It is false for local ateliers in general (a path of four lieux; twin lieux).
     - **Cograph ⇒ orthomodular is proved, and the converse fails.** On 5 vertices, 60 comparability graphs with an induced P₄ still have orthomodular Σ; one has Σ = 2³. H9-1 is refuted as an equivalence, and the refined hunch is H9b-1 (Dacey graphs).
     - **His Lemme 1 (156-9/72) is false;** his own Prop 4 repairs it. His transposition questions are settled, and his "(oui.)" of 156-9/108 is proved.
   - His own diagnosis (156-9/128): "Ce sont mes 'cordes' ... qui causent tous les ennuis".
6. **The July restart (156-9/5-16).**
   - The setting is the magasin of an ordered set: points and intervals with the positional order a < I_{a,b} < b (156-8/90-127).
   - |∘| is comparability, and the figures are the flags of the positional order, not of the incidence order.
   - It is faithful exactly when L is total.
7. **Documentary.**
   - The sheet "Table des Matières T 1 : T 10 … fascicule 4" on 156-9/3 is a reprography order for Récoltes et Semailles ("Fascicule 0"), not a table of the 1986 notes. H12 is refuted (SA21-K9-01).
   - Scans 5 and 7 of 156-8, scan 101 of 156-7 and scan 114 of 156-9 are Récoltes et Semailles leaves.
   - His name for the structure of 156-7/55-61 is "Stratos", decided on the scan; the Codex text reads "Stratop" or "Anatos".

**What stays open, in the order of the packages:**
- the support lattice of the non-faithful magasins (cords and strands), and the cograph hunch for comparability magasins (P8-1, P9-1);
- oriented maquettes against regular CW complexes in every dimension (P6, P8-2);
- the o-minimal contrée and its faithfulness (P2, H9-3);
- open on the pages:
  - the converse of the Théorème-Scholie of 156-6;
  - At 9_Σ + At 10 ⇒ At 12;
  - the uniqueness in At 14 bis;
  - the saturation (156-6, 156-9/3);
- what replaces C4 in the axioms.

## 1. What cote 156 is

A sequence of drafts from 5 June to 15 July 1986. The sheets are marked GF (or CF), from III to IX bis.

They look for an intrinsic axiomatics of "formes": the combinatorial structure carried by a tame (moderate) space, with no coordinates. The pieces are its strata ("multistrates"), its closed unions of strata ("figures"), its subdivisions and refinements, and its points ("lieux"). The topological spaces come back as realizations.

The order of the drafts:

| Part | What it does |
|---|---|
| 156-1, 156-2 | Segments, networks, ficelles, cuttings, rives and mailles: one-dimensional models first |
| 156-3 | Networks via cuttings, sheet III, 8 June |
| 156-4 | "Analysis situs (première mouture)", 10-14 June: contrées, in four successive axiom systems; read in full below |
| 156-5 | "Sorite ensembliste", 15-18 June |
| 156-6 | "Analysis situs (deuxième mouture)", 18-22 June: ateliers |
| 156-7 | "Analysis Situs (troisième mouture)", Chap VII, from 23 June |
| 156-8 | CF VIII, 27 June-4 July: magasins, oriented multistrata, polyhedral ateliers, lieux, supports |
| 156-9 | GF IX, 5-15 July: quasi-correspondences, morphisms of ateliers |

## 2. 156-4 "Analysis situs (première mouture)", 10-14 June 1986, read in full

### 2.1 The model, scans 2-17
**The setting (scans 2-3).** E is a separated space, or a moderate space for a given tame theory. There, "fermé" means a closed tame set.

**A figure** F of E is a closed set X decomposed into closed strata X_i such that:
- (a) the X_i are nonempty and locally compact;
- (b) the family is locally finite;
- (c) X_i ⊊ X_j implies X_i is nowhere dense in X_j;
- (d) int X_i = X_i ∖ ∂X_i, with ∂X_i = ⋃_{j<i} X_j, is a connected manifold (a tame manifold in the tame case);
- (e) a margin addition: i < j implies dim int X_i < dim int X_j, "pour éviter des phénomènes de sauvagerie";
- (f) X_i ∩ X_j is a union of strata.

So a figure is a stratification with the frontier condition, recorded as the set of its closed strata. This identification is mine; he does not name it.

**Sub-figures (scans 4-5)** are the closed (downward) subsets of the poset of strata. A figure is elementary if it has a largest stratum; on 11 June he renames these "multistrates". A figure is determined by its elementary sub-figures.

**Compatibility (scans 6-8).** Two figures are compatible when either of two conditions holds:
- (a) each X ∩ X′ is saturated for both figures;
- (b) any two open strata are disjoint or equal.

His proof of (a) ⇒ (b) goes as follows. The step from a common point to X_i = X′_j uses that X_i ∩ X′_j is closed and saturated and meets the dense open stratum U_i. The equality of the boundaries goes by induction on dimension. I checked the first step (CHECK_EVENTS); the induction is sketched on the page.

**Subdivision and refinement (scans 14-17).**
- F′ ≪ F (F′ refines F) when each open stratum of F′ lies in one of F.
- A subdivision is a refinement with the same support. Equivalently, a refinement maximal for inclusion.

His justification builds the canonical extension F̄′ of a refinement F′. Its open strata are those of F′ together with the components of U_i ∖ X′. He stops on the frontier condition for these components: "il y a un pb, qui a l'air intéressant, de topologie d'un espace stratifié (X′ ∩ U_i) plongé dans une variété (U_i)" (156-4/17). This is open on the page; see HUNCHES H8.

### 2.2 First intrinsic system, 11 June (scans 18-25)
**The data.** A contrée is given by:
- the multistrates M (the elementary figures);
- refinement ≪, an order;
- compatibility R, reflexive and symmetric;
- the "finite" configurations.

**The axioms.**
- Contr 1: X′ ≤ X :⇔ X′ ≪ X and compatible, and this is an order.
- Fig 1-2: finite combinatorial dimension.
- Contr 2: the geometric dimension is finite.
- Lieu: a multistrate minimal for ≪. In the model, a point.
- L_X: the lieux refining X.
- Contr 3: each X has a lieu in L°_X = L_X ∖ ⋃_{Y<X} L_Y.
- Contr 4: compatible distinct X, Y have disjoint L°.

**The Scholie (scan 24).** For a figure F:
- the L°_X, for X ∈ F, partition L_F;
- X ↦ L_X is injective on F;
- X ≤ Y ⇔ L_X ⊂ L_Y ⇔ L°_X ⊂ L_Y ⇔ L°_X ∩ L_Y ≠ ∅.

I re-derived (iv) ⇒ (i) and it holds; it uses L_Y = ⋃_{Y_i≤Y} L°_{Y_i}, which follows from finite dimension (scans 22-23).

**Cont 5 (scan 25).** The converses: ≪ and compatibility are read on open strata. His own warning: these hold "dans les exemples-types uni-strates … mais pas pour les réseaux p.ex.".

### 2.3 Second system: lieux and figures, 11-12 June (scans 26-45)
**The data and the first axioms (scans 26-31).** A contrée is now a set L of lieux together with figures, which are sets of subsets of L.
- Cont 1: the empty figure and the point figures.
- Cont 2: open strata are nonempty, and X ∩ Y is a union of strata below both. He calls such families "admissibles"; this is the frontier condition again.
- Cont 3: closed parts of a figure are figures. His warning: F′ ⊂ F does not make F′ a sub-figure; take X₀ ⊂ X₁ and F′ = {X₁}.
- Compatibility of figures is set-theoretic compatibility plus "F ∪ G is a figure".
- Cont 4: compatibility is tested on multistrates.
- "Contrées de points", or set-theoretic contrées: there, set-theoretic compatibility is compatibility.
- Disjoint lieux, and 0-spheres.

**12 June, the pseudo-discs (scans 32-33).** "Depuis hier j'ai pas mal réfléchi à la combinatoire des pseudodisques topologiques." In a pseudo-disc (D, ∂D), an interior lieu must carry a datum: an equivalence class of "cordes" joining it to ∂D. So a contrée cannot be described by lieux and sets of lieux in "la topologie combinatoire sans points". He returns to C = (M, ≪, R_M, figures) and decides to fix a geometric terminology first: "au lieu de dégager un bon syst. d'axiomes, dégager une terminologie géométrique" (156-4/33). See H5: the disk model with chords on cote 154.

**The terminology (scans 33-41).**
- Sub-contrées: subsets closed under ≪.
- Cont 1-2 and Fig 1-4:
  - the elementary figure F_X = M_{≤X};
  - figures are closed and pairwise compatible;
  - closed parts of figures are figures;
  - compatible figures have a union.
- Finitist contrées, where all figures are finite: there ≪ and R determine the figures (scan 35).
- Cont 3′: M_{≤X} is finite.
- Cont 3: the geometric dimension is finite.

**"Ombre" is defined here (scan 36):** the ombre (fermée) of X on L is L_X = {x ∈ L : x ≪ X}. The ombre of a figure is the union; there is the ombre ouverte, and the bord d'ombre. This answers, for 1986, the requested question on the "ombre" (H05G): the shadow of a multistrate on the set of lieux. See H4.

**The Scholie in shadow terms (scans 37-38).**
- X ↦ X̃ = L_X is injective, and its image is an admissible family.
- The open shadows partition the shadow of F.
- ≤ is inclusion of shadows.
- The sub-figures correspond to the closed parts of the shadow.
- Sub-contrées inherit the axioms (Proposition, scan 38).

**Disjointness (scans 39-40).**
- Disjoint figures are compatible with empty intersection.
- Proposition: F is a sub-figure of G ⇔ F refines G and is compatible with G. The proof is given and checks.
- Cont 5: disjointness passes to refinements.
- Cont 6 (facultative): disjointness can be detected on lieux.

**Induced contrées (scan 41).** The contrée induced by a figure; the residual contrée; subdivisions as maximal refinements.

**Subdivisions (scans 42-43).**
- Proposition: a refinement F′ of F is a subdivision ⇔ no multistrate refines F and is disjoint from F′ ⇔ no lieu of the shadow of F is disjoint from F′.
- In the proof of c ⇒ a he notes "il faut un axiome pour l'assurer", and adds Cond 7: compatible distinct X, Y have pairwise disjoint open-shadow lieux.
- Building F′ → F, he writes "Il semblerait qu'il manque quelque chose" (scan 43).

**Cond 8, the induced refinement (scan 44).** For Y ≪ X and X′ < X:
- the Y′ ≤ Y with Y′ ≪ X′ form a sub-figure R_{X′};
- every common refinement of Y and X′ refines R_{X′}, so R_{X′} is the infimum for ≪.

Corollary: if no X₁ satisfies Y ≪ X₁ < X, then Ỹ° ⊂ X̃°. I re-derived the proof and it holds (CHECK_EVENTS).

**Scan 45.** Open shadows of a refinement lie in open shadows.

He then notes that in the pseudo-disc two disjoint interior lieux x, y should not count as a refinement, because {x, y} does not extend to a subdivision. The sentence reads "qu'il existe une 'Subdivision' du disque dont ils soient des nœuds". Its conclusion needs "qu'il n'existe pas". At 200 dpi I see no negation in the ink, so this is probably his slip (CORRECTIONS SA21-K7). Whatever the reading, he draws the conclusion: subdivision becomes the primitive notion, and refinement means a sub-figure of a subdivision.

### 2.4 Third system: subdivision primitive (scans 46-52)
**The data.** C = (M, figures, Σ), with Σ the relation "F′ subdivise F".
- C1: each X lies in a smallest figure F_X; X ≤ Y :⇔ F_X ⊂ F_Y, and C′1 makes this an order.
- C2: closed parts of figures are figures.
- C3: compatibility is tested on elements.

**C4 (scan 48)**, as first stated: G′ ∪ (F ∖ G) is a subdivision of F. His own margin calls this false, "démenti par … les strates fermées et strates augmentées", and corrects it: there is a subdivision of F inducing G′, and G′ ∩ F ⊂ G (CORRECTIONS SA21-K8).

**Consequences.**
- Cor 3: X ∈ F ⇔ X is compatible with F and refines F; and X ≤ Y ⇔ X is compatible with Y and X ≪ Y (scan 49).
- C5: subdivision preserves disjointness.
- C6: induced subdivisions exist and are unique.
- C7: subdivisions glue; two subdivisions are equal iff they agree on every multistrate (scans 50-51).

**Induced refinement (scans 51-52).** G′ = {X ∈ F′ : X ≪ G} refines G and is Inf(F′, G) for ≪. This is the old Cont 8. He proves it through C6 and the corrected C4 and ends with "qed, ouf !". The proof is a diagram chase on the page; I followed it, and it uses only C4 corrected and C6.

### 2.5 Fourth system, 13-14 June (scans 53-89)
**The data.** C = (F, ≤, ⪯): the figures, with sub-figure ≤ and subdivision ⪯.

**The axioms for ≤ alone (scans 54-62).**
- C1: bounded families have a Sup, and there is an empty figure.
- Irreducible figures are the multistrates; C2: every figure is the Sup of its strata.

So (F, ≤) is a family of subsets of M closed under bounded unions, with a smallest member A_X containing each X. I re-derived the correspondence of scans 55-56 and it holds.

With C3 (compatibility tested on strata) and finite figures, the structure is equivalent to (M, ≤, R) with:
- M_{≤x} finite;
- R reflexive, symmetric and downward closed.

The figures are then the finite downward-closed R-cliques (scan 62). I checked this equivalence, including the step by which a finite clique has a Sup (induction with C3).

This is exactly a prime event structure: finite causes, conflict = non-R, inherited upwards, and the figures are its finite configurations. That identification is mine; see H1.

**Connectedness (scans 62-66).** Connected figures; connected components (the components of the poset F̄); components of the whole M.
- C4: elements in different components are compatible.
- C4 bis: every family of components is realized by a figure.

**Supports (scans 66-69).**
- The cosupport of Φ is the figures disjoint from all of Φ. The supports are the saturated sets (cosupport of a cosupport), and Σ is the virtual supports, with arbitrary Inf and Sup and cosupport as an anti-involution.
- He presumes Σ is a Boolean algebra, "ultrastonienne". In the set-theoretic model Σ = P(E), whose Stone space is β(E_disc); that is correct.
- But "je ne vois comment prouver … P ∧ (Q ∨ R) = (P ∧ Q) ∨ (P ∧ R)".
- In general Σ is the lattice of bi-orthogonally closed sets of the orthogonality (disjointness) relation, which need not be distributive (H3).
- The displayed formula for the cosupport (scan 69) omits the condition "no common lower element". As written it gives compatibility, not disjointness (CORRECTIONS SA21-K9). His conclusion, that Σ depends only on (M, ≤, R), stands.

**The subdivision order (scans 70-73).**
- Subdivisions of F are comparable if they have a common subdivision.
- **"La contrée est modérée si deux subdivisions d'une même F sont toujours comparables"** (scan 70). This is the Hauptvermutung taken as an axiom (H2). He adds that the condition will have to be strengthened.
- C5: F′ ⪯ F gives the same disjoint figures, so the same support; cosupports are sub-contrées.
- Sub-contrées.
- C6: induced subdivision of a sub-figure, unique, with strata {X′ ∈ F′ : X′ ≪ G}.
- C7₀: every subdivision of a sub-figure extends. The symmetric statement is false, as he says.

**Refinement as an order (scans 74-80).**
- G ≪ F :⇔ G ≤ F′ ⪯ F. Transitivity holds by C6.
- Antisymmetry needs: F ⪯ K ≤ F ⇒ K = F. He shows the axioms so far do not give it (scan 75, M with a least element and ⪯ discrete) and concludes "il manque un axiome".
- The induced refinement is Inf for ≪ (Lemma 1). For Lemma 2: "J'abandonne ! Il vaut mieux se reporter au texte page 51."
- Proposition: X ≪ F ⇒ a smallest stratum Y of F with X ≪ Y, characterized by "∂Y induces ≠ X". The proof is given and uses finite dimension.

**The missing axiom (scans 81-87, 14 June).** "Jusqu'à maintenant, les axiomes C5, C6, C7 … sont tautologiques, si on prend pour ⪯ l'égalité … Il serait temps d'en venir à des propriétés plus spécifiques !"
- C8₀ (provisional): X ≤ Φ ⪯ X ⇒ X = Φ, and X ⪯ Ψ ≤ X ⇒ X = Ψ. It is necessary and sufficient for ≪ to be an order.
- An abstract remark on two orders, (a) unique completion of squares, (b) existence of completions, (c), gives the order ≪ and cartesian squares. His margin: "Il manque sans doute des hypothèses".
- A plan of axiom packages:
  - α: ≤ alone;
  - β: the formal links between ≤ and ⪯;
  - γ: gluing of subdivisions; C8 now names this, giving Subdiv(∐F_i) = ∏ Subdiv(F_i);
  - δ: disjunction and support.

**Lieux, ombres, multiombres (scans 88-89).**
- A lieu is a nonempty figure minimal for ≪.
- The ombre of F is |F| = {x ∈ L : x ≪ F}.
- The multiombre is F̂ = {|X| : X ∈ F̄}.
- Proposition: the multiombre is an admissible family of subsets of L.

The part ends here.

### 2.6 What 156-4 establishes, and what it leaves open

**Proved on the page, and re-derived by me:**
- the Scholie (scan 24);
- the Cond 8 corollary (scan 44);
- sub-figure ⇔ refines and compatible (scan 39);
- the C1-C2 correspondence (scans 55-56);
- the finite (M, ≤, R) description (scan 62);
- the smallest stratum through which a multistrate refines (scan 80).

**Wrong as first stated, and corrected by him:**
- C4 (scan 48);
- the axioms before C8₀, which do not make ≪ an order (scans 75-76).

**Wrong in a formula, corrected by me:** the cosupport formula (scan 69).

**Open on the page:**
- the frontier condition for the canonical extension (scan 17);
- the distributivity of Σ (scan 69);
- Lemma 2 (scan 79, abandoned);
- his own "Il manque sans doute des hypothèses" (scan 86);
- the complete axiom list: he leaves it for the next mouture.

## 3. 156-1 and 156-2 (from sweeps 1-2)

- **The pages:** segments and networks with the axioms F1-F6; ficelles and regular immersions; cuttings; rives as germs of clopen sets; mailles.
- **The notes' counterexamples:** to arbitrary restriction (A12, with the repair A13) and to the local-to-global passage of filtering, which he withdrew himself (A21-A22).
- **The README conjecture:** a form recovered from a pro-object of finite posets is not on these pages (P01).
- These pages are the first of the series: the one-dimensional case of what 156-4 axiomatizes in general.

**The three readings left open in sweeps 1-2, decided on the scan images tonight** (renders of 156-1.pdf page 19 and 156-2.pdf pages 3 and 6, at 220-500 dpi). In all three the frozen transcription reads the ink correctly, and the fault is his:

| Place | What the ink shows | Verdict | Correction (editorial note, not an emendation) |
|---|---|---|---|
| 156-1/019 (A20, SA21-K1) | Above a heavily struck sign he wrote "x≤" (a one-stroke ≤); in the conclusion the bars under both ≤ are blacked out, leaving "x<u<y,z". | His slip, made in his own correction. The condition as he left it ("si x≤y,z, ∃u, x<u<y,z") fails at y = x. | Read "si x<y,z". His margin draws divisibility from it (x<y ⇒ ∃z, x<z<y), which needs the strict antecedent, and 156-1/013 has the strict form. |
| 156-2/003 (B04, SA21-K2) | "W'_t = X − V_t": a clear V. | His abuse of notation: V_t ⊂ X/A stands for its inverse image. | W'_t = X − W_t, with W_t = π⁻¹(V_t). |
| 156-2/006 (B10, SA21-K3) | "X∖{c} ne serait pas connexe". The c is as clear as the a of "X∖{a}" one line above. | His slip of letter. | The set V is open and closed in X∖{a}, non-empty and not everything, so the argument gives "X∖{a} ne serait pas connexe". |

## 4. 156-3 and 156-5 to 156-9: this agent's first account, and the readings

- Section 5 is this agent's first account, from the axiom, definition and dated lines (18 Nov).
- The readers' full readings supersede it where they differ. See §0, the merged blocks at the end of this file, and `readings/`.
- The corrections to section 5 are marked in place.

## 5. The later parts, in order

**156-3, "Réseaux … via découpages", 8-9 June 1986 (SA21-12): the one-dimensional axiomatics by segments.**
- **Scan 2:** "Je voudrais définir une autre axiomatique … l'axiomatique par les segments".
- **Scan 3:** the question whether T is known once C_𝓛(T) is known.
- **Scans 4-5:** "Axiomes provisoires" and an axiom on finite tame ("modérée") parts.
- **Scan 9:** the definition of a *tronçon ordonné*, an ordered set with an axiom a) and its dual a′).
- **Scan 12:** Lemme. A biordered tronçon structure is known from a ternary relation on three elements a, b, c, a betweenness relation.
- **Scan 13:** the order defining the biorder is determined by that relation.
- **Scan 14:** a lemma on four elements x, y, u, v.
- **Scan 20:** Prop. Two closed tame parts in tame relative position have a closed tame intersection. The Cor extends this to finite families.
- **Scans 22-25 (9 June):** the topology of a tronçon ordonné L, with the closed sets [a,b], L_{≥a}, L_{≤a}. He keeps the topology generated by the "intervalles".
- **Scan 29:** a Prop with equivalent conditions on T, T′, where a = Sup T and b = Inf T′.
- **What the part is:** the theory of 156-1/2 restated through order and betweenness. It is the one-dimensional case of the contrée.

**156-5, "Sorite ensembliste", 15-18 June 1986 (SA21-14): the set-theoretic model.**
- **Scan 2:** Proposition 1, equivalent conditions.
- **Scan 4:** a family 𝓛 ⊂ P(L) is *préadmissible* if it satisfies the equivalent conditions 1°-3°. Admissibility follows.
- **Scans 7-8:** a Prop with equivalent conditions on Ψ ⊂ P(L), for 𝓛 admissible.
  - The Scholie says these families correspond, order-preservingly, to the closed parts of 𝓛 or of |𝓛|.
  - A second Prop compares two admissible families.
- **Scan 10:** *compatibility* of Φ and Ψ: each is closed in Φ∪Ψ.
- **Scan 11 (margin):** Cor 3. For compatible Φ, Ψ, the closed parts Φ′ ≤ Φ and Ψ′ ≤ Ψ are admissible, and so is Φ′∪Ψ′.
- **Scan 12:** "Remords à prop. page 7", a further equivalent condition to a)-c).
- **Scan 14:** a Prop on connectedness. M is connected for card L ≤ 1, and there is a statement on the X for card L ≥ 1.
- **What the part is:** the model of the fourth system of 156-4 by families Φ ⊂ P(M), which I checked at 156-4/55-56 (section 2.5), worked out as a sorite. It is the same as 156-8/18, where a set-theoretic magasin is a set L with a family of subsets.

**156-6, "Analysis situs (deuxième mouture)", from 18 June 1986 (SA21-10): contrées with multistrates.**
- **Scan 2:** "Avant de décrire ce qu'est une contrée, je vais décrire ce qui sera une 'contrée avec notion de multistrates'". The data are 𝓛 ⊂ 𝓜 ⊂ 𝓕: lieux, multistrates and figures, with the canonical injections.
- **Scan 3:**
  - an incidence relation between 𝓜 and 𝓕;
  - Fig_𝓜(F) = {X̃ | X ∈ F̃ = Depl(F)} ⊂ P(𝓜), with X̃ = {Y ∈ 𝓜 | Y ≤ X};
  - "il résultera des axiomes que c'est une figure ensembliste dans 𝓜, indexée fidèlement par l'ens F̃ des strates de F";
  - F̃ is a closed part of (𝓜, ≤).
- **Scan 5:**
  - the map F ↦ Omb_𝓜(F), "l'ogombre de la figure F sur 𝓜, ou la grande ombre";
  - (1.8) defines Omb(X) = {Y ∈ 𝓜 | Y ≪ X}. The frozen text reads "Multomb"; the ink reads "Omb", decided on the scan by reader A (readings/156-6.md).
- **Scans 6-7:** the same with 𝓛 in place of 𝓜. **"l'ombre d'une figure est formée des lieux qui la raffinent — on dit aussi que ce sont les lieux 'de la figure' (à ne pas confondre avec les strates de la figure)" (scan 7).** This settles what the 1986 ombre is: the set of lieux that refine F. With lieux as points, it is the underlying point set |F| of 156-4/88-89.
- **Scan 8:**
  - the orders induced by ≤ and ≪ on 𝓛 are discrete;
  - the order ⪯ induced in 𝓜 matters less;
  - F and G are *compatible* when {F, G} is bounded above for ≤;
  - they are *disjoint* when they are compatible and their inf is ∅_𝓕 (scans 8-9).

**156-7, "Analysis Situs (troisième mouture)", ateliers (SA21-10).** Scans 2-9 were transcribed separately, as folder H156-01.
- **Scan 10:**
  - Propriété 1′₀ for F ≍ G with F′ ≪ F, G′ ≪ G and L = F∩G;
  - Cor 1-3, among them F ∥ G ⇒ F′ ∥ G′;
  - "J'ai tendance à regarder At CD comme 'axiomes obligatoires' pour les ateliers";
  - Propriété 2, of the "ateliers spacieux".
- **Scan 11:**
  - the "Critère de compatibilité absolue" for spacious and for polyhedral ateliers. Polyhedral means that two compatible multistrates bounded below have an inf.
  - "Tous les ateliers que j'ai vus comme motivants satisfont At CD 1₀, et l'un des deux axiomes At CD 2 ou At CD 2′".
  - At CD reduces the relation ≍ in M to ∥.
- **Scan 12:** the axioms to be "dégag[és] … en termes cette fois de (M, ≤, ≪, ∥)".
- **Scan 13:** "propriété qui remplace Axiome des Cat PL VI p.52". Readers A and B, both on the scans: "VI p.52" is GF VI = 156-6, p. 52 (scan 53), the axiom At ens 1. The margins of 156-6/53 and 156-7/13 cite each other.
- **Scan 14:**
  - an ordered set I is *polyédral* if two elements bounded below have an inf;
  - a Lemme for the case where every interval is inductive, for example finite;
  - a figure is polyhedral when F̃ is: "la condition de la stricte intersection".
- **Scan 15:** At simp 1. For every X ∈ M, ∂X = {Y | Y < X} is empty or has at least two elements. This begins the simplicial ateliers.

**156-8, the magasins, 26 June - 4 July 1986 (SA21-15).**
- **Scan 3:** the diagram of magasin types:
  - général (Mag 1-4, Σ_M ⊂ P(M));
  - local (M, ≤, ≪°, |∘|_L);
  - with faithful ombres;
  - with Σ_M ≃ P(L);
  - set-theoretic, and set-theoretic tame;
  - the maquettes: "une maquette, un espace ultra top. … T₀, n'est un magasin ponctuel que si elle est discrète", and "Il y a des magasins modérés non ensemblistes, p. ex. les maquettes".
- **Scan 4:** "Multistrates orientés — magasins orienteurs", with data M, ◁ (immediate incidence), ≪° and |∘|.
- **Scan 6:**
  - "Les maquettes orienteuses de dim ≤ 1 sont les 'graphes'";
  - in dimension 2: "Sauf erreur … complexes cellulaires combinatoires de dim ≤ 2".
- **Scans 5 and 7:** the back of a reused Récoltes et Semailles typescript (note 171, "L'Apothéose", 1 March 1985).
- **Scan 8, 26 June: "Analysis Situs (quatrième mouture)", a récapitulation:**
  - Mag 1: ≤ and ≪ are orders;
  - Mag 2;
  - Mag 3: |∘| is symmetric and antireflexive, with a clause (b);
  - Mag 4: Y, Z ≤ X with Y ≠ Z gives Y |∘| Z, which "établit élégamment l'axiome AtL3";
  - the relations ≍ and ∥.
- **Scan 9:** F_M is the set of closed, pairwise-≍ subsets, the "Nablien universel".
- **Scans 10-11, 27 June:** Prop 1-3 and their corollaries; ≪° is transitive through Mag 3 b.
- **Scans 12-14:** Prop 4, the gluing of refinements, and Raff(F).
- **Scans 15-17:**
  - the axioms for lieux: x ∥ y ⇔ x |∘| y; omb(X); Mog L1 (omb° ≠ ∅); Mog L2;
  - a Proposition-Scholie: a strictly divisible magma corresponds to (≤, ≪) with ∥ on L (Mog div 3);
  - Mog quasi.
- **Scan 18:** a set-theoretic magasin is a set L with a family of subsets: "le point de vue 'atlas' … nous avait plutôt compliqué la vie".
- **Scans 19-21, 27-28 June:**
  - antifiltres and atlases (Mag atl a-d);
  - At Fil, the stability axiom for infinite gluing;
  - At 1-At 5 with Mag 1-4;
  - the Scholie of the two points of view.

**156-9, July 1986 (in SA21-10 and SA21-11 for now; it needs an item of its own): ateliers, again from the start.**
- **Scan 3:**
  - Question: for x ∈ 𝓛, is x° = supp x a minimal element of Σ* = Σ∖{0_Σ}? He reduces it to finding, for x ≠ y in 𝓛, a Z with Z |∘| x and not Z |∘| y, and notes "Je n'y ai pensé que dans le cas x non-|∘| y".
  - "Requestion: opération de saturation d'un atelier, en sens contraire … J'en doute !"
  - A table of contents "T 1 : T 10", with "Les trois dernières pages … tirées avec le fascicule 4". Reader C read the sheet as a reprography order for Récoltes et Semailles ("Fascicule 0"), not a table of the 1986 notes (H12 refuted, SA21-K9-01).
- **Scan 4, 15 July: "Diagramme des principaux types d'ateliers (ou de 'contrées')".** The types are G (general), S (spatial), SF, LS (local spatial), FLS = E (faithful local spatial), Mq (maquettes) and SDiv. The margin: "À vérifier que la bonne notion d'atelier modéré doit bien impliquer qu'il est, non seulement spatial mais encore, fidèle. Sinon, diagramme moins joli !"
- **Scan 5, 5 July:** "L'affaire a tendance à s'enliser, et j'ai envie de tout reprendre, d'une façon un peu différente."
  - Notation ∂X ⊂ δX.
  - Incidence X ◁ Y iff X = x ∈ L, Y ∈ 𝓜₁ and x ∈ ∂Y.
  - "mieux introduire d'abord la relation ≤ sur 𝓜", with the intervals I°_{a,b}, I_{<a}, I_{>b}.
  - X ≪ Y ⇔ ∃Y′, X ≪° Y′ ⊴ Y.
- **Scans 6-7: the one-dimensional model.** Points a ∈ L and intervals are ordered by a < I_{a,b} < b.
  - X < Y ⇒ δX ∪ δY ∈ Drap(L).
  - Cor: X < Y, X′ ≪° X, Y′ ≪° Y ⇒ X′ < Y′.
  - Déf: X |∘| Y ⇔ X < Y or Y < X. "Le corollaire précédent montre Maq 3, et Maq 4 immédiat".
  - Proposition: X ≍ Y ⇔ X = Y or X |∘| Y.
  - Corollaire: a finite Φ ⊂ 𝓜 is a préfigure iff it is totally ordered, that is, a flag of 𝓜.

**What the later parts add to 156-4:**
1. The ombre is fixed (156-6/7).
2. The set-theoretic model is a sorite of its own (156-5).
3. The axioms move from figures to multistrates with ≤, ≪, |∘| and ∥: Mag 1-4 (156-8/8) and At CD (156-7/10-11).
4. Spacious, polyhedral and simplicial ateliers are separated (156-7).
5. The maquettes, the T₀ (Alexandrov) spaces, are a tame non-set-theoretic class (156-8/3). The oriented ones of dimension ≤ 1 are Serre's graphs. His "Sauf erreur" for dimension 2 needs "∂X connected" (reader C; §0, item 4).
6. In July (156-9/5) he restarts from the one-dimensional case, where figures are flags.

## 6. How it connects

**Within cote 156:**
- **156-1 to 156-3:** the one-dimensional and network cases.
- **156-4:** the contrée, first intrinsic, then (F, ≤, ⪯).
- **156-6 to 156-9:** the ateliers.
- **156-8:** reorganizes the axioms around magasins and |∘| (the broad agent's report, sweep2/REPORTS/cote156_against_tame_topology.md).

**To the tame axioms of cotes 120-121 (SA10-19, SA11-3):**
- A figure of 156-4/2-3 is a tame stratification with the frontier condition.
- "Contrée modérée" (156-4/70) means common subdivisions (refined in round 2: it is Cor 2 of 121/016, not the Hauptvermutung; see HUNCHES H2). It was first read here as the Hauptvermutung for subdivisions, which for definable sets is Shiota's theorem (SA10-5, SA11-4).
- These are my readings (H2, H7). The 120-121 side belongs to SA20's agent.

**To the "ombre" question (SA10-2, SA11-1, H05G):** the 1986 definition (156-4/36, 88-89).

**To cote 154 (SA11):** the pseudo-discs with chords (156-4/32) beside the disk model with chords of the pseudoline surface (H5).

## From the sub-agent readings

<!-- reading:156-3 -->
### From the reading of 156-3 (sub-agent; the full reading is readings/156-3.md)

**156-3, "Réseaux … via découpages", CF III, 8-9 June 1986, scans 2-41.**
- Read in full by Claude Opus 5.5 at effort max (reader B, sub-agent of a6d42bf6fe2b0d8a8) in the transcription, with no scan image viewed (readings/156-3.md).
- Michel Hua's project was used as a credited witness of remarks.

**What the part does.** A second axiomatics of the one-dimensional networks of 156-1/2: tame pairs of lieux (the 0-spheres S₀), and the connected components of the "tame complement" C(T) of a finite tame set (scans 2-6). In order:
1. **The ordered line (scan 7), and the definition of the "tronçon ordonné" (scan 9).** An ordered set that is divisible, directed both ways, with directed cones. It need not be totally ordered; ℝ² with the product order and the doubled line are tronçons.
2. **A tronçon is known up to reversal from strict betweenness** (Lemme, scans 12-14). Betweenness is in turn read off the cuts: for a < b < c only b has its two components disjoint (scans 15-16). Both re-proved; they use divisibility.
3. **The tronçons form the largest class closed under cones** (scan 17).
4. **Closed tame parts** (scans 18-22). Finite unions of mutually tame, disjoint wide closed sub-tronçons. Their decomposition is unique, and intersections and tame sups exist (Prop scan 20). His own counterexample: no tame closure of {0} ∪ {1/n}.
5. **9 June, topologies** (scans 22-25).
   - The interval topology is T₀ for ficelle lieux.
   - His question whether every tronçon is T₀: answered no, by the doubled line. Michel Hua's project gave the answer first, with "ℝ with a doubled origin".
   - Sobriety stays open.
6. **Pseudo-tronçons, the interstitial tronçon, Mod(L)** (scans 26-34).
   - Mod(L) is the poset of tame parts, with a tame complement X′ and a closure.
   - Properties 1)-8) make the mutually tame families Boolean.
   - His margin asks whether tameness is "X ∧ Y exists": refuted in ℝ².
7. **Relativization, components, and the Boolean algebra of a subdivision** (scans 35-40).
8. **His ending** (scan 41). "Ça doit avoir été fait depuis longtemps (Hilbert ?)". He is right for total orders: Hilbert 1899 §3; Huntington-Kline 1917. The recovery of betweenness from cuts in non-total tronçons is not covered there.

**The main connection.**
- For a totally ordered tronçon, Mod(L) is exactly the family of finite unions of points and open intervals: the definable sets of the o-minimal structure (L, <) (also in Michel Hua's project). So "modéré" on the line is the o-minimal condition, written down in June 1986. It is contemporary with Pillay-Steinhorn 1986.
- 156-7/71 corrects the terms of this part: the tame parts should be "constructibles", and the closed ones "modérées". It reuses the tronçon of 156-3/9 for the Stratos of an ordered set.

**Checked:** 13 check events. **Corrected:** 8 (four slips, one refinement, his own renaming, one refuted conjecture, one answered question).

**Open:**
- the axioms on betweenness or on the cut data characterizing a tronçon (scans 17, 41), in the non-total case;
- sobriety;
- properties 1)-8) for non-total tronçons;
- the axioms of scan 4, announced but never written.
<!-- /reading:156-3 -->

<!-- reading:156-5 -->
### From the reading of 156-5 (sub-agent; the full reading is readings/156-5.md)

**156-5, "Sorite ensembliste", GF V, 14-18 June 1986, scans 2-49 (SA21-14): the set-theoretic model of the contrées and ateliers.** It begins on 14 June, the day 156-4 ends, and runs into the first days of 156-6.

**Préadmissible and admissible families (scans 2-8).** For a family 𝓛 of subsets of L, Proposition 1 gives three equivalent forms of "every point lies in a smallest member". They hold on all 65,536 families on 4 points (SA21-R5-01).
- Admissible means in addition non-empty open strata A° = A ∖ ∂A, so ∅ is excluded.
- His Remark that η is "pas surabondante" holds only for infinite families. For artinian families γ alone gives η; his margin already calls his drawn example "idiot" and points to GF VIII, pp. 44-45.
- **An admissible family is an ordered set I with a surjection φ: S → I**, that is, a preorder on S ⊂ L. Its members are the irreducible closed sets, and the "parties 𝓛-constructibles" are the saturated sets.

**The figures ensemblistes (scans 8-12).** Compatibility of two families has four equivalent forms: a union in which both are closed; closed intersection with the common support; the common-support form; stratum by stratum ("Remords"). All four agree on all pairs on 3 points.
- The admissible families, ordered by "closed sub-family", are the **figures ensemblistes** Fig(L) of 156-6/3.
- Their irreducibles, the families with a largest member, are the **multistrates ensemblistes**.
- C1-C3 of 156-4's fourth system hold.

**Connectedness (scans 13-15): false.** He concludes that the multistrates form one component, so "l'axiome C4 ... est automatique". His bounding "multistrates" {A, {x}, A ∪ {x}} and F ⊠ G are not admissible: the top member is the union of the others. Computed: 3 components on 2 points and 5 on 3, with incompatible pairs across components. So **156-4's C4 fails in Fig(L)** (SA21-K5-01). 156-6 has no component axiom.

**Supports (scans 16-17).** Disjoint figures are those with disjoint supports, and the supports are P(L). From the figures one recovers P(L) but not L: "L̂, le compactifié de Stone" (H3, H6).

**Refinement and subdivision (scans 20-27).** Four equivalent forms of refinement; the simplest is that the preorder of F is finer than the one G induces on |F|. Four equivalent forms of subdivision; the simplest is refinement with the same support, equivalently maximal refinement. And F ≪ G ⇔ F is a sub-figure of a subdivision of G (156-4's definition (1.29) holds in this model). All are computed.
- Scan 27 states, in the model, the condition that 156-6 makes its At 13 (the "axiome du support").
- Scan 27 checks C5, C6, C7 and C8₀ of 156-4 in this model. **156-5 is the model test of 156-4's fourth system.**

**Intersection and extension (scans 28-36).** The "figure intersection" F.G is the Inf for ≪, "s'apparente à une propriété de 'modération'".
- C7: F′ = G′ ∪ (F ∖ G) extends a subdivision of a sub-figure (computed).
- The coarsest such extension K = J′ ⨿ (I ∖ J), with a cartesian square, is the model of 156-6's At (fac) 14 bis.

**Ultratopologies (scans 37-49, 18 June).** "le point de vue des ultr. topologies (i.e. top. préordonnées) est peut-être le plus pratique".
- A lemma on the coarsest topology extending a finer topology on a closed part (re-derived).
- Corollaries on "homotopiquement propre" maps and "équivalence d'homotopie faible universelle" (scan 47; not re-derived).
- His own "C'est ultra faux", with a three-element counterexample, ends in the right characterization: closures of parts outside T are unchanged.

**Counts:** 16 check events, 5 corrections. No scan image was viewed; the open readings are listed in `156-5.md` §8.
<!-- /reading:156-5 -->

<!-- reading:156-6 -->
### From the reading of 156-6 (sub-agent; the full reading is readings/156-6.md)

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
<!-- /reading:156-6 -->

<!-- reading:156-7 -->
### From the reading of 156-7 (sub-agent; the full reading is readings/156-7.md)

**156-7, "Analysis Situs (troisième mouture)", Chap VII, 23-26 June 1986, scans 2-114.** Read by Claude Opus 5.5 at effort max (reader B, sub-agent of a6d42bf6fe2b0d8a8): scans 2-60 line by line, 61-114 for statements and proofs, five scans checked on the images (readings/156-7.md). His own pointer: "Cf surtout p. 23, 50-58, 59, 110-113" (scans 24, 51-60, 111-114).

**What the part does.**
1. **The atelier (𝓕, ≤, ≪) and its "sine qua non" axioms At 1-At 7 (scans 2-7).** With figures of finite type, (𝓕, ≤) is (M, ≤, ≍), the (M, ≤, R) of 156-4/62.
2. **The disjunction and compatibility axioms (scans 8-24).**
   - At CD, the "axiomes obligatoires" (scan 10): compatibility and disjointness of refinements are tested over the intersection.
   - The absolute compatibility criteria split the ateliers into spacious (At CD 2) and polyhedral (At CD 2′, scan 11).
   - Strict refinement and the "condition de la stricte intersection" (scans 12-14).
   - At simp 1 (scan 15).
   - At C, At D, At fil, At supp, At ens D, and the lieux axioms At L1 (divisibility, "l'introduction de l'infini actuel"), L2, L3 and CL.
   - The recapitulation (scan 24).
3. **A representation theorem, the Théorème-Scholie (scans 25-39), re-derived both ways.** A spacious atelier with L1-L3 and CL(spac) is the same as (M, ≤, ≪) with ML 0-ML 3 plus a disjointness graph on the ≪-minimal elements. Any graph containing the forced pairs Γ₀ will do.
4. **Dense parts Λ and the pre-ateliers (scans 40-54).**
   - The Λ-version fails: "Je n'arrive pas a le prouver". The block is that non-minimal elements of Λ can refine L in part.
   - The pre-atelier (M, ≤, ≪, ≍), with three axiom systems, is his summary (scans 51-53).
   - On any ordered set, ≪ = ≤ gives every axiom except divisibility.
5. **Set-theoretic and quasi-set-theoretic ateliers (scans 55-61).** With his own counterexamples (two affine structures on an arc; ≪_ens against ≪_pol), and the name "Stratos" (Codex "Stratop").
6. **Supports (scans 62-101).**
   - The lattice Σ of bi-orthogonally closed sets, with Σ ≅ P(L) when disjointness of lieux is "≠".
   - His own counterexamples: the "ficelle à deux brins", against distributivity (scans 82-84); a path A′–A–B–B′, against his formal Lemma (scan 99). That Lemma is the orthomodular law.
   - Realization by supports (scan 81).
7. **The turn (scans 102-114, 26 June).** The new primitive |∘| ("intérieurement disjoints"); "la ribambelle d'axiomes ... tombe en un bruit floche, Je reprends tout, encore une fois !". The magasin Mag 1-4 (scans 111-114) is the source of 156-8/8.

**What is proved:** the Théorème-Scholie, the polyhedral Lemme, L2 + L3 ⇒ D, his realization Proposition, his two counterexamples, and Mag 6 from Mag 4″ + 5″ (31 check events).

**What is wrong (10 corrections):**
- At 6's hypothesis "X ◁ F", which should be X ≪ F (image);
- his characterization of simplices. The face poset of a square satisfies "polyédral + At simp 1", so the "ateliers simpliciaux" of scan 15 are polytopal; simplices need distributivity (Birkhoff);
- Lemma 1 (scan 26), which lacks "X, Y ≤ Z";
- Lemma A, where Codex reads ≪ and the ink has ≤ over ≪;
- the distributivity of supports, false.

**Decided:** "Axiome des Cat PL VI p.52" (scan 13) is GF VI = 156-6 p. 52 (scan 53), the axiom At ens 1. The two margins point at each other. It is not a separate text on PL categories.

**Open:**
- the Théorème of scan 94 under L1, which needs orthomodularity of the supports of one figure's open strata;
- the Λ-criterion;
- the readings listed in the DELIVERABLES row.

**Connections:**
- 156-6 (cited pages 28, 32, 40, 51, 52, 67-68, 73);
- 156-5/20-21;
- 156-3 (scan 71 corrects its terms: "modérée fermée" should be "modérée", and "modérées" should be "constructibles");
- 156-4/62 and 66-69;
- 156-8/8 and 31.
<!-- /reading:156-7 -->

<!-- reading:156-8 -->
### From the reading of 156-8 (sub-agent; the full reading is readings/156-8.md)

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
<!-- /reading:156-8 -->

<!-- reading:156-9 -->
### From the reading of 156-9 (sub-agent; the full reading is readings/156-9.md)

**156-9, GF IX and CF IX bis, 5-15 July 1986, scans 2-140** (SA21-10; it needs an item of its own).
- Read by Claude Opus 5.5 at effort max (reader C, sub-agent of a6d42bf6fe2b0d8a8): scans 2-9, 46-50, 78-80, 109-111, 115-118 in full, the rest by statement lines (proofs not worked through); scan 3 on the image.

**Documentary.**
- The "Table des Matières T 1 : T 10 ... fascicule 4" of scan 3 is the right half of a folded sheet: a reprography order for "Fascicule 0" (Page de garde, Lettre L 1-L 43, Table des Matières, Introduction i-cxxii; 300 copies; "Mme LACAN"). It fits Récoltes et Semailles, not the 1986 notes. **H12 is refuted.**
- Scan 114 is a Récoltes et Semailles leaf (p. 1074, 8 May 1986).
- On 9 July (scan 41) he swaps the words: "je dirai 'atelier' là où je disais 'magasin', et inversement". Mag 1-4 become At 1-4. An edition and a translation need this in the glossary.

**The types (scans 2-4, 15 July).** The 156-8 classes, renamed: G, S (spatial), F (faithful), L (local), P = FL (ponctuaire), E = FLS (set-theoretic), M (tame), EM, Mq, D, Div.
- His presumption: tame ateliers are spatial, Σ is "modulaire ... donc une algèbre de Boole", "Il est possible que cela implique que l'atelier est aussi fidèle".
- As stated it fails: M = {x, y}, two non-disjoint lieux, has Σ = {∅, M}. It holds, both ways, in the form "under divisibility and Mag L2: faithful ⇔ Σ Boolean with the lieux as distinct atoms". This joins the 156-8 result that faithful magasins have Σ = regular open algebra.
- His Question (scan 3), whether supp°x is minimal: positive in faithful divisible magasins and in the two-strand ficelle; open in general.

**5 July, the restart (scans 5-9).** "L'affaire a tendance à s'enliser".
- The data: an ordered set L, with points and intervals I_{a,b}, and the positional order a < I_{a,b} < b. This is the magasin of an ordered set of 156-8/90-127.
- |∘| is comparability for this order. X ≍ Y ⇔ X = Y or X |∘| Y.
- **The figures are the flags (finite chains) of the positional order, closed under incidence.** Re-derived. This confirms H10, but the flags are chains of the positional order, not of the incidence order.
- With infinite intervals I_{<a}, I_{>a}, the duality cosupp°Φ = Omb°Φ* (scan 16) completes 156-8's broken-off computation.
- Then residual and sum magasins, and compactologies (8 July): "la base technique ... est plutôt notion de magasin compactologique".

**9-10 July, supports as ortholattices.**
- Spatial ateliers: ≪ is read off the supports of the strata ("l'espace occupé"), with axioms At spat 1-3 on (𝒜, ⊴, |∘|) alone.
- **Spatios = complete lattice + order-reversing involution C with x ∧ Cx = 0: a complete ortholattice.** Prop 1, every spatios is the support lattice of its own disjunction x ≤ Cy, is re-derived. It is reader B's H7-2, made by him into the definition.
- **Lemma 1 / Cor 1 (scans 109-111) are the orthomodular law** and its characterization by Boolean subalgebras generated by comparable or orthogonal pairs.
- His Questions are answered: not always (his margin: "Card Σ = 10"); the hexagon O₆ already arises from the fence a′ < a > b < b′, settling his "avoir le cœur net ... quand Σ est défini via un ens. ordonné"; and orthomodular does not imply Boolean (MO₂).

**The axiom of supports (scan 117).** The family of open strata of every figure is "admissible". For spatial figures of a spatios this is exactly the orthomodular law "e |∘| e′ ⇒ e′ = Ce ∧ (e ∨ e′)".
- It fails for O₆ (his "Oui !" of 156-8/89) and holds for faithful magasins.
- His diagnosis (scan 128): "Ce sont mes 'cordes' ... qui causent tous les ennuis ... et les seuls ennuis." The two readings prove it for the faithful side.

**12 July, CF IX bis (scans 130-140).** Morphisms of ateliers: a figure is a sub-atelier (a maquette); a provisional homomorphism is f: A → A′ ⨿ {∅} preserving ⊴, ≪°, |∘|.

**Counts:** 12 check events, 3 corrections.
<!-- /reading:156-9 -->

<!-- reading:156-7_061-114 -->
### From the reading of 156-7_061-114 (sub-agent; the full reading is readings/156-7_061-114.md)

**156-7, scans 61-114 (25-26 June 1986), read page by page in round 2** by Claude Opus 5.5 at effort max (reader B, sub-agent of a6d42bf6fe2b0d8a8). The reading is readings/156-7_061-114.md: 31 check events, 17 corrections, ten scans checked on the images. It completes the first reading (readings/156-7.md), which took these scans by their statements. It uses reader C's results on Σ rather than redoing them.

**What the pages do, in order.**
1. **The name (scan 61).** The quasi-set-theoretic pre-atelier, "à peine plus compliqué qu'une topologie", is to be called **"Stratos"**. Codex reads "Stratop" there and "Anatos/Antos" later; the word is decided on the images of scans 61 and 67.
2. **Supports (62-69).** Σ is the bi-orthogonal closure of disjointness, a complete ortholattice.
   - His margin asks whether disjointness of supports is the same as orthogonality. For all pairs that holds exactly when Σ is Boolean, and the same is true of the converse of his (x).
   - Disj_Λ transports supports to a dense part, and to the lieux under At L2.
   - A struck page (69) already has the realization of scan 81.
3. **The stratos of an ordered set (70-73),** with all axioms except divisibility. Compatibility must be read as his cases α/β, not "intersection a point". "card X̃ = 1" in the ink (Codex 0).
4. **Realization by supports (74-81).**
   - The Proposition: under Supp¹ and Supp², Σ_M ≅ P(P), commuting with ∁.
   - His suspicion that (iv)_M follows from the others holds under his Hyp.
5. **The two-strand ficelle (82-84):** distributivity fails ("ne sont pas comparables" in the ink). His Conclusion-Scholie restricts supports to compatible strata.
6. **Open strata (85-101).**
   - X° = supp X ∩ cosupp ∂X; At supp 1 (Y ∈ X° ⇒ Y ≪ X), "un axiome vraiment crucial".
   - Lemmas 1-4 hold under L1-L3.
   - **The Théorème of scan 94 fails.** He hoped "du moins sous l'hypothèse de divisibilité Ax L1". It fails in an eight-element atelier with a seven-lieu disjointness graph satisfying At 1-7, L1-L3, CL(spac), At D, At supp and At supp 1. Both the relative complement and the inf commutation fail.
   - It holds where distinct lieux are disjoint (Σ Boolean). This is why 156-8/88 must pose it as "Axiome supp 1", which reader C identified with the orthomodular law, true in faithful magasins.
   - His formal counterexample (99) needs A′ and B′ unlinked, else the supports are Boolean.
   - The subdivision Lemma (100-101) holds under a faithful realization.
   - The foot of scan 101 is a reused Récoltes et Semailles typescript leaf, a new location for SA21-11.
7. **The turn (102-114).**
   - |∘| ("intérieurement disjoints") replaces ≍ and ∥; Mag 4″ replaces At L3.
   - The Scholie matches ≍-magasins with L1-L3 and At C(spec) to |∘|-magasins with Mag 6″.
   - The struck first list (110) had the induced refinement as an axiom. In the final Mag 1-4 (111-114) it is a theorem, through At 7 (reader C's Prop 3 at 156-8/11).

**What it means for cote 156.**
- Supports are a sound formalism exactly where distinct lieux are disjoint (quasi-set-theoretic or faithful). Outside it, divisibility does not repair them, which his own counterexamples (84, 99) already suggest.
- The move of 26 June to |∘|, "une notion de disjonction intrinsèque", is his response, and the axiomatics that 156-8 and 156-9 build on.

**Open:**
- the name in his parenthesis of scan 61;
- the ≪° margin of scan 70;
- (iv)_M without Hyp;
- the subdivision Lemma without a realization;
- which ateliers with cords satisfy the Théorème.
<!-- /reading:156-7_061-114 -->

<!-- reading:156-9_rest -->
### From the reading of 156-9_rest (sub-agent; the full reading is readings/156-9_rest.md)

**156-9, the rest read page by page (sweep 3, round 2): scans 10-45, 51-77, 81-108 and 119-140.**
- Read by Claude Opus 5.5 at effort max (reader C, sub-agent of a6d42bf6fe2b0d8a8), with scans 10, 113 and 130 on the images and computations in `156-9_rest_checks.py` (readings/156-9_rest.md). With the first reading, all of 156-9 is now read except the drawings of scan 112.
- Michel Hua's project is credited where it makes the same identifications.

**5-6 July: the complement duality.**
- He adds infinite intervals I_{<a}, I_{>a} to the magasin of an ordered set. The rule is X ≪° I_{<a} iff X < a positionally; the transcription's "≤" is resolved by the image and the computation.
- His theorem cosupp°(Φ) = Omb°(Φ*) for polygons (scan 16) is re-proved and computed on 21 492 polygons. It completes the duality on which 156-8 breaks off.
- His formula δΦ* = δΦ ∖ Φ_red fails at extreme points; he repairs it himself on 6 July.
- Constructible parts Omb°(Φ) are in bijection with finite polygons. With infinite intervals over a non-divisible L they collide.
- **For the oriented segment he proves the axiom of supports At supp 1 ((CΦ)** = Φ*); re-derived.** Computed for all 4 724 figures of the magasins of the 203 connected orders with at most 5 elements. **So Axiome supp 1 holds in the magasin of an ordered set; it fails only in lieux-only disjoncteurs such as the fence's O₆.**

**6-8 July.**
- Residual magasins M(J, Ω₀, Ω₁), and direct sums.
- Sub-magasins: Omb°(Φ) is one. The residual cosupp°Φ is not: his two-triangle counterexample is checked. The "large" residual is one.
- **Compactologies (M, ⊴, ≪°, |∘|, M_c)**, "la base technique de l'approche combinatoire de la topologie que je propose".
- The terminology swap of scan 41.

**9-11 July: supports as complete ortholattices, correspondences, transposition.**
- A spatial atelier is a spatios with a family of elementary spatial figures whose tops are join-dense (Dedekind-MacNeille-type; re-derived).
- Disjoncteurs (strict graphs) and correspondences α: E → P(E′).
- **His Lemme 1 (scan 72) is false** (twin disjoncteur). His own Prop 4 (scan 97) repairs it with a condition "rajoutée après-coup".
- Prop 4's equivalences are proved, including the two he marked "?" and his NB "J'ignore si ..." (yes). They are computed on 3 000 random pairs; in 989, sup-preservation without his added condition fails.
- Cor 1 (density ⇔ injectivity of S ↦ S ∩ E′) holds; a direct proof replaces his route through Cor 2.
- Correspondences with closed rows and columns are the bonds of formal concept analysis (also in Michel Hua's project). Transposition is C∘(right adjoint)∘C, a dagger structure ("Analogie avec les espaces de Hilbert ... opérateurs adjoints").
- **His Question (scan 108)**, whether α_*, β_* commuting with C are inverse isomorphisms: his "(oui.)" is proved.

**Scans 112-129.**
- The drawing of the "Card Σ = 10" counterexample (scan 113) is not reconstructed: the transcribed arrows do not form a lattice.
- Admissible families and the orthomodular instance (Lemme 2).
- "il n'est pas clair que ≪°_comm soit transitif !" is left open.
- His critique ends: "Ce sont mes 'cordes' ... qui causent tous les ennuis", and "peut-être les ateliers fidèles ?" (that Σ is Boolean): answered yes by the 156-8 reading.

**12 July, CF IX bis.**
- Morphisms of ateliers. The margin "CF XIII" is CF VIII pp. 46 and 27 (156-8/55, /36), by content.
- Sub-ateliers: a figure is a maquette. Provisional homomorphisms into A′ ⨿ {∅}; Ker f is ≪°-closed.
- The excision A/N is left open. Subdivision is read by lieux (156-4/42).

**Settled from the packages.**
- **Question of 156-9/3: true** for the magasins of connected ordered sets, proved with explicit separating strata and computed on 988 lieux; **false** for local ateliers in general (path a′–a–b–b′, twins).
- **H9-1 (orthomodular ⇔ cograph): "⇐" is proved** (horizontal sums and products). **"⇒" is refuted**: on 5 vertices 60 comparability graphs with an induced P₄ are orthomodular, for example an order whose Σ is 2³.

**Counts:** 29 check events (SA21-R9b-01 to -29), 9 corrections (SA21-K9b-01 to -09).
<!-- /reading:156-9_rest -->
