#!/usr/bin/env python3
"""Exact integer certificate for A-025; no floating point decisions."""
from datetime import datetime, timezone
from math import comb
from pathlib import Path
from fractions import Fraction
import json

BASE = Path(__file__).resolve().parent
M = 190
N = M**25


def coarse_size(m, u, v, retain_minus_fifty=True):
    qfactor = m*m-50 if retain_minus_fifty else m*m
    return (m+1)*comb(49+u, 49)+qfactor*comb(49+v, 49)-1


def best_coarse(B):
    values = [(coarse_size(M, u, B-1-u), u, B-1-u)
              for u in range(B)]
    minimum = min(values)
    return {
        "B": B,
        "splits_checked": len(values),
        "minimum_size": minimum[0],
        "minimizing_u": minimum[1],
        "minimizing_v": minimum[2],
        "successful_splits": [[u, v] for size, u, v in values if size <= N],
    }


def early_middle_count(m, u):
    t = min(m, u)
    return (m+1)*comb(49+t, 49)-49*comb(49+t, 50)


def last_middle_count(m, v):
    return comb(49+min(v, m), 49)+(m*m-51)*comb(49+min(v, m-1), 49)


def pruned_certificate():
    u, v = 325, 212
    records = []
    for m in range(190, 332):
        a = early_middle_count(m, u)
        direct_a = sum(comb(48+j, j)*(m-j+1) for j in range(min(m, u)+1))
        assert a == direct_a
        q = last_middle_count(m, v)
        total, nth = a+q, m**25
        margin = 99*nth-100*total
        assert margin > 0
        records.append({"m": m, "A": a, "Q": q, "T": total,
                        "m_to_25": nth, "margin_99N_minus_100T": margin})
    maximum = max(records, key=lambda row: Fraction(row["T"], row["m_to_25"]))
    assert maximum["m"] == 331
    assert 15875-48*331 < 0 and 2500-46*331**2 < 0
    # Witnesses only for this upper-count family, not optimal determinants.
    assert early_middle_count(332, 326) > 332**25
    assert last_middle_count(214, 213) > 214**25
    return {
        "B": u+v+1, "u": u, "v": v,
        "cases": records, "count": len(records),
        "maximum_ratio_m": maximum["m"],
        "maximum_ratio_exact": str(Fraction(maximum["T"], maximum["m_to_25"])),
        "tail": "2*m^26*(T/m^25)' = C37449*(15875-48m)+C26149*(2500-46m^2)<0 for real m>=331",
        "first_component_failure_witnesses": [
            {"u": 326, "m": 332, "A": early_middle_count(332, 326), "m_to_25": 332**25},
            {"v": 213, "m": 214, "Q": last_middle_count(214, 213), "m_to_25": 214**25},
        ],
    }


def alternate_certificate():
    u, v = 360, 195
    records = []
    for m in range(190, 361):
        p = comb(49+min(u, m), 49)
        q = early_middle_count(m, v)+(m*m-51)*early_middle_count(m-1, v)
        total, nth = p+q, m**25
        margin = 24*nth-25*total
        assert margin > 0
        records.append({"m": m, "P": p, "Q": q, "T": total,
                        "m_to_25": nth, "margin_24N_minus_25T": margin})
    maximum = max(records, key=lambda row: Fraction(row["T"], row["m_to_25"]))
    assert maximum["m"] == 360
    assert 360**2 >= 153 and 2*360*10 > 3*1911
    return {
        "B": u+v+1, "u": u, "v": v,
        "cases": records, "count": len(records),
        "maximum_ratio_m": maximum["m"],
        "maximum_ratio_exact": str(Fraction(maximum["T"], maximum["m_to_25"])),
        "tail": "For m>=360 each positive summand C40949/m^25, C24449*(m+1-c)/m^25, C24449*(m^2-51)*(m-c)/m^25 decreases; c=1911/10; logarithmic derivatives bounded by-22/m and-19/m",
    }


def main():
    C, D = comb(271, 49), comb(245, 49)
    upper = 191*C+36100*D
    margin = 49*N-50*upper
    assert margin > 0
    b419, b420 = best_coarse(419), best_coarse(420)
    assert b419["successful_splits"] == [[221, 197], [222, 196]]
    assert not b420["successful_splits"]
    result = {
        "finding": "A-025",
        "run": "GCT_KRON_20261120",
        "model": "GPT-6 Astra Pro",
        "effort": "not exposed",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "arithmetic": "Python unbounded integers; exact binomial coefficients",
        "m": M,
        "m_to_25": N,
        "C_271_49": C,
        "C_245_49": D,
        "coarse_clean_upper_at_190": upper,
        "strict_49_over_50_margin": margin,
        "coarse_search": [b419, b420],
        "pruned": pruned_certificate(),
        "alternate": alternate_certificate(),
        "uniform_tail_proof": "C*(m^-24+m^-25)+D*m^-23 decreases for positive m",
        "scope": "The finite optimum is only for the coarse two-cap size formula at m=190",
    }
    out = BASE/"JOINT_SUPPORT_CERTIFICATE.json"
    temporary = out.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, indent=2)+"\n")
    temporary.replace(out)
    print("PASS A-025 exact inequality, all839 coarse splits,142 pruned cases,171 alternate cases")
    print("positive exact margin:", margin)


if __name__ == "__main__":
    main()
