# A precise limitation of the NP.9 permutation argument for proper families

Saved 2026-11-19T18:29:24.496277+00:00. Unregistered method analysis only. It neither constructs a surviving ordinary Chow class nor proves that the component correction below glues over the entire SNC surface.

Let K be the algebraic closure of the hyperplane coefficient field used in NP.9. In particular K is not just Fpbar. Choose the **nontorsion** line bundle N=O_C(q2−q1) in Pic0(C)(K), whose nontorsion has already been proved. Let F=K(u_I) be the generic sextic coefficient field and L/F the degree24 finite separable field of one generic elliptic-edge root. Its normal closure has group S24 by NP.9.

Consider the proper abelian parameter P=Res_(L/F)(C_L). Over a splitting field it is C^24, with the Galois group permuting its factors. This restriction-of-scalars description follows directly from the finite étale base-change formula. For representability, Stacks97.11.2 and Proposition97.11.5, Tag05Y8, were freshly opened and read with their proofs on19November2026: https://stacks.math.columbia.edu/tag/05Y8 . The product ample bundle from O_C(0) on all24 factors has its canonical permutation linearization, so its section-ring Proj descends the product as a projective scheme. Thus no proper non-schematic parameter is required.

Write M_a=pr_a^*N over the splitting field. The class

    sum_a [r_a] tensor [M_a]

has simultaneous S24 invariance: the roots and the parameter factors are permuted together. Its coefficients are not all equal in Pic(P)_Q. Indeed restricting M_a M_b^(-1) to the ath factor gives N, which is nontorsion. It is therefore false that invariance forces the scalar-equality conclusion used in NP.9 once the coefficients can lie in the Picard group of a varying parameter.

The same phenomenon is represented by an actual component perfect class. If e_a denotes the exceptional divisor over r_a on E1, set

    v = sum_a ([O_E1(e_a)]−1) external ([M_a]−1)
        in K0(E1 times P)_Q.

This is a sum of actual external line-bundle classes and is invariant under the same descent data. Every point endpoint of P evaluates each [M_a]−1 to zero, so v is endpoint-zero. Its elliptic-edge restriction is the displayed family of divisor products. These are precisely the sorts of allowed component corrections that a scalar-only monodromy argument would overlook.

One need not claim that all curve restrictions preserve all coefficient independence. If an actual one-dimensional proper parameter is desired, choose a sufficiently high smooth connected complete-intersection curve through any two selected parameter points. The already proved successive Picard-restriction argument in C.3bp gives finite kernel on Pic0, so the indicated nontorsion coefficient differences can be retained for a suitable such curve. Restriction preserves the actual perfect class and its zero endpoint values. No global gluing assertion follows from this construction.

Thus norming or averaging an arbitrary proper-family witness cannot simply import the transposition argument of NP.9: its parameter can carry the same permutation representation as the roots. A genuine invariant must account for this parameter representation and for the coherent edge/triple totalization. NP.9 remains correct for integral scalar coefficients in the pointwise component Picard image.

## Source and scope update, 2026-11-19T18:49:40.819495+00:00

The continuation reviewer freshly reopened the complete primary Stacks section at Tag05Y8 and read Lemma97.11.2 and Proposition97.11.5 with their complete displayed proofs; retrieval reference `turn364923687view0`. Lemma97.11.2 is the exact finite-base-change identity used above, and Proposition97.11.5 gives algebraic-space representability. Projectivity in this specific finite-separable case follows from the stated permutation-linearized ample bundle argument, rather than from a stronger property attributed to that proposition. The exact bibliography entry is now `frSNCRestrictionScalars` in `C3_SNC_nonzero_period_references.bib`.

C.3bt is now certified and its application makes the NP.1–NP.8 puncture quotient zero because the components are rational. The monodromy observation remains a valid explanation of why scalar Picard-span arguments cannot control arbitrary proper parameters; it is not a nonvanishing argument and does not count as a separate main-gate advance.
