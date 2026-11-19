# SA11, Espaces stratifiés part 2 (cotes 121, 153, 154, 155): the study

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

**The brief:** the coordinator's message of 18 Nov, about 22:2x UTC (sweep 3).

## What was read, and how

**Read in full tonight:** cote 154, scans 34-43, the disk model (SA11-12), from the frozen Pro transcription MPL_154_001-045, cleaned to `sweep3/_tools_a6d42bf6/c154a.txt`.

**Not read tonight, so the sweep-2 map (`sweep2/SA11/WHAT_IS_WHERE.md`) stands for them:**
- the rest of cote 154 (SA11-8 to SA11-20), mine.
- cote 121, scans 49-73 (SA11-3, SA11-4). By the split of 18 Nov the tame axioms of cotes 120-121 are mine; I did not reach them.
- cotes 153 and 155 (SA11-5, SA11-6). By the same split, ae4ae3dc17acaa440 reads them (SA20-16, SA20-17).

**Round 2, 19 Nov 2026:**
- The rest of cote 154 (scans 1-33 and 44-176) was read page by page by the reader a1ee9ba0e8006bed4 (Claude Opus 5.5 at effort max): readings/154_001-176.md, 23 check events, 8 corrections.
- Cote 121, scans 1-48, is read for SA20 by a9e0641820ca2be57 (Claude Opus 5.5 at effort max, launched by ae4ae3dc17acaa440): sweep3/SA20/readings/121_001-048.md.
- aff4deb18a6ec3192 (Claude Opus 5.5 at effort max), the reader of 121/49-73, wrote the comparison of the axiom systems of cotes 120, 121 and 156 (sweep3/SA10/readings/axioms_120_121_156.md) and the SA11 integration of its 121/49-73 reading (readings/121_049-073_153_155*).
- Its main findings:
  - cote 120 is the repaired copy of the 121 drafts;
  - the 1986 figure of 156-4/2-3 is 121/052 condition by condition;
  - "contrée modérée" means common subdivisions, which fail in plain topology and hold o-minimally (Cor 2 of 121/016). It is not the Hauptvermutung.

## 0. Cote 154 after the reading (19 Nov 2026)

- **His injectivity (154/019) is true.** The deployed polygon of a relative position, read literally, determines the position, through Las Vergnas's characterization of single-element extensions.
  - Michel Hua's project states the oriented-matroid form and checks it in part in Lean.
  - The translation from his polygon to that form is the reader's.
- **154/018 is refined.** The compatibility of the polygon with the antipodies holds only for positions through no vertex. Through a vertex, each cluster of crossings is reversed (SA11-K154-01).
- **The genus formula on 154/120 is right, and H1 needs refining.**
  - When every relative position is a straight line, χ = 1 − n and his g = n. This was checked in full for n = 3 and n = 4.
  - So the surface is the rank-3 extension space blown up at the n lines of Σ, not the extension space itself (H154-1).
  - For pseudolines the general value is open: positions through three or more vertices give cubes of dimension three or more (154/154).
- **Open:**
  - a second pass over the unsure marks;
  - the 546 places where the Pro and Codex witnesses of 154/46-76 differ;
  - three readings to be checked on the scan, and one word on 154/094.


## 1. The disk model of a relative position (154/34-43)

**The setting:**
- Σ = (X, Σ) is an arrangement of pseudolines in the projective plane X, and L is a relative position: an added pseudoline, not trivial.
- A narrow Möbius band β_L around L has boundary L̃, the double cover of L ("rev. des vis").
- Its complement is a disc Δ_L.
- Each D_i ∈ Σ meets L̃ in two points and traces a chord d_i on Δ_L.
- All of this checks: the complement of an open Möbius band in the projective plane is a disc, and D_i meets L once, transversally (SA11-C3-01).

**A "système de cordes" (154/35):**
- (a) Two chords meet in at most one point, interior to Δ, where they cross.
- (b) The relation "i = j or d_i ∩ d_j = ∅" ("parallélisme") is an equivalence relation. A class of ν ≥ 2 chords has its 2ν ends in two packets S′, S″ of ν consecutive ends.

**Checks:**
- (b) holds for chord systems that come from a relative position (SA11-C3-02):
  - two chords are disjoint in Δ exactly when the two pseudolines meet on L;
  - transitivity holds because D_j meets L only once.
- **His claim of sufficiency:** "Ces conditions combinatoires nécessaires … est aussi suffisante", that is, every chord system with (a) and (b) is that of a relative position for a suitable Σ. I checked it by a sketch, not written out in full (SA11-C3-03):
  - By (b), chords of different classes cross. Pairwise crossing chords have their ends in antipodal cyclic order, so the antipodal structure on the boundary is forced.
  - Contract each packet to a point, then glue the boundary antipodally. The result is the projective plane, with the chords closed up to pseudolines meeting pairwise once and the boundary becoming L.
- Choosing one chord per class gives a strict chord system, totally crossing. That is immediate.

**Generization and specialization arcs (154/35-38):**
- **Generization arcs.** These are the two arcs cut off by the packets of a class. Modulo the antipodal map they correspond to the vertices of Σ on L. That is immediate from the construction.
- **Specialization arcs.** These are the bases of the "specialization triangles": sets σ of boundary vertices whose chords meet in one vertex t of Σ, with the triangles (t, s, s′).
- **Exceptional specialization arcs.** These correspond to corridors. L has two of them exactly when it is the bisector of a corridor (154/37).
- **Inertia arcs.** These are the remaining arcs of L̃. In the cases without exceptional arcs, inertia arcs alternate with transition arcs.
- 154/38 introduces "shrunk" exceptional arcs so that the transition arcs are disjoint in every case.
- Generization "crosses the strands" above the arc. In X it is an anti-sweep that pulls the vertex s off.
- These statements are his. I did not check them.

**Gluing the discs (154/38-40):**
- The discs Δ_L and Δ_{L′} are glued along corresponding generization and specialization arcs.
- He first takes the evident identification. He then rejects it ("il me semble que ce n'est pas le bon") for the one fixing s and t, the symmetry about the axis (s, t). Its transport isomorphism is "l'opposé de l'isom tautologique".
- With this identification all faces have order 4. Their sides are one of specialization type, one of generization type and two mixed. The faces correspond to the pairs (L, a), with a an inertia arc of specialization type.

**What is left (154/40-43):**
- The construction leaves out the supercritical relative positions.
- Without them one gets a compact surface with boundary. The holes are to be closed by the discs Δ_D for D ∈ Σ, which carry n−1 chords and a polygon of order 2(n−1).
- The generization arcs on Δ_D overlap ("empiètent les uns sur les autres"). His remedy, begun on 154/43, is to multiply each D into as many copies as it has vertices.

## 2. What it connects to

- **SA21, 156-4/32 and 45.** The "pseudo-disques" with "cordes" and their "nœuds" of 1986 are discs with chords crossing at most once, the object of 154/34-35. That they are the same object is my reading (SA21 H5). If so, the arrangements of cote 154 are a test case of the 1986 contrée axioms.
- **SA11-8, Esquisse §8.** The surface built here is the "surface combinatoire des positions relatives" of an added pseudoline. The notes of sweep 2 compare it with oriented matroids. My hunch (H1) is that it is the rank-3 extension space, which is homotopy equivalent to a sphere.
- **SA11-10 (his conjecture SA11-C1, 154/20-44)** is that the polygon invariant determines the deployment. It rests on these discs.

## From the sub-agent readings

<!-- reading:154_001-176 -->
### From the reading of 154_001-176 (sub-agent; the full reading is readings/154_001-176.md)

**What was read, and how.**
- Cote 154, scans 1-33 and 44-176, in full, from the frozen Pro transcriptions (GPT-6 Astra, ChatGPT Pro mode).
- Scans 46-76 collated word by word with the Codex witnesses K154-01/02 (546 differing runs).
- The scans looked at where a reading matters: 032, 047, 094, 120, 142, all 30 illegible places of 127-176.
- Scans 34-43 (the disk model) are a6d42bf6's reading and are not redone.
- Full reading: `154_001-176.md`.

**The order of writing**, which is not the scan order:
1. the axioms of the deployment (𝒳, K, L), 044-045, end of November 1983;
2. the structure of the set of relative positions PR(Σ) with its polygons, weights and transport, 012-033, 23-25 Dec 1983;
3. the disk model, 034-043;
4. the corrections of early January 1984, 046-095: the structural map, the signs, the monodromy, four gluings, "une erreur monumentale";
5. the five variants 𝒳_0 to 𝒳_3, 002-010, 18 Jan 1984;
6. undated sheets on fuseaux, flags and counts, 127-176.

**Findings.**
1. **His expected injectivity (019) holds.** The deployed polygon P̂(D) of a relative position is the contraction (M ∪ D)/D of the rank-3 oriented matroid, refined by the order of the crossings at the vertices on D. From it and Σ one reads the cocircuit signature, and by Las Vergnas's theorem the signature determines D (SA11-R154-08).
   - Michel Hua's project states the chirotope form and checks it partly in Lean.
   - The translation from the polygon to the contraction is ours.
2. **His claim that P̂(D) is compatible with the antipodies (018) fails for D through a vertex of Σ.** There the label antipodism is the half-turn followed by reversing each cluster of crossings. It holds for stable D (SA11-R154-07, SA11-K154-01).
3. **The genus formula of 120 is right.** χ(𝒳) = s₂ − s₀ (vertices of order 4), and his g is 1 − χ (SA11-R154-17).
   - When all relative positions are straight, the positions are the cells of the dual arrangement in X^∨ (his own 077-078). Then s₀ = 2E, so χ(𝒳) = 1 − n and g = n. Checked in full for n = 3 (s₂ = 10, s₀ = 12) and n = 4 (s₂ = 33, s₀ = 36) (SA11-R154-18).
   - So 𝒳 is not the extension space but the projectivized extension space blown up at the n supercritical points. Being non-orientable (064), it is a sum of n + 1 projective planes.
   - This refines H1.
4. **For pseudolines the extension poset is not two-dimensional.** A position through ν vertices has a ν-cube of generizations (154/154; SA11-R154-20). A semi-stable position can have more than two critical endpoints, which is his own difficulty on 151.
   - 𝒳 keeps only 2ν squares of each cube.
   - So the general value of χ(𝒳) is open (H154-1, package P154-1).
5. **Checked:**
   - the monodromy translation by n − 1 around each D_i (056, 064), whose order explains the parity split of 003;
   - χ_c is trivial, so χ_𝒳 = χ_X (064);
   - the flag identities and ρ_som ρ_f = σ₂σ₀ (032);
   - the index-2 subgroups of D_{2n} (086);
   - five cyclically commuting involutions (095);
   - the weight rules (017-022);
   - ν + ν₀ = n (019);
   - the count of critical positions 3·C(n,4) (142).
   23 check events in all.
6. **Readings:**
   - 032 decided (SA11-C2): the frozen reading stands, against Michel Hua's project;
   - 120 has "+";
   - 142 has "(n−2)";
   - on 047 the ink confirms an index that differs by one from 056/073, an inconsistency of his;
   - the 30 illegible places of 127-176: 28 printer show-through, one dash (153), one deleted phrase (171);
   - 8 corrections in all.

**Ready for an edition?** No: the four Pro packages carry 2,075 unsure marks, and the collation differences of 46-76 are not decided. Not ready for translation by GPT-6.2 Sol at reasoning effort max either.

**Links.**
- SA11-10 rests on SA11-12, and SA11-8 on SA11-11 and SA11-13.
- The 1986 pseudo-discs of SA21 (H5) are the chord systems of 034-035.
- The extension-space comparison is literature: Las Vergnas 1978; Sturmfels-Ziegler 1993; Björner-Las Vergnas-Sturmfels-White-Ziegler ch. 7 (locators to be checked).
<!-- /reading:154_001-176 -->

<!-- reading:121_049-073_153_155 -->
### From the reading of 121_049-073_153_155 (sub-agent; the full reading is readings/121_049-073_153_155.md)

**Cote 121 scans 49-73, cotes 153 and 155 (SA11-3 to SA11-6), read for SA20 and carried into SA11.** Claude Opus 5.5 at
effort max (aff4deb18a6ec3192) read the whole Pro package MPL_121_049-073+153+155 on 18 Nov 2026 for ae4ae3dc17acaa440 (SA20-15,
-16, -17). The full working, the 39 check events and the 15 corrections are in `sweep3/SA20/readings/121_049-073_153_155*`;
they are not duplicated here. The comparison of the axiom systems of 120, 121 and 156 is in
`sweep3/SA10/readings/axioms_120_121_156*`.

**SA11-3, the tame axiomatics of 121/49-73.** Five drafts:
- admissible partitions and their closed leaves (049-052);
- a moderate category over compact spaces, with its reconstruction from families of compact subsets of cubes (054-058);
- the categorical form and gluing under injectivity and zero loci (059-063);
- a list with triangulation (065), and an attaching construction by products (066-068);
- the C_* draft of models and C_*-spaces (070-073).

Proved and re-derived:
- the incidence order and the closed-leaf presentation (050-052);
- conservativity with faithfulness, and the effective-epimorphism lemma (054);
- local compactness of the special ind-objects (055);
- the reconstruction (057-059);
- the gluing proof of 062, which is complete;
- the attaching criterion and the product trick (066-068).

Wrong, with corrections:
- 049: the first open stage must be X − ∪ Fr(T_α), which is what his 121/015 uses;
- 050 and 052: decided on the images (X^{i−1} for X^{i+1}; no closure bar), his slips;
- 056: the field and vector-space claim needs the product axiom;
- 057: composition of graphs needs the image axiom;
- 058: the conditions M′4 need I = [−1, 1];
- 063, 065: two typing slips;
- 070: intersections do not follow from a)-d) (countermodels). Cote 120 repairs this with M2.

Open: the induction of 049 (proved on 015-017 for finitely many members of a Boolean family); the pushout question of 073
(proved in cote 120 under M6-M7); F3 of 063.

**SA11-4, the comparison with o-minimal and related theories.** None of the five drafts is o-minimal as written. Only the
triangulation axiom of 065 forces finiteness in dimension one, and cote 120 has none. 121/004-010 (the one-space Boolean
axioms, read for SA20 by a9e0641820ca2be57) has complements and finitely many components, but on one space. The details are
in the axiom comparison: what corresponds, what each system allows and excludes, and the hunches H2, H7, H9-3 of SA21 tested.

**SA11-5, the analysers (153, from April 1982).** A commutative pseudo-ring with a composition, right composition a ring
homomorphism, optional finite coaddition and comultiplication. Examples: maps A → A, polynomials, the binomial analyser
Int(Z), λ-rings, divided powers (not unital).
- Checked by computation: the binomial structure constants are integral (product, composition, coaddition,
  comultiplication).
- Refined: "OK si Ω libre" (004) needs the domain hypothesis he struck out.
- Today: a one-sided form of the plethories of Tall-Wraith and Borger-Wieland.

**SA11-6, a tensor category with a fibre functor over k′/k (155, from mid-1984).** A reconstruction claim: an abelian
k-linear ⊗-category with a faithful ⊗-functor to Modf(k′) is equivalent to an augmented commutative k′-algebra U whose dual
pro-ring A has a coproduct into the idealizer quotient J̃/J.
- New in this reading: J̃/J is Takeuchi's product A ×_{k′} A, so A is a bialgebroid over k′.
- The example Modf(k), the exactness test (étale against inseparable k′), End_A(U) ≅ A^o and F′(D(M)) = M^∨ are re-derived.
- His question (do rigidity and End(1) = k suffice?) was answered by Deligne (1990).

**Versos (for the user's decision).** 153: IBM printout of 19 April 1982. 155: a publishing-contract page and university
papers of June-October 1984, one of them a commission's minutes with candidates' names and votes.
<!-- /reading:121_049-073_153_155 -->
