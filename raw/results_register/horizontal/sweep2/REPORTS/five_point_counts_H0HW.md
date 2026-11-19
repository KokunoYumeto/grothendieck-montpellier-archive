# The five-point counts against M_{0,5} (object H0HW, "the five-point problem")

By the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), horizontal sweep 2, part 2, 18 Nov 2026. I read the page on the scan image itself (cote 148, PDF page 33, at 70, 300 and 600 dpi). The scan number is the PDF page: page 33 carries the table that the transcription places at `\scanpage{33}`.

## Where it is
| what | cote and scans | notes and transcription |
|---|---|---|
| the five-point diagram: objects, arrows, work programme (SA31-5, SA31-Q1) | 148/029-034 | Pro MPL_148_029-072. Notes: `grothendieck_archive_transcription_20261110/returns/MPL_148_029-072_unzipped/MPL_148_029-072_notes.md` (Q1a, R01-R04, R09). Transcription lines 64-504 of `MPL_148_029-072_transcription.tex` |
| the boundary of the moduli of five points (SA30-6) | 147/066-068; 146/058-090 | MPL_147_048-137 and MPL_146_001-099, notes N066-01..N067-02 and R072 |
| the dodecahedral groupoid: 120 frames, 62 cells (SA30-7) | 146/071-097 | MPL_146_001-099 |
| the order-five relation: not written before 148/028 (SA29-Q1) | 144, 145, 148/001-028 | MPL_144_*, MPL_145 |
| canonical (0,4) configurations, 14 = 3×4 + 2 (SA29-18) | 148/018-028 | MPL_144_168-184+148_001-028 |
| a five-point coherence test in the cutting coordinates (SA22-7; joined at ae4ae3dc17acaa440's word) | 67/063-081 | MPL_67_053-101 |

## What his pages contain
- **148/031, the objects.** Nine families of objects under G = Aut⁺ (order 120). Each family has 120/i members, i the order of its stabilizer. The rows are 12, 20, 30; 60, 60, 120; 60, 120, 60. The rows add to 62 + 240 + 240 = 542.
- **148/034, the special configurations.**
  - μ₅ with group D₅;
  - μ₄ ∪ {∞} with group ℤ/4;
  - μ₃ ∪ {0, ∞} with group D₃.
- **148/033, the arrows.** There are fourteen named arrow families in three blocks:
  - block 180: 60 + 120;
  - block 420: 60 + 120 + 60 + 60 + 120;
  - block 1020: 120 + 120 + 120 + 120 + 3×120 + 120 + 60.

  The total, 1620, is written as 5×60 + 11×120.
- **The work programme on 148/033.**
  1. "déterminer un syst. fondamental de relations entre les 1620 flèches du diagramme", with the margin: write every arrow as a composite of arrows "provenant de la dimension relative ≤ 1";
  2. eliminate the vertices of level 0;
  3. eliminate the "tétraédrales" pieces II₁.
- **147/068, the boundary.** His Proposition: the divisor at infinity of the moduli of five points over Spec ℤ is a split stable curve with ten rational components (the 2-subsets) and fifteen nodes (the partitions of type (2,2,1)).

## What the ink shows on 148/033 (decided on the scan)
1. **The 1020 block.**
   - The fifth row reads "3×120 =" followed by "2×60 = 2×60", struck through, and above it "3×40 = 3×40". The transcription has this right.
   - The block total "1020" is written next to a struck "900".
2. **The total.** It reads: struck "1500", then "= 5×60 + 11×120", with "11" written over an earlier digit, and "1620" below.
3. **The programme line.** It reads: "… entre les 1620 flèches du diagramme, se partageant [struck word] 14 [struck word, read 'orbites' by the transcription] sous G_K (aux 542 …". He struck the word after "14". An interlinear word above it is not legible at 600 dpi.

## Checks
1. **The first row of objects is the set of special configurations.**
   - 5-point configurations on P¹ with an automorphism group of order at least 3: the stabilizer of a 5-set in PGL₂(ℂ) is a finite group acting faithfully on the five points.
   - A₄, S₄ and A₅ have no invariant 5-sets. Their orbits have sizes 4, 6 and 12; 6, 8, 12 and 24; 12, 20, 30 and 60. So the group is cyclic or dihedral.
   - An element of order 3, 4 or 5 forces μ₃ ∪ {0, ∞} (group D₃), μ₄ ∪ {∞} (group C₄) or μ₅ (group D₅).
   - Orbit-stabilizer under S₅ then gives 20, 30 and 12 labelled configurations. These are his i = 6, 4 and 10.
   - **Agrees** with 031 and 034. LM4_SUCCESSOR:E.37 (proved in the research runs) gives the same nine types with these stabilizers: I₁₀, I₆, I₄, II₂, II′₂, II₁, III₂, III₁, III′₂.
2. **The arithmetic and the history of corrections.**
   - 62 + 240 + 240 = 542.
   - 60 + 120 = 180; 60 + 120 + 60 + 60 + 120 = 420; 120 + 120 + 120 + 120 + 360 + 120 + 60 = 1020; 180 + 420 + 1020 = 1620 = 5×60 + 11×120.
   - Both corrections are +120. The block went from 900 to 1020 and the total from 1500 (= 5×60 + 10×120) to 1620 (= 5×60 + 11×120): the family γ_r^{1′} grew from two orbits of 120 to three.
   - **Agrees.**
3. **Fourteen families, sixteen orbits.**
   - The fourteen rows are fourteen families, but the family of 360 is three free orbits. So the arrows form 16 S₅-orbits: 5 of 60 and 11 of 120.
   - He struck the word after "14" on the page, and his own total, 5×60 + 11×120, counts 16 orbits. So **the page agrees with the refutation** LM4_SUCCESSOR:E.38, which refuted reading the fourteen families as fourteen orbits.
   - This is a correction to the Pro note R02, which counts "fourteen stated arrow orbits", and to Q1a.
4. **The factorization "3×40 = 3×40" is inconsistent with the rest of the page.**
   - For the other rows, the two products are (arrows per source × sources) and (arrows per target × targets), over the object families of 031.
   - No object family has 40 members (E.37). The run's reading of this family (E.38: from III₁ to II₁, three free orbits) gives 360 = 3×120 = 3×120.
   - **Decision:** the ink is as transcribed. The factorization is his slip or an unexplained intermediate count. The row total 3×120 and every total above are unaffected.
   - One way 40 could arise: the twenty configurations μ₃ ∪ {0, ∞} with one of their two orientations have stabilizer C₃ and orbit 40. That is my inference, not on the page.
5. **The boundary of M̄_{0,5}.**
   - There are 10 = C(5,2) components and 15 = 5·3 nodes, one for each pair of disjoint 2-subsets.
   - The dual graph is the Kneser graph K(5,2), which is the Petersen graph. Its first Betti number is 15 − 10 + 1 = 6, the arithmetic genus of a nodal curve with rational components.
   - **Agrees** with 147/068 and the notes' identification.
6. **How many relations the programme needs.**
   - The diagram is read as the fundamental groupoid of M_{0,5} at these 542 base points: EXIT_TOWER:B.25 (proved) realizes all 542 objects and 1620 arrows. M_{0,5} has Poincaré polynomial (1+2t)(1+3t), so b₁ = 5 and b₂ = 6.
   - Take a presentation complex P with 542 vertices, 1620 edges and R relators. Then 542 − 1620 + R = 1 − 5 + b₂(P), with b₂(P) ≥ 6 (Hopf). So **R ≥ 1080**, with equality when P is aspherical; M_{0,5} is a K(π,1).
   - Counted with stabilizers, the relators weigh 9 free S₅-orbits: 1/60 − 542/120 + 1620/120 = 9.
   - **Agrees** with EXIT_TOWER:B.15 (proved: 1080 defining relators, complete) and B.26 (proved: the counts are minimal). This is my recomputation of their bound by Euler characteristic.

## What depends on what
- SA31-Q1 (the programme) rests on SA31-5 (the diagram), which rests on SA30-6 and SA30-7 (the boundary of M_{0,5} and the dodecahedral cells).
- In the research runs, EXIT_TOWER:B.25 realizes the diagram. B.15 completes it with 1080 relators, and B.26 shows they are minimal. STRATA:F.17 (proved) gives the Lego presentation of the Teichmüller groupoid.
- The margin's request, arrows from relative dimension ≤ 1, is the Lego principle that F.17 proves.
- LM4_SUCCESSOR:E.32 (refuted) is his inference on 148/035 about antiholomorphic automorphisms of order 4. It sits on the next sheet, outside these counts.

## Corrections and refinements
- **R02 and Q1a of the Pro notes.** "14 stated arrow orbits" should read "14 arrow families, 16 orbits". He struck "orbites" himself.
- **R02.** "the evaluations are 360 and 120, with difference 240" is right about the factorization, but the totals use 360 throughout. The open point is only the "3×40" factorization (his slip or an unexplained count), not the total.
- **H0HW holds SA22-7** (cote 67, the cutting coordinates' five-point coherence test) at ae4ae3dc17acaa440's word. Part 3 should check that it is the same problem: a coherence test on five points, not the presentation of the five-point groupoid.

## Check events (GLOBAL/CHECK_EVENTS_broad.tsv)
Five events:
- the special configurations, by computation;
- the arithmetic of 031 and 033, recomputed;
- 148/033 read on the scan image;
- the boundary of M̄_{0,5}, by computation;
- the relator bound, agreeing with EXIT_TOWER:B.15 and B.26.
