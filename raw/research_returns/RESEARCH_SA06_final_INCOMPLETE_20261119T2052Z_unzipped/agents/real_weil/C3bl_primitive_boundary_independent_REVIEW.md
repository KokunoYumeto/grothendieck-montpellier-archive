# Independent complete audit of the primitive exceptional-boundary proposition

**Verdict: PASS**, including m=0, for the exact geometric hypotheses stated in PB.1–PB.2. This is an auxiliary theorem; it does not itself construct an ordinary family or a principal target. Completed 2026-11-19T15:19:15.098348+00:00. Final integral-quotient file SHA256 f1e3cfd593ebf66c011069729d9f7cb523bf9cc6cd56ed458789a69c8a5d6cf2.

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not separately exposed.

I read the complete original five-step Witt proof, independently rederived all steps, then read the entire replacement Step3 and the complete diff to the final `agents/frobenius/C3_primitive_exceptional_boundary.tex`. The only substantive replacement is the simpler free integral quotient in Step3. Both arguments pass; only the quotient proof is required by the final proposition.

## 1. Relative uniqueness and whole exceptional kernel

The canonical ordinary Milnor kernel is p-annihilated in every degree and every characteristic, including two. The all-degree Rost induction proves exactly the preceding H^(n−1)(V,K_n^M) divisible. Hence the relative H^n injects and identifies with the kernel of reduction. This supplies genuine unique relative lifts; it is not a Milnor–Quillen comparison on the nonreduced scheme.

I independently checked the elementary positive-adjoint proof on the integral cubic/projective Chow lattice after tensoring with the reals. On the cubic chain 1,A,3z, norms1,2,4 and lowering coefficients2,2 give commutator weights−2,0,2. Primitive divisors have weightzero. Tensoring gives ||Ev||²=||Fv||²−w||v||². It proves b and b² injective in the required degree; at weight−2, applying the identity to Ev and then adjointness proves the endpoint. This is an arithmetic calculation on an explicit free lattice and does not invoke a characteristic-zero geometric Lefschetz theorem.

For gamma=alpha+v[o]+eta, the free equations b alpha=0 and e alpha+bv=0 imply b²v=0, then v=alpha=0. Thus the exact residual kernel is the Smith kernel on B_(s−1) tensor Pic⁰(C). The Q_j in PB.9 are actual torsion line bundles with d_j Q_j=0; no Smith factor is made invertible modulo p.

## 2. Final integral saturation proof

The multigraded component (projective degree0; all cubic degrees1) is the tensor product of the cubic Picard lattices. Every anticanonical A_i is primitive, since it pairs to one with a line. Thus the quotient Λ=⊗(Pic(W_i)/Z A_i) is free over Z.

The map Ψ to this quotient annihilates bB_(s−1) term by term. The h-term has wrong multidegree; every other contributing term inserts A_i in a missing cubic factor. The coherent map Φ_k factors through Ψ because multiplication by dlog A_i factors through H¹(Ω¹_P3(1)|Wi)=0, as follows directly from the restricted Euler sequence and cubic cohomology. Therefore d_j Ψ(w_j)=0 implies Ψ(w_j)=0 in a free integral group before reduction to k. This handles every p-divisible Smith factor and all m≥0.

The earlier Witt proof also checks: H²(O_W)=0 lifts the Picard basis; formal existence algebraizes it; Euler and conormal sequences identify the designated twisted cotangent group with the free rank-four H³(P³_W(k),O(−5)); its base change is exact. The free target kills integer torsion before reduction. This remains a retained alternate, not a required final input.

## 3. Actual lifts and the crucial divisible map

H²(V,L^n)=0 gives all individual curve line-bundle lifts. Formal existence over the complete local base, regularity of the excellent completion, finite-data Popescu descent including the inverse, and smooth henselian lifting matching m² give actual bundles on Z. The argument does not assume a universal family over Pic⁰(C).

The canonical K-tilde=O_Z(−V) tensor q*L_T^(−1) restricts to K_C. The product K-tilde·Q-tilde reduces to zero because it comes from two divisor classes on the curve. Its relative H² lift is unique. Changing Q-tilde changes its differential by a' cup dlog K_C; a' has curve cohomological degreeone, so this cup has curve degree two and is zero. Therefore F(Q) is independent of the chosen actual lift. Tensoring lifts makes F additive. Pic⁰(C)(k) is divisible whereas the target is a characteristic-p vector space; hence F=0. This assertion concerns the differential image, not the relative class itself.

## 4. Actual Chow identity and final contradiction

The identity PB.18 follows literally from Chow projection formula and O_Z(V)=q*L_T^(−1) tensor K-tilde^(−1). The Smith relation bv_j=d_jw_j is pulled back as an integral polynomial in actual divisor classes. No rational division occurs.

For the first summands, the nil first jet of Q-tilde^d_j is in H⁰(T,L_T) tensor H¹(C,K_C). Its projected cup vanishes by Ψ(w_j)=0. For the second, the unique relative K-tilde·Q-tilde differential is F(Q_j)=0, and the relative symbol product identity gives the higher vanishing. All terms individually reduce to zero; relative uniqueness makes their sum the correct invariant of the actual Chow sum.

A hypothetical Chow identity descends, with its finitely many rational-equivalence witnesses and line bundles, to one pointed étale finite-type model. Properness permits shrinking to a regular source, hence smooth over the perfect coefficient field, while retaining the identical m² fibre. Integral Bloch and the full product comparison apply there, not on E. Restriction to E and unique relative lifting contradict the nonzero designated component. No unproved formal Chow algebraization or unbounded torsion argument is used.

## 5. Exact primary sources freshly inspected

Fresh complete primary statements/proofs read in this review:

* Stacks37.4.1 Tag0C6R: square-zero Picard obstruction exact sequence, https://stacks.math.columbia.edu/tag/0C6R ; retrieval turn977473220view0.
* Stacks30.24.3 Tag0885: projective formal existence over a Noetherian complete ring, https://stacks.math.columbia.edu/tag/0885 ; turn977473220view1.
* Stacks30.8.1–30.8.2 Tag01XS: explicit projective-space cohomology and base change, including the full Cech proof and multiplication compatibility, https://stacks.math.columbia.edu/tag/01XS ; turn977473220view2. This verifies both the final Euler argument and the retained alternate Witt calculation.
* Stacks15.51.14 Tag0AH2: regularity of completion for G-rings, https://stacks.math.columbia.edu/tag/0AH2 ; turn842242711view0.
* Stacks16.12.1 Tag07GC: Popescu filtered smooth presentation, https://stacks.math.columbia.edu/tag/07GC ; turn842242711view1.
* Stacks32.10.3(2) Tag0B8W: invertible-sheaf descent with inverse and isomorphism, https://stacks.math.columbia.edu/tag/0B8W ; turn842242711view2.
* Stacks15.13.3 Tag0H74: smooth henselian lifting preserving the quotient map, https://stacks.math.columbia.edu/tag/0H74 ; turn842242711view3.

Jiang's exact integral product blow-up maps and Stacks02TX were freshly read immediately earlier for C.3bk; Rost/Kerz/Braunling were freshly read and fully scoped in the preceding independent relative/cohomological audits. No independent re-proof of those cited literature theorems is claimed. No finite computation or build was independently rerun for this audit.
