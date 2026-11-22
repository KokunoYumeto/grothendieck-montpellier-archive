"""Exact F2(v)[L] arithmetic localized at v, v+1 and one degree-ten G.

This is computational infrastructure only.  It proves no geometric claim.
Binary-polynomial multiplication uses carry-free integer convolution and
parity extraction; the self-check compares with literal xor multiplication.
"""
from functools import lru_cache

G = (1 << 10) | (1 << 7) | (1 << 5) | (1 << 3) | 1


def slowmul(a, b):
    if a.bit_length() < b.bit_length():
        a, b = b, a
    out = 0
    while b:
        bit = b & -b
        out ^= a << (bit.bit_length() - 1)
        b ^= bit
    return out


@lru_cache(maxsize=512)
def masks(n, k):
    out = []
    bs = n // 2
    while bs:
        m = 0
        block = (1 << bs) - 1
        for i in range(n // bs):
            m |= block << (k * bs * i)
        out.append((bs, m))
        bs //= 2
    return tuple(out)


def spread(a, n, k):
    for bs, mask in masks(n, k):
        a = (a | (a << ((k - 1) * bs))) & mask
    return a


def unspread(a, n, k):
    ms = masks(n, k)
    if ms:
        a &= ms[-1][1]
    for i in range(len(ms) - 1, -1, -1):
        bs = ms[i][0]
        mask = ms[i - 1][1] if i else (1 << n) - 1
        a = (a | (a >> ((k - 1) * bs))) & mask
    return a


@lru_cache(maxsize=8192)
def cmul(a, b):
    if not a or not b:
        return 0
    if min(a.bit_length(), b.bit_length()) <= 96:
        return slowmul(a, b)
    n = 1 << (max(a.bit_length(), b.bit_length()) - 1).bit_length()
    k = min(a.bit_length(), b.bit_length()).bit_length()
    packed = spread(a, n, k) * spread(b, n, k)
    return unspread(packed, 2 * n, k)


def square(a):
    if not a:
        return 0
    n = 1 << (a.bit_length() - 1).bit_length()
    return spread(a, n, 2)


def divmodp(a, b):
    assert b
    q = 0
    shift = a.bit_length() - b.bit_length()
    while shift >= 0:
        q ^= 1 << shift
        a ^= b << shift
        shift = a.bit_length() - b.bit_length()
    return q, a


def gcdp(a, b):
    while b:
        a, b = b, divmodp(a, b)[1]
    return a


def divide_v_plus_one(a):
    assert a.bit_count() % 2 == 0
    q = a >> 1
    shift = 1
    while shift < a.bit_length():
        q ^= q >> shift
        shift <<= 1
    assert slowmul(q, 3) == a
    return q


@lru_cache(maxsize=2048)
def factor_power(b, n):
    result = 1
    while n:
        if n & 1:
            result = cmul(result, b)
        b = square(b)
        n >>= 1
    return result


def trimmed(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


class E:
    """A polynomial in L, divided by v^a (v+1)^b G(v)^c."""
    __slots__ = ("p", "d")

    def __init__(self, p=(), d=(0, 0, 0)):
        if isinstance(p, int):
            p = (p,)
        p = trimmed(p)
        if not p:
            self.p, self.d = (), (0, 0, 0)
            return
        a, b, c = d
        assert min(a, b, c) >= 0
        nonzero = [x for x in p if x]
        va = min((x & -x).bit_length() - 1 for x in nonzero)
        take = min(a, va)
        if take:
            p = tuple(x >> take for x in p)
            a -= take
        while b and all(x.bit_count() % 2 == 0 for x in p):
            p = tuple(divide_v_plus_one(x) if x else 0 for x in p)
            b -= 1
        while c:
            qr = [divmodp(x, G) for x in p]
            if any(rem for _, rem in qr):
                break
            p = tuple(q for q, _ in qr)
            c -= 1
        self.p, self.d = p, (a, b, c)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, E) else E(x & 1)

    def __bool__(self):
        return bool(self.p)

    def __eq__(self, other):
        other = self.coerce(other)
        return self.p == other.p and self.d == other.d

    def __add__(self, other):
        other = self.coerce(other)
        if not self:
            return other
        if not other:
            return self
        den = tuple(max(a, b) for a, b in zip(self.d, other.d))
        ps = []
        for elem in (self, other):
            a, b, c = (x - y for x, y in zip(den, elem.d))
            factor = cmul(factor_power(3, b), factor_power(G, c)) << a
            ps.append([cmul(x, factor) for x in elem.p])
        size = max(map(len, ps))
        return E([(ps[0][i] if i < len(ps[0]) else 0) ^
                  (ps[1][i] if i < len(ps[1]) else 0) for i in range(size)], den)

    __radd__ = __add__
    __sub__ = __add__
    __rsub__ = __add__

    def __mul__(self, other):
        other = self.coerce(other)
        if not self or not other:
            return E()
        if self is other:
            return self.squared()
        out = [0] * (len(self.p) + len(other.p) - 1)
        for i, x in enumerate(self.p):
            if x:
                for j, y in enumerate(other.p):
                    if y:
                        out[i+j] ^= cmul(x, y)
        return E(out, tuple(a+b for a, b in zip(self.d, other.d)))

    __rmul__ = __mul__

    def squared(self):
        if not self:
            return self
        out = [0] * (2 * len(self.p) - 1)
        for i, x in enumerate(self.p):
            out[2*i] = square(x)
        return E(out, tuple(2*x for x in self.d))

    def __pow__(self, n):
        assert n >= 0
        result, a = E(1), self
        while n:
            if n & 1:
                result = result * a
            a = a.squared()
            n >>= 1
        return result

    def inverse_constant(self):
        assert len(self.p) == 1
        q = self.p[0]
        a = (q & -q).bit_length() - 1
        q >>= a
        b = c = 0
        while q.bit_count() % 2 == 0:
            q = divide_v_plus_one(q)
            b += 1
        while True:
            quo, rem = divmodp(q, G)
            if rem:
                break
            q, c = quo, c+1
        assert q == 1, ("unapproved denominator factor", hex(q))
        da, db, dc = self.d
        numerator = cmul(factor_power(3, db), factor_power(G, dc)) << da
        return E(numerator, (a, b, c))

    def __truediv__(self, other):
        return self * self.coerce(other).inverse_constant()

    def serial(self):
        return {"numerator_L_coefficients_v_binary_hex": [hex(x) for x in self.p],
                "denominator_exponents_v_vplus1_G": list(self.d)}


def self_check():
    import random
    random.seed(271128)
    tests = 0
    for n in (1, 2, 3, 15, 16, 31, 32, 63, 64, 95, 96, 97, 127, 128,
              129, 255, 256, 511, 512, 1023):
        for _ in range(6):
            a, b = random.getrandbits(n), random.getrandbits(n)
            assert cmul(a, b) == slowmul(a, b)
            assert square(a) == slowmul(a, a)
            q = slowmul(a, 3)
            assert divide_v_plus_one(q) == a
            tests += 1
    v, L = E(2), E([0, 1])
    gamma = E(G, (0, 4, 0))
    assert gamma * gamma.inverse_constant() == 1
    assert (v+1) / (v+1) == 1
    assert (L+v).squared() == L.squared()+v.squared()
    assert (L+gamma)*(L+v) == L.squared()+(gamma+v)*L+gamma*v
    return tests


if __name__ == "__main__":
    import json, time
    from pathlib import Path
    from datetime import datetime, timezone
    start = time.perf_counter()
    count = self_check()
    result = {"status": "PASS_ARITHMETIC_SELF_CHECK_ONLY", "tests": count,
              "actual_utc": datetime.now(timezone.utc).isoformat(),
              "runtime_seconds": time.perf_counter()-start,
              "scope": "Binary coefficient arithmetic infrastructure; no geometric inference."}
    out = Path(__file__).resolve().parents[1]/"outputs/post_CP27_binary_coefficient_ring.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))
