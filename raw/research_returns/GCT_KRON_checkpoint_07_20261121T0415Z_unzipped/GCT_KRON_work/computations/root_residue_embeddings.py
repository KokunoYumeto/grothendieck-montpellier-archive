"""Finite exploratory comparisons of structured embeddings; no uniform theorem."""
import sys,json,datetime
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'agents/jet_review'))
from structured_residue_tensor import residue_matrix,quadratic_jacobian,rank_tool
p=1000003;rank=rank_tool();results=[]
for m in [3,4,5]:
 a=list(range(1,m+1));E=[(i,j) for i in range(m) for j in range(m) if i!=j];S=[residue_matrix(a,i,p) for i in range(m)];r=2*m-1
 for variant in ['rowcol','commutator_rowcol','weighted_rowcol','scaled_oriented','rowcol_2']:
  emb=[]
  for i,j in E:
   v=[0]*r
   if variant=='rowcol':
    v[i]=1
    if j<m-1:v[m+j]=1
   elif variant=='rowcol_2':
    v[i]=1
    if j<m-1:v[m+j]=2
   elif variant=='commutator_rowcol':
    v[i]=a[j]-a[i]
    if j<m-1:v[m+j]=a[j]-a[i]
   elif variant=='weighted_rowcol':
    v[i]=a[j]
    if j<m-1:v[m+j]=a[i]
   elif variant=='scaled_oriented':
    if i<j:v[i]=a[j]-a[i];v[j]=2*(a[j]-a[i])
    else:
     v[m+j]=a[j]-a[i]
     if i<m-1:v[m+i]=2*(a[j]-a[i])
   emb.append([z%p for z in v])
  J=quadratic_jacobian(S,emb,p);rr=rank(J,p)[0];res={'m':m,'embedding':variant,'rank':rr,'target':len(J)};results.append(res);print(res,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exploratory finite ranks only','results':results},indent=2)+'\n')
