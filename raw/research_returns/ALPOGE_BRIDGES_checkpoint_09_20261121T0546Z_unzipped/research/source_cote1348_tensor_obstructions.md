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

## Two further repairs tested, 2026-11-21

**Adding a third sort to the standard truncated tensor does not repair its functoriality.** The supplied intake describes `H(U0,U1,U2)=(E(U2),U0,U1)` and refers to `C.tex:1092` and an unrun coherence script; neither underlying file is present in the supplied archive. For the associated radical-square-zero category the free projectives are `P0(V)=(V,V,0)`, `P1(V)=(0,V,V)`, and `P2(V)=(EV,0,V)`. The ordinary truncated-cochain rules would give `P0(V) tensor P0(k)=P0(V) plus P1(V)`, `P2(W) tensor P0(k)=P2(W)`, and `P1(W) tensor P0(k)=P1(W) plus P2(W)`. Choose a nonzero ghost `a:P0(k)->P2(W)` coming from `k->EW`, and let `b:P2(W)->P1(W)` be the identity on the last component. Although `ba=0`, the proposed standard rules tensor these to `row(a,0)` followed by `column(b,±id)`, whose second component is `±a`, not zero. This excludes those specific standard rules, without certifying or refuting the unavailable intake construction.

**The one-sort commutative square-zero monad loses the required scalar embedding.** For any exact linear functor E on vector spaces, the monad `T=Id+E`, with the composite `E²` sent to zero, has the usual forward strengths and a commutative square-zero multiplication. Its algebras are `(V,a:EV->V)` with `a E(a)=0`. If E kills finite-dimensional spaces, then `κ(k)=(k,0)=T(k)` is free. If the trivial-algebra embedding κ had a right adjoint, it would preserve coproducts; thus its value on a free vector space V would have to be the free algebra T(V). This fails whenever EV is nonzero, so the two required scalar adjoints already fail.

There is also a direct scalar tensor obstruction. The usual algebra tensor of trivial algebras has underlying vector space `(V tensor W) plus E(V tensor W)/R`, where R is the sum of the images of `EV tensor W` and `V tensor EW` under the forward strengths; its action on this quotient is the quotient map, and is nonzero when that quotient is nonzero. For W=V with EV nonzero, choose a basis `(v_i)`, put `delta(v_i)=v_i tensor v_i`, and let `m(v_i tensor v_j)` be `v_i` if i=j and zero otherwise. Then `m delta=id`. Every fixed-vector contraction `m(- tensor v)` or `m(v tensor -)` has finite-dimensional image, so E(m) kills R. But `E(m) E(delta)=id_EV`; therefore `E(V tensor V)/R` is nonzero. The tensor is consequently not `κ(V tensor V)`. This failure concerns this explicit one-sort repair; no claim about all possible monoidal realizations follows.

The positive direction still requires a proof of all-free scalar derived normalization or the requisite derived coproduct comparisons from the original finite-additivity, scalar compatibility and interval assumptions. Exactness of tensoring by a scalar free object, closedness of the tensor, and AB4 have not been inserted as implicit assumptions.

**Current refinement (F-SM43–44, author and root complete-reading PASS):** automatic AB4 is now ruled out even with a closed tensor and a flat interval/quotient, while that example still has the desired localization. The canonical derived coproduct maps are automatically injective on every homology group and bijective in degrees zero and one. Only extra homology in degrees at least two remains to be ruled out; it is detected exactly by higher Ext classes against κ of an injective scalar cogenerator that vanish on each individual summand. Canonical scalar normalization already holds in degrees zero and one for every scalar module over arbitrary k. No full original counterexample or general higher-kernel vanishing theorem has been obtained.
