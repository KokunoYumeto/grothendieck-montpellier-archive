# G-16 author proof checks and source audit

Author/checker: `/root/rectangular_bridge`, GPT-6 Astra Pro; effort inherited/not exposed; run `CUE_GCT-20261121`.

The full proof is in `work/root/g16_fragment.tex`, following the enhanced-tensor route proposed by root. I read the complete draft after writing and checked each new step below. This is an author proof check; separate root/purity reviews are not claimed here.

## Algebraic identification

For an irreducible degree-n form cone Y and a=n-m>0, the projective Segre-Veronese image is isomorphic to P(Y) x P(V*), so its affine cone has dimension dimY+3. Pullback identifies degree d coordinate functions with exactly R[Y]_d tensor Sym^(ad)V: generators give all degree-d coefficient monomials paired with all degree-ad covector monomials, and the product coordinate ring gives injectivity. This does not require Y to be projectively normal.

The dual convention is explicit. The actual coordinate ring contains S_lambda V*, and the auxiliary covector ring supplies Sym^(ad)V. The SL4 invariant dimension is Hom_SL4(S_lambda V,Sym^(ad)V), equal to one exactly for lambda=(ad+r,r,r,r). The fixed total weight nd forces r=md/4. Thus no other labels enter the invariant extraction, and all invariant pieces vanish unless4 divides md.

## Stability and quotient dimensions

The chosen coefficients gamma=sqrt(binomial(n,m)) make the four monomial tensors equal in norm in the tensor-induced symmetric-power metric. Their weights are m e_i because the auxiliary covector subtracts exactly a e_0. Off-diagonal moments vanish separately on each factor. This remains true at arbitrary padding a, including far above the ordinary rectangular boundary.

The projective stabilizer calculation is independent of a generic-stabilizer theorem. If A F is proportional to F=x0^a q, reduction modulo x0 first forces A x0 proportional to x0. The Fermat factor q then has A q proportional to q. For m>=3 its ordered mixed monomials are distinct, forcing all off-diagonal entries zero and all diagonal entries equal; trace zero gives A=0. Any projective stabilizer of the decomposable tensor stabilizes its first-factor line, so the tensor stabilizer is finite too. Kempf-Ness gives stable points in both enhanced cones. Their invariant-quotient dimensions are dimY-12, namely2n^2-10 and dimP_m4-9, preserving the exact R14 gap.

## Degree bounds

I reopened the primary Derksen paper and read Theorem1.1 and Proposition1.2 on printedp956. Proposition1.2 requires a finite kernel, which is explicitly verified. The group presentation has16 matrix coordinates, dimension15, and equation degree4. The action on Sym^n V tensor Sym^a V* has matrix degree at most n+3a, because inverse transpose on SL4 is a transpose adjugate of degree3. Thus sigma<=4(n+3a)^15 and beta<=6b(n+3a)^30. The coordinate ring dual does not change which functions are invariant; the proposition's action-degree parameter is the action on W, as stated in its source.

The enhanced determinant parametrization has total parameter degree n+a, a different quantity. Composing a degree-e_i invariant gives degree(n+a)e_i. Homogenization in the affine generator embedding and the G10 image-degree argument give degree at most((n+a)beta)^u, u=2n^2-10. The G13 weighted filtration comparison then gives the stated finite first-degree bound. The G11 Veronese argument gives the optional explicit progression with Q=((n+a)E)^(u-1). All invariant dimensions are transferred back through the exact label extraction and the previously proved four-variable highest-weight restriction. The logarithmic first-degree bound is O(n^2 log n), since b=O(n^6) and beta=O(n^36).

## Actual finite supplement

`check_enhanced_padding.py` constructs the Lie action directly on monomial tensors, using the factorial word-basis norms and the correct negative dual action. For(m,n)=(3,4),(4,8),(5,11), all15 moment entries are exactly zero, the tensor norm squared is4, the Lie-orbit matrix has rank15, and adjoining the tensor gives rank16. These three checks supplement the uniform proof; no growing-size extrapolation is used. Results are in `enhanced_padding_check.json`.

## Primary locator

Derksen, H. (2001). Polynomial bounds for rings of invariants. Proceedings of the American Mathematical Society,129(4),955-963. https://doi.org/10.1090/S0002-9939-00-05698-7. Primary author PDF: https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.7.pdf . Theorem1.1 and Proposition1.2, printedp956. Tool reference from this run: turn666524677view0. Registered source G-B13 is reused rather than duplicating the bibliography.
