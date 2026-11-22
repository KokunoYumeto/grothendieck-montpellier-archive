#!/usr/bin/env python3
"""Independent CUE_GCT R-27 endpoint certificate; standard library only.

All entries are built as polynomials in (x,y,z,e), without the supplied
coefficient arrays or the original numerical-e interpolation program.
Uses check_projection.py solely for exact modular Gaussian elimination.
"""
import argparse
import hashlib
import json
from functools import lru_cache
from check_projection import packed_eliminate

P = 101
ZERO = (0, 0, 0, 0)
X, Y, Z = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)]
ALPHA = [86,18,1,17,95,90,80,90,48,100,9,60,2,25,78,53,54]
DELTA = [34,1,37,24,47,1,59,41,0,92,38,56,75,6,44,14]


def add(*polys):
    out = {}
    for poly in polys:
        for mon, value in poly.items():
            out[mon] = (out.get(mon, 0)+value) % P
    return {mon: value for mon, value in out.items() if value}


def mul(*polys):
    out = {ZERO: 1}
    for poly in polys:
        nxt = {}
        for a, va in out.items():
            for b, vb in poly.items():
                mon = tuple(ai+bi for ai, bi in zip(a,b))
                nxt[mon] = (nxt.get(mon, 0)+va*vb) % P
        out = {mon: value for mon, value in nxt.items() if value}
    return out


def shift(poly, a=0, b=0, c=0, scale=1):
    return {(ma+a, mb+b, mc+c, me): value*scale % P
            for (ma,mb,mc,me),value in poly.items() if value*scale % P}


def columns(alpha, delta):
    m, L = len(alpha), len(alpha)-1

    @lru_cache(None)
    def interval(a, b):
        # Partition path matchings by the status of the LEFTMOST vertex.
        if a > b:
            return {ZERO: 1}
        out = shift(interval(a+1,b), a=1, scale=alpha[a])
        if a < b:
            out = add(out, shift(interval(a+2,b), b=1, c=1, scale=delta[a]))
        return out

    def product(start, end):
        out = 1
        for value in delta[start:end]:
            out = out*value % P
        return out

    u0 = {X:1, (0,1,0,1):1, (0,0,1,1):2}
    uL = {Y:1, (1,0,0,1):3, (0,0,1,1):4}
    v0 = {X:1, (0,1,0,1):5, (0,0,1,1):6}
    vL = {Z:1, (1,0,0,1):7, (0,1,0,1):8}
    a, b, t, tp = [], [], [], []
    for i in range(m):
        Di, Ei = product(i,L), product(0,i)
        a.append(add(shift(mul(v0,interval(i+1,L)), b=i),
                     shift(mul(vL,interval(0,i-1)), c=L-i, scale=Di)))
        b.append(add(shift(mul(u0,interval(i+1,L)), c=i, scale=Ei),
                     shift(mul(uL,interval(0,i-1)), b=L-i)))
        left = shift(mul(u0,interval(1,i-1)), c=L-i, scale=Di) if i else {}
        right = shift(mul(uL,interval(i+1,L-1)), b=i) if i<L else {}
        t.append(shift(mul(v0,vL,add(left,right)), scale=2))
        left = shift(mul(v0,interval(1,i-1)), b=L-i) if i else {}
        right = shift(mul(vL,interval(i+1,L-1)), c=i, scale=Ei) if i<L else {}
        tp.append(shift(mul(u0,uL,add(left,right)), scale=2))
    return ([mul({e:1},interval(0,L)) for e in [X,Y,Z]]
            + [mul({e:1},v) for v in a for e in [X,Y,Z]]
            + [mul({e:1},v) for v in b for e in [X,Y,Z]] + t + tp)


def boundary(alpha, delta):
    m = len(alpha)
    actual = columns(alpha, delta)
    unit = columns(alpha, [value or 1 for value in delta])
    product = 1
    for value in delta:
        product = product*(value or 1) % P
    inv = pow(product, -1, P)
    allowed = set(range(6)) | set(range(m-5,m))
    labels = ([0,1,-1]
              + [c for i in range(m) for c in [i,i+1,i-1]]
              + [c for i in range(m) for c in [-i,-i+1,-i-1]]
              + list(range(m)) + [-i for i in range(m)])
    selected = [j for j,c in enumerate(labels) if c % m in allowed]
    rows = [(a,b,m+1-a-b) for a in range(m+1,-1,-1)
            for b in range(m+1-a,-1,-1)
            if (2*b+a-m-1) % m in allowed]
    jets = [[[0]*len(selected) for _ in rows] for _ in range(4)]
    for i, (a,b,c) in enumerate(rows):
        negative = -m-1 <= b-c <= -m+5
        source, factor = (unit,inv) if negative else (actual,1)
        for j, column in enumerate(selected):
            for k in range(4):
                jets[k][i][j] = source[column].get((a,b,c,k),0)*factor % P
    return rows, selected, jets


def toeplitz(jets, order):
    rows, cols = len(jets[0]), len(jets[0][0])
    return [[jets[i-j][r][c] if 0<=i-j<=order else 0
             for j in range(order+1) for c in range(cols)]
            for i in range(order+1) for r in range(rows)]


def check(insertions=2):
    alpha, delta = ALPHA[:], DELTA[:]
    rows, cols, jets = boundary(alpha,delta)
    assert len(rows)==124 and len(cols)==91
    records = []
    for k, (rank_expected, det_expected) in enumerate([(84,99),(172,74),(262,45)]):
        matrix = toeplitz(jets,k)
        rank, selected, determinant = packed_eliminate(matrix, ordered_pivots=True)
        assert (rank,determinant)==(rank_expected,det_expected), (k,rank,determinant)
        records.append(dict(order=k, rows=len(matrix), columns=len(matrix[0]),
                            rank=rank, ordered_pivot_determinant=determinant))
    comparisons = []
    for _ in range(insertions):
        alpha = alpha[:9]+[1]+alpha[9:]
        delta = delta[:8]+[0,0]+delta[9:]
        newrows, newcols, newjets = boundary(alpha,delta)
        lookup = {row:i for i,row in enumerate(newrows)}
        for k in range(4):
            expected = [[0]*91 for _ in newrows]
            for i,(a,b,c) in enumerate(rows):
                w = b-c
                if abs(w)<=5:
                    target = (a+1,b,c)
                elif w>5:
                    target = (a,b+1,c)
                else:
                    target = (a,b,c+1)
                expected[lookup[target]] = jets[k][i]
            assert expected==newjets[k], (len(alpha),k)
        comparisons.append(dict(new_size=len(alpha), jet_orders=[0,1,2,3],
                                all_entries_match=True, new_rows=len(newrows), columns=91))
        rows,cols,jets = newrows,newcols,newjets
    return dict(prime=P, base_size=17, toeplitz=records, insertions=comparisons,
                final_jets_sha256=hashlib.sha256(bytes(v for jet in jets for row in jet for v in row)).hexdigest(),
                scope='finite certificate and stated number of insertions; uniform proof is separate')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--insertions', type=int, default=2)
    parser.add_argument('--output')
    args = parser.parse_args()
    result = check(args.insertions)
    print(json.dumps(result,indent=2))
    if args.output:
        with open(args.output,'w') as stream:
            json.dump(result,stream,indent=2)
            stream.write('\n')


if __name__=='__main__':
    main()
