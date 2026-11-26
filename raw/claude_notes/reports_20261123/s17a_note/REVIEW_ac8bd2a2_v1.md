# S17a: editor's review (v1)

Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37), field expert for RESEARCH_SA17, 23 Nov 2026. Comments come
first, written before the note.

## Does it contribute something meaningful?

**Yes, modestly.** It gives a reduced base over which Grothendieck's crystalline Dieudonné functor on p-divisible groups
is not full. The base is the coordinate ring of two planes in affine 4-space meeting at a point. We found no reduced
counterexample in the literature.
- It shows that the torsion term in de Jong's 1995 theorem for reduced bases of finite type really occurs.
- It shows that reducedness cannot replace the hypotheses of the known positive theorems: local complete intersection
  (de Jong-Messing) and PD torsion freeness (Lau).

The non-reduced counterexample is classical: Berthelot-Messing III, 4.4.1, and the Stacks project, Example 60.22.1. The
note credits it as such. Its own contributions are three:
- the reduced lift;
- a non-noetherian reduced variant;
- a correction of the divided-power formula of Stacks Example 60.22.1 at p = 2.

**Kind: clear.** No Hexagon post touches the topic; I searched for "Dieudonné", "crystalline" and "p-divisible" on 23
Nov. I found no recent neighbouring work either.

## The gate (read at the source unless marked)

1. **The non-reduced example is classical.**
   - De Jong's ICM 1998 survey "Barsotti-Tate groups and crystals" (Doc. Math. Extra Vol. ICM II, 259-265), p. 261,
     item (x): "D is not fully faithful in general. This fails even over the ring F_p[x,y]/(x^2,xy,y^2). See [2,
     4.4.1]." Here [2] is Berthelot-Messing III.
   - Lau, "Divided Dieudonné crystals" (arXiv:1811.09439v2), Remark 3.4: the same ring k[X,Y]/(X,Y)^2, citing
     Berthelot-Ogus.
   - Stacks Example 60.22.1 (Tag 07LJ) has the element τ_0 = γ_p(x²)γ_p(y²) − γ_p(xy)², with pτ_0 = 0, dτ_0 = 0,
     F*(τ_0) = 0, and a finite detector sending τ_0 to uv ≠ 0. I read it through a page fetch: statements and formulas,
     not the full typeset page.
2. **For reduced bases, the positive results stop short of integral full faithfulness:**
   - de Jong, Publ. IHÉS 82 (1995), Main Theorem 2 = Theorem 5.1.1: over a reduced scheme of finite type over a field
     with a finite p-basis, Hom of Dieudonné crystals is (torsion) ⊕ D(Hom). The torsion is "known" to vanish for lci.
     No example of nonzero torsion is given there, nor in his ICM list (i)-(xi).
   - de Jong-Messing, Bull. SMF 127 (1999): fully faithful over excellent lci schemes; fully faithful up to isogeny over
     excellent local rings. Their Remark 1.4 concerns finite and truncated groups only.
   - Lau: an equivalence onto divided crystals; the ordinary functor is fully faithful on F-finite PD-torsion-free
     schemes (Corollary 1.7 = Theorem 7.9), and fully faithful up to isogeny with cokernel killed by p on F-finite
     F-nilpotent schemes (Corollary 1.6 = Corollary 9.5).
   - Zink, "A Dieudonné theory for p-divisible groups", Introduction p. 2: the crystalline functor fails over rings with
     nilpotents, while "for a reduced ring ... V^{-1} may be recovered". That is consistent with our example: τ vanishes
     on every p-torsion-free PD thickening, Witt vectors included (Remark 6.2 of the note).
3. **Not accessible: Berthelot-Messing III itself** (Grothendieck Festschrift I, 1990). Its 4.4.1 is the non-reduced
   ring, by de Jong's citation. De Jong's survey, written by a reader of that paper, lists no reduced counterexample.
4. **Hexagon** (23 Nov): no work on Dieudonné theory. The "Dieudonné" search returns 2610.00662 (crystalline Tate
   classes), which is unrelated.

Verdict: the reduced example is new as far as searched; write the note.

## What we want to say, and whom the run's text would not serve

- **The expert** must see at once that the non-reduced case is classical. The run's proposition presents three bases
  together, without crediting Berthelot-Messing for R_0, and cites Stacks only for the de Rham comparison. The note puts
  the classical case first, with its locators, and makes the reduced base the theorem.
- **The newcomer** needs the mechanism in one sentence: a p-torsion, Frobenius-killed global section of the crystalline
  structure sheaf is a morphism of Dieudonné crystals between D(μ_{p^∞}) and D(Q_p/Z_p), and over a reduced base no
  homomorphism exists between these groups in either direction. The run's text has this, but inside a long paper.
- **The authors whose work it touches:** de Jong (torsion term), de Jong-Messing (lci), Lau (PD torsion free;
  cokernel killed by p), Zink (reduced rings), Stacks (the example and its p = 2 formula). Each is stated by statement,
  never by merit.

## Faults found and repaired (check events in RECORDS.md)

1. **Credit.** The run claimed the R_0 example as its own. Repair: it is credited to Berthelot-Messing III 4.4.1 and
   to Stacks Example 60.22.1, and in the note it appears only as a remark and as a step in the proof.
2. **Stacks Example 60.22.1 at p = 2.** The displayed δ_p(z) = a^p u + c^p v fails the addition axiom at p = 2: it
   gives δ_2(u+v) = 0, while γ_2(u+v) = γ_2(u) + γ_2(v) + uv = uv. The correct formula adds δε·uv at p = 2.
   - The run found this. I verified it by hand on 20 Nov and again today.
   - The note gives the corrected formula and a complete proof of the divided-power axioms for every p.
3. **Convention.** The direction of the extra morphism depends on the convention for D. The note uses the contravariant
   convention: D(μ_{p^∞}) has F = p, D(Q_p/Z_p) has F = 1. It also observes that over a reduced base both Hom groups
   between the two groups vanish, so the conclusion does not depend on the convention.

No statement of the run is false. The changes are credit, the p = 2 detector formula, and the convention remark.
