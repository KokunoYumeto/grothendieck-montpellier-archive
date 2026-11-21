#!/usr/bin/env python3
"""Exact finite checks of A-027 conventions and mutation bookkeeping."""
from datetime import datetime, timezone
from pathlib import Path
import importlib.util
import json

BASE = Path(__file__).resolve().parent
WORK = BASE.parents[1]
spec = importlib.util.spec_from_file_location(
    "gct_castling_characters", WORK/"computations/independent_characters.py")
chars = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chars)


def main():
    checks = []
    for h in range(1, 4):
        old = (h,)*3
        new = ((2*h,)*3, (2*h,)*3, (h,)*6)
        left = chars.kronecker(old, old, old)
        right = chars.kronecker(*new)
        assert left == right
        checks.append({"format_old": [3,3,3], "format_new": [3,3,6],
                       "h": h, "old_value": left, "new_value": right})
    one = chars.kronecker((6,6), (4,4,4), (3,3,3,3))
    assert one == 1
    checks.append({"format": [2,3,4], "h": 1, "value": one})
    markov = []
    x, y, z = 1, 1, 1
    for _ in range(13):
        assert x*x+y*y+z*z == 3*x*y*z
        assert 1 <= x <= y <= z and 3*x*y-z > 0
        N = 3*x*y*z
        assert (y*z)*(3*x) == (x*z)*(3*y) == (x*y)*(3*z) == N
        markov.append({"triple": [x,y,z], "N_at_h1": N})
        last = 3*y*z-x
        assert last > z
        x, y, z = y, z, last
    unit = []
    a,b,c = 1,2,2
    for _ in range(13):
        assert a*b%2 == a*c%2 == b*c%2 == 0
        N = a*b*c//2
        assert (b*c//2)*a == (a*c//2)*b == (a*b//2)*c == N
        unit.append({"format": [a,b,c], "N_at_h1": N})
        last=b*c-a
        assert last > c
        a,b,c=b,c,last
    result = {
        "finding": "A-027", "run": "GCT_KRON_20261120",
        "model": "GPT-6 Astra Pro", "effort": "not exposed",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "exact_character_checks": checks,
        "markov_mutation_checks": markov,
        "unit_mutation_checks": unit,
        "scope": "Convention checks only; all-format equality and unboundedness have complete written proofs",
        "status": "PASS",
    }
    out = BASE/"CASTLING_CERTIFICATE.json"
    tmp = out.with_suffix(".tmp")
    tmp.write_text(json.dumps(result, indent=2)+"\n")
    tmp.replace(out)
    print("PASS four exact character comparisons and26 mutation bookkeeping cases")


if __name__ == "__main__":
    main()
