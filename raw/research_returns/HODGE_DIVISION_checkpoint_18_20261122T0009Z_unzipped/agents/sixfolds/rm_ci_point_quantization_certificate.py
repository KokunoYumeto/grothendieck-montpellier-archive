#!/usr/bin/env python3
"""Exact supplemental identities for SF-E836; no geometric or deformation claim.

Author: GPT-6 Astra Pro, inherited effort not exposed, /root/sixfolds.
No sibling certificate or helper is imported. Universal arguments are in the proof.
"""
from pathlib import Path
import hashlib, json, time
from datetime import datetime, timezone
import sympy as s

started=time.perf_counter()
checks=[]
def check(name,condition,scope):
    if not bool(condition):
        raise AssertionError(name)
    checks.append({'name':name,'PASS':True,'scope':scope})

a,b,c=s.symbols('phi_y phi_z phi_w')
g=s.symbols('g2_y g2_z g2_w g3_y g3_z g3_w g4_y g4_z g4_w')
G=s.Matrix(3,3,g)
J=s.zeros(4)
J[0,0]=1
J[0,1]=-a;J[0,2]=-b;J[0,3]=-c
for i in range(3):
    for j in range(3):J[i+1,j+1]=G[i,j]
p=s.zeros(4);p[0,1]=1;p[1,0]=-1
q=s.zeros(4);q[2,3]=1;q[3,2]=-1
P=J*p*J.T;Q=J*q*J.T
check('all_plus_triple_brackets_zero',all(P[i,j]==0 for i in range(1,4) for j in range(i+1,4)),'Formal Jacobian shape after eliminating x from the other three ideal generators, with unrestricted mixed first-row derivatives.')
def wedge4(U,V):
    return s.expand(U[0,1]*V[2,3]-U[0,2]*V[1,3]+U[0,3]*V[1,2]+U[2,3]*V[0,1]-U[1,3]*V[0,2]+U[1,2]*V[0,3])
W=wedge4(P,Q)
check('generic_mixed_wedge_equals_Jacobian',s.expand(W-J.det())==0,'Exact polynomial identity in all twelve independent first derivatives.')
check('generic_Jacobian_equals_three_variable_minor',s.expand(J.det()-G.det())==0,'No derivative or linear part of phi is assumed to vanish.')
terms=[P[0,1]*Q[2,3],-P[0,2]*Q[1,3],P[0,3]*Q[1,2]]
minors=[P[0,1]*Q[2,3]-Q[0,1]*P[2,3],-(P[0,2]*Q[1,3]-Q[0,2]*P[1,3]),P[0,3]*Q[1,2]-Q[0,3]*P[1,2]]
check('wedge_is_sum_of_three_necessary_cross_minors',all(s.expand(u-v)==0 for u,v in zip(terms,minors)) and s.expand(sum(minors)-W)==0,'Termwise reduction uses the zero commuting triple; it does not infer proportionality over a nonreduced ring.')
check('individual_plus_and_minus_squares_zero',wedge4(P,P)==0 and wedge4(Q,Q)==0,'Exact decomposable bracket forms; not itself the contradiction.')
X,Y,B,D=s.symbols('X Y B D',commutative=False)
alpha,beta,gamma,delta=s.symbols('alpha beta gamma delta')
syzygy=(alpha-X*B)*delta+X*B*(delta-Y*D)+X*(B*Y-beta)*D+beta*(X*D-gamma)-(alpha*delta-beta*gamma)
check('noncommutative_companion_syzygy',s.expand(syzygy)==0,'Formal associative word identity with central scalar coefficients; valid in every matrix size, not a sampled matrix check.')

x,y,z,w=s.symbols('x y z w')
coordinates=(x,y,z,w)
examples=[]
for name,fs,sub,vars0 in [
 ('mixed_linear_embedding_three',(x+z,y*y,z*z,w*w),{x:-z},(y,z,w)),
 ('square_embedding_four',(x*x,y*y,z*z,w*w),{},(x,y,z,w))]:
    A=s.Matrix([[s.diff(f,t) for t in coordinates] for f in fs]);AA=A*p*A.T;BB=A*q*A.T
    det=s.expand(A.det().subs(sub));cross=s.expand((AA[0,1]*BB[2,3]-BB[0,1]*AA[2,3]).subs(sub))
    # Both quotients are explicitly tensor products of square-zero one-variable rings.
    def residue(poly):
        P=s.Poly(s.expand(poly),*vars0,domain=s.QQ)
        return s.expand(sum(coef*s.prod(v**e for v,e in zip(vars0,mon)) for mon,coef in P.terms() if all(e<2 for e in mon)))
    jac=residue(det);bad=residue(cross)
    check(name+'_Jacobian_socle_nonzero',jac!=0 and all(residue(t*jac)==0 for t in vars0),'Direct finite quotient calculation; the universal socle result is the published theorem cited in the proof.')
    check(name+'_cross_minor_nonzero',bad==jac and bad!=0,'Explicit necessary-equation violation in the indicated Artinian ring.')
    examples.append({'name':name,'length':2**len(vars0),'embedding_dimension':len(vars0),'Jacobian_residue':str(jac),'cross_minor_residue':str(bad),'Ext2_per_m_squared':6*(2**len(vars0))})

result={'status':'PASS','author':'GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds','actual_finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-started,'check_count':len(checks),'checks':checks,'examples':examples,'universal_polynomial_variable_count':12,'scope':'Exact algebraic supplement only; no numerical verification of module deformation, formal generator changes, published theorem, sheaf construction, or invariant semiregularity is claimed.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path(__file__).with_name('rm_ci_point_quantization_certificate_output.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
