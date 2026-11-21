# A-018. The additive Witt-series morphism is determined by line values

This closes the remaining uniqueness assertion on cote43/scan037, in the precise category written there: morphisms of affine group schemes over `Z`. Let `S∞=Spec Z[a₁,a₂,…]` represent the group `1+tA[[t]]` whose group operation is ordinary multiplication of series. Let `G=Spec B` be an affine group scheme, and let `f,g:S∞→G` be additive group-scheme morphisms agreeing on the map

`A¹→S∞`, `x↦1+xt`.

We prove `f=g` by their actual coordinate maps. For each `b∈B`, the difference `f*(b)−g*(b)` is a polynomial `P(a₁,…,a_N)` in finitely many coordinates. Over the polynomial ring `Z[x₁,…,x_N]`, form

`u(t)=∏_(j=1)^N(1+x_jt)`.

Additivity and agreement on lines give `f(u)=g(u)`. Thus

`P(e₁(x),…,e_N(x))=0`.

The map `Z[a₁,…,a_N]→Z[x₁,…,x_N]`, `a_j↦e_j(x)`, is injective. One elementary proof uses lexicographic leading terms: the leading monomial of `e₁^(r₁)…e_N^(r_N)` has exponent vector `(r₁+…+r_N,r₂+…+r_N,…,r_N)`. These vectors are distinct for distinct nonnegative tuples `(r₁,…,r_N)`, and each leading coefficient is one, so a nonzero integral polynomial cannot map to zero. Hence `P=0`. This holds for every `b`, proving equality of the scheme morphisms.

Apply this to the affine p-typical Witt group scheme `G=W_p`. The established big-to-p-typical ring morphism, in the source convention `α(f)=1/f(−t)`, sends `1+at` to the Teichmüller vector `(a,0,0,…)`. The preceding argument proves that these line values uniquely determine its additive scheme morphism, over every base characteristic. It uses finite dependence of a coordinate polynomial; it introduces no unsupported continuity assumption and does not identify arbitrary abstract homomorphisms of groups of series with scheme morphisms.

The full proof, including the coordinate variance, finite-variable reduction and leading-monomial injection, was checked in this run.
