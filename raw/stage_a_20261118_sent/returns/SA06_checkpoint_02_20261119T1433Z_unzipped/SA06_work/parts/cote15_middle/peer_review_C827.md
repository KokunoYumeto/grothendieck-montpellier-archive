# Independent check of C-SA06-827

Checked on 19 November 2026 by GPT-6 Astra Pro, effort inherited/not exposed, run SA06-part2/cote15_middle. This is a review of the root package’s claim, not a new claim assigned to the present part.

## Verdict

The cubic-period argument is valid, including its extension to a smooth projective variety over the real numbers. The real-base argument must retain the projection onto one complex factor: the paired rational kernel has even dimension, so its total dimension alone is not a contradiction.

## Exact complex example

Let τ be the root of T³−2 in the upper half-plane and let E=C/(Z+τZ). The lattice has rank two over Z and E is an elliptic curve. The polynomial is irreducible by Eisenstein at2, so 1,τ,τ² are Q-linearly independent and τ³=2. Set V=H¹(E,Q)⊗³, a rational Hodge direct summand of H³(E³,Q) of dimension8.

Choose a rational basis of H¹(E,Q) so that its projection to H^{0,1}(E) has coefficients proportional to1 andτ. The projection V→V^{0,3} then has coefficients proportional to the eight products τ^{e1+e2+e3}, with e_j∈{0,1}. Its Q-image is the three-dimensional span of1,τ,τ², hence its rational kernel K has dimension5. The saved script computes the exact 3-by-8 matrix after reducing powers modulo T³−2 and returns five independent rational kernel vectors.

For a rational vector, vanishing of the (0,3) component implies vanishing of its complex-conjugate (3,0) component. Thus K is exactly the rational intersection with the level-one space V^{2,1}⊕V^{1,2}; equivalently K=V_Q∩F¹V_C∩overline(F¹V_C). If K were a rational sub-Hodge structure, its Hodge summands would occur in distinct conjugate pairs, since the total weight3 is odd. Its rational dimension would therefore be even, contradicting dim_Q K=5.

## Real-base extension

Take X=Res_{C/R}(E³), a real abelian variety, hence smooth and projective. Its complexification is E³×overline(E)³. The two pullbacks of the tensor H¹-parts give a rational Hodge direct summand W=V⊕overline(V) of H³(X_C,Q). The topological real Frobenius f∞ exchanges these summands and reverses their Hodge types. In particular W is f∞-stable and f∞F¹W_C=overline(F¹W_C).

The naive rational intersection on W is K⊕overline(K), of dimension10. Suppose the naive intersection on all H³(X_C,Q) were a rational sub-Hodge structure. Its intersection with the rational Hodge substructure W would then be a sub-Hodge structure, and projection along the Hodge direct sum W→V would make K a sub-Hodge structure. The preceding odd-dimension contradiction applies. This proves the real-base failure without claiming that projection onto V is itself defined over R or that V alone is f∞-stable; neither assertion is needed.

The filtration notation on manuscript scan205 remains diplomatic. This example refutes its broad rational-intersection interpretation once the displayed level is identified with the usual level-one Hodge condition. The correct candidate is the largest rational sub-Hodge structure contained in that intersection. Equality of this candidate with coniveau remains the generalized Hodge conjecture; this argument does not disprove the usual rational Hodge conjecture or prove the corrected general one.

## Primary comparison and source check

Grothendieck, A. (1969). Hodge’s general conjecture is false for trivial reasons. *Topology, 8*, 299–303. https://doi.org/10.1016/0040-9383(69)90016-0. The paper was received27October1968. Its §1, pp299–300 gives the cubic elliptic-period obstruction, and §2, pp300–301 states the corrected sub-Hodge-structure formulation and the motivic-effectivity interpretation. I opened the primary PDF at https://matematicas.unex.es/~navarro/res/articles/Hodge%27s%20Conjecture%20is%20False.pdf (search_036; reference turn739108580view0). The real restriction-of-scalars step above is this run’s independent reconstruction, not a claim that it is written in that paper.
