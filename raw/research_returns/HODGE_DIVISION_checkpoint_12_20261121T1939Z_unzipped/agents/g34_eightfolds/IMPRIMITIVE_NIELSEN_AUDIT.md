# Independent whole-proof audit of D-IM-08

**Result: PASS.** Read the entire D-IM-08 proof in `agents/imprimitive/IMPRIMITIVE_PROOFS.md` and the complete `nielsen_rank_one.py` certificate. Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION, 2026-11-21. This is a whole-proof mathematical audit together with a separate small exact arithmetic check.

## Generation

The uncolored commutator has the stated three-element support, and its cyclic translates give a connected support hypergraph. The elementary alternating-group lemma used in the proof is valid: when two three-cycles share exactly one old vertex, conjugating that old vertex to another old vertex and multiplying one cycle by the inverse of the other produces a three-cycle on two old vertices and one new vertex. This reduces to the two-vertex-overlap step. Since the existing alternating group is transitive even at the initial three vertices, the induction works. The twelve-cycle is odd, so the projected group is all of \(S_{12}\).

The two displayed powers of \(a^{-1}b\) are correct. Conjugating a diagonal element by a monomial lift depends only on its permutation. In the first case the selected transposition compares colors zero and minus one; in the second it compares seven and zero, with seven invertible modulo each of \(3,4,6\). Thus a primitive opposite-color diagonal belongs to the generated group. Permutation conjugation and powers generate every total-zero diagonal.

For \(e<d\), after dividing out that diagonal subgroup, the generated subgroup lies in \(\mu_{d/e}\times S_{12}\) and projects onto \(S_{12}\). Its commutator subgroup maps onto \(A_{12}\), lies in \(1\times A_{12}\), and hence equals that subgroup. The two odd generators then give independently the total-color generator and the sign generator. This proves the full quotient is generated. No lift of a transposition has been assumed before proving the permutation projection is surjective, and no explicit lift word is needed.

## Signature and geometry

The colored-cycle fixed dimensions and ages give signature \((5,5)\) in every case. The inverse-pair identity for ages proves both embeddings are balanced. The intermediate genera and ramification counts agree with the previously checked cyclic-tower formula.

The degeneration separating the two inverse pairs has trivial node inertia. The components over the two base components are the cosets of the cyclic subgroups, and their two-branch cyclic covers are rational. The graph is connected by generation. Its cellular exact sequence gives natural-representation multiplicity five by Frobenius reciprocity.

At every smoothing annulus the local logarithm is a positive Dehn-twist transvection. The vertex incidence relations are exactly the relations on vanishing-circle classes, by Mayer–Vietoris for the punctured rational components. The positive sum of the rank-one forms has image the full span of those circles. Therefore the total logarithm surjects onto graph cohomology. Taking the natural multiplicity component is exact in characteristic zero and preserves the image, so its logarithm has rank five.

A constant polarized weight-one period map has monodromy preserving its fixed Hodge structure. Such monodromy is unitary for the positive Hodge metric, and a unitary unipotent matrix is the identity. The nonzero logarithm therefore proves nonconstancy. Since the source is a Hurwitz curve, its image and generic differential have exactly rank one. The argument applies to every component containing the specified tuple.

## Independent finite verification

`audit_imprimitive_nielsen.py` uses basis-image arithmetic and does not import the author's implementation. It checks all nine \((d,e)\) choices: exact product one, the two diagonal powers, primitive commutators, fixed dimensions, ages, and graph multiplicity. It passed and wrote `audit_imprimitive_nielsen.json`. The full enormous groups are neither enumerated nor claimed to have been enumerated; generation is the proof above.

No defect was found. The result correctly disproves a universal maximal-rank assertion for arbitrary Nielsen classes, while leaving the previously proved maximum ranks unchanged.
