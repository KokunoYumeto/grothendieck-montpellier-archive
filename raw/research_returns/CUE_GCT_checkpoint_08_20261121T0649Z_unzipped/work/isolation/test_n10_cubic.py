"""Exact exploratory test of purity's proposed n10 balanced-cubic ansatz.

The Cauchy ansatz is tested, not asserted to classify all candidates.
"""
from itertools import combinations
from datetime import datetime,timezone
from pathlib import Path
import json
import sympy as s

n=10
nodes=list(map(s.Integer,range(n)))
M=s.Matrix([[a**k for a in nodes] for k in range(3)])
middle=list(range(3,7)); repair=list(range(3,6))
p=s.zeros(1,n)
for i in middle:
    p[i]=1/s.prod(nodes[i]-nodes[j] for j in middle if i!=j)
assert M*p.T==s.zeros(3,1)


def lift(i):
    row=s.zeros(1,n);row[i]=1
    correction=M[:,repair].inv()*(-M[:,i])
    for j,c in zip(repair,correction):row[j]=c
    assert M*row.T==s.zeros(3,1)
    return row


A=[lift(i) for i in range(3)]
B=[lift(j) for j in range(7,10)]
v=s.symbols('v0:3');w=s.symbols('w0:3')
coefficient={}
for subset in combinations(range(n),3):
    wedge=0
    for i in range(3):
        for j in range(3):
            determinant=s.Matrix.vstack(p,A[i],B[j])[:,list(subset)].det()
            wedge+=v[i]*w[j]*determinant/(nodes[i]-nodes[j+7])
    delta=s.prod(nodes[subset[j]]-nodes[subset[i]] for i in range(3) for j in range(i+1,3))
    coefficient[subset]=s.factor(wedge*delta)


def cut_blocks(cut,substitution):
    result=[]
    for degree in range(4):
        left=list(combinations(range(cut),degree))
        right=list(combinations(range(cut,n),3-degree))
        if not left or not right:
            result.append((0,None));continue
        matrix=s.Matrix([[coefficient[tuple(a+b)].subs(substitution) for b in right] for a in left])
        result.append((matrix.rank(),matrix))
    return result


def main():
    one={x:1 for x in v+w}
    ranks=[]
    for cut in range(1,n):
        blocks=cut_blocks(cut,one)
        ranks.append({'cut':cut,'degree_block_ranks':[z[0] for z in blocks],
                      'total_rank':sum(z[0] for z in blocks)})
    nonzero={','.join(map(str,k)):str(value.subs(one)) for k,value in coefficient.items()
             if value.subs(one)!=0}
    report={'time_utc':datetime.now(timezone.utc).isoformat(),
            'ansatz':'p wedge sum v_i w_j/(a_i-a_j) A_i wedge B_j, nodes0..9',
            'ranks_at_all_weights_one':ranks,'nonzero_coefficients':nonzero,
            'p':list(map(str,p)),'A':[list(map(str,a)) for a in A],
            'B':[list(map(str,b)) for b in B],
            'scope':'Exact ansatz test in the displayed order only; no classification or all-order assertion.'}
    target=Path('/workspace/scratch/64674c0aa6e9/work/isolation/n10_cubic_test.json')
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'time_utc':report['time_utc'],'cut_ranks':ranks,
                      'nonzero_coefficients':len(nonzero)}))


if __name__=='__main__':main()
