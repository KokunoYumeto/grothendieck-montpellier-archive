"""Exact finite supplements to the universal odd-kernel graph proof.

No geometric monodromy is inferred from these cases.  Both actual
cochain-heart spans and intersections of all type-diagonal spaces
are computed modulo vertex-star coboundaries.
"""
from itertools import product
from pathlib import Path
import datetime, json, time

started = time.perf_counter()

def basis(rows):
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    return pivots

def rank(rows):
    return len(basis(rows))

def orthogonal(rows, n):
    pivots = basis(rows)
    result = []
    for free in range(n):
        if free in pivots:
            continue
        v = 1 << free
        for p in sorted(pivots):
            if (pivots[p] & v).bit_count() & 1:
                v ^= 1 << p
        assert all(not ((row & v).bit_count() & 1) for row in pivots.values())
        result.append(v)
    assert len(result) == n - len(pivots)
    return result

cases = []
for moduli, m in [((3,),1),((3,),2),((5,),1),((5,),2),
                   ((7,),1),((9,),1),((15,),1),((21,),1),((3,3),1)]:
    group = list(product(*(range(q) for q in moduli)))
    d = len(group)
    zero = tuple(0 for q in moduli)
    def add(x,y): return tuple((a+b)%q for a,b,q in zip(x,y,moduli))
    def neg(x): return tuple((-a)%q for a,q in zip(x,moduli))
    types = sorted({min(x,neg(x)) for x in group if x != zero})
    t = len(types)
    assert 2*t == d-1
    group_index = {x:i for i,x in enumerate(group)}
    loop = lambda h,l: 1 << (18*h+l)
    edge = lambda j,k,a: 1 << (18*t+3*d*j+3*group_index[k]+a)
    n = 18*t+3*d*m
    stars = [sum(edge(j,k,a) for k in group for a in range(3)) for j in range(m)]
    assert rank(stars) == m
    hearts = []
    diagonal_annihilators = []
    count = 0
    for selected in product(group,repeat=m):
        diagonals=[]
        full_kernel=[]
        for hi,h in enumerate(types):
            new_edges=[loop(hi,l) for l in range(18)]
            for j,r in enumerate(selected):
                for k in [add(r,h),add(r,neg(h))]:
                    new_edges += [edge(j,k,a) for a in range(3)]
            assert len(new_edges)==18+6*m
            assert rank(stars+new_edges)-m==18+6*m
            heart=[new_edges[0]^v for v in new_edges[1:]]
            assert rank(stars+heart)-m==17+6*m
            hearts.extend(heart)
            diagonals.append(sum(new_edges))
            full_kernel.extend(new_edges)
        assert rank(stars+full_kernel)-m == t*(18+6*m)
        assert rank(stars+diagonals)-m == t
        diagonal_annihilators.extend(orthogonal(stars+diagonals,n))
        count += 1
    graph_dimension=n-m
    heart_span=rank(stars+hearts)-m
    diagonal_intersection=n-rank(diagonal_annihilators)-m
    assert heart_span==graph_dimension
    assert diagonal_intersection==0

    # An actual pair in one type heart is excluded by selecting its triple.
    h=types[0]
    pair=edge(0,h,0)^edge(0,h,1)
    selected=[zero]*m
    selected[0]=h
    new_kernel=[]
    for hi,v in enumerate(types):
        new_kernel += [loop(hi,l) for l in range(18)]
        for j,r in enumerate(selected):
            for k in [add(r,v),add(r,neg(v))]:
                new_kernel += [edge(j,k,a) for a in range(3)]
    assert rank(stars+new_kernel+[pair]) == rank(stars+new_kernel)+1
    cases.append({'kernel_moduli':moduli,'d':d,'m':m,'partial_choices':count,
                  'graph_dimension':graph_dimension,'heart_span':heart_span,
                  'type_diagonal_common_intersection':diagonal_intersection,
                  'selected_triple_excludes_pair':True})

result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Finite exact graph arithmetic only; universal proof is in the TeX graph lemma, and no geometric inference is made from these cases.',
        'cases':cases,'runtime_seconds':time.perf_counter()-started}
dest=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_mixed_odd_common_graph_checks.json')
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
