#!/usr/bin/env python3
"""Independent reconstruction of the necessary root Koszul certificates.

Does not import coordinate_koszul.py. Verifies full orbit coverage and one
sufficient pivot minor whenever the ordinary support bound is insufficient.
"""
from itertools import combinations, permutations
from pathlib import Path
import argparse
import json
import math


PAIRS = list(combinations(range(4), 2))
RECTS = [(I, J) for I in PAIRS for J in PAIRS]


def det_mod(a, p):
    a = [[v % p for v in row] for row in a]
    n = len(a)
    ans = 1
    for c in range(n):
        rr = next((r for r in range(c, n) if a[r][c]), None)
        if rr is None:
            return 0
        if rr != c:
            a[c], a[rr] = a[rr], a[c]
            ans = -ans
        pivot = a[c][c]
        ans = ans * pivot % p
        inv = pow(pivot, -1, p)
        for r in range(c + 1, n):
            scale = a[r][c] * inv % p
            if scale:
                a[r] = [(v - scale*w) % p for v, w in zip(a[r], a[c])]
    return ans % p


def rebuild_minor(rec, cert, sign):
    sub = rec['subset']
    support = rec['support']
    m = len(support)
    all_support = sorted({4*r+c for q in sub for r in RECTS[q][0] for c in RECTS[q][1]})
    assert support == all_support
    ix = {v: i for i,v in enumerate(support)}
    entries = []
    for q in sub:
        (r,s),(c,d) = RECTS[q]
        a,b,x,y = [ix[z] for z in (4*r+c,4*r+d,4*s+c,4*s+d)]
        entries.append({(a,y):1,(y,a):1,(b,x):sign,(x,b):sign})
    p = cert['p']
    src = list(combinations(range(len(sub)),p))
    dst = list(combinations(range(len(sub)),p+1))
    def entry(row, col):
        J,u = dst[row//m], row%m
        I,v = src[col//m], col%m
        diff = set(J)-set(I)
        if len(diff)!=1 or not set(I)<=set(J):
            return 0
        a = next(iter(diff))
        # a must move past every element of I less than a.
        sign_wedge = -1 if sum(x<a for x in I)%2 else 1
        return sign_wedge*entries[a].get((u,v),0)
    return [[entry(r,c) for c in cert['cols']] for r in cert['rows']]


def group_actions():
    index = {r:i for i,r in enumerate(RECTS)}
    result = []
    for rho in permutations(range(4)):
        for kappa in permutations(range(4)):
            for swap in (False,True):
                action=[]
                for I,J in RECTS:
                    K=tuple(sorted(rho[x] for x in I))
                    L=tuple(sorted(kappa[x] for x in J))
                    action.append(index[(L,K) if swap else (K,L)])
                result.append(action)
    assert len(set(map(tuple,result)))==1152
    return result


def audit(j, exact=False, strengthen_per5=False):
    root=Path(__file__).resolve().parents[1]/'root'
    data=json.loads((root/f'j{j}.json').read_text())
    actions=group_actions()
    seen=set()
    for rec in data['records']:
        sub=rec['subset']
        assert len(sub)==j and len(set(sub))==j and all(0<=x<36 for x in sub)
        orbit={sum(1<<a[i] for i in sub) for a in actions}
        assert len(orbit)==rec['orbit_size']
        assert not (orbit&seen), 'Repeated orbit'
        seen.update(orbit)
    assert len(seen)==math.comb(36,j)==data['orbit_sum']==data['number_of_subsets']
    outcomes=[]
    for family,sgn in [('det',-1),('per',1)]:
        target=data['minimum_certified'][family]
        if strengthen_per5 and j==5 and family=='per':
            target=11
        for rec in data['records']:
            if strengthen_per5 and j==5 and family=='per' and rec['subset']==[0,1,3,6,7]:
                outcomes.append({'family':family,'subset':rec['subset'],'bound':11,
                                 'external_certificate':'per5_prolongation_certificate.json'})
                continue
            if max(j,len(rec['support']))>=target:
                continue
            choices=[c for c in rec['families'][family]['koszul'] if c['bound']>=target]
            assert choices
            cert=min(choices,key=lambda x:x['rank_mod_p'])
            assert cert['pure_cost']==math.comb(j-1,cert['p'])
            assert cert['bound']==(cert['rank_mod_p']+cert['pure_cost']-1)//cert['pure_cost']
            matrix=rebuild_minor(rec,cert,sgn)
            assert len(matrix)==len(matrix[0])==cert['rank_mod_p']
            determinant=det_mod(matrix,cert['prime'])
            assert determinant==cert['pivot_product_mod_p']!=0
            out={'family':family,'subset':rec['subset'],'p':cert['p'],
                 'minor_order':len(matrix),'determinant_mod_p':determinant,
                 'prime':cert['prime'],'bound':cert['bound']}
            if exact:
                from sympy import Matrix
                from sympy.polys.matrices import DomainMatrix
                integer_det=int(DomainMatrix.from_Matrix(Matrix(matrix)).det())
                assert integer_det%cert['prime']==determinant
                out['determinant_Z']=integer_det
            outcomes.append(out)
    return {'j':j,'orbit_coverage':'PASS','covered':len(seen),
            'minimum_certified':data['minimum_certified'],
            'required_minors_verified':len(outcomes),'minors':outcomes}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--j',type=int,nargs='+',default=[3,4,5,6])
    parser.add_argument('--exact',action='store_true')
    parser.add_argument('--strengthen-per5',action='store_true')
    args=parser.parse_args()
    result=[]
    for j in args.j:
        item=audit(j,args.exact,args.strengthen_per5)
        result.append(item)
        print(json.dumps({k:v for k,v in item.items() if k!='minors'}),flush=True)
    out=Path(__file__).with_name('root_certificate_audit_strengthened.json' if args.strengthen_per5 else 'root_certificate_audit.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',out)


if __name__=='__main__':
    main()
