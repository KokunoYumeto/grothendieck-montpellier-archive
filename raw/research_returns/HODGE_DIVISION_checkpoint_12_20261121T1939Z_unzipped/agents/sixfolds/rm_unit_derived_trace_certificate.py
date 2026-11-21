#!/usr/bin/env python3
"""Exact minimal-order obstruction to a homotopy of inner conjugation."""
from pathlib import Path
import json
import sympy as s

x,y=s.symbols('x y')
degrees=[-2,-1,0];dims={-2:1,-1:2,0:2};offset={-2:0,-1:1,0:3}
P=s.zeros(5)
v=s.Matrix([-y,x]);w=s.Matrix([[x,y]])
P[1:3,0:1]=v;P[3:5,1:3]=v*w
delta=s.diag(-y,-y,-y,s.S.Zero,s.S.Zero)
delta[3:5,3:5]=s.Matrix([[-y,0],[x,0]])
assert P*P==s.zeros(5)
assert delta*P==P*delta
U=s.eye(5)+delta
assert s.expand(U.det()-(1-y)**4)==0

bases={}
for n in range(-2,3):
    vals=[]
    for i in degrees:
        for j in degrees:
            if i-j!=n:continue
            for a in range(dims[i]):
                for b in range(dims[j]):
                    E=s.zeros(5);E[offset[i]+a,offset[j]+b]=1
                    vals.append((i,j,a,b,E))
    bases[n]=vals

def coords(M,n):
    return s.Matrix([M[offset[i]+a,offset[j]+b] for i,j,a,b,_ in bases[n]])
def linear(M):
    return M.applyfunc(lambda f:s.diff(f,x).subs({x:0,y:0})*x+s.diff(f,y).subs({x:0,y:0})*y)

D={}
for n in range(-2,2):
    D[n]=s.Matrix.hstack(*(coords(P*E-(1 if n%2==0 else -1)*E*P,n+1) for *_,E in bases[n]))
    if n>-2:assert s.simplify(D[n]*D[n-1])==s.zeros(len(bases[n+1]),len(bases[n-1]))
V=[j for j,(i,k,a,b,E) in enumerate(bases[0]) if i==k==0]
assert linear(D[-1])[V,:]==s.zeros(4,len(bases[-1]))
assert linear(D[0])[:,V]==s.zeros(len(bases[1]),4)
X=s.zeros(5);X[3,3]=1
comm=delta*X-X*delta
assert comm[3:5,3:5]==s.Matrix([[0,0],[x,0]])
out={'result':'PASS','endomorphism_complex_ranks':{str(n):len(v) for n,v in bases.items()},
     'chain_automorphism_determinant':str(s.factor(U.det())),
     'linear_differential_into_EndP0':'zero','linear_differential_out_of_EndP0':'zero',
     'nonzero_linear_conjugation_block':str(comm[3:5,3:5]),
     'limits':'The obstruction to every power-series homotopy is the written minimal-order argument. No quotient-trace obstruction or semiregularity consequence is inferred from this certificate.'}
Path(__file__).with_name('rm_unit_derived_trace_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
