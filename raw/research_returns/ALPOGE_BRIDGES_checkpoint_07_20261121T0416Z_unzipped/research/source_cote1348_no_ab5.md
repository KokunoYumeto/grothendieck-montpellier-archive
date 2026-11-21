# F-SM-31: the original interval hypotheses do not imply AB5

**Model:** GPT-6 Astra Pro. **Effort:** not exposed. **Run:** /root/source_and_masullo. **Date:** 2026-11-21 UTC.

The complete proof is in source_cote1348_no_ab5.tex.

## Exact outcome

The original adjoints, enough projectives, canonical unit normalization, symmetric monoidal coherence, and full tensor interval do **not** force either AB5 or local presentability. This remains false even when the tensor is exact and preserves arbitrary colimits in each variable, and the category has a projective generator.

The example is M=Ch≥0(k) × Vect(k)^op for any field k. Write objects as (C,A). Define

\[
(C,A)\boxtimes(D,B)=\left(C\otimes D,\operatorname{Hom}_k(C_0,B)\oplus\operatorname{Hom}_k(D_0,A)\right).
\]

The second coordinate is interpreted in the opposite category. Its m-fold normal form has one summand for each chosen opposite-vector factor A_i, namely Hom(⊗_{j≠i}(C_j)_0,A_i). Currying and permutations of these labelled summands prove the pentagon, triangles and hexagons. The proof specifies tensor maps, rather than giving only an object formula.

The unit is (k[0],0), κU=(U[0],0), φ(C,A)=H0(C), and the right adjoint of κ is C0. The actual derived functor is F(C,A)=C. The interval J=(D1(k),0) acts as J⊠(C,A)=(D1(k)⊗C,A); its tensor inclusion has identity second coordinate and the usual chain inclusion in the first. The displayed signed contraction proves F(J⊠X)=0 in **all** degrees.

AB5 fails through the explicit inverse system of tail subspaces V_S⊂k^(N): inverse limits turn its quotient sequence into the nonsurjection k^(N)→k^N. To rule out local presentability at every rank, use all subsets S⊂λ of size <λ. Their tail subspaces have inverse limit zero, but a map sending every basis vector to one chosen nonzero a∈A survives all restrictions. Thus no nonzero object of Vect(k)^op is λ-presentable. A λ-presentable object of M must have zero second coordinate, and such objects cannot generate (0,k) by filtered colimits.

## Scope that must be retained

This **does not refute the original localization theorem**. In the example the projection to Ch≥0(k) and the section C↦(C,0) give the claimed localization equivalence immediately, because the natural projection (C,A)→(C,0) is always a weak equivalence. The example instead closes the proposed route of deducing the extra Grothendieck hypothesis in F-SM-30 from the original predicates.

## Other attempted route, not promoted

The supplied three-sort E(V)=V**/V model has a reconstructible additive core. Its objects have maps a:E(X2)→X0, b:X0→X1, c:X1→X2 with ba=cb=aE(c)=0. The free projectives give a periodic resolution with L_{3n}φ(κV)=E^n(V). This diagnoses failure of normalization for infinite scalar modules and failure of exact coproducts. However, this alone is not a full interval counterexample. The symmetric tensor and its full monic interval have not been reconstructed. A naïve truncated-chain tensor would make the relevant top-degree tensor square zero, preventing the required monomorphism after tensoring. No assertion that the absent original coherence certificate was checked is made.

## Verification

The entire saved F-SM-31 proof was read by the author. Mathematical checks included the opposite-variance tensor maps, scalar copowers, finite currying normal form for all coherence diagrams, exactness and arbitrary-coproduct preservation of tensor, both adjoints, the derived-functor identification, the signed contraction including degree zero, the AB5 witness, and the every-regular-cardinal presentability obstruction. Small TeX delimiter and text typos were corrected; all additions were checked in context. The result is an author complete-proof reading, not an independent reproof. Parent independent reading was requested separately.

Primary historical source: Grothendieck, A. (n.d.). *Pursuing stacks: Linearization of homotopy types*, cote134-8, manuscript footers47–48. https://grothendieck.umontpellier.fr/134-8.pdf . The mathematical construction is proved completely here and only invokes the already proved internal lemmas BR-13401/02.
