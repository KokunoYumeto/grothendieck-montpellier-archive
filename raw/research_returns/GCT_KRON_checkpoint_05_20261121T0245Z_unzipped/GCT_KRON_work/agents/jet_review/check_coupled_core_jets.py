"""Direct full-matrix cofactor certificates for M016 and F023."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from math import isqrt,comb
import json,hashlib

source=Path(__file__).parents[1]/'formulas/check_shared_core_jets.py'
ns={}
exec(source.read_text().split('\nrecords = []')[0],ns)
sp=ns['sp']; build=ns['build']; minor_engine=ns['minor_engine']; indices=ns['indices']

def independent_columns(columns,dim):
    basis={}; chosen=[]; pivot_values=[]
    for col_id,vec in enumerate(columns):
        v={i:Fraction(int(x)) for i,x in enumerate(vec) if x}
        while v:
            p=min(v)
            if p not in basis:
                val=v[p];pivot_values.append(str(val))
                basis[p]={j:x/val for j,x in v.items()}
                chosen.append(col_id)
                break
            val=v[p]
            for j,x in basis[p].items():
                y=v.get(j,0)-val*x
                if y:v[j]=y
                elif j in v:del v[j]
        if len(basis)==dim:break
    return len(basis),chosen,pivot_values

records=[]
for r,ell in [(4,1),(5,1)]:
    R=r-1;h=isqrt(r-1)+1;b=2*ell+2
    local,z,node,fixed=build(R,ell);L=local.rows;N=h*L
    B=sp.zeros(N)
    for a in range(h):B[a*L:(a+1)*L,a*L:(a+1)*L]=local
    slots=[(a,c) for a in range(h) for c in range(h) if (a,c)!=(h-1,h-1)]
    C=sp.zeros(h)
    for v,(a,c) in zip(z,slots):B[a*L,c*L]+=v;C[a,c]=v
    targets=indices(R,b);position={v:i for i,v in enumerate(targets)}
    s=sum(z[i]*z[(i+1)%R] for i in range(R))
    for signed,name in [(True,'determinant'),(False,'permanent')]:
        A=sp.eye(N)+(-B if signed else B)
        value,bits=minor_engine(A,signed)
        W=sp.eye(h)+(-C-s*sp.eye(h) if signed else C+s*sp.eye(h))
        wvalue,wbits=minor_engine(W,signed)
        assert sp.expand(value(bits,bits)-wvalue(wbits,wbits))==0
        cols=[];digest=hashlib.sha256();cofactors=0
        for i in range(N):
            for j in range(N):
                if (i,j)==(fixed,fixed):continue
                cof=value(bits^(1<<i),bits^(1<<j))
                if signed:cof*=(-1)**(i+j)
                cof=sp.expand(cof);cofactors+=1
                digest.update(str((i,j,cof)).encode())
                poly=sp.Poly(cof,*z)
                terms=[(exp,int(c)) for exp,c in poly.terms() if sum(exp)<=b]
                for u in range(R+1):
                    column=[0]*len(targets)
                    for exp,c in terms:
                        if u:
                            e=list(exp);e[u-1]+=1;e=tuple(e)
                        else:e=exp
                        if e in position:column[position[e]]+=c
                    cols.append(column)
        rank,selected,pivots=independent_columns(cols,len(targets))
        assert rank==len(targets)==comb(R+b,b)
        records.append({'r':r,'ell':ell,'h':h,'matrix_size':N,'jet_order':b,'polynomial':name,'exact_rational_Jacobian_rank':rank,'target_dimension':len(targets),'source_columns':len(cols),'direct_full_matrix_cofactors':cofactors,'fixed_nonal_root_diagonal_avoided':True,'independent_column_indices':selected,'elimination_pivots':pivots,'cofactor_sha256':digest.hexdigest()})
        print(json.dumps({k:records[-1][k] for k in ('r','matrix_size','polynomial','exact_rational_Jacobian_rank')}),flush=True)
result={'findings':['M-016','F-023'],'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','status':'PASS','method':'Every matrix-entry cofactor evaluated by signed/unsigned sparse permutation recursion; exact Fraction column elimination gives full target rank. Distinguished nonroot diagonal held fixed. Finite checks supplement the general written proof.','records':records}
p=Path(__file__).with_name('coupled_core_jet_certificate.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(str(p),flush=True)
