# Cote 81 (SA01, "Géométrie et topologie combinatoire", part 1): the reading

- **Who:** Claude Opus 5.5 at effort max, reader R4 of the deep-sweep agent a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max), horizontal sweep 3, wave 1, topic SA01.
- **Date:** 19 Nov 2026.
- **What was read, and how:**
  - The Codex-web transcriptions `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J81-01` to `J81-07` (`out/<folder>_transcription.tex`). They were run through the lead's cleaner (`sweep3/_tools_a6d42bf6/clean_tex.py`, then `show.py`), then my squeezer, then a filter that drops drawing coordinates. Drawings were not read as text; seven scans were looked at as images.
  - These folders are the only witness for cote 81. The Pro package `MPL_81_038-055+154_046-076` holds only cote 154, scans 46-76, despite its name: its notes say the cote 81 scans "were explicitly omitted". So there was no cote 81 text to compare. Its notes were searched only for links to cote 81 (section "Links").
  - The doubts files and audits were used only by counts (inventory script). The notes files of the seven folders were read.
  - Scans: `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/81.pdf` (55 pages, scan N = PDF page N).
- **Item:** SA01-29 (cote 81). The sweep 2 map describes it as "immersions of the disc and of the circle". The pages contain no such text; see the correction SA01-K81-07.
- **Ids:** check events SA01-R81-nn; corrections SA01-K81-nn.
- **Computations:** `c81checks.py` in my scratchpad (`r4sa01`).

## What the cote contains (map of the 55 scans)

| Scans | Content |
|---|---|
| 2-6 | "0 Cartes sphériques en général": oriented spherical maps with a frame ↔ "special" rational functions (Belyi functions); the Galois action |
| 7-8 | an attempt at Fermat's equation (the Barlow-Abel relations), in another hand |
| 10, 12 | drawings: discs with chords, marked "OK" (one "?"); a tripod, a triangle, line arrangements; scan 12 is a drawing only |
| 11 | scratch: P(X × Z) ≃? Hom(...), Hom(X,Y) ⊂ P(X × Y) |
| 13 | a table of his meditation "Notes" 1-23 (A-E, 1976/77-1981) |
| 14-25 | "décompositions et découpages n-aires d'espaces topologiques", Version I: separating closed sets, the atoms, the tree |
| 26-30 | binary decompositions of a set; trees give families of them |
| 32-40 | Version II, "Décompositions n-aires d'un espace topologique" 1.1-1.3: hemispheres, equator, non-"panachées" pairs, "maquettes ordonnées" |
| 41 | title "relations d'équiv. non panachées" |
| 42-53 | bicircular (polygon) structures on a finite set; segments; non-panaché (non-crossing) subsets; non-crossing partitions; laminar families of segments; "onglets"; the same on a path |
| 54 | attaching two maps along edges: faces and genus |
| 55 | blank; 4 carries only a margin mark |

Scans 1, 9 and 31 have no inventory row.

## 81/2-6. Spherical maps and special rational functions

**What he does.**
- 81/3: "Carte sphérique (orientée) avec repère (dans cat. isotopique)" ≃ a "special" morphism f: P^1_C → P^1_C. Special means:
  - f(0) = 0, f(1) = 1, f(∞) = ∞;
  - f is étale over P^1 - {0,1,∞};
  - every critical point z with f(z) ∉ {0,∞} has f(z) = 1 and f''(z) ≠ 0 (ramification 2).
- He translates this into pairs P, Q of coprime polynomials with P(0) = 0, P(1) = Q(1) = 1 and deg Q < deg P, plus conditions on P', Q', P'', Q''. His NB is QP' - PQ' = (Q-P)P' + P(P'-Q').
- Then the question "peut-on avoir P'(z) = 0 (d'où aussi Q'(z) = 0) ... sans avoir P(z) = Q(z) ?". He answers yes with Q = 1, P = aT² + bT: P'(-b/2a) = 0 and P(-b/2a) = -b²/4a ≠ 1.
- 81/5: Aut(C) acts on the special f through Gal(Q̄/Q), because their coefficients are algebraic.
- 81/6: the derivatives of P/Q.

**Checks.**
- **SA01-R81-01 (targeted proof check).** All right:
  - the identity of the NB;
  - at a point with P = Q ≠ 0 and P' = Q', f''(z) = (P'' - Q'')P/Q², so f'' ≠ 0 ⇔ P'' ≠ Q'', as he writes;
  - his example, and (P/Q)'' = (P''Q² - Q''PQ - 2P'QQ' + 2PQ'²)/Q³ (81/6).
  - His conditions allow unramified points over 1, i.e. half-edges fixed by the edge involution (the free half-edges of the cartographic convention). With "f(z) = 1 ⇒ f'(z) = 0" added, one gets the clean Belyi functions, i.e. maps without free half-edges.
  - The case Q = 1 that he tries (f a polynomial, one face) is the plane-tree case: Shabat polynomials.
- **SA01-R81-02 (targeted proof check).** 81/5 is right. The special f of given degree are finite in number, since they correspond to the framed maps with that many darts, and the set is Aut(C)-stable. So each has finitely many conjugates and algebraic coefficients.

## 81/7-8. Fermat's equation, in another hand

**What the pages do.**
- a, b, c pairwise coprime with a^q + b^q = c^q, q prime. Put c = a + b' = b + a'. Then b' divides b^q, and for a prime p ≠ q, p^{α'} ‖ b' and p^α ‖ b give α' = qα. Hence b' = q^γ b_0^q and a' = q^ζ a_0^q, with ζγ = 0.
- "Je fais l'hypothése suivante si q premier et 1 ≤ i < q alors q | C_q^i". The conclusion is "γ = 0 ou γ = qα - 1 (sous réserve que l'hypothése est vraie)".

**Checks.**
- **SA01-R81-03 (independent re-proof).** The derivation is right. These are the Barlow-Abel relations: c - a = b_0^q if q ∤ b, and q^{qα-1}b_0^q if q^α ‖ b.
  - The "hypothesis" is a theorem.
  - The exclusion of γ = qα uses that the cofactor is ≡ q a^{q-1} mod q² for q ≥ 3.
  - a' and b' are coprime because a common prime would divide a^q and b^q.
- **The hand (SA01-R81-12).** On the scan the hand is upright and rounded, unlike his slanted hand on 81/34-40. The style points the same way: a standard fact is called a hypothesis. These pages are probably a correspondent's or a student's attempt kept in the folder. The attribution is mine and is not settled.

## 81/10-13. Drawings, scratch, the "Notes" table

- 81/10 and 81/12 (seen on the scans): circles with chords (chord diagrams), several marked "OK" and one "?"; a tripod, a triangle, crossing lines. They look like enumerations of small chord or line configurations in a disc. They were not analysed.
- 81/11: scratch on P(X × Z), Hom(X, Y) ⊂ P(X × Y) and a pullback square; "≃" carries a "?". Not checked.
- 81/13: a table of his meditation "Notes" 1, 5, 7, 15, 20, 23, under the headings A (1976/77) "Découverte de la Méditation" to E (1981) "Der Baumeister / Le Bâtisseur". It dates this sheet to 1981 or later. It is not mathematics.

## 81/14-25. Version I: n-ary cuttings of a topological space

**What he does.**
- Setting: X a topological space and (E_i)_{i∈I} closed sets with:
  - (a) X - E_i has exactly two components;
  - (b) E_j lies in one of them for j ≠ i;
  - (margin) each component of X - E_i has E_i in its closure, which holds if X is connected.
- Card I = 2: Σ_i^+ is the component of X - E_i not containing E_j. Then (1) Σ_1^+ ∩ Σ_2^+ = ∅ ⇔ (2) Σ_1^+ ⊂ Σ_2^-, and X = Σ_1^+ ⊔ E_1 ⊔ Σ_12 ⊔ E_2 ⊔ Σ_2^+.
- General I: the classes of Π_I° (the atoms of the binary partitions of X - ∪E_i) number card I + 1, by induction.
  - Each class is X - ∪_{α∈K} Σ̄_α^+ with the Σ_α^+ disjoint, and this expression is unique, with K = {α : V̄ ∩ E_α ≠ ∅}.
  - The incidence "U_s meets Ē_i" makes (classes, I) a strict graph, and "Le graphe est un arbre" (81/24).

**Checks.**
- **SA01-R81-04 (targeted proof check).**
  - Card I = 2 re-proved: the two components of X - E_i are open in X because there are only two.
  - The classes are atoms, not components. On a circle with E_1 = {p, q}, E_2 = {r, s} (r, s on one side), Σ_12 has two arcs but is one class, so the count n + 1 stands.
  - The general statement is the passage from pairwise compatible ("non panachées") splits to a tree (Buneman's theorem; locator to be checked). The induction was read, not checked line by line.
- **Correction SA01-K81-06 (transcription).** Closure bars are missing throughout 81/15-22, e.g. "Σ_1^+ ∩ E_1 ≠ ∅ i.e. Σ_1^+ ≠ Σ_1^+" and "Σ_1^+ ⊊ Σ_1^+ ⊂ Σ_1^+ ∪ E_1". The cleaner keeps \overline (it appears on 81/16), so the bars are missing from the transcription.

## 81/26-30. Binary decompositions of a set; trees

**What he does.**
- A binary decomposition is two subsets ("hémisphères") covering X, neither contained in the other, meeting in the "équateur". Two of them are "non panachées" if they are distinct and have disjoint hemispheres Σ_1^+, Σ_2^+. The four sets need not be distinct (Σ_1^+ = Σ_2^- is allowed).
- Every tree Γ = (S, A) with sets U_s, E_a gives, by cutting at each edge, a family of binary decompositions of X = ⊔U_s ⊔ ⊔E_a:
  - (∗): proper iff U_s ≠ ∅ at every leaf;
  - (∗∗): π_a ≠ π_b iff one of U_s, E_a, E_b is non-empty at each vertex s of order 2;
  - (∗∗∗): strict non-parallelism iff U_s ≠ ∅ or E_a ≠ ∅ there.
- "Le cas où certains des ensembles U_s, E_a pourraient être vides est à examiner avec plus de soin".

**Checks.** SA01-R81-05 (targeted proof check): (∗) and (∗∗) re-proved; (∗∗∗) read, not checked.

## 81/32-40. Version II: binary decompositions, non-panachées pairs, ordered models

**What he does.**
- 1.1: binary decompositions into closed hemispheres (1)-(4); (5) X connected ⇒ E ≠ ∅, and with connected hemispheres X connected ⇔ E ≠ ∅; Σ^{∘ε} = X - Σ^{ε'} (6)-(8).
- 1.2:
  - non-panachées pairs (10) Σ_1^+ ∩ Σ_2^+ = ∅, "condition qui équivaut à" (11) Σ_1^+ ⊂ Σ_2^- or (11bis);
  - the diagram (14) of three cartesian and cocartesian squares;
  - (16) Σ_12 ≠ ∅;
  - Proposition (81/35): the disjoint couple (Σ_1^+, Σ_2^+) is unique;
  - (20): the four hemispheres are distinct unless exactly one of a) E_1 = Σ_12, a') E_2 = Σ_12, b) Σ_12 = X holds;
  - Cor. (81/37) and "strictement non panachées" (21).
- 1.3:
  - a non-panachée family (Π_α), the set C = ⊔ω_α with the involution σ and the order (26): x < y ⇔ α ≠ β and Σ_α^x ∩ Σ_β^{σy} = ∅;
  - φ: C → P(X) is increasing, and an order-embedding iff the family is strict;
  - Definition (81/39): a "maquette ordonnée" is a finite set with a fixed-point-free involution σ and an order such that (28 a) x, y are comparable iff σx, y are not, and (28 b) x < y ⇒ σy < σx.
  - Proposition (81/40): "pour tt x ∈ C, les ens. C_{≥x}, C_{≤x} sont tot^t ordonnés". The proof breaks off at the foot of the page ("d'où σz <"), and 81/41 starts a new title.

**Checks.**
- **SA01-R81-06 (targeted proof check).** The following are right:
  - (5)-(8);
  - the squares (14)-(15): Σ_2^- = Σ_1^+ ∪ Σ_12, E_1 = Σ_1^+ ∩ Σ_12;
  - (16 c);
  - the uniqueness in the Proposition of 81/35: the other three couples would force Σ_12 = ∅ or an empty hemisphere;
  - (20) with its mutual exclusions;
  - the Cor. of 81/37;
  - the transitivity in (26), which he calls "immédiat" (x < y < x would force Π_α = Π_β);
  - σ an anti-automorphism.
- **SA01-R81-07 (refuted, refined SA01-K81-01).** (10) implies (11) and (11bis), but not conversely, since closed hemispheres can share equator points.
  - On X = [0,3], take Σ_2^- = [0,2], Σ_2^+ = [2,3], Σ_1^+ = [1,2] and Σ_1^- = [0,1] ∪ [2,3]. Then (11) and (11bis) hold, but Σ_1^+ ∩ Σ_2^+ = {2}.
  - This is harmless, because (10) is the definition used afterwards.
- **SA01-R81-08 (computation, `c81checks.py` (1); refuted, refined SA01-K81-02): the Proposition of 81/40 is false.**
  - I built the maquette of every labelled tree with 3-7 vertices (18,247 trees). All satisfy (28 a, b).
  - C_{≥x} fails to be a chain already for the tripod: x the leaf side of one edge, y and z the large sides of the other two edges.
  - What holds in all cases:
    - if x < y, x < z and y, z are incomparable, then σy < z (the two hemispheres cover X). This is exactly where his proof stops;
    - every interval [x, y] is a chain.
  - The intervals statement is what reconstructing the tree needs.

**Corrections.**
- SA01-K81-01: (10) ⇔ (11).
- SA01-K81-02: the Proposition of 81/40.
- SA01-K81-04 (slips, his or the transcription's):
  - (4) "∩ Σ^ω" for ∩ Σ^ε;
  - (13) "E_2 = Σ_1^+ ∩ Σ_2^-" for Σ_2^+ ∩ Σ_2^-;
  - (15) "Σ_22" for Σ_12.
- SA01-K81-05: (***) a) reads "(Σ_1^+ ≠ Σ_2^-) ⟺ E_1 ≠ Σ_12" for "=" on both sides, as (20) a) has it.

## 81/42-53. Polygon structures, non-panachés subsets, non-crossing partitions

**What he does.**
- 81/42: S finite (N ≥ 3) with "une structure polygonale ou bi-circularisation {u, u^{-1}}".
  - Segments are T = {s_0, us_0, ..., u^{i-1}s_0} with 0 < i < N. Complements, intersections and unions of segments are segments in the stated cases.
  - The segment components of a subset S' correspond to the components of X - S'' in a topological polygon.
- Proposition (81/43-44): for disjoint non-empty A, B the following are equivalent; when they hold, A and B are "non panachés":
  - a) A and B lie in disjoint segments;
  - b) for a, a' ∈ A and b, b' ∈ B, {a, a'} is a side of the induced square;
  - c) B lies in one segment component of S - A, and c') the same with A and B exchanged;
  - d) (margin) the convex hulls in a plane realization are disjoint.
- 81/45, "Structure à étudier": partitions into mutually non-panachées classes ("partitions non panachées"). "Intuition": a functorial passage to such partitions with classes of size 2 on N' ≤ N points.
- 81/46-48: Σ a family of segments, laminar (σ1) and with (σ2) (a strictly smaller member contains no end of the larger). A* = A - ∪_{B⊊A} B contains ∂A.
  - The A* are disjoint and non-panachés, so they give a non-crossing partition.
  - Under (σ3) he claims that the partition determines Σ. He marks it "faux" in the margin and gives the counterexample with classes {a_1,a'_1}, {b,b'}, {a_2,a'_2}.
- 81/49-51: R a non-panachée equivalence relation and R-saturated segments.
  - Prop.: the minimal saturated segments are the classes that are segments, the "onglets".
  - Cor.: every saturated segment contains one, and there are at least two when R is not coarse.
  - Then a peeling T_1 ⊂ T_2 ⊂ ... by onglets; margin "Dessin plié".
- 81/52-53: the same for a path I ("graphe-segment"): non-panachées pairs, and non-crossing partitions of I from special families Σ; "Toute partition non panachée peut s'obtenir ainsi, mais de plusieurs façons".

**Checks.**
- **SA01-R81-09 (computation, `c81checks.py` (2a)).** a) ⇔ b) ⇔ c) ⇔ c') holds for all 27,474 pairs of disjoint non-empty subsets of polygons with N = 4..9. d) is the usual convex-hull form of non-crossing.
- **SA01-R81-10 (targeted proof check).**
  - The Prop. of 81/46 (disjointness, non-panaché, injectivity of A ↦ A*) is right.
  - His own "faux" is right: on the hexagon b, a_1, a'_1, b', a_2, a'_2, the families Σ_1 = {{a_1,a'_1}, {a_2,a'_2}, {b,a_1,a'_1,b'}} and the symmetric Σ_2 (with {b',a_2,a'_2,b}) satisfy (σ1)-(σ3) and give the same partition.
- **SA01-R81-11 (computation, `c81checks.py` (2b)).** For all 6,914 non-crossing partitions of N = 3..9 points, the minimal saturated segments are exactly the onglets, and there are at least two onglets when there are at least two classes. The peeling of 81/50-51 was read, not checked.
- These are the non-crossing partitions of Kreweras (1972; locator to be checked), with the onglets as their interval blocks.

## 81/54. Attaching two maps along edges

**What he does.** He takes an edge in each of two maps, cuts both at their midpoints and reconnects them crosswise. An edge is "birive" if it has different faces on its two sides, "monorive" if the same face.
- Two birive edges: "4 faces deviennent 2", f = f' + f'' - 2, g = g' + g''.
- One monorive and one birive: "trois faces deviennent 1", f = f' + f'' - 2, g = g' + g'' (the transcription has "g' - g''").
- Two monorive edges: f = f' + f'', g = g' + g'' - 1.

**Checks.**
- **SA01-R81-13 (computation, `c81checks.py` (3); 3,000 random pairs of oriented maps as permutations, both reconnections).**
  - The first two cases always give a connected map with F = F' + F'' - 2 and g = g' + g''.
  - In the third case F = F' + F'', and g = g' + g'' - 1 whenever the result is connected. When both edges are bridges the result has two components, and his formula holds for the formal genus 1 - χ/2.
  - All his formulas are right as written in the ink.
- **SA01-K81-03 (transcription).** On the scan the second "g = g' - g''" reads g = g' + g'' (150 dpi crop).

## Links

- **SA04, my readings of cotes 76-79:**
  - 81/3 realizes on the sphere the maps that the cartographic group G_2 of 76/37 describes (SA04-24); the regular maps of cote 79 (SA04-27) are a special case.
  - The "structure polygonale ou bi-circularisation {u, u^{-1}}" of 81/42 is the polygon structure Pol(E) of 79/138-141 (ω ↦ ω^ν) and of the polygons of cote 78 (SA04-26).
  - Cote 80, "Systèmes de pseudo-droites", was read by another reader; the chord and line drawings of 81/10 and 81/12 are of that kind.
- **SA11, cote 154/46-76 (Pro package, read for SA11; not reread):**
  - shared vocabulary for the two sides of an edge: 81/54 "birive/monorive" and 154's "rives" ("prolongation des rives", the "facing shore" of 154/069-074);
  - the margin "Dessin plié" (81/50) and the "folding"/"double folding" of 154/046;
  - the polygon structures of 81/42 and the polygonal transport and dihedral monodromy of 154/056-064.
  - These are links of vocabulary and structure, not identifications. The Pro notes date 154 to 1983-1984; 81/13 dates cote 81 to 1981 or later.
- **SA01:** SA01-29 (this cote; its description is corrected in SA01-K81-07). SA01-9 to -12 and SA01-15 are indexed in sweep 2 under cote 81 but belong to cote 154.

## Reused material (one line each)

- 81/13: the table of his meditation "Notes" (1976/77-1981), on a mathematical sheet.
- No printed or typed sheets were noticed in the transcriptions of this cote.

## What was not reached (exactly)

- Every transcribed scan was read: 52 scans (2-8, 10-30, 32-55).
- Scans 1, 9 and 31 have no inventory row and were not viewed.
- The drawings of 81/10, 12 and 54 were looked at only in 40 dpi overviews; drawings elsewhere were not read.
- Read but not checked step by step:
  - the induction of Version I (81/18-25);
  - (∗∗∗) of 81/30;
  - the peeling of 81/50-51;
  - 81/52-53;
  - the "Intuition" of 81/45;
  - the scratch of 81/11.
- The doubts files and audits were used only by counts.
- Scans viewed: 81/7, 10, 12, 34, 36, 40 and 54 (40 dpi overviews), with 150 dpi crops of 81/34, 36 and 54. The crop of 81/34 does not settle the subscript in (13) (SA01-K81-04), and the crop of 81/36 missed (***) (SA01-K81-05).
