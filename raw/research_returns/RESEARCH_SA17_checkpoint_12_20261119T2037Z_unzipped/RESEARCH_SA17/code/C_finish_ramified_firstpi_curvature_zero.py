#!/usr/bin/env python3
"""Exact scope check for a proposed first-pi curvature image difference.

Over Z[pi]/(pi^2-2, pi^3), the first-pi Bocksteins on the two
residual C2 Tate groups agree.  Their curvature actions also agree.
Thus a difference of their q-primary image lengths is identically zero.
This is not a Swan-class vanishing assertion.  The all-rank argument
is in notes/C_ramified_firstpi_curvature_zero.md.
"""
from itertools import product
from pathlib import Path
from time import perf_counter
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'higherpage', HERE / 'C_finish_ramified_higherpage_failure.py')
ring = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ring)


def lift_product(a, b):
    """Untruncated Z[pi], pi^2=2, exact integer pairs."""
    return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def apply_lift(matrix, vector, diagonal_shift):
    ans = []
    for i, row in enumerate(matrix):
        a = sum(entry[0]*x for entry, x in zip(row, vector))
        b = sum(entry[1]*x for entry, x in zip(row, vector))
        ans.append((a+diagonal_shift*vector[i], b))
    return ans


def check_action(t):
    n = len(t)
    assert ring.mm(t,t) == ring.ident(n)
    dbar = [[(entry[0]-(i == j)) % 2 for j,entry in enumerate(row)]
            for i,row in enumerate(t)]
    assert ring.gf_mm(dbar,dbar) == [[0]*n for _ in range(n)]
    checked = 0
    for v in product((0,1), repeat=n):
        if any(sum(dbar[i][j]*v[j] for j in range(n)) % 2
               for i in range(n)):
            continue
        minus = apply_lift(t,v,-1)
        plus = apply_lift(t,v,1)
        # a+b*pi is divisible by pi iff a is even.  Its quotient has
        # residue b mod2.  The difference between the two quotients is
        # (2/pi)*v=pi*v, whose residue is zero.
        assert all(a % 2 == 0 for a,b in minus+plus)
        beta_minus = [b % 2 for a,b in minus]
        beta_plus = [b % 2 for a,b in plus]
        assert beta_minus == beta_plus
        assert all(sum(dbar[i][j]*beta_minus[j] for j in range(n)) % 2 == 0
                   for i in range(n))
        checked += 1
    curvature = []
    for i in range(n):
        row = []
        for j in range(n):
            pairs = [lift_product(t[i][k],t[k][j]) for k in range(n)]
            a = sum(z[0] for z in pairs)-(i == j)
            b = sum(z[1] for z in pairs)
            assert a % 4 == 0 and b % 2 == 0
            # (a+b*pi)/pi^3 = b/2 + (a/4)*pi.
            row.append((b//2) % 2)
        curvature.append(row)
    # Both Tate products are literally Ttilde^2-I, so this one matrix
    # is the curvature in both parities.  It preserves residual cycles.
    assert ring.gf_mm(curvature,dbar) == ring.gf_mm(dbar,curvature)
    return checked


def main():
    started = perf_counter()
    exhaustive = []
    total_cycles = 0
    for n in (1,2):
        count = 0
        for vals in product(ring.ELEMENTS, repeat=n*n):
            t = [list(vals[i*n:(i+1)*n]) for i in range(n)]
            if ring.mm(t,t) != ring.ident(n):
                continue
            total_cycles += check_action(t)
            count += 1
        exhaustive.append({'rank':n,'involutions':count,'ambient_matrices':8**(n*n)})
    extensions = 0
    for n in (1,2,3):
        for vals in product((0,1), repeat=n*n):
            matrix = [list(vals[i*n:(i+1)*n]) for i in range(n)]
            t,e = ring.build_extension(matrix)
            total_cycles += check_action(t)
            total_cycles += check_action(e)
            extensions += 1
    report = {
        'status':'PASS: first-pi curvature-primary image difference is zero in the tested actions',
        'ring':'Z[pi]/(pi^2-2,pi^3), exact eight-element ring',
        'exhaustive_actions':exhaustive,
        'prior_counterexample_family_extensions':extensions,
        'residual_cycle_vectors_checked':total_cycles,
        'all_rank_reason':'The residual Tate differentials coincide; their first-pi Bocksteins differ by (2/pi)I=pi I, zero modulo pi; both curvatures are (Ttilde^2-I)/pi^3. Hence the two primary image modules are identical.',
        'not_claimed':'No additivity theorem for a new invariant, no vanishing or nonvanishing of node Swan classes, and no solution of C.1.',
        'runtime_seconds':perf_counter()-started,
    }
    dst=HERE.parent/'logs/C_finish_ramified_firstpi_curvature_zero.json'
    dst.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
