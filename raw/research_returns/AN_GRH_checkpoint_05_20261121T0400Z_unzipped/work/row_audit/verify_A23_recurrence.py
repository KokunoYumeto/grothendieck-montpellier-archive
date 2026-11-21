#!/usr/bin/env python3
"""Exact finite cross-checks for A23, not a substitute for its symbolic proof."""
import json
from pathlib import Path

def main():
    traces = [2, 1]
    for _ in range(2, 41):
        traces.append(traces[-1] - 4 * traces[-2])
    rows = []
    for m in range(1, 41):
        q = 4**m
        e = q + 1 - traces[m]
        n = q + 1 - 2 * traces[m]
        j = e * e
        assert e > 0 and n >= 3
        assert n == 2 * e - (q + 1)
        assert 2 * j - e * n == (q + 1) * e > 0
        rows.append(dict(m=m, Q=q, t_m=traces[m], e_m=e,
                         curve_points=n, jacobian_points=j,
                         gap_at_upper_bound_prime=e*(q+1)))
    assert rows[0]["curve_points"] == 3
    assert rows[0]["jacobian_points"] == 16
    assert rows[6]["e_m"] == 16636
    assert rows[6]["jacobian_points"] == 16636**2
    assert traces[7] == -251
    out = {"scope": "Exact recurrence checks for 1 <= m <= 40; the written symbolic proof establishes all m.",
           "result": "PASS", "rows": rows}
    path = Path(__file__).with_name("A23_RECURRENCE_CHECK.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"result": out["result"], "checked_m": [1, 40], "output": str(path)}))

if __name__ == "__main__":
    main()
