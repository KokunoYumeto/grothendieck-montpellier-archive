"""Exact, dependency-free checks for the independently derived Kummer examples."""

import json

P = 17
ZERO = (0, 0)
ONE = (1, 0)
T = (0, 1)


def a_add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def a_neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def a_mul(x, y):
    a, b = x
    c, d = y
    return ((a * c - b * d) % P, (a * d + b * c - b * d) % P)


def power(value, exponent, multiply, one):
    answer = one
    while exponent:
        if exponent & 1:
            answer = multiply(answer, value)
        value = multiply(value, value)
        exponent >>= 1
    return answer


def a_pow(x, exponent):
    return power(x, exponent, a_mul, ONE)


def sigma(x):
    # T -> T^2 = -1-T.
    return ((x[0] - x[1]) % P, (-x[1]) % P)


def quotient_multiplication(c):
    """Coefficients in A, with X^3+c[2]X^2+c[1]X+c[0]=0."""
    def multiply(x, y):
        z = [ZERO for _ in range(5)]
        for i in range(3):
            for j in range(3):
                z[i + j] = a_add(z[i + j], a_mul(x[i], y[j]))
        for k in (4, 3):
            for j in range(3):
                z[k - 3 + j] = a_add(z[k - 3 + j], a_neg(a_mul(z[k], c[j])))
        return tuple(z[:3])
    return multiply


def v_add(x, y):
    return tuple(a_add(a, b) for a, b in zip(x, y))


def v_scale(x, a):
    return tuple(a_mul(a, b) for b in x)


V_ONE = (ONE, ZERO, ZERO)
X = (ZERO, ONE, ZERO)

assert all((z * z + z + 1) % P for z in range(P))
f_values = [(z**3 + z**2 - 2*z - 1) % P for z in range(P)]
g_values = [(z**3 - 3*z - 7) % P for z in range(P)]
assert all(f_values) and all(g_values)
assert pow(P, 2, 7) == 2
assert (pow(P, 1, 3), pow(P, 2, 3)) == (2, 1)
assert P**2 - 1 == 32 * 9

u = (9, 11)
assert a_pow((1, 3), 32) == u
assert a_pow(u, 3) == T
assert a_pow(u, 9) == ONE
assert sigma(u) == a_pow(u, 8) == (15, 6)
assert a_add(u, a_pow(u, 8)) == (7, 0)
assert a_pow((1, 16), 32) == T
assert a_add(a_add(a_pow(u, 2), a_mul((10, 0), u)), ONE) == ZERO
assert a_add(a_add(a_pow(u, 6), a_pow(u, 3)), ONE) == ZERO
assert min(j for j in range(1, 7) if pow(P, j, 27) == 1) == 6

# Check the forward Kummer descent identity in A[X]/(X^3-u).
b_mul = quotient_multiplication((a_neg(u), ZERO, ZERO))
b_pow = lambda x, n: power(x, n, b_mul, V_ONE)
assert b_pow(X, 27) == V_ONE
assert b_pow(X, 9) != V_ONE
assert v_add(v_add(b_pow(X, 6), v_scale(b_pow(X, 3), (10, 0))), V_ONE) == (ZERO, ZERO, ZERO)
beta = v_add(X, b_pow(X, 26))
assert v_add(v_add(b_pow(beta, 3), v_scale(beta, (14, 0))), ((10, 0), ZERO, ZERO)) == (ZERO, ZERO, ZERO)

# Check the reverse resolvent for the displayed Gaussian-period cubic.
c_mul = quotient_multiplication(((16, 0), (15, 0), ONE))
c_pow = lambda x, n: power(x, n, c_mul, V_ONE)
v = (ZERO, ZERO, ZERO)
for i in range(3):
    v = v_add(v, v_scale(c_pow(X, P**i), a_pow(T, (-i) % 3)))
w = c_pow(v, 3)
assert w[1:] == (ZERO, ZERO)
assert a_pow(w[0], (P**2 - 1) // 3) == a_pow(T, 2)
y = a_pow(w[0], 32)
projected = a_mul(a_pow(y, 5), a_pow(sigma(y), 4))
assert a_pow(projected, 3) == a_pow(T, 2)
assert a_pow(projected, 9) == ONE
assert sigma(projected) == a_pow(projected, 8)

# Independently check the raw-resolvent vanishing counterexample over F_7.
assert set(pow(z, 3, 7) for z in range(1, 7)) == {1, 6}
assert (1 + 4 * 4 + 2 * 2) % 7 == 0

# The small-coordinate route: u+T is a noncube exactly when the
# explicit cubic Y^3-3Y-(2-3/(u^2-u+1)) has no F_17 root.
affine_character_counts = {ONE: 0, T: 0, a_pow(T, 2): 0}
affine_good_parameters = []
for parameter in range(P):
    character = a_pow((parameter, 1), (P**2 - 1) // 3)
    affine_character_counts[character] += 1
    norm = (parameter * parameter - parameter + 1) % P
    coefficient = (2 - 3 * pow(norm, -1, P)) % P
    has_root = any((z**3 - 3*z - coefficient) % P == 0 for z in range(P))
    assert has_root == (character == ONE)
    if not has_root:
        affine_good_parameters.append(parameter)
assert sorted(affine_character_counts.values()) == [5, 6, 6]
assert affine_good_parameters[0] == 3
assert a_pow((3, 1), (P**2 - 1) // 3) != ONE
assert 3**2 - 3 + 1 == 7
assert all((z**3 - 3*z - 4) % P for z in range(P))
for small_candidate in (T, (1, 1), (1, 16), (2, 1)):
    assert a_pow(small_candidate, (P**2 - 1) // 3) == ONE

print(json.dumps({
    "status": "all exact checks passed",
    "p": P,
    "r": 3,
    "s": 2,
    "a": 2,
    "auxiliary_prime": 7,
    "gaussian_period_cubic_values": f_values,
    "kummer_descent_cubic_values": g_values,
    "maximal_teichmuller_unit": u,
    "unit_cubed": a_pow(u, 3),
    "selected_partial_factor_Phi_9": "X^2-7X+1",
    "selected_irreducible_factor_Phi_27": "X^6-7X^3+1",
    "reverse_resolvent_w": w[0],
    "reverse_resolvent_maximal_unit": projected,
    "failed_cyclotomic_unit_projection": a_pow((1, 16), 32),
    "raw_resolvent_counterexample": {"p": 7, "f": "X^3-2", "zeta_3": 4, "resolvent": 0},
    "affine_character_counts": {str(key): value for key, value in affine_character_counts.items()},
    "first_affine_noncube_parameter": affine_good_parameters[0],
    "small_candidate_cubic": "Y^3-3Y-4"
}, indent=2))
