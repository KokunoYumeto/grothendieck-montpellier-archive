"""Exact finite certificates for the mathematical computations in cote91:59–98.

Finite ranges below are explicitly finite checks, not proofs of unbounded
identities. The independent all-degree arguments are in proof_checks.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from math import comb, factorial
import json
import sympy as S

def plus(a,b):
    c=Counter(a)
    for w,v in b.items(): c[w]+=v
    return {w:v for w,v in c.items() if v}
def scale(a,n): return {w:v*n for w,v in a.items() if v*n}
def mul(a,b):
    c=Counter()
    for u,x in a.items():
        for v,y in b.items(): c[u+v]+=x*y
    return dict(c)
def sub(a,b): return plus(a,scale(b,-1))
def ad(x,y): return sub(mul(x,y),mul(y,x))
def mod(a,p): return {w:v%p for w,v in a.items() if v%p}
def letter(x): return {(x,):1}
def ad_power(x,y,n):
    for _ in range(n): y=ad(x,y)
    return y
def g(i,j):
    return {w:1 for w in product(('x','y'),repeat=i+j) if w.count('x')==i}

out={}
x,y=letter('x'),letter('y')
for n in range(13):
    rhs={('x',)*i+('y',)+('x',)*(n-i):(-1)**(n-i)*comb(n,i) for i in range(n+1)}
    assert ad_power(x,y,n)==rhs
out['ad_binomial']={'checked_n':list(range(13)),'result':'all exact word coefficients agree over Z'}
pol=[]
for k in range(1,8):
    for i in range(k+1):
        labels=['x']*i+['y']*(k-i)
        f=Counter(tuple(labels[j] for j in order) for order in permutations(range(k)))
        assert dict(f)==scale(g(i,k-i),factorial(i)*factorial(k-i))
    pol.append(k)
out['polarization']={'checked_k':pol,'result':'f_k(x repeated i,y repeated k-i)=i!(k-i)!g_(i,k-i)'}
char=[]
for p in (2,3,5,7):
    assert mod(ad_power(x,y,p),p)==mod(sub(mul({('x',)*p:1},y),mul(y,{('x',)*p:1})),p)
    assert mod(ad_power(x,y,p-1),p)=={('x',)*i+('y',)+('x',)*(p-1-i):1 for i in range(p)}
    labels=tuple('x'+str(i) for i in range(p-1))
    lhs={}
    for perm in permutations(labels):
        term=letter('y')
        for a in reversed(perm): term=ad(letter(a),term)
        lhs=plus(lhs,term)
    rhs={w:1 for w in permutations(labels+('y',))}
    assert mod(lhs,p)==mod(rhs,p)
    for i in range(p):
        lhs={}
        for word in product(('x','y'),repeat=p-1):
            if word.count('x')!=i: continue
            term=y
            for a in reversed(word): term=ad(letter(a),term)
            lhs=plus(lhs,term)
        assert mod(lhs,p)==mod(scale(g(i,p-i),p-i),p)
    char.append({'p':p,'restricted_ad':True,'degree_p_minus_1':True,'multilinear_polarization':True,'g_coefficient_identity':True})
out['characteristic_p']=char

exp=[]
for n in range(13):
    for i in range(n+1):
        assert Fraction(comb(n,i),factorial(n))==Fraction(1,factorial(i)*factorial(n-i))
    exp.append(n)
out['formal_exponential']={'checked_total_degrees':exp,'coefficient_formula':'binom(n,i)/n!=1/(i!(n-i)!)'}
pbw=[]
for s in range(1,7):
    survive=sum(1 for slots in product(range(s),repeat=s) if len(set(slots))==s)
    assert survive==factorial(s)
    pbw.append({'s':s,'surviving_assignments':survive,'s_factorial':factorial(s)})
out['pbw_top_tensor_coefficient']=pbw

H=S.diag(1,0); E=S.Matrix([[0,1],[0,0]])
assert H*E-E*H==E
v=S.Matrix([1,0])
assert H*v==v and E*v==S.zeros(2,1)
Hdual=S.eye(2)-H.T; Edual=-E.T
common=S.Matrix.vstack(Hdual,Edual).nullspace()
assert common==[]
out['tensor_reciprocity_counterexample']={'field':'Q','H':str(H),'E':str(E),'bracket':'[H,E]=E','weight_one_submodule_vector':[1,0],'reverse_H':str(Hdual),'reverse_E':str(Edual),'reverse_invariants_dimension':len(common)}
out['dual_basis_counterexample']=[]
for c in (1,2,3):
    wrong=Fraction(c);correct=Fraction(c)*Fraction(1,c)
    assert correct==1
    out['dual_basis_counterexample'].append({'basis_scalar':c,'wrong_tensor_scalar':str(wrong),'correct_dual_tensor_scalar':str(correct)})

# Monomial shadows of the infinite-dimensional proofs: degree in y is not bounded
# in either ring. These finite checks illustrate the invariant x-degree argument.
ring=[]
for m in (1,2,4,8,16):
    JmodJ2=[(1,j) for j in range(m)]
    quotient=[(1,j) for j in range(m)]
    assert all(a[0]+b[0]>=2 for a in quotient for b in quotient)
    ring.append({'y_exponents_tested':m,'independent_x_yj_classes_mod_x2':len(JmodJ2),'pairwise_products_vanish_mod_x2':True})
out['nonnoetherian_and_nonfinite_type_finite_shadows']=ring

# Stagewise indicator maps on the points a_m=m. The generic-stratum obstruction
# for infinitely many m is proved in the dossier, not by this finite table.
N=12
stage_vectors=[[int(point==j) for j in range(1,N+1)] for point in range(1,N+1)]
assert all(v[:n]==[int(point==j) for j in range(1,n+1)] for point,v in enumerate(stage_vectors,1) for n in range(1,N+1))
out['indicator_map_finite_shadow']={'stages':N,'distinct_point_value_vectors':len(set(tuple(v) for v in stage_vectors)),'compatible_under_coordinate_projection':True,'infinite_result':'requires generic-open proof, not this check'}

# An explicit element 1/2 of Z_3 is not the image of an ordinary integer.
adic=[]
for n in range(1,10):
    a=(3**n+1)//2
    assert 2*a%3**n==1
    if n>1: assert a%(3**(n-1))==adic[-1]['residue']
    adic.append({'n':n,'modulus':3**n,'residue':a})
out['non_surjective_Z_to_Z3_example']=adic
print(json.dumps(out,ensure_ascii=False,indent=2))
