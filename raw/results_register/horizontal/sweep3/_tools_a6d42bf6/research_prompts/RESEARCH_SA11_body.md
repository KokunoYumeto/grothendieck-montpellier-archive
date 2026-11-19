# RESEARCH_SA11: the combinatorial surface of the relative positions of a pseudoline (cote 154, Esquisse §8)

**To be settled:** the topology and the combinatorics of the surface 𝒳 that he builds from the relative positions of a pseudoline added to an arrangement Σ of n pseudolines in the projective plane, against oriented-matroid theory. A.1 is the main question.

His axiomatics of tame spaces (cotes 120 and 121) and his notes on cotes 153 and 155 are asked in a separate prompt, RESEARCH_SA20. They are not part of this one.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA11`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA11_study.zip`: our study of cote 154 and its topic.**
  - `study/STUDY.md`, with the disk model of 154/34-43 read in full.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`:
    - the full reading of cote 154, scans 1-33 and 44-176, with 23 check events and 8 corrections;
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the items SA11-1 to SA11-20.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in the CHECK_EVENTS tables and nowhere else.
- **`RESEARCH_SA11_transcriptions.zip`: the AI transcriptions (LaTeX) of cote 154, with their notes and doubt tables.**
  - Cote 154 was transcribed by GPT-6 Astra (ChatGPT Pro mode).
  - The Codex witnesses K154-01/02 for 154/46-76 are by GPT-6 Astra at reasoning effort max in Codex web.
  - `\scanpage{N}` marks scan N of the cote's PDF. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA11_broad.zip`:** the studies of the two neighbouring topics of the cluster: SA10, the stratified spaces of cotes 150-151, and SA21, the axiomatics of forms of cote 156.
- Fetch the literature yourself. It is listed under "Sources" below.

## Where this comes from

**Cote 154 (Nov 1983 - Jan 1984): the surface of relative positions.** This is the worked-out form of §8 of the Esquisse d'un programme (1984).
- **The objects.** For an arrangement Σ of n pseudolines in the projective plane X, he takes the set PR(Σ) of relative positions D of an added pseudoline. Each comes with its polygon, its weights and its transport. He glues the discs Δ_D of the "disk model" along transition arcs into a cellular surface 𝒳, with faces of order 4.
- **The order of writing:**
  1. the axioms of the deployment (𝒳, K, L) (154/44-45);
  2. the polygons (154/12-33);
  3. the disk model (154/34-43);
  4. the corrections of January 1984 (154/46-95);
  5. the five variants 𝒳₀ to 𝒳₃ (154/2-10);
  6. the fuseaux and the counts (154/127-176).

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes, and a partial Lean check of a form of 154/019 (`lean/Grothendieck/Folder154.lean`). You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA11-C3-01 to -03).** The disk model is as follows.
  - Cutting X along a narrow Möbius band around D gives a disc in which each pseudoline of Σ is a chord.
  - Two chords meet at most once, crossing there. Parallelism (being disjoint in the disc) is an equivalence relation whose classes are the vertices of Σ on D.
  - His claim that these two conditions characterize the chord systems of relative positions holds; we checked it by a sketch.
- **R2 (SA11-R154-08).** His expected injectivity (154/019) holds. The deployed polygon P̂(D) is the contraction (M ∪ D)/D of the rank-3 oriented matroid, refined by the order of the crossings at the vertices on D. It determines D by Las Vergnas's theorem.
- **R3 (SA11-R154-07, SA11-K154-01).** His claim that P̂(D) is compatible with the antipodies (154/018) holds for stable D. It fails for D through a vertex of Σ, where the antipodism is the half-turn followed by reversing each cluster of crossings.
- **R4 (SA11-R154-17, -18).** His genus formula on 154/120 is right: χ(𝒳) = s₂ − s₀ and g = 1 − χ.
  - When every relative position is straight, s₀ = 2E, so χ(𝒳) = 1 − n and g = n. This was checked in full for n = 3 (s₂ = 10, s₀ = 12) and n = 4 (s₂ = 33, s₀ = 36).
  - 𝒳 is non-orientable (154/064), so in that case it is a sum of n + 1 projective planes.
- **R5 (SA11-R154-20).** For pseudolines, a position through ν vertices has a ν-cube of generizations (154/154), of which 𝒳 keeps 2ν squares. A semi-stable position can have more than two critical endpoints (154/151).

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** χ(𝒳) = 1 − n for every non-trivial arrangement of n pseudolines, and 𝒳 is, up to homotopy, the rank-3 extension space modulo reorientation, blown up at the n supercritical points. Sturmfels-Ziegler: the extension space of a rank-3 oriented matroid is homotopy equivalent to a sphere.
- **L2.** 𝒳 is a "cyclic section" of the cubical extension space. At a position through ν vertices, the cyclic order of the 2ν generization points selects 2ν of the 2^ν stable generizations, as the coherent cells form a subcomplex in the generalized Baues problem.
- **L3.** The image of the polygon invariant is cut out by local conditions: the 2n weight rule, the reversed clusters at the vertices on D, and the existence of three triangles (Levi). These would be the rank-2 contraction conditions of Las Vergnas.
- **L4.** The 1986 "pseudo-disques" with "cordes" of cote 156 (156-4/32, 45) are the chord systems of R1.

## What the outcome must be

{{OUTCOME}}

## Parts

**A. The surface of relative positions. The main question is A.1.**
- **A.1 (main).** Determine the topology of 𝒳 for every non-trivial arrangement Σ of n pseudolines.
  - Is 𝒳 well defined: are all vertices of order 4, and are the gluings consistent when relative positions pass through three or more vertices, or when semi-stable positions have more than two critical endpoints (R5)?
  - Is χ(𝒳) = 1 − n?
  - Determine the homotopy relation of 𝒳 to the extension space of the rank-3 oriented matroid of Σ and to its blow-up at the supercritical points. Settle L1.
  - **Test case:** a simple arrangement of 6 pseudolines with v₁₂, v₃₄ and v₅₆ on one pseudoline. Count s₀ and s₂ there by program.
- **A.2.** Settle L2: describe the cells of 𝒳 inside the cubical extension space.
- **A.3.** Settle L3 and his question 2° on 154/020.
  - Determine which cyclic orders on the set of half-pseudolines, with the cluster twist of R3, come from relative positions.
  - Determine whether the weighted, cellularly embedded graph Γ(Σ) can be rebuilt from them.
- **A.4.** Write out the complete proofs of R2 and R3 from Las Vergnas's theorem, and of the sufficiency in R1.


## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- A. Björner, M. Las Vergnas, B. Sturmfels, N. White, G. M. Ziegler, *Oriented matroids* (2nd ed. 1999), ch. 6-7.
- M. Las Vergnas, "Extensions ponctuelles d'une géométrie combinatoire orientée" (1978).
- B. Sturmfels and G. M. Ziegler, "Extension spaces of oriented matroids", Discrete Comput. Geom. 10 (1993) 23-45.
- N. E. Mnëv and J. Richter-Gebert, "Two constructions of oriented matroids with disconnected extension space" (1993).
- L. J. Billera, M. M. Kapranov, B. Sturmfels, "Cellular strings on polytopes", Proc. AMS 122 (1994).
- J. E. Goodman and R. Pollack on allowable sequences and wiring diagrams.

{{RULES}}

{{DELIVER}}
