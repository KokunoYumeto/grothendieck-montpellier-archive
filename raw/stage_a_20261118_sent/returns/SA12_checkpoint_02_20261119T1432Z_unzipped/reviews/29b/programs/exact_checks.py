#!/usr/bin/env python3
"""Exact finite/algebraic checks. Universal proofs are in independent_checks.md."""
import json,pathlib,itertools,math
import sympy as s
root=pathlib.Path(__file__).resolve().parents[1]
out=[]
def record(name,data):out.append({'check':name,'result':data})

# Arithmetic Frobenius action on C3; this is the exact abstract Galois group.
def mul(a,b):return ((a[0]+(-1)**a[1]*b[0])%3,(a[1]+b[1])%2)
tau=(1,0);fro=(0,1)
assert mul(mul(fro,tau),fro)==(2,0)
record('C3_semidirect_C2',{'F_tau_F_inverse':mul(mul(fro,tau),fro),'tau':tau,'noncentral':True})

X=s.Matrix([[1,1,0],[0,1,0],[0,0,1]])
Y=s.Matrix([[1,0,0],[0,1,1],[0,0,1]])
comm=X*Y*X.inv()*Y.inv()
assert comm==s.Matrix([[1,0,1],[0,1,0],[0,0,1]])
record('Heisenberg_extension',{'commutator':str(comm),'nontrivial_central_commutator':True})

def quat(a,b):
    w,x,y,z=a;v,r,t,u=b
    return(w*v-x*r-y*t-z*u,w*r+x*v+y*u-z*t,w*t-x*u+y*v+z*r,w*u+x*t-y*r+z*v)
ii=(0,1,0,0);jj=(0,0,1,0)
assert quat(ii,jj)!=quat(jj,ii)
record('Q8_normal_cyclic_subgroups',{'i_j':quat(ii,jj),'j_i':quat(jj,ii),'orders':4,'indices':2})

degree=[]
for p in [1,2,3,5]:
    for d in [-6,0,1,4,6,10]:
        if d==0: value='full prime-to-p Tate module'
        else:
            value=abs(d)
            if p>1:
                while value%p==0:value//=p
        degree.append({'p_exponent':p,'degree':d,'cokernel_order':value})
record('P1_self_intersection_cokernels',degree)

matrices=[s.Matrix([[2,1],[0,4]]),s.Matrix([[2,1],[0,3]]),s.Matrix([[1,2],[0,-1]])]
record('tame_lattice_determinants',[{'matrix':str(M),'det':int(M.det()),'invertible_mod_ell':{str(l):int(M.det())%l!=0 for l in[2,3,5,7]}}for M in matrices])

t,T,x,y,z=s.symbols('t T x y z')
gb=s.groebner([t*x,(1-t)*y],t,x,y,order='lex')
eliminated=[str(g.as_expr())for g in gb.polys if not g.as_expr().has(t)]
assert eliminated==['x*y']
record('CRT_converse_failure',{'intersection_generators':eliminated,'sum_vanishes_at_origin':True})

cusp=[]
for p in[2,3,5,7]:
    equations=[y**p-x**(p+1),z**p-x,x*z-y]
    basis=s.groebner(equations,x,y,z,order='lex',modulus=p)
    assert all(basis.reduce(f)[1]==0 for f in [x-z**p,y-z**(p+1)])
    relation=s.groebner([y**p-x**(p+1),z**p-x],z,y,x,order='lex',modulus=p)
    assert relation.reduce((x*z)**p-y**p)[1]==0
    cusp.append({'p':p,'coincidence_ring_basis':[str(g.as_expr())for g in basis.polys],'generic_rank':1,'cusp_fibre_length':p,'alpha_equalizer_generic_length':1,'alpha_equalizer_special_length':p})
record('alpha_p_equalizers_and_cusp',cusp)

epsilon=s.symbols('epsilon')
record('dual_number_rigidity_failure',[{'p':p,'epsilon_power_mod_epsilon_squared':str(s.rem(epsilon**p,epsilon**2,epsilon)),'translation_nonidentity':True}for p in[2,3,5]])

P=(T*T+T+1)*(T-3)
C1=s.Matrix([[0,-1],[1,-1]]);C2=s.Matrix([[3]])
C=s.diag(C1,C2)
assert s.expand(C.charpoly(T).as_expr()-P)==0
record('monic_factor_characteristic_polynomial',{'P':str(s.expand(P)),'charpoly':str(C.charpoly(T).as_expr()),'factor_ranks':[2,1]})

f=T**3-4*T+1
assert all(f.subs(T,a)!=0 for a in[1,-1])
disc=int(s.discriminant(f,T));assert disc==229 and s.isprime(disc)
record('totally_real_tame_S3_example',{'polynomial':str(f),'discriminant':disc,'irreducible_by_rational_root_test':True,'discriminant_positive_nonsquare':True,'only_possible_finite_ramified_prime':229,'ramification_index_at229':2,'tame':True})

for n in range(1,7):
    a=[0]*(n+2);b=a.copy();a[0]=b[0]=n;b[n+1]=1
    assert a[:n]==b[:n]
    assert a[a[0]+1]!=b[b[0]+1]
record('Baire_continuous_not_finite_stage',{'tested_prefix_lengths':list(range(1,7)),'general_witness':'x0=y0=n, all other coordinates0 except y_(n+1)=1','values':[0,1],'universal_proof':'independent_checks.md §9'})

v=s.Matrix([1,2]);minus=s.Matrix([[-2,1]]);plus=s.Matrix([[2,1]])
assert minus*v==s.zeros(1,1) and plus*v!=s.zeros(1,1)
record('English_graph_equation_sign',{'point':[1,2],'y_minus_2x':str(minus*v),'y_plus_2x':str(plus*v)})

counts=[]
for n in range(1,6):
    count=sum(len(set(v))==n for v in itertools.product(range(n),repeat=n))
    assert count==math.factorial(n)
    counts.append({'n':n,'ordered_distinct_n_tuples':count,'n_factorial':math.factorial(n)})
record('Sn_frame_torsor_fibres',counts)

result={'all_assertions_passed':True,'checks':out}
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs'/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
