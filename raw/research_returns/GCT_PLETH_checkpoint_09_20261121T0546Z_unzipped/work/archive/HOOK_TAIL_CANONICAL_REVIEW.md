# A101. Actual canonical isomorphisms on every hook tail

## Result and scope

**PASS.** I read the whole R050 report, HM.1–HM.27 and all seven sections, and the two complete verification programs. I independently opened the primary Langley–Remmel and Solomon texts and read the precise statements and proofs cited below. The audit covers the actual finite-row power-sum map, all unstable row bounds, the normalized canonical factorization, the exact inverse description and the complete unit-family scalar.

The strongest point is the range with inner degree $n<t$. Its proof uses the separate row degree of the actual source polynomial, so no stable homogenization hypothesis is inserted there. Both canonical maps inject on the full hook-tail multiplicity spaces and consequently are isomorphisms.

## 1. Finite moment generation through the displayed map

The unrestricted power-sum generation proof is an induction on the number of occupied rows in a row-orbit sum. In a product of polarized power sums, the distinct-row contribution is exactly that orbit sum times the factorial of the repeated row types. Every other equality pattern has fewer occupied rows. The diagonal term is nonzero over $\mathbb Q$, so the induction solves for every orbit sum.

For a fixed formal linear covector, Newton recursion expresses the elementary symmetric functions of the $s$ scalar row values in their power sums through degree $s$. Their monic characteristic polynomial gives the recurrence for every larger power sum. Coefficient extraction in the covector variables is literal polarization; hence it expresses every larger polarized generator in generators of degree at most $s$.

The centering map is the actual projection $P_s$. The direct splitting into the mean line and $W_s$ makes the invariant projection surjective, and the first power sum becomes zero. The remaining generators are exactly HM.3 with scalar one. This proves its surjectivity in every degree, including the empty positive-degree algebra at $s=1$.

## 2. The source hook calculation and its primary locator

The virtual specialization is defined on every power sum by $p_j\mapsto1-z^j$. It follows directly from the complete-function generating series that $h_d[1-z]=1-z$ for $d\ge1$. Applying Adams substitution first gives $p_j[h_d][1-z]=1-z^j$, so $h_b[h_d][1-z]=1-z$ for every positive $b,d$.

The skew-Schur coproduct proves that only hooks survive this specialization. The two remaining row choices give
$s_{(D-r,1^r)}[1-z]=(-z)^r(1-z)$, including the column endpoint where one of the two rows is empty. Thus a fixed moment multidegree with $k$ nonzero generator degrees contributes exactly $\binom{k-1}{r}$ to the hook multiplicity. Comparing coefficients after dividing the fixed-degree identity by $1-z$ is legitimate: the hook polynomials $(-z)^r$ are linearly independent.

I opened Langley–Remmel, *The plethysm $s_\lambda[s_\mu]$ at hook and near-hook shapes*, Theorem 3.1 and its complete proof, printed pp.6–8, including the preceding virtual-alphabet conventions in Theorem 2.1. The report uses precisely the row-by-row special case and then multiplies the resulting specializations. Its calculation is supplied in full, and the source attribution is accurate:

https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r11/pdf

## 3. The target invariant forms and the actual faithful map

For the full permutation representation, the Jacobian of $p_1,\ldots,p_s$ is $s!$ times the Vandermonde. Expanding a polynomial differential form in their wedges is unique over the rational function field. For an invariant form, wedge with complementary invariant differentials. The resulting coefficient in the standard top form is alternating, so every $x_j-x_i$ divides it; these linear factors are relatively prime. Division by the displayed Jacobian therefore leaves a polynomial, and its symmetry follows from the same transformation rule. This proves the invariant-form algebra used in HM.9.

The mean-coordinate splitting is exact. Writing the original power sums in the mean and centered power sums is triangular with nonzero constant diagonal. Its differential substitution is also triangular. Removing the mean coordinate and its differential consequently gives precisely
$I_s\otimes\Lambda(dq_2,\ldots,dq_s)$ on $W_s$.

I freshly read Solomon, *Invariants of finite reflection groups*, §3, the unnumbered theorem on p.59 and full proof pp.59–61, together with formula (4) and its grading on p.62. The report's explicit Vandermonde proof is the relevant symmetric-group specialization of that theorem:

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/160748DDB7C9D17C5379F6FF65BB5B98/S0027763000011028a.pdf/invariants-of-finite-reflection-groups.pdf

For $\xi_d=dq_d/d$, Euler contraction is $\partial\xi_d=q_d$. Total degree gives the same weight $d$ to $q_d$ and $\xi_d$, and $\partial d+d\partial=D$ gives the rational contracting homotopy in positive total degree.

Exterior Pieri identifies the kernel at coefficient degree $t$ and form degree $r>0$ with $S_{(t,1^r)}W_s^*$: the other Pieri summand has a nonzero displayed highest-vector contraction, while the hook summand is absent from the codomain. At $r=0$, contraction vanishes and only positive polynomial degree is retained. This also covers all small dimensions by the usual vanishing of an oversized Schur shape.

In a nonzero invariant multidegree $\beta$, contraction is the ordinary exterior contraction sending every support vector to $1$. Replacing the support basis by its least vector and the differences with that vector gives the kernel basis HM.11. Its denominators cancel termwise because the support exponents are positive and wedge expansion never repeats a selected denominator. Its dimension is $\binom{k-1}{r}$.

The sum over moment multidegrees therefore equals the source hook multiplicity proved in §2. The already established surjectivity of the specific map HM.3 now makes that very map an isomorphism on each hook component. No assertion that the map respects the auxiliary moment multigrading is needed; equality is used only after summing in the total degree. This is the precise bridge from the two calculations to faithful evaluation.

## 4. All actual inner degrees, including $n<t$

A source highest polynomial has the unique dense-chart expression HM.14. Because it is an actual polynomial of separate slot degree $n$, its dehomogenization has separate row degree at most $n$. Common-translation invariance follows from the first-coordinate highest equations, and the remaining highest weight is $(t,1^r)$. This is an injection from the actual highest space; no converse stable-chart claim is made at $n<t$.

Independent-row polarization is injective on this subspace. Given a normalized functional, translating by its mean replaces it by a mean-zero functional without changing its evaluation on the common-translation-invariant polynomial. Homogeneity in the functional restores the dense open set with nonzero constant coordinate. Ordinary diagonal polarization then recovers the original row-symmetric tensor. Its exact row-degree bound puts the image in $\mathcal M_{\le n}$.

The split-moment calculation uses only degrees $2\le d\le n$, all of which have nonzero $(n)_d$. The displayed monomial pairing gives its exact factorial normalization. Equality-pattern inversion produces the set-partition coefficients
$(-1)^{|B|-1}(|B|-1)!$ without omitted multiplicities. Each generator has one single-block term with nonzero coefficient, and every other term uses lower degrees. The substitution is therefore the specified triangular automorphism of $\mathcal M_{\le n}$.

The grid pairing is exactly $\mathsf p_n\Psi_nE_a$. Its first factor on the source side is injective by polarization, its middle factor is invertible, and the final evaluation is injective on the exact hook component by §3. Translation by the common mean and homogeneous restoration determine the full polynomial from this chart calculation. Thus the actual canonical map injects on every highest multiplicity space.

Interchanging $a,n$ proves the opposite injection. The multiplicity spaces are finite dimensional, so both maps are bijective. Equivariance then gives isomorphisms on the full isotypic components. This proves HM.2 without assuming equality of the two coefficients in advance.

The inverse description is also correct: invert the proved nonsingular power-sum matrix on its hook component, invert the moment substitution recursively, then use diagonal polarization and the original homogenization. Since the canonical map has been proved bijective, this expression lies in the actual source image with its requisite row bound. It does not identify the reverse canonical map with this inverse.

## 5. The unit family and normalized scalar

For an $m$-subset of rows, the Vandermonde and affine determinant both change sign under a row permutation, so their product is row symmetric. Their displayed formulas prove translation invariance and the separate row bound $m$. The determinant's upper-unipotent column operations and the first-coordinate Vandermonde give exactly the tail weight $(T,1^{m-2})$.

On the moment curve, each summand is a square of a nonzero rational Vandermonde, so the polynomial is nonzero. At total tail degree
$D=2+3+\cdots+m$, an invariant hook kernel of leg $m-2$ needs at least $m-1$ distinct generator degrees. The minimum possible sum is already $D$, forcing precisely the support $\{2,\ldots,m\}$ with every exponent one. Therefore the full centered hook space is one-dimensional. The exhibited row-degree-$m$ vector attains it in every $a,n\ge m$.

Expanding the two determinants and pairing independent rows gives $m!$ times the determinant of one-row moments. The mean-zero first row is $(1,0,\ldots,0)$, leaving $J_m$. Multiplication by $\binom am$ gives exactly $E_aP_{a,m}=(a)_mJ_m$.

For population power sums, augment the moment matrix by the constant row and column. Its first row is $(s,0,\ldots,0)$, so its determinant is $sJ_m(p)$. Cauchy–Binet with increasing row subsets is precisely the sum defining $P_{s,m}$; the two determinant orientations agree. This proves HM.23 with the factor $s$, and the derivative row factors give the additional exact relation to the Euler form.

The hook subspace of the moment algebra in this degree is one-dimensional. In $J_m$, its original moment multidegree uses degrees $2,\ldots,m$ once each. Under the triangular substitution, the coefficient in that multidegree is the product of the single-block coefficients. A lower-degree replacement cannot recover the largest degree that it replaces. Equivariance and one-dimensionality therefore give the entire scalar action.

Combining the two determinant identities yields exactly
$$
C_m(a,n)=(-1)^{\binom m2}\frac{(a)_m}{n}
\frac{\prod_{j=1}^{m-1}j!}{\prod_{d=2}^m(n)_d}.
$$
All factors are nonzero in the stated range. At $a=n=m$, the factorial simplification gives the square formula HM.25. I independently checked its values $-1/2,-1/9,1/96,1/2500$ at $m=2,3,4,5$ directly from those products. The first-row equality at $a=n=m$ is $m^2-D=T$, as required for the square weight.

## 6. Further family, endpoints and verification status

The Euler-form support $\{2,\ldots,r+2\}$ with all exponents one supplies the nonzero hook cycle in HM.26, and multiplication by $q_2^uq_3^v$ preserves it. The column bound gives separate row degree at most $t$, so for $n\ge t$ the actual highest space equals the full centered hook space. This justifies its common rank $H_a(t+r,r)$ and its positive endpoint.

At $t=1$, the total degree is too small for the required $r+1$ distinct generator degrees, so every hook-tail component is zero. At $a=1$ or $n=1$, the finite moment algebra has no positive part; the actual tensor map has only the row component. The empty tail is treated separately with scalar one. Every rational denominator used in the proof is nonzero in its stated range.

I read the complete finite-row, multidegree, reciprocity and literal-pairing implementations. Their reported checks distinguish coefficients from actual map rank, and the literal scalar side expands the original determinant permutations rather than using the moment identity being tested. Those 4,650, 729, 457 and 75 comparisons are the author's executed receipts and are not rerun here. The present audit establishes the complete proof and the primary-source use independently.
