# SNC exceptional divisors: exact progress and remaining gates

Updated 19 November 2026, after C.3bc. This is research material, not a certified arbitrary-germ theorem. C.3az treats a single smooth exceptional divisor over any algebraically closed positive-characteristic field. C.3bc now treats SNC exceptional divisors over Fpbar under the stated regular projective resolution and ample exceptional combination hypotheses.

## 1. The intended product torus does not survive the required geometry automatically

Let C be a cycle of rational curves and let E=C×P¹. The torus Pic⁰(C)=G_m contributes a nonzero summand Pic⁰(C)·h to K₀(E) of rational Adams weight two, by the projective-bundle formula. Take a non-torsion element when k is not algebraic over a finite field. Its Cartan image in G₀(E) is zero: on the normalization of C the line bundle is trivial, and the normalization exact sequence gives the same coherent-sheaf class for every gluing scalar.

If this exact E were a Cartier divisor in a regular threefold with conormal L of positive P¹ degree a, self-intersection would give u(1−L)=0 because the coherent pushforward of u vanishes. The product calculation instead gives −a·u h, which is nonzero rationally. Thus one cannot simply put a negative ample normal bundle on that unmodified SNC product inside a regular ambient threefold.

The actual regular plumbing alters the component Picard groups. In the simple cycle case, the old boundary-degree matrix has rows (1,0,−1), (−1,1,0), (0,−1,1), of rank two. Blowing up a point of one boundary curve on one surface component supplies a new exceptional divisor with boundary-degree row (1,0,0), raising the rank to three. The dual graph is unchanged, while the top degree-unit gluing quotient disappears. A preserved dual-complex loop by itself is insufficient.

Multiplying a lifted Picard-torus class by c₁(O_Z(−E)) is also not a new puncture class: that product is exceptional-supported and vanishes on the puncture.

## 2. A general weighted intersection identity kills the degree-unit edge quotient

The complete proof is in `C3_SNC_energy_lemma.tex`, kept unregistered pending the parent’s decision. Let E=∪E_i be a projective SNC divisor of dimension d≥2 in regular Z. Let D=Σ a_iE_i with all a_i>0, and let H be ample on E. Assume λ_ij=deg((−D)|E_i∩E_j H^(d−2))>0 for every double stratum. In particular this holds when −D restricts to an ample bundle on E.

A functional t on the edge degree vectors annihilates the component-curve restriction map precisely when R_i=Σ_j t_ij[E_i∩E_j] is numerically zero on every E_i, with t_ij=−t_ji. Put u_ij=t_ij/(a_i a_j). Squaring the numerical relations, multiplying by H^(d−2), and summing with weights a_i gives

    0 = −Σ_edges a_i a_j λ_ij u_ij²
        −Σ_triples a_i a_j a_k deg(H^(d−2)|E_i∩E_j∩E_k)
                       (u_ij+u_jk+u_ki)².

The transverse normal identities produce exactly these coefficients. Positivity forces every t to vanish. Hence the restriction-degree map from component curve classes onto the edge degree vectors is surjective over Q. Tensoring with k*⊗Q kills the entire proposed degree-unit edge cokernel using curve-class-times-unit K₁ elements on the components.

This proves a method limitation and an exact linear-algebraic input; it does not dispose of every term in the SNC K-theory spectral sequence or lift arbitrary proper-parameter relations from E to Z.

The symbolic certificate is `code/check_SNC_energy_identity.py`, with output `output/check_SNC_energy_identity.json`. Final successful run began 11:47:35.265121 UTC and took 0.043683026 seconds. Both exact weighted polynomial expansions vanish; the displayed degree matrices have ranks two and three. The first attempt completed the mathematics but failed JSON serialization of SymPy integer objects; explicit integer conversion repaired only output serialization. No geometric inference depends on a bounded computation.

## 3. Primary plumbing and contraction source actually read

Kollár, J. (2014). Simple normal crossing varieties with prescribed dual complex. *Algebraic Geometry, 1*(1), 57–68. https://doi.org/10.14231/AG-2014-004 . Primary full PDF: <https://content.algebraicgeometry.nl/2014-1/2014-1-004.pdf>.

We opened the full published PDF and read Lemma 15, printed p.63, Lemma16 and full explicit chart proof, pp.63–64, and the proof of Theorem2, p.64. Starting with a projective SNC divisor D in smooth Y, blowing up D∩H preserves its strict transform as the same abstract D and changes its normal bundle to O_Y(D−H)|D. The new ambient has the explicit local equations x₁…x_r=yz. Ordered blowups of the irreducible components supply a small log resolution, preserving the dual complex but altering some component geometry. The contraction step invokes Artin1970 Corollary6.12.a and gives an algebraic construction étale locally. We have not yet independently opened that underlying Artin source in this SNC investigation; it is a cited input in the fully opened Kollár proof. Page59 explicitly says the constructions apply over arbitrary fields, with the positive-characteristic/nonclosed-field caveat referred to Kollár’s book. The branch used here is the explicit blowup/small-resolution construction, not the separate double-cover construction of Lemma14.

This source resolves the regular-plumbing question for these models, but does not preserve the top K₁ class proposed on the initial product.

## 4. Triple strata: coefficient K₂ is neither automatically rigid nor automatically liftable

The precise proper-curve symbol lemma was already fully proved and independently audited in real_weil/TOP_QUOTIENT_RESEARCH.md §2. For a,b∈k* with neither equal to1, normalize a component through (a,b) of

    (f−1)²(g−1)² = c f g,  c=(a−1)²(b−1)²/(ab).

There are no vertical/horizontal components. At the boundary one coordinate is1, so {f,g} has no tame residue. At the unique point over (0,1), the derivative −c is nonzero even in characteristic2, f=u(g−1)², and the Steinberg relation kills 2{g−1,g}. The specialization is zero there and is {a,b} at the chosen interior point. Quillen’s exact curve localization sequence and Gersten theorem give an actual element of K₂ of the smooth proper parameter curve. This works in every characteristic. The peer’s exact primary locators are Quillen1973 §7 Proposition3.2/equation(3.3), pp.127–128, and Theorem5.11, pp.133–134, with the full primary PDF retained in its source ledger.

Consequently, if a triple-stratum class in K₀(E) is the product of a fixed class κ∈K_{−2}(E) with a coefficient in K₂(k), the same multiplication on E×P converts that coefficient-symbol relation into an actual proper-parameter K₀ relation on E. It is not legitimate to call this term rigid solely because it involves field K₂.

There is a second, separate obstruction before even discussing ordinary families on Z. KST descent, after the rational nilpotent comparison, gives the exact segment

    K₀(Z)_Q → K₀(E)_Q → K_{−1}(R)_Q → 0,

because Z is regular and local K₀(R)=Q maps onto local K₀(k)=Q. At the negative end it gives K_{−2}(E)_Q ≅ K_{−3}(R)_Q. All maps are K(k)-linear. Thus multiplying a dual-complex generator by a coefficient in K₂(k) may map nontrivially into K_{−1}(R), rather than lie in the image of K₀(Z). No injectivity of that product map or uniform image description has been proved here. This is an exact lifting gate, not an existing counterexample.

Even if a class lies in that image, a proper-family relation on E still needs an actual lift to the fixed Z×P. C.3az constructs such lifts for the smooth exceptional case by a special surface-and-line-bundle argument. No corresponding result for general SNC E is claimed.

## 5. Complex negative-K source: exact scope

Burke, A., Popa, M., and Shen, W. (2026, September15). Negative K-theory and Hodge theory. Primary preprint: https://people.math.harvard.edu/~mpopa/papers/NegativeK.pdf . The canonical opened-marked entry is frBurkePopaShen2026 in C3_SNC_references.bib. The local full PDF and text are retained in sources/burke_popa_shen2026_negativeK.pdf and .txt; SHA256 78f37b7f256a694f0f7aad4620a594ed4ccc6441f2887fceb0facbf7c1df17c1.

Theorem9.1, pp28–31, proves surjectivity of rational CH² of a resolution onto the direct sum of exceptional-surface CH0 groups for complex projective isolated klt-type threefolds. The rational-singularity case has a Bloch-conjectural condition; the additional LCI hypothesis supplies an integral refinement, further explained on pp31–32. The proof uses the exceptional Gysin/Albanese matrix and mixed-Hodge purity and polarization. Lemma13.1, p40, transfers negative K-theory between algebraic semilocal models and compactifications with the same isolated singularities. It does not assert invariance under henselization or completion. Corollary13.2(ii) still records the algebraic-versus-analytic factoriality defect. Neither the complex hypothesis nor the singularity hypotheses can be dropped here. The source therefore gives no automatic positive-characteristic or arbitrary strict-local SNC lifting theorem.

The product boundary warning in §4 remains rational: a nonzero dual-complex class in negative K does not imply its positive-coefficient product has nonzero connecting image in K−1(R)_Q. The surface-cusp calculation already shows that such products can vanish. No integral vanishing of the remaining p-primary groups is asserted.

## 6. Completed Fpbar theorem and next gate

C.3bc is finalized in C3_SNC_Fpbar_top.tex, with full report, one statement row and canonical events. The Fpbar hypothesis kills all positive top-weight field Milnor K groups. Closed-union excision and the explicitly arbitrary-scheme Adams construction then identify the top weight of K0(E)_Q with component degree vectors. Uniform KST finite detection injects CH^d(Z)_Q into that vector space, and a negative-definite exceptional-curve degree matrix spans it. Thus the entire rational top Chow group of the puncture is zero. No family lifting is needed for this field.

The next proposed extension is to arbitrary excellent isolated germs by alterations or ldh descent. This is unproved here. A generically finite alteration is not an isomorphism away from the closed point, so it does not yield the abstract blow-up square or the constant-group finite-detection argument used in C.3bc. A low-dimensional corollary must separately establish a regular projective SNC resolution and a positive exceptional divisor with negative ample restriction. No arbitrary-dimensional resolution theorem is presumed.
