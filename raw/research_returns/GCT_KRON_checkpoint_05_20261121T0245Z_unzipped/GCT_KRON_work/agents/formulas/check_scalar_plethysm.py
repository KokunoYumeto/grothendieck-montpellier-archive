#!/usr/bin/env python3
"""Independent cycle-index/Murnaghan--Nakayama check of F-011."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
from time import perf_counter

engine_path = Path(__file__).parents[2] / "computations/independent_characters.py"
spec = importlib.util.spec_from_file_location("gct_mn_engine", engine_path)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)


@lru_cache(None)
def plethysm_power_sum(d, n):
    # h_d[h_n] = sum_{mu|-d} z_mu^-1 prod_{r in mu} p_r[h_n].
    result = defaultdict(Fraction)
    for mu in engine.partitions(d):
        expansion = {(): Fraction(1, engine.z_type(mu))}
        for r in mu:
            nxt = defaultdict(Fraction)
            for old, value in expansion.items():
                for nu in engine.partitions(n):
                    cycle = tuple(sorted(old + tuple(r*x for x in nu), reverse=True))
                    nxt[cycle] += value / engine.z_type(nu)
            expansion = nxt
        for cycle, value in expansion.items():
            result[cycle] += value
    return dict(result)


def coefficient(d, n, lam):
    value = sum((weight * engine.character(lam, cycle)
                 for cycle, weight in plethysm_power_sum(d, n).items()), Fraction())
    assert value.denominator == 1
    return value.numerator


def run():
    started = perf_counter()
    rows = []
    for d in range(1, 6):
        for n in range(1, 7):
            if d*n > 15:
                continue
            for k in range(n+1):
                lam = tuple(part for part in (d*(n-k)+k,) + (k,)*(d-1) if part)
                got = coefficient(d, n, lam)
                expected = int(d == 1 or k % 2 == 0)
                assert got == expected, (d, n, k, lam, got, expected)
                rows.append({"d": d, "n": n, "k": k,
                             "lambda": lam, "coefficient": got})
    near_rows = []
    for d in range(2, 6):
        for n in range(1, 7):
            if d*n > 15:
                continue
            for k in range(n):
                for s in range(d):
                    D = d*(n-k)
                    lam = tuple(part for part in (D+k-s,) + (k+1,)*s + (k,)*(d-s-1) if part)
                    got = coefficient(d, n, lam)
                    expected = int((s == 0 and k % 2 == 0) or (s == d-1 and k % 2 == 1))
                    assert got == expected, (d, n, k, s, lam, got, expected)
                    near_rows.append({"d": d, "n": n, "k": k, "s": s,
                                      "lambda": lam, "coefficient": got})
    def rectangle_count(j, height, width):
        if j < 0 or width < 0:
            return 0
        return sum(len(part) <= height for part in engine.partitions(j, width))
    shifted_rows = []
    for d in range(2, 6):
        for n in range(1, 7):
            if d*n > 15:
                continue
            for k in range(n+1):
                a = n-k
                D = d*a
                delta = d*(d-1)//2
                for t in range(D//2+1):
                    lam = tuple(part for part in (D-t+k,t+k) + (k,)*(d-2) if part)
                    got = coefficient(d, n, lam)
                    u, width = (t,a) if k % 2 == 0 else (t-delta,a-d+1)
                    expected = rectangle_count(u,d,width) - rectangle_count(u-1,d,width)
                    assert got == expected, (d, n, k, t, lam, got, expected)
                    shifted_rows.append({"d":d,"n":n,"k":k,"t":t,
                                         "lambda":lam,"coefficient":got})
    assert rectangle_count(6,6,6)-rectangle_count(5,6,6) == 4
    stabilization_rows = []
    for d in range(2,6):
        for n in range(1,7):
            if d*n > 15:
                continue
            for lam in engine.partitions(d*n):
                if len(lam) > d:
                    continue
                b = lam[1] if len(lam) > 1 else 0
                if b > n:
                    continue
                mu = tuple(part for part in (d*b-sum(lam[1:]),)+lam[1:] if part)
                got = coefficient(d,n,lam)
                lower = coefficient(d,b,mu)
                assert got == lower, (d,n,lam,b,mu,got,lower)
                stabilization_rows.append({"d":d,"n":n,"lambda":lam,
                                            "base_degree":b,"base_partition":mu,
                                            "coefficient":got})
    result = {"finding": "F-011, F-012, F-013 and F-014", "method": "power-sum cycle index plus independent Murnaghan--Nakayama engine",
              "checks": len(rows), "maximum_total_degree": 15,
              "rows": rows, "near_rectangle_checks": len(near_rows),
              "near_rectangle_rows": near_rows, "status": "PASS",
              "shifted_two_row_checks":len(shifted_rows),
              "shifted_two_row_rows":shifted_rows,
              "four_copy_partition_difference":4,
              "second_row_stabilization_checks":len(stabilization_rows),
              "second_row_stabilization_rows":stabilization_rows,
              "elapsed_seconds": round(perf_counter()-started, 2)}
    Path(__file__).with_name("scalar_plethysm_certificate.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                      ("finding", "method", "checks", "near_rectangle_checks", "shifted_two_row_checks", "second_row_stabilization_checks", "maximum_total_degree", "status", "elapsed_seconds")}))


if __name__ == "__main__":
    run()
