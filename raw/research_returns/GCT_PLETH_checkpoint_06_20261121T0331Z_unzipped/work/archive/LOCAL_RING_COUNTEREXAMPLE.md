# A-023. A characteristic-zero local ring where the rho classes do not generate

Take the explicit commutative ring

`A=Z_(2)[ε]/(2ε, ε²)`.

As an abelian group it is `Z_(2)⊕F₂ε`, with product

`(a+bε)(c+dε)=ac+(ād+c̄b)ε`.

This proves that `ε≠0` and that `A` has characteristic zero. An element `a+bε` is a unit precisely when `a` is a unit of `Z_(2)`: its inverse is `a^(−1)−a^(−2)bε`. Hence `A` is local with maximal ideal `(2,ε)` and residue field `F₂`.

The coefficient ring also has `K₀(A)≅Z`, with the isomorphism given by rank. Indeed, for a finite projective module `P`, lift a basis of `P/(2,ε)P` to obtain a surjection `A^r→P` by Nakayama's lemma. It splits because `P` is projective. Its complementary finite projective module has zero residue quotient and is therefore zero by the same lemma. Thus every finite projective `A`-module is free, and rank identifies its Grothendieck group with `Z`. The example therefore also addresses the originalpage29 parenthetical question about coefficient rings with `K(k)≅Z`.

Let `G=S₂=C₂`, with generator `g`. The free rank-one `A`-module `L=Ae` with action

`g(e)=(1+ε)e`

is a representation, since `(1+ε)²=1`. Its determinant character sends `g` to `1+ε`.

For every `A[G]`-module `M` whose underlying `A`-module is finite free, the determinant of each group element defines a character `det(M):G→A×`. This gives a homomorphism

`det:K₀(L_A(G))→Hom(G,A×)`

from the exact Grothendieck group (written additively) to the character group (written multiplicatively). Indeed, every admissible exact sequence splits as a sequence of underlying `A`-modules. In an `A`-basis adapted to its submodule, a group element acts by a block upper triangular matrix. Its determinant is the product of the determinants on submodule and quotient. Thus the determinant respects precisely the exact relations defining this `K₀`.

In degree two, the monomials in the proposed generators are

`ρ₂=[A_trivial]`,

`ρ₁²=[Ind_{S₁×S₁}^{S₂}A]=[A[S₂]]`.

The corresponding determinant characters take `g` to `1` and `−1`, respectively: on the standard basis of the regular module, `g` interchanges two basis vectors. Consequently the determinant of every integer linear combination `aρ₂+bρ₁²` takes `g` to `(-1)^b`.

The character `1+ε` equals neither `1` nor `−1`. The first inequality follows from `ε≠0`. Reduction modulo `ε` maps the second proposed equality to `1=−1` in the characteristic-zero ring `Z_(2)`, which is false. Therefore

`[L] ∉ Zρ₂+Zρ₁²`.

The graded map `Z[ρ₁,ρ₂,…]→⊕_n K₀(L_A(S_n))` fails surjectivity already in degree two. This is an explicit counterexample even among characteristic-zero local rings. It is compatible with A-021: the ring `A` has the nonzero torsion element `ε` and is not a discrete valuation ring. The exact determinant map above is the witness for the failure; no distinction between two unnamed representation categories is being used.

The supplied study marks the classification of coefficient rings as open and its later annotation points to a characteristic-zero local counterexample in another record. That other record was not read here. The ring, representation, determinant map and non-generation proof above were constructed and checked directly in this run.
