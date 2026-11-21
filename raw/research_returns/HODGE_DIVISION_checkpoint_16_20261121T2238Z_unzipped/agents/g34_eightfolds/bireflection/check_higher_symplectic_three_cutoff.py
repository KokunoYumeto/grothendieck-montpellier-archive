#!/usr/bin/env python3
"""Exact supplements for HOS13--15. Universal representation proof is in TeX."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import hashlib,json,time
import numpy as np
import sympy as s

start=time.perf_counter()
base=Path(__file__).resolve().parent
proof=base/'higher_odd_symplectic_three_cutoff_section.tex'
out={'status':'PASS','proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}

# Every symmetric form in dimensions2,3,4, not merely diagonal normal forms.
forms=0;bydim=[]
for n in (2,3,4):
    coords=[(i,j) for i in range(n) for j in range(i,n)]
    vec=np.array(list(product(range(3),repeat=n)),dtype=np.int16)
    coeff=np.array(list(product(range(3),repeat=len(coords))),dtype=np.int16)[1:]
    values=np.array([vec[:,i]*vec[:,j]*(1 if i==j else 2) for i,j in coords],dtype=np.int16)
    checked=0
    for k in range(0,len(coeff),512):
        q=(coeff[k:k+512]@values)%3
        counts=np.stack([(q==j).sum(axis=1) for j in range(3)],axis=1)
        assert np.all(9*(counts[:,0]-1)<=5*(3**n-1))
        assert np.all(counts[:,1:]<=2*3**(n-1))
        assert F(2*3**(n-1),3**n-1)<=F(7,9)
        checked+=len(q)
    bydim.append({'dimension':n,'nonzero_symmetric_forms':checked,'vectors_each':3**n})
    forms+=checked
out['all_symmetric_weight_checks']=bydim
out['symmetric_forms_total']=forms

# Exact word turning a symmetric upper short-root shear into a Levi elementary.
c=s.symbols('c')
n=3;I=s.eye(6);J=s.zeros(6)
for i in range(n):J[i,n+i]=1;J[n+i,i]=-1
def transvection(v,t):
    return I+t*v*(v.T*J)
e=[I[:,i] for i in range(n)]
f=[I[:,n+i] for i in range(n)]
w=transvection(e[1],1)*transvection(f[1],1)*transvection(e[1],1)
C=s.zeros(n);C[0,1]=C[1,0]=c
U=I.copy()
U[:n,n:]=C
L=s.simplify(w*U*w.inv())
assert all(L[i,j]==0 for i in range(n) for j in range(n,2*n))
assert all(L[i,j]==0 for j in range(n) for i in range(n,2*n))
assert s.simplify(L[n:,n:]-L[:n,:n].inv().T)==s.zeros(n)
assert L[:n,:n]!=s.eye(n) and s.simplify(L.T*J*L-J)==s.zeros(6)
assert w*w==s.diag(1,-1,1,1,-1,1)
out['siegel_generation_word']=str(L[:n,:n])

# All quadratic shear carriers in dimension9, with every Weyl displacement.
# Monomial columns are omega^phase[u] delta_(u+x); this is an exact
# Heisenberg displacement times a quadratic shear. Phase twists are retained.
vec=list(product(range(3),repeat=2));idx={v:i for i,v in enumerate(vec)}
def mm(A,B):
    p,e=A;q,f=B
    return [p[q[i]] for i in range(9)],[(f[i]+e[q[i]])%3 for i in range(9)]
ident=(list(range(9)),[0]*9)
def abs_trace_square(A):
    p,e=A;cnt=Counter(e[i] for i in range(9) if p[i]==i)
    z=[cnt[j] for j in range(3)]
    return sum(t*t for t in z)-sum(z[i]*z[j] for i in range(3) for j in range(i+1,3))
def spectra(A):
    p,e=A;unseen=set(range(9));counts=[0]*9
    while unseen:
        root=min(unseen);orb=[root];v=p[root]
        while v!=root:orb.append(v);v=p[v]
        unseen.difference_update(orb)
        assert len(orb) in (1,3)
        phase=sum(e[i] for i in orb)%3
        if len(orb)==1:counts[3*phase]+=1
        else:
            for j in range(3):counts[(phase+3*j)%9]+=1
    assert sum(counts)==9
    return counts
carrier_count=0;rank2_count=0;minimum_rank2_support=9
for aa,bb,dd in product(range(3),repeat=3):
    det=(aa*dd-bb*bb)%3
    rank=2 if det else int(any((aa,bb,dd)))
    for x in vec:
        for y in vec:
            p=[idx[((u[0]+x[0])%3,(u[1]+x[1])%3)] for u in vec]
            phase=[(2*(aa*u[0]**2+2*bb*u[0]*u[1]+dd*u[1]**2)+y[0]*u[0]+y[1]*u[1])%3 for u in vec]
            A=(p,phase);A2=mm(A,A);A3=mm(A,A2)
            assert A3[0]==ident[0] and len(set(A3[1]))==1
            for T in (A,A2):assert abs_trace_square(T)<=3**(4-rank)
            counts=spectra(A)
            if rank==2:
                assert 9-max(counts)>=4
                rank2_count+=1
                minimum_rank2_support=min(minimum_rank2_support,9-max(counts))
            carrier_count+=1
out['phase_twisted_carriers']={'operators':carrier_count,'rank2_operators':rank2_count,
 'minimum_rank2_support':minimum_rank2_support,'trace_power_checks':2*carrier_count}

# Exact universal arithmetic, without constructing enormous group degrees.
sigma=F(1,10**29);N0=10**30
actual=F(1,6507*2**21*10**18)
assert actual>7*sigma
assert F(N0-1,2*10**29)>1
assert F(1,2)*F(2,3)*F(2,3)==F(2,9)
assert F(1,4)*(1-F(1,9))==F(2,9)
assert F(1,2)*F(4,5)*F(2,3)==F(4,15)>F(2,9)
assert 6/(12*F(2,9)-2)==9
out['constants']={'sigma':str(sigma),'natural_rank_cutoff':str(N0),
 'unipotent_support':'2/9','odd_semisimple_plane_support':'4/15','source_degree_ceiling':9}
out['seconds']=time.perf_counter()-start
out['scope']='Exact weight distributions, matrix word, displaced quadratic carrier spectra and constants. Universal group generation, representation decomposition, automorphism scope and actual Hurwitz factorization remain fully written mathematical arguments.'
base.joinpath('check_higher_symplectic_three_cutoff.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

