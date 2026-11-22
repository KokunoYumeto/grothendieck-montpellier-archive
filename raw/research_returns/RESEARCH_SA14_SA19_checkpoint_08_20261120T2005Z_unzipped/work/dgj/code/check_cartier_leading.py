"""Exact coefficient certificate for the local Cartier-fixed model.

This is not a global/projective counterexample.  Coefficients are in F_p;
the general proof is the displayed reindexing in A2_cartier_leading.tex.
"""
import json
import time
from pathlib import Path

start = time.perf_counter()
rows = []
target_terms = 32
for p in (2, 3, 5, 7):
    source = {}
    for n in range(p * target_terms):
        source[(p * (n + 1), n)] = pow(-1, n, p)
    image = {}
    for (t_power, x_power), coeff in source.items():
        if t_power % p == 0 and x_power % p == p - 1:
            image[(t_power // p, (x_power - p + 1) // p)] = coeff
    expected = {
        (p * (r + 1), r): pow(-1, r, p)
        for r in range(target_terms)
    }
    assert image == expected
    assert min(t for t, x in expected) == p
    assert expected[(p, 0)] == 1
    rows.append({
        "p": p,
        "input_terms": p * target_terms,
        "output_terms": len(image),
        "exact_vanishing_order": p,
        "leading_tangential_coefficient": "dx",
        "Cartier_coefficients_match": True,
    })
result = {
    "model": "dlog(1+t^p*x)=t^p*dx/(1+t^p*x)",
    "scope": "affine local; no projective or ampleness conclusion",
    "certificate": rows,
    "runtime_seconds": round(time.perf_counter() - start, 6),
}
out = Path(__file__).resolve().parents[1] / "outputs" / "check_cartier_leading.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
