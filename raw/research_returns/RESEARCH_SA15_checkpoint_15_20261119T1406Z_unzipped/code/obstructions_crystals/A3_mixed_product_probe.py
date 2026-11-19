#!/usr/bin/env python3
"""Exact mixed ordinary/supersingular Cartier matrices; finite probes only.

Eo: y^2+xy=x^3+1, invariant differential dx/x (ordinary).
Es: y^2+y=x^3, invariant differential dx (supersingular).
For N_(a,b)=O_Eo(aO) box O_Es(bO), construct T_s(u)=C(su omega).
Since C(omega)=0, T_s(s)=0.  The dual quotient H0(N)/ks computes
the relative coherent Frobenius.  Generic all-degree sharpness is not
inferred from the finite witnesses below.
"""
import itertools
import json
import random
import time
from pathlib import Path

started = time.perf_counter()

def toggle(out, term):
    if term in out:
        out.remove(term)
    else:
        out.add(term)

def multiply(a, b, ordinary):
    i, j = a
    u, v = b
    if j+v < 2:
        return {(i+u, j+v)}
    if ordinary:
        return {(i+u+1, 1), (i+u+3, 0), (i+u, 0)}
    return {(i+u, 1), (i+u+3, 0)}

def cartier(poly, ordinary):
    out = set()
    for i, j in poly:
        if not j:
            if ordinary and i % 2 == 0:
                toggle(out, (i//2, 0))
            if not ordinary and i % 2:
                toggle(out, ((i-1)//2, 0))
        elif i % 2:
            toggle(out, ((i-1)//2, 1))
            if ordinary:
                toggle(out, ((i-1)//2, 0))
        else:
            toggle(out, (i//2+1, 0))
    return out

def basis(m):
    out = [(i, 0) for i in range(m//2+1)]
    out += [(i, 1) for i in range((m-3)//2+1)]
    assert len(out) == m
    return out

def rank(columns):
    pivots = {}
    for v in columns:
        while v:
            n = v.bit_length()-1
            if n in pivots:
                v ^= pivots[n]
            else:
                pivots[n] = v
                break
    return len(pivots)

def apply(columns, vector):
    out = 0
    while vector:
        bit = vector & -vector
        vector ^= bit
        out ^= columns[bit.bit_length()-1]
    return out

def stable_rank(columns):
    seq = [len(columns)]
    power = columns[:]
    for _ in range(len(columns)+1):
        seq.append(rank(power))
        if seq[-1] == seq[-2]:
            return seq[-1], seq
        power = [apply(columns, c) for c in power]
    raise AssertionError('No stabilization within dimension bound')

def run(a, b, seed, attempts=500):
    first, second = basis(a), basis(b)
    pairs = list(itertools.product(first, second))
    indices = {v:i for i,v in enumerate(pairs)}
    m1 = [[cartier(multiply(c,u,True),True) for u in first] for c in first]
    m2 = [[cartier(multiply(c,u,False),False) for u in second] for c in second]
    coefficients = []
    for c, d in itertools.product(range(a), range(b)):
        coefficients.append([
            sum(1 << indices[(u,v)] for u in m1[c][i] for v in m2[d][j])
            for i, j in itertools.product(range(a), range(b))
        ])
    rng = random.Random(seed)
    best, witness, histogram = -1, None, {}
    target = a*b-(1 if a % 2 else 2)
    for attempt in range(1, attempts+1):
        section = rng.getrandbits(a*b)
        vector = section
        columns = [0]*(a*b)
        while vector:
            bit = vector & -vector
            vector ^= bit
            columns = [x ^ y for x,y in zip(columns,coefficients[bit.bit_length()-1])]
        assert apply(columns,section) == 0
        sr, seq = stable_rank(columns)
        histogram[sr] = histogram.get(sr,0)+1
        if sr > best:
            best = sr
            witness = {'section_bits':section,'columns':columns,'rank_sequence':seq,'attempt':attempt}
        if sr == target:
            break
    return {'a':a,'b':b,'seed':seed,'best_stable_rank':best,'predicted_upper_bound':target,
            'attempts':attempt,'histogram':histogram,'witness':witness}

assert cartier({(0,0)},True) == {(0,0)}
assert cartier({(0,0)},False) == set()
diagonal = [run(3*d,3*d,202611191000+d,200) for d in range(1,7)]
rectangular = [run(a,3,20000+a) for a in range(3,32)]
assert all(r['best_stable_rank']==r['predicted_upper_bound'] for r in diagonal+rectangular)
result = {'status':'finite_probes_complete','scope':'Retained exact finite Cartier witnesses, no inference of uniform odd-degree existence.',
          'ordinary_curve':'y^2+xy=x^3+1 over F2','supersingular_curve':'y^2+y=x^3 over F2',
          'diagonal_degrees_1_through_6':diagonal,'rectangular_b3_a3_through_31':rectangular,
          'elapsed_seconds':time.perf_counter()-started}
destination = Path(__file__).with_name('A3_mixed_product_probe_output.json')
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'diagonal_ranks':[r['best_stable_rank'] for r in diagonal],
                  'rectangular_cases':len(rectangular),'all_predicted_upper_bounds_attained':True,
                  'elapsed_seconds':result['elapsed_seconds']},indent=2))
