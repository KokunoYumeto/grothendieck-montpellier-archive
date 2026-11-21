# Independent algebraic checks for the uniform border attempt

Run CUE_GCT_20261121_R1; root, GPT-6 Astra Pro; effort not exposed.
These are intermediate proof calculations for the still-open uniform R25
antecedent. They do not assert its rank or a new untested-size dimension.

## One-path q-Vandermonde identity

Let q be a primitive mth root, K_l(X,Y)=prod_(j=1)^l(X−q^jY), and
F_k=K_k(x,y)K_(m−1−k)(z,y), 0<=k<m. For a,c>=0 with a+c<=m−1,
the coefficient of x^a z^c y^(m−1−a−c) in q^(−k(k+1))F_k equals

(-1)^a q^(a(a−1)/2) X^(−a)
prod_(j=−a+1)^c(1−q^j X) / ((q;q)_a(q;q)_c), evaluated at X=q^k.

Independent derivation: expand the two products by Gaussian binomial
coefficients. The second binomial becomes
(-1)^c q^(−ck−c(c+1)/2) prod_(j=1)^c(1−q^(k+j))/(q;q)_c.
After the factor q^(−k(k+1)), the remaining exponent is
−ka+a(a−1)/2+m(m−1)/2−m(k+c). Since
q^(m(m−1)/2)=(-1)^(m−1), this gives the displayed sign and exponent.
If a>k or c>m−1−k, one factor on the right is zero, so the formula
also covers those cases rather than requiring a separate extension.

Therefore summing with q^(tk) extracts one Laurent coefficient. If
there is a representative t' congruent to t modulo m in [-c,a], then
the sum is

m(-1)^t' q^(t'(t'−1)/2)
[a+c choose a−t']_q / ((q;q)_a(q;q)_c).

If there is no such representative it is zero. The representative
is unique since a+c<=m−1. All denominators are nonzero because their
indices are less than m. This explicitly handles the wrap cases.

## First-family normalized coefficient

For the balanced covariant family proposed by rectangular, put
X=q^A,Z=q^C and
W=m(q;q)_(A+C−1)/((q;q)_A^2(q;q)_C^2).
In the interior range where these denominators and the three
unwrapped Vandermonde terms are defined, the contributions to a_0
from Vx,Vy,Vz are respectively

- Vx W(1−X)^2;
- −q Vy W(1−XZ)(1−X)/(1−qZ);
- q^3 Vz W(1−X)(1−X/q)(1−Z)/(1−qZ).

These follow directly by taking (a,c,t)=(A−1,C,0),(A,C,1),
(A,C−1,2), respectively, with the extra q^t from j=k+1.
This independently confirms the first-family formula. It does not
resolve its exceptional endpoints or the Hessian-family minors.

## Two-arc factorization for a Hessian column

For a cyclic matrix with diagonal ell_i and upper cyclic entry beta_i,
and general linear u,v, the R25 column t_0 has the polynomial identity

t_0 = 2 sum_(k=1)^(m−1) u_k L_k R_k,

where

L_k = sum_(j=1)^k v_j
       (prod_(r=1)^(j−1) ell_r)(prod_(r=j)^(k−1) beta_r),

R_k = v_0 prod_(r=k+1)^(m−1) ell_r
    + sum_(j=k+1)^(m−1) v_j
       (prod_(r=k+1)^(j−1) ell_r)(prod_(r=j)^(m−1) beta_r).

Empty products are one. To derive it, differentiate the coefficient
of t^2 in per(A+tuv^T) in u_0. The other selected row is k. Removing
rows0,k cuts the bipartite cycle into two paths; a matching exists
exactly when the two removed columns lie in the two respective arcs
{1,...,k} and {k+1,...,m−1,0}. Every resulting matching is unique,
and its product is the product of the indicated left and right path
terms. The two assignments of the rank-one entries give the factor2.
The degrees are degL_k=k, degR_k=m−k, hence degt_0=m+1, as required.

The counterpart for t'_0 follows by transposition with the explicitly
shifted lower-cycle indexing. That index translation has not yet been
written out here. A q-Vandermonde collapse of the two-arc expression
and a uniform nonzero characterwise minor remain work to do.
