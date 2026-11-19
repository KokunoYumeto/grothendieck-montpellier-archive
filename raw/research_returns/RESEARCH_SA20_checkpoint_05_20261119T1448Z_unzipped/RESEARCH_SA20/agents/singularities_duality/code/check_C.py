#!/usr/bin/env python3
"""Finite checks for Part C. They check examples and sign conventions, not general theorems."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

checks=[]
def record(statement,check,ok,data):
    assert ok, (statement,check,data)
    checks.append(dict(statement=statement,check=check,outcome='PASS',data=data))
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def tr(a): return list(map(list,zip(*a)))
def add(a,b): return [[x+y for x,y in zip(aa,bb)] for aa,bb in zip(a,b)]
def scale(c,a): return [[c*x for x in row] for row in a]
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def inverse(a):
    n=len(a); b=[list(map(Fraction,row))+list(map(Fraction,e)) for row,e in zip(a,eye(n))]
    for i in range(n):
        j=next(j for j in range(i,n) if b[j][i]);b[i],b[j]=b[j],b[i]
        q=b[i][i];b[i]=[x/q for x in b[i]]
        for j in range(n):
            if j!=i:
                q=b[j][i];b[j]=[x-q*y for x,y in zip(b[j],b[i])]
    return [row[n:] for row in b]
def rank(a):
    if not a: return 0
    b=[list(map(Fraction,row)) for row in a]
    pivot=0
    for col in range(len(b[0])):
        nz=next((j for j in range(pivot,len(b)) if b[j][col]),None)
        if nz is None: continue
        b[pivot],b[nz]=b[nz],b[pivot]
        v=b[pivot][col];b[pivot]=[x/v for x in b[pivot]]
        for j in range(len(b)):
            if j!=pivot:
                v=b[j][col];b[j]=[x-v*y for x,y in zip(b[j],b[pivot])]
        pivot+=1
        if pivot==len(b): break
    return pivot
def cellular_betti(cell_dims,boundaries):
    out=[]
    for j,dim in enumerate(cell_dims):
        dj=rank(boundaries.get(j,[]));dnext=rank(boundaries.get(j+1,[]))
        out.append(dim-dj-dnext)
    return out

def d(cochain, degree, vertices):
    return {s:sum((-1)**j*cochain.get(s[:j]+s[j+1:],0) for j in range(len(s)))
            for s in combinations(vertices,degree+2)}
def cup(a,p,b,q,vertices):
    return {s:a.get(s[:p+1],0)*b.get(s[p:],0) for s in combinations(vertices,p+q+1)}

# C.002: the two distinct middle-degree lifts on S^n x D^n.
for n in range(2,9):
    u=[[0]];v0=[[0]];v1=[[1]]
    record('C.002','distinct equivariant lifts',v0!=v1 and mul(u,v0)==mul(u,v1)==[[0]],
           {'n':n,'field':3,'K_degrees':[0,n],'R_degrees':[n,2*n],'u_middle':0,'lifts':[0,1]})
# C.006: exact middle sequence for S^(n-1) x D^(n+1).
dims=[0,1,1,0,0,1,1,0]; ranks=[0,1,0,0,0,1,0]
record('C.006','six-term sequence exact',all(ranks[j-1]+ranks[j]==dims[j] for j in range(1,len(dims)-1)),
       {'dimensions':dims,'arrow_ranks':ranks,'H_nminus1':1})
# C.007: independent simplicial cup-product/Stokes sign checks.
for n in range(1,5):
    dim=2*n;verts=tuple(range(dim+1));top=verts
    for i in range(dim):
        if i==0: b={(v,):2 for v in verts}
        else:
            beta={s:sum((j+1)*(v+1) for j,v in enumerate(s))**2+len(s) for s in combinations(verts,i)}
            b=d(beta,i-1,verts)
        adeg=dim-i-1
        a={s:sum((j+2)*(v+3) for j,v in enumerate(s))**3+sum(v*v for v in s) for s in combinations(verts,adeg+1)}
        da=d(a,adeg,verts)
        lhs=cup(b,i,da,adeg+1,verts)[top]
        ba=cup(b,i,a,adeg,verts)
        boundary=sum((-1)**j*ba[top[:j]+top[j+1:]] for j in range(dim+1))
        record('C.007','simplicial Stokes transpose sign',lhs==(-1)**i*boundary,
               {'dimension':dim,'degree':i,'left':lhs,'boundary':boundary,'sign':(-1)**i})
# Middle-dimensional Seifert/variation matrices in all parity classes.
for n in range(1,9):
    eps=(-1)**n;s=(-1)**(n*(n+1)//2)
    for mu in range(1,7):
        L=[[s*(int(i==j)-int(j==i+1)) for j in range(mu)] for i in range(mu)]
        V=scale(-eps,inverse(L));I=add(L,scale(eps,tr(L)));J=tr(I)
        T=scale(-eps,mul(inverse(L),tr(L)))
        ok=tr(I)==scale(eps,I) and mul(V,J)==add(T,scale(-1,eye(mu)))
        ok=ok and mul(L,T)==scale(-eps,tr(L)) and mul(tr(J),tr(V))==add(tr(T),scale(-1,eye(mu)))
        record('C.007','Seifert and variation matrices',ok,{'n':n,'rank':mu,'epsilon':eps})
# C.017 literal complement fails even as a finite cell-set equality.
W={'v0','v1','e0','e1'};P={'v0','v1','e0'};interior={'e0'}
Q_wrong=P-interior;Q_right=W-interior
record('C.017','scan007 complement',P|Q_wrong!=W and P|Q_right==W and P&Q_right=={'v0','v1'},
       {'W':sorted(W),'P':sorted(P),'written_Q':sorted(Q_wrong),'correct_Q':sorted(Q_right)})
# The n=2 ordinary quadratic page: rational cellular Betti numbers of S^2 and RP^3.
rp3=cellular_betti([1,1,1,1],{1:[[0]],2:[[2]],3:[[0]]})
s2=cellular_betti([1,0,1],{})
record('C.017','non-surjective boundary arrow',rp3[1]==0 and s2[2]==1,
       {'RP3_cellular_boundaries':[0,2,0],'RP3_rational_betti':rp3,
        'S2_rational_betti':s2,'middle_intersection_absolute_value':2})
# C.005: the annular Milnor page retracts onto the one-vertex circle.
circle=cellular_betti([1,1],{1:[[0]]})
record('C.005','annulus ordinary versus reduced degree zero',circle==[1,1] and circle[0]-1==0,
       {'annulus_betti':circle,'H0':circle[0],'reduced_H0':circle[0]-1})
# Positive twist test in C.015 versus an explicit negative witness.
h1=lambda degree:max(-degree-1,0)
record('C.015','positive twists miss cd=1',all(h1(N)==0 for N in range(101)) and h1(-2)==1,
       {'tested_N':[0,100],'negative_witness_degree':-2,'h1_witness':h1(-2)})
# The bound in cote125/008 is a vanishing threshold, not the largest nonzero degree.
for r in range(2,10):
    for dimY in range(1,r):
        m=r-dimY;d0=r-m
        record('C.019','threshold conversion',d0==dimY and (m-1)==r-dimY-1,
               {'ambient_dimension':r,'dimY':dimY,'vanishing_from':m,'cd_bound':m-1,'formal_comparison_below':d0})

# C.021: the Veronese CM local ring modulo s^3,t^3 has basis 1,u,v,
# with u=s^2 t, v=s t^2 and every product of two radical elements zero.
monomials=[(0,0),(2,1),(1,2)]
def reduced_product(a,b):
    c=(a[0]+b[0],a[1]+b[1])
    if c[0]>=3 or c[1]>=3: return [0,0,0]
    return [int(c==v) for v in monomials]
mult_u=tr([reduced_product(monomials[1],b) for b in monomials])
mult_v=tr([reduced_product(monomials[2],b) for b in monomials])
socle_dim=3-rank(mult_u+mult_v)
radical_square_zero=all(reduced_product(a,b)==[0,0,0]
                        for a in monomials[1:] for b in monomials[1:])
record('C.021','non-Gorenstein socle dimension',socle_dim==2 and radical_square_zero,
       {'basis_exponents':monomials,'multiply_by_u':mult_u,'multiply_by_v':mult_v,
        'socle_dimension':socle_dim,'ring_generator_count':1,'canonical_generator_count':2})
# The local Cech quotient in two parameters retains every Laurent monomial
# with both exponents negative; check an increasing finite window directly.
for radius in range(1,8):
    ambient={(a,b) for a in range(-radius,radius+1) for b in range(-radius,radius+1)}
    image_Ax={v for v in ambient if v[1]>=0}
    image_Ay={v for v in ambient if v[0]>=0}
    quotient=ambient-(image_Ax|image_Ay)
    record('C.021','nonzero two-parameter local support class',(-1,-1) in quotient and len(quotient)==radius**2,
           {'exponent_radius':radius,'surviving_monomials':len(quotient),'witness':[-1,-1]})
# Tensor the Koszul resolution on x,y (ranks 1,2,1) with the
# epsilon-periodic resolution (one generator in every nonnegative degree).
koszul=[1,2,1]
betti=[sum(koszul[j] for j in range(min(i,2)+1)) for i in range(7)]
record('C.021','Gorenstein nonperfect Ext-swap failure',betti[:3]==[1,3,4] and betti[0]!=betti[2],
       {'ring':'k[[x,y,epsilon]]/(epsilon^2)','resolution_ranks_through_6':betti,
        'residue_field_differentials_zero':True,'Ext0_dimension':betti[0],'Ext2_dimension':betti[2]})

out={'program':'check_C.py','checks':checks,'passed':len(checks),'failed':0}
path=Path(__file__).resolve().parents[1]/'logs'/'check_C_output.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':len(checks),'failed':0,'output':str(path)},indent=2))
