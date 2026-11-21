#!/usr/bin/env python3
"""Exact rightmost-kernel identities and all108 raw last-coordinate maps."""
from pathlib import Path
import json,numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return tuple(a)
def inv(w):return tuple(-x for x in w[::-1])
def subst(w,images):
    out=()
    for x in w:out=red(out+(images[x-1]if x>0 else inv(images[-x-1])))
    return out
def braid(word,n):
    ident=[(j+1,)for j in range(n)];out=ident.copy()
    for j in word:
        s=ident.copy()
        if j>0:s[j-1]=(j,j+1,-j);s[j]=(j,)
        else:
            k=-j;s[k-1]=(k+1,);s[k]=(-k-1,k,k+1)
        out=[subst(w,out)for w in s]
    return out
def same(a,b,n):return braid(a,n)==braid(b,n)
def comm(a,b):return a+b+inv(a)+inv(b)
def z(n):return tuple(range(1,n))*n

def run():
    identities=[]
    for n in [2,3,4,5]:
        us=[]
        for i in range(1,n+1):
            v=tuple(range(n,i,-1));us.append(v+(i,i)+inv(v))
        D=sum(us,());u=us[-1]
        y=tuple(range(n-1,1,-1))+(1,1)+tuple(range(2,n))
        c=inv(z(n-1))+z(n+1)
        assert same(z(n)+D,z(n+1),n+1)
        assert same(y,c+inv(D),n+1)
        assert same(comm(c,D),(),n+1)and same(comm(c,u),(),n+1)
        identities.append({'n':n,'boundary_relation':True,'y_equals_c_D_inverse':True,
                           'c_commutes_both_inputs':True})
    raw=np.load(ROOT/'records/hurwitz_product_fixed_cover.npz')
    vals=np.load(PENT/'hurwitz_raw_survivor_covariance.npz')
    last=raw['tuples'][:,-1];points=np.unique(last);lookup={int(a):i for i,a in enumerate(points)}
    assert len(points)==36
    deck=raw['deck'];deckpowers=[np.arange(8064)]
    for j in range(1,6):deckpowers.append(deck[deckpowers[-1]])
    maps=[];labels=[]
    for key in vals.files:
        if not key.startswith('V_'):continue
        i,j=map(int,key.split('_')[1:]);v=vals[key]
        for phase,t in enumerate(deckpowers):
            vp=t[v];vi=np.argsort(vp);target=[]
            for b in points:
                image=np.unique(last[vi[last==b]]);assert len(image)==1
                target.append(lookup[int(image[0])])
            assert len(set(target))==36
            maps.append(target);labels.append([i,j,phase])
    assert len(labels)==108
    out={'statement':'D23.F40','braid_identities':identities,'raw_candidates':18,
         'deck_phases_each':6,'last_entry_values':36,'all108_partition_tests':True,
         'result':'PASS','scope':'Exact algebraic braid checks and partition necessity only; a common f-value table is additional.'}
    (HERE/'hurwitz_last_coordinate.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'hurwitz_last_coordinate.npz',labels=labels,
                        kappa_last_maps=maps,last_entries=points)
    print(json.dumps(out,indent=2))
if __name__=='__main__':run()
