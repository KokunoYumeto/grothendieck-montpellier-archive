#!/usr/bin/env python3
"""Exact characteristic-two test on E x E, E: y^2+xy=x^3+1.

L=O_E(3O) box O_E(3O), d=2.  W=H0(L^2) has dimension36.
The canonical differential is dx/x, and C(f dx/x)=T(f)dx/x.
All polynomial arithmetic and linear algebra is exact over F2.
Four affine charts cover E x E; singularity ideals are checked
by Groebner bases, with invariant vector fields as tangent bases.
"""
import itertools, json, random, time
from pathlib import Path
import sympy as sp

started=time.perf_counter()
basis=[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)]
index={a:i for i,a in enumerate(basis)}
tensor=list(itertools.product(range(6),repeat=2))
tindex={a:i for i,a in enumerate(tensor)}

def add_term(a,key):
    if key in a: a.remove(key)
    else: a.add(key)

def mul(a,b):
    out=set()
    for i,j in a:
        for k,l in b:
            if j+l<2: add_term(out,(i+k,j+l))
            else:
                for term in [(i+k+3,0),(i+k+1,1),(i+k,0)]:
                    add_term(out,term)
    return out

def cartier(a):
    out=set()
    for i,j in a:
        if j==0:
            if i%2==0: add_term(out,(i//2,0))
        elif i%2==0: add_term(out,(i//2+1,0))
        else:
            add_term(out,((i-1)//2,1)); add_term(out,((i-1)//2,0))
    return out

def deriv(a):
    out=set()
    for i,j in a:
        if j==0:
            if i%2: add_term(out,(i,0))
        else:
            add_term(out,(i+2,0))
            if i%2==0: add_term(out,(i,1))
    return out

def rank(cols):
    piv={}
    for z in cols:
        while z:
            b=z.bit_length()-1
            if b in piv: z^=piv[b]
            else: piv[b]=z; break
    return len(piv)

def apply(cols,v):
    z=0
    while v:
        a=(v&-v).bit_length()-1; z^=cols[a]; v&=v-1
    return z

ec={(a,b):[index[z] for z in cartier(mul({basis[a]},{basis[b]}))]
        for a in range(6) for b in range(6)}
dc=[[index[z] for z in deriv({basis[a]})] for a in range(6)]
D=[]
for side in (0,1):
    cols=[]
    for a,b in tensor:
        z=0
        for j in dc[(a,b)[side]]:
            ab=(j,b) if side==0 else (a,j)
            z^=1<<tindex[ab]
        cols.append(z)
    D.append(cols)
assert all(apply(D[h],D[h][j])==D[h][j] for h in (0,1) for j in range(36))
assert all(apply(D[0],D[1][j])==apply(D[1],D[0][j]) for j in range(36))

def components(s):
    out=[]
    for a,b in itertools.product((0,1),repeat=2):
        v=apply(D[0],s) if a else s^apply(D[0],s)
        v=apply(D[1],v) if b else v^apply(D[1],v)
        out.append(v)
    assert out[0]^out[1]^out[2]^out[3]==s
    return out

def Cmatrix(s):
    cols=[]
    active=[tensor[i] for i in range(36) if (s>>i)&1]
    for a,b in tensor:
        z=0
        for u,v in active:
            for i in ec[u,a]:
                for j in ec[v,b]: z^=1<<tindex[i,j]
        cols.append(z)
    return cols

u,v,w,z=sp.symbols('u v w z')
coords=(u,v,w,z)

def chart_data(a,b,which):
    if which=='Z':
        eq=b*b+a*b+a**3+1
        db=(a,a*a+b)
        sections=[1,a,a*a,b*b+a*b+1,b,a*b]
    else:
        eq=b+a*b+a**3+b**3
        db=(1+a+b*b,a*a+b)
        sections=[b*b,a*b,a*a,1+a+b*b,b,a]
    return eq,db,sections

def smooth_check(s):
    checks=[]
    active=[tensor[i] for i in range(36) if (s>>i)&1]
    for c1,c2 in itertools.product(('Z','Y'),repeat=2):
        e1,d1,b1=chart_data(u,v,c1)
        e2,d2,b2=chart_data(w,z,c2)
        sec=sp.expand(sum(b1[a]*b2[b] for a,b in active))
        t1=sp.diff(sec,u)*d1[0]+sp.diff(sec,v)*d1[1]
        t2=sp.diff(sec,w)*d2[0]+sp.diff(sec,z)*d2[1]
        gb=sp.groebner([e1,e2,sec,t1,t2],*coords,modulus=2,order='grevlex')
        unit=len(gb.polys)==1 and gb.polys[0].as_expr()==1
        checks.append({'charts':[c1,c2],'unit_ideal':unit})
        if not unit: return False,checks
    return True,checks

rng=random.Random(20261119)
attempts=[]
chosen=None
for attempt in range(1,501):
    s=rng.getrandbits(36)
    cs=components(s)
    C=Cmatrix(s)
    assert all(apply(C,x)==x for x in cs)
    r=rank(C)
    attempts.append({'attempt':attempt,'section_bits':s,'Cartier_rank':r,
                     'character_component_rank':rank(cs)})
    if r!=36 or rank(cs)!=4: continue
    smooth,charts=smooth_check(s)
    attempts[-1]['smooth']=smooth
    if smooth:
        chosen=(s,cs,C,charts,attempt); break
assert chosen is not None
s,cs,C,charts,attempt=chosen
points=[(0,1,1),(1,0,1),(1,1,1),(0,1,0)]
def vals(P):
    X,Y,Z=P
    return [Z*Z,X*Z,X*X,Y*Y+X*Y+Z*Z,Y*Z,X*Y]
count=0
for P,Q in itertools.product(points,repeat=2):
    bp,bq=vals(P),vals(Q)
    value=sum(bp[a]*bq[b] for j,(a,b) in enumerate(tensor) if (s>>j)&1)%2
    count+=value==0
trace=sum((C[i]>>i)&1 for i in range(36))%2
assert count%2==trace
result={
 'field':'F2','elliptic_curve':'Y^2 Z + X Y Z + X^3 + Z^3 = 0',
 'ambient':'E x E, Segre embedding of the two plane cubics',
 'L':'O_E(3O) box O_E(3O)','degree_d':2,
 'basis_E':['1','x','x^2','x^3','y','xy'],
 'homogeneous_basis_E':['Z^2','XZ','X^2','Y^2+XY+Z^2','YZ','XY'],
 'section_terms':[[a,b] for j,(a,b) in enumerate(tensor) if (s>>j)&1],
 'section_bits':s,'random_seed':20261119,'chosen_attempt':attempt,
 'W_dimension':36,'C_matrix_columns_binary':C,'C_rank':rank(C),
 'relative_E_dimension':35,'relative_E_stable_rank':35,
 'curve_genus':37,'curve_p_rank':37,
 'fixed_character_vectors_binary':cs,'fixed_character_rank_W':rank(cs),
 'fixed_covector_rank_relative':rank(cs)-1,
 'sum_character_vectors_equals_section':True,
 'smoothness_chart_certificates':charts,
 'point_count_F2':count,'Cartier_trace_W_mod2':trace,
 'attempts':attempts,'runtime_seconds':time.perf_counter()-started,
}
dest=Path(__file__).resolve().parents[1]/'outputs'/'ordinary_abelian_surface.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('C_matrix_columns_binary','attempts')},indent=2))
