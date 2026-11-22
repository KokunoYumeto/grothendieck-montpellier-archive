#!/usr/bin/env python3
"""Certify why the exploratory n=4 route does not refute fixed-M L3."""
import json
import time
from polygons_certificates import vector_chi, q_from_word
from polygons_l3_search import local_triangles

started = time.perf_counter()
word = [1, 2, 3, 4, -1, -2, -3, -4]
fixed = [(1,0,0), (0,1,0), (0,0,1), (1,1,1)]
other = [(1,t,t*t) for t in range(4)]
q = q_from_word(word)
fixed_triangles = local_triangles(word, vector_chi(fixed), q, 4)
other_triangles = local_triangles(word, vector_chi(other), q, 4)
assert [x['arc'] for x in fixed_triangles] == [[1,2]]
assert [x['arc'] for x in other_triangles] == [[1,2],[4,-1],[-3,-4]]
print(json.dumps({
    'status': 'superseded exploratory route, not a fixed-M L3 counterexample',
    'word': word, 'fixed_base': fixed, 'other_base': other,
    'fixed_base_triangle_count': len(fixed_triangles),
    'fixed_base_triangles': fixed_triangles,
    'other_base_triangle_count': len(other_triangles),
    'other_base_triangles': other_triangles,
    'valid_replacement': 'P5; polygons_l3_verify.py',
    'runtime_seconds': time.perf_counter() - started
}, indent=2))
