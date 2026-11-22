"""Exact auxiliary identities for the uniform mixed degree-one Lang-cover gate.

The dimension argument is a separate proof; this program checks its matrices,
smooth-cubic partials, Gram differential, and the uniform exceptional-locus witness.
"""
from pathlib import Path
import sympy as S
import json,time
start=time.perf_counter()
a,u0,u1,u2=S.symbols('a u0 u1 u2')
q=S.symbols('q00 q10 q20 q01 q11 q21')
variables=(a,u0,u1,u2)+q
def red(x):
    n,d=S.fraction(S.cancel(x))
    return S.Poly(n,*variables,modulus=2).as_expr()/S.Poly(d,*variables,modulus=2).as_expr()
def rm(M):return M.applyfunc(red)
def zero(M):return all(red(x)==0 for x in M)
def B(u):
    x,y,z=u
    return S.Matrix([[x,0,a*z],[0,a*z,a*(y+z)],
                     [a*z,a*(y+z),a*(x+y+z)]])
Ro=S.Matrix([[1,0,a],[0,0,a],[0,a,a]])
J=S.Matrix([[0,0,1],[0,1,0],[1,0,0]])
U=S.Matrix([u0,u1,u2])
cubic=u0**2*u2+u0*u1*u2+u0*u1**2+a*u2**3
assert red(B(U).det()-a*a*cubic)==0
partials=[red(S.diff(cubic,x)) for x in (u0,u1,u2)]
assert partials==[u1*u2+u1**2,u0*u2,u0**2+u0*u1+a*u2**2]
# If u0=0, cubic=a*u2^3 forces u2=0, and partial0=u1^2.
# If u2=0 and u0!=0, cubic forces u1=0, and partial2=u0^2.
assert red(cubic.subs(u0,0)-a*u2**3)==0
assert red(partials[0].subs({u0:0,u2:0})-u1**2)==0
assert red(cubic.subs(u2,0)-u0*u1**2)==0
assert red(partials[2].subs({u1:0,u2:0})-u0**2)==0

e0=S.Matrix([1,0,0]);e1=S.Matrix([0,1,0]);e2=S.Matrix([0,0,1])
u=rm(Ro.T.inv()*e0);v=rm(Ro.T.inv()*e1)
B1=rm(B(u));B2=rm(B(v));C=rm(B2*B1.inv())
assert zero(u-S.Matrix([1,1,0]))
assert zero(v-S.Matrix([0,1/a,1/a]))
assert red(B1.det()-a*a)==0
assert zero(B2-J)
assert zero(C*e0-e2)

Q=S.Matrix([[q[0],q[3]],[q[1],q[4]],[q[2],q[5]]])
Q2=Q.applyfunc(lambda x:x*x)
H=Q.T*J*Q2
Jac=rm(S.Matrix(list(H)).jacobian(q))
L=(J*Q2).T
expected=S.diag(L,L)
assert Jac.shape==(4,6) and zero(Jac-expected)
minor_checks=[]
pairs=[(0,1),(0,2),(1,2)]
for I in pairs:
    for K in pairs:
        cols=list(I)+[i+3 for i in K]
        lhs=Jac[:,cols].det()
        rhs=L[:,list(I)].det()*L[:,list(K)].det()
        assert red(lhs-rhs)==0
        minor_checks.append({'first_columns':I,'second_columns':K,'identity':True})

out={'status':'PASS','scope':'Auxiliary symbolic identities only; the geometric dimensions and Lang-cover connectedness require the separate proof.',
     'det_B':str(a*a*cubic),'cubic_partials':[str(x) for x in partials],
     'smooth_cubic_for_all_a_nonzero':True,
     'uniform_frame_witness':{'T':'(e0,e1)','B1_determinant':'a^2','B2':'J','C_e0':'e2'},
     'gram_jacobian_shape':list(Jac.shape),'gram_block_identity':True,
     'gram_minor_checks':minor_checks,
     'rank_two_dimension_bounds':{'generic':6+(6-3)-4,'exceptional':5+(6-2)-4},
     'elapsed_seconds':time.perf_counter()-start}
dest=Path(__file__).resolve().parents[1]/'outputs/independent_mixed_lang_rank_compatibility.json'
assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
