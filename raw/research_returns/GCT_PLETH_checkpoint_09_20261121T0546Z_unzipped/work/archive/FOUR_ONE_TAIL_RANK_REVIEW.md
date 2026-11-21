# A071 — independent review of the higher-row width-four canonical family

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. I read the complete R039 report `work/rectangular/four_one_tail_canonical_rank_law.md`, HO.1–HO.18 and its transport discussion. **PASS**, including the unit bound, the exact scalar and preimage, the inner-degree-three extension, and every source-length zero endpoint. I also reread R037 EP.3–EP.5 for the exact coordinate-pullback convention. This review does not claim another execution of the author's 72 polynomial or 90 coefficient checks.

## 1. The invariant algebra and the unit bound

The signed row-power-sum induction used in HO.3 works for all finite row counts. Its discrete equality partition is the injective row-assignment sum; all other nonzero terms have fewer occupied rows with their literal exterior signs. Equal odd row types have an odd stabilizer transposition and average to zero. Projection to the sum-zero representation is equivariantly split and removes the singleton generators. This proves the actual surjection in HO.3.

In the six two-form variables, the only incomparable pair of two-subsets under componentwise order is \((1,4),(2,3)\). The displayed Plücker replacement removes one copy of each offending factor and introduces neither. It terminates. Comparable products correspond to the two-row semistandard tableaux, and their diagonal monomials in a generic two-by-four matrix are distinct: the two sorted row multisets determine the tableau. A diagonal-leading term order therefore proves their independence.

The Pfaffian is an irreducible quadratic because its bilinear matrix has rank six, whereas a factored quadratic has rank at most two. On its \(X_{12}\ne0\) chart, the minor map realizes every permitted coordinate and solves for \(X_{34}\). Primality then gives the exact kernel globally. The nonzero highest-column map and the semistandard dimension count identify the degree-\(d\) quotient with \(S_{(d,d)}T\). Multiplication by the determinant-weight Pfaffian, followed by characteristic-zero complete reducibility, gives exactly
\[
\operatorname{Sym}^d(\Lambda^2T)
=\bigoplus_{q=0}^{\lfloor d/2\rfloor}
S_{(d-q,d-q,q,q)}T.
\]

The exterior contraction also gives \(\Lambda^3(\Lambda^3T)=(\det T)^2\otimes T\). Since the target total degree is odd, only exterior degrees one and three occur. Degree three has fourth part at least two and cannot produce \(\gamma_4=1\). For degree one, a determinant generator can occur at most once; after one such factor, the remaining target has only two nonzero rows, so it cannot contain the required vertical three-strip. With no determinant generator, the only strip adds in rows \(1,3,4\) to \((m-1,m-1,0,0)\). This remains an admissible unique strip at \(m=2\). Hence the invariant space has dimension at most one, with the actual Schur maps specified in the report.

## 2. The centered highest vector and its affine minor formula

The tensor contraction in HO.9 transforms by
\[
(\det\mathbf Q^m)^2\otimes
\operatorname{Sym}^2(\mathbf Q^m)\otimes(\mathbf Q^m)^*.
\]
The two covariant indices \(1,1\) and the final dual index \(m\) give an actual highest component. Its weight is \((4,2^{m-2},1)\). Common translations and row permutations preserve the centered formula.

For HO.10, both centering column operations have determinant one. The operation on the quadratic column is available because \(m\ge2\) and its linear \(w_1\) column is present. The centered \(R^tB\) has first column \((a,0,\ldots,0)^t\), and its remaining block is \(S\) with its final column replaced by \((C_{i11})\). Last-column cofactor expansion gives \(aH_{a,m}\); the written indices \(\operatorname{adj}(S)_{im}\) agree with the cofactor indices because \(S\), hence its adjugate, is symmetric. Cauchy–Binet gives exactly the product of the two minors, with no additional orientation sign.

Each row has degree at most three in this product. On the specified centered configuration,
\[
\operatorname{adj}(S)=(m+1)I-\mathbf1\mathbf1^t,\qquad
(C_{11i})=(0,-1,\ldots,-1).
\]
Their final component is \(-(m+1)+(m-1)=-2\). Thus \(H=-2\) and \(A=-2a\), including the minimal number \(a=m+1\) of rows.

The homogenized minor formula has denominator cancellation exactly as printed: the first determinant contributes one power of every inside \(x_i\), the second contributes two, and \(u^n\) leaves the factors in HO.13. Every slot has degree \(n\). The two row-permutation determinant signs cancel. The common-translation and lower-coordinate highest equations give precisely HO.1's weight.

Dehomogenization is injective in the fixed slot degrees. Common translation invariance identifies its image with polynomials on the sum-zero row quotient through the explicit centering projection. Cauchy Young extraction then embeds its highest space into the invariant module bounded in §1. The nonzero homogeneous vector extends at \(n=3\) because its per-row degree is three, even though the largest tail part is four. This proves multiplicity one throughout the stated target domain.

## 3. Exact determinant pairing, scalar, and inverse

Expanding both determinants in HO.14 and fixing the first permutation leaves the determinant of the moment-pairing matrix, with the same sign. There are exactly \((m+1)!\) first permutations. The first column is \((1,0,\ldots,0)^t\), so the lower block has \(m-1\) second-moment columns and one third-moment column. Summing over its \(\binom a{m+1}\) subsets gives exactly \((a)_{m+1}\), with every outside slot contributing \(L(1)=1\).

The normalized split-form pairing gives the second moment \(-S/[n(n-1)]\) and the third moment \(2C/[n(n-1)(n-2)]\). These are ordered-distinct-index identities, including repeated coordinate labels. Factoring the scalars from the \(m-1\) second-moment columns and the one third-moment column gives
\[
\frac{2(-1)^{m-1}}{n^m(n-1)^m(n-2)}.
\]
The remaining determinant is \(H_{n,m}=A_{n,m}/n\), so the exact final scalar is
\[
c_{a,n,m}
=\frac{2(-1)^{m-1}(a)_{m+1}}
{n^{m+1}(n-1)^m(n-2)}.
\]
Translation and separate homogeneity extend the computation on first coordinates one to the full polynomial identity.

For the desired map with parameters reversed, the reciprocal of \(c_{n,a,m}\) is exactly
\[
\frac{(-1)^{m-1}a^{m+1}(a-1)^m(a-2)}
{2(n)_{m+1}},
\]
as in HO.18. It gives the actual rational preimage when \(a,n\ge m+1\).

For \(3\le n\le m\), the opposite minor sum is empty. Independently, its source sits in the tensor product of \(n\) one-row symmetric powers, and the actual iterated Pieri inclusions give at most \(n\) rows. The specified \(\lambda\) has \(m+1\) rows, so the source multiplicity is zero while the target remains the proved unit line. This proves the entire zero-image range. All displayed denominators remain nonzero in their declared domains.

## 4. Coordinate and bundle maps

R037 EP.3–EP.5 gives the product morphism \(V^a\to\operatorname{Sym}^aV\), its algebra pullback, and its degree-\(n\) component with scalar-one normalized grid convention. I reread this passage: the evaluation tensor \(v_1^n\cdots v_a^n\) maps under the transposed grid to \((v_1\cdots v_a)^n\). Thus the nonzero cases of HO.17–HO.18 give the claimed nonzero Chow coordinate-ring classes through this exact morphism.

The Young and tensor maps are natural in the vector space and therefore have these same multiplicity matrices in every dimension at least \(m+1\). Their rational constant-rank maps and explicit inverses glue under frame changes. The cited Grothendieck transport is used in the already checked scope. No uncomputed change of basis or categorical separation is needed.

