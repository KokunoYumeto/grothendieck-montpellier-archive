# Five points: the Kummer Casimir is not divisible by two

**Status: proved auxiliary obstruction to one proposed extension of the Kummer method, with a complete bounded exterior-algebra certificate. No main-gate movement and no integral-Hodge-conjecture counterexample.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed. Date: 19 November 2026. Root independently found the four-distinct-site coefficient and reconstructed its collision support test. The cycles reviewer identified the necessary torsion repair in Section4 and supplied the indicator-polynomial independence argument. No priority claim.

## 1. Exact statement and normalization

Let A be any complex abelian surface, let K=K_4(A) be the zero-sum fibre of A^[5], and let U_K in CH²(A×K) be the actual universal length-five subscheme. Put

    μ(a)=(U_K)_*a in H²(K,Z),  a in H²(A,Z).

This is the usual incidence map; for five points its Nakajima expression is (1/4!)θ^*(q1(a)q1(1)^4|0>). In particular it has no extra arbitrary scalar. Choose an oriented integral basis a1,a2,a3,a4 of H¹(A,Z) with integral_A a1a2a3a4=1, and define

    Q_K = μ(a1a2)μ(a3a4)
          + μ(a1a3)μ(a4a2)
          + μ(a1a4)μ(a2a3) in H⁴(K,Z).                (FP.1)

Then the rational class Q_K/2 is **not** in the image of H⁴(K,Z) in H⁴(K,Q).

No polarization or generic Hodge-endomorphism hypothesis is needed. In particular the relation Q/6=[Y_p] on the generalized Kummer fourfold K_2(A) cannot be extended to an assertion Q/(2N) integral for every odd number N of points: N=5 already contradicts it.

This statement does not construct a Hodge surface class pairing oddly with the transcendental form. The detecting functional below is topological and is not asserted to be Hodge or algebraic.

## 2. Ordered points and the coefficient detector

Put V=A⁴, with ordered coordinates x1,x2,x3,x4, and define x5=−x1−x2−x3−x4. Let D_ij be the locus xi=xj, for 1≤i<j≤5, and let

    D=union D_ij,       V°=V minus D.

The map sending a tuple to its unordered set of five points is a finite étale cover

    V° → K°,

of degree 5!, where K° is the open distinct-support locus in K. Over this locus the universal incidence cycle is exactly the union of the five graphs. Write x_iα=pr_i^*aα for i=1,…,4 and α=1,…,4. Pulling μ(aαaβ) back to V° gives the restriction of the following integral class on V:

    M_αβ = sum_i x_iα x_iβ
            +(sum_i x_iα)(sum_j x_jβ).                (FP.2)

Indeed the last term is x5^*(aαaβ), since both degree-one factors acquire a minus sign. In the point-index matrix of (FP.2), diagonal entries are 2 and off-diagonal entries are 1. The pullback of Q_K is therefore the restriction of

    Q_V=M_12 M_34+M_13 M_42+M_14 M_23.                (FP.3)

The integral cohomology ring of V is the exterior algebra on the sixteen x_iα. Let λ be the coefficient of

    x_11 x_22 x_33 x_44

in degree four, using point index first, then α, for the total order. Each of the three products in (FP.3) contributes +1: the reordering in the second and third terms has even sign. Consequently

    λ(Q_V)=3.                                        (FP.4)

For i<j≤4, the collision D_ij is the kernel of xi−xj:V→A. Its class is

    [D_ij]=product_(α=1)^4 (x_iα−x_jα),

so λ([D_ij])=0 because only two point indices occur. For i≤4, the collision D_i5 is the kernel of

    2xi+sum_(j≠i)xj:V→A.

Thus

    [D_i5]=product_(α=1)^4 (2x_iα+sum_(j≠i)x_jα),
    λ([D_i5])=2.                                    (FP.5)

Each defining row is primitive over Z, so these ten kernels are connected smooth abelian subvarieties isomorphic to A³. Two distinct rows are linearly independent; their joint kernel has complex dimension four. In fact the retained certificate checks that all 45 two-row matrices have minors of gcd one, so these pairwise intersections are connected as well, although that strengthening is unnecessary.

## 3. Why the detector survives deletion of collisions

All intersections of distinct collision components have real dimension at most eight, whereas each component has real dimension twelve. Triangulate the finite complex algebraic arrangement compatibly with its components. Mayer–Vietoris, or its finite-union cellular version, gives

    H_12(D,Z)=direct-sum_(i<j) Z[D_ij],
    H_11(D,Z)=direct-sum_(i<j) H_11(D_ij,Z).           (FP.6)

For the second equality the relevant intersection groups in degrees eleven and ten vanish, since their spaces have real dimension at most eight. In particular H_11(D,Z) is free.

Support duality in the oriented real sixteen-manifold V identifies

    H⁴(V,V°,Z)=H_12(D,Z),
    H⁵(V,V°,Z)=H_11(D,Z).                            (FP.7)

The map H⁴(V,V°,Z)→H⁴(V,Z) sends each component fundamental generator to its cohomological class. This is also immediate from compatible regular neighborhoods, relative Poincaré duality and the deformation retraction to the triangulated support. With F2 coefficients, exactness and (FP.6) show that the kernel of restriction H⁴(V,F2)→H⁴(V°,F2) is spanned by the ten collision classes. Equations(FP.4)–(FP.5) therefore detect a nonzero restriction of Q_V modulo two.

This last conclusion alone only excludes literal divisibility by two. For the statement about an integral representative of the rational class Q_K/2, the possible torsion discrepancy must also be controlled. We do that next.

## 4. The required two-primary saturation and torsion check

Reduce the ten collision rows modulo two. They are exactly the ten distinct nonzero vectors r in F2⁴ of weights two or three. Their degree-four classes have coefficients

    r_(i1) r_(i2) r_(i3) r_(i4)

in the monomials containing one generator of each α type; the signs disappear modulo two. These ten coefficient vectors are linearly independent.

Here is a proof without relying on the computation. Every squarefree monomial in r1,r2,r3,r4 of degree between one and four is obtained from such a coefficient by repeating some of its point indices until there are four factors. Over F2, repeating an index does not change its value. For any fixed nonzero vector r, the Boolean polynomial

    δ_r(X)=product_(r_i=1) X_i · product_(r_i=0) (1+X_i)

has zero constant term, takes value one at r, and zero at all other F2⁴ vectors. It is an F2-linear combination of the nonconstant squarefree monomials just described. Applying the corresponding coefficient functional to a purported dependence isolates its coefficient at r. Hence all fifteen nonzero rows would give independent classes; in particular our ten do.

Let L be the integral span of the ten collision classes in the free group H⁴(V,Z). Their independence modulo two proves that H⁴(V,Z)/L has no two-primary torsion: equivalently, a matrix of these generators has a maximal minor odd, so its Smith invariants are all odd. No integral saturation at odd primes is needed.

The integral localization sequence contains

    H⁴(V,V°,Z) → H⁴(V,Z) → H⁴(V°,Z)
                    → H⁵(V,V°,Z).

By (FP.6)–(FP.7), its last group is free. Thus H⁴(V°,Z) is an extension of H⁴(V,Z)/L by a subgroup of a free group, and has no two-primary torsion. This is the missing ingredient in the preliminary modulo-two-only argument.

Suppose now that Q_K/2 were represented by an integral class η on K. Then Q_K−2η is torsion. Pulling back to V° gives

    Q_V|V°−2η|V° = torsion.

Every torsion element of H⁴(V°,Z) has odd order, by the preceding paragraph. Such an element is twice another integral torsion element, and hence has zero reduction modulo two. The displayed equality would force Q_V|V° to have zero reduction modulo two, contradicting Section3. This proves the statement of Section1.

The same argument would apply if Q_K−2η initially had arbitrary torsion in H⁴(K,Z); no unproved global torsion-freeness assertion about generalized Kummer varieties has entered.

## 5. Complete bounded certificate

The script `code/check_kummer_five_point_detector.py` uses the integral exterior algebra on sixteen generators. It constructs the complete degree-four coefficient vectors in the basis of size binomial(16,4)=1820, constructs all ten collision vectors from their actual integral defining rows, and performs exact binary Gaussian elimination. It checks:

| Quantity | Verified value |
|---|---:|
| λ(Q_V) | 3 |
| λ(D_ij), i<j≤4 | 0, for all six |
| λ(D_i5), i≤4 | 2, for all four |
| Rank of ten collision classes over F2 | 10 |
| Rank after adjoining Q_V | 11 |
| Gcd of the two-row minors | 1, for all 45 pairs |
| Content of the five-point Q_V | 1 |
| Content of the analogous three-point ordered pullback | 6 |

The three-point calculation is a normalization control, not a proof of integral saturation on K_2(A). The rank and coefficient checks cover every coordinate; this is not a sample of random choices.

Successful run: 20:07:31.738155–20:07:31.745625 UTC on19November2026; measured internal runtime **0.007460480999725405seconds**; exit zero. The entire sparse vectors and all pairwise minor checks are retained in `output/kummer_five_point_detector.json`, SHA256 **ab7078cafddae017c6088020d3c4e5fbfeacef4a896ae03a03eb2a8a6285df7a**. The complete printed summary is retained in `output/kummer_five_point_detector.out`.

The program does not establish support duality, the geometry of the incidence cover, or Hodge/algebraic representability. Those steps are proved or explicitly sourced above.

## 6. Failed extensions and audit boundaries

The first idea was to copy Q/(2N) integrality from N=3 to every odd N. The N=5 calculation disproves that particular claim. The original four-distinct-site coefficient did not itself justify survival after collision deletion; Sections3–4 supply the support and saturation arguments. The preliminary modulo-two-only version also omitted the possible torsion discrepancy in rational integrality; the cycles peer caught this, and Section4 repairs it. These gaps are retained rather than counted as previously completed proofs.

For N>5, using only the same four sites does not automatically produce a detector: collisions with additional points can have an odd value under that coefficient functional. No all-N nondivisibility theorem is asserted here. The one case N=5 suffices to refute the proposed universal divisibility lemma.

The exact ordinary C.4 gate is unchanged. In particular, failure of Q_K/2 to be integral is not evidence that an odd transcendental scalar is attained by an actual surface in K_4(A), still less by a rational map from A. It removes one shortcut to an all-N exclusion.

## 7. Sources actually read

The universal incidence and its arbitrary-N normalization are from Kapfer and Menet (2018), Section3 and Notation5.13, freshly read at the exact published/author scopes in `C4_KUMMER_INCIDENCE_RESEARCH.md`. On the distinct-support open, (FP.2) is also derived directly from the actual five graphs, so it does not rely on an unnormalized Nakajima formula.

For support duality, the retained Cornell chapter PDF of Hatcher was opened during the checkpoint23 freeze. The complete displayed statements and proofs of Theorems3.43–3.44 in that file, printed pp.254–255, were read. That chapter file numbers the compact-support theorem3.44; later full-book layouts can number the related statement differently. The earlier cap-product/Poincaré-duality and neighborhood-retract foundations were not all freshly reopened. The integral cohomology-with-support form used here follows from relative duality on compatible regular neighborhoods, as explained in Section3. The finite-subcomplex and torus arguments are supplied explicitly in this note.

Hatcher, A. (2002). *Algebraic topology*. Cambridge University Press. Opened author chapter file: https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf (retrievals turn722071263view0 and turn882523322view0; exact read scope above).

Kapfer, S., & Menet, G. (2018). Integral cohomology of the generalized Kummer fourfold. *Algebraic Geometry, 5*(5), 523–567. https://doi.org/10.14231/AG-2018-014
