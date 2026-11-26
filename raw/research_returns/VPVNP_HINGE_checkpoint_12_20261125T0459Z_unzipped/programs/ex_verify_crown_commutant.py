"""Independent integer audit of PG-CAUCHY-COMMUTANT.

Builds tensors by internal edge assignments, rather than evaluating boundary
epsilon products. Computes quotient arrays by accumulating sparse support,
and determinants by their permutation expansions. No source checker imports.
"""
from itertools import permutations, product
from pathlib import Path
import json
import os

ROOT = Path(__file__).resolve().parents[1]
PERMS = list(permutations(range(3)))
COEFF = [-1, 1, 1, -1, -1, 1]
ROWS = [[260,266,278,284,290,302], [98,104,116,122,128,140],
        [44,50,143,149,155,248], [53,86,125,158,191,230],
        [65,89,137,161,185,233], [69,93,141,165,189,237]]


def port(vertex, neighbour):
    return sorted(set(range(3)) - {vertex}).index(neighbour)


def expand_edges(edges):
    tensor = {}
    for labels in product((0, 1), repeat=len(edges)):
        coordinate = [0] * 6
        for (a, ap, b, bp), bit in zip(edges, labels):
            coordinate[a] |= bit << ap
            coordinate[b] |= (1-bit) << bp
        key = tuple(coordinate)
        tensor[key] = tensor.get(key, 0) + (-1)**sum(labels)
    return tensor


target_edges = [(side+i, port(i,j), side+j, port(j,i))
                for side in (0,3) for i in range(3) for j in range(i+1,3)]
target = expand_edges(target_edges)
crowns = []
for sigma in PERMS:
    edges = [(i, port(i,ell), 3+sigma[ell], port(sigma[ell],sigma[i]))
             for i in range(3) for ell in range(3) if i != ell]
    crowns.append(expand_edges(edges))


def quotient(tensor, retained, swap=False):
    result = [0] * 972
    for coordinate, value in tensor.items():
        index = 0
        for party, entry in enumerate(coordinate):
            if party == retained:
                if swap:
                    entry = 2*(entry & 1) + (entry >> 1)
                index = 4*index + entry
            else:
                index = 3*index + (entry & 1) + (entry >> 1)
        result[index] += value
    return result


def determinant(matrix):
    total = 0
    for p in permutations(range(len(matrix))):
        sign = (-1)**sum(p[i] > p[j] for i in range(len(p))
                         for j in range(i+1,len(p)))
        term = sign
        for i, j in enumerate(p):
            term *= matrix[i][j]
        total += term
    return total


sectors = []
for retained, rows in enumerate(ROWS):
    q = [quotient(t, retained) for t in crowns]
    h = quotient(target, retained)
    errors = [sum(c*t[i] for c,t in zip(COEFF,q))-h[i]
              for i in range(972)]
    assert not any(errors)
    differences = [[a-b for a,b in zip(quotient(t,retained,True), qt)]
                   for t,qt in zip(crowns,q)]
    minor = [[column[i] for column in differences] for i in rows]
    det = determinant(minor)
    assert det == (-1)**retained
    sectors.append({'retained_party': retained, 'rows': rows,
                    'determinant': det, 'matrix': minor,
                    'exact_coordinates_checked': 972})

coordinate = (0,0,1,1,3,3)
h = target.get(coordinate,0)
bare = sum(c*t.get(coordinate,0) for c,t in zip(COEFF,crowns))
assert (h,bare) == (0,1)
output = {'status':'PASS', 'construction':'independent internal-edge expansion',
          'sectors':sectors, 'bare_failure':{'coordinate':coordinate,
          'target':h, 'bare_sum':bare},
          'scope':'Six prescribed crowns; one product of local span{I,SWAP} maps per crown. Every field, by integral unit minors.'}
path = ROOT/'outputs/ex_crown_commutant_independent.json'
temporary = path.with_name(path.name+'.atomic_tmp')
with temporary.open('w') as f:
    json.dump(output,f,indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())
os.replace(temporary,path)
print(json.dumps({'status':'PASS','exact_quotient_coordinates':6*972,
                  'unit_minors':[s['determinant'] for s in sectors],
                  'bare_target':h,'bare_sum':bare}))
