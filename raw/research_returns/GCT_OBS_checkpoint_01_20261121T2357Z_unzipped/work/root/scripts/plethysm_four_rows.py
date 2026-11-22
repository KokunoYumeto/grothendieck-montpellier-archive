#!/usr/bin/env python3
"""Exact four-row plethysm coefficient by bounded weight counting (stdlib)."""
from itertools import permutations
import argparse
import json
import time


def weight_table(n, d, caps):
    bmax, cmax, emax = caps
    ne = emax+1
    nc = (cmax+1)*ne
    nb = (bmax+1)*nc
    a = [0]*((d+1)*nb)
    # The zero-tail monomial fills any remaining coefficient degree.
    for k in range(d+1):
        a[k*nb] = 1
    for b in range(min(n, bmax)+1):
        for c in range(min(n-b, cmax)+1):
            for e in range(min(n-b-c, emax)+1):
                if not b+c+e:
                    continue
                offset = nb+b*nc+c*ne+e
                for k in range(1, d+1):
                    for i in range(b, bmax+1):
                        for j in range(c, cmax+1):
                            base = k*nb+i*nc+j*ne
                            for h in range(e, emax+1):
                                index = base+h
                                a[index] += a[index-offset]
    return a, (ne,nc,nb)


def multiplicity(n, d, lam, table=None):
    assert len(lam) == 4 and sum(lam) == n*d
    if table is None:
        caps = tuple(lam[j]+3-j for j in range(1, 4))
        table = weight_table(n,d,caps)
    a,(ne,nc,nb)=table
    terms = []
    for sig in permutations(range(4)):
        alpha = tuple(lam[j]+sig[j]-j for j in range(4))
        parity = (-1)**sum(sig[i] > sig[j] for i in range(4) for j in range(i+1,4))
        if min(alpha) < 0:
            value = 0
        else:
            value = a[d*nb+alpha[1]*nc+alpha[2]*ne+alpha[3]]
        terms.append(dict(permutation=sig, weight=alpha, sign=parity, count=value))
    return dict(n=n, d=d, partition=lam,
                multiplicity=sum(t['sign']*t['count'] for t in terms),
                weyl_terms=terms)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('n', type=int)
    p.add_argument('d', type=int)
    p.add_argument('partition', type=int, nargs=4)
    p.add_argument('--output')
    args = p.parse_args()
    start = time.monotonic()
    result = multiplicity(args.n, args.d, args.partition)
    result['elapsed_seconds'] = round(time.monotonic()-start,3)
    if args.output:
        with open(args.output,'w') as f:
            json.dump(result,f,indent=2)
            f.write('\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
