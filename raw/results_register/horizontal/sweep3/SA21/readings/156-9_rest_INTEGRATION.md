## STUDY

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

## HUNCHES

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

## PACKAGES

**P9b-1. Orthomodularity of the supports of ordered sets and of magasins.**
- **The question:**
  - Characterize the ordered sets L whose comparability disjoncteur has an orthomodular, respectively Boolean, Σ (H9b-1). Find the exact "repair" condition and prove it.
  - For the magasins of ordered sets (with segments), where Axiome supp 1 holds, decide whether the whole Σ_M is orthomodular.
  - Reconstruct and check his 10-element counterexample (156-9/113).
  - Decide the transitivity of ≪°_comm (156-9/123).
- **Why it matters:** these are his open questions of 156-9/111 ("avoir le cœur net ... quand Σ est défini via un ens. ordonné") and 156-9/123. The answer decides where the "cordes" pathologies live.
- **What it rests on:** 156-9/109-123; 156-8/90-127; `156-9_rest_checks.py` (graphs on at most 6 vertices; magasins of orders on at most 5 elements); SA21-R9b-27, -28.
- **Strongest known reduction:**
  - cograph ⇒ orthomodular (proved);
  - O₆ for the fence (not orthomodular);
  - 2³ for a 5-element order with an N (Boolean);
  - Axiome supp 1 in all magasins of orders on at most 5 elements (computed).
- **Material:**
  - the 156-9 .tex with scans 109-123 and the drawings of 112-113;
  - the two check scripts of this folder;
  - Sumner 1974; Kalmbach 1983 (locators to be checked).

**P9b-2. Morphisms, excision and the category of ateliers (CF IX bis).**
- **The question:**
  - Prove or refute that the provisional homomorphisms of 156-9/134 induce correspondences of spatios; decide Σ_{A′} ↪ Σ_A for the four sub-ateliers of 156-9/130-131.
  - Construct the excision A → A/N for a ≪°-closed N, or show it does not exist. He calls it "un tantinet délicate". Start with set-theoretic ateliers and maquettes, as he proposes.
- **Why it matters:** these morphisms are what the forms need in order to be glued and mapped, and the last open construction of the 1986 series.
- **What it rests on:** 156-9/130-139; 156-8/36-38 and 55-60.
- **Strongest known reduction:**
  - Ker f is ≪°-closed;
  - for maquettes A/N = A ∖ N;
  - the transposition theory of Prop 3-4 (re-derived).
- **Material:** the 156-9 and 156-8 .tex with scans 130-140 and 55-60; Jacobs 2010 (locator to be checked).
