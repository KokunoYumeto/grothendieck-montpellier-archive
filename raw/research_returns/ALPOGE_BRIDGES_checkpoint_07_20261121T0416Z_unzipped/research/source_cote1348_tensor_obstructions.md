# Direct tensor repairs of the additive counterexample

## Exact results

The companion TeX gives complete proofs of **F-SM36** and **F-SM37**. These are failed-route obstructions, not a counterexample to the full original symmetric-tensor hypotheses.

**F-SM36.** For `E(V)=V**/V`, no natural normalized map `E(V tensor W) -> E(V) tensor W` exists. A functional on a product of copies of `V*` can have a prescribed nonzero quotient class in every coordinate. Naturality would send that element to an ordinary algebraic tensor with infinitely many nonzero coordinates, which is impossible. Testing the actual projective object `P1(V)=(E(V),V,0,id)` consequently rules out *any* unital bifunctor on F-SM34's category whose tensor with a scalar object has the ordinary componentwise vector-space tensor, compatibly with the unit. A different tensor may enlarge the components.

**F-SM37.** F-SM34's category is the algebra category of the square-zero monad `T=id+H` on arrows, where `H(C0 -> C1)=(E(coker b) -> 0)`. For the usual truncated cochain tensor, T has no natural unital tensorial strength. The complete contradiction uses `S=(0 -> V)`, `D(V)=(V -> V)`, and `D(k)`: unit naturality forces the strength on the degree-zero `E(V)` to be the identity, while naturality for `S -> D(V)` forces that same map to be zero. Thus a commutative-strong-monad tensor on this particular base cannot be invoked to supply the missing tensor.

## Approaches considered but not proved

- The two scalar adjoints and exactness of κ imply that the canonical underived counit φκ is the identity on all scalar modules once it is so on the scalar ring: use free presentations and right exactness. Thus κ is a fully faithful bireflective scalar embedding. The counterexample defect is higher derived normalization, not underived scalar normalization.
- A square-zero commutative strong monad on vector spaces can have a simpler tensor, but its unit is a free object. That does not preserve the required scalar embedding and normalization in the attempted construction.
- A variant using an exact shifted functor on connective cochain complexes was tested, but it did not retain the scalar obstruction. No counterexample or general tensor theorem from that variant is used in this module.
- Contramodules over a completed Hopf algebra remain a possible different construction. Neither their symmetric tensor with trivial-module unit nor the necessary failure on infinite scalar modules has been established here. The ordinary `k[[t]]` model fails finite-unit acyclicity. A topological idempotent augmentation ideal is only a proposed direction, not a proved example.

## Bounded primary-source inspection

Johnston, D. (2026). Contramodules for algebraic groups: The existence of mock projectives. *Canadian Mathematical Bulletin, 69*(1), 184–200. https://doi.org/10.4153/S0008439525100933 . Published online August 4, 2025.

Section 2.3 explicitly supplies a `Hom_k` action with a comodule and a contramodule, not an automatic tensor of two contramodules. Only this exact source point was checked; no nonexistence theorem for all completed Hopf constructions is inferred. Primary page: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/contramodules-for-algebraic-groups-the-existence-of-mock-projectives/1E4EC0C42A966CA97ACB559E0A090525 . Web refs: `turn775953858view0`, `turn870082128view0`.

## Remaining original gate

The original abstract row is still not decided by F-SM34. A full counterexample must construct a symmetric bilinear tensor, identify κ(k) as its unit with the stipulated scalar compatibility, and supply the monic interval. A positive closure must derive the missing countable realization / free-scalar normalization conditions from those exact original hypotheses. F-SM36–37 narrow two specific construction routes without replacing either requirement.
