#!/usr/bin/env python3
"""Bounded rational matrix checks for DC.5; the universal proof is in the text."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
from itertools import combinations
import sympy as s
import json

start = perf_counter()
started = datetime.now(timezone.utc).isoformat()
base = Path(__file__).resolve().parents[1]
rows = []

def data(M):
    return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

cases = [
    ('one_triangle',3,[(0,1,2)]),
    ('two_triangles',4,[(0,1,2),(1,2,3)]),
    ('tetrahedron_missing_face',4,[(0,1,2),(0,1,3),(0,2,3)]),
    ('fan',6,[(0,1,2),(0,2,3),(0,3,4),(0,4,5)]),
    ('disjoint_faces',6,[(0,1,2),(3,4,5)]),
]
for name,n,faces in cases:
    edges = sorted(set(e for face in faces for e in combinations(face,2)))
    D = s.zeros(len(faces),len(edges))
    d0 = s.zeros(len(edges),n)
    for j,(a,b) in enumerate(edges):
        d0[j,a] = -1
        d0[j,b] = 1
    for i,face in enumerate(faces):
        for omit in range(3):
            edge = tuple(v for j,v in enumerate(face) if j!=omit)
            D[i,edges.index(edge)] = (-1)**omit
    R = D.T*(D*D.T).inv()
    good = D.rank()==len(faces) and D*d0==s.zeros(len(faces),n) and D*R==s.eye(len(faces))
    rows.append({'name':name,'passed':bool(good),'faces':faces,'edges':edges,
                 'delta':data(D),'right_inverse':data(R),'H2_dimension':len(faces)-D.rank()})
    for coefficient_dimension in (1,2,3):
        I=s.eye(coefficient_dimension)
        ok=s.kronecker_product(D,I)*s.kronecker_product(R,I)==s.eye(len(faces)*coefficient_dimension)
        rows.append({'name':name+f'_coefficient_dimension_{coefficient_dimension}','passed':bool(ok)})

# Negative controls: the proof must not silently use a right inverse when H2 is nonzero.
for name,faces in [('full_tetrahedron',list(combinations(range(4),3))),
                   ('two_faces_same_boundary',[(0,1,2),(0,1,2)])]:
    edges=sorted(set(e for face in faces for e in combinations(face,2)))
    D=s.zeros(len(faces),len(edges))
    for i,face in enumerate(faces):
        for omit in range(3):
            edge=tuple(v for j,v in enumerate(face) if j!=omit)
            D[i,edges.index(edge)]=(-1)**omit
    h2=len(faces)-D.rank()
    rows.append({'name':name+'_excluded_nonzero_H2','passed':bool(h2==1),
                 'delta':data(D),'H2_dimension':h2,'right_inverse_claimed':False})

record={'statement':'C.3bs','started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':perf_counter()-start,
        'scope':'Finite rational dual-cochain/right-inverse and tensor-coefficient identities only. No K-theory descent, generic geometry, actual family existence or universal theorem is inferred from these samples.',
        'checks':rows,'summary':{'passed':sum(x['passed'] for x in rows),
                                'failed':sum(not x['passed'] for x in rows),'total':len(rows)}}
(base/'output/dual_component_lifting_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if record['summary']['failed']:
    raise SystemExit(1)
