"""Exact dual-number certificate for an etale-to-infinitesimal map.

R = F_2[e]/(e^2), represented by two-bit integers a+be.
The map (Z/2)_R -> mu_2 sends its nonzero component to 1+e.
This checks only the finite group calculation; D4a proves the
geometric failure of an Albanese-fibration lift.
"""
import json
import time
from pathlib import Path

started = time.perf_counter()

def add(x, y):
    return x ^ y

def mul(x, y):
    a, b = x & 1, (x >> 1) & 1
    c, d = y & 1, (y >> 1) & 1
    return (a * c) | (((a * d + b * c) & 1) << 1)

one, epsilon, one_plus_epsilon = 1, 2, 3
assert mul(epsilon, epsilon) == 0
assert one_plus_epsilon != one
assert mul(one_plus_epsilon, one_plus_epsilon) == one

h = [one, one_plus_epsilon]
law_checks = []
for a in range(2):
    for b in range(2):
        left = h[(a + b) % 2]
        right = mul(h[a], h[b])
        assert left == right
        law_checks.append({"a": a, "b": b, "h(a+b)": left, "h(a)h(b)": right})

# On Hopf algebras the coordinate u goes to (1, 1+e) in R x R.
# The defining relation u^2=1, counit, and comultiplication all hold.
assert [mul(x, x) for x in h] == [one, one]
assert h[0] == one
assert [x & 1 for x in h] == [1, 1]

out = {
    "ring": "F2[e]/(e^2)",
    "encoding": "a+b*e is encoded as a+2*b",
    "coordinate_map_u": h,
    "defining_relation_u_squared_equals_one": True,
    "counit_preserved": True,
    "comultiplication_group_law_checks": law_checks,
    "special_fibre_is_trivial": True,
    "map_over_R_is_nontrivial": True,
    "geometric_scope": "Finite group inference only; Albanese obstruction is proved separately in D4a/D4b.",
    "runtime_seconds": round(time.perf_counter() - started, 6),
}
dest = Path(__file__).resolve().parents[1] / "outputs" / "check_partsch_etale_step.json"
dest.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
