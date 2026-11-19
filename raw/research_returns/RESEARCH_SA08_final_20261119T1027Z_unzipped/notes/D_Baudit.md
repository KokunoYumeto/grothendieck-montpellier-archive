# Independent focused audit of B01/B03 and the discontinuous limit

GPT-6 Astra (OpenAI, ChatGPT Pro mode), SA08 D-agent, 2026-11-19.
Read sections/B_automorphisms.tex B-01 and B-03 in full.

B-01: The one-variable derivative is an actual module isomorphism
from the PD augmentation ideal to the whole polynomial PD algebra,
sending X^[j] to X^[j-1]. Thus the recursion Ai'=Ai-1 A1' with
Ai(0)=0 really forces Ai=gamma_i(A1), over arbitrary torsion bases.
The independent-variable commutators are exactly 2Bi(U)Bj(V)dUdV
and 2Bi(U)A'(V)dUdV. Since A has no constant X coefficient, the
coefficients of A' are exactly those of A with indices shifted.
Hence 2BiL is the precise coefficient ideal condition. The endpoint
PD condition is well typed because A(t') belongs to the given J'.
The same mixed identities repair the graded-Leibniz signs after
exterior degree is forgotten. Every monotone map pulls cumulative
coordinates back to another cumulative coordinate, 0, or t; therefore
all simplicial compatibility follows from the two endpoints and
one-variable formula. No flatness assumption was silently used.

B-03: For a continuous completed morphism with unit determinant,
the leading coefficient a1(T) is a unit, so the coefficient ideal
condition gives 2Bi=0. The derivation therefore factors through the
polynomial source modulo2, with target the 2-torsion module. The
binary presentation and characteristic2 derivative of y_m^2 give
arbitrary binary values c_m. Continuity is exactly c_m->0: in every
summand A^[n-2^m]c_m either m is large or the exponent is large.
The simultaneous T and cumulative-variable substitution has graded
weight-w action Delta^w; the complete recursive inverse therefore
requires only a unit Delta, not division by factorials. Removing
this even inverse leaves an exterior-filtration-raising operator,
whose nilpotence in simplex dimension n is at most n+1. Its finite
geometric inverse is continuous and respects all structure. No
mathematical flaw was found in these precise categories.

Discontinuous construction proposed and checked after that audit:
over F2 choose the continuous kernel automorphism Phi_N having only
binary coefficient c_N=1. Every completed simplex is a product of
finite discrete weight spaces, hence compact Hausdorff. For a fixed
nonprincipal ultrafilter U, the pointwise U-limit Phi exists on every
element. Addition, multiplication, differential and simplicial maps
are continuous, so the limit preserves every finite identity.
The closed exterior filtration retains (Phi-id)(F_ext^q) contained
in F_ext^(q+1). Thus Phi is a genuine automorphism, by the finite
geometric inverse in each simplex. It fixes every polynomial, but
s(X)=sum_m X^[2^m] is sent to s(X)+dX; it is therefore not continuous.

For the stronger infinite-order witness let
F_n(U1,...,Un)=sum_{m1<...<mn} product_j Uj^[2^mj]. Each finite Phi_N
can alter at most one slot, because the indices are distinct. For
any fixed output coefficient, as N tends to infinity the altered
slot can only be the last: any later unchanged slot would have a
fixed index greater than N, impossible eventually. Consequently
N(F_n)=F_(n-1)dU_n for N=Phi-id. Iterating gives
N^n(F_n)=dU1...dUn. In characteristic2 Phi^(2^r)=id+N^(2^r), so Phi
has infinite order over all simplex dimensions. This is a choice-
based infinite counterexample, not something a finite program can
certify or refute.

Finally the completed cycle argument does not require projectivity
of product k. Each NZ_w^i is bounded below, has projective k-terms,
and sole projective homology k in degree i. Splitting from the
bottom degree inductively gives an actual chain homotopy equivalence
with k[i]. Products of the chosen maps and homotopies give
N(product_w Z_w^i) chain-homotopy equivalent to (product_w k)[i].
Every strict degree-zero chain map between distinct concentrated
degrees is zero, so any simplicial k-linear map of these completed
cycle objects in different degrees is nullhomotopic, even if the
map is discontinuous. This is a statement in the chain homotopy
category, stronger than trying to deduce it from projectivity in
the derived category.
