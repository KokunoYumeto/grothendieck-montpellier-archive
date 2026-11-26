"""Exact finite checks for the moving-shift proofs. Python standard library."""

from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import sys


def primes_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes([0, 0])
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = bytes((limit - prime * prime) // prime + 1)
    return (n for n, prime in enumerate(sieve) if prime)


def divisors(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return small + [n // d for d in reversed(small) if n // d != d]


def check_histogram(p, r, a, ds, sigma):
    s = p * a
    units = [g for g in range(1, r) if gcd(g, r) == 1]
    hist = dict.fromkeys(units, 0)
    # Weights are scaled to integers by S when sigma=+1.
    for d in ds:
        hist[d % r] += {1: s // d, 0: 1, -1: d}[sigma]
    total, h = sum(hist.values()), len(units)
    opp = sum(hist[g] * hist[-g % r] for g in units)
    h_num = h * sum(t * t for t in hist.values()) - total**2
    assert abs(h * opp - total**2) <= h_num
    assert sum(abs(h * t - total) for t in hist.values())**2 <= h * h * h_num
    assert max((h * t - total)**2 for t in hist.values()) <= (h - 1) * h_num
    return opp, total


def check_actual_shells():
    inputs = cases = occupied = lower_window_failed = 0
    first_misses = []
    for p in primes_to(60000):
        if not 2400 < p or p % 24 != 1:
            continue
        inputs += 1
        wins = []
        for r in range(3, 32, 4):
            cases += 1
            a = (p + r) // 4
            base = divisors(a)
            ds = base + [p * t for t in base]
            assert len(ds) == len(set(ds)) and all(p * a % d == 0 for d in ds)
            assert gcd(p * a, r) == 1 and p < 4 * a < 2 * p
            zero, tau = check_histogram(p, r, a, ds, 0)
            pos, total_pos = check_histogram(p, r, a, ds, 1)
            neg, total_neg = check_histogram(p, r, a, ds, -1)
            assert bool(zero) == bool(pos) == bool(neg)
            # The involution d -> S/d sends opposition to opposition.
            assert (pos, total_pos) == (neg, total_neg)
            if cases % 59 == 1:
                matches = [(d, e) for d in ds for e in ds if (d + e) % r == 0]
                assert len(matches) == zero
                assert pos == sum((p * a // d) * (p * a // e) for d, e in matches)
                assert neg == sum(d * e for d, e in matches)
                assert tau == len(ds)
            if zero:
                witness = {d % r: d for d in ds}
                d, e = next((d, witness[-d % r]) for d in ds if -d % r in witness)
                num = p * a * (d + e)
                b, rem_b = divmod(num, d * r)
                c, rem_c = divmod(num, e * r)
                assert rem_b == rem_c == 0 and min(b, c) > a
                assert 4 * a * b * c == p * (b * c + a * c + a * b)
                occupied += 1
                wins.append(r)
            elif len(first_misses) < 4:
                first_misses.append((p, r))
        lower_window_failed += not any(r >= 16 for r in wins)
    print(f"{inputs} primes 1 modulo 24 in (2400,60000], {cases} actual shells, "
          f"{occupied} occupied; {lower_window_failed} primes miss every shift from 19 to 31.")
    print(f"First empty (p,R) pairs ordered by input: {first_misses}")


def check_sieve_factors():
    shifts = (3, 11)
    primes = (5, 7)
    probabilities = ((Fraction(2, 7), Fraction(3, 5)),
                     (Fraction(1, 3), Fraction(4, 5)))
    expected = Fraction()
    for bits in product((0, 1), repeat=4):
        product_density = weight = Fraction(1)
        for i, q in enumerate(primes):
            marked = bits[2 * i:2 * i + 2]
            count = sum(n % q != 0 and all(not mark or (n + r) % q or (n + r) % (q*q) == 0
                                           for r, mark in zip(shifts, marked))
                        for n in range(q*q))
            assert count == q*q - q - sum(marked) * (q - 1)
            product_density *= Fraction(count, q*q)
            weight *= prod(v if b else 1-v for v, b in zip(probabilities[i], marked))
        modulus = prod(q*q for q in primes)
        survivors = 0
        for n in range(modulus):
            if any(n % q == 0 for q in primes):
                continue
            if any(bits[2*i+j] and (n+r) % q == 0 and (n+r) % (q*q) != 0
                   for i, q in enumerate(primes) for j, r in enumerate(shifts)):
                continue
            survivors += 1
        assert product_density == Fraction(survivors, modulus)
        expected += weight * product_density
    exact = prod(Fraction(q-1, q) * (1-sum(probs) / q)
                 for q, probs in zip(primes, probabilities))
    assert expected == exact
    print(f"All 16 two-prime/two-shift mark patterns and all 1225 CRT classes pass; "
          f"expected surviving density {exact}.")


def draw_shell_table():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    ps = [p for p in primes_to(60000) if p % 840 == 1][:12]
    shifts = list(range(3, 32, 4))
    counts = []
    for p in ps:
        row = []
        for r in shifts:
            a = (p + r) // 4
            ad = divisors(a)
            row.append(check_histogram(p, r, a, ad + [p*d for d in ad], 0)[0])
        counts.append(row)
    fig, ax = plt.subplots(figsize=(8, 6.4), layout="constrained")
    ax.imshow([[int(n > 0) for n in row] for row in counts], aspect="auto",
              cmap=ListedColormap(["#efd8bf", "#dcebe2"]), vmin=0, vmax=1)
    for i, row in enumerate(counts):
        for j, n in enumerate(row):
            ax.text(j, i, str(n), ha="center", va="center", color="#20332a")
    ax.set_xticks(range(len(shifts)), shifts)
    ax.set_yticks(range(len(ps)), [str(p) for p in ps])
    ax.tick_params(axis="both", which="both", length=0)
    ax.set_xlabel("Shift R, with first denominator a = (p + R)/4")
    ax.set_ylabel("Prime p congruent to 1 modulo 840")
    ax.set_title("Ordered opposite-divisor pairs at the first eight shifts", pad=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.savefig(Path(__file__).with_name("moving_shells.png"), dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    check_sieve_factors()
    check_actual_shells()
    if "--figure" in sys.argv[1:]:
        draw_shell_table()
