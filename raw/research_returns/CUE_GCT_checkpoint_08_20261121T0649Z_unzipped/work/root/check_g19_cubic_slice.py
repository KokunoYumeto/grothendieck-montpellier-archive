#!/usr/bin/env python3
"""Find and certify one small smooth five-variable slice of per_3.

The certificate is a full-row-rank degree-six Macaulay matrix of the five
quadratic partial derivatives. Its nonzero selected210minor modulo101 proves
smoothness over C without evaluating the degree80 discriminant.
"""
from pathlib import Path
from datetime import datetime,timezone
from itertools import permutations
import hashlib,json
import numpy as np
import sympy as sp

base=Path(__file__).resolve().parents[2]
out=base/'work/root/g19_cubic';out.mkdir(exist_ok=True)
x=sp.symbols('x0:5');p=101
coeff=np.array([[[0,1,1,1,0],[0,0,1,1,0],[0,0,0,1,1]],[[1,0,1,0,1],[1,0,0,1,0],[1,1,0,0,1]],[[0,0,1,1,0],[0,1,0,1,0],[1,1,1,0,0]]],dtype=np.int64)
def compositions(total,k):
    if k==1:
        return [(total,)]
    return [(a,)+b for a in range(total,-1,-1) for b in compositions(total-a,k-1)]
rows=compositions(6,5);mults=compositions(4,5);index={a:i for i,a in enumerate(rows)}
def polynomial(c):
    A=[[sum(int(c[i,j,k])*x[k] for k in range(5)) for j in range(3)]for i in range(3)]
    return sp.Poly(sp.expand(sum(sp.prod(A[i][s[i]] for i in range(3)) for s in permutations(range(3)))),*x)
def macaulay(c):
    f=polynomial(c);grads=[f.diff(z) for z in x];M=np.zeros((210,350),dtype=np.int64)
    for j,g in enumerate(grads):
        for z,b in enumerate(mults):
            for a,v in g.terms():
                target=tuple(ai+bi for ai,bi in zip(a,b));M[index[target],70*j+z]=int(v)%p
    return f,M
def select_minor(M):
    A=M.copy();rank=0;columns=[];det=1
    for j in range(A.shape[1]):
        cand=np.flatnonzero(A[rank:,j])
        if not len(cand):continue
        k=rank+int(cand[0])
        if k!=rank:A[[k,rank]]=A[[rank,k]];det=-det
        pivot=int(A[rank,j]);det=det*pivot%p
        A[rank]=A[rank]*pow(pivot,-1,p)%p
        A[rank+1:]=(A[rank+1:]-A[rank+1:,j,None]*A[None,rank])%p
        columns.append(j);rank+=1
        if rank==len(A):break
    return rank,columns,det%p
f,M=macaulay(coeff);assert select_minor(M)[0]==210
attempts=[]
for loc in list(zip(*np.nonzero(coeff))):
    test=coeff.copy();test[loc]=0
    tf,TM=macaulay(test);rank,_,_=select_minor(TM)
    attempts.append({'entry':list(map(int,loc)),'rank_after_removal':rank})
    if rank==210:coeff=test;f=tf;M=TM
rank,cols,det=select_minor(M);assert rank==210
raw=M.astype(np.uint8).tobytes();(out/'macaulay_degree6.u8').write_bytes(raw)
certificate={'checked_utc':datetime.now(timezone.utc).isoformat(),'who':'GPT-6 Astra Pro; root; effort not exposed; CUE_GCT_20261121_R1','prime':p,'pencil_coefficients_i_j_k':coeff.tolist(),'permanent':str(f.as_expr()),'degree6_row_monomials':rows,'degree4_multiplier_monomials':mults,'column_order':'70*j+b, derivative indexj0..4 and decreasing-lex degree4 multiplier indexb','matrix_shape':[210,350],'matrix_encoding':'row-major uint8, entries0..100','rank':rank,'selected_columns_zero_based':cols,'selected_minor_determinant_mod101':det,'matrix_sha256':hashlib.sha256(raw).hexdigest(),'greedy_sparsification_attempts':attempts,'conclusion':'Every degree6 monomial belongs to the gradient ideal after localization away from the selected integer determinant; no nonzero common projective zero overC. Thus the displayed per3 slice is smooth.','limitations':'This is one explicit five-variable cubic slice, not a general-size search or a discriminant coefficient computation.'}
(out/'certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps({k:v for k,v in certificate.items() if k not in ['degree6_row_monomials','degree4_multiplier_monomials','selected_columns_zero_based','greedy_sparsification_attempts']}))
