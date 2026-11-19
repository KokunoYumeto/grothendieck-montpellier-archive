"""Exact rational rank in the independently reviewed cubic-period Hodge example."""
from pathlib import Path
import itertools,json
import sympy as s
P=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle')
t=s.symbols('t');f=t**3-2
words=list(itertools.product([0,1],repeat=3))
columns=[]
for w in words:
    r=s.rem(t**sum(w),f,t)
    columns.append([r.coeff(t,j) for j in range(3)])
M=s.Matrix(3,8,lambda i,j:columns[j][i])
K=M.nullspace()
assert s.Poly(f,t).is_irreducible
assert M.rank()==3 and len(K)==5
assert all(M*v==s.zeros(3,1) for v in K)
paired=s.diag(M,M)
assert paired.rank()==6 and len(paired.nullspace())==10
out={'minimal_polynomial':str(f),'irreducible':True,'period_choice':'the root of t^3−2 in the upper half-plane; irreducible also by Eisenstein at2','tensor_basis':words,'projection_matrix':M.tolist(),'rank':M.rank(),'kernel_dimension':len(K),'kernel_basis':[list(v) for v in K],'paired_rank':paired.rank(),'paired_kernel_dimension':len(paired.nullspace()),'scope':'Exact finite-dimensional linear algebra only. The Hodge and restriction-of-scalars argument is supplied in peer_review_C827.md.'}
out=json.loads(json.dumps(out,default=str))
(P/'audit/peer_review_C827.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
