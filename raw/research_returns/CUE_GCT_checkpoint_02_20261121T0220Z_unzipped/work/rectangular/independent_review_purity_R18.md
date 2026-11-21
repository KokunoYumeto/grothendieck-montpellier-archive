# Independent whole-proof review: R-18

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

I read the complete `r18_fragment.tex` proof and reopened the relevant complete R-16 definitions and calculations. I independently rederived the local identities, coefficient transformations, determinant cancellation, and dimension consequences below. **PASS.** This is a targeted mathematical proof reading and algebraic rederivation, not a formal verification or an external certification. No large numerical matrices were rerun.

## Simultaneous cofactor identities

For each disjoint row pair, write its three complementary permanents as

`C_0=(v_0v_1+p ell_1)R`, `C_1=(ell_0v_1+pq)R`, and `C_2=(ell_0ell_1+v_0q)R`.

Direct expansion gives both displayed identities: `ell_0 C_0-v_0 C_1-p C_2=-2pqv_0R` and `q C_0+ell_1 C_1-v_1 C_2=2pqell_1R`. They remain exact when all other disjoint pairs are perturbed, because these two rows still have support in their three specified columns. With `p=epsilon ell_1`, `q=epsilon v_2`, the two proposed polynomial families therefore belong to the same deformed differential image for every nonzero `epsilon`.

The complementary permanent at zero has the stated unique matching. The choice of row `a+k` for `U` and `a+k+1` for `V` gives bidegree `(m-k,k)` in both cases. The range `3<=k<=m-3` keeps every deleted row distinct from the two chosen rows and permits every subsequent four-coordinate argument.

## Coefficient-ratio identities

Let `A=product_(i=k)^(m-1)(x-q^i y)`. The first ratio can be verified without division of coefficients: factor the shared roots to obtain

`A_U=alpha A(x,qy)+beta A(x,y)`.

The remaining two linear factors agree because `alpha+beta=1` and `alpha+K beta=q`. Similarly,

`A_V=gamma_2 A(x,q^2 y)+gamma_1 A(x,qy)+gamma_0 A(x,y)`.

After factoring `product_(i=k+2)^(m-1)(x-q^i y)`, this is the quadratic identity

`(x-qy)^2 = gamma_2(x-y)(x-qy) + gamma_1(x-y)(x-qKy) + gamma_0(x-Ky)(x-qKy)`.

The proposed coefficients satisfy it, as one sees from its leading coefficient and evaluations at `x/y=1,q`. These polynomial identities rederive the two displayed coefficient ratios, including their endpoints. The finite-product coefficient ratios in the written proof are compatible with these simpler identities. The nonvanishing of every `A_r` is already established in R-16.

## Fourier factors and the two-normal determinant

Writing `H=product_(i=2)^(k-2)(z-q^i w)`, the unshifted and shifted `U` factors are respectively `v_0 v_2 v_(k-1) H` and `v_(-1)v_1^2 H`. The three `V` factors after shifts by zero, minus one, and minus two are exactly the three products in the proof. With `r+s=t`, the factors `q^r` and `q^(2r)` therefore give the four stated cubics, with `X=q^t`.

Here is an independent check of the determinant rather than a numerical sample. The four needed evaluations reduce to

* `U_X(1,1)=alpha X(q-1)^3/q`;
* `U_X(q,1)=-beta(q-1)^2(q^2-K)`;
* `V_X(1,1)=gamma_1 X(q-1)^2(q-K)/q + gamma_0(q-1)(q+1)(q-K)(K-1)/q`;
* `V_X(q,1)=-gamma_0(q-1)(q^2-K)(q-K)`.

In their two-by-two determinant, the coefficient of `X` is proportional to `-alpha gamma_0+beta gamma_1=0`. The constant term is

`(q-K)(q^2-K)(q-1)^6(q+1)/(q(K-1)(qK-1))`,

exactly as stated. All factors in the denominator and numerator are nonzero for a primitive `m`th root with `m>=6` and `3<=k<=m-3`. In particular the proof does not depend on a generic choice of character `t` after this calculation. The first two cubics span the kernel of evaluation at `1,q`, so the four full cubic vectors are independent.

## Restriction to available Fourier coordinates

For `3<=k,t<=m-3`, the allowable index interval

`max(0,t-(m-k)) <= s <= min(k,t)`

has at least four consecutive indices. Its initial four may be denoted `b,b+1,b+2,b+3`, with `0<=b<=k-3`. Division by `A_(t-s)` is legitimate throughout this interval. The multiplication-by-`H` four-column determinant is the Toeplitz determinant displayed in the proof. Up to signs and transpose, dual Jacobi–Trudi identifies it with `s_(4^b)(q^2,...,q^(k-2))`.

There are `N=k-3` variables and `b<=N`. After removing the common geometric scaling, the Weyl numerator is a Vandermonde in the distinct powers with exponents `lambda_i+N-i` for `lambda=(4^b)`. These lie in `[0,N+3]=[0,k]`, hence below `m`; the denominator also has distinct powers. This proves nonvanishing, including `N=b=0`, when the determinant is one. Thus the coefficient restriction cannot destroy independence of the four cubics, and the two normal classes are independent modulo the two-dimensional old character span.

## Two Vandermonde systems and simultaneous dimension growth

Both normal families translate exactly by the cyclic operator `tau`, with no unrecorded scalar. For a fixed bidegree, projecting a relation to character `t` gives two separate scalar equations because its two normal classes are independent. The consecutive characters `t=3,...,j_m+2` are available since `j_m<=m-5`. They give two invertible Vandermonde matrices in the distinct numbers `q^a`, `a=0,2,...,2(j_m-1)`. Distinctness holds for both parities of `m`, since `j_m<=floor(m/2)`.

There are `2j_m` independent classes in each of the `m-5` distinct bidegrees. Adding all their polynomial deformations to a fixed cyclic Jacobian basis gives one coefficient minor with nonzero constant term. For generic nonzero `epsilon`, every added column belongs to the actual differential image by the two exact identities above, so this is a simultaneous increase at one pencil. It proves `dim P_(m,4)>=2m^2+2+2j_m(m-5)`.

## Padding and rectangular consequences

The displayed padding inequality implies `dim P_(m,4)+3>=2n^2+3`, strictly above the determinant bound. Moreover `G_m<=m(m-5)` implies `n^2<3m^2/2`, and hence `n<4m/3`; both G-11 hypotheses hold. Since `G_m=m^2+O(m)`, all fixed ratios below `sqrt(3/2)` eventually satisfy the inequality. The result correctly keeps the R-16 bound available when it is better for a particular small size.

The inference to every sufficiently large degree uses the already stated G-10 bound, while the every-degree rectangular progression uses G-11. Neither conclusion claims that all four-row partitions give gaps or that the ambient Kronecker multiplicity equals an orbit-closure multiplicity. The proof uses characteristic zero throughout the geometric conclusion, as intended.
