#!/usr/bin/env python3
"""Exhaustive pentagonal search for sqrt(rank) on Mat_3(F_2).
Fix right pair (0,Z); GL_3 x GL_3 reduces Z to diag(I_r,0), r=1,2,3.
Every floating-point operation is avoided in the exhaustive search.
Positive distances use integer upper bounds and negative distances lower
bounds, so a negative reported maximum is a rigorous no-violation bound.
"""
import json
import math
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PARAMS = json.loads((ROOT / 'inputs/ex_pentagon_m3_parameters.json').read_text())
N = PARAMS['dimension']
assert N == 3 and PARAMS['field_order'] == 2
SCALE = PARAMS['integer_scale']

def rank2(bits):
    rows = [(bits >> (N*i)) & ((1 << N)-1) for i in range(N)]
    rank = 0
    for col in range(N):
        pivot = next((i for i in range(rank,N) if (rows[i] >> col) & 1),None)
        if pivot is None: continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        for i in range(N):
            if i != rank and ((rows[i] >> col) & 1): rows[i] ^= rows[rank]
        rank += 1
    return rank

def matrix(bits):
    return [[(bits >> (N*i+j)) & 1 for j in range(N)] for i in range(N)]

ranks = np.array([rank2(x) for x in range(1 << (N*N))],dtype=np.int8)
lo = np.array([math.isqrt(r*SCALE*SCALE) for r in range(N+1)],dtype=np.int64)
hi = lo + np.array([int(x*x != r*SCALE*SCALE) for r,x in enumerate(lo)],dtype=np.int64)
allx = np.arange(1 << (N*N),dtype=np.int64)
results = []
for r in range(1,N+1):
    z = sum(1 << (N*i+i) for i in range(r))
    vertices = allx[(allx != 0) & (allx != z)]
    pairr = ranks[np.bitwise_xor(vertices[:,None],vertices[None,:])]
    pairhi = hi[pairr]
    weightslo = lo[ranks[vertices]] + lo[ranks[np.bitwise_xor(vertices,z)]]
    best = -(1 << 60)
    witness = None
    count = 0
    for i in range(len(vertices)-2):
        inds = np.arange(i+1,len(vertices))
        upper = pairhi[np.ix_(inds,inds)] + pairhi[i,inds][:,None] + pairhi[i,inds][None,:]
        upper = upper - weightslo[inds,None] - weightslo[None,inds] - weightslo[i] + hi[r]
        upper[np.tril_indices(len(inds))] = -(1 << 60)
        flat = int(np.argmax(upper))
        value = int(upper.flat[flat])
        count += len(inds)*(len(inds)-1)//2
        if value > best:
            j,k = np.unravel_index(flat,upper.shape)
            best = value
            witness = [int(vertices[i]),int(vertices[inds[j]]),int(vertices[inds[k]])]
    coeff = [0]*(N+1)
    for i in range(3):
        for j in range(i): coeff[int(ranks[witness[i]^witness[j]])] += 1
        coeff[int(ranks[witness[i]])] -= 1
        coeff[int(ranks[witness[i]^z])] -= 1
    coeff[r] += 1
    exact_lo = sum(c*int(lo[s] if c>=0 else hi[s]) for s,c in enumerate(coeff))
    exact_hi = sum(c*int(hi[s] if c>=0 else lo[s]) for s,c in enumerate(coeff))
    assert exact_hi <= best <= exact_hi + 10
    item = dict(right_rank=r,right_bits=[0,z],left_bits=witness,
        right_matrices=[matrix(0),matrix(z)],left_matrices=[matrix(x) for x in witness],
        total_unordered_left_triples=count,coefficient_by_square_root=coeff,
        rigorous_global_objective_upper_numerator=best,denominator=SCALE,
        witness_objective_lower_numerator=exact_lo,witness_objective_upper_numerator=exact_hi,
        strict_violation_found=bool(exact_lo>0),all_pentagons_nonpositive_certified=bool(best<=0))
    results.append(item)
    print(json.dumps(item),flush=True)
output = dict(parameters=PARAMS,method='exhaustive integer upper bounds after translation and GL3xGL3 orbit reduction',results=results)
(ROOT / 'outputs/ex_pentagon_m3_results.json').write_text(json.dumps(output,indent=2)+'\n')
assert all(x['total_unordered_left_triples'] == math.comb(510,3) for x in results)
