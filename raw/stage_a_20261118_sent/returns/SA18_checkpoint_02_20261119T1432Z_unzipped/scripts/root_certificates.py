"""Exact arithmetic certificates for the root's SA18 checks.

The accompanying mathematical proofs explain why the computations model the
manuscript objects. Finite tests are not represented as proofs for all ranks.
No symbolic package or floating-point arithmetic is needed.
"""
from itertools import permutations,combinations,product
from collections import defaultdict
from math import gcd,comb
from functools import reduce
from fractions import Fraction
import json
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'outputs/root_certificates.json'
results={}

# Square-free polynomial rings CH*((P1)^k), with integral coefficients.
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return {m:c for m,c in out.items() if c}
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
    out=defaultdict(int)
    for m,c in p.items():
        for n,d in q.items():
            if not m&n:out[m|n]+=c*d
    return {m:c for m,c in out.items() if c}
def y(i):return {1<<i:1}
def delta(i,j):return add(y(i),y(j))
def fmt(p):return {str(m):c for m,c in sorted(p.items())}
d12=delta(0,1);d23=delta(1,2);d13=delta(0,2)
small=mul(d12,d23)
assert mul(d12,d12)==scale(mul(y(0),y(1)),2)
assert small==add(mul(y(0),y(1)),mul(y(0),y(2)),mul(y(1),y(2)))
assert mul(small,small)=={}
assert mul(d12,small)==scale(mul(mul(y(0),y(1)),y(2)),2)
assert add(d12,scale(y(0),-1),scale(y(1),-1))=={}
cycle4=mul(mul(delta(0,1),delta(1,2)),mul(delta(2,3),delta(3,0)))
assert cycle4=={15:2}
results['P1_diagonals']={'delta12_square':fmt(mul(d12,d12)),
 'small_diagonal':fmt(small),'delta12_times_small':fmt(mul(d12,small)),
 'four_cycle':fmt(cycle4),'base_claim_counterexample':'delta12=y1+y2; the three listed middle generators are dependent.'}

# Integer stabilizers of subtori in SL4. Cocharacters/characters are explicit.
r=(3,1,-1,-3);a=(1,2,-7,4)
assert sum(r)==0 and sum(x*z for x,z in zip(a,r))==0
assert reduce(gcd,(abs(x-a[-1]) for x in a[:-1]))==1
WR=[];WT=[]
for p in permutations(range(4)):
    rp=tuple(r[i] for i in p);ap=tuple(a[i] for i in p)
    if rp==r or rp==tuple(-x for x in r):WR.append(p)
    for sgn in (1,-1):
        dif=tuple(x-sgn*z for x,z in zip(ap,a))
        if len(set(dif))==1:
            WT.append(p);break
assert len(WR)==2 and len(WT)==1
# Restricted weights on T are distinct: e_i-e_j is not a rational multiple
# of a modulo the all-ones vector. Determinants check rank of [1,a,root].
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
root_checks=[]
for i,j in combinations(range(4),2):
    rt=tuple(int(t==i)-int(t==j) for t in range(4))
    minors=[det3([[1,a[t],rt[t]] for t in inds]) for inds in combinations(range(4),3)]
    assert any(minors)
    root_checks.append({'root':[i+1,j+1],'minors':minors})
results['nested_tori']={'cocharacter_R':r,'character_T':a,
 'W_R_permutations_1_based':[[i+1 for i in p] for p in WR],
 'W_T_permutations_1_based':[[i+1 for i in p] for p in WT],
 'restricted_weights_distinct_certificates':root_checks,
 'conclusion':'W(R)=C2 and W(T)=1; C2 is not a subquotient of the trivial group.'}

# Quadric intersection rings: primitive integral bases, n>=1.
def basis(n):
    m=n//2
    if n%2:return [(i,'h') if i<=m else (i,'l') for i in range(n+1)]
    return [(i,'h') for i in range(m)]+[(m,'a'),(m,'b')]+[(i,'l') for i in range(m+1,n+1)]
def bmul(n,x,z):
    i,s=x;j,t=z;k=i+j
    if k>n:return {}
    if i==0:return {z:1}
    if j==0:return {x:1}
    m=n//2
    if n%2:
        if s==t=='h':return {(k,'h' if k<=m else 'l'):1 if k<=m else 2}
        return {(k,'l'):1}
    if s==t=='h':
        if k<m:return {(k,'h'):1}
        if k==m:return {(m,'a'):1,(m,'b'):1}
        return {(k,'l'):2}
    if s in ('a','b') and t in ('a','b'):
        return {(n,'l'):1} if (s==t)==(m%2==0) else {}
    return {(k,'l'):1}
def qmul(n,p,q):
    out=defaultdict(int)
    for x,c in p.items():
        for z,d in q.items():
            for u,v in bmul(n,x,z).items():out[u]+=c*d*v
    return {k:v for k,v in out.items() if v}
quad=[]
for n in range(1,13):
    b=basis(n);assoc_count=0
    for x,z,w in product(b,repeat=3):
        assert qmul(n,bmul(n,x,z),{w:1})==qmul(n,{x:1},bmul(n,z,w))
        assoc_count+=1
    h={(1,'h'):1} if n>=3 else ({(1,'a'):1,(1,'b'):1} if n==2 else {(1,'l'):2})
    hmaps=[]
    for i in range(n):
        src=[x for x in b if x[0]==i];dst=[x for x in b if x[0]==i+1]
        matrix=[[qmul(n,h,{x:1}).get(z,0) for x in src] for z in dst]
        hmaps.append({'codim':i,'matrix':matrix})
    row={'dimension':n,'basis':b,'hyperplane_maps':hmaps,'associativity_basis_tests':assoc_count}
    if n%2==0:
        m=n//2;lam={(m,'a'):1,(m,'b'):-1}
        square=qmul(n,lam,lam)
        assert square=={(n,'l'):2*(-1)**m}
        row['primitive_square_degree']=2*(-1)**m
        row['punctured_cone_integral_cohomology']={'0':'Z',str(n):'Z',str(n+1):'Z',str(2*n+1):'Z'}
    else:
        row['punctured_cone_integral_cohomology']={'0':'Z',str(n+1):'Z/2',str(2*n+1):'Z'}
    quad.append(row)
results['quadrics']=quad
results['quadric_middle_lattice']={'matrix':[[1,1],[1,-1]],'determinant':-2,'Smith_diagonal':[1,2]}
results['quadric_Q0']={'geometry':'two reduced points','punctured_cone':'two disjoint G_m','H0':'Z²','H1':'Z²'}

# Group law by exact multivariate polynomial multiplication.
def pmul(p,q):
    out=defaultdict(int)
    for a,c in p.items():
        for b,d in q.items():out[tuple(x+y for x,y in zip(a,b))]+=c*d
    return {k:v for k,v in out.items() if v}
def pvar(i,n=4):return {tuple(int(i==j) for j in range(n)):1}
x,yv,z,t=[pvar(i) for i in range(4)]
def law(p,q):return add(p,q,pmul(t,pmul(p,q)))
lhs=law(law(x,yv),z);rhs=law(x,law(yv,z))
assert lhs==rhs
results['Gm_Ga_group_law']={'associativity_polynomial':{str(k):v for k,v in sorted(lhs.items())},
 'identity':0,'inverse':'−x/(1+t*x)','multiplicative_coordinate':'u=1+t*x','generic_t':'3 in Z_(3), invertible in Q','special_t':'0, additive law'}

# Total SW class of (L_a-1)(L_b-1): degree<=2 formal F2 calculation.
def tr2(p):return {m:c%2 for m,c in p.items() if sum(m)<=2 and c%2}
def f2mul(p,q):return tr2(pmul(p,q))
one={(0,0):1};u={(1,0):1};v={(0,1):1}
inv_u=add(one,u,{(2,0):1});inv_v=add(one,v,{(0,2):1})
sw=f2mul(f2mul(add(one,u,v),inv_u),inv_v)
assert sw=={(0,0):1,(1,1):1}
results['SW_rankzero_product']={'through_degree_2':{str(k):v for k,v in sw.items()},'degree2':'u cup v'}
real=[]
for neg in range(65):
    bits=[comb(neg,2**j)%2 if 2**j<=neg else 0 for j in range(7)]
    assert sum(v*2**j for j,v in enumerate(bits))==neg
    real.append({'negative_index':neg,'SW_power_two_coefficients':bits})
results['real_signature_binary_check']=real

# RP2 cellular local-coefficient complexes, over characteristic zero.
# cochains C0->C1->C2, differential (g-1),(1+g).
rp=[]
for g in (1,-1):
    d0=g-1;d1=1+g
    h0=int(d0==0);h1=int(d1==0)-int(d0!=0)
    assert h1==0
    rp.append({'monodromy':g,'d0':d0,'d1':d1,'dim_H0':h0,'dim_H1':h1})
results['RP2_LemmaA_counterexample']=rp

# Literal torus basis change: v4-v1=ik e2. Column operation determinant1.
results['literal_torus']={'basis_change':'v4 -> v4-v1','unimodular_determinant':1,
 'product':'C/(Z+iZ) × C/(Z+ikZ)',
 'failed_proof_witness':'x=e2 has first complex coordinate0, invalidating inference c in Q(i).'}
results['alternative_torus']={'basis':['(1,0)','(i,0)','(0,1)','(k,i)'],
 'real_determinant':1,'hypothesis':'k real irrational',
 'contradiction_equation':'k*(d*cprime-dprime*c)=uprime*z-u*zprime in Q(i), with nonzero integer coefficient',
 'conclusion':'no complementary elliptic subtorus; hence not projective by Poincare complete reducibility'}

# Clifford rank4 raw-difference reading, real quaternion Brauer classes.
def quaternion_R(a,b):return int(a<0 and b<0)
def clifford4(q):
    a,b,c,d=q
    return (quaternion_R(a,b)+quaternion_R(-a*b*c,-a*b*d))%2
def sw2_real(q):return comb(sum(x<0 for x in q),2)%2
q=(-1,1,1,1);p=(1,1,1,1)
assert clifford4(q)==0 and clifford4(p)==1 and sw2_real(q)==0
results['Clifford_normalization_alarm']={'q':q,'unit_form':p,
 'Brauer_Cq':0,'Brauer_Cunit':1,'raw_difference':1,'w2_q':0,
 'scope':'refutes raw full-Clifford difference interpretation; not a refutation of a separately normalized invariant'}

# Sorted zero-sum cone: exact extreme-ray decomposition, including its inverse.
cone=[]
for m in range(1,8):
    N=m+1;v=tuple(2*j-m for j in range(N))
    ds=tuple(v[i]-v[i-1] for i in range(1,N))
    rays=[tuple(-(N-i) if j<i else i for j in range(N)) for i in range(1,N)]
    inv=tuple(sum(Fraction(ds[i-1],N)*rays[i-1][j] for i in range(1,N)) for j in range(N))
    assert sum(v)==0 and inv==v
    assert all(sum(ray)==0 for ray in rays)
    cone.append({'m':m,'v':v,'differences':ds,'rays':rays,'coefficients':[str(Fraction(d,N)) for d in ds],'inverse':[str(x) for x in inv]})
results['sorted_cone']=cone
results['separation_missing_nonzero']={'functional':'ell=0','all_nonnegative_tests':True,'vanishes_on_ones':True,'separates_an_interior_point':False}

OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps({'certificate_groups':list(results),'quadric_dimensions_tested':[1,12],
 'all_assertions':'passed','output':str(OUT)},ensure_ascii=False,indent=2))
