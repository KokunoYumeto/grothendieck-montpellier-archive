#!/usr/bin/env python3
"""Exact F_9 certificate for the ramified non-Picard base-change example.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
No external packages. F_9=F_3[a]/(a^2+1), encoded u+v*a as u+3*v.
B has ordered basis e0,e1,x,y, x=e0*x*e1, y=e1*y*e0, radical^2=0.
"""
from itertools import product
from json import dumps
from pathlib import Path
from time import perf_counter

started = perf_counter()


def fadd(z, w):
    return ((z % 3 + w % 3) % 3) + 3 * ((z // 3 + w // 3) % 3)


def fneg(z):
    return ((-z % 3) % 3) + 3 * ((-(z // 3)) % 3)


def fmul(z, w):
    u, v, s, t = z % 3, z // 3, w % 3, w // 3
    return ((u * s - v * t) % 3) + 3 * ((u * t + v * s) % 3)


def fpow(z, n):
    answer = 1
    while n:
        if n & 1:
            answer = fmul(answer, z)
        z = fmul(z, z)
        n //= 2
    return answer


def finv(z):
    assert z
    return fpow(z, 7)


def bmul(z, w):
    a, b, c, d = z
    e, f, g, h = w
    return (fmul(a, e), fmul(b, f),
            fadd(fmul(a, g), fmul(c, f)),
            fadd(fmul(b, h), fmul(d, e)))


def norm(z):
    return fmul(z[0], z[1])


def binv(z):
    a, b, c, d = z
    assert a and b
    n_inv = finv(fmul(a, b))
    return (finv(a), finv(b), fneg(fmul(c, n_inv)), fneg(fmul(d, n_inv)))


def S(z):
    a, b, c, d = z
    return b, a, d, c


t = 4  # 1+a


def T(z):
    a, b, c, d = z
    return a, b, fmul(t, c), d


def ST(z):
    return S(T(z))


def TS(z):
    return T(S(z))


basis = [tuple(1 if i == j else 0 for i in range(4)) for j in range(4)]
one = (1, 1, 0, 0)
zero = (0, 0, 0, 0)
elements = list(product(range(9), repeat=4))
units = [z for z in elements if norm(z)]
squares = sorted({fmul(c, c) for c in range(1, 9)})
assert t not in squares and fpow(t, 4) == 2 and fpow(t, 8) == 1

# Associativity on a basis suffices by trilinearity over F_9.
assert all(bmul(bmul(a, b), c) == bmul(a, bmul(b, c))
           for a, b, c in product(basis, repeat=3))
assert all(bmul(one, z) == z == bmul(z, one) for z in elements)
assert all(bmul(z, binv(z)) == one == bmul(binv(z), z) for z in units)
assert all(bmul(x, y) == zero for x, y in product(basis[2:], repeat=2))

# F_9-linearity and the basis multiplication table certify automorphisms.
for functor in [S, T]:
    assert functor(one) == one
    assert all(functor(bmul(a, b)) == bmul(functor(a), functor(b))
               for a, b in product(basis, repeat=2))
    assert len({functor(z) for z in elements}) == len(elements)
    assert all(norm(functor(z)) == norm(z) for z in elements)

# Centre calculation enumerates every algebra element, including the radical.
centre = [z for z in elements if all(bmul(z, a) == bmul(a, z) for a in basis)]
assert centre == [(c, c, 0, 0) for c in range(9)]

d = (t, 1, 0, 0)
assert norm(d) == t
assert all(TS(a) == bmul(bmul(d, ST(a)), binv(d)) for a in elements)

# An intertwiner b satisfies b ST(a)=TS(a)b on all a; basis tests suffice.
intertwiners = [b for b in units
                if all(bmul(b, ST(a)) == bmul(TS(a), b) for a in basis)]
expected = [(fmul(c, t), c, 0, 0) for c in range(1, 9)]
assert sorted(intertwiners) == sorted(expected)
assert all(norm(b) != 1 for b in intertwiners)
norms = sorted({norm(b) for b in intertwiners})
assert norms == sorted(set(range(1, 9)) - set(squares))

result = {
    "title": "Ramified F_9 fibre: determinant-rigidified autoequivalences do not commute",
    "field": "F_3[a]/(a^2+1); u+v*a encoded as u+3*v",
    "t": t,
    "t_expression": "1+a",
    "t_order": 8,
    "nonzero_squares": squares,
    "algebra_element_count": len(elements),
    "unit_count": len(units),
    "centre": centre,
    "S_basis_images": [S(a) for a in basis],
    "T_basis_images": [T(a) for a in basis],
    "ST_basis_images": [ST(a) for a in basis],
    "TS_basis_images": [TS(a) for a in basis],
    "inner_conjugator_d": d,
    "norm_d": norm(d),
    "all_intertwiners": intertwiners,
    "intertwiner_norms": norms,
    "norm_one_intertwiner_count": sum(norm(b) == 1 for b in intertwiners),
    "checks": [
        "Associative multiplication, identity, unit inverses verified",
        "Radical square zero verified on its basis",
        "S,T F_9-linear algebra automorphisms preserve the norm of every element",
        "Centre enumerated exhaustively: only scalar multiples of the identity",
        "TS=Int(d)ST verified on every element",
        "Every invertible natural intertwiner enumerated; precisely c*d",
        "All intertwiner norms nonsquare, so no determinant-preserving isomorphism"
    ],
    "runtime_seconds": round(perf_counter() - started, 6),
}
target = Path(__file__).resolve().parents[1] / "output"
target.mkdir(parents=True, exist_ok=True)
(target / "verify_ramified_picard_counterexample.json").write_text(dumps(result, indent=2) + "\n")
print(dumps(result, indent=2))
