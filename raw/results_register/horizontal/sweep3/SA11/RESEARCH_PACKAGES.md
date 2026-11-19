# SA11: research packages, in concept

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

These are concepts only. No prompt is written tonight.

## P1. The surface of relative positions (Esquisse §8) as an extension space (H1, H2)

**The question:**
- Is his cellular surface of relative positions of an added pseudoline (cote 154) the extension space of the rank-3 oriented matroid of Σ, or its antipodal quotient?
- Do his face counts and his genus formula (154/120) agree with its known homotopy type?
- Is his conjecture true that the polygon invariant determines the deployment (SA11-C1, 154/20-44)?

**Why it matters:**
- Cote 154 is the worked-out form of Esquisse §8.
- An identification would place it in a known theory and decide its open claims.
- It is the one place in the archive where his tame topology meets explicit combinatorics.

**What it rests on:**
- 154/34-43 (read; SA11-12);
- 154/1-33 and 44-176 (SA11-8 to SA11-20, not read tonight);
- the Esquisse §8 (cote 119).

**Strongest known reduction:**
- the disk model and its sufficiency (154/35; SA11-C3-01 to 03);
- the rank-3 extension-space theorem (Sturmfels-Ziegler 1993, to be checked).

**Material:**
- the four MPL_154 packages and K154-01/02 `.tex`, with the scans of cote 154;
- Sturmfels-Ziegler 1993;
- *Oriented matroids*, ch. 6-7;
- the sweep-2 notes of SA11-8.

## P2. With SA21 P5: the 1986 pseudo-discs and the chord systems

See `sweep3/SA21/RESEARCH_PACKAGES.md`, P5. This side adds the definition of a chord system (154/35) and the sufficiency claim.

## From the sub-agent readings

<!-- reading:154_001-176 -->
### From the reading of 154_001-176 (sub-agent; the full reading is readings/154_001-176.md)

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
<!-- /reading:154_001-176 -->

<!-- reading:121_049-073_153_155 -->
### From the reading of 121_049-073_153_155 (sub-agent; the full reading is readings/121_049-073_153_155.md)

Registered in SA20 (`sweep3/SA20/readings/121_049-073_153_155_PACKAGES.md`): R20-121_049-073_153_155-1 (a reconstruction
theorem for the compact-model axioms; now joined to P-AX1 of the axiom comparison), -2 (the canonical partition), -51
(analysers against plethories), -52 (155 against Deligne 1990 and the bialgebroid literature).
<!-- /reading:121_049-073_153_155 -->
