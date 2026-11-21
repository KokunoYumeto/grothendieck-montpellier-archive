"""Exact exterior-algebra check for the balanced-RM lattice obstruction.

This verifies the defining contraction identity in a split basis. The
rational descent and p-adic Smith argument are mathematical proofs in S30,
not claims made by this finite computation.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

def wedge(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            if set(i)&set(j): continue
            sign=(-1)**sum(k>l for k in i for l in j)
            key=tuple(sorted(i+j))
            out[key]=out.get(key,Fraction(0))+sign*x*y
    return {i:x for i,x in out.items() if x}

def contract_vector(a,k):
    out={}
    for i,x in a.items():
        if k not in i: continue
        p=i.index(k);j=i[:p]+i[p+1:]
        out[j]=out.get(j,Fraction(0))+(-1)**p*x
    return {i:x for i,x in out.items() if x}

def contract_pair(a,pair):
    return contract_vector(contract_vector(a,pair[0]),pair[1])

top={tuple(range(8)):Fraction(1)}
c={tuple(range(4)):Fraction(1),tuple(range(4,8)):Fraction(1)}
pairs=list(combinations(range(8),2))
diagonal=[]
for pair in pairs:
    actual=wedge(contract_pair(c,pair),c)
    internal=(pair[1]<4 or pair[0]>=4)
    expected=contract_pair(top,pair) if internal else {}
    assert actual==expected,(pair,actual,expected)
    diagonal.append(int(internal))
assert wedge(c,c)=={tuple(range(8)):Fraction(2)}
qdiag=[2*x-1 for x in diagonal]
assert all(x*x==1 for x in qdiag)
assert qdiag==[(1 if i<4 else -1)*(1 if j<4 else -1) for i,j in pairs]
record={'statement':'S-30 split-basis exterior identity',
        'basis_dimension':8,'bivector_dimension':28,
        'contraction_checks':28,'all_exact':True,
        'C_square_top_coefficient':2,
        'P_rank':sum(diagonal),'P_diagonal':diagonal,
        'Q_plus_multiplicity':qdiag.count(1),
        'Q_minus_multiplicity':qdiag.count(-1),
        'Q_involution':True,'wedge_square_T_div_d_identity':True,
        'scope':'Finite exact linear-algebra verification; no proof-assistant or p-adic formalization claimed'}
dest=Path(__file__).resolve().parents[1]/'research/rm_exterior_certificate.json'
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='P_diagonal'}))
