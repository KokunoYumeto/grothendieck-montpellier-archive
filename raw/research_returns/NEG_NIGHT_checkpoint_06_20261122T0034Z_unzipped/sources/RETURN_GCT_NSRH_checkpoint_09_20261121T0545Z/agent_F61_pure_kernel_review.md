# Independent full review: F61 pure rank-three kernels

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited effort is not exposed. Date: 2026-11-21 UTC.

## Verdict and exact scope

**PASS. No mathematical correction required.** I read the entire final report and the entire 484-line generated fragment, and independently reconstructed the statements and proofs. This is a full mathematical and report-to-fragment check, including the new formal-bar section and the separate dictionary. It is not a fresh compilation or visual-layout check.

Exact targets:

- `agent_pure_rank3_kernel_lift.md`, SHA256 `f48551682261cf37efe0160e23fffd103245d013a079a1b1778d8694efd5816a`.
- `finding_F61.tex`, SHA256 `765a660843a8954a309b63291976b29fe96e80a99c0471ad44f0f5c1c63cc9f1`.

The proof constructs pure coefficient complexes and actual relation maps for the already specified rank-three kernel category. It does not claim a canonical realization of the source's designated bases, a single radius on total cohomology, or a categorical presentation with unspecified higher relations.

## 1. Full-Tate construction

For a formal degree e, E(-e)[-2e] has cohomology only in degree 2e with eigenvalue q^e and weight 2e. Its complex weight is zero. The multiplicity spaces have trivial Frobenius, so finite sums retain that weight and have the asserted positive Euler trace. Negative formal degrees merely give negative cohomological degrees and positive Tate twists; every individual object remains bounded.

I checked the tensorator on homogeneous elements. Tate twists and shifts both add exactly. Associativity preserves the ordered tensor, and every cohomological degree is even, so ordinary source symmetry agrees with derived symmetry. This proves symmetric strong monoidality on the entire coefficient category, with all grading shifts. Entrywise application to matrix kernels preserves the intermediate state and gives the stated strong monoidal, generally noncommutative convolution construction. No symmetry of the matrix-kernel category itself is incorrectly inferred.

## 2. Half-step construction and exact domain

The line L_e with eigenvalue lambda^e, lambda the fixed positive square root of q, has weight e at every complex embedding. These eigenvalues are ell-adic units. The closure of the cyclic group they generate is a profinite subgroup of the units of a finite ell-adic coefficient field, so the map from the integers extends continuously to the procyclic point Galois group. No geometric half-Tate motive is asserted.

For d_ab=t_b-t_a the summand L_e[-e+d_ab] has cohomological degree e-d_ab and complex weight d_ab. The parity condition e=d_ab modulo two is exactly what makes its Euler contribution positive. Necessity follows from the previously reviewed pure-point criterion; it is not a universal condition on unrelated categorizations.

The parity subcategory contains the unit and is closed under convolution because the potentials telescope. It contains even global shifts; an arbitrary odd shift is not claimed. The tensorator preserves the ordered path and uses the exact shift identity

(-e+d_ah)+(-f+d_hb)=-(e+f)+d_ab.

All resulting point cohomological degrees are even, so coefficient permutations carry no unaccounted Koszul signs. A closed path has weight zero. This is an actual functor on the stated subcategory, rather than a separate choice for each trace polynomial.

## 3. Actual states and maps

I checked the potentials on all block types: scalar states have potential zero; each N(delta) has (0,1); each N(D-2) has (0,0). Diagonal D degrees are even, A_1 off-diagonal degrees are odd, and A_2 off-diagonal degrees are even. Both named kernels therefore lie in the parity domain. The explicit two entries in the N(delta) example have shifts 0,-2 and 2,0, respectively, and weights -1,+1 as stated.

The quadratic reset-loop comparisons preserve chronological coefficient order. The potential contributions cancel on the extracted diagonal coefficients. For the degree-five map, I matched all four positions on each A_1 and A_2 block to their displayed targets; the A_2 second and fourth components use precisely the U/V flip needed to compare VU and UV. The plus and minus sectors are correctly treated. All scalar U,V,S,T degrees are even. The proof does not accidentally require the odd A_1 to be an allowed central half-step coefficient.

These maps are actual homogeneous linear isomorphisms before realization. A strong monoidal functor sends their inverses, compositions, tensor contexts and already specified comparison diagrams to the asserted chain maps. The text correctly refrains from declaring every possible rewrite loop to be the identity. Repeated multiplicity copies have identical potentials, so their matrix-unit compatibility is retained.

## 4. Formal bar

Full-Tate ordinary point duality sends E(-e)[-2e] to E(e)[2e], exactly the image of the formal graded dual.

In the half-step convention, dualizing L_e[-e+d_ab] gives L_-e[e-d_ab], whereas realization of the graded dual gives L_-e[e+d_ab]. The difference is exactly [2d_ab]. Thus the corrected entrywise bar is C_ab dual shifted by 2d_ab, without a state transpose.

I reconstructed its tensorator, rather than checking objects alone. Duality commutes with the finite intermediate-state direct sum; the potentials add; and the order-preserving product pairing is well defined because all relevant cohomological degrees and shifts are even. On a triple path both associativity routes are the same product of three pairings. Naturality is precomposition with the two original linear maps. The diagonal unit has zero potential.

Dualizing twice cancels the two shifts. The resulting double-dual identification is the ordinary coherent evaluation map, with its monoidal and involutive identities verified on pure tensors. A pure weight d_ab entry dualizes to weight -d_ab and the shift [2d_ab] restores weight d_ab. The bar stays in the specified split image.

The F56 self-dual forms and isometric permutation maps therefore transport exactly, so the named maps bar to their inverses under the chosen forms. Shifted contexts are replaced by their bars; the proof does not assert that all shifted objects are self-dual. This is entrywise formal duality, not a transpose-dual adjoint or a positive Hermitian form.

## 5. Derived Gaussian transport

I reread the exact F53 Gaussian-gauge, image-unit, commutor and weight passages. The product and its symmetry are the transported ones. In particular the existing minus sign between naive swapping and the correct Gaussian symmetry is retained.

For a split point complex, extending J term by term with the original shifts is the displayed derived formula. Expanding finite sums reduces every tensor comparison, associator and unit identity to the already proved F53 identity with a common total shift. In the present image, coefficient cohomological degrees are even, so the additional coefficient Koszul sign is one. This does not discard the separate Gaussian symmetry correction.

If the point coefficient in degree i has weight w+i, tensoring G dual gives lisse weight w+i-1; the shift [1] gives J(C_i) complex weight w+i; the subsequent shift [-i] gives weight w. This proves purity of the finite split sum. The compact Gaussian evaluation recovers the original point complex on this specified image. The text correctly distinguishes the resulting derived objects from the perverse heart and does not assert monoidality or t-exactness on all constructible complexes.

The transported formal bar is defined through the specified equivalence. It is not silently identified with literal Verdier duality on the line.

## 6. Source and scope audit

The original BBD text at 5.1.8, pp. 126-127, and 5.1.11, pp. 127-128, was reread in this review. The smooth/lisse qualification applies both to the point and to the explicitly lisse shifted Gaussian coefficients. The shift convention and geometric Frobenius convention match the formulas. The underlying integer-weight and compact-support source contexts were fully read in the preceding F57/F53 audits; this review does not claim a newly retrieved source.

The full-Tate D object has radii q^2,1,q^-2; the half-step D object has radii q,1,q^-1. They are pure of complex weight zero because their degree-i cohomology has weight i, not because their total cohomology has one radius. The word amplitude is allowed to grow. The pointwise/independent-dual estimates, canonical labels, global lattices, positivity polarization and completion/adjoint limitations remain explicit.

The rank-four F57 statement is restricted to extending this particular pure word-trace comparison through the actual extra block. At full Tate parameter all visible roots have even weights, so a single pure complex weight would force one Euler-coefficient sign. The mixed signs violate that condition. The statement is not a refutation of the source's signed/factored positivity or a mixed model.

The separate dictionary uses split-torus representations, symmetric coefficient lambda/sigma operations, perfect complexes and BBD weights in their legitimate scopes. It does not put a lambda-ring structure on the noncommutative word algebra, attribute the extra grading comparison to an archive manuscript, or turn the archive framework into a proof of this new construction.

## 7. Verification limits

No formal proof assistant, new numerical certificate or fresh syntax/visual compilation was used in this review. All 357 report lines and all 484 fragment lines were read. The fragment retains every construction, proof, bar correction, dictionary qualification and mathematical scope of the reviewed report; no additional unreviewed mathematical assertion was found.
