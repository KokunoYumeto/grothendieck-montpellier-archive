# Whole-product operators for the conditional C6 extension

AI-produced by GPT-6 Astra, root, current run, 19 November 2026. No priority is claimed. The operator statements below are proved. The proposed local-monodromy theorem still requires the separate simultaneous-alteration and semilinear-action audit.

## 1. Conventions and the two involutions

Let Z be smooth projective of dimension d over a characteristic-zero field, with ample class L. Work in one classical Weil realization. On a primitive vector p in degree i≤d, write n=d−i. Its Lefschetz string is p,Lp,…,L^n p. The Lefschetz involution S and Hodge involution T of André (1996, section1.1, printedp10) satisfy

\[
S(L^k p)=L^{n-k}p,\qquad
T(L^k p)=(-1)^{i(i+1)/2}\frac{k!}{(n-k)!}L^{n-k}p.
\]

All factorials are rational scalars. Tate twists are restored when these are viewed as maps: on degree j, either involution has target H^(2d−j)(Z)(d−j). Define the normalized lowering operator

\[
\Lambda(L^k p)=k(n-k+1)L^{k-1}p.
\]

The displayed coefficient formula gives T²=1 and TLT=Λ directly. Moreover h=[Λ,L] has eigenvalue d−j in degree j. These identities do not require an algebraic Lefschetz inverse.

There is a printed normalization discrepancy in the sentence on Andrép11 that equates SLS and TLT. For Z=P², on the class L, the first is1 and the second is2. The p10 definitions instead give SLS(L^kp)=L^(k−1)p for k>0, while TLT is the normalized operator Λ above. We use the definitions and the directly verified identity TLT=Λ; we do not use the discrepant equality. The primary page images were actually inspected. This is a correction to that specific displayed equality, not a refutation of Proposition1.2 or of the motivated-cycle construction.

## 2. Recovering a factor operator on a whole product

Let P=X×Y, with a product ample class. Put dX=dimX and dY=dimY. Let LX and LY denote cup product with the pulled-back ample classes, regarded as algebraic correspondence operators on P. Let T be the Hodge involution of P.

André's Lemma1.3.2 (printedp13, complete proof opened) states, on H^m(X)⊗H^n(Y),

\[
T=(-1)^{mn}(T_X\otimes T_Y).
\]

The cross-parity operator D=(-1)^(mn) commutes with LX and LY and with both factor involutions, since all of these preserve the parities of the individual degrees. Also D²=1. It follows from the directly verified single-factor identity that

\[
T L_X T=\Lambda_X\otimes1,
\qquad
T L_Y T=1\otimes\Lambda_Y.
\]

Thus hX=[TLXT,LX] is a finite expression in the algebraic partial Lefschetz operator and the global involution; it acts by dX−m on the factor of degree m. The projector onto that factor degree is the explicit rational polynomial

\[
\pi_m^X=
\prod_{\substack{0\leq r\leq2d_X\\r\ne m}}
\frac{h_X-(d_X-r)}{r-m}.
\]

Absent cohomological degrees cause no problem: the same polynomial is simply zero there. This constructs an operator, not an algebraic cycle representing the projector.

The normalized sl2 relations give the Weyl operator

\[
w_X=\exp(L_X)\exp(-\Lambda_X)\exp(L_X),
\]

where the exponentials are finite rational polynomials because the operators are nilpotent. On degree m, wX=(-1)^(m(m+1)/2) TX. This can be checked on each primitive string, where it is the standard action of the matrix ((0,−1),(1,0)) on the symmetric power of the two-dimensional representation. Therefore

\[
T_X\otimes1=w_X\sum_{m=0}^{2d_X}(-1)^{m(m+1)/2}\pi_m^X.
\]

The order is essential: the sign acts on the input, so it is on the right of wX. The analogous formula recovers1⊗TY. Hence factor degree projectors and factor Hodge involutions can be replaced by finite rational expressions in partial algebraic cup products and the single global Hodge involution of the product. No algebraic generic Künneth projector and no tensor comparison on an E1 page has been assumed.

## 3. A global involution uses finitely many Hard-Lefschetz inverses

For j≤d and j≥2, put

\[
Q_j=L\,(L^{d-j+2})^{-1}\,L^{d-j+1}:H^j(Z)\longrightarrow H^j(Z).
\]

The inverse is that of the Hard-Lefschetz isomorphism H^(j−2)(Z)→H^(2d−j+2)(Z)(d−j+2). The twists in the composition cancel. If x=L y, then Qj x=x; if x is primitive of degree j, then L^(d−j+1)x=0 and Qj x=0. Thus1−Qj is the primitive projector. Set Qj=0 for j<2. Iterating the same operation on y=(L^(d−j+2))^−1 L^(d−j+1)x gives the entire Lefschetz decomposition. For j>d, first use the inverse of L^(j−d):H^(2d−j)(Z)→H^j(Z)(j−d), then perform this decomposition in degree2d−j. The coefficient formula in section1 now constructs T in each degree using finitely many algebraic Lefschetz maps, their Hard-Lefschetz inverses, rational scalars, addition and composition.

When these expressions mix degrees, treat the finitely many normalized groups H^(i+2r)(Z)(r), for a fixed parity i, as separate vertices. Every arrow then has degree and Tate twist explicitly determined; there is no unspecified inverse of an inhomogeneous operator.

## 4. The action of a motivated correspondence as such an expression

Let U be smooth projective of dimension d. A homogeneous motivated endomorphism e is a finite sum of terms

\[
e=\operatorname{pr}_{12*}(\alpha\cup T_P\beta),
\qquad P=U_1\times U_2\times V,
\]

as in André's Definition1, section2.1, printedp14. Let c=dimV, D=dimP=2d+c, and let α and β have codimensions a and b. Since e has codimension d, necessarily b=a+d. The same argument applies termwise if the initial presentation has several homogeneous components.

Introduce W=U0×P. The action of e on H^i(U0) is the following finite composition:

1. Exterior multiplication by the algebraic cycle β sends H^i(U0) to H^(i+2b)(W)(b).
2. Apply1⊗TP, expressed by section2 in partial cup products and the global involution TW. The result lies in H^(i+2D−2b)(W)(D−b).
3. Pull back by the algebraic map δ:P→W identifying U0 with U2, multiply by α, then push forward along P→U1.

The final degree is

\[
i+2(D-b)+2a-2(D-d)=i,
\]

and the final twist is(D−b)+a−(D−d)=0. This is exactly the standard pull–cup–push action of e. All arrows in steps1 and3 are algebraic correspondences; section2 removes the factor involution, and section3 removes the remaining global involution in favor of finite Hard-Lefschetz inverse expressions on whole smooth projective products. Thus the action of a fixed motivated correspondence admits the finite expression required by the graph-rank lemma in root_rank_diagram_note.md.

## 5. What must be retained after semistable alteration

For a proper generically finite alteration f:Y→Z of degree δ, H^j(Z) identifies with the image of q=δ^−1 f*f_* on H^j(Y). The transferred Hard-Lefschetz map is an isomorphism only between these images; it must not be inverted on all of H^j(Y). In the graph description impose(q−1)x=0 for every variable that represents a Z vertex. Both q and the transferred elementary maps are induced by algebraic correspondences and have common E1 maps by Saito's construction. Their actual projector and inverse relations are required only on E2, where E2=GrW of the abutment.

The graph-rank identity remains valid with these image constraints: for any linear constraint matrix R and output projection π, the output image is π(kerR), whose dimension is rank(R,π)−rankR. No projector is required on the chain complex. Invertibility on the specified images ensures that this output image is precisely the image of the intended motivated map.

The remaining audit is the simultaneous construction over a common finite Galois local extension, compatibility of all these transferred operations with the weight filtration and monodromy, and the algebraic action of the original inertia quotient on the conjugate semistable models. None of those is inferred solely from the calculations above.

## 6. Verification and source scope

Root read André (1996), printedpp10–14, including the full proofs supplied for Proposition1.2 and Lemma1.3.2 and Definition1. The first algebra-generation assertion of Proposition1.2 refers to Kleiman; the needed operator statements here have been directly proved on primitive strings, so no unchecked Kleiman assertion is used. The remainder of Proposition2.1 beyondp14 was not reread in this audit.

code/check_lefschetz_factor_operators.py verifies21 primitive strings and100 tensor-string pairs with exact rational matrices, including the global/factor Hodge identity, conjugation, degree projectors, Weyl-operator sign order and the P² normalization discrepancy. The program and complete output are retained. These checks do not verify the geometric obligation in section5.

André, Y. (1996). Pour une théorie inconditionnelle des motifs. *Publications Mathématiques de l'IHÉS, 83*, 5–49. https://www.numdam.org/item/PMIHES_1996__83__5_0.pdf. Opened as specified above.

Saito, T. (2003). Weight spectral sequences and independence of ℓ. *Journal of the Institute of Mathematics of Jussieu, 2*(4), 583–634. https://doi.org/10.1017/S1474748003000173. The full correspondence construction in author section2.4, pp33–36, was directly read in the preceding root audit.
