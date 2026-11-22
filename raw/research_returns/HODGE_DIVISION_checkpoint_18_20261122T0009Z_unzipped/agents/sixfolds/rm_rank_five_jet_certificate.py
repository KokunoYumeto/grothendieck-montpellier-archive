#!/usr/bin/env python3
"""Finite exact supplement for SF-E839; no module or action construction."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

start = time.perf_counter()
z = sp.symbols("z1:5")
a,b = sp.symbols("a b")
pairs = [(i,j) for i in range(4) for j in range(i+1,4)]
J = sp.Matrix([[0,1,0,1],[1,1,3,2],[1,0,1,0],[1,0,2,0]])
pi = sp.zeros(4); pi[0,1]=1; pi[1,0]=-1
qi = sp.zeros(4); qi[2,3]=1; qi[3,2]=-1
p = J*pi*J.T
q = J*qi*J.T
records = []
def check(name, condition, data=None):
    assert condition, name
    records.append({"name":name,"pass":True,"data":data})
check("parameter_determinant",J.det()==-1)
check("two_transformed_coefficient_lists",
      [p[i,j] for i,j in pairs]==[-1,-1,-1,-1,-1,0]
      and [q[i,j] for i,j in pairs]==[-3,-1,-2,-2,-4,0])
def pf(M):
    return M[0,1]*M[2,3]-M[0,2]*M[1,3]+M[0,3]*M[1,2]
check("individual_and_mixed_wedges",pf(p)==pf(q)==0 and pf(p+q)==-1)

ell=list(J*sp.Matrix(z))
F=[ell[0]**2+ell[1]*ell[2],ell[1]**2,ell[2]**2,ell[3]**2]
def br(f,g,k):
    return sp.expand(sp.diff(f,z[k])*sp.diff(g,z[k+1])
                     -sp.diff(f,z[k+1])*sp.diff(g,z[k]))
brp=[br(F[i],F[j],0) for i,j in pairs]
brq=[br(F[i],F[j],2) for i,j in pairs]
check("actual_last_bracket_zero",brp[-1]==brq[-1]==0)
monomials=[x*x for x in z]+[z[i]*z[j] for i,j in pairs]
def matrix(polys):
    return sp.Matrix([[sp.Poly(f,z).coeff_monomial(mon) for f in polys]
                      for mon in monomials])
full=matrix(F+[a*x+b*y for x,y in zip(brp,brq)])
check("actual_full_determinant_identically_zero",
      DomainMatrix.from_Matrix(full).det().as_expr()==0)
for aa,bb in [(1,0),(0,1),(1,1)]:
    rank=DomainMatrix.from_Matrix(full.subs({a:aa,b:bb})).rank()
    check(f"actual_full_rank_{aa}_{bb}",rank==9,rank)

# Independently differentiate the relation shape in ell coordinates with
# the transformed bivector, then reduce quadrics by the four relations.
g=[z[0]**2+z[1]*z[2],z[1]**2,z[2]**2,z[3]**2]
form=a*p+b*q
columns=[]
for i,j in pairs:
    poly=sp.expand(sum(form[k,l]*sp.diff(g[i],z[k])*sp.diff(g[j],z[l])
                       for k in range(4) for l in range(4)))
    coeff=list(matrix([poly]))
    reduced=coeff[4:]
    reduced[3]-=coeff[0]
    columns.append(sp.Matrix(reduced))
M=sp.Matrix.hstack(*columns)
expected_minor=-1024*(a+3*b)*(a+b)*(a+2*b)**2*(a+4*b)
minor=sp.factor(DomainMatrix.from_Matrix(M[:5,:5]).det().as_expr())
check("entire_five_by_five_minor",sp.expand(minor-expected_minor)==0,str(minor))
check("last_column_zero",M[:,5]==sp.zeros(6,1))
for aa,bb in [(1,0),(0,1),(1,1)]:
    rank=DomainMatrix.from_Matrix(M.subs({a:aa,b:bb})).rank()
    check(f"quotient_rank_{aa}_{bb}",rank==5,rank)
check("generic_quotient_rank",DomainMatrix.from_Matrix(M).rank()==5)

actual_jac=sp.Matrix([[sp.diff(f,x) for x in z] for f in F]).det()
check("actual_jacobian_socle",
      sp.expand(actual_jac+16*sp.prod(ell))==0,
      "-16 ell1 ell2 ell3 ell4")
c,u,v,w=sp.symbols("c u v w")
H=sp.Matrix([[c,0,0,0],[0,u,c/2,0],[0,c/2,v,0],[0,0,0,w]])
check("rank_one_forces_c_zero",
      sp.det(H.extract([0,1],[0,2]))==c**2/2,
      "A rank-one matrix has this minor zero, hence c=0 over C.")
check("remaining_diagonal_rank_one_conditions",
      [sp.det(H.subs(c,0).extract(ii,ii)) for ii in [(1,2),(1,3),(2,3)]]
      ==[u*v,u*w,v*w])

# Sharpness boundary for the abstract five-annihilator argument only.
edge_incidence=sp.Matrix([[int(i in pair) for i in range(4)] for pair in pairs])
check("four_annihilator_boundary_rank",
      DomainMatrix.from_Matrix(edge_incidence).rank()==4)
check("residual_coefficient_count",36*6==216)
output={
    "status":"PASS",
    "completed_utc":datetime.now(timezone.utc).isoformat(),
    "runtime_seconds":time.perf_counter()-start,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope":"Exact algebra supplement only; no all-size theorem or module-deformation verification.",
    "quotient_matrix":str(M),
    "checks":records,
}
path=Path(__file__).with_name("rm_rank_five_jet_certificate_output.json")
path.write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps({"status":"PASS","checks":len(records),
                  "runtime_seconds":output["runtime_seconds"],
                  "output":str(path)},indent=2))
