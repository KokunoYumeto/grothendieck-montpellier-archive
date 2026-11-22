"""Exact graph certificate for the proposed common-boundary d=3 argument.

This checks only graph/cochain arithmetic for 729 partial normalizations.
It does not prove the separately required norm-family monodromy/shear lemma.
"""
from itertools import product
from pathlib import Path
import datetime,json,time
start=time.perf_counter()
def basis(vectors):
    out={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in out:v^=out[p]
            else:out[p]=v;break
    return out
def rank(vectors):return len(basis(vectors))
def reduce_mod(v,pivots):
    for p in sorted(pivots,reverse=True):
        if (v>>p)&1:v^=pivots[p]
    return v
loops=[1<<i for i in range(18)]
edge=lambda j,l:1<<(18+9*j+l)
cuts=[sum(edge(j,l) for l in range(9)) for j in range(6)]
cuts_basis=basis(cuts);assert len(cuts_basis)==6
graph_dimension=72-rank(cuts);assert graph_dimension==66
diagonals=set();all_annihilators=[];cases=0
first_diagonals=[]
for choices in product(range(3),repeat=6):
    new_edges=loops[:];annihilators=[]
    for j,r in enumerate(choices):
        chosen={3*r,3*r+1,3*r+2}
        new_edges.extend(edge(j,l) for l in range(9) if l not in chosen)
        annihilators.extend([edge(j,3*r)^edge(j,3*r+1),edge(j,3*r)^edge(j,3*r+2)])
    assert len(new_edges)==54
    assert rank(cuts+new_edges)-rank(cuts)==54
    assert rank(annihilators)==12
    assert all((a&c).bit_count()%2==0 for a in annihilators for c in cuts)
    assert all((a&e).bit_count()%2==0 for a in annihilators for e in new_edges)
    heart=[new_edges[0]^e for e in new_edges[1:]]
    assert rank(cuts+heart)-rank(cuts)==53
    diagonal=reduce_mod(sum(new_edges),cuts_basis)
    assert diagonal!=0 and diagonal not in diagonals
    diagonals.add(diagonal)
    if len(first_diagonals)<2:first_diagonals.append(diagonal)
    all_annihilators.extend(annihilators);cases+=1
annihilator_rank=rank(all_annihilators)
assert annihilator_rank==36
intersection=graph_dimension-annihilator_rank
assert intersection==30 and intersection<53
assert rank(cuts+first_diagonals)-rank(cuts)==2
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Exact graph arithmetic only; norm-family S54/GL26/shears remain separate mathematical hypotheses.',
        'partial_normalizations':cases,'ambient_edges':72,'vertex_coboundary_rank':6,
        'graph_dimension':graph_dimension,'each_partial_kernel_dimension':54,
        'each_sum_zero_heart_dimension':53,'joint_annihilator_rank':annihilator_rank,
        'all_partial_kernel_intersection_dimension':intersection,
        'distinct_nonzero_diagonal_classes':len(diagonals),'two_sample_diagonals_independent':True,
        'runtime_seconds':time.perf_counter()-start}
w=Path(__file__).resolve().parents[1]
(w/'outputs/mixed_degree_three_partial_normalizations.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
