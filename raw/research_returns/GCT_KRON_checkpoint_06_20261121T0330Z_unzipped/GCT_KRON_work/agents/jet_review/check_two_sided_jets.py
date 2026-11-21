"""Direct minor and unit-column certificates for M019 constant bridges."""
from pathlib import Path
from math import isqrt,comb
from itertools import product
from datetime import datetime,timezone
import json,hashlib
ns={}
source=Path(__file__).parents[1]/'formulas/check_shared_core_jets.py'
exec(source.read_text().split('\nrecords = []')[0],ns)
sp=ns['sp'];indices=ns['indices'];minor_engine=ns['minor_engine']

def add(*es):return tuple(map(sum,zip(*es)))
def setup(R,ell,acap,bcap):
 z=sp.symbols(f'z0:{R}');r=R+1;h=isqrt(r-1)+1;core=indices(R,ell);Q=len(core);T=h*Q
 idealA=[(i,)+(0,)*(R-1) for i in range(acap+1)]
 idealB=[(0,i)+(0,)*(R-2) for i in range(bcap+1)]
 N=T*(len(idealA)+len(idealB));Adj=sp.zeros(N);coord={a:i for i,a in enumerate(core)}
 for side in range(2):
  for c in range(h):
   for a in core:
    if not sum(a):continue
    j=max(i for i,v in enumerate(a) if v);p=list(a);p[j]-=1;p=tuple(p)
    u=side*T+c*Q+coord[a];v=side*T+c*Q+coord[p]
    if side:u,v=v,u
    Adj[u,v]=z[j]
 labels=[sp.Integer(1),*z];bridge={}
 for label,(a,c) in zip(labels,product(range(h),repeat=2)):
  u=a*Q;v=T+c*Q;Adj[u,v]=label;bridge[str(label)]=(u,v)
 next_id=2*T;attachments=[]
 for side,ideal in [(0,idealA),(1,idealB)]:
  for root in range(side*T,(side+1)*T):
   node={ideal[0]:root}
   for a in ideal[1:]:node[a]=next_id;next_id+=1
   for a in ideal[1:]:
    j=max(i for i,v in enumerate(a) if v);p=list(a);p[j]-=1;p=tuple(p)
    u,v=node[a],node[p]
    if side:u,v=v,u
    Adj[u,v]=z[j]
   attachments.append((side,root,node))
 assert next_id==N
 gamma=sorted({add(a,b,e) for a in idealA for b in idealB for e in indices(R,2*ell+2)},key=lambda a:(sum(a),a))
 return Adj,z,gamma,T,bridge,attachments

records=[]
for R,ell,acap,bcap in [(2,0,2,2),(3,0,1,1),(2,1,0,0)]:
 Adj,z,target,fixed,bridge,attachments=setup(R,ell,acap,bcap)
 N=Adj.rows;targetset=set(target);dim=len(target)
 for signed,name in [(True,'determinant'),(False,'permanent')]:
  value,bits=minor_engine(sp.eye(N)+(-Adj if signed else Adj),signed)
  assert value(bits,bits)==1
  hit={};digest=hashlib.sha256();cofactor_count=0
  for i in range(N):
   for j in range(N):
    if i==j:continue
    cof=value(bits^(1<<i),bits^(1<<j))
    if signed:cof*=(-1)**(i+j)
    cof=sp.expand(cof);cofactor_count+=1
    digest.update(str((i,j,cof)).encode())
    if cof==0:continue
    terms=sp.Poly(cof,*z).terms()
    assert len(terms)==1 and terms[0][1]==1
    exp=terms[0][0]
    for u in range(R+1):
     e=list(exp)
     if u:e[u-1]+=1
     e=tuple(e)
     if e in targetset and e not in hit:hit[e]=(i,j,u)
  assert len(hit)==dim
  assert len(set(hit.values()))==dim
  # Direct check that both extensions work with the degree-zero core bridge.
  a,c=bridge['1']
  ain=next(node for side,root,node in attachments if side==0 and root==a)
  bout=next(node for side,root,node in attachments if side==1 and root==c)
  alpha=max(ain,key=sum);beta=max(bout,key=sum);u=ain[alpha];v=bout[beta]
  cof=value(bits^(1<<v),bits^(1<<u))
  if signed:cof*=(-1)**(v+u)
  expected=sp.prod(z[i]**(alpha[i]+beta[i]) for i in range(R))
  assert sp.expand(cof-expected)==0
  records.append({'R':R,'ell':ell,'A_chain_cap':acap,'B_chain_cap':bcap,'matrix_size':N,'polynomial':name,'target_dimension':dim,'identity_Jacobian_rank':dim,'all_selected_directions_off_diagonal':True,'constant_bridge_with_both_extensions_checked':True,'direct_offdiagonal_cofactors':cofactor_count,'cofactor_sha256':digest.hexdigest(),'selected_source_coordinates':list(hit.values())})
  print(json.dumps({k:records[-1][k] for k in ('R','ell','matrix_size','polynomial','identity_Jacobian_rank')}),flush=True)
result={'finding':'M-019','date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','status':'PASS','method':'Signed/unsigned full matrix permutation recursion; every off-diagonal minor directly computed, identity Jacobian columns and both extensions on the constant bridge checked. Finite checks supplement the arbitrary-order-ideal proof.','records':records}
p=Path(__file__).with_name('two_sided_jet_certificate.json');p.write_text(json.dumps(result,indent=2)+'\n');print(str(p),flush=True)
