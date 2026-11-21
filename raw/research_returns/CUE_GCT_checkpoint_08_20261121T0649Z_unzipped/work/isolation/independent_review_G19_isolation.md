# Independent whole-proof review of G-19

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/isolation`.
Run: CUE-GCT-20261121-I.
Review completed: 2026-11-21T04:01:00+00:00.
Reviewed file: `work/root/g19_fragment.tex`.
Reviewed SHA256: `c34802a86533c3a0ca3d577a590934645afbfdee7a57bb4ac53a6e810b325236`.

## Outcome

**PASS**, with one source-precision request and an optional convention clarification sent to root. This records a complete reading and mathematical rederivation of the displayed new proof. It is not a machine proof certificate, a numerical verification, or a historical-priority judgment.

## Checks performed

1. The affine singular-locus codimension at least k implies projective singular-locus dimension at most N-k-1. A general (k-1)-plane misses it, and characteristic-zero Bertini on the smooth locus gives a smooth degree-m section. The full-rank linear maps form the required nonempty open subset. For determinant restrictions, the inspected ABV Theorem1.7 covers every linear map, including noninjective maps; identically zero restrictions have zero discriminant.
2. The hypersurface discriminant coefficient degree is D=k(m-1)^(k-1). Scalar variable dilation gives k*delta=m*D, hence delta=m(m-1)^(k-1). With the argument space V and forms Sym^m(V*), coordinate functions lie in Sym^D(Sym^m V): the first-k-variable discriminant transforms by the determinant character on GL_k, is killed by its raising operators, and involves no later indices. It is therefore a positive highest-weight vector of rectangular weight (delta^k). Under the paper's dual convention the same isomorphism type is consistently relabeled; no multiplicity changes.
3. In a semisimple representation, a single highest-weight vector of fixed weight, even across multiple isotypic copies, generates the image of one irreducible module. Its translates vanish on every determinant orbit point and its closure. One nonzero permanent restriction makes the equivariant restriction map on that copy nonzero, hence injective.
4. The Weyl dimension product has exactly the stated crossing factors i<=k<j. Schur orthogonality applied to the actual copy gives the factor ||h||^2/dim(W), independently of the scaling of the invariant Hermitian inner product. The determinant energy is zero; the permanent energy is strictly positive.
5. A primitive integer discriminant composed with the integer coefficient polynomials of per_m gives a nonzero homogeneous integer polynomial of total degree mD. Independent standard complex Gaussian monomials have exactly the alpha! norm and zero cross terms. Thus the energy is a positive integer at least1. A grid of mD+1 distinct integers in each of kN coordinates cannot kill a nonzero polynomial of total degree mD.
6. A kernel statement on one specified irreducible copy does not compare the ranks on the entire multiplicity space. The argument correctly asserts neither a total multiplicity inequality nor absence of the type on the determinant side.
7. Every positive padding has either a repeated linear factor or two positive-degree factors meeting projectively. At their intersection all first derivatives vanish. The stated k>=5 is more than sufficient for the nonempty intersection, and the zero-restriction case is covered. Hence the degree-n discriminant supplies no padded separator.

## Primary sources independently inspected

- Alper, Bogart, and Velasco, author PDF https://sites.math.washington.edu/~jarod/papers/determinantal-complexity.pdf : Theorem1.7, printed p3, and its complete local proof, printed p5. Retrievals `turn797865049view0`, `turn585207288view0`.
- Benoist, primary PDF https://www.math.ens.psl.eu/~benoist/articles/degreic.pdf : equations(1.1)--(1.6), Theorem1.3 and Theorem1.7, printed pp1190--1191, and Example1.8, p1192, including a screenshot of that page. Retrievals `turn797865049view1`, `turn585207288view1`, `turn585207288view2`.
- **Source typo flagged:** Example1.8 prints deg_var=e_1^N, omitting the d_1 factor. Theorem1.3(1.6), equation(1.4), and scalar dilation all give the correct d_1 e_1^N. G19's actual exponent is correct; root was asked to cite these correct formulas explicitly.
- The singular-locus input R-B17 and Mukai5.20/5.21 were treated as already audited background in this run; I did not independently reopen their primary pages during this review. No additional source-read claim is made.

## Subsequent exact finite certificate check

At 2026-11-21T04:02:21.920730+00:00, I independently executed `check_G19_cubic_independent.py`. The program imports neither SymPy nor the root construction/elimination routines. It rebuilds the displayed pencil and its permanent from six dictionary products, all five derivatives, and all210×350 Macaulay entries by independent Cartesian enumeration and convolution. All73500 bytes match; matrix SHA256 `c739e7d83b6c43a3e48e6f20c92667fd77282af7e1240c3806d55989af0928e5`. Independent elimination of the selected210×210 minor returns94 modulo101. The nonzero integer minor makes the degree-six gradient-ideal map surjective over Q, so no nonzero projective common gradient zero exists over C. This is a fully verified finite smooth cubic example, not a family theorem. Details and exact event are in `G19_cubic_independent_checks.json`.

## Added certificate display and row-minimality

At 2026-11-21T04:10:20+00:00 I read the added paragraphs in full, expanded all listed inclusive multiplier-index ranges, and matched the resulting ordered210columns exactly with the already verified JSON. D=80 and delta=48 are correct. R11 explicitly provides density of the four-variable determinant-cubic image; a positive highest-weight polynomial with at most four rows uses only those coefficient variables. Hence no nonzero such determinant equation exists, while the displayed discriminant gives a five-row equation. This proves row-minimality for a specified separating polynomial, without a multiplicity comparison. PASS.
