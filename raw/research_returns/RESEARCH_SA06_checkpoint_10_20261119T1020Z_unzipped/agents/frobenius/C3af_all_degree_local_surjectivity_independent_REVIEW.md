# Independent complete-proof audit: C.3af

**Outcome: passed for the full-basis draft read at 09:03–09:04 UTC, 2026-11-19.** File audited: `research/agents/cycles/all_degree_local_surjectivity.tex`. This review covers the threshold N≥3·4^(r−1)+2r−1. A later proposed sharper coefficient construction is not included in this certification.

The construction has q=3·4^(r−1) explicit basis sections with coefficients0/1. Their basepoint freeness follows at every point by choosing one nonzero coordinate in each factor. The dimension count m=N−2r≥q−1 gives a rank-m incidence projective bundle whose first relation is above codimensionr. The projective-bundle evaluation h→−a therefore provides the stated exact Chow quotient, independently of any Hodge calculation.

The conormal exterior sequence has kernel L tensor Ω^(r−1). The Chern character of an actual virtual-bundle lift of the closure supplies the vanishing under contraction with the first-neighborhood class. Rational Chern characters suffice, since only a mixed Hodge component is being killed; the resulting morphism between complex abelian varieties is zero integrally once its differential is zero.

The projection of the obstruction is correctly isolated. The deformation contracts only a C differential. Multiplication by a section on each K3 factor preserves that factor's separate cohomology and differential degrees. Thus (2,0) and (0,2) factors, and all terms with positive projective-space degree, cannot feed the selected tensor of H1(Ω1) factors. On each Fermat K3, the joint multiplication map has kernel precisely C·H_i; its quotient is dual to the surjective degree1 times degree3 multiplication onto degree4 of the Jacobian ring. Tensoring these injections yields exactly the sum of kernels with an H_i factor. Pairing with all τ_i kills that sum.

Every correction term a^j b_j with j≥1 is also handled. A canonical class from C gives the wrong curve cohomology degree for the mixed Picard component. An H_i factor must pair with τ_i and a degree-zero residual factor, hence vanishes because τ_iH_i=0. Repeated H_i factors have excessive degree. This reasoning applies to arbitrary cycles on the product and makes no divisor-generation assumption.

The invariant commutes with fibres of actual families on the fixed puncture. Compactifying a curve parameter and closing its cycle does not replace the ordinary equivalence relation. Vanishing of the mixed Hodge component makes the induced parameter-Jacobian homomorphism zero, so the source ordinary subgroup is killed. The target Poincare family has composite (−9)^(r−1) times the identity. Divisibility of Pic0(C)(C) proves the integral cokernel surjection, and the specified nontorsion point proves rational nonsurjectivity.

No flaw was found in the full-basis proof. It uses an algebraic tensor argument for every r, not extrapolation from finite matrices. The improved r2 threshold from C.3ae is correctly kept separate. The proof relies on the previously independently audited C.3ae local-geometric and Chern-character constructions, with the changes in dimensions and ranks explicitly checked here.

## Sharper section construction: complete follow-up audit

**Passed at 09:06:40 UTC, 2026-11-19**, after reading the newly typed Step5 in full and independently reproducing its finite certificate. This extends the certification to the stated bound **N≥4^(r−1)+2r−1**.

The independent script `code/audit_quartic_column_pairs.py` reads only the selected coefficient tuple, assembles the three column matrices separately, and uses lexicographic Groebner bases rather than the owner's grevlex order. All twelve chart ideals are [1] modulo101; the column determinants are independently reproduced as −36,4,200. Runtime0.190871seconds. Complete output is retained in `output/audit_quartic_column_pairs.json` and `.out`. Properness of the projective determinantal loci over Z makes this a characteristic-zero emptiness certificate.

The all-s argument also checks independently. For s≥2, the three first column factors are pairwise independent and the three remaining tensor factors are pairwise independent. Any dependence of the three full pure tensors must use all three terms. If the first three factors span dimension3 it is impossible immediately. If they span dimension2, the third has two nonzero coefficients in the first two, and comparison forces proportional remaining factors, again impossible. Thus the compressed sections are basepoint free. The s=1 case is exactly the already audited original C.3ae basepoint-free calculation.

The correlation of coefficients in the obstruction is correctly handled. The rank57 original map is an injection from Ubar tensor E_C. The linear map E_C→E_C^(tensor s) sending the chosen basis vector e_k to e_k^(tensor s) is injective. Composing its tensor with the s-fold product of the original injection produces exactly the coefficient products in the compressed sections. No additional C factors are introduced geometrically. Before passing to Ubar in each factor, the kernel is precisely the previously described sum with an H_i factor. The projection, correction terms, actual-family argument and integral conclusion therefore remain valid.

The smaller rank m≥4^(r−1)−1 still satisfies m>r for every r≥2. No exception at r2 is hidden: m≥3>2 and the threshold is exactly N≥7.
