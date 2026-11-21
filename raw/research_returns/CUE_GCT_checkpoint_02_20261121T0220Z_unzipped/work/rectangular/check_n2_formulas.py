"""Finite exact checks for R-10 and two algebraic identities used in the audit.

No numerical approximation and no claim to verify the general theorem.
Characters are computed independently from the cited formula by the
Murnaghan--Nakayama recursion, enumerating removable border strips.
"""
from functools import lru_cache
from fractions import Fraction
from math import factorial, comb
import json
from pathlib import Path


@lru_cache(None)
def partitions(n, maximum=None):
    if n == 0:
        return ((),)
    if maximum is None:
        maximum = n
    return tuple((first,) + tail
                 for first in range(min(n, maximum), 0, -1)
                 for tail in partitions(n-first, first))


@lru_cache(None)
def border_removals(shape, k):
    out = []
    for small in partitions(sum(shape)-k):
        if len(small) > len(shape):
            continue
        if any(x > shape[i] for i, x in enumerate(small)):
            continue
        cells = {(i, j) for i, row in enumerate(shape)
                 for j in range(small[i] if i < len(small) else 0, row)}
        if len(cells) != k or not cells:
            continue
        if any({(i+1, j), (i, j+1), (i+1, j+1)} <= cells
               for i, j in cells):
            continue
        frontier = [next(iter(cells))]
        seen = set(frontier)
        while frontier:
            i, j = frontier.pop()
            for neighbour in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if neighbour in cells and neighbour not in seen:
                    seen.add(neighbour)
                    frontier.append(neighbour)
        if seen == cells:
            out.append((small, (-1)**(len({i for i, _ in cells})-1)))
    return tuple(out)


@lru_cache(None)
def character(shape, cycles):
    if not cycles:
        return int(not shape)
    if not shape or sum(shape) != sum(cycles):
        return 0
    return sum(sign * character(small, cycles[1:])
               for small, sign in border_removals(shape, cycles[0]))


def z_of(cycles):
    out = 1
    for k in set(cycles):
        count = cycles.count(k)
        out *= k**count * factorial(count)
    return out


def square_cycles(cycles):
    out = []
    for k in cycles:
        out.extend([k//2, k//2] if k % 2 == 0 else [k])
    return tuple(sorted(out, reverse=True))


def schur_dimension(shape, n):
    shape = shape + (0,)*(n-len(shape))
    answer = Fraction(1)
    for i in range(n):
        for j in range(i+1, n):
            answer *= Fraction(shape[i]-shape[j]+j-i, j-i)
    assert answer.denominator == 1
    return answer.numerator


results = {"rectangular_cases": [], "ambient_dimensions": []}
checked_labels = 0
for d in range(1, 7):
    n = 2*d
    r = (d, d)
    table = []
    for cycles in partitions(n):
        value = character(r, cycles)
        table.append((cycles, z_of(cycles), value,
                      character(r, square_cycles(cycles))))
    ordinary = {}
    symmetric = {}
    exterior = {}
    for shape in partitions(n):
        g = gp = gm = Fraction(0)
        for cycles, z, value, squared_argument in table:
            chi = character(shape, cycles)
            g += Fraction(chi * value**2, z)
            gp += Fraction(chi * (value**2+squared_argument), 2*z)
            gm += Fraction(chi * (value**2-squared_argument), 2*z)
        even = len(shape) <= 4 and all(x % 2 == 0 for x in shape)
        odd = len(shape) == 4 and all(x % 2 == 1 for x in shape)
        assert (g, gp, gm) == (int(even or odd), int(even), int(odd)), (d, shape)
        checked_labels += 1
        if g:
            ordinary[str(shape)] = int(g)
        if gp:
            symmetric[str(shape)] = int(gp)
        if gm:
            exterior[str(shape)] = int(gm)
    results["rectangular_cases"].append({
        "d": d, "partitions_checked": len(partitions(n)),
        "ordinary": ordinary, "symmetric": symmetric, "exterior": exterior})

for d in range(11):
    actual = sum(schur_dimension(tuple(2*x for x in mu), 4)
                 for mu in partitions(d) if len(mu) <= 4)
    expected = comb(d+9, 9)
    assert actual == expected
    results["ambient_dimensions"].append({"d": d, "dimension": actual})

import sympy as sp
y = sp.symbols("y1:5")
q = sp.symbols("q", nonzero=True)
M = sp.Matrix([[y[0]+sp.I*y[1], y[2]+sp.I*y[3]],
               [-y[2]+sp.I*y[3], y[0]-sp.I*y[1]]])
assert sp.expand(M.det()-sum(t*t for t in y)) == 0
quantum_integer = lambda k: sum(q**(k-1-2*j) for j in range(k))
mixed = sp.cancel((quantum_integer(6)*(quantum_integer(7)-quantum_integer(3))
                   - quantum_integer(3)*quantum_integer(8))/quantum_integer(2))
target = q**10-q**4-q**(-4)+q**(-10)
assert sp.simplify(mixed-target) == 0
results["symbolic_quadric_identity"] = True
results["gct_iv_example_17_8_laurent_identity"] = str(sp.expand(mixed))
results["total_rectangular_labels_checked"] = checked_labels
out = Path(__file__).with_name("n2_formula_results.json")
out.write_text(json.dumps(results, indent=2)+"\n")
print(json.dumps({"labels_checked": checked_labels,
                  "ambient_dimension_checks": len(results["ambient_dimensions"]),
                  "quadric_identity": True,
                  "mixed_laurent_identity": True,
                  "output": str(out)}))
