#!/usr/bin/env python3
"""Stdlib-only independent integer-minor and exhaustive support verifier.

The sole external mathematical input is R-04 for the exceptional per5 tensor.
Its separate unit-minor certificates are verified by their standalone checker.
"""
from itertools import combinations, permutations
from pathlib import Path
import json
import math

PAIRS=list(combinations(range(4),2))
RECTS=[(I,J) for I in PAIRS for J in PAIRS]
SUPPORT_MASKS=[sum(1<<(4*i+j) for i in I for j in J) for I,J in RECTS]


def integer_det(a):
    a=[list(map(int,row)) for row in a]
    n=len(a)
    sign=1
    previous=1
    if n==0:return 1
    for k in range(n-1):
        if a[k][k]==0:
            rr=next((r for r in range(k+1,n) if a[r][k]),None)
            if rr is None:return 0
            a[k],a[rr]=a[rr],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
        for i in range(k+1,n):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]


def actions():
    ix={x:i for i,x in enumerate(RECTS)}
    result=[]
    for rho in permutations(range(4)):
        for gamma in permutations(range(4)):
            for transpose in (False,True):
                action=[]
                for I,J in RECTS:
                    K=tuple(sorted(rho[i] for i in I))
                    L=tuple(sorted(gamma[j] for j in J))
                    action.append(ix[(L,K) if transpose else (K,L)])
                result.append(action)
    assert len({tuple(x) for x in result})==1152
    return result


def minor(rec,cert,sign):
    S=rec['subset'];support=rec['support'];m=len(support)
    ix={v:i for i,v in enumerate(support)}
    expected=sorted({4*i+j for q in S for i in RECTS[q][0] for j in RECTS[q][1]})
    assert support==expected
    slices=[]
    for q in S:
        (r,s),(c,d)=RECTS[q]
        a,b,x,y=[ix[z] for z in [4*r+c,4*r+d,4*s+c,4*s+d]]
        slices.append({(a,y):1,(y,a):1,(b,x):sign,(x,b):sign})
    p=cert['p']
    src=list(combinations(range(len(S)),p))
    dst=list(combinations(range(len(S)),p+1))
    def entry(row,col):
        J,u=dst[row//m],row%m
        I,v=src[col//m],col%m
        if not set(I)<=set(J):return 0
        difference=set(J)-set(I)
        if len(difference)!=1:return 0
        a=next(iter(difference))
        return (-1)**sum(x<a for x in I)*slices[a].get((u,v),0)
    return [[entry(r,c) for c in cert['cols']] for r in cert['rows']]


def main():
    data=json.loads(Path(__file__).with_name('global_j345_certificate.json').read_text())
    group=actions()
    summary=[]
    for finding in data:
        j=finding['j'];target=finding['uniform_residual_lower_bound']
        covered=set()
        for rec in finding['records']:
            orbit={sum(1<<g[i] for i in rec['subset']) for g in group}
            assert len(orbit)==rec['orbit_size']
            assert not (covered&orbit)
            covered.update(orbit)
            for family,sign in [('det',-1),('per',1)]:
                c=rec['families'][family]
                if 'p' not in c:
                    assert j==5 and family=='per' and rec['subset']==[0,1,3,6,7]
                    assert c['certificate'].startswith('R-04:')
                    continue
                assert c['pure_cost']==math.comb(j-1,c['p'])
                assert len(c['rows'])==len(c['cols'])==c['minor_order']
                value=integer_det(minor(rec,c,sign))
                assert value==c['determinant_Z']!=0
                assert (c['minor_order']+c['pure_cost']-1)//c['pure_cost']>=target
                # Permanent certificates are units; determinant certificates
                # are units times powers of 2. Characteristic 2 uses per=det.
                absolute=abs(value)
                if family=='per':assert absolute==1
                else:assert absolute&(absolute-1)==0
        low=0;total=0
        for S in combinations(range(36),j):
            total+=1
            mask=0
            for q in S:mask|=SUPPORT_MASKS[q]
            if mask.bit_count()<target:
                low+=1
                assert sum(1<<q for q in S) in covered
        assert total==math.comb(36,j)==finding['all_subsets']
        assert low==len(covered)
        summary.append({'j':j,'target':target,'all_subsets':total,
                        'all_low_support_subsets':low,
                        'exact_minor_and_exhaustive_support_check':'PASS'})
        print(json.dumps(summary[-1]),flush=True)
    out=Path(__file__).with_name('global_bounds_verification.json')
    out.write_text(json.dumps({'results':summary,
                              'external_input':'R-04 exceptional per5 unit-minor prolongation certificate'},indent=2)+'\n')
    print('PASS; R-04 is independently verified by its standalone checker.')


if __name__=='__main__':main()
