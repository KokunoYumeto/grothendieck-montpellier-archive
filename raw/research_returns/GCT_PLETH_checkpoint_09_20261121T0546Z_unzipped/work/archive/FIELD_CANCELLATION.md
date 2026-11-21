# A-019. The field cancellation input on cote133/008

The original target's field cancellation step is valid for the specified strictly nondegenerate quadratic forms, including characteristic two. The exact primary locator is Elman–Karpenko–Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms*, §8, Theorem8.4, p48; its proof uses Theorem8.3 and Lemma8.2, pp47–48. The author-hosted book is https://www.math.ucla.edu/~merkurev/Book/Kniga-final/Kniga.pdf .

In the source's notation, put `V=q⊥(−q′)`. An isometry

`V⊥H(F) ≅ H(E)`

over a field has `dim E≥dim F`. Choose a vector space `G` of dimension `dim E−dim F`, and identify `H(E)≅H(G)⊥H(F)`. The polar form of `H(F)` is nondegenerate in every characteristic. The cited cancellation theorem therefore gives the actual isometry `V≅H(G)`, removing the stabilizer.

The complete proof of Lemma8.2 and Theorems8.3–8.4 was read and checked in this run, including the reflection calculations, the finite-field exception `F₂`, and the restriction of an extended isometry to orthogonal complements. Its characteristic-two hypothesis is nondegeneracy of the polar form of the cancelled summand, which `H(F)` satisfies.
