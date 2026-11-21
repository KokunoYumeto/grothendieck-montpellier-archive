"""Independent cycle-index / MN checks for both T032--T034 chambers.

The proposed side counts the displayed polytope lattice points directly.
The actual side expands s_mu[h_n] in power sums, then uses rim-hook
Murnaghan--Nakayama character values. No balanced-chart or SO3 characters
are used on the actual side.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter, defaultdict
from functools import lru_cache
import csv
from verify_rectangular import partitions, z, character

HERE = Path(__file__).resolve().parent
TAGS = {
    (4,): (0, 9),
    (1, 1, 1, 1): (3, 6),
    (2, 2): (2, 4, 5, 7),
    (3, 1): (2, 3, 4, 5, 6, 7),
    (2, 1, 1): (1, 3, 4, 5, 6, 8),
}


def transpose(lam):
    return tuple(sum(x >= j for x in lam)
                 for j in range(1, max(lam, default=0) + 1))


@lru_cache(None)
def power_sum(mu, n):
    ans = defaultdict(Fraction)
    for rho in partitions(sum(mu)):
        chi = character(mu, rho)
        if not chi:
            continue
        term = {(): Fraction(chi, z(rho))}
        for k in rho:
            nxt = defaultdict(Fraction)
            for old, coeff in term.items():
                for beta in partitions(n):
                    cyc = tuple(sorted(old + tuple(k*j for j in beta), reverse=True))
                    nxt[cyc] += coeff / z(beta)
            term = nxt
        for cyc, coeff in term.items():
            ans[cyc] += coeff
    return {cyc: coeff for cyc, coeff in ans.items() if coeff}


@lru_cache(None)
def actual(mu, n, lam):
    shape = tuple(x for x in lam if x)
    result = sum((coeff * character(shape, cyc)
                  for cyc, coeff in power_sum(mu, n).items()), Fraction())
    assert result.denominator == 1 and result >= 0
    return int(result)


@lru_cache(None)
def chamber(mu, lam):
    c, b, d = lam[1] - lam[2], lam[2] - lam[3], lam[3]
    A, s = max(c, b), min(c, b)
    tau = transpose(mu) if (c+d) % 2 else mu
    count = 0
    for e in TAGS[tau]:
        for j in range((s-1)//2 + 1):
            for x in range((A+s)//4 + 1):
                for y in range((A+s)//6 + 1):
                    count += s-2*j <= 4*x+6*y+e <= s-2*j+A
        if s % 2 == 0:
            for j in range(A//2 + 1):
                for x in range(A//4 + 1):
                    for y in range(A//6 + 1):
                        count += 2*j+4*x+6*y == A-e
    return count


def main():
    rows = []
    for n in range(7):
        for part in partitions(4*n):
            if len(part) > 4:
                continue
            lam = part + (0,)*(4-len(part))
            lower, upper = lam[1] <= n, lam[2] >= n
            if not (lower or upper):
                continue
            for mu in partitions(4):
                value = actual(mu, n, lam)
                if lower:
                    expected = chamber(mu, lam)
                    assert value == expected, (n, mu, lam, value, expected, 'lower')
                    rows.append(dict(chamber='lower', n=n,
                        outer=','.join(map(str,mu)), output=','.join(map(str,lam)),
                        transformed_n=n, transformed_outer=','.join(map(str,mu)),
                        transformed_output=','.join(map(str,lam)),
                        cycle_index_MN=value, lattice_count=expected, status='PASS'))
                if upper:
                    H = lam[0]
                    hat = (H-lam[3], H-lam[2], H-lam[1], 0)
                    hatn = H-n
                    hatmu = transpose(mu) if H % 2 else mu
                    assert hat[1] <= hatn and sum(hat) == 4*hatn
                    expected = chamber(hatmu, hat)
                    assert value == expected, (n, mu, lam, value, expected, 'upper')
                    rows.append(dict(chamber='upper', n=n,
                        outer=','.join(map(str,mu)), output=','.join(map(str,lam)),
                        transformed_n=hatn, transformed_outer=','.join(map(str,hatmu)),
                        transformed_output=','.join(map(str,hat)),
                        cycle_index_MN=value, lattice_count=expected, status='PASS'))
        print('completed n =', n, 'cases =', len(rows), flush=True)
    with (HERE/'OUTER4_CHAMBER_INDEPENDENT_CHECK.tsv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    print('PASS all', len(rows), 'cases:', dict(Counter(r['chamber'] for r in rows)))


if __name__ == '__main__':
    main()
