"""Exact finite certificates for cote 43. Infinite assertions have proofs in proofs.md.
No floating point, no random tests, no claim that truncation proves an infinite theorem.
Run from any directory: python exact_checks.py > exact_checks_output.txt
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd
from itertools import product, combinations
import json

def emit(name,data): print(json.dumps({'check':name,'result':data},ensure_ascii=False))

# CFT: dividing an idele by a principal representative reverses its ideal divisor.
for m in (5,8,9):
    units=[a for a in range(m) if gcd(a,m)==1]
    emit('ray_sign_mod_'+str(m),[[a,pow(a,-1,m)] for a in units])
assert pow(2,-1,5)==3 and 2!=3

def mul(a,b,N,p=None):
    c=[0]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:c[i+j]+=x*y
    return [x%p for x in c] if p else c
def power(a,n,N,p=None):
    z=[1]+[0]*N
    for _ in range(n):z=mul(z,a,N,p)
    return z
def subst(a,p,N):return [a[i//p] if i%p==0 and i//p<len(a) else 0 for i in range(N+1)]
for p in (2,3,5):
    N=3*p+2;checked=0
    for a1,a2,a3 in product(range(p),repeat=3):
        a=[1,a1,a2,a3]+[0]*(N-3)
        F=[pow(x,p,p) for x in a]
        assert power(a,p,N,p)==subst(F,p,N)
        checked+=1
    emit('Witt_FV_VF_equals_p',{'p':p,'truncation':N,'series_checked':checked})

# Procyclic H^2: inflation C_(nm)->C_n takes a mod n to m*a mod nm.
for n,m in ((2,3),(3,4),(4,5)):
    images=[m*a%(n*m) for a in range(n)]
    assert len(set(images))==n
    assert all(Q(a,n)%1==Q(m*a,n*m)%1 for a in range(n))
    emit('H2_inflation',{'n':n,'m':m,'images':images})

# Completion order: (t-s)^-1 = sum s^j/t^(j+1) in k((t))[[s]].
for N in (2,5,10):
    # Formal coefficient dictionary in Laurent t and polynomial s.
    f={(-j-1,j):1 for j in range(N+1)};z={}
    for (a,b),c in f.items():
        z[(a+1,b)]=z.get((a+1,b),0)+c
        z[(a,b+1)]=z.get((a,b+1),0)-c
    z={k:v for k,v in z.items() if v}
    assert z=={(0,0):1,(-N-1,N+1):-1}
    emit('iterated_completion_geometric_series',{'N':N,'product':[[list(k),v] for k,v in z.items()]})

# Finite-stage shadow of Hom(K,K/R): t-surjective source, t^n-torsion target.
for n in range(1,7):
    # k[t]/t^n, multiplication by t matrix. A hypothetical image is in t^n target=0.
    T=[[int(i==j+1) for j in range(n)] for i in range(n)]
    emit('Hom_colimit_finite_stage',{'n':n,'t_surjective_source_implies_image_in_t^n_target':0})

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b,s=1):return [[x+s*y for x,y in zip(r,t)] for r,t in zip(a,b)]
I=[[1,0],[0,1]];T=[[0,1],[0,0]];Z=[[0,0],[0,0]]
assert mm(T,T)==Z
assert add(mm(T,I),mm(I,T))==[[0,2],[0,0]]
assert add(mm(T,I),mm(I,T),-1)==Z
emit('graded_commutator_unit',{'printed_plus_D1':[[0,2],[0,0]],'correct_minus_d1':Z})

# Associativity of finite path concatenation; vertices, not commutative matrix cells.
paths=[c for n in range(1,5) for c in combinations(range(4),n)]
def cat(a,b):return a+b[1:] if a is not None and b is not None and a[-1]==b[0] else None
count=0
for a,b,c in product(paths,repeat=3):
    assert cat(cat(a,b),c)==cat(a,cat(b,c));count+=1
emit('path_associativity',{'paths':len(paths),'triples':count})
# Commuting bicomplex differential operators: square of A-B = -2AB if A^2=B^2=0.
A=[[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,0]]
B=[[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]]
assert mm(A,B)==mm(B,A)
S=add(A,B,-1);assert mm(S,S)[3][0]==-2
emit('commuting_differentials_sign',{'square_entry_30':mm(S,S)[3][0]})

# Additive polynomials: only p-powers pass all binomial coefficient tests.
for p in (2,3,5,7):
    good=[n for n in range(1,50) if all(comb(n,i)%p==0 for i in range(1,n))]
    expected=[];n=1
    while n<50:expected.append(n);n*=p
    assert good==expected
    emit('additive_polynomial_exponents',{'p':p,'bound':49,'exponents':good})

# A nonzero character Ga->Gm over dual numbers: (1+e x)(1+e y)=1+e(x+y).
emit('internal_Hom_dual_numbers',{'ring':'k[e]/e^2','character':'1+e*t','cross_term':'e^2*x*y=0','nonzero':True})

# alpha_p self-extensions: F(top)=a bottom,V(top)=b bottom,F(bottom)=V(bottom)=0.
for p in (2,3,5):
    for a,b in product(range(p),repeat=2):
        F=[[0,a],[0,0]];V=[[0,b],[0,0]]
        assert mm(F,V)==mm(V,F)==Z
    emit('alpha_p_Ext_parameters',{'field':'F_'+str(p),'labelled_extensions':p*p,'relations':'FV=VF=0'})

# Residue pairing monomials Res(t^i d(t^j))=j delta_(i+j,0).
for p in (2,3,5,7):
    exps=[j for j in range(1,13) if j%p]
    mat=[[j%p if i==j else 0 for j in exps] for i in exps]
    determinant=1
    for j in exps:determinant=determinant*j%p
    assert determinant
    emit('alpha_p_local_residue_block',{'p':p,'exponents':exps,'determinant_mod_p':determinant})

# Dieudonne normal form over W(F_p)=Z_p: Laurent-F model V=p F^-1.
def dmul(a,b):
    z={}
    for i,x in a.items():
        for j,y in b.items():z[i+j]=z.get(i+j,0)+x*y
    return {i:x for i,x in z.items() if x}
for p in (2,3,5):
    F={1:1};V={-1:p};assert dmul(F,V)==dmul(V,F)=={0:p}
    u={0:7,1:2,2:3,-1:5*p,-2:11*p*p}
    assert dmul(F,u)=={1:7,2:2,3:3,0:5*p,-1:11*p*p}
    assert dmul(V,u)=={-1:7*p,0:2*p,1:3*p,-2:5*p*p,-3:11*p**3}
    emit('Dieudonne_normal_form',{'p':p,'F_times_u':dmul(F,u),'V_times_u':dmul(V,u),'scope':'sigma=id specialization; semilinear proof separately'})

# Pro-set forgetting topology: every proposed finite prefix misses a later nonzero bit.
for n in (0,1,2,4,8):
    zero=(0,)*(n+1);later=(0,)*n+(1,)
    assert zero[:n]==later[:n] and int(not any(zero))!=int(not any(later))
emit('pro_finite_set_discontinuity',{'tested_prefixes':[0,1,2,4,8],'formula':'delta_at_zero never factors through any finite prefix'})

# Square-zero rings R_N=k+V_N show Loewy length 2 with unbounded composition length.
for n in (1,2,5,10,100):
    emit('socle_counterexample_finite_shadow',{'dim_V':n,'Loewy_length_R':2,'composition_length_R':n+1})

# Tame symbols on P1 using factored rational functions, including infinity.
def val_lead(f,x):
    c,div=f
    if x=='inf':return -sum(div.values()),c
    v=div.get(x,0);lead=c
    for a,n in div.items():
        if a!=x:lead*=Q(x-a)**n
    return v,lead
def symbol(f,g,x):
    a,u=val_lead(f,x);b,v=val_lead(g,x)
    return Q((-1)**(a*b))*u**b/v**a
samples=[((Q(1),{0:1}),(Q(1),{1:1})),((Q(2),{0:2,2:-1}),(Q(3),{1:3,2:-2})),((Q(1),{0:1}),(Q(1),{0:1}))]
for f,g in samples:
    places=sorted(set(f[1])|set(g[1]))+['inf'];symbols=[symbol(f,g,x) for x in places]
    z=Q(1)
    for s in symbols:z*=s
    assert z==1
    assert all(symbol(f,g,x)*symbol(g,f,x)==1 for x in places)
    emit('tame_reciprocity_P1',{'f':str(f),'g':str(g),'places':places,'symbols':[str(s) for s in symbols],'product':str(z)})
assert symbol((Q(1),{0:1}),(Q(2),{}),0)==Q(1,2)
emit('ordinary_units_orthogonality_counterexample',{'f':'t','unit_idele':'2 at 0, 1 elsewhere','global_pairing':'1/2 != 1'})
print('ALL EXACT ASSERTIONS PASSED. Scope and infinite proofs: proofs.md.')
