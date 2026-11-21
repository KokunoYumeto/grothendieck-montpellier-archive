#!/usr/bin/env python3
"""Exact C4 action on the abelianization of each solvable mixed derived block."""
import json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
source=json.loads((HERE.parent/'characters/records/krammer_mixed_correlation.json').read_text())
def to3(a):
    out=np.zeros((2*len(a),2*len(a)),dtype=np.int16)
    for j,row in enumerate(a):
        for k,v in enumerate(row):
            u,b=int(v)%3,int(v)//3
            out[2*j:2*j+2,2*k:2*k+2]=[[u,-b%3],[b,u]]
    return out
def mm(a,b):return a@b%3
def mp(a,n):
    out=np.eye(len(a),dtype=np.int16)
    while n:
        if n&1:out=mm(out,a)
        a=mm(a,a);n//=2
    return out
def inv(a):
    d=len(a);ar=np.concatenate([a.copy(),np.eye(d,dtype=np.int16)],axis=1)
    for j in range(d):
        p=next(k for k in range(j,d) if ar[k,j])
        ar[[j,p]]=ar[[p,j]];ar[j]=ar[j]*int(ar[j,j])%3
        for k in range(d):
            if k!=j and ar[k,j]:ar[k]=(ar[k]-ar[k,j]*ar[j])%3
    return ar[:,d:]
def conj(a,b):return mm(mm(a,b),inv(a))
def comm(a,b):return mm(conj(a,b),inv(b))
def key(a):return a.astype(np.int8).tobytes()
def f9(a):return [[int(a[2*j,2*k])+3*int(a[2*j+1,2*k]) for k in range(len(a)//2)] for j in range(len(a)//2)]
def group(gs):
    unit=np.eye(len(gs[0]),dtype=np.int16);els=[unit];seen={key(unit)}
    for a in els:
        for g in gs:
            b=mm(a,g);k=key(b)
            if k not in seen:seen.add(k);els.append(b)
    return els
records=[]
for pair in source['pairs']:
    x,y=map(to3,pair['solvable_generators'])
    H=group([x,y]);assert len(H)==108
    A=comm(x,y);B=conj(y,A);Z=comm(A,B)
    HD=group([A,B]);assert len(HD)==27
    assert all(np.array_equal(mp(g,3),np.eye(6,dtype=np.int16)) for g in HD)
    assert not np.array_equal(Z,np.eye(6,dtype=np.int16))
    assert all(np.array_equal(mm(g,Z),mm(Z,g)) for g in HD)
    coords={}
    for a in range(3):
        for b in range(3):
            for c in range(3):
                g=mm(mm(mp(A,a),mp(B,b)),mp(Z,c));coords[key(g)]=(a,b,c)
    assert len(coords)==27 and set(coords)=={key(g) for g in HD}
    actions=[]
    for g in [x,y]:
        ca,cb=coords[key(conj(g,A))],coords[key(conj(g,B))]
        actions.append([[ca[0],cb[0]],[ca[1],cb[1]]])
    J=np.array(actions[1],dtype=np.int16)
    assert np.array_equal(J@J%3,2*np.eye(2,dtype=np.int16))
    assert (int(np.trace(J))%3,(int(J[0,0]*J[1,1]-J[0,1]*J[1,0]))%3)==(0,1)
    assert np.array_equal(np.array(actions[0]),J if pair['pair']==[4,5] else 2*np.eye(2,dtype=np.int16))
    records.append({'pair':pair['pair'],'H_order':len(H),'Hprime_order':len(HD),'Hsecond_order':3,'derived_generators_F9':[f9(A),f9(B)],'central_commutator_F9':f9(Z),'conjugation_actions_x_y_F3':actions,'characteristic_polynomial_of_order4_action':'T^2+1, irreducible over F3','result':'PASS'})
out={'statement':'D23.F17','pairs':records,'result':'PASS'}
(HERE/'krammer_solvable_action.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
