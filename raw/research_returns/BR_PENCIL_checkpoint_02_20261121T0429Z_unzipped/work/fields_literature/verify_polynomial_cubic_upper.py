#!/usr/bin/env python3
"""Exact integral upper curves for the polynomial cubic adjacent pencil.

Determinant: 30 pure terms; permanent: 24 pure terms. Both curves are
verified coefficient by coefficient over Z, with no factorial division.
"""
from collections import defaultdict
from itertools import permutations,product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
def target(sign):
    result={}
    for a,last in enumerate((2,3)):
        cols=(0,1,last)
        for row in permutations(range(3)):
            for order in permutations(range(3)):
                word=tuple(4*row[i]+cols[order[i]] for i in range(3))
                result[(a,)+word]=parity(row)*parity(order) if sign==-1 else 1
    return result

def row_atoms(sign):
    # A vector is a list of (coordinate, degree, coefficient) triples.
    e=lambda i:[(i,0,1)]
    if sign==-1:
        atoms=[(-1,1,[[(0,0,1),(2,1,1)],[(0,0,1),(2,1,-1)],[(1,0,1),(2,1,1)]]),
               (-1,-1,[e(0),e(0),e(1)]),
               (-1,1,[[(1,0,1),(2,1,-1)],[(1,0,1),(2,1,1)],[(0,0,1),(2,1,-1)]]),
               (-1,-1,[e(1),e(1),e(0)]),
               (0,-1,[[(0,0,1),(1,0,1)],[(0,0,1),(1,0,-1)],e(2)])]
        return atoms,2
    atoms=[]
    for directions,c in [((),1),((1,),-1),((2,),-1),((1,2),1)]:
        v=e(0)+[(i,1,1) for i in directions]
        atoms.append((-2,c,[v,v,v]))
    return atoms,3

def expand_row(atoms):
    out=defaultdict(int)
    for degree,coeff,factors in atoms:
        for qs in product(*factors):
            word=tuple(q[0] for q in qs);d=degree+sum(q[1] for q in qs);v=coeff
            for q in qs:v*=q[2]
            out[word,d]+=v
    return out

def pencil_atoms(row,s_degree):
    result=[]
    evaluations=[((),[1,1]),((1,),[-1,-1]),((2,),[-1,0]),
                 ((3,),[0,-1]),((1,2),[1,0]),((1,3),[0,1])]
    for degree,coeff,(u,v,w) in row:
        for directions,first in evaluations:
            vector=[(4*r,d,c) for r,d,c in u]
            for col in directions:
                src=v if col==1 else w
                vector.extend((4*r+col,d+s_degree,c) for r,d,c in src)
            result.append({'scalar_degree':degree-2*s_degree,'scalar_coefficient':coeff,
                           'first_factor':first,'vector':vector})
    return result

def main():
    saved={}
    for sign,name,bound in [(-1,'det',30),(1,'per',24)]:
        row,sdegree=row_atoms(sign)
        curve=expand_row(row)
        assert all(not v for (w,d),v in curve.items() if d<0)
        for w in product(range(3),repeat=3):
            expected=(parity(w) if sign==-1 else 1) if len(set(w))==3 else 0
            assert curve[w,0]==expected
        atoms=pencil_atoms(row,sdegree)
        assert len(atoms)==bound
        curve=defaultdict(int)
        for atom in atoms:
            for a in range(2):
                first=atom['first_factor'][a]
                if not first:continue
                for qs in product(atom['vector'],repeat=3):
                    word=(a,)+tuple(q[0] for q in qs)
                    d=atom['scalar_degree']+sum(q[1] for q in qs)
                    value=first*atom['scalar_coefficient']
                    for q in qs:value*=q[2]
                    curve[word,d]+=value
        assert all(not v for (w,d),v in curve.items() if d<0)
        expected=target(sign)
        for w in product(range(2),range(12),range(12),range(12)):
            assert curve[w,0]==expected.get(w,0)
        saved[name]={'upper_bound_all_characteristics':bound,'s_exponent':sdegree,'atoms':atoms}
        print(name,bound,'pure terms; all3456 constant coefficients and all negative powers PASS overZ')
    (HERE/'polynomial_cubic_upper_certificate.json').write_text(json.dumps(saved,indent=2)+'\n')
    print('PASS: determinant upper30 and permanent upper24 in every characteristic')

if __name__=='__main__':main()
