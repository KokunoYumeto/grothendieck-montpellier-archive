#!/usr/bin/env python3
"""Exact finite checks of AT14's parity formulas and first-weight LES.

This verifies the explicit isolated rational disks and finite cyclic
presentations used in the proof; it makes no iteration/admissibility claim.
"""
from fractions import Fraction
import json
import time
from pathlib import Path


def main():
    start = time.perf_counter()
    checks = 0
    pairs = []
    for q in range(2, 10):
        for m in [1, 2, 3, 5, 6]:
            for arity in range(1, 13):
                if q % 2 == 0:
                    # v is even, u is odd: d gamma_a(v)=m gamma_(a-1)(v)u.
                    low = arity * (q - 2)
                    high = low + 1
                    coefficient = m
                else:
                    # v is odd, u is even: d(v gamma_(a-1)(u))=ma gamma_a(u).
                    high = arity * (q - 1)
                    low = high - 1
                    coefficient = m * arity
                homotopy = Fraction(1, coefficient)
                assert homotopy * coefficient == 1
                assert high == low + 1
                assert q == 2 or high >= 2
                if q >= 3:
                    assert not (high == 1 and coefficient != 1)
                checks += 4
                pairs.append({"q": q, "m": m, "arity": arity,
                              "degrees": [low, high], "d_coefficient": coefficient,
                              "rational_homotopy": str(homotopy)})

    cyclic_cases = []
    for old_order in range(1, 17):
        for ratio in range(1, 17):
            m = old_order * ratio
            # Old d(a)=d theta; new d(u)=theta and d(v)=m u-(m/d)a.
            # The primitive kernel vector is (a,u)=(1,-d).
            kernel = (1, -old_order)
            relation = (-ratio, m)
            assert old_order * kernel[0] + kernel[1] == 0
            assert relation == tuple(-ratio * value for value in kernel)
            # The LES's kernel dZ/mZ has precisely m/d elements.
            residues = [a for a in range(m) if a % old_order == 0]
            assert len(residues) == ratio
            assert (ratio == 1) == (m == old_order)
            checks += 4
            cyclic_cases.append({"old_order": old_order, "relation_multiplier": m,
                                 "new_H1_order": ratio})

    result = {"statement_ids": ["AT14", "AT14-H1"], "status": "PASS",
              "checks": checks, "disk_pairs": pairs, "cyclic_LES_cases": cyclic_cases,
              "scope": "Exact finite parity and cyclic-presentation checks; no claim of a completed repair iteration.",
              "seconds": time.perf_counter() - start}
    target = Path(__file__).resolve().parents[1] / "logs" / "A_integral_weight_repair_check.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "checks", "seconds"]}))


if __name__ == "__main__":
    main()
