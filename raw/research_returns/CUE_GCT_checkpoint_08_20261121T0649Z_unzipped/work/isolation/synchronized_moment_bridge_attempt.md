# Synchronized moment bridges: exact restricted repair and its limit

Status: a checked construction/attempt, not a new general ROABP result and not
an accepted numbered claim. Author: GPT-6 Astra Pro, effort not exposed,
agent `/root/isolation`, run `CUE-GCT-20261121-I`.

## Constant interfaces

Let `r,s >= 1`, and let `X^(1),...,X^(s)` be generic `r by r` matrices
whose entries are all distinct independent variables. Let `a,b` be constant
row/column boundaries and let `C_1,...,C_(s-1)` be arbitrary constant matrices.
Consider

`f = a X^(1) C_1 X^(2) ... C_(s-1) X^(s) b`.

Index matrix entries by `0,...,r-1`. Put

`p(S) = (1,S,...,S^(r-1))^T`,

`q(S) = (1,S^r,...,S^(r(r-1)))^T`.

Use the same substitution in every bridge:

`X^(h)_(ij) = S^(1+i+r*j)`.

Each bridge becomes `S p(S) q(S)^T`, so the image of `f` is exactly

`S^s (a p(S)) (q(S)^T b) product_h (q(S)^T C_h p(S))`.

The `r^2` monomials in the last scalar factor have pairwise distinct
exponents `r*j+i`, ranging from `0` to `r^2-1`. Thus this factor is nonzero
if and only if `C_h` is nonzero, over every field. Similarly the boundary
factors are nonzero exactly when the respective boundaries are nonzero.
Every nonzero original `f` has all these nonzero boundaries/interfaces,
and hence survives. Conversely, the displayed product shows that these
nonzero conditions suffice for the original generic-matrix word to be
nonzero. The final degree is at most `s*r^2`, and the largest variable
weight is `r^2`. A grid of `s*r^2+1` distinct values therefore hits the
class, using an extension when needed.

The map uses the known row/column label of each generic entry. It is
independent of the coefficients and interface ranks. It also tolerates
any order of the whole generic bridge blocks, because exactly the same
entry-label rule is used in each block. It does not cover arbitrary
regrouping or interleaving of the individual generic entry variables.
Constant left/right gauges can be absorbed into the boundaries and
interfaces. This is a restricted instance of familiar independent-entry
matrix-word isolation, not a historical novelty claim.

## Why the symmetric Hankel choice fails and asymmetry repairs it

For `r=2`, let `J=[[0,1],[-1,0]]`. It is invertible in every characteristic.
With `p=(1,S)^T`, one has `p^T J p=0`. Thus mapping both generic bridges
to the symmetric rank-one matrix `p p^T` kills

`e_1^T X J Y e_1 = X_00 Y_10 - X_01 Y_00`,

although this polynomial is nonzero. The asymmetric choice gives
`q^T J p=S-S^2`, which is nonzero over every field.

Within the specific class of univariate rank-one curves `p(S)q(S)^T`
that test *every* constant matrix interface, degree `r^2-1` is optimal:
the map `C -> q(S)^T C p(S)` must be injective on an `r^2`-dimensional
vector space. Polynomials of degree at most `d` have dimension `d+1`,
so `d>=r^2-1`. This is a restriction on that test architecture, not a
general hitting-set lower bound.

## Actual width-2r read-once implementation

Set

`T_h = product_(i,j) (I_(2r)+X^(h)_(ij) E_(i,r+j)) = [[I,X^(h)],[0,I]]`,

`D_h = [[0,0],[C_h,0]]`.

All products of two displayed upper-right matrix units vanish. Hence
the internal product can be taken in any entry order, and every variable
factor is invertible. Direct block multiplication gives

`(a,0) T_1 D_1 T_2 ... D_(s-1) T_s (0,b)^T = f`.

The constant resets have rank `rank(C_h) <= r`. Constants may be absorbed
into neighboring variable factors. Thus the construction includes an
actual width-`2r` ROABP subclass with arbitrarily many noncommuting
constant rank-`r` resets, with the known entry-grid promise stated above.

## Retained cut variables: a polynomial repair for two-variable interfaces

The same factorization is valid over `F(Z_1,...,Z_m)`. Suppose each entry
of each interface, and each entry of each boundary, is a polynomial of
individual degree at most the integer `delta>=1`, and each entire
interface/boundary depends on a fixed set of at most two cut variables.
These sets may overlap arbitrarily and need not be supplied to the map.

Choose `m` distinct primes `p_i>delta`, each at most a polynomial bound
`P=poly(m,delta)`, using the elementary prime bound already proved in I33.
Use a second parameter `U`, algebraically independent of `S`, and set
`Z_i=U^(p_i)`.

This substitution is injective on the space of all polynomials of
individual degree at most `delta` in any fixed pair of cut variables.
Indeed, if two monomials collide, then

`(a-a') p_i + (b-b') p_j = 0`,

where both differences have absolute value at most `delta`. Divisibility
by `p_i` forces `b-b'=0`, because `p_i>delta` and `p_i != p_j`; then
`a-a'=0`. The one-variable case is immediate. Consequently every nonzero
interface matrix and nonzero boundary remains nonzero over `F(U)`.
The distinct `S` exponents still encode its entries, so all scalar factors
above remain nonzero in `F[S,U]`. Their product remains nonzero despite
arbitrary overlap among the original cut-variable sets.

The image degree in `S` is at most `s*r^2`. There are `s-1` interfaces
and two boundaries, so its degree in `U` is at most

`B_cut = 2*delta*(s+1)*P`.

Thus a rectangular grid with

`(s*r^2+1)*(B_cut+1)`

points suffices. Equivalently, put `S=V^(B_cut+1)` and `U=V`.
The map on the bidegree box is injective because exponents
`a*(B_cut+1)+b` are distinct for `0<=b<=B_cut`. This gives one
polynomial-degree curve, with degree at most

`s*r^2*(B_cut+1)+B_cut`.

This restricted positive result is uniform in the unknown coefficients,
the unknown two-variable incidence sets, and the number of cuts. It is
not a theorem for arbitrary matrix bridges: the generic-entry bridge
promise is essential. In the read-once realization above, univariate
interfaces can each be placed in their own reset variable. Arbitrarily
overlapping bivariate interfaces are an algebraic class extension; no
read-once representation for every such overlapping instance is asserted.

## Two exact failures of the next proposed generalization

First, directly identifying the moment parameter with a retained cut
parameter is invalid. For `r=2`, take

`C(Z)=[[Z,-1],[0,0]]`.

Then `q(S)^T C(Z) p(S)=Z-S`, which is nonzero in the independent
parameters but becomes zero when `Z=S`. The original interface is
nonzero and has rank one. Thus even the asymmetric moment curve needs
either an independent cut parameter or a proved degree-separated encoding.

Second, the rank-one specialization is unavailable for general unit
bridges. If an `r by r` polynomial matrix `B(X)` has nonzero constant
determinant and `r>=2`, every polynomial or rational substitution at which
its entries are defined retains that same nonzero determinant. Hence no
such substitution can make `B` rank one. Products of unipotent factors
already have this property. Generic entry matrices admit rank-one
specializations, whereas these actual invertible ROABP bridges do not.

The restricted positive calculation therefore does not supply the
missing rank-r reset synchronization theorem. It identifies exactly
where scalar product closure succeeds (rank-one bridge images plus
injective interface tests) and why the same architecture cannot treat
all invertible internal words.
