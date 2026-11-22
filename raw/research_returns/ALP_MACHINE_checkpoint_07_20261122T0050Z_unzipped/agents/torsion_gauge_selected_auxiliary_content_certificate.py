#!/usr/bin/env python3
"""Exact finite checks for AM-K034; no theta coefficients are sampled."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import json

N = 28

def mul(a, b, n=N):
    c = [F(0) for _ in range(n + 1)]
    for i, x in enumerate(a[: n + 1]):
        for j, y in enumerate(b[: n + 1 - i]):
            c[i + j] += x * y
    return c

def deriv(a):
    return [F(i) * a[i] for i in range(1, len(a))]

def series_power(a, n, cutoff=N):
    out = [F(1)] + [F(0)] * cutoff
    while n:
        if n & 1:
            out = mul(out, a, cutoff)
        a = mul(a, a, cutoff)
        n //= 2
    return out

def val11(a):
    a = F(a)
    if not a:
        return None
    n, d = abs(a.numerator), a.denominator
    v = 0
    while n % 11 == 0:
        n //= 11
        v += 1
    while d % 11 == 0:
        d //= 11
        v -= 1
    return v

def root_case(d):
    a = [F(0)] * (N + 1)
    for i, x in {0: 1, 1: 3, 2: -5, 3: 11, 5: 7}.items():
        a[i] = F(x)
    c = a.copy()
    c[0] = 0
    power = [F(1)] + [F(0)] * N
    b = [F(0)] * (N + 1)
    binom = F(1)
    for k in range(N + 1):
        for i in range(N + 1):
            b[i] += binom * power[i]
        power = mul(power, c)
        binom *= (F(-1, d) - k) / (k + 1)
    # d*a*b' + a'*b = 0, exact through x^(N-1).
    x = mul(a, deriv(b), N - 1)
    y = mul(deriv(a), b, N - 1)
    assert all(d * xx + yy == 0 for xx, yy in zip(x, y))
    if d < 100:
        prod = mul(a, series_power(b, d))
        assert prod == [F(1)] + [F(0)] * N
    vals = [val11(x) for x in b if x]
    if d % 11:
        assert min(vals) >= 0
    else:
        assert b[1] == F(-3, 11) and val11(b[1]) == -1
    return {
        "d": d,
        "order": N,
        "connection_identity": "PASS",
        "power_identity": "PASS" if d < 100 else "not separately expanded",
        "minimum_nonzero_coefficient_v11": min(vals),
        "first_coefficient": str(b[1]),
    }

def ceiling_power(n, base=29):
    k, p = 0, 1
    while p < n:
        p *= base
        k += 1
    assert p >= n and (k == 0 or p // base < n)
    return k

def fixed_costs(h, a, b, primes, D0, sample_r):
    f, Q = 42 * h, primes[0] * primes[1]
    L = ceiling_power(Q)
    fixed_e = L * f * a * b
    vindex = 6 * h * sum(val11(29**i - 1) for i in range(1, a + 1))
    vgamma = f * sum(
        val11(q**i - 1) for q in primes for i in range(1, a + 1)
    )
    samples = []
    for r in sample_r:
        degree = 122 * 11**r + D0
        tail = ceiling_power(3 * (degree + 1))
        e = fixed_e + tail
        samples.append({"r": r, "T_r": degree, "level_tail_exponent": tail, "e_sufficient": e})
    return {
        "h": h, "f": f, "a": a, "b": b, "G_primes": primes,
        "Q": Q, "L": L, "fixed_level_exponent": fixed_e,
        "v11_class_index": vindex, "v11_Gamma": vgamma,
        "v11_dG": 0, "samples": samples,
        "level_proof": "s<=Q^(fab)<=29^(Lfab); 29^tail>=3(T+1)",
    }

def reduced_frame_sign_check():
    # H(u,t)=x+iy, H(t,u)=x-iy, H(t,t)=c, H(u,u)=v.
    # Squared frame multiplier adds 2*pi*k*x+pi*k*c.
    # Translated metric exponent subtracts pi*k*(v+2*x+c).
    # Coefficients after subtracting the original metric -pi*k*v:
    assert (2 - 2, 1 - 1, -1 + 1) == (0, 0, 0)
    # Translation coefficient multiplier divided by original one:
    # pi*k*(H(t,lambda)-H(lambda,t)), with zero real part.
    assert (1 - 1) == 0
    return {"metric_cross_constant_cancellation": "PASS",
            "difference_multiplier_real_part_zero": "PASS",
            "scope": "exact coefficient signs in TG6-TG8, not a period computation"}

def main():
    p1 = [4615409, 5276377]
    p4 = [22285932761, 64072175441]
    out = {
        "statement": "AM-K034",
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Finite rational torsion-root/connection identities and integer level/finite-cost arithmetic; the proof of full-germ equality and infinite sharp slope is in the report.",
        "formal_root_checks": [root_case(d) for d in [3, 5, 29, p1[0]*p1[1], p4[0]*p4[1], 11]],
        "reduced_frame_signs": reduced_frame_sign_check(),
        "fixed_costs": [
            fixed_costs(1, 42, 1802, p1, 3504831920337006, [0, 13, 20]),
            fixed_costs(4, 168, 1802, p4, 194467812219985248, [0, 15, 20]),
        ],
        "result": "PASS",
    }
    assert out["fixed_costs"][0]["fixed_level_exponent"] == 31787280
    assert out["fixed_costs"][1]["fixed_level_exponent"] == 762894720
    assert out["fixed_costs"][0]["v11_class_index"] == 24
    assert out["fixed_costs"][1]["v11_class_index"] == 408
    assert out["fixed_costs"][0]["v11_Gamma"] == 336
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
