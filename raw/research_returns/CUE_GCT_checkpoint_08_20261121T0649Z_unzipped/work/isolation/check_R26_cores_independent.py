"""Independent finite audit of R26's 17 normalized Jacobi core minors.

Continuants are enumerated as matchings of a path, without using the
author's continuant recurrence or importing any author check code.  Each
8 by 8 minor is evaluated by its full Leibniz formula, without elimination.
This finite check does not replace the separate vertex-insertion proof.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path
import re

ROOT = Path('/workspace/scratch/64674c0aa6e9')
SOURCE = ROOT / 'work/rectangular/border_ternary/jacobi_uniform_cores.json'
DRAFT = ROOT / 'work/rectangular/r26_fragment.tex'


def matching_coefficients(a, b, edge, prime):
    """Coefficients of sum over disjoint edge subsets of [a,b]."""
    length = max(0, b - a + 1)
    result = [0] * (length // 2 + 1)
    edges = list(range(a, b))
    for mask in range(1 << len(edges)):
        if mask & (mask << 1):
            continue
        value = 1
        number = 0
        for k, e in enumerate(edges):
            if mask >> k & 1:
                value = value * edge[e] % prime
                number += 1
        result[number] = (result[number] + value) % prime
    return result


PERMS = [(p, -1 if sum(p[i] > p[j] for i in range(8)
                       for j in range(i + 1, 8)) % 2 else 1)
         for p in permutations(range(8))]


def leibniz(matrix, prime):
    total = 0
    for permutation, sign in PERMS:
        term = sign
        for i, j in enumerate(permutation):
            term = term * matrix[i][j] % prime
            if not term:
                break
        total = (total + term) % prime
    return total


def reconstruct(item):
    r, j, m, prime = (item[k] for k in ('r', 'j', 'm', 'prime'))
    d, K = item['d'], item['K']
    assert m == r + j and len(d) == m - 1
    assert d[r] and d[j - 1]
    assert all(d[i] == 0 for i in item['cuts'])
    formula = [(7*i*i + 13*i + 36) % prime or 1
               for i in range(m - 1)]
    for i in item['cuts']:
        formula[i] = 0
    assert formula == d
    if min(r, j) < 6:
        numerator = denominator = 1
        for i in range(min(r, j)):
            numerator = numerator * d[i] % prime
        for i in range(max(r, j), m - 1):
            denominator = denominator * d[i] % prime
        assert K == numerator * pow(denominator, -1, prime) % prime
    else:
        left_zeros = sum(not d[i] for i in range(min(r, j)))
        right_zeros = sum(not d[i] for i in range(max(r, j), m - 1))
        assert left_zeros == right_zeros and left_zeros > 0 and K == 14

    # Each tuple is (interval left, interval right, h power, scalar).
    # Powers of x are fixed by the displayed common weighted degrees.
    positive = [(r+1,m-1,0,1), (r,m-1,0,1), (r+2,m-1,1,1),
                (0,j-1,0,1), (0,j,0,1), (0,j-2,1,1),
                (r+1,m-2,1,2), (1,j-1,0,2)]
    negative = [(0,r-1,0,1), (0,r-2,1,d[r-1]),
                (0,r,0,pow(d[r],-1,prime)), (j+1,m-1,0,K),
                (j+2,m-1,1,K*d[j]),
                (j,m-1,0,K*pow(d[j-1],-1,prime)),
                (1,r-1,0,2), (j+1,m-2,1,2*K)]
    plus_length = (j+1)//2+1
    minus_length = (r+1)//2+1
    matrix = [[0]*8 for _ in range(plus_length+minus_length)]
    for offset, specs in ((0, positive), (plus_length, negative)):
        for column, (a,b,power,scale) in enumerate(specs):
            for k, value in enumerate(matching_coefficients(a,b,d,prime)):
                matrix[offset+k+power][column] = value*scale % prime
    assert matrix == item['matrix'], (r,j,'coefficient mismatch')
    rows = item['selected_rows_in_order']
    assert len(rows) == len(set(rows)) == 8
    determinant = leibniz([matrix[i] for i in rows], prime)
    assert determinant == item['selected_minor'] and determinant != 0
    return {'r': r, 'j': j, 'rows': rows, 'determinant_mod_101': determinant,
            'coefficient_entries_verified': 8*len(matrix)}


def main():
    items = json.loads(SOURCE.read_text())
    results = [reconstruct(item) for item in items]
    assert len(results) == 17
    tabular = DRAFT.read_text().split('\\begin{tabular}{rrrlr}')[1].split('\\end{tabular}')[0]
    table = []
    for line in tabular.splitlines():
        if re.match(r'^\d+&\d+&', line):
            cells = line.split('&')
            table.append((int(cells[0]), int(cells[1]), int(cells[2]),
                          list(map(int, re.findall(r'\d+',cells[3]))),
                          int(re.search(r'\d+',cells[4]).group())))
    assert table == [(x['r'],x['j'],x['K'],x['selected_rows_in_order'],
                      x['selected_minor']) for x in items]
    record = {'time_utc': datetime.now(timezone.utc).isoformat(),
              'checker': 'GPT-6 Astra Pro; effort not exposed; agent=/root/isolation',
              'method': 'Independent path-matching enumeration and full 8! Leibniz determinants; no author-code imports.',
              'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
              'draft_sha256': sha256(DRAFT.read_bytes()).hexdigest(),
              'cases': results,
              'scope': 'All 17 finite normalized core matrices/minors and the manuscript table; the uniform insertion proof is audited separately.'}
    output = ROOT / 'work/isolation/R26_cores_independent_checks.json'
    output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'cases':len(results),'entries':sum(x['coefficient_entries_verified'] for x in results),
                      'all_pass':True,'time_utc':record['time_utc'],
                      'output':str(output)}))


if __name__ == '__main__':
    main()
