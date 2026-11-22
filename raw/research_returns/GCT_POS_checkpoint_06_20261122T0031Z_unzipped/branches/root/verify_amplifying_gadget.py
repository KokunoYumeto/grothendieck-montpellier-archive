#!/usr/bin/env python3
"""Independent exact audit of the 8-coordinate gadget and n=9 tensor.

Written by /root from the displayed data, without importing branch search code.
The finite checks support, but do not replace, the induction in K-018.
"""
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp

BASE = Path(__file__).resolve().parents[1] / "kronecker"


def incidence(n, edges):
    return sp.Matrix([[int(e[a] == i) for e in edges]
                      for a in range(3) for i in range(n)])


def free(edges):
    return all(len({(e[a], e[b]) for e in edges}) == len(edges)
               for a, b in ((0, 1), (0, 2), (1, 2)))


def balanced(n, edges, masses):
    return all(sum((w for e, w in zip(edges, masses) if e[a] == i), Q(0)) == 1
               for a in range(3) for i in range(n))


def rank_mod(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    nr, nc, r = len(a), len(a[0]), 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = pow(a[r][c], -1, p)
        a[r] = [(x*z) % p for x in a[r]]
        for i in range(r+1, nr):
            if a[i][c]:
                z = a[i][c]
                a[i] = [(x-z*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == nr:
            break
    return r


def main():
    g = json.loads((BASE / "amplifying_gadget_q8.json").read_text())
    edges = [tuple(e) for e in g["support"]]
    boundary = tuple(g["boundary"])
    u, v = g["intercept_numerators"], g["slope_numerators"]
    den = g["denominator"]
    a = incidence(8, edges)
    expected_u = [0 if i == boundary[j] else den for j in range(3) for i in range(8)]
    expected_v = [den if i == boundary[j] else 0 for j in range(3) for i in range(8)]
    assert list(a*sp.Matrix(u)) == expected_u
    assert list(a*sp.Matrix(v)) == expected_v
    assert free(edges)
    minor = a.extract([i for i in range(24) if i not in g["minor_omitted_rows"]], range(22))
    det_g = int(minor.det())
    assert abs(det_g) == 256
    lower = max(Q(-x,y) for x,y in zip(u,v) if y > 0)
    upper = min(Q(-x,y) for x,y in zip(u,v) if y < 0)
    assert (lower, upper) == (Q(3,11), Q(37,61))
    assert all(x > 0 for x,y in zip(u,v) if y == 0)
    sel = g["selected_edge_index"]
    assert (u[sel],v[sel]) == (131,-43)
    f = lambda r: (131-43*r)/256
    image = (f(upper), f(lower))
    assert image == (Q(25,61), Q(41,88))
    assert lower < image[0] < image[1] < upper

    c = json.loads((BASE / "n9_period512_counterexample.json").read_text())
    e9 = [tuple(e) for e in c["support"]]
    m9 = [Q(x,c["mass_denominator"]) for x in c["mass_numerators"]]
    assert len(e9) == 25 and min(m9) > 0 and free(e9) and balanced(9,e9,m9)
    a9 = incidence(9,e9)
    det9 = int(a9.extract([i for i in range(27) if i not in (17,26)],range(25)).det())
    assert abs(det9) == 512
    assert math.lcm(*(x.denominator for x in m9)) == 512
    w = c["W"]
    fixed = {e for e in itertools.product(range(9),repeat=3)
             if sum(w[j][e[j]] for j in range(3)) % 512 == 0}
    assert fixed == set(e9)
    chi = sum(map(sum,w)) % 512
    assert chi == 219 and math.gcd(chi,512) == 1
    pairs = [[(i,j) for i in range(9) for j in range(i+1,9)
              if (row[i]-row[j]) % 512 == 256] for row in w]
    assert pairs == [[],[(0,6)],[]]
    lie = [[0]*(3*9*9) for _ in range(9**3)]
    for edge in e9:
        for mode in range(3):
            for new in range(9):
                out = list(edge)
                out[mode] = new
                row = out[0]*81 + out[1]*9 + out[2]
                col = mode*81 + new*9 + edge[mode]
                lie[row][col] += 1
    lie_rank = rank_mod(lie,10007)
    assert lie_rank == 241

    # Reconstruct the iterated insertion independently, retaining exact masses.
    n = 2
    ee = [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
    mm = [Q(1,2)]*4
    target = 0
    iterations = []
    for k in range(1,5):
        old, r = ee.pop(target), mm.pop(target)
        maps = []
        for mode in range(3):
            new = iter(range(n,n+7))
            maps.append([old[mode] if j == boundary[mode] else next(new)
                         for j in range(8)])
        new_edges = [tuple(maps[j][e[j]] for j in range(3)) for e in edges]
        new_masses = [(Q(x)+Q(y)*r)/den for x,y in zip(u,v)]
        target = len(ee)+sel
        ee += new_edges
        mm += new_masses
        n += 7
        assert len(ee) == 3*n-2 and free(ee) and balanced(n,ee,mm) and min(mm)>0
        period = math.lcm(*(x.denominator for x in mm))
        assert period == 2**(1+8*k)
        # A modular full rank suffices to verify rational column independence.
        rank = rank_mod(incidence(n,ee).tolist(),10007)
        assert rank == len(ee)
        assert mm[target] == f(r)
        if k == 1:
            assert dict(zip(ee,mm)) == dict(zip(e9,m9))
        iterations.append({"k":k,"n":n,"edges":len(ee),"period":period,
                           "rank_mod_10007":rank,"next_mass":str(mm[target])})
    print(json.dumps({"outcome":"PASS", "gadget_determinant":det_g,
          "positive_interval":[str(lower),str(upper)],
          "image_interval":[str(x) for x in image],
          "n9":{"incidence_minor":det9,"character_exponent":chi,
                "period":512,"full_fixed_edges":len(fixed),
                "lie_rank_mod_10007":lie_rank,"antipodal_pairs":pairs},
          "finite_induction_checks":iterations},indent=2))


if __name__ == "__main__":
    main()
