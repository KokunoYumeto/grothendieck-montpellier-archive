"""Independent finite character verification of the rank-six exterior cube table.

Does not import few_columns.py. The two sides are built by:
  1. Gray-code enumeration of all 2^20 subsets of the twenty 3-subsets;
  2. direct semistandard-tableau enumeration for each reported Schur summand.
Every torus-weight coefficient in every exterior degree is compared exactly.
"""
from collections import Counter
import csv
from hashlib import sha256
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT / 'work/theta/EXTERIOR_CUBE_RANK_6.tsv'
OUT = Path(__file__).resolve().parent


def exterior_by_gray_subsets():
    triples = tuple(combinations(range(6),3))
    result = [Counter() for _ in range(21)]
    weights = [0]*6
    degree = 0
    result[0][tuple(weights)] = 1
    for i in range(1,1 << 20):
        bit = i & -i
        which = bit.bit_length()-1
        gray = i ^ (i >> 1)
        change = 1 if gray & bit else -1
        degree += change
        for j in triples[which]:
            weights[j] += change
        result[degree][tuple(weights)] += 1
    return result


def schur_by_semistandard(lam):
    """Weight generating function of SSYT of shape lam with entries 0,...,5.

    Full height-six columns are removed first. Their filling is forced to be
    0,1,...,5; reinserting them adds a common determinant twist to each weight.
    """
    twist = lam[-1]
    shape = tuple(v-twist for v in lam)
    cells = [(r,c) for r in range(6) for c in range(shape[r])]
    diagram = [[-1]*shape[r] for r in range(6)]
    heights = [sum(v>c for v in shape) for c in range(max(shape,default=0))]
    weights = [twist]*6
    result = Counter()

    def visit(pos):
        if pos == len(cells):
            result[tuple(weights)] += 1
            return
        r,c = cells[pos]
        low = 0
        if c:
            low = max(low,diagram[r][c-1])
        if r:
            low = max(low,diagram[r-1][c]+1)
        high = 5 - (heights[c]-r-1)
        for entry in range(low,high+1):
            diagram[r][c] = entry
            weights[entry] += 1
            visit(pos+1)
            weights[entry] -= 1
        diagram[r][c] = -1
    visit(0)
    return result


def main():
    with TABLE.open() as f:
        rows = list(csv.DictReader(f,delimiter='\t'))
    actual = exterior_by_gray_subsets()
    predicted = [Counter() for _ in range(21)]
    summands = [0]*21
    tableau_total = 0
    for row in rows:
        deg = int(row['exterior_degree'])
        lam = tuple(map(int,row['partition'].split(',')))
        mult = int(row['multiplicity'])
        dim = int(row['dimension'])
        assert len(lam)==6 and all(lam[i]>=lam[i+1] for i in range(5))
        assert sum(lam)==3*deg
        character = schur_by_semistandard(lam)
        enumerated = sum(character.values())
        assert enumerated == dim, (deg,lam,enumerated,dim)
        tableau_total += enumerated*mult
        summands[deg] += 1
        for wt, coeff in character.items():
            predicted[deg][wt] += mult*coeff
    assert predicted == actual, 'A full torus-character coefficient differs.'
    assert len(rows)==156 and all(int(row['multiplicity'])==1 for row in rows)
    assert tableau_total == 2**20
    summary = ['exterior_degree\tsummands\tdistinct_weights\tdimension\tfull_character_equal']
    for j in range(21):
        summary.append(f'{j}\t{summands[j]}\t{len(actual[j])}\t{sum(actual[j].values())}\ttrue')
    (OUT/'EXTERIOR_CUBE_INDEPENDENT_CHECK.tsv').write_text('\n'.join(summary)+'\n')
    receipt = ('Exact independent verification passed.\n'
               'Source table: '+str(TABLE)+'\n'
               'Source table SHA256: '+sha256(TABLE.read_bytes()).hexdigest()+'\n'
               'Left side: Gray-code enumeration of all 1,048,576 subsets.\n'
               'Right side: all 1,048,576 semistandard tableaux in the 156 summands.\n'
               'All 21 exterior degrees and every torus-weight coefficient agree.\n')
    (OUT/'EXTERIOR_CUBE_INDEPENDENT_CHECK.txt').write_text(receipt)
    print(receipt,end='')


if __name__ == '__main__':
    main()
