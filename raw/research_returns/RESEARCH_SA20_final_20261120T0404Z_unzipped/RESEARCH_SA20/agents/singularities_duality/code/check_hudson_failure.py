"""Exact rational certificate for the failed SA extension of Mnev Prop.52.

The general proof is x^3=s*x, with s>0 arbitrarily small.  This file
checks the concrete s=1/16 configuration using Fraction arithmetic.
It does not refute the concordance comparison itself.
"""
from fractions import Fraction as Q
import json

s = Q(1, 16)
points = [(Q(0), Q(0)), (Q(1, 4), Q(1, 64)),
          (-Q(1, 4), -Q(1, 64))]
checks = []

def check(label, condition):
    assert condition, label
    checks.append({"check": label, "passed": True})

for x, t in points:
    label = f"x={x},t={t}"
    check(label + ": cube-root leaf", x**3 == t)
    check(label + ": affine Hudson graph", s*x == t)
    check(label + ": parameter interval", -Q(1, 8) <= t <= Q(1, 8))
    check(label + ": left branch strictly increasing", 1+x >= Q(1, 2))
    check(label + ": right branch strictly increasing", 1-x >= Q(1, 2))
    check(label + ": fixed left endpoint", (1+x)*(-1)+x == -1)
    check(label + ": fixed right endpoint", (1-x)*1+x == 1)
    check(label + ": branches meet", (1+x)*0+x == (1-x)*0+x)

check("three distinct intersections", len(set(points)) == 3)
check("standard-base graph in [0,1]", 0 <= Q(1,2)-4*s < Q(1,2)+4*s <= 1)
check("Hudson diameter", (Q(1,2)+4*s)-(Q(1,2)-4*s) == 8*s)

print(json.dumps({"status": "PASS", "checks": len(checks),
                  "s": str(s),
                  "intersections": [[str(x), str(t)] for x,t in points],
                  "details": checks}, indent=2))
