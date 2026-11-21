"""G-019 positive plethysm evaluator with its fixed companion JSON table."""
from pathlib import Path
from math import comb
from itertools import combinations
import argparse
import json

DATA = json.loads(Path(__file__).with_name('FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json').read_text())
TABLE = DATA['labels']
LABELS = tuple(tuple(map(int, text.split(','))) for text in TABLE)


def transpose(mu):
    return tuple(sum(x >= j for x in mu) for j in range(1, mu[0]+1))


def parameters(a, k, d, outer=(5,)):
    if any(not isinstance(x, int) or x < 0 for x in (a, k, d)):
        raise ValueError('a, k, and d must be nonnegative integers')
    outer = tuple(outer)
    if outer not in LABELS:
        raise ValueError('outer must be a partition of five')
    effective = transpose(outer) if (d+a) % 2 else outer
    lam = (d+2*a+3*k,d+a+2*k,d+a,d+a,d)
    return effective, d+a+k, tuple(x for x in lam if x)


def coefficient(a, k, d, outer=(5,)):
    effective, _, _ = parameters(a,k,d,outer)
    values = TABLE[','.join(map(str,effective))][a%60][k%60]
    p, q = a//60, k//60
    return sum(c * comb(p,i) * comb(q,j)
               for i in range(4) for j in range(4)
               if (c := values[4*i+j]))


def polytopes(a, k, d, outer=(5,)):
    """Export the at most16 contributing residue tags as exact constraints."""
    effective, _, _ = parameters(a,k,d,outer)
    values = TABLE[','.join(map(str,effective))][a%60][k%60]
    result=[]
    for i in range(4):
        for j in range(4):
            c=values[4*i+j]
            if c:
                result.append({'tag':[a%60,k%60,i,j],
                               'p':a//60,'q':k//60,'multiplicity_interval':[0,c-1],
                               'x_ordered_subset_size':i,'x_interval':[1,a//60],
                               'z_ordered_subset_size':j,'z_interval':[1,k//60],
                               'integer_variable_count':3+i+j})
    return result


def witnesses(a, k, d, outer=(5,)):
    for poly in polytopes(a,k,d,outer):
        i,j=poly['tag'][2:]
        if i>poly['p'] or j>poly['q']:
            continue
        for xs in combinations(range(1,poly['p']+1),i):
            for zs in combinations(range(1,poly['q']+1),j):
                for y in range(poly['multiplicity_interval'][1]+1):
                    yield {'tag':poly['tag'],'p':poly['p'],'q':poly['q'],
                           'y':y,'x':xs,'z':zs}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('a','k','d'):
        parser.add_argument('--'+name,type=int,required=True)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    parser.add_argument('--witnesses',action='store_true')
    args=parser.parse_args()
    outer=tuple(map(int,args.outer.split(',')))
    effective,n,lam=parameters(args.a,args.k,args.d,outer)
    result={'statement':'G-019','outer':outer,'inner':n,'lambda':lam,
            'effective_label':effective,
            'coefficient':coefficient(args.a,args.k,args.d,outer)}
    if args.polytopes:result['polytopes']=polytopes(args.a,args.k,args.d,outer)
    if args.witnesses:result['witnesses']=list(witnesses(args.a,args.k,args.d,outer))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
