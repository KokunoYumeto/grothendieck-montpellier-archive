"""Finite checks for the November conversation and its consequences.

Run with Python and SymPy. The input is the 132-row table supplied in the
GCT consult, before any specialization. An alternate path can be passed.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


NAMES = ["mu", "Sigma"] + [
    f"g{cell}_{word}" for cell in (1, 2) for word in ("1", "2", "12", "21")
]
DEFAULT_TABLE = (
    Path.home() / "Documents/reports_20261120/split_zero/consults"
    / "E4_scripts/e3_constants.json"
)


def grading_checks(table):
    v = sp.Symbol("v")
    source = json.loads(table.read_text(encoding="utf-8-sig"))
    assert len(source) == 132
    counts = {}
    for label, polynomial, degrees, modulus, last in (
        ("sign_point", v**2 + 1, [0, 3, 1, 1, 2, 2, 3, 3, 0, 0], 6, 6),
        ("cubic_point", v**2 + v + 1, [0, 2] + [1] * 8, None, 0),
        ("other_square_root_at_cubic_point", v**2 - v + 1, [0, 2] + [1] * 8, None, 0),
    ):
        relations = []
        for entry in source:
            numerator, denominator = sp.fraction(sp.cancel(sp.sympify(entry["c"], locals={"v": v})))
            assert sp.gcd(denominator, polynomial, v) == 1
            if sp.rem(numerator, polynomial, v) == 0:
                continue
            if last == 0 and entry["b"] != "mu" and entry["bp"] != "mu":
                assert entry["bpp"] == "Sigma" and sp.rem(numerator-denominator, polynomial, v) == 0
            relation = [0] * len(NAMES)
            for key, sign in (("b", 1), ("bp", 1), ("bpp", -1)):
                relation[NAMES.index(entry[key])] += sign
            difference = sum(r * d for r, d in zip(relation, degrees))
            assert (difference % modulus if modulus else difference) == 0
            relations.append(relation)
        diagonal = [abs(int(n)) for n in smith_normal_form(sp.Matrix(relations), domain=sp.ZZ).diagonal()]
        assert diagonal == [1] * 9 + [last]
        counts[label] = {"surviving_coefficients": len(relations), "smith_diagonal": diagonal}
    # The nine nonunit basis elements are forced into degree zero everywhere
    # else by the two-sided products with Sigma, checked as identities in v.
    D = (v + 1/v)**2
    sigma_products = {}
    for item in source:
        if item["b"] == "Sigma":
            assert item["bpp"] == "Sigma"
            sigma_products[item["bp"]] = sp.sympify(item["c"], locals={"v": v})
    assert set(sigma_products) == set(NAMES)
    for name in NAMES:
        if name == "mu":
            expected = 1
        elif name == "Sigma":
            expected = 4 * D**2 * (D-1)**2
        else:
            cell, word = name.split("_")
            expected = D**(len(word)-1) * (4*D*(D-1) if cell == "g1" else D**2*(D-1))
        assert sp.cancel(sigma_products[name]-expected) == 0
    return counts


def finite_actions():
    infinity = 23
    def permutation(a, b, c, d):
        def image(x):
            num, den = (a, c) if x == infinity else (a*x+b, c*x+d)
            return infinity if den % 23 == 0 else num*pow(den, -1, 23) % 23
        return tuple(image(i) for i in range(24))

    identity = tuple(range(24))
    generators = [permutation(12, 5, 1, 12), permutation(1, 7, 3, 22)]
    group, todo = {identity}, [identity]
    while todo:
        g = todo.pop()
        for h in generators:
            gh = tuple(g[h[i]] for i in identity)
            if gh not in group:
                group.add(gh)
                todo.append(gh)
    assert len(group) == 12
    assert all(all(g[i] != i for i in identity) for g in group if g != identity)
    golay_orbits = {frozenset(g[i] for g in group) for i in identity}
    assert sorted(map(len, golay_orbits)) == [12, 12]
    c = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    swap = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(3), sp.eye(3)),
                            sp.Matrix.hstack(sp.eye(3), sp.zeros(3)))
    graph = sp.Matrix.vstack(sp.eye(3), reflection)
    assert reflection*c*reflection == c.inv()
    assert graph*c == sp.diag(c, c.inv())*graph and graph*reflection == swap*graph
    assert graph.T*swap*graph == 2*reflection and (c-c.inv()).rank() == 2
    counts = Counter()
    for signs in product((1, -1), repeat=3):
        if signs[0] * signs[1] * signs[2] != 1:
            continue
        for winding in range(3):
            block = sp.diag(*signs) * c**winding
            u = int((c**winding).trace())
            t = int(block.trace())
            j = u + 8*t
            leech = 2*(u+3*t)
            assert j - (leech-u) == 2*t
            counts[(u, t, j, leech)] += 1
    assert sorted(counts.values()) == [1, 3, 8]
    # The trace obstruction separates as the diagonal plus the sum-zero
    # plane over Z/4. Rotation on that plane obeys 1+C+C^2=0.
    diag = set()
    plane = set()
    for t in product(range(4), repeat=3):
        a = sum(t)*3 % 4
        w = tuple((x-a) % 4 for x in t)
        assert sum(w) % 4 == 0 and all((a+y) % 4 == x for x, y in zip(t, w))
        diag.add(a)
        plane.add(w)
    assert (len(diag), len(plane)) == (4, 16)
    return {str(k): n for k, n in sorted(counts.items())}


def quartic_and_shell():
    x = sp.Symbol("x")
    f = sp.Poly(x**4 + 8*x + 12, x)
    assert f.is_irreducible and f.discriminant() == 576**2
    cubic = sp.Poly(x**3-3*x-1, x)
    assert cubic.is_irreducible and cubic.discriminant() == 81
    assert sp.QQ.alg_field_from_poly(f, "alpha").discriminant() == 5184
    assert sp.QQ.alg_field_from_poly(cubic, "z").discriminant() == 81
    assert sp.rem(x**8-x, cubic.as_expr(), x) == 28*x**2+26*x+6
    prime_examples = {}
    for p in sp.primerange(5, 200):
        factors = sp.Poly(f, x, modulus=p).factor_list()[1]
        kind = tuple(sorted(poly.degree() for poly, m in factors for _ in range(m)))
        prime_examples.setdefault(str(kind), int(p))
        roots = [i for i in range(p) if cubic.eval(i) % p == 0]
        assert len(roots) == (3 if p % 9 in (1, 8) else 0)
        assert sum(int(sp.legendre_symbol(i,p)) for i in roots) == kind.count(1)-1
    assert len(prime_examples) == 3
    weight = Counter(int(d) % 27 for d in sp.divisors(73*25))
    units = [r for r in range(27) if gcd(r,27) == 1]
    def correlation(g):
        return sum(weight[r]*weight[g*r % 27] for r in units)
    assert [correlation(g) for g in (1, 10, 19, 26)] == [6, 3, 3, 0]
    norm = sum(Fraction(sum(weight[g*r % 27] for g in (1, 10, 19)), 3)**2 for r in units)
    assert (3*norm-correlation(1))/2 == correlation(10)
    assert {n*n % 840 for n in range(840) if gcd(n,840)==1} == {1,121,169,289,361,529}
    return prime_examples


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TABLE
    print(json.dumps({"gradings": grading_checks(path), "characters_U_T_J_Leech": finite_actions(),
                      "quartic_factor_degrees_first_prime": quartic_and_shell()}, indent=2))
