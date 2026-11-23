"""HD-N19, 21 November 2026, GPT-6 Astra Pro, inherited effort.

Universal binomial exterior-ideal calculation over Q(d), with every cycle
checked to have exponent zero.  Therefore the quotient ranks are the same
for every nonzero d.  A separate, fresh exterior implementation checks the
whole-character Hochschild ranks at two finite fields and indefinite eta.
No stored ranks or matrices are loaded.
"""
from itertools import combinations
from math import comb, factorial
from fractions import Fraction
from pathlib import Path
import json


def wedge_sign(a, b):
    if a & b:
        return 0
    inv = sum((b & ((1 << i)-1)).bit_count()
              for i in range(12) if (a >> i) & 1)
    return -1 if inv % 2 else 1


def mul_weight(a, b):
    return a[0]*b[0], a[1]+b[1]


def inv_weight(a):
    return a[0], -a[1]


class BinomialQuotient:
    """A basis vector equals its parent times sign*d**exponent."""
    def __init__(self, masks):
        self.parent = {m: m for m in masks}
        self.weight = {m: (1, 0) for m in masks}
        self.zero = set()
        self.cycles = 0
        self.zero_cycles = 0

    def find(self, a):
        p = self.parent[a]
        if p == a:
            return a, (1, 0)
        root, w = self.find(p)
        self.weight[a] = mul_weight(self.weight[a], w)
        self.parent[a] = root
        return root, self.weight[a]

    def force_zero(self, a):
        root, _ = self.find(a)
        self.zero.add(root)

    def relate(self, a, b, ratio):
        """Impose a=ratio*b, with ratio a signed power of d."""
        ra, wa = self.find(a)
        rb, wb = self.find(b)
        rel = mul_weight(mul_weight(ratio, wb), inv_weight(wa))
        if ra == rb:
            self.cycles += 1
            # The number of A indices controls the exponent, so a cycle
            # has exponent zero.  No exceptional nonzero specialization.
            assert rel[1] == 0
            if rel[0] == -1:
                self.zero.add(ra)
                self.zero_cycles += 1
            return
        was_zero = ra in self.zero or rb in self.zero
        self.parent[ra] = rb
        self.weight[ra] = rel
        self.zero.discard(ra)
        if was_zero:
            self.zero.add(rb)

    def dimension(self):
        roots = {self.find(a)[0] for a in self.parent}
        zero_roots = {self.find(a)[0] for a in self.zero}
        return len(roots-zero_roots)


hilbert = []
for k in range(13):
    masks = [sum(1 << i for i in I) for I in combinations(range(12), k)]
    Q = BinomialQuotient(masks)
    relations = 0
    if k >= 2:
        for i, j in combinations(range(6), 2):
            aa = (1 << i) | (1 << j)
            bb = (1 << (i+6)) | (1 << (j+6))
            for I in combinations(range(12), k-2):
                m = sum(1 << t for t in I)
                sa, sb = wedge_sign(aa, m), wedge_sign(bb, m)
                # (A_i A_j+d B_i B_j) wedge m.
                if not sa and not sb:
                    continue
                relations += 1
                if not sa:
                    Q.force_zero(bb | m)
                elif not sb:
                    Q.force_zero(aa | m)
                else:
                    Q.relate(aa | m, bb | m, (-sb*sa, 1))
    dim = Q.dimension()
    expected = (1 if k == 0 else 12 if k == 1 else 51 if k == 2
                else 2*comb(6, k) if k <= 6 else 0)
    assert dim == expected, (k, dim, expected)
    hilbert.append(dict(degree=k, ambient=comb(12, k), quotient=dim,
                        relations=relations, consistency_cycles=Q.cycles,
                        forced_zero_cycles=Q.zero_cycles,
                        all_cycles_have_exponent_zero=True))


def wedge(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            sign = wedge_sign(ma, mb)
            if sign:
                key = ma | mb
                out[key] = out.get(key, 0)+sign*ca*cb
    return {m: c for m, c in out.items() if c}


def contract(a, i):
    bit = 1 << i
    return {m ^ bit: c*(-1 if (m & (bit-1)).bit_count() % 2 else 1)
            for m, c in a.items() if m & bit}


def hh_action(a, i):
    # Holomorphic forms are the even positions, antiholomorphic the odd.
    return (wedge({1 << (2*i+1): 1}, a) if i < 6
            else contract(a, 2*(i-6)))


def rank(columns, p):
    basis = {}
    for col in columns:
        v = {m: int(c) % p for m, c in col.items() if int(c) % p}
        while v:
            lead = min(v)
            if lead not in basis:
                scale = pow(v[lead], -1, p)
                basis[lead] = {m: c*scale % p for m, c in v.items()}
                break
            a = v[lead]
            for m, c in basis[lead].items():
                t = (v.get(m, 0)-a*c) % p
                if t:
                    v[m] = t
                else:
                    v.pop(m, None)
    return len(basis)


eta = {(1 << (2*i)) | (1 << (2*i+1)): c
       for i, c in enumerate((1, 2, 3, -4, -5, -6))}
eta2 = wedge(eta, eta)
eta4 = wedge(eta2, eta2)
eta6 = wedge(eta4, eta2)
assert eta6[(1 << 12)-1] == factorial(6)*(-720)
rank_cases = []
for d in (1, 2, 7, 163):
    # 360 times the exact rank-two character.
    v = {0: 720}
    for form, c in ((eta2, -360*d), (eta4, 30*d*d), (eta6, -d**3)):
        for m, a in form.items():
            v[m] = v.get(m, 0)+c*a
    row = dict(d=d, eta_diagonal=[1, 2, 3, -4, -5, -6], fields={})
    for k in (1, 2, 3, 4, 5, 6):
        columns = []
        for I in combinations(range(12), k):
            w = v
            for i in reversed(I):
                w = hh_action(w, i)
            columns.append(w)
        # At k=6 the two exponential images share the same top
        # antiholomorphic line.  Degree4, used in the proof, has rank30.
        expected = (12 if k == 1 else 30 if k == 2 else 1 if k == 6
                    else 2*comb(6, k))
        for p in (1009, 65537):
            got = rank(columns, p)
            assert got == expected, (d, k, p, got)
            row['fields'].setdefault(str(p), {})[str(k)] = got
    rank_cases.append(row)

# Exact RR top coefficients in the formal variable eta, for d=1;
# the common factor d^3 and the volume cancel in the ratio.
ch = {0: Fraction(2), 2: Fraction(-1), 4: Fraction(1, 12),
      6: Fraction(-1, 360)}
end_top = sum(a*b for i, a in ch.items() for j, b in ch.items() if i+j == 6)
assert end_top == Fraction(-8, 45)
assert end_top/ch[6] == 64
result = dict(statement='HD-N19', date='2026-11-21',
              universal_exterior_quotient=hilbert,
              independent_character_rank_cases=rank_cases,
              RR_ratio=64, universal_claim_scope='all nonzero d for quotient',
              note='Finite-field character ranks are cross-checks; proof is in TeX.')
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print('PASS: universal Hilbert vector', [r['quotient'] for r in hilbert])
print('PASS: 48 independent modular character ranks; RR ratio64.')
