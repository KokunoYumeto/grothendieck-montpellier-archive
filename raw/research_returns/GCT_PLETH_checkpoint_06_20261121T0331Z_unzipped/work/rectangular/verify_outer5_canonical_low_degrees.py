"""Exact low-degree multiplicities for the actual canonical outer-five map.

Character arithmetic here is independent of the published injectivity input.
Two coefficient computations are compared: literal power-sum expansion plus
Murnaghan--Nakayama, and a direct monomial multiset character plus alternant.
The n=4 source is additionally compared with T037's positive polytopes.
"""
from pathlib import Path
from itertools import permutations
from collections import defaultdict
from math import comb
import csv
import importlib.util
import sys

from verify_rectangular import partitions, sign
from verify_outer4_chambers import actual

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'outer4_positive_audit', HERE.parent/'theta/outer4/outer4_positive.py')
positive = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = positive
spec.loader.exec_module(positive)


def compositions(n, r):
    if r == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in compositions(n - first, r - 1):
            yield (first,) + rest


def multiset_character(outer, inner, rank):
    dp = [defaultdict(int) for _ in range(outer + 1)]
    dp[0][(0,)*rank] = 1
    for alpha in compositions(inner, rank):
        # Ascending j permits every multiplicity of the present monomial.
        for j in range(1, outer + 1):
            for weight, coeff in dp[j-1].items():
                beta = tuple(x+y for x, y in zip(weight, alpha))
                dp[j][beta] += coeff
    assert sum(dp[outer].values()) == comb(comb(inner+rank-1, rank-1)+outer-1, outer)
    return dp[outer]


def alternant_coefficient(character, lam, rank):
    lam = lam + (0,)*(rank-len(lam))
    rho = tuple(range(rank-1, -1, -1))
    return sum(sign(p)*character.get(tuple(lam[i]+rho[i]-rho[p[i]]
                    for i in range(rank)), 0)
               for p in permutations(range(rank)))


def main():
    rows = []
    strict = []
    for n in range(1, 5):
        source = multiset_character(n, 5, 5)
        target = multiset_character(5, n, 5)
        for shape in partitions(5*n):
            if len(shape) > 5:
                continue
            lam = shape + (0,)*(5-len(shape))
            smn = actual((n,), 5, shape)
            tmn = actual((5,), n, shape)
            sa = alternant_coefficient(source, shape, 5)
            ta = alternant_coefficient(target, shape, 5)
            assert (smn,tmn) == (sa,ta), (n,lam,smn,tmn,sa,ta)
            assert 0 <= smn <= tmn
            four = positive.coefficient((4,), 5, shape) if n == 4 else ''
            assert n != 4 or four == smn, (lam,smn,four)
            row = dict(n=n, output=','.join(map(str,lam)),
                       source_MN=smn, source_monomial_alternant=sa,
                       target_MN=tmn, target_monomial_alternant=ta,
                       outer4_positive=four,
                       actual_image_multiplicity=smn,
                       actual_cokernel_multiplicity=tmn-smn, status='PASS')
            rows.append(row)
            if all(lam[i] > lam[i+1] for i in range(4)):
                strict.append(row)
        print('PASS n =',n,'cumulative partition cases =',len(rows),flush=True)
    for name,data in [('OUTER5_CANONICAL_LOW_DEGREE_CHECK.tsv',rows),
                      ('OUTER5_CANONICAL_STRICT_LOW_DEGREES.tsv',strict)]:
        with (HERE/name).open('w',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=list(data[0]),delimiter='\t')
            writer.writeheader();writer.writerows(data)
    lines = ['| n | Strict partition | Source = actual image | Target | Cokernel |',
             '|---:|---|---:|---:|---:|']
    lines += [f'| {r["n"]} | ({r["output"]}) | {r["source_MN"]} | {r["target_MN"]} | {r["actual_cokernel_multiplicity"]} |'
              for r in strict]
    (HERE/'OUTER5_CANONICAL_STRICT_LOW_DEGREES.md').write_text('\n'.join(lines)+'\n')
    print('PASS',len(rows),'complete low-degree partition cases;',len(strict),'strict cases',flush=True)


if __name__ == '__main__':
    main()
