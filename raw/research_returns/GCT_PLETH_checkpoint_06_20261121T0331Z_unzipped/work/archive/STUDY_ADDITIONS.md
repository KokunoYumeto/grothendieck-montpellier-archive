# A-013. Exact checks of the supplied study's finite-set additions

The assertions below are reported by `SA17_STUDY_cote133_lambda.md` for cote133 scans20–27. Those scans were not part of the supplied transcription set. All public original PDFpages20–27 have now been retrieved and visually read. They confirm the injection/map-power definitions, the deleted coarse induction formula, the quotient-partition count, the representable/map-power definitions, the single-map-power summand assertion, and the distinguished-functor and eventual-equivalence definitions discussed below. These current inspections are recorded separately from the earlier supplied study.

## Injection powers and map powers

For a finite `G`-set `E`, let `τⁿ(E)=Mon([n],E)`, with `G` acting on the target and `S_n` acting by inverse precomposition. For `E⊔F`, the inverse image of `E` under an injection is a subset `A⊂[n]`. Fixing `|A|=i` and choosing the usual ordered representative gives the equivariant bijection

`Mon([n],E⊔F) ≅ ⊔_(i+j=n) Ind_(G×S_i×S_j)^(G×S_n)(Mon([i],E)×Mon([j],F))`.

Explicitly, a coset representative `σ` and the two injections produce the injection whose restrictions to `σ([i])` and its complement are those given injections transported by `σ⁻¹`. Changing `σ` within `S_i×S_j` is precisely the induction balancing relation. The inverse extracts the two restrictions. This proves multiplicativity of the total injection series in the induction product. Its degree-zero term is 1. The degree completion has inverses for every series with that constant term, so the universal group completion extends it to the Burnside group.

For `Tⁿ(E)=Hom([n],E)`, classify each map by the partition of `[n]` into its nonempty fibers. A type `α` has `α_j` blocks of size `j`, with `Σjα_j=n` and `k=Σα_j`. Fix one such partition and a quotient map `p_α:[n]→[k]`. Its stabilizer is

`W_α=∏_j(S_j wr S_(α_j))`,

and its action on blocks is the quotient `W_α→H_α=∏_j S_(α_j)⊂S_k`. The exact component of `Tⁿ(E)` is

`Ind_(W_α)^(S_n) Inf_(H_α)^(W_α) Res_(H_α)^(S_k) Mon([k],E)`.

The actual bijection sends `[σ,i]` to `i∘p_α∘σ⁻¹`; the stabilizer relation is exactly what makes it well-defined, and recovering the kernel partition and the injection on its quotient gives the inverse. The number of source partitions of this type is the index `n!/∏_j(α_j!(j!)^(α_j))`. This proves the study's corrected wreath-stabilizer formula. The deleted induction-from-`S_i` formula already fails for `n=2`: diagonal maps give a trivial `S_2` action, whereas induction from `S_1` gives a free two-point action.

## Representables, limits and composition

Let `FI` be the category of finite sets and injections, and let `h_I(E)=Mon(I,E)`. The category of elements of `h_I` has initial object `(I,id)`, so `h_I` is connected. Fiber partitions give a natural disjoint union

`Hom(J,E)=⊔_(π partition of J) Mon(J/π,E)`.

These are precisely its connected components. In particular, `h_I` is a direct summand of `Hom(I,-)`.

The statement equating **all finite sums of representables** with direct summands of **a single** `Hom(I,-)` is false. It appears in the original PDF page25/site24 itself: after the finite-sum definition, the manuscript says that these are direct summands of `H_I` for `I` of sufficiently large cardinality. The constant functor with two elements is `h_∅⊔h_∅`. At a singleton `E`, every `Hom(I,E)` is a singleton, so it cannot contain that two-element summand, for any `I`. The corrected equality uses finite sums of the `Hom(I,-)`: each representable is a summand of its own map-power functor, and every summand of a finite sum of map powers is a union of their connected representable components. This is a correction to the actual manuscript assertion as well as to the study's summary.

Finite sums of representables are closed under finite limits. The terminal object is `h_∅`. The product `h_I×h_J` is a finite disjoint union of representables, indexed by the equivalence relations on `I⊔J` whose restrictions to both summands are equality; each relation is the overlap pattern of two injections into `E`. Its quotient gives the corresponding representable. To check equalizers, restrict two natural maps to a source component `h_I`. Yoneda identifies each with a choice of target component `h_J` and an injection `J→I`. Different target components have empty equalizer. Within the same component, two distinct injections remain distinct after composition with every injection `I→E`, so their equalizer is empty; identical injections have the whole component as equalizer.

They are closed under composition as well. In `h_I(⊔_a h_(J_a)(E))`, first choose for each element of `I` the component `a` of its image. Then form the finite disjoint union of the corresponding sets `J_a`. The kernel partition of its combined map to `E` records every overlap. Admissible partitions restrict to equality on each `J_a` and make the resulting injections distinct whenever two selected components coincide. Each admissible partition gives exactly the representable of the quotient set. There are finitely many component choices and partitions. Outer finite coproducts preserve this decomposition.

The contracted-product description of the distinguished functors is exact: decompose a finite `S_n`-set `X_n` into its transitive orbits `S_n/H`, and

`Mon([n],E)×_(S_n)(S_n/H) ≅ Mon([n],E)/H`.

A formulation by a finite sum requires finite support in `n`. Arbitrary infinite sequences of finite `X_n` can still give finite values on each finite `E`, but are not all finite sums; the powerset functor is an immediate example.

## Eventual equivalences and injective transition maps

For composable natural transformations that are bijective on all sets beyond specified size thresholds, the set-theoretic two-out-of-three property applies beyond the maximum threshold. Pullbacks of set bijections are bijections, proving stability under base change. Pointwise coproducts and products preserve injective transition maps. Composition also preserves them: the inner functor sends each injection to an injection of finite sets, and the outer functor sends that injection to an injection.

All arguments above have been checked in full. Original PDFpages20–27 were visually inspected in the public-source follow-up. The numerical quotient-partition count is on originalPDFpage23, and the eventual-equivalence definition and its two properties are onPDFpage26; the ledger now uses those precise original page locators.
