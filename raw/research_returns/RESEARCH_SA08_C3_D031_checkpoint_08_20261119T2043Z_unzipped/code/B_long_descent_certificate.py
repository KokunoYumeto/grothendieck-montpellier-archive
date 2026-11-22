#!/usr/bin/env python3
"""Independent finite checks for the prescribed-completion descent witness.

The triple-coordinate calculation is the actual simplicial parameter used in
the proof.  The truncated Frobenius rings are finite analogues of its
dimension-shifting step, not finite models of the whole divided-power ring.
"""
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time


def rank_mod(rows, p):
    a = [[v % p for v in row] for row in rows]
    rank = 0
    ncols = len(a[0]) if a else 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col]:
                c = a[r][col]
                a[r] = [(x - c * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def descent_system(p, length, include_bottom):
    # R=F_p[t]/t^p.  Jbar=F_p*u0 direct sum (t), and F_0=R^2.
    # pi(u)=u0, pi(e)=t.  In F_i, i>=1, the diagonal differential
    # alternates (t,t^(p-1)) and (t^(p-1),t).
    # L=(t^(p-1)) has projective differential t,t^(p-1),t,... .
    # h_i has two polynomial components in F_i.  A bottom variable,
    # when included, is constrained to ker(F_(length-1)->previous).
    nblocks = length + int(include_bottom)
    width = nblocks * 2 * p
    rows = []
    rhs = []

    def ix(block, component, power):
        return block * 2 * p + component * p + power

    def equation(terms, value=0):
        row = [0] * width
        for pos, coeff in terms:
            row[pos] += coeff
        rows.append(row)
        rhs.append(value)

    equation([(ix(0, 0, 0), 1)])
    for power in range(p - 1):
        equation([(ix(0, 1, power), 1)], int(power == p - 2))

    def f_exponent(i, component):
        return (1 if component == 0 else p - 1) if i % 2 else (p - 1 if component == 0 else 1)

    def q_exponent(i):
        return 1 if i % 2 else p - 1

    for i in range(1, length):
        for component in range(2):
            a = f_exponent(i, component)
            b = q_exponent(i)
            for power in range(p):
                terms = []
                if power >= a:
                    terms.append((ix(i, component, power - a), 1))
                if power >= b:
                    terms.append((ix(i - 1, component, power - b), -1))
                equation(terms)

    # The final defect must vanish if the bottom K_length component is
    # forbidden.  With that component present it equals its inclusion.
    b = q_exponent(length)
    for component in range(2):
        for power in range(p):
            terms = []
            if power >= b:
                terms.append((ix(length - 1, component, power - b), 1))
            if include_bottom:
                terms.append((ix(length, component, power), -1))
            equation(terms)
    if include_bottom:
        if length == 1:
            equation([(ix(length, 0, 0), 1)])
            for power in range(p - 1):
                equation([(ix(length, 1, power), 1)])
        else:
            for component in range(2):
                a = f_exponent(length - 1, component)
                for power in range(a, p):
                    equation([(ix(length, component, power - a), 1)])
        # The last homotopy component must also be a cocycle on Q_length.
        bnext = q_exponent(length + 1)
        for component in range(2):
            for power in range(bnext, p):
                equation([(ix(length, component, power - bnext), 1)])
    rank = rank_mod(rows, p)
    augmented_rank = rank_mod([row + [value] for row, value in zip(rows, rhs)], p)
    return {"p": p, "length": length, "bottom_allowed": include_bottom,
            "variables": width, "equations": len(rows), "rank": rank,
            "augmented_rank": augmented_rank, "consistent": rank == augmented_rank}


def triples():
    normalized = {}
    differential = {}
    for n in range(9):
        normalized[n] = [t for t in combinations_with_replacement(range(n + 1), 3)
                         if set(range(1, n + 1)) <= set(t)]
        differential[n] = {t: tuple(v - 1 for v in t) if 0 not in t else None
                           for t in normalized[n]}
    expected = {0: [(0, 0, 0)], 1: [(0, 0, 1), (0, 1, 1), (1, 1, 1)],
                2: [(0, 1, 2), (1, 1, 2), (1, 2, 2)], 3: [(1, 2, 3)]}
    checks = 0
    for n in range(9):
        assert normalized[n] == expected.get(n, [])
        checks += 1
    assert differential[3][(1, 2, 3)] == (0, 1, 2)
    assert differential[2][(0, 1, 2)] is None
    assert differential[2][(1, 1, 2)] == (0, 0, 1)
    assert differential[2][(1, 2, 2)] == (0, 1, 1)
    assert differential[1][(1, 1, 1)] == (0, 0, 0)
    checks += 5
    h = {(0, 0, 0): (1, 1, 1), (0, 0, 1): (1, 1, 2),
         (0, 1, 1): (1, 2, 2), (0, 1, 2): (1, 2, 3)}
    for n, basis in normalized.items():
        for t in basis:
            ht = h.get(t)
            dt = differential[n][t]
            dht = differential[n + 1].get(ht) if ht is not None else None
            hdt = h.get(dt) if dt is not None else None
            assert (dht == t and hdt is None) or (hdt == t and dht is None)
            checks += 1
    # Top of D_2 goes to epsilon_012, its boundary goes to zero.
    assert differential[2][(0, 1, 2)] is None
    checks += 1
    return {"checks": checks, "normalized_ranks": [len(normalized[n]) for n in range(9)],
            "D2_top": [0, 1, 2], "D2_bottom_image": 0}


def main():
    started = time.perf_counter()
    triple = triples()
    systems = []
    for p in (2, 3, 5, 7):
        for length in range(1, 9):
            no_bottom = descent_system(p, length, False)
            with_bottom = descent_system(p, length, True)
            assert not no_bottom["consistent"]
            assert with_bottom["consistent"]
            systems.extend((no_bottom, with_bottom))
    result = {"scope": "Actual monotone-triple coordinate parameter; independent finite Frobenius-ring analogues of forced bottom descent. The finite rings are not identified with the full divided-power coefficient ring.",
              "triple_parameter": triple, "descent_systems": systems,
              "checks": triple["checks"] + len(systems),
              "runtime_seconds": time.perf_counter() - started}
    out = Path(__file__).resolve().parents[1] / "logs" / "B_long_descent_certificate.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"checks": result["checks"], "systems": len(systems),
                      "runtime_seconds": result["runtime_seconds"], "output": str(out)}))


if __name__ == "__main__":
    main()
