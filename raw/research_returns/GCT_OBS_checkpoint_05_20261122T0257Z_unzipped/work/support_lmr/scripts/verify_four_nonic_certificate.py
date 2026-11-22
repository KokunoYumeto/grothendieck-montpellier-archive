#!/usr/bin/env python3
"""Complete standard-library verification of S011, the nonic a4 gate.

The four integral bracket expressions are written explicitly below.
Rebuild their polarized coefficients on x2^2*ternary septics, their
evaluation on an explicit translated9x9 determinant, the24-term ambient
character upper bound, and the resulting nonzero4x4 minor.

No pickle cache or exploratory matrix is trusted.  Optional --resume
accepts scalar coefficient records only when every source hash, symbol,
point or monomial target agrees.  Default execution recomputes everything.
"""
import argparse
from collections import defaultdict
import hashlib
from itertools import permutations
import json
from math import factorial,prod
from pathlib import Path
import time

import check_equal_tail_stabilization as characters
import check_nonic_a4_ternary_slice as ternary
import evaluate_four_nonic_sparse as sparse
import explore_four_nonic_covariants as ambient

P=101
ROOT=Path(__file__).resolve().parents[1]
SYMBOLS=[
 [((0,1,2,3),4),((0,1,4,5),4),((0,2,3,4),1),((2,3,4,5),3),
  ((1,2),1),((3,5),1),((4,5),1)],
 [((0,1,2,3),4),((0,1,2,4),1),((0,1,4,5),3),((0,2,3,4),1),((2,3,4,5),3),
  ((1,5),1),((3,5),1),((4,5),1)],
 [((0,1,2,3),3),((0,1,4,5),3),((0,2,3,4),3),((1,2,4,5),1),((2,3,4,5),2),
  ((1,5),2),((3,5),1)],
 [((0,1,2,3),3),((0,1,2,4),2),((0,1,4,5),3),((0,2,3,4),1),
  ((1,2,3,5),1),((2,3,4,5),2),((3,5),2),((4,5),1)],
]
POINTS=[
 [[93,13,44],[97,40,38],[63,76,74],[85,14,99],[52,42,35],[25,12,10]],
 [[89,42,96],[77,40,46],[78,54,1],[29,20,86],[86,98,95],[90,42,20]],
 [[89,65,6],[69,75,100],[96,67,68],[87,74,78],[33,69,60],[100,32,27]],
]
EXPECTED=[
 [33,50,68,81],
 [59,62,90,99],
 [56,64,34,3],
 [64,40,23,50],
]

def atomic_json(path,data):
    temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data,indent=2)+'\n')
    temporary.replace(path)

def exact_det(matrix):
    return sum(ambient.parity(pi)*prod(matrix[i][pi[i]] for i in range(len(matrix)))
               for pi in permutations(range(len(matrix))))

def ambient_count():
    n=9;d=6;lam=(15,15,12,12);rho=(3,2,1,0);cap=17;base=cap+1
    counts=characters.table(n,cap,d);terms=[]
    for p in permutations(rho):
        sign=(-1)**sum(p[i]<p[j] for i in range(4) for j in range(i+1,4))
        weight=tuple(lam[i]+rho[i]-p[i] for i in range(4))
        x,y,z=weight[1:]
        terms.append(dict(permutation=p,sign=sign,weight=weight,
                          dimension=counts[d][(x*base+y)*base+z]))
    result=sum(t['sign']*t['dimension'] for t in terms)
    assert result==4
    return result,terms

def build_table(symbol,dp):
    core=sparse.core;powers=dict(symbol)
    aa=[];bb=defaultdict(list)
    for key,value in dp[powers[(0,1,4,5)]].items():
        rows=tuple((key>>(core.ROWBITS*i))&core.ROWMASK for i in range(4))
        aa.append((rows,value))
    for key,value in dp[powers[(0,1,2,3)]].items():
        rows=tuple((key>>(core.ROWBITS*i))&core.ROWMASK for i in range(4))
        bb[rows[:2]].append((rows[2],rows[3],value))
    return aa,bb,sparse.small_terms(symbol,dp),dp[powers[(2,3,4,5)]]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--output',type=Path,
                    default=ROOT/'results/four_nonic_verification.json')
    args=ap.parse_args();began=time.monotonic()
    modules=[Path(__file__),Path(characters.__file__),Path(ternary.__file__),
             Path(sparse.__file__),Path(ambient.__file__),Path(sparse.core.__file__),
             Path(sparse.PEER/'explore_three_nonic_join.py')]
    hashes={str(path.relative_to(ROOT.parent)):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in modules}
    cache_dir=ROOT/'results/four_nonic_verification_blocks';cache_dir.mkdir(exist_ok=True)
    for symbol in SYMBOLS:
        assert all(tuple(sorted(edge))==edge and len(set(edge))==len(edge)
                   for edge,power in symbol)
        assert [sum(power for edge,power in symbol if i in edge) for i in range(6)]==[9]*6
        assert sum(power for edge,power in symbol if len(edge)==4)==12
        assert sum(power for edge,power in symbol if len(edge)==2)==3
    g=[[1,1,1,0],[0,0,0,1],[0,1,0,0],[0,0,1,0]]
    assert exact_det(g)==1
    ambient_multiplicity,weight_terms=ambient_count()
    print(json.dumps(dict(stage='ambient',multiplicity=ambient_multiplicity,
                          seconds=time.monotonic()-began)),flush=True)
    ternary_rows=[];common=pow(2*factorial(7),6,P);assert common==37
    for i,symbol in enumerate(SYMBOLS):
        row=[]
        for j,points in enumerate(POINTS):
            path=cache_dir/f'ternary_s{i}_p{j}.json'
            identity=dict(hashes=hashes,symbol=symbol,points=points)
            record=None
            if args.resume and path.exists():
                candidate=json.loads(path.read_text())
                if candidate['identity']==json.loads(json.dumps(identity)):record=candidate
            if record is None:
                value,nonzero=ternary.polarized_value(symbol,points)
                record=dict(identity=identity,unscaled=value,
                            nonzero_ordered_terms=nonzero)
                atomic_json(path,record)
            row.append(record['unscaled']*common%P)
        ternary_rows.append(row)
        print(json.dumps(dict(stage='ternary',symbol=i,values=row,
                              seconds=time.monotonic()-began)),flush=True)
    dp={power:sparse.core.det_power(power) for power in (1,2,3,4)}
    A=(2,2,2,3);E=(3,3,3,0);pattern=(A,)*5+(E,)
    derivative_factor=prod(factorial(a) for m in pattern for a in m)%P
    assert derivative_factor==91
    last=[];sparse_records=[]
    for i,symbol in enumerate(SYMBOLS):
        table=build_table(symbol,dp);powers=dict(symbol)
        joined=max(powers[(0,1,2,3)],powers[(0,1,4,5)])<=3
        outer=sparse.product_groups(table) if joined else None
        total=0;groups=sparse.grouped_targets(pattern,symbol)
        assert sum(count for _,count in groups)==6
        for j,(target,orbit_multiplicity) in enumerate(groups):
            path=cache_dir/f'sparse_s{i}_g{j}.json'
            identity=dict(hashes=hashes,symbol=symbol,target=target,multiplicity=orbit_multiplicity)
            record=None
            if args.resume and path.exists():
                candidate=json.loads(path.read_text())
                if candidate['identity']==json.loads(json.dumps(identity)):record=candidate
            if record is None:
                if joined:value,joins,tested=sparse.coefficient_join(target,table,outer)
                else:value,joins=sparse.core.coefficient(target,table);tested=None
                record=dict(identity=identity,coefficient=value,joins=joins,tested=tested)
                atomic_json(path,record)
            total=(total+orbit_multiplicity*record['coefficient'])%P
            print(json.dumps(dict(stage='sparse',symbol=i,group=j,
                                  coefficient=record['coefficient'],
                                  seconds=time.monotonic()-began)),flush=True)
        last.append(total*derivative_factor%P)
        sparse_records.append(dict(symbol=i,coefficient_sum=total,
                                   differential_value=last[-1],groups=len(groups)))
    matrix=[row+[value] for row,value in zip(ternary_rows,last)]
    assert matrix==EXPECTED
    integer_minor=exact_det(matrix);assert integer_minor%P==21
    result=dict(status='PASS',n=9,degree=6,partition=[15,15,12,12],prime=P,
                ambient=ambient_multiplicity,determinant_rank=4,matrix=matrix,
                integer_minor_of_residue_matrix=integer_minor,minor_mod_prime=21,
                character_terms=weight_terms,sparse_records=sparse_records,
                source_hashes=hashes,seconds=time.monotonic()-began)
    atomic_json(args.output,result)
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ('character_terms','source_hashes')}),flush=True)

if __name__=='__main__':main()
