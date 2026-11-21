"""Independent integral Hessian identity and F028 pair-minor check."""
from itertools import permutations
from pathlib import Path
from datetime import datetime, timezone
from math import prod
import hashlib
import json
import sympy as sp

x = sp.symbols("x0:9")
terms = list(permutations(range(3)))
P = sum(prod(x[3*i+p[i]] for i in range(3)) for p in terms)
H = sp.hessian(P,x)
a,b,c,d = sp.symbols("a b c d")
normalized = [1,1,1,1,a,b,1,c,d]
hn = sp.expand(H.subs(dict(zip(x,normalized))).det(method="domain-ge"))
pn = P.subs(dict(zip(x,normalized)))
dn = sp.Matrix(3,3,normalized).det()
assert sp.expand(hn-(64*a*b*c*d-2*pn*dn**2)) == 0

def per(X):
    return sum(prod(X[3*i+p[i]] for i in range(3)) for p in terms)

def det(X):
    return sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
               *prod(X[3*i+p[i]] for i in range(3)) for p in terms)

def gradients(X):
    f,z = per(X),det(X)
    gp,gh = [],[]
    for k in range(9):
        i,j = divmod(k,3)
        rr = [v for v in range(3) if v!=i]
        cc = [v for v in range(3) if v!=j]
        ad = X[3*rr[0]+cc[0]]*X[3*rr[1]+cc[1]]
        bc = X[3*rr[0]+cc[1]]*X[3*rr[1]+cc[0]]
        cp,cd = ad+bc,(-1)**(i+j)*(ad-bc)
        gp.append(cp)
        gh.append(64*prod(v for index,v in enumerate(X) if index!=k)
                  -2*cp*z*z-4*f*z*cd)
    return gp,gh

A = [4,1,-1,1,4,3,4,0,-1]
B = [1,-2,-4,4,-1,-2,4,-1,2]
J=[]
for t in range(4):
    gp,_ = gradients([v+t*w for v,w in zip(A,B)])
    J.append(gp+[t*v for v in gp])
for t in range(10):
    _,gh = gradients([v+t*w for v,w in zip(A,B)])
    J.append(gh+[t*v for v in gh])
source=Path(__file__).parents[1]/"jet_review"/"per3_binary_hessian_pair_certificate.json"
old=json.loads(source.read_text())
assert [[v%old["prime"] for v in row] for row in J] == [[v%old["prime"] for v in row] for row in old["best"]["Jacobian_mod_prime"]]
minor=sp.Matrix([row[:14] for row in J])
delta=int(minor.det(method="domain-ge"))
assert delta == 74225698308427431762191786581639618962627273701228066915866112824442880000000
assert delta%1000003 == 8357

def series(parts,maximum):
    out=[0]*(maximum+1)
    out[0]=1
    for part in parts:
        for k in range(part,maximum+1):
            out[k]+=out[k-part]
    return out

maximum=200
g3=series([2,3],maximum)
qbound=series([2,3]+list(range(1,10)),maximum)
assert all(qbound[s]>g3[s] for s in range(1,maximum+1))
g4=series([2,3,4],2*maximum)
for u in range(1,maximum+1):
    positive_sum=sum((u-3*v)//2+1 for v in range(u//3+1))
    assert positive_sum==g4[2*u]

result={
 "date_utc":datetime.now(timezone.utc).isoformat(),
 "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
 "method":"Symbolic Hessian of six permanent monomials and normalized exact determinant; dense torus-covariance proof gives the integral identity. Fresh pencil transcription and analytic derivatives of64product-2per*det², using only2x2 cofactors, independently give the complete pair Jacobian and integer minor.",
 "normalized_hessian_polynomial_terms":len(sp.Poly(hn,a,b,c,d).terms()),
 "compared_entries":14*18,"input_certificate_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
 "integer_minor":str(delta),"prime":1000003,"residue":delta%1000003,
 "F028_first_six_lower_bounds":qbound[1:7],"F028_first_six_ordinary":g3[1:7],
 "strict_coefficient_checks":maximum,
 "O028_even_dilation_sum_checks":maximum,
 "O028_n4_first_six_even_values":[g4[2*u] for u in range(1,7)],
 "status":"PASS",
}
Path(__file__).with_name("cubic_hessian_pair_identity_certificate.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
