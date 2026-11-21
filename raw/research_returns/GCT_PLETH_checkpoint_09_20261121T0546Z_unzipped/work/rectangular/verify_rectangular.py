"""Exact finite certificates for report R-001/R-002/R-003.

No third-party packages. Run from any working directory.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path

OUT = Path(__file__).resolve().parent


@lru_cache(None)
def partitions(n, bound=None):
    bound = n if bound is None else min(n, bound)
    if n == 0:
        return ((),)
    return tuple((k,) + rest for k in range(bound, 0, -1)
                 for rest in partitions(n-k, k))


def z(part):
    ans = 1
    for k, m in Counter(part).items():
        ans *= k**m * factorial(m)
    return ans


def sign(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                    for j in range(i+1, len(p))) % 2 else 1


def latin_reduced(n):
    """First row and first column are 0,1,...,n-1; all squares counted."""
    first = tuple(range(n))
    candidates = {i: [p for p in permutations(range(n)) if p[0] == i]
                  for i in range(1, n)}
    rows = [first]
    used = [1 << j for j in range(n)]
    count = signed = 0

    def visit(i):
        nonlocal count, signed
        if i == n:
            count += 1
            col_sign = 1
            for j in range(n):
                col_sign *= sign(tuple(rows[k][j] for k in range(n)))
            signed += col_sign
            return
        for p in candidates[i]:
            if any(used[j] & (1 << p[j]) for j in range(n)):
                continue
            rows.append(p)
            for j in range(n):
                used[j] |= 1 << p[j]
            visit(i+1)
            for j in range(n):
                used[j] ^= 1 << p[j]
            rows.pop()
    visit(1)
    return count, signed


@lru_cache(None)
def rim_removals(lam, k):
    out = []
    for mu in partitions(sum(lam)-k):
        if len(mu) > len(lam) or any(mu[i] > lam[i] for i in range(len(mu))):
            continue
        padded = mu + (0,)*(len(lam)-len(mu))
        cells = {(i,j) for i in range(len(lam)) for j in range(padded[i], lam[i])}
        if len(cells) != k:
            continue
        if any((i+1,j) in cells and (i,j+1) in cells and (i+1,j+1) in cells
               for i,j in cells):
            continue
        seen = set()
        todo = [next(iter(cells))]
        while todo:
            pos = todo.pop()
            if pos in seen:
                continue
            seen.add(pos)
            i,j = pos
            todo.extend(q for q in ((i+1,j),(i-1,j),(i,j+1),(i,j-1))
                        if q in cells and q not in seen)
        if seen != cells:
            continue
        out.append((mu, (-1)**(len({i for i,j in cells})-1)))
    return tuple(out)


@lru_cache(None)
def character(lam, cyc):
    if not cyc:
        return int(not lam)
    return sum(s * character(mu, cyc[1:]) for mu,s in rim_removals(lam,cyc[0]))


def hook_character(cyc,k):
    # det(1+t sigma | standard) = prod_l (1-(-t)^l)/(1+t).
    coeff = [1] + [0]*k
    for ell in cyc:
        for j in range(k,ell-1,-1):
            coeff[j] -= (-1)**ell * coeff[j-ell]
    return sum((-1)**(k-j)*coeff[j] for j in range(k+1))


def power_sum_plethysm(d,n):
    # h_d[h_n] in the p-basis, with exact rational coefficients.
    result = defaultdict(Fraction)
    for alpha in partitions(d):
        term = {(): Fraction(1,z(alpha))}
        for k in alpha:
            nxt = defaultdict(Fraction)
            for mu,c in term.items():
                for beta in partitions(n):
                    nu = tuple(sorted(mu + tuple(k*x for x in beta), reverse=True))
                    nxt[nu] += c / z(beta)
            term = nxt
        for nu,c in term.items():
            result[nu] += c
    return result


def run():
    lines = ['n\treduced_total\treduced_column_signed\ttotal\tcolumn_signed\thowe_scalar']
    expected = {2:(1,-1),4:(4,4),6:(9408,-2304)}
    for n in (2,4,6):
        count,signed = latin_reduced(n)
        assert (count,signed) == expected[n], (n,count,signed)
        factor = factorial(n)*factorial(n-1)
        delta = signed*factor
        scalar = Fraction(delta,factorial(n)**n)
        lines.append(f'{n}\t{count}\t{signed}\t{count*factor}\t{delta}\t{scalar}')
    (OUT/'latin_scalar_certificates.tsv').write_text('\n'.join(lines)+'\n')

    n=d=4; k=3; N=n*d; rectangle=(4,4,4,4)
    g = sum(Fraction(hook_character(cyc,k)*character(rectangle,cyc)**2,z(cyc))
            for cyc in partitions(N))
    a = sum(c*hook_character(cyc,k) for cyc,c in power_sum_plethysm(d,n).items())
    assert g == 1 and a == 0, (g,a)
    hook_poly = [1]
    for j in range(2,d+1):
        ell = 2*j-1
        new = hook_poly + [0]*ell
        for i,c in enumerate(hook_poly):
            new[i+ell] += c
        hook_poly = new
    assert hook_poly[k] == g
    out = ('lambda\td\tn\tplethysm_a\trectangular_g\tmethod\n'
           f'(13,1,1,1)\t4\t4\t{a}\t{g}\t'
           'cycle-index plethysm; Murnaghan-Nakayama class sum\n')
    (OUT/'hook_counterexample.tsv').write_text(out)
    print((OUT/'latin_scalar_certificates.tsv').read_text(),end='')
    print(out,end='')


if __name__ == '__main__':
    run()
