#!/usr/bin/env python3
"""Direct exact verifier of P5; no search or floating-point arithmetic."""
from itertools import combinations
import json
import time
from polygons_certificates import vector_chi, q_from_word, combined_chi, basis_exchange, det
from polygons_l3_search import local_triangles, gp_failure

start = time.perf_counter()
vectors = [(1, t, t*t) for t in range(6)]
chi = vector_chi(vectors)
assert all(det(*(vectors[i] for i in t)) > 0 for t in combinations(range(6), 3))
word = [1, 2, -3, -4, -6, -5, -1, -2, 3, 4, 6, 5]
assert len(set(word)) == 12 and sorted(abs(x) for x in word) == sorted(list(range(1,7))*2)
assert all(word[i+6] == -word[i] for i in range(6))
q = q_from_word(word)
triangles = local_triangles(word, chi, q, 6)
assert [t['arc'] for t in triangles] == [[2,-3],[-1,-2],[3,4]]
arcs = [word.index(t['arc'][0]) for t in triangles]
corner_weights = [(arcs[(j+1)%3]-(arcs[j]+1))%12 for j in range(3)]
assert corner_weights == [4,1,4]
assert sum(corner_weights)+3 == 12
ext = combined_chi(chi,q,6)
terms = [ext(4,0,2)*ext(4,5,6), -ext(4,0,5)*ext(4,2,6), ext(4,0,6)*ext(4,2,5)]
assert terms == [-1,-1,-1]
full = basis_exchange(ext,range(7))
assert not full['valid']
print(json.dumps({'id':'P5','verified':True,'vectors':vectors,'word':word,
    'q': {f'{i+1}{j+1}':q(i,j) for i,j in combinations(range(6),2)},
    'triangles':triangles,'arrow_weights':[1,1,1],'corner_weights':corner_weights,
    'weight_sum':12,'gp_terms':terms,'full_basis_exchange_failure':full,
    'runtime_seconds':time.perf_counter()-start},indent=2))
