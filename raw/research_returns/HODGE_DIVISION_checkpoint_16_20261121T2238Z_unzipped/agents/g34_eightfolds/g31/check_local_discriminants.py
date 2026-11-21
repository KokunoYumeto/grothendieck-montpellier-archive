#!/usr/bin/env python3
"""Exact local Hermitian determinants for every conjugacy class of G29/G31.
The class enumeration is independently performed by the companion C++ file.
No unrefereed class labels, determinants, spectra or conclusions are imported.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import lcm
from functools import lru_cache
import json
import gaussian_exact as M

HERE=Path(__file__).resolve().parent

def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p

def divide(p,q):
    p=p[:];out=[Q(0)]*max(1,len(p)-len(q)+1)
    while len(p)>=len(q) and any(p):
        j=len(p)-len(q);a=p[-1]/q[-1];out[j]=a
        for k,b in enumerate(q):p[j+k]-=a*b
        trim(p)
    return trim(out),trim(p)

@lru_cache(None)
def cyclotomic(n):
    p=[Q(-1)]+[Q(0)]*(n-1)+[Q(1)]
    for d in range(1,n):
        if n%d==0:
            p,r=divide(p,list(cyclotomic(d)));assert not any(r)
    return tuple(p)

def spectrum(g,order):
    N=lcm(order,4);phi=list(cyclotomic(N))
    powers=[];p=M.eye(4)
    for j in range(order):
        powers.append(sum((p[i][i] for i in range(4)),M.Z))
        p=M.mul(p,g)
    assert p==M.eye(4)
    counts=[]
    for k in range(order):
        polynomial=[Q(0)]*N
        for j,tr in enumerate(powers):
            e=(-k*j*(N//order))%N
            polynomial[e]+=tr.a/order
            polynomial[(e+N//4)%N]+=tr.b/order
        unused,rem=divide(trim(polynomial),phi)
        assert len(rem)==1 and rem[0].denominator==1 and rem[0]>=0
        counts.append(int(rem[0]))
    assert sum(counts)==4
    return counts

def inert_parities(q):
    assert q>0
    bad=[]
    for value,sign in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=value:
            n=0
            while value%p==0:value//=p;n+=1
            if p%4==3 and n%2:bad.append(p)
            p+=1
        if value>1 and value%4==3:bad.append(value)
    return sorted(p for p in set(bad) if bad.count(p)%2)

def check(group):
    raw=json.loads((HERE/f'G{group}_classes.json').read_text())
    classes=[];covered=0
    for item in raw['classes']:
        encoded=item['representative']
        g=[[M.F(Q(encoded[2*(4*j+k)],2),Q(encoded[2*(4*j+k)+1],2)) for k in range(4)] for j in range(4)]
        assert M.mul(M.star(g),g)==M.eye(4)
        determinant=M.det(g);assert determinant in [M.ONE,-M.ONE]
        a=M.sub(M.eye(4),g);cols=M.rref(a)[1];d=len(cols)
        if not d:
            gramdet=b=M.ONE
        else:
            U=M.tr([M.tr(a)[j] for j in cols])
            rows=M.rref(M.tr(U))[1]
            left=M.inv([U[j] for j in rows])
            action=M.mul(left,[M.mul(g,U)[j] for j in rows])
            assert M.mul(U,action)==M.mul(g,U)
            gramdet=M.det(M.mul(M.star(U),U))
            b=M.det(M.sub(M.eye(d),action))
        assert not gramdet.b and gramdet.a>0 and b
        assert not b.a or not b.b
        positive_q=gramdet.a/(abs(b.a) if b.a else abs(b.b))
        bad=inert_parities(positive_q)
        eigen=spectrum(g,item['order'])
        assert 4-eigen[0]==d
        age=sum((Q(k*n,item['order']) for k,n in enumerate(eigen)),Q(0))
        row=dict(item)
        row.update({'moving_rank':d,'matrix_determinant':determinant.pair(),
                    'moving_gram_determinant':gramdet.pair(),
                    'det_one_minus_moving':b.pair(),
                    'positive_local_q':str(positive_q),
                    'inert_prime_odd_valuations':bad,'is_gaussian_norm':not bad,
                    'eigenvalue_multiplicities':eigen,'age':str(age),
                    'age_imbalance':str(age-Q(d,2))})
        classes.append(row);covered+=item['size']
    assert covered==raw['group_order']
    nonnorm=[c for c in classes if not c['is_gaussian_norm']]
    invol=[c for c in classes if c['order']==2]
    refs=[c for c in classes if c['moving_rank']==1]
    assert all(c['order']==2 and c['is_gaussian_norm'] for c in refs)
    assert all(c['is_gaussian_norm'] for c in classes if c['moving_rank']<=3)
    assert all(c['is_gaussian_norm'] for c in invol)
    if group==29:assert not nonnorm
    else:assert len(nonnorm)==3 and all(c['moving_rank']==4 for c in nonnorm)
    out={'group':f'G{group}','group_order':raw['group_order'],'class_count':len(classes),
         'reflection_count':sum(c['size'] for c in refs),
         'nonidentity_involution_count':sum(c['size'] for c in invol),
         'classes':classes,'nonnorm_class_indices':[c['index'] for c in nonnorm],
         'all_moving_rank_at_most_three_are_norms':True,
         'all_involutions_are_norms':True,
         'all_checks_exact':True}
    (HERE/f'G{group}_local_discriminants.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'G{group}: {len(classes)} classes, {out["reflection_count"]} reflections; nonnorm classes '+str([(c['index'],c['size'],c['order'],c['positive_local_q'],c['age_imbalance']) for c in nonnorm]))
    return out

if __name__=='__main__':
    check(29);check(31)
