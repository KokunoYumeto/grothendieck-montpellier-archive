# AM-R-004 — an actual CM period lattice, theta section and uniform archimedean jet bound

Author: GPT-6 Astra Pro, ALP_MACHINE `/root`, 21 November 2026 UTC; reasoning effort is not separately exposed. This is a geometric normalization theorem on the actual Jacobian. It is not a construction of the requested global automorphic lift chain. The period-matrix theorem itself is known: the exact source is Tadokoro (2014), Proposition 3.2, Proposition 4.1 and Theorem 4.4, arXiv:1211.6910v5, pp. 9–10 and 13–15. We cite that theorem and calculate the particular basis, polarization, sections and bounds needed here.

## Statement

Let C be the smooth projective curve y²=x⁷−1, J its principally polarized Jacobian, ζ=exp(2πi/7), E=Q(ζ), and Φ={1,2,3}. Put

\[
 \omega_i=x^{i-1}dx/y,\qquad
 c_i=-\frac{2i_{\mathbb C}}7 B(i/7,1/2)(\zeta^i-1),\quad
 D=\operatorname{diag}(c_1,c_2,c_3).
 \tag{R4.1}
\]

Here i_C is the imaginary unit, distinct from the index i. Define the 3 by 3 matrices, with i=1,2,3 and j=0,1,2,

\[
 A_{ij}=\zeta^{2ij},\qquad
 B_{ij}=\sum_{k=j}^{2}\zeta^{i(2k+1)},\qquad P=DA,
 \qquad \tau=A^{-1}B.
 \tag{R4.2}
\]

The following normalizations are explicit.

1. The actual period lattice in the integral coordinates u_i=∫ω_i is

\[
 \Lambda=D\Phi(\mathcal O_E)=P(\mathbb Z^3+\tau\mathbb Z^3).
 \tag{R4.3}
\]

Its principal Riemann form in O_E coordinates is

\[
 \mathcal E(x,y)=\operatorname{Tr}_{E/\mathbb Q}
       \left(\frac{\zeta-\zeta^{-1}}7x\bar y\right).
 \tag{R4.4}
\]

In particular this is a concrete mixed-type CM torus with its actual principal polarization, not a torus induced from the quadratic type {1,2,4}.

2. The normalized matrix is the following symmetric element of the Siegel upper half-space:

\[
\tau=\begin{pmatrix}
-\zeta^5-1&-\zeta^5-\zeta^4-\zeta^2-2&\zeta^5+\zeta^3+\zeta\\
-\zeta^5-\zeta^4-\zeta^2-2&\zeta^5-\zeta^4+2\zeta^3+\zeta&\zeta^5+\zeta^3+\zeta^2+1\\
\zeta^5+\zeta^3+\zeta&\zeta^5+\zeta^3+\zeta^2+1&\zeta^2
\end{pmatrix}.
\tag{R4.5}
\]

Write Y=Im τ, and let G=diag(G_1,G_2,G_3) be the Hodge Gram matrix computed in ALP-LIFT-03. Then

\[
 G=P Y\bar P^{\mathsf T},\qquad
 \operatorname{covol}_{\mathbb R^6}(\Lambda)=\det G
 =\frac{7^{5/2}}8\prod_i|c_i|^2.
 \tag{R4.6}
\]

The Euclidean volume here refers to the displayed u coordinates. It is not a level-group volume or a `MainX` covolume.

3. For every integer κ≥1, define

\[
 \theta_\kappa(z)=\sum_{n\in\mathbb Z^3}
     \exp(\pi i\kappa n^{\mathsf T}\tau n+2\pi i\kappa n^{\mathsf T}z),
 \quad
 F_\kappa(u)=
 \frac{\exp\!\left(\frac{\pi\kappa}{2}z^{\mathsf T}Y^{-1}z\right)
       \theta_\kappa(z)}{\theta_\kappa(0)},\quad z=P^{-1}u.
 \tag{R4.7}
\]

These are actual sections of L^κ, for the symmetric principal theta line L attached to τ, written in its local Chern-normalized holomorphic frame. Their rigidified germs satisfy F_κ(0)=1. Explicit rational bounds prove

\[
 \lambda_{\min}(Y)>6/25,\qquad
 |\theta_\kappa(0)-1|<3/8,\qquad
 |\theta_\kappa(0)|>5/8.
 \tag{R4.8}
\]

Uniformly for every u∈C³ and κ≥1,

\[
 |F_\kappa(u)|<49\exp\!\left(
       \frac{\pi\kappa}{2}\sum_{i=1}^3\frac{|u_i|^2}{G_i}\right).
 \tag{R4.9}
\]

Consequently, for every multi-index α=(α_1,α_2,α_3) of nonnegative integers,

\[
 |\partial^\alpha F_\kappa(0)|
 \le49\,\alpha!\prod_{\alpha_i>0}
       \left(\frac{\pi e\kappa}{\alpha_iG_i}\right)^{\alpha_i/2}.
 \tag{R4.10}
\]

For the source-shaped level normalization κ=M² and N=|α| this gives the exact cancellation

\[
 \left|M^{-N}\partial^\alpha F_{M^2}(0)\right|
 \le49\,\alpha!\prod_{\alpha_i>0}
       \left(\frac{\pi e}{\alpha_iG_i}\right)^{\alpha_i/2}.
 \tag{R4.11}
\]

This is a uniform archimedean inequality for an explicit family of sections. It supplies neither a prescribed nonzero positive-degree jet nor its required integral finite-place lattice.

4. With probability Haar measure dx dt on J(C), z=x+τt, the metric in the usual theta frame is exp(−2πκ t^T Yt). In this metric the exact squared L² norm of the rigidified section is

\[
 \|\theta_\kappa/\theta_\kappa(0)\|_{L^2}^2
   =\frac{\det(2\kappa Y)^{-1/2}}{|\theta_\kappa(0)|^2}.
 \tag{R4.12}
\]

Thus even in this explicit example, normalization to value 1 and normalization to L² norm 1 are different operations, with the difference recorded rather than discarded.

## Proof of the lattice and polarization

Use Tadokoro's paths λ_j from (0,i_C) to (0,−i_C) through the branch point ζ^j, and write γ_j=λ_{j+1}−λ_j, j=0,…,5. Tadokoro's Proposition 3.2 states that

\[
 a_i^{\rm T}=-\gamma_{2i-1},\qquad
 b_i^{\rm T}=\sum_{k=0}^{i-1}\gamma_{2k},\quad i=1,2,3
\]

are a symplectic basis. This fixes the topological orientation; it is not inferred from a numerical period calculation. Set

\[
 a_j=\gamma_{2j},\qquad b_j=\sum_{k=j}^{2}\gamma_{2k+1},
       \quad j=0,1,2.
\]

These are integral invertible triangular combinations of the previous basis: a_j=b^T_{j+1}−b^T_j with b^T_0=0, and b_j=−Σ_{k=j}²a^T_{k+1}. Therefore they form a Z basis. Directly their intersections are

\[
 a_i\cdot b_j=\mathbf1_{i\ge j}-\mathbf1_{i-1\ge j}=\delta_{ij},
 \qquad a_i\cdot a_j=b_i\cdot b_j=0.
\]

On the outward segment x=ζ^j t, y=i_C√(1−t⁷), the beta substitution s=t⁷ gives

\[
 \int_{\lambda_j}\omega_i
   =-\frac{2i_{\mathbb C}}7 B(i/7,1/2)\zeta^{ij}.
\]

The factor 2 includes the return segment on the opposite sheet. Subtracting adjacent paths gives ∫γ_j ω_i=c_i ζ^{ij}. Hence the periods on a_j and b_j are DA and DB. The six γ_j themselves are a Z basis, so their period columns give DΦ(Z[ζ])=DΦ(O_E), proving (R4.3). The Vandermonde matrix A is invertible because ζ²,ζ⁴,ζ⁶ are distinct.

For ξ=(ζ−ζ^−1)/7, the cyclotomic trace formula is

\[
 \operatorname{Tr}(\zeta^h)=
 \begin{cases}6,&7\mid h,\\-1,&7\nmid h.\end{cases}
\]

It follows that Tr(ξ ζ^j \overline{ζ^k}) is 1 for k=j+1, −1 for j=k+1, and zero otherwise for 0≤j,k≤5. These are exactly the intersections of the γ basis determined above. Thus (R4.4) is the actual principal Riemann form. Its positivity also follows directly from Im σ_i(ξ)>0 for i=1,2,3. The ideal ξ O_E is the codifferent: ζ−ζ^−1 generates the prime above 7, whereas 7 has valuation 6 there, so its exponent is −5, the inverse of the different of Q(ζ_7). This is consistent with unimodularity and does not replace the explicit intersection check.

Multiplying A by the matrix in (R4.5), reducing by 1+ζ+⋯+ζ⁶=0, gives B. This proves the displayed exact matrix; symmetry is visible. Positive definiteness follows either from the Riemann bilinear relations for the symplectic basis, or from the independent positive lower bound below.

The bilinear relations give G=P Y \bar P^T. Taking determinants gives det G=|det P|²det Y, which is the real covolume of the six columns P and Pτ. The standard complex-embedding lattice of O_E has covolume 2^−3√|disc E|=7^{5/2}/8. Multiplication by D scales real volume by ∏|c_i|², proving (R4.6). The discriminant formula here is also the determinant of the full cyclotomic embedding matrix; it can be checked from the polynomial discriminant of 1+X+⋯+X⁶.

## Exact nonvanishing certificate

Put a=sin(π/7), b=sin(2π/7), c=sin(3π/7). Formula (R4.5) gives

\[
 Y=\begin{pmatrix}
 c&a&a+b-c\\
 a&3a+b-c&a\\
 a+b-c&a&c
 \end{pmatrix}.
 \tag{R4.13}
\]

The supplied reproducible script `scripts/jacobian_theta_certificate.py` uses only exact `Fraction` arithmetic for its proof assertions. It brackets π by Machin's identity 16 arctan(1/5)−4 arctan(1/239), with 40-term alternating-series bounds, and brackets the three sines with 24-term alternating-series bounds. Outward rounding then gives rational intervals with denominator 10⁶. The smallest Gershgorin lower bound of this rational enclosure is strictly greater than 6/25; all signs of the off-diagonal entries are positive. This proves the first part of (R4.8).

Here is the full finite reduction behind the remaining assertions. For t≥0 define

\[
 U(t)=\left(\sum_{k=0}^{40}\frac{t^k}{k!}\right)^{-1}\ge e^{-t}.
\]

The code rounds U upward to a multiple of 10^−12. For each nonzero n in the cube |n_i|≤3 it uses the rational interval lower endpoint q_n for n^T Yn, choosing the lower or upper matrix endpoint according to the sign of n_i n_j. Thus q_n>0 and

\[
 \sum_{\substack{n\ne0\\|n_i|\le3}}e^{-\pi n^TYn}
 \le\sum_{\substack{n\ne0\\|n_i|\le3}}
       U((314159/100000)q_n).
\]

For the complement of the cube, π λ_min(Y)>3/4. Set a_0=3/4, q=e^−a_0. Then

\[
 \sum_{k\in\mathbb Z}e^{-a_0 k^2}\le1+\frac{2q}{1-q},\qquad
 \sum_{|k|>3}e^{-a_0 k^2}
 \le\frac{2e^{-16a_0}}{1-e^{-9a_0}}.
\]

The second inequality uses (4+j)²≥16+9j. A union bound on which of the three coordinates lies outside the cube bounds the complement by

\[
 3\frac{2e^{-16a_0}}{1-e^{-9a_0}}
       \left(1+\frac{2e^{-a_0}}{1-e^{-a_0}}\right)^2.
\]

Replacing the three exponentials by U with upward rounding gives a rational upper bound. The final rational comparison is strictly less than 3/8 (its separately labelled decimal approximation is 0.366129006419). All numerators and denominators and all inequalities are retained in `evidence/theta_certificate.json`. This proves Σ_{n≠0}exp(−πn^TYn)<3/8. Increasing κ decreases every absolute summand. Consequently |θ_κ(0)−1|<3/8 for all κ≥1, proving (R4.8). No floating-point approximation is a premise in this certificate.

## Sections, Chern jets and the uniform bound

The series θ_κ converges normally on compact sets. Direct reindexing gives, for a,b∈Z³,

\[
 \theta_\kappa(z+a+\tau b)
  =e^{-\pi i\kappa b^T\tau b-2\pi i\kappa b^Tz}\theta_\kappa(z).
\]

This is the factor of automorphy of L^κ, so these are genuine sections on the actual abelian variety. The line L is a symmetric representative of its principal polarization. We have not asserted that this representative or its particular section is fixed by the order-seven action. That distinction matters for a prescribed CM-labelled automorphic row.

In the usual holomorphic theta frame the metric is h(z)=exp(−2πκ(Im z)^T Y^−1 Im z). Its Chern connection has (1,0) coefficient πκ Y^−1(z−\bar z). Put Q(z)=πκ z^TY^−1z/2. Replacing the frame e by e′=e^−Q e makes the connection coefficient −πκ Y^−1\bar z and the metric exp(−πκ\bar z^TY^−1z). Thus on the formal holomorphic directions at 0, covariant derivatives are exactly the ordinary derivatives of e^Qθ_κ. Normalization by the nonzero θ_κ(0) proves the claimed interpretation of F_κ.

For y=Im z, completing the square yields

\[
 |\theta_\kappa(z)|
 \le e^{\pi\kappa y^TY^{-1}y}
      \sum_{n\in\mathbb Z^3}
        e^{-\pi\kappa(n+Y^{-1}y)^TY(n+Y^{-1}y)}.
\]

For every λ>0 and real t, the elementary unimodal Gaussian bound is

\[
 \sum_{n\in\mathbb Z}e^{-\pi\lambda(n+t)^2}
      \le1+\lambda^{-1/2}.
\]

To see it, keep a nearest-to-zero sample as a term at most 1. Every sample to its left or right is at most the Gaussian integral on the adjoining unit interval toward that nearest sample; these intervals partition the real line. The remaining sum is at most the Gaussian integral λ^−1/2. Applying this in three coordinates, using κ≥1 and λ_min(Y)>6/25, bounds the displayed three-dimensional sum by (1+5/√6)³<(25/8)³.

Multiplication by |e^Q| changes the exponential to

\[
 \exp\left(\frac{\pi\kappa}{2}\bar z^T Y^{-1}z\right).
\]

Since G=P Y\bar P^T is real diagonal,
\(\bar z^TY^{-1}z=\sum_i|u_i|^2/G_i\).
Dividing by |θ_κ(0)|>5/8 leaves a constant smaller than (25/8)³(8/5)=3125/64<49. This proves (R4.9).

Cauchy's integral inequality on a polydisc of radii R_i gives

\[
 |\partial^\alpha F_\kappa(0)|
 \le49\alpha!\prod_i
      \left(e^{\pi\kappa R_i^2/(2G_i)}R_i^{-\alpha_i}\right).
\]

For α_i>0 minimize at R_i²=α_i G_i/(πκ); for α_i=0 take the limit R_i→0. This proves (R4.10). With κ=M², the factor κ^{|α|/2} is precisely M^N, proving (R4.11). This calculation is an explicit instance of the source normalization issue already emphasized in DP50; it does not alter DP50's carried proof status.

Finally integrate the squared section norm with z=x+τt. Integration in x over [0,1]³ kills all cross terms n≠m. The remaining integrand is Σ_n exp(−2πκ(n+t)^TY(n+t)). Integration in t unfolds the unit cubes into R³, whose Gaussian integral is det(2κY)^−1/2. Division by |θ_κ(0)|² proves (R4.12). All integrations are justified by normal convergence or positive-term Tonelli integration. This completes the proof.

## What remains before this is a lift-count input

The statement now fixes an actual mixed-type CM lattice, polarization, complex covolume, nonzero section family, metric, Chern gauge and level-uniform archimedean jet bound. The new exact finite Hodge lattices in ALP-LIFT-05 complement it. These are concrete geometric data that can be used in a replacement arithmetic constructor.

They do not identify F_κ with the primitive trace-one Poincaré kernel of the selected source row. Nor do they establish integral normalized coefficients, the allowable-translate expansion with controlled algebraic coefficient height, membership in the chosen automorphic theta image, all-degree `ClsK.Core`, `SizeData₂`, or the six identities for that tied actual family. In particular, θ_κ(0)≠0 proves nonvanishing of the section at the origin; it is not controlled nonvanishing of the prescribed high-degree harmonic jet or terminal lift. Passing from a nonzero complex section to such a family remains a substantive arithmetic step.

In Grothendieck's language, (R4.3–6) fix the Betti lattice and polarization of the Picard variety; (R4.7–12) fix its complex metrized theta line and a Hodge-splitting jet calculation. The Poincaré biextension framework is SGA 7 I, Exposés VII–VIII; the integral crystalline realization and its filtration remain the objects of cote 54 scans 3 and 5–7 and cote 4 scan 3, (8.1.1–2). No assertion in those manuscripts is replaced by the complex analytic bounds here.

## References

Tadokoro, Y. (2014). The period matrix of the hyperelliptic curve w²=z^(2g+1)−1. *Tsukuba Journal of Mathematics, 38*(2), 137–158. The version actually consulted is arXiv:1211.6910v5, Proposition 3.2, Proposition 4.1, Theorem 4.4, pp. 9–10, 13–15. https://arxiv.org/abs/1211.6910.

Supplied programme sources: DP_MULT DP49, DP50, DP57, DP64, DP65 and DP67; THETA3 Part II G1. Their statuses are carried without upgrade. The exact new rational certificate and the symbolic period check are documented separately.
