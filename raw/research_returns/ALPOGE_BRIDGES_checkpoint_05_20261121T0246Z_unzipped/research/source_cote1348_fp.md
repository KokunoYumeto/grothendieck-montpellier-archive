# Cote 134-8: the finite-flat-dimension obstruction and a further arbitrary-ring theorem

**Run:** /root/source_and_masullo  
**Model:** GPT-6 Astra Pro  
**Effort:** not exposed  
**Complete draft check:** 2026-11-21 01:06:27 UTC  
**Proof module:** source_cote1348_fp.tex

## F-SM-26: the interval excludes finite flat dimension of D

The full original interval hypothesis is stronger than the positive-degree version: its middle object has zero derived image in every degree, including degree zero. Its monomorphism therefore gives a short exact sequence whose cokernel realizes the homological suspension under Lφ. Iterating the cokernel on the normalized unit T produces objects S^nT with Lφ(S^nT)=k[n].

For nonzero k this forces Tor_n^R(D,S^nT)=k for every n. Thus D has infinite flat and projective dimension. Adding a finite flat-dimension assumption on D would eliminate every nonzero example satisfying the actual normalization and interval. This is a complete short proof, not an unsuccessful estimate or a speculative obstruction.

## F-SM-27: arbitrary scalar ring, provided D is of type FP-infinity

The new positive result retains the ringoid construction of BR-13405 and the scalar compatibility made explicit in F-SM-24. It assumes that D has a resolution A by finitely generated projective left R-modules in every degree. The resolution may have infinite length. This finiteness condition on D is additional; finitely presented projective generators for the ambient module category do not supply it.

Under this assumption, the exact original connective adjunction induces the desired equivalence for **any commutative scalar ring k**, with arbitrary projective (possibly infinitely generated) scalar morphism modules R(x,y). In fact Lφ annihilates every product of coinduced modules C_x(U), with no projectivity restriction on the scalar coefficients U.

The proof has four substantive parts:

1. The interval inclusions are objectwise scalar-pure. Coinduction of a scalar pure-injective module is injective relative to these inclusions, so it splits off its interval object and has zero derived image.
2. Finite-projective duality identifies A⊗_R C_x(U) with Hom_k(K_x,U), where K_x=Hom_R(A,R(x,-)). The scalar terms of K_x are projective. Testing against every pure-injective U proves that K_x is pure-acyclic; the proof spells out why exactness of the transpose complexes extends maps from each cycle module, and why character modules detect purity.
3. The cycle modules of K_x are flat. Summing their short exact sequences gives a projective periodic presentation of their direct sum. The precise known Benson–Goodearl theorem makes that sum projective, so each cycle is projective and K_x is contractible. This is a genuine pure-acyclic argument and does not assume that an arbitrary bounded-below cochain complex of projectives splits.
4. Finite projectivity of every A_n makes its tensor functor commute with products. Thus products of the coinduced modules remain acyclic. The right adjoint from the originally specified, possibly infinitely generated resolution B sends every acyclic projective chain object to just such a product. BR-13403 and F-SM-17 give the equivalence; the canonical normalization is used at that last step for the degree-zero projective summands.

## Exact primary input and source-check scope

Benson, D. J., & Goodearl, K. R. (2000). Periodic flat modules, and flat modules for finite groups. *Pacific Journal of Mathematics, 196*(1), 45–67. https://doi.org/10.2140/pjm.2000.196.45

- Exact theorem: **Theorem 2.5, p. 50**; also **Theorem 1.1, p. 46**.
- The theorem applies to arbitrary rings: a flat module with a projective periodic short exact presentation is projective.
- Primary publisher PDF: https://msp.org/pjm/2000/196-1/pjm-v196-n1-p03-s.pdf
- Retrieved primary refs: turn189471893search8 and turn773425813view0.
- The exact theorem and its arbitrary-ring hypotheses were checked directly. The external theorem's full proof is cited as a known input; it is not claimed as independently re-proved. The periodic-sum deduction needed here is proved completely in our module.
- No reliance on a search snippet alone, on an unpublished outline, or on ordinary acyclic-projective splitting.

## What remains unresolved

The extra FP-infinity hypothesis is used twice: to identify the coinduced tensor complex with an ordinary dual complex, and to commute its computation with arbitrary products. These two operations are not justified for unrestricted infinite coproducts of representables.

A naive reduction to countable scalar subrings does not yet fix this. The outer tensor expression for a Tor element has finite support, but its coefficients in GP are maps on complete modules B_n(y). A boundary obtained over a smaller ringoid can require compatible extension of these maps to all of B_n(y). That extension is an additional global linear problem. We have not proved it, and no descent conclusion is asserted.

The general case without a finite pure-injective dimension bound, without finite generation of the scalar morphism modules, and without FP-infinity for D remains the exact acyclic-projective counit test. No counterexample satisfying all the full interval and canonical normalization assumptions has been found.

## Verification

Both complete proofs were reread from the saved TeX, including every displayed map and degree convention. Checked especially the nonzero-k qualification, shift direction, coinduction variance, character-module purity test, unbounded-right cochain contractibility via the actual periodicity theorem, finite-projective evaluation duality, product exactness, and the distinction between the auxiliary finite resolution A and the originally specified resolution B. Self-check outcome: pass. Independent parent check was requested separately and must not be inferred from this self-check.

