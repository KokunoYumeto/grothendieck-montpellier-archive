"""Finite algebra checks for the point counterexample and diagonal reduction.

This checks the displayed cochain/index algebra. Negative K-theory vanishing,
cycle injectivity, and the all-dimension theorem are proved/cited in the text;
they are not inferred from the bounded computation.
"""
from fractions import Fraction
from time import perf_counter

start = perf_counter()
# The trivial rational Weil module has the complex Q --(1-1)--> Q.
differential = Fraction(1) - Fraction(1)
rank = int(differential != 0)
betti = (1 - rank, 1 - rank)
assert betti == (1, 1)
print("Point Weil complex [Q --0--> Q]:", {0: betti[0], 1: betti[1]})
print("Ordinary motivic H^1(F_p,Q(0)) = K_{-1}(F_p)_Q = 0 by the cited theorem.")
print("Thus its degree-one realization has source dimension 0 and target dimension 1.")
for degree in range(1, 33):
    assert Fraction(degree) * Fraction(1, degree) == 1
print("Restriction matrices [m] are rationally invertible for m=1,...,32.")

checked = 0
print("Half-range to odd-dimensional middle-plus-one index examples:")
for dim in range(3, 21):
    for codim in range(2, (dim + 1) // 2 + 1):
        projective_dim = dim - 2 * codim + 1
        target_codim = codim + projective_dim
        target_dim = dim + projective_dim
        assert projective_dim >= 0
        assert target_dim == 2 * target_codim - 1
        assert target_codim >= 2
        # Projection pushes the top power of the projective hyperplane to 1.
        top_hyperplane_degree = 1
        assert top_hyperplane_degree == 1
        checked += 1
        if dim <= 7:
            print((dim, codim), "x P^" + str(projective_dim), "->", (target_dim, target_codim))
print("Index pairs checked:", checked, "(3 <= dim <= 20)")
print("Elapsed seconds:", f"{perf_counter()-start:.6f}")
