# Cote 154, scans 1-33 and 44-176: integration (SA11, horizontal sweep 3)

**Who:** Claude Opus 5.5 at effort max, reader for a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max), horizontal sweep 3, 19 Nov 2026.

## STUDY

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

## HUNCHES

**H154-1 (sharpens H1). χ(𝒳) = 1 − n for every non-trivial arrangement of n pseudolines.**
- The hunch: Grothendieck's surface is, up to homotopy, the rank-3 extension space modulo reorientation, blown up at the n supercritical points.
- Grounds:
  - the straight case, proved by the count s₀ = 2E (SA11-R154-18);
  - the Sturmfels-Ziegler theorem that rank-3 extension spaces are homotopy spheres.
- Against:
  - the ν-cubes of generizations (154/154);
  - the multiple endpoints of a semi-stable position (154/151).
  Both are absent from the straight case, and 𝒳 keeps only part of each cube.
- Test: a pseudoline arrangement with a non-straight relative position through three vertices, for example a simple arrangement of 6 pseudolines with v₁₂, v₃₄, v₅₆ on one pseudoline; count s₀ and s₂ there.
- Relation to H1: confirms it in the realizable case, in refined form (blow-up), and leaves the general case open.

**H154-2. 𝒳 is a "cyclic section" of the cubical extension space.**
- The hunch: at a position through ν vertices, the cyclic order of the 2ν generization points on D̃ selects 2ν of the 2^ν stable generizations, those met by turning around the critical position. 𝒳 would then be the subcomplex of cyclically coherent cells, as the coherent (realizable) cells form a subcomplex in the generalized Baues problem.
- Literature: L. J. Billera, M. M. Kapranov, B. Sturmfels, "Cellular strings on polytopes", Proc. Amer. Math. Soc. 122 (1994), 549-555; the Bohne-Dress theorem, via Sturmfels-Ziegler 1993 (locators to be checked).

**H154-3. The image of the polygon invariant is cut out by local conditions** (his question 2°, 154/020).
- The conditions: the 2n weight rule, the reversed clusters at the vertices on D, and the existence of three triangles (Levi).
- Grounds:
  - SA11-R154-08 shows the polygon is the contraction refined by local orders;
  - Las Vergnas's characterization of single-element extensions is by conditions on rank-2 contractions, which are local.

## PACKAGES

**P154-1. The topology of the surface of relative positions (Esquisse §8) for pseudoline arrangements** (H1, H154-1, H154-2).
- **Question.**
  - Is 𝒳 well defined (all vertices of order 4, gluings consistent) when relative positions pass through three or more vertices, or when semi-stable positions have more than two critical endpoints?
  - Is χ(𝒳) = 1 − n?
  - What is the homotopy relation of 𝒳 to the extension space blown up at the supercritical points?
- **Why it matters.**
  - 154/120 is the one place where the folder computes the topology of the surface it builds, and the straight case now has its value.
  - A positive answer places Esquisse §8 inside the theory of extension spaces. A negative one shows that his surface records more than the extension poset.
- **What it rests on.** 154/012-033, 044-045, 077-079, 120, 151-154 (read), and the disk model 034-043.
- **Strongest known reduction.**
  - The straight case, χ = 1 − n (SA11-R154-18).
  - Sturmfels-Ziegler, Discrete Comput. Geom. 10 (1993) 23-45 (rank-3 extension spaces are homotopy spheres; locator to be checked).
- **Material.**
  - The four MPL_154 packages and K154-01/02 with the scans of cote 154.
  - This reading and a6d42bf6's STUDY §1.
  - Sturmfels-Ziegler 1993; BLSWZ, *Oriented matroids*, ch. 6-7.
  - Billera-Kapranov-Sturmfels 1994.
  - Goodman-Pollack on allowable sequences.

**P154-2. The image of the polygon invariant and the reconstruction of Γ(Σ)** (H154-3).
- **Question.**
  - Which cyclic orders on Ĩ, with the cluster twist, come from relative positions?
  - Can the weighted, cellularly embedded graph Γ(Σ) be rebuilt from them, as his question 2° on 154/020 asks?
- **Why it matters.** It turns his invariant into a combinatorial model of the surface.
- **What it rests on.** 154/017-025 (read) and SA11-R154-07, 08.
- **Strongest known reduction.** Injectivity (SA11-R154-08) and Las Vergnas's localizations.
- **Material.**
  - BLSWZ §7.1.
  - Michel Hua's project, `lean/Grothendieck/Folder154.lean` (`problem17_holds`), credited.
  - The packages of cote 154.
