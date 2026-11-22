"""Exact numerical source-parameter and valuation certificate for AM-K026."""

from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import mpmath as mp

mp.mp.dps = 80


def vp(n, p=11):
    if n == 0:
        raise ValueError("valuation of zero")
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def vfac(n, p=11):
    out = 0
    while n:
        n //= p
        out += n
    return out


def min_index(degree):
    level, exponent = 29, 1
    while level < 3 * degree + 2:
        level *= 29
        exponent += 1
    return level, exponent


def hook_value_direct(part):
    a = len(part)
    value = sum(vfac(part[i] + a - 1 - i) for i in range(a))
    value -= sum(vp(part[i] - part[j] + j - i)
                 for i in range(a) for j in range(i + 1, a))
    return value


def index_value(rank):
    power = 1
    result = 0
    for i in range(1, rank + 1):
        power *= 29
        result += vp(power - 1)
    return 6 * result


def coefficient_dimension(part):
    # Return only exact v_11 and high-precision logarithm, not huge integer.
    a = len(part)
    value = 0
    logdim = mp.mpf(0)
    for i in range(a):
        for j in range(i + 1, a):
            if part[i] == part[j]:
                continue
            numerator = part[i] - part[j] + j - i
            denominator = j - i
            value += vp(numerator) - vp(denominator)
            logdim += mp.log(mp.mpf(numerator) / denominator)
    return value, logdim


def main():
    k, m, t, order = 6, 2, 1795, 3
    d = t + 1
    r = k + m - 1
    S = r + m * t
    q = S ** 3 + 2
    gap = 2 * q + d
    u = [Fraction(2 * k - 1 - 2 * i, 2) for i in range(k)]
    v = [k - 1 - i for i in range(k - 1)]
    b = [j * gap for j in range(m)]
    e = [bj + gap // 2 for bj in b]
    H = Fraction(t + 3, 2)
    ranks = [
        k % 2 == 0, m % 2 == 0, t % 2 == 1, m >= 2,
        m + 3 <= k, k + m - 1 + 5 <= t, 3 * m < t,
        m <= 2 * order <= k, m * m <= k + m * (t + 1),
    ]
    assert all(ranks)
    assert 1801 <= r + t
    assert all(u[i + 1] < v[i] < u[i] for i in range(k - 1))
    assert u[-1] > -b[0]
    assert all(b[j] < e[j] for j in range(m))
    assert all(e[j] < b[j + 1] for j in range(m - 1))
    assert all(e[j] - b[j] >= H for j in range(m))
    assert all(b[j + 1] - e[j] >= H for j in range(m - 1))

    centred = []
    for j in range(m):
        candidates = [abs(ui + e[j]) for ui in u]
        candidates += [abs(vi + e[j]) for vi in v]
        candidates += [abs(e[j] - bi) for bi in b]
        for other in range(m):
            if other == j:
                continue
            candidates += [
                abs(-e[other] + Fraction(t - 1, 2) - ell + e[j])
                for ell in range(t)
            ]
        centred.append(min(candidates))
        assert min(candidates) >= H

    nc = []
    for j in range(m + 1):
        entries = [(Fraction(vi), True) for vi in v]
        entries += [(Fraction(-b[i]), i <= j or (i - j) % 2 == 0)
                    for i in range(m)]
        for i in range(min(j, m)):
            entries += [(Fraction(-e[i]) + Fraction(t - 1, 2) - ell, True)
                        for ell in range(t)]
        positive = [x for x, sign in entries if sign]
        negative = [x for x, sign in entries if not sign]
        if negative:
            minimum = min(abs(x - y) for x in positive for y in negative)
            assert minimum > S ** 3
            nc.append({"j": j, "minimum_cross_sign_gap": str(minimum)})
        else:
            nc.append({"j": j, "no_opposite_sign_pair": True})

    stages = []
    previous_partition = []
    previous_hook_value = 0
    previous_hook_log = mp.mpf(0)
    for j in range(m):
        a, target = k + j * d, k + (j + 1) * d
        part = [(2 * j + 1) * q] * k
        for ell in range(j, 0, -1):
            part += [2 * ell * q] * d
        eta = previous_partition + [0] * (a - len(previous_partition))
        uniform = q if j == 0 else 2 * q
        assert part == [entry + uniform for entry in eta]
        degree = 6 * sum(part)
        Rj = k * j + d * j * (j + 1) // 2
        upper = 6 * k * vfac(q) + 6 * Rj * vfac(2 * q)
        ratio_value = sum(vfac(eta[i] + uniform + a - 1 - i)
                          - vfac(eta[i] + a - 1 - i) for i in range(a))
        ratio_log = sum(
            mp.loggamma(eta[i] + uniform + a - i)
            - mp.loggamma(eta[i] + a - i)
            for i in range(a)
        )
        hook_value = previous_hook_value + ratio_value
        hook_log = previous_hook_log + ratio_log
        assert hook_value == hook_value_direct(part)
        level, exponent = min_index(degree)
        assert degree > 3140 * a * target
        dim_value, dim_log = coefficient_dimension(eta)
        logindex = 6 * a * a * exponent * mp.log(29)
        logindex += 6 * sum(mp.log1p(-mp.power(29, -ell))
                           for ell in range(1, a + 1))
        stages.append({
            "j": j, "source_rank": a, "target_rank": target,
            "total_degree_six_labels": degree,
            "D_over_ab_exact": str(Fraction(degree, a * target)),
            "D_over_3140ab": mp.nstr(mp.mpf(degree) / (3140 * a * target), 25),
            "content_lower_bound_from_mod11": 1,
            "content_upper_bound_adjacent_gap": upper,
            "hook_v11_one_label": hook_value,
            "hook_insertion_ratio_v11_one_label": ratio_value,
            "hook_log_one_label": mp.nstr(hook_log, 30),
            "hook_insertion_ratio_log_one_label": mp.nstr(ratio_log, 30),
            "least_level_exponent": exponent, "least_level": level,
            "index_v11": index_value(a),
            "index_log": mp.nstr(logindex, 30),
            "source_compact_dimension_v11_one_label": dim_value,
            "source_compact_dimension_log_six_labels": mp.nstr(6 * dim_log, 30),
            "source_compact_dimension_v11_six_labels": 6 * dim_value,
        })
        previous_partition = part
        previous_hook_value, previous_hook_log = hook_value, hook_log

    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "claim": "Exact source numerical Hyp3 clauses and finite valuations; logarithms are labelled high-precision numerical evaluations, not exact proof certificates.",
        "parameters": {"k": k, "m": m, "t": t, "d": d, "r": r,
                       "order": order, "S": S, "q": q, "gap": gap,
                       "b": b, "e": e, "u": [str(x) for x in u], "v": v},
        "rank_checks": all(ranks), "strong_1801_check": True,
        "centred_minima": [str(x) for x in centred],
        "ncgaps_threshold": S ** 3, "ncgaps": nc,
        "factorial_v11": {"q": vfac(q), "2q": vfac(2 * q)},
        "stages": stages, "pass": True,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
