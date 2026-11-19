# SA21, Vers une géométrie des formes (cote 156): hunches

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

**What this file is:**
- A hunch is what may be true, with its grounds: the pages, the items, and the links to other topics and to the literature.
- None of them is proved here. Where a hunch rests on a step I checked, the check is in CHECK_EVENTS.tsv.
- Literature is named from memory. Every locator marked "locator to be checked" must be checked before a prompt or a text uses it.
- The research packages built on these hunches are in RESEARCH_PACKAGES.md.

## H1. The finitist contrées of 156-4 are prime event structures

**The hunch.** The structure of 156-4/62 is the same thing as a prime event structure of Nielsen, Plotkin and Winskel, and its figures are that structure's configurations:
- (M, ≤, R), with M_{≤x} finite and R reflexive, symmetric and closed downward;
- figures as the finite, downward-closed R-cliques.

**The dictionary:**
- ≤ is causality, with finite causes;
- the complement of R is conflict, and conflict is inherited upward exactly when R is closed downward;
- figures are finite configurations;
- refinement and subdivision become maps of event structures.

**Grounds:**
- 156-4/62, checked (CHECK_EVENTS, SA21-C3-05).
- Conflict inheritance is the dual of his condition that R is closed downward.

**Literature:** M. Nielsen, G. Plotkin, G. Winskel, "Petri nets, event structures and domains, part I", Theoretical Computer Science 13 (1981), 85-108 (locator to be checked).

**Why it matters:**
- The finite configurations of an event structure form a coherent, prime algebraic domain. That is a known order-theoretic description of his figure order (F, ⪯).
- His Σ (supports) would then be a known lattice of the domain.

## H2. "Contrée modérée" is the Hauptvermutung taken as an axiom

**Refined by aff4deb18a6ec3192, round 2 (sweep3/SA10/readings/axioms_120_121_156.md):** "contrée modérée" means that any two subdivisions of a figure have a common subdivision. That fails in plain topology (a diameter of a disc against an arc crossing it infinitely often), holds o-minimally by the stratification theorem, and is Corollary 2 of 121/016. It is not the Hauptvermutung, which is about homeomorphic polyhedra; the link to the Hauptvermutung is withdrawn. The figure of 156-4/2-3 is 121/052 condition by condition (H7 confirmed).

**The hunch.** "Contrée modérée" (156-4/70) asks that any two subdivisions be comparable, meaning that they have a common refinement. That is the Hauptvermutung for subdivisions, made into an axiom.

**What it predicts:**
- For semialgebraic, subanalytic or o-minimal sets it holds. There, any two definable triangulations have a common definable subdivision up to definable homeomorphism, by Shiota's theorem.
- For general topological polyhedra it fails, by the Milnor counterexample.

**Grounds:** 156-4/70; the tame axioms of cotes 120-121 (SA20-12 to SA20-15, not read tonight); SA10-5 and SA11-4.

**Literature:**
- M. Shiota, *Geometry of subanalytic and semialgebraic sets*, Progress in Math. 150, Birkhäuser 1997, ch. II (locator to be checked);
- J. Milnor, "Two complexes which are homeomorphic but combinatorially distinct", Annals of Math. 74 (1961), 575-590.

**Why it matters:** this is the place where "géométrie modérée" enters the axioms of the forms. It shows what he meant by tame in 1986.

## H3. The supports Σ: a lattice of closed sets, and when it is Boolean

**Settled further by reader C (readings/156-8.md, 156-9.md):**
- In faithful magasins, Σ_M is the complete Boolean algebra of regular open sets of the Alexandrov topology of (M, ≪°).
- Under divisibility and Mag L2: faithful ⇔ Σ is Boolean with the lieux as distinct atoms. The plain "distributive ⇔ faithful" is refuted.
- His axiom of supports (156-9/117) is the orthomodular law. It fails on the hexagon O₆, and MO₂ is orthomodular but not Boolean.
- What remains is the non-faithful case of cords and strands (H8-1, H9-1).

**Settled in part by reader B (readings/156-7.md):** distributivity fails, by his own counterexample (156-7/84). His formal lemma (156-7/97-99) is the orthomodular law, also false. The supports are canonically P(L) exactly when distinct lieux are disjoint.

**The hunch.** Σ (156-4/66-69) is the lattice of the sets closed under the Galois connection of the disjointness relation, that is, of the bi-orthogonally closed sets.

**What is known:**
- In the set-theoretic case Σ is Boolean, and its Stone space is β of the discrete set. I checked this (SA21-C3-08).
- Under his axioms, distributivity is open. His own doubt is on scan 69.
- My test lattice MO₂ is excluded by C4 when M is discrete, so it is no counterexample.
- 156-8/3 has a class of magasins "Σ_M ≃ P(L)". The question of 156-9/3, whether supp x is an atom of Σ* for a lieu x, is the step to that class. His own reduction is a separation property: for x ≠ y there is a Z with Z |∘| x and not Z |∘| y.

**The hunch, sharpened:** under local finiteness, Σ ≃ P(L) holds exactly when that separation property holds.

## H4. The ombre of 1986 answers H05G

**What the 1986 ombre is:**
- the set of lieux that refine a figure (156-6/7);
- with lieux as points, the underlying set |F| (156-4/36, 88-89);
- the multiombre F̂ is the family of the strata's ombres;
- the "grande ombre" Omb_𝓜(F) and Multomb(X) = {Y | Y ≪ X} are its versions on 𝓜 (156-6/5).

**A correction to my own premise.** The word "ombre" does not occur in the transcriptions of cotes 150 and 151 (MPL_150_001-043, 044-084, 085-099+151_001-031, 151_032-075). It does not occur in those of 121 (pages 49-73), 153, 155 or 154 either; the matches there are "nombre". Cotes 150-151 speak of "voisinages tubulaires" V_{X_i,X_j} (151/44, 57, 69, 71). The notes find "ombre" only as a use, never defined:
- 1975: the étale-tubular passage on 149/133, with uncertain readings "l'ombre", "ombres" and "tubulures étales", next to an expression in X̂∖D (notes C150 Q1a-Q1d);
- cotes 67, 136 and 147 (SA10-2, SA22-7).

**The hunch:**
- The 1975 use and the 1986 definition may be the same notion: what a structure living above a space casts on that space.
  - In 1975 that is perhaps what a tubular neighbourhood of D casts on X∖D.
  - In 1986 it is the lieux that refine a figure.
- If so, 156-6/7 is the only definition of the word in the archive read so far.

**What is to be done:** a comparison of the uses (SA10-2) is a package (P4).

## H5. The pseudo-discs with chords are the disk model of cote 154

**The hunch.** The pseudo-discs with "cordes" of 156-4/32 are the same combinatorial object as the disk model with chords of the pseudoline arrangements on cote 154 (SA11-12). He met it there first and generalized it here.

**Grounds:**
- 156-4/32, where the pseudo-discs bring him to (M, ≪, R): "la topologie combinatoire sans points";
- the SA11-12 notes of sweep 2.

## H6. From points to multistrates is pointless topology

**The hunch:**
- Taking the order of figures as primary, and recovering points as lieux, is the move of locale theory.
- The distributivity of Σ is the frame condition.
- His set-theoretic contrées, where Σ ≃ P(L), are the spatial ones. His word "spatial" for ateliers (156-9/4) has the same sense.

**Literature:** P. T. Johnstone, *Stone spaces*, Cambridge 1982, ch. II (locator to be checked).

## H7. A figure is a stratification with the frontier condition

**The hunch:**
- A figure of 156-4/2-3 (conditions (a)-(f)) is a finite stratification with the frontier condition.
- Cont 2 (156-4/18-25) is that condition.
- The adapted partitions of cote 121 give magasin data.

**Grounds:** 156-4/2-3 and 18-25, read in full. The 121 side is not read (SA20-12 to SA20-15, left to me by ae4ae3dc17acaa440, not reached tonight).

## H8. The frontier problem of 156-4/17

**The problem:** the frontier condition for the components of Uᵢ∖X′, which he calls "un pb … intéressant".

**The hunch:**
- It is false for topological stratifications: wild examples exist.
- It holds after refinement in tame (o-minimal) categories, where every definable stratification can be refined to satisfy the frontier condition.

## H9. The maquettes are finite T₀ spaces, and the oriented ones of dimension ≤ 2 are regular cell complexes

**Refined by readers B and C:**
- In dimension ≤ 1, oriented maquettes are Serre's graphs (156-8/6; Michel Hua's project first).
- In dimension 2 his "Sauf erreur" is not right as stated: the axioms admit 2-cells bounded by several disjoint cycles and exclude the one-vertex torus. With "∂X connected" added, they are the 2-complexes with simple closed attaching paths.
- Polyhedral + At simp 1 does not characterize simplices: the face poset of a square satisfies both (156-7/14-15).
- See H8-2 and P8-2.

**The hunch:**
- The maquettes of 156-8/3 are finite (or locally finite) T₀ (Alexandrov) spaces: "un espace ultra top. … T₀". They are therefore posets.
- His claim on 156-8/6, "Sauf erreur", that oriented maquettes of dimension 2 are combinatorial cell complexes, is a version of a known result: a poset is the face poset of a regular CW complex exactly when each lower interval is the face poset of a sphere.
- For posets of dimension ≤ 2 that condition is checkable by hand: thin intervals (the diamond property) and circle links.
- At simp 1 (156-7/15), "∂X empty or with at least two elements", is the first piece of that condition.

**Literature:**
- M. C. McCord, "Singular homology groups and homotopy groups of finite topological spaces", Duke Math. J. 33 (1966), 465-474;
- A. Björner, "Posets, regular CW complexes and Bruhat order", European J. Combin. 5 (1984), 7-16 (locator of the statement to be checked).

**Why it matters:**
- This is where the programme questions on finite T₀ spaces and pro-objects of finite posets (SA21-8, P01-P16 of the notes) meet his own text.
- The README conjecture, a form recovered from a pro-object of finite posets, is not on these pages (P01). The maquettes are the nearest he comes.

## H10. In the July restart, figures are flags

**Confirmed and corrected by reader C:** the figures are the flags of the positional order a < I_{a,b} < b, not of the incidence order (156-9/6-8; 156-8/106-107). See H8-3 and H9-1.

**What 156-9/5-7 does:** he restarts from the one-dimensional model. There, points and intervals are ordered by a < I_{a,b} < b, and a finite family is a préfigure exactly when it is a chain.

**The hunch:**
- The general case of this restart is the poset of strata of a regular cell complex with its flags.
- A figure is then a subcomplex of the barycentric subdivision.
- This is the same link as H9, approached from the other side.

## H11. REFUTED by readers A and B: "VI p.52" (156-7/13) is 156-6, p. 52 (scan 53), the axiom At ens 1; the two margins cite each other (readings/156-6.md, 156-7.md). The entry below is kept as written.

### H11 as first written: "Axiome des Cat PL VI p.52" (156-7/13) points to an earlier text of his on PL categories

**The hunch:** the reference is to chapter VI, p. 52 of an earlier text of his on PL categories. That is probably the tame topology notes of cotes 120-121, or another archive cote.

**What is to be done:** locating it closes a dependency (DEPENDS row "candidate").

## H12. REFUTED by reader C: the sheet of 156-9/3 is a reprography order for Récoltes et Semailles ("Fascicule 0"), not a table of the 1986 notes (SA21-K9-01). The entry below is kept as written.

### H12 as first written: the 1986 series was organized in fascicules with a table of contents

**The evidence:** 156-9/3 lists a "Table des Matières T 1 : T 10" and says its last three pages were "tirées avec le fascicule 4". The parts of cote 156, marked GF (or CF) III to IX bis, would then be the fascicules.

**The hunch:** the table of contents, once read in full, gives the order of the parts and the titles he gave them. That decides the edition's structure.

## From the sub-agent readings

<!-- reading:156-3 -->
### From the reading of 156-3 (sub-agent; the full reading is readings/156-3.md)

**H3-1. Grothendieck's tame parts of a line are the o-minimal sets, and 156-3 is the one-dimensional case of H2** (sharpens H2).
- For totally ordered L, Mod(L) is the definable sets of (L, <). The facts he lists, X finite ⇔ X° = ∅ and the uniqueness of the decomposition, are the o-minimal monotonicity facts on the line. His "constructibles" (156-7/71) is the right word for that Boolean algebra.
- Grounds: 156-3/30-34, 40; 156-7/71; Michel Hua's project makes the same link.
- Literature: L. van den Dries, *Tame topology and o-minimal structures*, LMS LN 248, CUP 1998, ch. 1 (locator to be checked); A. Pillay and C. Steinhorn, "Definable sets in ordered structures I", Trans. AMS 295 (1986) 565-592 (locator to be checked).

**H3-2. The cut data (S₀, R_ε) of 156-3 determine the biorder for non-total tronçons too, and their axiomatization is a new, finite-type question.**
- For total orders betweenness is classical (Huntington-Kline 1917), and for partial orders the order from betweenness and comparability is in the literature (Michel Hua's project cites Altwegg 1950 and Courcelle 2020).
- The recovery from cuts (scans 15-16), and the axioms on (S₀, R_ε) that he left as an exercise (scans 17, 41), are not, per the same project's note on Courcelle.
- Grounds: 156-3/12-17, 41, re-proved here.

**H3-3. The Boolean algebra of a subdivision (156-3/40) is the germ of the supports of 156-4/66-69 and 156-7/62-68.** In dimension one, mutually tame parts generate a Boolean algebra whose atoms are the points and open intervals of the subdivision. The failure of distributivity found on 156-7/84 (two strands) is exactly where mutual tameness fails. This confirms his "Conclusion-Scholie" of 156-7/84 and sharpens H3: Boolean on mutually tame families, not beyond.
<!-- /reading:156-3 -->

<!-- reading:156-5 -->
### From the reading of 156-5 (sub-agent; the full reading is readings/156-5.md)

**H5-1. Fig(L) is the category of preorders on subsets of L, the Alexandrov (T₀ after quotient) spaces, and his 18 June switch to "ultratopologies" makes this explicit (sharpens H6 and H9).**
- **Grounds:** the (I, S, φ) description (scans 5-6); refinement as a finer induced preorder (margin b″, computed); subdivision as the same support (scan 24); scans 37-38.
- **What it predicts:** the maquettes of 156-8/3 ("un espace ultra top. … T₀") are this model taken abstractly, and the multistrates of an atelier under ≪ (156-6/30, H6-1) are its points.

**H5-2. Scan 47 is a fibre lemma for maps of finite T₀ spaces, the first homotopy statement in cote 156 (confirms the link SA21-8, H9).**
- **Grounds:** 156-5/47, "φ* homotopiquement propre i.e. les φ*⁻¹(J_{≤x}) 'faiblement contractiles'" and "équivalence d'homotopie faible universelle".
- **What it says:** the hypothesis is that of Quillen's fibre lemma for poset maps, and the conclusion is a weak homotopy equivalence, as for finite spaces in McCord's theory.
- **Literature:** D. Quillen, "Homotopy properties of the poset of nontrivial p-subgroups of a group", Adv. Math. 28 (1978), 101-128, Prop. 1.6; M. C. McCord, Duke Math. J. 33 (1966), 465-474 (locators to be checked).
- **The hunch:** his statement, that the property passes from φ* to φ, is a gluing form of that lemma along a closed part.

**H5-3. 156-4's C4 is false in the set-theoretic model, which is plausibly why the component axioms disappear after 156-4.**
- **Grounds:** SA21-R5-08 (computation), and At 1-At 14 of 156-6, which contain none.
- **The diagnosis:** his error is a join intuition. A union of strata has no new points, so it has no open stratum, while a geometric join has an interior. In models with cones (polyhedra, tame sets) the bounding multistrates exist.
- **What it predicts:** the component axiom holds in polyhedral or tame contrées and fails in Fig(L).

**H5-4. Two different tameness axioms (sharpens H2).**
- **Grounds:** 156-5/29, where the existence of an Inf for ≪ "s'apparente à une propriété de 'modération'"; and 156-4/70, where "modérée" is the comparability of subdivisions.
- **The two axioms:**
  - common refinement (Inf for ≪) is the o-minimal statement that finitely many definable sets admit a common compatible cell decomposition;
  - comparability of subdivisions is the Hauptvermutung (Shiota).
- **The hunch:** the 1986 notion of "modéré" bundles the two, and they separate in models. In topological polyhedra the Inf for ≪ exists (common refinement of two subdivisions after a further subdivision), while comparability of subdivisions of the same figure is the Hauptvermutung, which fails (Milnor 1961).
<!-- /reading:156-5 -->

<!-- reading:156-6 -->
### From the reading of 156-6 (sub-agent; the full reading is readings/156-6.md)

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
<!-- /reading:156-6 -->

<!-- reading:156-7 -->
### From the reading of 156-7 (sub-agent; the full reading is readings/156-7.md)

**H7-1. The "ateliers simpliciaux" of 156-7/15 are the polytopal (lattice) cell structures** (sharpens H9).
- At pol 1 + At simp 1 hold for the face poset of every convex polytope.
- Simplices are the distributive case (SA21-R7-06).
- Grounds: 156-7/14-15; the square.
- Literature: G. M. Ziegler, *Lectures on polytopes*, GTM 152, Springer 1995, ch. 2 (face lattices) (locator to be checked); A. Björner, European J. Combin. 5 (1984) 7-16 (locator to be checked).
- Prediction: his oriented maquettes of dimension ≤ 2 (156-8/6) satisfy At pol 1 + At simp 1 only when every 2-cell is a polygon whose face poset is a lattice. A regular CW complex with two edges between the same two vertices (a digon) breaks At pol 1.

**H7-2. Supports are an orthogonality lattice, not a locale** (refutes the distributivity hoped for in H3; sharpens H3 and H6).
- Given At L2, Σ is the complete ortholattice of the disjointness graph (𝓛, ∥).
- It is canonically P(𝓛) iff ∥ is "≠" (SA21-R7-20).
- It is not orthomodular in general (his path, scan 99: the hexagon O₆), still less distributive (his ficelle, scan 84; MO₂).
- So the ateliers are not locales in general. The |∘|-magasins of scan 110 are orthogonality spaces (𝓛, |∘|) carrying an order. That is the frame of quantum logic, not of pointless topology.
- Literature: G. Birkhoff, *Lattice theory*, 3rd ed., AMS 1967, ch. V §7 (polarities) (locator to be checked); G. Kalmbach, *Orthomodular lattices*, Academic Press 1983, ch. 1 (locator to be checked).

**H7-3. The Théorème-Scholie is a representation of spacious ateliers by an event structure with a refinement order and a conflict graph on its minimal events** (sharpens H1).
- (M, ≤, ≍) of finite type is a prime event structure; ≪ is the extra refinement order.
- The graph Γ, free between Γ₀ and P₂(𝓛), plays the role of conflict on the minimal events.
- Concurrency theory has "action refinement" on event structures. R. van Glabbeek and U. Goltz, "Refinement of actions and equivalence notions for concurrent systems", Acta Informatica 37 (2001) 229-327 (locator to be checked).

**H7-4. The magasin axioms Mag 1-4 (156-7/110-114) hold for the open cells of a regular CW complex with |∘| = "the open cells are disjoint" and ≪ = refinement under subdivision.** Mag 4 (distinct strata of a multistrate are |∘|) is the frontier condition in |∘| form (H7).
- Grounds: 156-7/102-114, against 156-4/2-3.
- To be tested against 156-8/8-21, which is not read here.

**H7-5. Divisibility (At L1) is the axiom that separates his "espaces infiniment divisibles" from the finite T₀ models.** Every other axiom holds on any ordered set with ≪ = ≤ (156-7/54, checked).
- The finite (McCord) models of 156-8/3 sit exactly where At L1 fails.
- His turn to |∘| (scan 109: the common structure "paraît trop restrictive ... par la seule présence de At L1") is the move that admits them (H9).
<!-- /reading:156-7 -->

<!-- reading:156-8 -->
### From the reading of 156-8 (sub-agent; the full reading is readings/156-8.md)

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
<!-- /reading:156-8 -->

<!-- reading:156-9 -->
### From the reading of 156-9 (sub-agent; the full reading is readings/156-9.md)

**H9-1. H10 refined: the July figures are flags of a positional order, and the general statement is about comparability magasins** (sharpens H10, H8-3).
- **Grounds:** 156-9/6-8 and 156-8/106-107: figures are the chains of the positional order <, not of incidence ⊴.
- **The hunch:** the magasins whose |∘| is the comparability relation of an order compatible with ⊴ and ≪° are the "one-dimensional" class. In them figures are flags, and Σ is the polarity lattice of a comparability graph.
- **What it predicts:** orthomodularity of Σ fails exactly when the comparability graph contains an induced path on 4 vertices (O₆ from the fence). Graphs without induced P₄ are the cographs; the hunch is that Σ is orthomodular iff the graph is a cograph.
- **Literature:** D. G. Corneil, H. Lerchs and L. Stewart Burlingham, "Complement reducible graphs", Discrete Appl. Math. 3 (1981) 163-174 (locator to be checked); T. Gallai, "Transitiv orientierbare Graphen", Acta Math. Acad. Sci. Hungar. 18 (1967) 25-66 (locator to be checked).

**H9-2. The 1986 supports are quantum-logic objects, and his "spatios" anticipate the orthogonality spaces of Foulis and Randall** (sharpens H7-2).
- **Grounds:** 156-9/78-80 (spatios = complete ortholattices; disjoncteurs = orthogonality spaces) and 156-9/109-117 (orthomodularity and the axiom of supports).
- **The hunch:** his correspondences of disjoncteurs (scans 61-108) are the morphisms of orthogonality spaces later studied in operational quantum logic.
- **Literature:** J. R. Dacey, *Orthomodular spaces*, PhD thesis, University of Massachusetts 1968; D. J. Foulis and C. H. Randall, "Operational statistics I", J. Math. Phys. 13 (1972) 1667-1675 (locators to be checked).

**H9-3. Tame ateliers should be faithful, and then their supports are Boolean** (his margin, 156-9/4; joins H2 and H8-1).
- **Grounds:** his margin "À vérifier que la bonne notion d'atelier modéré doit bien impliquer qu'il est ... fidèle"; faithful ⇒ Σ Boolean (SA21-R8-25).
- **The hunch:** in an o-minimal model, with strata as definable cells and |∘| as interiors disjoint, the atelier is faithful, because points are definable and disjoint. The cords of 156-7/84 are exactly what o-minimal tameness excludes.

**H12 (sweep 3) refuted:** the table of contents of 156-9/3 belongs to Récoltes et Semailles (SA21-K9-01).
<!-- /reading:156-9 -->

<!-- reading:156-7_061-114 -->
### From the reading of 156-7_061-114 (sub-agent; the full reading is readings/156-7_061-114.md)

**H7b-1. The Théorème of 156-7/94 holds for exactly those figures whose open strata span a Boolean subalgebra, and in the ateliers of his axioms that is a condition on the cords alone** (sharpens H3 and reader B's H7-2).
- Grounds:
  - the counterexample of SA21-R7b-21 uses only foreign lieux (e, w, h, g) that are disjoint from some strata of the figure and not from others;
  - when every lieu disjoint from one open stratum is disjoint from all the others of its figure, the failure pattern O₆ cannot form inside the span.
- A precise form to test: the Théorème holds for F iff no lieu outside omb(F) is disjoint from a proper part of the open strata of F without lying in their support.
- Links: reader C's admissibility = orthomodular law (156-9/117); Kalmbach 1983, ch. 1 (locator to be checked).

**H7b-2. "Stratos" (156-7/61) is the structure of the first reading's Théorème-Scholie with ∥ fixed as "≠"** (sharpens H7-3 and the first reading's §2.1). The quasi-set-theoretic pre-atelier is (M, ≤, ≪) with Prat quas 1-4. That is the event-structure-with-refinement of H1/H7-3, with the conflict graph empty on lieux.
- His later uses of "stratos" (scans 65-83) are the general case, with a disjointness graph.
- The name should replace "Stratop" in the edition and in the register.

**H7b-3. The 26 June turn to |∘| is forced by maquettes, not by the counterexamples** (sharpens H7-5). His stated reason (scan 102) is that on a simplicial maquette every open part X° is empty ("C'est triste mais c'est vrai"). The supports pathologies (84, 99) came before and did not move him. The finite T₀ models (H9) are therefore what shaped Mag 1-4.
<!-- /reading:156-7_061-114 -->

<!-- reading:156-9_rest -->
### From the reading of 156-9_rest (sub-agent; the full reading is readings/156-9_rest.md)

**H9b-1. The orthomodular disjoncteurs are the Dacey graphs, and among comparability graphs the class lies strictly between the cographs and all orders** (refines H9-1, which is refuted as an equivalence).
- **What is proved:** cograph ⇒ orthomodular (SA21-R9b-27). Already on 5 vertices there are non-cographs with Boolean Σ: the order 1 < 2 < 0, 4 < 0, 1 < 3, which contains the fence N, has Σ = 2³. The middle element 2 "repairs" the fence.
- **The hunch:** for an ordered set, Σ (comparability) is orthomodular iff every induced fence N lies under a "repair" of this kind, that is, iff the comparability graph is a Dacey graph in Sumner's sense.
- **Literature:** D. P. Sumner, "Dacey graphs", J. Austral. Math. Soc. 18 (1974) 492-502 (locator to be checked).

**H9b-2. The faithful ateliers are exactly the frame of Boolean supports he hoped for, and the compactologized faithful ateliers are his intended "topologie modérée"** (joins H8-1 and H9-3).
- **Grounds:** 156-9/127 ("peut-être les ateliers fidèles ?"); SA21-R8-25 (faithful ⇒ Σ Boolean); the compactologies of 156-9/34-37; his diagnosis that the cords are "les seuls ennuis".
- **The hunch:** a tame (o-minimal) model, with strata the definable cells, |∘| = interiors disjoint and M_c = bounded cells, is a faithful compactologized atelier. All of his support axioms then hold there.

**H9b-3. His disjoncteurs with correspondences form the category of orthogonality spaces with adjointable relations, and its dagger is his transposition** (sharpens H9-2).
- **Grounds:** 156-9/61-108; Prop 3-4 re-derived (SA21-R9b-15 to -20).
- **Literature:** B. Jacobs, "Orthomodular lattices, Foulis semigroups and dagger kernel categories", Logical Methods in Computer Science 6 (2010); J. Paseka and T. Vetterlein, on categories of orthogonality spaces (locators to be checked). Michel Hua's project also gives Jacobs 2010 and the bonds.
- **What it predicts:** his open question on C and |∘| for Corr(Σ, Σ′) (scans 102-103) has a negative answer in general, and a positive one in the orthomodular (dagger kernel) case.
<!-- /reading:156-9_rest -->

**Round 2, reader C:** H9-1 (the cograph hunch, in the merged block of 156-9) is half refuted. Cograph ⇒ orthomodular is proved; the converse fails on 5 vertices. Its refinement is H9b-1, the Dacey graphs of Sumner (readings/156-9_rest.md).
