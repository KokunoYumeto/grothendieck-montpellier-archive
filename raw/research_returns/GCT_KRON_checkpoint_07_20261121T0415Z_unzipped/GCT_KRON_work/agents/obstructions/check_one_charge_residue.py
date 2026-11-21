"""One-charge residue embedding and an independently derived gradient normal form."""
from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,sys
source=Path(__file__).parents[1]/"jet_review/structured_residue_tensor.py"
spec=importlib.util.spec_from_file_location("structured",source)
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
prime=1000003
rank=s.rank_tool()
def multiply(f,g):
    ans=[0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):ans[i+j]=(ans[i+j]+x*y)%prime
    return ans
def delta(a,excluded):
    f=[1]
    for i,x in enumerate(a):
        if i not in excluded:f=multiply(f,[x,1])
    return f
def residue(f,a,i):
    x=-a[i];v=0
    for c in reversed(f):v=(v*x+c)%prime
    den=1
    for j,y in enumerate(a):
        if j!=i:den=den*(y-a[i])%prime
    return v*pow(den,-1,prime)%prime
records=[]
for m in map(int,sys.argv[1:] or [3,4,5,6]):
    a=list(range(1,m+1));r=2*m-1
    edges,_=s.kernel_basis(a,prime)
    B=[]
    for i,j in edges:
        row=[0]*r;row[i]+=1;row[j]+=1
        if i<m-1:row[m+i]+=1
        if j<m-1:row[m+j]-=1
        row[m-1]+=1 if i<j else -1
        B.append([x%prime for x in row])
    mats=[s.residue_matrix(a,i,prime) for i in range(m)]
    e=[]
    for i in range(m):
        row=[0]*r;row[i]=-2
        for j in range(m):
            if i==j:continue
            c=2*a[i]*pow(a[j]-a[i],-1,prime)%prime
            row[i]+=c;row[j]+=c
        e.append([x%prime for x in row])
    comparisons=0
    for edge_index,(i,j) in enumerate(edges):
        lo,hi=sorted((i,j));A=a[lo];C=a[hi];D=C-A;iv=pow(D,-1,prime)
        f=delta(a,{lo,hi})
        P=[(k+1)*x%prime for k,x in enumerate(f)]
        Q=f[:]
        for mid in range(lo+1,hi):
            g=delta(a,{lo,hi,mid})
            for k,x in enumerate(g):Q[k+1]=(Q[k+1]+2*x)%prime
        alpha=(A+C)*iv%prime
        beta=[(C*x-A*y)*iv%prime for x,y in zip(e[lo],e[hi])]
        orientation=1 if i<j else -1
        for root in range(m):
            rp=residue(P,a,root);rf=residue(f,a,root);rq=residue(Q,a,root)
            predicted=[-rf*x%prime for x in beta]
            predicted[lo]-=alpha*rp;predicted[hi]+=alpha*rp
            if lo<m-1:predicted[m+lo]-=orientation*rp
            if hi<m-1:predicted[m+hi]+=orientation*rp
            predicted[m-1]-=orientation*rq
            predicted=[x%prime for x in predicted]
            actual=[sum(mats[root][edge_index][v]*B[v][c] for v in range(len(edges)))%prime for c in range(r)]
            assert actual==predicted,(m,(i,j),root,actual,predicted)
            comparisons+=r
    J=s.quadratic_jacobian(mats,B,prime)
    rk,columns,res=rank(J,prime)
    record={"m":m,"a":a,"dimension":len(J),"rank":rk,
            "normal_form_entries_compared":comparisons,
            "normal_form_match":True,"selected_minor_mod_prime":res,
            "embedding_free_edge_coefficients":B,
            "selected_columns":columns,
            "scope":"Finite rational-parameter nonvanishing modulo a prime; no general-m rank theorem."}
    records.append(record)
    print({k:v for k,v in record.items() if k not in ["embedding_free_edge_coefficients","selected_columns"]},flush=True)
result={"date_utc":datetime.now(timezone.utc).isoformat(),
        "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
        "prime":prime,"candidate":"B_ij=p_i+p_j+q_i-q_j+sgn(j-i)*p_m, q_m=0",
        "method":"Direct raw-residue tensor versus independent row/column-scaling normal form, followed by complete square Jacobian elimination.",
        "records":records}
Path(__file__).with_name("one_charge_residue_certificate.json").write_text(json.dumps(result,indent=2)+"\n")

