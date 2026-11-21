"""T050: exact positive Newton certificates for k=2,3,4 endpoints."""
from pathlib import Path
from math import comb
from itertools import product
import hashlib
import json
import numpy as np
import sympy as sp
from two_row_ray_certificate import (LABELS,CLASSES,WEIGHTS,h,schur_terms,
                                    pair_line_correction)

HERE=Path(__file__).resolve().parent
# A variable B means b=B+shift; otherwise b is fixed.
BRANCHES=(
    dict(name='k2_bge2',k=2,b_variable=True,b=2,x=0),
    dict(name='k2_b1',k=2,b_variable=False,b=1,x=2),
    dict(name='k2_b0',k=2,b_variable=False,b=0,x=4),
    dict(name='k3_bge2',k=3,b_variable=True,b=2,x=0),
    dict(name='k3_b1',k=3,b_variable=False,b=1,x=1),
    dict(name='k3_b0',k=3,b_variable=False,b=0,x=3),
    dict(name='k4_bge1',k=4,b_variable=True,b=1,x=0),
    dict(name='k4_b0',k=4,b_variable=False,b=0,x=2),
)


def trace(g,x,b,k):
    c=2*k-2;A,B,C=schur_terms(g,x,b)
    jet=CLASSES[g].count(1)*h(g,k-1)
    return (A*(h(g,c)-jet)-B*(h(g,c-1)-jet)+C*(h(g,c-2)-jet)
            +pair_line_correction(g,x,b))


def multiplicity(label,x,b,k):
    total=sum(w*trace(g,x,b,k) for g,w in enumerate(WEIGHTS[LABELS.index(tuple(label))]))
    assert total%120==0
    return total//120


def degree_certificate(branch):
    X,B=sp.symbols('X B');x=X+branch['x'];b=B+branch['b'] if branch['b_variable'] else sp.Integer(branch['b'])
    k=branch['k'];c=2*k-2
    identity=sp.Poly(sp.expand((x+1)*(b+x+2)*(b+1)*
        ((c+1)*(b+c+2)*(b+x+c+3)-5*k*(k+1)*(k+2))+120*(x+1)),X,B)
    assert all(v>0 for e,v in identity.terms()),(branch,identity)
    assert identity.degree(X)<=3 and identity.degree(B)<=4 and identity.total_degree()<=5
    phases=[]
    for g,modulus,bound in ((1,2,3),(2,2,3),(3,3,1)):
        for px,pb in product(range(modulus),repeat=2):
            subst={X:px,B:pb}
            def HP(n):
                n=sp.sympify(n);r=int(n.subs(subst))%modulus
                if g==1:return (n*n+4*n+4-r)/4
                if g==2:return sp.Integer(0) if r else (n+2)/2
                return (n+3-r)/3
            a=b+x
            AA=HP(a)*HP(b)-HP(a+1)*HP(b-1)
            BB=HP(a-1)*HP(b)-HP(a+1)*HP(b-2)
            CC=HP(a-1)*HP(b-1)-HP(a)*HP(b-2)
            jet=CLASSES[g].count(1)*h(g,k-1)
            if g==1:cor=3*(-1)**int(b.subs(subst))*int(int(x.subs(subst))%2==0)-(x+1)
            elif g==2:cor=-2*(-1)**int(b.subs(subst))*int(int(x.subs(subst))%2==0)
            else:cor=sp.Integer((1,-1,0)[int(x.subs(subst))%3])
            pp=sp.Poly(sp.expand(AA*(h(g,c)-jet)-BB*(h(g,c-1)-jet)+CC*(h(g,c-2)-jet)+cor),X,B)
            assert pp.total_degree()<=bound,(branch,g,px,pb,pp)
            phases.append({'class_index':g,'phase':[px,pb],'total_degree':int(pp.total_degree())})
    return {'identity_terms':[[list(e),int(v)] for e,v in identity.terms()],
            'phase_bounds':phases}


def main():
    result={'statement':'T-050','branches':{},'verified_entries':0}
    negatives=[]
    for branch in BRANCHES:
        variable=branch['b_variable'];bwidth=300 if variable else 1
        arrays=[np.array([[trace(g,X+branch['x'],B+branch['b'],branch['k'])
                          for B in range(bwidth)] for X in range(240)],dtype=np.int64)
                for g in range(7)]
        bound=max(sum(abs(w)*int(np.abs(v).max()) for w,v in zip(row,arrays)) for row in WEIGHTS)*2**7
        assert bound<2**63
        rec={'parameters':branch,'degree_certificate':degree_certificate(branch),
             'signed64_bound':bound,'labels':{}}
        for label,weights in zip(LABELS,WEIGHTS):
            key=','.join(map(str,label));values=sum(w*v for w,v in zip(weights,arrays))
            assert np.all(values%120==0);values//=120
            assert values.min()>=0,(branch,label,int(values.min()))
            lo={};hi={};zeros=[];hasher=hashlib.sha256();active=[]
            for i in range(4):
                for j in range(5 if variable else 1):
                    value=np.zeros((60,60 if variable else 1),dtype=np.int64)
                    for u in range(i+1):
                        for v in range(j+1):
                            value+=(-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*values[
                                60*u:60*(u+1),60*v:60*(v+1) if variable else 1]
                    slot=f'{i},{j}';lo[slot]=int(value.min());hi[slot]=int(value.max())
                    if hi[slot]:active.append([i,j])
                    if lo[slot]<0:negatives.append({'branch':branch['name'],'label':key,'order':[i,j],'minimum':lo[slot]})
                    if i==j==0:zeros=[list(map(int,p)) for p in np.argwhere(value==0)]
                    hasher.update(value.astype('<i8',copy=False).tobytes(order='C'))
                    result['verified_entries']+=value.size
            rec['labels'][key]={'minima':lo,'maxima':hi,'active_orders':active,'zero_residues':zeros,'sha256':hasher.hexdigest()}
        result['branches'][branch['name']]=rec
        print('completed',branch['name'],'entries',result['verified_entries'],flush=True)
    result['negative_blocks']=negatives
    (HERE/'TWO_BELOW_ENDPOINTS_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
    text=f"{'PASS' if not negatives else 'FAIL'}: {result['verified_entries']} fixed exact constants; {len(negatives)} negative blocks.\n"
    text+=json.dumps(negatives,indent=2)+'\n'
    (HERE/'TWO_BELOW_ENDPOINTS_CHECK.txt').write_text(text);print(text)
    assert not negatives


if __name__=='__main__':main()
