"""Exact small-rank convention check for the separately proved all-n Lie lemma."""
from collections import defaultdict
from pathlib import Path
import json
from sympy import Matrix

def rank_at(n):
    F=defaultdict(int)
    for i in range(n-1):
        F[(i,i,i+1)]+=1
        F[(i,i+1,i)]-=2
        F[(i+1,i,i)]+=1
    A=[[0]*(n*n) for _ in range(n+n**3)]
    for a in range(n):
        for b in range(n):
            col=a*n+b
            if b==n-1:A[a][col]=1
            for w,c in F.items():
                for j in range(3):
                    if w[j]==b:
                        out=list(w);out[j]=a
                        row=n+out[0]*n*n+out[1]*n+out[2]
                        A[row][col]+=c
    rank=Matrix(A).rank()
    assert rank==n*n
    return {'n':n,'rows':n+n**3,'columns':n*n,'rank_over_Q':rank}

receipts=[rank_at(n) for n in range(2,9)]
out={'status':'PASS','scope':'finite convention checks for the independent all-dimensional proof','receipts':receipts}
(Path(__file__).resolve().parents[2]/'reviews/hook_chain_lie_root_computation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
