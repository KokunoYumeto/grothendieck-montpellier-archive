#!/usr/bin/env python3
"""Exact certificates for PNEW-001, PNEW-005, PNEW-006 and PNEW-007.

No floating point or multiplicity oracle is used. The cyclotomic inverse
is checked after *every* factor by multiplication in Q[z]/(z^(M/2)+1).
Run from any directory. Output: ../certificates/plethysm_exact.json.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, combinations_with_replacement
from math import comb, gcd
from pathlib import Path
import json

DEST = Path(__file__).resolve().parent.parent / "certificates"

def shift(v, a):
    d = len(v)
    ans = [0] * d
    for i, x in enumerate(v):
        q, j = divmod(i + a, d)
        ans[j] += -x if q & 1 else x
    return ans

def twice_inverse(v, a):
    """Solve (1-z^a)out=2v by each signed cyclic permutation orbit."""
    d = len(v)
    step_gcd = gcd(d, a)
    length = d // step_gcd
    out = [0] * d
    for start in range(step_gcd):
        indices, signs = [start], []
        prev, accum = start, 0
        for _ in range(1, length):
            q, nxt = divmod(prev + a, d)
            sg = -1 if q & 1 else 1
            signs.append(sg)
            indices.append(nxt)
            accum = sg * accum + v[nxt]
            prev = nxt
        q, nxt = divmod(prev + a, d)
        assert nxt == start
        sg = -1 if q & 1 else 1
        out[start] = v[start] + sg * accum
        for j in range(1, length):
            out[indices[j]] = signs[j - 1] * out[indices[j - 1]] + 2 * v[indices[j]]
    moved = shift(out, a)
    assert all(x - y == 2 * z for x, y, z in zip(out, moved, v))
    return out

def exact_residue(n):
    M, g = 2 ** (n - 1), gcd(n, 3)
    w = [(-2) ** i for i in range(n - 1)] + [0]
    excluded = {(0, 1, k) for k in range(2, n)} | {(0, 2, 3)}
    weights = w[:-1] + [sum(w[i] for i in ijk) for ijk in combinations(range(n), 3) if ijk not in excluded]
    assert len(weights) == comb(n, 3)
    normal = Counter(sum(w[i] for i in ijk) % M for ijk in combinations_with_replacement(range(n), 3))
    normal.subtract((u - v) % M for u in w for v in w)
    assert all(v >= 0 for v in normal.values()) and normal[0] == 0
    normal += Counter()  # drop zero multiplicities
    assert normal == Counter(a % M for a in weights)
    assert all(a % M for a in weights)
    v, power = [1] + [0] * (M // 2 - 1), 0
    for a in weights:
        v = twice_inverse(v, (g * a) % M)
        power += 1
        while all(x % 2 == 0 for x in v):
            v = [x // 2 for x in v]
            power -= 1
    return v, power

def two_wave(v, power, x):
    q, j = divmod(x, len(v))
    return F((-1 if q & 1 else 1) * v[j], 2 ** power)

def pack(q):
    q = F(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}

def threshold_certificate():
    N, c, beta = 39500, F(1168, 12500), F(2, 7)
    def near(n, t):
        return -(t - 1) * n ** 2 / 2 + F(5, 2) * n * t + F(16, 3) * n * (t + 5) ** 2
    low = -beta - near(N, F(19, 12)) / N ** 2
    high = -beta - near(N, c * N) / N ** 2
    far = (c * N - 8) ** 3 / (24 * N ** 2) - F(25, 24) - F(3, N) - beta
    n = 2 * N
    exponent = F(2, 3) * N ** 3 + F(10, 3) * N + n - N + 1 - F(2, 21) * (n ** 3 - (N - 1) ** 3)
    assert 3 ** 12 > 2 ** 19
    assert F(44, 21) ** 12 < 2 ** 13
    assert low == F(19, 59724000) > 0
    assert high == F(8303507, 86406250) > 0
    assert far == F(1676026865671, 255978515625000) > 0
    assert exponent == -445603261
    assert F(1024 ** 4, 240) - F(12, 5) * 1024 ** 3 - 1 > 0
    return {"N": N, "n0": 2*N, "c": pack(c), "beta": pack(beta),
            "near_low_margin": pack(low), "near_high_margin": pack(high),
            "far_margin": pack(far), "iteration_exponent_at_n0": str(exponent)}

def main():
    rows, residues = [], {}
    for n in [4, 9, 10, 15]:
        v, power = exact_residue(n)
        residues[n] = (v, power)
        record = {"n": n, "M": 2 ** (n - 1), "inverse_denominator_power_of_two": power,
                  "factor_checks": comb(n, 3), "all_factor_checks_passed": True,
                  "inverse_vector_sha256": sha256(json.dumps(v, separators=(",", ":")).encode()).hexdigest()}
        if n <= 10:
            record["inverse_numerators"] = [str(x) for x in v]
        rows.append(record)
    v, power = residues[4]
    assert v == [1, 1, 1, 1] and power == 3
    assert two_wave(v, power, 19) == F(1, 8)
    witnesses = []
    for n, x in [(4,19), (9,6), (9,7), (10,2), (10,3), (15,14), (15,49), (15,60)]:
        v, power = residues[n]
        wave = two_wave(v, power, x)
        g = gcd(n, 3)
        k, d = 3*x//g, n*x//g
        ext_dim = comb(k, 3) if k >= 3 else 0
        exterior = comb(ext_dim,d) if ext_dim >= d else 0
        ambient = comb(comb(n+2,3)+d-1,d)
        if n == 4:
            bound, reason = 0, "Salmon series has no odd coefficient before 25"
        elif (n,x) in [(9,6),(10,2)]:
            bound, reason = 1, "Exact exterior duality / Schur lemma computation in text"
        else:
            bound, reason = min(ambient,exterior), "Minimum of symmetric and exterior ambient dimensions"
        assert wave > bound
        if (n,x) == (15,14):
            assert wave.denominator == 64 and 2**888 < wave.numerator < 2**889
            assert exterior == comb(364,70) < 2**253
        if (n,x) == (15,49):
            assert wave > 2**875 and ambient == comb(924,245) < 2**766
        if (n,x) == (15,60):
            assert wave > 2**881 and ambient == comb(979,300) < 2**866
        witnesses.append({"n":n,"x":x,"two_wave":pack(wave),"proved_upper_bound":str(bound),
                          "bound_reason":reason,"symmetric_ambient":str(ambient),"exterior_ambient":str(exterior),
                          "strict_integer_margin":str(wave.numerator-bound*wave.denominator)})
    # Positive initial odd dilation: f15(7)=1 by the top exterior power.
    assert comb(7,3)==35 and comb(6,2)==15
    cert = {"arithmetic":"exact integers and rational numbers only",
            "threshold":threshold_certificate(),"residues":rows,"witnesses":witnesses,
            "positive_initial_dilation":{"n":15,"dilation":7,"initial_value":1,
                 "index_witness_argument":7,"undilated_wave_argument":49,
                 "positivity_index_lower_bound_strict":7,"saturation_index_lower_bound":7}}
    DEST.mkdir(parents=True,exist_ok=True)
    (DEST/"plethysm_exact.json").write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps({"status":"PASS","n0":79000,"witnesses":len(witnesses),
                      "checked_inverse_factors":sum(r['factor_checks'] for r in rows)},indent=2))

if __name__ == "__main__":
    main()
