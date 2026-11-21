# G041 working construction — full report and verification active

At 05:44 UTC on21November2026, the active root route is the finite
multiple-coinvariant numerator for every fixed tail length ell.
No completed G041 theorem has yet been entered in QUESTIONS.tsv.

Let W=h_m, N=binom(m,2), I=Q[e2,...,em], Q_m(z)=prod_(j=2)^m(1-z^j).
The actual tensor-word map identifies P(E tensor Q^ell) with
Q[x1,...,xell] tensor-powered m, with literal S_m slot permutations.
Schur–Weyl identifies the nu multiplicity with the Schur functor on
that graded polynomial alphabet. Removing the ell mean coordinates
gives Hilbert series

    prod_i(1-z_i) s_nu[prod_i(1-z_i)^(-1)].

The averaged coinvariant section identifies each P(W) with I tensor
H_m, and H_m has degrees0..N. Therefore the actual numerator

    F_nu(z)=prod_i prod_(j=1)^m(1-z_i^j)
             s_nu[prod_i(1-z_i)^(-1)]

has each coordinate degree at most N and nonnegative integer
coefficients. Compute it in Q[z1,...,zell]/(z1^(N+1),...,zell^(N+1)):
power sums p_d=prod_i(1-z_i^d)^(-1), Newton recursion for h_j to2m,
then Jacobi–Trudi. Use division-free/Faddeev characteristic recursion
for the determinant, dividing only the known exact integer coefficients
by the recursion index; no subset/permutation determinant algorithm
in varying m. The array has (N+1)^ell coefficients. For fixed ell,
all operations and their coefficient heights are polynomial in m.

Weight multiplicities at any binary exponent vector v are obtained
from the finite convolution of F with the ell separate 1/Q_m series,
whose shifted coefficients use the checked Bostan–Mori procedure.
For a dominant tail alpha of length≤ell, multiply by the GL_ell
alternant: sum_(sigma in S_ell) sign(sigma) H(alpha+delta-sigma delta).
This is its exact highest multiplicity. The number of permutations
depends only on ell; no variable degree is expanded at runtime.

Stable flag/mean maps identify this with the original plethysm at
lambda=(mn-|alpha|-(m-1)t, alpha1+t,...,alphaell+t,t^(m-1-ell)),
n≥alpha1+t, with effective label nu=mu or mu transpose according to t.
The full proof must state the exact source locators, actual Young/mean
maps, bit bounds for the entire circuit, zero/empty-tail endpoints,
and the explicit-m encoding qualification. Root is implementing
this circuit and will compare against independent cycle averages
and original plethysms before completion. Archive is independently
challenging the identity and complexity.

One positive-polytope consequence uses the circuit's computed
nonnegative integer as the endpoint of an interval. That arithmetic
preprocessing must be stated explicitly; it uses no coefficient
oracle. The rational comparison with the original multiplicity
space can use its ordered primitive-Young nullspace basis, as in
T067. The direct geometric multivariate lattice construction remains
a separate question and is not silently replaced in the record.
