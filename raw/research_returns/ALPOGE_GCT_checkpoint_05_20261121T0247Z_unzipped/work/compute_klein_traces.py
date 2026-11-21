"""Bounded exact experiments for the P-F44 primitive Klein trace.

This computes a specified signed contribution, not the whole B_n or U_n.
The certificate is an inverse modulo the cyclotomic polynomial.  The trace
of x**j is the Ramanujan sum c_P(j), so all final arithmetic is rational.
"""

from __future__ import annotations

import argparse
import json
import math
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from time import monotonic

import sympy as sp


def compute(n: int) -> dict:
    if n < 4 or n % 3 == 0:
        raise ValueError("P-F44 requires n >= 4 and 3 not dividing n")
    started = monotonic()
    P = (2**n - (-1)**n) // 3
    x = sp.Symbol("x")
    phi = sp.Poly(sp.cyclotomic_poly(P, x), x, domain=sp.QQ)
    weights = [pow(-2, i, P) for i in range(n)]
    residues = [(-sum(weights[i] for i in triple)) % P
                for triple in combinations(range(n), 3)]
    assert all(residues)
    denominator = sp.Poly(1, x, domain=sp.QQ)
    for residue in residues:
        denominator = (denominator *
                       sp.Poly(1 - x**residue, x, domain=sp.QQ)).rem(phi)
    print(f"n={n} P={P}: denominator reduced, "
          f"{monotonic()-started:.2f}s", flush=True)
    inverse = sp.invert(denominator, phi)
    assert (denominator * inverse).rem(phi) == sp.Poly(1, x, domain=sp.QQ)
    totient = int(sp.totient(P))
    trace = sp.Rational(0)
    for (exponent,), coefficient in inverse.terms():
        quotient = P // math.gcd(P, exponent)
        ramanujan = int(sp.mobius(quotient)) * (
            totient // int(sp.totient(quotient)))
        trace += coefficient * ramanujan
    result = {
        "n": n,
        "P": P,
        "D": math.comb(n, 3),
        "cyclotomic_degree": phi.degree(),
        "trace_C1": str(trace),
        "K_n": str(trace / (n * P)),
        "inverse_modulo_phi_verified": True,
        "odd_D_zero_verified": (trace == 0 if math.comb(n, 3) % 2 else None),
        "denominator_mod_phi": [
            [exponent[0], str(coefficient)]
            for exponent, coefficient in denominator.terms()
        ],
        "inverse_mod_phi": [
            [exponent[0], str(coefficient)]
            for exponent, coefficient in inverse.terms()
        ],
        "elapsed_seconds": monotonic() - started,
        "scope": "Exploratory exact primitive-Klein contribution only; "
                 "not a value or bound for the full average polynomial.",
    }
    print({key: result[key] for key in
           ("n", "P", "trace_C1", "K_n", "elapsed_seconds")}, flush=True)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--output", default="work/klein_trace_experiments.json")
    args = parser.parse_args()
    output = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "model": "GPT-6 Astra Pro",
        "effort": "inherited/undisclosed",
        "run": "/root/complexity",
        "results": [],
    }
    for n in args.n:
        output["results"].append(compute(n))
        Path(args.output).write_text(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()
