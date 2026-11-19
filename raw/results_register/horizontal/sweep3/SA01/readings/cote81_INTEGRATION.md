# Cote 81: integration (reader R4, Claude Opus 5.5 at effort max, 19 Nov 2026)

## STUDY

**Extent.**
- Every transcribed scan of cote 81 was read: 52 scans, in the Codex-web folders J81-01 to J81-07, the only witness.
- The Pro package named after cote 81 holds only cote 154.
- Seven scans were viewed. The checks are 13 check events (re-proofs, three brute-force computations, scan readings) and 7 corrections.

**What the cote is.** It is not about immersions of the disc, as the sweep 2 map says (SA01-K81-07). It has five parts.

1. **Spherical maps and Belyi functions (81/2-6, "0 Cartes sphériques en général").**
   - Framed oriented spherical maps ↔ "special" rational functions f = P/Q: f(0) = 0, f(1) = 1, f(∞) = ∞, étale over P^1 - {0,1,∞}, critical points off f^{-1}{0,∞} lying over 1 with index 2.
   - He translates this into conditions on P and Q, and observes that Aut(C) acts through Gal(Q̄/Q).
   - Everything checks. His conditions allow free half-edges, as in the cartographic convention, and his trial case Q = 1 is the plane trees (Shabat polynomials).
   - This is the dessins correspondence for the cartographic group G_2 of cote 76 (SA04-24).
2. **A Fermat computation in another hand (81/7-8).** It derives the Barlow-Abel relations correctly and calls the divisibility q | C(q,i) a "hypothesis". The hand on the scan is not his; my attribution, not settled.
3. **n-ary decompositions of a space (81/14-40), in two versions.**
   - Version I: n disjoint closed sets, each cutting a connected X into two components, cut X into n + 1 atoms whose incidence graph is a tree.
   - Version II axiomatizes binary decompositions (closed hemispheres, equator) and non-"panachées" (compatible) pairs, and gives the four-set diagram and its degenerate cases.
   - It then defines a "maquette ordonnée": a finite poset with an order-reversing fixed-point-free involution in which, for every pair, exactly one of x, σx is comparable with y. This is the compatible-split, or nested-pocset, description of a tree.
   - Two errors:
     - (10) ⇔ (11) holds only one way (harmless);
     - the Proposition of 81/40, "C_{≥x} is totally ordered", is false already for the tripod. The true statement, intervals are chains, is where his proof breaks off. Checked over all trees with up to 7 vertices.
4. **Polygon structures and non-crossing partitions (81/41-53).**
   - A finite set with a "bi-circularisation" (the polygon structure of cotes 78-79); segments; "non panachés" (non-crossing) subsets, with four equivalent characterizations, checked for N ≤ 9.
   - Non-crossing partitions from laminar families of segments. He marks his own reconstruction claim "faux" and gives a correct counterexample.
   - "Onglets" (interval blocks): the minimal saturated segments, at least two of them. Checked over 6,914 partitions.
   - A peeling by onglets; the same theory on a path.
5. **Gluing maps along edges (81/54).** Faces and genus when two edges (with one or two "rives") are cut and reconnected. His formulas are right as written in the ink; the transcription's "g' - g''" is wrong.

**Dating.** 81/13 carries a table of his meditation "Notes" up to 1981, so the cote is from 1981 or later. That fits cote 79 (1982 or later) and cote 154 (1983-1984).

**Links.**
- SA04: the cartographic groups of cote 76 and the polygon structures of cotes 78-79.
- SA11: the vocabulary of "rives", "Dessin plié" and polygon structures, shared with the relative-position surface of 154/46-76.
- Cote 80 (pseudolines): the chord and line drawings of 81/10-12.

## HUNCHES

- **H81-1.** The "maquettes ordonnées" of 81/38-40 are the finite nested poc-sets, i.e. compatible split systems, and every one is the maquette of a unique finite tree.
  - The tree is recovered from the intervals, which are chains (SA01-R81-08). This is what his abandoned proof was heading for.
  - Literature, all locators to be checked: Buneman (1971) on compatible splits; Dunwoody (1979) on nested sets; Roller (1998), "Poc sets, median algebras and group actions"; Sageev (1995). His (28 a) is the form of nestedness in which exactly one of the four relations holds up to σ.
- **H81-2.** Parts 1, 3 and 4 fit together as a combinatorial preparation for the Galois action on plane trees.
  - 81/3 with Q = 1 is plane trees (Shabat polynomials).
  - Non-crossing partitions of n points correspond to plane trees (Kreweras 1972; Dershowitz-Zaks; locators to be checked).
  - Trees are recovered from compatible decompositions (H81-1).
  - Test: compare with the Esquisse's discussion of trees (cote 119) and with the other SA01 cotes.
- **H81-3 (speculative).** The margin "Dessin plié" (81/50) and the chord diagrams of 81/10-12 suggest that a folded disc is described by a non-crossing partition of its boundary points. That would make cote 81 the boundary combinatorics behind the folded maps and immersion models of 154/46-76.

## PACKAGES

- **P-R4-4. Cote 81 against cote 154: what the non-crossing structures are for.**
  - Question: do the ordered models and non-crossing partitions of 81/26-53, and the edge gluing of 81/54, supply the local data of the relative-position surface of 154/46-76? Write the dictionary: "rives" and birive/monorive edges, folded maps ("Dessin plié", "folding", "double folding"), polygon structures and polygonal transport. For each statement of 154 that uses such a structure, give its counterpart in 81 or record that there is none.
  - Why it matters: SA01-9 to -12 (the relative-position surface of an added pseudoline, Esquisse §8) are open constructions on his pages. If cote 81 is their combinatorial basis, its proved statements (with SA01-K81-01 and -02 corrected, and the reconstruction of trees cited from the literature) become the first fixed pieces.
  - Strongest reduction on the page: the corrected 81/40 and the four characterizations of non-panaché pairs (81/43-44), both checked.
  - Material: J81-04 to J81-07; `c81checks.py` in reader R4's scratchpad; the SA11 readings of 154/46-76; the Pro notes MPL_81_038-055+154_046-076 (cote 154 only).
