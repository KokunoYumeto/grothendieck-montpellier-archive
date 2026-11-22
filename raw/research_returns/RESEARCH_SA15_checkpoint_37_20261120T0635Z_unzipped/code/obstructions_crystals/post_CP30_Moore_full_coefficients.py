"""Exact universal determinant coefficients; one-zero Laurent relations only.

No ideal-radical or geometric parameter-surface assertion is made.
"""
from pathlib import Path
from itertools import product, permutations
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json,time,hashlib
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import numpy as np

start=time.perf_counter()
points=list(product(range(3),repeat=2));index={a:i for i,a in enumerate(points)}
plus=[[index[tuple((x+y)%3 for x,y in zip(a,b))] for b in points] for a in points]
minus=[[index[tuple((x-y)%3 for x,y in zip(a,b))] for b in points] for a in points]
entries=[[(1<<(36+4*minus[i][j]))+(1<<(4*plus[i][j])) for j in range(9)] for i in range(9)]
terms=set()
for perm in permutations(range(9)):
    term=sum(entries[i][j] for i,j in enumerate(perm))
    if term in terms:terms.remove(term)
    else:terms.add(term)
coefficients=defaultdict(list)
for term in terms:coefficients[term&((1<<36)-1)].append(term>>36)
for values in coefficients.values():values.sort()
lengths=Counter(map(len,coefficients.values()))
def decode(packed):return tuple((packed>>(4*i))&15 for i in range(9))

# Restriction c_0=0; cancel only an explicit common monomial.
restricted=[];binomial_vectors=[];binomial_records=[]
for xmon,values in sorted(coefficients.items()):
    remaining=[decode(v) for v in values if (v&15)==0]
    if not remaining:continue
    common=tuple(min(v[i] for v in remaining) for i in range(9))
    residual=[tuple(v[i]-common[i] for i in range(9)) for v in remaining]
    restricted.append({'x_monomial':hex(xmon),'common_c_monomial':common,'residual':residual})
    if len(residual)==2:
        difference=tuple(residual[0][i]-residual[1][i] for i in range(1,9))
        binomial_vectors.append(difference)
        binomial_records.append({'x_monomial':hex(xmon),'difference':difference,
                                  'common_c_monomial':common,'residual':residual})
unique=sorted(set(binomial_vectors))
matrix=sp.Matrix(unique)
snf=smith_normal_form(matrix,domain=ZZ)
diagonal=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]

# A separate finite diagnostic for parameters with >=2 zero coordinates
# in every one of the same 40 bases. No author output is overwritten.
dependency=Path(__file__).with_name('post_CP30_Moore_40_bases_probe.py')
source=dependency.read_text();assert source.count('vectors=[]\n')==1
env={};exec(compile(source.split('vectors=[]\n')[0],str(dependency),'exec'),env)
bases=env['bases'];mul=env['mul']
vectors=[]
for first in range(9):
    for tail in product(range(4),repeat=8-first):vectors.append((0,)*first+(1,)+tail)
remaining=np.array(vectors,dtype=np.uint8);two_zero_steps=[]
for name,basis in bases:
    values=np.zeros((len(remaining),9),dtype=np.uint8)
    for j in range(9):values ^= mul[remaining[:,j,None],basis[None,:,j]]
    remaining=remaining[np.count_nonzero(values==0,axis=1)>=2]
    two_zero_steps.append({'basis':name,'points':len(remaining)})
initial=json.loads(dependency.with_suffix('.output.json').read_text())
known=set()
for plane in initial['known_planes']:known.update(plane['projective_points'])
pack=lambda row:sum(int(v)<<(2*i) for i,v in enumerate(row))
outside=[tuple(map(int,v)) for v in remaining if pack(v) not in known]

out={'status':'EXACT_COEFFICIENT_ANALYSIS_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'permutations':362880,
     'universal_monomial_count':len(terms),'x_coefficient_count':len(coefficients),
     'coefficient_lengths':dict(sorted(lengths.items())),
     'coefficients':{hex(x):[hex(c) for c in cs] for x,cs in sorted(coefficients.items())},
     'one_zero_restricted_coefficient_count':len(restricted),
     'one_zero_binomial_count':len(binomial_records),
     'unique_binomial_relation_count':len(unique),
     'binomial_lattice_smith_diagonal':diagonal,
     'binomial_records':binomial_records,
     'two_zero_every_basis_F4_count':len(remaining),
     'two_zero_every_basis_outside_known_F4_count':len(outside),
     'two_zero_outside_examples':outside[:20],'two_zero_steps':two_zero_steps,
     'dependency_sha256':hashlib.sha256(dependency.read_bytes()).hexdigest(),
     'scope':'Universal determinant coefficients were collected exactly over F2. The binomial lattice only describes necessary Laurent relations on the c0=0 chart with the other eight c coordinates nonzero. Smith data alone are not asserted to classify the full singular locus. Finite F4 two-zero diagnostics are not a geometric theorem. No Cartier theta identification.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds','universal_monomial_count',
    'x_coefficient_count','coefficient_lengths','one_zero_binomial_count','unique_binomial_relation_count',
    'binomial_lattice_smith_diagonal','two_zero_every_basis_F4_count','two_zero_every_basis_outside_known_F4_count')}))
