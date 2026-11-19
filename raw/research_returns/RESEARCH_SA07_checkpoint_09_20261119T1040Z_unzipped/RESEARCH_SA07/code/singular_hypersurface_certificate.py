"""Exact polynomial certificate for the nodal normalization in F.3.14.

The cohomology and general finite-projection arguments are proofs in F_audit.tex.
This script checks the particular polynomial morphism and its projective charts.
Only integer arithmetic is used; there are no external dependencies.
"""

def add(a, b):
    out = dict(a)
    for exponent, coefficient in b.items():
        out[exponent] = out.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}

def neg(a):
    return {exponent: -coefficient for exponent, coefficient in a.items()}

def mul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            exponent = (i+k, j+ell)
            out[exponent] = out.get(exponent, 0) + c*d
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}

def power(a, n):
    result = {(0, 0): 1}
    for _ in range(n):
        result = mul(result, a)
    return result

def evaluate(a, u, v):
    return sum(c * u**i * v**j for (i, j), c in a.items())

u, v = {(1, 0): 1}, {(0, 1): 1}
factor = add(power(u, 2), neg(power(v, 2)))
x, y, z = mul(v, factor), mul(u, factor), power(v, 3)
relation = add(mul(power(y, 2), z), neg(mul(power(x, 2), add(x, z))))
assert relation == {}
print('PASS: y^2*z - x^2*(x+z) vanishes identically after substitution.')

# The two chart assertions exhaust P^1 over every characteristic-zero field.
assert z == {(0, 3): 1}
assert {e: c for e, c in y.items() if e[1] == 0} == {(3, 0): 1}
assert {e: c for e, c in x.items() if e[1] == 0} == {}
assert {e: c for e, c in z.items() if e[1] == 0} == {}
print('PASS: v!=0 gives z=v^3!=0; v=0 gives y=u^3!=0 for [u:v] in P^1.')

assert add(mul(y, v), neg(mul(x, u))) == {}
print('PASS: y*v=x*u, giving the rational inverse u/v=y/x on x!=0.')

for sign in [-1, 1]:
    assert tuple(evaluate(a, sign, 1) for a in [x, y, z]) == (0, 0, 1)
assert tuple(evaluate(a, 1, 0) for a in [x, y, z]) == (0, 1, 0)
assert add(power(u, 2), {(0, 0): -1}) == mul(add(u, {(0, 0): -1}), add(u, {(0, 0): 1}))
print('PASS: the node has exactly u/v=+1,-1; [1:0] maps to [0:1:0].')
print('All F.3.14 polynomial and projective-chart certificates passed.')
