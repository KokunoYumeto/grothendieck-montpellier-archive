"""Finite exact Newton-chain supplement for B76; no BT existence inferred."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from collections import Counter
import json
import time


def vp(a, p):
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def ppow(p, exponent):
    return F(p ** exponent) if exponent >= 0 else F(1, p ** (-exponent))


def inverse_steps(p, b, z):
    if b >= z * F(p - 1, p):
        return [(z / (p * p), 'uniform')]
    return [((z - b) / p, 'high'), (F(b, p * (p - 1)), 'low')]


started = time.perf_counter()
counts = Counter()
terminal_modes = Counter()
witnesses = {}
max_high_steps = 0
ranges = [(5, 650), (7, 500), (11, 350), (13, 250)]
for p, max_a in ranges:
    q = p * p
    N = q - 1
    for a in range(1, max_a + 1):
        v = vp(a, p)
        for b in range(1, a + 2):
            counts['newton_parameters'] += 1
            if b >= F(a * p, p + 1):
                starts = [(F(a, N), 'one-slope')]
            else:
                starts = [(F(a - b, p - 1), 'initial-high'),
                          (F(b, p * (p - 1)), 'initial-low')]
            chains = [(z, origin, (), 0) for z, origin in starts
                      if z > 0 and z.denominator == 1]
            for n in range(2, 7):
                new = []
                for z, origin, history, high_count in chains:
                    for w, branch in inverse_steps(p, b, z):
                        counts['inverse_branches'] += 1
                        assert 0 < w < z < a
                        if 'uniform' in history or 'low' in history or origin != 'initial-high':
                            assert branch == 'uniform'
                        if w.denominator != 1:
                            continue
                        h = high_count + int(branch == 'high')
                        assert h <= v
                        max_high_steps = max(max_high_steps, h)
                        steps = history + (branch,)
                        if origin == 'initial-high' and all(t == 'high' for t in steps):
                            assert w == (F(a, p ** h) - b) / (p - 1)
                        assert F(a) > N * ppow(p, 2 * n - 3 - v)
                        counts['rational_torsion_chains'] += 1
                        if v:
                            counts['wild_rational_torsion_chains'] += 1
                        mode = origin if origin != 'initial-high' else next(
                            (t for t in steps if t != 'high'), 'all-high')
                        terminal_modes[mode] += 1
                        if mode not in witnesses:
                            witnesses[mode] = dict(p=p, a=a, b=b, n=n, v=v,
                                                  final_valuation=int(w), steps=list(steps))
                        new.append((w, origin, steps, h))
                chains = new

# Check the general case split's equality exclusions and mixed degree transfer
# at a larger finite range than the direct rational-chain enumeration.
for p in (5, 7, 11, 13, 17, 19):
    N = p * p - 1
    divisors = [m for m in range(1, N + 1) if N % m == 0]
    for n in range(2, 10):
        for v in range(n + 3):
            for j in range(min(v, n - 2) + 1):
                E = 2 * n - 3 - j
                assert E >= 2 * n - 3 - v
                if j == v:
                    assert E > v
                    assert vp(N * p ** E, p) != v
                counts['uniform_equality_cases'] += 1
            if v >= n - 1:
                assert p ** n > N * ppow(p, 2 * n - 3 - v)
                counts['all_high_inequalities'] += 1
        for e in range(1, 1501):
            v = vp(e, p)
            threshold = ppow(p, 2 * n - 3 - v)
            for m in divisors:
                assert vp(m * e, p) == v
                if m * e > N * threshold:
                    assert e > threshold
                counts['mixed_degree_transfers'] += 1
            # Integer valuation of a primitive cyclotomic difference forces
            # the asserted p-part lower bound, even at wild absolute index.
            for r in range(n):
                valuation = F(e * p ** r, p ** (n - 1) * (p - 1))
                if valuation.denominator == 1:
                    assert r >= n - 1 - v
                counts['cyclotomic_denominators'] += 1

assert all(terminal_modes[t] for t in
           ('one-slope', 'initial-low', 'uniform', 'low', 'all-high'))
assert vp(20, 5) == 1 and 20 <= 5 ** (2 * 3 - 3 - 1)
assert 3 >= vp(20, 5) + 2
out = dict(status='PASS', actual_utc=datetime.now(timezone.utc).isoformat(),
           runtime_seconds=time.perf_counter() - started,
           counts=dict(counts), terminal_modes=dict(terminal_modes),
           max_consecutive_high_steps=max_high_steps,
           witnesses=witnesses, newton_ranges=ranges, max_newton_level=6,
           wild_gate=dict(p=5, e=20, n=3, mixed_necessary_threshold=25,
                          mixed_possible=False, whole_formal_case='unresolved'),
           scope='Exact rational Newton chains in the stated finite ranges, all five branch types, equality exclusions, tame-degree transfers, and cyclotomic denominator checks. Finite Newton possibilities do not assert existence of formal groups or rational points; no exact wild least index is inferred.')
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
