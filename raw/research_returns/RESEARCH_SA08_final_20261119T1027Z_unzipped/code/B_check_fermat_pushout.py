"""Exact finite certificates for C19; the general proof is symbolic."""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
T, U, W, beta, t = sp.symbols("T U W beta t")
checks = []
for p in (3, 5, 7):
    L = U + W
    Q = sum((-1) ** j * U ** (p - 1 - j) * W ** j for j in range(p))
    f = U ** p + W ** p - T ** p
    delta = sp.diff(Q, U) - sp.diff(Q, W)
    identities = {
        "factorization": sp.expand(L * Q - f - T ** p),
        "dU_relation": sp.expand(L * sp.diff(Q, U) + Q - sp.diff(f, U)),
        "dW_relation": sp.expand(L * sp.diff(Q, W) + Q - sp.diff(f, W)),
        "closedness_syzygy": sp.expand(
            T ** p * delta - Q * (sp.diff(f, U) - sp.diff(f, W)) + f * delta
        ),
    }
    assert all(value == 0 for value in identities.values())
    coefficient_weight = sp.Poly(T ** p * Q, T, U, W).total_degree()
    assert coefficient_weight + 1 == 2 * p
    root_polynomial = sp.div(beta ** p + 1, beta + 1, beta)[0]
    inverse = sp.invert(beta + 1, root_polynomial, beta)
    assert sp.rem((beta + 1) * inverse - 1, root_polynomial, beta) == 0
    # U'=beta*(1-t^p)^(1/p); expansion through t^(2p).
    unit_series = 1 - t ** p / p - sp.Rational(p - 1, 2 * p * p) * t ** (2 * p)
    curve_series = sp.series((beta * unit_series) ** p + 1 - t ** p,
                             t, 0, 3 * p).removeO().expand()
    reduced_curve = sum(
        sp.rem(coefficient, root_polynomial, beta) * t ** exponent[0]
        for exponent, coefficient in sp.Poly(curve_series, t).terms()
    )
    assert sp.expand(reduced_curve) == 0
    coordinate_series = (beta * unit_series + 1) / t
    log_derivative = sp.series(sp.diff(coordinate_series, t) / coordinate_series,
                               t, 0, p + 1).removeO().expand()
    # Cancel rational coefficients before extracting the Laurent coefficient.
    residue = sp.limit(t * sp.diff(coordinate_series, t) / coordinate_series, t, 0)
    assert residue == -1
    checks.append({
        "p": p,
        "Q": str(Q),
        "identities_zero": {key: str(value) for key, value in identities.items()},
        "theta_weight": coefficient_weight + 1,
        "beta_root_polynomial": str(root_polynomial),
        "inverse_of_beta_plus_one": str(inverse),
        "curve_series_remainder_through_order_3p_minus_1": str(reduced_curve),
        "u_plus_w_series": str(sp.expand(coordinate_series)),
        "logarithmic_residue": str(residue),
    })
result = {
    "claim": "C19 ordinary pushout Fermat-curve witness",
    "coefficient_domain": "exact rational polynomials and Q[beta]/((beta^p+1)/(beta+1))",
    "primes_checked": [3, 5, 7],
    "checks": checks,
    "runtime_seconds": time.perf_counter() - started,
    "scope": "Finite certificates corroborate the all-odd-prime proof; no numerical approximation.",
}
path = root / "logs/B_fermat_pushout_checks.json"
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"path": str(path), "runtime_seconds": result["runtime_seconds"],
                  "primes_checked": result["primes_checked"], "all_checks_passed": True}))
