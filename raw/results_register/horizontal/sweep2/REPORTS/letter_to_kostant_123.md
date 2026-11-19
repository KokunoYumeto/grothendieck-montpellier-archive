# Cote 123: the letter to Kostant of 22 October 1969

Piece of horizontal sweep 2, part 2. Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. Topic SA20, item
SA20-W4; related items SA20-W1 and SA20-W3.

## Where it is

| What | Location |
|---|---|
| The letter | Cote 123, scans 022–023 (`grothendieck_archive_montpellier/13_autour_desquisse_dun_programme/123.pdf`, pages 22–23; images `img/123_022.png`, `img/123_023.png`). A typed letter, "Dear Kostant", signed "A Grothendieck"; the date is written by hand. |
| Our notes on it | The Codex notes on the sheets of folder C123-02 (`codex:C123-02#1`, `#2`) and its transcription (`results_register/horizontal/inputs/SA20/codex/C123-02_transcription.tex`). There is no Pro note and no companion unit. |
| The folder's cover | K123-02, scan 015: "Résumé th. de conjugaison Kostant + lettre à Kostant". |

## What it says

These are read on the scan images; paraphrased, with his words in quotation marks.

1. **The date.** "Massy 22. 10. 1969"; he lived at Massy then.
2. **Why he wrote.** He reread Kostant's papers in the American Journal of Mathematics, "The principal
   three-dimensional subgroup …" and "Lie group representations on polynomial rings". He was prompted by "some nice work
   of Brieskorn on Klein singularities", and says the work "cries for careful reconsideration in the framework of Alg.
   Geometry".
3. **Quadruples.** He classifies quadruples (T, B, T′, B′): T and T′ are maximal tori "in apposition" (Kostant's term),
   and B ⊃ T, B′ ⊃ T′ are Borel subgroups.
   - The number of conjugacy classes is card(W)²/(h z φ(h)), with W the Weyl group, h the Coxeter number, z the order
     of the centre and φ Euler's function.
   - With a generating element of the cyclic group T ∩ N(T′) (of order h) also given, it is card(W)²/(h z).
   - The stabilizer of a quadruple is T ∩ T′ = e, so such a structure makes G rigid up to outer automorphisms.
   - A footnote: N(T) ∩ N(T′) is an extension of (Z/hZ)* by Z/hZ × (the centre).
4. **Questions on quadruples.**
   - Are B and B′ in general position, that is, is B ∩ B′ a maximal torus?
   - Is there a distinguished conjugacy class of quadruples?
   - What are their automorphism groups (subgroups of the outer automorphism group)?
5. **The adjoint quotient.** He asks about the canonical morphism 𝔤 → 𝔥/W, Steinberg's G → T/W, and the orbits.
   - "How varies the rank … of the tangent map"?
   - For unipotent orbits of dimension n − r − 2, "just the next lower after the maximal dimension n − r", he believes
     the rank is r − 1 when all roots have the same length ("the corresponding diagrams A, D, E₆, E₇, E₈ are those
     corresponding to Klein singularities"), and less than r − 1 otherwise.
   - In the first case he expects "just one orbit", and "maybe this property will be caracteristic of the
     'homogeneous' case".
6. **The dimension of the Borel varieties.** "If 2N = n − r is the number of roots and if the dimension of the orbit of
   the given element is 2N − 2i, I would expect the dimension of the previous variety to be equal to i."
   - The previous variety is the set of Borel subgroups containing g ∈ G, or whose Lie algebra contains x ∈ 𝔤.
   - "The inequality ≤ i would imply, by generalizing a depth argument of Brieskorn, that the singularities of the
     fibers of your map 𝔤 → 𝔥/W (resp. Steinberg's G → T/W in case G is simply connected …) are 'rational'". That is,
     R^i f_*(O_{F′}) = 0 for i > 0, for a resolution f: F′ → F.
7. **His closing remark.** "For some of them, it would indeed be scandalous that the experts do not know the answer!"

## What depends on what

- **SA20-W4 uses SA20-W1** (K123-01, "Lissification du morphisme de Kostant" and "… de Steinberg").
  - These are the same two morphisms, taken over a base S. The dimension of the variety of Borels through an element
    is asked on 123/007 ("Quelle est sa dimension").
- **SA20-W4 uses SA20-W3** (K123-02, K123-03, C123-01: principal subgroups, Coxeter elements, μ_h → G, the remarkable
  homogeneous spaces).
  - The quadruples are built from tori in apposition and the cyclic group of order h.
- **The margin of 123/019** (C123-01) belongs to the same circle: "pas le cas, p.ex. pour A₂, A₄ (cela l'est pour A₃)".
  - It is explained on line 126: the parabolics attached to the subregular unipotents are Borel subgroups.
  - Checked by computation: the subregular weighted Dynkin diagrams are (1,1) for A₂ and (2,1,1,2) for A₄, with no
    zero node; for A₃ the diagram is (2,0,2).

## What agrees and what conflicts

**Agrees** (literature from memory, not re-read; for part 3 to confirm):
- The expectation in item 6 is the formula dim B_x = ½(dim Z_G(x) − r). With dim G = 2N + r, an orbit of dimension
  2N − 2i has a centralizer of dimension r + 2i. Steinberg proved the formula in 1976, "On the desingularization of the
  unipotent variety", Invent. Math. 36.
- The transversal singularity of the nilpotent cone at a subregular element is a Klein singularity, of the same type in
  the simply-laced case. This is Brieskorn's ICM 1970 talk, with the simultaneous resolution credited to Grothendieck;
  Slodowy, LNM 815, 1980.
- The nilpotent variety has rational singularities (Hesselink 1976).

**Conflicts:**
- His guess that a single subregular orbit characterizes the simply-laced case.
  - The subregular unipotent class is unique in every simple type (Steinberg, LNM 366, 1974; from memory).
  - So uniqueness cannot single out the simply-laced case. What singles it out is the type of the transversal
    singularity.

**Not checked:**
- The count card(W)²/(h z φ(h)). It is consistent with his footnote: a group of order h z φ(h) acts freely on the
  card(W)² choices of (B, B′).
- It gives whole numbers for A₁ (1), A₂ (2), B₂ (4), G₂ (12) and E₈ (2,903,040) (my arithmetic).

## What cote 123 is

My reading, for part 3 to check, from the titles and this letter: cote 123 holds his own notes of about 1969 on the
adjoint quotient.
- "Lissification du morphisme de Steinberg" is likely his simultaneous resolution, known from Brieskorn and Slodowy.
- With it come the subregular singularities and the dimension of Springer fibres, which the letter asks for.

## Corrections and records

| Record | File |
|---|---|
| Refinement of the subregular guess | `SA20/CORRECTIONS.tsv` |
| Claim links: the dimension formula, subregular uniqueness, rational singularities, the quadruple count | `SA20/CLAIM_LINKS.tsv` |
| The readings decided on the images (date, the expectation passage) | `SA20/CHECK_EVENTS.tsv` |
| The A₂/A₄/A₃ check | `SA20/CHECK_EVENTS.tsv` (part 1) |

**For part 3:**
- Read Brieskorn (1970), Slodowy (1980) and Steinberg (1974, 1976), and see whether they cite this letter or attribute
  the dimension formula to Grothendieck.
- Check the quadruple count.
