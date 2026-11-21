"""Exact bounded checks of the cyclic generators and old syzygies in R23."""
from math import comb
from pathlib import Path
import json
from check_uniform_staircase import field, product


def rank(columns, p):
    if not columns:
        return 0
    a = [list(row) for row in zip(*columns)]
    row = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(row, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col] % p, -1, p)
        a[row] = [x * inv % p for x in a[row]]
        for i in range(row + 1, len(a)):
            v = a[i][col] % p
            if v:
                a[i] = [(x - v * y) % p for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def check(m):
    p, q = field(m)
    block_ranks = []
    for k in range(m):
        aa = product([pow(q, i, p) for i in range(m - k - 1)], p)
        bb = product([pow(q, i, p) for i in range(m - k - 1, m - 1)], p)
        columns = [[a * b * pow(q, t * (i + j), p) % p
                    for i, a in enumerate(aa) for j, b in enumerate(bb)]
                   for t in range(m)]
        block_ranks.append(rank(columns, p))
    assert block_ranks == [m] * m
    entries = {}
    for i in range(m):
        entries[i, i] = [1, -pow(q, i, p) % p, 0, 0]
        entries[i, (i + 1) % m] = [0, 0, 1, -pow(q, i, p) % p]
    relations = []
    for side in ('row', 'column'):
        for index in range(1, m):
            col = []
            for i in range(m):
                for j in range(m):
                    pos = i if side == 'row' else j
                    scalar = int(pos == index) - int(pos == 0)
                    col += [scalar * x % p for x in entries.get((i, j), [0] * 4)]
            relations.append(col)
    old_rank = rank(relations, p)
    assert old_rank == 2 * m - 2
    return {'m': m, 'p': p, 'q': q, 'gradient_rank': sum(block_ranks),
            'old_relation_rank': old_rank, 'passed': True}


def main():
    data = {'cyclic_checks': [check(m) for m in range(3, 13)],
            'generic_defects_from_proved_dominance':
                [{'m': m, 'epsilon': 4 * m * m - 2 * m + 2 - comb(m + 3, 3)}
                 for m in range(3, 17)],
            'scope': 'bounded generator and relation ranks; generic epsilon uses existing R13 theorem, not a fresh generic-Jacobian run',
            'passed': True}
    Path(__file__).with_name('tor_defect_check.json').write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
