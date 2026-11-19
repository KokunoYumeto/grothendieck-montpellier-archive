# Independent audit of the actual formal-leaf size and arithmetic type

19 November 2026. Auditor: OpenAI GPT-6 Astra, elliptic_splitting.
Audited file: `work/H1_adelic_formal_leaf_audit.md`, sections1--4.
Verdict: **Pass**, with the exact stated algebraic-complement scope.
No conclusion about algebraicity or transcendence of the actual non-CM h.

## 1. Integral graph and first nonintegral coefficient

Fix the one K-defined etale coordinate pair X,Y and invariant D=D_a
with DX(e)=1,DY(e)=0. There is one finite excluded prime set, not a
new set depending on p: a smooth integral neighborhood, the coordinate
map and D all spread out there. D preserves its ring of regular
functions; evaluating D^nX,D^nY at the integral identity gives integral
numbers for every n.

At an unramified remaining place of characteristic p, X(t)=t+... and
Y(t) starts at degree2. Their coefficients through degree p-1 are
integral. Reversion of a series with unit linear coefficient is
polynomial with integer coefficients in the previous coefficients,
so the inverse X^{-1}(T) has integral coefficients through degree p-1.
For a term Y_j (X^{-1}(T))^j with j>=2, its degree-p coefficient only
uses inverse coefficients of index at most p-j+1<=p-1. Thus every such
contribution with j<p is integral. The j=p term contributes exactly
Y_p, and no linear Y term exists. Therefore

    [T^p]Y(X^{-1}(T)) = D^pY(e)/p! modulo O_v.

Reduction of D^p is an invariant derivation. Since D(e) spans the
horizontal tangent and DY(e)=0, the reduced line fails p-closure
exactly when D^pY(e) is nonzero in the residue field. It is then a
unit, and v_p(p!)=1 gives the exact valuation -1 of this coefficient.
No repeated differentiation of an arbitrarily changed coordinate
system is being assumed to be invariant: the invariant vector field
is fixed and its transverse contraction is evaluated in the chosen
coframe at e.

## 2. Geometric size

The integral shear (X,Y) -> (X,Y+X) is an automorphism with integral
inverse and determinant1. It changes the graph to T+phi(T), whose
linear coefficient is the unit1 and whose coefficient in degree p is
unchanged. This uses actual coordinate invariance of the geometric
size. The graph has positive convergence radius by the regular
p-adic differential equation, also implicit in the positive lower
bound of Bost--Chambert-Loir Proposition3.6.

Proposition3.5(2) expresses size by the first Newton-polygon slope.
The degree-p coefficient bounds that slope by log|p|_v/(p-1), giving
the required upper bound. Proposition3.6 gives the same lower bound
for any nonsingular integral foliation. Hence size is exactly
|p|_v^(1/(p-1)) at the specified nonclosed places. At p-closed
unramified places the stronger lower bound in Proposition3.6 applies.
This is size of the actual embedded graph, not an unproved equality
between size and the convergence radius of an arbitrary parametrization.

## 3. Adelic product and normalized arithmetic type

With BCL's normalization, |p|_v=p^(-d_v), d_v=[K_v:Q_p]. The entire
p-closed contribution to the negative logarithm of the size product
is between0 and d sum_p log(p)/(p(p-1)), a convergent series. The
nonclosed contribution is exactly its weighted harmonic sum. The
complementary upper harmonic density supplied by A.4.32 is positive,
so that sum is unbounded. Thus the product is zero. This disproves
A-analyticity for this actual algebraic-complement leaf; it is not
merely failure to verify a sufficient hypothesis.

For André, epsilon_v=d_v/d and |p|_v=p^(-epsilon_v). In the fixed
series phi the coefficient in degree p therefore contributes
log^+|b_p|_v=epsilon_v log p. For each n and any fixed lower prime
threshold, the defining sum for tau(phi) is at least the sum of these
contributions over nonclosed p<=n. Removing that fixed finite threshold
changes the latter lower bound by a constant divided by n.

Set theta_B(T)=sum_(p<=T,v in B) epsilon_v log p and
H_B(T)=sum_(p<=T,v in B) epsilon_v log p/(p-1). Partial summation,
with the bounded replacement of1/(p-1) by1/p, gives

    H_B(T)=theta_B(T)/T + integral_2^T theta_B(t)/t^2 dt + O(1).

If L=limsup theta_B(T)/T, then theta_B(t)<= (L+epsilon)t beyond a
fixed threshold. Division by logT in this identity gives
limsup H_B(T)/logT<=L. The all-place normalization has
sum_v epsilon_v=1 above each p, so the full harmonic sum is
logT+O(1). A.4.32 therefore gives limsup H_B(T)/logT>=1/(4d).
Consequently the exact definition on André printedp74 yields

    tau(phi)>=L>=1/(4d)>0.

Every density used here is upper; no upper density has been promoted
to a lower density. The original zero-tau hypothesis of Theorem5.4.3
therefore fails on this fixed graph. No equality with the arithmetic
type of a linear connection is used.

The archimedean observation also checks: apply BCL Proposition5.15
to the actual entire uniformization into the proved projective
compactification, restricted to discs of radius R. Its nonzero
derivative has canonical seminorm bounded by the capacitary norm
1/R; taking R to infinity gives zero. This does not change the finite
product computation.

## 4. Independent primary reading

Opened Bost--Chambert-Loir original arXiv math/0702593v3 in full:
https://arxiv.org/pdf/math/0702593 , webref turn564640158view0,
exact source find turn871892366view0. Read Proposition3.5 printed11--12,
Proposition3.6 printed12, Definition3.7 printed13, and Proposition5.15
printed33 in the retained original text.

Opened André's original publisher preview (115 PDF pages, not the
whole book):
https://api.pageplace.de/preview/DT0400.9783110198133_A19084047/preview-9783110198133_A19084047.pdf ,
webref turn564640158view1; exact definition refs turn871892366view1--2.
Visually inspected printed70,74,76, saved as
`work/sources_elliptic/andre2004_visual_audit/p70.png`, `p74.png`,
`p76.png`. These show the epsilon_v normalization, exact tau order of
inf/limsup/sum/sup, and zero-tau hypothesis with the product of radii
in Theorem5.4.3. A small symbolic inversion certificate has been
requested from the authoring agent; the general proof above is complete.
