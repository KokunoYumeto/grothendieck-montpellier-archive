# Locally finite Frobenius can gain a non-torsion eigenvalue after completion

This is a failed-approach diagnostic for B1, not a counterexample to a
cycle conjecture. The proposed implication was: every Milnor symbol over
an algebraic closure of a finite field uses only finitely many constants,
so its arithmetic Frobenius orbit is finite; therefore its completed
cohomology cannot have an eigenvalue q other than a root of unity.
The implication from local finiteness to the assertion about completion
is false even for a torsion-free module.

Let

    M = C_lc(Z_3,Z),        (Fh)(x)=h(x+1),

where the target Z is discrete. Equivalently, M is the direct limit of
the free groups of integer-valued functions on Z/3^s, with transition
maps given by inflation. Every element h factors through some Z/3^s,
so F^(3^s)h=h. The same holds for every element of M tensor Q. Thus

    ker(F-4 : M tensor Q -> M tensor Q)=0:

if Fh=4h, then (4^(3^s)-1)h=0, hence h=0.

The 3-adic completion has a different answer. Reduction gives

    M/3^r M = C_lc(Z_3,Z/3^r).

Surjectivity follows by choosing integer lifts on the finitely many
clopen fibres of a locally constant function; its kernel is exactly
3^r M. Compatible finite-valued continuous functions are the same as
continuous functions to Z_3, so

    M_hat_3 = lim_r M/3^r M = C(Z_3,Z_3).

This identification is F-equivariant. Define, for r>=1,

    h_r(x) = 4^(x mod 3^(r-1)) mod 3^r.

The elementary valuation identity

    v_3(4^(3^s)-1)=s+1

follows by induction from 4=1+3: if u=1+3^a b with a>=1 and 3 not
dividing b, then u^3-1=3^(a+1)b(1+3^a b+3^(2a-1)b^2), and the last
factor is a 3-adic unit. Consequently h_(r+1) reduces to h_r, and

    h_r(x+1)=4 h_r(x) mod 3^r,

including at the wraparound of the period. The resulting h in M_hat_3
is the continuous function ordinarily denoted 4^x. It satisfies

    Fh=4h,                  h(0)=1.

In particular h is nonzero and not 3-primary torsion. It remains a
nonzero4-eigenvector in M_hat_3 tensor Q_3, although M tensor Q has none.
Every individual finite-level permutation representation before the
direct limit has only roots of unity as rational eigenvalues.

The exact finite certificate `code/frobenius_completion_counterexample.py`
checks periods, wraparound eigenrelations and compatible reductions
through r=10, as well as the valuation formula through s=12. Its output
is `output/frobenius_completion_counterexample.txt`. The proof above,
not those finitely many tests, proves the infinite assertion.

## Consequence for the B1 attack

The algebraic argument from finite Frobenius orbits of coefficients or
symbols to a completed q-eigenspace vanishing requires an additional
uniform control on the integral module or on the allowed ramification.
Torsion-freeness alone does not supply it. The completed module in this
example is not claimed to be the Milnor K-group or the birational
cohomology group occurring in B1. The degree-four projective-space and
threefold Chow-phantom gates remain unchanged.

## A distinction needed for residue arguments

This example uses **inflation/refinement** maps between finite permutation
lattices. It is not the completion of a direct sum of fixed finite
Frobenius orbits. If instead

    P = direct_sum_O Z[O]

for fixed finite F-orbits O, its 3-adic completion injects into
product_O Z_3[O] by the coefficient maps. For a q-eigenvector with
q not a root of unity, projection to an orbit of size d gives
(q^d-1)v_O=0, hence v_O=0. All coefficients vanish, so v=0.
This retains the elementary vanishing on a divisor permutation module.
The issue in an attempted higher Gersten argument is the unramified
kernel and the actual transition maps, not a failure of this particular
permutation-module calculation.

Root independently checked the mathematical construction and this
distinction. Part D read the complete first proof and passed it, while
explicitly not claiming a separate inspection of its finite script/output.
Those actual check scopes are recorded in the event ledger.
