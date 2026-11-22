#!/usr/bin/env python3
"""Independent HD-AST07--09 supplement: convolution and actual matrices.

The root proof and full root checker were read before writing this program.
No author code, selected rows, grid-cycle computation or output is imported.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations_with_replacement, permutations
from math import lcm
from pathlib import Path
import json
import time
import sympy as sp

started=time.perf_counter()
here=Path(__file__).resolve().parent
root=here.parents[2]
proof=root/'research/alternating_standard_two_factor_section.tex'
proof_hash=sha256(proof.read_bytes()).hexdigest()
assert proof_hash=='32b5cc512a130b41b5d6f3d8e0d4f2d5fa02e3714ce9d6ba6d6b89d5a4163108'

def partitions(n,bound=None):
    if n==0:
        yield ()
        return
    if bound is None:bound=n
    for k in range(min(n,bound),0,-1):
        for p in partitions(n-k,k):yield (k,)+p

def profile(part):
    order=lcm(*part)
    eigenvalues=Counter()
    for length in part:
        for j in range(length):eigenvalues[j*(order//length)]+=1
    eigenvalues[0]-=1
    return order,{k:v for k,v in eigenvalues.items() if v}

pair_count=spectral_entries=real_target_checks=0
summaries=[]
for n in range(15,19):
    a=n-1;e=a*a
    rows=[(p,*profile(p)) for p in partitions(n)]
    minimum=None
    for left,right in combinations_with_replacement(rows,2):
        p,Lp,P=left;q,Lq,Q=right
        k=2*n-len(p)-len(q)
        if k==0:continue
        order=lcm(Lp,Lq)
        counts={}
        for x,c in P.items():
            xx=x*(order//Lp)
            for y,d in Q.items():
                phase=(xx+y*(order//Lq))%order
                counts[phase]=counts.get(phase,0)+c*d
        assert sum(counts.values())==e
        assert all(counts.get((-x)%order,0)==m for x,m in counts.items())
        moving=e-max(counts.values())
        twice_gap=2*moving-(n-3)*k-n
        assert twice_gap>=0 and 2*moving>=(n-2)*k
        assert sum(m*m for m in P.values())<=(n-2)*len(p)+1
        assert sum(m*m for m in Q.values())<=(n-2)*len(q)+1
        if k<n:
            assert 2*(e-counts.get(0,0))>=(n-3)*k+n
            real_target_checks+=1
            if order%2==0:
                assert 2*(e-counts.get(order//2,0))>=(n-3)*k+n
                real_target_checks+=1
        minimum=twice_gap if minimum is None else min(minimum,twice_gap)
        pair_count+=1;spectral_entries+=len(counts)
    summaries.append({'n':n,'minimum_twice_gap':minimum})

def permutation_from_cycles(part):
    p=[];offset=0
    for length in part:
        p.extend(offset+(j+1)%length for j in range(length))
        offset+=length
    return p

matrix_cases=0;matrix_degrees=[]
for n in range(4,9):
    a=n-1;e=a*a
    swap=sp.zeros(e)
    for i in range(a):
        for j in range(a):swap[j*a+i,i*a+j]=1
    for part in partitions(n):
        p=permutation_from_cycles(part)
        # Actual deleted-letter basis b_i=e_i-e_n, not a spectral formula.
        U=sp.Matrix(a,a,lambda r,c:int(r==p[c])-int(r==p[-1]))
        assert U**lcm(*part)==sp.eye(a)
        T=sp.kronecker_product(U,sp.eye(a))*swap
        assert T*T==sp.kronecker_product(U,U)
        factors=sp.factor_list(T.charpoly().as_expr())[1]
        assert sum(sp.degree(f)*m for f,m in factors)==e
        largest=max(m for _,m in factors)
        moving=e-largest
        index=n-len(part)
        assert 2*moving>=e-a and 2*moving>=e+a*index-2*a
        matrix_cases+=1;matrix_degrees.append(e)

def cycle_lengths(p):
    unseen=set(range(len(p)));out=[]
    while unseen:
        start=min(unseen);v=start;length=0
        while v in unseen:
            unseen.remove(v);v=p[v];length+=1
        assert v==start
        out.append(length)
    return sorted(out)

quotient_cases=0
for n in (2,3,4):
    ps=list(permutations(range(n)))
    for x in ps:
        for y in ps:
            actual=[n+y[i] for i in range(n)]+[x[i] for i in range(n)]
            h=[x[y[i]] for i in range(n)]
            assert cycle_lengths(actual)==[2*d for d in cycle_lengths(h)]
            assert 2*n-len(cycle_lengths(actual))==n+n-len(cycle_lengths(h))
            quotient_cases+=1

u=sp.symbols('u',nonnegative=True)
n=15+u;a=n-1;e=a*a
assert sp.expand(e+(n-3)*(n-1)+5*n-2*(n-1)-(2*e+a+5))==0
assert sp.expand(a+5-6)==u+13
assert sp.expand(6*a-6)==6*u+78
assert sp.expand((e-a)/2-a).as_poly(u).all_coeffs()==[sp.Rational(1,2),sp.Rational(25,2),77]

out={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-started,'proof_sha256':proof_hash,
     'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'partition_pairs':pair_count,'convolution_spectral_entries':spectral_entries,
     'low_index_real_target_checks':real_target_checks,'minimum_gaps':summaries,
     'actual_deleted_basis_weighted_matrices':matrix_cases,
     'matrix_degree_range':[min(matrix_degrees),max(matrix_degrees)],
     'actual_two_block_quotient_actions':quotient_cases,
     'universal_symbolic_identities':4,
     'scope':'Independent spectral convolution, actual rational deleted-basis matrices and quotient permutations. Full universal Cauchy/parity/actual-cover proof checked separately. Root code was read first, none imported.'}
(here/'audit_standard_two_factor.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
