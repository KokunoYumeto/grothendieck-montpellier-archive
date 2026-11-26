"""Finite computational probe of cubic construction routes; no asymptotic claim.

The cubic menu contains x^3+a*x^2+b*x+c with a in {-1,0,1},
|b| <= coefficient_bound, 1 <= c <= constant_bound, negative polynomial
discriminant, and no rational root. We do NOT compute maximal orders or
claim to find the least complex cubic FIELD discriminant.
"""
import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path


def primes_through(limit):
    sieve = bytearray(b"\1") * (limit + 1)
    sieve[:2] = b"\0\0"
    for n in range(2, math.isqrt(limit) + 1):
        if sieve[n]:
            sieve[n*n:limit+1:n] = b"\0" * (((limit - n*n) // n) + 1)
    return [n for n, yes in enumerate(sieve) if yes]


def discriminant(a, b, c):
    return a*a*b*b - 4*b*b*b - 4*a*a*a*c - 27*c*c + 18*a*b*c


def has_integer_root(a, b, c):
    for d in range(1, math.isqrt(c) + 1):
        if c % d == 0:
            for x in (d, -d, c//d, -c//d):
                if x*x*x + a*x*x + b*x + c == 0:
                    return True
    return False


def trim(f):
    while f and f[-1] == 0:
        f.pop()
    return f


def remainder(f, g, p):
    f = trim([v % p for v in f])
    g = trim([v % p for v in g])
    inverse = pow(g[-1], -1, p)
    while len(f) >= len(g):
        multiplier = f[-1] * inverse % p
        shift = len(f) - len(g)
        for j, value in enumerate(g):
            f[j+shift] = (f[j+shift] - multiplier*value) % p
        trim(f)
    return f


def irreducible_cubic(a, b, c, p):
    # A cubic is irreducible iff gcd(f, X^p-X)=1.
    def multiply(x, y):
        z = [0] * 5
        for i in range(3):
            for j in range(3):
                z[i+j] += x[i]*y[j]
        for i in (4, 3):
            value = z[i] % p
            z[i-3] -= value*c
            z[i-2] -= value*b
            z[i-1] -= value*a
        return tuple(v % p for v in z[:3])
    result, base, exponent = (1, 0, 0), (0, 1, 0), p
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    g = trim([result[0], (result[1]-1) % p, result[2]])
    f = [c % p, b % p, a % p, 1]
    while g:
        f, g = g, remainder(f, g, p)
    return len(f) == 1


def pair_multiply(x, y, p):
    a, b = x
    c, d = y
    return ((a*c - b*d) % p, (a*d + b*c - b*d) % p)


def cubic_character(a, b, p):
    value, base, exponent = (1, 0), (a % p, b % p), (p*p-1)//3
    while exponent:
        if exponent & 1:
            value = pair_multiply(value, base, p)
        base = pair_multiply(base, base, p)
        exponent >>= 1
    return value


def height_witness(p, least_auxiliary):
    upper = math.isqrt(least_auxiliary) + 1
    for height in range(1, upper+1):
        for a in range(-height, height+1):
            for b in range(-height, height+1):
                if max(abs(a), abs(b)) != height or b == 0:
                    continue
                if a % p == 0 and b % p == 0:
                    continue
                if cubic_character(a, b, p) != (1, 0):
                    norm = a*a-a*b+b*b
                    assert least_auxiliary <= norm <= 3*height*height
                    return height, a, b, norm
    raise AssertionError("The reciprocity bound should supply a height witness")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--coefficient-bound", type=int, default=12)
    parser.add_argument("--constant-bound", type=int, default=24)
    parser.add_argument("--output-prefix", default="cubic_probe")
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    candidates = []
    for a in (-1, 0, 1):
        for b in range(-args.coefficient_bound, args.coefficient_bound+1):
            for c in range(1, args.constant_bound+1):
                disc = discriminant(a, b, c)
                if disc < 0 and not has_integer_root(a, b, c):
                    candidates.append((abs(disc), a, b, c))
    candidates.sort()
    # Independent brute-force validation of the modular irreducibility test.
    for p in (17, 53, 71):
        for _, a, b, c in candidates[:100]:
            brute = not any((x**3+a*x*x+b*x+c) % p == 0 for x in range(p))
            assert irreducible_cubic(a, b, c, p) == brute
    all_primes = primes_through(max(args.limit, 10000))
    auxiliary_primes = [ell for ell in all_primes if ell % 3 == 1]
    rows = []
    for p in all_primes:
        if p > args.limit or p % 9 != 8:
            continue
        valuation, temp = 0, p+1
        while temp % 3 == 0:
            valuation += 1
            temp //= 3
        least_auxiliary = next(
            ell for ell in auxiliary_primes
            if pow(p, (ell-1)//3, ell) != 1
        )
        height, A, B, norm = height_witness(p, least_auxiliary)
        line = next(t for t in range(p) if cubic_character(t, 1, p) != (1, 0))
        assert least_auxiliary <= line*line-line+1
        chosen = None
        for rank, (disc, a, b, c) in enumerate(candidates, 1):
            if disc % p and irreducible_cubic(a, b, c, p):
                chosen = (disc, a, b, c, rank)
                break
        assert chosen is not None
        disc, a, b, c, rank = chosen
        plus = next(m for m in range(1, p) if irreducible_cubic(0, 1, m, p))
        minus = next(m for m in range(1, p) if irreducible_cubic(0, -1, m, p))
        rows.append(dict(
            p=p, a_3=valuation, least_auxiliary=least_auxiliary,
            least_eisenstein_height=height, A=A, B=B, norm=norm,
            least_affine_parameter=line,
            cubic_polynomial_discriminant=-disc,
            cubic_a=a, cubic_b=b, cubic_c=c, menu_rank=rank,
            least_m_x3_plus_x_plus_m=plus,
            least_m_x3_minus_x_plus_m=minus
        ))
    csv_path = directory / (args.output_prefix + ".csv")
    with csv_path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metrics = [
        "least_auxiliary", "least_eisenstein_height",
        "least_affine_parameter", "menu_rank",
        "least_m_x3_plus_x_plus_m", "least_m_x3_minus_x_plus_m"
    ]
    summary = {
        "status": "finite exact probe only; no asymptotic bound",
        "prime_limit": args.limit,
        "number_of_hard_primes": len(rows),
        "integer_polynomial_menu_size": len(candidates),
        "menu_description": {
            "monic": True, "a": [-1, 0, 1],
            "b_interval": [-args.coefficient_bound, args.coefficient_bound],
            "c_interval": [1, args.constant_bound],
            "discriminant": "negative polynomial discriminant; field index not computed"
        },
        "valuation_counts": dict(sorted(Counter(row["a_3"] for row in rows).items())),
        "maxima": {
            metric: {
                "value": max(row[metric] for row in rows),
                "first_primes": [row["p"] for row in rows if row[metric] == max(v[metric] for v in rows)][:20]
            } for metric in metrics
        },
        "largest_menu_polynomial_discriminant": max(-row["cubic_polynomial_discriminant"] for row in rows),
        "largest_discriminant_rows": sorted(rows, key=lambda row: row["cubic_polynomial_discriminant"])[:12],
        "most_frequent_polynomial_discriminants": Counter(row["cubic_polynomial_discriminant"] for row in rows).most_common(12),
        "all_valuation_ge_2": all(row["a_3"] >= 2 for row in rows),
        "cross_checks": "irreducibility compared with exhaustive roots on 300 small cases; reciprocity inequalities checked on every row"
    }
    json_path = directory / (args.output_prefix + "_summary.json")
    json_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

