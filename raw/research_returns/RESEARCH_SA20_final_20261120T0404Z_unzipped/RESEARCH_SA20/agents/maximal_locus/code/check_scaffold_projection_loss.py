#!/usr/bin/env python3
"""Exact algebra for SF.5--6a; not a test of the A5 finite-pool gate."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time

import sympy as s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    x, y, v, q = s.symbols("x y v q", real=True)
    third = s.Rational(1, 3)
    pieces = [2*x, 1-x, 2*x-1]
    domains = [(s.S.Zero, third), (third, 2*third), (2*third, s.S.One)]
    checks = []

    def check(name, condition, detail):
        value = bool(condition)
        checks.append({"name": name, "pass": value, "detail": str(detail)})
        if not value:
            raise AssertionError(name)

    def zero(expr):
        return s.simplify(expr) == 0

    check("first breakpoint", zero(pieces[0].subs(x, third)-pieces[1].subs(x, third)), "q(1/3)=2/3 from both sides")
    check("second breakpoint", zero(pieces[1].subs(x, 2*third)-pieces[2].subs(x, 2*third)), "q(2/3)=1/3 from both sides")
    check("outer endpoints", pieces[0].subs(x, 0) == 0 and pieces[2].subs(x, 1) == 1, "q(0)=0; q(1)=1")
    slopes = [s.diff(p, x) for p in pieces]
    check("three affine slopes", slopes == [2, -1, 2], slopes)
    expected_ranges = [(s.S.Zero, 2*third), (third, 2*third), (third, s.S.One)]
    for i, (p, (a, b), expected) in enumerate(zip(pieces, domains, expected_ranges), 1):
        values = [p.subs(x, a), p.subs(x, b)]
        actual = (min(values), max(values))
        check(f"affine range {i}", actual == expected and all(0 <= z <= 1 for z in values) and s.diff(p, x) != 0,
              {"domain": [str(a), str(b)], "range": list(map(str, actual)), "strict_interior": "nonzero affine slope; only outer endpoints attain 0 or 1"})
    preimages = [s.Rational(1, 4), s.Rational(1, 2), s.Rational(3, 4)]
    values = [p.subs(x, a) for p, a in zip(pieces, preimages)]
    check("three distinct preimages", len(set(preimages)) == 3 and values == [s.Rational(1, 2)]*3,
          {"points": list(map(str, preimages)), "images": list(map(str, values))})

    low = y*q/x
    high = q+(y-x)*(1-q)/(1-x)
    inv_low = x*v/q
    inv_high = x+(1-x)*(v-q)/(1-q)
    check("forward vertical gluing", zero(low.subs(y, x)-q) and zero(high.subs(y, x)-q), "both branches send x to q")
    check("inverse vertical gluing", zero(inv_low.subs(v, q)-x) and zero(inv_high.subs(v, q)-x), "both inverse branches send q to x")
    check("forward vertical endpoints", low.subs(y, 0) == 0 and zero(high.subs(y, 1)-1), "0 maps to 0; 1 maps to 1")
    check("inverse vertical endpoints", inv_low.subs(v, 0) == 0 and zero(inv_high.subs(v, 1)-1), "0 maps to 0; 1 maps to 1")
    check("inverse after lower branch", zero(inv_low.subs(v, low)-y), "h_low^-1(h_low(y))=y")
    check("inverse after upper branch", zero(inv_high.subs(v, high)-y), "h_high^-1(h_high(y))=y")
    check("lower branch after inverse", zero(low.subs(y, inv_low)-v), "h_low(h_low^-1(v))=v")
    check("upper branch after inverse", zero(high.subs(y, inv_high)-v), "h_high(h_high^-1(v))=v")
    A, B = s.symbols("A B", positive=True)
    unit_substitution = {q: A/(1+A), x: B/(1+B)}
    all_slopes = [s.diff(low, y), s.diff(high, y), s.diff(inv_low, v), s.diff(inv_high, v)]
    positive_slopes = [s.factor(z.subs(unit_substitution)) for z in all_slopes]
    check("all vertical slopes positive", all(z.is_positive is True for z in positive_slopes),
          {"unit_interval_parameterization": "q=A/(1+A), x=B/(1+B), A,B>0", "slopes": list(map(str, positive_slopes))})
    check("left lower displacement", zero((low-y).subs(q, 2*x)-y), "h_x(y)-y=y on y<=x near x=0")
    check("left upper displacement", zero((high-y).subs(q, 2*x)-x*(1-y)/(1-x)), "h_x(y)-y=x(1-y)/(1-x) on y>=x near x=0")
    check("right lower displacement", zero((low-y).subs(q, 2*x-1)+(1-x)*y/x), "h_x(y)-y=-(1-x)y/x on y<=x near x=1")
    check("right upper displacement", zero((high-y).subs(q, 2*x-1)-(y-1)), "h_x(y)-y=y-1 on y>=x near x=1")

    result = {
        "certificate": "SF.5--SF.6a projection-loss diagnostic",
        "arithmetic": "exact SymPy rational/symbolic arithmetic; no floating-point tests",
        "utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Algebraic identities, interval ranges and vertical positivity only; continuity and the bisection argument are proved in scaffold_format_gate_0340.tex. No A5 conclusion.",
        "passed": sum(c["pass"] for c in checks),
        "total": len(checks),
        "elapsed_seconds": time.perf_counter()-started,
        "checks": checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in ["certificate", "passed", "total", "elapsed_seconds", "utc"]}, indent=2))


if __name__ == "__main__":
    main()
