#!/usr/bin/env python3
"""Independent finite checks for split fibres, OR gates and hidden quadrics.

Run: python3 workbench/programs/structured_verify.py
Uses only the Python standard library. All checks are exact finite arithmetic.
This file is an original implementation for the accompanying paper.
"""
from itertools import product, permutations
from functools import lru_cache
from random import Random
import json


def pdiv(a, b, p):
    a = list(a)
    while a and not a[-1] % p:
        a.pop()
    while len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, p) % p
        for j in range(len(b)):
            a[k+j] = (a[k+j] - c*b[j]) % p
        while a and not a[-1]:
            a.pop()
    return a


class FiniteField:
    def __init__(self, p, degree):
        self.p, self.h, self.q = p, degree, p**degree
        for low in product(range(p), repeat=degree):
            f = list(low) + [1]
            irreducible = True
            for d in range(1, degree//2+1):
                for coeff in product(range(p), repeat=d):
                    if not pdiv(f, list(coeff)+[1], p):
                        irreducible = False
                        break
                if not irreducible:
                    break
            if irreducible:
                self.modulus = f
                break
        self.digits = [tuple((x//p**i) % p for i in range(degree))
                       for x in range(self.q)]

    def encode(self, v):
        return sum((a % self.p)*self.p**i for i, a in enumerate(v))

    def add(self, a, b):
        return self.encode([x+y for x, y in zip(self.digits[a], self.digits[b])])

    def neg(self, a):
        return self.encode([-x for x in self.digits[a]])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    @lru_cache(None)
    def mul(self, a, b):
        v = [0]*(2*self.h-1)
        for i, x in enumerate(self.digits[a]):
            for j, y in enumerate(self.digits[b]):
                v[i+j] = (v[i+j]+x*y) % self.p
        for i in range(len(v)-1, self.h-1, -1):
            c = v[i]
            for j in range(self.h):
                v[i-self.h+j] = (v[i-self.h+j]-c*self.modulus[j]) % self.p
        return self.encode(v[:self.h])

    def power(self, a, e):
        r = 1
        while e:
            if e & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            e >>= 1
        return r

    def inv(self, a):
        assert a
        return self.power(a, self.q-2)


def rref(a, k):
    a = [list(row) for row in a]
    if not a:
        return a, []
    row, pivots = 0, []
    for col in range(len(a[0])):
        take = next((i for i in range(row, len(a)) if a[i][col]), None)
        if take is None:
            continue
        a[row], a[take] = a[take], a[row]
        c = k.inv(a[row][col])
        a[row] = [k.mul(c, x) for x in a[row]]
        for i in range(len(a)):
            if i != row:
                c = a[i][col]
                a[i] = [k.sub(x, k.mul(c, y)) for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def inverse(a, k):
    n = len(a)
    b, pivots = rref([row+[int(i == j) for j in range(n)]
                      for i, row in enumerate(a)], k)
    if pivots[:n] != list(range(n)):
        return None
    return [row[n:] for row in b]


def mm(a, b, k):
    out = []
    for row in a:
        line = []
        for col in zip(*b):
            v = 0
            for x, y in zip(row, col):
                v = k.add(v, k.mul(x, y))
            line.append(v)
        out.append(line)
    return out


def combination(matrices, lam, k):
    n = len(matrices[0])
    out = [[0]*n for _ in range(n)]
    c = 1
    for a in matrices:
        for i in range(n):
            for j in range(n):
                out[i][j] = k.add(out[i][j], k.mul(c, a[i][j]))
        c = k.mul(c, lam)
    return out


def recover_axes(matrices, p):
    t = len(matrices)
    degree = 1
    while p**degree <= t**3+1:
        degree += 1
    k = FiniteField(p, degree)
    for lam in range(k.q):
        h = combination(matrices, lam, k)
        ih = inverse(h, k)
        if ih is not None:
            break
    else:
        raise AssertionError('No regular pencil value')
    for mu in range(k.q):
        a = mm(ih, combination(matrices, mu, k), k)
        eigen = []
        for val in range(k.q):
            b = [[k.sub(a[i][j], val if i == j else 0)
                  for j in range(t)] for i in range(t)]
            rr, pivots = rref(b, k)
            if len(pivots) < t:
                eigen.append((rr, pivots))
        if len(eigen) == t:
            break
    else:
        raise AssertionError('No separating pencil value')
    columns = []
    for rr, pivots in eigen:
        assert len(pivots) == t-1
        free = next(j for j in range(t) if j not in pivots)
        v = [int(j == free) for j in range(t)]
        for i, pivot in enumerate(pivots):
            v[pivot] = k.neg(rr[i][free])
        assert all(x < p for x in v), 'Eigenline did not descend'
        columns.append(v)
    return [list(row) for row in zip(*columns)], k.q, lam, mu


def invertible_matrix(t, p, rng):
    k = FiniteField(p, 1)
    while True:
        a = [[rng.randrange(p) for _ in range(t)] for _ in range(t)]
        if inverse(a, k) is not None:
            return a


def hidden_quadrics():
    rng = Random(63721)
    cases = []
    for p in (3, 5, 7):
        kp = FiniteField(p, 1)
        for t in (1, 2, 3, 4):
            a = invertible_matrix(t, p, rng)
            mix = invertible_matrix(t, p, rng)
            # Two base bits; translations b_i*x+c_i are arbitrary.
            shifts = [[rng.randrange(p) for _ in range(3)] for _ in range(t)]
            matrices = [[[sum(mix[j][i]*a[i][u]*a[i][v] for i in range(t)) % p
                          for v in range(t)] for u in range(t)] for j in range(t)]
            axes, q, lam, mu = recover_axes(matrices, p)
            ap = mm(a, axes, kp)
            assert all(sum(bool(v) for v in row) == 1 for row in ap)
            assert len({next(j for j, v in enumerate(row) if v) for row in ap}) == t
            d = [[sum(mix[j][i]*ap[i][u]**2 for i in range(t)) % p
                  for u in range(t)] for j in range(t)]
            di = inverse(d, kp)
            assert di is not None
            # q_u uses row u of d^{-1} as weights on the input quadrics.
            for u in range(t):
                weights = di[u]
                orig = [sum(weights[j]*mix[j][i] for j in range(t)) % p
                        for i in range(t)]
                owner = next(i for i in range(t) if ap[i][u])
                scale = ap[owner][u]
                assert orig[owner] == pow(scale*scale, -1, p)
                assert all(orig[i] == 0 for i in range(t) if i != owner)
                for x in product((0, 1), repeat=2):
                    shift = (sum(shifts[owner][j]*x[j] for j in range(2))
                             + shifts[owner][2]) % p
                    half_linear = shift*pow(scale, -1, p) % p
                    const = (shift*shift-1)*pow(scale*scale, -1, p) % p
                    delta = (half_linear**2-const) % p
                    assert delta == pow(scale*scale, -1, p)
                    assert any(v*v % p == delta for v in range(1, p))
            # Binary exponent reduction is only asserted on F_p values.
            huge = (1 << 70)+17
            for z in range(p):
                assert pow(z, huge, p) == pow(z, 1+(huge-1) % (p-1), p)
            cases.append({'p': p, 'private': t, 'extension_size': q,
                          'pencil_parameters': [lam, mu]})
    return cases


def or_minimum(p, degree, r):
    q, count = p**degree, 1 << r
    digits = [tuple((a//p**i) % p for i in range(degree)) for a in range(q)]
    def add(a, b):
        return sum(((x+y) % p)*p**i for i, (x, y) in enumerate(zip(digits[a],digits[b])))
    legal_masks = set()
    for coeff in product(range(q), repeat=r):
        values = []
        for x in range(count):
            val = 1
            for i, c in enumerate(coeff):
                if x >> i & 1:
                    val = add(val, c)
            values.append(val)
        for c in range(q):
            if any(add(v, c) == 0 for v in values[1:]):
                continue
            mask = int(add(1, c) == 0)
            for x in range(1, count):
                if values[x] == 0:
                    mask |= 1 << x
            if mask:
                legal_masks.add(mask)
    whole = (1 << count)-1
    union = 0
    for m in legal_masks:
        union |= m
    if union != whole:
        return None
    best = {0: 0}
    for depth in range(1, r+2):
        frontier = set()
        for old in best:
            for m in legal_masks:
                new = old | m
                if new == whole:
                    return depth
                if new not in best:
                    frontier.add(new)
        for new in frontier:
            best[new] = depth
    raise AssertionError('Set cover did not terminate')


def private_permutation():
    k = FiniteField(3,1)
    initial = [(0,1),(2,3),(4,5),(6,7)]
    changed = [(0,1),(2,4),(3,6),(5,7)]
    def row_list(pairs):
        return [[int((mask & (a ^ b)).bit_count() % 2 == 0)
                 for a, b in pairs] for mask in range(8)]
    old, new = row_list(initial), row_list(changed)
    assert len(rref(old,k)[1]) == 1
    assert len(rref(new,k)[1]) == 4
    return {'old_rank':1,'new_rank':4,'new_squared_rows':new}


def valuation_multiplier():
    out = []
    for a in (1,2,3,5,10,20,40,100,300):
        n = 1
        while (1 << n) < 3**(a+1):
            n *= 2
        base, increments = 0, []
        for k in range(1,n+1):
            b = 2*((1<<n)-(-1)**k*(1<<(n-k)))//3
            delta = (-1)**k*(1<<(n-k))
            base += min(b,b+delta)
            increments.append(abs(delta))
        target = base + ((3**a-base) % 3**(a+1))
        assert base <= target < base+(1<<n)
        assert target % 3**(a+1) == 3**a
        assert sorted(increments) == [1 << j for j in range(n)]
        if n <= 8:
            # Enumerate the selected actual polynomial values on its entire cube.
            total = 0
            for k in range(1,n+1):
                delta = (-1)**k*(1<<(n-k))
                choose_high = (target-base) >> (n-k) & 1
                offset = (int(k % 2 == 1) ^ choose_high)
                for signs in product((-1,1), repeat=n):
                    total += (sum(signs[:k])+offset) % 3 != 0
            assert total == target
        out.append({'valuation':a,'independent_signs':n,'support_bits':target.bit_length()})
    return out


def bilinear_fibres():
    checked = 0
    for m in range(1,8):
        for k in range(m+1):
            direct = sum(sum(v[:k]) % 3 == 1 for v in product((-1,1), repeat=m))
            formula = (1 << (m-k))*((1<<k)-(-1)**k)//3
            assert direct == formula
            if k:
                a, b = direct, k
                va = vb = 0
                while a % 3 == 0:
                    a //= 3; va += 1
                while b % 3 == 0:
                    b //= 3; vb += 1
                assert va == vb
            checked += 1
    return checked


def mixed_add(a, b, p):
    out=dict(a)
    for key,c in b.items():
        out[key]=(out.get(key,0)+c)%p
        if not out[key]: del out[key]
    return out


def mixed_mul(a, b, p):
    out={}
    for (x,z),c in a.items():
        for (u,v),d in b.items():
            key=(x|u,z^v)
            out[key]=(out.get(key,0)+c*d)%p
    return {key:c for key,c in out.items() if c}


def mixed_power(a, e, p):
    out={(0,0):1}
    for _ in range(e): out=mixed_mul(out,a,p)
    return out


def mixed_eval(a, x, z, p):
    return sum(c*((-1)**((b&z).bit_count()%2)) for (v,b),c in a.items()
               if x&v==v)%p


def powered_rows(b,p):
    rows={}
    for (a,beta),c in b.items(): rows.setdefault(beta,{})[(a,0)]=c
    return {tuple(sorted(mixed_power(row,p-1,p).items())) for row in rows.values()}


def split_row_tests():
    rng=Random(85213); checks=0; shears=0
    for p in (3,5,7):
        k=FiniteField(p,1)
        n,t=3,2
        for trial in range(20):
            equations=[]
            for _ in range(1+trial%2):
                f={}
                for j in range(5):
                    key=(rng.randrange(1<<n),rng.randrange(1<<t))
                    f[key]=rng.randrange(1,p)
                equations.append(f)
            indicator={(0,0):1}
            for f in equations:
                neg={key:(-c)%p for key,c in mixed_power(f,p-1,p).items()}
                indicator=mixed_mul(indicator,mixed_add({(0,0):1},neg,p),p)
            rows=powered_rows(indicator,p)
            vectors=[[dict(row).get((mask,0),0) for mask in range(1<<n)]
                     for row in rows]
            # Pick original independent rows greedily, not echelon combinations.
            basis=[]; basis_polys=[]
            for row,vector in zip(rows,vectors):
                if len(rref(basis+[vector],k)[1])>len(basis):
                    basis.append(vector); basis_polys.append(dict(row))
            empty={(0,0):1}
            for row in basis_polys:
                empty=mixed_mul(empty,mixed_add({(0,0):1},
                                  {key:(-c)%p for key,c in row.items()},p),p)
            for x in range(1<<n):
                population=0
                for z in range(1<<t):
                    good=all(mixed_eval(f,x,z,p)==0 for f in equations)
                    assert mixed_eval(indicator,x,z,p)==int(good)
                    population+=good
                assert mixed_eval(empty,x,0,p)==int(population==0)
                checks+=1
            # Multiply by a nonzero indicator on one fresh sign, then hide it.
            extended=mixed_mul(indicator,{(0,0):pow(2,-1,p),
                                       (0,1<<t):pow(2,-1,p)},p)
            dim=t+1
            images=[1<<j for j in range(dim)]
            for _ in range(12):
                i,j=rng.sample(range(dim),2);images[i]^=images[j]
            shifts=[rng.randrange(1<<n) for _ in range(dim)]
            transformed={}
            for (mask,beta),c in extended.items():
                newmask=shear=0
                for j in range(dim):
                    if beta>>j&1: newmask^=images[j];shear^=shifts[j]
                unit={(0,0):1}
                for j in range(n):
                    if shear>>j&1:
                        unit=mixed_mul(unit,{(0,0):1,(1<<j,0):(-2)%p},p)
                term=mixed_mul({(mask,newmask):c},unit,p)
                transformed=mixed_add(transformed,term,p)
            assert powered_rows(transformed,p)==rows
            shears+=1
    return {'base_word_checks':checks,'hidden_multiplier_checks':shears,
            'primes':[3,5,7]}

def main():
    or_cases=[]
    for p,d in ((2,1),(3,1),(2,2),(5,1),(2,3),(3,2)):
        maximum=d*(p-1)
        got=[or_minimum(p,d,r) for r in range(1, maximum+2)]
        assert got == list(range(1,maximum+1))+[None]
        or_cases.append({'q':p**d,'minimum_forms_positive_arities':got})
    result={'OR_exact_covers':or_cases,'hidden_quadric_recovery':hidden_quadrics(),
            'private_permutation_counterexample':private_permutation(),
            'valuation_multipliers':valuation_multiplier(),
            'bilinear_population_checks':bilinear_fibres(),'split_row_rank_checks':split_row_tests()}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
