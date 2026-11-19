# SA11, Espaces stratifiés part 2 (cotes 121, 153, 154, 155): the study

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

**The brief:** the coordinator's message of 18 Nov, about 22:2x UTC (sweep 3).

## What was read, and how

**Read in full tonight:** cote 154, scans 34-43, the disk model (SA11-12), from the frozen Pro transcription MPL_154_001-045, cleaned to `sweep3/_tools_a6d42bf6/c154a.txt`.

**Not read tonight, so the sweep-2 map (`sweep2/SA11/WHAT_IS_WHERE.md`) stands for them:**
- the rest of cote 154 (SA11-8 to SA11-20), mine.
- cote 121, scans 49-73 (SA11-3, SA11-4). By the split of 18 Nov the tame axioms of cotes 120-121 are mine; I did not reach them.
- cotes 153 and 155 (SA11-5, SA11-6). By the same split, ae4ae3dc17acaa440 reads them (SA20-16, SA20-17).

**This is the thinnest of my three studies.** SA21 had 156-4 read in full, and SA10 had 151/32-75.

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
