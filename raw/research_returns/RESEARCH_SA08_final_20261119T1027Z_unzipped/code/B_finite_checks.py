"""Finite certificates for the B corrections; all arithmetic is exact."""
from math import comb, factorial, gcd
from fractions import Fraction
from itertools import combinations
from time import perf_counter
import json
from pathlib import Path
start=perf_counter()
results=[]
def record(name,data):
    results.append({'name':name,**data})
# Exact finite-support PD algebra operations (one T, one X, exterior dX).
def pdmul(a,b,p):
    out={}
    for (t,x,e),c in a.items():
        for (u,y,f),d in b.items():
            if e and f:continue
            key=(t+u,x+y,e+f)
            out[key]=(out.get(key,0)+c*d*comb(t+u,t)*comb(x+y,x))%p
    return {k:v for k,v in out.items() if v}
def pdsub(a,b,p):
    out=dict(a)
    for k,v in b.items():out[k]=(out.get(k,0)-v)%p
    return {k:v for k,v in out.items() if v}
# Missing M in F2: X * (X^(2)+dX) versus 3 X^(3).
xi1={(0,1,0):1};xi2={(0,2,0):1,(0,0,1):1};xi3={(0,3,0):1}
assert pdsub(pdmul(xi1,xi2,2),xi3,2)=={(0,1,1):1}
assert comb(3,1)%2==1
record('missing_M_F2',{'i':1,'j':2,'lhs_B':0,'rhs_B':'X','nonzero_witness':'X dX','hypotheses_1_to_3':'phi0=id, A=X; condition3 automatic in F2'})
# Reduced coefficient base F3, A=0, B3=T^(5).
assert comb(3,1)%3==0 and comb(3,2)%3==0
assert comb(10,5)%3==0
assert pdmul({(5,0,0):1},{(5,0,0):1},3)=={}
record('F3_margin_counterexample',{'coefficient_ring':'F3','B3':'T^(5)','binom(3,1)':comb(3,1),'binom(10,5)':comb(10,5),'all_M_checks':'only i+j=3 can be nonzero; both binomials vanish mod3','condition3':'(T^(5))^2=252 T^(10)=0'})
# PD substitution f=T+T^(2); matrix f^(m), weight <= 12.
N=12
mat=[[0]*(N+1) for _ in range(N+1)]
for m in range(N+1):
    # (T+T^2/2)^m/m!, coefficient of T^(m+j).
    for j in range(m+1):
        n=m+j
        if n<=N:
            v=Fraction(factorial(n)*comb(m,j),factorial(m)*2**j)
            assert v.denominator==1
            mat[n][m]=int(v)
assert all(mat[i][i]==1 for i in range(N+1))
inv=[[0]*(N+1) for _ in range(N+1)]
for col in range(N+1):
    for row in range(N+1):
        inv[row][col]=(1 if row==col else 0)-sum(mat[row][h]*inv[h][col] for h in range(row))
for r in range(N+1):
    for c in range(N+1):
        assert sum(mat[r][h]*inv[h][c] for h in range(N+1))==(r==c)
record('determinant_one_nonlinear_coefficient_action',{'cutoff':N,'matrix_diagonal':[mat[i][i] for i in range(N+1)],'phi_T':[mat[i][1] for i in range(N+1)],'inverse_T_coefficients':[inv[i][1] for i in range(N+1)],'exact_matrix_identity_checks':(N+1)**2})
# Arithmetic underpinning Ann(T)^2=0, independently of a finite test.
lim=512
for i in range(1,lim+1):
    for j in range(1,lim+1):
        assert comb(i+j,i)%gcd(i+1,j+1)==0
record('annihilator_binomial_divisibility',{'range_i_j':[1,lim],'pairs':lim*lim,'failures':0})
# Six-vertex triangulation of RP2: check manifold and nonzero square.
facets=[(0,1,2),(0,1,3),(0,2,4),(0,3,5),(0,4,5),(1,2,5),(1,3,4),(1,4,5),(2,3,4),(2,3,5)]
edges=list(combinations(range(6),2)); eidx={e:i for i,e in enumerate(edges)}
counts={e:sum(set(e)<=set(f) for f in facets) for e in edges}
assert set(counts.values())=={2}
for v in range(6):
    link_edges=[tuple(x for x in f if x!=v) for f in facets if v in f]
    deg={w:sum(w in e for e in link_edges) for w in range(6) if w!=v}
    assert set(deg.values())=={2}
    seen={next(iter(deg))}
    while True:
        new=seen|{w for e in link_edges if any(t in seen for t in e) for w in e}
        if new==seen:break
        seen=new
    assert len(seen)==5
coboundaries=set()
for a in range(64):
    b=sum((((a>>i)^(a>>j))&1)<<r for r,(i,j) in enumerate(edges))
    coboundaries.add(b)
cocycles=[]
for b in range(1<<len(edges)):
    if all(sum((b>>eidx[e])&1 for e in combinations(f,2))%2==0 for f in facets):
        cocycles.append(b)
a=next(b for b in cocycles if b not in coboundaries)
square=[((a>>eidx[(i,j)])&1)*((a>>eidx[(j,k)])&1) for i,j,k in facets]
assert sum(square)%2==1
record('RP2_square_detects_failed_sphere_test',{'facets':facets,'f_vector':[6,15,10],'cocycle_count':len(cocycles),'coboundary_count':len(coboundaries),'H1_dimension':1,'H2_dimension':1,'edge_order':edges,'cocycle_bits':[(a>>r)&1 for r in range(15)],'square_on_faces':square,'square_on_mod2_fundamental_cycle':sum(square)%2})
# Monoid splitting obstruction A=X(T-X) with coefficient map T->0.
A={(1,1):Fraction(1),(0,2):Fraction(-1)}
alpha={t:c for (t,x),c in A.items() if x==0}
beta={}
for (t,x),c in A.items():beta[t+x]=beta.get(t+x,0)+c
beta={n:c for n,c in beta.items() if c}
assert alpha=={} and beta=={} and A[(1,1)]==1
record('monoid_semidirect_counterexample',{'ring':'Q','A':'XT-X^2','A_at_X_0':'0','A_at_X_T':'0','coefficient_map':'T->0','unique_G_parameter_over_map':'lambda=0','any_H_composition_with_G0_on_X':'0','A_nonzero_coefficients':{'XT':1,'X^2':-1}})
# Trivial-filtration counterexample: S=F2,t=0, X=Delta2/boundary.
# A relative weight2 one-form has coefficients a U dU+b V dU+c U dV+d V dV.
relative=[]
for bits in range(16):
    a,b,c,d=[(bits>>r)&1 for r in range(4)]
    if a==0 and d==0 and (a+b+c+d)%2==0:
        relative.append({'abcd':[a,b,c,d],'derivative_UV':(b+c)%2})
assert len(relative)==2 and all(r['derivative_UV']==0 for r in relative)
record('t_zero_S2_nonzero_DR2',{'ring':'F2','scalar_PD_ideal':0,'t':0,'X':'Delta[2]/boundary','one_form_candidates':16,'relative_one_forms':relative,'two_form':'dU dV','two_form_closed':True,'two_form_not_boundary':True})
seconds=perf_counter()-start
out={'program':Path(__file__).name,'checks':results,'seconds':seconds}
print(json.dumps(out,indent=2))
(Path(__file__).resolve().parents[1]/'logs'/'B_finite_checks.json').write_text(json.dumps(out,indent=2))
