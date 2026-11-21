"""Exact rational right kernels at the a_m=0 structured-residue boundary."""
from pathlib import Path
from itertools import combinations
from datetime import datetime,timezone
import json,sys,math
import sympy as S
from structured_residue_tensor import two_channel_embedding

def data(m):
    a=list(map(S.Integer,range(1,m)))+[S.Integer(0)]
    edges=[(i,j) for i in range(m) for j in range(m) if i!=j]
    basis=[{(i,j):S.Integer(1),(i,i):a[i]/(a[j]-a[i]),
            (j,j):a[j]/(a[i]-a[j])} for i,j in edges]
    def raw(e,f,root):
        i,j=e;k,l=f
        if i==k or j==l:return S.Integer(0)
        union={i,j,k,l}
        if root not in union:return S.Integer(0)
        value=(-a[root])**(len(union)-2)
        for vertex in union-{root}:value/=a[vertex]-a[root]
        return value
    matrices=[S.Matrix([[sum(c*d*raw(e,f,root) for e,c in u.items() for f,d in v.items())
                     for v in basis] for u in basis]) for root in range(m)]
    B=S.Matrix(two_channel_embedding(m))
    r=2*m-1;n=len(edges)
    rows=[]
    for matrix in matrices[:-1]:
        P=matrix*B
        for c in range(r):
            for d in range(c,r):
                row=[S.Integer(0)]*(n*r)
                for u in range(n):
                    row[u*r+c]+=P[u,d]
                    row[u*r+d]+=P[u,c]
                den=S.ilcm(*[x.q for x in row])
                rows.append([int(x*den) for x in row])
    J=S.Matrix(rows)
    ker=J.nullspace()
    out=[]
    for v in ker:
        den=S.ilcm(*[x.q for x in v])
        ints=[int(x*den) for x in v]
        gcd=math.gcd(*ints)
        ints=[x//gcd for x in ints]
        out.append({str(edge):ints[u*r:(u+1)*r] for u,edge in enumerate(edges)})
    return {"m":m,"a":list(map(int,a)),"dimension":J.rows,
            "right_kernel_dimension":len(ker),"right_kernel_by_edge":out}
records=[]
for m in map(int,sys.argv[1:] or [3,4]):
    value=data(m);records.append(value);print(json.dumps(value),flush=True)
path=Path(__file__).parents[1]/"obstructions/structured_boundary_right_kernels.json"
path.write_text(json.dumps({"date_utc":datetime.now(timezone.utc).isoformat(),
  "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
  "scope":"Exact finite rational nullspaces of the displayed boundary tensor; no uniform uniqueness claim.",
  "records":records},indent=2)+"\n")

