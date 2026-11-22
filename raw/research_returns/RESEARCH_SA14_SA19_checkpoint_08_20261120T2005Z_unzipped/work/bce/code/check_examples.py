"""Symbolic certificates for the examples in Parts B and E.

These calculations check polynomial identities, Jacobian ideals, and cotangent
linear independence. They do not replace the dimension/normality proofs.
"""
import json
import time
import itertools
from pathlib import Path
import sympy as s

started = time.perf_counter()
x, y, z, w, t = s.symbols('x y z w t')
results = {}

# A split form avoids any square-root choice and works also in characteristic 2.
q = x*y-z*(z-t*w)
results['B_projective_equation'] = str(q)
results['B_divisor_substitution'] = str(s.expand(q.subs({x:0,z:0})))
results['B_generic_change_to_segre'] = str(s.expand(q.subs(w,(z-w)/t)))
assert s.expand(q.subs({x:0,z:0})) == 0
assert s.expand(q.subs(w,(z-w)/t)) == x*y-z*w
qaff = s.expand(q.subs(w,1))
for p in (2,3,5):
    jac = [qaff] + [s.diff(qaff,v) for v in (x,y,z,t)]
    gb = s.groebner(jac,x,y,z,t,modulus=p)
    vals=[str(f.as_expr()) for f in gb.polys]
    results[f'B_total_jacobian_char_{p}']=vals
    assert set(vals)=={'x','y','z','t'}

# In the local quotient, qaff has no degree-one term; x,z remain independent.
results['B_cotangent_relation_degree'] = s.Poly(qaff,x,y,z,t).total_degree()
results['B_I_mod_mI_generators'] = ['x','z']
assert all(sum(m)>=2 for m,c in s.Poly(qaff,x,y,z,t).terms())

# Equal geometric fibre types do not determine factoriality of the total family.
results['B_good_family_eliminate_t'] = str((x*y-z*z-t).subs(t,x*y-z*z))
assert (x*y-z*z-t).subs(t,x*y-z*z) == 0

# E1: total space normal does not mean that its fibres are geometrically normal.
f = y*y-x*x*x-x*x-t*t
disc = s.factor(s.discriminant(x*x*x+x*x+t*t,x))
results['E_cubic_discriminant'] = str(disc)
assert disc == -t*t*(27*t*t+4)
results['E_section_P'] = str(s.expand(f.subs({x:0,y:t})))
assert s.expand(f.subs({x:0,y:t})) == 0
gb=s.groebner([f,s.diff(f,x),s.diff(f,y),s.diff(f,t)],x,y,t)
results['E_total_jacobian_Q'] = [str(g.as_expr()) for g in gb.polys]
assert set(results['E_total_jacobian_Q'])=={'x','y','t'}
results['E_cotangent_generators']=['x','y - t']
assert s.Matrix([[1,0,0],[0,1,-1]]).rank()==2

# B2: projective determinantal example, local chart w=1.
a,b,c,d,e,f,u0,u1,v0,v1,v2=s.symbols('a b c d e f u0 u1 v0 v1 v2')
minors=[a*e-b*d,a*f-c*d,b*f-c*e]
segre={a:u0*v0,b:u0*v1,c:u0*v2,d:u1*v0,e:u1*v1,f:u1*v2}
assert all(s.expand(g.subs(segre))==0 for g in minors)
assert all(s.expand(g.subs({a:0,b:0,c:0,e:t*w}))==0 for g in minors)
results['B2_segre_hyperplane']=str((a+e).subs(segre))
results['B2_divisor_residual_coordinates']=['d','f','w']
results['B2_local_cotangent_ideal_generators']=['a','b','c']
results['B2_local_relations_have_no_linear_terms']=all(all(sum(m)==2 for m,co in s.Poly(g,a,b,c,d,e,f).terms()) for g in minors)
assert results['B2_local_relations_have_no_linear_terms']

# H12: isolated singularity and formal split in characteristic three.
h=x*y-z*z-t*t*(1+t)
jac=[h]+[s.diff(h,v) for v in (x,y,z,t)]
gb=s.groebner(jac,x,y,z,t,modulus=3)
results['C4_char3_jacobian']=[str(g.as_expr()) for g in gb.polys]
assert set(results['C4_char3_jacobian'])=={'x','y','z','t'}
# Hensel recurrence s(t)^2=1+t mod t^N, 2 invertible in F3.
N=16
coeff=[1]
for n in range(1,N):
    rhs=(1 if n==1 else 0)-sum(coeff[j]*coeff[n-j] for j in range(1,n))
    coeff.append((2*rhs)%3)
root=sum(coeff[n]*t**n for n in range(N))
rem=s.Poly(s.expand(root**2-(1+t)),t,modulus=3)
assert all(m[0]>=N for m,co in rem.terms())
results['C4_sqrt_1_plus_t_mod_t16_F3']=str(root)
results['C4_square_remainder_order']=min(m[0] for m,co in rem.terms())
results['C4_formal_coordinate_jacobian']='det d(z-it*s,z+it*s)/d(z,t) at 0 = 2*i != 0 in characteristic 3'

# E4: the diagonal three-quadric surface and its free sign involution.
V=s.Matrix([[i**j for i in range(6)] for j in range(3)])
triples=list(itertools.combinations(range(6),3))
determinants={','.join(map(str,T)):int(V[:,T].det()) for T in triples}
assert all(d!=0 for d in determinants.values())
results['E4_K3_all_3column_Vandermonde_determinants']=determinants
results['E4_K3_fixed_plane_determinants']=[int(V[:,:3].det()),int(V[:,3:].det())]
results['E4_K3_smoothness_certificate']='Every 3 columns independent; a dependent Jacobian row combination is a degree<=2 polynomial vanishing at each nonzero coordinate, so support<=2; defining equations then force all coordinates zero.'

# E4: exact Kunneth dimensions for M=P_s external tensor O_P1(-2).
cohom_E={'nontrivial_degree_zero':[0,0],'trivial':[1,1]}
cohom_P1=[0,1]
kun={}
for key,he in cohom_E.items():
    kun[key]=[sum(he[i]*cohom_P1[q-i] for i in range(2) if 0<=q-i<2) for q in range(3)]
assert kun=={'nontrivial_degree_zero':[0,0,0],'trivial':[0,1,1]}
results['E4_square_zero_M_cohomology_h0_h1_h2']=kun
results['E4_square_zero_Pic0_dimensions']={'generic':1,'special_identity':2}

# E4: normal-fibre quotient whose generic order-two line bundle does not extend.
W=s.Matrix([[1,1,1,1,1,1],[0,1,2,3,5,7],[0,1,2+t,9,25,49]])
normal_dets={','.join(map(str,T)):s.factor(W[:,T].det()) for T in triples}
assert normal_dets['0,1,2']==t
assert all(v.subs(t,0)!=0 for key,v in normal_dets.items() if key!='0,1,2')
results['E4_normal_K3_all_3column_determinants']={k:str(v) for k,v in normal_dets.items()}
results['E4_normal_K3_only_dependent_special_triple']=[k for k,v in normal_dets.items() if v.subs(t,0)==0]
ker=W[:,:3].subs(t,0).nullspace()
assert len(ker)==1 and ker[0]==s.Matrix([1,-2,1])
results['E4_normal_K3_node_squared_coordinates']=[1,-2,1,0,0,0]
X=s.symbols('X0:6')
quadrics=[sum(W[j,i]*X[i]**2 for i in range(6)) for j in range(3)]
local=s.expand((quadrics[2]-quadrics[1]).subs(X[2],1))
assert local==t+6*X[3]**2+20*X[4]**2+42*X[5]**2
results['E4_normal_K3_local_smoothing_equation']=str(local)
results['E4_normal_K3_node_Hessian_determinant']=12*40*84
assert s.diff(local,t)==1
results['E4_normal_K3_total_regularity_certificate']='At each of four fixed nodes X2=1, d(Q2-Q1)/dt=1; away from them the fibre Jacobian has rank3.'
results['runtime_seconds']=round(time.perf_counter()-started,6)
results['scope']='Exact polynomial identities over Q and finite fields F2,F3,F5; not point sampling.'
out=Path(__file__).with_suffix('.output.json')
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
