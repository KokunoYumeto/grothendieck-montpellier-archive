# Independent whole-proof audit of SF-E829

**Outcome: PASS in the exact inherited finite-action scope. No repair requested.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited/unexposed effort, HODGE_DIVISION. The complete reviewed draft is `agents/sixfolds/rm_surface_support_wedge_gate_draft.md`, SHA-256 `4cab77bfcc30b75151e946b3a1da06e29e2461ce59f8787c326c9aa5ab666b28`. This report follows a complete reading of all sections, a fresh reading of the actual E827 diagonal argument, and an independently written exterior-algebra certificate. Record time is in CHECK_EVENTS.tsv; no estimated future interval is used.

## Exact result and boundary

The theorem gives an Ext bound for an actual coherent extension with actual preserved blocks, under the translation/tensor action specified in E827. It does not cover arbitrary automorphisms acting nontrivially on `H²(O_X)`. It allows all line differences of Hermitian rank at least two and the acyclic rank-one differences. For the exceptional surface-index-one directions, it forms their support-line span `Z` in `Lambda² H¹(O_X)` and obtains a surviving space of dimension

`w = 6 − dim Z − dim rad(q_wedge|Z)`.

The exact conclusion is `ext²_Γ(E,E) ≥ w(u+|J|)`. The balanced-character weak-semiregularity consequence retains the previously audited supplied invariant-compatibility premise. Nonacyclic elliptic directions are deliberately outside this theorem, and the draft proves why the whole-Ext diagonal method may yield no class there. No existence or nonexistence outside this architecture is inferred.

## Rational Riemann-form complement

I independently checked the tangent-space construction. Relative to the nondegenerate polarization form, the integral numerical form of `N` defines a rational operator `T`. Type `(1,1)` makes it commute with the complex structure; alternation makes it self-adjoint for the positive polarization Hermitian form. Thus it is diagonalizable with real eigenvalues, and its kernel and image are complementary rational complex subspaces, orthogonal for the polarization.

Their intersections with the original lattice are full lattices in those subspaces. They therefore define compact complex subtori, and the restricted positive polarization makes them abelian subvarieties. The sum map has an invertible differential and finite lattice index, so it is an isogeny. This argument uses rational numerical forms. It does not treat an irrational RM eigenspace as an abelian subvariety.

The numerical form of `N` is nondegenerate on the image factor, zero on the kernel factor, and zero on the mixed terms. Subtracting the line restricted to the image leaves a topologically trivial line. A flat character of a product lattice splits into its two factor characters, so the asserted external tensor-product decomposition holds for actual line bundles, with the possible flat image factor absorbed into `N_C`.

The natural pullback on `H¹(O)` is an isomorphism. Pullback of line cohomology is injective because normalized finite étale trace splits it; products commute with pullback. Therefore product containments and multiplication vanishings proved on the product descend. No surjectivity on line cohomology is assumed. In particular an acyclic original line whose pullback happens to have cohomology can only make the chosen support span conservative.

## All rank and index cases

The nondegenerate factor has cohomology in exactly its index, with inverse index `r−j`. I checked every possible `r=2,3,4` and `j=0,…,r`, including the kernel-factor contribution when `j=0`.

- For rank four, both degree-one directions cannot coexist; any possible degree-one group has zero degree-three target.
- For rank three, the one-dimensional kernel has no second exterior power, and the inverse indices cannot both be at most one. Both the multiplication and diagonal-product conclusions follow.
- For rank two with index zero or two, the only possible degree-one group is `H⁰(N_C) tensor H¹(O_K)`, and a kernel two-form would land in its zero third exterior power. All other two-form components raise the nondegenerate-factor index and vanish.
- For rank two with index one, both degree-one groups are supported entirely on the surface factor. Their diagonal products lie in its one-dimensional `Lambda² H¹(O_C)`. Multiplication to degree three depends only on the kernel two-form component. Its vanishing is exactly orthogonality to that surface support line under the four-dimensional wedge pairing.

This is exhaustive in the stated rank range. It does not use a generic-position assumption or numerical nondegeneracy on the original fourfold.

## Wedge linear algebra and actual invariant Ext argument

The wedge form on the six-dimensional second exterior power is nondegenerate and symmetric. Its annihilator has dimension `6−dim Z`; its intersection with `Z` is exactly the radical of the restricted form. A complement to that intersection therefore has the stated dimension and is disjoint from all incoming diagonal products. Enlarging `Z` by conservative extra support lines cannot strengthen the resulting bound; it only shrinks the allowable complement.

I reread both actual E827 long exact sequence maps. The A-diagonal classes inject because all preceding diagonal coefficients lie in `Z`, and their next boundary vanishes by the multiplication annihilator. The selected B-diagonal identities lift; normalized diagonal trace modulo `Z` detects them after the preceding boundary. The additional unit-block term vanishes by the stated `Ext³(M_b,A0)` condition and Serre duality. These two contributions lie in image and kernel of the same actual map and therefore add. No spectral-sequence degeneration or formality is used.

The inherited translation/tensor functors act trivially on `H²(O_X)`, so every chosen subspace is invariant. Identity matrices and normalized trace are invariant under the multiplicity action, including projective descriptions. Exact finite invariants and averaging give the required invariant lifts.

## Examples and method limitation

I checked the single-line, complementary-line and intersecting-line examples. A decomposable two-vector squares to zero; two complementary surface planes pair nontrivially; two intersecting planes have zero mutual wedge. Their surviving dimensions are respectively `4,4,2`, with the zero-support case giving `6`.

For the nonacyclic elliptic example, elliptic Serre duality makes the diagonal product span all of `V_C wedge V_K`. Killing the inverse degree-one group forces the two-form into that same three-space. Hence no nonzero common annihilator complement disjoint from the product span can be extracted. This is a genuine limitation of this diagonal extraction, not a semiregularity conclusion.

## Sources and exact arithmetic

The nondegenerate line index/Riemann–Roch input remains Mumford, *Abelian Varieties* (1970), §16, printed pp.150–153. I freshly reread those retained original-page statements and calculations, and visually reread the full Hermitian-index corollary and proof on pp.162–163. The previously completed full source checks in E826 remain recorded separately. The Pic⁰ vanishing also has the complete direct unitary-flat proof in the draft. Künneth, finite trace, and the rational complement are used exactly as written. The full supplied S21 and published BF statuses remain unchanged.

`audit_surface_elliptic_gates.py/.json` is an independently written exact exterior calculation shared with the E830 audit. The actual run passed in `0.03255264600011287` seconds. It verifies the full wedge matrix, all twelve rank/index cases, the support/radical examples, and the additional entry-specific elliptic/trivial-line cases used by E830. It computes no isogeny, equivariant object, or gluing theorem; those are covered by the whole written proof review. No author arithmetic program was imported.
