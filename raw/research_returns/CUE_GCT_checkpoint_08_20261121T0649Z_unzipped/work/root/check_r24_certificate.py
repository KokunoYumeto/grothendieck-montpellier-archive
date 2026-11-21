#!/usr/bin/env python3
"""Root verification of the explicit m=17 maximal permanent Jacobian minor.

The author separately regenerated every entry by subset DP and by Ryser's
formula. Here a different fraction-free modular determinant computation checks
the compact selected minor, while all row/column scaling identities are tested
against the complete stored evaluation matrix. No generic-m conclusion follows.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import numpy as np

base=Path(__file__).resolve().parents[2]
root=base/'work/rectangular/permanent_maximal'
d=json.loads((root/'permanent_range_n17.json').read_text())
p=d['prime'];m=d['n'];r=d['rank'];q=4*m*m
assert (p,m,r,q)==(101,17,1124,1156)
state=20261121+1009*m
co=[]
for _ in range(q):
    state=(1664525*state+1013904223)&0xffffffff
    co.append((state>>16)%p)
assert co==d['pencil_coefficients_flat_i_j_k']
pts=[]
for a in range(m,-1,-1):
    for b in range(m-a,-1,-1):
        for c in range(m-a-b,-1,-1):
            pts.append([a,b,c,m-a-b-c])
assert pts==d['evaluation_points']
raw=(root/'permanent_range_n17.u8').read_bytes()
A=np.frombuffer(raw,dtype=np.uint8).reshape(len(pts),q).astype(np.int64)
excluded={68*i+67 for i in range(1,16)}|{1091+4*j for j in range(17)}
cols=[j for j in range(q) if j not in excluded]
assert cols==d['selected_columns_zero_based']
assert sorted(d['selected_rows_zero_based_in_minor_order'])==list(range(r))
B=A[:r,cols].copy()
started=time.monotonic();prev=1;sign=1
for k in range(r-1):
    if not B[k,k]:
        candidates=np.flatnonzero(B[k+1:,k])
        assert len(candidates),'singular selected minor'
        j=k+1+int(candidates[0]);B[[k,j]]=B[[j,k]];sign=-sign
    pivot=int(B[k,k])
    B[k+1:,k+1:]=((pivot*B[k+1:,k+1:]-B[k+1:,k,None]*B[None,k,k+1:])*pow(prev,-1,p))%p
    B[k+1:,k]=0
    prev=pivot
det=sign*int(B[-1,-1])%p
assert det==88
coeff=np.array(co,dtype=np.int64).reshape(m,m,4)
relations=[]
for i in range(1,m):
    v=np.zeros_like(coeff);v[i]=coeff[i];v[0]=-coeff[0];relations.append(v.reshape(-1)%p)
for j in range(1,m):
    v=np.zeros_like(coeff);v[:,j]=coeff[:,j];v[:,0]=-coeff[:,0];relations.append(v.reshape(-1)%p)
K=np.array(relations,dtype=np.int64)
assert np.all((A@K.T)%p==0)
rank=0;C=K.copy()
for j in range(q):
    candidates=np.flatnonzero(C[rank:,j])
    if not len(candidates):continue
    k=rank+int(candidates[0]);C[[rank,k]]=C[[k,rank]]
    C[rank]=C[rank]*pow(int(C[rank,j]),-1,p)%p
    C[rank+1:]=(C[rank+1:]-C[rank+1:,j,None]*C[None,rank])%p
    rank+=1
    if rank==len(C):break
assert rank==2*m-2
out={'checked_utc':datetime.now(timezone.utc).isoformat(),'who':'GPT-6 Astra Pro; root; effort not exposed; CUE_GCT_20261121_R1','status':'PASS','n':m,'prime':p,'rank':r,'increasing_row_column_minor_mod_prime':det,'determinant_method':'fraction-free Bareiss recurrence reduced modulo101, with explicit row-swap signs','lcg_and_all_evaluation_points_reconstructed':True,'old_scaling_relations_checked_on_complete_matrix':2*m-2,'old_relation_rank':rank,'matrix_sha256':hashlib.sha256(raw).hexdigest(),'certificate_sha256':hashlib.sha256((root/'permanent_range_n17.json').read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-started,'scope':'Independent selected-minor and gauge-kernel verification. All-entry Ryser verification is a separately recorded author computation; not repeated or relabelled here.'}
(base/'work/root/r24_certificate_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
