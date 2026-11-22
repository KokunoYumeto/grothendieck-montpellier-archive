#!/usr/bin/env python3
"""Reproducible exact finite inputs to AM-K020's all-order sharpness proof."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from jacobian_sigma_hurwitz_determinant import sigma_jets


def digit_sum(n, p):
    answer = 0
    while n:
        answer += n % p
        n //= p
    return answer


records = []
for p, i, m, expected in [(3, 1, 18, 1), (5, 2, 30, 4)]:
    first = sigma_jets(p, i, m, 0)
    extra = sigma_jets(p, i, m, 14)
    assert first["sigma_q_hurwitz"] == extra["sigma_q_hurwitz"]
    assert first["sigma_q_hurwitz"][m] == expected
    q = p**3
    s = Fraction(1, p-1)
    c = s/(q+1)
    w = s-c
    delta = (p-1)*c
    nu = s*digit_sum(m, p)-c*m
    bound = int(nu/delta)
    residue = {1: 4, 2: 2}[i]
    candidates = [n for n in range(1, bound+1) if n % 14 == residue]
    lower_weights = {n: s*digit_sum(n, p)-c*n for n in candidates}
    assert min(lower_weights, key=lower_weights.get) == m
    assert all(lower_weights[n] > nu for n in candidates if n != m)
    assert delta*(q+1+m) > nu+s
    samples = []
    for r in range(12):
        n = (q+1)*p**r+m
        value = Fraction(p**r+3-digit_sum(n, p), p-1)
        assert value.denominator == 1 and value >= 0
        if p == 5 or r >= 3:
            assert value == Fraction(p**r-1, p-1)
        samples.append({"r": r, "order": n, "base_p_digit_sum": digit_sum(n, p),
                        "valuation_proved_by_K020": int(value)})
    records.append({
        "prime": p, "direction": i, "unit_derivative_order": m,
        "unit_derivative_residue": expected,
        "matrix_sizes": [first["matrix_size"], extra["matrix_size"]],
        "constant_ranks": [first["constant_rank"], extra["constant_rank"]],
        "complete_derivative_vectors_agree": True,
        "nonzero_sigma_derivatives": first["nonzero_sigma_derivatives"],
        "q": q, "critical_weight": str(w), "sharp_slope": str(c),
        "prefactor_margin": str(delta), "critical_prefactor_weight": str(nu),
        "possible_initial_orders_after_bare_bound": candidates,
        "initial_order_lower_weights": {str(n): str(v) for n, v in lower_weights.items()},
        "unique_initial_order": m, "witness_samples": samples,
    })

root = Path(__file__).parent
result = {
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "method": "Fresh exact Sato determinants in truncated Hurwitz rings modulo3 and5, with fourteen extra identity-tail rows; exact rational critical weights and digit sums.",
    "records": records,
    "proof_scope": "Finite unit inputs and rational arithmetic are certified here. Infinite witness valuations and sharp slopes use the complete weighted-initial-form and actual-prefactor arguments of AM-K020.",
    "scripts_sha256": {
        name: sha256((root/name).read_bytes()).hexdigest()
        for name in ["jacobian_sigma_hurwitz_determinant.py",
                     "jacobian_sigma_sharp_certificate.py"]
    },
    "status": "PASS",
}
destination = root/"jacobian_sigma_sharp_certificate.json"
destination.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"status": result["status"], "saved": str(destination),
                  "unit_inputs": [[r["prime"], r["direction"],
                                   r["unit_derivative_order"],
                                   r["unit_derivative_residue"]] for r in records]}))
